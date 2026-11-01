---
{"title": "Swarm mode", "url": "https://docs.docker.com/engine/swarm/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Swarm mode {#swarm-mode pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

> Note
>
> Swarm mode is an advanced feature for managing a cluster of Docker daemons.
>
> Use Swarm mode if you intend to use Swarm as a production runtime environment.
>
> If you\'re not planning on deploying with Swarm, use [Docker Compose](/compose/) instead. If you\'re developing for a Kubernetes deployment, consider using the [integrated Kubernetes feature](https://docs.docker.com/desktop/use-desktop/kubernetes/) in Docker Desktop.

Current versions of Docker include Swarm mode for natively managing a cluster of Docker Engines called a swarm. Use the Docker CLI to create a swarm, deploy application services to a swarm, and manage swarm behavior.

Docker Swarm mode is built into the Docker Engine. Do not confuse Docker Swarm mode with [Docker Classic Swarm](https://github.com/docker/classicswarm) which is no longer actively developed.

## [Feature highlights](#feature-highlights) {#feature-highlights .scroll-mt-20 .flex .items-center .gap-2}

### [Cluster management integrated with Docker Engine](#cluster-management-integrated-with-docker-engine) {#cluster-management-integrated-with-docker-engine .scroll-mt-20 .flex .items-center .gap-2}

Use the Docker Engine CLI to create a swarm of Docker Engines where you can deploy application services. You don\'t need additional orchestration software to create or manage a swarm.

### [Decentralized design](#decentralized-design) {#decentralized-design .scroll-mt-20 .flex .items-center .gap-2}

Instead of handling differentiation between node roles at deployment time, the Docker Engine handles any specialization at runtime. You can deploy both kinds of nodes, managers and workers, using the Docker Engine. This means you can build an entire swarm from a single disk image.

### [Declarative service model](#declarative-service-model) {#declarative-service-model .scroll-mt-20 .flex .items-center .gap-2}

Docker Engine uses a declarative approach to let you define the desired state of the various services in your application stack. For example, you might describe an application comprised of a web front end service with message queueing services and a database backend.

### [Scaling](#scaling) {#scaling .scroll-mt-20 .flex .items-center .gap-2}

For each service, you can declare the number of tasks you want to run. When you scale up or down, the swarm manager automatically adapts by adding or removing tasks to maintain the desired state.

### [Desired state reconciliation](#desired-state-reconciliation) {#desired-state-reconciliation .scroll-mt-20 .flex .items-center .gap-2}

The swarm manager node constantly monitors the cluster state and reconciles any differences between the actual state and your expressed desired state. For example, if you set up a service to run 10 replicas of a container, and a worker machine hosting two of those replicas crashes, the manager creates two new replicas to replace the replicas that crashed. The swarm manager assigns the new replicas to workers that are running and available.

### [Multi-host networking](#multi-host-networking) {#multi-host-networking .scroll-mt-20 .flex .items-center .gap-2}

You can specify an overlay network for your services. The swarm manager automatically assigns addresses to the containers on the overlay network when it initializes or updates the application.

### [Service discovery](#service-discovery) {#service-discovery .scroll-mt-20 .flex .items-center .gap-2}

Swarm manager nodes assign each service in the swarm a unique DNS name and load balance running containers. You can query every container running in the swarm through a DNS server embedded in the swarm.

### [Load balancing](#load-balancing) {#load-balancing .scroll-mt-20 .flex .items-center .gap-2}

You can expose the ports for services to an external load balancer. Internally, the swarm lets you specify how to distribute service containers between nodes.

### [Secure by default](#secure-by-default) {#secure-by-default .scroll-mt-20 .flex .items-center .gap-2}

Each node in the swarm enforces TLS mutual authentication and encryption to secure communications between itself and all other nodes. You have the option to use self-signed root certificates or certificates from a custom root CA.

### [Rolling updates](#rolling-updates) {#rolling-updates .scroll-mt-20 .flex .items-center .gap-2}

At rollout time you can apply service updates to nodes incrementally. The swarm manager lets you control the delay between service deployment to different sets of nodes. If anything goes wrong, you can roll back to a previous version of the service.

## [What\'s next?](#whats-next) {#whats-next .scroll-mt-20 .flex .items-center .gap-2}

-   Learn Swarm mode [key concepts](https://docs.docker.com/engine/swarm/key-concepts/).
-   Get started with the [Swarm mode tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/).
-   Explore Swarm mode CLI commands
    -   [swarm init](/reference/cli/docker/swarm/init/)
    -   [swarm join](/reference/cli/docker/swarm/join/)
    -   [service create](/reference/cli/docker/service/create/)
    -   [service inspect](/reference/cli/docker/service/inspect/)
    -   [service ls](/reference/cli/docker/service/ls/)
    -   [service rm](/reference/cli/docker/service/rm/)
    -   [service scale](/reference/cli/docker/service/scale/)
    -   [service ps](/reference/cli/docker/service/ps/)
    -   [service update](/reference/cli/docker/service/update/)
