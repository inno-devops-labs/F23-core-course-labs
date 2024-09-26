# Lab 7: Monitoring and Logging

## Task 1: Logging Stack Setup

**6 Points:**

In this lab, you will become familiar with a logging stack that includes Promtail, Loki, and Grafana. Your goal is to create a Docker Compose configuration and configuration files to set up this logging stack.

1. Study the Logging Stack:
   - Begin by researching the components of the logging stack:
     - [Grafana Webinar: Loki Getting Started](https://grafana.com/go/webinar/loki-getting-started/)
     - [Loki Overview](https://grafana.com/docs/loki/latest/overview/)
     - [Loki GitHub Repository](https://github.com/grafana/loki)

2. Create a Monitoring Folder:
   - Start by creating a new folder named `monitoring` in your project directory.

3. Docker Compose Configuration:
   - Inside the `monitoring` folder, prepare a `docker-compose.yml` file that defines the entire logging stack along with your application.
   - To assist you in this task, refer to these resources for sample Docker Compose configurations:
     - [Example Docker Compose Configuration from Loki Repository](https://github.com/grafana/loki/blob/main/production/docker-compose.yaml)
     - [Promtail Configuration Example](https://github.com/black-rosary/loki-nginx/blob/master/promtail/promtail.yml) (Adapt it as needed)

4. Testing:
   - Verify that the configured logging stack and your application work as expected.

## Task 2: Documentation and Reporting

**6 Points:**

1. Logging Stack Report:
   - Create a new file named `LOGGING.md` to document how the logging stack you've set up functions.
   - Provide detailed explanations of each component's role within the stack.

2. Screenshots:
   - Capture screenshots that demonstrate the successful operation of your logging stack.
   - Include these screenshots in your `LOGGING.md` report for reference.

3. Pull Request to Forked Repository:
   - Initiate a Pull Request (PR) to the main branch of the forked repository.
   - Request that your teammates review this PR, and also review PRs from your teammates.

4. Pull Request in Your Repository:
   - Create a PR in your own repository from the lab7 branch to the main branch.
   - This step is essential for grading and tracking your work.

## Bonus

**2.5 Points:**

1. Integrating Your Extra App:
   - Extend the `docker-compose.yml` configuration to include your additional application.

2. Configure Stack for Comprehensive Logging:
   - Modify the logging stack's configuration to collect logs from all containers defined in the `docker-compose.yml`.
   - Include screenshots in your `LOGGING.md` report to demonstrate your success.

**Guidelines:**

- Ensure that your documentation in `LOGGING.md` is well-structured and comprehensible.
- Follow proper naming conventions for files and folders.
- Use code blocks and Markdown formatting where appropriate.
- Participate actively in the peer review process by submitting and reviewing PRs.
- When creating the PR in your repository, make it from the lab4 branch to the lab3 branch.

> Note: Thoroughly document your work, and ensure the logging stack functions correctly. Utilize the bonus points opportunity to enhance your understanding and the completeness of your setup.
