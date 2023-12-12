import re
import sys
from collections import defaultdict
from functools import partial

from dotenv import load_dotenv
from tabulate import tabulate

from .parse import parse_progress


def default(problems):
    n_cat = 3
    n_diff_cat = 2

    unsolved_problems = [p for p in problems if not p.solved]

    easiest = sorted(unsolved_problems, key=lambda p: p.difficulty)[:n_cat]
    most_solvers = sorted(unsolved_problems, key=lambda p: p.solvers)[-n_cat:]
    recent = sorted(unsolved_problems, key=lambda p: p.problem_id)[-n_cat:]
    oldest = sorted(unsolved_problems, key=lambda p: p.problem_id)[:n_cat]
    diff_cat = []
    diff_freq = defaultdict(int)
    by_solver = sorted(unsolved_problems, key=lambda p: -p.solvers)
    for prob in by_solver:
        if diff_freq[prob.difficulty] < n_diff_cat:
            diff_cat.append(prob)
            diff_freq[prob.difficulty] += 1

    selected_problems = dict()
    for prob in easiest + most_solvers + recent + oldest + diff_cat:
        selected_problems[prob.problem_id] = prob

    selected_problems = sorted(
        selected_problems.values(), key=lambda p: (p.difficulty, -p.solvers)
    )

    return selected_problems


def get(p, id):
    if id == "pid":
        return p.problem_id
    elif id.startswith("diff"):
        return p.difficulty
    elif id.startswith("solver"):
        return p.solvers
    else:
        return int(id)


AVAILABLE_OPS = ["<", "<=", ">", ">=", "=="]
OPS = "|".join(AVAILABLE_OPS)


def compare(left, op, right):
    assert isinstance(left, int)
    assert isinstance(right, int)
    assert op in AVAILABLE_OPS
    return eval(f"{left} {op} {right}")


FIELDS = "pid|diff[a-z]*|solvers?"


def parse_filter(f):
    solved = re.match("^(not )?solved$", f)
    if solved:
        want_solved = solved.group(1) is None
        fn = lambda p: p.solved == want_solved
        return partial(filter, fn)

    comparison = re.match(f"^({FIELDS}|[0-9]+) ({OPS}) ({FIELDS}|[0-9]+)$", f)
    if comparison:
        left = comparison.group(1)
        op = comparison.group(2)
        right = comparison.group(3)
        fn = lambda p: compare(get(p, left), op, get(p, right))
        return partial(filter, fn)

    sort = re.match(f"^sort ({FIELDS})( asc| desc)?$", f)
    if sort:
        reverse = sort.group(2) == " desc"
        fn = lambda ps: sorted(ps, key=lambda p: get(p, sort.group(1)), reverse=reverse)
        return fn

    return lambda x: x


def main():
    load_dotenv()
    problems = parse_progress()

    if len(sys.argv) == 2:
        for f in sys.argv[1].split("|"):
            f = f.strip(" ").lower()
            fn = parse_filter(f)
            problems = fn(problems)
        selected_problems = problems
    else:
        selected_problems = default(problems)

    print(tabulate(selected_problems, headers="keys"))
