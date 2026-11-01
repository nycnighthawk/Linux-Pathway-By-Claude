---
{"title": "HTTPS Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/https/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# HTTPS Example[](#https-example "Link to this heading")

This example builds on the previous [HTTP Example](../http/#gs-gateway-http) and add TLS termination for two HTTP routes. For simplicity, the second route to `productpage`{.docutils .literal .notranslate} is omitted.

``` {#codecell0}
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: tls-gateway
spec:
  gatewayClassName: cilium
  listeners:
  - name: https-1
    protocol: HTTPS
    port: 443
    hostname: "bookinfo.cilium.rocks"
    tls:
      certificateRefs:
      - kind: Secret
        name: ca
  - name: https-2
    protocol: HTTPS
    port: 443
    hostname: "hipstershop.cilium.rocks"
    tls:
      certificateRefs:
      - kind: Secret
        name: ca
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: https-app-route-1
spec:
  parentRefs:
  - name: tls-gateway
  hostnames:
  - "bookinfo.cilium.rocks"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /details
    backendRefs:
    - name: details
      port: 9080
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: https-app-route-2
spec:
  parentRefs:
  - name: tls-gateway
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

## Create TLS Certificate and Private Key[](#create-tls-certificate-and-private-key "Link to this heading")

For demonstration purposes we will use a TLS certificate signed by a made-up, [self-signed](https://cert-manager.io/docs/faq/terminology/#what-does-self-signed-mean-is-my-ca-self-signed) certificate authority (CA). One easy way to do this is with [mkcert](https://github.com/FiloSottile/mkcert). We want a certificate that will validate `bookinfo.cilium.rocks`{.docutils .literal .notranslate} and `hipstershop.cilium.rocks`{.docutils .literal .notranslate}, as these are the host names used in this example.

``` {#codecell1}
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

``` {#codecell2}
$ kubectl create secret tls demo-cert --key=bookinfo.cilium.rocks+1-key.pem --cert=bookinfo.cilium.rocks+1.pem
```

Copy Line

Let us install cert-manager:

``` {#codecell3}
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

``` {#codecell4 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/ca-issuer.yaml
```

Copy Line

## Deploy the Gateway and HTTPRoute[](#deploy-the-gateway-and-httproute "Link to this heading")

The Gateway configuration for this demo provides the similar routing to the `details`{.docutils .literal .notranslate} and `productpage`{.docutils .literal .notranslate} services.

``` {#codecell5 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/basic-https.yaml
```

Copy Line

``` {#codecell6 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/basic-https.yaml
```

Copy Line

To tell cert-manager that this Ingress needs a certificate, annotate the Gateway with the name of the CA issuer we previously created:

``` {#codecell7}
$ kubectl annotate gateway tls-gateway cert-manager.io/issuer=ca-issuer
```

Copy Line

This creates a Certificate object along with a Secret containing the TLS certificate.

``` {#codecell8}
$ kubectl get certificate,secret demo-cert
NAME                                    READY   SECRET      AGE
certificate.cert-manager.io/demo-cert   True    demo-cert   29s
NAME               TYPE                DATA   AGE
secret/demo-cert   kubernetes.io/tls   3      29s
```

Copy First Line Copy Commands Copy All

External IP address will be shown up in Gateway. Also, the host names should be shown up in related HTTPRoutes.

``` {#codecell9}
$ kubectl get gateway tls-gateway
NAME          CLASS    ADDRESS         PROGRAMMED   AGE
tls-gateway   cilium   10.104.247.23   True         29s

$ kubectl get httproutes https-app-route-1 https-app-route-2
NAME                HOSTNAMES                      AGE
https-app-route-1   ["bookinfo.cilium.rocks"]      29s
https-app-route-2   ["hipstershop.cilium.rocks"]   29s
```

Copy First Line Copy Commands Copy All

Update `/etc/hosts`{.docutils .literal .notranslate} with the host names and IP address of the Gateway:

``` {#codecell10}
$ sudo perl -ni -e 'print if !/\.cilium\.rocks$/d' /etc/hosts; sudo tee -a /etc/hosts \
  <<<"$(kubectl get gateway tls-gateway -o jsonpath='{.status.addresses[0].value}') bookinfo.cilium.rocks hipstershop.cilium.rocks"
```

Copy First Line Copy Commands Copy All

## Make HTTPS Requests[](#make-https-requests "Link to this heading")

By specifying the CA's certificate on a curl request, you can say that you trust certificates signed by that CA.

``` {#codecell11}
$ curl --cacert minica.pem -v https://bookinfo.cilium.rocks/details/1
$ curl --cacert minica.pem -v https://hipstershop.cilium.rocks/
```

Copy First Line Copy Commands Copy All

If you prefer, instead of supplying the CA you can specify `-k`{.docutils .literal .notranslate} to tell the curl client not to validate the server's certificate. Without either, you will get an error that the certificate was signed by an unknown authority.

Specifying -v on the curl request, you can see that the TLS handshake took place successfully.

``` {#codecell12}
$ curl https://bookinfo.cilium.rocks/details/1
$ curl https://hipstershop.cilium.rocks/
```

Copy First Line Copy Commands Copy All
