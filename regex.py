import json
import re

def generate_regex_for_key_value(json_str, key):
    """
    Generate a regex pattern to capture the value for a given key in a JSON string.
    
    Args:
    - json_str: The JSON string to analyze.
    - key: The key for which to generate the regex pattern.
    
    Returns:
    - A regex pattern string.
    """
    # Escape key for regex pattern
    escaped_key = re.escape(key)
    
    # Generate regex pattern
    # This pattern matches the key and captures its value, assuming the value is a string.
    pattern = rf'"{escaped_key}"\s*:\s*"\s*([^"]+)\s*"'
    
    return pattern

# Example Usage
key = "hobby"
json_str = '{"name": "John Doe", "age": 30, "city": "New York", "friends": ["Alice", "Bob"], "details": {"nickname": "Johnny", "hobby": "hiking"}}'

# Generate the regex pattern
regex_pattern = generate_regex_for_key_value(json_str, key)
print(f"Generated Regex Pattern: {regex_pattern}")

# Example of using the regex pattern to find and capture the value
import re
match = re.search(regex_pattern, json_str)
if match:
    value = match.group(1)
    print(f"Captured Value: {value}")
else:
    print("No match found.")
