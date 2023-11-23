# My Django App Helm Chart

This Helm chart deploys My Django App to a Kubernetes cluster with the necessary resources, such as Deployments, Services, and optional Ingress.

## Pre-Install and Post-Install Hooks

This chart includes both a `pre-install` and `post-install` hook. These hooks are Kubernetes pods that perform simple operations before and after the main helm install operation.

### Pre-Install Hook

The pre-install hook executes a pod that sleeps for 20 seconds before the main install begins. This is a placeholder for where you could potentially run any pre-install scripts or checks.

#### Configuration:

- **Name:** `${RELEASE_NAME}-pre-install-hook`
- **Image:** `busybox`
- **Command:** `sleep 20`

### Post-Install Hook

The post-install hook executes a pod that sleeps for 20 seconds after the install has completed. This is where you can run any post-installation setup or checks.

#### Configuration:

- **Name:** `${RELEASE_NAME}-post-install-hook`
- **Image:** `busybox`
- **Command:** `sleep 20`

### Hook Delete Policy

Both hooks are configured with a `hook-succeeded` delete policy, which means that the hooks will be automatically deleted after they run successfully.

## Usage

To install this chart, use the following command:

```bash
helm install [RELEASE_NAME] [CHART_PATH]
```

Replace `[RELEASE_NAME]` with the release name you want to use for your deployment, and `[CHART_PATH]` with the path to the chart directory.

## Configuration

You can customize the installation by modifying the `values.yaml` file or by using the `--set` flag with the helm install command.

For example, to change the number of replicas for the Django app, you could use:

```bash
helm install [RELEASE_NAME] [CHART_PATH] --set replicaCount=3
```

## Uninstalling the Chart

To uninstall/delete the deployment:

```bash
helm delete [RELEASE_NAME]
```

This command removes all the Kubernetes components associated with the chart and deletes the release.

## Exercise outputs

### Hook description ouput

```bash
kubectl get po
NAME                                     READY   STATUS      RESTARTS        AGE
django-deployment-79997f7486-2mdsm       1/1     Running     4 (3h29m ago)   4d2h
django-deployment-79997f7486-7zlxw       1/1     Running     4 (3h29m ago)   4d2h
django-deployment-79997f7486-9fbl6       1/1     Running     4 (3h29m ago)   4d2h
my-django-app-release-867d97dd8f-b6cdw   1/1     Running     0               86s
my-django-app-release-post-install       0/1     Completed   0               86s
my-django-app-release-pre-install        0/1     Completed   0               109s
```

<br>

```bash
kubectl describe po my-django-app-release-post-install
Name:             my-django-app-release-post-install
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.67.2
Start Time:       Thu, 09 Nov 2023 17:42:46 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-weight: 1
Status:           Succeeded
IP:               10.244.0.44
IPs:
  IP:  10.244.0.44
Containers:
  post-install:
    Container ID:  docker://6f308b12d5878462a58ef78bf0774cd76fd08feba07e69aeb3111273314b38ef
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 09 Nov 2023 17:42:47 +0300
      Finished:     Thu, 09 Nov 2023 17:43:07 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mbfbw (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-mbfbw:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  89s   default-scheduler  Successfully assigned default/my-django-app-release-post-install to minikube
  Normal  Pulled     89s   kubelet            Container image "busybox" already present on machine
  Normal  Created    89s   kubelet            Created container post-install
  Normal  Started    89s   kubelet            Started container post-install
```

```bash
kubectl describe po my-django-app-release-pre-install
Name:             my-django-app-release-pre-install
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.67.2
Start Time:       Thu, 09 Nov 2023 17:42:23 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-weight: 1
Status:           Succeeded
IP:               10.244.0.42
IPs:
  IP:  10.244.0.42
Containers:
  pre-install:
    Container ID:  docker://e73125d86a8f5b26fa4c8b7cab5817747484f34378b676087a7432df126c01a1
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo Pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 09 Nov 2023 17:42:24 +0300
      Finished:     Thu, 09 Nov 2023 17:42:44 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-f7p22 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-f7p22:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  2m1s  default-scheduler  Successfully assigned default/my-django-app-release-pre-install to minikube
  Normal  Pulled     2m    kubelet            Container image "busybox" already present on machine
  Normal  Created    2m    kubelet            Created container pre-install
  Normal  Started    2m    kubelet            Started container pre-install
```

###  After setting delete policy

```bash
kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS        AGE
pod/django-deployment-79997f7486-2mdsm       1/1     Running   4 (3h35m ago)   4d3h
pod/django-deployment-79997f7486-7zlxw       1/1     Running   4 (3h35m ago)   4d3h
pod/django-deployment-79997f7486-9fbl6       1/1     Running   4 (3h35m ago)   4d3h
pod/my-django-app-release-867d97dd8f-4grbj   1/1     Running   0               2m15s

NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/django-service          NodePort    10.103.56.237   <none>        5000:30001/TCP   4d3h
service/kubernetes              ClusterIP   10.96.0.1       <none>        443/TCP          8d
service/my-django-app-release   NodePort    10.109.42.51    <none>        5000:30002/TCP   2m15s
```