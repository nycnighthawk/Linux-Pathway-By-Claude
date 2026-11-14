---
{"title": "git-patch-id(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-patch-id.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-patch-id(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-PATCH-ID(1)                 Git Manual                GIT-PATCH-ID(1)

## [](#NAME)NAME

           git-patch-id - Compute unique IDs for patches

## [](#SYNOPSIS)SYNOPSIS

           git patch-id [--stable | --unstable | --verbatim]

## [](#DESCRIPTION)DESCRIPTION

           Read patches from standard input and compute the patch IDs.

           A "patch ID" is nothing but a sum of SHA-1 of the file diffs
           associated with a patch, with line numbers ignored. As such, it’s
           "reasonably stable", but at the same time also reasonably unique,
           i.e., two patches that have the same "patch ID" are almost
           guaranteed to be the same thing.

           The main usecase for this command is to look for likely duplicate
           commits.

           When dealing with git diff-tree --patch output, it takes advantage
           of the fact that the patch is prefixed with the object name of the
           commit, and outputs two 40-byte hexadecimal strings. The first
           string is the patch ID, and the second string is the commit ID.
           This can be used to make a mapping from patch ID to commit ID for
           a set or range of commits.

## [](#OPTIONS)OPTIONS

           --verbatim
               Calculate the patch ID of the input as it is given, do not
               strip any whitespace. Implies --stable and forbids --unstable.

               This is the default if patchid.verbatim is true.

           --stable
               Use a "stable" sum of hashes as the patch ID. With this
               option:

               •   Reordering file diffs that make up a patch does not affect
                   the ID. In particular, two patches produced by comparing
                   the same two trees with two different settings for
                   -O<orderfile> result in the same patch ID signature,
                   thereby allowing the computed result to be used as a key
                   to index some meta-information about the change between
                   the two trees.

               •   The result is different from the value produced by Git 1.9
                   and older or produced when an "unstable" hash (see
                   --unstable below) is configured - even when used on a diff
                   output taken without any use of -O<orderfile>, thereby
                   making existing databases storing such "unstable" or
                   historical patch IDs unusable.

               •   All whitespace within the patch is ignored and does not
                   affect the ID.

               This is the default if patchid.stable is set to true.

           --unstable
               Use an "unstable" hash as the patch ID. With this option, the
               result produced is compatible with the patch ID value produced
               by Git 1.9 and older and whitespace is ignored. Users with
               pre-existing databases storing patch IDs produced by Git 1.9
               and older (who do not deal with reordered patches) may want to
               use this option.

               This is the default.

## [](#EXAMPLES)EXAMPLES

           git-cherry(1) shows what commits from a branch have patch ID
           equivalent commits in some upstream branch. But it only tells you
           whether such a commit exists or not. What if you wanted to know
           the relevant commits in the upstream? We can use this command to
           make a mapping between your branch and the upstream branch:

               #!/bin/sh

               upstream="$1"
               branch="$2"
               test -z "$branch" && branch=HEAD
               limit="$3"
               if test -n "$limit"
               then
                   tail_opts="$limit".."$upstream"
               else
                   since=$(git log --format=%aI "$upstream".."$branch" | tail -1)
                   tail_opts=--since="$since"' '"$upstream"
               fi
               for_branch=$(mktemp)
               for_upstream=$(mktemp)

               git rev-list --no-merges "$upstream".."$branch" |
                   git diff-tree --patch --stdin |
                   git patch-id  --stable | sort >"$for_branch"
               git rev-list --no-merges $tail_opts |
                   git diff-tree --patch --stdin |
                   git patch-id  --stable | sort >"$for_upstream"
               join -a1 "$for_branch" "$for_upstream" | cut -d' ' -f2,3
               rm "$for_branch"
               rm "$for_upstream"

           Now the first column shows the commit from your branch and the
           second column shows the patch ID equivalent commit, if it exists.

## [](#SEE_ALSO)SEE ALSO

           git-cherry(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03                GIT-PATCH-ID(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-cherry(1)](../man1/git-cherry.1.html),  [git-range-diff(1)](../man1/git-range-diff.1.html)

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
