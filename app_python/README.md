# My Python Web App

This is a simple Python web application that displays the current time in Moscow.

## Overview

``` python
from flask import Flask
from datetime import datetime
import pytz
```

### Code here is imports of libraries that I will use later

``` python
app = Flask(__name__)
@app.route('/')
```

### Here I created flask application and defined a route

```python
def show_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    return f'Current time in Moscow: {current_time}'
```

### This function is getting current time in Moscow and then returns it in web client

``` python
if __name__ == '__main__':
    app.run()
```

### Here I just run my application  

## Usage

1. Install the required dependencies (Flask).
2. Run the application using `python app.py`.
3. Open your web browser and visit `http://localhost:5000` to see the current time in Moscow.

## Author

Khabib Khaysadykov
