# Project information

## Best practices used
1. Document and Comment Your Code Properly. Example: The project has documented functions.
2. Write Readable Code.
3. Test Your Code. Example: The project has two tests.
4. Use logging. I have used `kotlin-logging-jvm` library that provided logger.
5. Keep the unified file structure that matches conventions.
6. Use `.editorconfig` to keep code style unified.
7. Use `.gitignore` to keep project files clean.
8. Use code linter that is injected in application building process. I have used `detekt` formatter.
9. Use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit naming.
10. Use MVC pattern for code architecture.
11. Use Spring Dependency Injection and Inversion of Control patterns.

## Linter
I have used code linter named [`detekt`](https://detekt.dev/) for Kotlin. For linting I have used default `detekt` rules with some overriding. The changes could be found here: `./app_kotlin/config/detekt.yml`.

## Framework selection

I have used Spring production framework because it is the most popular and used framework that provides Dependency Injection and Web for Java/Kotlin. Also, I have already had experience with it.
