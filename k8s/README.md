# Output

- ```kubectl get pods```
  ```
    NAME                   READY   STATUS        RESTARTS   AGE  
    app-86d97686c9-62w2j   1/1     Running       0          18m
    app-86d97686c9-b7xgk   1/1     Running       0          18m
    app-86d97686c9-8cn4k   1/1     Running       0          18m
   ```
- ```kubectl get svc```
  ```
    NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
    app          ClusterIP   10.103.32.62   <none>        8080/TCP   11s
    kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP    8m14s
  ```
- ```minikube service --all```
  ```
    |-----------|------------|-------------|------------------------|
    | NAMESPACE |    NAME    | TARGET PORT |          URL           |
    |-----------|------------|-------------|------------------------|
    | default   | app        |             | http://127.0.0.1:53723 |
    | default   | kubernetes |             | http://127.0.0.1:53725 |
    |-----------|------------|-------------|------------------------|
  ```
  
# Screenshots

![screenshot](img.png)
![screenshot](img_1.png)

