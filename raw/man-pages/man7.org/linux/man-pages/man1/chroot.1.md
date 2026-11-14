---
{"title": "chroot(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/chroot.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chroot(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHROOT(1)                     User Commands                     CHROOT(1)

## [](#NAME)NAME

           chroot - run command or interactive shell with special root
           directory

## [](#SYNOPSIS)SYNOPSIS

           chroot [OPTION]... NEWROOT [COMMAND [ARG]...]

## [](#DESCRIPTION)DESCRIPTION

           Run COMMAND with root directory set to NEWROOT.

           --groups=G_LIST
                  specify supplementary groups as g1,g2,..,gN

           --userspec=USER:GROUP
                  specify user and group (ID or name) to use

           --skip-chdir
                  do not change working directory to '/'

           --help display this help and exit

           --version
                  output version information and exit

           If no command is given, run '"$SHELL" -i' (default: '/bin/sh -i').

       Exit status:
           125    if the chroot command itself fails

           126    if COMMAND is found but cannot be invoked

           127    if COMMAND cannot be found

           -      the exit status of COMMAND otherwise

## [](#AUTHOR)AUTHOR

           Written by Roland McGrath.

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

           chroot(2)

           Full documentation <https://www.gnu.org/software/coreutils/chroot>
           or available locally via: info '(coreutils) chroot invocation'

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

    GNU coreutils 9.11              April 2026                      CHROOT(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [chroot(2)](../man2/chroot.2.html),  [lxc.container.conf(5)](../man5/lxc.container.conf.5.html),  [mount_namespaces(7)](../man7/mount_namespaces.7.html),  [btrfs-receive(8)](../man8/btrfs-receive.8.html),  [pivot_root(8)](../man8/pivot_root.8.html)

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
