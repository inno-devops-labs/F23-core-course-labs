# Miscellaneous

## Code quality

In order to lint the project there are `ruff` and `markdownlint`:

```bash
ruff main.py
markdownlint PYTHON.md README.md
```

### Examples

```bash
> ruff main.py
main.py:20:89: E501 Line too long (90 > 88 characters)
Found 1 error.
```

```bash
> markdownlint PYTHON.md README.md
PYTHON.md:3 MD022/blanks-around-headings/blanks-around-headers
    Headings should be surrounded by blank lines
    [Expected: 1; Actual: 0; Below] [Context: "## Code quality"]
PYTHON.md:5 MD031/blanks-around-fences
    Fenced code blocks should be surrounded by blank lines [Context: "```bash"]
PYTHON.md:10 MD022/blanks-around-headings/blanks-around-headers
    Headings should be surrounded by blank lines 
    [Expected: 1; Actual: 0; Below] [Context: "### Examples:"]
PYTHON.md:10:13 MD026/no-trailing-punctuation
    Trailing punctuation in Headings
    [Punctuation: ':']
PYTHON.md:11 MD031/blanks-around-fences
    Fenced code blocks should be surrounded by blank lines
    [Context: "```bash"]
PYTHON.md:15 MD031/blanks-around-fences
    Fenced code blocks should be surrounded by blank lines
    [Context: "```"]
PYTHON.md:16 MD031/blanks-around-fences
    Fenced code blocks should be surrounded by blank lines
    [Context: "```bash"]
README.md:10 MD032/blanks-around-lists
    Lists should be surrounded by blank lines
    [Context: "1. Install [npm](https://docs...."]
```
