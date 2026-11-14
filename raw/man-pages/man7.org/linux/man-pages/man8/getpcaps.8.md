---
{"title": "getpcaps(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/getpcaps.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getpcaps(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GETPCAPS(8)              System Manager's Manual              GETPCAPS(8)

## [](#NAME)NAME

           getpcaps - display process capabilities

## [](#SYNOPSIS)SYNOPSIS

           getpcaps [optional args] pid...

## [](#DESCRIPTION)DESCRIPTION

           getpcaps displays the capabilities on the processes indicated by
           the pid value(s) given on the command line.  A pid of 0 displays
           the capabilities of the process that is running getpcaps itself.

           The capability Set of the process is displayed in the text
           represenation described here: cap_text_formats(7).

           Optional arguments:

           --help or --usage
                  Displays usage information and exits.

           --ugly or --legacy
                  Displays output in a somewhat ugly legacy format.

           --verbose
                  Displays usage in a legacy-like format but not quite so
                  ugly in modern default terminal fonts.

           --iab  Displays IAB tuple capabilities from the process. The
                  output format here is also described in
                  cap_text_formats(7).  Double quotes encase the regular
                  process capabilities and square brackets encase the IAB
                  tuple. This format is also used by captree(8).

## [](#REPORTING_BUGS)REPORTING BUGS

           Please report bugs via the bugtracker referenced at:

           https://sites.google.com/site/fullycapable

## [](#SEE_ALSO)SEE ALSO

           capsh(1), cap_from_text(3), cap_iab(3), cap_text_format(7),
           capabilities(7), captree(8), getcap(8), and setcap(8).

## [](#AUTHOR)AUTHOR

           This manual page was originally written by Robert Bihlmeyer
           <robbe@debian.org>, for the Debian GNU/Linux system (but may be
           used by others).

## [](#COLOPHON)COLOPHON

           This page is part of the libcap (capabilities commands and
           library) project.  Information about the project can be found at
           ⟨https://sites.google.com/site/fullycapable/⟩.  If you have a bug
           report for this manual page, send it to morgan@kernel.org (please
           put "libcap" in the Subject line).  This page was obtained from
           the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/libs/libcap/libcap.git/⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-30.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                    2026-04-07                    GETPCAPS(8)

------------------------------------------------------------------------

Pages that refer to this page: [capsh(1)](../man1/capsh.1.html),  [libcap(3)](../man3/libcap.3.html),  [capabilities(7)](../man7/capabilities.7.html),  [getcap(8)](../man8/getcap.8.html),  [setcap(8)](../man8/setcap.8.html)

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
