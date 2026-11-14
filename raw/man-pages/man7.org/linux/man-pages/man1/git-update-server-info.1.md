---
{"title": "git-update-server-info(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-update-server-info.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-update-server-info(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OUTPUT](#OUTPUT) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-UPDATE-SERVER-INFO(1)       Git Manual      GIT-UPDATE-SERVER-INFO(1)

## [](#NAME)NAME

           git-update-server-info - Update auxiliary info file to help dumb
           servers

## [](#SYNOPSIS)SYNOPSIS

           git update-server-info [-f | --force]

## [](#DESCRIPTION)DESCRIPTION

           A dumb server that does not do on-the-fly pack generations must
           have some auxiliary information files in $GIT_DIR/info and
           $GIT_OBJECT_DIRECTORY/info directories to help clients discover
           what references and packs the server has. This command generates
           such auxiliary files.

## [](#OPTIONS)OPTIONS

           -f, --force
               Update the info files from scratch.

## [](#OUTPUT)OUTPUT

           Currently the command updates the following files. Please see
           gitrepository-layout(5) for a description of what they are for:

           •   objects/info/packs

           •   info/refs

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

    Git 2.55.0.493.g5b2471          2026-08-03      GIT-UPDATE-SERVER-INFO(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-config(1)](../man1/git-config.1.html),  [git-repack(1)](../man1/git-repack.1.html)

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
