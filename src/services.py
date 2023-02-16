import json
import re
from pathlib import Path
from urllib import request


def get(url: str) -> dict:
    """
    Make a GET request to the API REST ENDPOINT and return the deserialized response.
    :param str url: url to the API REST endpoint
    :return: dict response
    """
    with request.urlopen(url, timeout=10) as response:
        body: bytes = response.read()
    return json.loads(body)


def update_readme_section(readme_path: Path, section_name: str, section_text: str):
    """
    Update (Replace) the text in the marked section of the README file.
    :param str readme_path: absolute path of the README file
    :param str section_name: name of the section to find
    :param str section_text: text of the section to replace with
    :return: None
    """
    file_data = ""

    # * Read file content
    with open(readme_path, "r", encoding="utf-8") as f:
        file_data = f.read()

    # * Find the section to replace
    start = f"<!-- {section_name}:START -->"
    end = f"<!-- {section_name}:END -->"
    pattern = fr"(?={re.escape(start)})(.*)(?<={re.escape(end)})"
    match = re.search(pattern, file_data, re.DOTALL)
    if match:
        selected_text = match.group()
        file_data = file_data.replace(selected_text, start + section_text + end)

    # * Write new content to file
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(file_data)
