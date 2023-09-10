# Flask App README

## Project Overview

This Flask app displays the current time in Moscow's time zone (MSK).

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository and navigate to it.

2. Install dependencies:

```bash
    pip install -r requirements.txt
```

## Running the App

To run the Flask app in development:

```bash
    python run.py
```

Or with gunicorn:

```bash
    gunicorn --bind 0.0.0.0:5050 --workers 4 run:app
```

The app will be available at <http://localhost:5050/>.

## Testing the App

To test the Flask app run:

```bash
    python -m unittest tests.py
```
