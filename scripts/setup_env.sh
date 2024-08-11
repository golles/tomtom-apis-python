#!/usr/bin/env bash

set -e

cd "$(dirname "$0")/.."

# Function to log messages in yellow color
log_yellow() {
    echo -e "\e[33m$1\e[0m"
}

# Function to log error messages in red color
log_error() {
    echo -e "\e[31m$1\e[0m" >&2
}

# Error handling
error_exit() {
    log_error "An error occurred. Exiting..."
    exit 1
}

# Trap any error and execute the error_exit function
trap error_exit ERR

# Check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Ensure Poetry is installed
if ! command_exists poetry; then
    log_yellow "Poetry is not installed. Checking for pipx..."
    if command_exists pipx; then
        log_yellow "pipx is installed. Installing Poetry using pipx..."
        pipx install poetry
    else
        log_error "Neither Poetry nor pipx is installed. Please install pipx or Poetry manually."
        exit 1
    fi
fi

# Ensure npm is installed
if ! command_exists npm; then
    log_error "npm is not installed. Please install npm manually."
    exit 1
fi

# Configure venv with Poetry
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true

# Install project dependencies
poetry install

# Install other programs
npm install -g prettier

if [ "$CI" != "true" ]; then
    # Trust the repo
    git config --global --add safe.directory /workspaces/tomtom-api-python

    # Add the pre-commit hook if not on CI
    poetry run pre-commit install

    # Install auto completions
    mkdir -p ~/.zfunc
    poetry completions zsh > ~/.zfunc/_poetry
    grep -qxF 'fpath+=~/.zfunc' ~/.zshrc || echo 'fpath+=~/.zfunc' >> ~/.zshrc
    grep -qxF 'autoload -Uz compinit && compinit' ~/.zshrc || echo 'autoload -Uz compinit && compinit' >> ~/.zshrc

    log_yellow "poetry auto completion has been added or updated, you need to reload your terminal"
fi

# Check for --devcontainer argument
if [ "$1" == "--devcontainer" ]; then
    log_yellow "\n\nThe dev container is ready"
    log_yellow "Once all the extensions are installed, reload this window (CMD+P -> Developer: Reload Window) to make sure all extensions are activated!"
else
    log_yellow "\nDone"
fi
