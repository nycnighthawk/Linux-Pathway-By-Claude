---
{"title": "gRPC Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/grpc/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# gRPC Example[](#grpc-example "Link to this heading")

This example demonstrates how to set up a Gateway that terminates TLS traffic and routes requests to a gRPC service (i.e. using HTTP/2). In order for this example to work, ALPN support needs to be enabled with the Helm flag `gatewayAPI.enableAlpn`{.docutils .literal .notranslate} set to true. This enables clients to request HTTP/2 through the TLS negotiation.

``` {#codecell0}
apiVersion: gateway.networking.k8s.io/v1beta1
kind: Gateway
metadata:
  name: tls-gateway
spec:
  gatewayClassName: cilium
  listeners:
  - name: https
    protocol: HTTPS
    port: 443
    hostname: grpc-echo.cilium.rocks
    tls:
      certificateRefs:
      - kind: Secret
        name: grpc-certificate
---
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: grpc-route
spec:
  parentRefs:
  - name: tls-gateway
  rules:
  - backendRefs:
    - name: grpc-echo
      port: 7070
---
apiVersion: v1
kind: Service
metadata:
  name: grpc-echo
spec:
  selector:
    app.kubernetes.io/name: grpc-echo
  ports:
    - name: grpc
      port: 7070
      # This is needed to instruct the route to use plaintext HTTP/2 or
      # you will get protocol errors.
      appProtocol: kubernetes.io/h2c
      targetPort: grpc
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: grpc-echo
  labels:
    app.kubernetes.io/name: grpc-echo
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: grpc-echo
  template:
    metadata:
      labels:
        app.kubernetes.io/name: grpc-echo
    spec:
      containers:
        - name: app
          image: gcr.io/istio-testing/app:latest
          ports:
            - name: grpc
              containerPort: 7070
          readinessProbe:
            failureThreshold: 2
            grpc:
              port: 7070
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
```

Copy First Line Copy All

This example uses a TLS certificate signed by a made-up, [self-signed](https://cert-manager.io/docs/faq/terminology/#what-does-self-signed-mean-is-my-ca-self-signed) certificate authority (CA). One easy way to do this is with [mkcert](https://github.com/FiloSottile/mkcert). The certificate will validate the hostname `grpc-echo.cilium.rocks`{.docutils .literal .notranslate} used in this example.

``` {#codecell1}
$ mkcert bookinfo.cilium.rocks hispter.cilium.rocks
Created a new local CA 💥
Note: the local CA is not installed in the system trust store.
Run "mkcert -install" for certificates to be trusted automatically ⚠

Created a new certificate valid for the following names 📜
 - "grpc-echo.cilium.rocks"

The certificate is at "./grpc-echo.cilium.rocks.pem" and the key at "./grpc-echo.cilium.rocks-key.pem" ✅

It will expire on 28 September 2027 🗓
```

Copy First Line Copy Commands Copy All

Create a Kubernetes secret with this demo key and certificate:

``` {#codecell2}
$ kubectl create secret tls grpc-certificate --key=grpc-echo.cilium.rocks-key.pem --cert=grpc-echo.cilium.rocks.pem
```

Copy Line

Install cert-manager:

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

## Deploy the Gateway and GRPCRoute[](#deploy-the-gateway-and-grpcroute "Link to this heading")

This sets up a simple gRPC echo server and a Gateway to expose it.

``` {#codecell5 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/grpc-tls-termination.yaml
```

Copy Line

The self-signed certificate Secrets from the previous step will be used by this Gateway.

``` {#codecell6 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/grpc-tls-termination.yaml
```

Copy Line

To tell cert-manager that this Gateway needs a certificate, annotate the Gateway with the name of the CA issuer you created previously:

``` {#codecell7}
$ kubectl annotate gateway tls-gateway cert-manager.io/issuer=ca-issuer
```

Copy Line

This creates a Certificate object along with a Secret containing the TLS certificate.

``` {#codecell8}
$ kubectl get certificate,secret grpc-certificate
NAME                                           READY   SECRET             AGE
certificate.cert-manager.io/grpc-certificate   True    grpc-certificate   83s
NAME                      TYPE                DATA   AGE
secret/grpc-certificate   kubernetes.io/tls   3      78s
```

Copy First Line Copy Commands Copy All

External IP address will be shown up in Gateway. Also, the host names should show up in related HTTPRoutes.

``` {#codecell9}
$ kubectl get gateway tls-gateway
NAME          CLASS    ADDRESS         PROGRAMMED   AGE
tls-gateway   cilium   10.104.247.23   True         29s

$ kubectl get grpcroutes
NAME         HOSTNAMES   AGE
grpc-route               116s
```

Copy First Line Copy Commands Copy All

## gRPC-web Translation[](#grpc-web-translation "Link to this heading")

Cilium Gateway API enables Envoy's gRPC-web to gRPC request translation by default. To pass gRPC-web requests through unchanged for all Gateways using a parameterized GatewayClass, set `httpOptions.grpcWebTranslation.enabled`{.docutils .literal .notranslate} to `false`{.docutils .literal .notranslate} in the `CiliumGatewayClassConfig`{.docutils .literal .notranslate} referenced by the `GatewayClass`{.docutils .literal .notranslate}. See [Disable gRPC-web translation](../parameterized-gatewayclass/#gs-gateway-disable-grpc-web-translation) for an example.

Update `/etc/hosts`{.docutils .literal .notranslate} with the host names and IP address of the Gateway:

``` {#codecell10}
$ sudo perl -ni -e 'print if !/\.cilium\.rocks$/d' /etc/hosts; sudo tee -a /etc/hosts \
  <<<"$(kubectl get gateway tls-gateway -o jsonpath='{.status.addresses[0].value}') grpc-echo.cilium.rocks"
```

Copy First Line Copy Commands Copy All

## Make gRPC Requests[](#make-grpc-requests "Link to this heading")

You can use the [grpcurl](https://github.com/fullstorydev/grpcurl) cli tool to verify that the service works correctly. The echo server used in this example will respond with information about the HTTP/2 request the client made.

By specifying the CA's certificate on a curl request, you can say that you trust certificates signed by that CA.

``` {#codecell11}
$ grpcurl -cacert ~/.local/share/mkcert/rootCA.pem grpc-echo.cilium.rocks:443 proto.EchoTestService/Echo
```

Copy Line

If you prefer, instead of supplying the CA you can specify `-insecure`{.docutils .literal .notranslate} to tell the curl client not to validate the server's certificate. Without either, you will get an error that the certificate was signed by an unknown authority.

``` {#codecell12}
$ grpcurl grpc-echo.cilium.rocks:443 proto.EchoTestService/Echo
{
  "message": "Host=grpc-echo.cilium.rocks:443\nRequestHeader=:authority:grpc-echo.cilium.rocks:443\nRequestHeader=content-type:application/grpc\nRequestHeader=grpc-accept-encoding:gzip\nRequestHeader=x-forwarded-proto:https\nRequestHeader=x-request-id:f7889cda-08b2-45cf-9329-833633ae8d9c\nRequestHeader=user-agent:grpcurl/dev-build (no version set) grpc-go/1.61.0\nRequestHeader=x-forwarded-for:172.22.0.7\nRequestHeader=x-envoy-internal:true\nStatusCode=200\nServiceVersion=\nServicePort=7070\nIP=10.244.1.101\nProto=GRPC\nEcho=\nHostname=grpc-echo-6879fc6969-2kh6r\n"
}
```

Copy First Line Copy Commands Copy All
