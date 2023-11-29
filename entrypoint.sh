#!/bin/sh

# Run Trivy scan and save results in JSON format
trivy image -f json -o trivy_results.json $@

#!/bin/bash
# Pass the results to the Python script
#pip3 install requests --root-user-action=ignore
pip install requests --root-user-action=ignore
python reporter.py trivy_results.json
