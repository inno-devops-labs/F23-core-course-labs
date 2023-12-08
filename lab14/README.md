# Kube prometheus stack

## Describe components

## Install

```bash
> helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
> helm repo update
"prometheus-community" has been added to your repositories
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "prometheus-community" chart repository
Update Complete. ⎈Happy Helming!⎈
```

```bash
> helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack
NAME: kube-prometheus-stack
LAST DEPLOYED: Fri Dec  8 10:25:28 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
kube-prometheus-stack has been installed. Check its status by running:
  kubectl --namespace default get pods -l "release=kube-prometheus-stack"

Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.
```

```bash
> kubectl get po,sts,svc,pvc,cm
NAME                                                            READY   STATUS            RESTARTS      AGE
pod/alertmanager-kube-prometheus-stack-alertmanager-0           0/2     PodInitializing   0             56s
pod/app-python-0                                                1/1     Running           0             17m
pod/app-python-1                                                1/1     Running           0             17m
pod/app-python-2                                                1/1     Running           0             17m
pod/app-rust-54745b4ff9-vdj42                                   1/1     Running           2 (10d ago)   31d
pod/kube-prometheus-stack-grafana-56bf765f49-5mwzx              2/3     Running           0             70s
pod/kube-prometheus-stack-kube-state-metrics-5c68dd7f45-jsp79   1/1     Running           0             70s
pod/kube-prometheus-stack-operator-7db8f987bb-cqxnk             1/1     Running           0             70s
pod/kube-prometheus-stack-prometheus-node-exporter-6c6pf        1/1     Running           0             70s
pod/prometheus-kube-prometheus-stack-prometheus-0               0/2     PodInitializing   0             55s
pod/vault-0                                                     0/1     Running           1 (10d ago)   11d
pod/vault-agent-injector-576cc6ffc4-m2896                       1/1     Running           1 (10d ago)   11d

NAME                                                               READY   AGE
statefulset.apps/alertmanager-kube-prometheus-stack-alertmanager   0/1     56s
statefulset.apps/app-python                                        3/3     19m
statefulset.apps/prometheus-kube-prometheus-stack-prometheus       0/1     55s
statefulset.apps/vault                                             0/1     11d

NAME                                                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
service/alertmanager-operated                            ClusterIP   None             <none>        9093/TCP,9094/TCP,9094/UDP   57s
service/app-python                                       ClusterIP   10.96.143.18     <none>        80/TCP                       31d
service/app-rust                                         ClusterIP   10.102.85.85     <none>        80/TCP                       31d
service/kube-prometheus-stack-alertmanager               ClusterIP   10.101.57.246    <none>        9093/TCP,8080/TCP            71s
service/kube-prometheus-stack-grafana                    ClusterIP   10.107.120.244   <none>        80/TCP                       71s
service/kube-prometheus-stack-kube-state-metrics         ClusterIP   10.107.105.111   <none>        8080/TCP                     71s
service/kube-prometheus-stack-operator                   ClusterIP   10.106.10.83     <none>        443/TCP                      71s
service/kube-prometheus-stack-prometheus                 ClusterIP   10.101.53.5      <none>        9090/TCP,8080/TCP            71s
service/kube-prometheus-stack-prometheus-node-exporter   ClusterIP   10.108.66.56     <none>        9100/TCP                     71s
service/kubernetes                                       ClusterIP   10.96.0.1        <none>        443/TCP                      31d
service/prometheus-operated                              ClusterIP   None             <none>        9090/TCP                     56s
service/vault                                            ClusterIP   10.105.114.1     <none>        8200/TCP,8201/TCP            11d
service/vault-agent-injector-svc                         ClusterIP   10.106.12.35     <none>        443/TCP                      11d
service/vault-internal                                   ClusterIP   None             <none>        8200/TCP,8201/TCP            11d

NAME                                 STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/data-vault-0   Bound    pvc-d86e01d7-6c2a-4679-bd7b-84f5b948f5c5   10Gi       RWO            standard       11d

NAME                                                                DATA   AGE
configmap/kube-prometheus-stack-alertmanager-overview               1      78s
configmap/kube-prometheus-stack-apiserver                           1      78s
configmap/kube-prometheus-stack-cluster-total                       1      78s
configmap/kube-prometheus-stack-controller-manager                  1      78s
configmap/kube-prometheus-stack-etcd                                1      78s
configmap/kube-prometheus-stack-grafana                             1      78s
configmap/kube-prometheus-stack-grafana-config-dashboards           1      78s
configmap/kube-prometheus-stack-grafana-datasource                  1      78s
configmap/kube-prometheus-stack-grafana-overview                    1      78s
configmap/kube-prometheus-stack-k8s-coredns                         1      78s
configmap/kube-prometheus-stack-k8s-resources-cluster               1      78s
configmap/kube-prometheus-stack-k8s-resources-multicluster          1      78s
configmap/kube-prometheus-stack-k8s-resources-namespace             1      78s
configmap/kube-prometheus-stack-k8s-resources-node                  1      78s
configmap/kube-prometheus-stack-k8s-resources-pod                   1      78s
configmap/kube-prometheus-stack-k8s-resources-workload              1      78s
configmap/kube-prometheus-stack-k8s-resources-workloads-namespace   1      78s
configmap/kube-prometheus-stack-kubelet                             1      78s
configmap/kube-prometheus-stack-namespace-by-pod                    1      78s
configmap/kube-prometheus-stack-namespace-by-workload               1      78s
configmap/kube-prometheus-stack-node-cluster-rsrc-use               1      78s
configmap/kube-prometheus-stack-node-rsrc-use                       1      78s
configmap/kube-prometheus-stack-nodes                               1      78s
configmap/kube-prometheus-stack-nodes-darwin                        1      78s
configmap/kube-prometheus-stack-persistentvolumesusage              1      78s
configmap/kube-prometheus-stack-pod-total                           1      78s
configmap/kube-prometheus-stack-prometheus                          1      78s
configmap/kube-prometheus-stack-proxy                               1      78s
configmap/kube-prometheus-stack-scheduler                           1      78s
configmap/kube-prometheus-stack-workload-total                      1      78s
configmap/kube-root-ca.crt                                          1      31d
configmap/prometheus-kube-prometheus-stack-prometheus-rulefiles-0   34     64s
```
