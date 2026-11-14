---
{"title": "readlink(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/readlink.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# readlink(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    READLINK(1)                   User Commands                   READLINK(1)

## [](#NAME)NAME

           readlink - print resolved symbolic links or canonical file names

## [](#SYNOPSIS)SYNOPSIS

           readlink [OPTION]... FILE...

## [](#DESCRIPTION)DESCRIPTION

           realpath(1) is a better command for canonicalization
           functionality.

           Print value of a symbolic link or canonical file name

           -f, --canonicalize
                  canonicalize by following every symlink in every component
                  of the given name recursively; all but the last component
                  must exist

           -e, --canonicalize-existing
                  canonicalize by following every symlink in every component
                  of the given name recursively; all components must exist

           -m, --canonicalize-missing
                  canonicalize by following every symlink in every component
                  of the given name recursively, without requirements on
                  components existence

           -n, --no-newline
                  do not output the trailing delimiter

           -q, --quiet

           -s, --silent
                  suppress most error messages (on by default if
                  POSIXLY_CORRECT is not set)

           -v, --verbose
                  report error messages (on by default if POSIXLY_CORRECT is
                  set)

           -z, --zero
                  end each output line with NUL, not newline

           --help display this help and exit

           --version
                  output version information and exit

## [](#AUTHOR)AUTHOR

           Written by Dmitry V. Levin.

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

           readlink(2), realpath(1), realpath(3)

           Full documentation
           <https://www.gnu.org/software/coreutils/readlink>
           or available locally via: info '(coreutils) readlink invocation'

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

    GNU coreutils 9.11              April 2026                    READLINK(1)

------------------------------------------------------------------------

Pages that refer to this page: [basename(1)](../man1/basename.1.html),  [dirname(1)](../man1/dirname.1.html),  [dpkg-realpath(1)](../man1/dpkg-realpath.1.html),  [realpath(1)](../man1/realpath.1.html),  [unshare(1)](../man1/unshare.1.html),  [mount(2)](../man2/mount.2.html),  [readlink(2)](../man2/readlink.2.html),  [unshare(2)](../man2/unshare.2.html),  [namespaces(7)](../man7/namespaces.7.html),  [mount(8)](../man8/mount.8.html)

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
