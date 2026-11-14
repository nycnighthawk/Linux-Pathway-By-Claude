---
{"title": "pam_securetty(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_securetty.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_securetty(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_SECURETTY(8)             Linux-PAM Manual            PAM_SECURETTY(8)

## [](#NAME)NAME

           pam_securetty - Limit root login to special devices

## [](#SYNOPSIS)SYNOPSIS

           pam_securetty.so [debug]

## [](#DESCRIPTION)DESCRIPTION

           pam_securetty is a PAM module that allows root logins only if the
           user is logging in on a "secure" tty, as defined by the listing in
           the securetty file. pam_securetty checks at first, if
           /etc/securetty exists. If not and it was built with vendordir
           support, it will use /usr/share/pam/securetty. pam_securetty also
           checks that the securetty files are plain files and not world
           writable. It will also allow root logins on the tty specified with
           console= switch on the kernel command line and on ttys from the
           /sys/class/tty/console/active.

           This module has no effect on non-root users and requires that the
           application fills in the PAM_TTY item correctly.

           For canonical usage, should be listed as a required authentication
           method before any sufficient authentication methods.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

           noconsole
               Do not automatically allow root logins on the kernel console
               device, as specified on the kernel command line or by the sys
               file, if it is not also specified in the securetty file.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the auth module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The user is allowed to continue authentication. Either the
               user is not root, or the root user is trying to log in on an
               acceptable device.

           PAM_AUTH_ERR
               Authentication is rejected. Either root is attempting to log
               in via an unacceptable device, or the securetty file is world
               writable or not a normal file.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_CONV_ERR
               The conversation method supplied by the application failed to
               obtain the username.

           PAM_INCOMPLETE
               The conversation method supplied by the application returned
               PAM_CONV_AGAIN.

           PAM_SERVICE_ERR
               An error occurred while the module was determining the user's
               name or tty, or the module could not open the securetty file.

           PAM_USER_UNKNOWN
               The module could not find the user name in the /etc/passwd
               file to verify whether the user had a UID of 0. Therefore, the
               results of running this module are ignored.

## [](#EXAMPLES)EXAMPLES

               auth  required  pam_securetty.so
               auth  required  pam_unix.so

## [](#SEE_ALSO)SEE ALSO

           securetty(5), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_securetty was written by Elliot Lee <sopwith@cuc.edu>.

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

    Linux-PAM                       08/04/2026               PAM_SECURETTY(8)

------------------------------------------------------------------------

Pages that refer to this page: [securetty(5)](../man5/securetty.5.html)

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
