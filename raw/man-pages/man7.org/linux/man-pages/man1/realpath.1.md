---
{"title": "realpath(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/realpath.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# realpath(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    REALPATH(1)                   User Commands                   REALPATH(1)

## [](#NAME)NAME

           realpath - print the resolved path

## [](#SYNOPSIS)SYNOPSIS

           realpath [OPTION]... FILE...

## [](#DESCRIPTION)DESCRIPTION

           Print the resolved absolute file name.

           -E, --canonicalize
                  all but the last component must exist (default)

           -e, --canonicalize-existing
                  all components of the path must exist

           -m, --canonicalize-missing
                  no path components need exist or be a directory

           -L, --logical
                  resolve '..' components before symlinks

           -P, --physical
                  resolve symlinks as encountered (default)

           -q, --quiet
                  suppress most error messages

           --relative-to=DIR
                  print the resolved path relative to DIR

           --relative-base=DIR
                  print absolute paths unless paths below DIR

           -s, --strip, --no-symlinks
                  don't expand symlinks

           -z, --zero
                  end each output line with NUL, not newline

           --help display this help and exit

           --version
                  output version information and exit

## [](#AUTHOR)AUTHOR

           Written by Padraig Brady.

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

           readlink(1), readlink(2), realpath(3)

           Full documentation
           <https://www.gnu.org/software/coreutils/realpath>
           or available locally via: info '(coreutils) realpath invocation'

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

    GNU coreutils 9.11              April 2026                    REALPATH(1)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-realpath(1)](../man1/dpkg-realpath.1.html),  [readlink(1)](../man1/readlink.1.html),  [mount(2)](../man2/mount.2.html),  [realpath(3)](../man3/realpath.3.html),  [mount(8)](../man8/mount.8.html)

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
