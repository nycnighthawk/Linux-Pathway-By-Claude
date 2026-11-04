---
{"title": "Start the daemon", "url": "https://docs.docker.com/engine/daemon/start/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Start the daemon {#start-the-daemon pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

This page shows how to start the daemon, either manually or using OS utilities.

## [Start the daemon using operating system utilities](#start-the-daemon-using-operating-system-utilities) {#start-the-daemon-using-operating-system-utilities .scroll-mt-20 .flex .items-center .gap-2}

On a typical installation the Docker daemon is started by a system utility, not manually by a user. This makes it easier to automatically start Docker when the machine reboots.

The command to start Docker depends on your operating system. Check the correct page under [Install Docker](https://docs.docker.com/engine/install/).

### [Start with systemd](#start-with-systemd) {#start-with-systemd .scroll-mt-20 .flex .items-center .gap-2}

On some operating systems, like Ubuntu and Debian, the Docker daemon service starts automatically. Use the following command to start it manually:

``` {.chroma tabindex="0"}
$ sudo systemctl start docker
```

If you want Docker to start at boot, see [Configure Docker to start on boot](https://docs.docker.com/engine/install/linux-postinstall/#configure-docker-to-start-on-boot-with-systemd).

## [Start the daemon manually](#start-the-daemon-manually) {#start-the-daemon-manually .scroll-mt-20 .flex .items-center .gap-2}

If you don\'t want to use a system utility to manage the Docker daemon, or just want to test things out, you can manually run it using the `dockerd` command. You may need to use `sudo`, depending on your operating system configuration.

When you start Docker this way, it runs in the foreground and sends its logs directly to your terminal.

``` {.chroma tabindex="0"}
$ dockerd

INFO[0000] +job init_networkdriver()
INFO[0000] +job serveapi(unix:///var/run/docker.sock)
INFO[0000] Listening for HTTP on unix (/var/run/docker.sock)
```

To stop Docker when you have started it manually, issue a `Ctrl+C` in your terminal.
