---
{"title": "nscd.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/nscd.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nscd.conf(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nscd.conf(5)               File Formats Manual               nscd.conf(5)

## [](#NAME)NAME

           nscd.conf - name service cache daemon configuration file

## [](#DESCRIPTION)DESCRIPTION

           The file /etc/nscd.conf is read from nscd(8) at startup.  Each
           line specifies either an attribute and a value, or an attribute,
           service, and a value.  Fields are separated either by SPACE or TAB
           characters.  A '#' (number sign) indicates the beginning of a
           comment; following characters, up to the end of the line, are not
           interpreted by nscd.

           Valid services are passwd, group, hosts, services, or netgroup.

           logfile debug-file-name
                  Specifies name of the file to which debug info should be
                  written.

           debug-level value
                  Sets the desired debug level.  0 hides debug info.  1 shows
                  general debug info.  2 additionally shows data in cache
                  dumps.  3 (and above) shows all debug info.  The default is
                  0.

           threads number
                  This is the initial number of threads that are started to
                  wait for requests.  At least five threads will always be
                  created.  The number of threads may increase dynamically up
                  to max-threads in response to demand from clients, but
                  never decreases.

           max-threads number
                  Specifies the maximum number of threads.  The default is
                  32.

           server-user user
                  If this option is set, nscd will run as this user and not
                  as root.  If a separate cache for every user is used (-S
                  parameter), this option is ignored.

           stat-user user
                  Specifies the user who is allowed to request statistics.

           reload-count unlimited | number
                  Sets a limit on the number of times a cached entry gets
                  reloaded without being used before it gets removed.  The
                  limit can take values ranging from 0 to 254; values 255 or
                  higher behave the same as unlimited.  Limit values can be
                  specified in either decimal or hexadecimal with a "0x"
                  prefix.  The special value unlimited is case-insensitive.
                  The default limit is 5.  A limit of 0 turns off the
                  reloading feature.  See NOTES below for further discussion
                  of reloading.

           paranoia <yes|no>
                  Enabling paranoia mode causes nscd to restart itself
                  periodically.  The default is no.

           restart-interval time
                  Sets the restart interval to time seconds if periodic
                  restart is enabled by enabling paranoia mode.  The default
                  is 3600.

           enable-cache service <yes|no>
                  Enables or disables the specified service cache.  The
                  default is no.

           positive-time-to-live service value
                  Sets the TTL (time-to-live) for positive entries
                  (successful queries) in the specified cache for service.
                  Value is in seconds.  Larger values increase cache hit
                  rates and reduce mean response times, but increase problems
                  with cache coherence.  Note that for some name services
                  (including specifically DNS) the TTL returned from the name
                  service is used and this attribute is ignored.

           negative-time-to-live service value
                  Sets the TTL (time-to-live) for negative entries
                  (unsuccessful queries) in the specified cache for service.
                  Value is in seconds.  Can result in significant performance
                  improvements if there are several files owned by UIDs (user
                  IDs) not in system databases (for example, untarring the
                  Linux kernel sources as root); should be kept small to
                  reduce cache coherency problems.

           suggested-size service value
                  This is the internal hash table size, value should remain a
                  prime number for optimum efficiency.  The default is 211.

           check-files service <yes|no>
                  Enables or disables checking the file belonging to the
                  specified service for changes.  The files are /etc/passwd,
                  /etc/group, /etc/hosts, /etc/resolv.conf, /etc/services,
                  and /etc/netgroup.  The default is yes.

           persistent service <yes|no>
                  Keep the content of the cache for service over server
                  restarts; useful when paranoia mode is set.  The default is
                  no.

           shared service <yes|no>
                  The memory mapping of the nscd databases for service is
                  shared with the clients so that they can directly search in
                  them instead of having to ask the daemon over the socket
                  each time a lookup is performed.  The default is no.  Note
                  that a cache miss will still result in asking the daemon
                  over the socket.

           max-db-size service bytes
                  The maximum allowable size, in bytes, of the database files
                  for the service.  The default is 33554432.

           auto-propagate service <yes|no>
                  When set to no for passwd or group service, then the
                  .byname requests are not added to passwd.byuid or
                  group.bygid cache.  This can help with tables containing
                  multiple records for the same ID.  The default is yes.
                  This option is valid only for services passwd and group.

## [](#NOTES)NOTES

           The default values stated in this manual page originate from the
           source code of nscd(8) and are used if not overridden in the
           configuration file.  The default values used in the configuration
           file of your distribution might differ.

       Reloading
           nscd(8) has a feature called reloading, whose behavior can be
           surprising.

           Reloading is enabled when the reload-count attribute has a non-
           zero value.  The default value in the source code enables
           reloading, although your distribution may differ.

           When reloading is enabled, positive cached entries (the results of
           successful queries) do not simply expire when their TTL is up.
           Instead, at the expiry time, nscd will "reload", i.e., re-issue to
           the name service the same query that created the cached entry, to
           get a new value to cache.  Depending on /etc/nsswitch.conf this
           may mean that a DNS, LDAP, or NIS request is made.  If the new
           query is successful, reloading will repeat when the new value
           would expire, until reload-count reloads have happened for the
           entry, and only then will it actually be removed from the cache.
           A request from a client which hits the entry will reset the reload
           counter on the entry.  Purging the cache using nscd -i overrides
           the reload logic and removes the entry.

           Reloading has the effect of extending cache entry TTLs without
           compromising on cache coherency, at the cost of additional load on
           the backing name service.  Whether this is a good idea on your
           system depends on details of your applications' behavior, your
           name service, and the effective TTL values of your cache entries.
           Note that for some name services (for example, DNS), the effective
           TTL is the value returned from the name service and not the value
           of the positive-time-to-live attribute.

           Please consider the following advice carefully:

           •  If your application will make a second request for the same
              name, after more than 1 TTL but before reload-count TTLs, and
              is sensitive to the latency of a cache miss, then reloading may
              be a good idea for you.

           •  If your name service is configured to return very short TTLs,
              and your applications only make requests rarely under normal
              circumstances, then reloading may result in additional load on
              your backing name service without any benefit to applications,
              which is probably a bad idea for you.

           •  If your name service capacity is limited, reloading may have
              the surprising effect of increasing load on your name service
              instead of reducing it, and may be a bad idea for you.

           •  Setting reload-count to unlimited is almost never a good idea,
              as it will result in a cache that never expires entries and
              puts never-ending additional load on the backing name service.

           Some distributions have an init script for nscd(8) with a reload
           command which uses nscd -i to purge the cache.  That use of the
           word "reload" is entirely different from the "reloading" described
           here.

## [](#SEE_ALSO)SEE ALSO

           nscd(8)

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

    Linux man-pages 6.19            2026-02-08                   nscd.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [nscd(8)](../man8/nscd.8.html)

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
