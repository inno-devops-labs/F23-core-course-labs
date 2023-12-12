```
r-shakirova-osx:core-course-labs r-shakirova$ kubectl get pods
NAME                         READY   STATUS    RESTARTS   AGE
python-web-app-6f5d8cfdcf-sx47n   1/1     Running   0          3m11s

r-shakirova-osx:core-course-labs r-shakirova$ kubectl get svc
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          17m
python-web-app   LoadBalancer   10.111.15.11    <pending>     8000:31685/TCP   78s
```

```
r-shakirova-osx:k8s r-shakirova$ kubectl delete deployment python-web-app
deployment.apps "python-web-app" deleted
```

Applying deployment and service manifests
```
r-shakirova-osx:k8s r-shakirova$ kubectl apply -f deployment.yaml
deployment.apps/python-web-app created
r-shakirova-osx:k8s r-shakirova$ kubectl apply -f service.yml
service/python-web-app created
```


```
r-shakirova-osx:k8s r-shakirova$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | python-web-app |        8000 | http://192.168.49.2:31685 |
|-----------|----------------|-------------|---------------------------|
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service python-web-app.
|-----------|----------------|-------------|------------------------|
| NAMESPACE |      NAME      | TARGET PORT |          URL           |
|-----------|----------------|-------------|------------------------|
| default   | kubernetes     |             | http://127.0.0.1:63915 |
| default   | python-web-app |             | http://127.0.0.1:63925 |
|-----------|----------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/python-web-app in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```
 ![browser](Screenshot.png)
