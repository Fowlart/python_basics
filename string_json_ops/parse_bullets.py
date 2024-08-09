import re


def replace_escaped_quotes(text):
    """Replaces escaped double quotes (\") with double single quotes ('')."""
    return text.replace(r'\"', "''")

def parse_string_with_escaped_quotes(input_string):
    """Parses a string into a list of items, handling escaped double quotes."""

    modified_string = replace_escaped_quotes(input_string)

    return re.findall(r'"([^"]+)"', modified_string)

# Example usage
string_data = r"""["CUTS FASTER than traditional belts", "Available Sizes : 3\" x 18\", 3\" x 21\", 3\" x 24\", 4\" x 24\" and 4\" x 36\""]"""

for s in parse_string_with_escaped_quotes(string_data):
    print(s)
