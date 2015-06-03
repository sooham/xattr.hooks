# git-xattr-hooks

Git Hooks designed to store OS X extended attributes retrieved from `xattr`
and custom Finder file icons. Allows git to store file custom icons, tags, 
permissions etc in remote repositories.

### How does it work?
The pre-commit hook scans the local repository for extended attributes and 
custom finder icons using `xattr`. This information is stored in a temporary
file `.metadata` which is then committed. When merged/pulled/cloned the
information from `.metadata` is used to updated files.

### How to use
```
chmod +x <path-to-git-xattr-hooks>/*
cp <path-to-git-xattr-hooks>/* <path-to-local-repo>/.git/hooks/
```
Edit shebang line for both executables if needed.

### Dependencies
* Xcode Command Line Tools


