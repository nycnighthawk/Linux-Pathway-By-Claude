---
{"title": "Troubleshooting", "url": "https://docs.cilium.io/en/stable/security/policy/troubleshooting/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Troubleshooting[](#troubleshooting "Link to this heading")

## Policy Rule to Endpoint Mapping[](#policy-rule-to-endpoint-mapping "Link to this heading")

To determine which policy rules are currently in effect for an endpoint the data from `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate} and `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate} can be paired with the data from `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`policy`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}. `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate} will list the labels of each rule that applies to an endpoint. The list of labels can be passed to `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`policy`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate} to show that exact source policy. Note that rules that have no labels cannot be fetched alone (a no label `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`policy`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate} returns the complete policy on the node). Rules with the same labels will be returned together.

In the above example, for one of the `deathstar`{.docutils .literal .notranslate} pods the endpoint id is 568. We can print all policies applied to it with:

``` {#codecell0}
$ # Get a shell on the Cilium pod

$ kubectl exec -ti cilium-88k78 -n kube-system -- /bin/bash

$ # print out the ingress labels
$ # clean up the data
$ # fetch each policy via each set of labels
$ # (Note that while the structure is "...l4.ingress...", it reflects all L3, L4 and L7 policy.

$ cilium-dbg endpoint get 568 -o jsonpath='{range ..status.policy.realized.l4.ingress[*].derived-from-rules}{@}{"\n"}{end}'|tr -d '][' | xargs -I{} bash -c 'echo "Labels: {}"; cilium-dbg policy get {}'
Labels: k8s:io.cilium.k8s.policy.name=rule1 k8s:io.cilium.k8s.policy.namespace=default
[
  {
    "endpointSelector": {
      "matchLabels": {
        "any:class": "deathstar",
        "any:org": "empire",
        "k8s:io.kubernetes.pod.namespace": "default"
      }
    },
    "ingress": [
      {
        "fromEndpoints": [
          {
            "matchLabels": {
              "any:org": "empire",
              "k8s:io.kubernetes.pod.namespace": "default"
            }
          }
        ],
        "toPorts": [
          {
            "ports": [
              {
                "port": "80",
                "protocol": "TCP"
              }
            ],
            "rules": {
              "http": [
                {
                  "path": "/v1/request-landing",
                  "method": "POST"
                }
              ]
            }
          }
        ]
      }
    ],
    "labels": [
      {
        "key": "io.cilium.k8s.policy.name",
        "value": "rule1",
        "source": "k8s"
      },
      {
        "key": "io.cilium.k8s.policy.namespace",
        "value": "default",
        "source": "k8s"
      }
    ]
  }
]
Revision: 217

$ # repeat for egress
$ cilium-dbg endpoint get 568 -o jsonpath='{range ..status.policy.realized.l4.egress[*].derived-from-rules}{@}{"\n"}{end}' | tr -d '][' | xargs -I{} bash -c 'echo "Labels: {}"; cilium-dbg policy get {}'
```

Copy First Line Copy Commands Copy All

## Troubleshooting `toFQDNs`{.docutils .literal .notranslate} rules[](#troubleshooting-tofqdns-rules "Link to this heading")

`toFQDNs`{.docutils .literal .notranslate} rules do nothing if there is no [L7 DNS rule](../layer7/#dns-obtaining-data) covering the endpoint.

The effect of `toFQDNs`{.docutils .literal .notranslate} may change long after a policy is applied, as DNS data changes. This can make it difficult to debug unexpectedly blocked connections, or transient failures. Cilium provides CLI tools to introspect the state of applying FQDN policy in multiple layers of the daemon:

1.  `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`policy`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate} should show the FQDN policy that was imported:

    ``` {#codecell1}
    {
      "endpointSelector": {
        "matchLabels": {
          "any:class": "mediabot",
          "any:org": "empire",
          "k8s:io.kubernetes.pod.namespace": "default"
        }
      },
      "egress": [
        {
          "toFQDNs": [
            {
              "matchName": "api.github.com"
            }
          ]
        },
        {
          "toEndpoints": [
            {
              "matchLabels": {
                "k8s:io.kubernetes.pod.namespace": "kube-system",
                "k8s:k8s-app": "kube-dns"
              }
            }
          ],
          "toPorts": [
            {
              "ports": [
                {
                  "port": "53",
                  "protocol": "ANY"
                }
              ],
              "rules": {
                "dns": [
                  {
                    "matchPattern": "*"
                  }
                ]
              }
            }
          ]
        }
      ],
      "labels": [
        {
          "key": "io.cilium.k8s.policy.derived-from",
          "value": "CiliumNetworkPolicy",
          "source": "k8s"
        },
        {
          "key": "io.cilium.k8s.policy.name",
          "value": "fqdn",
          "source": "k8s"
        },
        {
          "key": "io.cilium.k8s.policy.namespace",
          "value": "default",
          "source": "k8s"
        },
        {
          "key": "io.cilium.k8s.policy.uid",
          "value": "f213c6b2-c87b-449c-a66c-e19a288062ba",
          "source": "k8s"
        }
      ]
    }
    ```

    Copy First Line Copy All

2.  After making a DNS request, the FQDN to IP mapping should be available via `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`fqdn`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`cache`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate}:

    ``` {#codecell2}
    # cilium-dbg fqdn cache list
    Endpoint   Source   FQDN                  TTL    ExpirationTime             IPs
    725        lookup   api.github.com.       3600   2023-02-10T18:16:05.842Z   140.82.121.6
    725        lookup   support.github.com.   3600   2023-02-10T18:16:09.371Z   185.199.111.133,185.199.109.133,185.199.110.133,185.199.108.133
    ```

    Copy First Line Copy Commands Copy All

3.  If the traffic is allowed, then these IPs should have corresponding local identities via `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`ip`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`list`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`|`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`grep`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`<IP>`{.docutils .literal .notranslate}:

    ``` {#codecell3}
    # cilium-dbg ip list | grep -A 1 140.82.121.6
    140.82.121.6/32                 fqdn:api.github.com
                                    reserved:world
    ```

    Copy First Line Copy Commands Copy All

### Monitoring `toFQDNs`{.docutils .literal .notranslate} identity usage[](#monitoring-tofqdns-identity-usage "Link to this heading")

When using `toFQDNs`{.docutils .literal .notranslate} selectors, every IP observed by a matching DNS lookup will be labeled with that selector. As a DNS name might be matched by multiple selectors, and because an IP might map to multiple names, an IP might be labeled by multiple selectors. As with regular cluster identities, every unique combination of labels will allocate its own numeric security identity. This can lead to many different identities being allocated, as described in [Limiting Identity-Relevant Labels](../../../operations/performance/scalability/identity-relevant-labels/#identity-relevant-labels).

To detect potential identity exhaustion for `toFQDNs`{.docutils .literal .notranslate} identities, the number allocated FQDN identities can be monitored using the `identity_label_sources{type="fqdn"}`{.docutils .literal .notranslate} metric. As a comparative reference the `fqdn_selectors`{.docutils .literal .notranslate} metric monitors the number of registered `toFQDNs`{.docutils .literal .notranslate} selectors. For more details on metrics, please refer to [Monitoring & Metrics](../../../observability/metrics/#metrics).
