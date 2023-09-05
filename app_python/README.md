# Current Moscow time application 

This application is using standard Python libraries `datetime` and `zoneinfo` to respond with current moscow time on a simple GET / request.
The application based on Django framework.

## How to run
### Prerequisite:
Django and Python installed ([installation guide](https://docs.djangoproject.com/en/4.2/intro/install/))

### Running from command line
```
cd app_python
python manage.py runserver
```
Server runs on default localhost path http://127.0.0.1:8000/ which can be opened in any browser. The page displays current time in Moscow timezone.