from pony.orm import *
from pathlib import Path

set_sql_debug(True)
db = Database()


class Problem(db.Entity):
    problem_id = PrimaryKey(int)
    title = Required(str)
    content = Required(str)
    solvers = Optional(int)
    difficulty = Optional(int)
    solution = Optional(lambda: Solution)
    thread_comment = Set(lambda: ThreadComment)


class Solution(db.Entity):
    problem = Required(Problem)
    solution = Required(str)


class ThreadComment(db.Entity):
    comment_id = PrimaryKey(int, auto=True)
    problem = Required(Problem)
    content = Required(str)
    author = Optional(str)
    likes = Required(int)


def init():
    db.bind(
        provider="sqlite", filename=str(Path("pe.sqlite").absolute()), create_db=True
    )
    db.generate_mapping(create_tables=True)
