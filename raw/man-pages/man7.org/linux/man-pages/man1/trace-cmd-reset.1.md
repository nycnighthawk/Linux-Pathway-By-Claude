---
{"title": "trace-cmd-reset(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-reset.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-reset(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-RESET(1)          libtracefs Manual          TRACE-CMD-RESET(1)

## [](#NAME)NAME

           trace-cmd-reset - turn off all Ftrace tracing to bring back full
           performance

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd reset [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) reset command turns off all tracing of Ftrace.
           This will bring back the performance of the system before tracing
           was enabled. This is necessary since trace-cmd-record(1),
           trace-cmd-stop(1) and trace-cmd-extract(1) do not disable the
           tracer, event after the data has been pulled from the buffers. The
           rational is that the user may want to manually enable the tracer
           with the Ftrace pseudo file system, or examine other parts of
           Ftrace to see what trace-cmd did. After the reset command happens,
           the data in the ring buffer, and the options that were used are
           all lost.

## [](#OPTIONS)OPTIONS

           Please note that the order that options are specified on the
           command line is significant. See EXAMPLES.

           -b buffer_size
               When the kernel boots, the Ftrace ring buffer is of a minimal
               size (3 pages per CPU). The first time the tracer is used, the
               ring buffer size expands to what it was set for (default 1.4
               Megs per CPU).

                   If no more tracing is to be done, this option allows you to shrink the
                   ring buffer down to free up available memory.

                   trace-cmd reset -b 1

                   The buffer instance affected is the one (or ones) specified by the most
                   recently preceding *-B*, *-t*, or *-a* option:

                   When used after *-B*, resizes the buffer instance that precedes it on
                   the command line.

                   When used after *-a*, resizes all buffer instances except the top one.

                   When used after *-t* or before any *-B* or *-a*, resizes the top
                   instance.

           -B buffer-name
               If the kernel supports multiple buffers, this will reset the
               trace for only the given buffer. It does not affect any other
               buffer. This may be used multiple times to specify different
               buffers. The top level buffer will not be reset if this option
               is given (unless the -t option is also supplied).

           -a
               Reset the trace for all existing buffer instances. When this
               option is used, the top level instance will not be reset
               unless -t is given.

           -d
               This option deletes the instance buffer(s) specified by the
               most recently preceding -B or -a option. Because the top-level
               instance buffer cannot be deleted, it is invalid to use this
               immediately following -t or prior to any -B or -a option on
               the command line.

           -t
               Resets the top level instance buffer. Without the -B or -a
               option this is the same as the default. But if -B or -a is
               used, this is required if the top level instance buffer should
               also be reset.

           -k dynevent-name
               This option allows preserving specified dynamic event during
               reset. Valid parameters are kprobe, kretprobe, uprobe,
               uretprobe, eprobe, synth and all (for keeping all dynamic
               events). This may be used multiple times to specify different
               dynamic event types.

## [](#EXAMPLES)EXAMPLES

           Reset tracing for instance-one and set its per-cpu buffer size to
           4096kb. Also deletes instance-two. The top level instance and any
           other instances remain unaffected:

               trace-cmd reset -B instance-one -b 4096 -B instance-two -d

           Delete all instance buffers. Top level instance remains
           unaffected:

               trace-cmd reset -a -d

           Delete all instance buffers and also reset the top instance:

               trace-cmd reset -t -a -d

           Invalid. This command implies an attempt to delete the top
           instance:

               trace-cmd reset -a -t -d

           Reset the top instance and set its per-cpu buffer size to 1024kb.
           If any instance buffers exist, they will be unaffected:

               trace-cmd reset -b 1024

           Prevent kprobes and kretprobes from being destroyed during reset:

               trace-cmd reset -k kprobe -k kretprobe

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-stop(1), trace-cmd-extract(1),
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

    libtracefs                      01/02/2025             TRACE-CMD-RESET(1)

------------------------------------------------------------------------

Pages that refer to this page: [trace-cmd(1)](../man1/trace-cmd.1.html),  [trace-cmd-agent(1)](../man1/trace-cmd-agent.1.html),  [trace-cmd-attach(1)](../man1/trace-cmd-attach.1.html),  [trace-cmd-check-events(1)](../man1/trace-cmd-check-events.1.html),  [trace-cmd-clear(1)](../man1/trace-cmd-clear.1.html),  [trace-cmd-extract(1)](../man1/trace-cmd-extract.1.html),  [trace-cmd-hist(1)](../man1/trace-cmd-hist.1.html),  [trace-cmd-list(1)](../man1/trace-cmd-list.1.html),  [trace-cmd-listen(1)](../man1/trace-cmd-listen.1.html),  [trace-cmd-mem(1)](../man1/trace-cmd-mem.1.html),  [trace-cmd-options(1)](../man1/trace-cmd-options.1.html),  [trace-cmd-profile(1)](../man1/trace-cmd-profile.1.html),  [trace-cmd-record(1)](../man1/trace-cmd-record.1.html),  [trace-cmd-report(1)](../man1/trace-cmd-report.1.html),  [trace-cmd-restore(1)](../man1/trace-cmd-restore.1.html),  [trace-cmd-set(1)](../man1/trace-cmd-set.1.html),  [trace-cmd-show(1)](../man1/trace-cmd-show.1.html),  [trace-cmd-snapshot(1)](../man1/trace-cmd-snapshot.1.html),  [trace-cmd-split(1)](../man1/trace-cmd-split.1.html),  [trace-cmd-stack(1)](../man1/trace-cmd-stack.1.html),  [trace-cmd-start(1)](../man1/trace-cmd-start.1.html),  [trace-cmd-stat(1)](../man1/trace-cmd-stat.1.html),  [trace-cmd-stop(1)](../man1/trace-cmd-stop.1.html),  [trace-cmd-stream(1)](../man1/trace-cmd-stream.1.html),  [trace-cmd.dat.v6(5)](../man5/trace-cmd.dat.v6.5.html),  [trace-cmd.dat.v7(5)](../man5/trace-cmd.dat.v7.5.html)

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
