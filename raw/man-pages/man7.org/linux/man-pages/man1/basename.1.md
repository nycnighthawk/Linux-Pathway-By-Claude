---
{"title": "basename(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/basename.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# basename(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    BASENAME(1)                   User Commands                   BASENAME(1)

## [](#NAME)NAME

           basename - strip directory and suffix from filenames

## [](#SYNOPSIS)SYNOPSIS

           basename NAME [SUFFIX]
           basename OPTION... NAME...

## [](#DESCRIPTION)DESCRIPTION

           Print NAME with any leading directory components removed.  If
           specified, also remove a trailing SUFFIX.

           Mandatory arguments to long options are mandatory for short
           options too.

           -a, --multiple
                  support multiple arguments and treat each as a NAME

           -s, --suffix=SUFFIX
                  remove a trailing SUFFIX; implies -a

           -z, --zero
                  end each output line with NUL, not newline

           --help display this help and exit

           --version
                  output version information and exit

## [](#EXAMPLES)EXAMPLES

           basename /usr/bin/sort
                  -> "sort"

           basename include/stdio.h .h
                  -> "stdio"

           basename -s .h include/stdio.h
                  -> "stdio"

           basename -a any/str1 any/str2
                  -> "str1" followed by "str2"

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

           dirname(1), readlink(1)

           Full documentation
           <https://www.gnu.org/software/coreutils/basename>
           or available locally via: info '(coreutils) basename invocation'

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

    GNU coreutils 9.11              April 2026                    BASENAME(1)

------------------------------------------------------------------------

Pages that refer to this page: [dirname(1)](../man1/dirname.1.html),  [pmsignal(1)](../man1/pmsignal.1.html),  [basename(3)](../man3/basename.3.html),  [rpm-dependency-generators(7)](../man7/rpm-dependency-generators.7.html),  [rpm-macros(7)](../man7/rpm-macros.7.html)

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
