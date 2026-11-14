---
{"title": "git-gui(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-gui.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-gui(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [OTHER](#OTHER) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-GUI(1)                      Git Manual                     GIT-GUI(1)

## [](#NAME)NAME

           git-gui - A portable graphical interface to Git

## [](#SYNOPSIS)SYNOPSIS

           git gui [<command>] [<arguments>]

## [](#DESCRIPTION)DESCRIPTION

           A Tcl/Tk based graphical user interface to Git. git gui focuses on
           allowing users to make changes to their repository by making new
           commits, amending existing ones, creating branches, performing
           local merges, and fetching/pushing to remote repositories.

           Unlike gitk, git gui focuses on commit generation and single file
           annotation and does not show project history. It does however
           supply menu actions to start a gitk session from within git gui.

           git gui is known to work on all popular UNIX systems, Mac OS X,
           and Windows (under both Cygwin and MSYS). To the extent possible
           OS specific user interface guidelines are followed, making git gui
           a fairly native interface for users.

## [](#COMMANDS)COMMANDS

           blame
               Start a blame viewer on the specified file on the given
               version (or working directory if not specified).

           browser
               Start a tree browser showing all files in the specified
               commit. Files selected through the browser are opened in the
               blame viewer.

           citool
               Start git gui and arrange to make exactly one commit before
               exiting and returning to the shell. The interface is limited
               to only commit actions, slightly reducing the application’s
               startup time and simplifying the menubar.

           version
               Display the currently running version of git gui.

## [](#EXAMPLES)EXAMPLES

           git gui blame Makefile
               Show the contents of the file Makefile in the current working
               directory, and provide annotations for both the original
               author of each line, and who moved the line to its current
               location. The uncommitted file is annotated, and uncommitted
               changes (if any) are explicitly attributed to Not Yet
               Committed.

           git gui blame v0.99.8 Makefile
               Show the contents of Makefile in revision v0.99.8 and provide
               annotations for each line. Unlike the above example the file
               is read from the object database and not the working
               directory.

           git gui blame --line=100 Makefile
               Loads annotations as described above and automatically scrolls
               the view to center on line 100.

           git gui citool
               Make one commit and return to the shell when it is complete.
               This command returns a non-zero exit code if the window was
               closed in any way other than by making a commit.

           git gui citool --amend
               Automatically enter the Amend Last Commit mode of the
               interface.

           git gui citool --nocommit
               Behave as normal citool, but instead of making a commit simply
               terminate with a zero exit code. It still checks that the
               index does not contain any unmerged entries, so you can use it
               as a GUI version of git-mergetool(1)

           git citool
               Same as git gui citool (above).

           git gui browser maint
               Show a browser for the tree of the maint branch. Files
               selected in the browser can be viewed with the internal blame
               viewer.

## [](#SEE_ALSO)SEE ALSO

           gitk(1)
               The Git repository browser. Shows branches, commit history and
               file differences. gitk is the utility started by git gui's
               Repository Visualize actions.

## [](#OTHER)OTHER

           git gui is actually maintained as an independent project, but
           stable versions are distributed as part of the Git suite for the
           convenience of end users.

           The official repository of the git gui project can be found at:

               https://github.com/j6t/git-gui

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

    Git 2.55.0.493.g5b2471          2026-08-03                     GIT-GUI(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-citool(1)](../man1/git-citool.1.html),  [git-config(1)](../man1/git-config.1.html),  [gitattributes(5)](../man5/gitattributes.5.html)

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
