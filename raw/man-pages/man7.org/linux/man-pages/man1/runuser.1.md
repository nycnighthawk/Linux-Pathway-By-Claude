---
{"title": "runuser(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/runuser.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# runuser(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIG FILES](#CONFIG_FILES) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SECURITY NOTES](#SECURITY_NOTES) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RUNUSER(1)                    User Commands                    RUNUSER(1)

## [](#NAME)NAME

           runuser - run a command with substitute user and group ID

## [](#SYNOPSIS)SYNOPSIS

           runuser [options] -u user [[--] command [argument...]]

           runuser [options] [-] [user [argument...]]

## [](#DESCRIPTION)DESCRIPTION

           runuser can be used to run commands with a substitute user and
           group ID. If the option -u is not given, runuser falls back to
           su-compatible semantics and a shell is executed. The difference
           between the commands runuser and su is that runuser does not ask
           for a password (because it may be executed by the root user only)
           and it uses a different PAM configuration. The command runuser
           does not have to be installed with set-user-ID permissions.

           If the PAM session is not required, then the recommended solution
           is to use the setpriv(1) command.

           When called without arguments, runuser defaults to running an
           interactive shell as root.

           For backward compatibility, runuser defaults to not changing the
           current directory and to setting only the environment variables
           HOME and SHELL (plus USER and LOGNAME if the target user is not
           root). This version of runuser uses PAM for session management.

           Note that runuser in all cases use PAM (pam_getenvlist(3)) to do
           the final environment modification. Command-line options such as
           --login and --preserve-environment affect the environment before
           it is modified by PAM.

           Since version 2.38 runuser resets process resource limits
           RLIMIT_NICE, RLIMIT_RTPRIO, RLIMIT_FSIZE, RLIMIT_AS and
           RLIMIT_NOFILE.

## [](#OPTIONS)OPTIONS

           -c, --command=command
               Pass command to the shell with the -c option. Creates a new
               session via setsid(2). Refer to --session-command to keep the
               same session.

           -f, --fast
               Pass -f to the shell, which may or may not be useful,
               depending on the shell.

           -g, --group=group
               The primary group to be used. This option is allowed for the
               root user only.

           -G, --supp-group=group
               Specify a supplementary group. This option is available to the
               root user only. The first specified supplementary group is
               also used as a primary group if the option --group is not
               specified.

           -, -l, --login
               Start the shell as a login shell with an environment similar
               to a real login:

               •   clears all the environment variables except for TERM,
                   COLORTERM, NO_COLOR and variables specified by
                   --whitelist-environment

               •   initializes the environment variables HOME, SHELL, USER,
                   LOGNAME, and PATH

               •   changes to the target user’s home directory

               •   sets argv[0] of the shell to '-' in order to make the
                   shell a login shell

           -m, -p, --preserve-environment
               Preserve the entire environment, i.e., do not set HOME, SHELL,
               USER or LOGNAME. The option is ignored if the option --login
               is specified.

           -P, --pty
               Create a pseudoterminal for the session. The independent
               terminal provides better security as the user does not share a
               terminal with the original session. Please note security
               advice about TIOCSTI vulnerability below.

               The entire session can also be moved to the background (e.g.,
               runuser --pty -u user -- command &). If the pseudoterminal is
               enabled, then runuser works as a proxy between the sessions
               (sync stdin and stdout).

               This feature is mostly designed for interactive sessions. If
               the standard input is not a terminal, but for example a pipe
               (e.g., echo "date" | runuser --pty -u user), then the ECHO
               flag for the pseudoterminal is disabled to avoid messy output.

           -s, --shell=shell
               Run the specified shell instead of the default. The shell to
               run is selected according to the following rules, in order:

               •   the shell specified with --shell

               •   the shell specified in the environment variable SHELL if
                   the --preserve-environment option is used

               •   the shell listed in the passwd entry of the target user

               •   /bin/sh

                   If the target user has a restricted shell (i.e., not
                   listed in /etc/shells), then the --shell option and the
                   SHELL environment variables are ignored unless the calling
                   user is root.

           --session-command=command
               Same as -c, but do not create a new session. (Discouraged.)
               Please note security advice about TIOCSTI vulnerability below.

           -T, --no-pty
               Do not create a pseudo-terminal, opposite of --pty and -P.
               Please note security advice about TIOCSTI vulnerability below.

           -u, --user=user
               Run command with the effective user ID and group ID of the
               user name user.

           -w, --whitelist-environment=list
               Don’t reset the environment variables specified in the
               comma-separated list when clearing the environment for
               --login. The whitelist is ignored for the environment
               variables HOME, SHELL, USER, LOGNAME, and PATH.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#CONFIG_FILES)CONFIG FILES

           runuser reads the /etc/default/runuser and /etc/login.defs
           configuration files. The following configuration items are
           relevant for runuser:

           ENV_PATH (string)
               Defines the PATH environment variable for a regular user. The
               default value is /usr/local/bin:/bin:/usr/bin.

           ENV_ROOTPATH (string), ENV_SUPATH (string)
               Defines the PATH environment variable for root. ENV_SUPATH
               takes precedence. The default value is
               /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin.

           ALWAYS_SET_PATH (boolean)
               If set to yes and --login and --preserve-environment were not
               specified runuser initializes PATH.

           The environment variable PATH may be different on systems where
           /bin and /sbin are merged into /usr; this variable is also
           affected by the --login command-line option and the PAM system
           setting (e.g., pam_env(8)).

## [](#EXIT_STATUS)EXIT STATUS

           runuser normally returns the exit status of the command it
           executed. If the command was killed by a signal, runuser returns
           the number of the signal plus 128.

           Exit status generated by runuser itself:

           1
               Generic error before executing the requested command

           126
               The requested command could not be executed

           127
               The requested command was not found

## [](#ENVIRONMENT)ENVIRONMENT

           SU_DEBUG=all
               Enable su debug output.

           ULPTY_DEBUG=all
               Enable pty debug output.

## [](#FILES)FILES

           /etc/pam.d/runuser
               default PAM configuration file

           /etc/pam.d/runuser-l
               PAM configuration file if --login is specified

           /etc/default/runuser
               runuser specific logindef config file

           /etc/login.defs
               global logindef config file

## [](#SECURITY_NOTES)SECURITY NOTES

           If runuser shares a terminal with the original session, it is
           potentially vulnerable to privilege escalation through
           TIOCSTI/TIOCLINUX ioctl command injection. There are two built-in
           ways to prevent this: Either you can use runuser with the -c
           option, which starts a new session via setsid(2) without a
           controlling terminal. Or, if your use case requires a controlling
           terminal, for example an interactive session, you can instruct
           runuser to use a pseudoterminal with the --pty or -P option.

## [](#HISTORY)HISTORY

           This runuser command was derived from coreutils' su, which was
           based on an implementation by David MacKenzie, and the Fedora
           runuser command by Dan Walsh.

## [](#SEE_ALSO)SEE ALSO

           setpriv(1), su(1), login.defs(5), shells(5), pam(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The runuser command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                     RUNUSER(1)

------------------------------------------------------------------------

Pages that refer to this page: [setpriv(1)](../man1/setpriv.1.html),  [su(1)](../man1/su.1.html),  [credentials(7)](../man7/credentials.7.html)

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
