# How to contribute

Thank you for taking the time and effort to read this guide! Your contributions are valuable, and we appreciate your interest in improving our project.

## Getting Started

Before you start contributing, it's essential to familiarize yourself with the codebase. Spend some time reading the existing code to understand the current style and structure. This will help you align your contributions with the project's conventions and optimize for readability.

## Development Environment

To ensure a consistent development environment, we recommend using a devcontainer or GitHub Codespace. These tools provide a standardized setup that matches the project's requirements.

If you prefer using a local development environment, you can create a Python virtual environment using the `scripts/setup_env.sh` script. This script relies heavily on Poetry to manage dependencies and environment settings and will also install prettier and the pre-commit hook.

```sh
./scripts/setup_env.sh
```

### Setting Up the .env File

Some of the scripts (e.g., `update_test_fixtures.py`) and the examples require an existing API key. To avoid the hassle of entering the API key every time you run these scripts, you can copy `.env.sample` to `.env` and fill in the API key. The VS Code terminal should automatically source this file when a new terminal is opened.

```sh
cp .env.sample .env
# Edit the .env file to add your API key
```

## Pre-Commit Hook

We use a pre-commit hook to help identify simple issues before submitting your code for review. This ensures that your code meets the project's quality standards and reduces the chances of encountering avoidable errors during the review process.

## Submitting Changes

Changes should be proposed through a pull request (PR). When creating a PR, please include the following:

- A summary of the changes you are proposing.
- Links to any related issues.
- Relevant motivation and context for the changes.

This information helps reviewers understand the purpose of your changes and facilitates a smoother review process.

## Adding Tests

To ensure the stability and reliability of the codebase, please include tests with your pull request. Adding tests helps verify that your changes work as intended and do not introduce new issues.

Thank you for contributing to [Your Project Name]! Your efforts help us maintain a high-quality codebase and make the project better for everyone.

Happy coding!
