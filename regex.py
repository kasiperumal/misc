import json
import re

def generate_regex_for_key_value(json_str, key):
    """
    Generate a regex pattern to capture all string values for a given key in a JSON string.
    
    Args:
    - json_str: The JSON string to analyze.
    - key: The key for which to generate the regex pattern.
    
    Returns:
    - A regex pattern string.
    """
    # Escape key for regex pattern
    escaped_key = re.escape(key)
    
    # Generate regex pattern
    # This pattern matches the key and captures all its string values.
    pattern = rf'"{escaped_key}"\s*:\s*"\s*([^"]+)\s*"'
    
    return pattern

# Example Usage
key = "hobby"
json_str = '{"name": "John Doe", "age": 30, "city": "New York", "friends": ["Alice", "Bob"], "details": {"nickname": "Johnny", "hobby": "hiking", "hobby": "reading"}}'

# Generate the regex pattern
regex_pattern = generate_regex_for_key_value(json_str, key)
print(f"Generated Regex Pattern: {regex_pattern}")

# Use the regex pattern to find and capture all string values for the key
matches = re.findall(regex_pattern, json_str)
if matches:
    for value in matches:
        print(f"Captured Value: {value}")
else:
    print("No match found.")
