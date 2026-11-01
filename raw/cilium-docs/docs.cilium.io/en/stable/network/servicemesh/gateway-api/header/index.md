---
{"title": "HTTP Header Modifier Examples", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/header/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# HTTP Header Modifier Examples[](#http-header-modifier-examples "Link to this heading")

The Gateway can modify the headers of HTTP requests from clients.

## Deploy the Echo App[](#deploy-the-echo-app "Link to this heading")

We will use a deployment made of echo servers.

The application will reply to the client and, in the body of the reply, will include information about the Pod receiving the original request. We will use this information to illustrate how the traffic is manipulated by the Gateway.

``` {#codecell0 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/echo-basic.yaml
```

Copy Line

Verify the Pods are running as expected.

``` {#codecell1}
$ kubectl get pods
NAME                      READY   STATUS    RESTARTS   AGE
echo-1-7d88f779b-m6r46    1/1     Running   0          21s
echo-2-5bfb6668b4-n7llh   1/1     Running   0          21s
```

Copy First Line Copy Commands Copy All

## Deploy the Cilium Gateway[](#deploy-the-cilium-gateway "Link to this heading")

HTTP header modification is the process of adding, removing, or modifying HTTP headers in incoming requests. To configure HTTP header modification, define a Gateway object with one or more HTTP filters. Each filter specifies a specific modification to make to incoming requests, such as adding a custom header or modifying an existing header.

To add a header to a HTTP request, use a filter of the type `RequestHeaderModifier`{.docutils .literal .notranslate} with the `add`{.docutils .literal .notranslate} action and the name and value of the header.

You can find an example Gateway and HTTPRoute definition in `request-header.yaml`{.docutils .literal .notranslate}:

``` {#codecell2}
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: cilium-gw
spec:
  gatewayClassName: cilium
  listeners:
  - protocol: HTTP
    port: 80
    name: web-gw-echo
    allowedRoutes:
      namespaces:
        from: Same
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: header-http-echo
spec:
  parentRefs:
    - name: cilium-gw
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /add-a-request-header
      filters:
        - type: RequestHeaderModifier
          requestHeaderModifier:
            add:
              - name: my-header-name
                value: my-header-value
      backendRefs:
        - name: echo-1
          port: 8080
```

Copy First Line Copy All

This example adds a header named `my-header-name`{.docutils .literal .notranslate} with the `my-header-value`{.docutils .literal .notranslate} value.

Deploy the Gateway and the HTTPRoute:

``` {#codecell3 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/request-header.yaml
```

Copy Line

The preceding kubectl command creates a Gateway named `cilium-gw`{.docutils .literal .notranslate} that listens on port 80.

``` {#codecell4}
$ kubectl get gateway cilium-gw
NAME        CLASS    ADDRESS          PROGRAMMED   AGE
cilium-gw   cilium   172.18.255.200                8s
```

Copy First Line Copy Commands Copy All

Note

Some providers like EKS use a fully-qualified domain name rather than an IP address.

## Modify incoming HTTP Requests[](#modify-incoming-http-requests "Link to this heading")

Now that the Gateway is ready, you can make HTTP requests.

``` {#codecell5}
$ curl -s http://$GATEWAY/add-a-request-header
{
 "path": "/add-a-request-header",
 "host": "172.18.255.200",
 "method": "GET",
 "proto": "HTTP/1.1",
 "headers": {
  "Accept": [
   "*/*"
  ],
  "My-Header-Name": [
   "my-header-value"
  ],
  "User-Agent": [
   "curl/7.81.0"
  ],
  "X-Envoy-Internal": [
   "true"
  ],
  "X-Forwarded-For": [
   "172.18.0.1"
  ],
  "X-Forwarded-Proto": [
   "http"
  ],
  "X-Request-Id": [
   "61a72702-3dfa-4bc3-a21c-7544ef36af7b"
  ]
 },
 "httpPort": "3000",
 "namespace": "default",
 "ingress": "",
 "service": "",
 "pod": "echo-1-7d88f779b-m6r46"
}
```

Copy First Line Copy Commands Copy All

If the curl succeeds, you can see the HTTP Header from the incoming request in the body of the response sent back from the echo server. You can also see that the Gateway added the header.

You can also remove headers with the `remove`{.docutils .literal .notranslate} keyword and a list of header names.

``` {#codecell6}
filters
- type: RequestHeaderModifier
  requestHeaderModifier:
    remove: ["x-request-id"]
```

Copy First Line Copy All

Notice that the `x-request-id`{.docutils .literal .notranslate} header is removed when you add the `remove-a-request-header`{.docutils .literal .notranslate} prefix match to the filter:

``` {#codecell7}
$ curl --fail -s http://$GATEWAY/remove-a-request-header
{
 "path": "/remove-a-request-header",
 "host": "172.18.255.200",
 "method": "GET",
 "proto": "HTTP/1.1",
 "headers": {
  "Accept": [
   "*/*"
  ],
  "User-Agent": [
   "curl/7.81.0"
  ],
  "X-Envoy-Internal": [
   "true"
  ],
  "X-Forwarded-For": [
   "172.18.0.1"
  ],
  "X-Forwarded-Proto": [
   "http"
  ]
 },
 "httpPort": "3000",
 "namespace": "default",
 "ingress": "",
 "service": "",
 "pod": "echo-1-7d88f779b-m6r46"
}
```

Copy First Line Copy Commands Copy All

To edit an existing header, use the `set`{.docutils .literal .notranslate} action to specify the value of the header to modify as well as the new header value to set.

``` {#codecell8}
filters:
- type: RequestHeaderModifier
  requestHeaderModifier:
    set:
    - name: x-request-id
      value: set-cilium-header-value
```

Copy First Line Copy All

Notice that the `x-request-id`{.docutils .literal .notranslate} header is changed when you add the `edit-a-request-header`{.docutils .literal .notranslate} prefix match to the filter:

``` {#codecell9}
$ curl -s http://$GATEWAY/edit-a-request-header
{
 "path": "/edit-a-request-header",
 "host": "172.18.255.200",
 "method": "GET",
 "proto": "HTTP/1.1",
 "headers": {
  "Accept": [
   "*/*"
  ],
  "User-Agent": [
   "curl/7.81.0"
  ],
  "X-Envoy-Internal": [
   "true"
  ],
  "X-Forwarded-For": [
   "172.18.0.1"
  ],
  "X-Forwarded-Proto": [
   "http"
  ],
  "X-Request-Id": [
   "set-cilium-header-value"
  ]
 },
 "httpPort": "3000",
 "namespace": "default",
 "ingress": "",
 "service": "",
 "pod": "echo-1-7d88f779b-m6r46"
}
```

Copy First Line Copy Commands Copy All
