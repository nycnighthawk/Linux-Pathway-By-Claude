---
{"title": "systemd-debug-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-debug-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-debug-generator(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SYSTEM CREDENTIALS](#SYSTEM_CREDENTIALS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-...GENERATOR(8)  systemd-debug-generator  SYSTEMD-...GENERATOR(8)

## [](#NAME)NAME

           systemd-debug-generator - Generator for enabling a runtime debug
           shell and masking specific units at boot

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-debug-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-debug-generator is a generator that provides some
           debugging functionality.

           systemd-debug-generator implements systemd.generator(7).

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-debug-generator understands the following kernel command
           line parameters:

           systemd.mask=, rd.systemd.mask=
               These options take a unit name as argument. The unit specified
               is masked for the runtime (i.e. for this session — from boot
               to shutdown), similarly to the effect of systemctl(1)'s mask
               command. This is useful to boot with certain units removed
               from the initial boot transaction for debugging system
               startup. May be specified more than once. The option prefixed
               with "rd."  is honored only in the initrd, while the one
               without prefix is only honored on the host.

               Added in version 215.

           systemd.wants=, rd.systemd.wants=
               These options take a unit name as argument. A start job for
               this unit is added to the initial transaction. This is useful
               to start one or more additional units at boot. May be
               specified more than once. The option prefixed with "rd."  is
               honored only in the initrd, while the one that is not prefixed
               only on the host.

               Added in version 215.

           systemd.debug_shell, rd.systemd.debug_shell,
           systemd.default_debug_tty=, rd.systemd.default_debug_tty=
               If the systemd.debug_shell or rd.systemd.debug_shell option is
               specified, the debug shell service "debug-shell.service" is
               pulled into the boot transaction and a debug shell will be
               spawned during early boot. By default, /dev/tty9 is used, but
               a specific tty can also be specified, either with or without
               the /dev/ prefix. To set the tty to use without enabling the
               debug shell, the systemd.default_debug_tty= option can be used
               which also takes a tty with or without the /dev/ prefix. Note
               that the shell may also be turned on persistently by enabling
               it with systemctl(1)'s enable command. The options prefixed
               with "rd."  are honored only in the initrd, while the ones
               without prefix are only honored on the host.

               Added in version 215.

           systemd.break=, rd.systemd.break=
               Takes one of pre-udev, pre-basic, pre-mount, or
               pre-switch-root (the default for the "rd."  option). It also
               accepts multiple values separated by comma (","). These
               options allow one to pause the boot process at a certain point
               and spawn a debug shell. After exiting this shell, the system
               will resume booting. The option prefixed with "rd."  is
               honored only in the initrd, while the one without prefix is
               only honored on the host.

               Table 1. Available breakpoints
               ┌─────────────────┬───────────────────────┬────────────────┬────────────────┐
               │ Breakpoints     │ Description           │ Can be used in │ Can be used on │
               │                 │                       │ the initrd     │ the host       │
               ├─────────────────┼───────────────────────┼────────────────┼────────────────┤
               │ pre-udev        │ Before starting       │ ✓              │ ✓              │
               │                 │ to process            │                │                │
               │                 │ kernel uevents,       │                │                │
               │                 │ i.e., before          │                │                │
               │                 │ systemd-udevd.service │                │                │
               │                 │ starts.               │                │                │
               ├─────────────────┼───────────────────────┼────────────────┼────────────────┤
               │ pre-basic       │ Before leaving early  │ ✓              │ ✓              │
               │                 │ boot and regular      │                │                │
               │                 │ services start, i.e., │                │                │
               │                 │ before basic.target   │                │                │
               │                 │ is reached.           │                │                │
               ├─────────────────┼───────────────────────┼────────────────┼────────────────┤
               │ pre-mount       │ Before the root       │ ✓              │ ✗              │
               │                 │ filesystem is         │                │                │
               │                 │ mounted, i.e., before │                │                │
               │                 │ sysroot.mount starts. │                │                │
               ├─────────────────┼───────────────────────┼────────────────┼────────────────┤
               │ pre-switch-root │ Before switching from │ ✓              │ ✗              │
               │                 │ the initrd to the     │                │                │
               │                 │ real root.            │                │                │
               └─────────────────┴───────────────────────┴────────────────┴────────────────┘

               Added in version 258.

## [](#SYSTEM_CREDENTIALS)SYSTEM CREDENTIALS

           systemd.extra-unit.*
               Credentials prefixed with "systemd.extra-unit."  specify
               additional units to add to the final system. Note that these
               additional units are added to both the initrd and the final
               system.  ConditionPathExists=!/etc/initrd-release can be used
               to make sure the unit is conditioned out in the initrd. Note
               that this can also be used to mask units, by simply specifying
               an empty value.

               Added in version 256.

           systemd.unit-dropin.*
               Credentials prefixed with "systemd.unit-dropin."  add drop-ins
               for the corresponding units in the final system. Each
               credential must be suffixed with the full unit name including
               the unit extension. Its contents must be a valid unit drop-in
               file. Optionally, the unit name may be followed with "~",
               followed by the drop-in name without the ".conf" suffix. If
               not specified, the name of the generated drop-in will be
               "50-credential.conf". Note that these additional drop-ins are
               added to both the initrd and the final system.

               Added in version 256.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), kernel-command-line(7),
           systemd.system-credentials(7), bootup(7)

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
