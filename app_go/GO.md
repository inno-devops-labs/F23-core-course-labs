## Choosing framework
No framework was choosen, in this app build-in . (Author writes in Go for the first time)
Moreover application have no external dependencies yet.

### Best practices used
- Project have `templates` to display info, it is better quality than hardcode page.
- Added [pre-commit](https://pre-commit.com/) hooks to check code formatting before commit. It uses:
    - `go-fmt` to format GO code.
    - `go-unit-tests` test to check web server functionality.
- Added unit test for man page.
- Added `gitignore` file to exclude unnecessary files from git.

### Unit Tests
I have created following unit tests:
- test if page loads with status code 200
- test if pade contains body
- test if displayed time is correct (with a one second margin of error)

**Best practices used**:

- **Documented**: Each test is now named descriptively to indicate what it is testing. There are clear error messages to indicate what went wrong if the test fails. This helps in understanding the purpose and expected behavior of each test.

- **One test for one function**: Each test function is responsible for testing a specific functionality or behavior of the application. For example, one for page status, and one for checking time correctness.

- **High coverage**: The tests cover most, if not all, aspects of the application's functionality.

- **Integration in CI**: Tets are integrated into the github actions.

Run tests:
```
go test
```
