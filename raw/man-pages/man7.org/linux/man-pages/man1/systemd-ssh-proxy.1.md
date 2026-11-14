---
{"title": "systemd-ssh-proxy(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-ssh-proxy.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-ssh-proxy(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-SSH-PROXY(1)        systemd-ssh-proxy        SYSTEMD-SSH-PROXY(1)

## [](#NAME)NAME

           systemd-ssh-proxy - SSH client plugin for connecting to AF_VSOCK
           and AF_UNIX sockets

## [](#SYNOPSIS)SYNOPSIS

           Host unix/* unix%* vsock/* vsock%* vsock-mux/* vsock-mux%*
               ProxyCommand /usr/lib/systemd/systemd-ssh-proxy %h %p
               ProxyUseFdpass yes

           /usr/lib/systemd/systemd-ssh-proxy [ADDRESS] [PORT]

## [](#DESCRIPTION)DESCRIPTION

           systemd-ssh-proxy is a small "proxy" plugin for the ssh(1) tool
           that allows connecting to AF_UNIX and AF_VSOCK sockets. It
           implements the interface defined by ssh's ProxyCommand
           configuration option. It's supposed to be used with an
           ssh_config(5) configuration fragment like the following:

               Host unix/* unix%* vsock/* vsock%* vsock-mux/* vsock-mux%*
                   ProxyCommand /usr/lib/systemd/systemd-ssh-proxy %h %p
                   ProxyUseFdpass yes
                   CheckHostIP no

               Host .host
                   ProxyCommand /usr/lib/systemd/systemd-ssh-proxy unix/run/ssh-unix-local/socket %p
                   ProxyUseFdpass yes
                   CheckHostIP no

           A configuration fragment along these lines is by default installed
           into /etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf.

           With this in place, SSH connections to host string "unix/"
           followed by an absolute AF_UNIX file system path to a socket will
           be directed to the specified socket, which must be of type
           SOCK_STREAM. Similar, SSH connections to "vsock/" followed by an
           AF_VSOCK CID will result in an SSH connection made to that CID.
           "vsock-mux/" followed by an absolute AF_UNIX file system path to a
           socket is similar but for cloud-hypervisor/firecracker which do
           not allow direct AF_VSOCK communication between the host and
           guests, and provide their own multiplexer over AF_UNIX sockets.
           See cloud-hypervisor VSOCK support[1] and Using the Firecracker
           Virtio-vsock Device[2]. Note that "%" can be used as a separator
           instead of "/" to be compatible with tools like "scp" and "rsync".

           Moreover, connecting to ".host" will connect to the local host via
           SSH, without involving networking.

           This tool is supposed to be used together with
           systemd-ssh-generator(8) which when run inside a VM or container
           will bind SSH to suitable addresses.  systemd-ssh-generator is
           supposed to run in the container or VM guest, and
           systemd-ssh-proxy is run on the host, in order to connect to the
           container or VM guest.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           Example 1. Talk to a local VM with CID 4711

               ssh vsock/4711

           Example 2. Talk to a VM guest hosted with
           cloud-hypervisor/firecracker

               ssh vsock-mux/run/vm-1234.sock

           Example 3. Talk to the local host via ssh

               ssh .host

           or equivalent:

               ssh unix/run/ssh-unix-local/socket

           Example 4. Copy local 'foo' file to a local VM with CID 1348

               scp foo vsock%1348:

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-ssh-generator(8), vsock(7), unix(7), ssh(1),
           sshd(8)

## [](#NOTES)NOTES

            1. cloud-hypervisor VSOCK support
               https://github.com/cloud-hypervisor/cloud-hypervisor/blob/main/docs/vsock.md

            2. Using the Firecracker Virtio-vsock Device
               https://github.com/firecracker-microvm/firecracker/blob/main/docs/vsock.md

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                    SYSTEMD-SSH-PROXY(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-ssh-generator(8)](../man8/systemd-ssh-generator.8.html)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
