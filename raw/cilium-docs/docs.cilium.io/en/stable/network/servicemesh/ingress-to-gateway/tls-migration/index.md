---
{"title": "TLS Migration", "url": "https://docs.cilium.io/en/stable/network/servicemesh/ingress-to-gateway/tls-migration/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# TLS Migration[](#tls-migration "Link to this heading")

This migration example builds on the previous [HTTP Migration Example](../http-migration/#gs-gateway-http-migration) and adds TLS termination for two HTTP routes. For simplicity, this example omits the second route to `productpage`{.docutils .literal .notranslate}.

## Review Ingress Configuration[](#review-ingress-configuration "Link to this heading")

You can find the example Ingress definition in `tls-ingress.yaml`{.docutils .literal .notranslate}.

``` {#codecell0}
# TLS ingress example, requires the below two applications
# https://raw.githubusercontent.com/istio/istio/release-1.11/samples/bookinfo/platform/kube/bookinfo.yaml
# https://github.com/GoogleCloudPlatform/microservices-demo
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-ingress
  namespace: default
spec:
  ingressClassName: cilium
  rules:
  - host: hipstershop.cilium.rocks
    http:
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
  - host: bookinfo.cilium.rocks
    http:
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
  tls:
  - hosts:
    - bookinfo.cilium.rocks
    - hipstershop.cilium.rocks
    secretName: demo-cert
```

Copy First Line Copy All

This example:

-   listens for HTTPS traffic on port 443.

-   terminates TLS for the `hipstershop.cilium.rocks`{.docutils .literal .notranslate} and `bookinfo.cilium.rocks`{.docutils .literal .notranslate} hostnames using the TLS certificate and key from the Secret *demo-cert*.

-   routes HTTPS requests for the `hipstershop.cilium.rocks`{.docutils .literal .notranslate} hostname with the URI prefix `/hipstershop.ProductCatalogService`{.docutils .literal .notranslate} to the *productcatalogservice* Service.

-   routes HTTPS requests for the `hipstershop.cilium.rocks`{.docutils .literal .notranslate} hostname with the URI prefix `/hipstershop.CurrencyService`{.docutils .literal .notranslate} to the *currencyservice* Service.

-   routes HTTPS requests for the `bookinfo.cilium.rocks`{.docutils .literal .notranslate} hostname with the URI prefix `/details`{.docutils .literal .notranslate} to the *details* Service.

-   routes HTTPS requests for the `bookinfo.cilium.rocks`{.docutils .literal .notranslate} hostname with any other prefix to the *productpage* Service.

## Create Equivalent Gateway Configuration[](#create-equivalent-gateway-configuration "Link to this heading")

To create the equivalent TLS termination configuration, consider the following:

-   TLS Termination

The Ingress resource supports TLS termination via the TLS section, where the TLS certificate and key are stored in a Kubernetes Secret.

``` {#codecell1}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-ingress
  namespace: default
[...]
spec:
  tls:
  - hosts:
    - bookinfo.cilium.rocks
    - hipstershop.cilium.rocks
    secretName: demo-cert
```

Copy First Line Copy All

In the Gateway API, TLS termination is a property of the Gateway listener, and similarly to the Ingress, a TLS certificate and key are also stored in a Secret.

``` {#codecell2}
apiVersion: gateway.networking.k8s.io/v1beta1
kind: Gateway
metadata:
  name: tls-gateway
spec:
  gatewayClassName: cilium
  listeners:
  - name: bookinfo.cilium.rocks
    protocol: HTTPS
    port: 443
    hostname: "bookinfo.cilium.rocks"
    tls:
      certificateRefs:
      - kind: Secret
        name: demo-cert
  - name: hipstershop.cilium.rocks
    protocol: HTTPS
    port: 443
    hostname: "hipstershop.cilium.rocks"
    tls:
      certificateRefs:
      - kind: Secret
        name: demo-cert
```

Copy First Line Copy All

-   Host-header-based Routing Rules

The Ingress API uses the term *host*. With Ingress, each host has separate routing rules.

``` {#codecell3}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-ingress
  namespace: default
spec:
  ingressClassName: cilium
rules:
- host: hipstershop.cilium.rocks
    http:
    paths:
    - backend:
        service:
            name: productcatalogservice
            port:
            number: 3550
        path: /hipstershop.ProductCatalogService
        pathType: Prefix
```

Copy First Line Copy All

The Gateway API uses the *hostname* term. The host-header-based routing rules map to the hostnames of the HTTPRoute. In the HTTPRoute, the routing rules apply to all hostnames.

The hostnames of an HTTPRoute must match the hostname of the Gateway listener. Otherwise, the listener will ignore the routing rules for the unmatched hostnames.

``` {#codecell4}
---
apiVersion: gateway.networking.k8s.io/v1beta1
kind: HTTPRoute
metadata:
  name: hipstershop-cilium-rocks
  namespace: default
spec:
  hostnames:
  - hipstershop.cilium.rocks
  parentRefs:
  - name: cilium-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /hipstershop.ProductCatalogService
    backendRefs:
    - name: productcatalogservice
      port: 3550
```

Copy First Line Copy All

## Review Equivalent Gateway Configuration[](#review-equivalent-gateway-configuration "Link to this heading")

You can find the equivalent final Gateway and HTTPRoute definition in `tls-migration.yaml`{.docutils .literal .notranslate}.

``` {#codecell5}
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: cilium-gateway
  namespace: default
spec:
  gatewayClassName: cilium
  listeners:
  - hostname: hipstershop.cilium.rocks
    name: hipstershop-cilium-rocks-http
    port: 80
    protocol: HTTP
  - hostname: hipstershop.cilium.rocks
    name: hipstershop-cilium-rocks-https
    port: 443
    protocol: HTTPS
    tls:
      certificateRefs:
      - kind: Secret
        name: demo-cert
  - hostname: bookinfo.cilium.rocks
    name: bookinfo-cilium-rocks-http
    port: 80
    protocol: HTTP
  - hostname: bookinfo.cilium.rocks
    name: bookinfo-cilium-rocks-https
    port: 443
    protocol: HTTPS
    tls:
      certificateRefs:
      - kind: Secret
        name: demo-cert
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: hipstershop-cilium-rocks
  namespace: default
spec:
  hostnames:
  - hipstershop.cilium.rocks
  parentRefs:
  - name: cilium-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /hipstershop.ProductCatalogService
    backendRefs:
    - name: productcatalogservice
      port: 3550
  - matches:
    - path:
        type: PathPrefix
        value: /hipstershop.CurrencyService
    backendRefs:
    - name: currencyservice
      port: 7000
      
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: bookinfo-cilium-rocks
  namespace: default
spec:
  hostnames:
  - bookinfo.cilium.rocks
  parentRefs:
  - name: cilium-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /details
    backendRefs:
    - name: details
      port: 9080
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: productpage
      port: 9080
```

Copy First Line Copy All

Deploy the resources and verify that HTTPS requests are routed successfully to the services. For more information, consult the Gateway API [HTTPS Example](../../gateway-api/https/#gs-gateway-https).
