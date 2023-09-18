## Implemented best practices
1. The Pytest testing tool was used.
2. GitHub secrets were used to store sensitive data, such as credentials for Dockerhub.
3. Caching of pip dependencies was implemented to improve building time.
4. The `timeout-minutes` parameter was used to limit the pipeline execution time.
5. The Matrix OS test strategy was employed to ensure that the tests pass in all environments used on production servers.
6. The linting job was separated from the testing job since it only requires access to the source code and not execution. Additionally, invoking the linter for each OS would be redundant, considering the tests are running on multiple OS.
7. Parallel execution was implemented. Linting and testing are performed simultaneously, while building and pushing the container to the container registry depends on the results of previous job execution. Furthermore, tests on various OS are executed in parallel.
8. Action triggers were limited. The pipelines are executed only on push and pull_request events. By eliminating unnecessary pipelines, we can optimize runner usage quota.
9. Three-octet versions were used for referencing external GitHub actions. This approach is more human-readable than using the commit hash, and it helps avoid pipeline faults due to unexpected breaking changes in new action versions.
10. The default directory directive was used to reference code from the subdirectory relatively, without the need to prefix the subdirectory or use the cd command to navigate into it.