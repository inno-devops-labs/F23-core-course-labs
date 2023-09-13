# Containerization Lab

> In this .md file, I describe how I crafted the dockerfile, what best practices I used. How did I build and test an image. How did I push and pull an image, verifying and validating its functionality. 

## Docker application ( `Quick Guide` )
 
 > You can find my image on dockerhub, the link is clickable -  [my-node-app](https://hub.docker.com/layers/m4k4rich/my-node-app/dev/images/sha256:ae865650ef996ee89da47f6bda8182234f62f24a43d4210e96e0a2fd9db4af51)

 1. **How to build?** 
 
     - Clone a repository.
     - Change directory to app_python.
     - Run ```docker build -t registry/name/tag .```

 2. **How to pull?**

    - Login in your dockerhub account.
    - Run ```docker pull m4k4rich/my-node-app/dev```

 3. **How to run?**

    - Pull or build an image first.
    - Run ```docker run -p PORT:8080 m4k4rich/my-node-app/dev``` instead of `PORT` specify which port you want to use**
