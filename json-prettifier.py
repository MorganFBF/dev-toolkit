# json-prettifier.py
import json
import sys

def pretty_print_json(json_data):
    try:
        parsed = json.loads(json_data)
        print(json.dumps(parsed, indent=4, sort_keys=True))
    except json.JSONDecodeError:
        print("Invalid JSON input.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Read JSON from file
        with open(sys.argv[1], 'r') as file:
            data = file.read()
            pretty_print_json(data)
    else:
        # Read JSON from stdin
        print("Paste JSON and press Ctrl+D (or Ctrl+Z on Windows) to format:")
        input_data = sys.stdin.read()
        pretty_print_json(input_data)
