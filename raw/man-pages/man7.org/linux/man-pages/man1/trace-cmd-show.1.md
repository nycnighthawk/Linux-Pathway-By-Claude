---
{"title": "trace-cmd-show(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-show.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-show(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-SHOW(1)           libtracefs Manual           TRACE-CMD-SHOW(1)

## [](#NAME)NAME

           trace-cmd-show - show the contents of the Ftrace Linux kernel
           tracing buffer.

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd show [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) show displays the contents of one of the Ftrace
           Linux kernel tracing files: trace, snapshot, or trace_pipe. It is
           basically the equivalent of doing:

               cat /sys/kernel/debug/tracing/trace

## [](#OPTIONS)OPTIONS

           -p
               Instead of displaying the contents of the "trace" file, use
               the "trace_pipe" file. The difference between the two is that
               the "trace" file is static. That is, if tracing is stopped,
               the "trace" file will show the same contents each time.

                   The "trace_pipe" file is a consuming read, where a read of the file
                   will consume the output of what was read and it will not read the
                   same thing a second time even if tracing is stopped. This file
                   als will block. If no data is available, trace-cmd show will stop
                   and wait for data to appear.

           -s
               Instead of reading the "trace" file, read the snapshot file.
               The snapshot is made by an application writing into it and the
               kernel will perform as swap between the currently active
               buffer and the current snapshot buffer. If no more swaps are
               made, the snapshot will remain static. This is not a consuming
               read.

           -c cpu
               Read only the trace file for a specified CPU.

           -f
               Display the full path name of the file that is being
               displayed.

           -B buf
               If a buffer instance was created, then the -B option will
               access the files associated with the given buffer.

           --tracing_on
               Show if tracing is on for the given instance.

           --current_tracer
               Show what the current tracer is.

           --buffer_size
               Show the current buffer size (per-cpu)

           --buffer_total_size
               Show the total size of all buffers.

           --buffer_subbuf_size
               Show the size in kilobytes of the sub-buffers of the ring
               buffer. The ring buffer is broken up into equal size
               sub-buffers were an event can only be as big as the sub-buffer
               data section (the size minus its meta data).

           --buffer_percent
               Show the percentage the buffer must be filled before a reader
               that is blocked on the trace_pipe_raw file will be woken up.

                   0       : wake up immediately on any new data
                   1 - 99  : wake up on this percentage of the sub-buffers being full
                   100     : wake up after the buffer is full and the writer is on the last sub-buffer

           --ftrace_filter
               Show what function filters are set.

           --ftrace_notrace
               Show what function disabled filters are set.

           --ftrace_pid
               Show the PIDs the function tracer is limited to (if any).

           --graph_function
               Show the functions that will be graphed.

           --graph_notrace
               Show the functions that will not be graphed.

           --hist [system:]event
               Show the content of a histogram "hist" file for a given event

           --trigger [system:]event
               Show the content of the "trigger" file for a given event

           --cpumask
               Show the mask of CPUs that tracing will trace.

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

    libtracefs                      06/13/2024              TRACE-CMD-SHOW(1)

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
