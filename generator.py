"""
Random ID generator for JSON records.

This module provides functionality to generate random IDs and assign them to JSON records.
"""
import random
import string
from typing import Dict, List, Any, Set


class IDGenerator:
    """Class that handles the generation of unique random IDs for JSON records."""

    def __init__(
        self,
        id_field: str = "id",
        id_length: int = 6,
        id_method: str = "random_unique",
        charset: str = None,
        retry_limit: int = 100,
        uppercase: bool = False,
        prefix: str = "",
    ):
        """
        Initialize the ID Generator with the given parameters.

        Args:
            id_field: Name of the field to store the ID (default: "id")
            id_length: Length of the ID to generate (default: 6)
            id_method: Method to use for ID generation (default: "random_unique")
            charset: Characters to use for ID generation (default: alphanumeric)
            retry_limit: Maximum number of attempts to generate a unique ID (default: 100)
            uppercase: Whether to convert IDs to uppercase (default: False)
            prefix: Optional prefix for IDs (default: "")
        """
        self.id_field = id_field
        self.id_length = id_length
        self.id_method = id_method
        
        # Set default charset if none provided
        if charset is None:
            self.charset = string.ascii_letters + string.digits
        else:
            self.charset = charset
            
        self.retry_limit = retry_limit
        self.uppercase = uppercase
        self.prefix = prefix
        self.used_ids: Set[str] = set()

    def generate_id(self) -> str:
        """
        Generate a unique random ID according to the configured parameters.

        Returns:
            A unique random ID string

        Raises:
            ValueError: If a unique ID cannot be generated within the retry limit
        """
        if self.id_method == "random_unique":
            return self._generate_random_unique_id()
        else:
            raise ValueError(f"Unknown ID method: {self.id_method}")

    def _generate_random_unique_id(self) -> str:
        """
        Generate a unique random ID using the random_unique method.

        Returns:
            A unique random ID string

        Raises:
            ValueError: If a unique ID cannot be generated within the retry limit
        """
        for attempt in range(self.retry_limit):
            # Generate a random ID
            random_id = ''.join(random.choice(self.charset) for _ in range(self.id_length))
            
            # Apply uppercase if configured
            if self.uppercase:
                random_id = random_id.upper()
                
            # Add prefix if configured
            full_id = f"{self.prefix}{random_id}"
            
            # Check if the ID is unique
            if full_id not in self.used_ids:
                self.used_ids.add(full_id)
                return full_id
                
        # If we've reached this point, we couldn't generate a unique ID
        raise ValueError(
            f"Failed to generate a unique ID after {self.retry_limit} attempts. "
            f"Consider increasing the ID length or using a different charset."
        )

    def process_records(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process a list of records, adding a unique ID to each.

        Args:
            records: List of dictionary records to process

        Returns:
            The processed records with IDs added

        Raises:
            ValueError: If unique IDs cannot be generated for all records
        """
        processed_records = []
        for record in records:
            # Create a new dict with the ID field first for better readability
            new_record = {self.id_field: self.generate_id()}
            # Add the rest of the fields
            new_record.update(record)
            processed_records.append(new_record)
            
        return processed_records