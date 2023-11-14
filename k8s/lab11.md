# Lab 11. Kubernetes Secrets and Hashicorp Vault

 ## Task 1
 ### 1.2
 ```
 $ kubectl create secret generic jwt-token --from-literal=token=SECRET_TOKEN
 secret/jwt-token created
 ```

 ```
 $ kubectl describe secret jwt-token
 Name:         jwt-token
 Namespace:    default
 Labels:       <none>
 Annotations:  <none>
 Type:  Opaque
 Data
 ====
 token:  12 bytes
 ```

 ```
 $ kubectl get secret jwt-token -o jsonpath='{.data.token}' | base64 --decode
 SECRET_TOKEN
 ```

 ### Task 1.3
 ```
 $ helm secrets install app-python . -n default -f ./secrets.yaml 
 NAME: app-python
 LAST DEPLOYED: Tue Nov 14 02:31:21 2023
 NAMESPACE: default
 STATUS: deployed
 REVISION: 1
 NOTES:
 1. Get the application URL by running these commands:
   export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services app-python)
   export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
   echo http://$NODE_IP:$NODE_PORT
 removed './secrets.yaml.dec'
 ```

 ```
 $ kubectl describe deployment app-python
 Name:                   app-python
 Namespace:              default
 CreationTimestamp:      Tue, 14 Nov 2023 02:31:25 +0300
 Labels:                 app.kubernetes.io/instance=app-python
                         app.kubernetes.io/managed-by=Helm
                         app.kubernetes.io/version=1.16.0
 Annotations:            deployment.kubernetes.io/revision: 1
                         meta.helm.sh/release-name: app-python
                         meta.helm.sh/release-namespace: default
 Selector:               app.kubernetes.io/instance=app-python,app.kubernetes.io/managed-by=Helm,app.kubernetes.io/version=1.16.0
 Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
 StrategyType:           RollingUpdate
 MinReadySeconds:        0
 RollingUpdateStrategy:  25% max unavailable, 25% max surge
 Pod Template:
   Labels:           app.kubernetes.io/instance=app-python
                     app.kubernetes.io/managed-by=Helm
                     app.kubernetes.io/version=1.16.0
   Service Account:  app-python
   Containers:
    app-python:
     Image:      k-tyulebaeva/moscow-time-app:latest
     Port:       80/TCP
     Host Port:  0/TCP
     Liveness:   http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
     Readiness:  http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
     Environment:
       JWT_TOKEN:  <set to the key 'token' in secret 'credentials'>  Optional: false
     Mounts:       <none>
   Volumes:        <none>
 Conditions:
   Type           Status  Reason
   ----           ------  ------
   Available      True    MinimumReplicasAvailable
   Progressing    True    NewReplicaSetAvailable
 OldReplicaSets:  <none>
 NewReplicaSet:   app-python-6487867bfd (3/3 replicas created)
 Events:
   Type    Reason             Age   From                   Message
   ----    ------             ----  ----                   -------
   Normal  ScalingReplicaSet  34s   deployment-controller  Scaled up replica set app-python-6487867bfd to 3
 ```


 ```
 $ kubectl get secret credentials -o yaml
 apiVersion: v1
 data:
   token: U0VDUkVUX1RPS0VO
 kind: Secret
 metadata:
   annotations:
     meta.helm.sh/release-name: app-python
     meta.helm.sh/release-namespace: default
   creationTimestamp: "2023-11-13T23:31:25Z"
   labels:
     app: app-python
     app.kubernetes.io/managed-by: Helm
     chart: app-python-0.1.0
     heritage: Helm
     release: app-python
   name: credentials
   namespace: default
   resourceVersion: "29902"
   uid: 241497c7-8bba-4440-a2ee-c759c08976ab
 type: Opaque
 ```

 ```
 $ echo "U0VDUkVUX1RPS0VO" | base64 -d
 SECRET_TOKEN
 ```

 ```
 $ kubectl get po
 NAME                          READY   STATUS    RESTARTS   AGE
 app-python-6487867bfd-2jh8x   1/1     Running   0          107s
 app-python-6487867bfd-cwlqm   1/1     Running   0          107s
 app-python-6487867bfd-k6sjr   1/1     Running   0          107s
 ```

 ```
 $ kubectl exec app-python-6487867bfd-2jh8x -- printenv | grep "JWT_TOKEN"
 JWT_TOKEN=SECRET_TOKEN
 ```

 ## Task 2
 ### 3.2 
 #### Set vault secret
 ```
 $ kubectl exec -it vault-0 -- /bin/sh
 / $ vault secrets enable -path=internal kv-v2
 Success! Enabled the kv-v2 secrets engine at: internal/
 ```

 ```
 $ vault kv put internal/database/config token="SECRET_TOKEN_VAULT"
 ======== Secret Path ========
 internal/data/database/config
 ======= Metadata =======
 Key                Value
 ---                -----
 created_time       2023-11-13T23:50:39.898228407Z
 custom_metadata    <nil>
 deletion_time      n/a
 destroyed          false
 version            1
 ```

 ```
 $ vault kv get internal/database/config
 ======== Secret Path ========
 internal/data/database/config
 ======= Metadata =======
 Key                Value
 ---                -----
 created_time       2023-11-13T23:50:39.898228407Z
 custom_metadata    <nil>
 deletion_time      n/a
 destroyed          false
 version            1
 ==== Data ====
 Key      Value
 ---      -----
 token    SECRET_TOKEN_VAULT
 ```

 #### Configure Kubernetes authentication
 ```
 $ vault auth enable kubernetes
 Success! Enabled kubernetes auth method at: kubernetes/
 ```

 ```
 $ vault write auth/kubernetes/config \
 >       kubernetes_host="https://$KUBERNETES_PORT_443_TCP_ADDR:443"
 Success! Data written to: auth/kubernetes/config
 ```

 ```
 $ vault policy write internal-app - <<EOF
 > path "internal/data/database/config" {
 >    capabilities = ["read"]
 > }
 > EOF
 Success! Uploaded policy: internal-app
 ```

 ```
 $ vault write auth/kubernetes/role/internal-app \
 >       bound_service_account_names=internal-app \
 >       bound_service_account_namespaces=default \
 >       policies=internal-app \
 >       ttl=24h
 Success! Data written to: auth/kubernetes/role/internal-app
 ```


 #### Create service account
 ```
 $ kubectl create sa internal-app
 serviceaccount/internal-app created
 ```

 ```
 $ kubectl get serviceaccounts
 NAME                   SECRETS   AGE
 app-python             0         26m
 default                0         14d
 internal-app           0         5s
 vault                  0         18m
 ```


 #### Injected secrets
 ```
 $ kubectl get po
 NAME                                    READY   STATUS    RESTARTS   AGE
 app-python-6547659489-8fltb             2/2     Running   0          26s
 app-python-6547659489-cxzq9             2/2     Running   0          26s
 app-python-6547659489-f5vhz             2/2     Running   0          26s
 vault-0                                 1/1     Running   0          67m
 vault-agent-injector-5cd8b87c6c-rctsv   1/1     Running   0          67m
 ```

 ```
 $ kubectl exec -it app-python-6547659489-8fltb -- bash
 ```

 ```
 $ cat /vault/secrets/database-config.txt 
 Bearer token: SECRET_TOKEN_VAULT
 ```

 ```
 $ df -h
 Filesystem      Size  Used Avail Use% Mounted on
 overlay          55G   50G  2.0G  97% /
 tmpfs            64M     0   64M   0% /dev
 tmpfs           3.8G     0  3.8G   0% /sys/fs/cgroup
 tmpfs           7.5G  4.0K  7.5G   1% /vault/secrets
 /dev/nvme0n1p5   55G   50G  2.0G  97% /etc/hosts
 shm              64M     0   64M   0% /dev/shm
 tmpfs           7.5G   12K  7.5G   1% /run/secrets/kubernetes.io/serviceaccount
 tmpfs           3.8G     0  3.8G   0% /proc/asound
 tmpfs           3.8G     0  3.8G   0% /proc/acpi
 tmpfs           3.8G     0  3.8G   0% /proc/scsi
 tmpfs           3.8G     0  3.8G   0% /sys/firmware
 ```

 ## Bonus task
 #### Python app
 ```
 $ kubectl describe deploy app-python
 Name:                   app-python
 Namespace:              default
 CreationTimestamp:      Tue, 14 Nov 2023 04:22:36 +0300
 Labels:                 app.kubernetes.io/instance=app-python
                         app.kubernetes.io/managed-by=Helm
                         app.kubernetes.io/version=1.16.0
 Annotations:            deployment.kubernetes.io/revision: 1
                         meta.helm.sh/release-name: app-python
                         meta.helm.sh/release-namespace: default
 Selector:               app.kubernetes.io/instance=app-python,app.kubernetes.io/managed-by=Helm,app.kubernetes.io/version=1.16.0
 Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
 StrategyType:           RollingUpdate
 MinReadySeconds:        0
 RollingUpdateStrategy:  25% max unavailable, 25% max surge
 Pod Template:
   Labels:           app.kubernetes.io/instance=app-python
                     app.kubernetes.io/managed-by=Helm
                     app.kubernetes.io/version=1.16.0
   Annotations:      vault.hashicorp.com/agent-inject: true
                     vault.hashicorp.com/agent-inject-secret-database-config.txt: internal/data/database/config
                     vault.hashicorp.com/agent-inject-status: update
                     vault.hashicorp.com/agent-inject-template-database-config.txt:
                       {{- with secret "internal/data/database/config" -}}Bearer token: {{ .Data.data.token }}{{- end -}}
                     vault.hashicorp.com/role: internal-app
   Service Account:  internal-app
   Containers:
    app-python:
     Image:      k-tyulebaeva/moscow-time-app:latest
     Port:       80/TCP
     Host Port:  0/TCP
     Limits:
       cpu:     500m
       memory:  128Mi
     Requests:
       cpu:      250m
       memory:   64Mi
     Liveness:   http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
     Readiness:  http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
     Environment:
       EXTERNAL_SERVICE_URL:  https://url:8083
       IS_RETRY_STRATEGY_ON:  true
       JWT_TOKEN:             <set to the key 'token' in secret 'credentials'>  Optional: false
     Mounts:                  <none>
   Volumes:                   <none>
 Conditions:
   Type           Status  Reason
   ----           ------  ------
   Available      True    MinimumReplicasAvailable
   Progressing    True    NewReplicaSetAvailable
 OldReplicaSets:  <none>
 NewReplicaSet:   app-python-548f9dd5cc (3/3 replicas created)
 Events:
   Type    Reason             Age   From                   Message
   ----    ------             ----  ----                   -------
   Normal  ScalingReplicaSet  30s   deployment-controller  Scaled up replica set app-python-548f9dd5cc to 3
 ```
