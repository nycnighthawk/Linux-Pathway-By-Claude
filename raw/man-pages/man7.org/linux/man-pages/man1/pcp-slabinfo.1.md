---
{"title": "pcp-slabinfo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-slabinfo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-slabinfo(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-SLABINFO(1)          General Commands Manual          PCP-SLABINFO(1)

## [](#NAME)NAME

           pcp-slabinfo - Report statistics for kernel slab allocator

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] slabinfo [-a archive] [-s samples] [-Z timezone]

## [](#DESCRIPTION)DESCRIPTION

           The pcp-slabinfo command is used for viewing different stats
           related to slab.  It helps users analyze useful information
           related to the slab allocator.  The information includes the total
           number of objects that are currently active, allocated objects,
           pages per slab, etc.  By default, pcp-slabinfo reports live data
           for the local host.

           The statistics shown are as follows:
           HEADER         DESCRIPTION
           ───────────────────────────────────────────────────────────────────
           active_objs    The number of objects that are currently active
                          (i.e., in use)
           num_objs       The total number of allocated objects (i.e. objects
                          that are both in use and not in use).
           objsize        The size of objects in this slab, in bytes.
           objperslab     The number of objects stored in each slab.
           pagesperslab   The number of pages allocated for each slab
           active_slabs   The number of active slabs.
           num_slabs      The total number of slabs.

## [](#OPTIONS)OPTIONS

           -a file, --archive=file
                  Fetch /proc/slabinfo for a specified archive file

           -s count, --samples=count
                  Get the slabinfo statistics for specified number of samples
                  count

           -V, --version
                  Display version number and exit.

           -z, --hostzone
                  Use the local timezone of the host that is the source of
                  the performance metrics, as identified by either the -h or
                  the -a options.  The default is to use the timezone of the
                  local host.

           -Z timezone, --timezone=timezone
                  Use timezone for the date and time.  Timezone is in the
                  format of the environment variable TZ as described in
                  environ(7).

           -?, --help
                  Display usage message and exit.

## [](#NOTES)NOTES

           pcp-slabinfo collects information from /proc/slabinfo.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP. On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables. The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), pmParseInterval(3), environ(7).

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

    Performance Co-Pilot               PCP                    PCP-SLABINFO(1)

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
