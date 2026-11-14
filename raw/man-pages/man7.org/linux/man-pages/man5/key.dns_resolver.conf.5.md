---
{"title": "key.dns_resolver.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/key.dns_resolver.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# key.dns_resolver.conf(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KEY.DNS...VER.CONF(5) Linux Key Management UtilitiesKEY.DNS...VER.CONF(5)

## [](#NAME)NAME

           key.dns_resolver.conf - Kernel DNS resolver config

## [](#DESCRIPTION)DESCRIPTION

           This file is used by the key.dns_resolver(5) program to set
           parameters.  Unless otherwise overridden with the -c flag, the
           program reads:

                  /etc/key.dns_resolver.conf

           Configuration options are given in key[=value] form, where value
           is optional.  If present, the value may be surrounded by a pair of
           single ('') or double quotes ("") which will be stripped off.  The
           special characters in the value may be escaped with a backslash to
           turn them into ordinary characters.

           Lines beginning with a '#' are considered comments and ignored.  A
           '#' symbol anywhere after the '=' makes the rest of the line into
           a comment unless the '#' is inside a quoted section or is escaped.

           Leading and trailing spaces and spaces around the '=' symbol will
           be stripped off.

           Available options include:

           default_ttl=<number>
                  The number of seconds to set as the expiration on a cached
                  record.  This will be overridden if the program manages to
                  retrieve TTL information along with the addresses (if, for
                  example, it accesses the DNS directly).  The default is 5
                  seconds.  The value must be in the range 1 to INT_MAX.

           The file can also include comments beginning with a '#' character
           unless otherwise suppressed by being inside a quoted value or
           being escaped with a backslash.

## [](#FILES)FILES

           /etc/key.dns_resolver.conf

## [](#SEE_ALSO)SEE ALSO

           key.dns_resolver(8)

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

    Linux                          18 May 2020          KEY.DNS...VER.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [key.dns_resolver(8)](../man8/key.dns_resolver.8.html)

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
