---
{"title": "Ingress Path Types Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/path-types/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Ingress Path Types Example[](#ingress-path-types-example "Link to this heading")

This example walks through how various path types interact and allows you to test that Cilium is working as it should.

This example requires that Cilium Ingress is enabled, and `kubectl`{.docutils .literal .notranslate} and `jq`{.docutils .literal .notranslate} must be installed.

## Deploy the example app[](#deploy-the-example-app "Link to this heading")

This deploys five copies of the ingress-conformance-echo tool, that will allow us to see what paths are forwarded to what backends.

``` {#codecell0}
$ # Apply the base definitions
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/main/examples/kubernetes/servicemesh/ingress-path-types.yaml
$ # Apply the Ingress
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/main/examples/kubernetes/servicemesh/ingress-path-types-ingress.yaml
```

Copy First Line Copy Commands Copy All

## Review the Ingress[](#review-the-ingress "Link to this heading")

Here is the Ingress used:

``` {#codecell1}
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multiple-path-types
  namespace: default
spec:
  ingressClassName: cilium
  rules:
  - host: "pathtypes.example.com"
    http:
      paths:
      - backend:
          service:
            name: exactpath
            port:
              number: 80
        path: /exact
        pathType: Exact
      - backend:
          service:
            name: prefixpath
            port:
              number: 80
        path: /
        pathType: Prefix
      - backend:
          service:
            name: prefixpath2
            port:
              number: 80
        path: /prefix
        pathType: Prefix
      - backend:
          service:
            name: implpath
            port:
              number: 80
        path: /impl
        pathType: ImplementationSpecific
      - backend:
          service:
            name: implpath2
            port:
              number: 80
        path: /impl.+
        pathType: ImplementationSpecific
```

Copy First Line Copy All

You can see here that there are five matches, one for each of our deployments.

The Ingress deliberately has the rules in a different order to what they will be configured in Envoy.

-   For Exact matches, we only match `/exact`{.docutils .literal .notranslate} and send that to the `exactpath`{.docutils .literal .notranslate} Service.

-   For Prefix matches, we match `/`{.docutils .literal .notranslate}, send that to the `prefixpath`{.docutils .literal .notranslate} Service, and match `/prefix`{.docutils .literal .notranslate} and send that to the `prefixpath2`{.docutils .literal .notranslate} Service.

-   For ImplementationSpecific matches, we match `/impl.+`{.docutils .literal .notranslate} (a full regex), and send that to the `implpath2`{.docutils .literal .notranslate} Service. We also match `/impl`{.docutils .literal .notranslate} (without regex characters) and send that to the `implpath`{.docutils .literal .notranslate} Service.

The intent here is to allow us to tell which rule we have matched by consulting the echoed response from the ingress-conformance-echo containers.

## Check that the Ingress has provisioned correctly[](#check-that-the-ingress-has-provisioned-correctly "Link to this heading")

Firstly, we need to check that the Ingress has been provisioned correctly.

``` {#codecell2}
$ export PATHTYPE_IP=`k get ing multiple-path-types -o json | jq -r '.status.loadBalancer.ingress[0].ip'`
$ curl -s -H "Host: pathtypes.example.com" http://$PATHTYPE_IP/ | jq
{
"path": "/",
"host": "pathtypes.example.com",
"method": "GET",
"proto": "HTTP/1.1",
"headers": {
    "Accept": [
    "*/*"
    ],
    "User-Agent": [
    "curl/7.81.0"
    ],
    "X-Envoy-External-Address": [
    "your-ip-here"
    ],
    "X-Forwarded-For": [
    "your-ip-here"
    ],
    "X-Forwarded-Proto": [
    "http"
    ],
    "X-Request-Id": [
    "6bb145e8-addb-4fd5-a76f-b53d07bd1867"
    ]
},
"namespace": "default",
"ingress": "",
"service": "",
"pod": "prefixpath-7cb697f5cd-wvv7b"
}
```

Copy First Line Copy Commands Copy All

Here you can see that the Ingress has been provisioned correctly and is responding to requests. Also, you can see that the `/`{.docutils .literal .notranslate} path has been served by the `prefixpath`{.docutils .literal .notranslate} deployment, which is as expected from the Ingress.

## Check that paths perform as expected[](#check-that-paths-perform-as-expected "Link to this heading")

The following example uses `jq`{.docutils .literal .notranslate} to extract the first element out of the `pod`{.docutils .literal .notranslate} field, which is the name of the associated deployment. So, `prefixpath-7cb697f5cd-wvv7b`{.docutils .literal .notranslate} will return `prefixpath`{.docutils .literal .notranslate}.

``` {#codecell3}
$ echo Should show "prefixpath"
Should show prefixpath
$ curl -s -H "Host: pathtypes.example.com" http://$PATHTYPE_IP/ | jq '.pod | split("-")[0]'
"prefixpath"
$ echo Should show "exactpath"
Should show exactpath
$ curl -s -H "Host: pathtypes.example.com" http://$PATHTYPE_IP/exact | jq '.pod | split("-")[0]'
"exactpath"
$ echo Should show "prefixpath2"
Should show prefixpath2
$ curl -s -H "Host: pathtypes.example.com" http://$PATHTYPE_IP/prefix | jq '.pod | split("-")[0]'
"prefixpath2"
$ echo Should show "implpath"
Should show implpath
$ curl -s -H "Host: pathtypes.example.com" http://$PATHTYPE_IP/impl | jq '.pod | split("-")[0]'
"implpath"
$ echo Should show "implpath2"
Should show implpath2
$ curl -s -H "Host: pathtypes.example.com" http://$PATHTYPE_IP/implementation | jq '.pod | split("-")[0]'
"implpath2"
```

Copy First Line Copy Commands Copy All

(You can use the "Copy Commands" button above to do less copy-and-paste.)

The most interesting example here is the last one, where we send `/implementation`{.docutils .literal .notranslate} to the `implpath2`{.docutils .literal .notranslate} Service, while `/impl`{.docutils .literal .notranslate} goes to `implpath`{.docutils .literal .notranslate}. This is because `/implementation`{.docutils .literal .notranslate} matches the `/impl.+`{.docutils .literal .notranslate} regex, and `/impl`{.docutils .literal .notranslate} matches the `/impl`{.docutils .literal .notranslate} regex.

If we now patch the Ingress object to use the regex `/impl.*`{.docutils .literal .notranslate} instead (note the `*`{.docutils .literal .notranslate}, which matches **zero or more** characters of the type instead of the previous `+`{.docutils .literal .notranslate}, which matches **one or more** characters), then we will get a different result for the last two checks:

``` {#codecell4}
$ echo Should show "implpath2"
Should show implpath
$ curl -s -H "Host: pathtypes.example.com" http://$PATHTYPE_IP/impl | jq '.pod | split("-")[0]'
"implpath"
$ echo Should show "implpath2"
Should show implpath2
$ curl -s -H "Host: pathtypes.example.com" http://$PATHTYPE_IP/implementation | jq '.pod | split("-")[0]'
"implpath2"
```

Copy First Line Copy Commands Copy All

The request to `/impl`{.docutils .literal .notranslate} now matches the **longer** pattern `/impl.*`{.docutils .literal .notranslate}.

The moral here is to be careful with your regular expressions!

## Clean up the example[](#clean-up-the-example "Link to this heading")

Finally, we clean up our example:

``` {#codecell5}
$ # Apply the base definitions
$ kubectl delete -f https://raw.githubusercontent.com/cilium/cilium/main/examples/kubernetes/servicemesh/ingress-path-types.yaml
$ # Apply the Ingress
$ kubectl delete -f https://raw.githubusercontent.com/cilium/cilium/main/examples/kubernetes/servicemesh/ingress-path-types-ingress.yaml
```

Copy First Line Copy Commands Copy All
