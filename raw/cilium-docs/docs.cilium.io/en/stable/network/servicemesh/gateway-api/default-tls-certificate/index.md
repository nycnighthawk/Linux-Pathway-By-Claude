---
{"title": "Default TLS Certificate", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/default-tls-certificate/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Default TLS Certificate[](#default-tls-certificate "Link to this heading")

A default TLS certificate acts as a fallback when no other certificates match the hostname specified in the SNI header, or when SNI is absent. The Gateway API specification does not natively support a default TLS certificate. Instead, a listener with an empty `spec.listeners[].hostname`{.docutils .literal .notranslate} field matches all hostnames, effectively serving as a fallback for that specific protocol and port.

In this example, we will deploy a simple HTTP service and expose it via the Cilium Gateway API.

We will use the `bookinfo`{.docutils .literal .notranslate} sample application from the Istio project.

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

## Create TLS Certificate and Private Key[](#create-tls-certificate-and-private-key "Link to this heading")

For demonstration purposes we will use a TLS certificate signed by a made-up, [self-signed](https://cert-manager.io/docs/faq/terminology/#what-does-self-signed-mean-is-my-ca-self-signed) certificate authority (CA). One easy way to do this is with [mkcert](https://github.com/FiloSottile/mkcert). We want a certificate that will validate `bookinfo.cilium.rocks`{.docutils .literal .notranslate} and `hipstershop.cilium.rocks`{.docutils .literal .notranslate}, as these are the host names used in this example.

``` {#codecell2}
$ mkcert bookinfo.cilium.rocks hipstershop.cilium.rocks
Note: the local CA is not installed in the system trust store.
Run "mkcert -install" for certificates to be trusted automatically ⚠️

Created a new certificate valid for the following names 📜
 - "bookinfo.cilium.rocks"
 - "hipstershop.cilium.rocks"

The certificate is at "./bookinfo.cilium.rocks+1.pem" and the key at "./bookinfo.cilium.rocks+1-key.pem" ✅

It will expire on 29 November 2026 🗓
```

Copy First Line Copy Commands Copy All

Create a Kubernetes secret with this demo key and certificate:

``` {#codecell3}
$ kubectl create secret tls demo-cert --key=bookinfo.cilium.rocks+1-key.pem --cert=bookinfo.cilium.rocks+1.pem
```

Copy Line

Let us install cert-manager:

``` {#codecell4}
$ helm repo add jetstack https://charts.jetstack.io
$ helm install cert-manager jetstack/cert-manager --version v1.16.2 \
    --namespace cert-manager \
    --set crds.enabled=true \
    --create-namespace \
    --set config.apiVersion="controller.config.cert-manager.io/v1alpha1" \
    --set config.kind="ControllerConfiguration" \
    --set config.enableGatewayAPI=true
```

Copy First Line Copy Commands Copy All

Now, create a CA Issuer:

``` {#codecell5 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/ca-issuer.yaml
```

Copy Line

## Deploy the Gateway and HTTPRoutes[](#deploy-the-gateway-and-httproutes "Link to this heading")

In this example, a single certificate serves all incoming TLS connections, which are then routed to the appropriate backend based on the hostnames defined in the HTTPRoutes.

``` {#codecell6}
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: tls-gateway
spec:
  gatewayClassName: cilium
  listeners:
  - name: default
    protocol: HTTPS
    port: 443
    tls:
      certificateRefs:
      - kind: Secret
        name: demo-cert
      mode: Terminate
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: bookinfo
spec:
  parentRefs:
  - name: tls-gateway
    sectionName: default
  hostnames:
  - "bookinfo.cilium.rocks"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: details
      port: 9080
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: hipstershop
spec:
  parentRefs:
  - name: tls-gateway
    sectionName: default
  hostnames:
  - "hipstershop.cilium.rocks"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: productpage
      port: 9080
```

Copy First Line Copy All

Apply the configuration:

``` {#codecell7 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/https-default-tls-certificate.yaml
```

Copy Line

Once the Gateway and HTTPRoutes are deployed, you can find external IP address in Gateway, and ensure hostnames are valid in HTTPRoute.

``` {#codecell8}
$ kubectl get gateway tls-gateway
NAME          CLASS    ADDRESS          PROGRAMMED   AGE
tls-gateway   cilium   172.18.255.200   True         27m

$ kubectl get httproute bookinfo hipstershop
NAME          HOSTNAMES                      AGE
bookinfo      ["bookinfo.cilium.rocks"]      27m
hipstershop   ["hipstershop.cilium.rocks"]   27m
```

Copy First Line Copy Commands Copy All

## Make HTTPS Requests[](#make-https-requests "Link to this heading")

By specifying the CA's certificate in a curl request, you can indicate that you trust certificates signed by that CA.

``` {#codecell9}
$ curl --cacert minica.pem -v https://bookinfo.cilium.rocks/details/1 --resolve bookinfo.cilium.rocks:443:172.18.255.200
$ curl --cacert minica.pem -v https://hipstershop.cilium.rocks/ --resolve hipstershop.cilium.rocks:443:172.18.255.200
...
*   subjectAltName: "bookinfo.cilium.rocks" matches cert's "bookinfo.cilium.rocks"
* SSL certificate verified via OpenSSL.
```

Copy First Line Copy Commands Copy All

You should see no warning messages, as the TLS certificate was issued for the requested hostnames.

The following request demonstrates that when accessing the service via an IP address, the client does not provide an SNI header. This typically occurs when Cilium acts as a backend for a load balancer or proxy that uses an IP address to establish connections. Despite the lack of SNI, a TLS connection is still established using the default certificate. Note that since the certificate's hostname will not match the IP address, we use the `-k`{.docutils .literal .notranslate} flag in curl to bypass validation.

Subsequent routing to the correct backend is then determined by the `Host`{.docutils .literal .notranslate} HTTP header, which we provide explicitly in this example.

``` {#codecell10}
$ curl -H "Host: hipstershop.cilium.rocks" -k -v https://172.18.255.200/
...
*  SSL certificate verification failed, continuing anyway!
* Established connection to 172.18.255.200 (172.18.255.200 port 443) from 10.244.0.52 port 42458
```

Copy First Line Copy Commands Copy All

By specifying `-v`{.docutils .literal .notranslate} in the curl request, you can see that the TLS handshake was successful.

By specifying the CA's certificate in a curl request, you can indicate that you trust certificates signed by that CA.

``` {#codecell11}
$ curl --cacert cm-cert.pem -v https://bookinfo.cilium.rocks/details/1 --resolve bookinfo.cilium.rocks:443:172.18.255.200
$ curl --cacert cm-cert.pem -v https://hipstershop.cilium.rocks/ --resolve hipstershop.cilium.rocks:443:172.18.255.200
...
*   subjectAltName: "bookinfo.cilium.rocks" matches cert's "bookinfo.cilium.rocks"
* SSL certificate verified via OpenSSL.
```

Copy First Line Copy Commands Copy All

You should see no warning messages, as the TLS certificate was issued for the requested hostnames.

The following request demonstrates that when accessing the service via an IP address, the client does not provide an SNI header. This typically occurs when Cilium acts as a backend for a load balancer or proxy that uses an IP address to establish connections. Despite the lack of SNI, a TLS connection is still established using the default certificate. Note that since the certificate's hostname will not match the IP address, we use the `-k`{.docutils .literal .notranslate} flag in curl to bypass validation.

Subsequent routing to the correct backend is then determined by the `Host`{.docutils .literal .notranslate} HTTP header, which we provide explicitly in this example.

``` {#codecell12}
$ curl -H "Host: hipstershop.cilium.rocks" -k -v https://172.18.255.200/
...
*  SSL certificate verification failed, continuing anyway!
* Established connection to 172.18.255.200 (172.18.255.200 port 443) from 10.244.0.52 port 42458
```

Copy First Line Copy Commands Copy All

By specifying `-v`{.docutils .literal .notranslate} in the curl request, you can see that the TLS handshake was successful.
