---
{"title": "systemd-tpm2-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-tpm2-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-tpm2-generator(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-TPM2-GENERATOR(8) systemd-tpm2-generatorSYSTEMD-TPM2-GENERATOR(8)

## [](#NAME)NAME

           systemd-tpm2-generator - Generator for inserting TPM2
           synchronization point in the boot process

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-tpm2-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-tpm2-generator is a generator that adds a Wants=
           dependency from sysinit.target to tpm2.target when it detects that
           the firmware discovered a TPM2 device but the OS kernel so far did
           not.  tpm2.target is supposed to act as synchronization point for
           all services that require TPM2 device access. See
           systemd.special(7) for details.

           The systemd.tpm2_wait= kernel command line option may be used to
           override behaviour of the generator. It accepts a boolean value:
           if true then tpm2.target will be added as synchronization point
           even if the firmware has not detected a TPM2 device. If false, the
           target will not be inserted even if firmware reported a device but
           the OS kernel does not expose a device for it yet. The latter
           might be useful in environments where a suitable TPM2 driver for
           the available hardware is not available.

           The systemd.tpm2_software_fallback= kernel command line option
           (which takes a boolean argument, defaulting to false) may be used
           to enable an automatic software TPM fallback in case a hardware
           TPM is not detected and swtpm(8) is available. This pulls in the
           systemd-tpm2-swtpm.service(8) service.

           systemd-tpm2-generator implements systemd.generator(7).

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.special(7), kernel-command-line(7),
           systemd-tpm2-swtpm.service(8)

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

    systemd 262~devel                               SYSTEMD-TPM2-GENERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [systemd-tpm2-swtpm.service(8)](../man8/systemd-tpm2-swtpm.service.8.html)

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
