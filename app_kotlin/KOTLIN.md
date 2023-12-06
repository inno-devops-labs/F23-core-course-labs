## Framework
I use **Spring** because it's the most popular and comfortable framework for Java/Kotlin web development. 
Also, I already have experience with this

## Best practises
* **Consistent & predictable project structure** - divide app into controller, services, etc. 
to implement single responsibility principle
* **Use Spring DI functionality** - to make the code more readable, testable and less coherent
* **Use custom exception** - for providing correct code statuses in API
* **Divide test into WebMVC and Service test** - to avoid creating Spring Context at every test running
* **Logging** - log all needed info to monitor app state

## Code quality
* Implemented unit tests
* Use SonarLint for checking code style

## Unit tests
I created unit tests for controller and service separately:
* For controller I check status codes for different exceptions
* For service I check business logic of my app.

Best practices:
* Make test code short and readable
* Isolate components
* Test one thing at a time
* Meaningfully naming
* Use mockito
* Make javadoc for each test
* Create tests for value boundaries (For example, for my app the maximum base is 150. I test functionality for 150 and for 151)