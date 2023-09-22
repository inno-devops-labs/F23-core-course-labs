# Moscow Time Display Web Application

This is a simple Flask web application that displays the current time in Moscow.

## Technologies Used

- Flask
- Python 3.7
- HTML/CSS/Bootstrap

## Installation and Run

1. Clone the repository to your local machine.
2. Run the virtual environment by running `python3 -m venv venv`.
3. Install running `pip install Flask`
4. And to run the app:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

4. Open your web browser and navigate to http://localhost:5000 to view the current time in Moscow.

## Usage

The application displays the current time in Moscow in the 24 hours format `HH:MM:SS`. Also there is date in format `Wday,Month day, year`
The time is updated every second.

## Testing

To run the automated tests for this system, run python app_test.py.

## Project Structure

<pre>
app_python/ 
 ├── app.py 
 ├── test_app.py  
 ├── README.md 
 ├── PYTHON.md 
 └── templates/ 
      └── base.html 
</pre>

- app.py: contains the Flask app code.
- test_app.py: contains the unit test for the Flask app.
- README.md: contains the documentation for this project.
- PYTHON.md: contains the documentation of best practices for this project.
- templates/base.html: contains the HTML code for the home page of the web application.
