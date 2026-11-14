---
{"title": "atop-daily(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/atop-daily.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# atop-daily(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ATOP-DAILY(1)            General Commands Manual            ATOP-DAILY(1)

## [](#NAME)NAME

           atop-daily - daily maintenance of pcp-atop PCP archives

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/atop-daily [--compress-only] [--help] [LOGPATH]

## [](#DESCRIPTION)DESCRIPTION

           atop-daily performs daily maintenance of pcp-atop(1) PCP archives.
           It is normally called from systemd(1) via the atop-daily.timer
           unit, or automatically by pcp-atop(1) at startup.

           When run without options, atop-daily creates the archive directory
           if absent, compresses prior-day archives using xz(1) for metadata
           and zstd(1) for data volumes, and culls archives older than
           LOGGENERATIONS days (default 28).

           Compression is non-blocking: files are atomically renamed then
           compressed by background processes so the caller and pcp-atop(1)
           can proceed immediately.

## [](#OPTIONS)OPTIONS

           --compress-only
                  Compress prior-day archives only; do not cull old archives.
                  This mode is used when called from pcp-atop(1) itself at
                  startup.

           --help Display a usage message and exit.

## [](#CONFIGURATION)CONFIGURATION

           The following environment variables may be set in the pcp-atop(1)
           sysconfig file (/etc/sysconfig/atop or /etc/default/atop):

           LOGPATH
                  Archive directory.  Default: /var/log/atop.  May also be
                  specified as a command line argument.

           LOGGENERATIONS
                  Number of days of archives to retain.  Default: 28.  A
                  value of 0 disables culling.

## [](#FILES)FILES

           /var/log/atop
                  Default directory for pcp-atop(1) archive files.

## [](#SEE_ALSO)SEE ALSO

           pcp-atop(1), pcp-atopsar(1), PCPIntro(1), systemd(1), xz(1),
           zstd(1), pcp.conf(5) and pcp.env(5).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.
           Information about the project can be found at 
           ⟨http://www.pcp.io/⟩.  If you have a bug report for this manual
           page, send it to pcp@groups.io.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot               PCP                      ATOP-DAILY(1)

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
