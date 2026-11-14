---
{"title": "blkmapd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/blkmapd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# blkmapd(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION FILE](#CONFIGURATION_FILE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    blkmapd(8)               System Manager's Manual               blkmapd(8)

## [](#NAME)NAME

           blkmapd - pNFS block layout mapping daemon

## [](#SYNOPSIS)SYNOPSIS

           blkmapd [-h] [-d] [-f]

## [](#DESCRIPTION)DESCRIPTION

           The blkmapd daemon performs device discovery and mapping for the
           parallel NFS (pNFS) block layout client [RFC5663].

           The pNFS block layout protocol builds a complex storage hierarchy
           from a set of simple volumes.  These simple volumes are addressed
           by content, using a signature on the volume to uniquely name each
           one.  The daemon locates a volume by examining each block device
           in the system for the given signature.

           The topology typically consists of a hierarchy of volumes built by
           striping, slicing, and concatenating the simple volumes.  The
           blkmapd daemon uses the device-mapper driver to construct logical
           devices that reflect the server topology, and passes these devices
           to the kernel for use by the pNFS block layout client.

## [](#OPTIONS)OPTIONS

           -h     Display usage message.

           -d     Performs device discovery only then exits.

           -f     Runs blkmapd in the foreground and sends output to stderr
                  (as opposed to syslogd)

## [](#CONFIGURATION_FILE)CONFIGURATION FILE

           The blkmapd daemon recognizes the following value from the
           [general] section of the /etc/nfs.conf configuration file:

           pipefs-directory
                  Tells blkmapd where to look for the rpc_pipefs filesystem.
                  The default value is /var/lib/nfs/rpc_pipefs.

## [](#SEE_ALSO)SEE ALSO

           nfs(5), dmsetup(8), nfs.conf(5)

           RFC 5661 for the NFS version 4.1 specification.
           RFC 5663 for the pNFS block layout specification.

## [](#AUTHORS)AUTHORS

           Haiying Tang <Tang_Haiying@emc.com>
           Jim Rees <rees@umich.edu>

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

                                  11 August 2011                   blkmapd(8)

------------------------------------------------------------------------

Pages that refer to this page: [nfs.conf(5)](../man5/nfs.conf.5.html)

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
