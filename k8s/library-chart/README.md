# Helm labels library 

This Helm library provides labels for web servers

- Update dependencies in your helm chart:
    - app-python
        ```bash
        helm dependency update app-python/
        ```
        ```text
        Saving 1 charts
        Deleting outdated charts
        ```
    - app-js
        ```bash
        helm dependency update app-js/
        ```
        ```text
        Saving 1 charts
        Deleting outdated charts
        ```

- Import this library in *Chart.yaml*:

    ```yaml
    dependencies:
      - name: library-chart
        version: 1.0.0
        repository: file://../library-chart
    ```
