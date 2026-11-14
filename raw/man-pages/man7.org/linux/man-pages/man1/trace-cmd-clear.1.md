---
{"title": "trace-cmd-clear(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-clear.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-clear(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [LICENSE](#LICENSE) \| [RESOURCES](#RESOURCES) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-CLEAR(1)          libtracefs Manual          TRACE-CMD-CLEAR(1)

## [](#NAME)NAME

           trace-cmd-clear - clear the Ftrace buffer.

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd clear [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) clear clears the content of the Ftrace ring
           buffer.

## [](#OPTIONS)OPTIONS

           -B buffer-name
               If the kernel supports multiple buffers, this will clear only
               the given buffer. It does not affect any other buffers. This
               may be used multiple times to specify different buffers. The
               top level buffer will not be clearded if this option is given.

           -a
               Clear all existing buffers, including the top level one.

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-record(1), trace-cmd-report(1),
           trace-cmd-start(1), trace-cmd-extract(1), trace-cmd-reset(1),
           trace-cmd-split(1), trace-cmd-list(1), trace-cmd-listen(1)

## [](#AUTHOR)AUTHOR

               Steven Rostedt <rostedt@goodmis.org[1]>, author of trace-cmd.
               Tzvetomir Stoyanov <tz.stoyanov@gmail.com[2]>, author of this man page.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to <linux-trace-devel@vger.kernel.org[3]>

## [](#LICENSE)LICENSE

           trace-cmd is Free Software licensed under the terms of the GNU
           Public License (GPL).

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#NOTES)NOTES

            1. rostedt@goodmis.org
               mailto:rostedt@goodmis.org

            2. tz.stoyanov@gmail.com
               mailto:tz.stoyanov@gmail.com

            3. linux-trace-devel@vger.kernel.org
               mailto:linux-trace-devel@vger.kernel.org

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

    libtracefs                      09/24/2023             TRACE-CMD-CLEAR(1)

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
