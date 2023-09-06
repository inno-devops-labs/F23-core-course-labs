## Practices I used for dockerizing this application:
    - caching is turned of for pip dependencies (recommendation for python images)
    - container is rootless
    - Container uses the image of python v3.11.5 based on alpine(security-oriented and lightweight Linux distribution)
    - Container exposes only the port that is used by application
    - ADD instructions are avoided
    - image is built based on necessary context (i.e. only /src directory and requirements.txt are copied inside container)
    - dependencies being installed before source code is being copied (layer sanity is followed)
    - metadata label is added for better image management
    - `hadolint` linter was used for analyzing Dockerfile