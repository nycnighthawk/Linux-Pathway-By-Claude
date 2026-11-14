---
{"title": "git-cvsexportcommit(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-cvsexportcommit.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-cvsexportcommit(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [EXAMPLES](#EXAMPLES) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-CVSEXPORTCOMMIT(1)          Git Manual         GIT-CVSEXPORTCOMMIT(1)

## [](#NAME)NAME

           git-cvsexportcommit - Export a single commit to a CVS checkout

## [](#SYNOPSIS)SYNOPSIS

           git cvsexportcommit [-h] [-u] [-v] [-c] [-P] [-p] [-a] [-d <cvsroot>]
                   [-w <cvs-workdir>] [-W] [-f] [-m <msgprefix>] [<parent-commit>] <commit-id>

## [](#DESCRIPTION)DESCRIPTION

           Exports a commit from Git to a CVS checkout, making it easier to
           merge patches from a Git repository into a CVS repository.

           Specify the name of a CVS checkout using the -w switch or execute
           it from the root of the CVS working copy. In the latter case
           GIT_DIR must be defined. See examples below.

           It does its best to do the safe thing, it will check that the
           files are unchanged and up to date in the CVS checkout, and it
           will not autocommit by default.

           Supports file additions, removals, and commits that affect binary
           files.

           If the commit is a merge commit, you must tell git cvsexportcommit
           what parent the changeset should be done against.

## [](#OPTIONS)OPTIONS

           -c
               Commit automatically if the patch applied cleanly. It will not
               commit if any hunks fail to apply or there were other
               problems.

           -p
               Be pedantic (paranoid) when applying patches. Invokes patch
               with --fuzz=0

           -a
               Add authorship information. Adds Author line, and Committer
               (if different from Author) to the message.

           -d
               Set an alternative CVSROOT to use. This corresponds to the CVS
               -d parameter. Usually users will not want to set this, except
               if using CVS in an asymmetric fashion.

           -f
               Force the merge even if the files are not up to date.

           -P
               Force the parent commit, even if it is not a direct parent.

           -m
               Prepend the commit message with the provided prefix. Useful
               for patch series and the like.

           -u
               Update affected files from CVS repository before attempting
               export.

           -k
               Reverse CVS keyword expansion (e.g. $Revision: 1.2.3.4$
               becomes $Revision$) in working CVS checkout before applying
               patch.

           -w
               Specify the location of the CVS checkout to use for the
               export. This option does not require GIT_DIR to be set before
               execution if the current directory is within a Git repository.
               The default is the value of cvsexportcommit.cvsdir.

           -W
               Tell cvsexportcommit that the current working directory is not
               only a Git checkout, but also the CVS checkout. Therefore, Git
               will reset the working directory to the parent commit before
               proceeding.

           -v
               Verbose.

## [](#CONFIGURATION)CONFIGURATION

           cvsexportcommit.cvsdir
               The default location of the CVS checkout to use for the
               export.

## [](#EXAMPLES)EXAMPLES

           Merge one patch into CVS

                   $ export GIT_DIR=~/project/.git
                   $ cd ~/project_cvs_checkout
                   $ git cvsexportcommit -v <commit-sha1>
                   $ cvs commit -F .msg <files>

           Merge one patch into CVS (-c and -w options). The working
           directory is within the Git Repo

                           $ git cvsexportcommit -v -c -w ~/project_cvs_checkout <commit-sha1>

           Merge pending patches into CVS automatically — only if you really
           know what you are doing

                   $ export GIT_DIR=~/project/.git
                   $ cd ~/project_cvs_checkout
                   $ git cherry cvshead myhead | sed -n 's/^+ //p' | xargs -l1 git cvsexportcommit -c -p -v

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

    Git 2.55.0.493.g5b2471          2026-08-03         GIT-CVSEXPORTCOMMIT(1)

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
