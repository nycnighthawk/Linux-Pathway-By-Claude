---
{"title": "NGINX Ingress Annotations to Gateway API Migration", "url": "https://docs.cilium.io/en/stable/network/servicemesh/ingress-to-gateway/nginx-annotations-migration/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# NGINX Ingress Annotations to Gateway API Migration[](#nginx-ingress-annotations-to-gateway-api-migration "Link to this heading")

This page provides a practical migration guide for NGINX Ingress annotations when moving to Gateway API in Cilium environments.

This guide focuses on common annotation patterns and their closest Gateway API equivalents or alternatives.

## Migration Triage Model[](#migration-triage-model "Link to this heading")

Use this order when migrating annotations:

1.  **Direct mapping**: replace the annotation with native Gateway API fields and filters.

2.  **Extension-dependent**: migrate only if your environment supports the required experimental or implementation-specific extension.

3.  **No equivalent / not planned**: redesign behavior (policy, app, or platform setting) instead of searching for a 1:1 translation.

Note

When a mapping references a GEP or experimental API, verify feature support in both your installed Gateway API version and Cilium release. Entries marked **Not yet supported** have no Cilium implementation today and may be added in future releases.

## Inventory Existing NGINX Annotations[](#inventory-existing-nginx-annotations "Link to this heading")

Extract currently used annotations before conversion:

``` {#codecell0}
kubectl get ingress -A -o json \
  | jq -r '.items[]
  | [.metadata.namespace, .metadata.name,
     ((.metadata.annotations // {}) | to_entries[]
      | select(.key | startswith("nginx.ingress.kubernetes.io/"))
      | "\(.key)=\(.value)")] | @tsv'
```

Copy First Line Copy All

Prioritize by frequency and production criticality (auth, redirect, timeout, TLS, and source restriction annotations first).

## Common Direct Mappings[](#common-direct-mappings "Link to this heading")

  NGINX annotation                                                 Gateway API equivalent                                                                                                                                 External reference                                                                                 Cilium support                                                                 Notes
  ---------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `canary-weight`{.docutils .literal .notranslate}                 `HTTPRoute.rules.backendRefs[].weight`{.docutils .literal .notranslate}                                                                                [Traffic Splitting Guide](https://gateway-api.sigs.k8s.io/guides/traffic-splitting/)               Yes                                                                            Weighted traffic splitting.
  `canary-by-header`{.docutils .literal .notranslate}              `HTTPRoute.rules.matches.headers`{.docutils .literal .notranslate}                                                                                     [Traffic Splitting Guide](https://gateway-api.sigs.k8s.io/guides/traffic-splitting/)               Yes                                                                            Combine with weighted `backendRefs`{.docutils .literal .notranslate} for canary.
  `use-regex`{.docutils .literal .notranslate}                     `HTTPRouteMatch.path.type:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`RegularExpression`{.docutils .literal .notranslate}   [HTTP Routing Guide](https://gateway-api.sigs.k8s.io/guides/http-routing/)                         Yes                                                                            Supported in Cilium, but regex matching remains implementation-specific in Gateway API.
  `rewrite-target`{.docutils .literal .notranslate}                `HTTPRoute.filters.type:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`URLRewrite`{.docutils .literal .notranslate}            [Redirects and Rewrites Guide](https://gateway-api.sigs.k8s.io/guides/http-redirect-rewrite/)      Yes                                                                            Use per-rule rewrite filters.
  `force-ssl-redirect`{.docutils .literal .notranslate}            `HTTPRoute.filters.type:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`RequestRedirect`{.docutils .literal .notranslate}       [Redirects and Rewrites Guide](https://gateway-api.sigs.k8s.io/guides/http-redirect-rewrite/)      Yes                                                                            Redirect HTTP to HTTPS at route level.
  `permanent-redirect`{.docutils .literal .notranslate}            `HTTPRoute.filters.type:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`RequestRedirect`{.docutils .literal .notranslate}       [Redirects and Rewrites Guide](https://gateway-api.sigs.k8s.io/guides/http-redirect-rewrite/)      Yes                                                                            Set permanent redirect behavior.
  `proxy-read-timeout`{.docutils .literal .notranslate}            `HTTPRoute.rules.timeouts.backendRequest`{.docutils .literal .notranslate}                                                                             [HTTP Timeouts Guide](https://gateway-api.sigs.k8s.io/guides/http-timeouts/)                       Yes                                                                            Closest match for upstream response timing; compare carefully with end-to-end `request`{.docutils .literal .notranslate} timeout semantics.
  `proxy-next-upstream-tries`{.docutils .literal .notranslate}     `HTTPRoute.rules.retry.attempts`{.docutils .literal .notranslate}                                                                                      [GEP-1731](https://gateway-api.sigs.k8s.io/geps/gep-1731/)                                         Yes                                                                            Experimental in Gateway API (GEP-1731). Maps retry count only, not the full `proxy-next-upstream*`{.docutils .literal .notranslate} behavior set.
  `kubernetes.io/ingress.class`{.docutils .literal .notranslate}   `Gateway.spec.gatewayClassName`{.docutils .literal .notranslate}                                                                                       [Gateway API Overview](https://gateway-api.sigs.k8s.io/docs/concepts/api-overview/)                Yes                                                                            Replace controller selection model. Note: uses the `kubernetes.io/`{.docutils .literal .notranslate} prefix, not `nginx.ingress.kubernetes.io/`{.docutils .literal .notranslate}; won't appear in the NGINX-scoped inventory above.
  `server-alias`{.docutils .literal .notranslate}                  `HTTPRoute.spec.hostnames`{.docutils .literal .notranslate}                                                                                            [Gateway API Overview](https://gateway-api.sigs.k8s.io/docs/concepts/api-overview/)                Yes                                                                            Migrate alternate hostnames explicitly.
  `backend-protocol`{.docutils .literal .notranslate}              `Service.spec.ports[].appProtocol`{.docutils .literal .notranslate}                                                                                    [GEP-1911](https://gateway-api.sigs.k8s.io/geps/gep-1911/)                                         Yes (enable `gatewayAPI.enableAppProtocol`{.docutils .literal .notranslate})   For backend protocol hints.
  `enable-cors`{.docutils .literal .notranslate}                   `HTTPRoute.filters.type:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`CORS`{.docutils .literal .notranslate}                  [GEP-1767](https://gateway-api.sigs.k8s.io/geps/gep-1767/)                                         Not yet supported                                                              Experimental in Gateway API (GEP-1767).
  `proxy-ssl-secret`{.docutils .literal .notranslate}              `BackendTLSPolicy.spec.validation.caCertificateRefs`{.docutils .literal .notranslate}                                                                  [BackendTLSPolicy](https://gateway-api.sigs.k8s.io/reference/api-types/policy/backendtlspolicy/)   Yes                                                                            Backend TLS trust material.
  `proxy-ssl-verify`{.docutils .literal .notranslate}              `BackendTLSPolicy.spec.validation`{.docutils .literal .notranslate}                                                                                    [BackendTLSPolicy](https://gateway-api.sigs.k8s.io/reference/api-types/policy/backendtlspolicy/)   Yes                                                                            CA and validation behavior.
  `secure-backends`{.docutils .literal .notranslate}               `BackendTLSPolicy`{.docutils .literal .notranslate}                                                                                                    [BackendTLSPolicy](https://gateway-api.sigs.k8s.io/reference/api-types/policy/backendtlspolicy/)   Yes                                                                            Use policy attachment for backend TLS.

## Complex Mappings and Extension-Dependent Cases[](#complex-mappings-and-extension-dependent-cases "Link to this heading")

The following annotations do not have a direct Gateway API equivalent today. Migration depends on implementation-specific extensions or the graduation of upstream GEPs into the Gateway API standard. Unless noted otherwise, **Cilium does not yet support these mappings**.

+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| NGINX annotation                                                                                                                                       | Suggested approach                                                                    | External reference                                                                                                     | Cilium support    | Complexity  |
+========================================================================================================================================================+=======================================================================================+========================================================================================================================+===================+=============+
| `upstream-hash-by`{.docutils .literal .notranslate}                                                                                                    | Implementation-specific traffic policy extension                                      | -                                                                                                                      | Not yet supported | High        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| `keep-alive`{.docutils .literal .notranslate}, `keepalive-*`{.docutils .literal .notranslate}, `upstream-keepalive-*`{.docutils .literal .notranslate} | Implementation-specific data-plane tuning policy                                      | -                                                                                                                      | Not yet supported | High        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| `auth-type`{.docutils .literal .notranslate}, `auth-url`{.docutils .literal .notranslate}                                                              | `ExternalAuth`{.docutils .literal .notranslate}-style HTTPRoute filter (experimental) | [GEP-1494](https://gateway-api.sigs.k8s.io/geps/gep-1494/)                                                             | Not yet supported | High        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| `auth-tls-secret`{.docutils .literal .notranslate}, `auth-tls-verify-client`{.docutils .literal .notranslate}                                          | Frontend/client certificate validation extension                                      | [GEP-91](https://gateway-api.sigs.k8s.io/geps/gep-91/)                                                                 | Not yet supported | High        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| other `proxy-next-upstream*`{.docutils .literal .notranslate} annotations                                                                              | Retry and timeout fields (partly experimental)                                        | [GEP-1731](https://gateway-api.sigs.k8s.io/geps/gep-1731/), [GEP-1742](https://gateway-api.sigs.k8s.io/geps/gep-1742/) | Not yet supported | High        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| `tcp-services-configmap`{.docutils .literal .notranslate}                                                                                              | `TCPRoute`{.docutils .literal .notranslate} resources (experimental channel)          | [TCPRoute](https://gateway-api.sigs.k8s.io/reference/api-spec/main/spec/#tcproute)                                     | Not yet supported | High        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| `use-forwarded-headers`{.docutils .literal .notranslate}                                                                                               | Implementation-specific client traffic policy                                         | -                                                                                                                      | Not yet supported | High        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| `whitelist-source-range`{.docutils .literal .notranslate}                                                                                              | Cilium network policy and/or implementation-specific route security filters           | -                                                                                                                      | Not yet supported | High        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+

## No Equivalent or Not Planned[](#no-equivalent-or-not-planned "Link to this heading")

These are common examples that do not have a 1:1 Gateway API migration target:

-   `configuration-snippet`{.docutils .literal .notranslate}, `server-snippet`{.docutils .literal .notranslate}, `server-snippets`{.docutils .literal .notranslate} (`won't`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`add`{.docutils .literal .notranslate})

-   `sendfile`{.docutils .literal .notranslate} (`won't`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`add`{.docutils .literal .notranslate})

-   `proxy-store`{.docutils .literal .notranslate} (no direct equivalent)

-   `proxy-buffering`{.docutils .literal .notranslate} and related proxy buffer tuning annotations

-   `worker-processes`{.docutils .literal .notranslate} (`N/A`{.docutils .literal .notranslate})

For these cases, prefer one of:

1.  Move behavior to application/runtime configuration.

2.  Move behavior to dedicated platform policy objects (if available).

3.  Drop legacy tuning that is no longer relevant with Gateway API + Envoy.

## Validation[](#validation "Link to this heading")

For every migrated annotation, validate:

-   Route/Gateway condition status (Accepted, Programmed, ResolvedRefs).

-   End-to-end behavior parity (redirects, headers, auth, retries, TLS).

-   SLO impact during rollout (error rate, latency, retry amplification).

## Related Content[](#related-content "Link to this heading")

-   [Migrating from Ingress to Gateway](../ingress-to-gateway/#gs-ingress-to-gateway)

-   [HTTP Migration Example](../http-migration/#gs-gateway-http-migration)

-   [TLS Migration](../tls-migration/#gs-gateway-tls-migration)

-   [Gateway API Support](../../gateway-api/gateway-api/#gs-gateway-api)
