---
{"title": "perf-buildid-cache(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/perf-buildid-cache.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perf-buildid-cache(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERF-BUILDID-CACHE(1)          perf Manual          PERF-BUILDID-CACHE(1)

## [](#NAME)NAME

           perf-buildid-cache - Manage build-id cache.

## [](#SYNOPSIS)SYNOPSIS

           perf buildid-cache <options>

## [](#DESCRIPTION)DESCRIPTION

           This command manages the build-id cache. It can add, remove,
           update and purge files to/from the cache. In the future it should
           as well set upper limits for the space used by the cache, etc.
           This also scans the target binary for SDT (Statically Defined
           Tracing) and record it along with the buildid-cache, which will be
           used by perf-probe. For more details, see perf-probe(1).

## [](#OPTIONS)OPTIONS

           -a, --add=
               Add specified file to the cache.

           -f, --force
               Don’t complain, do it.

           -k, --kcore
               Add specified kcore file to the cache. For the current host
               that is /proc/kcore which requires root permissions to read.
               Be aware that running perf buildid-cache as root may update
               root’s build-id cache not the user’s. Use the -v option to see
               where the file is created. Note that the copied file contains
               only code sections not the whole core image. Note also that
               files "kallsyms" and "modules" must also be in the same
               directory and are also copied. All 3 files are created with
               read permissions for root only. kcore will not be added if
               there is already a kcore in the cache (with the same build-id)
               that has the same modules at the same addresses. Use the -v
               option to see if a copy of kcore is actually made.

           -r, --remove=
               Remove a cached binary which has same build-id of specified
               file from the cache.

           -p, --purge=
               Purge all cached binaries including older caches which have
               specified path from the cache.

           -P, --purge-all
               Purge all cached binaries. This will flush out entire cache.

           -M, --missing=
               List missing build ids in the cache for the specified file.

           -u, --update=
               Update specified file of the cache. Note that this doesn’t
               remove older entries since those may be still needed for
               annotating old (or remote) perf.data. Only if there is already
               a cache which has exactly same build-id, that is replaced by
               new one. It can be used to update kallsyms and kernel dso to
               vmlinux in order to support annotation.

           -l, --list
               List all valid binaries from cache.

           -v, --verbose
               Be more verbose.

           --target-ns=PID: Obtain mount namespace information from the
           target pid. This is used when creating a uprobe for a process that
           resides in a different mount namespace from the perf(1) utility.

           --debuginfod[=URLs]
               Specify debuginfod URL to be used when retrieving perf.data
               binaries, it follows the same syntax as the DEBUGINFOD_URLS
               variable, like:

                   buildid-cache.debuginfod=http://192.168.122.174:8002

                   If the URLs is not specified, the value of DEBUGINFOD_URLS
                   system environment variable is used.

## [](#SEE_ALSO)SEE ALSO

           perf-record(1), perf-report(1), perf-buildid-list(1)

## [](#COLOPHON)COLOPHON

           This page is part of the perf (Performance analysis tools for
           Linux (in Linux source tree)) project.  Information about the
           project can be found at 
           ⟨https://perf.wiki.kernel.org/index.php/Main_Page⟩.  If you have a
           bug report for this manual page, send it to
           linux-kernel@vger.kernel.org.  This page was obtained from the
           project's upstream Git repository
           ⟨http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-08-03.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    perf                            2022-01-15          PERF-BUILDID-CACHE(1)

------------------------------------------------------------------------

Pages that refer to this page: [perf(1)](../man1/perf.1.html),  [perf-probe(1)](../man1/perf-probe.1.html)

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
