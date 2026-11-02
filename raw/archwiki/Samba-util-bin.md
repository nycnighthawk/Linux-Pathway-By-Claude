---
{"title": "Samba-util-bin", "url": "https://wiki.archlinux.org/title/Samba-util-bin", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Samba-util-bin

\
[samba-util-bin](https://github.com/mijocecr/samba-util/releases) is a graphical user interface (GUI) for managing Samba configuration on Linux systems. It provides a visual front‑end for editing `smb.conf`, managing Samba users and inspecting service status. The application is built with the cross‑platform **Avalonia** framework and is available as both an AppImage and an AUR package.

## Features {#Features}

-   Graphical editor for `smb.conf`.
-   Creation, modification and removal of Samba shares.
-   Management of Samba users through `smbpasswd`.
-   Validation of filesystem permissions for shared directories.
-   Service status inspection for `smbd` and `nmbd`.
-   Log viewer for Samba‑related journal entries.
-   Cross‑platform Avalonia‑based interface.

## Installation {#Installation}

The package is available as [samba-util-bin](https://aur.archlinux.org/packages/samba-util-bin/)^AUR^.

Alternatively, an AppImage can be downloaded from the [project's release](https://github.com/mijocecr/samba-util/releases) page.

The following dependencies are required for full functionality:

-   [samba](https://archlinux.org/packages/?name=samba) --- provides `smbd`, `nmbd`, `testparm` and user management tools.
-   [util-linux](https://archlinux.org/packages/?name=util-linux) --- provides `mount`, `umount`, `lsblk`, `blkid`.
-   [libnotify](https://archlinux.org/packages/?name=libnotify) --- desktop notifications.
-   [systemd](https://archlinux.org/packages/?name=systemd) --- service management.

Optional dependencies:

-   [gvfs-smb](https://archlinux.org/packages/?name=gvfs-smb) --- SMB integration in graphical file managers.
-   [nss-mdns](https://archlinux.org/packages/?name=nss-mdns) --- mDNS name resolution.
-   [avahi](https://archlinux.org/packages/?name=avahi) --- mDNS/zeroconf service discovery.

## Usage {#Usage}

When launched, the application reads the system configuration from `/etc/samba/smb.conf`. The interface provides access to:

-   Editing global and per‑share configuration.
-   Creating and removing Samba shares.
-   Managing Samba users:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
bash
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
smbpasswd -a <user>
```

-   Inspecting the status of `smbd` and `nmbd`.
-   Viewing logs related to Samba services.

Changes to `smb.conf` can be validated using `testparm`.

## System integration {#System_integration}

samba-util interacts with the standard [samba](https://archlinux.org/packages/?name=samba) mechanisms for configuration and service control. For details on Samba configuration, see:

-   [Samba](../en/Samba.html "Samba")
-   [Samba/Tips and tricks](../en/Samba/Tips_and_tricks.html "Samba/Tips and tricks")

## Troubleshooting {#Troubleshooting}

Issues encountered while using the application generally correspond to underlying Samba configuration or filesystem permissions. Refer to:

-   `testparm` for configuration validation.
-   `journalctl -u smbd` for service logs.
-   [Samba](../en/Samba.html "Samba") for detailed configuration guidance.

## See also {#See_also}

-   [GitHub repository](https://github.com/mijocecr/samba-util)
-   [AUR package](https://aur.archlinux.org/packages/samba-util-bin)
