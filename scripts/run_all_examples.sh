#!/usr/bin/env bash

# This script runs all the example python scripts in the examples directory.

set -e

# shellcheck source=/dev/null
source "$(dirname "$0")/utils.sh"

# Source environment variables if .env file exists
if [ -f .env ]; then
    set -a
    # shellcheck source=/dev/null
    source .env
    set +a
fi

# Prompt for API key if not set
if [ -z "${TOMTOM_API_KEY:-}" ]; then
  read -rp "Please enter your API key: " TOMTOM_API_KEY
  export TOMTOM_API_KEY
fi

# Run all example scripts
for filename in $(find examples -type f -name "*.py" | sort); do
    log_yellow "Run $filename:"
    uv run "$filename"
done
