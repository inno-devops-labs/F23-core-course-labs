# Use a specific version of node, here we are using v14
FROM node:14-slim

# Expose the port the app runs on
EXPOSE 3000

# Create app directory to hold the application code inside the image.
WORKDIR /app

# Copy the package.json (and package-lock.json if available) file first for better caching.
COPY package*.json ./

# Install app dependencies.
# A wildcard is used to ensure both package.json AND package-lock.json are copied.
RUN npm install

# Create a non-root user and switch to it.
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

# Bundle app source inside the docker image.
COPY . .

# Add a health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:3000/ || exit 1

# Define the command to run the app
CMD [ "npm", "start" ]
