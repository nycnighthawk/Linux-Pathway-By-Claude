---
{"title": "host.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/host.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# host.conf(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    host.conf(5)               File Formats Manual               host.conf(5)

## [](#NAME)NAME

           host.conf - resolver configuration file

## [](#DESCRIPTION)DESCRIPTION

           The file /etc/host.conf contains configuration information
           specific to the resolver library.  It should contain one
           configuration keyword per line, followed by appropriate
           configuration information.  The following keywords are recognized:

           trim   This keyword may be listed more than once.  Each time it
                  should be followed by a list of domains, separated by
                  colons (':'), semicolons (';') or commas (','), with the
                  leading dot.  When set, the resolver library will
                  automatically trim the given domain name from the end of
                  any hostname resolved via DNS.  This is intended for use
                  with local hosts and domains.  (Related note: trim will not
                  affect hostnames gathered via NIS or the hosts(5) file.
                  Care should be taken to ensure that the first hostname for
                  each entry in the hosts file is fully qualified or
                  unqualified, as appropriate for the local installation.)

           multi  Valid values are on and off.  If set to on, the resolver
                  library will return all valid addresses for a host that
                  appears in the /etc/hosts file, instead of only the first.
                  This is off by default, as it may cause a substantial
                  performance loss at sites with large hosts files.

           reorder
                  Valid values are on and off.  If set to on, the resolver
                  library will attempt to reorder host addresses so that
                  local addresses (i.e., on the same subnet) are listed first
                  when a gethostbyname(3) is performed.  Reordering is done
                  for all lookup methods.  The default value is off.

## [](#ENVIRONMENT)ENVIRONMENT

           The following environment variables can be used to allow users to
           override the behavior which is configured in /etc/host.conf:

           RESOLV_HOST_CONF
                  If set, this variable points to a file that should be read
                  instead of /etc/host.conf.

           RESOLV_MULTI
                  Overrides the multi command.

           RESOLV_REORDER
                  Overrides the reorder command.

           RESOLV_ADD_TRIM_DOMAINS
                  A list of domains, separated by colons (':'), semicolons
                  (';'), or commas (','), with the leading dot, which will be
                  added to the list of domains that should be trimmed.

           RESOLV_OVERRIDE_TRIM_DOMAINS
                  A list of domains, separated by colons (':'), semicolons
                  (';'), or commas (','), with the leading dot, which will
                  replace the list of domains that should be trimmed.
                  Overrides the trim command.

## [](#FILES)FILES

           /etc/host.conf
                  Resolver configuration file

           /etc/resolv.conf
                  Resolver configuration file

           /etc/hosts
                  Local hosts database

## [](#NOTES)NOTES

           The following differences exist compared to the original
           implementation.  A new command spoof and a new environment
           variable RESOLV_SPOOF_CHECK can take arguments like off, nowarn,
           and warn.  Line comments can appear anywhere and not only at the
           beginning of a line.

       Historical
           The nsswitch.conf(5) file is the modern way of controlling the
           order of host lookups.

           In glibc 2.4 and earlier, the following keyword is recognized:

           order  This keyword specifies how host lookups are to be
                  performed.  It should be followed by one or more lookup
                  methods, separated by commas.  Valid methods are bind,
                  hosts, and nis.

           RESOLV_SERV_ORDER
                  Overrides the order command.

           Since glibc 2.0.7, and up through glibc 2.24, the following
           keywords and environment variable have been recognized but never
           implemented:

           nospoof
                  Valid values are on and off.  If set to on, the resolver
                  library will attempt to prevent hostname spoofing to
                  enhance the security of rlogin and rsh.  It works as
                  follows: after performing a host address lookup, the
                  resolver library will perform a hostname lookup for that
                  address.  If the two hostnames do not match, the query
                  fails.  The default value is off.

           spoofalert
                  Valid values are on and off.  If this option is set to on
                  and the nospoof option is also set, the resolver library
                  will log a warning of the error via the syslog facility.
                  The default value is off.

           spoof  Valid values are off, nowarn, and warn.  If this option is
                  set to off, spoofed addresses are permitted and no warnings
                  will be emitted via the syslog facility.  If this option is
                  set to warn, the resolver library will attempt to prevent
                  hostname spoofing to enhance the security and log a warning
                  of the error via the syslog facility.  If this option is
                  set to nowarn, the resolver library will attempt to prevent
                  hostname spoofing to enhance the security but not emit
                  warnings via the syslog facility.  Setting this option to
                  anything else is equal to setting it to nowarn.

           RESOLV_SPOOF_CHECK
                  Overrides the nospoof, spoofalert, and spoof commands in
                  the same way as the spoof command is parsed.  Valid values
                  are off, nowarn, and warn.

## [](#SEE_ALSO)SEE ALSO

           gethostbyname(3), hosts(5), nsswitch.conf(5), resolv.conf(5),
           hostname(7), named(8)

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

    Linux man-pages 6.19            2026-02-08                   host.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [gethostbyname(3)](../man3/gethostbyname.3.html),  [hosts(5)](../man5/hosts.5.html),  [resolv.conf(5)](../man5/resolv.conf.5.html)

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
