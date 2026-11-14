---
{"title": "pam_umask(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_umask.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_umask(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_UMASK(8)                 Linux-PAM Manual                PAM_UMASK(8)

## [](#NAME)NAME

           pam_umask - PAM module to set the file mode creation mask

## [](#SYNOPSIS)SYNOPSIS

           pam_umask.so [debug] [silent] [usergroups] [nousergroups]
                        [umask=mask]

## [](#DESCRIPTION)DESCRIPTION

           pam_umask is a PAM module to set the file mode creation mask of
           the current environment. The umask affects the default permissions
           assigned to newly created files.

           The PAM module tries to get the umask value from the following
           places in the following order:

           •   umask= entry in the user's GECOS field (see below for details)

           •   umask= argument

           •   UMASK entry from /etc/login.defs

           •   UMASK= entry from /etc/default/login

           The GECOS field is split on comma ',' characters. Entries must be
           set in its 'other' (sub-)field (the 5th field within the GECOS
           field), which could be done, for example, using chfn --other. In
           addition to the umask= entry, the module also recognizes the pri=
           entry, which sets the nice priority value for the session, and the
           ulimit= entry, which sets the maximum size of files the processes
           in the session can create.

## [](#OPTIONS)OPTIONS

           debug
               Print debug information.

           silent
               Don't print informative messages.

           usergroups
               If the user is not root and the username is the same as
               primary group name, the umask group bits are set to be the
               same as owner bits (examples: 022 -> 002, 077 -> 007).

           nousergroups
               This is the direct opposite of the usergroups option described
               above, which can be useful in case pam_umask has been compiled
               with usergroups enabled by default and you want to disable it
               at runtime.

           umask=mask
               Sets the calling process's file mode creation mask (umask) to
               mask & 0777. The value is interpreted as Octal.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the session type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The new umask was set successfully.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_CONV_ERR
               The conversation method supplied by the application failed to
               obtain the username.

           PAM_INCOMPLETE
               The conversation method supplied by the application returned
               PAM_CONV_AGAIN.

           PAM_SERVICE_ERR
               No username was given.

           PAM_USER_UNKNOWN
               User not known.

## [](#EXAMPLES)EXAMPLES

           Add the following line to /etc/pam.d/login to set the user
           specific umask at login:

                       session optional pam_umask.so umask=0022

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_umask was written by Thorsten Kukuk <kukuk@thkukuk.de>.

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

    Linux-PAM                       08/04/2026                   PAM_UMASK(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.exec(5)](../man5/systemd.exec.5.html)

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
