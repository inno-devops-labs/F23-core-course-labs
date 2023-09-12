Image: https://hub.docker.com/r/kinjalik/devops-course-app

1. No root, so even if for some reason the container used with --priveleged, it won't be exploited
2. Low layers with dependency management to avoid production of unnecessary layers when deps are unchanged
3. Minimized number of layers - so minimal memory used
4. Removed pip cache in order not to pollute the image
5. Reduced image size because of Alpine - one of the smallest distros for docker images
6. Exact version of base image is used - no unexpected behavior because of version bump