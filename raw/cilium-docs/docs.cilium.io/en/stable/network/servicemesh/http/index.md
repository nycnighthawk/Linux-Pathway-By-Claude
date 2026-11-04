---
{"title": "Ingress HTTP Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/http/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Ingress HTTP Example[](#ingress-http-example "Link to this heading")

The example ingress configuration routes traffic to backend services from the `bookinfo`{.docutils .literal .notranslate} demo microservices app from the Istio project.

## Deploy the Demo App[](#deploy-the-demo-app "Link to this heading")

``` {#codecell0}
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.11/samples/bookinfo/platform/kube/bookinfo.yaml
```

Copy Line

This is just deploying the demo app, it's not adding any Istio components. You can confirm that with Cilium Service Mesh there is no Envoy sidecar created alongside each of the demo app microservices.

``` {#codecell1}
$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
details-v1-5498c86cf5-kjzkj       1/1     Running   0          2m39s
productpage-v1-65b75f6885-ff59g   1/1     Running   0          2m39s
ratings-v1-b477cf6cf-kv7bh        1/1     Running   0          2m39s
reviews-v1-79d546878f-r5bjz       1/1     Running   0          2m39s
reviews-v2-548c57f459-pld2f       1/1     Running   0          2m39s
reviews-v3-6dd79655b9-nhrnh       1/1     Running   0          2m39s
```

Copy First Line Copy Commands Copy All

Note

With the sidecar implementation the output would show 2/2 READY. One for the microservice and one for the Envoy sidecar.

## Deploy the First Ingress[](#deploy-the-first-ingress "Link to this heading")

You'll find the example Ingress definition in `basic-ingress.yaml`{.docutils .literal .notranslate}.

``` {#codecell2}
# Basic ingress for istio bookinfo demo application, which can be found in below
# https://raw.githubusercontent.com/istio/istio/release-1.11/samples/bookinfo/platform/kube/bookinfo.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: basic-ingress
  namespace: default
spec:
  ingressClassName: cilium
  rules:
  - http:
      paths:
      - backend:
          service:
            name: details
            port:
              number: 9080
        path: /details
        pathType: Prefix
      - backend:
          service:
            name: productpage
            port:
              number: 9080
        path: /
        pathType: Prefix
```

Copy First Line Copy All

``` {#codecell3 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/basic-ingress.yaml
```

Copy Line

This example routes requests for the path `/details`{.docutils .literal .notranslate} to the `details`{.docutils .literal .notranslate} service, and `/`{.docutils .literal .notranslate} to the `productpage`{.docutils .literal .notranslate} service.

Getting the list of services, you'll see a LoadBalancer service is automatically created for this ingress. Your cloud provider will automatically provision an external IP address, but it may take around 30 seconds.

``` {#codecell4}
# For dedicated load balancer mode
$ kubectl get svc
NAME                           TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE
cilium-ingress-basic-ingress   LoadBalancer   10.98.169.125    10.98.169.125   80:32478/TCP   2m11s
details                        ClusterIP      10.102.131.226   <none>          9080/TCP       2m15s
kubernetes                     ClusterIP      10.96.0.1        <none>          443/TCP        10m
productpage                    ClusterIP      10.97.231.139    <none>          9080/TCP       2m15s
ratings                        ClusterIP      10.108.152.42    <none>          9080/TCP       2m15s
reviews                        ClusterIP      10.111.145.160   <none>          9080/TCP       2m15s

# For shared load balancer mode
$ kubectl get services -n kube-system cilium-ingress
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
cilium-ingress   LoadBalancer   10.98.169.125   10.98.169.125   80:32690/TCP,443:31566/TCP   18m
```

Copy First Line Copy Commands Copy All

The external IP address should also be populated into the Ingress:

``` {#codecell5}
$ kubectl get ingress
NAME            CLASS    HOSTS   ADDRESS         PORTS   AGE
basic-ingress   cilium   *       10.98.169.125   80      97s
```

Copy First Line Copy Commands Copy All

Note

Some providers e.g. EKS use a fully-qualified domain name rather than an IP address.

## Make HTTP Requests[](#make-http-requests "Link to this heading")

Check (with `curl`{.docutils .literal .notranslate} or in your browser) that you can make HTTP requests to that external address. The `/`{.docutils .literal .notranslate} path takes you to the home page for the bookinfo application.

From outside the cluster you can also make requests directly to the `details`{.docutils .literal .notranslate} service using the path `/details`{.docutils .literal .notranslate}. But you can't directly access other URL paths that weren't defined in `basic-ingress.yaml`{.docutils .literal .notranslate}.

For example, you can get JSON data from a request to `<address>/details/1`{.docutils .literal .notranslate} and get back some data, but you will get a 404 error if you make a request to `<address>/ratings`{.docutils .literal .notranslate}.

``` {#codecell6}
$ HTTP_INGRESS=$(kubectl get ingress basic-ingress -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ curl --fail -s http://"$HTTP_INGRESS"/details/1 | jq
{
  "id": 1,
  "author": "William Shakespeare",
  "year": 1595,
  "type": "paperback",
  "pages": 200,
  "publisher": "PublisherA",
  "language": "English",
  "ISBN-10": "1234567890",
  "ISBN-13": "123-1234567890"
}
```

Copy First Line Copy Commands Copy All
