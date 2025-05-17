"""Utility to sort classes in a file."""

import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


def sort_classes_alphabetically(file_path: Path) -> None:
    """Sort classes alphabetically in a given file."""
    with file_path.open(encoding="UTF-8") as file:
        content = file.read()

    # Regular expression to match class definitions, including decorators and docstrings.
    class_pattern = re.compile(
        r"(@[^\n]+\n)*"  # Match decorators
        r"(class\s+\w+.*?:\n)"  # Match class definition line
        r"((?:\s{4}.*\n)*)",  # Match class content (indented lines)
    )

    # Find all classes.
    classes: list[tuple[str, str, str]] = class_pattern.findall(content)

    # Sort classes alphabetically by their class names.
    def get_class_name(class_match: tuple[str, str, str]) -> str:
        match = re.search(r"class\s+(\w+)", class_match[1])
        if match:
            return match.group(1)
        return ""  # Fallback in case no match is found, though it shouldn't happen here.

    sorted_classes = sorted(classes, key=get_class_name)

    # Reconstruct the file content with sorted classes.
    sorted_classes_content = ["".join(cls) for cls in sorted_classes]
    non_class_content = class_pattern.sub("", content).strip()

    new_content = non_class_content + "\n\n\n" + "\n\n".join(sorted_classes_content)

    # Write the new content back to the file.
    with file_path.open(mode="w", encoding="UTF-8") as file:
        file.write(new_content)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: python {sys.argv[0]} <file_path>")
        sys.exit(1)

    file_to_sort = Path(sys.argv[1])
    if not file_to_sort.exists():
        print(f"File '{file_to_sort}' does not exist")
        sys.exit(1)

    sort_classes_alphabetically(file_to_sort)
    print(f"Classes in '{file_to_sort}' have been sorted alphabetically")

    # Format the file.
    subprocess.run(
        [f"{PROJECT_ROOT}/.venv/bin/ruff", "format", file_to_sort],
        check=True,
        stdout=subprocess.DEVNULL,
    )
