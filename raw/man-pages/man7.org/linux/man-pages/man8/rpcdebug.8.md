---
{"title": "rpcdebug(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpcdebug.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpcdebug(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    rpcdebug(8)              System Manager's Manual              rpcdebug(8)

## [](#NAME)NAME

           rpcdebug - set and clear NFS and RPC kernel debug flags

## [](#SYNOPSIS)SYNOPSIS

           rpcdebug -vh
           rpcdebug -m module
           rpcdebug -m module -s flags...
           rpcdebug -m module -c flags...

## [](#DESCRIPTION)DESCRIPTION

           The rpcdebug command allows an administrator to set and clear the
           Linux kernel's NFS client and server debug flags.  Setting these
           flags causes the kernel to emit messages to the system log in
           response to NFS activity; this is typically useful when debugging
           NFS problems.

           The first form in the synopsis can be used to list all available
           debug flags.  The second form shows the currently set debug flags
           for the given module.  The third form sets one or more flags, and
           the fourth form clears one or more flags.

           The value all may be used to set or clear all the flags for the
           given module.

## [](#OPTIONS)OPTIONS

           -c     Clear the given debug flags.

           -h     Print a help message and exit.  When combined with the -v
                  option, also prints the available debug flags.

           -m module
                  Specify which module's flags to set or clear.  Available
                  modules are:

                  nfsd   The NFS server.

                  nfs    The NFS client.

                  nlm    The Network Lock Manager, in either an NFS client or
                         server.

                  rpc    The Remote Procedure Call module, in either an NFS
                         client or server.

           -s     Set the given debug flags.

           -v     Increase the verbosity of rpcdebug's output.

## [](#FILES)FILES

           /proc/sys/sunrpc/{rpc,nfs,nfsd,nlm}_debug
                  procfs-based interface to kernel debug flags.

## [](#SEE_ALSO)SEE ALSO

           rpc.nfsd(8), nfs(5), syslogd(8).

## [](#BUGS)BUGS

           Bugs can be found or reported at http://nfs.sf.net/ .

## [](#AUTHOR)AUTHOR

           Program by Olaf Kirch <okir@suse.de> and
           <frederic.jolly@bull.ext.net>.  Manpage by Greg Banks
           <gnb@melbourne.sgi.com>.

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

                                    5 Jul 2006                    rpcdebug(8)

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
