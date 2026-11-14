---
{"title": "git-revert(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-revert.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-revert(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEQUENCER SUBCOMMANDS](#SEQUENCER_SUBCOMMANDS) \| [EXAMPLES](#EXAMPLES) \| [DISCUSSION](#DISCUSSION) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-REVERT(1)                   Git Manual                  GIT-REVERT(1)

## [](#NAME)NAME

           git-revert - Revert some existing commits

## [](#SYNOPSIS)SYNOPSIS

           git revert [--[no-]edit] [-n] [-m <parent-number>] [-s] [-S[<keyid>]] <commit>...
           git revert (--continue | --skip | --abort | --quit)

## [](#DESCRIPTION)DESCRIPTION

           Given one or more existing commits, revert the changes that the
           related patches introduce, and record some new commits that record
           them. This requires your working tree to be clean (no
           modifications from the HEAD commit).

           Note: git revert is used to record some new commits to reverse the
           effect of some earlier commits (often only a faulty one). If you
           want to throw away all uncommitted changes in your working
           directory, you should see git-reset(1), particularly the --hard
           option. If you want to extract specific files as they were in
           another commit, you should see git-restore(1), specifically the
           --source option. Take care with these alternatives as both will
           discard uncommitted changes in your working directory.

           See "Reset, restore and revert" in git(1) for the differences
           between the three commands.

## [](#OPTIONS)OPTIONS

           <commit>...
               Commits to revert. For a more complete list of ways to spell
               commit names, see gitrevisions(7). Sets of commits can also be
               given but no traversal is done by default, see git-rev-list(1)
               and its --no-walk option.

           -e, --edit
               With this option, git revert will let you edit the commit
               message prior to committing the revert. This is the default if
               you run the command from a terminal.

           -m parent-number, --mainline parent-number
               Usually you cannot revert a merge because you do not know
               which side of the merge should be considered the mainline.
               This option specifies the parent number (starting from 1) of
               the mainline and allows revert to reverse the change relative
               to the specified parent.

               Reverting a merge commit declares that you will never want the
               tree changes brought in by the merge. As a result, later
               merges will only bring in tree changes introduced by commits
               that are not ancestors of the previously reverted merge. This
               may or may not be what you want.

               See the revert-a-faulty-merge How-To[1] for more details.

           --no-edit
               With this option, git revert will not start the commit message
               editor.

           --cleanup=<mode>
               This option determines how the commit message will be cleaned
               up before being passed on to the commit machinery. See
               git-commit(1) for more details. In particular, if the <mode>
               is given a value of scissors, scissors will be appended to
               MERGE_MSG before being passed on in the case of a conflict.

           -n, --no-commit
               Usually the command automatically creates some commits with
               commit log messages stating which commits were reverted. This
               flag applies the changes necessary to revert the named commits
               to your working tree and the index, but does not make the
               commits. In addition, when this option is used, your index
               does not have to match the HEAD commit. The revert is done
               against the beginning state of your index.

               This is useful when reverting more than one commits' effect to
               your index in a row.

           -S[<keyid>], --gpg-sign[=<keyid>], --no-gpg-sign
               GPG-sign commits. The keyid argument is optional and defaults
               to the committer identity; if specified, it must be stuck to
               the option without a space.  --no-gpg-sign is useful to
               countermand both commit.gpgSign configuration variable, and
               earlier --gpg-sign.

           -s, --signoff
               Add a Signed-off-by trailer at the end of the commit message.
               See the signoff option in git-commit(1) for more information.

           --strategy=<strategy>
               Use the given merge strategy. Should only be used once. See
               the MERGE STRATEGIES section in git-merge(1) for details.

           -X<option>, --strategy-option=<option>
               Pass the merge strategy-specific option through to the merge
               strategy. See git-merge(1) for details.

           --rerere-autoupdate, --no-rerere-autoupdate
               After the rerere mechanism reuses a recorded resolution on the
               current conflict to update the files in the working tree,
               allow it to also update the index with the result of
               resolution.  --no-rerere-autoupdate is a good way to
               double-check what git-rerere(1) did and catch potential
               mismerges, before committing the result to the index with a
               separate git-add(1).

           --reference
               Instead of starting the body of the log message with "This
               reverts <full-object-name-of-the-commit-being-reverted>.",
               refer to the commit using "--pretty=reference" format (cf.
               git-log(1)). The revert.reference configuration variable can
               be used to enable this option by default.

## [](#SEQUENCER_SUBCOMMANDS)SEQUENCER SUBCOMMANDS

           --continue
               Continue the operation in progress using the information in
               .git/sequencer. Can be used to continue after resolving
               conflicts in a failed cherry-pick or revert.

           --skip
               Skip the current commit and continue with the rest of the
               sequence.

           --quit
               Forget about the current operation in progress. Can be used to
               clear the sequencer state after a failed cherry-pick or
               revert.

           --abort
               Cancel the operation and return to the pre-sequence state.

## [](#EXAMPLES)EXAMPLES

           git revert HEAD~3
               Revert the changes specified by the fourth last commit in HEAD
               and create a new commit with the reverted changes.

           git revert -n master~5..master~2
               Revert the changes done by commits from the fifth last commit
               in master (included) to the third last commit in master
               (included), but do not create any commit with the reverted
               changes. The revert only modifies the working tree and the
               index.

## [](#DISCUSSION)DISCUSSION

           While git creates a basic commit message automatically, it is
           strongly recommended to explain why the original commit is being
           reverted. In addition, repeatedly reverting reverts will result in
           increasingly unwieldy subject lines, for example Reapply "Reapply
           "<original-subject>"". Please consider rewording these to be
           shorter and more unique.

## [](#CONFIGURATION)CONFIGURATION

           Everything below this line in this section is selectively included
           from the git-config(1) documentation. The content is the same as
           what’s found there:

           revert.reference
               Setting this variable to true makes git revert behave as if
               the --reference option is given.

## [](#SEE_ALSO)SEE ALSO

           git-cherry-pick(1)

## [](#GIT)GIT

           Part of the git(1) suite

## [](#NOTES)NOTES

            1. revert-a-faulty-merge How-To
               file:///home/mtk/share/doc/git-doc/howto/revert-a-faulty-merge.html

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

    Git 2.55.0.493.g5b2471          2026-08-03                  GIT-REVERT(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-cherry-pick(1)](../man1/git-cherry-pick.1.html),  [giteveryday(7)](../man7/giteveryday.7.html)

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
