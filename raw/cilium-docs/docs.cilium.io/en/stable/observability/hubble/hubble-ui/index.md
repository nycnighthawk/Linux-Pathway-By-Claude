---
{"title": "Service Map & Hubble UI", "url": "https://docs.cilium.io/en/stable/observability/hubble/hubble-ui/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Service Map & Hubble UI[](#service-map-hubble-ui "Link to this heading")

This tutorial guides you through enabling the Hubble UI to access the graphical service map.

Note

This guide assumes that Cilium and Hubble have been correctly installed in your Kubernetes cluster. Please see [Cilium Quick Installation](../../../gettingstarted/k8s-install-default/#k8s-quick-install) and [Setting up Hubble Observability](../setup/#hubble-setup) for more information. If unsure, run `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} and validate that Cilium and Hubble are installed.

## Enable the Hubble UI[](#enable-the-hubble-ui "Link to this heading")

Enable the Hubble UI by running the following command:

``` {#codecell0}
cilium hubble enable --ui
🔑 Found existing CA in secret cilium-ca
✨ Patching ConfigMap cilium-config to enable Hubble...
♻️ Restarted Cilium pods
✅ Relay is already deployed
✅ Hubble UI is already deployed
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace $CILIUM_NAMESPACE \
   --reuse-values \
   --set hubble.relay.enabled=true \
   --set hubble.ui.enabled=true
```

Copy First Line Copy All

``` {#codecell2 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace $CILIUM_NAMESPACE \
   --reuse-values \
   --set hubble.relay.enabled=true \
   --set hubble.ui.enabled=true
```

Copy First Line Copy All

Clusters sometimes come with Cilium, Hubble, and Hubble relay already installed. When this is the case you can still use Helm to install only Hubble UI on top of the pre-installed components.

You will need to set `hubble.ui.standalone.enabled`{.docutils .literal .notranslate} to `true`{.docutils .literal .notranslate} and optionally provide a volume to mount Hubble UI client certificates if TLS is enabled on Hubble Relay server side.

Below is an example deploying Hubble UI as standalone, with client certificates mounted from a `my-hubble-ui-client-certs`{.docutils .literal .notranslate} secret:

``` {#codecell3 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace $CILIUM_NAMESPACE \
   --reuse-values \
   --set hubble.relay.enabled=true \
   --set hubble.ui.enabledd=true \
   --values - <<EOF
   agent: false
   operator:
     enabled: false
   cni:
     install: false
   hubble:
     enabled: false
     relay:
       # set this to false as Hubble relay is already installed
       enabled: false
       tls:
         server:
           # set this to true if tls is enabled on Hubble relay server side
           enabled: true
     ui:
       # enable Hubble UI
       enabled: true
       standalone:
         # enable Hubble UI standalone deployment
         enabled: true
         # provide a volume containing Hubble relay client certificates to mount in Hubble UI pod
         tls:
           certsVolume:
             projected:
               defaultMode: 0400
               sources:
                 - secret:
                     name: my-hubble-ui-client-certs
                     items:
                       - key: tls.crt
                         path: client.crt
                       - key: tls.key
                         path: client.key
                       - key: ca.crt
                         path: hubble-relay-ca.crt
   EOF
```

Copy First Line Copy All

``` {#codecell4 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace $CILIUM_NAMESPACE \
   --reuse-values \
   --set hubble.relay.enabled=true \
   --set hubble.ui.enabledd=true \
   --values - <<EOF
   agent: false
   operator:
     enabled: false
   cni:
     install: false
   hubble:
     enabled: false
     relay:
       # set this to false as Hubble relay is already installed
       enabled: false
       tls:
         server:
           # set this to true if tls is enabled on Hubble relay server side
           enabled: true
     ui:
       # enable Hubble UI
       enabled: true
       standalone:
         # enable Hubble UI standalone deployment
         enabled: true
         # provide a volume containing Hubble relay client certificates to mount in Hubble UI pod
         tls:
           certsVolume:
             projected:
               defaultMode: 0400
               sources:
                 - secret:
                     name: my-hubble-ui-client-certs
                     items:
                       - key: tls.crt
                         path: client.crt
                       - key: tls.key
                         path: client.key
                       - key: ca.crt
                         path: hubble-relay-ca.crt
   EOF
```

Copy First Line Copy All

Please note that Hubble UI expects the certificate files to be available under the following paths:

``` {#codecell5}
- name: TLS_RELAY_CA_CERT_FILES
  value: /var/lib/hubble-ui/certs/hubble-relay-ca.crt
- name: TLS_RELAY_CLIENT_CERT_FILE
  value: /var/lib/hubble-ui/certs/client.crt
- name: TLS_RELAY_CLIENT_KEY_FILE
  value: /var/lib/hubble-ui/certs/client.key
```

Copy First Line Copy All

Keep this in mind when providing the volume containing the certificate.

## Open the Hubble UI[](#open-the-hubble-ui "Link to this heading")

Open the Hubble UI in your browser by running `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ui`{.docutils .literal .notranslate}. It will automatically set up a port forward to the hubble-ui service in your Kubernetes cluster and make it available on a local port on your machine.

``` {#codecell6}
cilium hubble ui
Forwarding from 0.0.0.0:12000 -> 8081
Forwarding from [::]:12000 -> 8081
```

Copy First Line Copy All

Tip

The above command will block and continue running while the port forward is active. You can interrupt the command to abort the port forward and re-run the command to make the UI accessible again.

If your browser has not automatically opened the UI, open the page [http://localhost:12000](http://localhost:12000) in your browser. You should see a screen with an invitation to select a namespace, use the namespace selector dropdown on the left top corner to select a namespace:

In this example, we are deploying the Star Wars demo from the [Identity-Aware and HTTP-Aware Policy Enforcement](../../../security/http/#gs-http) guide. However you can apply the same techniques to observe application connectivity dependencies in your own namespace, and clusters for application of any type.

Once the deployment is ready, issue a request from both spaceships to emulate some traffic.

``` {#codecell7}
$ kubectl exec xwing -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
Ship landed
$ kubectl exec tiefighter -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
Ship landed
```

Copy First Line Copy Commands Copy All

These requests will then be displayed in the UI as service dependencies between the different pods:

In the bottom of the interface, you may also inspect each recent Hubble flow event in your current namespace individually.

## Inspecting a wide variety of network traffic[](#inspecting-a-wide-variety-of-network-traffic "Link to this heading")

In order to generate some network traffic, run the connectivity test in a loop:

``` {#codecell8}
while true; do cilium connectivity test; done
```

Copy Line

To see the traffic in Hubble, open [http://localhost:12000/cilium-test](http://localhost:12000/cilium-test) in your browser.
