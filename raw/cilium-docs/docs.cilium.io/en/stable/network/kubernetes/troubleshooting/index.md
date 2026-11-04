---
{"title": "Troubleshooting", "url": "https://docs.cilium.io/en/stable/network/kubernetes/troubleshooting/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Troubleshooting[](#troubleshooting "Link to this heading")

## Verifying the installation[](#verifying-the-installation "Link to this heading")

Check the status of the [DaemonSet](../../../glossary/#term-DaemonSet) and verify that all desired instances are in "ready" state:

``` {#codecell0}
$ kubectl --namespace kube-system get ds
NAME      DESIRED   CURRENT   READY     NODE-SELECTOR   AGE
cilium    1         1         0         <none>          3s
```

Copy First Line Copy Commands Copy All

In this example, we see a desired state of 1 with 0 being ready. This indicates a problem. The next step is to list all cilium pods by matching on the label `k8s-app=cilium`{.docutils .literal .notranslate} and also sort the list by the restart count of each pod to easily identify the failing pods:

``` {#codecell1}
$ kubectl --namespace kube-system get pods --selector k8s-app=cilium \
          --sort-by='.status.containerStatuses[0].restartCount'
NAME           READY     STATUS             RESTARTS   AGE
cilium-813gf   0/1       CrashLoopBackOff   2          44s
```

Copy First Line Copy Commands Copy All

Pod `cilium-813gf`{.docutils .literal .notranslate} is failing and has already been restarted 2 times. Let's print the logfile of that pod to investigate the cause:

``` {#codecell2}
$ kubectl --namespace kube-system logs cilium-813gf
INFO      _ _ _
INFO  ___|_| |_|_ _ _____
INFO |  _| | | | | |     |
INFO |___|_|_|_|___|_|_|_|
INFO Cilium 0.8.90 f022e2f Thu, 27 Apr 2017 23:17:56 -0700 go version go1.7.5 linux/amd64
CRIT kernel version: NOT OK: minimal supported kernel version is >= 4.8
```

Copy First Line Copy Commands Copy All

In this example, the cause for the failure is a Linux kernel running on the worker node which is not meeting [System Requirements](../../../operations/system_requirements/#admin-system-reqs).

If the cause for the problem is not apparent based on these simple steps, please come and seek help on [Cilium Slack](https://slack.cilium.io).

## Apiserver outside of cluster[](#apiserver-outside-of-cluster "Link to this heading")

If you are running Kubernetes Apiserver outside of your cluster for some reason (like keeping master nodes behind a firewall), make sure that you run Cilium on master nodes too. Otherwise Kubernetes pod proxies created by Apiserver will not be able to route to pod IPs and you may encounter errors when trying to proxy traffic to pods.

You may run Cilium as a [static pod](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/) or set [tolerations](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/) for Cilium DaemonSet to ensure that Cilium pods will be scheduled on your master nodes. The exact way to do it depends on your setup.
