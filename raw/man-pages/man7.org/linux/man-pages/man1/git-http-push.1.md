---
{"title": "git-http-push(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-http-push.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-http-push(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SPECIFYING THE REFS](#SPECIFYING_THE_REFS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-HTTP-PUSH(1)                Git Manual               GIT-HTTP-PUSH(1)

## [](#NAME)NAME

           git-http-push - Push objects over HTTP/DAV to another repository

## [](#SYNOPSIS)SYNOPSIS

           git http-push [--all] [--dry-run] [--force] [--verbose] <URL> <ref> [<ref>...]

## [](#DESCRIPTION)DESCRIPTION

           Sends missing objects to the remote repository, and updates the
           remote branch.

           NOTE: This command is temporarily disabled if your libcurl is
           older than 7.16, as the combination has been reported not to work
           and sometimes corrupts the repository.

## [](#OPTIONS)OPTIONS

           --all
               Do not assume that the remote repository is complete in its
               current state, and verify all objects in the entire local
               ref’s history exist in the remote repository.

           --force
               Usually, the command refuses to update a remote ref that is
               not an ancestor of the local ref used to overwrite it. This
               flag disables the check. What this means is that the remote
               repository can lose commits; use it with care.

           --dry-run
               Do everything except actually send the updates.

           --verbose
               Report the list of objects being walked locally and the list
               of objects successfully sent to the remote repository.

           -d, -D
               Remove <ref> from remote repository. The specified branch
               cannot be the remote HEAD. If -d is specified, the following
               other conditions must also be met:

               •   Remote HEAD must resolve to an object that exists locally

               •   Specified branch resolves to an object that exists locally

               •   Specified branch is an ancestor of the remote HEAD

           <ref>...
               The remote refs to update.

## [](#SPECIFYING_THE_REFS)SPECIFYING THE REFS

           A <ref> specification can be either a single pattern, or a pair of
           such patterns separated by a colon ":" (this means that a ref name
           cannot have a colon in it). A single pattern <name> is just a
           shorthand for <name>:<name>.

           Each pattern pair <src>:<dst> consists of the source side (before
           the colon) and the destination side (after the colon). The ref to
           be pushed is determined by finding a match that matches the source
           side, and where it is pushed is determined by using the
           destination side.

           •   It is an error if <src> does not match exactly one of the
               local refs.

           •   If <dst> does not match any remote ref, either

               •   it has to start with "refs/"; <dst> is used as the
                   destination literally in this case.

               •   <src> == <dst> and the ref that matched the <src> must not
                   exist in the set of remote refs; the ref matched <src>
                   locally is used as the name of the destination.

           Without ‘--force`, the <src> ref is stored at the remote only if
           <dst> does not exist, or <dst> is a proper subset (i.e. an
           ancestor) of <src>. This check, known as "fast-forward check", is
           performed to avoid accidentally overwriting the remote ref and
           losing other peoples’ commits from there.

           With --force, the fast-forward check is disabled for all refs.

           Optionally, a <ref> parameter can be prefixed with a plus + sign
           to disable the fast-forward check only on that ref.

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

    Git 2.55.0.493.g5b2471          2026-08-03               GIT-HTTP-PUSH(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html)

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
