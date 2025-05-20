#!/usr/bin/env python3
"""
Main entry point for the random ID generator.

This script reads a JSON file, adds unique random IDs to each record,
and saves the result to a new JSON file.
"""
import sys
from generator import IDGenerator
from cli import parse_args
from utils import read_json_file, write_json_file


def main():
    """Run the random ID generator application."""
    try:
        # Parse command-line arguments
        args = parse_args()
        
        # Read input JSON file
        print(f"Reading input file: {args.input_file}")
        records = read_json_file(args.input_file)
        
        # Initialize the ID generator
        id_generator = IDGenerator(
            id_field=args.id_field,
            id_length=args.id_length,
            id_method=args.id_method,
            charset=args.charset,
            retry_limit=args.retry_limit,
            uppercase=args.upper,
            prefix=args.prefix
        )
        
        # Process records
        print(f"Processing {len(records)} records...")
        processed_records = id_generator.process_records(records)
        
        # Write output JSON file
        print(f"Writing output to: {args.output_file}")
        write_json_file(args.output_file, processed_records)
        
        print("✅ Done! IDs have been successfully generated.")
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())