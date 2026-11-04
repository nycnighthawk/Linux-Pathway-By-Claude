---
{"title": "How nodes work", "url": "https://docs.docker.com/engine/swarm/how-swarm-mode-works/nodes/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# How nodes work {#how-nodes-work pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

Swarm mode lets you create a cluster of one or more Docker Engines called a swarm. A swarm consists of one or more nodes: physical or virtual machines running Docker Engine.

There are two types of nodes: [managers](#manager-nodes) and [workers](#worker-nodes).

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9ImN1cnJlbnRDb2xvciIgYXJpYS1oaWRkZW49InRydWUiIGRhdGEtc2xvdD0iaWNvbiI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNNS40NyA1LjQ3YS43NS43NS4wIDAxMS4wNi4wTDEyIDEwLjk0bDUuNDctNS40N2EuNzUuNzUuMCAxMTEuMDYgMS4wNkwxMy4wNiAxMmw1LjQ3IDUuNDdhLjc1Ljc1LjAgMTEtMS4wNiAxLjA2TDEyIDEzLjA2bC01LjQ3IDUuNDdhLjc1Ljc1LjAgMDEtMS4wNi0xLjA2TDEwLjk0IDEyIDUuNDcgNi41M2EuNzUuNzUuMCAwMTAtMS4wNnoiIGNsaXAtcnVsZT0iZXZlbm9kZCI+PC9wYXRoPjwvc3ZnPg==)

![Swarm mode cluster](/engine/swarm/images/swarm-diagram.webp)

If you haven\'t already, read through the [Swarm mode overview](https://docs.docker.com/engine/swarm/) and [key concepts](https://docs.docker.com/engine/swarm/key-concepts/).

## [Manager nodes](#manager-nodes) {#manager-nodes .scroll-mt-20 .flex .items-center .gap-2}

Manager nodes handle cluster management tasks:

-   Maintaining cluster state
-   Scheduling services
-   Serving Swarm mode [HTTP API endpoints](https://docs.docker.com/reference/api/engine/)

Using a [Raft](https://raft.github.io/raft.pdf) implementation, the managers maintain a consistent internal state of the entire swarm and all the services running on it. For testing purposes it is OK to run a swarm with a single manager. If the manager in a single-manager swarm fails, your services continue to run, but you need to create a new cluster to recover.

To take advantage of Swarm mode\'s fault-tolerance features, we recommend you implement an odd number of nodes according to your organization\'s high-availability requirements. When you have multiple managers you can recover from the failure of a manager node without downtime.

-   A three-manager swarm tolerates a maximum loss of one manager.

-   A five-manager swarm tolerates a maximum simultaneous loss of two manager nodes.

-   An odd number `N` of manager nodes in the cluster tolerates the loss of at most `(N-1)/2` managers. Docker recommends a maximum of seven manager nodes for a swarm.

    > Important
    >
    > Adding more managers does NOT mean increased scalability or higher performance. In general, the opposite is true.

## [Worker nodes](#worker-nodes) {#worker-nodes .scroll-mt-20 .flex .items-center .gap-2}

Worker nodes are also instances of Docker Engine whose sole purpose is to execute containers. Worker nodes don\'t participate in the Raft distributed state, make scheduling decisions, or serve the swarm mode HTTP API.

You can create a swarm of one manager node, but you cannot have a worker node without at least one manager node. By default, all managers are also workers. In a single manager node cluster, you can run commands like `docker service create` and the scheduler places all tasks on the local engine.

To prevent the scheduler from placing tasks on a manager node in a multi-node swarm, set the availability for the manager node to `Drain`. The scheduler gracefully stops tasks on nodes in `Drain` mode and schedules the tasks on an `Active` node. The scheduler does not assign new tasks to nodes with `Drain` availability.

Refer to the [`docker node update`](/reference/cli/docker/node/update/) command line reference to see how to change node availability.

## [Change roles](#change-roles) {#change-roles .scroll-mt-20 .flex .items-center .gap-2}

You can promote a worker node to be a manager by running `docker node promote`. For example, you may want to promote a worker node when you take a manager node offline for maintenance. See [node promote](/reference/cli/docker/node/promote/).

You can also demote a manager node to a worker node. See [node demote](/reference/cli/docker/node/demote/).

## [Learn more](#learn-more) {#learn-more .scroll-mt-20 .flex .items-center .gap-2}

-   Read about how Swarm mode [services](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/) work.
-   Learn how [PKI](https://docs.docker.com/engine/swarm/how-swarm-mode-works/pki/) works in Swarm mode.
