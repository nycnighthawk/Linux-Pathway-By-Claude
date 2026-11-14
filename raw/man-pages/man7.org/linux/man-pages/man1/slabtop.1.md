---
{"title": "slabtop(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/slabtop.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# slabtop(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SORT CRITERIA](#SORT_CRITERIA) \| [COMMANDS](#COMMANDS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SLABTOP(1)               General Commands Manual               SLABTOP(1)

## [](#NAME)NAME

           slabtop - display kernel slab cache information in real time

## [](#SYNOPSIS)SYNOPSIS

           slabtop [option ...]

## [](#DESCRIPTION)DESCRIPTION

           slabtop displays detailed kernel slab cache information in real
           time.  It displays a listing of the top caches sorted by one of
           the listed sort criteria.  It also displays a statistics header
           filled with slab layer information.

## [](#OPTIONS)OPTIONS

           Normal invocation of slabtop does not require any options.  The
           behavior, however, can be fine-tuned by specifying one or more of
           the following flags:

           -d, --delay=N
                  Refresh the display every n in seconds.  By default,
                  slabtop refreshes the display every three seconds.  To exit
                  the program, hit q.  This cannot be combined with the -o
                  option.

           -s, --sort=S
                  Sort by S, where S is one of the sort criteria.

           -o, --once
                  Display the output once and then exit.

           --human
                  Show slab sizes automatically scaled to shortest three
                  digit unit and display the units of print out.  Following
                  units are used.

                    B = bytes
                    Ki = kibibyte
                    Mi = mebibyte
                    Gi = gibibyte
                    Ti = tebibyte
                    Pi = pebibyte

           If this flag is not used, the slab sizes will be shown in KiB.

           -V, --version
                  Display version information and exit.

           -h, --help
                  Display usage information and exit.

## [](#SORT_CRITERIA)SORT CRITERIA

           The following are valid sort criteria used to sort the individual
           slab caches and thereby determine what are the "top" slab caches
           to display.  The default sort criteria is to sort by the number of
           objects ("o").

           The sort criteria can also be changed while slabtop is running by
           pressing the associated character.
           character   description                header
           a           number of active objects   ACTIVE
           b           objects per slab           OBJ/SLAB
           c           cache size                 CACHE SIZE
           l           number of slabs            SLABS
           v           number of active slabs     N/A
           n           name                       NAME
           o           number of objects          OBJS
           p           pages per slab             N/A
           s           object size                OBJ SIZE
           u           cache utilization          USE

## [](#COMMANDS)COMMANDS

           slabtop accepts keyboard commands from the user during use.  The
           following are supported.  In the case of letters, both cases are
           accepted.

           Each of the valid sort characters are also accepted, to change the
           sort routine. See the section SORT CRITERIA.

           <SPACEBAR>
                  Refresh the screen.

           Q      Quit the program.

## [](#FILES)FILES

           /proc/slabinfo
                  slab information

## [](#SEE_ALSO)SEE ALSO

           free(1), ps(1), top(1), vmstat(8)

## [](#NOTES)NOTES

           Currently, slabtop requires a 2.4 or later kernel (specifically, a
           version 1.1 or later /proc/slabinfo).  Kernel 2.2 should be
           supported in the future.

           The slabtop statistic header is tracking how many bytes of slabs
           are being used and is not a measure of physical memory.  The
           'Slab' field in the /proc/meminfo file is tracking information
           about used slab physical memory.

           The CACHE SIZE column is not accurate, it's the upper limit of
           memory used by specific slab. When system using slub (most common
           case) is under high memory pressure, there are slab order
           fallbacks, which means "pages per slab" is not constant and may
           decrease.

## [](#AUTHORS)AUTHORS

           Written by Chris Rivera and Robert Love.

           slabtop was inspired by Martin Bligh's perl script, vmtop.

## [](#REPORTING_BUGS)REPORTING BUGS

           Please send bug reports to ⟨procps@freelists.org⟩.

## [](#COLOPHON)COLOPHON

           This page is part of the procps-ng (/proc filesystem utilities)
           project.  Information about the project can be found at 
           ⟨https://gitlab.com/procps-ng/procps⟩.  If you have a bug report
           for this manual page, see
           ⟨https://gitlab.com/procps-ng/procps/blob/master/Documentation/bugs.md⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/procps-ng/procps.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    procps-ng                       2023-12-26                     SLABTOP(1)

------------------------------------------------------------------------

Pages that refer to this page: [free(1)](../man1/free.1.html),  [top(1)](../man1/top.1.html),  [slabinfo(5)](../man5/slabinfo.5.html)

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
