### Implemented best practices

1. Alpine based python image with reduced size
2. Non-root user with no shell access and no home directory
3. Separate layer for `requirements.txt` which helps to avoid dependencies installation when no changes were made 
4. Listen host and port are parametrized with default value and might be changed via environmental variables
5. Argument list is used for the CMD instead of the plain string command
6. `EXPOSE` directive is used to point that application is listening on particular port