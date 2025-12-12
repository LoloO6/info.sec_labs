"""Template definitions for project generator."""

TEMPLATES = {
    "react": {
        "folders": [
            "src",
            "src/components",
            "public",
        ],
        "files": {
            "package.json": """{
  "name": "{{PROJECT_NAME}}",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}""",

            "src/index.js": """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
""",

            "src/App.js": """export default function App() {
  return (
    <div>
      <h1>Hello from {{PROJECT_NAME}}!</h1>
    </div>
  );
}
""",

            "public/index.html": """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>{{PROJECT_NAME}}</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>""",
        },
    },

    "fastapi": {
        "folders": [
            "app",
            "app/api",
            "app/core",
        ],
        "files": {
            "main.py": """from fastapi import FastAPI
from app.api.routers import router

app = FastAPI(title="{{PROJECT_NAME}} API")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to {{PROJECT_NAME}}!"}
""",

            "app/__init__.py": "",
            "app/api/routers.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}
""",
            "app/core/config.py": "# Configuration settings",
            "app/core/database.py": "# Database connection and models",
            "requirements.txt": "fastapi\nuvicorn\n",
            "README.md": "# {{PROJECT_NAME}} FastAPI Project",
        },
    },

    "spring": {
        "folders": [
            "src/main/java/com/example/{{PROJECT_NAME}}",
            "src/main/resources",
        ],
        "files": {
            "pom.xml": """<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>{{PROJECT_NAME}}</artifactId>
  <version>1.0-SNAPSHOT</version>
</project>""",

            "src/main/java/com/example/{{PROJECT_NAME}}/{{PROJECT_NAME.capitalize()}}Application.java": """package com.example.{{PROJECT_NAME}};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {{PROJECT_NAME.capitalize()}}Application {
    public static void main(String[] args) {
        SpringApplication.run({{PROJECT_NAME.capitalize()}}Application.class, args);
    }
}
""",
            "src/main/java/com/example/{{PROJECT_NAME}}/MyController.java": """package com.example.{{PROJECT_NAME}};

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyController {
    @GetMapping("/")
    public String home() {
        return "Hello from {{PROJECT_NAME}}!";
    }
}
""",
            "src/main/java/com/example/{{PROJECT_NAME}}/MyService.java": """package com.example.{{PROJECT_NAME}};

import org.springframework.stereotype.Service;

@Service
public class MyService {
    // Business logic here
}
""",
            "src/main/resources/application.properties": "# Spring Boot configuration",
            "README.md": "# {{PROJECT_NAME}} Spring Boot Project",
        },
    },
}