---
{"title": "systemd-vconsole-setup.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-vconsole-setup.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-vconsole-setup.service(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CREDENTIALS](#CREDENTIALS) \| [FIRMWARE-PROVIDED KEYBOARD LAYOUT](#FIRMWARE-PROVIDED_KEYBOARD_LAYOUT) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD....SERVICE(8) systemd-vconsole-setup.serviceSYSTEMD....SERVICE(8)

## [](#NAME)NAME

           systemd-vconsole-setup.service, systemd-vconsole-setup - Configure
           the virtual consoles

## [](#SYNOPSIS)SYNOPSIS

           systemd-vconsole-setup.service

           /usr/lib/systemd/systemd-vconsole-setup [TTY]

## [](#DESCRIPTION)DESCRIPTION

           systemd-vconsole-setup sets up and configures either all virtual
           consoles, or — if the optional TTY parameter is provided — a
           specific one. When the system is booting up,
           systemd-vconsole-setup.service is called by systemd-udevd(8)
           during VT console subsystem initialization. Also,
           systemd-localed.service(8) invokes it as needed when language or
           console changes are made. Internally, this program calls
           loadkeys(1) and setfont(8).

           Execute systemctl restart systemd-vconsole-setup.service in order
           to apply any manual changes made to /etc/vconsole.conf.

           See vconsole.conf(5) for information about the configuration files
           and kernel command line options understood by this program.

## [](#CREDENTIALS)CREDENTIALS

           systemd-vconsole-setup supports the service credentials logic as
           implemented by ImportCredential=/LoadCredential=/SetCredential=
           (see systemd.exec(5) for details). The following credentials are
           used when passed in:

           vconsole.keymap, vconsole.keymap_toggle
               The keymap (and toggle keymap) to apply. The matching options
               in vconsole.conf and on the kernel command line take
               precedence over these credentials.

               Note the relationship to the firstboot.keymap credential
               understood by systemd-firstboot.service(8): both ultimately
               affect the same setting, but firstboot.keymap is written into
               /etc/vconsole.conf on first boot (if not already configured),
               and then read from there by systemd-vconsole-setup, while
               vconsole.keymap is read on every boot, and is not persisted to
               disk (but any configuration in vconsole.conf will take
               precedence if present).

               Added in version 253.

           vconsole.font, vconsole.font_map, vconsole.font_unimap
               The console font settings to apply. The matching options in
               vconsole.conf and on the kernel command line take precedence
               over these credentials.

               Added in version 253.

## [](#FIRMWARE-PROVIDED_KEYBOARD_LAYOUT)FIRMWARE-PROVIDED KEYBOARD LAYOUT

           If the boot loader reports the firmware-configured keyboard layout
           via the LoaderKeyboardLayout EFI variable (see the Boot Loader
           Interface[1]), systemd-vconsole-setup uses it as the
           lowest-priority fallback for the keymap. The RFC 4646 / BCP 47
           language tag reported by the firmware (e.g.  "de-DE") is matched
           against the optional sixth column of
           /usr/share/systemd/kbd-model-map, which lists the language tags
           each virtual-console keymap covers. Credentials,
           /etc/vconsole.conf, and kernel command line options all override
           this firmware-provided default.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), vconsole.conf(5), loadkeys(1), setfont(8),
           systemd-localed.service(8)

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

    systemd 262~devel                                   SYSTEMD....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [vconsole.conf(5)](../man5/vconsole.conf.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html)

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
