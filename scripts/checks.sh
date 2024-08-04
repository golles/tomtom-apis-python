#!/usr/bin/env bash

# Dev tool to run all the code checks

set -e

cd "$(dirname "$0")/.."

# Function to log messages in yellow color
log_yellow() {
    echo -e "\e[33m$1\e[0m"
}

log_yellow "mypy"
poetry run mypy .

log_yellow "Prettier"
poetry run prettier --check .

log_yellow "Pylint"
poetry run pylint src tests

log_yellow "Ruff linter"
poetry run ruff check .

log_yellow "Ruff formatter"
poetry run ruff format --check .

log_yellow "YamlLint"
poetry run yamllint .

echo -e "\nOK!"
