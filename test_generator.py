"""
Unit tests for the ID generator.

This module contains tests for the ID generator functionality.
"""
import unittest
from generator import IDGenerator


class TestIDGenerator(unittest.TestCase):
    """Tests for the IDGenerator class."""
    
    def test_id_length(self):
        """Test that generated IDs have the correct length."""
        # Test with default length
        generator = IDGenerator()
        id_val = generator.generate_id()
        self.assertEqual(len(id_val), 6)
        
        # Test with custom length
        generator = IDGenerator(id_length=10)
        id_val = generator.generate_id()
        self.assertEqual(len(id_val), 10)
        
        # Test with prefix
        generator = IDGenerator(id_length=5, prefix="PRE-")
        id_val = generator.generate_id()
        self.assertEqual(len(id_val), 9)  # 5 + 4 (prefix)
        self.assertTrue(id_val.startswith("PRE-"))
    
    def test_id_uniqueness(self):
        """Test that generated IDs are unique."""
        generator = IDGenerator(id_length=4, charset="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        ids = set()
        
        # Generate 100 IDs and check they're all unique
        for _ in range(100):
            id_val = generator.generate_id()
            self.assertNotIn(id_val, ids)
            ids.add(id_val)
    
    def test_id_charset(self):
        """Test that IDs only contain characters from the specified charset."""
        charset = "ABCDEF0123456789"
        generator = IDGenerator(charset=charset)
        
        # Generate 50 IDs and check they only contain characters from the charset
        for _ in range(50):
            id_val = generator.generate_id()
            for char in id_val:
                self.assertIn(char, charset)
    
    def test_uppercase(self):
        """Test that uppercase option works correctly."""
        # Test with lowercase charset and uppercase=True
        generator = IDGenerator(charset="abcdef", uppercase=True)
        id_val = generator.generate_id()
        self.assertEqual(id_val, id_val.upper())
    
    def test_process_records(self):
        """Test processing a list of records."""
        records = [
            {"name": "John", "age": 30},
            {"name": "Jane", "age": 25},
            {"name": "Bob", "age": 40}
        ]
        
        generator = IDGenerator(id_field="user_id")
        processed = generator.process_records(records)
        
        # Check that we have the same number of records
        self.assertEqual(len(processed), len(records))
        
        # Check that each record has an ID field
        for record in processed:
            self.assertIn("user_id", record)
            
        # Check that IDs are unique
        ids = set(record["user_id"] for record in processed)
        self.assertEqual(len(ids), len(records))


if __name__ == "__main__":
    unittest.main()