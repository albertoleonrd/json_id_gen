"""
Command-line interface for the random ID generator.

This module defines the command-line interface for the application.
"""
import argparse
import sys
from typing import List, Optional


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.

    Args:
        args: Command-line arguments (defaults to sys.argv[1:] if None)

    Returns:
        An argparse.Namespace containing the parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Generate random IDs for records in a JSON file.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '--i', 
        dest='input_file',
        required=True,
        help='Path to the input JSON file'
    )
    
    parser.add_argument(
        '--o', 
        dest='output_file',
        required=True,
        help='Path to the output JSON file'
    )
    
    parser.add_argument(
        '--id-field',
        default='id',
        help='Name of the field where the ID will be written'
    )
    
    parser.add_argument(
        '--id-length',
        type=int,
        default=6,
        help='Length of the random ID to generate'
    )
    
    parser.add_argument(
        '--id-method',
        default='random_unique',
        choices=['random_unique'],
        help='Method used to generate the ID'
    )
    
    parser.add_argument(
        '--charset',
        help='Characters allowed for the ID (e.g., "ABCDEF0123456789")'
    )
    
    parser.add_argument(
        '--retry-limit',
        type=int,
        default=100,
        help='Maximum number of attempts to avoid ID collisions'
    )
    
    parser.add_argument(
        '--upper',
        action='store_true',
        help='Force uppercase for the generated IDs'
    )
    
    parser.add_argument(
        '--prefix',
        default='',
        help='Optional prefix for the IDs'
    )

    return parser.parse_args(args)