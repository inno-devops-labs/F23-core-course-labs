# Continuous Integration (CI) Workflow 

## Workflow Structure

The workflow is triggered on pushes to specific branches (e.g., `lab1`, `lab2`, `lab3`) and pull requests to the `main` branch.

### Key Steps in the Workflow
    - **Checkout code**
    - **Cashe dependencies**
    - **Set up Python**
    - **Install dependencies** 
    - **Lint code** 
    - **Run tests**
    - **Login to Docker Hub**
    - **Build and push Docker image**

## Optimization and Caching
- Casheing is used to store Python dependencies between workflow runs to speed up builds.
