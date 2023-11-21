
## Task 1: Kubernetes Setup and Basic Deployment
1. Learn about Kubernetes: done

2. Install kubernetes Tools: done

3. Deploy your application:

+ Deploy the application using `kubectl create` command:
```bash
    kubectl create deployment python-app --image=docker.io/ar7ch/devops-app-python
```

4. Access your application:

```bash
    kubectl expose deployment python-app --type=LoadBalancer --port=80
    minikube service python-app
```

5. Create a Kubernetes Folder: done
Command output:
```bash
    $ kubectl get pods,svc
    NAME                             READY   STATUS    RESTARTS   AGE
    pod/python-app-5d844c9bd-lwzvq   1/1     Running   0          14m

    NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
    service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP        111m
    service/python-app   LoadBalancer   10.111.2.135   <pending>     80:31901/TCP   93m
```

6. Cleanup:

```bash
kubectl delete service python-app
kubectl delete deployment python-app
```


## Task 2: Declarative Kubernetes Manifests

```bash
    kubectl apply -f deployment-python.yml
    kubectl apply -f service-python.yml
```

```bash
$ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-95b6b597c-2xjtt   1/1     Running   0          8m2s
pod/app-python-95b6b597c-kxhwg   1/1     Running   0          8m2s
pod/app-python-95b6b597c-pscg9   1/1     Running   0          8m2s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/app-python   LoadBalancer   10.102.193.243   <pending>     80:30080/TCP   7m59s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        10h
```
