---
{"title": "git-pack-refs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-pack-refs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-pack-refs(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-PACK-REFS(1)                Git Manual               GIT-PACK-REFS(1)

## [](#NAME)NAME

           git-pack-refs - Pack heads and tags for efficient repository
           access

## [](#SYNOPSIS)SYNOPSIS

           git pack-refs [--all] [--no-prune] [--auto] [--include <pattern>] [--exclude <pattern>]

## [](#DESCRIPTION)DESCRIPTION

           Traditionally, tips of branches and tags (collectively known as
           refs) were stored one file per ref in a (sub)directory under
           $GIT_DIR/refs directory. While many branch tips tend to be updated
           often, most tags and some branch tips are never updated. When a
           repository has hundreds or thousands of tags, this
           one-file-per-ref format both wastes storage and hurts performance.

           This command is used to solve the storage and performance problem
           by storing the refs in a single file, $GIT_DIR/packed-refs. When a
           ref is missing from the traditional $GIT_DIR/refs directory
           hierarchy, it is looked up in this file and used if found.

           Subsequent updates to branches always create new files under
           $GIT_DIR/refs directory hierarchy.

           A recommended practice to deal with a repository with too many
           refs is to pack its refs with --all once, and occasionally run git
           pack-refs. Tags are by definition stationary and are not expected
           to change. Branch heads will be packed with the initial pack-refs
           --all, but only the currently active branch heads will become
           unpacked, and the next pack-refs (without --all) will leave them
           unpacked.

## [](#OPTIONS)OPTIONS

           --all
               The command by default packs all tags and refs that are
               already packed, and leaves other refs alone. This is because
               branches are expected to be actively developed and packing
               their tips does not help performance. This option causes all
               refs to be packed as well, with the exception of hidden refs,
               broken refs, and symbolic refs. Useful for a repository with
               many branches of historical interests.

           --no-prune
               The command usually removes loose refs under $GIT_DIR/refs
               hierarchy after packing them. This option tells it not to.

           --auto
               Pack refs as needed depending on the current state of the ref
               database. The behavior depends on the ref format used by the
               repository and may change in the future.

               •   "files": Loose references are packed into the packed-refs
                   file based on the ratio of loose references to the size of
                   the packed-refs file. The bigger the packed-refs file, the
                   more loose references need to exist before we repack.

               •   "reftable": Tables are compacted such that they form a
                   geometric sequence. For two tables N and N+1, where N+1 is
                   newer, this maintains the property that N is at least
                   twice as big as N+1. Only tables that violate this
                   property are compacted.

           --include <pattern>
               Pack refs based on a glob(7) pattern. Repetitions of this
               option accumulate inclusion patterns. If a ref is both
               included in --include and --exclude, --exclude takes
               precedence. Using --include will preclude all tags from being
               included by default. Symbolic refs and broken refs will never
               be packed. When used with --all, it will be a noop. Use
               --no-include to clear and reset the list of patterns.

           --exclude <pattern>
               Do not pack refs matching the given glob(7) pattern.
               Repetitions of this option accumulate exclusion patterns. Use
               --no-exclude to clear and reset the list of patterns. If a ref
               is already packed, including it with --exclude will not unpack
               it.

               When used with --all, pack only loose refs which do not match
               any of the provided --exclude patterns.

               When used with --include, refs provided to --include, minus
               refs that are provided to --exclude will be packed.

## [](#BUGS)BUGS

           Older documentation written before the packed-refs mechanism was
           introduced may still say things like ".git/refs/heads/<branch>
           file exists" when it means "branch <branch> exists".

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

    Git 2.55.0.493.g5b2471          2026-08-03               GIT-PACK-REFS(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-maintenance(1)](../man1/git-maintenance.1.html),  [git-refs(1)](../man1/git-refs.1.html),  [gitrepository-layout(5)](../man5/gitrepository-layout.5.html),  [gitglossary(7)](../man7/gitglossary.7.html)

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
