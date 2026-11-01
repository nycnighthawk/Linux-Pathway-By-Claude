---
{"title": "Uninstall Docker Compose", "url": "https://docs.docker.com/compose/install/uninstall/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Uninstall Docker Compose {#uninstall-docker-compose pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

How you uninstall Docker Compose depends on how it was installed. This guide covers uninstallation instructions for:

-   Docker Compose installed via Docker Desktop
-   Docker Compose installed as a CLI plugin

## [Uninstalling Docker Compose with Docker Desktop](#uninstalling-docker-compose-with-docker-desktop) {#uninstalling-docker-compose-with-docker-desktop .scroll-mt-20 .flex .items-center .gap-2}

If you want to uninstall Docker Compose and you have installed Docker Desktop, see [Uninstall Docker Desktop](https://docs.docker.com/desktop/uninstall/).

> Warning
>
> Unless you have other Docker instances installed on that specific environment, uninstalling Docker Desktop removes all Docker components, including Docker Engine, Docker CLI, and Docker Compose.

## [Uninstalling the Docker Compose CLI plugin](#uninstalling-the-docker-compose-cli-plugin) {#uninstalling-the-docker-compose-cli-plugin .scroll-mt-20 .flex .items-center .gap-2}

If you installed Docker Compose via a package manager, run:

On Ubuntu or Debian:

``` {.chroma tabindex="0"}
$ sudo apt-get remove docker-compose-plugin
```

On RPM-based distributions:

``` {.chroma tabindex="0"}
$ sudo yum remove docker-compose-plugin
```

### [Manually installed](#manually-installed) {#manually-installed .scroll-mt-20 .flex .items-center .gap-2}

If you installed Docker Compose manually (using curl), remove it by deleting the binary:

``` {.chroma tabindex="0"}
$ rm $DOCKER_CONFIG/cli-plugins/docker-compose
```

### [Remove for all users](#remove-for-all-users) {#remove-for-all-users .scroll-mt-20 .flex .items-center .gap-2}

If installed for all users, remove it from the system directory:

``` {.chroma tabindex="0"}
$ rm /usr/local/lib/docker/cli-plugins/docker-compose
```

> Note
>
> If you get a **Permission denied** error using either of the previous methods, you do not have the permissions needed to remove Docker Compose. To force the removal, prepend `sudo` to either of the previous instructions and run it again.

### [Inspect the location of the Compose CLI plugin](#inspect-the-location-of-the-compose-cli-plugin) {#inspect-the-location-of-the-compose-cli-plugin .scroll-mt-20 .flex .items-center .gap-2}

To check where Compose is installed, use:

``` {.chroma tabindex="0"}
$ docker info --format '{{range .ClientInfo.Plugins}}{{if eq .Name "compose"}}{{.Path}}{{end}}{{end}}'
```
