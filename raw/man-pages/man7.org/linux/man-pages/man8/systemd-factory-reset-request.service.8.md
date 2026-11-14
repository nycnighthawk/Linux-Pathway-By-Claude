---
{"title": "systemd-factory-reset(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-factory-reset-request.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-factory-reset(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [EFI VARIABLES](#EFI_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-FACTORY-RESET(8)  systemd-factory-reset  SYSTEMD-FACTORY-RESET(8)

## [](#NAME)NAME

           systemd-factory-reset, systemd-factory-reset-request.service,
           systemd-factory-reset-complete.service, systemd-factory-
           reset.socket, systemd-factory-reset@.service - Request or complete
           a factory reset operation, or query current factory reset mode

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/systemd-factory-reset

           systemd-factory-reset-request.service

           systemd-factory-reset-complete.service

           systemd-factory-reset.socket

           systemd-factory-reset@.service

## [](#DESCRIPTION)DESCRIPTION

           systemd-factory-reset is a tool that can query the current factory
           reset state, request factory request operations or complete them.

           Some of the functionality is also available via the
           /run/systemd/io.systemd.FactoryReset Varlink service (implemented
           via the
           systemd-factory-reset.socket/systemd-factory-reset@.service
           units).

           See Factory Reset[1] for an overview of the factory reset logic.

## [](#COMMANDS)COMMANDS

           The /usr/lib/systemd/systemd-factory-reset executable may also be
           invoked from the command line, taking one of the following command
           arguments:

           status
               Report current factory reset state. Reports one of
               "unsupported" (if the OS does not support a factory reset
               logic), "unspecified" (if no factory reset was requested, but
               it wasn't turned off explicitly either), "off" (if the factory
               reset logic was explicitly turned off via the kernel command
               line option), "on" (if the factory reset is currently enabled
               and executed), "complete" (if the factory reset logic ran
               during the current boot but is complete now), "pending" (if a
               factory reset has been requested for the next boot).

               Returns with an exit status of 0 if the factory reset
               mechanism is currently not in effect, 10 if a factory reset is
               currently being executed, or 11 if it is pending for the next
               boot.

               Added in version 258.

           request
               Request a factory reset operation to be executed on next boot.

               Note that this is a relatively low-level operation. The
               primary interface for requesting a factory reset operation is
               by starting the factory-reset.target unit.

               This sets the FactoryResetRequest EFI variable, see below.

               This operation is executed when the
               systemd-factory-reset-request.service unit is started (which
               is typically one of the services hooked into and ordered
               before factory-reset.target).

               Added in version 258.

           cancel
               Cancel any previously requested (but not yet executed) factory
               reset operation.

               Added in version 258.

           complete
               Mark an ongoing factory reset operation as complete.

               This operation is executed when the
               systemd-factory-reset-complete.service unit is started (which
               is typically one of the services hooked into and ordered after
               factory-reset-now.target).

               Added in version 258.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --retrigger
               When used with the complete command retriggers all block
               devices, which might result in auto-discovered devices being
               usable that previously weren't because the factory reset logic
               was in place.

               Added in version 258.

           --quiet, -q
               Suppresses the state output of status, but still sets the exit
               status as documented.

               Added in version 258.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EFI_VARIABLES)EFI VARIABLES

           The following EFI variable is set and read by
           systemd-factory-reset, under the vendor UUID
           "8cf2644b-4b0b-428f-9387-6d876050dc67", for communication between
           this boot and the next.

           FactoryResetRequest
               Set whenever a factory reset is requested from the next boot,
               deleted once the factory reset is complete. Contains JSON data
               describing the requesting OS, in order to avoid confusion in
               multi-boot systems.

               Added in version 258.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-factory-reset-generator(8),
           systemd.special(7), Factory Reset[1]

## [](#NOTES)NOTES

            1. Factory Reset
               https://systemd.io/FACTORY_RESET

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

    systemd 262~devel                                SYSTEMD-FACTORY-RESET(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-factory-reset-generator(8)](../man8/systemd-factory-reset-generator.8.html),  [systemd-tpm2-clear.service(8)](../man8/systemd-tpm2-clear.service.8.html)

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
