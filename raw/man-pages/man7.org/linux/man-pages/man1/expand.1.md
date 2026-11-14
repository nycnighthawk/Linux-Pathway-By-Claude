---
{"title": "expand(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/expand.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# expand(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    EXPAND(1)                     User Commands                     EXPAND(1)

## [](#NAME)NAME

           expand - convert tabs to spaces

## [](#SYNOPSIS)SYNOPSIS

           expand [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           Convert tabs in each FILE to spaces, writing to standard output.

           With no FILE, or when FILE is -, read standard input.

           Mandatory arguments to long options are mandatory for short
           options too.

           -i, --initial
                  do not convert tabs after non blanks

           -t, --tabs=N
                  have tabs N characters apart, not 8

           -t, --tabs=LIST
                  use comma separated list of tab positions.  The last
                  specified position can be prefixed with '/' to specify a
                  tab size to use after the last explicitly specified tab
                  stop.  Also a prefix of '+' can be used to align remaining
                  tab stops relative to the last specified tab stop instead
                  of the first column

           --help display this help and exit

           --version
                  output version information and exit

## [](#AUTHOR)AUTHOR

           Written by David MacKenzie.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to: bug-coreutils@gnu.org
           GNU coreutils home page: <https://www.gnu.org/software/coreutils/>
           General help using GNU software: <https://www.gnu.org/gethelp/>
           Report any translation bugs to
           <https://translationproject.org/team/>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2026 Free Software Foundation, Inc.  License GPLv3+:
           GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
           This is free software: you are free to change and redistribute it.
           There is NO WARRANTY, to the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           unexpand(1)

           Full documentation <https://www.gnu.org/software/coreutils/expand>
           or available locally via: info '(coreutils) expand invocation'

## [](#COLOPHON)COLOPHON

           This page is part of the coreutils (basic file, shell and text
           manipulation utilities) project.  Information about the project
           can be found at ⟨http://www.gnu.org/software/coreutils/⟩.  If you
           have a bug report for this manual page, see
           ⟨http://www.gnu.org/software/coreutils/⟩.  This page was obtained
           from the tarball coreutils-9.11.tar.xz fetched from
           ⟨http://ftp.gnu.org/gnu/coreutils/⟩ on 2026-08-03.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    GNU coreutils 9.11              April 2026                      EXPAND(1)

------------------------------------------------------------------------

Pages that refer to this page: [col(1)](../man1/col.1.html),  [colrm(1)](../man1/colrm.1.html),  [unexpand(1)](../man1/unexpand.1.html)

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
