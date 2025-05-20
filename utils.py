"""
Utility functions for the random ID generator.

This module provides helper functions for file operations and error handling.
"""
import json
import os
from typing import Dict, List, Any


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Read JSON data from a file.

    Args:
        file_path: Path to the JSON file

    Returns:
        List of dictionary records from the JSON file

    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file is not valid JSON
        ValueError: If the JSON data is not a list of dictionaries
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    # Ensure the data is a list of dictionaries
    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of records")
    
    # Check if all items are dictionaries
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All items in the input JSON must be dictionaries")
        
    return data


def write_json_file(file_path: str, data: List[Dict[str, Any]]) -> None:
    """
    Write JSON data to a file.

    Args:
        file_path: Path where to write the JSON file
        data: List of dictionary records to write

    Raises:
        PermissionError: If the file cannot be written due to permissions
    """
    # Create directory if it doesn't exist
    output_dir = os.path.dirname(file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)