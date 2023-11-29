#!/bin/sh
echo "running trivy scan with additional args: $@"


trivy \
    image \
    --insecure \
    --ignore-unfixed \
    --username @username \
    --password @password \
    --format json \
    --output results.json \
    $@