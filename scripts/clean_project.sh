#!/usr/bin/env bash

set -e

clean_project() {
    local mode="$1"
    local dry_flag=""

    if [[ "$mode" == "dry-run" ]]; then
        dry_flag="n"
    fi

    git clean -"${dry_flag}"dfx -e .env -e .tmp/
}

echo "You're about to clean the project by deleting all untracked files and directories."
echo "Excluded from deletion: .env, .tmp/"
echo

read -rp "Proceed? [y]es / [n]o / [m]ore info: " choice

case "$choice" in
    [Yy])
        clean_project clean
        echo "Project cleaned."
        ;;
    [Mm])
        echo
        echo "The following files/directories would be deleted:"
        clean_project dry-run
        echo
        read -rp "Do you want to proceed with cleaning? (y/n) " confirm
        case "$confirm" in
            [Yy])
                clean_project clean
                echo "Project cleaned."
                ;;
            *)
                echo "Aborted."
                ;;
        esac
        ;;
    *)
        echo "Aborted."
        ;;
esac
