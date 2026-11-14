---
{"title": "git-remote-fd(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-remote-fd.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-remote-fd(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-REMOTE-FD(1)                Git Manual               GIT-REMOTE-FD(1)

## [](#NAME)NAME

           git-remote-fd - Reflect smart transport stream back to caller

## [](#SYNOPSIS)SYNOPSIS

           "fd::<infd>[,<outfd>][/<anything>]" (as URL)

## [](#DESCRIPTION)DESCRIPTION

           This helper uses specified file descriptors to connect to a remote
           Git server. This is not meant for end users but for programs and
           scripts calling git fetch, push, or archive.

           If only <infd> is given, it is assumed to be a bidirectional
           socket connected to a remote Git server (git-upload-pack,
           git-receive-pack, or git-upload-archive). If both <infd> and
           <outfd> are given, they are assumed to be pipes connected to a
           remote Git server (<infd> being the inbound pipe and <outfd> being
           the outbound pipe).

           It is assumed that any handshaking procedures have already been
           completed (such as sending service request for git://) before this
           helper is started.

           <anything> can be any string. It is ignored. It is meant for
           providing information to the user in the URL in case that URL is
           displayed in some context.

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           GIT_TRANSLOOP_DEBUG
               If set, prints debugging information about various
               reads/writes.

## [](#EXAMPLES)EXAMPLES

           git fetch fd::17 master
               Fetch master, using file descriptor #17 to communicate with
               git-upload-pack.

           git fetch fd::17/foo master
               Same as above.

           git push fd::7,8 master (as URL)
               Push master, using file descriptor #7 to read data from
               git-receive-pack and file descriptor #8 to write data to the
               same service.

           git push fd::7,8/bar master
               Same as above.

## [](#SEE_ALSO)SEE ALSO

           gitremote-helpers(7)

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

    Git 2.55.0.493.g5b2471          2026-08-03               GIT-REMOTE-FD(1)

------------------------------------------------------------------------

Pages that refer to this page: [gitremote-helpers(7)](../man7/gitremote-helpers.7.html)

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
