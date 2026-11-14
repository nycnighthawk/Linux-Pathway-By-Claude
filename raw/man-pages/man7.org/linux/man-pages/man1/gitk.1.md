---
{"title": "gitk(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/gitk.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gitk(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GITK(1)                         Git Manual                        GITK(1)

## [](#NAME)NAME

           gitk - The Git repository browser

## [](#SYNOPSIS)SYNOPSIS

           gitk [<options>] [<revision-range>] [--] [<path>...]

## [](#DESCRIPTION)DESCRIPTION

           Displays changes in a repository or a selected set of commits.
           This includes visualizing the commit graph, showing information
           related to each commit, and the files in the trees of each
           revision.

## [](#OPTIONS)OPTIONS

           To control which revisions to show, gitk supports most options
           applicable to the git rev-list command. It also supports a few
           options applicable to the git diff-* commands to control how the
           changes each commit introduces are shown. Finally, it supports
           some gitk-specific options.

           gitk generally only understands options with arguments in the
           stuck form (see gitcli(7)) due to limitations in the command-line
           parser.

       rev-list options and arguments
           This manual page describes only the most frequently used options.
           See git-rev-list(1) for a complete list.

           --all
               Show all refs (branches, tags, etc.).

           --branches[=<pattern>], --tags[=<pattern>], --remotes[=<pattern>]
               Pretend as if all the branches (tags, remote branches, resp.)
               are listed on the command line as <commit>. If <pattern> is
               given, limit refs to ones matching given shell glob. If
               pattern lacks ?, *, or [, /* at the end is implied.

           --since=<date>
               Show commits more recent than a specific date.

           --until=<date>
               Show commits older than a specific date.

           --date-order
               Sort commits by date when possible.

           --merge
               After an attempt to merge stops with conflicts, show the
               commits on the history between two branches (i.e. the HEAD and
               the MERGE_HEAD) that modify the conflicted files and do not
               exist on all the heads being merged.

           --left-right
               Mark which side of a symmetric difference a commit is
               reachable from. Commits from the left side are prefixed with a
               < symbol and those from the right with a > symbol.

           --full-history
               When filtering history with <path>..., does not prune some
               history. (See "History simplification" in git-log(1) for a
               more detailed explanation.)

           --simplify-merges
               Additional option to --full-history to remove some needless
               merges from the resulting history, as there are no selected
               commits contributing to this merge. (See "History
               simplification" in git-log(1) for a more detailed
               explanation.)

           --ancestry-path
               When given a range of commits to display (e.g.
               commit1..commit2 or commit2 ^commit1), only display commits
               that exist directly on the ancestry chain between the commit1
               and commit2, i.e. commits that are both descendants of
               commit1, and ancestors of commit2. (See "History
               simplification" in git-log(1) for a more detailed
               explanation.)

           -L<start>,<end>:<file>, -L:<funcname>:<file>
               Trace the evolution of the line range given by <start>,<end>,
               or by the function name regex <funcname>, within the <file>.
               You may not give any pathspec limiters. This is currently
               limited to a walk starting from a single revision, i.e., you
               may only give zero or one positive revision arguments, and
               <start> and <end> (or <funcname>) must exist in the starting
               revision. You can specify this option more than once. Implies
               --patch. Patch output can be suppressed using --no-patch.
               Non-patch diff formats --raw, --name-only, --name-status, and
               --summary are supported. Diff stat formats (--stat, --numstat,
               --shortstat, --dirstat) are not currently implemented.

               Patch formatting options such as --word-diff, --color-moved,
               --no-prefix, and whitespace options (-w, -b) are supported, as
               are pickaxe options (-S, -G) and --diff-filter.

               <start> and <end> can take one of these forms:

               •   <number>

                   If <start> or <end> is a number, it specifies an absolute
                   line number (lines count from 1).

               •   /<regex>/

                   This form will use the first line matching the given POSIX
                   <regex>. If <start> is a regex, it will search from the
                   end of the previous -L range, if any, otherwise from the
                   start of file. If <start> is ^/<regex>/, it will search
                   from the start of file. If <end> is a regex, it will
                   search starting at the line given by <start>.

               •   +<offset> or -<offset>

                   This is only valid for <end> and will specify a number of
                   lines before or after the line given by <start>.

               If :<funcname> is given in place of <start> and <end>, it is a
               regular expression that denotes the range from the first
               funcname line that matches <funcname>, up to the next funcname
               line.  :<funcname> searches from the end of the previous -L
               range, if any, otherwise from the start of file.  ^:<funcname>
               searches from the start of file. The function names are
               determined in the same way as git diff works out patch hunk
               headers (see Defining a custom hunk-header in
               gitattributes(5)).

           <revision range>
               Limit the revisions to show. This can be either a single
               revision meaning show from the given revision and back, or it
               can be a range in the form "<from>..<to>" to show all
               revisions between <from> and back to <to>. Note, more advanced
               revision selection can be applied. For a more complete list of
               ways to spell object names, see gitrevisions(7).

           <path>...
               Limit commits to the ones touching files in the given paths.
               Note, to avoid ambiguity with respect to revision names use
               "--" to separate the paths from any preceding options.

       gitk-specific options
           --argscmd=<command>
               Command to be run each time gitk has to determine the revision
               range to show. The command is expected to print on its
               standard output a list of additional revisions to be shown,
               one per line. Use this instead of explicitly specifying a
               <revision-range> if the set of commits to show may vary
               between refreshes.

           --select-commit=<ref>
               Select the specified commit after loading the graph. Default
               behavior is equivalent to specifying --select-commit=HEAD.

## [](#EXAMPLES)EXAMPLES

           gitk v2.6.12.. include/scsi drivers/scsi
               Show the changes since version v2.6.12 that changed any file
               in the include/scsi or drivers/scsi subdirectories

           gitk --since="2 weeks ago" -- gitk
               Show the changes during the last two weeks to the file gitk.
               The "--" is necessary to avoid confusion with the branch named
               gitk

           gitk --max-count=100 --all -- Makefile
               Show at most 100 changes made to the file Makefile. Instead of
               only looking for changes in the current branch look in all
               branches.

## [](#FILES)FILES

           User configuration and preferences are stored at:

           •   $XDG_CONFIG_HOME/git/gitk if it exists, otherwise

           •   $HOME/.gitk if it exists

           If neither of the above exist then $XDG_CONFIG_HOME/git/gitk is
           created and used by default. If $XDG_CONFIG_HOME is not set it
           defaults to $HOME/.config in all cases.

## [](#HISTORY)HISTORY

           Gitk was the first graphical repository browser, written by Paul
           Mackerras in Tcl/Tk.

           gitk is actually maintained as an independent project, but stable
           versions are distributed as part of the Git suite for the
           convenience of end users.

           gitk-git/ comes from Johannes Sixt’s gitk project:

               https://github.com/j6t/gitk

## [](#SEE_ALSO)SEE ALSO

           qgit(1)
               A repository browser written in C++ using Qt.

           tig(1)
               A minimal repository browser and Git tool output highlighter
               written in C using Ncurses.

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

    Git 2.55.0.493.g5b2471          2026-08-03                        GITK(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-config(1)](../man1/git-config.1.html),  [git-gui(1)](../man1/git-gui.1.html),  [gitattributes(5)](../man5/gitattributes.5.html)

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
