To run this application:

```bash
uvicorn main:app --host localhost --port 8000
```

To terminate:

```
Ctrl + C
```

Docker section:

To build image:

inside the app_python folder
```
sudo docker build -t app_python .
```

To run image:
```
sudo docker run -p 8000:8000 app_python
```

To pull image:
```
sudo docker pull realpxkn/app_python
```

To run tests:
```
pytest test.py
```

[![Python CI with Docker](https://github.com/beleet/core-course-labs/actions/workflows/docker-ci.yml/badge.svg)](https://github.com/beleet/core-course-labs/actions/workflows/docker-ci.yml)
