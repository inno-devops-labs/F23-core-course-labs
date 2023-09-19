# CI Best Practices

## Job Organization

The workflow is organized into multiple jobs based on their responsibilities.

## Secret Management

Sensitive information is managed securely using GitHub's Secrets feature.

## Don’t install dependencies unnecessarily

I used Snyk in build stage to reduce dependencies installations.

## Utilize build cache

I utilize build cache to reuse it.