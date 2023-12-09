"""
Run the module app for gunicorn
"""
from main import app as application


if __name__ == "__main__":
    application.run()
