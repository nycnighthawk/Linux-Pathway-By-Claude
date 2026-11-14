---
{"title": "pam_group(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_group.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_group(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_GROUP(8)                 Linux-PAM Manual                PAM_GROUP(8)

## [](#NAME)NAME

           pam_group - PAM module for group access

## [](#SYNOPSIS)SYNOPSIS

           pam_group.so

## [](#DESCRIPTION)DESCRIPTION

           The pam_group PAM module does not authenticate the user, but
           instead it grants group memberships (in the credential setting
           phase of the authentication module) to the user. Such memberships
           are based on the service they are applying for.

           By default rules for group memberships are taken from config file
           /etc/security/group.conf.

           If /etc/security/group.conf does not exist,
           /usr/share/pam/security/group.conf is used.

           This module's usefulness relies on the file-systems accessible to
           the user. The point being that once granted the membership of a
           group, the user may attempt to create a setgid binary with a
           restricted group ownership. Later, when the user is not given
           membership to this group, they can recover group membership with
           the precompiled binary. The reason that the file-systems that the
           user has access to are so significant, is the fact that when a
           system is mounted nosuid the user is unable to create or execute
           such a binary file. For this module to provide any level of
           security, all file-systems that the user has write access to
           should be mounted nosuid.

           The pam_group module functions in parallel with the /etc/group
           file. If the user is granted any groups based on the behavior of
           this module, they are granted in addition to those entries
           /etc/group (or equivalent).

## [](#OPTIONS)OPTIONS

           This module does not recognise any options.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the auth module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               group membership was granted.

           PAM_ABORT
               Not all relevant data could be gotten.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_CRED_ERR
               Group membership was not granted.

           PAM_IGNORE
               pam_sm_authenticate was called which does nothing.

           PAM_USER_UNKNOWN
               The user is not known to the system.

## [](#FILES)FILES

           /etc/security/group.conf
               Default configuration file

## [](#SEE_ALSO)SEE ALSO

           group.conf(5), pam.d(5), pam(8).

## [](#AUTHORS)AUTHORS

           pam_group was written by Andrew G. Morgan <morgan@kernel.org>.

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

    Linux-PAM                       08/04/2026                   PAM_GROUP(8)

------------------------------------------------------------------------

Pages that refer to this page: [group.conf(5)](../man5/group.conf.5.html)

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
