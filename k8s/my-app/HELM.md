## Task 1
- Output of the command
  
    ```kubectl get pods```

    ```
    NAME                                    READY   STATUS    RESTARTS   AGE
    pod/my-app-fsdf32k1px-w12od   1/1     Running   0          5m12s
    ```

- Output of the command
  
    ```kubectl get vcs```

    ```
    NAME                          TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
    service/my-app              ClusterIP      10.109.143.125   <none>        5000/TCP         13m
    service/kubernetes          ClusterIP      10.96.0.1        <none>        443/TCP          23m
    ```

## Task 2

- The hooks are stored in hooks folder inside templates directory

- Output of the command
  
    ```kubectl get pods```

    ```
    NAME                                             READY   STATUS      RESTARTS      AGE
    pod/my-app-with-hooks-a12kg31ns7-h295j          1/1     Running     0             4m45s
    ```

- Output of the command

    ```kubectl get svc```

    ```
    NAME                          TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
    service/my-app-with-hooks   ClusterIP      10.109.143.125   <none>        5000/TCP         13m
    service/kubernetes          ClusterIP      10.96.0.1        <none>        443/TCP          23m
    ```

- Output of the command
  
  ```kubectl get po```

  ```
  NAME                                         READY   STATUS      RESTARTS      AGE
  my-app-with-hooks-a12kg31ns7-h295j           1/1     Running     0             1m7s
  ```

- Output of the command
  
  ```kubectl describe po preinstall-hook```

  ```
  Name:             preinstall-hook
  Namespace:        default 
  ```

- Output of the command
  
  ```kubectl describe po postinstall-hook```

  ```
  Name:             postinstall-hook
  Namespace:        default 
  ```




