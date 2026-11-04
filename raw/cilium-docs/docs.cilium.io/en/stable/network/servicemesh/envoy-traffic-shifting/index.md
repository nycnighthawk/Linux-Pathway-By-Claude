---
{"title": "L7 Traffic Shifting", "url": "https://docs.cilium.io/en/stable/network/servicemesh/envoy-traffic-shifting/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# L7 Traffic Shifting[](#l7-traffic-shifting "Link to this heading")

Cilium Service Mesh defines a `CiliumEnvoyConfig`{.docutils .literal .notranslate} CRD which allows users to set the configuration of the Envoy component built into Cilium agents.

This example sets up an Envoy listener which load balances requests to the helloworld Service by sending 90% of incoming requests to the backend `helloworld-v1`{.docutils .literal .notranslate} and 10% of incoming requests to the backend `helloworld-v2`{.docutils .literal .notranslate}.

## Deploy Test Applications[](#deploy-test-applications "Link to this heading")

``` {#codecell0 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/client-helloworld.yaml
```

Copy Line

The test workloads consist of:

-   One client Deployment, `client`{.docutils .literal .notranslate}

-   Two server Deployments, `helloworld-v1`{.docutils .literal .notranslate} and `helloworld-v2`{.docutils .literal .notranslate}

View information about these Pods and the helloworld Service:

``` {#codecell1}
$ kubectl get pods --show-labels -o wide
NAME                             READY   STATUS    RESTARTS   AGE     IP           NODE                   NOMINATED NODE   READINESS GATES   LABELS
client-64848f85dd-sjfmb          1/1     Running   0          2m23s   10.0.0.206   cilium-control-plane   <none>           <none>            kind=client,name=client,pod-template-hash=64848f85dd
helloworld-v1-5845f97d6b-gkdtk   1/1     Running   0          2m23s   10.0.0.241   cilium-control-plane   <none>           <none>            app=helloworld,pod-template-hash=5845f97d6b,version=v1
helloworld-v2-7d55d87964-ns9kh   1/1     Running   0          2m23s   10.0.0.251   cilium-control-plane   <none>           <none>            app=helloworld,pod-template-hash=7d55d87964,version=v2

$ kubectl get svc --show-labels
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE   LABELS
helloworld   ClusterIP   10.96.194.77   <none>        5000/TCP   8m27s app=helloworld,service=helloworld
```

Copy First Line Copy Commands Copy All

## Apply weight-based routing[](#apply-weight-based-routing "Link to this heading")

Make an environment variable with the Pod name for client:

``` {#codecell2}
$ export CLIENT=$(kubectl get pods -l name=client -o jsonpath='{.items[0].metadata.name}')
```

Copy Line

Try making several requests to the helloworld Service.

``` {#codecell3}
$ for i in {1..10}; do  kubectl exec -it $CLIENT -- curl  helloworld:5000/hello; done
```

Copy Line

The test results are as follows:

``` {#codecell4}
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
```

Copy First Line Copy All

The test results were as expected. Of the requests sent to the helloworld service, 50% of them were sent to the backend `helloworld-v1`{.docutils .literal .notranslate} and 50% of them were sent to the backend `helloworld-v2`{.docutils .literal .notranslate}.

`CiliumEnvoyConfig`{.docutils .literal .notranslate} can be used to load balance traffic destined to one Service to a group of backend Services. To load balance traffic to the helloworld Service, first create individual Services for each backend Deployment.

``` {#codecell5 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/helloworld-service-v1-v2.yaml
```

Copy Line

Apply the `envoy-helloworld-v1-90-v2-10.yaml`{.docutils .literal .notranslate} file, which defines a `CiliumEnvoyConfig`{.docutils .literal .notranslate} to send 90% of traffic to the helloworld-v1 Service backend and 10% of traffic to the helloworld-v2 Service backend:

``` {#codecell6 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/envoy-helloworld-v1-90-v2-10.yaml
```

Copy Line

View information about these Pods and Services:

``` {#codecell7}
$ kubectl get pods --show-labels -o wide
NAME                             READY   STATUS    RESTARTS   AGE     IP           NODE                   NOMINATED NODE   READINESS GATES   LABELS
client-64848f85dd-sjfmb          1/1     Running   0          2m23s   10.0.0.206   cilium-control-plane   <none>           <none>            kind=client,name=client,pod-template-hash=64848f85dd
helloworld-v1-5845f97d6b-gkdtk   1/1     Running   0          2m23s   10.0.0.241   cilium-control-plane   <none>           <none>            app=helloworld,pod-template-hash=5845f97d6b,version=v1
helloworld-v2-7d55d87964-ns9kh   1/1     Running   0          2m23s   10.0.0.251   cilium-control-plane   <none>           <none>            app=helloworld,pod-template-hash=7d55d87964,version=v2

$ kubectl get svc --show-labels
NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE   LABELS
helloworld      ClusterIP   10.96.194.77   <none>        5000/TCP   16m   app=helloworld,service=helloworld
helloworld-v1   ClusterIP   10.96.0.240    <none>        5000/TCP   4s    app=helloworld,service=helloworld,version=v1
helloworld-v2   ClusterIP   10.96.41.142   <none>        5000/TCP   4s    app=helloworld,service=helloworld,version=v2
```

Copy First Line Copy Commands Copy All

Note

Note that these Envoy resources are not validated by K8s at all, so any errors in the Envoy resources will only be seen by the Cilium Agent observing these CRDs. This means that `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`apply`{.docutils .literal .notranslate} will report success, while parsing and/or installing the resources for the node-local Envoy instance may have failed. Currently the only way of verifying this is by observing Cilium Agent logs for errors and warnings. Additionally, Cilium Agent will print warning logs for any conflicting Envoy resources in the cluster.

Note

Note that Cilium Ingress Controller will configure required Envoy resource under the hood. Please check Cilium Agent logs if you are creating Envoy resources explicitly to make sure there is no conflict.

Try making several requests to the helloworld Service again.

``` {#codecell8}
$ for i in {1..10}; do  kubectl exec -it $CLIENT -- curl  helloworld:5000/hello; done
```

Copy Line

The test results are as follows:

``` {#codecell9}
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
```

Copy First Line Copy All

The test results were as expected. Of the requests sent to the helloworld service, 90% of them were sent to the backend `helloworld-v1`{.docutils .literal .notranslate} and 10% of them were sent to the backend `helloworld-v2`{.docutils .literal .notranslate}.

## Cleaning up[](#cleaning-up "Link to this heading")

Remove the rules.

``` {#codecell10 .literal-block}
$ kubectl delete -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/envoy-helloworld-v1-90-v2-10.yaml
```

Copy Line

Remove the test application.

``` {#codecell11 .literal-block}
$ kubectl delete -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/client-helloworld.yaml
$ kubectl delete -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/helloworld-service-v1-v2.yaml
```

Copy First Line Copy All
