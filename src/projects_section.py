from datetime import datetime

from src.services import get


def get_project_link(project, endpoint):
    if project.get("link"):
        return project["link"]
    if project.get("github_url"):
        return project["github_url"]
    if project.get("activate_details") and project.get("slug"):
        return endpoint + project.get("slug")
    return endpoint


def get_project_technologies(project: dict) -> list[tuple]:
    project_technologies = []
    if project.get("technology_set"):
        for technology_link in project["technology_set"]:
            data = get(technology_link)
            project_technologies.append((data.get("name"), data.get("logo")))
    return project_technologies


def generate_latest_projects_section(endpoint: str, api_endpoint: str) -> str:
    # * Get projects data from source
    projects: list[dict] = get(api_endpoint).get("results", [])
    # * Generate and return the section text
    projects_text: str = '\n## Latest Projects:\n<table style="width:100%">\n<tr>\n'
    for project in projects:
        project_name = project.get("title")
        project_image_url = project.get("cover_image")
        project_link = get_project_link(project, endpoint)
        project_technologies = get_project_technologies(project)
        project_technologies_text = [f'<img height="20px" src="{tech[1]}" alt="{tech[0]}">'
                                     for tech in project_technologies]
        projects_text += f'<td>' \
                         f'\n <a href="{project_link}">' \
                         f'\n <img src="{project_image_url}" alt="Project {project_name}">' \
                         f'\n <p align="center">{" ".join(project_technologies_text)}</p>' \
                         f'\n </a>\n</td>\n'
    projects_text += '</tr>\n</table>\n'
    projects_text += f'<p align="right"><sub>[Bot] Projects updated on {datetime.now().strftime("%m-%d-%Y")}</sub></p>\n'
    return projects_text
