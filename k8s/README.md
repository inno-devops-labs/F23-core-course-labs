# Kubernetes

## Basic deployment

1. Let's create deployment for the applications:

    ```shell
    kubectl create deployment app-python --image=yesliesnayder/app_python:1.0.5
    kubectl create deployment app-golang --image=yesliesnayder/webservicego:1.0.0
    kubectl get deployments
    ```
    ```text
    deployment.apps/app-python created
    deployment.apps/app-golang created
    NAME         READY   UP-TO-DATE   AVAILABLE   AGE
    app-golang   1/1     1            1           13s
    app-python   1/1     1            1           83s
    ```

1. Expose the Pods to the public internet using the `kubectl expose` command.
It will create new services to access the applications:

    ```shell
    kubectl expose deployment app-python --type=LoadBalancer --port=8000
    kubectl expose deployment app-golang --type=LoadBalancer --port=8000
    ```
    ```text
    service/app-python exposed
    service/app-golang exposed
    ```

1. Show running pods and services:

    ```shell
    kubectl get pods,svc
    ```
    ```text
    NAME                              READY   STATUS    RESTARTS   AGE
    pod/app-golang-57b7596b46-kjrnh   1/1     Running   0          9m30s
    pod/app-python-868f94d4c-gwx87    1/1     Running   0          10m
    
    NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
    service/app-golang   LoadBalancer   10.98.139.103    <pending>     8000:32668/TCP   5m43s
    service/app-python   LoadBalancer   10.104.142.180   <pending>     8000:30793/TCP   5m48s
    service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          24m
    ```
   
    The following command opens up a browser window that serves all running applications and shows their response:
    ```shell
    minikube service --all
    ```
    ```text
    |-----------|------------|-------------|---------------------------|
    | NAMESPACE |    NAME    | TARGET PORT |            URL            |
    |-----------|------------|-------------|---------------------------|
    | default   | app-golang |        8000 | http://192.168.49.2:32668 |
    |-----------|------------|-------------|---------------------------|
    |-----------|------------|-------------|---------------------------|
    | NAMESPACE |    NAME    | TARGET PORT |            URL            |
    |-----------|------------|-------------|---------------------------|
    | default   | app-python |        8000 | http://192.168.49.2:30793 |
    |-----------|------------|-------------|---------------------------|
    |-----------|------------|-------------|--------------|
    | NAMESPACE |    NAME    | TARGET PORT |     URL      |
    |-----------|------------|-------------|--------------|
    | default   | kubernetes |             | No node port |
    |-----------|------------|-------------|--------------|
    😿  service default/kubernetes has no node port
    🎉  Opening service default/app-golang in default browser...
    🎉  Opening service default/app-python in default browser...
    ```
    ![Running Services](./images/running_services.png)

1. Cleanup:

    ```shell
    kubectl delete svc app-python app-golang
    kubectl delete deployment app-python app-golang
    ```