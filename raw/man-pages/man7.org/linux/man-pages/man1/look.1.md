---
{"title": "look(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/look.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# look(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LOOK(1)                       User Commands                       LOOK(1)

## [](#NAME)NAME

           look - display lines beginning with a given string

## [](#SYNOPSIS)SYNOPSIS

           look [options] string [file]

## [](#DESCRIPTION)DESCRIPTION

           The look utility displays any lines in file which contain string
           as a prefix. As look performs a binary search, the lines in file
           must be sorted (where sort(1) was given the same options -d and/or
           -f that look is invoked with).

           If file is not specified, the file /usr/share/dict/words is used,
           only alphanumeric characters are compared and the case of
           alphabetic characters is ignored.

## [](#OPTIONS)OPTIONS

           -a, --alternative
               Use the alternative dictionary file.

           -d, --alphanum
               Use normal dictionary character set and order, i.e., only
               blanks and alphanumeric characters are compared. This is on by
               default if no file is specified.

               Note that blanks have been added to dictionary character set
               for compatibility with sort -d command since version 2.28.

           -f, --ignore-case
               Ignore the case of alphabetic characters. This is on by
               default if no file is specified.

           -t, --terminate character
               Specify a string termination character, i.e., only the
               characters in string up to and including the first occurrence
               of character are compared.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           The look utility exits 0 if one or more lines were found and
           displayed, 1 if no lines were found, and >1 if an error occurred.

## [](#ENVIRONMENT)ENVIRONMENT

           WORDLIST
               Override the standard location of the dictionary file.

## [](#FILES)FILES

           /usr/share/dict/words
               the dictionary

           /usr/share/dict/web2
               the alternative dictionary

## [](#HISTORY)HISTORY

           The look utility appeared in Version 7 AT&T Unix.

## [](#EXAMPLES)EXAMPLES

               sort -d /etc/passwd -o /tmp/look.dict
               look -t: root:foobar /tmp/look.dict

## [](#SEE_ALSO)SEE ALSO

           grep(1), sort(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The look command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                        LOOK(1)

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
