# Helm library for labels

## Description

This Helm library provides common labels for both applications: **App python** and **App golang**.

## How it works

1. Import this library in your helm chart by adding `dependencies` in *Chart.yaml* file:

    ```yaml
    dependencies:
      - name: library-chart
        version: 1.0.0
        repository: file://../library-chart
    ```

1. Update dependencies in your helm chart:

   ```shell
   helm dependency update app-python/
   helm dependency update app-golang/
   ```
   ```text
   Saving 1 charts
   Deleting outdated charts
   Saving 1 charts
   Deleting outdated charts
   ```

1. Change labels in `templates/deployment.yaml` file to:

   ```text
   {{- include "library-chart.labels" . | indent 4 }}
   ```
