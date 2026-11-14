---
{"title": "runcon(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/runcon.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# runcon(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RUNCON(1)                     User Commands                     RUNCON(1)

## [](#NAME)NAME

           runcon - run command with specified security context

## [](#SYNOPSIS)SYNOPSIS

           runcon [CONTEXT COMMAND [ARG]...]
           runcon [-c] [-u USER] [-r ROLE] [-t TYPE] [-l RANGE] COMMAND
           [ARG]...

## [](#DESCRIPTION)DESCRIPTION

           Run COMMAND with completely-specified CONTEXT, or with current or
           transitioned security context modified by one or more of LEVEL,
           ROLE, TYPE, and USER.

           If none of -c, -t, -u, -r, or -l, is specified, the first argument
           is used as the complete context.  Any additional arguments after
           COMMAND are interpreted as arguments to the command.

           Only carefully-chosen contexts are likely to run successfully.

           Run a program in a different SELinux security context.  With
           neither CONTEXT nor COMMAND, print the current security context.

           Mandatory arguments to long options are mandatory for short
           options too.

           CONTEXT
                  Complete security context

           -c, --compute
                  compute process transition context before modifying

           -t, --type=TYPE
                  type (for same role as parent)

           -u, --user=USER
                  user identity

           -r, --role=ROLE
                  role

           -l, --range=RANGE
                  levelrange

           --help display this help and exit

           --version
                  output version information and exit

       Exit status:
           125    if the runcon command itself fails

           126    if COMMAND is found but cannot be invoked

           127    if COMMAND cannot be found

           -      the exit status of COMMAND otherwise

## [](#AUTHOR)AUTHOR

           Written by Russell Coker.

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

           Full documentation <https://www.gnu.org/software/coreutils/runcon>
           or available locally via: info '(coreutils) runcon invocation'

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

    GNU coreutils 9.11              April 2026                      RUNCON(1)

------------------------------------------------------------------------

Pages that refer to this page: [newrole(1)](../man1/newrole.1.html),  [setpriv(1)](../man1/setpriv.1.html),  [run_init(8)](../man8/run_init.8.html),  [sandbox(8)](../man8/sandbox.8.html),  [seunshare(8)](../man8/seunshare.8.html)

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
