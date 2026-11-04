---
{"title": "Configure TLS with Hubble", "url": "https://docs.cilium.io/en/stable/observability/hubble/configuration/tls/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Configure TLS with Hubble[](#configure-tls-with-hubble "Link to this heading")

This page provides guidance to configure Hubble with TLS in a way that suits your environment. Instructions to enable Hubble are provided as part of each Cilium [Getting Started](../../../../#getting-started) guide.

## Enable TLS on the Hubble API[](#enable-tls-on-the-hubble-api "Link to this heading")

When Hubble Relay is deployed, Hubble listens on a TCP port on the host network. This allows Hubble Relay to communicate with all Hubble instances in the cluster. Connections between Hubble instances and Hubble Relay are secured using mutual TLS (mTLS) by default.

TLS certificates can be generated automatically or manually provided.

The following options are available to configure TLS certificates automatically:

-   cilium's [certgen](https://github.com/cilium/certgen) (using a Kubernetes `CronJob`{.docutils .literal .notranslate})

-   [cert-manager](https://cert-manager.io/)

-   [Helm](https://helm.sh/docs/chart_template_guide/function_list/#gensignedcert)

Each of these method handles certificate rotation differently, but the end result is the secrets containing the key pair will be updated. As Hubble server and Hubble Relay support TLS certificates hot reloading, including CA certificates, this does not disrupt any existing connection. New connections are automatically established using the new certificates without having to restart Hubble server or Hubble Relay.

When using certgen, TLS certificates are generated at installation time and a Kubernetes `CronJob`{.docutils .literal .notranslate} is scheduled to renew them (regardless of their expiration date). The certgen method is easier to implement than cert-manager but less flexible.

The following Helm values configure certgen:

``` {#codecell0}
hubble:
  tls:
    auto:
      # enable automatic TLS certificate generation
      enabled: true
      # auto generate certificates using cronJob method
      method: cronJob
      # certificates validity duration in days (default 3 years)
      certValidityDuration: 1095
      # schedule for certificates re-generation (crontab syntax)
      schedule: "0 0 1 */4 *"
```

Copy First Line Copy All

This method relies on [cert-manager](https://cert-manager.io/) to generate the TLS certificates. cert-manager is the de facto way to manage TLS certificates on Kubernetes, and it has the following advantages compared to the other documented methods:

-   Support for multiple issuers (e.g. a custom CA, [Vault](https://www.vaultproject.io/), [Let's Encrypt](https://letsencrypt.org/), [Google's Certificate Authority Service](https://cloud.google.com/certificate-authority-service), and more) allowing to choose the issuer fitting your organization's requirements.

-   Manages certificates via a [CRD](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) which is easier to inspect with Kubernetes tools than PEM files.

**Installation steps**:

1.  First, install [cert-manager](https://cert-manager.io/docs/installation/) and setup an [issuer](https://cert-manager.io/docs/configuration/). Please make sure that your issuer is able to create certificates under the `cilium.io`{.docutils .literal .notranslate} domain name.

2.  Install or upgrade Cilium with the following Helm values:

``` {#codecell1}
hubble:
  tls:
    auto:
      # enable automatic TLS certificate generation
      enabled: true
      # auto generate certificates using cert-manager
      method: certmanager
      # certificates validity duration in days (default 3 years)
      certValidityDuration: 1095
      certManagerIssuerRef:
        # Reference to cert-manager's issuer
        group: cert-manager.io
        kind: ClusterIssuer
        name: ca-issuer
```

Copy First Line Copy All

During the first Cilium installation, cert-manager's webhook might not yet be available when Cilium creates its `Certificate`{.docutils .literal .notranslate} resources. See [Troubleshooting](#hubble-enable-tls-troubleshooting) if that occurs.

When using Helm, TLS certificates are (re-)generated every time Helm is used to install or upgrade Cilium.

The following Helm values configure Helm certificate generation:

``` {#codecell2}
hubble:
  tls:
    auto:
      # enable automatic TLS certificate generation
      enabled: true
      # auto generate certificates using helm method
      method: helm
      # certificates validity duration in days (default 3 years)
      certValidityDuration: 1095
```

Copy First Line Copy All

The downside of the Helm method is that while certificates are automatically generated, they are not automatically renewed. Consequently, running `helm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`upgrade`{.docutils .literal .notranslate} is required when certificates are about to expire (i.e. before the configured `hubble.tls.auto.certValidityDuration`{.docutils .literal .notranslate}).

In order to provide your own TLS certificates, `hubble.tls.auto.enabled`{.docutils .literal .notranslate} must be set to `false`{.docutils .literal .notranslate}, secrets containing the certificates must be created in the namespace where Cilium is installed, which is typically `kube-system`{.docutils .literal .notranslate}, and the secret names must be provided to Helm.

The **Common Name (CN)** and **Subject Alternative Name (SAN)** of the certificates must be set as follows. `<cluster-name>`{.docutils .literal .notranslate} refers to the cluster name defined by `cluster.name`{.docutils .literal .notranslate} (defaults to `default`{.docutils .literal .notranslate}):

-   Hubble server: `*.<cluster-name>.hubble-grpc.cilium.io`{.docutils .literal .notranslate}

-   Hubble Relay: `*.hubble-relay.cilium.io`{.docutils .literal .notranslate}

-   Hubble UI: `*.hubble-ui.cilium.io`{.docutils .literal .notranslate}

-   Hubble metrics: `<cluster-name>.hubble-metrics.cilium.io`{.docutils .literal .notranslate}

Once the certificates have been issued, create the secrets in the target namespace.

Each secret must contain the following keys:

-   `tls.crt`{.docutils .literal .notranslate}: The certificate file.

-   `tls.key`{.docutils .literal .notranslate}: The private key file.

-   `ca.crt`{.docutils .literal .notranslate}: The CA certificate file.

The following examples demonstrates how to create the secrets.

Create the hubble server certificate secret:

``` {#codecell3}
$ kubectl -n kube-system create secret generic hubble-server-certs --from-file=hubble-server.crt --from-file=hubble-server.key --from-file=ca.crt
```

Copy Line

If hubble-relay is enabled, the following secrets must be created:

``` {#codecell4}
$ kubectl -n kube-system create secret generic hubble-relay-server-certs --from-file=hubble-relay-server.crt --from-file=hubble-relay-server.key --from-file=ca.crt
$ kubectl -n kube-system create secret generic hubble-relay-client-certs --from-file=hubble-relay-client.crt --from-file=hubble-relay-client.key --from-file=ca.crt
```

Copy First Line Copy Commands Copy All

If hubble-ui is enabled, the following secret must be created:

``` {#codecell5}
$ kubectl -n kube-system create secret generic hubble-ui-client-certs --from-file=hubble-ui-client.crt --from-file=hubble-ui-client.key --from-file=ca.crt
```

Copy Line

Lastly, if the Hubble metrics API is enabled, the following secret must be created:

``` {#codecell6}
$ kubectl -n kube-system create secret generic hubble-metrics-certs --from-file=hubble-metrics.crt --from-file=hubble-metrics.key --from-file=ca.crt
```

Copy Line

After the secrets have been created, provide their names to Helm and disable automatic certificate generation with the following Helm values:

``` {#codecell7}
hubble:
  tls:
    auto:
      # Disable automatic TLS certificate generation.
      enabled: false
    server:
      existingSecret: hubble-server-certs
  relay:
    tls:
      server:
        # Enable TLS on Hubble Relay (optional).
        enabled: true
        existingSecret: hubble-relay-server-certs
      client:
        existingSecret: hubble-relay-client-certs
  ui:
    tls:
      client:
        existingSecret: hubble-ui-client-certs
  metrics:
    tls:
      # Enable TLS on the Hubble metrics API (optional).
      enabled: true
      server:
        existingSecret: hubble-metrics-certs
```

Copy First Line Copy All

-   `hubble.relay.tls.server.existingSecret`{.docutils .literal .notranslate} and `hubble.ui.tls.client.existingSecret`{.docutils .literal .notranslate} only need to be provided when `hubble.relay.tls.server.enabled=true`{.docutils .literal .notranslate} (default `false`{.docutils .literal .notranslate}).

-   `hubble.ui.tls.client.existingSecret`{.docutils .literal .notranslate} only needs to be provided when `hubble.ui.enabled`{.docutils .literal .notranslate} (default `false`{.docutils .literal .notranslate}).

-   `hubble.metrics.tls.server.existingSecret`{.docutils .literal .notranslate} only needs to be provided when `hubble.metrics.tls.enabled`{.docutils .literal .notranslate} (default `false`{.docutils .literal .notranslate}). For more details on configuring the Hubble metrics API with TLS, see [Hubble Metrics TLS and Authentication](#hubble-configure-metrics-tls).

### Troubleshooting[](#troubleshooting "Link to this heading")

If you encounter issues after enabling TLS, you can use the following instructions to help diagnose the problem.

While installing Cilium or cert-manager you may get the following error:

``` {#codecell8}
Error: Internal error occurred: failed calling webhook "webhook.cert-manager.io": Post "https://cert-manager-webhook.cert-manager.svc:443/mutate?timeout=10s": dial tcp x.x.x.x:443: connect: connection refused
```

Copy Line

This happens when cert-manager's webhook (which is used to verify the `Certificate`{.docutils .literal .notranslate}'s CRD resources) is not available. There are several ways to resolve this issue. Pick one of the following options:

Install cert-manager CRDs before Cilium and cert-manager (see [cert-manager's documentation about installing CRDs with kubectl](https://cert-manager.io/docs/installation/helm/#option-1-installing-crds-with-kubectl)):

``` {#codecell9}
$ kubectl create -f cert-manager.crds.yaml
```

Copy Line

Then install cert-manager, configure an issuer, and install Cilium.

Upgrade Cilium from an installation with TLS disabled:

``` {#codecell10}
$ helm install cilium cilium/cilium \
    --set hubble.tls.enabled=false \
    ...
```

Copy First Line Copy Commands Copy All

Then install cert-manager, configure an issuer, and upgrade Cilium enabling TLS:

``` {#codecell11}
$ helm install cilium cilium/cilium --set hubble.tls.enabled=true
```

Copy Line

Disable cert-manager validation (assuming Cilium is installed in the `kube-system`{.docutils .literal .notranslate} namespace):

``` {#codecell12}
$ kubectl label namespace kube-system cert-manager.io/disable-validation=true
```

Copy Line

Then install Cilium, cert-manager, and configure an issuer.

Configure cert-manager to expose its webhook within the host network namespace:

``` {#codecell13}
$ helm install cert-manager jetstack/cert-manager \
        --set webhook.hostNetwork=true \
        --set 'webhook.tolerations[0].operator=Exists'
```

Copy First Line Copy Commands Copy All

Then configure an issuer and install Cilium.

When using Helm certificates are not automatically renewed. If you encounter issues with expired certificates, you can manually renew them by running `helm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`upgrade`{.docutils .literal .notranslate} to renew the certificates.

If you encounter issues with the certificates, you can check the certificates and keys by decoding them:

``` {#codecell14}
$ kubectl -n kube-system get secret hubble-server-certs -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -text -noout
$ kubectl -n kube-system get secret hubble-server-certs -o jsonpath='{.data.tls\.key}' | base64 -d | openssl rsa -text -noout
$ kubectl -n kube-system get secret hubble-server-certs -o jsonpath='{.data.ca\.crt}' | base64 -d | openssl x509 -text -noout
```

Copy First Line Copy Commands Copy All

The same commands can be used for the other secrets as well.

If hubble-relay is enabled but not responding or the pod is failing it's readiness probe, check the certificates and ensure the client certificate is issued by the CA (`ca.crt`{.docutils .literal .notranslate}) specified in the `hubble-server-certs`{.docutils .literal .notranslate} secret.

Additionally you must ensure the **Common Name (CN)** and **Subject Alternative Name (SAN)** of the certificate for Hubble server MUST be set to `*.{cluster-name}.hubble-grpc.cilium.io`{.docutils .literal .notranslate} where `{cluster-name}`{.docutils .literal .notranslate} is the cluster name defined by `cluster.name`{.docutils .literal .notranslate} (defaults to `default`{.docutils .literal .notranslate}).

### Validating the Installation[](#validating-the-installation "Link to this heading")

The following section guides you through validating that TLS is enabled for Hubble and the connection between Hubble Relay and Hubble Server is using mTLS to secure the session. Additionally, the commands below can be used to troubleshoot issues with your TLS configuration if you encounter any issues.

Before beginning verify TLS has been configured correctly by running the following command:

``` {#codecell15}
$ kubectl get configmap -n kube-system cilium-config -oyaml | grep hubble-disable-tls
  hubble-disable-tls: "false"
```

Copy First Line Copy Commands Copy All

You should see that the `hubble-disable-tls`{.docutils .literal .notranslate} configuration option is set to `false`{.docutils .literal .notranslate}.

Start by creating a Hubble CLI pod within the namespace that Hubble components are running in (for example: `kube-system`{.docutils .literal .notranslate}):

``` {#codecell16}
$ kubectl apply -n kube-system -f https://raw.githubusercontent.com/cilium/cilium/main/examples/hubble/hubble-cli.yaml
```

Copy Line

List Hubble Servers by running `hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`watch`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`peers`{.docutils .literal .notranslate} within the newly created pod:

``` {#codecell17}
$ kubectl exec -it -n kube-system deployment/hubble-cli -- \
hubble watch peers --server unix:///var/run/cilium/hubble.sock

PEER_ADDED   172.18.0.2 kind-worker (TLS.ServerName: kind-worker.default.hubble-grpc.cilium.io)
PEER_ADDED   172.18.0.3 kind-control-plane (TLS.ServerName: kind-control-plane.kind.hubble-grpc.cilium.io)
```

Copy First Line Copy Commands Copy All

Copy the IP and the server name of the first peer into the following environment variables for the next steps:

Note

If the `TLS.ServerName`{.docutils .literal .notranslate} is missing from your output then TLS is not enabled for the Hubble server and the following steps will not work. If this is the case, please refer to the previous sections to enable TLS.

``` {#codecell18}
$ IP=172.18.0.2
$ SERVERNAME=kind-worker.default.hubble-grpc.cilium.io
```

Copy First Line Copy Commands Copy All

Connect to the first peer with the Hubble Relay client certificate to confirm that the Hubble server is accepting connections from clients who present the correct certificate:

``` {#codecell19}
$ kubectl exec -it -n kube-system deployment/hubble-cli -- \
hubble observe --server tls://${IP?}:4244 \
    --tls-server-name ${SERVERNAME?} \
    --tls-ca-cert-files /var/lib/hubble-relay/tls/hubble-server-ca.crt \
    --tls-client-cert-file /var/lib/hubble-relay/tls/client.crt \
    --tls-client-key-file /var/lib/hubble-relay/tls/client.key

Dec 13 08:49:58.888: 10.20.1.124:60588 (host) -> kube-system/coredns-565d847f94-pp8zs:8181 (ID:7518) to-endpoint FORWARDED (TCP Flags: SYN)
Dec 13 08:49:58.888: 10.20.1.124:36308 (host) <- kube-system/coredns-565d847f94-pp8zs:8080 (ID:7518) to-stack FORWARDED (TCP Flags: SYN, ACK)
Dec 13 08:49:58.888: 10.20.1.124:60588 (host) <- kube-system/coredns-565d847f94-pp8zs:8181 (ID:7518) to-stack FORWARDED (TCP Flags: SYN, ACK)
...
...
```

Copy First Line Copy Commands Copy All

Now try to query the Hubble server without providing any client certificate:

``` {#codecell20}
$ kubectl exec -it -n kube-system deployment/hubble-cli -- \
hubble observe --server tls://${IP?}:4244 \
    --tls-server-name ${SERVERNAME?} \
    --tls-ca-cert-files /var/lib/hubble-relay/tls/hubble-server-ca.crt

failed to connect to '172.18.0.2:4244': context deadline exceeded: connection error: desc = "error reading server preface: remote error: tls: certificate requiredd"
command terminated with exit code 1
```

Copy First Line Copy Commands Copy All

You can also try to connect without TLS:

``` {#codecell21}
$ kubectl exec -it -n kube-system deployment/hubble-cli -- \
hubble observe --server ${IP?}:4244

failed to connect to '172.18.0.2:4244': context deadline exceeded: connection error: desc = "error reading server preface: EOF"
command terminated with exit code 1
```

Copy First Line Copy Commands Copy All

To troubleshoot the connection, install OpenSSL in the Hubble CLI pod:

``` {#codecell22}
$ kubectl exec -it -n kube-system deployment/hubble-cli -- apk add --update openssl
```

Copy Line

Then, use OpenSSL to connect to the Hubble server get more details about the TLS handshake:

``` {#codecell23}
$ kubectl exec -it -n kube-system deployment/hubble-cli -- \
openssl s_client -showcerts -servername ${SERVERNAME} -connect ${IP?}:4244 \
-CAfile /var/lib/hubble-relay/tls/hubble-server-ca.crt

CONNECTED(00000004)
depth=1 C = US, ST = San Francisco, L = CA, O = Cilium, OU = Cilium, CN = Cilium CA
verify return:1
depth=0 CN = *.default.hubble-grpc.cilium.io
verify return:1
---
Certificate chain
 0 s:CN = *.default.hubble-grpc.cilium.io
   i:C = US, ST = San Francisco, L = CA, O = Cilium, OU = Cilium, CN = Cilium CA
   a:PKEY: id-ecPublicKey, 256 (bit); sigalg: ecdsa-with-SHA256
   v:NotBefore: Aug 15 17:39:00 2024 GMT; NotAfter: Aug 15 17:39:00 2027 GMT
-----BEGIN CERTIFICATE-----
MIICNzCCAd2gAwIBAgIUAlgykDuc1J+mzseHS0pREX6Uv3cwCgYIKoZIzj0EAwIw
aDELMAkGA1UEBhMCVVMxFjAUBgNVBAgTDVNhbiBGcmFuY2lzY28xCzAJBgNVBAcT
AkNBMQ8wDQYDVQQKEwZDaWxpdW0xDzANBgNVBAsTBkNpbGl1bTESMBAGA1UEAxMJ
Q2lsaXVtIENBMB4XDTI0MDgxNTE3MzkwMFoXDTI3MDgxNTE3MzkwMFowKjEoMCYG
A1UEAwwfKi5kZWZhdWx0Lmh1YmJsZS1ncnBjLmNpbGl1bS5pbzBZMBMGByqGSM49
AgEGCCqGSM49AwEHA0IABGjtY50MM21TolEy5RUrBa6WqHsw7PjNB3MhYLCsuJmO
aQ1tIy6J2e7a9Cw2jmBlyj+dL8g0YLhRQX4n+leItSSjgaIwgZ8wDgYDVR0PAQH/
BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAwGA1UdEwEB/wQCMAAwHQYDVR0O
BBYEFCDf5epVs8yyyZCdtBzc90HrQzpFMB8GA1UdIwQYMBaAFDKuJMmhNPJ71FvB
AyHEMztI62NbMCoGA1UdEQQjMCGCHyouZGVmYXVsdC5odWJibGUtZ3JwYy5jaWxp
dW0uaW8wCgYIKoZIzj0EAwIDSAAwRQIhAP0kyl0Eb7FBQw1uZE+LWnRyr5GDsB3+
6rA/Rx042XZgAiBZML3lOW60tWMI1Pyn4cR4trFbzZpsUSwnQmOAb+paEw==
-----END CERTIFICATE-----
---
Server certificate
subject=CN = *.default.hubble-grpc.cilium.io
issuer=C = US, ST = San Francisco, L = CA, O = Cilium, OU = Cilium, CN = Cilium CA
---
Acceptable client certificate CA names
C = US, ST = San Francisco, L = CA, O = Cilium, OU = Cilium, CN = Cilium CA
Requested Signature Algorithms: RSA-PSS+SHA256:ECDSA+SHA256:Ed25519:RSA-PSS+SHA384:RSA-PSS+SHA512:RSA+SHA256:RSA+SHA384:RSA+SHA512:ECDSA+SHA384:ECDSA+SHA512:RSA+SHA1:ECDSA+SHA1
Shared Requested Signature Algorithms: RSA-PSS+SHA256:ECDSA+SHA256:Ed25519:RSA-PSS+SHA384:RSA-PSS+SHA512:RSA+SHA256:RSA+SHA384:RSA+SHA512:ECDSA+SHA384:ECDSA+SHA512
Peer signing digest: SHA256
Peer signature type: ECDSA
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1106 bytes and written 437 bytes
Verification: OK
---
New, TLSv1.3, Cipher is TLS_AES_128_GCM_SHA256
Server public key is 256 bit
This TLS version forbids renegotiation.
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
08EBFFFFFF7F0000:error:0A00045C:SSL routines:ssl3_read_bytes:tlsv13 alert certificate required:ssl/record/rec_layer_s3.c:1605:SSL alert number 116
command terminated with exit code 1
```

Copy First Line Copy Commands Copy All

Breaking the output down:

-   `Server`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Certificate`{.docutils .literal .notranslate}: This is the server certificate presented by the server.

-   `Acceptable`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`client`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`certificate`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`CA`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`names`{.docutils .literal .notranslate}: These are the CA names that the server accepts for client certificates.

-   `SSL`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`handshake`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`has`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`read`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`1108`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bytes`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`and`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`written`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`387`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`bytes`{.docutils .literal .notranslate}: Details on the handshake. Errors could be presented here if any occurred.

-   `Verification:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`OK`{.docutils .literal .notranslate}: The server certificate is valid.

-   `Verify`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`return`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`code:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`0`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`(ok)`{.docutils .literal .notranslate}: The server certificate was verified successfully.

-   `error:0A00045C:SSL`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`routines:ssl3_read_bytes:tlsv13`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`alert`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`certificate`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`required`{.docutils .literal .notranslate}: The server requires a client certificate to be provided. Since a client certificate was not provided, the connection failed.

If you provide the correct client certificate and key, the connection should be successful:

``` {#codecell24}
$ kubectl exec -i -n kube-system deployment/hubble-cli -- \
openssl s_client -showcerts -servername ${SERVERNAME} -connect ${IP?}:4244 \
  -CAfile /var/lib/hubble-relay/tls/hubble-server-ca.crt \
  -cert /var/lib/hubble-relay/tls/client.crt \
  -key /var/lib/hubble-relay/tls/client.key

CONNECTED(00000004)
depth=1 C = US, ST = San Francisco, L = CA, O = Cilium, OU = Cilium, CN = Cilium CA
verify return:1
depth=0 CN = *.default.hubble-grpc.cilium.io
verify return:1
---
Certificate chain
 0 s:CN = *.default.hubble-grpc.cilium.io
   i:C = US, ST = San Francisco, L = CA, O = Cilium, OU = Cilium, CN = Cilium CA
   a:PKEY: id-ecPublicKey, 256 (bit); sigalg: ecdsa-with-SHA256
   v:NotBefore: Aug 15 17:39:00 2024 GMT; NotAfter: Aug 15 17:39:00 2027 GMT
-----BEGIN CERTIFICATE-----
MIICNzCCAd2gAwIBAgIUAlgykDuc1J+mzseHS0pREX6Uv3cwCgYIKoZIzj0EAwIw
aDELMAkGA1UEBhMCVVMxFjAUBgNVBAgTDVNhbiBGcmFuY2lzY28xCzAJBgNVBAcT
AkNBMQ8wDQYDVQQKEwZDaWxpdW0xDzANBgNVBAsTBkNpbGl1bTESMBAGA1UEAxMJ
Q2lsaXVtIENBMB4XDTI0MDgxNTE3MzkwMFoXDTI3MDgxNTE3MzkwMFowKjEoMCYG
A1UEAwwfKi5kZWZhdWx0Lmh1YmJsZS1ncnBjLmNpbGl1bS5pbzBZMBMGByqGSM49
AgEGCCqGSM49AwEHA0IABGjtY50MM21TolEy5RUrBa6WqHsw7PjNB3MhYLCsuJmO
aQ1tIy6J2e7a9Cw2jmBlyj+dL8g0YLhRQX4n+leItSSjgaIwgZ8wDgYDVR0PAQH/
BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAwGA1UdEwEB/wQCMAAwHQYDVR0O
BBYEFCDf5epVs8yyyZCdtBzc90HrQzpFMB8GA1UdIwQYMBaAFDKuJMmhNPJ71FvB
AyHEMztI62NbMCoGA1UdEQQjMCGCHyouZGVmYXVsdC5odWJibGUtZ3JwYy5jaWxp
dW0uaW8wCgYIKoZIzj0EAwIDSAAwRQIhAP0kyl0Eb7FBQw1uZE+LWnRyr5GDsB3+
6rA/Rx042XZgAiBZML3lOW60tWMI1Pyn4cR4trFbzZpsUSwnQmOAb+paEw==
-----END CERTIFICATE-----
---
Server certificate
subject=CN = *.default.hubble-grpc.cilium.io
issuer=C = US, ST = San Francisco, L = CA, O = Cilium, OU = Cilium, CN = Cilium CA
---
Acceptable client certificate CA names
C = US, ST = San Francisco, L = CA, O = Cilium, OU = Cilium, CN = Cilium CA
Requested Signature Algorithms: RSA-PSS+SHA256:ECDSA+SHA256:Ed25519:RSA-PSS+SHA384:RSA-PSS+SHA512:RSA+SHA256:RSA+SHA384:RSA+SHA512:ECDSA+SHA384:ECDSA+SHA512:RSA+SHA1:ECDSA+SHA1
Shared Requested Signature Algorithms: RSA-PSS+SHA256:ECDSA+SHA256:Ed25519:RSA-PSS+SHA384:RSA-PSS+SHA512:RSA+SHA256:RSA+SHA384:RSA+SHA512:ECDSA+SHA384:ECDSA+SHA512
Peer signing digest: SHA256
Peer signature type: ECDSA
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1106 bytes and written 1651 bytes
Verification: OK
---
New, TLSv1.3, Cipher is TLS_AES_128_GCM_SHA256
Server public key is 256 bit
This TLS version forbids renegotiation.
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_128_GCM_SHA256
    Session-ID: 9ADFAFBDFFB876A9A8D4CC025470168D25485FF51929615199E9561F46FBF97B
    Session-ID-ctx:
    Resumption PSK: 58DD7621E7B353BD5C6FC3AAB5A907FF3D3251FAA184D28D2C69560E96806495
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 604800 (seconds)
    TLS session ticket:
    0000 - 55 93 99 70 30 37 6a 77-43 d7 0c 34 9f 24 51 40   U..p07jwC..4.$Q@
    ...
    ...
    0690 - 11 6d 26 ec 99 3a 6e a9-56 c9 ad a0 49 e2 f5 6a   .m&..:n.V...I..j
```

Copy First Line Copy Commands Copy All

Press `ctrl-d`{.docutils .literal .notranslate} to signal the TLS session and connection should be terminated. After the session has ended you will see output similar to the following:

``` {#codecell25}
@DONE
    06a0 - bf eb 8b 1d 8d 43 46 2a-07 02 e1 44 35 45 b1 a0   .....CF*...D5E..
    06b0 - 7d bb 27 2f 1a 35 b2 da-0d 00 15 fd 6c 1f 00 3b   }.'/.5......l..;
    06c0 - 9a 6e ff c9 5d ad 6b af-f7 20 39 99 5b ae 72 03   .n..].k.. 9.[.r.
    06d0 - c8 2d 93 7a e5 a7 e0 d5-70 95 8f b5 0b 56 9c      .-.z....p....V.

    Start Time: 1723744378
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
```

Copy First Line Copy All

The output of this OpenSSL command is similar to the previous output, but without the error message.

There is also an additional section, starting with `Post-Handshake`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`New`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Session`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Ticket`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`arrived`{.docutils .literal .notranslate}, the presence of which indicates that the client certificate is valid and a TLS session was established. The summary of the TLS session printed after the connection has ended can also be used as an indicator of the established TLS session.

## Hubble Metrics TLS and Authentication[](#hubble-metrics-tls-and-authentication "Link to this heading")

Starting with Cilium 1.16, Hubble supports configuring TLS on the Hubble metrics API in addition to the Hubble observer API.

This can be done by specifying the following options to Helm at install or upgrade time, along with the TLS configuration options described in the previous section.

Note

This section assumes that you have already enabled [Hubble metrics](../../../metrics/#hubble-metrics).

To enable TLS on the Hubble metrics API, add the following Helm flag to your list of options:

``` {#codecell26}
--set hubble.metrics.tls.enabled=true # Enable TLS on the Hubble metrics API
```

Copy Line

If you also want to enable authentication using mTLS on the Hubble metrics API, first create a ConfigMap with a CA certificate to use for verifying client certificates:

``` {#codecell27}
kubectl -n kube-system create configmap hubble-metrics-ca --from-file=ca.crt
```

Copy Line

Then, add the following flags to your Helm command to enable mTLS:

``` {#codecell28}
--set hubble.metrics.tls.enabled=true                       # Enable TLS on the Hubble metrics API
--set hubble.metrics.tls.server.mtls.enabled=true           # Enable mTLS authentication on the Hubble metrics API
--set hubble.metrics.tls.server.mtls.name=hubble-metrics-ca # Use the CA certificate from the ConfigMap
```

Copy First Line Copy All

After the configuration is applied, clients will be required to authenticate using a certificate signed by the configured CA certificate to access the Hubble metrics API.

Note

When using TLS with the Hubble metrics API you will need to update your Prometheus scrape configuration to use HTTPS by setting a `tls_config`{.docutils .literal .notranslate} and provide the path to the CA certificate. When using mTLS you will also need to provide a client certificate and key signed by the CA certificate for Prometheus to authenticate to the Hubble metrics API.

## Access the Hubble API with TLS Enabled[](#access-the-hubble-api-with-tls-enabled "Link to this heading")

The examples are adapted from [Inspecting Network Flows with the CLI](../../hubble-cli/#hubble-cli).

Before you can access the Hubble API with TLS enabled, you need to obtain the CA certificate from the secret that was created when enabling TLS. The following examples demonstrate how to obtain the CA certificate and use it to access the Hubble API.

Run the following command to obtain the CA certificate from the `hubble-relay-server-certs`{.docutils .literal .notranslate} secret:

``` {#codecell29}
$ kubectl -n kube-system get secret hubble-relay-server-certs -o jsonpath='{.data.ca\.crt}' | base64 -d > hubble-ca.crt
```

Copy Line

After obtaining the CA certificate you can use the `--tls`{.docutils .literal .notranslate} to enable TLS and `--tls-ca-cert-files`{.docutils .literal .notranslate} flag to specify the CA certificate. Additionally, when port-forwarding to Hubble Relay, you will need to specify the `--tls-server-name`{.docutils .literal .notranslate} flag:

``` {#codecell30}
$ hubble observe --tls --tls-ca-cert-files ./hubble-ca.crt --tls-server-name hubble.hubble-relay.cilium.io --pod deathstar --protocol http
May  4 13:23:40.501: default/tiefighter:42690 -> default/deathstar-c74d84667-cx5kp:80 http-request FORWARDED (HTTP/1.1 POST http://deathstar.default.svc.cluster.local/v1/request-landing)
May  4 13:23:40.502: default/tiefighter:42690 <- default/deathstar-c74d84667-cx5kp:80 http-response FORWARDED (HTTP/1.1 200 0ms (POST http://deathstar.default.svc.cluster.local/v1/request-landing))
May  4 13:23:43.791: default/tiefighter:42742 -> default/deathstar-c74d84667-cx5kp:80 http-request DROPPED (HTTP/1.1 PUT http://deathstar.default.svc.cluster.local/v1/exhaust-port)
```

Copy First Line Copy Commands Copy All

To persist these options for the shell session, set the following environment variables:

``` {#codecell31}
$ export HUBBLE_TLS=true
$ export HUBBLE_TLS_CA_CERT_FILES=./hubble-ca.crt
$ export HUBBLE_TLS_SERVER_NAME=hubble.hubble-relay.cilium.io
```

Copy First Line Copy Commands Copy All
