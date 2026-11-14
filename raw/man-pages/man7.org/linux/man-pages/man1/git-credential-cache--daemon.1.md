---
{"title": "git-credential-cache--daemon(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-credential-cache--daemon.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-credential-cache\--daemon(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-CREDENTIAL-CACHE--DAEMON(1) Git ManualGIT-CREDENTIAL-CACHE--DAEMON(1)

## [](#NAME)NAME

           git-credential-cache--daemon - Temporarily store user credentials
           in memory

## [](#SYNOPSIS)SYNOPSIS

           git credential-cache--daemon [--debug] <socket-path>

## [](#DESCRIPTION)DESCRIPTION

               Note

               You probably don’t want to invoke this command yourself; it is
               started automatically when you use git-credential-cache(1).

           This command listens on the Unix domain socket specified by
           <socket-path> for git-credential-cache clients. Clients may store
           and retrieve credentials. Each credential is held for a timeout
           specified by the client; once no credentials are held, the daemon
           exits.

           If the --debug option is specified, the daemon does not close its
           stderr stream, and may output extra diagnostics to it even after
           it has begun listening for clients.

## [](#GIT)GIT

           Part of the git(1) suite

## [](#COLOPHON)COLOPHON

           This page is part of the git (Git distributed version control
           system) project.  Information about the project can be found at 
           ⟨http://git-scm.com/⟩.  If you have a bug report for this manual
           page, see ⟨http://git-scm.com/community⟩.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/git/git.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Git 2.55.0.493.g5b2471          2026-08-03GIT-CREDENTIAL-CACHE--DAEMON(1)

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
