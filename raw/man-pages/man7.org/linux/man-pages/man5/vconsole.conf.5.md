---
{"title": "vconsole.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/vconsole.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# vconsole.conf(5) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    VCONSOLE.CONF(5)              vconsole.conf              VCONSOLE.CONF(5)

## [](#NAME)NAME

           vconsole.conf - Configuration file for the virtual console

## [](#SYNOPSIS)SYNOPSIS

           /etc/vconsole.conf

## [](#DESCRIPTION)DESCRIPTION

           The /etc/vconsole.conf file configures the virtual console, i.e.
           keyboard mapping and console font. It is applied at boot by udev
           using 90-vconsole.rules file. You can safely mask this file if you
           want to avoid this kind of initialization.

           The format of vconsole.conf is a newline-separated list of
           environment-like shell-compatible variable assignments, ignoring
           comments and empty lines. It is possible to source the
           configuration from shell scripts, however, beyond mere variable
           assignments no shell features are supported, allowing applications
           to read the file without implementing a shell compatible execution
           engine. See os-release(5) for a detailed description of the
           format.

           Note that the kernel command line options vconsole.keymap=,
           vconsole.keymap_toggle=, vconsole.font=, vconsole.font_map=,
           vconsole.font_unimap= may be used to override the console settings
           at boot.

           Depending on the operating system other configuration files might
           be checked for configuration of the virtual console as well,
           however only as fallback.

           If the boot loader reports the firmware-configured keyboard layout
           via the LoaderKeyboardLayout EFI variable (see the Boot Loader
           Interface[1]), it is used as the lowest-priority fallback for
           KEYMAP=. Any setting from credentials, /etc/vconsole.conf, or the
           kernel command line overrides it.

           /etc/vconsole.conf is usually created and updated using
           systemd-localed.service(8).  localectl(1) may be used to instruct
           systemd-localed.service to query or update configuration.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           KEYMAP=, KEYMAP_TOGGLE=
               Configures the key mapping table for the keyboard.  KEYMAP=
               defaults to "us" if not set. As a special case, if "@kernel"
               is specified, no keymap will be loaded, i.e. the kernel's
               default keymap will be used. The KEYMAP_TOGGLE= can be used to
               configure a second toggle keymap and is by default unset.

           FONT=, FONT_MAP=, FONT_UNIMAP=
               Configures the console font, the console map and the unicode
               font map.

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           A few configuration parameters from vconsole.conf may be
           overridden on the kernel command line:

           vconsole.keymap=, vconsole.keymap_toggle=
               Overrides KEYMAP= and KEYMAP_TOGGLE=.

               Added in version 232.

           vconsole.font=, vconsole.font_map=, vconsole.font_unimap=
               Overrides FONT=, FONT_MAP=, and FONT_UNIMAP=.

               Added in version 232.

## [](#EXAMPLE)EXAMPLE

           Example 1. German keyboard and console

           /etc/vconsole.conf:

               KEYMAP=de-latin1
               FONT=eurlatgr

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-vconsole-setup.service(8), loadkeys(1),
           setfont(8), locale.conf(5), systemd-localed.service(8)

## [](#NOTES)NOTES

            1. Boot Loader Interface
               https://systemd.io/BOOT_LOADER_INTERFACE

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

    systemd 262~devel                                        VCONSOLE.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [localectl(1)](../man1/localectl.1.html),  [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-localed.service(8)](../man8/systemd-localed.service.8.html),  [systemd-vconsole-setup.service(8)](../man8/systemd-vconsole-setup.service.8.html)

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
