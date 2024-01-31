import datetime
import logging
from flask import Flask, render_template

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/')
def display_time():
    try:
        # Correct the usage of datetime.utcnow()
        moscow_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
        formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

        # Log the current time
        logging.info(f"Displayed Moscow time: {formatted_time}")

        # Log a custom message
        logging.info("Custom log message")

        return render_template('index.html', time=formatted_time)
    except Exception as e:
        # Log any exceptions that occur
        logging.error(f"An error occurred: {str(e)}")

        # You can create an error template for users
        return render_template('error.html')


if __name__ == '__main__':
    app.run()
