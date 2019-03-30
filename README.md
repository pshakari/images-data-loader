# images-data-loader
Creates a postgresql container on OpenShift and then loads images from a data loader image as a kubernetes [job](http://kubernetesbyexample.com/jobs/)


```sh
oc cluster up

oc new-project facerec

oc new-app --template=postgresql-persistent \
-p POSTGRESQL_USER=username \
-p POSTGRESQL_PASSWORD=password \
-p POSTGRESQL_DATABASE=imagesDb
```

```sh
oc create -f https://github.com/pshakari/images-data-loader/master/images-data-loader.yaml 

oc new-app --template=images-data-loader
```
