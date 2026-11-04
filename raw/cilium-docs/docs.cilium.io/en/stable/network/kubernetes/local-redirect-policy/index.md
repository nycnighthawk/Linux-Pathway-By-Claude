---
{"title": "Local Redirect Policy", "url": "https://docs.cilium.io/en/stable/network/kubernetes/local-redirect-policy/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Local Redirect Policy[](#local-redirect-policy "Link to this heading")

This document explains how to configure Cilium's Local Redirect Policy, that enables pod traffic destined to an IP address and port/protocol tuple or Kubernetes service to be redirected locally to backend pod(s) within a node, using eBPF. The namespace of backend pod(s) need to match with that of the policy. The CiliumLocalRedirectPolicy is configured as a `CustomResourceDefinition`{.docutils .literal .notranslate}.

Video

Aside from this document, you can watch a video explanation of Cilium's Local Redirect Policy on [eCHO episode 39: Local Redirect Policy](https://www.youtube.com/watch?v=BT_gdlhjiQc&t=176s).

There are two types of Local Redirect Policies supported. When traffic for a Kubernetes service needs to be redirected, use the [ServiceMatcher](#servicematcher) type. The service needs to be of type `clusterIP`{.docutils .literal .notranslate}. When traffic matching IP address and port/protocol, that doesn't belong to any Kubernetes service, needs to be redirected, use the [AddressMatcher](#addressmatcher) type.

The policies can be gated by Kubernetes Role-based access control (RBAC) framework. See the official [RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

When policies are applied, matched pod traffic is redirected. If desired, RBAC configurations can be used such that application developers can not escape the redirection.

## Prerequisites[](#prerequisites "Link to this heading")

Setup Helm repository:

``` {#codecell0}
helm repo add cilium https://helm.cilium.io/
```

Copy Line

Cilium charts are also available via OCI registries (Quay.io and Docker Hub). No setup required - you can install directly using `oci://`{.docutils .literal .notranslate} URLs.

See the [OCI Registry section](../../../installation/k8s-install-helm/#k8s-install-helm) for more information, including chart signing verification and digest-based installations.

Enable the feature by setting the `localRedirectPolicies.enabled`{.docutils .literal .notranslate} value to `true`{.docutils .literal .notranslate}.

``` {#codecell1 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set localRedirectPolicies.enabled=true
```

Copy First Line Copy All

``` {#codecell2 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --reuse-values \
   --set localRedirectPolicies.enabled=true
```

Copy First Line Copy All

Rollout the operator and agent pods to make the changes effective:

``` {#codecell3}
$ kubectl rollout restart deploy cilium-operator -n kube-system
$ kubectl rollout restart ds cilium -n kube-system
```

Copy First Line Copy Commands Copy All

Verify that Cilium agent and operator pods are running.

``` {#codecell4}
$ kubectl -n kube-system get pods -l k8s-app=cilium
NAME           READY   STATUS    RESTARTS   AGE
cilium-5ngzd   1/1     Running   0          3m19s

$ kubectl -n kube-system get pods -l name=cilium-operator
NAME                               READY   STATUS    RESTARTS   AGE
cilium-operator-544b4d5cdd-qxvpv   1/1     Running   0          3m19s
```

Copy First Line Copy Commands Copy All

Validate that the Cilium Local Redirect Policy CRD has been registered.

``` {#codecell5}
$ kubectl get crds
NAME                              CREATED AT
[...]
ciliumlocalredirectpolicies.cilium.io              2020-08-24T05:31:47Z
```

Copy First Line Copy Commands Copy All

Note

Local Redirect Policy supports either the socket-level loadbalancer or the tc loadbalancer. The configuration depends on your specific use case and the type of service handling required. Below are the Helm setups to work with `localRedirectPolicies.enabled=true`{.docutils .literal .notranslate}:

1.  Enable full kube-proxy replacement:

> This setup is for users who want to replace kube-proxy with Cilium's eBPF implementation and leverage Local Redirect Policy.
>
> ``` {#codecell6}
> kubeProxyReplacement: true
> localRedirectPolicies:
>   enabled: true
> ```
>
> Copy First Line Copy All

2.  Bypass the socket-level loadbalancer in pod namespaces:

> This setup is for users who want to disable the socket-level loadbalancer in pod namespaces. For example, this might be needed if there are custom redirection rules in the pod namespace that would conflict with the socket-level load balancer.
>
> ``` {#codecell7}
> kubeProxyReplacement: true
> socketLB:
>   hostNamespaceOnly: true
> localRedirectPolicies:
>   enabled: true
> ```
>
> Copy First Line Copy All

3.  Enable the socket-level loadbalancer only:

> This setup is for users who prefer to retain kube-proxy for overall service handling but still want to leverage Cilium's Local Redirect Policy.
>
> ``` {#codecell8}
> kubeProxyReplacement: false
> socketLB:
>   enabled: true
> localRedirectPolicies:
>   enabled: true
> ```
>
> Copy First Line Copy All

4.  Disable any service handling except for ClusterIP services accessed from pods:

> If you want to fully rely on kube-proxy for the service handling, you can disable all kube-proxy replacement functionality expect ClusterIP services accessed from pod namespace. Note that the pod traffic from host namespace isn't handled by Local Redirect Policy with this setup.
>
> ``` {#codecell9}
> kubeProxyReplacement: false
> localRedirectPolicies:
>   enabled: true
> ```
>
> Copy First Line Copy All

## Create backend and client pods[](#create-backend-and-client-pods "Link to this heading")

Deploy a backend pod where traffic needs to be redirected to based on the configurations specified in a CiliumLocalRedirectPolicy. The metadata labels and container port and protocol respectively match with the labels, port and protocol fields specified in the CiliumLocalRedirectPolicy custom resources that will be created in the next step.

``` {#codecell10}
apiVersion: v1
kind: Pod
metadata:
  name: lrp-pod
  labels:
    app: proxy
spec:
  containers:
    - name: lrp-pod
      image: nginx
      ports:
        - containerPort: 80
          name: tcp
          protocol: TCP
```

Copy First Line Copy All

``` {#codecell11 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-local-redirect/backend-pod.yaml
```

Copy Line

Verify that the pod is running.

``` {#codecell12}
$ kubectl get pods | grep lrp-pod
lrp-pod                      1/1     Running   0          46s
```

Copy First Line Copy Commands Copy All

Deploy a client pod that will generate traffic which will be redirected based on the configurations specified in the CiliumLocalRedirectPolicy.

``` {#codecell13 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-dns/dns-sw-app.yaml
$ kubectl wait pod/mediabot --for=condition=Ready
$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
pod/mediabot                     1/1     Running   0          14s
```

Copy First Line Copy All

## Create Cilium Local Redirect Policy Custom Resources[](#create-cilium-local-redirect-policy-custom-resources "Link to this heading")

There are two types of configurations supported in the CiliumLocalRedirectPolicy in order to match the traffic that needs to be redirected.

### AddressMatcher[](#addressmatcher "Link to this heading")

This type of configuration is specified using an IP address and a Layer 4 port/protocol. When multiple ports are specified for frontend in `toPorts`{.docutils .literal .notranslate}, the ports need to be named. The port names will be used to map frontend ports with backend ports.

Verify that the ports specified in `toPorts`{.docutils .literal .notranslate} under `redirectBackend`{.docutils .literal .notranslate} exist in the backend pod spec.

The example shows how to redirect from traffic matching, IP address `169.254.169.254`{.docutils .literal .notranslate} and Layer 4 port `8080`{.docutils .literal .notranslate} with protocol `TCP`{.docutils .literal .notranslate}, to a backend pod deployed with labels `app=proxy`{.docutils .literal .notranslate} and Layer 4 port `80`{.docutils .literal .notranslate} with protocol `TCP`{.docutils .literal .notranslate}. The `localEndpointSelector`{.docutils .literal .notranslate} set to `app=proxy`{.docutils .literal .notranslate} in the policy is used to select the backend pods where traffic is redirected to.

Create a custom resource of type CiliumLocalRedirectPolicy with `addressMatcher`{.docutils .literal .notranslate} configuration.

``` {#codecell14}
apiVersion: "cilium.io/v2"
kind: CiliumLocalRedirectPolicy
metadata:
  name: "lrp-addr"
spec:
  redirectFrontend:
    addressMatcher:
      ip: "169.254.169.254"
      toPorts:
        - port: "8080"
          protocol: TCP
  redirectBackend:
    localEndpointSelector:
      matchLabels:
        app: proxy
    toPorts:
      - port: "80"
        protocol: TCP
```

Copy First Line Copy All

``` {#codecell15 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-local-redirect/lrp-addrmatcher.yaml
```

Copy Line

Verify that the custom resource is created.

``` {#codecell16}
$ kubectl get ciliumlocalredirectpolicies | grep lrp-addr
NAME           AGE
lrp-addr       20h
```

Copy First Line Copy Commands Copy All

Verify that Cilium's eBPF kube-proxy replacement created a `LocalRedirect`{.docutils .literal .notranslate} service entry with the backend IP address of that of the `lrp-pod`{.docutils .literal .notranslate} that was selected by the policy. Make sure that `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`service`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate} is run in Cilium pod running on the same node as `lrp-pod`{.docutils .literal .notranslate}.

``` {#codecell17}
$ kubectl describe pod lrp-pod  | grep 'IP:'
IP:           10.16.70.187
```

Copy First Line Copy Commands Copy All

``` {#codecell18}
$ kubectl exec -it -n kube-system cilium-5ngzd -- cilium-dbg service list
ID   Frontend               Service Type       Backend
[...]
4    172.20.0.51:80         LocalRedirect      1 => 10.16.70.187:80
```

Copy First Line Copy Commands Copy All

Invoke a curl command from the client pod to the IP address and port configuration specified in the `lrp-addr`{.docutils .literal .notranslate} custom resource above.

``` {#codecell19}
$ kubectl exec mediabot -- curl -I -s http://169.254.169.254:8080/index.html
HTTP/1.1 200 OK
Server: nginx/1.19.2
Date: Fri, 28 Aug 2020 01:33:34 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 11 Aug 2020 14:50:35 GMT
Connection: keep-alive
ETag: "5f32b03b-264"
Accept-Ranges: bytes
```

Copy First Line Copy Commands Copy All

Verify that the traffic was redirected to the `lrp-pod`{.docutils .literal .notranslate} that was deployed. `tcpdump`{.docutils .literal .notranslate} should be run on the same node that `lrp-pod`{.docutils .literal .notranslate} is running on.

``` {#codecell20}
$ sudo tcpdump -i any -n port 80
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes
01:36:24.608566 IP 10.16.215.55.60876 > 10.16.70.187.80: Flags [S], seq 2119454273, win 28200, options [mss 1410,sackOK,TS val 2541637677 ecr 0,nop,wscale 7], length 0
01:36:24.608600 IP 10.16.70.187.80 > 10.16.215.55.60876: Flags [S.], seq 1315636594, ack 2119454274, win 27960, options [mss 1410,sackOK,TS val 2962246962 ecr 2541637677,nop,wscale 7], length 0
01:36:24.608638 IP 10.16.215.55.60876 > 10.16.70.187.80: Flags [.], ack 1, win 221, options [nop,nop,TS val 2541637677 ecr 2962246962], length 0
01:36:24.608867 IP 10.16.215.55.60876 > 10.16.70.187.80: Flags [P.], seq 1:96, ack 1, win 221, options [nop,nop,TS val 2541637677 ecr 2962246962], length 95: HTTP: HEAD /index.html HTTP/1.1
01:36:24.608876 IP 10.16.70.187.80 > 10.16.215.55.60876: Flags [.], ack 96, win 219, options [nop,nop,TS val 2962246962 ecr 2541637677], length 0
01:36:24.609007 IP 10.16.70.187.80 > 10.16.215.55.60876: Flags [P.], seq 1:239, ack 96, win 219, options [nop,nop,TS val 2962246962 ecr 2541637677], length 238: HTTP: HTTP/1.1 200 OK
01:36:24.609052 IP 10.16.215.55.60876 > 10.16.70.187.80: Flags [.], ack 239, win 229, options [nop,nop,TS val 2541637677 ecr 2962246962], length 0
```

Copy First Line Copy Commands Copy All

The allowed addresses can be constrained clusterwide using the `localRedirectPolicies.addressMatcherCIDRs`{.docutils .literal .notranslate} helm option:

``` {#codecell21}
localRedirectPolicies:
  enabled: true
  addressMatchCIDRs:
      - 169.254.169.254/32
```

Copy First Line Copy All

The above would only allow traffic going to `169.254.169.254`{.docutils .literal .notranslate} to be redirected with an AddressMatcher rule. A policy with a disallowed address will be rejected and a warning log message is emitted by cilium-agent.

Note

AddressMatcher is intended for IPs that do not belong to a Kubernetes Service. If the IP and port/protocol in `redirectFrontend.addressMatcher`{.docutils .literal .notranslate} coincide with an existing `ClusterIP`{.docutils .literal .notranslate} Service frontend, the policy is not applied to that address. Cilium refuses to override a frontend owned by another Service and logs:

``` {#codecell22}
LocalRedirectPolicy matches an address owned by an existing service => refusing to override
```

Copy Line

To redirect traffic destined for a Service, use [ServiceMatcher](#servicematcher) instead.

### ServiceMatcher[](#servicematcher "Link to this heading")

This type of configuration is specified using Kubernetes service name and namespace for which traffic needs to be redirected. The service must be of type `clusterIP`{.docutils .literal .notranslate}. When `toPorts`{.docutils .literal .notranslate} under `redirectFrontend`{.docutils .literal .notranslate} are not specified, traffic for all the service ports will be redirected. However, if traffic destined to only a subset of ports needs to be redirected, these ports need to be specified in the spec. Additionally, when multiple service ports are specified in the spec, they must be named. The port names will be used to map frontend ports with backend ports. Verify that the ports specified in `toPorts`{.docutils .literal .notranslate} under `redirectBackend`{.docutils .literal .notranslate} exist in the backend pod spec. The `localEndpointSelector`{.docutils .literal .notranslate} set to `app=proxy`{.docutils .literal .notranslate} in the policy is used to select the backend pods where traffic is redirected to.

When a policy of this type is applied, the existing service entry created by Cilium's eBPF kube-proxy replacement will be replaced with a new service entry of type `LocalRedirect`{.docutils .literal .notranslate}. This entry may only have node-local backend pods.

The example shows how to redirect from traffic matching `my-service`{.docutils .literal .notranslate}, to a backend pod deployed with labels `app=proxy`{.docutils .literal .notranslate} and Layer 4 port `80`{.docutils .literal .notranslate} with protocol `TCP`{.docutils .literal .notranslate}. The `localEndpointSelector`{.docutils .literal .notranslate} set to `app=proxy`{.docutils .literal .notranslate} in the policy is used to select the backend pods where traffic is redirected to.

Deploy the Kubernetes service for which traffic needs to be redirected.

``` {#codecell23}
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - name: tcp
      protocol: TCP
      port: 80
```

Copy First Line Copy All

``` {#codecell24 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-local-redirect/k8s-svc.yaml
```

Copy Line

Verify that the service is created.

``` {#codecell25}
$ kubectl get service | grep 'my-service'
my-service   ClusterIP   172.20.0.51   <none>        80/TCP     2d7h
```

Copy First Line Copy Commands Copy All

Verify that Cilium's eBPF kube-proxy replacement created a `ClusterIP`{.docutils .literal .notranslate} service entry.

``` {#codecell26}
$ kubectl exec -it -n kube-system ds/cilium -- cilium-dbg service list
ID   Frontend               Service Type   Backend
[...]
4    172.20.0.51:80         ClusterIP
```

Copy First Line Copy Commands Copy All

Create a custom resource of type CiliumLocalRedirectPolicy with `serviceMatcher`{.docutils .literal .notranslate} configuration.

``` {#codecell27}
apiVersion: "cilium.io/v2"
kind: CiliumLocalRedirectPolicy
metadata:
  name: "lrp-svc"
spec:
  redirectFrontend:
    serviceMatcher:
      serviceName: my-service
      namespace: default
  redirectBackend:
    localEndpointSelector:
      matchLabels:
        app: proxy
    toPorts:
      - port: "80"
        protocol: TCP
```

Copy First Line Copy All

``` {#codecell28 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-local-redirect/lrp-svcmatcher.yaml
```

Copy Line

Verify that the custom resource is created.

``` {#codecell29}
$ kubectl get ciliumlocalredirectpolicies | grep svc
NAME               AGE
lrp-svc   20h
```

Copy First Line Copy Commands Copy All

Verify that entry Cilium's eBPF kube-proxy replacement updated the service entry with type `LocalRedirect`{.docutils .literal .notranslate} and the node-local backend selected by the policy. Make sure to run `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`service`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate} in Cilium pod running on the same node as `lrp-pod`{.docutils .literal .notranslate}.

``` {#codecell30}
$ kubectl exec -it -n kube-system cilium-5ngzd -- cilium-dbg service list
ID   Frontend               Service Type       Backend
[...]
4    172.20.0.51:80         LocalRedirect      1 => 10.16.70.187:80
```

Copy First Line Copy Commands Copy All

Invoke a curl command from the client pod to the Cluster IP address and port of `my-service`{.docutils .literal .notranslate} specified in the `lrp-svc`{.docutils .literal .notranslate} custom resource above.

``` {#codecell31}
$ kubectl exec mediabot -- curl -I -s http://172.20.0.51/index.html
HTTP/1.1 200 OK
Server: nginx/1.19.2
Date: Fri, 28 Aug 2020 01:50:50 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 11 Aug 2020 14:50:35 GMT
Connection: keep-alive
ETag: "5f32b03b-264"
Accept-Ranges: bytes
```

Copy First Line Copy Commands Copy All

Verify that the traffic was redirected to the `lrp-pod`{.docutils .literal .notranslate} that was deployed. `tcpdump`{.docutils .literal .notranslate} should be run on the same node that `lrp-pod`{.docutils .literal .notranslate} is running on.

``` {#codecell32}
$ kubectl describe pod lrp-pod  | grep 'IP:'
IP:           10.16.70.187
```

Copy First Line Copy Commands Copy All

``` {#codecell33}
$ sudo tcpdump -i any -n port 80
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes
01:36:24.608566 IP 10.16.215.55.60186 > 10.16.70.187.80: Flags [S], seq 2119454273, win 28200, options [mss 1410,sackOK,TS val 2541637677 ecr 0,nop,wscale 7], length 0
01:36:24.608600 IP 10.16.70.187.80 > 10.16.215.55.60876: Flags [S.], seq 1315636594, ack 2119454274, win 27960, options [mss 1410,sackOK,TS val 2962246962 ecr 2541637677,nop,wscale 7], length 0
01:36:24.608638 IP 10.16.215.55.60876 > 10.16.70.187.80: Flags [.], ack 1, win 221, options [nop,nop,TS val 2541637677 ecr 2962246962], length 0
01:36:24.608867 IP 10.16.215.55.60876 > 10.16.70.187.80: Flags [P.], seq 1:96, ack 1, win 221, options [nop,nop,TS val 2541637677 ecr 2962246962], length 95: HTTP: HEAD /index.html HTTP/1.1
01:36:24.608876 IP 10.16.70.187.80 > 10.16.215.55.60876: Flags [.], ack 96, win 219, options [nop,nop,TS val 2962246962 ecr 2541637677], length 0
01:36:24.609007 IP 10.16.70.187.80 > 10.16.215.55.60876: Flags [P.], seq 1:239, ack 96, win 219, options [nop,nop,TS val 2962246962 ecr 2541637677], length 238: HTTP: HTTP/1.1 200 OK
01:36:24.609052 IP 10.16.215.55.60876 > 10.16.70.187.80: Flags [.], ack 239, win 229, options [nop,nop,TS val 2541637677 ecr 2962246962], length 0
```

Copy First Line Copy Commands Copy All

## Limitations[](#limitations "Link to this heading")

When you create a Local Redirect Policy, traffic for all the new connections that get established after the policy is enforced will be redirected. But if you have existing active connections to remote pods that match the configurations specified in the policy, then these might not get redirected. To ensure all such connections are redirected locally, restart the client pods after configuring the CiliumLocalRedirectPolicy.

Local Redirect Policy updates are currently not supported. If there are any changes to be made, delete the existing policy, and re-create a new one.

## Use Cases[](#use-cases "Link to this heading")

Local Redirect Policy allows Cilium to support the following use cases:

### Node-local DNS cache[](#node-local-dns-cache "Link to this heading")

[DNS node-cache](https://github.com/kubernetes/dns) listens on a static IP to intercept traffic from application pods to the cluster's DNS service VIP by default, which will be bypassed when Cilium is handling service resolution at or before the veth interface of the application pod. To enable the DNS node-cache in a Cilium cluster, the following example steers traffic to a local DNS node-cache which runs as a normal pod.

-   Deploy DNS node-cache in pod namespace.

    Deploy DNS node-cache.

    Note

    -   The example yaml is populated with default values for `__PILLAR_LOCAL_DNS__`{.docutils .literal .notranslate} and `__PILLAR_DNS_DOMAIN__`{.docutils .literal .notranslate}.

    -   If you have a different deployment, please follow the official [NodeLocal DNSCache Configuration](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/#configuration) to fill in the required template variables `__PILLAR__LOCAL__DNS__`{.docutils .literal .notranslate}, `__PILLAR__DNS__DOMAIN__`{.docutils .literal .notranslate}, and `__PILLAR__DNS__SERVER__`{.docutils .literal .notranslate} before applying the yaml.

    ``` {#codecell34 .literal-block}
    $ wget https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-local-redirect/node-local-dns.yaml

    $ kubedns=$(kubectl get svc kube-dns -n kube-system -o jsonpath={.spec.clusterIP}) && sed -i "s/__PILLAR__DNS__SERVER__/$kubedns/g;" node-local-dns.yaml

    $ kubectl apply -f node-local-dns.yaml
    ```

    Copy First Line Copy All

    -   Follow the official [NodeLocal DNSCache Configuration](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/#configuration) to fill in the required template variables `__PILLAR__LOCAL__DNS__`{.docutils .literal .notranslate}, `__PILLAR__DNS__DOMAIN__`{.docutils .literal .notranslate}, and `__PILLAR__DNS__SERVER__`{.docutils .literal .notranslate} before applying the yaml.

    -   Make sure to use a Node-local DNS image with a release version \>= 1.15.16. This is to ensure that we have a knob to disable dummy network interface creation/deletion in Node-local DNS when we deploy it in non-host namespace.

    -   Modify Node-local DNS cache's deployment yaml to pass these additional arguments to node-cache: `-skipteardown=true`{.docutils .literal .notranslate}, `-setupinterface=false`{.docutils .literal .notranslate}, and `-setupiptables=false`{.docutils .literal .notranslate}.

    -   Modify Node-local DNS cache's deployment yaml to put it in non-host namespace by setting `hostNetwork:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`false`{.docutils .literal .notranslate} for the daemonset.

    -   In the Corefile, bind to `0.0.0.0`{.docutils .literal .notranslate} instead of the static IP.

    -   In the Corefile, let CoreDNS serve health-check on its own IP instead of the static IP by removing the host IP string after health plugin.

    -   Modify Node-local DNS cache's deployment yaml to point readiness probe to its own IP by removing the `host`{.docutils .literal .notranslate} field under `readinessProbe`{.docutils .literal .notranslate}.

-   Deploy Local Redirect Policy (LRP) to steer DNS traffic to the node local dns cache.

    ``` {#codecell35 .literal-block}
    $ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-local-redirect/node-local-dns-lrp.yaml
    ```

    Copy Line

    Note

    -   The LRP above uses `kube-dns`{.docutils .literal .notranslate} for the cluster DNS service, however if your cluster DNS service is different, you will need to modify this example LRP to specify it.

    -   The namespace specified in the LRP above is set to the same namespace as the cluster's dns service.

    -   The LRP above uses the same port names `dns`{.docutils .literal .notranslate} and `dns-tcp`{.docutils .literal .notranslate} as the example quick deployment yaml, you will need to modify those to match your deployment if they are different.

After all `node-local-dns`{.docutils .literal .notranslate} pods are in ready status, DNS traffic will now go to the local node-cache first. You can verify by checking the DNS cache's metrics `coredns_dns_requests_total`{.docutils .literal .notranslate} via curling `<node-local-dns`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`pod`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`IP>:9253/metrics`{.docutils .literal .notranslate}, the metric should increment as new DNS requests being issued from application pods are now redirected to the `node-local-dns`{.docutils .literal .notranslate} pod.

In the absence of a node-local DNS cache, DNS queries from application pods will get directed to cluster DNS pods backed by the `kube-dns`{.docutils .literal .notranslate} service.

-   Troubleshooting

    > If DNS requests are failing to resolve, check the following:
    >
    > > -   Ensure that the node-local DNS cache pods are running and ready.
    > >
    > > > ``` {#codecell36}
    > > > $ kubectl --namespace kube-system get pods --selector=k8s-app=node-local-dns
    > > > NAME                   READY   STATUS    RESTARTS   AGE
    > > > node-local-dns-72r7m   1/1     Running   0          2d2h
    > > > node-local-dns-gc5bx   1/1     Running   0          2d2h
    > > > ```
    > > >
    > > > Copy First Line Copy Commands Copy All
    > >
    > > -   Check if the local redirect policy has been applied correctly on all the cilium agent pods.
    > >
    > > > ``` {#codecell37}
    > > > $ kubectl exec -it cilium-mhnhz -n kube-system -- cilium-dbg lrp list
    > > > LRP namespace   LRP name       FrontendType                Matching Service
    > > > kube-system     nodelocaldns   clusterIP + all svc ports   kube-system/kube-dns
    > > >                 |              10.96.0.10:53/UDP -> 10.244.1.49:53(kube-system/node-local-dns-72r7m),
    > > >                 |              10.96.0.10:53/TCP -> 10.244.1.49:53(kube-system/node-local-dns-72r7m),
    > > > ```
    > > >
    > > > Copy First Line Copy Commands Copy All
    > >
    > > -   Check if the corresponding local redirect service entry has been created. If the service entry is missing, there might have been a race condition in applying the policy and the node-local DNS DaemonSet pod resources. As a workaround, you can restart the node-local DNS DaemonSet pods. File a [GitHub issue](https://github.com/cilium/cilium/issues/new/choose) with a [sysdump](../../../operations/troubleshooting/#sysdump) if the issue persists.
    > >
    > > > ``` {#codecell38}
    > > > $ kubectl exec -it cilium-mhnhz -n kube-system -- cilium-dbg service list | grep LocalRedirect
    > > > 11   10.96.0.10:53      LocalRedirect   1 => 10.244.1.49:53 (active)
    > > > ```
    > > >
    > > > Copy First Line Copy Commands Copy All

## Advanced configurations[](#advanced-configurations "Link to this heading")

When a local redirect policy is applied, cilium BPF datapath redirects traffic going to the policy frontend (identified by ip/port/protocol tuple) address to a node-local backend pod selected by the policy. However, for traffic originating from a node-local backend pod destined to the policy frontend, users may want to skip redirecting the traffic back to the node-local backend pod, and instead forward the traffic to the original frontend. This behavior can be enabled by setting the `skipRedirectFromBackend`{.docutils .literal .notranslate} flag to `true`{.docutils .literal .notranslate} in the local redirect policy spec. This configuration requires the use of `getsockopt()`{.docutils .literal .notranslate} with the `SO_NETNS_COOKIE`{.docutils .literal .notranslate} option, which is available in Linux kernel version \>= 5.12. Note that `SO_NETNS_COOKIE`{.docutils .literal .notranslate} was introduced in 5.7 (available to BPF programs), and exposed to user space in versions \>= 5.12.

Note

In order to enable this configuration starting Cilium version 1.16.0, previously applied local redirect policies and policies selected backend pods need to be deleted, and re-created.
