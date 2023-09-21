"""This module serves as the entry point to launch the application"""

from app import create_app
import os


app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("APP_PORT", "5000"))

    host = "0.0.0.0"

    print(f"Running server on {port=}...")

    app.run(host=host, port=port, debug=True)
