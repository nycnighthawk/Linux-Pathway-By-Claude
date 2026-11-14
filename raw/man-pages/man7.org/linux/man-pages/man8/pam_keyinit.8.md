---
{"title": "pam_keyinit(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_keyinit.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_keyinit(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_KEYINIT(8)               Linux-PAM Manual              PAM_KEYINIT(8)

## [](#NAME)NAME

           pam_keyinit - Kernel session keyring initialiser module

## [](#SYNOPSIS)SYNOPSIS

           pam_keyinit.so [debug] [force] [revoke]

## [](#DESCRIPTION)DESCRIPTION

           The pam_keyinit PAM module ensures that the invoking process has a
           session keyring other than the user default session keyring.

           The module checks to see if the process's session keyring is the
           user-session-keyring(7), and, if it is, creates a new
           session-keyring(7) with which to replace it. If a new session
           keyring is created, it will install a link to the user-keyring(7)
           in the session keyring so that keys common to the user will be
           automatically accessible through it. The session keyring of the
           invoking process will thenceforth be inherited by all its children
           unless they override it.

           In order to allow other PAM modules to attach tokens to the
           keyring, this module provides both an auth (limited to
           pam_setcred(3) and a session component. The session keyring is
           created in the module called. Moreover this module should be
           included as early as possible in a PAM configuration.

           This module is intended primarily for use by login processes. Be
           aware that after the session keyring has been replaced, the old
           session keyring and the keys it contains will no longer be
           accessible.

           This module should not, generally, be invoked by programs like su,
           since it is usually desirable for the key set to percolate through
           to the alternate context. The keys have their own permissions
           system to manage this.

           The keyutils package is used to manipulate keys more directly.
           This can be obtained from:

           Keyutils[1]

## [](#OPTIONS)OPTIONS

           debug
               Log debug information with syslog(3).

           force
               Causes the session keyring of the invoking process to be
               replaced unconditionally.

           revoke
               Causes the session keyring of the invoking process to be
               revoked when the invoking process exits if the session keyring
               was created for this process in the first place.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the session module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               This module will usually return this value

           PAM_AUTH_ERR
               Authentication failure.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_IGNORE
               The return value should be ignored by PAM dispatch.

           PAM_SERVICE_ERR
               Cannot determine the user name.

           PAM_SESSION_ERR
               This module will return this value if its arguments are
               invalid or if a system error such as ENOMEM occurs.

           PAM_USER_UNKNOWN
               User not known.

## [](#EXAMPLES)EXAMPLES

           Add this line to your login entries to start each login session
           with its own session keyring:

               session  required  pam_keyinit.so

           This will prevent keys from one session leaking into another
           session for the same user.

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8), keyctl(1)

## [](#AUTHOR)AUTHOR

           pam_keyinit was written by David Howells, <dhowells@redhat.com>.

## [](#NOTES)NOTES

            1. Keyutils
               http://people.redhat.com/~dhowells/keyutils/

## [](#COLOPHON)COLOPHON

           This page is part of the linux-pam (Pluggable Authentication
           Modules for Linux) project.  Information about the project can be
           found at ⟨http://www.linux-pam.org/⟩.  If you have a bug report
           for this manual page, see ⟨//www.linux-pam.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/linux-pam/linux-pam.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux-PAM                       08/04/2026                 PAM_KEYINIT(8)

------------------------------------------------------------------------

Pages that refer to this page: [cifscreds(1)](../man1/cifscreds.1.html),  [keyrings(7)](../man7/keyrings.7.html),  [keyutils(7)](../man7/keyutils.7.html),  [session-keyring(7)](../man7/session-keyring.7.html),  [user-keyring(7)](../man7/user-keyring.7.html),  [user-session-keyring(7)](../man7/user-session-keyring.7.html),  [pam_cifscreds(8)](../man8/pam_cifscreds.8.html)

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
