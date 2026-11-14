---
{"title": "nss(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/nss.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nss(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nss(5)                     File Formats Manual                     nss(5)

## [](#NAME)NAME

           nss - Name Service Switch configuration file

## [](#DESCRIPTION)DESCRIPTION

           Each call to a function which retrieves data from a system
           database like the password or group database is handled by the
           Name Service Switch implementation in the GNU C library.  The
           various services provided are implemented by independent modules,
           each of which naturally varies widely from the other.

           The default implementations coming with the GNU C library are by
           default conservative and do not use unsafe data.  This might be
           very costly in some situations, especially when the databases are
           large.  Some modules allow the system administrator to request
           taking shortcuts if these are known to be safe.  It is then the
           system administrator's responsibility to ensure the assumption is
           correct.

           There are other modules where the implementation changed over
           time.  If an implementation used to sacrifice speed for memory
           consumption, it might create problems if the preference is
           switched.

           The /etc/default/nss file contains a number of variable
           assignments.  Each variable controls the behavior of one or more
           NSS modules.  White spaces are ignored.  Lines beginning with '#'
           are treated as comments.

           The variables currently recognized are:

           NETID_AUTHORITATIVE = TRUE|FALSE
                  If set to TRUE, the NIS backend for the initgroups(3)
                  function will accept the information from the netid.byname
                  NIS map as authoritative.  This can speed up the function
                  significantly if the group.byname map is large.  The
                  content of the netid.byname map is used as is.  The system
                  administrator has to make sure it is correctly generated.

           SERVICES_AUTHORITATIVE = TRUE|FALSE
                  If set to TRUE, the NIS backend for the getservbyname(3)
                  and getservbyname_r(3) functions will assume that the
                  services.byservicename NIS map exists and is authoritative,
                  particularly that it contains both keys with /proto and
                  without /proto for both primary service names and service
                  aliases.  The system administrator has to make sure it is
                  correctly generated.

           SETENT_BATCH_READ = TRUE|FALSE
                  If set to TRUE, the NIS backend for the setpwent(3) and
                  setgrent(3) functions will read the entire database at once
                  and then hand out the requests one by one from memory with
                  every corresponding getpwent(3) or getgrent(3) call
                  respectively.  Otherwise, each getpwent(3) or getgrent(3)
                  call might result in a network communication with the
                  server to get the next entry.

## [](#FILES)FILES

           /etc/default/nss

## [](#EXAMPLES)EXAMPLES

           The default configuration corresponds to the following
           configuration file:

               NETID_AUTHORITATIVE=FALSE
               SERVICES_AUTHORITATIVE=FALSE
               SETENT_BATCH_READ=FALSE

## [](#SEE_ALSO)SEE ALSO

           nsswitch.conf(5)

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

    Linux man-pages 6.19            2026-02-08                         nss(5)

------------------------------------------------------------------------

Pages that refer to this page: [nsswitch.conf(5)](../man5/nsswitch.conf.5.html),  [systemd-resolved.service(8)](../man8/systemd-resolved.service.8.html)

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
