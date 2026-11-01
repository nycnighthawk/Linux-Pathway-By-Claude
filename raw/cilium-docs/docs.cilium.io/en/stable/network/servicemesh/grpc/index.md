---
{"title": "Ingress gRPC Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/grpc/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Ingress gRPC Example[](#ingress-grpc-example "Link to this heading")

The example ingress configuration in `grpc-ingress.yaml`{.docutils .literal .notranslate} shows how to route gRPC traffic to backend services.

## Deploy the Demo App[](#deploy-the-demo-app "Link to this heading")

For this demo we will use [GCP's microservices demo app](https://github.com/GoogleCloudPlatform/microservices-demo).

``` {#codecell0}
$ kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/main/release/kubernetes-manifests.yaml
```

Copy Line

Since gRPC is binary-encoded, you also need the proto definitions for the gRPC services in order to make gRPC requests. Download this for the demo app:

``` {#codecell1}
$ curl -o demo.proto https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/main/protos/demo.proto
```

Copy Line

## Deploy GRPC Ingress[](#deploy-grpc-ingress "Link to this heading")

You'll find the example Ingress definition in `examples/kubernetes/servicemesh/grpc-ingress.yaml`{.docutils .literal .notranslate}.

``` {#codecell2}
# GRPC ingress for GCP microservice demo application
# https://github.com/GoogleCloudPlatform/microservices-demo
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: grpc-ingress
  namespace: default
spec:
  ingressClassName: cilium
  rules:
  - http:
      paths:
      - backend:
          service:
            name: productcatalogservice
            port:
              number: 3550
        path: /hipstershop.ProductCatalogService
        pathType: Prefix
      - backend:
          service:
            name: currencyservice
            port:
              number: 7000
        path: /hipstershop.CurrencyService
        pathType: Prefix
```

Copy First Line Copy All

``` {#codecell3 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/grpc-ingress.yaml
```

Copy Line

This defines paths for requests to be routed to the `productcatalogservice`{.docutils .literal .notranslate} and `currencyservice`{.docutils .literal .notranslate} microservices.

Just as in the previous HTTP Ingress Example, this creates a LoadBalancer service, and it may take a little while for your cloud provider to provision an external IP address.

``` {#codecell4}
$ kubectl get ingress
NAME           CLASS    HOSTS   ADDRESS         PORTS   AGE
grpc-ingress   cilium   *       10.111.109.99   80      3s
```

Copy First Line Copy Commands Copy All

## Make gRPC Requests to Backend Services[](#make-grpc-requests-to-backend-services "Link to this heading")

To issue client gRPC requests you can use [grpcurl](https://github.com/fullstorydev/grpcurl#binaries).

``` {#codecell5}
$ GRPC_INGRESS=$(kubectl get ingress grpc-ingress -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
# To access the currency service:
$ grpcurl -plaintext -proto ./demo.proto $GRPC_INGRESS:80 hipstershop.CurrencyService/GetSupportedCurrencies
#To access the product catalog service:
$ grpcurl -plaintext -proto ./demo.proto $GRPC_INGRESS:80 hipstershop.ProductCatalogService/ListProducts
```

Copy First Line Copy Commands Copy All
