---
{"title": "systemd-getty-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-getty-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-getty-generator(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [ENVIRONMENT](#ENVIRONMENT) \| [SYSTEM CREDENTIALS](#SYSTEM_CREDENTIALS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-...GENERATOR(8)  systemd-getty-generator  SYSTEMD-...GENERATOR(8)

## [](#NAME)NAME

           systemd-getty-generator - Generator for enabling getty instances
           on the console

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-getty-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-getty-generator is a generator that automatically
           instantiates serial-getty@.service on the kernel consoles, if they
           can function as ttys and are not provided by the virtual console
           subsystem. It will also instantiate serial-getty@.service
           instances for virtualizer consoles, if execution in a virtualized
           environment is detected. If execution in a container environment
           is detected, it will instead enable console-getty.service for
           /dev/console, and container-getty@.service instances for
           additional container pseudo TTYs as requested by the container
           manager (see Container Interface[1]). This should ensure that the
           user is shown a login prompt at the right place, regardless of
           which environment the system is started in. For example, it is
           sufficient to redirect the kernel console with a kernel command
           line argument such as console= to get both kernel messages and a
           getty prompt on a serial TTY. See The kernel's command-line
           parameters[2] for more information on the console= kernel
           parameter.

           systemd-getty-generator implements systemd.generator(7).

           Further information about configuration of gettys can be found in
           systemd for Administrators, Part XVI: Gettys on Serial Consoles
           (and Elsewhere)[3].

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-getty-generator understands the following
           kernel-command-line(7) parameters:

           systemd.getty_auto=
               This kernel command line option may be used to control the
               execution mode of the generator. Takes an optional boolean
               argument. Since v258, this also takes comma-separated list of
               special values: "credential", "container", "console", and
               "builtin".

               When "credential" is specified, the two credentials
               getty.ttys.serial and getty.ttys.container will be parsed. See
               System Credentials section below for more details.

               When "container" is specified, console-getty.service and
               container-getty@.service will be enabled when the system is
               running in a container. This option will be ignored when the
               system is not in a container.

               When "console" is specified, serial-getty@.service for active
               kernel consoles will be enabled. This option will be ignored
               when the system is running in a container.

               When "builtins" is specified, serial-getty@.service for
               available virtualizer consoles will be enabled. This option
               will be ignored when the system is running in a container.

               When yes, the above four options will be enabled. When no, all
               options are disabled and no service will be enabled. When the
               kernel command line option is specified without an argument,
               defaults to yes. The generator is enabled by default, and a
               false value may be used to disable it.

               Added in version 250.

## [](#ENVIRONMENT)ENVIRONMENT

           $SYSTEMD_GETTY_AUTO
               This environment variable may be used to control the execution
               mode of the generator. Takes the same value as
               systemd.getty_auto= kernel command line option.

               Added in version 250.

## [](#SYSTEM_CREDENTIALS)SYSTEM CREDENTIALS

           getty.auto
               The system credential may be used to control the execution
               mode of the generator. Takes the same value as
               systemd.getty_auto= kernel command line option.

               Added in version 258.

           getty.ttys.serial, getty.ttys.container
               These system credentials may be used to spawn additional login
               prompts on selected TTYs. The two credentials should contain a
               newline-separated list of TTY names to spawn instances of
               serial-getty@.service (in case of getty.ttys.serial) and
               container-getty@.service (in case of getty.ttys.container) on.
               Any lines starting with a "#" will be ignored.

               Added in version 254.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), kernel-command-line(7), systemd.system-credentials(7),
           agetty(8)

## [](#NOTES)NOTES

            1. Container
                   Interface
               https://systemd.io/CONTAINER_INTERFACE

            2. The kernel's command-line parameters
               https://docs.kernel.org/admin-guide/kernel-parameters.html

            3. systemd for Administrators, Part XVI: Gettys on Serial
               Consoles (and Elsewhere)
               https://0pointer.de/blog/projects/serial-console.html

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

    systemd 262~devel                                 SYSTEMD-...GENERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.generator(7)](../man7/systemd.generator.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html)

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
