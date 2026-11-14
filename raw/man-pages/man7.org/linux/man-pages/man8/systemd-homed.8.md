---
{"title": "systemd-homed.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-homed.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-homed.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KEY MANAGEMENT](#KEY_MANAGEMENT) \| [SIGNALS](#SIGNALS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-HOMED.SERVICE(8)  systemd-homed.service  SYSTEMD-HOMED.SERVICE(8)

## [](#NAME)NAME

           systemd-homed.service, systemd-homed - Home Area/User Account
           Manager

## [](#SYNOPSIS)SYNOPSIS

           systemd-homed.service

           /usr/lib/systemd/systemd-homed

## [](#DESCRIPTION)DESCRIPTION

           systemd-homed is a system service that may be used to create,
           remove, change or inspect home areas (directories and network
           mounts and real or loopback block devices with a filesystem,
           optionally encrypted).

           Most of systemd-homed's functionality is accessible through the
           homectl(1) command.

           See the Home Directories[1] documentation for details about the
           format and design of home areas managed by systemd-homed.service.

           Each home directory managed by systemd-homed.service synthesizes a
           local user and group. These are made available to the system using
           the User/Group Record Lookup API via Varlink[2], and thus may be
           browsed with userdbctl(1).

           systemd-homed.service also manages blob directories for each home
           directory it manages. See User Record Blob Directories[3] for more
           details.

## [](#KEY_MANAGEMENT)KEY MANAGEMENT

           User records are cryptographically signed with a public/private
           key pair (the signature is part of the JSON record itself). For a
           user to be permitted to log in locally the public key matching the
           signature of their user record must be installed. For a user
           record to be modified locally the private key matching the
           signature must be installed locally, too. The keys are stored in
           the /var/lib/systemd/home/ directory:

           /var/lib/systemd/home/local.private
               The private key of the public/private key pair used for local
               records. Currently, only a single such key may be installed.

               Added in version 246.

           /var/lib/systemd/home/local.public
               The public key of the public/private key pair used for local
               records. Currently, only a single such key may be installed.

               Added in version 246.

           /var/lib/systemd/home/*.public
               Additional public keys. Any users whose user records are
               signed with any of these keys are permitted to log in locally.
               An arbitrary number of keys may be installed this way.

               Added in version 246.

           All key files listed above are in PEM format.

           In order to migrate a home directory from a host "foobar" to
           another host "quux" it is hence sufficient to copy
           /var/lib/systemd/home/local.public from the host "foobar" to
           "quux", maybe calling the file on the destination
           /var/lib/systemd/home/foobar.public, reflecting the origin of the
           key. If the user record should be modifiable on "quux" the pair
           /var/lib/systemd/home/local.public and
           /var/lib/systemd/home/local.private need to be copied from
           "foobar" to "quux", and placed under the identical paths there, as
           currently only a single private key is supported per host. Note of
           course that the latter means that user records generated/signed
           before the key pair is copied in, lose their validity.

## [](#SIGNALS)SIGNALS

           SIGUSR1
               Upon reception of the SIGUSR1 process signal systemd-homed
               will reestablish its file watches on /home/ and rescan the
               directory for home directories.

               Added in version 258.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), homed.conf(5), homectl(1), pam_systemd_home(8),
           userdbctl(1), org.freedesktop.home1(5)

## [](#NOTES)NOTES

            1. Home Directories
               https://systemd.io/HOME_DIRECTORY

            2. User/Group Record Lookup API via Varlink
               https://systemd.io/USER_GROUP_API

            3. User Record Blob Directories
               https://systemd.io/USER_RECORD_BLOB_DIRS

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

    systemd 262~devel                                SYSTEMD-HOMED.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [homectl(1)](../man1/homectl.1.html),  [userdbctl(1)](../man1/userdbctl.1.html),  [mount_setattr(2)](../man2/mount_setattr.2.html),  [homed.conf(5)](../man5/homed.conf.5.html),  [org.freedesktop.home1(5)](../man5/org.freedesktop.home1.5.html),  [repart.d(5)](../man5/repart.d.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [nss-systemd(8)](../man8/nss-systemd.8.html),  [pam_systemd(8)](../man8/pam_systemd.8.html),  [pam_systemd_home(8)](../man8/pam_systemd_home.8.html),  [systemd-userdbd.service(8)](../man8/systemd-userdbd.service.8.html)

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
