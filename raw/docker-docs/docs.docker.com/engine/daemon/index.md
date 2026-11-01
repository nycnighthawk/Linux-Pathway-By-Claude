---
{"title": "Docker daemon configuration overview", "url": "https://docs.docker.com/engine/daemon/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Docker daemon configuration overview {#docker-daemon-configuration-overview pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

This page shows you how to customize the Docker daemon, `dockerd`.

> Note
>
> This page is for users who\'ve installed Docker Engine manually. If you\'re using Docker Desktop, refer to the [settings page](https://docs.docker.com/desktop/settings-and-maintenance/settings/#docker-engine).

## [Configure the Docker daemon](#configure-the-docker-daemon) {#configure-the-docker-daemon .scroll-mt-20 .flex .items-center .gap-2}

There are two ways to configure the Docker daemon:

-   Use a JSON configuration file. This is the preferred option, since it keeps all configurations in a single place.
-   Use flags when starting `dockerd`.

You can use both of these options together as long as you don\'t specify the same option both as a flag and in the JSON file. If that happens, the Docker daemon won\'t start and prints an error message.

### [Configuration file](#configuration-file) {#configuration-file .scroll-mt-20 .flex .items-center .gap-2}

The following table shows the location where the Docker daemon expects to find the configuration file by default, depending on your system and how you\'re running the daemon.

  OS and configuration   File location
  ---------------------- --------------------------------------------
  Linux, regular setup   `/etc/docker/daemon.json`
  Linux, rootless mode   `~/.config/docker/daemon.json`
  Windows                `C:\ProgramData\docker\config\daemon.json`

For rootless mode, the daemon respects the `XDG_CONFIG_HOME` variable. If set, the expected file location is `$XDG_CONFIG_HOME/docker/daemon.json`.

You can also explicitly specify the location of the configuration file on startup, using the `dockerd --config-file` flag.

Learn about the available configuration options in the [dockerd reference docs](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file)

### [Configuration using flags](#configuration-using-flags) {#configuration-using-flags .scroll-mt-20 .flex .items-center .gap-2}

You can also start the Docker daemon manually and configure it using flags. This can be useful for troubleshooting problems.

Here\'s an example of how to manually start the Docker daemon, using the same configurations as shown in the previous JSON configuration:

``` {.chroma tabindex="0"}
$ dockerd --debug \
  --tls=true \
  --tlscert=/var/docker/server.pem \
  --tlskey=/var/docker/serverkey.pem \
  --host tcp://192.168.59.3:2376
```

#### [Listen on a Unix socket on Windows](#listen-on-a-unix-socket-on-windows) {#listen-on-a-unix-socket-on-windows .scroll-mt-20 .flex .items-center .gap-2}

Starting with Docker Engine 29.5, you can configure `dockerd` on Windows to listen on a Unix socket. This setting is optional. The default Windows endpoint remains the `npipe` named pipe.

Run `dockerd` from an elevated PowerShell session:

``` {.chroma tabindex="0"}
PS C:\> dockerd -H unix://C:/Users/<USER>/docker.sock --group docker-users
```

Replace `<USER>` with the name of your Windows user profile directory. Without `--group`, only members of the Administrators group and the `SYSTEM` account can access the socket. Use a comma-separated list to grant access to multiple users or groups.

Use a path in the user profile when granting access with `--group`. A socket created directly under `C:\` can inherit a high integrity level that blocks access for the configured users and groups.

Configure the Docker client to use the same socket:

``` {.chroma tabindex="0"}
PS C:\> docker -H unix://C:/Users/<USER>/docker.sock info
```

Learn about the available configuration options in the [dockerd reference docs](https://docs.docker.com/reference/cli/dockerd/), or by running:

``` {.chroma tabindex="0"}
$ dockerd --help
```

## [Daemon data directory](#daemon-data-directory) {#daemon-data-directory .scroll-mt-20 .flex .items-center .gap-2}

The Docker daemon persists all data in a single directory. This tracks everything related to Docker, including containers, images, volumes, service definition, and secrets.

By default the daemon stores data in:

-   `/var/lib/docker` on Linux
-   `C:\ProgramData\docker` on Windows

When using the [containerd image store](https://docs.docker.com/engine/storage/containerd/) (the default for Docker Engine 29.0 and later on fresh installations), image contents and container snapshots are stored in `/var/lib/containerd`. Other daemon data (volumes, configs) remains in `/var/lib/docker`.

When using [classic storage drivers](https://docs.docker.com/engine/storage/drivers/) like `overlay2` (the default for upgraded installations), all data is stored in `/var/lib/docker`.

### [Configure the data directory location](#configure-the-data-directory-location) {#configure-the-data-directory-location .scroll-mt-20 .flex .items-center .gap-2}

You can configure the Docker daemon to use a different storage directory using the `data-root` configuration option.

``` {.chroma tabindex="0"}
{
  "data-root": "/mnt/docker-data"
}
```

The `data-root` option does not affect image and container data stored in `/var/lib/containerd` when using the containerd image store. To change the storage location of containerd snapshotters, use the system containerd configuration file:

/etc/containerd/config.toml

``` {.chroma tabindex="0"}
version = 2
root = "/mnt/containerd-data"
```

Make sure you use a dedicated directory for each daemon. If two daemons share the same directory, for example an NFS share, you will experience errors that are difficult to troubleshoot.

## [Next steps](#next-steps) {#next-steps .scroll-mt-20 .flex .items-center .gap-2}

Many specific configuration options are discussed throughout the Docker documentation. Some places to go next include:

-   [Automatically start containers](https://docs.docker.com/engine/containers/start-containers-automatically/)
-   [Run containerd in the Docker daemon](https://docs.docker.com/engine/daemon/embedded-containerd/)
-   [Limit a container\'s resources](https://docs.docker.com/engine/containers/resource_constraints/)
-   [Configure storage drivers](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)
-   [Container security](https://docs.docker.com/engine/security/)
-   [Configure the Docker daemon to use a proxy](https://docs.docker.com/engine/daemon/proxy/)
