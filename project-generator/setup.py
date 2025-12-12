"""Setup configuration for project-generator package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="project-generator",
    version="1.0.0",
    author="Leila",
    author_email="ml12365@auca.kg",
    description="A terminal utility for creating project templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LoloO6/info.sec_labs",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "project-gen=project_generator.__main__:main",
        ],
    },
)