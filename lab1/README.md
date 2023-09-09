# Lab 1 - Web application

Azamat Shakirov B20-CS

a.shakirov@innopolis.university



## Overview

Application to display current time in Moscow in format YYYY-MM-DD HH:MM:SS

## Docker

Building docker container:

```bash
docker build dev-ops-lab-2 .
```

Or pulling from Docker Hub:

```bash
docker pull hephzibah301/dev-ops-lab-2:latest
```

To start docker image:

```bash
docker run -p 5000:5000 dev-ops-lab-2
```

Application will available via [http://127.0.0.1:5000](http://127.0.0.1:5000) 

## Build

Packages installation:

```bash
pip3 install -r requirements.txt
```

## Run

```python
python3 main.py
```

## Test

```python
pytest test.py
```

## Usage

After starting the application visit [http://127.0.0.1:5000](http://127.0.0.1:5000) or directly from terminal

```bash
curl http://127.0.0.1:5000
```

## Contact

a.shakirov@innopolis.university

