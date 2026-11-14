---
{"title": "git-upload-archive(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-upload-archive.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-upload-archive(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SECURITY](#SECURITY) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-UPLOAD-ARCHIVE(1)           Git Manual          GIT-UPLOAD-ARCHIVE(1)

## [](#NAME)NAME

           git-upload-archive - Send archive back to git-archive

## [](#SYNOPSIS)SYNOPSIS

           git upload-archive <repository>

## [](#DESCRIPTION)DESCRIPTION

           Invoked by git archive --remote and sends a generated archive to
           the other end over the Git protocol.

           This command is usually not invoked directly by the end user. The
           UI for the protocol is on the git archive side, and the program
           pair is meant to be used to get an archive from a remote
           repository.

## [](#SECURITY)SECURITY

           In order to protect the privacy of objects that have been removed
           from history but may not yet have been pruned, git-upload-archive
           avoids serving archives for commits and trees that are not
           reachable from the repository’s refs. However, because calculating
           object reachability is computationally expensive,
           git-upload-archive implements a stricter but easier-to-check set
           of rules:

            1. Clients may request a commit or tree that is pointed to
               directly by a ref. E.g., git archive --remote=origin v1.0.

            2. Clients may request a sub-tree within a commit or tree using
               the ref:path syntax. E.g., git archive --remote=origin
               v1.0:Documentation.

            3. Clients may not use other sha1 expressions, even if the end
               result is reachable. E.g., neither a relative commit like
               master^ nor a literal sha1 like abcd1234 is allowed, even if
               the result is reachable from the refs.

           Note that rule 3 disallows many cases that do not have any privacy
           implications. These rules are subject to change in future versions
           of git, and the server accessed by git archive --remote may or may
           not follow these exact rules.

           If the config option uploadArchive.allowUnreachable is true, these
           rules are ignored, and clients may use arbitrary sha1 expressions.
           This is useful if you do not care about the privacy of unreachable
           objects, or if your object database is already publicly available
           for access via non-smart-http.

## [](#OPTIONS)OPTIONS

           <repository>
               The repository to get a tar archive from.

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

    Git 2.55.0.493.g5b2471          2026-08-03          GIT-UPLOAD-ARCHIVE(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-archive(1)](../man1/git-archive.1.html),  [git-config(1)](../man1/git-config.1.html)

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
