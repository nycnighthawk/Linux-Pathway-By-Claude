---
{"title": "git-backfill(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-backfill.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-backfill(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-BACKFILL(1)                 Git Manual                GIT-BACKFILL(1)

## [](#NAME)NAME

           git-backfill - Download missing objects in a partial clone

## [](#SYNOPSIS)SYNOPSIS

           git backfill [--min-batch-size=<n>] [--[no-]sparse] [--[no-]include-edges] [<revision-range>]

## [](#DESCRIPTION)DESCRIPTION

           Blobless partial clones are created using git clone
           --filter=blob:none and then configure the local repository such
           that the Git client avoids downloading blob objects unless they
           are required for a local operation. This initially means that the
           clone and later fetches download reachable commits and trees but
           no blobs. Later operations that change the HEAD pointer, such as
           git checkout or git merge, may need to download missing blobs in
           order to complete their operation.

           In the worst cases, commands that compute blob diffs, such as git
           blame, become very slow as they download the missing blobs in
           single-blob requests to satisfy the missing object as the Git
           command needs it. This leads to multiple download requests and no
           ability for the Git server to provide delta compression across
           those objects.

           The git backfill command provides a way for the user to request
           that Git downloads the missing blobs (with optional filters) such
           that the missing blobs representing historical versions of files
           can be downloaded in batches. The backfill command attempts to
           optimize the request by grouping blobs that appear at the same
           path, hopefully leading to good delta compression in the packfile
           sent by the server.

           In this way, git backfill provides a mechanism to break a large
           clone into smaller chunks. Starting with a blobless partial clone
           with git clone --filter=blob:none and then running git backfill in
           the local repository provides a way to download all reachable
           objects in several smaller network calls than downloading the
           entire repository at clone time.

           By default, git backfill downloads all blobs reachable from the
           HEAD commit. This set can be restricted or expanded using various
           options below.

           THIS COMMAND IS EXPERIMENTAL. ITS BEHAVIOR MAY CHANGE IN THE
           FUTURE.

## [](#OPTIONS)OPTIONS

           --min-batch-size=<n>
               Specify a minimum size for a batch of missing objects to
               request from the server. This size may be exceeded by the last
               set of blobs seen at a given path. The default minimum batch
               size is 50,000.

           --sparse, --no-sparse
               Only download objects if they appear at a path that matches
               the current sparse-checkout. If the sparse-checkout feature is
               enabled, then --sparse is assumed and can be disabled with
               --no-sparse.

           --include-edges, --no-include-edges
               Include blobs from boundary commits in the backfill. Useful in
               preparation for commands like git log -p A..B or git replay
               --onto TARGET A..B, where A..B normally excludes A but you
               need the blobs from A as well.  --include-edges is the
               default.

           <revision-range>
               Backfill only blobs reachable from commits in the specified
               revision range. When no <revision-range> is specified, it
               defaults to HEAD (i.e. the whole history leading to the
               current commit). For a complete list of ways to spell
               <revision-range>, see the "Specifying Ranges" section of
               gitrevisions(7).

               You may also use commit-limiting options understood by
               git-rev-list(1) such as --first-parent, --since, or pathspecs.

               Most --filter=<spec> options don’t work with the purpose of
               git backfill, but the sparse:<oid> filter is integrated to
               provide a focused set of paths to download, distinct from the
               --sparse option.

## [](#SEE_ALSO)SEE ALSO

           git-clone(1), git-rev-list(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03                GIT-BACKFILL(1)

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
