# CI/CD Best Practices
1. Caching of Gradle - we reuse Gradle's deps and drastically increase build speed
2. Caching of Konan (Kotin Native compiler) - we reus binary used by Konan and also increase build speed
3. Caching of Docker - I use :buildcache-python tag for that
4. Security check using Snyk
5. Linter produces retty output right into GitHub interface
6. Repor of unit tests is loaded into GitHub and pretty good shows what's going wrong if going
7. CI triggers only if specifc files are changed
8. Secrets are stored in Github's secrets storage
9. First test - then build