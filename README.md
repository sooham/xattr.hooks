# git-xattr-hooks

Git Hooks designed to store and OS X icons resource from a file's resource fork
in a remote repository.

Adding capability for OS X tags (com.apple.metadata:_kMDItemUserTags) later

## Outline of program execution
In Mac OS X's HFS filesystem , all file include a sub-element called a 
`resource fork` - used to store non-compiled data for OS X GUI into subelements
called `resources`. The resource relevant to the file icon is named `icns`.

The pre-commit hook, which is executed by `.git` before commits, uses OS X 
`DeRez` utility to decompile the resource forks of all files with the com.apple.ResourceFork
extended attribute as a resource file on the remote repo. The post-merge hook
appends this back to the files in order.
```
1. DeRez fileWithIconResource -only icns > tempStorage.rsrc
2. git commit tempStorage.rsrc
3. Pull / Fetch repo
4. Rez tempStorage.rsrc -append -o fileWithIconResource
5. SetFile -a C fileWithIconResource
```

## How to use
```
chmod +x <path-to-git-xattr-hooks>/*
cp <path-to-git-xattr-hooks>/* <path-to-local-repo>/.git/hooks/
```
Edit shebang line for both executables if needed.

### Dependencies
* Xcode Command Line Tools


