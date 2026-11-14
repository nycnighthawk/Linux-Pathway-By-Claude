---
{"title": "nscd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/nscd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nscd(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nscd(8)                  System Manager's Manual                  nscd(8)

## [](#NAME)NAME

           nscd - name service cache daemon

## [](#DESCRIPTION)DESCRIPTION

           nscd is a daemon that provides a cache for the most common name
           service requests.  The default configuration file, /etc/nscd.conf,
           determines the behavior of the cache daemon.  See nscd.conf(5).

           nscd provides caching for accesses of the passwd(5), group(5),
           hosts(5) services(5) and netgroup databases through standard libc
           interfaces, such as getpwnam(3), getpwuid(3), getgrnam(3),
           getgrgid(3), gethostbyname(3), and others.

           There are two caches for each database: a positive one for items
           found, and a negative one for items not found.  Each cache has a
           separate TTL (time-to-live) period for its data.  Note that the
           shadow file is specifically not cached.  getspnam(3) calls remain
           uncached as a result.

## [](#OPTIONS)OPTIONS

           --help will give you a list with all options and what they do.

## [](#NOTES)NOTES

           The daemon will try to watch for changes in configuration files
           appropriate for each database (e.g., /etc/passwd for the passwd
           database or /etc/hosts and /etc/resolv.conf for the hosts
           database), and flush the cache when these are changed.  However,
           this will happen only after a short delay (unless the inotify(7)
           mechanism is available and glibc 2.9 or later is available), and
           this auto-detection does not cover configuration files required by
           nonstandard NSS modules, if any are specified in
           /etc/nsswitch.conf.  In that case, you need to run the following
           command after changing the configuration file of the database so
           that nscd invalidates its cache:

               $ nscd -i <database>

## [](#SEE_ALSO)SEE ALSO

           nscd.conf(5), nsswitch.conf(5)

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

    Linux man-pages 6.19            2026-02-08                        nscd(8)

------------------------------------------------------------------------

Pages that refer to this page: [nscd.conf(5)](../man5/nscd.conf.5.html)

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
