from pathlib import Path
from templates import TEMPLATES

def create_project(template_name: str, project_name: str, destination: str):
    template_name = template_name.lower()
    if template_name not in TEMPLATES:
        print(f"Template '{template_name}' not found.")
        return

    project_path = Path(destination) / project_name
    print(f"[DEBUG] Destination path: {project_path}")
    print(f"Creating project at: {project_path}")

    if project_path.exists():
        print(f"Error: '{project_path}' already exists.")
        return

    project_path.mkdir(parents=True)
    template = TEMPLATES[template_name]

    for path in template["structure"]:
        full_path = project_path / path
        if path.endswith("/"):
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"Created folder: {full_path}")
        else:
            full_path.parent.mkdir(parents=True, exist_ok=True)
            content = template["files_content"].get(path, "")
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created file: {full_path}")

    print(f"Project '{project_name}' created successfully!")
