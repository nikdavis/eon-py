#!/usr/bin/env python3
"""Test script for eon Python bindings"""

import eon
import json

def test_loads_basic():
    """Test parsing basic EON strings"""
    print("Testing basic loads...")
    
    # Test null
    result = eon.loads("null")
    assert result is None, f"Expected None, got {result}"
    print("✓ Null parsing works")
    
    # Test boolean
    result = eon.loads("true")
    assert result is True, f"Expected True, got {result}"
    result = eon.loads("false")
    assert result is False, f"Expected False, got {result}"
    print("✓ Boolean parsing works")
    
    # Test numbers
    result = eon.loads("42")
    assert result == 42, f"Expected 42, got {result}"
    result = eon.loads("3.14")
    assert abs(result - 3.14) < 0.001, f"Expected 3.14, got {result}"
    print("✓ Number parsing works")
    
    # Test strings
    result = eon.loads('"hello world"')
    assert result == "hello world", f"Expected 'hello world', got {result}"
    print("✓ String parsing works")
    
    # Test lists
    result = eon.loads('[1, 2, 3]')
    assert result == [1, 2, 3], f"Expected [1, 2, 3], got {result}"
    print("✓ List parsing works")

def test_loads_complex():
    """Test parsing complex EON structures"""
    print("\nTesting complex loads...")
    
    eon_string = """
    {
        name: "Alice",
        age: 30,
        is_active: true,
        skills: ["Python", "Rust", "JavaScript"],
        metadata: {
            created_at: "2024-01-01",
            updated_at: "2024-01-15"
        }
    }
    """
    
    result = eon.loads(eon_string)
    
    assert result["name"] == "Alice", f"Expected name='Alice', got {result['name']}"
    assert result["age"] == 30, f"Expected age=30, got {result['age']}"
    assert result["is_active"] is True, f"Expected is_active=True, got {result['is_active']}"
    assert result["skills"] == ["Python", "Rust", "JavaScript"], f"Expected skills list, got {result['skills']}"
    assert result["metadata"]["created_at"] == "2024-01-01", f"Expected metadata.created_at='2024-01-01', got {result['metadata']['created_at']}"
    
    print("✓ Complex object parsing works")
    print(f"Parsed object: {json.dumps(result, indent=2)}")

def test_dumps():
    """Test serializing Python objects to EON"""
    print("\nTesting dumps...")
    
    # Test basic types
    assert eon.dumps(None) == "null"
    assert eon.dumps(True) == "true"
    assert eon.dumps(False) == "false"
    assert eon.dumps(42) == "42"
    assert eon.dumps(3.14) == "3.14"
    assert eon.dumps("hello") == '"hello"'
    assert eon.dumps([1, 2, 3]) == "[1, 2, 3]"
    print("✓ Basic type serialization works")
    
    # Test complex object
    obj = {
        "name": "Bob",
        "age": 25,
        "active": True,
        "scores": [95, 87, 92]
    }
    result = eon.dumps(obj)
    # Parse it back to verify round-trip
    parsed = eon.loads(result)
    assert parsed == obj, f"Round-trip failed: {parsed} != {obj}"
    print("✓ Complex object serialization works")
    
    # Test formatted output
    formatted = eon.dumps(obj, indent=2)
    assert "\n" in formatted, "Expected multiline output with indent"
    print("✓ Formatted output works")
    print(f"Formatted EON:\n{formatted}")

def test_load_dump_files():
    """Test load/dump with file objects"""
    print("\nTesting load/dump with files...")
    
    # Test load from file
    with open("test.eon", "r") as f:
        result = eon.load(f)
    
    assert "user" in result, f"Expected 'user' key in result, got {result.keys()}"
    assert result["user"]["name"] == "Alice", f"Expected user.name='Alice', got {result['user']['name']}"
    print("✓ load() from file works")
    
    # Test dump to file
    test_obj = {"test": "data", "number": 123}
    with open("test_output.eon", "w") as f:
        eon.dump(test_obj, f, indent=2)
    
    # Read it back to verify
    with open("test_output.eon", "r") as f:
        loaded = eon.load(f)
    
    assert loaded == test_obj, f"File round-trip failed: {loaded} != {test_obj}"
    print("✓ dump() to file works")

def test_error_handling():
    """Test error handling"""
    print("\nTesting error handling...")
    
    try:
        eon.loads("invalid { syntax")
        assert False, "Should have raised an error"
    except ValueError as e:
        print(f"✓ Caught parsing error: {e}")
    
    try:
        with open("nonexistent.eon", "r") as f:
            eon.load(f)
        assert False, "Should have raised an error"
    except FileNotFoundError:
        print(f"✓ Caught file not found error")

if __name__ == "__main__":
    print("=" * 50)
    print("EON Python Bindings Test Suite")
    print("=" * 50)
    
    test_loads_basic()
    test_loads_complex()
    test_dumps()
    test_load_dump_files()
    test_error_handling()
    
    print("\n" + "=" * 50)
    print("All tests passed! ✅")
    print("=" * 50)