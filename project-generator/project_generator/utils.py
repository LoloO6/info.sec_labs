"""Utility functions for project generation."""

import os
from pathlib import Path
from typing import Dict


def create_directory(path: Path) -> None:
    """
    Create a directory if it doesn't exist.
    
    Args:
        path: Path to the directory to create
    """
    path.mkdir(parents=True, exist_ok=True)
    print(f"  📁 Created directory: {path}")


def write_file(path: Path, content: str) -> None:
    """
    Write content to a file.
    
    Args:
        path: Path to the file
        content: Content to write
    """
    # Ensure parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the file
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  📄 Created file: {path}")


def replace_placeholders(text: str, placeholders: Dict[str, str]) -> str:
    """
    Replace placeholders in text with actual values.
    
    Args:
        text: Text containing placeholders
        placeholders: Dictionary of placeholder -> value mappings
        
    Returns:
        Text with placeholders replaced
    """
    for placeholder, value in placeholders.items():
        text = text.replace(placeholder, value)
    return text


def sanitize_project_name(name: str) -> str:
    """
    Sanitize project name to be valid for file systems and package names.
    
    Args:
        name: Original project name
        
    Returns:
        Sanitized project name
    """
    # Replace spaces and special characters with hyphens
    sanitized = name.strip().lower()
    sanitized = ''.join(c if c.isalnum() or c in '-_' else '-' for c in sanitized)
    
    # Remove consecutive hyphens
    while '--' in sanitized:
        sanitized = sanitized.replace('--', '-')
    
    # Remove leading/trailing hyphens
    sanitized = sanitized.strip('-')
    
    return sanitized


def validate_project_name(name: str) -> bool:
    """
    Validate that a project name is acceptable.
    
    Args:
        name: Project name to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not name:
        return False
    
    # Check for invalid characters
    if any(c in name for c in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']):
        return False
    
    return True