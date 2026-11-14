---
{"title": "error::inode-uprobes(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/error::inode-uprobes.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# error::inode-uprobes(7stap) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    ERROR::INODE-UPROBES(7stap)                   ERROR::INODE-UPROBES(7stap)

## [](#NAME)NAME

           error::inode-uprobes - limitations of inode-uprobes

## [](#DESCRIPTION)DESCRIPTION

           The uprobes kernel facility introduced in Linux 3.5 aims to
           supplant the earlier out-of-tree utrace patch to enable user-space
           probing.  There have been some functional limitations in inode-
           uprobes that preclude some systemtap constructs.  Over time, we
           hope these regressions will be corrected.

           function.return probes
                  process.function().return probes require "return-probes" or
                  "uretprobes" functionality, which was not implemented in
                  the builtin inode-uprobes until kernel 3.10.  If you cannot
                  upgrade your kernel, consider using process.statement()
                  probes placed on source line numbers at the function's
                  return statements.

           function.statement.absolute probes
                  In utrace-equipped kernels, systemtap made it possible to
                  address probes by literal addresses in the process virtual
                  memory address space.  The new inode-uprobes does not have
                  this capability.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           http://kernelnewbies.org/Linux_3.5 ,
           http://sourceware.org/systemtap/wiki/utrace ,
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

                                                  ERROR::INODE-UPROBES(7stap)

------------------------------------------------------------------------

Pages that refer to this page: [error::pass2(7stap)](../man7/error::pass2.7stap.html)

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
