---
{"title": "git-show-branch(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-show-branch.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-show-branch(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OUTPUT](#OUTPUT) \| [EXAMPLES](#EXAMPLES) \| [CONFIGURATION](#CONFIGURATION) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-SHOW-BRANCH(1)              Git Manual             GIT-SHOW-BRANCH(1)

## [](#NAME)NAME

           git-show-branch - Show branches and their commits

## [](#SYNOPSIS)SYNOPSIS

           git show-branch [-a | --all] [-r | --remotes] [--topo-order | --date-order]
                           [--current] [--color[=<when>] | --no-color] [--sparse]
                           [--more=<n> | --list | --independent | --merge-base]
                           [--no-name | --sha1-name] [--topics]
                           [(<rev> | <glob>)...]
           git show-branch (-g | --reflog)[=<n>[,<base>]] [--list] [<ref>]

## [](#DESCRIPTION)DESCRIPTION

           Shows the commit ancestry graph starting from the commits named
           with <rev>s or <glob>s (or all refs under refs/heads and/or
           refs/tags) semi-visually.

           It cannot show more than 26 branches and commits at a time.

           It uses showbranch.default multi-valued configuration items if no
           <rev> or <glob> is given on the command line.

## [](#OPTIONS)OPTIONS

           <rev>
               Arbitrary extended SHA-1 expression (see gitrevisions(7)) that
               typically names a branch head or a tag.

           <glob>
               A glob pattern that matches branch or tag names under refs/.
               For example, if you have many topic branches under
               refs/heads/topic, giving topic/* would show all of them.

           -r, --remotes
               Show the remote-tracking branches.

           -a, --all
               Show both remote-tracking branches and local branches.

           --current
               With this option, the command includes the current branch in
               the list of revs to be shown when it is not given on the
               command line.

           --topo-order
               By default, the branches and their commits are shown in
               reverse chronological order. This option makes them appear in
               topological order (i.e., descendant commits are shown before
               their parents).

           --date-order
               This option is similar to --topo-order in the sense that no
               parent comes before all of its children, but otherwise commits
               are ordered according to their commit date.

           --sparse
               By default, the output omits merges that are reachable from
               only one tip being shown. This option makes them visible.

           --more=<n>
               Usually the command stops output upon showing the commit that
               is the common ancestor of all the branches. This flag tells
               the command to go <n> more common commits beyond that. When
               <n> is negative, display only the <ref>s given, without
               showing the commit ancestry tree.

           --list
               Synonym to --more=-1

           --merge-base
               Instead of showing the commit list, determine possible merge
               bases for the specified commits. All merge bases will be
               contained in all specified commits. This is different from how
               git-merge-base(1) handles the case of three or more commits.

           --independent
               Among the <ref>s given, display only the ones that cannot be
               reached from any other <ref>.

           --no-name
               Do not show naming strings for each commit.

           --sha1-name
               Instead of naming the commits using the path to reach them
               from heads (e.g. "master~2" to mean the grandparent of
               "master"), name them with the unique prefix of their object
               names.

           --topics
               Shows only commits that are NOT on the first branch given.
               This helps track topic branches by hiding any commit that is
               already in the main line of development. When given "git
               show-branch --topics master topic1 topic2", this will show the
               revisions given by "git rev-list ^master topic1 topic2"

           -g, --reflog[=<n>[,<base>]] [<ref>]
               Shows <n> most recent ref-log entries for the given ref. If
               <base> is given, <n> entries going back from that entry.
               <base> can be specified as count or date. When no explicit
               <ref> parameter is given, it defaults to the current branch
               (or HEAD if it is detached).

           --color[=<when>]
               Color the status sign (one of these: * !  + -) of each commit
               corresponding to the branch it’s in. The value must be always
               (the default), never, or auto.

           --no-color
               Turn off colored output, even when the configuration file
               gives the default to color output. Same as --color=never.

           Note that --more, --list, --independent, and --merge-base options
           are mutually exclusive.

## [](#OUTPUT)OUTPUT

           Given N <ref>s, the first N lines are the one-line description
           from their commit message. The branch head that is pointed at by
           $GIT_DIR/HEAD is prefixed with an asterisk * character while other
           heads are prefixed with a ! character.

           Following these N lines, a one-line log for each commit is
           displayed, indented N places. If a commit is on the I-th branch,
           the I-th indentation character shows a + sign; otherwise it shows
           a space. Merge commits are denoted by a - sign. Each commit shows
           a short name that can be used as an extended SHA-1 to name that
           commit.

           The following example shows three branches, "master", "fixes", and
           "mhf":

               $ git show-branch master fixes mhf
               * [master] Add 'git show-branch'.
                ! [fixes] Introduce "reset type" flag to "git reset"
                 ! [mhf] Allow "+remote:local" refspec to cause --force when fetching.
               ---
                 + [mhf] Allow "+remote:local" refspec to cause --force when fetching.
                 + [mhf~1] Use git-octopus when pulling more than one head.
                +  [fixes] Introduce "reset type" flag to "git reset"
                 + [mhf~2] "git fetch --force".
                 + [mhf~3] Use .git/remote/origin, not .git/branches/origin.
                 + [mhf~4] Make "git pull" and "git fetch" default to origin
                 + [mhf~5] Infamous 'octopus merge'
                 + [mhf~6] Retire git-parse-remote.
                 + [mhf~7] Multi-head fetch.
                 + [mhf~8] Start adding the $GIT_DIR/remotes/ support.
               *++ [master] Add 'git show-branch'.

           These three branches all forked from a common commit, [master],
           whose commit message is "Add 'git show-branch'". The "fixes"
           branch adds one commit "Introduce "reset type" flag to "git
           reset"". The "mhf" branch adds many other commits. The current
           branch is "master".

## [](#EXAMPLES)EXAMPLES

           If you keep your primary branches immediately under refs/heads,
           and topic branches in subdirectories of it, having the following
           in the configuration file may help:

               [showbranch]
                       default = --topo-order
                       default = heads/*

           With this, git show-branch without extra parameters would show
           only the primary branches. In addition, if you happen to be on
           your topic branch, it is shown as well.

               $ git show-branch --reflog="10,1 hour ago" --list master

           shows 10 reflog entries going back from the tip as of 1 hour ago.
           Without --list, the output also shows how these tips are
           topologically related to each other.

## [](#CONFIGURATION)CONFIGURATION

           Everything below this line in this section is selectively included
           from the git-config(1) documentation. The content is the same as
           what’s found there:

           showBranch.default
               The default set of branches for git-show-branch(1). See
               git-show-branch(1).

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

    Git 2.55.0.493.g5b2471          2026-08-03             GIT-SHOW-BRANCH(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-config(1)](../man1/git-config.1.html),  [git-merge-base(1)](../man1/git-merge-base.1.html),  [git-show-branch(1)](../man1/git-show-branch.1.html),  [gitcore-tutorial(7)](../man7/gitcore-tutorial.7.html)

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
