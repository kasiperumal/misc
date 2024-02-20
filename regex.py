import re

def find_values_by_key_in_parent(json_str, parent, key):
    """
    Find and print all values for a given key within a specified parent in a JSON string.
    
    Args:
    - json_str: The JSON string to analyze.
    - parent: The immediate parent key to search within.
    - key: The target key whose values to capture.
    """
    # Escape parent and key for regex pattern
    escaped_parent = re.escape(parent)
    escaped_key = re.escape(key)
    
    # Pattern to find an object/array named as parent and capture its content
    parent_pattern = rf'"{escaped_parent}"\s*:\s*(\{{.*?\}}|\[.*?\])'
    
    # Find parent object/array
    parent_matches = re.findall(parent_pattern, json_str, re.DOTALL)
    
    for parent_match in parent_matches:
        # Pattern to capture values for the given key within the parent content
        value_pattern = rf'"{escaped_key}"\s*:\s*"([^"]+)"'
        
        # Find all values for the key within each parent content
        values = re.findall(value_pattern, parent_match, re.DOTALL)
        
        for value in values:
            print(f"Captured Value: {value}")

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

find_values_by_key_in_parent(json_str, "details", "hobby")
