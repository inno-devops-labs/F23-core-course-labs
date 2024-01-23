# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy all of the application files to the container
COPY . /app

# Create user and set ownership and permissions as required
RUN adduser myuser -D && chown -R myuser /app 

# Pick the running user
USER myuser

# Expose the port on which your Node.js app will run
EXPOSE 3000

# Start the Node.js application
CMD ["node", "app.js"]
