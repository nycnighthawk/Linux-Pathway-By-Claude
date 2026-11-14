---
{"title": "pam_mkhomedir(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_mkhomedir.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_mkhomedir(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_MKHOMEDIR(8)             Linux-PAM Manual            PAM_MKHOMEDIR(8)

## [](#NAME)NAME

           pam_mkhomedir - PAM module to create users home directory

## [](#SYNOPSIS)SYNOPSIS

           pam_mkhomedir.so [silent] [debug] [umask=mode] [skel=skeldir]

## [](#DESCRIPTION)DESCRIPTION

           The pam_mkhomedir PAM module will create a users home directory if
           it does not exist when the session begins. This allows users to be
           present in central database (such as NIS, kerberos or LDAP)
           without using a distributed file system or pre-creating a large
           number of directories. The skeleton directory (usually /etc/skel/)
           is used to copy default files and also sets a umask for the
           creation.

           /usr/share/pam/skel will also be used unless skel option is
           specified.

           The new users home directory will not be removed after logout of
           the user.

## [](#OPTIONS)OPTIONS

           silent
               Don't print informative messages.

           debug
               Turns on debugging via syslog(3).

           umask=mask
               The file mode creation mask is set to mask. The default value
               of mask is 0022. If this option is not specified, then the
               permissions of created user home directory is set to the value
               of HOME_MODE configuration item from /etc/login.defs. If there
               is no such configuration item then the value is computed from
               the value of UMASK in the same file. If there is no such
               configuration option either the default value of 0755 is used
               for the mode.

           skel=/path/to/skel/directory
               Indicate an alternative skel directory to override the default
               /etc/skel.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the session module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_BUF_ERR
               Memory buffer error.

           PAM_PERM_DENIED
               Not enough permissions to create the new directory or read the
               skel directory.

           PAM_USER_UNKNOWN
               User not known to the underlying authentication module.

           PAM_SUCCESS
               Environment variables were set.

## [](#FILES)FILES

           /etc/skel
               Default skel directory

## [](#EXAMPLES)EXAMPLES

           A sample /etc/pam.d/login file:

                 auth       requisite   pam_securetty.so
                 auth       sufficient  pam_ldap.so
                 auth       required    pam_unix.so
                 auth       required    pam_nologin.so
                 account    sufficient  pam_ldap.so
                 account    required    pam_unix.so
                 password   required    pam_unix.so
                 session    required    pam_mkhomedir.so skel=/etc/skel/ umask=0022
                 session    required    pam_unix.so
                 session    optional    pam_lastlog.so
                 session    optional    pam_mail.so standard

## [](#SEE_ALSO)SEE ALSO

           pam.d(5), pam(8).

## [](#AUTHOR)AUTHOR

           pam_mkhomedir was written by Jason Gunthorpe <jgg@debian.org>.

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

    Linux-PAM                       08/04/2026               PAM_MKHOMEDIR(8)

------------------------------------------------------------------------

Pages that refer to this page: [mkhomedir_helper(8)](../man8/mkhomedir_helper.8.html)

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
