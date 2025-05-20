"""
Unit tests for utility functions.

This module contains tests for the utility functions that handle JSON file operations.
"""
import os
import unittest
import tempfile
import json
from utils import read_json_file, write_json_file


class TestUtils(unittest.TestCase):
    """Tests for utility functions."""
    
    def test_read_json_file(self):
        """Test reading a JSON file."""
        # Create a temporary JSON file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
            json.dump([{"name": "John"}, {"name": "Jane"}], temp_file)
            temp_file_path = temp_file.name
        
        try:
            # Read the file
            data = read_json_file(temp_file_path)
            
            # Verify the data
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["name"], "John")
            self.assertEqual(data[1]["name"], "Jane")
        finally:
            # Clean up
            os.unlink(temp_file_path)
    
    def test_read_nonexistent_file(self):
        """Test reading a file that doesn't exist."""
        with self.assertRaises(FileNotFoundError):
            read_json_file("nonexistent_file.json")
    
    def test_read_invalid_json(self):
        """Test reading an invalid JSON file."""
        # Create a temporary file with invalid JSON
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
            temp_file.write("This is not valid JSON")
            temp_file_path = temp_file.name
        
        try:
            # Try to read the file
            with self.assertRaises(json.JSONDecodeError):
                read_json_file(temp_file_path)
        finally:
            # Clean up
            os.unlink(temp_file_path)
    
    def test_write_json_file(self):
        """Test writing a JSON file."""
        # Create a temporary directory and file path
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, "output.json")
        
        data = [{"id": "123", "name": "John"}, {"id": "456", "name": "Jane"}]
        
        try:
            # Write the data
            write_json_file(temp_file_path, data)
            
            # Read it back and verify
            with open(temp_file_path, 'r', encoding='utf-8') as file:
                read_data = json.load(file)
            
            self.assertEqual(read_data, data)
        finally:
            # Clean up
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
            os.rmdir(temp_dir)


if __name__ == "__main__":
    unittest.main()