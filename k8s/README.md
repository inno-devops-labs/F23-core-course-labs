# Kubernetes

Easiest way to set up all of this is to use [minikube](https://minikube.sigs.k8s.io/docs/start/).

How to start:
1. Download kubectl and minikube
2. Start minikube with `minikube start`
3. Deploy docker image `kubectf create deployment devops-time-app --image=stiveman1/app_python:v2`
4. Expose deployment with load balancer `kubectl expose deployment devops-time-app --type=LoadBalancer --port=8000`

```bash 
❯ kubectl get pods,svc
NAME                                   READY   STATUS              RESTARTS   AGE
pod/devops-time-app-76dc96dc7c-wqvlq   0/1     ContainerCreating   0          30s

NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/devops-time-app   LoadBalancer   10.108.203.98   <pending>     8000:31156/TCP   9s
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP          56s

```

## Automatization

For automatic start I've created deployment.yaml and service.yaml files. 

To apply changes you should run `kubectl apply -f k8s/deployment.yml` and `kubectl apply -f k8s/service.yml`


```bash
❯ kubectl get pods,svc

NAME                                   READY   STATUS             RESTARTS   AGE
pod/devops-time-app-76dc96dc7c-vm5h5   1/1     ImagePullBackOff   0          7m13s
pod/devops-time-app-sz49rb1y11-wqvlq   1/1     ImagePullBackOff   0          7m13s
pod/devops-time-app-qultayus65-3j85j   1/1     ImagePullBackOff   0          7m13s

NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/exposer           LoadBalancer   10.108.42.107   <pending>     80:30654/TCP     4m37s
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP          7m39s

```

```bash
❯ minikube service --all

|-----------|---------|-------------|-----------------------------|
| NAMESPACE |  NAME   | TARGET PORT |             URL             |
|-----------|---------|-------------|-----------------------------|
| default   | exposer |          80 | http://192.168.59.100:30654 |
|-----------|---------|-------------|-----------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|

😿  service default/kubernetes has no node port
🏃  Starting tunnel for service exposer.
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |           URL          |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:17886 |
| default   | exposer    |             | http://127.0.0.1:17875 |
|-----------|------------|-------------|------------------------|

```

## Definitions

Ingress - tool in Kubernetes that allow to control status of pods, balance load, control network and vm's.

Ingress controller - required part of cluster for Ingress to work. Cluster may have several Ingress contlollers, they helps to manage Ingress (allow to use different hosts or tools).

StatefulSet - is a variant of Deployment it allows unique pods and able to work with different application states on machienes in cluster.

DaemonSet - app that controls pods on each node. Afrer rescaling cluster helps to rearragne pods over the nodes in cluster.

PersistentVolumes - is like Docker volume, it store some information required for pods. It is important to remember that this is common storage over pods.


# Lab 11: Kubernetes Secrets and Hashicorp Vault

## Task 1: Kubernetes Secrets and Resource Management

**6 Points:**

In this lab, you will learn how to manage sensitive data, such as passwords, tokens, or keys, within Kubernetes. Additionally, you will configure CPU and memory limits for your application.

1. Create a Secret Using `kubectl`:
   - Learn about Kubernetes Secrets and create a secret using the `kubectl` command:
     - [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
     - [Managing Secrets with kubectl](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/#decoding-secret)

2. Verify and Decode Your Secret:
   - Confirm and decode the secret, then create an `11.md` file within the `k8s` folder. Provide the output of the necessary commands inside this file.

3. Manage Secrets with Helm:
   - Use Helm to manage your secrets.
   - Create a `secrets.yaml` file in the `templates` folder.
   - Define a `secret` object within this YAML file.
   - Add an `env` field to your `Deployment`. The path to update is: `spec.template.spec.containers.env`.

     > Refer to this [Helm Secrets Video](https://www.youtube.com/watch?v=hRSlKRvYe1A) for guidance.

   - Update your Helm deployment as instructed in the video.
   - Retrieve the list of pods using the command `kubectl get po`. Use the name of the pod as proof of your success within the report.
   - Verify your secret inside the pod, for example: `kubectl exec demo-5f898f5f4c-2gpnd -- printenv | grep MY_PASS`. Share this output in `11.md`.

4. Create a Pull Request:
   - Generate a PR to the main branch of the forked repository.

5. Create a Pull Request in Your Own Repository:
   - Create a PR in your repository from the lab11 branch to the main one. This will facilitate the grading process.

## Task 2: Vault Secret Management System

**4 Points:**

1. Install Vault Using Helm Chart:
   - Install Vault using a Helm chart. Follow the steps provided in this guide:
     - [Vault Installation Guide](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#install-the-vault-helm-chart)

2. Follow the Tutorial with Your Helm Chart:
   - Adapt the tutorial to work with your Helm chart, including the following steps:
     - [Set a Secret in Vault](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#set-a-secret-in-vault)
     - [Configure Kubernetes Authentication](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#configure-kubernetes-authentication)
     - Be cautious with the service account. If you used `helm create ...`, it will be created automatically. In the guide, they create it manually.
       - [Manually Define a Kubernetes Service Account](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#define-a-kubernetes-service-account)

3. Implement Vault Secrets in Your Helm Chart:
   - Use the steps from the guide as an example for your Helm chart:
     - [Update values.yaml](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#launch-an-application)
     - [Add Labels](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-sidecar#inject-secrets-into-the-pod)
   - Test to ensure your credentials are injected successfully. Use the `kubectl exec -it <your_app> -- bash` command to access the container. Verify the injected secrets using `cat /path/to/your/secret` and `df -h`. Share the output in the `11.md` report.
   - Apply a template as described in the guide. Test the updates as you did in the previous step and provide the outputs in `11.md`.

**List of Requirements:**

- Proof of work with a secret in `11.md` for the Task 1 - steps 2 and 3.
- `secrets.yaml` file.
- Resource requests and limits for CPU and memory.
- Vault configuration implemented, with proofs in `11.md`.

## Bonus

**2.5 Points:**

1. Read About Resource Management:
   - Familiarize yourself with resource management in Kubernetes:
     - [Resource Management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

2. Set Up Requests and Limits for CPU and Memory for Both Helm Charts:
   - Configure resource requests and limits for CPU and memory for your application.
   - Test to ensure these configurations work correctly.

3. Add Environment Variables for Your Containers for Both Helm Charts:
   - Read about Kubernetes environment variables:
     - [Kubernetes Environment Variables](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/)
   - Update your Helm chart with several environment variables using named templates. Move these variables to the `_helpers.tpl` file:
     - [Helm Named Templates](https://helm.sh/docs/chart_template_guide/named_templates/)

**Guidelines:**

- Ensure that your documentation is clear and organized.
- Include all the necessary components.
- Follow appropriate file and folder naming conventions.
- When creating the PR in your repository, make it from the `lab11` branch to the main branch.

> Note: Thorough documentation is essential to demonstrate your success in managing secrets and resource allocation in Kubernetes. Explore the bonus tasks to enhance your skills further.