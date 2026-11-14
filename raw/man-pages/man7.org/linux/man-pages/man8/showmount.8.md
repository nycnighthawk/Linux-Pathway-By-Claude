---
{"title": "showmount(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/showmount.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# showmount(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SHOWMOUNT(8)             System Manager's Manual             SHOWMOUNT(8)

## [](#NAME)NAME

           showmount - show mount information for an NFS server

## [](#SYNOPSIS)SYNOPSIS

           showmount [ -adehv ] [ --all ] [ --directories ] [ --exports ]
           [ --help ] [ --version ] [ host ]

## [](#DESCRIPTION)DESCRIPTION

           showmount queries the mount daemon on a remote host for
           information about the state of the NFS server on that machine.
           With no options showmount lists the set of clients who are
           mounting from that host.  The output from showmount is designed to
           appear as though it were processed through ``sort -u''.

## [](#OPTIONS)OPTIONS

           -a or --all
                  List both the client hostname or IP address and mounted
                  directory in host:dir format. This info should not be
                  considered reliable. See the notes on rmtab in
                  rpc.mountd(8).

           -d or --directories
                  List only the directories mounted by some client.

           -e or --exports
                  Show the NFS server's export list.

           -h or --help
                  Provide a short help summary.

           -v or --version
                  Report the current version number of the program.

           --no-headers
                  Suppress the descriptive headings from the output.

## [](#SEE_ALSO)SEE ALSO

           rpc.mountd(8), rpc.nfsd(8)

## [](#BUGS)BUGS

           The completeness and accuracy of the information that showmount
           displays varies according to the NFS server's implementation.

           Because showmount sorts and uniqs the output, it is impossible to
           determine from the output whether a client is mounting the same
           directory more than once.

           showmount works by contacting the server's MNT service directly.
           NFSv4-only servers have no need to advertise their exported root
           filehandles via this method, and may not expose their MNT service
           to clients.

## [](#AUTHOR)AUTHOR

           Rick Sladkey <jrs@world.std.com>

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

                                  6 October 1993                 SHOWMOUNT(8)

------------------------------------------------------------------------

Pages that refer to this page: [exports(5)](../man5/exports.5.html),  [exportd(8)](../man8/exportd.8.html),  [mountd(8)](../man8/mountd.8.html)

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
