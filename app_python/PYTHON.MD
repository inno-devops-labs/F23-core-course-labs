## Framework
I've chosen **Flask** python framework since it's the most popular one and it has a well-written documentation. 

## Best practices
- **Separation of Concerns**:

    Separated configuration data (config.py) from application logic (app.py). This helps make the codebase cleaner and easier to maintain. Any changes related to configurations don't impact the main logic.

- **Error Handling**:

    Used a try-except block in the moscow_time function to handle potential errors and prevent the app from crashing unexpectedly. Instead, it logs the error and returns a meaningful message to the user.

- **Structured Logging**:

    Used a structured logging format which includes a timestamp, the logging level, the module where the log is from, and the log message. This provides clarity in log messages and aids in troubleshooting.

- **Log Rotation**:

    Used RotatingFileHandler to ensure the log file doesn't grow indefinitely. The handler rotates logs when they reach a certain size, preventing potential space issues and making log management more efficient.

- **Project Structure**:

    Organized the project in a clear structure, separating the virtual environment (venv), templates, static files, and application code. This structure makes the project easier to navigate, understand, and expand in the future

- **Code Documentation**: Throughout the code, concise and clear comments were incorporated to explain the purpose and functioning of various sections.
