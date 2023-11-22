## Visits

`> kubectl get po`
```
NAME                                    READY   STATUS      RESTARTS   AGE
postinstall-hook                        0/1     Completed   0          36s
preinstall-hook                         0/1     Completed   0          43s
python-app-8fc64889b-c6v2h              1/1     Running     0          36s
python-app-8fc64889b-nw4zs              1/1     Running     0          36s
python-app-8fc64889b-t89r9              1/1     Running     0          36s
vault-0                                 1/1     Running     0          25m
vault-agent-injector-5cd8b87c6c-lczzc   1/1     Running     0          25m
```

The pod with the running application is `python-app-8fc64889b-c6v2h` (or any other `python-app-...`).

`> kubectl exec python-app-8fc64889b-c6v2h -- cat /data/config.json`
```
{"counter": "2"}
```

`> kubectl get configmaps`
```
NAME               DATA   AGE
configmap-config   1      56s
kube-root-ca.crt   1      21d
```