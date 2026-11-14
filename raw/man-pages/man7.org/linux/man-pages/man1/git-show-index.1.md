---
{"title": "git-show-index(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-show-index.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-show-index(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-SHOW-INDEX(1)               Git Manual              GIT-SHOW-INDEX(1)

## [](#NAME)NAME

           git-show-index - Show packed archive index

## [](#SYNOPSIS)SYNOPSIS

           git show-index [--object-format=<hash-algorithm>] < <pack-idx-file>

## [](#DESCRIPTION)DESCRIPTION

           Read the .idx file for a Git packfile (created with
           git-pack-objects(1) or git-index-pack(1)) from the standard input,
           and dump its contents. The output consists of one object per line,
           with each line containing two or three space-separated columns:

           •   the first column is the offset in bytes of the object within
               the corresponding packfile

           •   the second column is the object id of the object

           •   if the index version is 2 or higher, the third column contains
               the CRC32 of the object data

           The objects are output in the order in which they are found in the
           index file, which should be (in a correctly constructed file)
           sorted by object id.

           Note that you can get more information on a packfile by calling
           git-verify-pack(1). However, as this command considers only the
           index file itself, it’s both faster and more flexible.

## [](#OPTIONS)OPTIONS

           --object-format=<hash-algorithm>
               Specify the given object format (hash algorithm) for the index
               file. The valid values are sha1 and (if enabled) sha256. The
               default is the algorithm for the current repository (set by
               extensions.objectFormat), or sha1 if no value is set or
               outside a repository..

               Note: At present, there is no interoperability between SHA-256
               repositories and SHA-1 repositories.

           Historically, we warned that SHA-256 repositories may later need
           backward incompatible changes when we introduce such
           interoperability features. Today, we only expect compatible
           changes. Furthermore, if such changes prove to be necessary, it
           can be expected that SHA-256 repositories created with today’s Git
           will be usable by future versions of Git without data loss.

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

    Git 2.55.0.493.g5b2471          2026-08-03              GIT-SHOW-INDEX(1)

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
