# Best practise that I used

* File: .github/workflows/python.yml

```yaml
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
        with:
          fetch-depth: 1 
          # Fetch only the latest commit for faster checkout
```

```yaml
    - name: Set up Python
      uses: actions/setup-python@v2  # Use v2 for simplicity
      with:
        python-version: 3.x
```

```yaml
    # Cache Python packages for faster subsequent runs
    - name: Cache dependencies
      uses: actions/cache@v2
      with:
        path: |
          ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-     
```

```yaml
    steps:
  - name: Checkout
    uses: actions/checkout@v4
    with:
      fetch-depth: 1
      # Fetch only the latest commit for faster checkout
```

* Parallel Jobs: If you have multiple steps that can run concurrently, split them into separate jobs to take advantage of parallelism and reduce workflow execution time.

* Caching: Utilize caching for dependencies to speed up workflow runs. Cache commonly used dependencies, such as Python packages, to avoid re-downloading them in each workflow run.

