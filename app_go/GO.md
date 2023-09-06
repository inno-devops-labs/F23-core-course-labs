## Choosing framework
No framework was choosen, in this app build-in . (Author writes in Go for the first time)
Moreover application have no external dependencies yet.

## Best practices used
- Project have `templates` to display info, it is better quality than hardcode page.
- Added [pre-commit](https://pre-commit.com/) hooks to check code formatting before commit. It uses:
    - `go-fmt` to format GO code.
    - `go-unit-tests` test to check web server functionality.
- Added unit test for man page.
- Added `gitignore` file to exclude unnecessary files from git.
