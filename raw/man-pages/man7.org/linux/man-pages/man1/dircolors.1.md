---
{"title": "dircolors(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dircolors.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dircolors(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DIRCOLORS(1)                  User Commands                  DIRCOLORS(1)

## [](#NAME)NAME

           dircolors - color setup for ls

## [](#SYNOPSIS)SYNOPSIS

           dircolors [OPTION]... [FILE]

## [](#DESCRIPTION)DESCRIPTION

           Output commands to set the LS_COLORS environment variable.

       Determine format of output:
           -b, --sh, --bourne-shell
                  output Bourne shell code to set LS_COLORS

           -c, --csh, --c-shell
                  output C shell code to set LS_COLORS

           -p, --print-database
                  output defaults

           --print-ls-colors
                  output fully escaped colors for display

           --help display this help and exit

           --version
                  output version information and exit

           If FILE is specified, read it to determine which colors to use for
           which file types and extensions.  Otherwise, a precompiled
           database is used.  For details on the format of these files, run
           'dircolors --print-database'.

## [](#AUTHOR)AUTHOR

           Written by H. Peter Anvin.

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

           Full documentation
           <https://www.gnu.org/software/coreutils/dircolors>
           or available locally via: info '(coreutils) dircolors invocation'

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

    GNU coreutils 9.11              April 2026                   DIRCOLORS(1)

------------------------------------------------------------------------

Pages that refer to this page: [dir(1)](../man1/dir.1.html),  [ls(1)](../man1/ls.1.html),  [vdir(1)](../man1/vdir.1.html),  [dir_colors(5)](../man5/dir_colors.5.html)

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
