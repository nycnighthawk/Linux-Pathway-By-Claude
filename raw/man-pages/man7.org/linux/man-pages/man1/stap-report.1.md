---
{"title": "stap-report(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stap-report.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stap-report(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAP-REPORT(1)           General Commands Manual           STAP-REPORT(1)

## [](#NAME)NAME

           stap-report - collect system information that is useful for
           debugging systemtap bugs

## [](#SYNOPSIS)SYNOPSIS

           stap-report

## [](#DESCRIPTION)DESCRIPTION

           The stap-report executable collects system information that is
           useful for debugging systemtap bugs. It is a good idea to include
           such a report in bug reports especially if you send them directly
           to the upstream. stap-report can be run either as a normal user or
           as root. The report will be more complete if stap-report is run as
           root.

## [](#EXAMPLES)EXAMPLES

                  $ stap-report > report.txt
                  $ head report.txt
                  == id ==
                  uid=1000(user) gid=1000(user) groups=122(stapdev),123(stapusr),129(stapsys)
                  == stap -V ==
                  Systemtap translator/driver (version 2.2.1/0.153, Debian version 2.2.1-1)
                  Copyright (C) 2005-2013 Red Hat, Inc. and others
                  This is free software; see the source for copying conditions.
                  enabled features: AVAHI LIBSQLITE3 NSS TR1_UNORDERED_MAP NLS
                  == which stap ==
                  /usr/bin/stap
                  == locate --regex '/stap(run)?$' | xargs ls -ald ==

## [](#SEE_ALSO)SEE ALSO

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

                                                               STAP-REPORT(1)

------------------------------------------------------------------------

Pages that refer to this page: [error::reporting(7stap)](../man7/error::reporting.7stap.html)

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
