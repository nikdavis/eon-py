# EON Python Bindings

Python bindings for the [EON (Extensible Object Notation)](https://github.com/emilk/eon) format - a human-friendly configuration format that's a superset of JSON.

## Installation

```bash
pip install eon
```

## Usage

```python
from eon import loads, dumps, load, dump

# Parse EON string
data = loads("""
{
    name: "Alice"
    age: 30
    skills: ["Python", "Rust", "JavaScript"]
}
""")
print(data)  # {'name': 'Alice', 'age': 30, 'skills': ['Python', 'Rust', 'JavaScript']}

# Serialize to EON
eon_str = dumps({"name": "Bob", "age": 25})
print(eon_str)  # name: "Bob"\nage: 25

# Work with files
with open("config.eon", "r") as f:
    config = load(f)

with open("output.eon", "w") as f:
    dump(data, f)
```

## Features

- ✅ Full support for all EON types (null, bool, numbers, strings, lists, maps, variants)
- ✅ Clean Python API matching `json` module conventions
- ✅ Fast Rust implementation
- ✅ Cross-platform wheels for Windows, macOS, and Linux (x86 and ARM)

## Development

### Building from source

```bash
# Install maturin
pip install maturin

# Build and install locally
maturin develop --release

# Run tests
python test_eon.py
```

### Project Structure

```
eon-py/
├── src/
│   └── eon/
│       ├── __init__.py    # Python API
│       └── lib.rs         # Rust implementation
├── Cargo.toml             # Rust dependencies
├── pyproject.toml         # Python package config
└── test_eon.py            # Test suite
```

## License

This project provides Python bindings for the EON format created by Emil Ernerfeldt.