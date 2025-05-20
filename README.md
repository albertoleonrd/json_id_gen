# Random ID Generator

A command-line tool for adding unique random IDs to JSON records. This tool reads a JSON file containing an array of records, generates a unique random ID for each record, and saves the result to a new JSON file.

## Features

- Generate unique random IDs for JSON records
- Customizable ID field name, length, and characters
- Prefix support for generated IDs
- Configurable retry limit to ensure uniqueness
- Option to force uppercase IDs
- Simple command-line interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/random_id_generator.git
cd random_id_generator
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the tool using the `main.py` script:

```bash
python main.py --i input.json --o output.json
```

### Example

Input file `input.json`:
```json
[
  {"apellido": "martinez", "nombre": "jose"},
  {"apellido": "rodriguez", "nombre": "pedro"}
]
```

Command:
```bash
python main.py --i input.json --o output.json --id-length 6 --charset "ABCDEF0123456789" --upper
```

Output file `output.json`:
```json
[
  {"id": "B4F3E2", "apellido": "martinez", "nombre": "jose"},
  {"id": "1D5A9C", "apellido": "rodriguez", "nombre": "pedro"}
]
```

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--i` | Path to input JSON file | *Required* |
| `--o` | Path to output JSON file | *Required* |
| `--id-field` | Name of the field where the ID will be written | `id` |
| `--id-length` | Length of the random ID to generate | `6` |
| `--id-method` | Method used to generate the ID | `random_unique` |
| `--charset` | Characters allowed for the ID | Alphanumeric (A-Z, a-z, 0-9) |
| `--retry-limit` | Maximum number of attempts to avoid ID collisions | `100` |
| `--upper` | Force uppercase for the generated IDs | `False` |
| `--prefix` | Optional prefix for the IDs | Empty string |

## Error Handling

The tool includes error handling for various scenarios:
- Invalid input file format
- File not found
- Permission errors
- Duplicate ID generation exceeding retry limit

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

> This project was developed with the assistance of artificial intelligence.