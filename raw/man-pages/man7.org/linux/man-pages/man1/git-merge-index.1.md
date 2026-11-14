---
{"title": "git-merge-index(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-merge-index.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-merge-index(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-MERGE-INDEX(1)              Git Manual             GIT-MERGE-INDEX(1)

## [](#NAME)NAME

           git-merge-index - Run a merge for files needing merging

## [](#SYNOPSIS)SYNOPSIS

           git merge-index [-o] [-q] <merge-program> (-a | ( [--] <file>...) )

## [](#DESCRIPTION)DESCRIPTION

           This looks up the <file>(s) in the index and, if there are any
           merge entries, passes the SHA-1 hash for those files as arguments
           1, 2, 3 (empty argument if no file), and <file> as argument 4.
           File modes for the three files are passed as arguments 5, 6 and 7.

## [](#OPTIONS)OPTIONS

           --
               Do not interpret any more arguments as options.

           -a
               Run merge against all files in the index that need merging.

           -o
               Instead of stopping at the first failed merge, do all of them
               in one shot - continue with merging even when previous merges
               returned errors, and only return the error code after all the
               merges.

           -q
               Do not complain about a failed merge program (a merge program
               failure usually indicates conflicts during the merge). This is
               for porcelains which might want to emit custom messages.

           If git merge-index is called with multiple <file>s (or -a) then it
           processes them in turn only stopping if merge returns a non-zero
           exit code.

           Typically this is run with a script calling Git’s imitation of the
           merge command from the RCS package.

           A sample script called git merge-one-file is included in the
           distribution.

           ALERT ALERT ALERT! The Git "merge object order" is different from
           the RCS merge program merge object order. In the above ordering,
           the original is first. But the argument order to the 3-way merge
           program merge is to have the original in the middle. Don’t ask me
           why.

           Examples:

               torvalds@ppc970:~/merge-test> git merge-index cat MM
               This is MM from the original tree.              # original
               This is modified MM in the branch A.            # merge1
               This is modified MM in the branch B.            # merge2
               This is modified MM in the branch B.            # current contents

           or

               torvalds@ppc970:~/merge-test> git merge-index cat AA MM
               cat: : No such file or directory
               This is added AA in the branch A.
               This is added AA in the branch B.
               This is added AA in the branch B.
               fatal: merge program failed

           where the latter example shows how git merge-index will stop
           trying to merge once anything has returned an error (i.e., cat
           returned an error for the AA file, because it didn’t exist in the
           original, and thus git merge-index didn’t even try to merge the MM
           thing).

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

    Git 2.55.0.493.g5b2471          2026-08-03             GIT-MERGE-INDEX(1)

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
