## Framework choice

The Flask framework was chosen for implementing the application due to several factors:

1. Lightweight and Minimalistic: Flask is a microframework, meaning it focuses on simplicity and minimalism. It doesn't come bundled with unnecessary features and is easy to set up and use, especially in case where our application doesn't need complicated features.  
2. Routing: Flask has a straightforward routing system that maps URL patterns to specific functions or views. 
3. Ease of Maintenance: Flask follows the "Keep It Simple" principle, which makes it easy to understand and maintain code written with the framework.
4. Popularity: Flask is a widely-used and popular framework within the Python community. Hence, it will be easier to troubleshoot any sort of bugs faced in the process of development

## Applied practices

- The following coding practices were implemented:
    - Test-Driven Development: unit test which verifies correctness of our returned time was implemented before the route itself. Pytest framework was used for testing. 
        - In order to verify correctness of returned time, I have made a sequence of requests and verified that the difference between returned value and client time is less than particular threshold.
    - Separate `requirements.txt`: Flask encourages the use of a separate `requirements.txt` file to manage project dependencies. 
    - Separation of configuration from the business logic: separate `config.py` is used to manage configuration of the application. It also supports environmental variables thus making distribution of the application easier. 
    - KISS (keep it simple, stupid): more complex flask applications might require different project layout and separation of components. However, for the simple web services, extension of which is unlikely, community encourages to use simpler repository structure.
        - The single route `display_time` is contained in the `handlers/routes.py` file. Business logic is not separated or delegated to separate service because the overall functionality is not demanding.
    - Variables naming according to the naming conventions
    - Commenting and documentation: key functions in the project are commented. Documentation to the project is present in the `README.md`