---
{"title": "BackendTLSPolicy Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/backendtlspolicy/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# BackendTLSPolicy Example[](#backendtlspolicy-example "Link to this heading")

This example will use the `echo-server`{.docutils .literal .notranslate} sample application to demonstrate how to use BackendTLSPolicy.

You will need `mkcert`{.docutils .literal .notranslate} tool to generate certificates. See the tool's [upstream site](github-mkcert) for details.

This task uses a self-signed CA, and is only for demonstration purposes.

## Deploy `echo-server`{.docutils .literal .notranslate}[](#deploy-echo-server "Link to this heading")

Apply the following to deploy the `echo-server`{.docutils .literal .notranslate}.

``` {#codecell0}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: backend
---
apiVersion: v1
kind: Service
metadata:
  name: backend
  labels:
    app: backend
    service: backend
spec:
  ports:
    - name: http
      port: 3000
      targetPort: 3000
  selector:
    app: backend
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backend
      version: v1
  template:
    metadata:
      labels:
        app: backend
        version: v1
    spec:
      serviceAccountName: backend
      containers:
        - image: gcr.io/k8s-staging-gateway-api/echo-basic:v20231214-v1.0.0-140-gf544a46e
          imagePullPolicy: IfNotPresent
          name: backend
          ports:
            - containerPort: 3000
          env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
```

Copy First Line Copy All

Apply the following to create a Gateway and HTTPRoute for the `echo-server`{.docutils .literal .notranslate}:

``` {#codecell1}
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gateway 
spec:
  gatewayClassName: cilium
  listeners:
    - name: http
      protocol: HTTP
      port: 80
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: backend
spec:
  parentRefs:
    - name: my-gateway
  hostnames:
    - "www.example.com"
  rules:
    - backendRefs:
        - group: ""
          kind: Service
          name: backend
          port: 3000
          weight: 1
      matches:
        - path:
            type: PathPrefix
            value: /
```

Copy First Line Copy All

Test the sample application:

``` {#codecell2}
$ curl -v --resolve www.example.com:80:<GATEWAY_IP_ADDRESS> http://www.example.com/get
```

Copy Line

The curl command will return the information about the request. It should look like the following:

``` {#codecell3}
{
 "path": "/get",
 "host": "www.example.com",
 "method": "GET",
 "proto": "HTTP/1.1",
 "headers": {
  "Accept": [
   "*/*"
  ],
  "User-Agent": [
   "curl/8.20.0"
  ],
  "X-Envoy-Internal": [
   "true"
  ],
  "X-Forwarded-For": [
   "172.19.0.1"
  ],
  "X-Forwarded-Proto": [
   "http"
  ],
  "X-Request-Id": [
   "bb913f3e-7538-4873-88e4-25499fe5b3ff"
  ]
 },
 "namespace": "default",
 "ingress": "",
 "service": "",
 "pod": "backend-86c6c76f-ptczl"
}
```

Copy First Line Copy All

## Generate demo TLS Certificates[](#generate-demo-tls-certificates "Link to this heading")

Generate the certificates and keys for example.com.

First, create the root certificate.

``` {#codecell4}
mkcert www.example.com
```

Copy Line

This will output the certificate and key in the current directory.

## Create the secret and configmap in your cluster[](#create-the-secret-and-configmap-in-your-cluster "Link to this heading")

Store the cert and key into a Kubernetes Secret.

``` {#codecell5}
kubectl create secret tls example-cert --key=www.example.com-key.pem --cert=www.example.com.pem
```

Copy Line

Create a configmap in your cluster.

``` {#codecell6}
kubectl create configmap example-ca --from-file=ca.crt=www.example.com.pem
```

Copy Line

## Setup TLS between gateway and backend[](#setup-tls-between-gateway-and-backend "Link to this heading")

Patch the backend deployment to enable TLS. The following command mounts the TLS certificate secret into the backend container as a volume.

``` {#codecell7}
 kubectl patch deployment backend --type=json --patch '
- op: add
  path: /spec/template/spec/containers/0/volumeMounts
  value:
  - name: secret-volume
    mountPath: /etc/secret-volume
- op: add
  path: /spec/template/spec/volumes
  value:
  - name: secret-volume
    secret:
      secretName: example-cert
      items:
      - key: tls.crt
        path: crt
      - key: tls.key
        path: key
- op: add
  path: /spec/template/spec/containers/0/env/-
  value:
    name: TLS_SERVER_CERT
    value: /etc/secret-volume/crt
- op: add
  path: /spec/template/spec/containers/0/env/-
  value:
    name: TLS_SERVER_PRIVKEY
    value: /etc/secret-volume/key
'
```

Copy First Line Copy All

Configure the backend service to expose port 443. Apply the following to update `backend`{.docutils .literal .notranslate} service the ports to listen on 443:

``` {#codecell8}
apiVersion: v1
kind: Service
metadata:
  labels:
    app: backend
    service: backend
  name: backend
spec:
  selector:
    app: backend
  ports:
  - name: https
    port: 443
    protocol: TCP
    targetPort: 8443
```

Copy First Line Copy All

Create the BackendTLSPolicy to tell the Cilium Gateway to use a TLS connection with the backend.

``` {#codecell9}
apiVersion: gateway.networking.k8s.io/v1
kind: BackendTLSPolicy
metadata:
  name: enable-backend-tls
  namespace: default
spec:
  targetRefs:
  - group: ''
    kind: Service
    name: backend
    sectionName: https
  validation:
    caCertificateRefs:
    - name: example-ca
      group: ''
      kind: ConfigMap
    hostname: www.example.com
```

Copy First Line Copy All

Patch the HTTPRoute backend reference, so that it uses the correct port edited in the backend service.

``` {#codecell10}
kubectl patch HTTPRoute backend --type=json --patch '
 - op: replace
   path: /spec/rules/0/backendRefs/0/port
   value: 443
'
```

Copy First Line Copy All

## Testing the backend TLS connection[](#testing-the-backend-tls-connection "Link to this heading")

Try to curl the service through the Gateway.

``` {#codecell11}
$ curl -vI --resolve "www.example.com:80:<YOUR_GATEWAY_EXTERNAL_IP>" http://www.example.com:80/get
```

Copy Line

You should receive back a `200`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`OK`{.docutils .literal .notranslate} response. The curl response will look similar to the earlier curl response, but note that the response also demonstrates the TLS encryption details:

``` {#codecell12}
{
  "tls": {
   "version": "TLSv1.3",
   "serverName": "www.example.com",
   "negotiatedProtocol": "http/1.1",
   "cipherSuite": "TLS_AES_128_GCM_SHA256"
  }
 }
```

Copy First Line Copy All
