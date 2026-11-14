---
{"title": "git-mktag(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-mktag.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-mktag(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [TAG FORMAT](#TAG_FORMAT) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-MKTAG(1)                    Git Manual                   GIT-MKTAG(1)

## [](#NAME)NAME

           git-mktag - Creates a tag object with extra validation

## [](#SYNOPSIS)SYNOPSIS

           git mktag

## [](#DESCRIPTION)DESCRIPTION

           Reads a tag’s contents on standard input and creates a tag object.
           The output is the new tag’s <object> identifier.

           This command is mostly equivalent to git-hash-object(1) invoked
           with -t tag -w --stdin. I.e. both of these will create and write a
           tag found in my-tag:

               git mktag <my-tag
               git hash-object -t tag -w --stdin <my-tag

           The difference is that mktag will die before writing the tag if
           the tag doesn’t pass a git-fsck(1) check.

           The "fsck" check done by mktag is stricter than what git-fsck(1)
           would run by default in that all fsck.<msg-id> messages are
           promoted from warnings to errors (so e.g. a missing "tagger" line
           is an error).

           Extra headers in the object are also an error under mktag, but
           ignored by git-fsck(1). This extra check can be turned off by
           setting the appropriate fsck.<msg-id> variable:

               git -c fsck.extraHeaderEntry=ignore mktag <my-tag-with-headers

## [](#OPTIONS)OPTIONS

           --strict
               By default mktag turns on the equivalent of git-fsck(1)
               --strict mode. Use --no-strict to disable it.

## [](#TAG_FORMAT)TAG FORMAT

           A tag signature file, to be fed to this command’s standard input,
           has a very simple fixed format: four lines of

               object <hash>
               type <typename>
               tag <tagname>
               tagger <tagger>

           followed by some optional free-form message (some tags created by
           older Git may not have a tagger line). The message, when it
           exists, is separated by a blank line from the header. The message
           part may contain a signature that Git itself doesn’t care about,
           but that can be verified with gpg.

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

    Git 2.55.0.493.g5b2471          2026-08-03                   GIT-MKTAG(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-merge-tree(1)](../man1/git-merge-tree.1.html)

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
