---
{"title": "systemd-machine-tag@.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-machine-tag@.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-machine-tag@.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8) systemd-machine-tag@.serviceSYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-machine-tag@.service - Add a machine tag to the host

## [](#SYNOPSIS)SYNOPSIS

           systemd-machine-tag@.service

## [](#DESCRIPTION)DESCRIPTION

           systemd-machine-tag@TAG.service is a service template that adds
           the machine tag TAG (taken from the instance name) to the host's
           list of machine tags. Whenever an instance of this template is
           pulled in, the corresponding tag is added; the operation is
           idempotent, so pulling it in repeatedly has no further effect.

           The primary use of this template is automatic, hardware-driven
           tagging: the SYSTEMD_MACHINE_TAG udev property, when set on a
           device, causes the matching instance of this template to be pulled
           in (via SYSTEMD_WANTS=), so that plugging in or detecting a
           specific device automatically tags the host. See systemd.device(5)
           for details on the SYSTEMD_WANTS= mechanism.

           Machine tags may be inspected and edited with the tags verb of
           hostnamectl(1), and are stored in the TAGS= field of
           machine-info(5). Each tag must be 1...255 characters long and
           consist only of ASCII alphanumeric characters, "-" and ".".

           Added in version 262.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), hostnamectl(1), systemd-hostnamed.service(8),
           machine-info(5), udev(7)

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

    systemd 262~devel                                  SYSTEMD-....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
