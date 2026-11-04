---
{"title": "Traffic Splitting Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/splitting/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Traffic Splitting Example[](#traffic-splitting-example "Link to this heading")

HTTP traffic splitting is the process of sending incoming traffic to multiple backend services, based on predefined weights or other criteria. The Cilium Gateway API includes built-in support for traffic splitting, allowing users to easily distribute incoming traffic across multiple backend services. This is very useful for canary testing or A/B scenarios.

This particular example uses the Gateway API to load balance incoming traffic to different backends, starting with the same weights before testing with a 99/1 weight distribution.

## Deploy the Echo App[](#deploy-the-echo-app "Link to this heading")

We will use a deployment made of echo servers.

The application will reply to the client and, in the body of the reply, will include information about the Pod receiving the original request. We will use this information to illustrate how the traffic is manipulated by the Gateway.

``` {#codecell0 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/echo-basic.yaml
```

Copy Line

Verify the Pods are running as expected.

``` {#codecell1}
$ kubectl get pods
NAME                      READY   STATUS    RESTARTS   AGE
echo-1-7d88f779b-m6r46    1/1     Running   0          21s
echo-2-5bfb6668b4-n7llh   1/1     Running   0          21s
```

Copy First Line Copy Commands Copy All

## Deploy the Cilium Gateway[](#deploy-the-cilium-gateway "Link to this heading")

You can find an example Gateway and HTTPRoute definition in `splitting.yaml`{.docutils .literal .notranslate}:

``` {#codecell2}
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: cilium-gw
spec:
  gatewayClassName: cilium
  listeners:
  - protocol: HTTP
    port: 80
    name: web-gw-echo
    allowedRoutes:
      namespaces:
        from: Same
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: example-route-1
spec:
  parentRefs:
  - name: cilium-gw
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /echo
    backendRefs:
    - kind: Service
      name: echo-1
      port: 8080
      weight: 50
    - kind: Service
      name: echo-2
      port: 8090
      weight: 50
```

Copy First Line Copy All

Notice the even 50/50 split between the two Services.

Deploy the Gateway and the HTTPRoute:

``` {#codecell3 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/splitting.yaml
```

Copy Line

The preceding example creates a Gateway named `cilium-gw`{.docutils .literal .notranslate} that listens on port 80. A single route is defined and includes two different `backendRefs`{.docutils .literal .notranslate} (`echo-1`{.docutils .literal .notranslate} and `echo-2`{.docutils .literal .notranslate}) and weights associated with them.

``` {#codecell4}
$ kubectl get gateway cilium-gw
NAME        CLASS    ADDRESS          PROGRAMMED   AGE
cilium-gw   cilium   172.18.255.200                8s
```

Copy First Line Copy Commands Copy All

Note

Some providers like EKS use a fully-qualified domain name rather than an IP address.

## Even traffic split[](#even-traffic-split "Link to this heading")

Now that the Gateway is ready, you can make HTTP requests to the services.

``` {#codecell5}
$ GATEWAY=$(kubectl get gateway cilium-gw -o jsonpath='{.status.addresses[0].value}')
$ curl --fail -s http://$GATEWAY/echo
{
 "path": "/echo",
 "host": "172.18.255.200",
 "method": "GET",
 "proto": "HTTP/1.1",
 "headers": {
  "Accept": [
   "*/*"
  ],
  "User-Agent": [
   "curl/7.81.0"
  ],
  "X-Envoy-Internal": [
   "true"
  ],
  "X-Forwarded-For": [
   "172.18.0.1"
  ],
  "X-Forwarded-Proto": [
   "http"
  ],
  "X-Request-Id": [
   "ee152a07-2be2-4539-b74d-ebcebf912907"
  ]
 },
 "httpPort": "3000",
 "namespace": "default",
 "ingress": "",
 "service": "",
 "pod": "echo-1-7d88f779b-m6r46"
}
```

Copy First Line Copy Commands Copy All

Notice that the reply includes the name of the Pod that received the query in the `pod`{.docutils .literal .notranslate} field. For example:

``` {#codecell6}
"pod": "echo-2-5bfb6668b4-2rl4t"
```

Copy Line

Repeat the command several times. You should see the reply balanced evenly across both Pods and Nodes. Verify that traffic is evenly split across multiple Pods by running a loop and counting the requests:

``` {#codecell7}
$ while true; do curl -s -k "http://$GATEWAY/echo" >> curlresponses.txt ;done
```

Copy Line

Stop the loop with `Ctrl+C`{.docutils .literal .notranslate}. Verify that the responses are more or less evenly distributed.

``` {#codecell8}
$ cat curlresponses.txt| grep -c '"pod": "echo-1'
1221
$ cat curlresponses.txt| grep -c '"pod": "echo-2'
1162
```

Copy First Line Copy Commands Copy All

## Uneven (99/1) traffic split[](#uneven-99-1-traffic-split "Link to this heading")

Update the HTTPRoute weights, either by using `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`edit`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`httproute`{.docutils .literal .notranslate} or by updating the value in the original manifest before reapplying it to. For example, set `99`{.docutils .literal .notranslate} for echo-1 and `1`{.docutils .literal .notranslate} for echo-2:

``` {#codecell9}
backendRefs:
- kind: Service
  name: echo-1
  port: 8080
  weight: 99
- kind: Service
  name: echo-2
  port: 8090
  weight: 1
```

Copy First Line Copy All

Verify that traffic is unevenly split across multiple Pods by running a loop and counting the requests:

``` {#codecell10}
$ while true; do curl -s -k "http://$GATEWAY/echo" >> curlresponses991.txt ;done
```

Copy Line

Stop the loop with `Ctrl+C`{.docutils .literal .notranslate}. Verify that responses are more or less evenly distributed.

``` {#codecell11}
$ cat curlresponses991.txt| grep -c '"pod": "echo-1'
24739
$ cat curlresponses991.txt| grep -c '"pod": "echo-2'
239
```

Copy First Line Copy Commands Copy All
