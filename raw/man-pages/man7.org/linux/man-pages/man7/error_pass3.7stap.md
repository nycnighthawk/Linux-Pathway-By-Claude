---
{"title": "error::pass3(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/error::pass3.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# error::pass3(7stap) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [GATHERING MORE INFORMATION](#GATHERING_MORE_INFORMATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ERROR::PASS3(7stap)                                   ERROR::PASS3(7stap)

## [](#NAME)NAME

           error::pass3 - systemtap pass-3 errors

## [](#DESCRIPTION)DESCRIPTION

           Errors during pass 3 (translation) occur only rarely.

           unsupported code generation
                  Some script language constructs are not available in every
                  probe point.  For example, the @perf() counter-reading
                  function may only be used in process.*  probes.

## [](#GATHERING_MORE_INFORMATION)GATHERING MORE INFORMATION

           Increasing the verbosity of pass-3 with an option such as --vp 002
           may help pinpoint the problem.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           stapprobes(3stap)
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

                                                          ERROR::PASS3(7stap)

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
