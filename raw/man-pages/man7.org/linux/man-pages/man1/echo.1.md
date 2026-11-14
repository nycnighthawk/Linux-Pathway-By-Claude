---
{"title": "echo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/echo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# echo(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ECHO(1)                       User Commands                       ECHO(1)

## [](#NAME)NAME

           echo - display a line of text

## [](#SYNOPSIS)SYNOPSIS

           echo [SHORT-OPTION]... [STRING]...
           echo LONG-OPTION

## [](#DESCRIPTION)DESCRIPTION

           Echo the STRING(s) to standard output.

           -n     do not output the trailing newline

           -e     enable interpretation of backslash escapes

           -E     disable interpretation of backslash escapes (default)

           --help display this help and exit

           --version
                  output version information and exit

           If -e is in effect, the following sequences are recognized:

           \\     backslash

           \a     alert (BEL)

           \b     backspace

           \c     produce no further output

           \e     escape

           \f     form feed

           \n     new line

           \r     carriage return

           \t     horizontal tab

           \v     vertical tab

           \0NNN  byte with octal value NNN (1 to 3 digits)

           \xHH   byte with hexadecimal value HH (1 to 2 digits)

           Your shell may have its own version of echo, which usually
           supersedes the version described here.  Please refer to your
           shell's documentation for details about the options it supports.

           Consider using the printf(1) command instead, as it avoids
           problems when outputting option-like strings.

## [](#AUTHOR)AUTHOR

           Written by Brian Fox and Chet Ramey.

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

           printf(1)

           Full documentation <https://www.gnu.org/software/coreutils/echo>
           or available locally via: info '(coreutils) echo invocation'

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

    GNU coreutils 9.11              April 2026                        ECHO(1)

------------------------------------------------------------------------

Pages that refer to this page: [ldapcompare(1)](../man1/ldapcompare.1.html),  [systemd-ask-password(1)](../man1/systemd-ask-password.1.html),  [systemd-run(1)](../man1/systemd-run.1.html),  [cpuset(7)](../man7/cpuset.7.html)

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
