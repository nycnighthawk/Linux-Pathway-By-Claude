---
{"title": "systemd-bless-boot.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-bless-boot.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-bless-boot.service(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8)  systemd-bless-boot.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-bless-boot.service, systemd-bless-boot - Mark current boot
           process as successful

## [](#SYNOPSIS)SYNOPSIS

           systemd-bless-boot.service

           /usr/lib/systemd/systemd-bless-boot

## [](#DESCRIPTION)DESCRIPTION

           systemd-bless-boot.service is a system service that marks the
           current boot process as successful. It's automatically pulled into
           the initial transaction when systemd-bless-boot-generator(8)
           detects that systemd-boot(7) style boot counting is used.

           Internally, the service operates based on the LoaderBootCountPath
           EFI variable (of the vendor UUID
           4a67b082-0a4c-41cf-b6c7-440b29bb8c4f), which is passed from the
           boot loader to the OS. It contains a file system path (relative to
           the EFI system partition) of the UAPI.1 Boot Loader
           Specification[1] compliant boot loader entry file or unified
           kernel image file that was used to boot up the system.
           systemd-bless-boot.service removes the two "tries done" and "tries
           left" numeric boot counters from the filename, which indicates to
           future invocations of the boot loader that the entry has completed
           booting successfully at least once. (This service will hence
           rename the boot loader entry file or unified kernel image file on
           the first successful boot.)

## [](#OPTIONS)OPTIONS

           The /usr/lib/systemd/systemd-bless-boot executable may also be
           invoked from the command line, taking one of the following command
           arguments:

           status
               The current status of the boot loader entry file or unified
               kernel image file is shown. This outputs one of "good", "bad",
               "indeterminate", "clean", "dirty", depending on the state and
               previous invocations of the command. The string
               "indeterminate" is shown initially after boot, before it has
               been marked as "good" or "bad". The string "good" is shown
               after the boot was marked as "good" with the good command
               below, and "bad" conversely after the bad command was invoked.
               The string "clean" is returned when boot counting is currently
               not in effect (which includes the case where the current entry
               was already marked as persistently good). The string "dirty"
               is returned when the system is booted up with a known-bad
               kernel (i.e. one where the tries left counter has previously
               reached zero already).

               This command is implied if no command argument is specified.

               Added in version 240.

           good
               When invoked, the current boot loader entry file or unified
               kernel image file will be marked as "good", executing the file
               rename operation described above. This command is intended to
               be invoked at the end of a successful boot. The
               systemd-bless-boot.service unit invokes this command.

               Added in version 240.

           bad
               When called the "tries left" counter in the boot loader entry
               file name or unified kernel image file name is set to zero,
               marking the boot loader entry or kernel image as "bad", so
               that the boot loader will not consider it anymore on future
               boots (at least as long as there are other entries available
               that are not marked "bad" yet). This command is normally not
               executed, but can be used to instantly put an end to the boot
               counting logic if a problem is detected and persistently mark
               the boot entry as bad.

               Added in version 240.

           indeterminate
               This command undoes any marking of the current boot loader
               entry file or unified kernel image file as good or bad. This
               is implemented by renaming the boot loader entry file or
               unified kernel image file back to the path encoded in the
               LoaderBootCountPath EFI variable. Note that operation will
               fail if the current kernel is not booted with boot counting
               enabled (i.e. if the EFI variable is not set). If the boot
               counter already reached zero tries left on a previous boot
               this operation will fail too: once an entry is marked bad it
               can only be reset to good again, but not to indeterminate.

               Added in version 240.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-boot(7), systemd.special(7)

## [](#NOTES)NOTES

            1. UAPI.1 Boot Loader Specification
               https://uapi-group.org/specifications/specs/boot_loader_specification

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

Pages that refer to this page: [systemd-boot(7)](../man7/systemd-boot.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [systemd-bless-boot-generator(8)](../man8/systemd-bless-boot-generator.8.html)

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
