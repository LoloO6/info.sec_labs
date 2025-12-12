""" Core project generation logic."""

from pathlib import Path
from typing import Dict, Any, List

from .utils import create_directory, write_file, replace_placeholders
from .templates import TEMPLATES


class ProjectGenerator:
    """
    Main class responsible for generating a new project.
    """

    def __init__(self, template_name: str, project_name: str, destination: Path):
        self.template_name = template_name
        self.project_name = project_name
        self.destination = destination
        self.template = TEMPLATES[template_name]

    def generate(self) -> None:
        """
        Generate the project from template.
        """
        print(f" Generating project '{self.project_name}' using template '{self.template_name}'")
        base_path = self.destination / self.project_name

        # Create root directory
        create_directory(base_path)

        # Create directories
        for folder in self.template.get("folders", []):
            create_directory(base_path / folder)

        # Create files
        for file_path, content in self.template.get("files", {}).items():
            final_path = base_path / file_path

            placeholders = {
                "{{PROJECT_NAME}}": self.project_name,
            }
            content = replace_placeholders(content, placeholders)

            write_file(final_path, content)
