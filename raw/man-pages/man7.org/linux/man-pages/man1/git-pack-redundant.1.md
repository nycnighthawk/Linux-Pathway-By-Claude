---
{"title": "git-pack-redundant(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-pack-redundant.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-pack-redundant(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [WARNING](#WARNING) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-PACK-REDUNDANT(1)           Git Manual          GIT-PACK-REDUNDANT(1)

## [](#NAME)NAME

           git-pack-redundant - Find redundant pack files

## [](#SYNOPSIS)SYNOPSIS

           git pack-redundant [--verbose] [--alt-odb] (--all | <pack-filename>...)

## [](#WARNING)WARNING

           git pack-redundant has been deprecated and is scheduled for
           removal in a future version of Git. Because it can only remove
           entire duplicate packs and not individual duplicate objects, it is
           generally not a useful tool for reducing repository size. You are
           better off using git gc to do so, which will put objects into a
           new pack, removing duplicates.

           Running pack-redundant without the --i-still-use-this flag will
           fail in this release. If you believe you have a use case for which
           pack-redundant is better suited and oppose this removal, please
           contact the Git mailing list at git@vger.kernel.org[1]. More
           information about the list is available at
           https://git-scm.com/community .

## [](#DESCRIPTION)DESCRIPTION

           This program computes which packs in your repository are
           redundant. The output is suitable for piping to xargs rm if you
           are in the root of the repository.

           git pack-redundant accepts a list of objects on standard input.
           Any objects given will be ignored when checking which packs are
           required. This makes the following command useful when wanting to
           remove packs which contain unreachable objects.

           git fsck --full --unreachable | cut -d ' ' -f3 | \ git
           pack-redundant --all | xargs rm

## [](#OPTIONS)OPTIONS

           --all
               Processes all packs. Any filenames on the command line are
               ignored.

           --alt-odb
               Don’t require objects present in packs from alternate object
               database (odb) directories to be present in local packs.

           --verbose
               Outputs some statistics to stderr. Has a small performance
               penalty.

## [](#SEE_ALSO)SEE ALSO

           git-pack-objects(1) git-repack(1) git-prune-packed(1)

## [](#GIT)GIT

           Part of the git(1) suite

## [](#NOTES)NOTES

            1. git@vger.kernel.org
               mailto:git@vger.kernel.org

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

    Git 2.55.0.493.g5b2471          2026-08-03          GIT-PACK-REDUNDANT(1)

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
