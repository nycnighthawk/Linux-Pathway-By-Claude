---
{"title": "trace-cmd-snapshot(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-snapshot.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-snapshot(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-SNAPSHOT(1)       libtracefs Manual       TRACE-CMD-SNAPSHOT(1)

## [](#NAME)NAME

           trace-cmd-snapshot - take, reset, free, or show a Ftrace kernel
           snapshot

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd snapshot [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) snapshot controls or displays the Ftrace Linux
           kernel snapshot feature (if the kernel supports it). This is
           useful to "freeze" an instance of a live trace but without
           stopping the trace.

                trace-cmd start -p function
                trace-cmd snapshot -s
                trace-cmd snapshot
               [ dumps the content of buffer at 'trace-cmd snapshot -s' ]
                trace-cmd snapshot -s
                trace-cmd snapshot
               [ dumps the new content of the buffer at the last -s operation ]

## [](#OPTIONS)OPTIONS

           -s
               Take a snapshot of the currently running buffer.

           -r
               Clear out the buffer.

           -f
               Free the snapshot buffer. The buffer takes up memory inside
               the kernel. It is best to free it when not in use. The first
               -s operation will allocate it if it is not already allocated.

           -c cpu
               Operate on a per cpu snapshot (may not be fully supported by
               all kernels)

           -B buf
               If a buffer instance was created, then the -B option will
               operate on the snapshot within the buffer.

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-extract(1), trace-cmd-reset(1),
           trace-cmd-split(1), trace-cmd-list(1), trace-cmd-listen(1)

## [](#AUTHOR)AUTHOR

           Written by Steven Rostedt, <rostedt@goodmis.org[1]>

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#COPYING)COPYING

           Copyright (C) 2010 Red Hat, Inc. Free use of this software is
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

    libtracefs                      09/24/2023          TRACE-CMD-SNAPSHOT(1)

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
