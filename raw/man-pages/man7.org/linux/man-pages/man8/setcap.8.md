---
{"title": "setcap(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/setcap.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setcap(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXIT CODE](#EXIT_CODE) \| [REPORTING BUGS](#REPORTING_BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SETCAP(8)                System Manager's Manual                SETCAP(8)

## [](#NAME)NAME

           setcap - set file capabilities

## [](#SYNOPSIS)SYNOPSIS

           setcap [-q] [-n <rootuid>] [-v] {capabilities|-|-r} filename [ ...
           capabilitiesN fileN ]

## [](#DESCRIPTION)DESCRIPTION

           In the absence of the -v (verify) option setcap sets the
           capabilities of each specified filename to the capabilities
           specified.  The optional -n <rootuid> argument can be used to set
           the file capability for use only in a user namespace with this
           root user ID owner. The -v option is used to verify that the
           specified capabilities are currently associated with the file. If
           -v and -n are supplied, the -n <rootuid> argument is also
           verified.

           The capabilities Set are specified in the form described in
           cap_text_formats(7).

           The special capability string, '-', can be used to indicate that
           capabilities are read from the standard input. In such cases, the
           capability set is terminated with a blank line.

           The special capability string, '-r', is used to remove a
           capability set from a file. Note, setting an empty capability set
           is not the same as removing it. An empty set can be used to
           guarantee a file is not executed with privilege in spite of the
           fact that the prevailing ambient+inheritable sets would otherwise
           bestow capabilities on executed binaries.

           The '-f', is used to force completion even when it is in some way
           considered an invalid operation. This can affect '-r' and setting
           file capabilities the kernel will not be able to make sense of.

           The -q flag is used to make the program less verbose in its
           output.

## [](#EXIT_CODE)EXIT CODE

           The setcap program will exit with a 0 exit code if successful. On
           failure, the exit code is 1.

## [](#REPORTING_BUGS)REPORTING BUGS

           Please report bugs via the bugtracker referenced at:

           https://sites.google.com/site/fullycapable

## [](#SEE_ALSO)SEE ALSO

           capsh(1), cap_from_text(3), cap_get_file(3), cap_text_formats(7),
           capabilities(7), user_namespaces(7), captree(8), getcap(8) and
           getpcaps(8).

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

                                    2026-04-07                      SETCAP(8)

------------------------------------------------------------------------

Pages that refer to this page: [capsh(1)](../man1/capsh.1.html),  [cap_iab(3)](../man3/cap_iab.3.html),  [libcap(3)](../man3/libcap.3.html),  [capabilities(7)](../man7/capabilities.7.html),  [cap_text_formats(7)](../man7/cap_text_formats.7.html),  [getcap(8)](../man8/getcap.8.html),  [getpcaps(8)](../man8/getpcaps.8.html)

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
