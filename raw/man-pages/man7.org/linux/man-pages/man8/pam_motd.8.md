---
{"title": "pam_motd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_motd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_motd(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_MOTD(8)                  Linux-PAM Manual                 PAM_MOTD(8)

## [](#NAME)NAME

           pam_motd - Display the motd file

## [](#SYNOPSIS)SYNOPSIS

           pam_motd.so [motd=/path/filename] [motd_dir=/path/dirname.d]

## [](#DESCRIPTION)DESCRIPTION

           pam_motd is a PAM module that can be used to display arbitrary
           motd (message of the day) files after a successful login. By
           default, pam_motd shows files in the following locations:

               /etc/motd
               /run/motd
               /usr/lib/motd
               /etc/motd.d/
               /run/motd.d/
               /usr/lib/motd.d/

           Each message size is limited to 64KB.

           If /etc/motd does not exist, then /run/motd is shown. If /run/motd
           does not exist, then /usr/lib/motd is shown.

           Similar overriding behavior applies to the directories. Files in
           /etc/motd.d/ override files with the same name in /run/motd.d/ and
           /usr/lib/motd.d/. Files in /run/motd.d/ override files with the
           same name in /usr/lib/motd.d/.

           Files in the directories listed above are displayed in
           lexicographic order by name. Moreover, the files are filtered by
           reading them with the credentials of the target user
           authenticating on the system.

           To silence a message, a symbolic link with target /dev/null may be
           placed in /etc/motd.d with the same filename as the message to be
           silenced. Example: Creating a symbolic link as follows silences
           /usr/lib/motd.d/my_motd.

           ln -s /dev/null /etc/motd.d/my_motd

           The MOTD_SHOWN=pam environment variable is set after showing the
           motd files, even when all of them were silenced using symbolic
           links.

## [](#OPTIONS)OPTIONS

           motd=/path/filename
               The /path/filename file is displayed as message of the day.
               Multiple paths to try can be specified as a colon-separated
               list. By default this option is set to
               /etc/motd:/run/motd:/usr/lib/motd.

           motd_dir=/path/dirname.d
               The /path/dirname.d directory is scanned and each file
               contained inside of it is displayed. Multiple directories to
               scan can be specified as a colon-separated list. By default
               this option is set to /etc/motd.d:/run/motd.d:/usr/lib/motd.d.

           When no options are given, the default behavior applies for both
           options. Specifying either option (or both) will disable the
           default behavior for both options.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           Only the session module type is provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_ABORT
               Not all relevant data or options could be obtained.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_IGNORE
               This is the default return value of this module.

## [](#EXAMPLES)EXAMPLES

           The suggested usage for /etc/pam.d/login is:

               session  optional  pam_motd.so

           To use a motd file from a different location:

               session  optional  pam_motd.so motd=/elsewhere/motd

           To use a motd file from elsewhere, along with a corresponding .d
           directory:

               session  optional  pam_motd.so motd=/elsewhere/motd motd_dir=/elsewhere/motd.d

## [](#SEE_ALSO)SEE ALSO

           motd(5), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_motd was written by Ben Collins <bcollins@debian.org>.

           The motd_dir= option was added by Allison Karlitskaya
           <allison.karlitskaya@redhat.com>.

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

    Linux-PAM                       08/04/2026                    PAM_MOTD(8)

------------------------------------------------------------------------

Pages that refer to this page: [login(1)](../man1/login.1.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html)

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
