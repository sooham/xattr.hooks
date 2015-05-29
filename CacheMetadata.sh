#!/bin/sh
# pre-commit hook
xattr -lrx . > .metadata
git add -f .metadata
git commit --allow-empty -m "Added metadata"
