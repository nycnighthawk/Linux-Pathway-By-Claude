---
{"title": "id(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/id.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# id(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ID(1)                         User Commands                         ID(1)

## [](#NAME)NAME

           id - print real and effective user and group IDs

## [](#SYNOPSIS)SYNOPSIS

           id [OPTION]... [USER]...

## [](#DESCRIPTION)DESCRIPTION

           Print user and group information for each specified USER, or (when
           USER omitted) for the current process.

           -a     ignore, for compatibility with other versions

           -Z, --context
                  print only the security context of the process

           -g, --group
                  print only the effective group ID

           -G, --groups
                  print all group IDs

           -n, --name
                  print a name instead of a number, for -u,-g,-G

           -r, --real
                  print the real ID instead of the effective ID, with
                  -u,-g,-G

           -u, --user
                  print only the effective user ID

           -z, --zero
                  delimit entries with NUL characters, not whitespace; not
                  permitted in default format

           --help display this help and exit

           --version
                  output version information and exit

           Without any OPTION, print some useful set of identified
           information.

## [](#AUTHOR)AUTHOR

           Written by Arnold Robbins and David MacKenzie.

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

           Full documentation <https://www.gnu.org/software/coreutils/id>
           or available locally via: info '(coreutils) id invocation'

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

    GNU coreutils 9.11              April 2026                          ID(1)

------------------------------------------------------------------------

Pages that refer to this page: [newgrp(1)](../man1/newgrp.1.html),  [sg(1)](../man1/sg.1.html),  [strace(1)](../man1/strace.1.html),  [credentials(7)](../man7/credentials.7.html)

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
