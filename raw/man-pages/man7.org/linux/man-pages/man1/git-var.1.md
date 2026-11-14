---
{"title": "git-var(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-var.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-var(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [VARIABLES](#VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-VAR(1)                      Git Manual                     GIT-VAR(1)

## [](#NAME)NAME

           git-var - Show a Git logical variable

## [](#SYNOPSIS)SYNOPSIS

           git var (-l | <variable>)

## [](#DESCRIPTION)DESCRIPTION

           Prints a Git logical variable. Exits with code 1 if the variable
           has no value.

## [](#OPTIONS)OPTIONS

           -l
               Display the logical variables. In addition, all the variables
               of the Git configuration file .git/config are listed as well.
               (However, the configuration variables listing functionality is
               deprecated in favor of git config list.)

## [](#EXAMPLES)EXAMPLES

               $ git var GIT_AUTHOR_IDENT
               Eric W. Biederman <ebiederm@lnxi.com> 1121223278 -0600

## [](#VARIABLES)VARIABLES

           GIT_AUTHOR_IDENT
               The author of a piece of code.

           GIT_COMMITTER_IDENT
               The person who put a piece of code into Git.

           GIT_EDITOR
               Text editor for use by Git commands. The value is meant to be
               interpreted by the shell when it is used. Examples: ~/bin/vi,
               $SOME_ENVIRONMENT_VARIABLE, "C:\Program Files\Vim\gvim.exe"
               --nofork. The order of preference is $GIT_EDITOR, then
               core.editor configuration value, then $VISUAL, then $EDITOR,
               and then the default chosen at compile time, which is usually
               vi.

           GIT_SEQUENCE_EDITOR
               Text editor used to edit the todo file while running git
               rebase -i. Like GIT_EDITOR, the value is meant to be
               interpreted by the shell when it is used. The order of
               preference is $GIT_SEQUENCE_EDITOR, then sequence.editor
               configuration value, and then the value of git var GIT_EDITOR.

           GIT_PAGER
               Text viewer for use by Git commands (e.g., less). The value is
               meant to be interpreted by the shell. The order of preference
               is $GIT_PAGER, then the value of core.pager configuration,
               then $PAGER, and then the default chosen at compile time
               (usually less).

           GIT_DEFAULT_BRANCH
               The name of the first branch created in newly initialized
               repositories.

           GIT_SHELL_PATH
               The path of the binary providing the POSIX shell for commands
               which use the shell.

           GIT_ATTR_SYSTEM
               The path to the system gitattributes(5) file, if one is
               enabled.

           GIT_ATTR_GLOBAL
               The path to the global (per-user) gitattributes(5) file.

           GIT_CONFIG_SYSTEM
               The path to the system configuration file, if one is enabled.

           GIT_CONFIG_GLOBAL
               The path to the global (per-user) configuration files, if any.

           Most path values contain only one value. However, some can contain
           multiple values, which are separated by newlines, and are listed
           in order from highest to lowest priority. Callers should be
           prepared for any such path value to contain multiple items.

           Note that paths are printed even if they do not exist, but not if
           they are disabled by other environment variables.

## [](#SEE_ALSO)SEE ALSO

           git-commit-tree(1) git-tag(1) git-config(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03                     GIT-VAR(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-commit(1)](../man1/git-commit.1.html),  [git-config(1)](../man1/git-config.1.html),  [git-replace(1)](../man1/git-replace.1.html),  [git-send-email(1)](../man1/git-send-email.1.html),  [stg-email(1)](../man1/stg-email.1.html),  [gitfaq(7)](../man7/gitfaq.7.html)

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
