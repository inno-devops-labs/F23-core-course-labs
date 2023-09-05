# Current Moscow time application 

This application is using standard Python libraries `datetime` and `zoneinfo` to respond with current moscow time on a simple GET / request.
The application based on Django framework.

## Framework choice

I decided to use Django framework for this project, because it is wide-used, open-source and very friendly to beginners.
Also, it has full and good documentation with lots of different tutorials and a lot of users, which means that it is easy to solve any problem I could face with.
Despite that Django is an easy-to-start framework, it is very powerful, because some big applications implemented on it (e.g. Instagram, Spotify).

## Used best practices
- Regular Commits (used isolated commits for each step of the project)
- Descriptive Commit Messages (each commit has clear and full description of what was done)

## Testing and code quality
- For testing, I used build-in local Django server that detects every code change and deploys it immediately, so that the page http://127.0.0.1:8000/ always shows actual page content.
- I implemented an easy-to-understand, consistent, easy testable and free of bugs code to ensure code quality.

## How to run
### Prerequisite:
Django and Python installed ([installation guide](https://docs.djangoproject.com/en/4.2/intro/install/))

### Running from command line
```
cd app_python
python manage.py runserver
```
Server runs on default localhost path http://127.0.0.1:8000/ which can be opened in any browser. The page displays current time in Moscow timezone.