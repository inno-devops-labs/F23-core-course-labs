# Helm charts

## App python

1. **Create helm chart**

    ```shell
    helm create app-python
    ```
    
    Then change image in `values.yaml` file to download image of the app_python application.
    Change service parameters and enable ingress.

1. **Install Helm chart**

    ```shell
    helm install python app-python/
    ```
    ```text
    NAME: python
    LAST DEPLOYED: Sat Nov  4 16:01:48 2023
    NAMESPACE: default
    STATUS: deployed
    REVISION: 1
    NOTES:
    1. Get the application URL by running these commands:
      http://app-python/
    ```
   
1. **Check service availability**

    ```shell
    kubectl get pods,svc
    ```
    ```text
    NAME                                    READY   STATUS    RESTARTS   AGE
    pod/python-app-python-ff6f5c776-bx8pl   1/1     Running   0          2m35s
    pod/python-app-python-ff6f5c776-dk68b   1/1     Running   0          2m35s
    pod/python-app-python-ff6f5c776-zf6rc   1/1     Running   0          2m35s
    
    NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    service/kubernetes          ClusterIP      10.96.0.1       <none>        443/TCP          13d
    service/python-app-python   LoadBalancer   10.99.167.222   <pending>     8000:30650/TCP   2m35s
    ```
    
    And check service from minikube: `minikube service python-app-python`
    
    ```text
    |-----------|-------------------|-------------|---------------------------|
    | NAMESPACE |       NAME        | TARGET PORT |            URL            |
    |-----------|-------------------|-------------|---------------------------|
    | default   | python-app-python | http/8000   | http://192.168.49.2:30650 |
    |-----------|-------------------|-------------|---------------------------|
    🎉  Opening service default/python-app-python in default browser...
    ```
   
## Minikube dashboard

### App Python

![Dashboard with Python application](./images/helm_k8s_dashboard_python.png)