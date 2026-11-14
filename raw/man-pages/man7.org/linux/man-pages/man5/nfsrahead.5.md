---
{"title": "nfsrahead(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/nfsrahead.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nfsrahead(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [EXAMPLE CONFIGURATION](#EXAMPLE_CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    man(5)                      nfsrahead man page                     man(5)

## [](#NAME)NAME

           nfsrahead - Configure the readahead for NFS mounts

## [](#SYNOPSIS)SYNOPSIS

           nfsrahead [-F] [-d] <device>

## [](#DESCRIPTION)DESCRIPTION

           nfsrahead is a tool intended to be used with udev to set the
           read_ahead_kb parameter of NFS mounts, according to the
           configuration file (see CONFIGURATION). device is the device
           number for the NFS backing device as provided by the kernel.

## [](#OPTIONS)OPTIONS

           -F     Send messages to stderr instead of syslog

           -d     Increase the debugging level.

## [](#CONFIGURATION)CONFIGURATION

           nfsrahead is configured in /etc/nfs.conf, in the section titled
           nfsrahead.  It accepts the following configurations.

           nfs=<value>
                  The readahead value applied to NFSv3 mounts.

           nfs4=<value>
                  The readahead value applied to NFSv4 mounts.

           default=<value>
                  The default configuration when none of the configurations
                  above is set.

## [](#EXAMPLE_CONFIGURATION)EXAMPLE CONFIGURATION

           [nfsrahead]
           nfs=15000              # readahead of 15000 for NFSv3 mounts
           nfs4=16000             # readahead of 16000 for NFSv4 mounts
           default=128            # default is 128

## [](#SEE_ALSO)SEE ALSO

           mount.nfs(8), nfs(5), nfs.conf(5), udev(7), bcc-readahead(8)

## [](#BUGS)BUGS

           No known bugs.

## [](#AUTHOR)AUTHOR

           Thiago Rafael Becker <trbecker@gmail.com>

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

    1.0                            08 Mar 2022                         man(5)

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
