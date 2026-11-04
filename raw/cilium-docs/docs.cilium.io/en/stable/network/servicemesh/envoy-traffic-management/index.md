---
{"title": "L7 Load Balancing and URL re-writing", "url": "https://docs.cilium.io/en/stable/network/servicemesh/envoy-traffic-management/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# L7 Load Balancing and URL re-writing[](#l7-load-balancing-and-url-re-writing "Link to this heading")

Cilium Service Mesh defines a `CiliumEnvoyConfig`{.docutils .literal .notranslate} CRD which allows users to set the configuration of the Envoy component built into Cilium agents.

This example sets up an Envoy listener which load balances requests between two backend services.

## Deploy Test Applications[](#deploy-test-applications "Link to this heading")

``` {#codecell0 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/test-application.yaml
```

Copy Line

The test workloads consist of:

-   two client deployments, `client`{.docutils .literal .notranslate} and `client2`{.docutils .literal .notranslate}

-   two services, `echo-service-1`{.docutils .literal .notranslate} and `echo-service-2`{.docutils .literal .notranslate}

View information about these pods:

``` {#codecell1}
$ kubectl get pods --show-labels -o wide
NAME                              READY   STATUS    RESTARTS   AGE    IP          NODE           NOMINATED NODE   READINESS GATES   LABELS
client-7568bc7f86-dlfqr           1/1     Running   0          100s   10.0.1.8    minikube-m02   <none>           <none>            kind=client,name=client,pod-template-hash=7568bc7f86
client2-8b4c4fd75-xn25d           1/1     Running   0          100s   10.0.1.24   minikube-m02   <none>           <none>            kind=client,name=client2,other=client,pod-template-hash=8b4c4fd75
echo-service-1-97748874-4sztx     2/2     Running   0          100s   10.0.1.86   minikube-m02   <none>           <none>            kind=echo,name=echo-service-1,other=echo,pod-template-hash=97748874
echo-service-2-76c584c4bf-p4z4w   2/2     Running   0          100s   10.0.1.16   minikube-m02   <none>           <none>            kind=echo,name=echo-service-2,pod-template-hash=76c584c4bf
```

Copy First Line Copy Commands Copy All

You can see that

-   Only `client2`{.docutils .literal .notranslate} is labeled with `other=client`{.docutils .literal .notranslate} - we will use this in a `CiliumNetworkPolicy`{.docutils .literal .notranslate} definition later in this example.

Make an environment variable with the pod ID for `client2`{.docutils .literal .notranslate}:

``` {#codecell2}
$ export CLIENT2=$(kubectl get pods -l name=client2 -o jsonpath='{.items[0].metadata.name}')
```

Copy Line

We are going to use Envoy configuration to load-balance requests between these two services `echo-service-1`{.docutils .literal .notranslate} and `echo-service-2`{.docutils .literal .notranslate}.

## Start Observing Traffic with Hubble[](#start-observing-traffic-with-hubble "Link to this heading")

Enable Hubble in your cluster with the step mentioned in [Setting up Hubble Observability](../../../observability/hubble/setup/#hubble-setup).

Start a second terminal, then enable hubble port forwarding and observe traffic from the `client2`{.docutils .literal .notranslate} pod:

``` {#codecell3}
$ kubectl -n kube-system port-forward deployment/hubble-relay 4245:4245 &
$ hubble observe --from-pod $CLIENT2 -f
```

Copy First Line Copy Commands Copy All

You should be able to get a response from both of the backend services individually from `client2`{.docutils .literal .notranslate}:

``` {#codecell4}
$ kubectl exec -it $CLIENT2 -- curl -v echo-service-1:8080/
$ kubectl exec -it $CLIENT2 -- curl -v echo-service-2:8080/
```

Copy First Line Copy Commands Copy All

Notice that Hubble shows all the flows between these pods as being either `to/from-stack`{.docutils .literal .notranslate}, `to/from-overlay`{.docutils .literal .notranslate} or `to/from-endpoint`{.docutils .literal .notranslate} - there is no traffic marked as flowing to or from the proxy at this stage. (This assumes you don't already have any Layer 7 policies in place affecting this traffic.)

Verify that you get a 404 error response if you curl to the non-existent URL `/foo`{.docutils .literal .notranslate} on these services:

``` {#codecell5}
$ kubectl exec -it $CLIENT2 -- curl -v echo-service-1:8080/foo
$ kubectl exec -it $CLIENT2 -- curl -v echo-service-2:8080/foo
```

Copy First Line Copy Commands Copy All

## Add Layer 7 Policy[](#add-layer-7-policy "Link to this heading")

Adding a Layer 7 policy introduces the Envoy proxy into the path for this traffic.

``` {#codecell6 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/client-egress-l7-http.yaml
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/client-egress-only-dns.yaml
```

Copy First Line Copy All

Make a request to a backend service (either will do):

``` {#codecell7}
$ kubectl exec -it $CLIENT2 -- curl -v echo-service-1:8080/
$ kubectl exec -it $CLIENT2 -- curl -v echo-service-2:8080/foo
```

Copy First Line Copy Commands Copy All

Adding a Layer 7 policy enables Layer 7 visibility. Notice that the Hubble output now includes flows `to-proxy`{.docutils .literal .notranslate}, and also shows the HTTP protocol information at level 7 (for example `HTTP/1.1`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`GET`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`http://echo-service-1:8080/`{.docutils .literal .notranslate})

Note

Note that Envoy may [sanitize some headers](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/header_sanitizing#http-header-sanitizing).

Instead, you can make Envoy trust previous hops and prevent Envoy from rewriting some of these HTTP headers. Trust previous hops by setting Helm values `envoy.xffNumTrustedHopsL7PolicyIngress`{.docutils .literal .notranslate} and `envoy.xffNumTrustedHopsL7PolicyEgress`{.docutils .literal .notranslate} to the number of hops to trust.

For an egress policy the previous hop is the source pod, whereas for an ingress policy it can be either the source pod, the "egress policy transparent proxy", Cilium Ingress Controller, Cilium Gateway API, or any other Ingress proxy or infrastructure.

Depending on your environment, you should consider the security implications of trusting previous hops.

## Test Layer 7 Policy Enforcement[](#test-layer-7-policy-enforcement "Link to this heading")

The policy only permits GET requests to the `/`{.docutils .literal .notranslate} path, so you will see requests to any other URL being dropped. For example, try:

``` {#codecell8}
$ kubectl exec -it $CLIENT2 -- curl -v echo-service-1:8080/foo
```

Copy Line

The Hubble output will show the HTTP request being dropped, like this:

``` {#codecell9}
Jul  7 08:40:15.076: default/client2-8b4c4fd75-6pgvl:58586 -> default/echo-service-1-97748874-n7758:8080 http-request DROPPED (HTTP/1.1 GET http://echo-service-1:8080/foo)
```

Copy Line

And the curl should show a `403`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Forbidden`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`response`{.docutils .literal .notranslate}.

## Add Envoy load-balancing and URL re-writing[](#add-envoy-load-balancing-and-url-re-writing "Link to this heading")

Apply the `envoy-traffic-management-test.yaml`{.docutils .literal .notranslate} file, which defines a `CiliumClusterwideEnvoyConfig`{.docutils .literal .notranslate}.

``` {#codecell10 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/envoy-traffic-management-test.yaml
```

Copy Line

Note

Note that these Envoy resources are not validated by K8s at all, so any errors in the Envoy resources will only be seen by the Cilium Agent observing these CRDs. This means that `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`apply`{.docutils .literal .notranslate} will report success, while parsing and/or installing the resources for the node-local Envoy instance may have failed. Currently the only way of verifying this is by observing Cilium Agent logs for errors and warnings. Additionally, Cilium Agent will print warning logs for any conflicting Envoy resources in the cluster.

Note

Note that Cilium Ingress Controller will configure required Envoy resource under the hood. Please check Cilium Agent logs if you are creating Envoy resources explicitly to make sure there is no conflict.

This configuration listens for traffic intended for either of the two `echo-`{.docutils .literal .notranslate} services and:

-   load-balances 50/50 between the two backend `echo-`{.docutils .literal .notranslate} services

-   rewrites the path `/foo`{.docutils .literal .notranslate} to `/`{.docutils .literal .notranslate}

A request to `/foo`{.docutils .literal .notranslate} should now succeed, because of the path re-writing:

``` {#codecell11}
$ kubectl exec -it $CLIENT2 -- curl -v echo-service-1:8080/foo
```

Copy Line

But the network policy still prevents requests to any path that is not rewritten to `/`{.docutils .literal .notranslate}. For example, this request will result in a packet being dropped and a 403 Forbidden response code:

``` {#codecell12}
$ kubectl exec -it $CLIENT2 -- curl -v echo-service-1:8080/bar

### Output from hubble observe
Jul  7 08:43:47.165: default/client2-8b4c4fd75-6pgvl:33376 -> default/echo-service-2-76c584c4bf-874dm:8080 http-request DROPPED (HTTP/1.1 GET http://echo-service-1:8080/bar)
```

Copy First Line Copy Commands Copy All

Try making several requests to one backend service. You should see in the Hubble output approximately half the time, they are handled by the other backend.

Example:

``` {#codecell13}
Jul  7 08:45:25.807: default/client2-8b4c4fd75-6pgvl:37388 -> kube-system/coredns-64897985d-8jhhn:53 L3-L4 REDIRECTED (UDP)
Jul  7 08:45:25.807: default/client2-8b4c4fd75-6pgvl:37388 -> kube-system/coredns-64897985d-8jhhn:53 to-proxy FORWARDED (UDP)
Jul  7 08:45:25.807: default/client2-8b4c4fd75-6pgvl:37388 -> kube-system/coredns-64897985d-8jhhn:53 dns-request FORWARDED (DNS Query echo-service-1.default.svc.cluster.local. AAAA)
Jul  7 08:45:25.807: default/client2-8b4c4fd75-6pgvl:37388 -> kube-system/coredns-64897985d-8jhhn:53 dns-request FORWARDED (DNS Query echo-service-1.default.svc.cluster.local. A)
Jul  7 08:45:25.808: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-1:8080 none REDIRECTED (TCP Flags: SYN)
Jul  7 08:45:25.808: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-1:8080 to-proxy FORWARDED (TCP Flags: SYN)
Jul  7 08:45:25.808: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-1:8080 to-proxy FORWARDED (TCP Flags: ACK)
Jul  7 08:45:25.808: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-1:8080 to-proxy FORWARDED (TCP Flags: ACK, PSH)
Jul  7 08:45:25.809: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-2-76c584c4bf-874dm:8080 L3-L4 REDIRECTED (TCP Flags: SYN)
Jul  7 08:45:25.809: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-2-76c584c4bf-874dm:8080 to-endpoint FORWARDED (TCP Flags: SYN)
Jul  7 08:45:25.809: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-2-76c584c4bf-874dm:8080 to-endpoint FORWARDED (TCP Flags: ACK)
Jul  7 08:45:25.809: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-2-76c584c4bf-874dm:8080 to-endpoint FORWARDED (TCP Flags: ACK, PSH)
Jul  7 08:45:25.809: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-2-76c584c4bf-874dm:8080 http-request FORWARDED (HTTP/1.1 GET http://echo-service-1:8080/)
Jul  7 08:45:25.811: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-1:8080 to-proxy FORWARDED (TCP Flags: ACK, FIN)
Jul  7 08:45:25.811: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-1:8080 to-proxy FORWARDED (TCP Flags: ACK)
Jul  7 08:45:30.811: default/client2-8b4c4fd75-6pgvl:57942 -> default/echo-service-2-76c584c4bf-874dm:8080 to-endpoint FORWARDED (TCP Flags: ACK, FIN)
```

Copy First Line Copy All
