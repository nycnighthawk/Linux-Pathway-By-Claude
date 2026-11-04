---
{"title": "Inspecting Network Flows with the CLI", "url": "https://docs.cilium.io/en/stable/observability/hubble/hubble-cli/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Inspecting Network Flows with the CLI[](#inspecting-network-flows-with-the-cli "Link to this heading")

This guide walks you through using the Hubble CLI to inspect network flows and gain visibility into what is happening on the network level.

The best way to get help if you get stuck is to ask a question on [Cilium Slack](https://slack.cilium.io). With Cilium contributors across the globe, there is almost always someone available to help.

Note

This guide uses examples based on the Demo App. If you would like to run them, deploy the Demo App first. Please refer to [Identity-Aware and HTTP-Aware Policy Enforcement](../../../security/http/#gs-http) for more details.

## Pre-Requisites[](#pre-requisites "Link to this heading")

-   Cilium has been correctly [installed in your Kubernetes cluster](../../../gettingstarted/k8s-install-default/#k8s-quick-install).

-   [Hubble is enabled](../setup/#hubble-setup).

-   [Hubble CLI is installed](../setup/#hubble-cli-install).

-   [The Hubble API is accessible](../setup/#hubble-validate-api-access).

If unsure, run `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} and validate that Cilium and Hubble are up and running then run `hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`status`{.docutils .literal .notranslate} to verify you can communicate with the Hubble API .

## Inspecting the cluster's network traffic with Hubble Relay[](#inspecting-the-cluster-s-network-traffic-with-hubble-relay "Link to this heading")

Let's issue some requests to emulate some traffic again. This first request is allowed by the policy.

``` {#codecell0}
kubectl exec tiefighter -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
Ship landed
```

Copy First Line Copy All

This next request is accessing an HTTP endpoint which is denied by policy.

``` {#codecell1}
kubectl exec tiefighter -- curl -s -XPUT deathstar.default.svc.cluster.local/v1/exhaust-port
Access denied
```

Copy First Line Copy All

Finally, this last request will hang because the `xwing`{.docutils .literal .notranslate} pod does not have the `org=empire`{.docutils .literal .notranslate} label required by policy. Press Control-C to kill the curl request, or wait for it to time out.

``` {#codecell2}
kubectl exec xwing -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
command terminated with exit code 28
```

Copy First Line Copy All

Let's now inspect this traffic using the CLI. The command below filters all traffic on the application layer (L7, HTTP) to the `deathstar`{.docutils .literal .notranslate} pod:

``` {#codecell3}
hubble observe --pod deathstar --protocol http
May  4 13:23:40.501: default/tiefighter:42690 -> default/deathstar-c74d84667-cx5kp:80 http-request FORWARDED (HTTP/1.1 POST http://deathstar.default.svc.cluster.local/v1/request-landing)
May  4 13:23:40.502: default/tiefighter:42690 <- default/deathstar-c74d84667-cx5kp:80 http-response FORWARDED (HTTP/1.1 200 0ms (POST http://deathstar.default.svc.cluster.local/v1/request-landing))
May  4 13:23:43.791: default/tiefighter:42742 -> default/deathstar-c74d84667-cx5kp:80 http-request DROPPED (HTTP/1.1 PUT http://deathstar.default.svc.cluster.local/v1/exhaust-port)
```

Copy First Line Copy All

The following command shows all traffic to the `deathstar`{.docutils .literal .notranslate} pod that has been dropped:

``` {#codecell4}
hubble observe --pod deathstar --verdict DROPPED
May  4 13:23:43.791: default/tiefighter:42742 -> default/deathstar-c74d84667-cx5kp:80 http-request DROPPED (HTTP/1.1 PUT http://deathstar.default.svc.cluster.local/v1/exhaust-port)
May  4 13:23:47.852: default/xwing:42818 <> default/deathstar-c74d84667-cx5kp:80 Policy denied DROPPED (TCP Flags: SYN)
May  4 13:23:47.852: default/xwing:42818 <> default/deathstar-c74d84667-cx5kp:80 Policy denied DROPPED (TCP Flags: SYN)
May  4 13:23:48.854: default/xwing:42818 <> default/deathstar-c74d84667-cx5kp:80 Policy denied DROPPED (TCP Flags: SYN)
```

Copy First Line Copy All

Feel free to further inspect the traffic. To get help for the `observe`{.docutils .literal .notranslate} command, use `hubble`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`help`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`observe`{.docutils .literal .notranslate}.

## Filtering Encrypted Traffic[](#filtering-encrypted-traffic "Link to this heading")

You can filter flows based on whether they are encrypted (via WireGuard or IPsec) or not.

To see only encrypted flows:

``` {#codecell5}
$ hubble observe --encrypted
```

Copy Line

To see only unencrypted flows:

``` {#codecell6}
$ hubble observe --unencrypted
```

Copy Line

## Filtering Reply Traffic[](#filtering-reply-traffic "Link to this heading")

You can filter flows based on whether they are reply packets (server-to-client direction) or not.

To see only reply flows:

``` {#codecell7}
$ hubble observe --reply
```

Copy Line

To see only non-reply flows:

``` {#codecell8}
$ hubble observe --not-reply
```

Copy Line

## Next Steps[](#next-steps "Link to this heading")

-   [Access the Hubble API with TLS Enabled](../configuration/tls/#hubble-api-tls)
