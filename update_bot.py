from pathlib import Path

from src.projects_section import generate_latest_projects_section
from src.services import update_readme_section

BASE_DIR = Path(__file__).resolve().parent
README_PATH = Path(BASE_DIR, "README.md")
PROJECTS_SECTION_NAME = "LATEST-PROJECTS-LIST"
PROJECTS_ENDPOINT = "https://www.ruveloper.dev/projects/"
PROJECTS_API_ENDPOINT = "https://www.ruveloper.dev/api/cms/projects/?language=en&count=3"

if __name__ == "__main__":
    # * ---- UPDATE LATEST PROJECTS SECTION ----
    projects_section_text = generate_latest_projects_section(
        endpoint=PROJECTS_ENDPOINT,
        api_endpoint=PROJECTS_API_ENDPOINT
    )
    update_readme_section(
        readme_path=README_PATH,
        section_name=PROJECTS_SECTION_NAME,
        section_text=projects_section_text
    )
