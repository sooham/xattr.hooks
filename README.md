# git-xattr-saver-OSX

## What is it?
Git Hooks designed to store Mac OS X file extended attributes retrived from `xattr`.

Many filesystems store file metadata (icons, tags, permissions etc.) as "extended attributes".
Sadly Git and other version control systems do not store this information on file. git-xattr-saver solves this problem by providing simple pre-commit and post-merge hooks which cache the xattr information.

Works for Linux and Mac OS X.

## Why?
My project 'Bash-adventure' uses ordinary text files with icon metadata as sprites but is unable to store
them on git.
