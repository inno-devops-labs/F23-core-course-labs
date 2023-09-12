
## Best Practice:

+ Used `COPY` instead of `ADD`
+ Created non-rooted user
+ Not user `latest` tag for image which pulled. Latest tag is unpredictable
+ User alpine linux distro, it's lightweight and security-oriented
+ Created `.dockerignore` to reduce image size 
+ Added multi-stage 