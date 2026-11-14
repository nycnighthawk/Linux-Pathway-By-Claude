---
{"title": "cat(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cat.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cat(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CAT(1)                        User Commands                        CAT(1)

## [](#NAME)NAME

           cat - concatenate files and print on the standard output

## [](#SYNOPSIS)SYNOPSIS

           cat [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           Concatenate FILE(s) to standard output.

           With no FILE, or when FILE is -, read standard input.

           -A, --show-all
                  equivalent to -vET

           -b, --number-nonblank
                  number nonempty output lines, overrides -n

           -e     equivalent to -vE

           -E, --show-ends
                  display $ or ^M$ at end of each line

           -n, --number
                  number all output lines

           -s, --squeeze-blank
                  suppress repeated empty output lines

           -t     equivalent to -vT

           -T, --show-tabs
                  display TAB characters as ^I

           -u     (ignored)

           -v, --show-nonprinting
                  use ^ and M- notation, except for LFD and TAB

           --help display this help and exit

           --version
                  output version information and exit

## [](#EXAMPLES)EXAMPLES

           cat f - g
                  Output f's contents, then standard input, then g's
                  contents.

           cat    Copy standard input to standard output.

## [](#AUTHOR)AUTHOR

           Written by Torbjorn Granlund and Richard M. Stallman.

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

           tac(1)

           Full documentation <https://www.gnu.org/software/coreutils/cat>
           or available locally via: info '(coreutils) cat invocation'

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

    GNU coreutils 9.11              April 2026                         CAT(1)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg(1)](../man1/dpkg.1.html),  [dpkg-query(1)](../man1/dpkg-query.1.html),  [pmlogrewrite(1)](../man1/pmlogrewrite.1.html),  [pv(1)](../man1/pv.1.html),  [rpmuncompress(1)](../man1/rpmuncompress.1.html),  [systemd-socket-activate(1)](../man1/systemd-socket-activate.1.html),  [tac(1)](../man1/tac.1.html),  [ul(1)](../man1/ul.1.html),  [proc(5)](../man5/proc.5.html),  [proc_pid_net(5)](../man5/proc_pid_net.5.html),  [proc_scsi(5)](../man5/proc_scsi.5.html),  [cpuset(7)](../man7/cpuset.7.html),  [time_namespaces(7)](../man7/time_namespaces.7.html),  [readprofile(8)](../man8/readprofile.8.html)

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
