# Best practices

- No root user inside 
  ```
  RUN useradd -ms /bin/bash myuser
  USER myuser
  ```
- No bind to a specific UID
  ```
  RUN mkdir /myuser-dir && chown -R myuser /myuser-dir
  RUN chown -R myuser /myuser-dir
  ```
- Exposed ports
    ```
    EXPOSE 5000
    ```
- Usage of copy instead of add
    ```
  COPY requirements.txt .
  
    ...
  
    COPY . .
    ```
