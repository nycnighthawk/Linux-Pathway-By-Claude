---
{"title": "smbios-type-11(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/smbios-type-11.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# smbios-type-11(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [STRINGS](#STRINGS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SMBIOS-TYPE-11(7)             smbios-type-11            SMBIOS-TYPE-11(7)

## [](#NAME)NAME

           smbios-type-11 - SMBIOS Type 11 strings

## [](#SYNOPSIS)SYNOPSIS

           /sys/firmware/dmi/entries/11-*/raw

## [](#DESCRIPTION)DESCRIPTION

           Various OS components process SMBIOS Type 11 vendor strings that a
           virtual machine manager (VMM) may set and a virtual machine (VM)
           receives. SMBIOS Type 11 vendor strings may play a similar role as
           kernel-command-line(7) parameters but generally are under control
           of the VMM rather than the boot loader or UKI.

           For details on SMBIOS Type 11 see the System Management BIOS[1]
           specifications.

## [](#STRINGS)STRINGS

           The following strings are supported:

           io.systemd.credential:CREDENTIAL=VALUE,
           io.systemd.credential.binary:CREDENTIAL=VALUE
               This allows passing additional system credentials into the
               system, in textual or binary (Base64) form. See
               systemd.exec(5) and System and Service Credentials[2] for
               details.

               Added in version 252.

           io.systemd.stub.kernel-cmdline-extra=CMDLINE
               This allows configuration of additional kernel command line
               options, and is read by the kernel UEFI stub. For details see
               systemd-stub(7).

               Added in version 254.

           io.systemd.boot.kernel-cmdline-extra=CMDLINE
               This allows configuration of additional kernel command line
               options for Boot Loader Specification Type 1 entries, and is
               read by systemd-boot. For details see systemd-boot(7).

               Added in version 256.

           io.systemd.boot-entries.extra:ID=DEFINITION
               This allows inserting additional entries into the systemd-boot
               menu. For details see systemd-boot(7).

               Added in version 258.

           io.systemd.boot.loglevel=LEVEL
               This allows configuration of the log level, and is read by
               systemd-boot and systemd-stub. For details see systemd-boot(7)
               and systemd-stub(7).

               Added in version 259.

           io.systemd.boot.timeout=TIMEOUT
               This allows configuration of the menu timeout in seconds, and
               is read by systemd-boot. For details see systemd-boot(7).

               Added in version 260.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), kernel-command-line(7), systemd.system-credentials(7)

## [](#NOTES)NOTES

            1. System Management BIOS
               https://www.dmtf.org/standards/smbios/

            2. System and Service Credentials
               https://systemd.io/CREDENTIALS

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

    systemd 262~devel                                       SMBIOS-TYPE-11(7)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-analyze(1)](../man1/systemd-analyze.1.html),  [systemd-vmspawn(1)](../man1/systemd-vmspawn.1.html),  [loader.conf(5)](../man5/loader.conf.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html)

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
