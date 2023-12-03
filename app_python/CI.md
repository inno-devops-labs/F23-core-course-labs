# CI Best Practises

- **Defaults Section**:

    The 'defaults' section sets up common configurations for all jobs in the workflow.
    It specifies the default shell as 'bash' and sets the working directory to 'app_python,' ensuring consistency across all steps.

- **Workflow Triggers**:

    The workflow is triggered on 'push' events to the repository.
    The 'paths' attribute specifies that the workflow should only run when changes are pushed to the CI file itself ('.github/workflows/python_ci.yml') or any files in the 'app_python/' directory. This minimizes unnecessary runs of the CI pipeline.

- **Snyk Job**:

    This job focuses on security by checking for vulnerabilities in the Python dependencies.

- **Secrets**:

    Secrets are stored in GitHub's secret storage.

- **First Build then Deploy**:

    The Deploy job depends on Build job, so we can't push untested and bad artifact to DockerHub.