# Helm library for labels

## Description

This Helm library provides common labels for web servers

## How it works

- Import this library in *Chart.yaml*:

    ```yaml
    dependencies:
      - name: library-chart
        version: 1.0.0
        repository: file://../library-chart
    ```
- Update dependencies in your helm chart:
   ```shell
   helm dependency update app-python/
   helm dependency update app-js/
   ```
   ```text
   Saving 1 charts
   Deleting outdated charts
   Saving 1 charts
   Deleting outdated charts
   ```