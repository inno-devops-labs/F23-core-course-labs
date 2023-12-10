## Docker good practices
1. Fix dependencies - to avoid problems with dependecies
2. No root user inside - a big issue for security
3. Least frequently changed layers on the top
4. Lightweight baseline - one of good docker practices is to keep the image as small as possible. To save memory usage as well as reduce the attack area.
5. Used https://hadolint.github.io/hadolint/ to check quality of Dockerfile
