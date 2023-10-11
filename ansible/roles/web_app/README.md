# Web App Role

## Description

This Web App role exposes ports and launches the web app in a Docker container.
An app's Docker image, container name, and exposed port can all be specified by the user.
Also, the role provides ability to wipe. User can stop and remove the container of the app.
The role can work in 2 modes: container mode and docker compose mode. The second is set by default.

Use the tag 'web_app_wipe' in docker compose mode or 'web_app_wipe_container' in container mode while executing a playbook to stop and remove the container, and set the variable 'web_app_full_wipe: true'