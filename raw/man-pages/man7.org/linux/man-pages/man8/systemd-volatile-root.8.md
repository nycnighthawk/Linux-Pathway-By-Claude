---
{"title": "systemd-volatile-root.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-volatile-root.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-volatile-root.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD...SERVICE(8)  systemd-volatile-root.service  SYSTEMD...SERVICE(8)

## [](#NAME)NAME

           systemd-volatile-root.service, systemd-volatile-root - Make the
           root file system volatile

## [](#SYNOPSIS)SYNOPSIS

           systemd-volatile-root.service

           /usr/lib/systemd/systemd-volatile-root

## [](#DESCRIPTION)DESCRIPTION

           systemd-volatile-root.service is a service that replaces the root
           directory with a volatile memory file system ("tmpfs"), mounting
           the original (non-volatile) /usr/ inside it read-only. This way,
           vendor data from /usr/ is available as usual, but all
           configuration data in /etc/, all state data in /var/ and all other
           resources stored directly under the root directory are reset on
           boot and lost at shutdown, enabling fully stateless systems.

           This service is only enabled if full volatile mode is selected,
           for example by specifying "systemd.volatile=yes" on the kernel
           command line. This service runs only in the initrd, before the
           system transitions to the host's root directory. Note that this
           service is not used if "systemd.volatile=state" is used, as in
           that mode the root directory is non-volatile.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-fstab-generator(8), kernel-command-line(7)

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

    systemd 262~devel                                    SYSTEMD...SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-fstab-generator(8)](../man8/systemd-fstab-generator.8.html)

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
