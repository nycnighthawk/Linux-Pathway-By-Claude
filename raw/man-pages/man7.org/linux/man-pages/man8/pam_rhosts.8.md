---
{"title": "pam_rhosts(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_rhosts.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_rhosts(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_RHOSTS(8)                Linux-PAM Manual               PAM_RHOSTS(8)

## [](#NAME)NAME

           pam_rhosts - The rhosts PAM module

## [](#SYNOPSIS)SYNOPSIS

           pam_rhosts.so

## [](#DESCRIPTION)DESCRIPTION

           This module performs the standard network authentication for
           services, as used by traditional implementations of rlogin and rsh
           etc.

           The authentication mechanism of this module is based on the
           contents of two files: /etc/hosts.equiv and ~/.rhosts. Firstly,
           hosts listed in the former file are treated as equivalent to the
           localhost. Secondly, entries in the user's own copy of the latter
           file is used to map "remote-host remote-user" pairs to that user's
           account on the current host. Access is granted to the user if
           their host is present in /etc/hosts.equiv and their remote account
           is identical to their local one, or if their remote account has an
           entry in their personal configuration file.

           The module authenticates a remote user (internally specified by
           the item PAM_RUSER) connecting from the remote host (internally
           specified by the item PAM_RHOST). Accordingly, for applications to
           be compatible with this authentication module they must set these
           items prior to calling pam_authenticate(). The module is not
           capable of independently probing the network connection for such
           information.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

           silent
               Don't print informative messages.

           superuser=account
               Handle account as root.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the auth module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTH_ERR
               The remote host, remote user name or the local user name
               couldn't be determined or access was denied by .rhosts file.

           PAM_USER_UNKNOWN
               User is not known to system.

## [](#EXAMPLES)EXAMPLES

           To grant a remote user access by /etc/hosts.equiv or .rhosts for
           rsh add the following lines to /etc/pam.d/rsh:

               #%PAM-1.0
               #
               auth     required       pam_rhosts.so
               auth     required       pam_nologin.so
               auth     required       pam_env.so
               auth     required       pam_unix.so

## [](#SEE_ALSO)SEE ALSO

           rootok(3), hosts.equiv(5), rhosts(5), pam.conf(5), pam.d(5),
           pam(8)

## [](#AUTHOR)AUTHOR

           pam_rhosts was written by Thorsten Kukuk <kukuk@thkukuk.de>

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

    Linux-PAM                       08/04/2026                  PAM_RHOSTS(8)

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
