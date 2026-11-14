---
{"title": "trace-cmd-mem(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-mem.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-mem(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-MEM(1)            libtracefs Manual            TRACE-CMD-MEM(1)

## [](#NAME)NAME

           trace-cmd-mem - show memory usage of certain kmem events

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd mem [OPTIONS][input-file]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) mem requires a trace-cmd record that enabled the
           following events:

               kmalloc
               kmalloc_node
               kfree
               kmem_cache_alloc
               kmem_cache_alloc_node
               kmem_cache_alloc_free

           It then reads the amount requested and the ammount freed as well
           as the functions that called the allocation. It then reports the
           final amount of bytes requested and allocated, along with the
           total amount allocated and requested, as well as the max
           allocation and requested during the run. It reports the amount of
           wasted bytes (allocated - requested) that was not freed, as well
           as the max wasted amount during the run. The list is sorted by
           descending order of wasted bytes after the run.

                       Function                Waste   Alloc   req             TotAlloc     TotReq             MaxAlloc     MaxReq     MaxWaste
                       --------                -----   -----   ---             --------     ------             --------     ------     --------
                 rb_allocate_cpu_buffer        768     2304    1536                2304       1536                 2304       1536     768
                        alloc_pipe_info        400     1152    752                 1152        752                 1152        752     400
                         instance_mkdir        252     544     292                  544        292                  544        292     252
                              __d_alloc        215     1086560 1086345          1087208    1086993              1086560    1086345     215
                         get_empty_filp        72      2304    2232                4864       4712                 4864       4712     152
                               mm_alloc        40      960     920                  960        920                  960        920     40
                          prepare_creds        32      192     160                 1728       1440                 1728       1440     288
                   tracing_buffers_open        8       32      24                    32         24                   32         24     8
                                 do_brk        0       0       0                    368        368                  368        368     0
               journal_add_journal_head        0       6048    6048                6048       6048                 6048       6048     0
                          journal_start        0       0       0                   1224       1224                   48         48     0
                    __rb_allocate_pages        0       3289856 3289856          3289856    3289856              3289856    3289856     0
                         anon_vma_alloc        0       0       0                    936        936                  864        864     0
                                                                       [...]

## [](#OPTIONS)OPTIONS

           -i input-file
               By default, trace-cmd hist will read the file trace.dat. But
               the -i option open up the given input-file instead. Note, the
               input file may also be specified as the last item on the
               command line.

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-stop(1), trace-cmd-extract(1),
           trace-cmd-reset(1), trace-cmd-hist(1), trace-cmd-split(1),
           trace-cmd-listen(1)

## [](#AUTHOR)AUTHOR

           Written by Steven Rostedt, <rostedt@goodmis.org[1]>

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#COPYING)COPYING

           Copyright (C) 2013 Red Hat, Inc. Free use of this software is
           granted under the terms of the GNU Public License (GPL).

## [](#NOTES)NOTES

            1. rostedt@goodmis.org
               mailto:rostedt@goodmis.org

## [](#COLOPHON)COLOPHON

           This page is part of the trace-cmd (a front-end for Ftrace)
           project.  Information about the project can be found at 
           ⟨https://www.trace-cmd.org/⟩.  If you have a bug report for this
           manual page, see ⟨https://www.trace-cmd.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-05-29.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    libtracefs                      09/24/2023               TRACE-CMD-MEM(1)

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
