# Best CI Practices 

1. Usage of secrets.
    - In order to retrieve sensitive information I use github secrets, which allows me to safely interact with Docker and Snyk api.

2. Usage of dependend jobs.
    - Before building and pushing docker container, the process will need to wait until the security check and lint and test checks are completed. 

3. Security Check.
    - I implemented a security check using Snyk.

4. Caching Mechanism.
    - In order to increase the speed of installations I have implement ```actions/setup-python``` action used to cache all the necessary ependencies. 