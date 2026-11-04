---
{"title": "Deny Policies", "url": "https://docs.cilium.io/en/stable/security/policy/deny/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Deny Policies[](#deny-policies "Link to this heading")

Deny policies, available and enabled by default since Cilium 1.9, allows to explicitly restrict certain traffic to and from a Pod.

Deny policies take precedence over allow policies, regardless of whether they are a Cilium Network Policy, a Clusterwide Cilium Network Policy or even a Kubernetes Network Policy.

Similarly to "allow" policies, Pods will enter default-deny mode as soon a single policy selects it.

If multiple allow and deny policies are applied to the same pod, the following table represents the expected enforcement for that Pod:

  ------------------------------------------------------- ----------------------- --------- --------- -------- -------- --------
  **Set of Ingress Policies Deployed to Server Pod**                                                                    
  **Allow Policies**                                      Layer 7 (HTTP)          ✓         ✓         ✓        ✓        
                                                          Layer 4 (80/TCP)        ✓         ✓         ✓        ✓        
                                                          Layer 4 (81/TCP)        ✓         ✓         ✓        ✓        
                                                          Layer 3 (Pod: Client)   ✓         ✓         ✓        ✓        
  **Deny Policies**                                       Layer 4 (80/TCP)                  ✓                  ✓        ✓
                                                          Layer 3 (Pod: Client)                       ✓        ✓        
  **Result for Traffic Connections (Allowed / Denied)**                                                                 
  **Client → Server**                                     curl server:81          Allowed   Allowed   Denied   Denied   Denied
                                                          curl server:80          Allowed   Denied    Denied   Denied   Denied
                                                          ping server             Allowed   Allowed   Denied   Denied   Denied
  ------------------------------------------------------- ----------------------- --------- --------- -------- -------- --------

If we pick the second column in the above table, the bottom section shows the forwarding behaviour for a policy that selects curl or ping traffic between the client and server:

-   Curl to port 81 is allowed because there is an allow policy on port 81, and no deny policy on that port;

-   Curl to port 80 is denied because there is a deny policy on that port;

-   Ping to the server is allowed because there is a Layer 3 allow policy and no deny.

The following policy will deny ingress from "world" on all namespaces on all Pods managed by Cilium. Existing inter-cluster policies will still be allowed as this policy is allowing traffic from everywhere except from "world".

``` {#codecell0}
apiVersion: "cilium.io/v2"
kind: CiliumClusterwideNetworkPolicy
metadata:
  name: "external-lockdown"
spec:
  endpointSelector: {}
  ingressDeny:
  - fromEntities:
    - "world"
  ingress:
  - fromEntities:
    - "all"
```

Copy First Line Copy All

Deny policies do not support: policy enforcement at L7, i.e., specifically denying an URL and `toFQDNs`{.docutils .literal .notranslate}, i.e., specifically denying traffic to a specific domain name.
