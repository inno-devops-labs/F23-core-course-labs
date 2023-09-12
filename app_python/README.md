# App_python

This is application to show current time in specified region (timezone).
Initially, it shows Moscow time.

## How to run

1. Install `Python` at least version 3.11:

    ```shell
    apt install python:3.11
   ```

1. Create virtual environment. It will generate new folder with your virtual environment:

    ```shell
    python3 -m venv /path/to/your/environment
   source /path/to/your/environment/bin/activate
   ```

1. Install dependencies:

    ```shell
   pip install -r ./requirements/dev.txt
   ```

1. Run the application. To run it you must be in project folder (in *devops-course-labs*):

    ```shell
   cd ..
   python -m uvicorn app_python.src.main:app --reload
   ```

## Tests

1. To run tests make sure you installed dependencies:

    ```shell
    pip install -r ./requirements/dev.txt
    ```

1. Run tests. You can run the following command either in *app_python* or in *app_python/tests* folder:

    ```shell
    pytest
    ```