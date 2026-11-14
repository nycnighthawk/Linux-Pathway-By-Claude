---
{"title": "shadow(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/shadow.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# shadow(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SHADOW(5)             File Formats and Configuration            SHADOW(5)

## [](#NAME)NAME

           shadow - shadowed password file

## [](#DESCRIPTION)DESCRIPTION

           shadow is a file which contains the password information for the
           system's accounts and optional aging information.

           This file must not be readable by regular users if password
           security is to be maintained.

           Each line of this file contains 9 fields, separated by colons
           (“:”), in the following order:

           login name
               It must be a valid account name, which exists on the system.

           encrypted password
               If the password field is empty, the user can log in without a
               password. However, some applications that read the /etc/shadow
               file might block access if the password field is empty.

               If the password field begins with an exclamation mark !, the
               password is locked. The remaining characters on the line
               represent the password field before the password was locked.

               Refer to crypt(3) for details on how this string is
               interpreted.

               If the password field contains a string that is not a valid
               result of crypt(3), for instance ! or *, the user cannot use a
               UNIX password to log in. However, the user may log in the
               system by other means.

           date of last password change
               The date of the last password change, expressed as the number
               of days since 1970-01-01 00:00:00 UTC.

               The value 0 indicates that the user must change their password
               the next time they log in to the system.

               An empty field means that password aging features are
               disabled.

           minimum password age
               The minimum password age is the number of days the user must
               wait before they can change their password again.

               An empty field and value 0 mean that there is no minimum
               password age.

           maximum password age
               The maximum password age is the number of days after which the
               user must change their password.

               After this number of days has elapsed, the password may still
               be valid. The user is prompted to change their password at the
               next login.

               An empty field means that there are no maximum password age,
               no password warning period, and no password inactivity period
               (see below).

               If the maximum password age is lower than the minimum password
               age, the user cannot change her password.

           password warning period
               The number of days before a password expires (see the maximum
               password age above) during which the user is warned.

               An empty field and value 0 mean that there is no password
               warning period.

           password inactivity period
               The number of days after a password expires (see the maximum
               password age above) during which the password is still
               accepted, and the user must update their password at the next
               login.

               After the password expires and the password inactivity period
               elapses, the user cannot log in and must contact their
               administrator.

               An empty string means that no inactivity period is enforced.

           account expiration date
               The date when the account expires, expressed as the number of
               days since 1970-01-01.

               Note that account expiration differs from password expiration.
               Account expiration prevents the user from logging in, whereas
               password expiration only prevents users from logging in with
               their password.

               An empty field means that the account never expires.

               The value 0 should not be used, as it is interpreted either as
               an account with no expiration or as an expiration date of
               1970-01-01.

           reserved field
               This field is reserved for future use.

## [](#FILES)FILES

           /etc/passwd
               User account information.

           /etc/shadow
               Secure user account information.

           /etc/shadow-
               Backup file for /etc/shadow.

               Note that this file is used by the tools of the shadow
               toolsuite, but not by all user and password management tools.

## [](#SEE_ALSO)SEE ALSO

           chage(1), login(1), passwd(1), passwd(5), pwck(8), pwconv(8),
           pwunconv(8), su(1), sulogin(8).

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

    shadow-utils 4.19.0             08/04/2026                      SHADOW(5)

------------------------------------------------------------------------

Pages that refer to this page: [chage(1)](../man1/chage.1.html),  [expiry(1)](../man1/expiry.1.html),  [lslogins(1)](../man1/lslogins.1.html),  [passwd(1)](../man1/passwd.1.html),  [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [getspnam(3)](../man3/getspnam.3.html),  [getspnam(3@@shadow-utils)](../man3/getspnam.3@@shadow-utils.html),  [shadow(3)](../man3/shadow.3.html),  [login.defs(5)](../man5/login.defs.5.html),  [passwd(5)](../man5/passwd.5.html),  [passwd(5@@shadow-utils)](../man5/passwd.5@@shadow-utils.html),  [credentials(7)](../man7/credentials.7.html),  [grpck(8)](../man8/grpck.8.html),  [pam_unix(8)](../man8/pam_unix.8.html),  [pwck(8)](../man8/pwck.8.html),  [useradd(8)](../man8/useradd.8.html),  [vipw(8)](../man8/vipw.8.html)

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
