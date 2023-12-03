import pathlib
import os
import requests

session_id = os.getenv("AOC_SESSION_ID")


def __get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    resp = requests.get(url, cookies=dict(session=session_id))
    resp.raise_for_status()
    return resp.text


def save_input(year, day):
    path_string = f"{year}/{day:02d}"
    data = __get_input(year, day)
    pathlib.Path(f"{path_string}").mkdir(parents=True, exist_ok=True)
    with open(f"{path_string}/input.txt", "w") as f:
        f.write(data)
