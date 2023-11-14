# No configuration files
## Initialization
First we will start our minkube cluster
```bash
minikube start
```
Then deploy and expose our application
```bash
kubectl create deployment moscow-time --images/image=bizuki/moscow-time:latest
kubectl expose deployment moscow-time --type=LoadBalancer --port=8080
```
## Check our cluster

### Info from `kubectl get pods,svc`
![Alt text](images/image-2.png)

### Minikube tunnel to service
![Alt text](images/image.png)

## Clen up
![Alt text](images/image-1.png)


# With configuration files

## Initialization
First we will start our minkube cluster
```bash
minikube start
```

Then deploy and expose our application
```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```
## Checking cluster

### Info from `kubectl get pods,svc`
![Alt text](images/image-5.png)

### Minikube tunnel to service
![Alt text](images/image-4.png)
Result from browser. Ip is the same as in result of minikube command
![Alt text](images/image-3.png)

## Clean up
![Alt text](images/image-6.png)