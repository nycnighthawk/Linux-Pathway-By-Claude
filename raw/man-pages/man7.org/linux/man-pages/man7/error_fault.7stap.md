---
{"title": "error::fault(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/error::fault.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# error::fault(7stap) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    ERROR::FAULT(7stap)                                   ERROR::FAULT(7stap)

## [](#NAME)NAME

           error::fault - memory access faults

## [](#DESCRIPTION)DESCRIPTION

           Read or write faults can occur during the operation of a systemtap
           script, if the script causes dereferencing of a pointer that turns
           out to be invalid.  This can be caused by using context variables
           that do not happen to have valid values, or perhaps references to
           memory that is unavailable at that moment due to paging.

           These fault conditions are benign because they are caught by the
           systemtap runtime, which cleanly terminates the script.  If quick
           termination is not desired, consider using the --skip-badvars or
           --suppress-handler-errors or -DMAXERRORS=NN stap options, or
           wrapping relevant parts of the probe handlers in a try/catch
           block.

           It may be possible to adjust the target program, to make it more
           likely that needed context variables are paged in when systemtap
           looks for them.  Consider adding some lightweight processing on
           the key variables, like a strlen(foo) for a string, or iterating
           across elements of an array or linked list, or touching a few
           bytes of a heap-allocated block.  The idea is to trigger any page
           faults in the target program, before systemtap would need to (but
           can't).

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

                                                          ERROR::FAULT(7stap)

------------------------------------------------------------------------

Pages that refer to this page: [stapprobes(3stap)](../man3/stapprobes.3stap.html),  [error::pass5(7stap)](../man7/error::pass5.7stap.html)

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
