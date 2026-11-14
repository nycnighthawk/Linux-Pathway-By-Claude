---
{"title": "chsh(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/chsh.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chsh(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [VALID SHELLS](#VALID_SHELLS) \| [EXIT STATUS](#EXIT_STATUS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHSH(1)                       User Commands                       CHSH(1)

## [](#NAME)NAME

           chsh - change your login shell

## [](#SYNOPSIS)SYNOPSIS

           chsh [-s shell] [-l] [-h] [-V] [username|UID]

## [](#DESCRIPTION)DESCRIPTION

           chsh is used to change your login shell. If a shell is not given
           on the command line, chsh prompts for one.

           chsh supports non-local entries (kerberos, LDAP, etc.) if linked
           with libuser, otherwise use ypchsh(1), lchsh(1) or any other
           implementation for non-local entries.

## [](#OPTIONS)OPTIONS

           -s, --shell shell
               Specify your login shell.

           -l, --list-shells
               Print the list of shells listed in /etc/shells and exit.

           -h, --help
               Display help text and exit. (Short option -h is used since
               version 2.30; older versions used the now-deprecated -u).

           -V, --version
               Display version and exit. (Short option -V is used since
               version 2.39; older versions used the now-deprecated -v).

## [](#VALID_SHELLS)VALID SHELLS

           chsh will accept the full pathname of any executable file on the
           system.

           The default behavior for unprivileged users is to accept only
           shells listed in the /etc/shells file, and issue a warning for
           root user. It can also be configured at compile-time to only issue
           a warning for all users.

## [](#EXIT_STATUS)EXIT STATUS

           Returns 0 if operation was successful, 1 if operation failed or
           command syntax was not valid.

## [](#AUTHORS)AUTHORS

           Salvatore Valente <svalente@mit.edu>

## [](#SEE_ALSO)SEE ALSO

           login(1), login.defs(5), passwd(5), shells(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The chsh command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                        CHSH(1)

------------------------------------------------------------------------

Pages that refer to this page: [chfn(1)](../man1/chfn.1.html),  [chfn(1@@shadow-utils)](../man1/chfn.1@@shadow-utils.html),  [passwd(5)](../man5/passwd.5.html),  [shells(5)](../man5/shells.5.html),  [groupadd(8)](../man8/groupadd.8.html),  [groupdel(8)](../man8/groupdel.8.html),  [groupmems(8)](../man8/groupmems.8.html),  [groupmod(8)](../man8/groupmod.8.html),  [useradd(8)](../man8/useradd.8.html),  [userdel(8)](../man8/userdel.8.html),  [usermod(8)](../man8/usermod.8.html)

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
