---
{"title": "Docker Engine", "url": "https://docs.docker.com/engine/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Docker Engine {#docker-engine pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

Docker Engine is an open source containerization technology for building and containerizing your applications. Docker Engine acts as a client-server application with:

-   A server with a long-running daemon process [`dockerd`](/reference/cli/dockerd).
-   APIs which specify interfaces that programs can use to talk to and instruct the Docker daemon.
-   A command line interface (CLI) client [`docker`](/reference/cli/docker/).

The CLI uses [Docker APIs](https://docs.docker.com/reference/api/engine/) to control or interact with the Docker daemon through scripting or direct CLI commands. Many other Docker applications use the underlying API and CLI. The daemon creates and manages Docker objects, such as images, containers, networks, and volumes.

For more details, see [Docker Architecture](https://docs.docker.com/get-started/docker-overview/#docker-architecture).

[](/engine/install)

### Install Docker Engine {#install-docker-engine .card-title}

Learn how to install the open source Docker Engine for your distribution.

[](/storage)

### Storage {#storage .card-title}

Use persistent data with Docker containers.

[](/network)

### Networking {#networking .card-title}

Manage network connections between containers.

[](/config/containers/logging/)

### Container logs {#container-logs .card-title}

Learn how to view and read container logs.

[](/config/pruning)

### Prune {#prune .card-title}

Tidy up unused resources.

[](/config/daemon)

### Configure the daemon {#configure-the-daemon .card-title}

Delve into the configuration options of the Docker daemon.

[](/engine/security/rootless)

### Rootless mode {#rootless-mode .card-title}

Run Docker without root privileges.

[](/engine/deprecated/)

### Deprecated features {#deprecated-features .card-title}

Find out what features of Docker Engine you should stop using.

[](/engine/release-notes)

### Release notes {#release-notes .card-title}

Read the release notes for the latest version.

## [Licensing](#licensing) {#licensing .scroll-mt-20 .flex .items-center .gap-2}

Commercial use of Docker Engine obtained via Docker Desktop within larger enterprises (exceeding 250 employees OR with annual revenue surpassing \$10 million USD), requires a [paid subscription](https://www.docker.com/pricing?ref=Docs&refAction=DocsEngine). Apache License, Version 2.0. See [LICENSE](https://github.com/moby/moby/blob/master/LICENSE) for the full license.
