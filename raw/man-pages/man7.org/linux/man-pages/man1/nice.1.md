---
{"title": "nice(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/nice.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nice(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NICE(1)                       User Commands                       NICE(1)

## [](#NAME)NAME

           nice - run a program with modified scheduling priority

## [](#SYNOPSIS)SYNOPSIS

           nice [OPTION] [COMMAND [ARG]...]

## [](#DESCRIPTION)DESCRIPTION

           Run COMMAND with an adjusted niceness, which affects process
           scheduling.  With no COMMAND, print the current niceness.
           Niceness values range from -20 (most favorable to the process) to
           19 (least favorable to the process).

           Mandatory arguments to long options are mandatory for short
           options too.

           -n, --adjustment=N
                  add integer N to the niceness (default 10)

           --help display this help and exit

           --version
                  output version information and exit

           Your shell may have its own version of nice, which usually
           supersedes the version described here.  Please refer to your
           shell's documentation for details about the options it supports.

       Exit status:
           125    if the nice command itself fails

           126    if COMMAND is found but cannot be invoked

           127    if COMMAND cannot be found

           -      the exit status of COMMAND otherwise

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

           nice(2), renice(1)

           Full documentation <https://www.gnu.org/software/coreutils/nice>
           or available locally via: info '(coreutils) nice invocation'

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

    GNU coreutils 9.11              April 2026                        NICE(1)

------------------------------------------------------------------------

Pages that refer to this page: [chrt(1)](../man1/chrt.1.html),  [coresched(1)](../man1/coresched.1.html),  [kill(1@@procps-ng)](../man1/kill.1@@procps-ng.html),  [ps(1)](../man1/ps.1.html),  [renice(1)](../man1/renice.1.html),  [skill(1)](../man1/skill.1.html),  [taskset(1)](../man1/taskset.1.html),  [uclampset(1)](../man1/uclampset.1.html),  [getpriority(2)](../man2/getpriority.2.html),  [nice(2)](../man2/nice.2.html),  [sched(7)](../man7/sched.7.html),  [ovs-ctl(8)](../man8/ovs-ctl.8.html)

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
