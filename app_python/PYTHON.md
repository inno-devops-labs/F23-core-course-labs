# Python Web Application Development - Daniil Okrug

Framework choosing:

- The Web application uses the Flask framework.
- Flask is a lightweight and easy-to-use framework that is well-suited for small to medium-sized web applications like this one.
- Flask has built-in support for testing through Flask-Testing and integrates well with popular testing libraries like pytest. This makes it easy to write and run tests, ensuring the reliability of application
- While Flask is a lightweight framework, it is also scalable. If your project evolves and requires additional features or complexity, Flask can handle it.
- Flask's simplicity often translates into better performance, especially for small applications. It doesn't introduce unnecessary overhead, making it suitable for applications where performance is a consideration.
- Flask can be deployed on various hosting platforms and cloud providers, giving you the flexibility to choose the deployment method that best suits your project's requirements.

Best practices:

- I'm using Python Enhancement Proposal 8 (PEP 8) style guide for code formatting to ensure consistency and readability
- Project following Flask's recommended application structure, separating routes, templates, and static files
- Implemeted tests with pytest to cover different aspects of application. Coverage: 91%
