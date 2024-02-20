import json
import re

def find_values_by_key_under_parent(json_str, parent, key):
    """
    Find and print all values associated with a given key under a specified parent in a JSON string.
    
    Args:
    - json_str: The JSON string to analyze.
    - parent: The immediate parent name under which to look for the key.
    - key: The key for which to find values.
    """
    # Escape parent and key for regex pattern to avoid issues with special characters
    escaped_parent = re.escape(parent)
    escaped_key = re.escape(key)

    # Build a regex pattern that targets the specified parent and key.
    # This pattern is designed to be somewhat flexible, attempting to match key-value pairs within the scope of the given parent.
    # Note: This approach has limitations and may not work for all possible JSON structures.
    pattern = rf'"{escaped_parent}"\s*:\s*(?:\[\s*\{{|\{{)[^}}]*?"{escaped_key}"\s*:\s*"([^"]+)"'

    # Find all matches for the pattern
    matches = re.findall(pattern, json_str, re.DOTALL)
    
    if matches:
        for value in matches:
            print(f"Captured Value: {value}")
    else:
        print(f"No values found for key '{key}' under parent '{parent}'.")

# Example Usage
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

parent = "details"
key = "hobby"

find_values_by_key_under_parent(json_str, parent, key)
