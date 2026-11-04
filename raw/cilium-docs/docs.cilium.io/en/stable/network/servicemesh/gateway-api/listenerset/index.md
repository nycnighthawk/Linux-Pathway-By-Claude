---
{"title": "ListenerSet Support", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/listenerset/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# ListenerSet Support[](#listenerset-support "Link to this heading")

[ListenerSet](https://gateway-api.sigs.k8s.io/guides/user-guides/listener-set/) allows additional groups of listeners, defined in ListenerSet resources, to attach to a single Gateway. This lets an infrastructure owner manage the Gateway while application owners manage their listeners and TLS certificates in separate namespaces. All attached listeners use the parent Gateway's address and infrastructure.

Cilium supports the standard ListenerSet API. This feature does not require a separate Cilium feature flag. Install the ListenerSet CRD before starting the Cilium operator so that ListenerSet support is detected during startup (see [prerequisites](../gateway-api/#gs-gateway-api-prerequisites)). When adding the CRD to an existing installation, restart the Cilium operator afterward so that it can detect the new resource and enable ListenerSet support.

Note

By default, a Gateway resource does not accept ListenerSets. To enable ListenerSet attachment for a Gateway, use `spec.allowedListeners`{.docutils .literal .notranslate} to select the namespaces from which ListenerSets may attach.

## Delegate a listener[](#delegate-a-listener "Link to this heading")

The following example creates a Gateway in the `default`{.docutils .literal .notranslate} namespace and allows ListenerSets from namespaces with the `gateway-access:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`"true"`{.docutils .literal .notranslate} label. The ListenerSet and HTTPRoute are created in the `listenerset-demo`{.docutils .literal .notranslate} namespace which has this label.

``` {#codecell0}
---
apiVersion: v1
kind: Namespace
metadata:
  name: listenerset-demo
  labels:
    gateway-access: "true"
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: shared-gateway
  namespace: default
spec:
  gatewayClassName: cilium
  allowedListeners:
    namespaces:
      from: Selector
      selector:
        matchLabels:
          gateway-access: "true"
  listeners:
  - name: base-http
    protocol: HTTP
    port: 8081
---
apiVersion: gateway.networking.k8s.io/v1
kind: ListenerSet
metadata:
  name: delegated-listeners
  namespace: listenerset-demo
spec:
  parentRef:
    name: shared-gateway
    namespace: default
  listeners:
  - name: echo
    hostname: echo.example.com
    protocol: HTTP
    port: 80
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: echo
  namespace: listenerset-demo
spec:
  parentRefs:
  - group: gateway.networking.k8s.io
    kind: ListenerSet
    name: delegated-listeners
    sectionName: echo
  hostnames:
  - echo.example.com
  rules:
  - backendRefs:
    - name: echo-1
      port: 8080
```

Copy First Line Copy All

Apply the configuration and deploy the echo application in the delegated namespace:

``` {#codecell1 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/listenerset.yaml
$ kubectl -n listenerset-demo apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/echo-basic.yaml
```

Copy First Line Copy All

Routes attach directly to the resource that defines their listener. The HTTPRoute specifies `kind:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ListenerSet`{.docutils .literal .notranslate} and selects the `echo`{.docutils .literal .notranslate} listener. A Route which references only the Gateway would not attach to any ListenerSet listeners.

## Verify the ListenerSet[](#verify-the-listenerset "Link to this heading")

Check both the parent Gateway and the ListenerSet:

``` {#codecell2}
$ kubectl get gateway shared-gateway
NAME             CLASS    ADDRESS          PROGRAMMED   AGE
shared-gateway   cilium   192.0.2.100      True         1m

$ kubectl get listenerset -n listenerset-demo delegated-listeners
NAME                  ACCEPTED   PROGRAMMED   AGE
delegated-listeners   True       True         1m
```

Copy First Line Copy Commands Copy All

Send a request to the listener:

``` {#codecell3}
$ GATEWAY=$(kubectl get gateway shared-gateway -o jsonpath='{.status.addresses[0].value}')
$ curl --fail --header 'Host: echo.example.com' http://$GATEWAY/
```

Copy First Line Copy Commands Copy All

The Gateway reports the number of attached ListenerSets that contain at least one valid listener in `status.attachedListenerSets`{.docutils .literal .notranslate}. Detailed status for delegated listeners appears in the ListenerSet's `status.listeners`{.docutils .literal .notranslate} field. When troubleshooting, inspect the Accepted, Programmed, ResolvedRefs, and Conflicted conditions for each listener. Also confirm that the parent Gateway is programmed and has an address.

``` {#codecell4}
$ kubectl describe gateways -n default shared-gateway | grep Attached
  Attached Listener Sets:  1
    Attached Routes:  0

$ kubectl describe listenerset -n listenerset-demo delegated-listeners | grep Attached
    Attached Routes:  1
```

Copy First Line Copy Commands Copy All

## Operational considerations[](#operational-considerations "Link to this heading")

-   The Gateway controls which ListenerSet namespaces are accepted with `allowedListeners`{.docutils .literal .notranslate}. By default, no ListenerSets are allowed.

-   Each ListenerSet listener independently controls Route attachment with `allowedRoutes`{.docutils .literal .notranslate}. When this field is omitted, Routes from the ListenerSet's namespace are allowed.

-   A Route parent reference must explicitly set `kind:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ListenerSet`{.docutils .literal .notranslate}. If the kind is omitted, it defaults to `Gateway`{.docutils .literal .notranslate}.

-   HTTPRoute, GRPCRoute, TLSRoute, and the optional TCPRoute and UDPRoute APIs can target compatible listeners in a ListenerSet.

-   Listeners defined directly on the Gateway take precedence over conflicting ListenerSet listeners. Among ListenerSets, older ListenerSets take precedence. Conflicts are reported on the lower-precedence listener.

-   A ListenerSet with a mixture of valid and invalid listeners can be accepted. Check each listener's status instead of relying only on the ListenerSet's top-level conditions.

-   Certificate references are evaluated from the ListenerSet's namespace. A cross-namespace Secret requires a ReferenceGrant for the ListenerSet. Grants made to the parent Gateway are not inherited.

-   The parent Gateway must retain at least one valid listener of its own. A valid ListenerSet does not make an otherwise invalid Gateway accepted.

See the upstream [ListenerSet documentation](https://gateway-api.sigs.k8s.io/guides/user-guides/listener-set/) for complete attachment, conflict, and status semantics.
