import sys
import os

# Добавляем текущую директорию в путь Python
sys.path.insert(0, os.path.dirname(__file__))

try:
    from .generator import create_project
    from .utils import print_help
except ImportError:
    from generator import create_project
    from utils import print_help

print("[DEBUG] __main__.py is running")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_help()
    else:
        _, template_name, project_name, destination = sys.argv
        create_project(template_name, project_name, destination)
