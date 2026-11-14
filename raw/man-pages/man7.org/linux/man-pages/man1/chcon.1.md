---
{"title": "chcon(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/chcon.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chcon(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHCON(1)                      User Commands                      CHCON(1)

## [](#NAME)NAME

           chcon - change file security context

## [](#SYNOPSIS)SYNOPSIS

           chcon [OPTION]... CONTEXT FILE...
           chcon [OPTION]... [-u USER] [-r ROLE] [-l RANGE] [-t TYPE] FILE...
           chcon [OPTION]... --reference=RFILE FILE...

## [](#DESCRIPTION)DESCRIPTION

           Change the SELinux security context of each FILE to CONTEXT.  With
           --reference, change the security context of each FILE to that of
           RFILE.

           Mandatory arguments to long options are mandatory for short
           options too.

           --dereference
                  affect the referent of each symbolic link (this is the
                  default), rather than the symbolic link itself

           -h, --no-dereference
                  affect symbolic links instead of any referenced file

           -u, --user=USER
                  set user USER in the target security context

           -r, --role=ROLE
                  set role ROLE in the target security context

           -t, --type=TYPE
                  set type TYPE in the target security context

           -l, --range=RANGE
                  set range RANGE in the target security context

           --no-preserve-root
                  do not treat '/' specially (the default)

           --preserve-root
                  fail to operate recursively on '/'

           --reference=RFILE
                  use RFILE's security context rather than specifying a
                  CONTEXT value

           -R, --recursive
                  operate on files and directories recursively

           -v, --verbose
                  output a diagnostic for every file processed

           The following options modify how a hierarchy is traversed when the
           -R option is also specified.  If more than one is specified, only
           the final one takes effect. -P is the default.

           -H     if a command line argument is a symlink to a directory,
                  traverse it

           -L     traverse every symbolic link to a directory encountered

           -P     do not traverse any symbolic links

           --help display this help and exit

           --version
                  output version information and exit

## [](#AUTHOR)AUTHOR

           Written by Russell Coker and Jim Meyering.

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

           Full documentation <https://www.gnu.org/software/coreutils/chcon>
           or available locally via: info '(coreutils) chcon invocation'

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

    GNU coreutils 9.11              April 2026                       CHCON(1)

------------------------------------------------------------------------

Pages that refer to this page: [secon(1)](../man1/secon.1.html),  [setrans.conf(5)](../man5/setrans.conf.5.html),  [chcat(8)](../man8/chcat.8.html),  [mcs(8)](../man8/mcs.8.html)

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
