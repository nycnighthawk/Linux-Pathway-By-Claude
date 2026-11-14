---
{"title": "getcap(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/getcap.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getcap(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GETCAP(8)                System Manager's Manual                GETCAP(8)

## [](#NAME)NAME

           getcap - examine file capabilities

## [](#SYNOPSIS)SYNOPSIS

           getcap [-v] [-n] [-r] [-h] filename [ ... ]

## [](#DESCRIPTION)DESCRIPTION

           getcap displays the name and capabilities of each specified file.

## [](#OPTIONS)OPTIONS

           -h  prints quick usage.

           -n  prints any non-zero user namespace root user ID value found to
               be associated with a file's capabilities.

           -r  enables recursive search.

           -v  display all searched entries, even if the have no file-
               capabilities.

           NOTE: an empty value of '=' is not equivalent to an omitted (or
           removed) capability on a file. This is most significant with
           respect to the Ambient capability vector, since a process with
           Ambient capabilities will lose them when executing a file having
           '=' capabilities, but will retain the Ambient inheritance of
           privilege when executing a file with an omitted file capability.
           This special empty setting can be used to prevent a binary from
           executing with privilege. For some time, the kernel honored this
           suppression for root executing the file, but the kernel developers
           decided after a number of years that this behavior was unexpected
           for the superuser and reverted it just for that user identity.
           Suppression of root privilege, for a process tree, is possible,
           using the capsh(1) --mode option.

           filename
               One file per line.

## [](#REPORTING_BUGS)REPORTING BUGS

           Please report bugs via the bugtracker referenced at:

           https://sites.google.com/site/fullycapable

## [](#SEE_ALSO)SEE ALSO

           capsh(1), cap_get_file(3), cap_to_text(3), capabilities(7),
           user_namespaces(7), captree(8), getpcaps(8) and setcap(8).

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

                                    2026-04-07                      GETCAP(8)

------------------------------------------------------------------------

Pages that refer to this page: [capsh(1)](../man1/capsh.1.html),  [libcap(3)](../man3/libcap.3.html),  [capabilities(7)](../man7/capabilities.7.html),  [cap_text_formats(7)](../man7/cap_text_formats.7.html),  [getpcaps(8)](../man8/getpcaps.8.html),  [setcap(8)](../man8/setcap.8.html)

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
