---
{"title": "git-verify-pack(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-verify-pack.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-verify-pack(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OUTPUT FORMAT](#OUTPUT_FORMAT) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-VERIFY-PACK(1)              Git Manual             GIT-VERIFY-PACK(1)

## [](#NAME)NAME

           git-verify-pack - Validate packed Git archive files

## [](#SYNOPSIS)SYNOPSIS

           git verify-pack [-v | --verbose] [-s | --stat-only] [--] <pack>.idx...

## [](#DESCRIPTION)DESCRIPTION

           Read each idx file for packed Git archive given on the command
           line, and verify the idx file and the corresponding pack file.

## [](#OPTIONS)OPTIONS

           -v, --verbose
               After verifying the pack, show the list of objects contained
               in the pack and a histogram of delta chain length.

           -s, --stat-only
               Do not verify the pack contents; only show the histogram of
               delta chain length. With --verbose, the list of objects is
               also shown.

           --
               Do not interpret any more arguments as options.

## [](#OUTPUT_FORMAT)OUTPUT FORMAT

           When specifying the -v option the format used is:

               object-name type size size-in-packfile offset-in-packfile

           for objects that are not deltified in the pack, and

               object-name type size size-in-packfile offset-in-packfile depth base-object-name

           for objects that are deltified.

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

    Git 2.55.0.493.g5b2471          2026-08-03             GIT-VERIFY-PACK(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-show-index(1)](../man1/git-show-index.1.html)

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
