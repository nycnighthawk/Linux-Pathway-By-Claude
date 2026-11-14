---
{"title": "stg(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/stg.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stg(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [STGIT COMMANDS](#STGIT_COMMANDS) \| [CONFIGURATION MECHANISM](#CONFIGURATION_MECHANISM) \| [TEMPLATES](#TEMPLATES) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STG(1)                         StGit Manual                        STG(1)

## [](#NAME)NAME

           stg - Manage stacks of patches using the Git content tracker

## [](#SYNOPSIS)SYNOPSIS

           stg [OPTIONS] <command> [...]
           stg [OPTIONS] <-h|--help>
           stg --version

## [](#DESCRIPTION)DESCRIPTION

           StGit (Stacked Git) is an application that provides a convenient
           way to maintain a patch stack on top of a Git branch:

           •   The topmost (most recent) commits of a branch are given names.
               Such a named commit is called a patch.

           •   After making changes to the worktree, you can incorporate the
               changes into an existing patch; this is called refreshing. You
               may refresh any patch, not just the topmost one.

           •   You can pop a patch: temporarily putting it aside, so that the
               patch below it becomes the topmost patch. Later you may push
               it onto the stack again. Pushing and popping can be used to
               reorder patches.

           •   You can easily rebase your patch stack on top of any other Git
               commit. (The base of a patch stack is the most recent Git
               commit that is not an StGit patch.) For example, if you
               started making patches on top of someone else’s branch, and
               that person publishes an updated branch, you can take all your
               patches and apply them on top of the updated branch.

           •   As you would expect, changing what is below a patch can cause
               that patch to no longer apply cleanly — this can occur when
               you reorder patches, rebase patches, or refresh a non-topmost
               patch. StGit uses Git’s rename-aware three-way merge
               capability to automatically fix up what it can; if it still
               fails, it lets you manually resolve the conflict just like you
               would resolve a merge conflict in Git.

           •   The patch stack is just some extra metadata attached to
               regular Git commits, so you can continue to use most Git tools
               along with StGit.

       Typical uses
           Tracking branch
               Tracking changes from a remote branch, while maintaining local
               modifications against that branch, possibly with the intent of
               sending some patches upstream. You can modify your patch stack
               as much as you want, and when your patches are finally
               accepted upstream, the permanent recorded Git history will
               contain just the final sequence of patches, and not the messy
               sequence of edits that produced them.

               Commands of interest in this workflow are e.g. rebase and
               mail.

           Development branch
               Even if you have no "upstream" to send patches to, you can use
               StGit as a convenient way to modify the recent history of a
               Git branch. For example, instead of first committing change A,
               then change B, and then A2 to fix A because it wasn’t quite
               right, you could incorporate the fix directly into A. This way
               of working results in a much more readable Git history than if
               you had immortalized every misstep you made on your way to the
               right solution.

               Commands of interest in this workflow are e.g. uncommit, which
               can be used to move the patch stack base downwards — i.e.,
               turn Git commits into StGit patches after the fact — and
               commit, its inverse.

           For more information, see the tutorial[1].

       Specifying patches
           Most StGit commands have patch arguments. Patches in the stack may
           be specified in a variety of ways. A patch in the current branch
           may simply referred to by its name, or, alternatively, be located
           by a relative offset from the topmost patch (e.g. +3), as an
           absolute index into the stack (e.g. 7), or as an offset from the
           last visible patch (e.g. ^1).

           Some commands allow you to specify a patch in another branch of
           the repository; this is done by prefixing the patch name with the
           branch name and a colon (e.g. otherbranch:thatpatch).

           Commands that take multiple patch arguments may be supplied with
           patch ranges of the form patch1..patchN as an alternative to
           specifying each patch individually. For example, stg delete p0..p4
           would be equivalent to stg delete p0 p1 p2 p3 p4. Patch ranges may
           be open on either or both ends. For example, stg delete ..p2 would
           delete the first applied patch up to and including patch p2.
           Alternatively, stg delete p2.. would delete patch p2 up to and
           including the topmost applied patch. And stg delete .. would
           delete all applied patches.

           The complete syntax for locating patches follows:

           <patchname>, e.g. patch
               The name of a patch.

           @
               Refers to the topmost applied patch, or the base of the stack
               if no patches are applied.

           [<patchname>]~[<n>], e.g. ~2, patch~, patch~3
               The <n>th previous patch from the named patch. If <patchname>
               is not supplied, @ is implied. A single ~ represents the first
               previous patch. Multiple ~ may be specified, e.g.  patch~~~ is
               the same as patch~3. This is similar to git’s revision syntax
               where <rev>~[<n>] means the <n>th ancestor commit from <rev>
               following first parents.

           [<patchname>]+[<n>], e.g. +, +3, patch+, patch+3
               The <n>th next patch from the named patch. If <patchname> is
               not supplied, @ is implied. A single + represents the next
               patch in the series. Multiple + may be specified, e.g.
               patch+++ is the same as patch+3.

           -[<n>], e.g. -3, -
               References the <n>th previously applied patch. This is similar
               to ~<n>, except it is only valid without a patch name prefix.
               Note that certain commands with other options taking numeric
               values may require escaping - with \-, e.g.  \-10.

           <n>, e.g. 3
               The patch at absolute index <n> in the stack. This is a
               zero-based index, so 0 refers to the bottommost patch in the
               stack.

           ^[<n>], e.g. ^, ^3
               The patch at offset <n> from the last visible patch in the
               stack. This is a zero-based offset, so ^0 refers to the last
               visible patch in the stack, which is equivalent to just ^.
               Negative values of <n> are allowed and refer to hidden patches
               which are after the last visible patch in the stack.

           {base}+[<n>], e.g. {base}+, {base}+3
               The patch at offset <n> from the stack’s base commit. Since
               the stack base is not a commit, a positive offset is required.

           Take note that numeric patch locations of the form <n>, -<n>, and
           +<n>, e.g. 3, -3, or +3 are also valid patch names. I.e. it is
           possible (but not recommended) to name a patch, for example, "-3".
           In the case where a patch name could also be interpreted as a
           numeric index or offset, the literal patch name will take
           precidence when resolving the patch location.

       Specifying commits
           Some StGit commands take Git commits as arguments. StGit accepts
           all revision specifications that Git does (see gitrevisions(7));
           and additionally, the patch specifiers from above. The usual Git
           modifiers, including ^, are also allowed; e.g.
           some-branch:a-patch^^ refers to the grandparent of the commit that
           is patch a-patch on branch some-branch.

           If you need to pass a given StGit reference to a Git command,
           stg-id(1) will convert it to a Git commit id for you.

## [](#OPTIONS)OPTIONS

           The following generic option flags are available. Additional
           options are available for (and documented with) the different
           subcommands.

           --version
               Print version information

           --help
               Print help information.

           -C
               Run as if stg was started in <path> instead of the current
               working directory. When multiple -C options are given, each
               subsequent non-absolute -C <path> is interpreted relative to
               the preceding -C <path>.

               This option affects arguments that expect path names or path
               specs in that their interpretations of the path names would be
               made relative to the working directory caused by the -C
               option.

           --color <when>
               Specify when to colorize the output.

               auto (the default) enables colored output only when outputting
               to a terminal or TTY. The NO_COLOR environment variable is
               respected.

               always and never unconditionlly enable/disable colored output,
               respectively.

               ansi forces color to be output using ANSI escape sequences,
               even in a Windows console.

## [](#STGIT_COMMANDS)STGIT COMMANDS

           We divide StGit commands in thematic groups, according to the
           primary type of object they create or change.

           Here is a short description of each command. A more detailed
           description is available in individual command manpages. Those
           manpages are named stg-<command>(1).

       Patch Inspection
           stg-diff(1)
               Show a diff

           stg-files(1)
               Show files modified by a patch

           stg-id(1)
               Print git hash of a StGit revision

           stg-log(1)
               Display or optionally clear the stack changelog

           stg-name(1)
               Print patch name of a StGit revision

           stg-show(1)
               Show patch commits

       Patch Manipulation
           stg-edit(1)
               Edit a patch

           stg-fold(1)
               Fold diff file into the current patch

           stg-new(1)
               Create a new patch at top of the stack

           stg-refresh(1)
               Incorporate worktree changes into current patch

           stg-rename(1)
               Rename a patch

           stg-spill(1)
               Spill changes from the topmost patch

           stg-sync(1)
               Synchronize patches with a branch or a series

       Stack Inspection
           stg-email(1)
               Format and send patches as email

           stg-export(1)
               Export patches to a directory

           stg-next(1)
               Print the name of the next patch

           stg-patches(1)
               Show patches that modify files

           stg-prev(1)
               Print the name of the previous patch

           stg-series(1)
               Display the patch series

           stg-top(1)
               Print the name of the top patch

       Stack Manipulation
           stg-branch(1)
               Branch operations: switch, list, create, rename, delete, ...

           stg-clean(1)
               Delete empty patches from the series

           stg-commit(1)
               Finalize patches to the stack base

           stg-delete(1)
               Delete patches

           stg-float(1)
               Push patches to the top, even if applied

           stg-goto(1)
               Go to patch by pushing or popping as necessary

           stg-hide(1)
               Hide patches in the series

           stg-import(1)
               Import patches to stack

           stg-init(1)
               Initialize a StGit stack on a branch

           stg-pick(1)
               Import a patch from another branch or a commit object

           stg-pop(1)
               Pop (unapply) one or more applied patches

           stg-pull(1)
               Pull changes from a remote repository

           stg-push(1)
               Push (apply) one or more unapplied patches

           stg-rebase(1)
               Move the stack base to another point in history

           stg-redo(1)
               Undo the last undo operation

           stg-repair(1)
               Repair stack after branch is modified with git commands

           stg-reset(1)
               Reset the patch stack to an earlier state

           stg-sink(1)
               Move patches deeper in the stack

           stg-squash(1)
               Squash two or more patches into one

           stg-uncommit(1)
               Convert regular Git commits into StGit patches

           stg-undo(1)
               Undo the last command

           stg-unhide(1)
               Unhide hidden patches

       Administration
           stg-completion(1)
               Support for shell completions

           stg-help(1)
               Print this message or the help of the given subcommand(s)

           stg-version(1)
               Print version information and exit

## [](#CONFIGURATION_MECHANISM)CONFIGURATION MECHANISM

           StGit uses the same configuration mechanism as Git. See
           git-config(1) for more details.

       Variables
           branch.<name>.stgit.autostash, branch.<name>.stgit.fetchcmd,
           branch.<name>.stgit.pull-policy, branch.<name>.stgit.pullcmd,
           branch.<name>.stgit.rebasecmd
               Branch-specific configuration values. These take precedence
               over the corresponding non-branch specific configuration
               values (see below).

           branch.<name>.stgit.parentbranch
               Specifies the parent branch of a branch with a StGit stack.
               This value is set by stg-branch(1) when creating or cloning
               branches, and not typically set by the user. The parent branch
               is used by stg-pull(1) when stgit.pull-policy is either rebase
               or fetch-rebase to determine the target of the rebase.

           stgit.alias.*
               Command aliases for stg. For example, after defining
               stgit.alias.list = series -d, running stg list is equivalent
               to stg series -d. Arguments are split by spaces and the usual
               shell quoting and escaping is supported. A quote pair or
               backslash may be used to quote them.

               If the alias expansion is prefixed with an exclamation point
               (!), it will be treated as a shell command. For example,
               defining stgit.alias.outgoing = !git log @{u}, running stg
               outgoing is equivalent to running the shell command git log
               @{u}. Note that shell commands will be executed from the
               top-level directory of the working tree, which may not
               necessarily be the current directory.  GIT_PREFIX is set as
               returned by running git rev-parse --show-prefix from the
               original current directory. See git-rev-parse(1).

               Aliases that would hide existing StGit commands are ignored.

           stgit.autoimerge
               When set to true, if conflicts occur when pushing a patch,
               git-mergetool(1) is automatically run to attempt to resolve
               the conflicts.

           stgit.autosign
               Automatically add signoff trailer to commit messages for new
               patches created with stg-new(1) or lingstg:import[]. The value
               of this configuration variable will be used as the key of the
               trailer and therefore should be set to something like
               Signed-off-by.

           stgit.autostash
               When running stg-rebase(1), if any modified files are found in
               the working tree, a temporary stash is created with
               git-stash(1) before the operation begins and is applied after
               the operation completes.

           stgit.diff-opts
               Options to pass-through to git diff-tree for stg-diff(1),
               stg-export(1), stg-patches(1), and stg-show(1). Multiple
               space-separated options may be specified. See git-diff-tree(1)
               for information about the various available options.

           stgit.edit.verbose
               When set to true, the patch’s diff will be shown when
               interactively editing a patch description with, for example,
               stg-edit(1).

           stgit.editor
               Commands such as stg-edit(1) and stg-new(1) open an editor to
               edit the patch description and commit message. The editor set
               by this variable is launched when the GIT_EDITOR environment
               variable is not set. This variable takes precedence over the
               core.editor configuration variable as well as the VISUAL and
               EDITOR environment variables.

           stgit.fetchcmd
               The command specified by this variable will be run by
               stg-pull(1) to fetch from the remote repository when
               stgit.pull-policy is fetch-rebase. When not set, the default
               command is git fetch.

           stgit.gpgsign
               A boolean to specify whether StGit stack metadata commits
               should be GPG signed.

               N.B. Set commit.gpgsign to determine whether patch commits
               themselves are GPG signed. See git-config(1) for more
               information about commit.gpgsign.

           stgit.import.message-id
               When set to true, create Message-ID: trailer in the patch
               description of patches imported from email using
               stg-import(1).

           stgit.keepoptimized
               When set to true, after pulling changes with stg-pull(1), the
               repository’s object database will be optimized by running
               git-repack(1).

           stgit.namelength
               An integer used to determine the maximum length, in
               characters, of automatically generated patch names. The
               default value is 30. This option does not affect
               user-specified patch names. Setting to a value less than or
               equal to 0 will allow automatically generated patch names of
               unlimited length.

               Automatically generated patch names are truncated at word
               boundaries less than or equal to the value of
               stgit.namelength. As a result, patch names will typically not
               be truncated at exactly this number of characters. It is also
               possible for automatically generated patch names to be longer
               than this value if a work boundary cannot be found within this
               bound, or if additional characters need to be added to the
               patch name to make it unique.

           stgit.pick.expose-format
               Format of the commit message for patches picked using the
               --expose option with stg-pick(1). The value of this option is
               as may be specified to the --pretty option of git-show(1). The
               default is format:%B%n(imported from commit %H).

           stgit.pull-policy
               Policy used by stg-pull(1) for pulling changes from a remote
               repository. Valid values include:

               •   pull, the default, uses git-pull(1) or stgit.pullcmd, if
                   set, to pull changes from the remote repository.

               •   rebase uses git-reset(1) or stgit.rebasecmd, if set, to
                   rebase the patch stack before reapplying patches.

               •   fetch-rebase first fetches commits from the remote
                   repository using git-fetch(1) or stgit.fetchcmd, if set,
                   before performing the rebase as described above.

           stgit.pullcmd
               The command to be run by stg-pull(1) to pull changes from the
               remote repository when stgit.pull-policy is pull (the
               default). The default value is git pull.

           stgit.push.allow-conflicts
               A boolean to specify whether stg-push(1) and other commands
               that push patches will push patches that may result in merge
               conflicts. The default is true, which means that a patch with
               conflicts will be pushed and if the conflicts cannot be
               automatically resolved, the operation will stop and with the
               conflicts left to be resolved manually.

               When set to false, a patch that would have merge conflicts
               will not be pushed, thus leaving the stack on the last patch
               that could be pushed without conflicts.

               This configuration variable may be overridden on the command
               line with either --conflicts[=allow] or --conflicts=disallow.

               N.B.: stgit.autoimerge only has an affect when push conflicts
               are allowed.

           stgit.rebasecmd
               The command to be run by stg-pull(1) to set the new stack base
               when stgit.pull-policy is either rebase or fetch-rebase. The
               default is git reset --hard.

           stgit.refreshsubmodules
               A boolean to specify whether stg-refresh(1) includes
               submodules in patch content. This value may be overridden by
               the --submodules or --no-submodules option to stg-refresh(1).
               By default, submodule content is not included in patch
               content.

           stgit.shortnr
               The number of patches listed by stg-series(1) when the
               -s/--short option is specified. Defaults to 5.

## [](#TEMPLATES)TEMPLATES

           A number of StGit commands make use of template files to provide
           useful default texts to be edited by the user. These <name>.tmpl
           template files are searched in the following directories:

            1. $GITDIR/ (in practice, the .git/ directory in your repository)

            2. $XDG_CONFIG_HOME/stgit/templates/

            3. $HOME/.stgit/templates/

## [](#NOTES)NOTES

            1. tutorial
               https://stacked-git.github.io/guides/tutorial

## [](#COLOPHON)COLOPHON

           This page is part of the stgit (Stacked Git) project.  Information
           about the project can be found at ⟨http://www.procode.org/stgit/⟩.
           If you have a bug report for this manual page, see
           ⟨http://www.procode.org/stgit/⟩.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/stacked-git/stgit.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-19.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    StGit 2.6.1                     08/04/2026                         STG(1)

------------------------------------------------------------------------

Pages that refer to this page: [stg-branch(1)](../man1/stg-branch.1.html),  [stg-clean(1)](../man1/stg-clean.1.html),  [stg-commit(1)](../man1/stg-commit.1.html),  [stg-completion(1)](../man1/stg-completion.1.html),  [stg-delete(1)](../man1/stg-delete.1.html),  [stg-diff(1)](../man1/stg-diff.1.html),  [stg-edit(1)](../man1/stg-edit.1.html),  [stg-email(1)](../man1/stg-email.1.html),  [stg-export(1)](../man1/stg-export.1.html),  [stg-files(1)](../man1/stg-files.1.html),  [stg-float(1)](../man1/stg-float.1.html),  [stg-fold(1)](../man1/stg-fold.1.html),  [stg-goto(1)](../man1/stg-goto.1.html),  [stg-help(1)](../man1/stg-help.1.html),  [stg-hide(1)](../man1/stg-hide.1.html),  [stg-id(1)](../man1/stg-id.1.html),  [stg-import(1)](../man1/stg-import.1.html),  [stg-init(1)](../man1/stg-init.1.html),  [stg-log(1)](../man1/stg-log.1.html),  [stg-name(1)](../man1/stg-name.1.html),  [stg-new(1)](../man1/stg-new.1.html),  [stg-next(1)](../man1/stg-next.1.html),  [stg-patches(1)](../man1/stg-patches.1.html),  [stg-pick(1)](../man1/stg-pick.1.html),  [stg-pop(1)](../man1/stg-pop.1.html),  [stg-prev(1)](../man1/stg-prev.1.html),  [stg-pull(1)](../man1/stg-pull.1.html),  [stg-push(1)](../man1/stg-push.1.html),  [stg-rebase(1)](../man1/stg-rebase.1.html),  [stg-redo(1)](../man1/stg-redo.1.html),  [stg-refresh(1)](../man1/stg-refresh.1.html),  [stg-rename(1)](../man1/stg-rename.1.html),  [stg-repair(1)](../man1/stg-repair.1.html),  [stg-reset(1)](../man1/stg-reset.1.html),  [stg-series(1)](../man1/stg-series.1.html),  [stg-show(1)](../man1/stg-show.1.html),  [stg-sink(1)](../man1/stg-sink.1.html),  [stg-spill(1)](../man1/stg-spill.1.html),  [stg-squash(1)](../man1/stg-squash.1.html),  [stg-sync(1)](../man1/stg-sync.1.html),  [stg-top(1)](../man1/stg-top.1.html),  [stg-uncommit(1)](../man1/stg-uncommit.1.html),  [stg-undo(1)](../man1/stg-undo.1.html),  [stg-unhide(1)](../man1/stg-unhide.1.html),  [stg-version(1)](../man1/stg-version.1.html)

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
