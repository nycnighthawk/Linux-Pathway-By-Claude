---
{"title": "Storage", "url": "https://docs.docker.com/engine/storage/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Storage {#storage pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

Docker storage covers two different concepts:

**Container data persistence** (this page): How to store application data outside containers using volumes, bind mounts, and tmpfs mounts. This data persists independently of container lifecycle.

**Daemon storage backends** ([containerd image store](https://docs.docker.com/engine/storage/containerd/) and [storage drivers](https://docs.docker.com/engine/storage/drivers/)): How the daemon stores image layers and container writable layers on disk.

This page focuses on container data persistence. For information about how Docker stores images and container layers, see [containerd image store](https://docs.docker.com/engine/storage/containerd/) or [Storage drivers](https://docs.docker.com/engine/storage/drivers/).

## [Container layer basics](#container-layer-basics) {#container-layer-basics .scroll-mt-20 .flex .items-center .gap-2}

By default all files created inside a container are stored on a writable container layer that sits on top of the read-only, immutable image layers.

Data written to the container layer doesn\'t persist when the container is destroyed. This means that it can be difficult to get the data out of the container if another process needs it.

The writable layer is unique per container. You can\'t easily extract the data from the writeable layer to the host, or to another container.

## [Storage mount options](#storage-mount-options) {#storage-mount-options .scroll-mt-20 .flex .items-center .gap-2}

Docker supports the following types of storage mounts for storing data outside of the writable layer of the container:

-   [Volume mounts](#volume-mounts)
-   [Bind mounts](#bind-mounts)
-   [tmpfs mounts](#tmpfs-mounts)
-   [Image mounts](#image-mounts)
-   [Named pipes](#named-pipes)

No matter which type of mount you choose to use, the data looks the same from within the container. It is exposed as either a directory or an individual file in the container\'s filesystem.

### [Volume mounts](#volume-mounts) {#volume-mounts .scroll-mt-20 .flex .items-center .gap-2}

Volumes are persistent storage mechanisms managed by the Docker daemon. They retain data even after the containers using them are removed. Volume data is stored on the filesystem on the host, but in order to interact with the data in the volume, you must mount the volume to a container. Directly accessing or interacting with the volume data is unsupported, undefined behavior, and may result in the volume or its data breaking in unexpected ways.

Volumes are ideal for performance-critical data processing and long-term storage needs. Since the storage location is managed on the daemon host, volumes provide the same raw file performance as accessing the host filesystem directly.

### [Bind mounts](#bind-mounts) {#bind-mounts .scroll-mt-20 .flex .items-center .gap-2}

Bind mounts create a direct link between a host system path and a container, allowing access to files or directories stored anywhere on the host. Since they aren\'t isolated by Docker, both non-Docker processes on the host and container processes can modify the mounted files simultaneously.

Use bind mounts when you need to be able to access files from both the container and the host.

### [tmpfs mounts](#tmpfs-mounts) {#tmpfs-mounts .scroll-mt-20 .flex .items-center .gap-2}

A tmpfs mount stores files directly in the host machine\'s memory, ensuring the data is not written to disk. This storage is ephemeral: the data is lost when the container is stopped or restarted, or when the host is rebooted. tmpfs mounts do not persist data either on the Docker host or within the container\'s filesystem.

These mounts are suitable for scenarios requiring temporary, in-memory storage, such as caching intermediate data, handling sensitive information like credentials, or reducing disk I/O. Use tmpfs mounts only when the data does not need to persist beyond the current container session.

### [Image mounts](#image-mounts) {#image-mounts .scroll-mt-20 .flex .items-center .gap-2}

An image mount makes the contents of another image available inside a container at a path you choose. The mounted image is read-only and isn\'t part of the container\'s own image, so you can bring in tools or assets from one image without rebuilding another.

Use image mounts when you need to consume files packaged as an image, such as mounting a tool-rich image to debug a minimal container, or sharing read-only assets across containers running different images. Image mounts require the [containerd image store](https://docs.docker.com/engine/storage/containerd/).

### [Named pipes](#named-pipes) {#named-pipes .scroll-mt-20 .flex .items-center .gap-2}

[Named pipes](https://docs.microsoft.com/en-us/windows/desktop/ipc/named-pipes) can be used for communication between the Docker host and a container. Common use case is to run a third-party tool inside of a container and connect to the Docker Engine API using a named pipe.

## [Next steps](#next-steps) {#next-steps .scroll-mt-20 .flex .items-center .gap-2}

Learn more about container data persistence:

-   [Volumes](https://docs.docker.com/engine/storage/volumes/)
-   [Bind mounts](https://docs.docker.com/engine/storage/bind-mounts/)
-   [tmpfs mounts](https://docs.docker.com/engine/storage/tmpfs/)
-   [Image mounts](https://docs.docker.com/engine/storage/image-mounts/)

Learn more about daemon storage backends:

-   [containerd image store](https://docs.docker.com/engine/storage/containerd/)
-   [Storage drivers](https://docs.docker.com/engine/storage/drivers/)
