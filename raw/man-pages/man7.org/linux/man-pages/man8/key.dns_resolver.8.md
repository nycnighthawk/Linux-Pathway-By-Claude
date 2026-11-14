---
{"title": "key.dns_resolver(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/key.dns_resolver.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# key.dns_resolver(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEY.DNS_RESOLVER(8)   Linux Key Management Utilities  KEY.DNS_RESOLVER(8)

## [](#NAME)NAME

           key.dns_resolver - upcall for request-key to handle dns_resolver
           keys

## [](#SYNOPSIS)SYNOPSIS

           /sbin/key.dns_resolver <key>
           /sbin/key.dns_resolver --dump-config [-c <configfile>]
           /sbin/key.dns_resolver -D [-v] [-v] [-c <configfile>] <desc>
           <calloutinfo>

## [](#DESCRIPTION)DESCRIPTION

           This program is invoked by request-key on behalf of the kernel
           when kernel services (such as NFS, CIFS and AFS) want to perform a
           hostname lookup and the kernel does not have the key cached.  It
           is not ordinarily intended to be called directly.

           There program has internal parameters that can be changed with a
           configuration file (see key.dns_resolver.conf(5) for more
           information).  The default configuration file is in /etc, but this
           can be overridden with the -c flag.

           The program can be called in debugging mode to test its
           functionality by passing a -D or --debug flag on the command line.
           For this to work, the key description and the callout information
           must be supplied.  Verbosity can be increased by supplying one or
           more -v flags.

           The program may also be called with --dump-config to show the
           values that configurable parameters will have after parsing the
           config file.

## [](#ERRORS)ERRORS

           All errors will be logged to the syslog.

## [](#SEE_ALSO)SEE ALSO

           key.dns_resolver.conf(5), request-key.conf(5), keyrings(7),
           request-key(8)

## [](#COLOPHON)COLOPHON

           This page is part of the keyutils (key management utilities)
           project.  Information about the project can be found at [unknown
           -- if you know, please contact man-pages@man7.org] If you have a
           bug report for this manual page, send it to
           keyrings@linux-nfs.org.  This page was obtained from the project's
           upstream Git repository
           ⟨http://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2023-03-20.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Linux                          18 May 2020            KEY.DNS_RESOLVER(8)

------------------------------------------------------------------------

Pages that refer to this page: [key.dns_resolver.conf(5)](../man5/key.dns_resolver.conf.5.html),  [cifs.upcall(8)](../man8/cifs.upcall.8.html)

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
