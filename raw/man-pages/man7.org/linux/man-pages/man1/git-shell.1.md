---
{"title": "git-shell(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-shell.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-shell(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [INTERACTIVE USE](#INTERACTIVE_USE) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-SHELL(1)                    Git Manual                   GIT-SHELL(1)

## [](#NAME)NAME

           git-shell - Restricted login shell for Git-only SSH access

## [](#SYNOPSIS)SYNOPSIS

           chsh -s $(command -v git-shell) <user>
           git clone <user>@localhost:/path/to/repo.git
           ssh <user>@localhost

## [](#DESCRIPTION)DESCRIPTION

           This is a login shell for SSH accounts to provide restricted Git
           access. It permits execution only of server-side Git commands
           implementing the pull/push functionality, plus custom commands
           present in a subdirectory named git-shell-commands in the user’s
           home directory.

## [](#COMMANDS)COMMANDS

           git shell accepts the following commands after the -c option:

           git receive-pack <argument>, git upload-pack <argument>, git
           upload-archive <argument>
               Call the corresponding server-side command to support the
               client’s git push, git fetch, or git archive --remote request.

           cvs server
               Imitate a CVS server. See git-cvsserver(1).

           If a ~/git-shell-commands directory is present, git shell will
           also handle other, custom commands by running
           "git-shell-commands/<command> <arguments>" from the user’s home
           directory.

## [](#INTERACTIVE_USE)INTERACTIVE USE

           By default, the commands above can be executed only with the -c
           option; the shell is not interactive.

           If a ~/git-shell-commands directory is present, git shell can also
           be run interactively (with no arguments). If a help command is
           present in the git-shell-commands directory, it is run to provide
           the user with an overview of allowed actions. Then a "git> "
           prompt is presented at which one can enter any of the commands
           from the git-shell-commands directory, or exit to close the
           connection.

           Generally this mode is used as an administrative interface to
           allow users to list repositories they have access to, create,
           delete, or rename repositories, or change repository descriptions
           and permissions.

           If a no-interactive-login command exists, then it is run and the
           interactive shell is aborted.

## [](#EXAMPLES)EXAMPLES

           To disable interactive logins, displaying a greeting instead:

               $ chsh -s /usr/bin/git-shell
               $ mkdir $HOME/git-shell-commands
               $ cat >$HOME/git-shell-commands/no-interactive-login <<\EOF
               #!/bin/sh
               printf '%s\n' "Hi $USER! You've successfully authenticated, but I do not"
               printf '%s\n' "provide interactive shell access."
               exit 128
               EOF
               $ chmod +x $HOME/git-shell-commands/no-interactive-login

           To enable git-cvsserver access (which should generally have the
           no-interactive-login example above as a prerequisite, as creating
           the git-shell-commands directory allows interactive logins):

               $ cat >$HOME/git-shell-commands/cvs <<\EOF
               if ! test $# = 1 && test "$1" = "server"
               then
                       echo >&2 "git-cvsserver only handles \"server\""
                       exit 1
               fi
               exec git cvsserver server
               EOF
               $ chmod +x $HOME/git-shell-commands/cvs

## [](#SEE_ALSO)SEE ALSO

           ssh(1), git-daemon(1), contrib/git-shell-commands/README

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

    Git 2.55.0.493.g5b2471          2026-08-03                   GIT-SHELL(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [githooks(5)](../man5/githooks.5.html),  [gitcvs-migration(7)](../man7/gitcvs-migration.7.html),  [giteveryday(7)](../man7/giteveryday.7.html)

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
