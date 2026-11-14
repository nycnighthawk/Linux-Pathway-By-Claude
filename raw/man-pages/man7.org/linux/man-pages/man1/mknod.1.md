---
{"title": "mknod(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mknod.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mknod(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MKNOD(1)                      User Commands                      MKNOD(1)

## [](#NAME)NAME

           mknod - make block or character special files

## [](#SYNOPSIS)SYNOPSIS

           mknod [OPTION]... NAME TYPE [MAJOR MINOR]

## [](#DESCRIPTION)DESCRIPTION

           Create the special file NAME of the given TYPE.

           Mandatory arguments to long options are mandatory for short
           options too.

           -m, --mode=MODE
                  set file permission bits to MODE, not a=rw - umask

           -Z     set the SELinux security context to default type

           --context[=CTX]
                  like -Z, or if CTX is specified then set the SELinux or
                  SMACK security context to CTX

           --help display this help and exit

           --version
                  output version information and exit

           Both MAJOR and MINOR must be specified when TYPE is b, c, or u,
           and they must be omitted when TYPE is p.  If MAJOR or MINOR begins
           with 0x or 0X, it is interpreted as hexadecimal; otherwise, if it
           begins with 0, as octal; otherwise, as decimal.  TYPE may be:

           b      create a block (buffered) special file

           c, u   create a character (unbuffered) special file

           p      create a FIFO

           Your shell may have its own version of mknod, which usually
           supersedes the version described here.  Please refer to your
           shell's documentation for details about the options it supports.

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

           mknod(2)

           Full documentation <https://www.gnu.org/software/coreutils/mknod>
           or available locally via: info '(coreutils) mknod invocation'

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

    GNU coreutils 9.11              April 2026                       MKNOD(1)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_console(2)](../man2/ioctl_console.2.html),  [mknod(2)](../man2/mknod.2.html),  [fd(4)](../man4/fd.4.html),  [full(4)](../man4/full.4.html),  [hd(4)](../man4/hd.4.html),  [initrd(4)](../man4/initrd.4.html),  [intro(4)](../man4/intro.4.html),  [lp(4)](../man4/lp.4.html),  [mem(4)](../man4/mem.4.html),  [null(4)](../man4/null.4.html),  [ram(4)](../man4/ram.4.html),  [random(4)](../man4/random.4.html),  [tty(4)](../man4/tty.4.html),  [ttyS(4)](../man4/ttyS.4.html),  [hier(7)](../man7/hier.7.html)

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
