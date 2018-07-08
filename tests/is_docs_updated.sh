#! /usr/bin/env bash

main() {
    git status --porcelain
    diff=$(git status --porcelain | grep "docs/html")
    [[ -z "${diff}" ]]
}

main
