from collections import defaultdict

from dotenv import load_dotenv
from tabulate import tabulate

from .parse import parse_progress


def main():
    load_dotenv()
    problems = parse_progress()

    n_cat = 3
    n_diff_cat = 2

    unsolved_problems = [p for p in problems if not p.solved]

    easiest = sorted(unsolved_problems, key=lambda p: p.difficulty)[:n_cat]
    most_authors = sorted(unsolved_problems, key=lambda p: p.authors)[-n_cat:]
    recent = sorted(unsolved_problems, key=lambda p: p.problem_id)[-n_cat:]
    oldest = sorted(unsolved_problems, key=lambda p: p.problem_id)[:n_cat]
    diff_cat = []
    diff_freq = defaultdict(int)
    by_author = sorted(unsolved_problems, key=lambda p: -p.authors)
    for prob in by_author:
        if diff_freq[prob.difficulty] < n_diff_cat:
            diff_cat.append(prob)
            diff_freq[prob.difficulty] += 1

    selected_problems = dict()
    for prob in easiest + most_authors + recent + oldest + diff_cat:
        selected_problems[prob.problem_id] = prob

    selected_problems = sorted(
        selected_problems.values(), key=lambda p: (p.difficulty, -p.authors)
    )

    print(tabulate(selected_problems, headers="keys"))
