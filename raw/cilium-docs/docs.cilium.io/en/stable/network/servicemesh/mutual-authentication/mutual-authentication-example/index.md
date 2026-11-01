---
{"title": "Mutual Authentication Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/mutual-authentication/mutual-authentication-example/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Mutual Authentication Example[](#mutual-authentication-example "Link to this heading")

This example shows you how to enforce mutual authentication between two Pods.

Deploy a client (pod-worker) and a server (echo) using the following manifest:

``` {#codecell0 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/mutual-auth-example.yaml
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/cnp-without-mutual-auth.yaml
service/echo created
deployment.apps/echo created
pod/pod-worker created
ciliumnetworkpolicy.cilium.io/no-mutual-auth-echo created
```

Copy First Line Copy All

Verify that the Pods have been successfully deployed:

``` {#codecell1}
$ kubectl get svc echo
NAME   TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
echo   ClusterIP   10.96.16.90   <none>        3000/TCP   42m
$ kubectl get pod pod-worker
NAME         READY   STATUS    RESTARTS   AGE
pod-worker   1/1     Running   0          40m
```

Copy First Line Copy Commands Copy All

Verify that the network policy has been deployed successfully and filters the traffic as expected.

Run the following commands:

``` {#codecell2}
$ kubectl exec -it pod-worker -- curl -s -o /dev/null -w "%{http_code}" http://echo:3000/headers
200
$ kubectl exec -it pod-worker -- curl http://echo:3000/headers-1
Access denied
```

Copy First Line Copy Commands Copy All

The first request should be successful (the *pod-worker* Pod is able to connect to the *echo* Service over a specific HTTP path and the HTTP status code is `200`{.docutils .literal .notranslate}). The second one should be denied (the *pod-worker* Pod is unable to connect to the *echo* Service over a specific HTTP path other than '/headers').

Before we enable mutual authentication between `pod-worker`{.docutils .literal .notranslate} and `echo`{.docutils .literal .notranslate}, let's verify that the SPIRE server is healthy.

Assuming you have followed the installation instructions and have a SPIRE server serving Cilium, adding mutual authentication simply requires adding `authentication.mode:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"required"`{.docutils .literal .notranslate} in the ingress/egress block in your network policies.

## Verify SPIRE Health[](#verify-spire-health "Link to this heading")

Note

This example assumes a default SPIRE installation.

Let's first verify that the SPIRE server and agents automatically deployed are working as expected.

The SPIRE server is deployed as a StatefulSet and the SPIRE agents are deployed as a DaemonSet (you should therefore see one SPIRE agent per node).

``` {#codecell3}
$ kubectl get all -n cilium-spire
NAME                    READY   STATUS    RESTARTS   AGE
pod/spire-agent-27jd7   1/1     Running   0          144m
pod/spire-agent-qkc8l   1/1     Running   0          144m
pod/spire-server-0      2/2     Running   0          144m

NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/spire-server   ClusterIP   10.96.124.177   <none>        8081/TCP   144m

NAME                         DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
daemonset.apps/spire-agent   2         2         2       2            2           <none>          144m

NAME                            READY   AGE
statefulset.apps/spire-server   1/1     144m
```

Copy First Line Copy Commands Copy All

Run a healthcheck on the SPIRE server.

``` {#codecell4}
$ kubectl exec -n cilium-spire spire-server-0 -c spire-server -- /opt/spire/bin/spire-server healthcheck
Server is healthy.
```

Copy First Line Copy Commands Copy All

Verify the list of attested agents:

``` {#codecell5}
$ kubectl exec -n cilium-spire spire-server-0 -c spire-server -- /opt/spire/bin/spire-server agent list
Found 2 attested agents:

SPIFFE ID         : spiffe://spiffe.cilium/spire/agent/k8s_psat/default/64745bf2-bd9d-4e42-bb2b-e095a6b65121
Attestation type  : k8s_psat
Expiration time   : 2023-07-04 18:39:50 +0000 UTC
Serial number     : 110848236251310359782141595494072495768

SPIFFE ID         : spiffe://spiffe.cilium/spire/agent/k8s_psat/default/d4a8a6da-d808-4993-b67a-bed250bbc53e
Attestation type  : k8s_psat
Expiration time   : 2023-07-04 18:39:55 +0000 UTC
Serial number     : 7806033782886940845084156064765627978
```

Copy First Line Copy Commands Copy All

Notice that the SPIRE Server uses Kubernetes Projected Service Account Tokens (PSATs) to verify the Identity of a SPIRE Agent running on a Kubernetes Cluster. Projected Service Account Tokens provide additional security guarantees over traditional Kubernetes Service Account Tokens and when supported by a Kubernetes cluster, PSAT is the recommended attestation strategy.

## Verify SPIFFE Identities[](#verify-spiffe-identities "Link to this heading")

Now that we know the SPIRE service is healthy, let's verify that the Cilium and SPIRE integration has been successful:

-   The Cilium agent and operator should have a registered delegate Identity with the SPIRE Server.

-   The Cilium operator should have registered Identities with the SPIRE server on behalf of the workloads (Kubernetes Pods).

Verify that the Cilium agent and operator have Identities on the SPIRE server:

``` {#codecell6}
$ kubectl exec -n cilium-spire spire-server-0 -c spire-server -- /opt/spire/bin/spire-server entry show -parentID spiffe://spiffe.cilium/ns/cilium-spire/sa/spire-agent
Found 2 entries
Entry ID         : b6424c87-4323-4d64-98dd-cd5b51a1fcbb
SPIFFE ID        : spiffe://spiffe.cilium/cilium-agent
Parent ID        : spiffe://spiffe.cilium/ns/cilium-spire/sa/spire-agent
Revision         : 0
X509-SVID TTL    : default
JWT-SVID TTL     : default
Selector         : k8s:ns:kube-system
Selector         : k8s:sa:cilium

Entry ID         : 8aa91d65-16c4-48a0-bc1f-c9bf26e6a25f
SPIFFE ID        : spiffe://spiffe.cilium/cilium-operator
Parent ID        : spiffe://spiffe.cilium/ns/cilium-spire/sa/spire-agent
Revision         : 0
X509-SVID TTL    : default
JWT-SVID TTL     : default
Selector         : k8s:ns:kube-system
Selector         : k8s:sa:cilium-operator
```

Copy First Line Copy Commands Copy All

Next, verify that the *echo* Pod has an Identity registered with the SPIRE server.

To do this, you must first construct the Pod's SPIFFE ID. The SPIFFE ID for a workload is based on the `spiffe://spiffe.cilium/identity/$IDENTITY_ID`{.docutils .literal .notranslate} format, where `$IDENTITY_ID`{.docutils .literal .notranslate} is a workload's Cilium Identity.

Grab the Cilium Identity for the *echo* Pod;

``` {#codecell7}
$ IDENTITY_ID=$(kubectl get cep -l app=echo -o=jsonpath='{.items[0].status.identity.id}')
$ echo $IDENTITY_ID
17947
```

Copy First Line Copy Commands Copy All

Use the Cilium Identity for the *echo* pod to construct its SPIFFE ID and check it is registered on the SPIRE server:

``` {#codecell8}
$ kubectl exec -n cilium-spire spire-server-0 -c spire-server -- /opt/spire/bin/spire-server entry show -spiffeID spiffe://spiffe.cilium/identity/$IDENTITY_ID
Found 1 entry
Entry ID         : 9fc13971-fb19-4814-b9f0-737b30e336c6
SPIFFE ID        : spiffe://spiffe.cilium/identity/17947
Parent ID        : spiffe://spiffe.cilium/cilium-operator
Revision         : 0
X509-SVID TTL    : default
JWT-SVID TTL     : default
Selector         : cilium:mutual-auth
```

Copy First Line Copy Commands Copy All

You can see the that the *cilium-operator* was listed in the `Parent`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ID`{.docutils .literal .notranslate}. That is because the Cilium operator creates SPIRE entries for Cilium Identities as they are created.

To get all registered entries, execute the following command:

``` {#codecell9}
kubectl exec -n cilium-spire spire-server-0 -c spire-server -- /opt/spire/bin/spire-server entry show -selector cilium:mutual-auth
```

Copy Line

There are as many entries as there are identities. Verify that these match by running the command:

``` {#codecell10}
kubectl get ciliumidentities
```

Copy Line

The identify ID listed under `NAME`{.docutils .literal .notranslate} should match with the digits at the end of the SPIFFE ID executed in the previous command.

## Enforce Mutual Authentication[](#enforce-mutual-authentication "Link to this heading")

Rolling out mutual authentication with Cilium is as simple as adding the following block to an existing or new CiliumNetworkPolicy egress or ingress rules:

``` {#codecell11}
authentication:
    mode: "required"
```

Copy First Line Copy All

Update the existing rule to only allow ingress access to mutually authenticated workloads to access *echo* using:

``` {#codecell12 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/cnp-with-mutual-auth.yaml
```

Copy Line

## Verify Mutual Authentication[](#verify-mutual-authentication "Link to this heading")

Start by enabling debug level:

``` {#codecell13}
cilium config set debug true
```

Copy Line

Re-try your connectivity tests. They should give similar results as before:

``` {#codecell14}
$ kubectl exec -it pod-worker -- curl -s -o /dev/null -w "%{http_code}" http://echo:3000/headers
200
$ kubectl exec -it pod-worker -- curl http://echo:3000/headers-1
Access denied
```

Copy First Line Copy Commands Copy All

Verify that mutual authentication has happened by accessing the logs on the agent.

Examine the logs on the Cilium agent located in the same node as the *echo* Pod. For brevity, you can search for some specific log messages by label:

``` {#codecell15}
$ kubectl -n kube-system -c cilium-agent logs -l k8s-app=cilium --timestamps=true | grep "Policy is requiring authentication\|Validating Server SNI\|Validated certificate\|Successfully authenticated"
2023-07-04T17:58:28.795760597Z level=debug msg="Policy is requiring authentication" key="localIdentity=17947, remoteIdentity=39239, remoteNodeID=54264, authType=spire" subsys=auth
2023-07-04T17:58:28.800509503Z level=debug msg="Validating Server SNI" SNI ID=39239 subsys=auth
2023-07-04T17:58:28.800525190Z level=debug msg="Validated certificate" subsys=auth uri-san="[spiffe://spiffe.cilium/identity/39239]"
2023-07-04T17:58:28.801441968Z level=debug msg="Successfully authenticated" key="localIdentity=17947, remoteIdentity=39239, remoteNodeID=54264, authType=spire" remote_node_ip=10.0.1.175 subsys=auth
```

Copy First Line Copy Commands Copy All

When you apply a mutual authentication policy, the agent retrieves the identity of the source Pod, connects to the node where the destination Pod is running and performs a mutual TLS handshake (with the log above showing one side of the mutual TLS handshake). As the handshake succeeded, the connection was authenticated and the traffic protected by policy could proceed.

Packets between the two Pods can flow until the network policy is removed or the entry expires.
