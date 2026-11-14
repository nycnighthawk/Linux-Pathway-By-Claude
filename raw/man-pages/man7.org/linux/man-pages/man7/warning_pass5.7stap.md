---
{"title": "warning::pass5(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/warning::pass5.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# warning::pass5(7stap) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [GATHERING MORE INFORMATION](#GATHERING_MORE_INFORMATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ERROR::PASS5(7stap)                                   ERROR::PASS5(7stap)

## [](#NAME)NAME

           warning::pass5 - systemtap pass-5 warnings

## [](#DESCRIPTION)DESCRIPTION

           Warnings that occur during pass 5 (execution) can have a variety
           of causes.

           probe insertion errors
                  With any of the systemtap runtimes, it may be possible that
                  the backends are unable to insert probe points requested by
                  the systemtap script.  For example, you may see errors such
                  as

                  WARNING: probe [...] registration error (rc -524)

                  (524 is a kernel error code for ENOTSUPP).  These situa‐
                  tions are out of systemtap's control, and result in some
                  probes not receiving any hits.  This may be caused by tem‐
                  porary resource constraints or permanent problems.  One
                  common permanent problem is such a probe point being placed
                  at instructions that the runtime (kernel kprobes, uprobes
                  or dyninst) cannot decode or intercept.  A possible
                  workaround is to move the probe points slightly in the
                  script, so as to target a nearby statement, or a caller, or
                  a callee.  See also error::dwarf(7stap).

## [](#GATHERING_MORE_INFORMATION)GATHERING MORE INFORMATION

           Increasing the verbosity of pass-5 with an option such as --vp
           00001 can help pinpoint the problem.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           http://sourceware.org/systemtap/wiki/TipExhaustedResourceErrors ,
           error::pass5(7stap),
           error::reporting(7stap)
           error::dwarf(7stap)

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

                                                          ERROR::PASS5(7stap)

------------------------------------------------------------------------

Pages that refer to this page: [error::pass5(7stap)](../man7/error::pass5.7stap.html)

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
