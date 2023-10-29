# Task 1 

## 1. Start deployment

```
minikube start

minikube dashboard

kubectl create deployment test-node --image=docker.io/0x22d1ab/app_python 
```


```
kubectl get pods,svc
```

![](/assets/screenshots/2023-10-29-17-07-42.png)

![](/assets/screenshots/2023-10-29-18-24-27.png)



### 2. Expose service

```
kubectl expose deployment test-node --type=LoadBalancer --port=8000

minikube service test-node 
```



## 3. Perform cleanup

```
#kubectl delete pod test-node-f687fd78-9qt6d
kubectl delete service test-node
kubectl delete deployment test-node
```
![](/assets/screenshots/2023-10-29-18-25-41.png)

# Task 2


```
kubectl apply -f deployment.yml 


minikube service --all
```




![](/assets/screenshots/2023-10-29-19-01-53.png)

![](/assets/screenshots/2023-10-29-19-06-00.png)

![](/assets/screenshots/2023-10-29-19-05-32.png)



# Bonus

## 1. Additional application

![](/assets/screenshots/2023-10-29-19-16-36.png)
![](/assets/screenshots/2023-10-29-19-16-20.png)

## 2. Ingress controller

```
minikube addons enable ingress
```


![](/assets/screenshots/2023-10-29-19-29-40.png)

![](/assets/screenshots/2023-10-29-19-30-11.png)


### Verifying applications availability

```
curl --resolve "app-python.gigachaddevelopment:80:$( minikube ip )" -i app-python.gigachaddevelopment
```

![](/assets/screenshots/2023-10-29-19-41-50.png)

![](/assets/screenshots/2023-10-29-19-44-33.png)


- Note that the response has `google.com` since app-go is responsible for performing redirects according to user's query

## References
https://kubernetes.io/docs/concepts/services-networking/service/
https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/