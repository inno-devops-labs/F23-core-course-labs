# k8s

**Creating minikube cluster**

```
minikube start
```

**Creating deployment**

```
kubectl create deployment web-app-node --image=docker.io/elatypovinno/devops_inno:latest
```

**Creating service**

```
kubectl expose deployment web-app-node --type=LoadBalancer --port=8080
```

**Running service**

```
minikube service web-app-node
```

---

After the application successfully deployed, I run following command:

```
kubectl get pods,svc
```

And the output is:

```
NAME                               READY   STATUS    RESTARTS   AGE
pod/web-app-node-77c9d4f58-6lg28   1/1     Running   0          107s

NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes     ClusterIP      10.96.0.1       <none>        443/TCP          25m
service/web-app-node   LoadBalancer   10.111.211.46   <pending>     8080:32569/TCP   102s
```

---

To delete service and deployment, run:

```
kubectl delete service web-app-node
kubectl delete deployment web-app-node
```