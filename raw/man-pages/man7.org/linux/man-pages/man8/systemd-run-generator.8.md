---
{"title": "systemd-run-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-run-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-run-generator(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-RUN-GENERATOR(8)  systemd-run-generator  SYSTEMD-RUN-GENERATOR(8)

## [](#NAME)NAME

           systemd-run-generator - Generator for invoking commands specified
           on the kernel command line as system service

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-run-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-run-generator is a generator that reads the kernel command
           line and understands three options:

           If the systemd.run= option is specified and followed by a command
           line, a unit named kernel-command-line.service is generated for it
           and booted into. The service has Type=oneshot set, and has
           SuccessAction=exit and FailureAction=exit configured by default,
           thus ensuring that the system is shut down as soon as the command
           completes. The exit status of the command line is propagated to
           the invoking container manager, if this applies (which might
           propagate this further, to the calling shell — e.g.
           systemd-nspawn(1) does this). If this option is used multiple
           times the unit file will contain multiple ExecStart= lines, to
           execute all commands in order. The command is started as regular
           service, i.e. with DefaultDependencies= on.

           Use systemd.run_success_action= and systemd.run_failure_action= to
           tweak how to react to the process completing. In particular
           assigning "none" will leave the system running after the command
           completes. For further details on supported arguments, see
           systemd.unit(5).

           systemd-run-generator implements systemd.generator(7).

## [](#EXAMPLE)EXAMPLE

           Use a command like the following to add a user to the user
           database inside a container run with systemd-nspawn(1):

               # systemd-nspawn -D mycontainer -b systemd.run='"adduser test"'

           (Note the requirement for double quoting in the command line
           above. The first level of quoting ('') is processed and removed by
           the command shell used to invoke systemd-nspawn. The second level
           of quoting ("") is propagated to the kernel command line of the
           container and processed and removed by systemd-run-generator. Both
           together make sure both words of the specified command line
           adduser test end up in the generated unit file together and are
           neither split apart by the command shell nor by the generator.)

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), kernel-command-line(7),
           systemd-nspawn(1), systemd.unit(5), systemd.service(5)

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

    systemd 262~devel                                SYSTEMD-RUN-GENERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
