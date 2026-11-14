---
{"title": "opjitconv(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/opjitconv.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# opjitconv(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [VERSION](#VERSION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OPJITCONV(1)             General Commands Manual             OPJITCONV(1)

## [](#NAME)NAME

           opjitconv - convert jit dump file to an ELF

## [](#SYNOPSIS)SYNOPSIS

           opjitconv [ options ] [ [--debug | --non-root | --delete-jitdumps
           ] --session-dir=<dir> <starttime> <endtime> ]

## [](#DESCRIPTION)DESCRIPTION

           Convert a jit dump file to an ELF file

## [](#OPTIONS)OPTIONS

           --debug
                  Print debugging information.

           --non-root
                  Use when opjitconv was invoked by a non-root user via
                  operf.

           --delete-jitdumps
                  Delete jitdump files owned by the user.

           --session-dir [dir]
                  Session directory where sample data is stored.

           --help / -h
                  Display brief usage message.

## [](#VERSION)VERSION

           This man page is current for oprofile-1.5.0git.

## [](#SEE_ALSO)SEE ALSO

           oprofile(1)

## [](#COLOPHON)COLOPHON

           This page is part of the oprofile (a system-wide profiler for
           Linux) project.  Information about the project can be found at 
           ⟨http://oprofile.sourceforge.net/news/⟩.  If you have a bug report
           for this manual page, see ⟨http://oprofile.sourceforge.net/bugs/⟩.
           This page was obtained from the project's upstream Git repository
           ⟨git://git.code.sf.net/p/oprofile/oprofile⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2024-12-10.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    oprofile 1.5.0git            Sun 24 May 2026                 OPJITCONV(1)

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
