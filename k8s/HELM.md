```shell
helm install ch app-python
minikube service list
minikube service ch-app-python
```


```shell
> kubectl get pods,svc 
NAME                                  READY   STATUS             RESTARTS      AGE
pod/app-python-67b7cb9579-rcz5n       1/1     Running            1 (18m ago)   23m
pod/app-python-67b7cb9579-shwbv       1/1     Running            1 (18m ago)   23m
pod/ch-app-python-dd888f9c4-s4mjt     1/1     Running            0             3m54s
pod/hello-minikube-74f785749c-xnmcr   0/1     ImagePullBackOff   0             38d

NAME                    TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python      LoadBalancer   10.105.106.132   <pending>     7098:31849/TCP   21m
service/ch-app-python   ClusterIP      10.108.109.33    <none>        80/TCP           3m54s
service/kubernetes      ClusterIP      10.96.0.1        <none>        443/TCP          38d
```


## StatefulState

```shell
helm secrets install --dry-run -f example_secret.yaml ses app-python
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /Users/tyakhshigulov/.kube/config
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /Users/tyakhshigulov/.kube/config
[helm-secrets] Decrypt skipped: example_secret.yaml
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /Users/tyakhshigulov/.kube/config
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /Users/tyakhshigulov/.kube/config
NAME: ses
LAST DEPLOYED: Sat Dec  9 22:30:44 2023
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: app-python/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "ses-app-python-test-connection"
  labels:
    helm.sh/chart: app-python-0.1.0
    app.kubernetes.io/name: app-python
    app.kubernetes.io/instance: ses
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['ses-app-python:80']
  restartPolicy: Never
MANIFEST:
---
# Source: app-python/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ses-app-python
  labels:
    helm.sh/chart: app-python-0.1.0
    app.kubernetes.io/name: app-python
    app.kubernetes.io/instance: ses
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: app-python/templates/secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: secret-key
  labels:
    app: app-python
    chart: "app-python-0.1.0"
    release: "ses"
    heritage: "Helm"

type: Opaque
data:
  key: "c2VjcmV0X2tleQ=="
---
# Source: app-python/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: ses-app-python
  labels:
    helm.sh/chart: app-python-0.1.0
    app.kubernetes.io/name: app-python
    app.kubernetes.io/instance: ses
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: app-python
    app.kubernetes.io/instance: ses
---
# Source: app-python/templates/statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: ses-app-python
  labels:
    helm.sh/chart: app-python-0.1.0
    app.kubernetes.io/name: app-python
    app.kubernetes.io/instance: ses
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: app-python
      app.kubernetes.io/instance: ses
  template:
    metadata:
      labels:
        helm.sh/chart: app-python-0.1.0
        app.kubernetes.io/name: app-python
        app.kubernetes.io/instance: ses
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: ses-app-python
      securityContext:
        {}
      containers:
        - name: app-python
          env:
            - name: HELM_SECRET_KEY
              valueFrom:
                secretKeyRef:
                  name: secret-key
                  key: key
          securityContext:
            {}
          image: "wiirtex/python_time_service:0.4.0"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 7098
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
          volumeMounts:
            - mountPath: /app/volume/
              name: visits
  volumeClaimTemplates:
    - metadata:
        name: visits
      spec:
        accessModes: [ReadWriteOnce]
        resources:
          requests:
            storage: 1Mi

NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app-python,app.kubernetes.io/instance=ses" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```