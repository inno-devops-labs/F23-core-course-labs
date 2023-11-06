```
r-shakirova-osx:core-course-labs r-shakirova$ kubectl get pods
NAME                         READY   STATUS    RESTARTS   AGE
python-web-app-6f5d8cfdcf-sx47n   1/1     Running   0          3m11s

r-shakirova-osx:core-course-labs r-shakirova$ kubectl get svc
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          17m
python-web-app   LoadBalancer   10.111.15.11    <pending>     8080:32399/TCP   78s
```

```
r-shakirova-osx:k8s r-shakirova$ kubectl delete deployment python-web-app
deployment.apps "python-web-app" deleted
```

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
|-----------|------------|-------------|
|-----------|---------------|-------------|---------------------------|
| NAMESPACE |     NAME      | TARGET PORT |            URL            |
|-----------|---------------|-------------|---------------------------|
| default   | python-web-app |        8080 | http://192.168.49.2:32505 |
|-----------|---------------|-------------|---------------------------|
🎉  Opening service default/python-web-app in default browser...
r-shakirova-osx:k8s r-shakirova$ MESA-INTEL: warning: Performance support disabled, consider sysctl dev.i915.perf_stream_paranoid=0
Opening in existing browser session.
MESA-INTEL: warning: Performance support disabled, consider sysctl dev.i915.perf_stream_paranoid=0
Opening in existing browser session.
MESA-INTEL: warning: Performance support disabled, consider sysctl dev.i915.perf_stream_paranoid=0
MESA-INTEL: warning: Performance support disabled, consider sysctl dev.i915.perf_stream_paranoid=0
```
