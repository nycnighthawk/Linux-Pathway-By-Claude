---
{"title": "Overview of installing Docker Compose", "url": "https://docs.docker.com/compose/install", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Overview of installing Docker Compose {#overview-of-installing-docker-compose pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

This page summarizes the different ways you can install Docker Compose, depending on your platform and needs.

## [Installation scenarios](#installation-scenarios) {#installation-scenarios .scroll-mt-20 .flex .items-center .gap-2}

### [Docker Desktop (Recommended)](#docker-desktop-recommended) {#docker-desktop-recommended .scroll-mt-20 .flex .items-center .gap-2}

The easiest and recommended way to get Docker Compose is to install Docker Desktop.

Docker Desktop includes Docker Compose along with Docker Engine and Docker CLI which are Compose prerequisites.

Docker Desktop is available for:

-   [Linux](https://docs.docker.com/desktop/setup/install/linux/)
-   [Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
-   [Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

> Tip
>
> If you have already installed Docker Desktop, you can check which version of Compose you have by selecting **About Docker Desktop** from the Docker menu .

### [Plugin (Linux only)](#plugin-linux-only) {#plugin-linux-only .scroll-mt-20 .flex .items-center .gap-2}

> Important
>
> This method is only available on Linux.

If you already have Docker Engine and Docker CLI installed, you can install the Docker Compose plugin from the command line, by either:

-   [Using Docker\'s repository](https://docs.docker.com/compose/install/linux/#install-using-the-repository)
-   [Downloading and installing manually](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)

### [Standalone (Legacy)](#standalone-legacy) {#standalone-legacy .scroll-mt-20 .flex .items-center .gap-2}

> Warning
>
> This install scenario is not recommended and is only supported for backward compatibility purposes.

You can [install the Docker Compose standalone](https://docs.docker.com/compose/install/standalone/) on Linux or on Windows Server.
