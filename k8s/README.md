# Kubernetes Configuration for MyApplication

This repository contains the Kubernetes deployment configuration for MyApplication. The configuration is designed to be used with [Minikube](https://minikube.sigs.k8s.io/docs/) for development and testing purposes.

## Prerequisites

Before you begin, ensure you have the following installed:
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/), the Kubernetes command-line tool
- [Minikube](https://minikube.sigs.k8s.io/docs/start/), a tool that lets you run Kubernetes locally
- [Docker](https://docs.docker.com/get-docker/), as Minikube will use Docker to build and manage images

## Directory Structure

/k8s
|-- /dev
|   |-- deployment.yaml
|   |-- service.yaml
|-- README.md

The `k8s` directory contains subdirectories for different deployment environments, each with their own configuration files.

## Getting Started

1. **Start Minikube**:
   To start your Minikube cluster, use the following command:
   ```bash
   minikube start
   ```

2. **Apply Kubernetes Configurations**:
   To apply the configurations to your cluster, use the `kubectl apply` command. You should specify the environment you wish to deploy to:

   For development:
   ```bash
   kubectl apply -f k8s/dev/
   ```

3. **Accessing the Application**:
   Once the services are deployed, you can use the following command to get the URL of the application if you are using a `NodePort` service:
   ```bash
   minikube service <service-name> --url
   ```

## Output for: "kubectl get pods,svc"

```bash
NAME                                     READY   STATUS    RESTARTS   AGE
pod/django-deployment-79997f7486-2mdsm   1/1     Running   0          4m59s
pod/django-deployment-79997f7486-7zlxw   1/1     Running   0          4m59s
pod/django-deployment-79997f7486-9fbl6   1/1     Running   0          4m59s

NAME                     TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/django-service   NodePort    10.103.56.237   <none>        5000:30001/TCP   4m50s
service/kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP          4d2h
```