`brew install kubernetes-cli`
`brew install minikube`

`minikube start`
`eval $(minikube docker-env)`

`docker build . -t hostname-app:v1`

`kubectl apply -f deployment.yaml`
`kubectl apply -f service.yaml`

`minikube service hostname-app-service`

`kubectl scale --replicas=3 deployment hostname-app-deployment`

Observe in browser (refresh multiple times)

Copy the url and start the curl script in a new terminal window
`./curl.sh (address)`

See how it stops serving traffic instantly to 2 of the pods
`kubectl scale --replicas=1 deployment hostname-app-deployment`

Change replicas in deployment to 3 apply it and observe how the pods join the loadbalancer
`kubectl apply -f deployment.yml`

Update version in hostname response to v2
Build image with updated version tag
`docker build . -t hostname-app:v2`

Apply it and observe with the curl script how the version switches from V1 to V2 without any downtime
`kubectl apply -f deployment.yml`

