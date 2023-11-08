# Helm overview

## Task 1

1. Installed helm.

1. Created helm chart for python app. `helm create helm-python-app`.

1. Install helm chart. `helm install python-helm-app ./helm-python-app`

```bash
    NAME: python-helm-app
LAST DEPLOYED: Wed Nov  8 10:37:33 2023
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: helm-python-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "python-helm-app-helm-python-app-test-connection"
  labels:
    helm.sh/chart: helm-python-app-0.1.0
    app.kubernetes.io/name: helm-python-app
    app.kubernetes.io/instance: python-helm-app
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['python-helm-app-helm-python-app:80']
  restartPolicy: Never
MANIFEST:
---
# Source: helm-python-app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: python-helm-app-helm-python-app
  labels:
    helm.sh/chart: helm-python-app-0.1.0
    app.kubernetes.io/name: helm-python-app
    app.kubernetes.io/instance: python-helm-app
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: helm-python-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: python-helm-app-helm-python-app
  labels:
    helm.sh/chart: helm-python-app-0.1.0
    app.kubernetes.io/name: helm-python-app
    app.kubernetes.io/instance: python-helm-app
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: helm-python-app
    app.kubernetes.io/instance: python-helm-app
---
# Source: helm-python-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-helm-app-helm-python-app
  labels:
    helm.sh/chart: helm-python-app-0.1.0
    app.kubernetes.io/name: helm-python-app
    app.kubernetes.io/instance: python-helm-app
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: helm-python-app
      app.kubernetes.io/instance: python-helm-app
  template:
    metadata:
      labels:
        helm.sh/chart: helm-python-app-0.1.0
        app.kubernetes.io/name: helm-python-app
        app.kubernetes.io/instance: python-helm-app
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: python-helm-app-helm-python-app
      securityContext:
        {}
      containers:
        - name: helm-python-app
          securityContext:
            {}
          image: ":tagname"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http
          resources:
            {}

NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services python-helm-app-helm-python-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

### Check minikube pod and service

```bash
$minikube kubectl get pods,svc

NAME                                                  READY   STATUS             RESTARTS   AGE
pod/python-helm-app-helm-python-app-b69888b8f-cbdkz   1/1     Running   0          5m12s

NAME                                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes                        ClusterIP      10.96.0.1       <none>        443/TCP        44h
service/python-helm-app-helm-python-app   NodePort       10.110.80.62    <none>        80:31047/TCP   5m12s

