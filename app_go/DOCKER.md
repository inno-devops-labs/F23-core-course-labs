## Implemented best practices

1. Multi stage build is used
2. Lightweight golang alpine image is used for building the application
3. Empty base image was used for the release (`FROM scratch`)
4. Non-root user with no shell access and no home directory
5. `EXPOSE` directive is used to point that application is listening on particular port
6.  Separate layers for copying `go.mod`, `go.sum` and installing dependencies which helps to avoid unnecesarry packages downloading when no changes were made 
7. Listen host and port are parametrized with default value and might be changed via environmental variables
8. Argument list is used for the CMD instead of the plain string command
9. `EXPOSE` directive is used to point that application is listening on particular port
10. Release configuration for the Gin framework is set via environmental variable by default
