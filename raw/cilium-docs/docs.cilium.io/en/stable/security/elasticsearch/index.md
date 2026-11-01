---
{"title": "Securing Elasticsearch", "url": "https://docs.cilium.io/en/stable/security/elasticsearch/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Securing Elasticsearch[](#securing-elasticsearch "Link to this heading")

This document serves as an introduction for using Cilium to enforce Elasticsearch-aware security policies. It is a detailed walk-through of getting a single-node Cilium environment running on your machine. It is designed to take 15-30 minutes.

If you haven't read the [Introduction to Cilium & Hubble](../../overview/intro/#intro) yet, we'd encourage you to do that first.

The best way to get help if you get stuck is to ask a question on [Cilium Slack](https://slack.cilium.io). With Cilium contributors across the globe, there is almost always someone available to help.

## Setup Cilium[](#setup-cilium "Link to this heading")

If you have not set up Cilium yet, follow the guide [Cilium Quick Installation](../../gettingstarted/k8s-install-default/#k8s-install-standard) for instructions on how to quickly bootstrap a Kubernetes cluster and install Cilium. If in doubt, pick the minikube route, you will be good to go in less than 5 minutes.

## Deploy the Demo Application[](#deploy-the-demo-application "Link to this heading")

Following the Cilium tradition, we will use a Star Wars-inspired example. The Empire has a large scale Elasticsearch cluster which is used for storing a variety of data including:

-   `index:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`troop_logs`{.docutils .literal .notranslate}: Stormtroopers performance logs collected from every outpost which are used to identify and eliminate weak performers!

-   `index:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`spaceship_diagnostics`{.docutils .literal .notranslate}: Spaceships diagnostics data collected from every spaceship which is used for R&D and improvement of the spaceships.

Every outpost has an Elasticsearch client service to upload the Stormtroopers logs. And every spaceship has a service to upload diagnostics. Similarly, the Empire headquarters has a service to search and analyze the troop logs and spaceship diagnostics data. Before we look into the security concerns, let's first create this application scenario in minikube.

Deploy the app using command below, which will create

-   An `elasticsearch`{.docutils .literal .notranslate} service with the selector label `component:elasticsearch`{.docutils .literal .notranslate} and a pod running Elasticsearch.

-   Three Elasticsearch clients one each for `empire-hq`{.docutils .literal .notranslate}, `outpost`{.docutils .literal .notranslate} and `spaceship`{.docutils .literal .notranslate}.

``` {#codecell0 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-es/es-sw-app.yaml
serviceaccount "elasticsearch" created
service "elasticsearch" created
replicationcontroller "es" created
role "elasticsearch" created
rolebinding "elasticsearch" created
pod "outpost" created
pod "empire-hq" created
pod "spaceship" created
```

Copy First Line Copy All

``` {#codecell1}
$ kubectl get svc,pods
NAME                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                           AGE
svc/elasticsearch   NodePort    10.111.238.254   <none>        9200:30130/TCP,9300:31721/TCP     2d
svc/etcd-cilium     NodePort    10.98.67.60      <none>        32379:31079/TCP,32380:31080/TCP   9d
svc/kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP                           9d

NAME               READY     STATUS    RESTARTS   AGE
po/empire-hq       1/1       Running   0          2d
po/es-g9qk2        1/1       Running   0          2d
po/etcd-cilium-0   1/1       Running   0          9d
po/outpost         1/1       Running   0          2d
po/spaceship       1/1       Running   0          2d
```

Copy First Line Copy Commands Copy All

## Security Risks for Elasticsearch Access[](#security-risks-for-elasticsearch-access "Link to this heading")

For Elasticsearch clusters the **least privilege security** challenge is to give clients access only to particular indices, and to limit the operations each client is allowed to perform on each index. In this example, the `outpost`{.docutils .literal .notranslate} Elasticsearch clients only need access to upload troop logs; and the `empire-hq`{.docutils .literal .notranslate} client only needs search access to both the indices. From the security perspective, the outposts are weak spots and susceptible to be captured by the rebels. Once compromised, the clients can be used to search and manipulate the critical data in Elasticsearch. We can simulate this attack, but first let's run the commands for legitimate behavior for all the client services.

`outpost`{.docutils .literal .notranslate} client uploading troop logs

``` {#codecell2}
$ kubectl exec outpost -- python upload_logs.py
Uploading Stormtroopers Performance Logs
created :  {'_index': 'troop_logs', '_type': 'log', '_id': '1', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, 'created': True}
```

Copy First Line Copy Commands Copy All

`spaceship`{.docutils .literal .notranslate} uploading diagnostics

``` {#codecell3}
$ kubectl exec spaceship -- python upload_diagnostics.py
Uploading Spaceship Diagnostics
created :  {'_index': 'spaceship_diagnostics', '_type': 'stats', '_id': '1', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, 'created': True}
```

Copy First Line Copy Commands Copy All

`empire-hq`{.docutils .literal .notranslate} running search queries for logs and diagnostics

``` {#codecell4}
$ kubectl exec empire-hq -- python search.py
Searching for Spaceship Diagnostics
Got 1 Hits:
{'_index': 'spaceship_diagnostics', '_type': 'stats', '_id': '1', '_score': 1.0, \
 '_source': {'spaceshipid': '3459B78XNZTF', 'type': 'tiefighter', 'title': 'Engine Diagnostics', \
             'stats': '[CRITICAL] [ENGINE BURN @SPEED 5000 km/s] [CHANCE 80%]'}}
Searching for Stormtroopers Performance Logs
Got 1 Hits:
{'_index': 'troop_logs', '_type': 'log', '_id': '1', '_score': 1.0, \
 '_source': {'outpost': 'Endor', 'datetime': '33 ABY 4AM DST', 'title': 'Endor Corps 1: Morning Drill', \
             'notes': '5100 PRESENT; 15 ABSENT; 130 CODE-RED BELOW PAR PERFORMANCE'}}
```

Copy First Line Copy Commands Copy All

Now imagine an outpost captured by the rebels. In the commands below, the rebels first search all the indices and then manipulate the diagnostics data from a compromised outpost.

``` {#codecell5}
$ kubectl exec outpost -- python search.py
Searching for Spaceship Diagnostics
Got 1 Hits:
{'_index': 'spaceship_diagnostics', '_type': 'stats', '_id': '1', '_score': 1.0, \
 '_source': {'spaceshipid': '3459B78XNZTF', 'type': 'tiefighter', 'title': 'Engine Diagnostics', \
             'stats': '[CRITICAL] [ENGINE BURN @SPEED 5000 km/s] [CHANCE 80%]'}}
Searching for Stormtroopers Performance Logs
Got 1 Hits:
{'_index': 'troop_logs', '_type': 'log', '_id': '1', '_score': 1.0, \
 '_source': {'outpost': 'Endor', 'datetime': '33 ABY 4AM DST', 'title': 'Endor Corps 1: Morning Drill', \
             'notes': '5100 PRESENT; 15 ABSENT; 130 CODE-RED BELOW PAR PERFORMANCE'}}
```

Copy First Line Copy Commands Copy All

Rebels manipulate spaceship diagnostics data so that the spaceship defects are not known to the empire-hq! (Hint: Rebels have changed the `stats`{.docutils .literal .notranslate} for the tiefighter spaceship, a change hard to detect but with adverse impact!)

``` {#codecell6}
$ kubectl exec outpost -- python update.py
Uploading Spaceship Diagnostics
{'_index': 'spaceship_diagnostics', '_type': 'stats', '_id': '1', '_score': 1.0, \
 '_source': {'spaceshipid': '3459B78XNZTF', 'type': 'tiefighter', 'title': 'Engine Diagnostics', \
             'stats': '[OK] [ENGINE OK @SPEED 5000 km/s]'}}
```

Copy First Line Copy Commands Copy All

## Securing Elasticsearch Using Cilium[](#securing-elasticsearch-using-cilium "Link to this heading")

[](../../_images/cilium_es_gsg_topology.png)

Following the least privilege security principle, we want to the allow the following legitimate actions and nothing more:

-   `outpost`{.docutils .literal .notranslate} service only has upload access to `index:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`troop_logs`{.docutils .literal .notranslate}

-   `spaceship`{.docutils .literal .notranslate} service only has upload access to `index:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`spaceship_diagnostics`{.docutils .literal .notranslate}

-   `empire-hq`{.docutils .literal .notranslate} service only has search access for both the indices

Fortunately, the Empire DevOps team is using Cilium for their Kubernetes cluster. Cilium provides L7 visibility and security policies to control Elasticsearch API access. Cilium follows the **white-list, least privilege model** for security. That is to say, a *CiliumNetworkPolicy* contains a list of rules that define **allowed requests** and any request that does not match the rules is denied.

In this example, the policy rules are defined for inbound traffic (i.e., "ingress") connections to the *elasticsearch* service. Note that endpoints selected as backend pods for the service are defined by the *selector* labels. *Selector* labels use the same concept as Kubernetes to define a service. In this example, label `component:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`elasticsearch`{.docutils .literal .notranslate} defines the pods that are part of the *elasticsearch* service in Kubernetes.

In the policy file below, you will see the following rules for controlling the indices access and actions performed:

-   `fromEndpoints`{.docutils .literal .notranslate} with labels `app:spaceship`{.docutils .literal .notranslate} only `HTTP`{.docutils .literal .notranslate} `PUT`{.docutils .literal .notranslate} is allowed on paths matching regex `^/spaceship_diagnostics/stats/.*$`{.docutils .literal .notranslate}

-   `fromEndpoints`{.docutils .literal .notranslate} with labels `app:outpost`{.docutils .literal .notranslate} only `HTTP`{.docutils .literal .notranslate} `PUT`{.docutils .literal .notranslate} is allowed on paths matching regex `^/troop_logs/log/.*$`{.docutils .literal .notranslate}

-   `fromEndpoints`{.docutils .literal .notranslate} with labels `app:empire`{.docutils .literal .notranslate} only `HTTP`{.docutils .literal .notranslate} `GET`{.docutils .literal .notranslate} is allowed on paths matching regex `^/spaceship_diagnostics/_search/??.*$`{.docutils .literal .notranslate} and `^/troop_logs/search/??.*$`{.docutils .literal .notranslate}

``` {#codecell7}
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: secure-empire-elasticsearch
  namespace: default
specs:
- endpointSelector:
    matchLabels:
      component: elasticsearch
  ingress:
  - fromEndpoints:
    - matchLabels:
        app: spaceship
    toPorts:
    - ports:
      - port: "9200"
        protocol: TCP
      rules:
        http:
        - method: ^PUT$
          path: ^/spaceship_diagnostics/stats/.*$
  - fromEndpoints:
    - matchLabels:
        app: empire-hq
    toPorts:
    - ports:
      - port: "9200"
        protocol: TCP
      rules:
        http:
        - method: ^GET$
          path: ^/spaceship_diagnostics/_search/??.*$
        - method: ^GET$
          path: ^/troop_logs/_search/??.*$
  - fromEndpoints:
    - matchLabels:
        app: outpost
    toPorts:
    - ports:
      - port: "9200"
        protocol: TCP
      rules:
        http:
        - method: ^PUT$
          path: ^/troop_logs/log/.*$
- egress:
  - toEndpoints:
    - matchExpressions:
      - key: k8s:io.kubernetes.pod.namespace
        operator: Exists
  - toEntities:
    - cluster
    - host
  endpointSelector: {}
  ingress:
  - {}
```

Copy First Line Copy All

Apply this Elasticsearch-aware network security policy using `kubectl`{.docutils .literal .notranslate}:

``` {#codecell8 .literal-block}
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-es/es-sw-policy.yaml
ciliumnetworkpolicy "secure-empire-elasticsearch" created
```

Copy First Line Copy All

Let's test the security policies. Firstly, the search access is blocked for both outpost and spaceship. So from a compromised outpost, rebels will not be able to search and obtain knowledge about troops and spaceship diagnostics. Secondly, the outpost clients don't have access to create or update the `index:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`spaceship_diagnostics`{.docutils .literal .notranslate}.

``` {#codecell9}
$ kubectl exec outpost -- python search.py
GET http://elasticsearch:9200/spaceship_diagnostics/_search [status:403 request:0.008s]
...
...
elasticsearch.exceptions.AuthorizationException: TransportError(403, 'Access denied\r\n')
command terminated with exit code 1
```

Copy First Line Copy Commands Copy All

``` {#codecell10}
$ kubectl exec outpost -- python update.py
PUT http://elasticsearch:9200/spaceship_diagnostics/stats/1 [status:403 request:0.006s]
...
...
elasticsearch.exceptions.AuthorizationException: TransportError(403, 'Access denied\r\n')
command terminated with exit code 1
```

Copy First Line Copy Commands Copy All

We can re-run any of the below commands to show that the security policy still allows all legitimate requests (i.e., no 403 errors are returned).

``` {#codecell11}
$ kubectl exec outpost -- python upload_logs.py
...
$ kubectl exec spaceship -- python upload_diagnostics.py
...
$ kubectl exec empire-hq -- python search.py
...
```

Copy First Line Copy Commands Copy All

## Clean Up[](#clean-up "Link to this heading")

You have now installed Cilium, deployed a demo app, and finally deployed & tested Elasticsearch-aware network security policies. To clean up, run:

``` {#codecell12 .literal-block}
$ kubectl delete -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes-es/es-sw-app.yaml
$ kubectl delete cnp secure-empire-elasticsearch
```

Copy First Line Copy All
