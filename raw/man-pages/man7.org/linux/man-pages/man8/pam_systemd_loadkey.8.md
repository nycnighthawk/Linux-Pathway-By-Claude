---
{"title": "pam_systemd_loadkey(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_systemd_loadkey.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_systemd_loadkey(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_SYSTEMD_LOADKEY(8)     pam_systemd_loadkey     PAM_SYSTEMD_LOADKEY(8)

## [](#NAME)NAME

           pam_systemd_loadkey - Read password from kernel keyring and set it
           as PAM authtok

## [](#SYNOPSIS)SYNOPSIS

           pam_systemd_loadkey.so

## [](#DESCRIPTION)DESCRIPTION

           pam_systemd_loadkey reads a NUL-separated password list from the
           kernel keyring, and sets the last password in the list as the PAM
           authtok, which can be used by e.g.  pam_get_authtok(3).

           The password list is supposed to be stored in the "user" keyring
           of the root user, by an earlier call to systemd-ask-password(1)
           with --keyname=. You can pass the keyname to pam_systemd_loadkey
           via the keyname= option.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           keyname=
               Takes a string argument which sets the keyname to read. The
               default is "cryptsetup". During boot,
               systemd-cryptsetup@.service(8) stores a passphrase or PIN in
               the keyring. The LUKS2 volume key can also be used, via the
               link-volume-key option in crypttab(5).

               Table 1.  Possible values for keyname.
               ┌────────────┬────────────────────────┐
               │ Value      │ Description            │
               ├────────────┼────────────────────────┤
               │ cryptsetup │ Passphrase or recovery │
               │            │ key                    │
               ├────────────┼────────────────────────┤
               │ fido2-pin  │ Security token PIN     │
               ├────────────┼────────────────────────┤
               │ luks2-pin  │ LUKS2 token PIN        │
               ├────────────┼────────────────────────┤
               │ tpm2-pin   │ TPM2 PIN               │
               └────────────┴────────────────────────┘

               Added in version 255.

           debug
               The module will log debugging information as it operates.

               Added in version 255.

## [](#EXAMPLE)EXAMPLE

           This module is intended to be used when you use LUKS with a
           passphrase, enable autologin in the display manager, and want to
           unlock Gnome Keyring / KDE KWallet automatically. So in total, you
           only enter one password during boot.

           You need to set the password of your Gnome Keyring/KWallet to the
           same as your LUKS passphrase. Then add the following lines to your
           display manager's PAM config under /etc/pam.d/ (e.g.
           sddm-autologin):

               -auth       optional    pam_systemd_loadkey.so
               -auth       optional    pam_gnome_keyring.so
               -session    optional    pam_gnome_keyring.so auto_start
               -session    optional    pam_kwallet5.so auto_start

           And add the following lines to your display manager's systemd
           service file, so it can access root's keyring:

               [Service]
               KeyringMode=inherit

           In this setup, early during the boot process,
           systemd-cryptsetup@.service(8) will ask for the passphrase and
           store it in the kernel keyring with the keyname "cryptsetup". Then
           when the display manager does the autologin, pam_systemd_loadkey
           will read the passphrase from the kernel keyring, set it as the
           PAM authtok, and then pam_gnome_keyring and pam_kwallet5 will
           unlock with the same passphrase.

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

    systemd 262~devel                                  PAM_SYSTEMD_LOADKEY(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
