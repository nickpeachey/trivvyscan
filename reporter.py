# process_results.py

import sys
import json

def process_results(json_file):
    # Load the JSON results
    with open(json_file, 'r') as file:
        results = json.load(file)

    # Process the results as needed
    print("Trivy scan results:")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 process_results.py <trivy_results.json>")
        sys.exit(1)

    json_file = sys.argv[1]
    process_results(json_file)