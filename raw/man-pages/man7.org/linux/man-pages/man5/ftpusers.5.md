---
{"title": "ftpusers(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/ftpusers.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ftpusers(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ftpusers(5)                File Formats Manual                ftpusers(5)

## [](#NAME)NAME

           ftpusers - list of users that may not log in via the FTP daemon

## [](#DESCRIPTION)DESCRIPTION

           The text file ftpusers contains a list of users that may not log
           in using the File Transfer Protocol (FTP) server daemon.  This
           file is used not merely for system administration purposes but
           also for improving security within a TCP/IP networked environment.

           The ftpusers file will typically contain a list of the users that
           either have no business using ftp or have too many privileges to
           be allowed to log in through the FTP server daemon.  Such users
           usually include root, daemon, bin, uucp, and news.

           If your FTP server daemon doesn't use ftpusers, then it is
           suggested that you read its documentation to find out how to block
           access for certain users.  Washington University FTP server Daemon
           (wuftpd) and Professional FTP Daemon (proftpd) are known to make
           use of ftpusers.

       Format
           The format of ftpusers is very simple.  There is one account name
           (or username) per line.  Lines starting with a # are ignored.

## [](#FILES)FILES

           /etc/ftpusers

## [](#SEE_ALSO)SEE ALSO

           passwd(5), proftpd(8), wuftpd(8)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08                    ftpusers(5)

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
