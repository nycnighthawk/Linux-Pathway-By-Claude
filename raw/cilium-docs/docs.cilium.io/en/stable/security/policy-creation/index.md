---
{"title": "Creating Policies from Verdicts", "url": "https://docs.cilium.io/en/stable/security/policy-creation/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Creating Policies from Verdicts[](#creating-policies-from-verdicts "Link to this heading")

Policy Audit Mode configures Cilium to allow all traffic while logging all connections that would otherwise be dropped by network policies. Policy Audit Mode may be configured for the entire daemon using `--policy-audit-mode=true`{.docutils .literal .notranslate} or for individual Cilium Endpoints. When Policy Audit Mode is enabled, no network policy is enforced so this setting is **not recommended for production deployment**. Policy Audit Mode supports auditing network policies implemented at networks layers 3 and 4. This guide walks through the process of creating policies using Policy Audit Mode.

If you haven't read the [Introduction to Cilium & Hubble](../../overview/intro/#intro) yet, we'd encourage you to do that first.

The best way to get help if you get stuck is to ask a question on [Cilium Slack](https://slack.cilium.io). With Cilium contributors across the globe, there is almost always someone available to help.

## Setup Cilium[](#setup-cilium "Link to this heading")

If you have not set up Cilium yet, follow the guide [Cilium Quick Installation](../../gettingstarted/k8s-install-default/#k8s-install-standard) for instructions on how to quickly bootstrap a Kubernetes cluster and install Cilium. If in doubt, pick the minikube route, you will be good to go in less than 5 minutes.

## Deploy the Demo Application[](#deploy-the-demo-application "Link to this heading")

When we have Cilium deployed and `kube-dns`{.docutils .literal .notranslate} operating correctly we can deploy our demo application.

In our Star Wars-inspired example, there are three microservices applications: *deathstar*, *tiefighter*, and *xwing*. The *deathstar* runs an HTTP webservice on port 80, which is exposed as a [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/) to load-balance requests to *deathstar* across two pod replicas. The *deathstar* service provides landing services to the empire's spaceships so that they can request a landing port. The *tiefighter* pod represents a landing-request client service on a typical empire ship and *xwing* represents a similar service on an alliance ship. They exist so that we can test different security policies for access control to *deathstar* landing services.

**Application Topology for Cilium and Kubernetes**

[](../../_images/cilium_http_gsg.png)

The file `http-sw-app.yaml`{.docutils .literal .notranslate} contains a [Kubernetes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) for each of the three services. Each deployment is identified using the Kubernetes labels (`org=empire,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`class=deathstar`{.docutils .literal .notranslate}), (`org=empire,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`class=tiefighter`{.docutils .literal .notranslate}), and (`org=alliance,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`class=xwing`{.docutils .literal .notranslate}). It also includes a deathstar-service, which load-balances traffic to all pods with label (`org=empire,`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`class=deathstar`{.docutils .literal .notranslate}).

``` {#codecell0 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/minikube/http-sw-app.yaml
service/deathstar created
deployment.apps/deathstar created
pod/tiefighter created
pod/xwing created
```

Copy First Line Copy All

Kubernetes will deploy the pods and service in the background. Running `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`pods,svc`{.docutils .literal .notranslate} will inform you about the progress of the operation. Each pod will go through several states until it reaches `Running`{.docutils .literal .notranslate} at which point the pod is ready.

``` {#codecell1}
$ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/deathstar-6fb5694d48-5hmds   1/1     Running   0          107s
pod/deathstar-6fb5694d48-fhf65   1/1     Running   0          107s
pod/tiefighter                   1/1     Running   0          107s
pod/xwing                        1/1     Running   0          107s

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
service/deathstar    ClusterIP   10.96.110.8   <none>        80/TCP    107s
service/kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP   3m53s
```

Copy First Line Copy Commands Copy All

Each pod will be represented in Cilium as an [Endpoint](../../gettingstarted/terminology/#endpoint) in the local cilium agent. We can invoke the `cilium-dbg`{.docutils .literal .notranslate} tool inside the Cilium pod to list them (in a single-node installation `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`-n`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`kube-system`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`exec`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ds/cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`--`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate} lists them all, but in a multi-node installation, only the ones running on the same node will be listed):

``` {#codecell2}
$ kubectl -n kube-system get pods -l k8s-app=cilium
NAME           READY   STATUS    RESTARTS   AGE
cilium-5ngzd   1/1     Running   0          3m19s

$ kubectl -n kube-system exec cilium-5ngzd -- cilium-dbg endpoint list
ENDPOINT   POLICY (ingress)   POLICY (egress)   IDENTITY   LABELS (source:key[=value])                       IPv6   IPv4         STATUS
           ENFORCEMENT        ENFORCEMENT
232        Disabled           Disabled          16530      k8s:class=deathstar                                      10.0.0.147   ready
                                                           k8s:io.cilium.k8s.policy.cluster=default
                                                           k8s:io.cilium.k8s.policy.serviceaccount=default
                                                           k8s:io.kubernetes.pod.namespace=default
                                                           k8s:org=empire
726        Disabled           Disabled          1          reserved:host                                                         ready
883        Disabled           Disabled          4          reserved:health                                          10.0.0.244   ready
1634       Disabled           Disabled          51373      k8s:io.cilium.k8s.policy.cluster=default                 10.0.0.118   ready
                                                           k8s:io.cilium.k8s.policy.serviceaccount=coredns
                                                           k8s:io.kubernetes.pod.namespace=kube-system
                                                           k8s:k8s-app=kube-dns
1673       Disabled           Disabled          31028      k8s:class=tiefighter                                     10.0.0.112   ready
                                                           k8s:io.cilium.k8s.policy.cluster=default
                                                           k8s:io.cilium.k8s.policy.serviceaccount=default
                                                           k8s:io.kubernetes.pod.namespace=default
                                                           k8s:org=empire
2811       Disabled           Disabled          51373      k8s:io.cilium.k8s.policy.cluster=default                 10.0.0.47    ready
                                                           k8s:io.cilium.k8s.policy.serviceaccount=coredns
                                                           k8s:io.kubernetes.pod.namespace=kube-system
                                                           k8s:k8s-app=kube-dns
2843       Disabled           Disabled          16530      k8s:class=deathstar                                      10.0.0.89    ready
                                                           k8s:io.cilium.k8s.policy.cluster=default
                                                           k8s:io.cilium.k8s.policy.serviceaccount=default
                                                           k8s:io.kubernetes.pod.namespace=default
                                                           k8s:org=empire
3184       Disabled           Disabled          22654      k8s:class=xwing                                          10.0.0.30    ready
                                                           k8s:io.cilium.k8s.policy.cluster=default
                                                           k8s:io.cilium.k8s.policy.serviceaccount=default
                                                           k8s:io.kubernetes.pod.namespace=default
                                                           k8s:org=alliance
```

Copy First Line Copy Commands Copy All

Both ingress and egress policy enforcement is still disabled on all of these pods because no network policy has been imported yet which select any of the pods.

## Scale down the deathstar Deployment[](#scale-down-the-deathstar-deployment "Link to this heading")

In this guide we're going to scale down the deathstar Deployment in order to simplify the next steps:

``` {#codecell3}
$ kubectl scale --replicas=1 deployment deathstar
deployment.apps/deathstar scaled
```

Copy First Line Copy Commands Copy All

## Enable Policy Audit Mode (Entire Daemon)[](#enable-policy-audit-mode-entire-daemon "Link to this heading")

To observe policy audit messages for all endpoints managed by this Daemonset, modify the Cilium ConfigMap and restart all daemons:

> ``` {#codecell4}
> $ kubectl patch -n $CILIUM_NAMESPACE configmap cilium-config --type merge --patch '{"data":{"policy-audit-mode":"true"}}'
> configmap/cilium-config patched
> $ kubectl -n $CILIUM_NAMESPACE rollout restart ds/cilium
> daemonset.apps/cilium restarted
> $ kubectl -n $CILIUM_NAMESPACE rollout status ds/cilium
> Waiting for daemon set "cilium" rollout to finish: 0 of 1 updated pods are available...
> daemon set "cilium" successfully rolled out
> ```
>
> Copy First Line Copy Commands Copy All
>
> If you installed Cilium via `helm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`install`{.docutils .literal .notranslate}, then you can use `helm`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`upgrade`{.docutils .literal .notranslate} to enable Policy Audit Mode:
>
> ``` {#codecell5 .literal-block}
> helm upgrade cilium cilium/cilium --version 1.20.4 \
>    --namespace $CILIUM_NAMESPACE \
>    --reuse-values \
>    --set policyAuditMode=true
> ```
>
> Copy First Line Copy All
>
> ``` {#codecell6 .literal-block}
> helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
>    --namespace $CILIUM_NAMESPACE \
>    --reuse-values \
>    --set policyAuditMode=true
> ```
>
> Copy First Line Copy All

## Enable Policy Audit Mode (Specific Endpoint)[](#enable-policy-audit-mode-specific-endpoint "Link to this heading")

Cilium can enable Policy Audit Mode for a specific endpoint. This may be helpful when enabling Policy Audit Mode for the entire daemon is too broad. Enabling per endpoint will ensure other endpoints managed by the same daemon are not impacted.

This approach is meant to be temporary. **Restarting Cilium pod will reset the Policy Audit Mode to match the daemon's configuration.**

Policy Audit Mode is enabled for a given endpoint by modifying the endpoint configuration via the `cilium-dbg`{.docutils .literal .notranslate} tool on the endpoint's Kubernetes node. The steps include:

1.  Determine the endpoint id on which Policy Audit Mode will be enabled.

2.  Identify the Cilium pod running on the same Kubernetes node corresponding to the endpoint.

3.  Using the Cilium pod above, modify the endpoint configuration by setting `PolicyAuditMode=Enabled`{.docutils .literal .notranslate}.

The following shell commands perform these steps:

``` {#codecell7}
$ PODNAME=$(kubectl get pods -l app.kubernetes.io/name=deathstar -o jsonpath='{.items[*].metadata.name}')
$ NODENAME=$(kubectl get pod -o jsonpath="{.items[?(@.metadata.name=='$PODNAME')].spec.nodeName}")
$ ENDPOINT=$(kubectl get cep -o jsonpath="{.items[?(@.metadata.name=='$PODNAME')].status.id}")
$ CILIUM_POD=$(kubectl -n "$CILIUM_NAMESPACE" get pod --all-namespaces --field-selector spec.nodeName="$NODENAME" -lk8s-app=cilium -o jsonpath='{.items[*].metadata.name}')
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    cilium-dbg endpoint config "$ENDPOINT" PolicyAuditMode=Enabled
 Endpoint 232 configuration updated successfully
```

Copy First Line Copy Commands Copy All

We can check that Policy Audit Mode is enabled for this endpoint with

``` {#codecell8}
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    cilium-dbg endpoint get "$ENDPOINT" -o jsonpath='{[*].spec.options.PolicyAuditMode}'
Enabled
```

Copy First Line Copy Commands Copy All

## Observe policy verdicts[](#observe-policy-verdicts "Link to this heading")

In this example, we are tasked with applying security policy for the deathstar. First, from the Cilium pod we need to monitor the notifications for policy verdicts using the Hubble CLI. We'll be monitoring for inbound traffic towards the deathstar to identify it and determine whether to extend the network policy to allow that traffic.

Apply a default-deny policy:

``` {#codecell9}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "empire-default-deny"
spec:
  description: "Default-deny ingress policy for the empire"
  endpointSelector:
    matchLabels:
      org: empire
  ingress:
  - {}
```

Copy First Line Copy All

CiliumNetworkPolicies match on pod labels using an `endpointSelector`{.docutils .literal .notranslate} to identify the sources and destinations to which the policy applies. The above policy denies traffic sent to any pods with label (`org=empire`{.docutils .literal .notranslate}). Due to the Policy Audit Mode enabled above (either for the entire daemon, or for just the `deathstar`{.docutils .literal .notranslate} endpoint), the traffic will not actually be denied but will instead trigger policy verdict notifications.

To apply this policy, run:

``` {#codecell10 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/minikube/sw_deny_policy.yaml
ciliumnetworkpolicy.cilium.io/empire-default-deny created
```

Copy First Line Copy All

With the above policy, we will enable a default-deny posture on ingress to pods with the label `org=empire`{.docutils .literal .notranslate} and enable the policy verdict notifications for those pods. The same principle applies on egress as well.

Now let's send some traffic from the tiefighter to the deathstar:

``` {#codecell11}
$ kubectl exec tiefighter -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
Ship landed
```

Copy First Line Copy Commands Copy All

We can check the policy verdict from the Cilium Pod:

``` {#codecell12}
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict --last 1
Feb  7 12:53:39.168: default/tiefighter:54134 (ID:31028) -> default/deathstar-6fb5694d48-5hmds:80 (ID:16530) policy-verdict:none AUDITED (TCP Flags: SYN)
```

Copy First Line Copy Commands Copy All

In the above example, we can see that the Pod `deathstar-6fb5694d48-5hmds`{.docutils .literal .notranslate} has received traffic from the `tiefighter`{.docutils .literal .notranslate} Pod which doesn't match the policy (`policy-verdict:none`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`AUDITED`{.docutils .literal .notranslate}).

## Create the Network Policy[](#create-the-network-policy "Link to this heading")

We can get more information about the flow with

``` {#codecell13}
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict -o json --last 1
```

Copy First Line Copy Commands Copy All

Given the above information, we now know the labels of the source and destination Pods, the traffic direction, and the destination port. In this case, we can see clearly that the source (i.e. the tiefighter Pod) is an empire aircraft (as it has the `org=empire`{.docutils .literal .notranslate} label) so once we've determined that we expect this traffic to arrive at the deathstar, we can form a policy to match the traffic:

``` {#codecell14}
apiVersion: "cilium.io/v2"
kind: CiliumNetworkPolicy
metadata:
  name: "rule1"
spec:
  description: "L3-L4 policy to restrict deathstar access to empire ships only"
  endpointSelector:
    matchLabels:
      org: empire
      class: deathstar
  ingress:
  - fromEndpoints:
    - matchLabels:
        org: empire
    toPorts:
    - ports:
      - port: "80"
        protocol: TCP
```

Copy First Line Copy All

To apply this L3/L4 policy, run:

``` {#codecell15 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/minikube/sw_l3_l4_policy.yaml
ciliumnetworkpolicy.cilium.io/rule1 created
```

Copy First Line Copy All

Now if we run the landing requests again,

``` {#codecell16}
$ kubectl exec tiefighter -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
Ship landed
```

Copy First Line Copy Commands Copy All

we can then observe that the traffic which was previously audited to be dropped by the policy is reported as allowed:

``` {#codecell17}
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict --last 1
...
Feb  7 13:06:45.130: default/tiefighter:59824 (ID:31028) -> default/deathstar-6fb5694d48-5hmds:80 (ID:16530) policy-verdict:L3-L4 ALLOWED (TCP Flags: SYN)
```

Copy First Line Copy Commands Copy All

Now the policy verdict states that the traffic would be allowed: `policy-verdict:L3-L4`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ALLOWED`{.docutils .literal .notranslate}. Success!

## Disable Policy Audit Mode (Entire Daemon)[](#disable-policy-audit-mode-entire-daemon "Link to this heading")

These steps should be repeated for each connection in the cluster to ensure that the network policy allows all of the expected traffic. The final step after deploying the policy is to disable Policy Audit Mode again:

> ``` {#codecell18}
> $ kubectl patch -n $CILIUM_NAMESPACE configmap cilium-config --type merge --patch '{"data":{"policy-audit-mode":"false"}}'
> configmap/cilium-config patched
> $ kubectl -n $CILIUM_NAMESPACE rollout restart ds/cilium
> daemonset.apps/cilium restarted
> $ kubectl -n $CILIUM_NAMESPACE rollout status ds/cilium
> Waiting for daemon set "cilium" rollout to finish: 0 of 1 updated pods are available...
> daemon set "cilium" successfully rolled out
> ```
>
> Copy First Line Copy Commands Copy All
>
> ``` {#codecell19 .literal-block}
> helm upgrade cilium cilium/cilium --version 1.20.4 \
>    --namespace $CILIUM_NAMESPACE \
>    --reuse-values \
>    --set policyAuditMode=false
> ```
>
> Copy First Line Copy All
>
> ``` {#codecell20 .literal-block}
> helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
>    --namespace $CILIUM_NAMESPACE \
>    --reuse-values \
>    --set policyAuditMode=false
> ```
>
> Copy First Line Copy All

## Disable Policy Audit Mode (Specific Endpoint)[](#disable-policy-audit-mode-specific-endpoint "Link to this heading")

These steps are nearly identical to enabling Policy Audit Mode.

``` {#codecell21}
$ PODNAME=$(kubectl get pods -l app.kubernetes.io/name=deathstar -o jsonpath='{.items[*].metadata.name}')
$ NODENAME=$(kubectl get pod -o jsonpath="{.items[?(@.metadata.name=='$PODNAME')].spec.nodeName}")
$ ENDPOINT=$(kubectl get cep -o jsonpath="{.items[?(@.metadata.name=='$PODNAME')].status.id}")
$ CILIUM_POD=$(kubectl -n "$CILIUM_NAMESPACE" get pod --all-namespaces --field-selector spec.nodeName="$NODENAME" -lk8s-app=cilium -o jsonpath='{.items[*].metadata.name}')
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    cilium-dbg endpoint config "$ENDPOINT" PolicyAuditMode=Disabled
 Endpoint 232 configuration updated successfully
```

Copy First Line Copy Commands Copy All

Alternatively, **restarting the Cilium pod** will set the endpoint Policy Audit Mode to the daemon set configuration.

## Verify Policy Audit Mode is Disabled[](#verify-policy-audit-mode-is-disabled "Link to this heading")

``` {#codecell22}
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    cilium-dbg endpoint get "$ENDPOINT" -o jsonpath='{[*].spec.options.PolicyAuditMode}'
Disabled
```

Copy First Line Copy Commands Copy All

Now if we run the landing requests again, only the *tiefighter* pods with the label `org=empire`{.docutils .literal .notranslate} should succeed:

``` {#codecell23}
$ kubectl exec tiefighter -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
Ship landed
```

Copy First Line Copy Commands Copy All

And we can observe that the traffic was allowed by the policy:

``` {#codecell24}
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict --from-pod tiefighter --last 1
Feb  7 13:34:26.112: default/tiefighter:37314 (ID:31028) -> default/deathstar-6fb5694d48-5hmds:80 (ID:16530) policy-verdict:L3-L4 ALLOWED (TCP Flags: SYN)
```

Copy First Line Copy Commands Copy All

This works as expected. Now the same request from an *xwing* Pod should fail:

``` {#codecell25}
$ kubectl exec xwing -- curl --connect-timeout 3 -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
command terminated with exit code 28
```

Copy First Line Copy Commands Copy All

This curl request should timeout after three seconds, we can observe the policy verdict with:

``` {#codecell26}
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict --from-pod xwing --last 1
Feb  7 13:43:46.791: default/xwing:54842 (ID:22654) <> default/deathstar-6fb5694d48-5hmds:80 (ID:16530) policy-verdict:none DENIED (TCP Flags: SYN)
```

Copy First Line Copy Commands Copy All

We hope you enjoyed the tutorial. Feel free to play more with the setup, follow the [Identity-Aware and HTTP-Aware Policy Enforcement](../http/#gs-http) guide, and reach out to us on [Cilium Slack](https://slack.cilium.io) with any questions!

## Clean-up[](#clean-up "Link to this heading")

``` {#codecell27 .literal-block}
$ kubectl delete -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/minikube/http-sw-app.yaml
$ kubectl delete cnp empire-default-deny rule1
```

Copy First Line Copy All
