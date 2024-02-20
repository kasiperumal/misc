import json
import re

def generate_regex_for_key_under_parent(json_str, parent, key):
    """
    Generate a regex pattern to capture all values for a given key under a specified parent in a JSON string.
    
    Args:
    - json_str: The JSON string to analyze.
    - parent: The immediate parent name under which to look for the key.
    - key: The key for which to generate the regex pattern.
    
    Returns:
    - A regex pattern string.
    """
    # Escape parent and key for regex pattern
    escaped_parent = re.escape(parent)
    escaped_key = re.escape(key)
    
    # Generate regex pattern
    # This pattern matches the parent and captures all its contained key's values.
    # The pattern accounts for objects ({}) and arrays of objects ([{}]).
    pattern = rf'"{escaped_parent}"\s*:\s*(?:\{{[^{{}}]*?|[\[]\{{[^{{}}]*?)"{escaped_key}"\s*:\s*"\s*([^"]+)\s*"(?:[^{{}}]*?\}}|[^{{}}]*?\]}})'
    
    return pattern

# Example Usage
parent = "details"
key = "hobby"
json_str = '''
{
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "friends": ["Alice", "Bob"],
    "details": [{
        "nickname": "Johnny",
        "hobby": "hiking"
    },{
        "nickname": "Johnny",
        "hobby": "reading"
    }]
}'''

# Generate the regex pattern
regex_pattern = generate_regex_for_key_under_parent(json_str, parent, key)
print(f"Generated Regex Pattern: {regex_pattern}")

# Use the regex pattern to find and capture all values for the key under the specified parent
matches = re.findall(regex_pattern, json_str, re.DOTALL) # re.DOTALL to make '.' match newlines as well
if matches:
    for value in matches:
        print(f"Captured Value: {value}")
else:
    print("No match found.")
