---
{"title": "Locking Down External Access with DNS-Based Policies", "url": "https://docs.cilium.io/en/stable/security/dns/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Locking Down External Access with DNS-Based Policies[](#locking-down-external-access-with-dns-based-policies "Link to this heading")

This document serves as an introduction for using Cilium to enforce DNS-based security policies for Kubernetes pods.

If you haven't read the [Introduction to Cilium & Hubble](../../overview/intro/#intro) yet, we'd encourage you to do that first.

The best way to get help if you get stuck is to ask a question on [Cilium Slack](https://slack.cilium.io). With Cilium contributors across the globe, there is almost always someone available to help.

## Setup Cilium[](#setup-cilium "Link to this heading")

If you have not set up Cilium yet, follow the guide [Cilium Quick Installation](../../gettingstarted/k8s-install-default/#k8s-install-standard) for instructions on how to quickly bootstrap a Kubernetes cluster and install Cilium. If in doubt, pick the minikube route, you will be good to go in less than 5 minutes.

## Deploy the Demo Application[](#deploy-the-demo-application "Link to this heading")

DNS-based policies are very useful for controlling access to services running outside the Kubernetes cluster. DNS acts as a persistent service identifier for both external services provided by AWS, Google, Twilio, Stripe, etc., and internal services such as database clusters running in private subnets outside Kubernetes. CIDR or IP-based policies are cumbersome and hard to maintain as the IPs associated with external services can change frequently. The Cilium DNS-based policies provide an easy mechanism to specify access control while Cilium manages the harder aspects of tracking DNS to IP mapping.

In this guide we will learn about:

-   Controlling egress access to services outside the cluster using DNS-based policies

-   Using patterns (or wildcards) to whitelist a subset of DNS domains

-   Combining DNS, port and L7 rules for restricting access to external service

In line with our Star Wars theme examples, we will use a simple scenario where the Empire's `mediabot`{.docutils .literal .notranslate} pods need access to GitHub for managing the Empire's git repositories. The pods shouldn't have access to any other external service.

``` {#codecell0 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-dns/dns-sw-app.yaml
$ kubectl wait pod/mediabot --for=condition=Ready
$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
pod/mediabot                     1/1     Running   0          14s
```

Copy First Line Copy All

## Apply DNS Egress Policy[](#apply-dns-egress-policy "Link to this heading")

The following Cilium network policy allows `mediabot`{.docutils .literal .notranslate} pods to only access `api.github.com`{.docutils .literal .notranslate}.

``` {#codecell1}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "fqdn"
spec:
  endpointSelector:
    matchLabels:
      org: empire
      class: mediabot
  egress:
  - toFQDNs:
    - matchName: "api.github.com"
  - toEndpoints:
    - matchLabels:
        "k8s:io.kubernetes.pod.namespace": kube-system
        "k8s:k8s-app": kube-dns
    toPorts:
    - ports:
      - port: "53"
        protocol: ANY
      rules:
        dns:
        - matchPattern: "*"
```

Copy First Line Copy All

``` {#codecell2}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "fqdn"
spec:
  endpointSelector:
    matchLabels:
      org: empire
      class: mediabot
  egress:
  - toFQDNs:
    - matchName: "api.github.com"  
  - toEndpoints:
    - matchLabels:
        "k8s:io.kubernetes.pod.namespace": openshift-dns
    toPorts:
    - ports:
      - port: "5353"
        protocol: ANY
      rules:
        dns:
        - matchPattern: "*"
```

Copy First Line Copy All

Note

OpenShift users will need to modify the policies to match the namespace `openshift-dns`{.docutils .literal .notranslate} (instead of `kube-system`{.docutils .literal .notranslate}), remove the match on the `k8s:k8s-app=kube-dns`{.docutils .literal .notranslate} label, and change the port to 5353.

Let's take a closer look at the policy:

-   The first egress section uses `toFQDNs:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`matchName`{.docutils .literal .notranslate} specification to allow egress to `api.github.com`{.docutils .literal .notranslate}. The destination DNS should match exactly the name specified in the rule. The `endpointSelector`{.docutils .literal .notranslate} allows only pods with labels `class:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`mediabot,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`org:empire`{.docutils .literal .notranslate} to have the egress access.

-   The second egress section (`toEndpoints`{.docutils .literal .notranslate}) allows `mediabot`{.docutils .literal .notranslate} pods to access `kube-dns`{.docutils .literal .notranslate} service. Note that `rules:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`dns`{.docutils .literal .notranslate} instructs Cilium to inspect and allow DNS lookups matching specified patterns. In this case, inspect and allow all DNS queries.

Note that with this policy the `mediabot`{.docutils .literal .notranslate} doesn't have access to any internal cluster service other than `kube-dns`{.docutils .literal .notranslate}. Refer to [Overview of Network Policy](../policy/#id1) to learn more about policies for controlling access to internal cluster services.

Let's apply the policy:

``` {#codecell3 .literal-block}
kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-dns/dns-matchname.yaml
```

Copy Line

Testing the policy, we see that `mediabot`{.docutils .literal .notranslate} has access to `api.github.com`{.docutils .literal .notranslate} but doesn't have access to any other external service, e.g., `support.github.com`{.docutils .literal .notranslate}.

``` {#codecell4}
$ kubectl exec mediabot -- curl -I -s https://api.github.com | head -1
HTTP/2 200

$ kubectl exec mediabot -- curl -I -s --max-time 5 https://support.github.com | head -1
curl: (28) Connection timed out after 5000 milliseconds
command terminated with exit code 28
```

Copy First Line Copy Commands Copy All

## DNS Policies Using Patterns[](#dns-policies-using-patterns "Link to this heading")

The above policy controlled DNS access based on exact match of the DNS domain name. Often, it is required to allow access to a subset of domains. Let's say, in the above example, `mediabot`{.docutils .literal .notranslate} pods need access to any GitHub sub-domain, e.g., the pattern `*.github.com`{.docutils .literal .notranslate}. We can achieve this easily by changing the `toFQDN`{.docutils .literal .notranslate} rule to use `matchPattern`{.docutils .literal .notranslate} instead of `matchName`{.docutils .literal .notranslate}.

``` {#codecell5}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "fqdn"
spec:
  endpointSelector:
    matchLabels:
      org: empire
      class: mediabot
  egress:
  - toFQDNs:
    - matchPattern: "*.github.com"
  - toEndpoints:
    - matchLabels:
        "k8s:io.kubernetes.pod.namespace": kube-system
        "k8s:k8s-app": kube-dns
    toPorts:
    - ports:
      - port: "53"
        protocol: ANY
      rules:
        dns:
        - matchPattern: "*"
```

Copy First Line Copy All

``` {#codecell6 .literal-block}
kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-dns/dns-pattern.yaml
```

Copy Line

Test that `mediabot`{.docutils .literal .notranslate} has access to multiple GitHub services for which the DNS matches the pattern `*.github.com`{.docutils .literal .notranslate}. It is important to note and test that this doesn't allow access to `github.com`{.docutils .literal .notranslate} because the `*.`{.docutils .literal .notranslate} in the pattern requires one subdomain to be present in the DNS name. You can simply add more `matchName`{.docutils .literal .notranslate} and `matchPattern`{.docutils .literal .notranslate} clauses to extend the access. (See [DNS based](../policy/layer3/#dns-based) policies to learn more about specifying DNS rules using patterns and names.)

``` {#codecell7}
$ kubectl exec mediabot -- curl -I -s https://support.github.com | head -1
HTTP/1.1 200 OK

$ kubectl exec mediabot -- curl -I -s https://gist.github.com | head -1
HTTP/1.1 302 Found

$ kubectl exec mediabot -- curl -I -s --max-time 5 https://github.com | head -1
curl: (28) Connection timed out after 5000 milliseconds
command terminated with exit code 28
```

Copy First Line Copy Commands Copy All

## Combining DNS, Port and L7 Rules[](#combining-dns-port-and-l7-rules "Link to this heading")

The DNS-based policies can be combined with port (L4) and API (L7) rules to further restrict the access. In our example, we will restrict `mediabot`{.docutils .literal .notranslate} pods to access GitHub services only on ports `443`{.docutils .literal .notranslate}. The `toPorts`{.docutils .literal .notranslate} section in the policy below achieves the port-based restrictions along with the DNS-based policies.

``` {#codecell8}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "fqdn"
spec:
  endpointSelector:
    matchLabels:
      org: empire
      class: mediabot
  egress:
  - toFQDNs:
    - matchPattern: "*.github.com"
    toPorts:
    - ports:
      - port: "443"
        protocol: TCP
  - toEndpoints:
    - matchLabels:
        "k8s:io.kubernetes.pod.namespace": kube-system
        "k8s:k8s-app": kube-dns
    toPorts:
    - ports:
      - port: "53"
        protocol: ANY
      rules:
        dns:
        - matchPattern: "*"
```

Copy First Line Copy All

``` {#codecell9 .literal-block}
kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-dns/dns-port.yaml
```

Copy Line

Testing, the access to `https://support.github.com`{.docutils .literal .notranslate} on port `443`{.docutils .literal .notranslate} will succeed but the access to `http://support.github.com`{.docutils .literal .notranslate} on port `80`{.docutils .literal .notranslate} will be denied.

``` {#codecell10}
$ kubectl exec mediabot -- curl -I -s https://support.github.com | head -1
HTTP/1.1 200 OK

$ kubectl exec mediabot -- curl -I -s --max-time 5 http://support.github.com | head -1
curl: (28) Connection timed out after 5001 milliseconds
command terminated with exit code 28
```

Copy First Line Copy Commands Copy All

Refer to [Layer 4 Policies](../policy/layer4/#l4-policy) and [Layer 7 Policies](../policy/layer7/#l7-policy) to learn more about Cilium L4 and L7 network policies.

## Clean-up[](#clean-up "Link to this heading")

``` {#codecell11 .literal-block}
kubectl delete -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-dns/dns-sw-app.yaml
kubectl delete cnp fqdn
```

Copy First Line Copy All

## Limitations[](#limitations "Link to this heading")

By default, Cilium uses an in-agent DNS proxy for DNS policy enforcement. For high availability, consider using the [Standalone DNS Proxy (alpha)](../standalone-dns-proxy/#standalone-dns-proxy) (alpha feature).
