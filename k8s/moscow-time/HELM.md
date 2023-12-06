# 6 points
I commented out probes because i've encountered issues using them.
```bash
╭─bizuki@DESKTOP-A1F8O7S ~/proj/devops-course/k8s  ‹main*› 
╰─➤  kubectl get pods,svc        
NAME                               READY   STATUS    RESTARTS   AGE
pod/moscow-time-7d586bdf58-vpswc   1/1     Running   0          80s

NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/kubernetes    ClusterIP   10.96.0.1        <none>        443/TCP    14d
service/moscow-time   ClusterIP   10.103.237.116   <none>        8080/TCP   80s
```

# 4 points
Hooks themselfs
```bash
╭─bizuki@DESKTOP-A1F8O7S ~/proj/devops-course/k8s  ‹main*› 
╰─➤  helm install --dry-run helm-hooks moscow-time
NAME: helm-hooks
LAST DEPLOYED: Tue Nov 14 16:47:03 2023
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: moscow-time/templates/post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
   name: postinstall-hook
   annotations:
       "helm.sh/hook": "post-install"
       "helm.sh/hook-delete-policy": hook-succeeded,hook-failed
spec:
  containers:
  - name: post-install-container
    image: busybox
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: moscow-time/templates/pre-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
   name: preinstall-hook
   annotations:
       "helm.sh/hook": "pre-install"
       "helm.sh/hook-delete-policy": hook-succeeded,hook-failed
spec:
  containers:
  - name: pre-install-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo The pre-install hook is running' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---kubectl get po
```

```bash

╭─bizuki@DESKTOP-A1F8O7S ~/proj/devops-course/k8s  ‹main*› 
╰─➤  kubectl get po                               
NAME                           READY   STATUS    RESTARTS   AGE
moscow-time-7d586bdf58-vpswc   1/1     Running   0          9m21s

─bizuki@DESKTOP-A1F8O7S ~/proj/devops-course/k8s  ‹main*› 
╰─➤  kubectl describe po pre-install-hook
Error from server (NotFound): pods "pre-install-hook" not found

╭─bizuki@DESKTOP-A1F8O7S ~/proj/devops-course/k8s  ‹main*› 
╰─➤  kubectl describe po post-install-hook                                                                                                                                                        1 ↵
Error from server (NotFound): pods "post-install-hook" not found
```
