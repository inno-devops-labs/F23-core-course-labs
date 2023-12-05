```bash
➜ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-6f6bd85f9-xd7ph   1/1     Running   0          11m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
service/app-python   LoadBalancer   10.108.229.12   10.108.229.12   80:31829/TCP   3m22s
service/kubernetes   ClusterIP      10.96.0.1       <none>          443/TCP        16m
```

## Manifests:
```bash
➜ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-6f6bd85f9-2hjx4   1/1     Running   0          28s
pod/app-python-6f6bd85f9-n5svf   1/1     Running   0          28s
pod/app-python-6f6bd85f9-q87zf   1/1     Running   0          28s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
service/app-python   LoadBalancer   10.108.229.12   10.108.229.12   80:31829/TCP   22s
service/kubernetes   ClusterIP      10.96.0.1       <none>          443/TCP        29m
```

```bash
➜ minikube service --all
|-----------|------------|-------------|----------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL             |
|-----------|------------|-------------|----------------------------|
| default   | app-python |          80 | http://192.168.105.2:31829 |
|-----------|------------|-------------|----------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app-python in default browser...
```
<img width="1872" alt="image" src="https://github.com/sl1depengwyn/core-course-labs/assets/53992153/987baeb4-7fd4-443b-bf64-03db6df53b0e">

## Ingress:
```bash
➜ curl --resolve "python.app:80:$( minikube ip )" -i http://python.app

HTTP/1.1 200 OK
Date: Tue, 31 Oct 2023 21:38:27 GMT
Content-Type: application/json
Content-Length: 34
Connection: keep-alive

"2023-11-01T00:38:27.336980+03:00"%

➜ curl --resolve "elixir.app:80:$( minikube ip )" -i http://elixir.app

HTTP/1.1 200 OK
Date: Tue, 31 Oct 2023 21:38:39 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 195
Connection: keep-alive
cache-control: max-age=0, private, must-revalidate
x-request-id: bc379c38601f5bf05b1a5840ddd1d0df

  <p>Ect/UTC time is 2023-10-31 21:38:39.254451Z</p>
  <p>To know your time reload the page</p>
  <script>document.cookie = "timezone="+Intl.DateTimeFormat().resolvedOptions().timeZone;</script>
```
