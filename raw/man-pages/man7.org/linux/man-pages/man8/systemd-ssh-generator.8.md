---
{"title": "systemd-ssh-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-ssh-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-ssh-generator(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [CREDENTIALS](#CREDENTIALS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-SSH-GENERATOR(8)  systemd-ssh-generator  SYSTEMD-SSH-GENERATOR(8)

## [](#NAME)NAME

           systemd-ssh-generator - Generator for binding a socket-activated
           SSH server to local AF_VSOCK and AF_UNIX sockets

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-ssh-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-ssh-generator binds a socket-activated SSH server to local
           AF_VSOCK and AF_UNIX sockets under certain conditions. It only has
           an effect if the sshd(8) binary is installed. Specifically, it
           does the following:

           •   If invoked in a VM with AF_VSOCK support, a socket-activated
               SSH per-connection service is bound to AF_VSOCK port 22.

           •   If invoked in a container environment with a writable
               directory /run/host/unix-export/ pre-mounted it binds SSH to
               an AF_UNIX socket /run/host/unix-export/ssh. The assumption is
               that this directory is bind mounted to the host side as well,
               and can be used to connect to the container from there. See
               Container Interface[1] for more information about this
               interface.

           •   A local AF_UNIX socket /run/ssh-unix-local/socket is also
               bound, unconditionally. This may be used for SSH communication
               from the host to itself, without involving networking, for
               example to traverse security boundaries safely and with secure
               authentication.

           •   Additional AF_UNIX and AF_VSOCK sockets are optionally bound,
               based on the systemd.ssh_listen= kernel command line option or
               the ssh.listen system credential (see below).

           See systemd-ssh-proxy(1) for details on how to connect to these
           sockets via the ssh client.

           The ssh.authorized_keys.root credential can be used to allow
           specific public keys to log in over SSH. See
           systemd.system-credentials(7) for more information.

           The generator will use a packaged sshd@.service service template
           file if one exists, and otherwise generate a suitable service
           template file.

           systemd-ssh-generator implements systemd.generator(7).

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-ssh-generator understands the following
           kernel-command-line(7) parameters:

           systemd.ssh_auto=
               This option takes an optional boolean argument, and defaults
               to yes. If enabled, the automatic binding to the AF_VSOCK and
               AF_UNIX sockets listed above is done. If disable, this is not
               done, except for those explicitly requested via
               systemd.ssh_listen= on the kernel command line or via the
               ssh.listen system credential.

               Added in version 256.

           systemd.ssh_listen=
               This option configures an additional socket to bind SSH to. It
               may be used multiple times to bind multiple sockets. The
               syntax should follow the one of ListenStream=, see
               systemd.socket(5) for details. This functionality supports all
               socket families systemd(1) supports, including AF_INET and
               AF_INET6.

               Added in version 256.

## [](#CREDENTIALS)CREDENTIALS

           systemd-ssh-generator supports the system credentials logic. The
           following credentials are used when passed in:

           ssh.listen
               This credential should be a text file, with each line
               referencing one additional socket to bind SSH to. The syntax
               should follow the one of ListenStream=, see systemd.socket(5)
               for details. This functionality supports all socket families
               systemd supports, including AF_INET and AF_INET6.

               Added in version 256.

           ssh.ephemeral-authorized_keys-all
               Provides additional public keys, given in the customary
               authorized_keys format, for all users, for incoming
               connections via the generated AF_VSOCK and AF_UNIX socket
               units.

               The intended use of this is for a host system (in either VM or
               container configurations) to generate a keypair and inject the
               public key into the guest, using the private key to connect to
               any user account on the guest via ssh, without further
               authentication.

               Added in version 256.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), kernel-command-line(7), systemd.system-credentials(7),
           vsock(7), unix(7), ssh(1), sshd(8)

## [](#NOTES)NOTES

            1. Container Interface
               https://systemd.io/CONTAINER_INTERFACE

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

    systemd 262~devel                                SYSTEMD-SSH-GENERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-ssh-issue(1)](../man1/systemd-ssh-issue.1.html),  [systemd-ssh-proxy(1)](../man1/systemd-ssh-proxy.1.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html)

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
