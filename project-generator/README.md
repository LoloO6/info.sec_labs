# Project Template Generator

A terminal utility for creating structured project templates with proper architecture. Supports React, FastAPI, Spring Boot, and more.

## Features

*  **Quick Setup**: Generate complete project structures in seconds
*  **Best Practices**: Templates follow industry-standard architectures
*  **Multiple Frameworks**: React (TypeScript), FastAPI (Python), Spring Boot (Java)
*  **Organized Structure**: Proper separation of concerns (controllers, services, models, etc.)
*  **Customizable**: Easy to extend with new templates

## Installation

### Option 1: Install as Package

```bash
git clone https://github.com/LoloO6/info.sec_labs
cd project-generator
pip install -e .
project-gen --list
```

### Option 2: Run Directly

```bash
git clone https://github.com/LoloO6/info.sec_labs
cd project-generator
python -m project_generator --list
```

## Usage

### List Available Templates

```bash
project-gen --list
```

```bash
python -m project_generator --list
```

### Create a New Project

```bash
project-gen --type react --name my-react-app --dest ./projects
project-gen --type fastapi --name my-api --dest .
project-gen --type spring --name my-spring-app --dest ~/workspace
```

### Command Line Options

* `--list, -l`: List all templates

### Create project template

* project-gen react my-react-app
* project-gen fastapi my-api
* project-gen spring my-spring-app


## Available Templates

### React (JavaScript)

my-react-app/
├── public/
│   └── index.html
└── src/
    ├── components/
    ├── App.js
    └── index.js

### FastAPI (Python)

my-api/
├── app/
│   ├── api/
│   │   └── routers.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   └── __init__.py
├── main.py
├── requirements.txt
└── README.md

### Spring Boot (Java)

my-spring-app/
├── src/main/java/com/example/my-spring-app/
│   ├── MySpringAppApplication.java
│   ├── MyController.java
│   └── MyService.java
├── src/main/resources/
│   └── application.properties
├── pom.xml
└── README.md

## Placeholders

* `{{PROJECT_NAME}}`
* `{{PROJECT_NAME_UPPER}}`
* `{{PROJECT_NAME_LOWER}}`
* `{{PROJECT_NAME_CAPITALIZED}}`



 