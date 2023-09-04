"""
Download and parse Project Euler web.
"""

import os

import requests

from .utils import cache_on_disk


@cache_on_disk
def download_problem(problem_id: int) -> str:
    """Download the statement of a problem."""
    url = f"https://projecteuler.net/problem={problem_id}"
    PHPSESSID = os.environ["PROJECT_EULER_SESSION"]
    cookies = {"PHPSESSID": PHPSESSID}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    return response.text


def progress():
    url = "https://projecteuler.net/progress"
    PHPSESSID = os.environ["PROJECT_EULER_SESSION"]
    cookies = {"PHPSESSID": PHPSESSID}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    return response.text
