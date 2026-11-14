---
{"title": "restorecond(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/restorecond.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# restorecond(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHOR](#AUTHOR) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    restorecond(8)                                             restorecond(8)

## [](#NAME)NAME

           restorecond - daemon that watches for file creation and then sets
           the default SELinux file context

## [](#SYNOPSIS)SYNOPSIS

           restorecond [-d] [-h] [-f restorecond_file ] [-F] [-u] [-v]

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes the restorecond program.

           This daemon uses inotify to watch files listed in the
           /etc/selinux/restorecond.conf, when they are created, this daemon
           will make sure they have the correct file context associated with
           the policy.

## [](#OPTIONS)OPTIONS

           -d     Turns on debugging mode.   Application will stay in the
                  foreground and lots of debugs messages start printing.

           -h     Print usage statement.

           -f restorecond_file
                  Use alternative restorecond.conf file.

           -F     Run in foreground, do not become a daemon.

           -u     Turns on user mode.  Runs restorecond in the user session
                  and reads /etc/selinux/restorecond_user.conf.  Uses dbus to
                  make sure only one restorecond is running per user session.

           -v     Turns on verbose debugging.  (Report missing files)

## [](#AUTHOR)AUTHOR

           This man page and program was written by Dan Walsh
           <dwalsh@redhat.com>.

## [](#FILES)FILES

           /etc/selinux/restorecond.conf /etc/selinux/restorecond_user.conf

## [](#SEE_ALSO)SEE ALSO

           restorecon(8),

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2002031409                 restorecond(8)

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
