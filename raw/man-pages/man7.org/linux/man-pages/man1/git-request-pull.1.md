---
{"title": "git-request-pull(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-request-pull.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-request-pull(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-REQUEST-PULL(1)             Git Manual            GIT-REQUEST-PULL(1)

## [](#NAME)NAME

           git-request-pull - Generates a summary of pending changes

## [](#SYNOPSIS)SYNOPSIS

           git request-pull [-p] <start> <URL> [<end>]

## [](#DESCRIPTION)DESCRIPTION

           Generate a request asking your upstream project to pull changes
           into their tree. The request, printed to the standard output,
           begins with the branch description, summarizes the changes, and
           indicates from where they can be pulled.

           The upstream project is expected to have the commit named by
           <start> and the output asks it to integrate the changes you made
           since that commit, up to the commit named by <end>, by visiting
           the repository named by <URL>.

## [](#OPTIONS)OPTIONS

           -p
               Include patch text in the output.

           <start>
               Commit to start at. This names a commit that is already in the
               upstream history.

           <URL>
               The repository URL to be pulled from.

           <end>
               Commit to end at (defaults to HEAD). This names the commit at
               the tip of the history you are asking to be pulled.

               When the repository named by <URL> has the commit at a tip of
               a ref that is different from the ref you have locally, you can
               use the <local>:<remote> syntax, to have its local name, a
               colon :, and its remote name.

## [](#EXAMPLES)EXAMPLES

           Imagine that you built your work on your master branch on top of
           the v1.0 release, and want it to be integrated into the project.
           First you push that change to your public repository for others to
           see:

               git push https://git.ko.xz/project master

           Then, you run this command:

               git request-pull v1.0 https://git.ko.xz/project master

           which will produce a request to the upstream, summarizing the
           changes between the v1.0 release and your master, to pull it from
           your public repository.

           If you pushed your change to a branch whose name is different from
           the one you have locally, e.g.

               git push https://git.ko.xz/project master:for-linus

           then you can ask that to be pulled with

               git request-pull v1.0 https://git.ko.xz/project master:for-linus

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

    Git 2.55.0.493.g5b2471          2026-08-03            GIT-REQUEST-PULL(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [giteveryday(7)](../man7/giteveryday.7.html),  [gitworkflows(7)](../man7/gitworkflows.7.html)

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
