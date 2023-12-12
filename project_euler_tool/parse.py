import re
from dataclasses import dataclass
from typing import List, Optional, Tuple

from bs4 import BeautifulSoup

from .db import Problem, Solution
from .web import download_problem, progress


def parse_problem(problem_id: int, **kwargs) -> Tuple[Problem, Optional[Solution]]:
    """Parse the statement of a problem."""
    html = download_problem(problem_id, **kwargs)
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h2").text
    statement = soup.find("div", class_="problem_content").text

    info = soup.find("div", id="problem_icons").find_all("span")[2].text

    difficulty = re.search(r"Difficulty rating: (\d+)%", info)
    if difficulty is not None:
        difficulty = int(difficulty.group(1))

    solvers = re.search(r"Solved by (\d+);", info)
    if solvers is not None:
        solvers = int(solvers.group(1))

    problem = Problem(
        problem_id=problem_id,
        title=title,
        content=statement,
        solvers=solvers,
        difficulty=difficulty,
    )

    solution = soup.find("div", class_="data_entry").find("span")
    if solution is not None:
        solution = Solution(problem=problem, solution=solution.text)

    return problem, solution


@dataclass
class ProblemMeta:
    problem_id: int
    title: str
    difficulty: int
    solvers: int
    solved: bool


def parse_progress() -> List[ProblemMeta]:
    html = progress()
    soup = BeautifulSoup(html, "html.parser")

    problems_section = soup.find("div", id="problems_solved_section")

    problems = []
    for prob in problems_section.find_all("td"):
        divs = prob.find_all("div")
        problem_id = int(re.match(r"Problem (\d+)", divs[0].text).group(1))
        solvers = int(re.match(r"Solved by (\d+)", divs[1].text).group(1))
        difficulty = re.match(r"Difficulty rating: (\d+)%", divs[2].text)
        difficulty = int(difficulty.group(1)) if difficulty is not None else 0
        title = divs[-1].text.strip('"')
        solved = any(div.text.startswith("Completed") for div in divs)

        problem = ProblemMeta(problem_id, title, difficulty, solvers, solved)
        problems.append(problem)

    return problems
