---
{"title": "git-fmt-merge-msg(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-fmt-merge-msg.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-fmt-merge-msg(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-FMT-MERGE-MSG(1)            Git Manual           GIT-FMT-MERGE-MSG(1)

## [](#NAME)NAME

           git-fmt-merge-msg - Produce a merge commit message

## [](#SYNOPSIS)SYNOPSIS

           git fmt-merge-msg [-m <message>] [--into-name <branch>] [--log[=<n>] | --no-log]
           git fmt-merge-msg [-m <message>] [--log[=<n>] | --no-log] -F <file>

## [](#DESCRIPTION)DESCRIPTION

           Takes the list of merged objects on stdin and produces a suitable
           commit message to be used for the merge commit, usually to be
           passed as the <merge-message> argument of git merge.

           This command is intended mostly for internal use by scripts
           automatically invoking git merge.

## [](#OPTIONS)OPTIONS

           --log[=<n>]
               In addition to branch names, populate the log message with
               one-line descriptions from the actual commits that are being
               merged. At most <n> commits from each merge parent will be
               used (20 if <n> is omitted). This overrides the merge.log
               configuration variable.

           --no-log
               Do not list one-line descriptions from the actual commits
               being merged.

           --summary, --no-summary
               Synonyms to --log and --no-log; these are deprecated and will
               be removed in the future.

           -m <message>, --message <message>
               Use <message> instead of the branch names for the first line
               of the log message. For use with --log.

           --into-name <branch>
               Prepare the merge message as if merging to the branch
               <branch>, instead of the name of the real branch to which the
               merge is made.

           -F <file>, --file <file>
               Take the list of merged objects from <file> instead of stdin.

## [](#CONFIGURATION)CONFIGURATION

           merge.branchdesc
               In addition to branch names, populate the log message with the
               branch description text associated with them. Defaults to
               false.

           merge.log
               In addition to branch names, populate the log message with at
               most the specified number of one-line descriptions from the
               actual commits that are being merged. Defaults to false, and
               true is a synonym for 20.

           merge.suppressDest
               By adding a glob that matches the names of integration
               branches to this multi-valued configuration variable, the
               default merge message computed for merges into these
               integration branches will omit "into <branch-name>" from its
               title.

               An element with an empty value can be used to clear the list
               of globs accumulated from previous configuration entries. When
               there is no merge.suppressDest variable defined, the default
               value of master is used for backward compatibility.

           merge.summary
               Synonym to merge.log; this is deprecated and will be removed
               in the future.

## [](#EXAMPLES)EXAMPLES

               $ git fetch origin master
               $ git fmt-merge-msg --log <$GIT_DIR/FETCH_HEAD

           Print a log message describing a merge of the "master" branch from
           the "origin" remote.

## [](#SEE_ALSO)SEE ALSO

           git-merge(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03           GIT-FMT-MERGE-MSG(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-merge(1)](../man1/git-merge.1.html),  [git-pull(1)](../man1/git-pull.1.html)

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
