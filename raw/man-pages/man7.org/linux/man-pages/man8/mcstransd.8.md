---
{"title": "mcstransd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mcstransd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mcstransd(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHOR](#AUTHOR) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mcstransd(8)                mcs documentation                mcstransd(8)

## [](#NAME)NAME

           mcstransd - MCS (Multiple Category System) daemon.  Translates
           SELinux MCS/MLS labels to human readable form.

## [](#SYNOPSIS)SYNOPSIS

           mcstransd [-f] [-h]

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes the mcstransd program.

           This daemon reads /etc/selinux/{SELINUXTYPE}/setrans.conf
           configuration file, and communicates with libselinux via a socket
           in /var/run/setrans.

## [](#OPTIONS)OPTIONS

           -f     Run mcstransd in the foreground.  Do not run as a daemon.

           -h     Output a short summary of available command line options.

## [](#AUTHOR)AUTHOR

           This man page was written by Dan Walsh <dwalsh@redhat.com>.  The
           program was originally written by Dan Walsh <dwalsh@redhat.com>.
           The program was enhanced/rewritten by Joe Nall <joe@nall.com>.

## [](#FILES)FILES

           /etc/selinux/{SELINUXTYPE}/setrans.conf

## [](#SEE_ALSO)SEE ALSO

           setrans.conf(5),mcs(8)

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

    dwalsh@redhat.com              16 Oct 2009                   mcstransd(8)

------------------------------------------------------------------------

Pages that refer to this page: [selinux_raw_context_to_color(3)](../man3/selinux_raw_context_to_color.3.html)

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
