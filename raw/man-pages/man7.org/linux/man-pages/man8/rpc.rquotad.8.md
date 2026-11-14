---
{"title": "rpc.rquotad(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpc.rquotad.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpc.rquotad(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RQUOTAD(8)               System Manager's Manual               RQUOTAD(8)

## [](#NAME)NAME

           rpc.rquotad - remote quota server

## [](#SYNOPSIS)SYNOPSIS

           /usr/sbin/rpc.rquotad [ -FI ] [ -p port ] [ -s | -S ] [ -x path ]

           /usr/sbin/rpc.rquotad [ -h | -V ]

## [](#DESCRIPTION)DESCRIPTION

           rpc.rquotad is an rpc(3) server which returns quotas for a user of
           a local filesystem which is mounted by a remote machine over the
           NFS.  It also allows setting of quotas on NFS mounted filesystem
           (if configured during compilation and allowed by a command line
           option -S).  The results are used by quota(1) to display user
           quotas for remote filesystems and by edquota(8) to set quotas on
           remote filesystems.  rquotad daemon uses tcp-wrappers library
           (under service name rquotad) which allows you to specify hosts
           allowed/disallowed to use the daemon (see hosts.allow(5) manpage
           for more information). The rquotad daemon is normally started at
           boot time from the system startup scripts.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Show program usage and exit.  -V, --version Show version of
                  quota tools.

           -s, --no-setquota
                  Don't allow setting of quotas (default). This option is
                  available only if utilities were compiled with the
                  rpcsetquota option.

           -S, --setquota
                  Allow setting of quotas. This option is available only if
                  utilities were compiled with the rpcsetquota option.

           -F, --foreground
                  Run daemon in foreground (may be useful for debugging
                  purposes).

           -I, --autofs
                  Do not ignore autofs mountpoints.

           -p port, --port port
                  Listen on alternate port port.

           -x path, --xtab path
                  Set an alternative file with NFSD export table. This file
                  is used to determine pseudoroot of NFSv4 exports. The
                  pseudoroot is then prepended to each relative path (i.e. a
                  path not beginning by '/') received in a quota RPC request.

## [](#FILES)FILES

           aquota.user or aquota.group
                  quota file at the filesystem root (version 2 quota, non-XFS
                  filesystems)
           quota.user or quota.group
                  quota file at the filesystem root (version 1 quota, non-XFS
                  filesystems)
           /etc/mtab
                  default filesystems

## [](#SEE_ALSO)SEE ALSO

           quota(1), rpc(3), nfs(5), services(5), inetd(8)

## [](#COLOPHON)COLOPHON

           This page is part of the quota (Linux Diskquota Tools) project.
           Information about the project can be found at [unknown -- if you
           know, please contact man-pages@man7.org] It is not known how to
           report bugs for this man page; if you know, please send a mail to
           man-pages@man7.org.  This page was obtained from the project's
           upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/quota/quota-tools.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2025-12-11.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                                                   RQUOTAD(8)

------------------------------------------------------------------------

Pages that refer to this page: [mountd(8)](../man8/mountd.8.html),  [nfsd(8)](../man8/nfsd.8.html)

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
