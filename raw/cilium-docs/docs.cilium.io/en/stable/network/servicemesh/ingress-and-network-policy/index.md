---
{"title": "Ingress and Network Policy Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/ingress-and-network-policy/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Ingress and Network Policy Example[](#ingress-and-network-policy-example "Link to this heading")

This example uses the same configuration as the base HTTP Ingress example, using the `bookinfo`{.docutils .literal .notranslate} demo microservices app from the Istio project, and then adds CiliumNetworkPolicy on the top.

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

## Deploy the First Ingress[](#deploy-the-first-ingress "Link to this heading")

You'll find the example Ingress definition in `basic-ingress.yaml`{.docutils .literal .notranslate}.

``` {#codecell2}
# Basic ingress for istio bookinfo demo application, which can be found in below
# https://raw.githubusercontent.com/istio/istio/release-1.11/samples/bookinfo/platform/kube/bookinfo.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: basic-ingress
  namespace: default
spec:
  ingressClassName: cilium
  rules:
  - http:
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
```

Copy First Line Copy All

``` {#codecell3 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/basic-ingress.yaml
```

Copy Line

This example routes requests for the path `/details`{.docutils .literal .notranslate} to the `details`{.docutils .literal .notranslate} service, and `/`{.docutils .literal .notranslate} to the `productpage`{.docutils .literal .notranslate} service.

Getting the list of services, you'll see a LoadBalancer service is automatically created for this ingress. Your cloud provider will automatically provision an external IP address, but it may take around 30 seconds.

``` {#codecell4}
# For dedicated load balancer mode
$ kubectl get svc
NAME                           TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE
cilium-ingress-basic-ingress   LoadBalancer   10.98.169.125    10.98.169.125   80:32478/TCP   2m11s
details                        ClusterIP      10.102.131.226   <none>          9080/TCP       2m15s
kubernetes                     ClusterIP      10.96.0.1        <none>          443/TCP        10m
productpage                    ClusterIP      10.97.231.139    <none>          9080/TCP       2m15s
ratings                        ClusterIP      10.108.152.42    <none>          9080/TCP       2m15s
reviews                        ClusterIP      10.111.145.160   <none>          9080/TCP       2m15s

# For shared load balancer mode
$ kubectl get services -n kube-system cilium-ingress
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
cilium-ingress   LoadBalancer   10.98.169.125   10.98.169.125   80:32690/TCP,443:31566/TCP   18m
```

Copy First Line Copy Commands Copy All

The external IP address should also be populated into the Ingress:

``` {#codecell5}
$ kubectl get ingress
NAME            CLASS    HOSTS   ADDRESS         PORTS   AGE
basic-ingress   cilium   *       10.98.169.125   80      97s
```

Copy First Line Copy Commands Copy All

Note

Some providers e.g. EKS use a fully-qualified domain name rather than an IP address.

Confirm that your Ingress is working:

``` {#codecell6}
$ HTTP_INGRESS=$(kubectl get ingress basic-ingress -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ curl --fail -s http://"$HTTP_INGRESS"/details/1 | jq
{
  "id": 1,
  "author": "William Shakespeare",
  "year": 1595,
  "type": "paperback",
  "pages": 200,
  "publisher": "PublisherA",
  "language": "English",
  "ISBN-10": "1234567890",
  "ISBN-13": "123-1234567890"
}
```

Copy First Line Copy Commands Copy All

# External Lock-down Policy[](#external-lock-down-policy "Link to this heading")

By default, all the external traffic is allowed. Let's apply a [CiliumNetworkPolicy](../../kubernetes/policy/#ciliumnetworkpolicy) to lock down external traffic.

``` {#codecell7}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "external-lockdown"
spec:
  description: "Block all the traffic originating from outside of the cluster"
  endpointSelector: {}
  ingress:
  - fromEntities:
    - cluster
```

Copy First Line Copy All

``` {#codecell8 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/policy/external-lockdown.yaml
```

Copy Line

With this policy applied, any request originating from outside the cluster will be rejected with a `403`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Forbidden`{.docutils .literal .notranslate}

``` {#codecell9}
$ curl --fail -v http://"$HTTP_INGRESS"/details/1
*   Trying 172.18.255.194:80...
* Connected to 172.18.255.194 (172.18.255.194) port 80
> GET /details/1 HTTP/1.1
> Host: 172.18.255.194
> User-Agent: curl/8.6.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< content-length: 15
< content-type: text/plain
< date: Thu, 29 Feb 2024 12:59:54 GMT
< server: envoy
* The requested URL returned error: 403
* Closing connection
curl: (22) The requested URL returned error: 403

# Capture hubble flows in another terminal
$ kubectl --namespace=kube-system exec -i -t cilium-xjl4x -- hubble observe -f --identity ingress
Defaulted container "cilium-agent" out of: cilium-agent, config (init), mount-cgroup (init), apply-sysctl-overwrites (init), mount-bpf-fs (init), wait-for-node-init (init), clean-cilium-state (init), install-cni-binaries (init)
Feb 29 13:00:29.389: 172.18.0.1:53866 (ingress) -> kube-system/cilium-ingress:80 (world) http-request DROPPED (HTTP/1.1 GET http://172.18.255.194/details/1)
Feb 29 13:00:29.389: 172.18.0.1:53866 (ingress) <- kube-system/cilium-ingress:80 (world) http-response FORWARDED (HTTP/1.1 403 0ms (GET http://172.18.255.194/details/1))
```

Copy First Line Copy Commands Copy All

Let's check if in-cluster traffic to the Ingress endpoint is still allowed:

``` {#codecell10 .literal-block}
# The test-application.yaml contains a client pod with curl available
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/test-application.yaml
$ kubectl exec -it deployment/client -- curl -s http://$HTTP_INGRESS/details/1
{"id":1,"author":"William Shakespeare","year":1595,"type":"paperback","pages":200,"publisher":"PublisherA","language":"English","ISBN-10":"1234567890","ISBN-13":"123-1234567890"}%
```

Copy First Line Copy All

Another common use case is to allow only a specific set of IP addresses to access the Ingress. This can be achieved via the below policy

``` {#codecell11}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "allow-cidr"
spec:
  description: "Allow all the traffic originating from a specific CIDR"
  endpointSelector:
    matchExpressions:
    - key: reserved:ingress
      operator: Exists
  ingress:
  - fromCIDRSet:
    # Please update the CIDR to match your environment
    - cidr: 172.18.0.1/32
```

Copy First Line Copy All

``` {#codecell12 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/policy/allow-ingress-cidr.yaml
```

Copy Line

``` {#codecell13}
$ curl -s --fail http://"$HTTP_INGRESS"/details/1
{"id":1,"author":"William Shakespeare","year":1595,"type":"paperback","pages":200,"publisher":"PublisherA","language":"English","ISBN-10":"1234567890","ISBN-13":"123-1234567890"}
```

Copy First Line Copy Commands Copy All

# Default Deny Ingress Policy[](#default-deny-ingress-policy "Link to this heading")

Let's apply a [CiliumClusterwideNetworkPolicy](../../kubernetes/policy/#ciliumclusterwidenetworkpolicy) to deny all traffic by default:

``` {#codecell14}
---
apiVersion: cilium.io/v2
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "default-deny"
spec:
  description: "Block all the traffic (except DNS) by default"
  egress:
  - toEndpoints:
    - matchLabels:
        io.kubernetes.pod.namespace: kube-system
        k8s-app: kube-dns
    toPorts:
    - ports:
      - port: '53'
        protocol: UDP
      rules:
        dns:
        - matchPattern: '*'
  endpointSelector:
    matchExpressions:
    - key: io.kubernetes.pod.namespace
      operator: NotIn
      values:
      - kube-system
```

Copy First Line Copy All

``` {#codecell15 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/policy/default-deny.yaml
```

Copy Line

With this policy applied, the request to the `/details`{.docutils .literal .notranslate} endpoint will be denied for external and in-cluster traffic.

``` {#codecell16}
$ curl --fail -v http://"$HTTP_INGRESS"/details/1
*   Trying 172.19.255.194:80...
* Connected to 172.19.255.194 (172.19.255.194) port 80
> GET /details/1 HTTP/1.1
> Host: 172.19.255.194
> User-Agent: curl/8.6.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< content-length: 15
< content-type: text/plain
< date: Sun, 17 Mar 2024 13:52:38 GMT
< server: envoy
* The requested URL returned error: 403
* Closing connection
curl: (22) The requested URL returned error: 403

# Capture hubble flows in another terminal
$ kubectl --namespace=kube-system exec -i -t cilium-xjl4x -- hubble observe -f --identity ingress
Defaulted container "cilium-agent" out of: cilium-agent, config (init), mount-cgroup (init), apply-sysctl-overwrites (init), mount-bpf-fs (init), wait-for-node-init (init), clean-cilium-state (init), install-cni-binaries (init)
Mar 17 13:56:00.709: 172.19.0.1:34104 (ingress) -> default/cilium-ingress-basic-ingress:80 (world) http-request DROPPED (HTTP/1.1 GET http://172.19.255.194/details/1)
Mar 17 13:56:00.709: 172.19.0.1:34104 (ingress) <- default/cilium-ingress-basic-ingress:80 (world) http-response FORWARDED (HTTP/1.1 403 0ms (GET http://172.19.255.194/details/1))
```

Copy First Line Copy Commands Copy All

Now let's check if in-cluster traffic to the same endpoint is denied:

``` {#codecell17 .literal-block}
# The test-application.yaml contains a client pod with curl available
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/test-application.yaml
$ kubectl exec -it deployment/client -- curl -s http://$HTTP_INGRESS/details/1
Access denied
```

Copy First Line Copy All

The next step is to allow ingress traffic to the `/details`{.docutils .literal .notranslate} endpoint:

``` {#codecell18}
---
apiVersion: cilium.io/v2
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: allow-ingress-egress
spec:
  description: "Allow all the egress traffic from reserved ingress identity to any endpoints in the cluster"
  endpointSelector:
    matchExpressions:
    - key: reserved:ingress
      operator: Exists
  egress:
  - toEntities:
    - cluster
```

Copy First Line Copy All

``` {#codecell19 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/policy/allow-ingress-cluster.yaml
```

Copy Line

``` {#codecell20}
$ curl -s --fail http://"$HTTP_INGRESS"/details/1
{"id":1,"author":"William Shakespeare","year":1595,"type":"paperback","pages":200,"publisher":"PublisherA","language":"English","ISBN-10":"1234567890","ISBN-13":"123-1234567890"}
$ kubectl exec -it deployment/client -- curl -s http://$HTTP_INGRESS/details/1
{"id":1,"author":"William Shakespeare","year":1595,"type":"paperback","pages":200,"publisher":"PublisherA","language":"English","ISBN-10":"1234567890","ISBN-13":"123-1234567890"}
```

Copy First Line Copy Commands Copy All

NetworkPolicy that selects `reserved:ingress`{.docutils .literal .notranslate} and allows egress to specific identities could also be used. But in general, it's probably more reliable to allow all traffic from the `reserved:ingress`{.docutils .literal .notranslate} identity to all `cluster`{.docutils .literal .notranslate} identities, given that Cilium Ingress is part of the networking infrastructure.
