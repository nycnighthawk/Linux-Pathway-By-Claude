---
{"title": "pmlock(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlock.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlock(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOCK(1)                General Commands Manual                PMLOCK(1)

## [](#NAME)NAME

           pmlock - simple file-based mutex

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmlock [-i ident] [-v] file

## [](#DESCRIPTION)DESCRIPTION

           pmlock attempts to acquire an exclusive lock by creating a zero-
           sized file with a mode of 0.

           The -i option changes the behaviour to write ident into file,
           followed by a newline and the file mode is 0444.  ident is an
           arbitrary string, but by convention it is the process id of the
           locker followed by the name or identification of the locker
           command or script.

           The exit status is 0 for success, 1 for failure.

           To release the lock, remove file with rm(1) or unlink(2).

           In the event of a failure, the -v option produces an explanatory
           message on stderr.

## [](#SEE_ALSO)SEE ALSO

           rm(1) and unlink(2).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.
           Information about the project can be found at 
           ⟨http://www.pcp.io/⟩.  If you have a bug report for this manual
           page, send it to pcp@groups.io.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot               PCP                          PMLOCK(1)

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
