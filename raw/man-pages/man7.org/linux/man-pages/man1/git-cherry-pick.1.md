---
{"title": "git-cherry-pick(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-cherry-pick.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-cherry-pick(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEQUENCER SUBCOMMANDS](#SEQUENCER_SUBCOMMANDS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-CHERRY-PICK(1)              Git Manual             GIT-CHERRY-PICK(1)

## [](#NAME)NAME

           git-cherry-pick - Apply the changes introduced by some existing
           commits

## [](#SYNOPSIS)SYNOPSIS

           git cherry-pick [--edit] [-n] [-m <parent-number>] [-s] [-x] [--ff]
                             [-S[<keyid>]] <commit>...
           git cherry-pick (--continue | --skip | --abort | --quit)

## [](#DESCRIPTION)DESCRIPTION

           Given one or more existing commits, apply the change each one
           introduces, recording a new commit for each. This requires your
           working tree to be clean (no modifications from the HEAD commit).

           When it is not obvious how to apply a change, the following
           happens:

            1. The current branch and HEAD pointer stay at the last commit
               successfully made.

            2. The CHERRY_PICK_HEAD ref is set to point at the commit that
               introduced the change that is difficult to apply.

            3. Paths in which the change applied cleanly are updated both in
               the index file and in your working tree.

            4. For conflicting paths, the index file records up to three
               versions, as described in the "TRUE MERGE" section of
               git-merge(1). The working tree files will include a
               description of the conflict bracketed by the usual conflict
               markers <<<<<<< and >>>>>>>.

            5. No other modifications are made.

           See git-merge(1) for some hints on resolving such conflicts.

## [](#OPTIONS)OPTIONS

           <commit>...
               Commits to cherry-pick. For a more complete list of ways to
               spell commits, see gitrevisions(7). Sets of commits can be
               passed but no traversal is done by default, as if the
               --no-walk option was specified, see git-rev-list(1). Note that
               specifying a range will feed all <commit>... arguments to a
               single revision walk (see a later example that uses maint
               master..next).

           -e, --edit
               With this option, git cherry-pick will let you edit the commit
               message prior to committing.

           --cleanup=<mode>
               This option determines how the commit message will be cleaned
               up before being passed on to the commit machinery. See
               git-commit(1) for more details. In particular, if the <mode>
               is given a value of scissors, scissors will be appended to
               MERGE_MSG before being passed on in the case of a conflict.

           -x
               When recording the commit, append a line that says "(cherry
               picked from commit ...)" to the original commit message in
               order to indicate which commit this change was cherry-picked
               from. This is done only for cherry picks without conflicts. Do
               not use this option if you are cherry-picking from your
               private branch because the information is useless to the
               recipient. If on the other hand you are cherry-picking between
               two publicly visible branches (e.g. backporting a fix to a
               maintenance branch for an older release from a development
               branch), adding this information can be useful.

           -r
               It used to be that the command defaulted to do -x described
               above, and -r was to disable it. Now the default is not to do
               -x so this option is a no-op.

           -m <parent-number>, --mainline <parent-number>
               Usually you cannot cherry-pick a merge because you do not know
               which side of the merge should be considered the mainline.
               This option specifies the parent number (starting from 1) of
               the mainline and allows cherry-pick to replay the change
               relative to the specified parent.

           -n, --no-commit
               Usually the command automatically creates a sequence of
               commits. This flag applies the changes necessary to
               cherry-pick each named commit to your working tree and the
               index, without making any commit. In addition, when this
               option is used, your index does not have to match the HEAD
               commit. The cherry-pick is done against the beginning state of
               your index.

               This is useful when cherry-picking more than one commits'
               effect to your index in a row.

           -s, --signoff
               Add a Signed-off-by trailer at the end of the commit message.
               See the signoff option in git-commit(1) for more information.

           -S[<keyid>], --gpg-sign[=<keyid>], --no-gpg-sign
               GPG-sign commits. The keyid argument is optional and defaults
               to the committer identity; if specified, it must be stuck to
               the option without a space.  --no-gpg-sign is useful to
               countermand both commit.gpgSign configuration variable, and
               earlier --gpg-sign.

           --ff
               If the current HEAD is the same as the parent of the
               cherry-pick’ed commit, then a fast forward to this commit will
               be performed.

           --allow-empty
               By default, cherry-picking an empty commit will fail,
               indicating that an explicit invocation of git commit
               --allow-empty is required. This option overrides that
               behavior, allowing empty commits to be preserved automatically
               in a cherry-pick. Note that when "--ff" is in effect, empty
               commits that meet the "fast-forward" requirement will be kept
               even without this option. Note also, that use of this option
               only keeps commits that were initially empty (i.e. the commit
               recorded the same tree as its parent). Commits which are made
               empty due to a previous commit will cause the cherry-pick to
               fail. To force the inclusion of those commits, use
               --empty=keep.

           --allow-empty-message
               By default, cherry-picking a commit with an empty message will
               fail. This option overrides that behavior, allowing commits
               with empty messages to be cherry picked.

           --empty=(drop|keep|stop)
               How to handle commits being cherry-picked that are redundant
               with changes already in the current history.

               drop
                   The commit will be dropped.

               keep
                   The commit will be kept. Implies --allow-empty.

               stop
                   The cherry-pick will stop when the commit is applied,
                   allowing you to examine the commit. This is the default
                   behavior.

               Note that --empty=drop and --empty=stop only specify how to
               handle a commit that was not initially empty, but rather
               became empty due to a previous commit. Commits that were
               initially empty will still cause the cherry-pick to fail
               unless one of --empty=keep or --allow-empty are specified.

           --keep-redundant-commits
               Deprecated synonym for --empty=keep.

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

           git cherry-pick master
               Apply the change introduced by the commit at the tip of the
               master branch and create a new commit with this change.

           git cherry-pick ..master, git cherry-pick ^HEAD master
               Apply the changes introduced by all commits that are ancestors
               of master but not of HEAD to produce new commits.

           git cherry-pick maint next ^master, git cherry-pick maint
           master..next
               Apply the changes introduced by all commits that are ancestors
               of maint or next, but not master or any of its ancestors. Note
               that the latter does not mean maint and everything between
               master and next; specifically, maint will not be used if it is
               included in master.

           git cherry-pick master~4 master~2
               Apply the changes introduced by the fifth and third last
               commits pointed to by master and create 2 new commits with
               these changes.

           git cherry-pick -n master~1 next
               Apply to the working tree and the index the changes introduced
               by the second last commit pointed to by master and by the last
               commit pointed to by next, but do not create any commit with
               these changes.

           git cherry-pick --ff ..next
               If history is linear and HEAD is an ancestor of next, update
               the working tree and advance the HEAD pointer to match next.
               Otherwise, apply the changes introduced by those commits that
               are in next but not HEAD to the current branch, creating a new
               commit for each new change.

           git rev-list --reverse master -- README | git cherry-pick -n
           --stdin
               Apply the changes introduced by all commits on the master
               branch that touched README to the working tree and index, so
               the result can be inspected and made into a single new commit
               if suitable.

           The following sequence attempts to backport a patch, bails out
           because the code the patch applies to has changed too much, and
           then tries again, this time exercising more care about matching up
           context lines.

               $ git cherry-pick topic^             (1)
               $ git diff                           (2)
               $ git cherry-pick --abort            (3)
               $ git cherry-pick -Xpatience topic^  (4)

            1. apply the change that would be shown by git show
               topic^. In this example, the patch does not apply
               cleanly, so information about the conflict is written
               to the index and working tree and no new commit
               results.
            2. summarize changes to be reconciled
            3. cancel the cherry-pick. In other words, return to the
               pre-cherry-pick state, preserving any local
               modifications you had in the working tree.
            4. try to apply the change introduced by topic^ again,
               spending extra time to avoid mistakes based on
               incorrectly matching context lines.

## [](#SEE_ALSO)SEE ALSO

           git-revert(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03             GIT-CHERRY-PICK(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-cherry(1)](../man1/git-cherry.1.html),  [git-revert(1)](../man1/git-revert.1.html),  [gitworkflows(7)](../man7/gitworkflows.7.html)

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
