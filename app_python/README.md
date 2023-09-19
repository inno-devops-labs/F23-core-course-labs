# Web application

This application displays the current time in Moscow

## Getting started

### In host

1. Install python3
2. Install required packages
```pip install -r requirements.txt```
3. Run the application ```python3 main.py```
4. Visit page http://127.0.0.1:8000

### In docker

1. Build docker:
```docker build -f Dockerfile -t ign19ht/dev-ops-labs .```
2. Pull docker:
```docker pull ign19ht/dev-ops-labs```
3. Run docker:
```docker run -dp 8000:8000 ign19ht/dev-ops-labs```
