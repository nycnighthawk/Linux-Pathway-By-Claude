---
{"title": "stap-prep(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stap-prep.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stap-prep(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAP-PREP(1)             General Commands Manual             STAP-PREP(1)

## [](#NAME)NAME

           stap-prep - prepare system for systemtap use

## [](#SYNOPSIS)SYNOPSIS

           stap-prep [ KERNEL_VERSION ]

## [](#DESCRIPTION)DESCRIPTION

           The stap-prep executable prepares the system for systemtap use by
           installing kernel headers, debug symbols and build tools that
           match the currently running kernel or optionally the kernel
           version given by the user.

           If the debuginfod-find tool is installed and is able to fetch
           debuginfo for a kernel component, it is assumed to remain
           available later.  In this case, no debug symbols will be
           downloaded during stap-prep.

           The exact behavior of stap-prep may be customized by the
           distribution maintainers. It might for example only give
           suggestions and not actually install the required packages if that
           is difficult to automate.

## [](#EXAMPLES)EXAMPLES

                  $ stap-prep
                  Please install linux-image-3.2.0-2-amd64-dbg

## [](#SEE_ALSO)SEE ALSO

           http://sourceware.org/elfutils/Debuginfod.html 
           stap(1)

## [](#BUGS)BUGS

           Use the Bugzilla link of the project web page or our mailing list.
           http://sourceware.org/systemtap/ ,<systemtap@sourceware.org>.

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

                                                                 STAP-PREP(1)

------------------------------------------------------------------------

Pages that refer to this page: [stap(1)](../man1/stap.1.html),  [error::pass2(7stap)](../man7/error::pass2.7stap.html),  [warning::debuginfo(7stap)](../man7/warning::debuginfo.7stap.html)

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
