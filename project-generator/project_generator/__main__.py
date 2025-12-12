"""CLI entry point for Project Template Generator."""

import argparse
from pathlib import Path

from .generator import ProjectGenerator
from .templates import TEMPLATES
from .utils import validate_project_name, sanitize_project_name


def main():
    parser = argparse.ArgumentParser(
        description="Project Template Generator - Create new project structure."
    )


    parser.add_argument(
        "template",
        type=str,
        help=f"Template name. Available: {', '.join(TEMPLATES.keys())}",
    )

    parser.add_argument(
        "project_name",
        type=str,
        help="Name of the project to generate.",
    )

    parser.add_argument(
        "destination",
        type=str,
        help="Destination directory where the project will be created.",
    )

    args = parser.parse_args()

    # Validate project name
    if not validate_project_name(args.project_name):
        print("❌ Invalid project name. Remove special characters.")
        return

    project_name = sanitize_project_name(args.project_name)

    # Validate template
    if args.template not in TEMPLATES:
        print(f"❌ Unknown template '{args.template}'. Available: {list(TEMPLATES.keys())}")
        return

    dest_path = Path(args.destination)

    generator = ProjectGenerator(
        template_name=args.template,
        project_name=project_name,
        destination=dest_path,
    )

    generator.generate()
    print("\n🎉 Project created successfully!")


if __name__ == "__main__":
    main()