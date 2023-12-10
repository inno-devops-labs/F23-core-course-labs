# Best practices

## Secret management
All sensitive data are stored in github repo secrets
## Caching
Cache python dependencies to reduce pipeline time
## Verify vulnerabilites
Used snyk in order to check for dangerous dependencies and eliminate them (I have several for example)
## Responsibility management
Job are splitted into 2 parts by responsiblity - test and then build
## Testing
All code are tested and if it fails pipeline will be stopped
