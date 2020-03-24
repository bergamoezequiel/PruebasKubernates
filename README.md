# PruebasKubernates


docker build -t my-python-app .
docker run -p 5555:5555 -it --rm --name my-running-app my-python-app


__________________________________________________________________
docker build -t ezequielb/pruebas .
docker run -d -p 5555:5555 ezequielb/pruebas
#docker push ezequielb/pruebas

_______________________________________
IMPORTANTE
docker build -t ezequielb/pruebas:tag2 .
docker push ezequielb/pruebas:tag2   lo subo a mi dockerhub user:ezequielb pass: vento2.0T

kubectl apply -f k8s\deployment.yaml inmortalizador de pods. levanta x cantidad de pods y los mantiene vivos
kubectl get all -- te devuelve todo los objetos de kubernates pods , deploymeents , service
kubectl apply -f k8s\service.yaml levanta el servicio de tipo loadbalancer y lo hace accesible
Luego desde el navegador http://localhost:80/Clientes
kubectl delete service/(nombre)
kubectl delete deployment/(nombre)