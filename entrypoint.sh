#!/bin/sh

# Run Trivy scan and save results in JSON format
trivy image -f json -o trivy_results.json $@

#!/bin/bash
# Pass the results to the Python script
python reporter.py trivy_results.json
