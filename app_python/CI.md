## CI best Practices
1. Github action trigering: The workflow initiates in response to 'push' events occurring within the repository. Utilizing the 'paths' attribute, the workflow is specifically instructed to activate only when changes are pushed to the CI configuration file ('.github/workflows/app_python.yaml') or any files except *.md within the 'app_python/'  directory.
2. Snyk Security Check Job: This particular job is dedicated to enhancing security by conducting a thorough examination of potential vulnerabilities within the Python dependencies.
3. Handling Secrets: GitHub's secret storage is employed for the secure management of confidential information.
4. Cashing
5. Defaults Configuration: It establishes 'bash' as the default shell and promote consistency throughout the execution of various steps.
