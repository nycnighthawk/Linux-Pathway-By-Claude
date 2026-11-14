---
{"title": "error::process-tracking(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/warning::process-tracking.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# error::process-tracking(7stap) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [RESOLVING THE ISSUE](#RESOLVING_THE_ISSUE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WARNING::PROCESS-TRACKING(7stap)         WARNING::PROCESS-TRACKING(7stap)

## [](#NAME)NAME

           warning::process-tracking - process-tracking facilities are not
           available

## [](#DESCRIPTION)DESCRIPTION

           These errors and warnings occur when the kernel systemtap is
           running on lacks support for user-space process tracking
           facilities.

       COMPILE-TIME ERROR
           The error

                  ERROR: user-space process-tracking facilities not available

           occurs when the script contains a uprobes probe point that the
           current kernel does not support.

       RUNTIME WARNINGS
           The warning,

                  WARNING: process-tracking facilities are not available in this kernel

           and the related message,

                  WARNING: cannot track target in process '...'

           both occur at runtime when running on a kernel (generally an older
           version) that has neither utrace functionality nor an acceptable
           substitute.

           The script should still load and run. However, probes that rely on
           availability of process-tracking facilities will silently fail to
           trigger.

## [](#RESOLVING_THE_ISSUE)RESOLVING THE ISSUE

           If process-tracking functionality is absolutely necessary, either
           a kernel version newer than 3.5 is needed, or an older version
           must be compiled with appropriate utrace patches.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           error::reporting(7stap)

## [](#COLOPHON)COLOPHON

           This page is part of the systemtap (a tracing and live-system
           analysis tool) project.  Information about the project can be
           found at ⟨https://sourceware.org/systemtap/⟩.  If you have a bug
           report for this manual page, send it to systemtap@sourceware.org.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/systemtap.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                             WARNING::PROCESS-TRACKING(7stap)

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
