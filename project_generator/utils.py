from templates import TEMPLATES

def print_help():
    print("Usage:")
    print(" python -m project_generator <template> <project_name> <destination>")
    print("Available templates:", ", ".join(TEMPLATES.keys()))
