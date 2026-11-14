---
{"title": "sg(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/sg.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sg(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SG(1)                         User Commands                         SG(1)

## [](#NAME)NAME

           sg - execute command as different group ID

## [](#SYNOPSIS)SYNOPSIS

           sg [-] group [[-c] command]

## [](#DESCRIPTION)DESCRIPTION

           The sg command works similar to newgrp but accepts a command. The
           command will be executed with the /bin/sh shell. With most shells
           you may run sg from, you need to enclose multi-word commands in
           quotes. Another difference between newgrp and sg is that some
           shells treat newgrp specially, replacing themselves with a new
           instance of a shell that newgrp creates. This doesn't happen with
           sg, so upon exit from an sg command you are returned to your
           previous group ID.

## [](#OPTIONS)OPTIONS

           The options which apply to the sg command are:

           -, -l
               Start the shell as a login shell.

           -c
               Specify a command that will be invoked by the shell using its
               -c.

               This is the default; for backward compatibility.

## [](#CONFIGURATION)CONFIGURATION

           The following configuration variables in /etc/login.defs change
           the behavior of this tool:

           SYSLOG_SG_ENAB (boolean)
               Enable "syslog" logging of sg activity.

## [](#FILES)FILES

           /etc/passwd
               User account information.

           /etc/shadow
               Secure user account information.

           /etc/group
               Group account information.

           /etc/gshadow
               Secure group account information.

## [](#SEE_ALSO)SEE ALSO

           id(1), login(1), newgrp(1), su(1), gpasswd(1), group(5),
           gshadow(5).

## [](#COLOPHON)COLOPHON

           This page is part of the shadow-utils (utilities for managing
           accounts and shadow password files) project.  Information about
           the project can be found at 
           ⟨https://github.com/shadow-maint/shadow⟩.  If you have a bug report
           for this manual page, send it to
           pkg-shadow-devel@alioth-lists.debian.net.  This page was obtained
           from the tarball shadow-4.19.0.tar fetched from
           ⟨https://github.com/shadow-maint/shadow/releases⟩ on 2026-08-04.
           If you discover any rendering problems in this HTML version of the
           page, or you believe there is a better or more up-to-date source
           for the page, or you have corrections or improvements to the
           information in this COLOPHON (which is not part of the original
           manual page), send a mail to man-pages@man7.org

    shadow-utils 4.19.0             08/04/2026                          SG(1)

------------------------------------------------------------------------

Pages that refer to this page: [newgrp(1)](../man1/newgrp.1.html),  [su(1@@shadow-utils)](../man1/su.1@@shadow-utils.html),  [group(5)](../man5/group.5.html),  [credentials(7)](../man7/credentials.7.html)

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
