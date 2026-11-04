---
{"title": "Ingress Example with TLS Termination", "url": "https://docs.cilium.io/en/stable/network/servicemesh/tls-termination/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Ingress Example with TLS Termination[](#ingress-example-with-tls-termination "Link to this heading")

This example builds on the HTTP and gRPC ingress examples, adding TLS termination.

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

## Deploy the Ingress[](#deploy-the-ingress "Link to this heading")

The Ingress configuration for this demo provides the same routing as those demos but with the addition of TLS termination.

``` {#codecell5 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/tls-ingress.yaml
```

Copy Line

``` {#codecell6 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/tls-ingress.yaml
```

Copy Line

To tell cert-manager that this Ingress needs a certificate, annotate the Ingress with the name of the CA issuer we previously created:

``` {#codecell7}
$ kubectl annotate ingress tls-ingress cert-manager.io/issuer=ca-issuer
```

Copy Line

This creates a Certificate object along with a Secret containing the TLS certificate.

``` {#codecell8}
$ kubectl get certificate,secret demo-cert
NAME                                    READY   SECRET      AGE
certificate.cert-manager.io/demo-cert   True    demo-cert   33m
NAME               TYPE                DATA   AGE
secret/demo-cert   kubernetes.io/tls   3      33m
```

Copy First Line Copy Commands Copy All

External IP address will be shown up in Ingress

``` {#codecell9}
$ kubectl get ingress
NAME          CLASS    HOSTS                                            ADDRESS        PORTS     AGE
tls-ingress   cilium   hipstershop.cilium.rocks,bookinfo.cilium.rocks   35.195.24.75   80, 443   6m5s
```

Copy First Line Copy Commands Copy All

In this Ingress configuration, the host names `hipstershop.cilium.rocks`{.docutils .literal .notranslate} and `bookinfo.cilium.rocks`{.docutils .literal .notranslate} are specified in the path routing rules. The client needs to specify which host it wants to access. This can be achieved by editing your local `` /etc/hosts` ``{.docutils .literal .notranslate} file. (You will almost certainly need to be superuser to edit this file.) Add entries using the IP address assigned to the ingress service, so your file looks something like this:

``` {#codecell10}
$ sudo perl -ni -e 'print if !/\.cilium\.rocks$/d' /etc/hosts; sudo tee -a /etc/hosts \
  <<<"$(kubectl get ing tls-ingress -o=jsonpath='{.status.loadBalancer.ingress[0].ip}') bookinfo.cilium.rocks hipstershop.cilium.rocks"
```

Copy First Line Copy Commands Copy All

## Make HTTPS Requests[](#make-https-requests "Link to this heading")

By specifying the CA's certificate on a curl request, you can say that you trust certificates signed by that CA.

``` {#codecell11}
$ curl --cacert minica.pem -v https://bookinfo.cilium.rocks/details/1
```

Copy Line

If you prefer, instead of supplying the CA you can specify `-k`{.docutils .literal .notranslate} to tell the curl client not to validate the server's certificate. Without either, you will get an error that the certificate was signed by an unknown authority.

Specifying -v on the curl request, you can see that the TLS handshake took place successfully.

Similarly you can specify the CA on a gRPC request like this:

``` {#codecell12}
# Download demo.proto file if you have not done before
$ curl -o demo.proto https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/main/protos/demo.proto
$ grpcurl -proto ./demo.proto -cacert minica.pem hipstershop.cilium.rocks:443 hipstershop.ProductCatalogService/ListProducts
```

Copy First Line Copy Commands Copy All

``` {#codecell13}
$ curl https://bookinfo.cilium.rocks/details/1
```

Copy Line

Similarly you can specify the CA on a gRPC request like this:

``` {#codecell14}
grpcurl -proto ./demo.proto -cacert minica.pem hipstershop.cilium.rocks:443 hipstershop.ProductCatalogService/ListProducts
```

Copy Line

Note

See the gRPC Ingress example if you don't already have the `demo.proto`{.docutils .literal .notranslate} file downloaded.

You can also visit [https://bookinfo.cilium.rocks](https://bookinfo.cilium.rocks) in your browser. The browser might warn you that the certificate authority is unknown but if you proceed past this, you should see the bookstore application home page.

Note that requests will time out if you don't specify `https://`{.docutils .literal .notranslate}.
