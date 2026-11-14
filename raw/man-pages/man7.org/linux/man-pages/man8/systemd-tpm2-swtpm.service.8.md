---
{"title": "systemd-tpm2-swtpm.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-tpm2-swtpm.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-tpm2-swtpm.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8)  systemd-tpm2-swtpm.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-tpm2-swtpm.service, systemd-tpm2-swtpm - Provide a
           fallback software TPM

## [](#SYNOPSIS)SYNOPSIS

           systemd-tpm2-swtpm.service

           /usr/lib/systemd/systemd-tpm2-swtpm

## [](#DESCRIPTION)DESCRIPTION

           The systemd-tpm2-swtpm.service provides fallback software TPM
           functionality, intended for use in environments where a discrete
           or firmware TPM ("hardware TPM") is not available. It is pulled
           into the boot process by systemd-tpm2-generator(8) if a hardware
           TPM is not available, and the system is configured to provide a
           software TPM in that case.

           Note that a software TPM provides only very weak security
           properties compared to a hardware TPM, and hence should only be
           used as a fallback mechanism if a hardware TPM is not available
           but TPM semantics are desired. This service ultimately wraps
           swtpm(8).

           If the boot secret /.extra/boot-secret (in the initrd) or
           /run/systemd/stub/boot-secret (on the host) is available the
           software TPM NVRAM storage is encrypted with this key. See
           systemd-stub(7) for details.

           The TPM NVRAM storage is placed on the EFI System Partition as it
           needs to be accessible during very early boot-up, in particular
           before the root file system is decrypted and mounted.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-tpm2-generator(8), swtpm(8), systemd-stub(7)

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

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-tpm2-generator(8)](../man8/systemd-tpm2-generator.8.html)

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
