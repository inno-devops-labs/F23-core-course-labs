# My web application

The application contains ```app/__init__.py``` file, which contains the root endpoint for displaying Moscow time. 

## Run

You can run the application by running the ```run.py``` file.

![screenshot of working application](img.png)

# Docker

How to launch:
1. Build with ```sudo docker image build -t my_app .```
2. Pull with ```docker image pull tnechepurencko/my_app```
3. Run with ```sudo docker run -d -p 5000:5000 my_app```