---
{"title": "Install Arch Linux via Docker", "url": "https://wiki.archlinux.org/title/Install_Arch_Linux_via_Docker", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Install Arch Linux via Docker

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** Formatting does not comply to the guidelines, see [Help:Style](../en/Help:Style.html "Help:Style"). (Discuss in [Talk:Install Arch Linux via Docker](../en/Talk:Install_Arch_Linux_via_Docker.html))

This document is a guide for installing [Arch Linux](../en/Arch_Linux.html "Arch Linux") using the official [Arch Linux Container Image from Docker Hub](https://hub.docker.com/_/archlinux). For alternative means of installation, see [Category:Installation process](../en/Category:Installation_process.html "Category:Installation process").

Before installing, it would be advised to view the [FAQ](../en/Frequently_asked_questions.html "FAQ"). For conventions used in this document, see [Help:Reading](../en/Help:Reading.html "Help:Reading"). In particular, code examples may contain placeholders (formatted in *`italics`*) that must be replaced manually.

For more detailed instructions, see the respective [ArchWiki](../en/ArchWiki:About.html "ArchWiki") articles or the various programs\' [man pages](../en/Man_page.html "Man page"), both linked from this guide. For interactive help, the [IRC channel](../en/IRC_channel.html "IRC channel") and the [forums](https://bbs.archlinux.org/) are also available.

Arch Linux should run on any [x86_64](https://en.wikipedia.org/wiki/X86-64 "wikipedia:X86-64")-compatible machine with a minimum of 512 MiB RAM, though more memory is needed to boot the live system for installation [\[1\]](https://lists.archlinux.org/archives/list/arch-releng@lists.archlinux.org/message/D5HSGOFTPGYI6IZUEB3ZNAX4D3F3ID37/). A basic installation should take less than 2 GiB of disk space. As the installation process needs to retrieve packages from a remote repository, this guide assumes a working internet connection is available. Furthermore a working [Docker](../en/Docker.html "Docker") setup on the host is required. While technically it is certainly possible to use any qemu supported host to install Arch with, this guide will not cover this however.

## Pre-installation {#Pre-installation}

This guide assumes that the host system is already pre-configured with regards to normally expected things. E.g. the time is setup correctly, internet connection is working normally, EFI mode if required is setup correctly etc.

### Prepare an installation medium {#Prepare_an_installation_medium}

The installation requires a target directory to which Arch Linux will be installed. Any writable directory can be used, but it is quite likely that the target directory has a partition or volume mounted that will serve as the root disk.

#### Full disk partitions {#Full_disk_partitions}

If a full disk is being used as a target, it may need to be formatted. For details see [Installation guide#Partition the disks](../en/Installation_guide.html#Partition_the_disks "Installation guide") as the same partitioning instructions and order can be followed from there. All the same restrictions and requirements as from there apply as well.

Likewise, the new disk will also needed to be formatted. The instructions from [Installation guide#Format the partitions](../en/Installation_guide.html#Format_the_partitions "Installation guide") can be used for this as well.

#### Volumes {#Volumes}

When using filesystems such as [btrfs](../en/Btrfs.html "Btrfs") or zfs, filesystem volumes are an option to use. Depending on what filesystem is used, creating them uses their own list of commands. In this guide, btrfs will be used as an example.

First, a root volume for Arch Linux is created. This command assumes the current working directory is the btrfs root volume (subvolid=5), but anywhere could be used. If a different location is used, within an existing hierarchy, keep this in mind when later defining fstab and similar. Also note, that as the Arch Linux specific volume is created on a mounted (root) volume, it could be the case that the underlying stack is using (full)disk encryption.

     # btrfs subvolume create "arch_root"

**Note** To get the root volume, mount the btrfs with the `subvolid=5` option.

### Mount the file systems {#Mount_the_file_systems}

The following section assumes the location Arch Linux will be installed into */tmp/target*. It is thus required that the partition is thus mounted there. Using a btrfs subvolume called **arch_root**, with *autodefrag* and *LZO compression* enabled would look as:

    # mkdir -p /tmp/target
    # mount /dev/disk /tmp/target -o subvol=arch_root,compress=lzo,autodefrag

The instructions from [Installation guide#Mount the file systems](../en/Installation_guide.html#Mount_the_file_systems "Installation guide") can be used for this as well.

## Installation {#Installation}

### Launching the container {#Launching_the_container}

The remainder of the installation will be done inside a docker container, abbreviated with ADC, Arch Docker Container.

     # docker run \
              --env PS1="ADC(\#)[\d \T:\w]\\$ " \
              --interactive \
              --privileged \
              --rm \
              --tty \
              --volume "/tmp/target:/target" \
              "index.docker.io/library/archlinux:latest" /bin/sh

### Select the mirrors {#Select_the_mirrors}

Packages to be installed must be downloaded from [mirror servers](../en/Mirrors.html "Mirrors"), which are defined in `/etc/pacman.d/mirrorlist`. In the docker container we first install [reflector](../en/Reflector.html "Reflector"), which updates the mirror list by choosing 70 most recently synchronized HTTPS mirrors and sorting them by download rate. [\[2\]](https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/configs/releng/airootfs/etc/systemd/system/reflector.service) First we have to [install](../en/Help:Reading.html#Installation_of_packages "Install") [reflector](../en/Reflector.html "Reflector") in the docker container to be able to use it.

    # reflector [--country <country>] \
                 --latest 5 \
                 --protocol http,https \
                 --save "/etc/pacman.d/mirrorlist" \
                 --sort rate

The higher a mirror is placed in the list, the more priority it is given when downloading a package. Ensure to inspect the file to see if it is satisfactory. If it is not, edit the file accordingly, and move the geographically closest mirrors to the top of the list, although other criteria should be taken into account.

This file will later be copied to the new system by *pacstrap*, so it is worth getting right.

### Install essential packages {#Install_essential_packages}

To be able to start the installation, the [arch-install-scripts](https://archlinux.org/packages/?name=arch-install-scripts) package must be [installed](../en/Help:Reading.html#Installation_of_packages "Install") into the Docker image first. Once completed, the official installation guide can be followed starting with the section [Installation guide#Install essential packages](../en/Installation_guide.html#Install_essential_packages "Installation guide").

**Note** The docker container contains pacman configuration options intended for minification. Be sure to check `/etc/pacman.conf` and remove the `NoExtract` options at the end or you may get a broken installation.

Return to this guide before executing the **Reboot** step from the section [Installation guide#Reboot](../en/Installation_guide.html#Reboot "Installation guide") to instead continue with the [#Reboot](#Reboot) below.

## Reboot {#Reboot}

Exit the docker container by typing `exit` or pressing `Ctrl+d`.

Optionally manually unmount all the partitions with `umount -R "/target"`: this allows noticing any \"busy\" partitions, and finding the cause with [fuser(1)](https://man.archlinux.org/man/fuser.1).

With a correctly setup boot loader, a reboot should now be possible into the freshly installed Arch Linux.

## Post-installation {#Post-installation}

See [General recommendations](../en/General_recommendations.html "General recommendations") for system management directions and post-installation tutorials (like setting up a graphical user interface, sound or a touchpad).

For a list of applications that may be of interest, see [List of applications](../en/List_of_applications.html "List of applications").
