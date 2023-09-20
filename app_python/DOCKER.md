## Docker Best Practices Applied

----------------------------------------------------

- **Slim base image:** The base image used is python:3.10-slim, which reduces the size of the final Docker image.  
- **Creating a Low-Privilege User:** New user 'myuser' created with the '-m' option to create a home directory for the user.  
- **Setting a Working Directory:** The 'WORKDIR' instruction is used to set the working directory within the container to '/app'.  
- **Copying Requirements Separately:** mreqfdocker.txt file (minimalistic requirements for app) is copied from the rest of the application files and installed dependencies before copying the remaining files.  
- **Using a .dockerignore file:** Created .dockerignore file, which consists patterns of files and directories that should be excluded when building the Docker image.  
- **Copying Application Files:** All the application files are copied into the container using 'COPY . /app'  
- **Changing Ownership:** Using 'chown' changed the ownership of the copied files to the 'myuser' user.  
- **Switching to the New User:** The 'USER' instruction is used to switch to the 'myuser' user before running the application.  
- **CMD instruction:** The 'CMD' instruction is used to specify default command to run when the container starts.  

