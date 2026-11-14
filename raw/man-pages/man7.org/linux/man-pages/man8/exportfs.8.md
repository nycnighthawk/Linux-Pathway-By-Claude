---
{"title": "exportfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/exportfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# exportfs(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION FILE](#CONFIGURATION_FILE) \| [DISCUSSION](#DISCUSSION) \| [EXAMPLES](#EXAMPLES) \| [USAGE NOTES](#USAGE_NOTES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    exportfs(8)              System Manager's Manual              exportfs(8)

## [](#NAME)NAME

           exportfs - maintain table of exported NFS file systems

## [](#SYNOPSIS)SYNOPSIS

           /usr/sbin/exportfs [-avi] [-o options,..] [client:/path ..]
           /usr/sbin/exportfs -r [-v]
           /usr/sbin/exportfs [-av] -u [client:/path ..]
           /usr/sbin/exportfs [-v]
           /usr/sbin/exportfs -f
           /usr/sbin/exportfs -s

## [](#DESCRIPTION)DESCRIPTION

           An NFS server maintains a table of local physical file systems
           that are accessible to NFS clients.  Each file system in this
           table is  referred to as an exported file system, or export, for
           short.

           The exportfs command maintains the current table of exports for
           the NFS server.  The master export table is kept in a file named
           /var/lib/nfs/etab.  This file is read by rpc.mountd when a client
           sends an NFS MOUNT request.

           Normally the master export table is initialized with the contents
           of /etc/exports and files under /etc/exports.d by invoking
           exportfs -a.  However, a system administrator can choose to add or
           delete exports without modifying /etc/exports or files under
           /etc/exports.d by using the exportfs command.

           exportfs does not communicate with the kernel directly.  It writes
           export information to /var/lib/nfs/etab and relies on its partner
           programs rpc.mountd and nfsv4.exportd to manage kernel
           communication.  These daemons work in one of two modes: a netlink
           mode and a /proc mode.

           In the netlink mode, available on sufficiently recent kernels,
           rpc.mountd (or nfsv4.exportd) communicates with the kernel via
           generic netlink sockets.  The kernel sends multicast notifications
           when cache entries need to be resolved, and the daemon responds
           with the appropriate export information.  Cache flushing (via
           exportfs -f) is also performed over netlink.  This mode can be
           disabled with the -L option.

           In the /proc mode, used when netlink is unavailable, rpc.mountd
           manages kernel requests for information about exports via the
           /proc/net/rpc channel files.

## [](#OPTIONS)OPTIONS

           -d kind  or  --debug kind
                  Turn on debugging. Valid kinds are: all, auth, call,
                  general and parse.  Debugging can also be turned on by
                  setting debug= in the [exportfs] section of /etc/nfs.conf.

           -a     Export or unexport all directories.

           -o options,...
                  Specify a list of export options in the same manner as in
                  exports(5).

           -i     Ignore the /etc/exports file and files under /etc/exports.d
                  directory.  Only default options and options given on the
                  command line are used.

           -r     Reexport all directories, synchronizing /var/lib/nfs/etab
                  with /etc/exports and files under /etc/exports.d.  This
                  option removes entries in /var/lib/nfs/etab which have been
                  deleted from /etc/exports or files under /etc/exports.d,
                  and removes any entries from the kernel export table which
                  are no longer valid.

           -u     Unexport one or more directories.

           -f     If /proc/fs/nfsd or /proc/fs/nfs is mounted, flush
                  everything out of the kernel's export table.  Fresh entries
                  for active clients are added to the kernel's export table
                  by rpc.mountd when they make their next NFS mount request.

           -v     Be verbose. When exporting or unexporting, show what's
                  going on. When displaying the current export list, also
                  display the list of export options.

           -s     Display the current export list suitable for /etc/exports.

           -L     Disable the use of netlink for kernel communication and
                  force the use of the legacy /proc interfaces for cache
                  flushing and export validation.

## [](#CONFIGURATION_FILE)CONFIGURATION FILE

           The [exportfs] section of the /etc/nfs.conf configuration file can
           contain a debug value, which can be one or more from the list
           general, call, auth, parse, all.  When a list is given, the
           members should be comma-separated.

           exportfs will also recognize the state-directory-path and
           no-netlink values from both the [mountd] section and the [exportd]
           section.  When no-netlink is set, exportfs will skip the netlink
           probe and use the legacy /proc interfaces for cache flushing and
           export validation

## [](#DISCUSSION)DISCUSSION

       Exporting Directories
           The first synopsis shows how to invoke exportfs when adding new
           entries to the export table.  When using exportfs -a, all exports
           listed in /etc/exports and files under /etc/exports.d are added to
           /var/lib/nfs/etab.  The kernel's export table is also updated as
           needed.

           The host:/path argument specifies a local directory to export,
           along with the client or clients who are permitted to access it.
           See exports(5) for a description of supported options and access
           list formats.

           IPv6 presentation addresses contain colons, which are already used
           to separate the "host" and "path" command line arguments.  When
           specifying a client using a raw IPv6 address, enclose the address
           in square brackets.  For IPv6 network addresses, place the prefix
           just after the closing bracket.

           To export a directory to the world, simply specify :/path.

           The export options for a particular host/directory pair derive
           from several sources.  The default export options are
           sync,ro,root_squash,wdelay.  These can be overridden by entries in
           /etc/exports or files under /etc/exports.d.

           A system administrator may override options from these sources
           using the -o command-line option on exportfs.  This option takes a
           comma-separated list of options in the same fashion as one would
           specify them in /etc/exports.  In this way exportfs can be used to
           modify the export options of an already exported directory.

       Unexporting Directories
           The third synopsis shows how to unexport a currently exported
           directory.  When using exportfs -ua, all entries listed in
           /var/lib/nfs/etab are removed from the kernel export tables, and
           the file is cleared. This effectively shuts down all NFS activity.

           To remove an export, specify a host:/path pair. This deletes the
           specified entry from /var/lib/nfs/etab and removes the
           corresponding kernel entry (if any).

           When the last client for a given export path is unexported,
           exportfs signals the kernel to revoke NFSv4 state (opens, locks,
           and delegations) and release cached state for that path.  Without
           this revocation, retained state would prevent the underlying
           filesystem from being unmounted.  Affected clients receive
           NFS4ERR_ADMIN_REVOKED errors for operations that use revoked
           state.

           exportfs -ua does not revoke NFSv4 state, however.  If nfsd is
           then restarted, clients may reclaim state during the grace period.

       Dumping the Export Table
           Invoking exportfs without options shows the current list of
           exported file systems.  Adding the -v option causes exportfs to
           display the export options for each export.

## [](#EXAMPLES)EXAMPLES

           The following adds all directories listed in /etc/exports and
           files under /etc/exports.d to /var/lib/nfs/etab and pushes the
           resulting export entries into the kernel:

           # exportfs -a

           To export the /usr/tmp directory to host django, allowing insecure
           file locking requests from clients:

           # exportfs -o insecure_locks django:/usr/tmp

           To unexport the /usr/tmp directory:

           # exportfs -u django:/usr/tmp

           To unexport all exports listed in /etc/exports and files under
           /etc/exports.d:

           # exportfs -au

           To export the /usr/tmp directory to IPv6 link-local clients:

           # exportfs [fe80::]/64:/usr/tmp

## [](#USAGE_NOTES)USAGE NOTES

           Exporting to IP networks or DNS and NIS domains does not enable
           clients from these groups to access NFS immediately.  Rather,
           these sorts of exports are hints to rpc.mountd(8) to grant any
           mount requests from these clients.  This is usually not a problem,
           because any existing mounts are preserved in rmtab across reboots.

           When unexporting a network or domain entry, any current exports to
           members of this group will be checked against the remaining valid
           exports and if they themselves are no longer valid they will be
           removed.

## [](#FILES)FILES

           /etc/exports
                  input file listing exports, export options, and access
                  control lists

           /etc/exports.d
                  directory where extra input files are stored.  Note: only
                  files that end with .exports are used.

           /var/lib/nfs/etab
                  master table of exports

           /var/lib/nfs/rmtab
                  table of clients accessing server's exports

## [](#SEE_ALSO)SEE ALSO

           exports(5), nfs.conf(5), rpc.mountd(8), exportd(8), netgroup(5)

## [](#AUTHORS)AUTHORS

           Olaf Kirch <okir@monad.swb.de>
           Neil Brown <neilb@cse.unsw.edu.au>

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

                                30 September 2013                 exportfs(8)

------------------------------------------------------------------------

Pages that refer to this page: [exports(5)](../man5/exports.5.html),  [nfs.conf(5)](../man5/nfs.conf.5.html),  [nfsd(7)](../man7/nfsd.7.html),  [exportd(8)](../man8/exportd.8.html),  [mountd(8)](../man8/mountd.8.html),  [nfsconf(8)](../man8/nfsconf.8.html),  [nfsd(8)](../man8/nfsd.8.html),  [nfsdclnts(8)](../man8/nfsdclnts.8.html)

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
