# Best practices for CI workflows that I implemented

## 1. Path filters:
The workflow is triggered only when there are changes in the app_js directory. This ensures that the CI process runs only when relevant files are modified, saving resources.
## 2. Multiple triggers:
The workflow is triggered on push, pull_request, and manual workflow_dispatch events. This ensures that code is tested both before merging (pull requests) and after merging (push), and can also be manually triggered if needed.
## 3. Use of official actions:
Official actions like actions/checkout and actions/setup-node are used. These are maintained by the GitHub community and are generally more secure and up-to-date.
## 4. Explicit Node.js version:
The Node.js version is explicitly set to version '14'. This ensures consistency across runs and avoids potential issues with future Node.js versions.
## 5. Separate steps for different tasks:
Each task is a separate step. This makes the workflow easy to read and debug.
## 6. Working directory:
The working-directory attribute is used to specify where commands should be run. This ensures that commands are executed in the correct context.
## 7. Secure handling of secrets:
DockerHub credentials are stored as GitHub secrets and are referenced in the workflow. This keeps sensitive information secure and not hard-coded in the workflow.
## 8. Docker image tagging:
The Docker image is tagged with a specific name (latest-js). This makes it easy to identify and pull the image for deployments or further testing.
