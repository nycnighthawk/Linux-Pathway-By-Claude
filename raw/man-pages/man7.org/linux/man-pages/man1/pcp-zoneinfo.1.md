---
{"title": "pcp-zoneinfo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pcp-zoneinfo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-zoneinfo(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-ZONEINFO(1)          General Commands Manual          PCP-ZONEINFO(1)

## [](#NAME)NAME

           pcp-zoneinfo - Report NUMA zone statistics

## [](#SYNOPSIS)SYNOPSIS

           pcp [pcp options] zoneinfo [-Vz?]  [-s samples] [-a archive] [-S
           start_time] [-T end_time] [-Z timezone]

## [](#DESCRIPTION)DESCRIPTION

           The pcp-zoneinfo command is used for viewing the different kinds
           of stats related to NUMA nodes.  Using various options it helps a
           user to analyze useful information related to the zone
           availability for different NUMA nodes.  This is useful for
           analyzing virtual memory behavior.  By default pcp-zoneinfo
           reports live data for the local host.

           The statistics shown are as follows:

                            Per node stats (for each NUMA node)
           HEADER                          DESCRIPTION
           nr_inactive_anon                zone inactive anonymous pages
           nr_active_anon                  active anonymous memory pages
           nr_inactive_file                inactive file memory pages
           nr_active_file                  active file memory memory pages
           nr_unevictable                  unevictable pages
           nr_slab_reclaimable             reclaimable slab pages
           nr_slab_unreclaimable           unreclaimable slab pages
           nr_isolated_anon                isolated anonymous memory pages
           nr_isolated_file                isolated file memory pages
           nr_anon_pages                   anonymous mapped pagecache pages
           nr_mapped                       mapped pagecache pages
           nr_file_pages                   file pagecache pages
           nr_dirty                        pages dirty state
           nr_writeback                    pages writeback state
           nr_writeback_temp               temporary writeback pages
           nr_shmem                        shared memory pages
           nr_shmem_hugepages              shared memory huge pages
           nr_shmem_pmdmapped              shared memory PMD mappings
           nr_file_hugepages               file-backed huge pages
           nr_file_pmdmapped               file-backed PMD mappings
           nr_anon_transparent_hugepages   anonymous transparent huge pages
           nr_unstable                     pages in unstable state in each zone
           nr_vmscan_write                 pages written from the LRU by the VM
                                           scanner The VM is supposed to minimise
                                           the number of pages which get written
                                           from the LRU (for IO scheduling
                                           efficiency and reclaim success).
           nr_vmscan_immediate_reclaim     prioritise for reclaim when writeback
                                           ends
           nr_dirtied                      pages entering dirty state
           nr_written                      pages written out in each zone
           nr_kernel_misc_reclaimable      miscellaneous reclaimable kernel pages

                    Per zone stats (in each zone for each NUMA node)
           HEADER                  DESCRIPTION
           pages free              free space
           pages min               min space
           pages low               low space
           pages high              high space
           pages spanned           spanned space
           pages present           present space
           pages managed           managed space
           pages protection        protection space
           nr_free_pages           number of free pages
           nr_zone_inactive_anon   zone inactive anonymous pages
           nr_zone_active_anon     zone active anonymous pages
           nr_zone_inactive_file   zone inactive file-backed pages
           nr_zone_active_file     zone active file-backed pages
           nr_zone_unevictable     zone unevictable pages
           nr_zone_write_pending   zone write-pending pages
           nr_mlock                pages under mlock
           nr_page_table_pages     page table pages
           nr_kernel_stack         pages of kernel stack
           nr_bounce               bounce buffer pages
           nr_zspages              zsmalloc memory allocator pages
           nr_free_cma             free Contiguous Memory Allocator pages
           numa_hit                successful allocations from preferred NUMA
                                   zone
           numa_miss               unsuccessful allocations from preferred
                                   NUMA zone
           numa_foreign            foreign NUMA zone allocations
           numa_interleave         interleaved NUMA allocations
           numa_local              successful allocations from local NUMA
                                   zone
           numa_other              unsuccessful allocations from local NUMA
                                   zone

## [](#OPTIONS)OPTIONS

           -a file, --archive=file
                  Fetch /proc/zoneinfo for a specified archive file

           -s count, --samples=count
                  Get the zoneinfo statistics for specified number of samples
                  count

           -S, --start=time
                  Filter the samples from the archive from the given time

           -T, --finish=time
                  Filter the samples from the archive until the given time

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

           pcp-zoneinfo collects information from /proc/zoneinfo.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp(1), pmParseInterval(3) and environ(7).

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

    Performance Co-Pilot               PCP                    PCP-ZONEINFO(1)

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
