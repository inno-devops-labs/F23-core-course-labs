# app_python

## Overview

This is a simple Python web application built with Flask that displays the current time
in Moscow. It serves as a basic example of a web application and can be used as a
starting point for more complex projects.

## Build

To build and run this project locally, follow these steps:

1. Unpack the archive with the project

2. Navigate to the project directory:

   ```bash
   cd app_python
   ```

3. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:

   ```bash
   python app.py
   ```

7. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to
   view the current time in Moscow.

### With Docker
1. Clone the repository. Go to `app_python` folder
2. Build an image 
  
   ```
   docker build -t maksktl/app_python:latest .
   ```
      
    or pull an image from docker hub 

   ```
   docker pull maksktl/app_python:latest
   ```
3. Create and run a container from the built image
   ```
   docker run -d -p 8000:5000 maksktl/app_python
   ```
4. Access the website `localhost:8000`

## Usage

The application is straightforward to use. Once you have it running locally or deployed,
open a web browser and navigate to the provided URL to see the current time in Moscow.

## Contact

If you have any questions or need assistance, feel free to contact the project
maintainer:

- Name: Maxim Matantsev
- Email: m.matantsev@innopolis.university
