---
{"title": "chpasswd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/chpasswd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chpasswd(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CAVEATS](#CAVEATS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHPASSWD(8)             System Management Commands            CHPASSWD(8)

## [](#NAME)NAME

           chpasswd - update passwords in batch mode

## [](#SYNOPSIS)SYNOPSIS

           chpasswd [options]

## [](#DESCRIPTION)DESCRIPTION

           The chpasswd command reads a list of user name and password pairs
           from standard input and uses this information to update a group of
           existing users. Each line is of the format:

           user_name:password

           By default the passwords must be supplied in clear-text, and are
           encrypted by chpasswd. Also the password age will be updated, if
           present.

           By default, passwords are encrypted by PAM, but (even if not
           recommended) you can select a different encryption method with the
           -e, -m, or -c options.

           Except when PAM is used to encrypt the passwords, chpasswd first
           updates all the passwords in memory, and then commits all the
           changes to disk if no errors occurred for any user.

           When PAM is used to encrypt the passwords (and update the
           passwords in the system database) then if a password cannot be
           updated chpasswd continues updating the passwords of the next
           users, and will return an error code on exit.

           This command is intended to be used in a large system environment
           where many accounts are created at a single time.

## [](#OPTIONS)OPTIONS

           The options which apply to the chpasswd command are:

           -c, --crypt-method METHOD
               Use the specified method to encrypt the passwords.

               The available methods are DES, MD5, SHA256, SHA512 and NONE if
               your libc supports these methods.

               By default, PAM is used to encrypt the passwords.

           -e, --encrypted
               Supplied passwords are in encrypted form.

           -h, --help
               Display help message and exit.

           -m, --md5
               Use MD5 encryption instead of DES when the supplied passwords
               are not encrypted.

           -R, --root CHROOT_DIR
               Apply changes in the CHROOT_DIR directory and use the
               configuration files from the CHROOT_DIR directory. Only
               absolute paths are supported. No SELINUX support.

           -P, --prefix PREFIX_DIR
               Apply changes to configuration files under the root filesystem
               found under the directory PREFIX_DIR. This option does not
               chroot and is intended for preparing a cross-compilation
               target. Some limitations: NIS and LDAP users/groups are not
               verified. PAM authentication is using the host files. No
               SELINUX support.

           -s, --sha-rounds ROUNDS
               Use the specified number of rounds to encrypt the passwords.

               You can only use this option with crypt method: SHA256 SHA512

               By default, the number of rounds for SHA256 or SHA512 is
               defined by the SHA_CRYPT_MIN_ROUNDS and SHA_CRYPT_MAX_ROUNDS
               variables in /etc/login.defs.

               A minimal value of 1000 and a maximal value of 999,999,999
               will be enforced for SHA256 and SHA512. The default number of
               rounds is 5000.

## [](#CAVEATS)CAVEATS

           Remember to set permissions or umask to prevent readability of
           unencrypted files by other users.

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variables in /etc/login.defs change
           the behavior of this tool:

           SHA_CRYPT_MIN_ROUNDS (number), SHA_CRYPT_MAX_ROUNDS (number)
               When ENCRYPT_METHOD is set to SHA256 or SHA512, this defines
               the number of SHA rounds used by the encryption algorithm by
               default (when the number of rounds is not specified on the
               command line).

               With a lot of rounds, it is more difficult to brute force the
               password. But note also that more CPU resources will be needed
               to authenticate users.

               If not specified, the libc will choose the default number of
               rounds (5000), which is orders of magnitude too low for modern
               hardware.

               The values must be inside the 1000-999,999,999 range.

               If only one of the SHA_CRYPT_MIN_ROUNDS or
               SHA_CRYPT_MAX_ROUNDS values is set, then this value will be
               used.

               If SHA_CRYPT_MIN_ROUNDS > SHA_CRYPT_MAX_ROUNDS, the highest
               value will be used.

               Note: this only affect the generation of group passwords. The
               generation of user passwords is done by PAM and subject to the
               PAM configuration. It is recommended to set this variable
               consistently with the PAM configuration.

## [](#FILES)FILES

           /etc/passwd
               User account information.

           /etc/shadow
               Secure user account information.

           /etc/login.defs
               Shadow password suite configuration.

           /etc/pam.d/chpasswd
               PAM configuration for chpasswd.

## [](#SEE_ALSO)SEE ALSO

           passwd(1), newusers(8), login.defs(5), useradd(8).

## [](#COLOPHON)COLOPHON

           This page is part of the shadow-utils (utilities for managing
           accounts and shadow password files) project.  Information about
           the project can be found at 
           ⟨https://github.com/shadow-maint/shadow⟩.  If you have a bug report
           for this manual page, send it to
           pkg-shadow-devel@alioth-lists.debian.net.  This page was obtained
           from the tarball shadow-4.19.0.tar fetched from
           ⟨https://github.com/shadow-maint/shadow/releases⟩ on 2026-08-04.
           If you discover any rendering problems in this HTML version of the
           page, or you believe there is a better or more up-to-date source
           for the page, or you have corrections or improvements to the
           information in this COLOPHON (which is not part of the original
           manual page), send a mail to man-pages@man7.org

    shadow-utils 4.19.0             08/04/2026                    CHPASSWD(8)

------------------------------------------------------------------------

Pages that refer to this page: [passwd(1)](../man1/passwd.1.html)

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
