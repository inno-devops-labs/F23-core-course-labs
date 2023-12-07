FROM nginx:alpine
    
WORKDIR /usr/share/nginx/html

COPY index.html .

EXPOSE 80

# On the nginx base we can not run as non user (I tried a lot, really)
CMD ["nginx", "-g", "daemon off;"]