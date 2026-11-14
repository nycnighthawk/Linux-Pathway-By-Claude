---
{"title": "exportd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/exportd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# exportd(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION FILE](#CONFIGURATION_FILE) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nfsv4.exportd(8)         System Manager's Manual         nfsv4.exportd(8)

## [](#NAME)NAME

           nfsv4.exportd - NFSv4 Server Mount Daemon

## [](#SYNOPSIS)SYNOPSIS

           /usr/sbin/nfsv4.exportd [options]

## [](#DESCRIPTION)DESCRIPTION

           The nfsv4.exportd is used to manage NFSv4 exports.  The NFS server
           (nfsd) maintains a cache of authentication and authorization
           information which is used to identify the source of each request,
           and then what access permissions that source has to any local
           filesystem.  When required information is not found in the cache,
           the server sends a request to nfsv4.exportd to fill in the missing
           information.  nfsv4.exportd uses a table of information stored in
           /var/lib/nfs/etab and maintained by exportfs(8), possibly based on
           the contents of exports(5), to respond to each request.

## [](#OPTIONS)OPTIONS

           -d kind  or  --debug kind
                  Turn on debugging. Valid kinds are: all, auth, call,
                  general and parse.

           -l or --log-auth
                  Enable logging of responses to authentication and access
                  requests from nfsd.  Each response is then cached by the
                  kernel for 30 minutes (or as set by --ttl below), and will
                  be refreshed after 15 minutes (half the ttl time) if the
                  relevant client remains active.  Note that -l is equivalent
                  to -d auth and so can be enabled in /etc/nfs.conf with
                  "debug = auth" in the [exportd] section.

           -i or --cache-use-ipaddr
                  Normally each client IP address is matched against each
                  host identifier (name, wildcard, netgroup etc) found in
                  /etc/exports and a combined identity is formed from all
                  matching identifiers.  Often many clients will map to the
                  same combined identity so performing this mapping reduces
                  the number of distinct access details that the kernel needs
                  to store.  Specifying the -i option suppresses this mapping
                  so that access to each filesystem is requested and cached
                  separately for each client IP address.  Doing this can
                  increase the burden of updating the cache slightly, but can
                  make the log messages produced by the -l option easier to
                  read.

           -T  or  --ttl
                  Provide a time-to-live (TTL) for cached information given
                  to the kernel.  The kernel will normally request an update
                  if the information is needed after half of this time has
                  expired.  Increasing the provided number, which is in
                  seconds, reduces the rate of cache update requests, and
                  this is particularly noticeable when these requests are
                  logged with -l.  However increasing also means that changes
                  to hostname to address mappings can take longer to be
                  noticed.  The default TTL is 1800 (30 minutes).

           -F  or  --foreground
                  Run in foreground (do not daemonize)

           -h  or  --help
                  Display usage message.

           -t N or --num-threads=N or --num-threads N
                  This option specifies the number of worker threads that
                  nfsv4.exports spawns.  The default is 1 thread, which is
                  probably enough.  More threads are usually only needed for
                  NFS servers which need to handle mount storms of hundreds
                  of NFS mounts in a few seconds, or when your DNS server is
                  slow or unreliable.

           -g or --manage-gids
                  Accept requests from the kernel to map user id numbers into
                  lists of group id numbers for use in access control.  An
                  NFS request will normally (except when using Kerberos or
                  other cryptographic authentication) contain a user-id and a
                  list of group-ids.  Due to a limitation in the NFS
                  protocol, at most 16 groups ids can be listed.  If you use
                  the -g flag, then the list of group ids received from the
                  client will be replaced by a list of group ids determined
                  by an appropriate lookup on the server. Note that the
                  'primary' group id is not affected so a newgroup command on
                  the client will still be effective.  This function requires
                  a Linux Kernel with version at least 2.6.21.

           -L  or  --no-netlink
                  Disable the use of netlink for kernel communication and
                  force the use of the legacy /proc/net/rpc interfaces
                  instead.  This can be useful for debugging or working
                  around kernel netlink issues.

## [](#CONFIGURATION_FILE)CONFIGURATION FILE

           Many of the options that can be set on the command line can also
           be controlled through values set in the [exportd] or, in some
           cases, the [nfsd] sections of the /etc/nfs.conf configuration
           file.  Values recognized in the [exportd] section include
           cache-use-ipaddr , ttl, manage-gids, no-netlink, and debug which
           each have the same effect as the option with the same name.

## [](#FILES)FILES

           /etc/exports
                  input file for exportfs, listing exports, export options,
                  and access control lists

## [](#SEE_ALSO)SEE ALSO

           exportfs(8), exports(5), showmount(8), nfs.conf(5),
           firewall-cmd(1),

           RFC 7530 - "Network File System (NFS) Version 4 Protocol"
           RFC 8881 - "Network File System (NFS) Version 4 Minor Version 1
           Protocol"

## [](#COLOPHON)COLOPHON

           This page is part of the nfs-utils (NFS utilities) project.
           Information about the project can be found at 
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  If you have a bug
           report for this manual page, see
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.linux-nfs.org/projects/steved/nfs-utils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-23.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                   02 Feb 2021               nfsv4.exportd(8)

------------------------------------------------------------------------

Pages that refer to this page: [nfs.conf(5)](../man5/nfs.conf.5.html),  [exportfs(8)](../man8/exportfs.8.html)

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
