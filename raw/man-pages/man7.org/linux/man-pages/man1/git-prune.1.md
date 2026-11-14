---
{"title": "git-prune(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-prune.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-prune(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-PRUNE(1)                    Git Manual                   GIT-PRUNE(1)

## [](#NAME)NAME

           git-prune - Prune all unreachable objects from the object database

## [](#SYNOPSIS)SYNOPSIS

           git prune [-n] [-v] [--progress] [--expire <time>] [--] [<head>...]

## [](#DESCRIPTION)DESCRIPTION

               Note

               In most cases, users should run git gc, which calls git prune.
               See the section "NOTES", below.

           This runs git fsck --unreachable using all the refs available in
           refs/, optionally with an additional set of objects specified on
           the command line, and prunes all unpacked objects unreachable from
           any of these head objects from the object database. In addition,
           it prunes the unpacked objects that are also found in packs by
           running git prune-packed. It also removes entries from
           .git/shallow that are not reachable by any ref.

           Note that unreachable, packed objects will remain. If this is not
           desired, see git-repack(1).

## [](#OPTIONS)OPTIONS

           -n, --dry-run
               Do not remove anything; just report what it would remove.

           -v, --verbose
               Report all removed objects.

           --progress
               Show progress.

           --expire <time>
               Only expire loose objects older than <time>.

           --
               Do not interpret any more arguments as options.

           <head>...
               In addition to objects reachable from any of our references,
               keep objects reachable from listed <head>s.

## [](#EXAMPLES)EXAMPLES

           To prune objects not used by your repository or another that
           borrows from your repository via its .git/objects/info/alternates:

               $ git prune $(cd ../another && git rev-parse --all)

## [](#NOTES)NOTES

           In most cases, users will not need to call git prune directly, but
           should instead call git gc, which handles pruning along with many
           other housekeeping tasks.

           For a description of which objects are considered for pruning, see
           git fsck's --unreachable option.

## [](#SEE_ALSO)SEE ALSO

           git-fsck(1), git-gc(1), git-reflog(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03                   GIT-PRUNE(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-gc(1)](../man1/git-gc.1.html),  [gitformat-pack(5)](../man5/gitformat-pack.5.html)

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
