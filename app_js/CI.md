# Best implemented CI workflow practices

## Dependency management

Before running both tests or linting, I ensure that all required dependencies are installed. It both allows to change dependencies if we run only one of jobs and guarantees consistent results.

## Separate jobs

I've separated the CI process into distinct jobs: linting, testing, Docker-related tasks, and snyk checks. It shows which specific process exact might fail and makes logs and outputs more organized and easier to debug.

## Caching

By caching dependencies, I avoid redundant downloads and installations, reducing the overall time of the CI process.

## Docker integration

My CI workflow includes steps to build a Docker image of our application and push it to DockerHub. This ensures that my application is always available as a solution ready for deployment.

## Workflow status badge

Adding a workflow status badge to the README provides visibility into the CI process's status. It's a quick way to determine if the latest commit or pull request passed all CI checks.

## Vulnerability checks

I've integrated Snyk into CI workflow to check for vulnerabilities in my dependencies for security.

## Path filters

The workflow is triggered only when there are changes in the app_python directory. This ensures that the CI process runs only when relevant files are modified, saving resources.

## Working directory

The working-directory attribute is used to specify where commands should be run to ensure that commands are executed in the correct context.
