## Helm

### kubectl get pods,svc

```shell

NAME                                    READY   STATUS    RESTARTS   AGE
pod/helm-app-1667842-7998cc6799-m8svb   1/1     Running   0          2m6s

NAME                          TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/helm-app-1667842    ClusterIP      10.109.136.225   <pending>     5000/TCP         15m
service/kubernetes          ClusterIP      10.96.0.1        <none>        443/TCP          137m
```

### minikube service --all

```shell

|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------------|-------------|--------------|
| NAMESPACE |      NAME        | TARGET PORT |     URL      |
|-----------|------------------|-------------|--------------|
| default   | helm-app-1667842 |             | No node port |
|-----------|------------------|-------------|--------------|
😿  service default/helm-app-1667842 has no node port
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service helm-app-1667842.
|-----------|------------------|-------------|------------------------|
| NAMESPACE |      NAME        | TARGET PORT |          URL           |
|-----------|------------------|-------------|------------------------|
| default   | kubernetes       |             | http://127.0.0.1:59661 |
| default   | helm-app-1667842 |             | http://127.0.0.1:59665 |
|-----------|------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/helm-app-1667842 in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
^C✋  Stopping tunnel for service helm-app-1667842.
✋  Stopped tunnel for service kubernetes.

```

### screenshots

![](/k8s/screenshots/image.png)

### helm lint

```bash
helm lint helm-app
==> Linting helm-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

### helm install --dry-run helm-hooks

```bash
helm install nginx helm-app
NAME: helm-app
LAST DEPLOYED: Wed Nov  1 18:56:38 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=helm-app,app.kubernetes.io/instance=helm-app" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

### kubectl get po

```bash
kubectl get po
NAME                                 READY   STATUS      RESTARTS   AGE
helm-app-1667842-7998cc6799-m8svb    1/1     Running     0          33s
postinstall-hook                     0/1     Completed   0          33s
preinstall-hook                      0/1     Completed   0          63s

```

### delete policy

As a hook delete policy `"helm.sh/hook-delete-policy": hook-succeeded` was used
