---
{"title": "HTTP Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/http/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# HTTP Example[](#http-example "Link to this heading")

In this example, we will deploy a simple HTTP service and expose it to the Cilium Gateway API.

The demo application is from the `bookinfo`{.docutils .literal .notranslate} demo microservices app from the Istio project.

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

## Deploy the Cilium Gateway[](#deploy-the-cilium-gateway "Link to this heading")

You'll find the example Gateway and HTTPRoute definition in `basic-http.yaml`{.docutils .literal .notranslate}.

``` {#codecell2}
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gateway
spec:
  gatewayClassName: cilium
  listeners:
  - protocol: HTTP
    port: 80
    name: web-gw
    allowedRoutes:
      namespaces:
        from: Same
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http-app-1
spec:
  parentRefs:
  - name: my-gateway
    namespace: default
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /details
    backendRefs:
    - name: details
      port: 9080
  - matches:
    - headers:
      - type: Exact
        name: magic
        value: foo
      queryParams:
      - type: Exact
        name: great
        value: example
      path:
        type: PathPrefix
        value: /
      method: GET
    backendRefs:
    - name: productpage
      port: 9080
```

Copy First Line Copy All

``` {#codecell3 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/basic-http.yaml
```

Copy Line

The above example creates a Gateway named `my-gateway`{.docutils .literal .notranslate} that listens on port 80. Two routes are defined, one for `/details`{.docutils .literal .notranslate} to the `details`{.docutils .literal .notranslate} service, and one for `/`{.docutils .literal .notranslate} to the `productpage`{.docutils .literal .notranslate} service.

Your cloud provider will automatically provision an external IP address for the gateway, but it may take up to 20 minutes.

``` {#codecell4}
$ kubectl get gateway my-gateway
NAME         CLASS    ADDRESS        PROGRAMMED   AGE
my-gateway   cilium   10.100.26.37   True         2d7h
```

Copy First Line Copy Commands Copy All

Note

Some providers e.g. EKS use a fully-qualified domain name rather than an IP address.

## Make HTTP Requests[](#make-http-requests "Link to this heading")

Now that the Gateway is ready, you can make HTTP requests to the services.

``` {#codecell5}
$ GATEWAY=$(kubectl get gateway my-gateway -o jsonpath='{.status.addresses[0].value}')
$ curl --fail -s http://"$GATEWAY"/details/1 | jq
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
$ curl -v -H 'magic: foo' http://"$GATEWAY"\?great\=example
...
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Bookstore App</title>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="static/bootstrap/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="static/bootstrap/css/bootstrap-theme.min.css">

  </head>
  <body>

<p>
    <h3>Hello! This is a simple bookstore application consisting of three services as shown below</h3>
</p>

<table class="table table-condensed table-bordered table-hover"><tr><th>name</th><td>http://details:9080</td></tr><tr><th>endpoint</th><td>details</td></tr><tr><th>children</th><td><table class="table table-condensed table-bordered table-hover"><tr><th>name</th><th>endpoint</th><th>children</th></tr><tr><td>http://details:9080</td><td>details</td><td></td></tr><tr><td>http://reviews:9080</td><td>reviews</td><td><table class="table table-condensed table-bordered table-hover"><tr><th>name</th><th>endpoint</th><th>children</th></tr><tr><td>http://ratings:9080</td><td>ratings</td><td></td></tr></table></td></tr></table></td></tr></table>

<p>
    <h4>Click on one of the links below to auto generate a request to the backend as a real user or a tester
    </h4>
</p>
<p><a href="/productpage?u=normal">Normal user</a></p>
<p><a href="/productpage?u=test">Test user</a></p>

<!-- Latest compiled and minified JavaScript -->
<script src="static/jquery.min.js"></script>

<!-- Latest compiled and minified JavaScript -->
<script src="static/bootstrap/js/bootstrap.min.js"></script>

  </body>
</html>
```

Copy First Line Copy Commands Copy All
