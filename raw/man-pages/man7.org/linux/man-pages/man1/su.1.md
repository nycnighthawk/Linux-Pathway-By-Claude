---
{"title": "su(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/su.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# su(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SIGNALS](#SIGNALS) \| [CONFIG FILES](#CONFIG_FILES) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SECURITY NOTES](#SECURITY_NOTES) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SU(1)                         User Commands                         SU(1)

## [](#NAME)NAME

           su - run a command with substitute user and group ID

## [](#SYNOPSIS)SYNOPSIS

           su [options] [-] [user|UID [argument...]]

## [](#DESCRIPTION)DESCRIPTION

           su allows commands to be run with a substitute user and group ID.

           When called with no user specified, su defaults to running an
           interactive shell as root. When user is specified, additional
           arguments can be supplied, in which case they are passed to the
           shell.

           For backward compatibility, su defaults to not change the current
           directory and to only set the environment variables HOME and SHELL
           (plus USER and LOGNAME if the target user is not root). It is
           recommended to always use the --login option (instead of its
           shortcut -) to avoid side effects caused by mixing environments.

           This version of su uses PAM for authentication, account and
           session management. Some configuration options found in other su
           implementations, such as support for a wheel group, have to be
           configured via PAM.

           su is mostly designed for unprivileged users, the recommended
           solution for privileged users (e.g., scripts executed by root) is
           to use non-set-user-ID command runuser(1) that does not require
           authentication and provides separate PAM configuration. If the PAM
           session is not required at all then the recommended solution is to
           use command setpriv(1).

           Note that su in all cases uses PAM (pam_getenvlist(3)) to do the
           final environment modification. Command-line options such as
           --login and --preserve-environment affect the environment before
           it is modified by PAM.

           Since version 2.38 su resets process resource limits RLIMIT_NICE,
           RLIMIT_RTPRIO, RLIMIT_FSIZE, RLIMIT_AS and RLIMIT_NOFILE.

## [](#OPTIONS)OPTIONS

           -c, --command command
               Pass command to the shell with the -c option. Creates a new
               session via setsid(2). Refer to --session-command to keep the
               same session.

           -f, --fast
               Pass -f to the shell, which may or may not be useful,
               depending on the shell.

           -g, --group group
               Specify the primary group. This option is available to the
               root user only.

           -G, --supp-group group
               Specify a supplementary group. This option is available to the
               root user only. The first specified supplementary group is
               also used as a primary group if the option --group is not
               specified.

           -, -l, --login
               Start the shell as a login shell with an environment similar
               to a real login.

               Note that on systemd(1)-based systems, a new session may be
               defined as a real entry point to the system. However, su does
               not create a real session (by PAM) from this point of view.
               You need to use tools like systemd-run(1) or machinectl(1) to
               initiate a complete, real session.

               su does:

               •   clear all the environment variables except TERM,
                   COLORTERM, NO_COLOR and variables specified by
                   --whitelist-environment

               •   initialize the environment variables HOME, SHELL, USER,
                   LOGNAME, and PATH

               •   change to the target user’s home directory

               •   set argv[0] of the shell to '-' in order to make the shell
                   a login shell

           -m, -p, --preserve-environment
               Preserve the entire environment, i.e., do not set HOME, SHELL,
               USER or LOGNAME. This option is ignored if the option --login
               is specified.

           -P, --pty
               Create a pseudoterminal for the session. The independent
               terminal provides better security as the user does not share a
               terminal with the original session. Please note security
               advice about TIOCSTI vulnerability below.

               The entire session can also be moved to the background (e.g.,
               su --pty - user -c application &). If the pseudoterminal is
               enabled, then su works as a proxy between the sessions (sync
               stdin and stdout).

               This feature is mostly designed for interactive sessions. If
               the standard input is not a terminal, but for example a pipe
               (e.g., echo "date" | su --pty), then the ECHO flag for the
               pseudoterminal is disabled to avoid messy output.

           -s, --shell shell
               Run the specified shell instead of the default. If the target
               user has a restricted shell (i.e., not listed in /etc/shells),
               the --shell option and the SHELL environment variables are
               ignored unless the calling user is root.

               The shell to run is selected according to the following rules,
               in order:

               •   the shell specified with --shell

               •   the shell specified in the environment variable SHELL, if
                   the --preserve-environment option is used

               •   the shell listed in the passwd entry of the target user

               •   /bin/sh

           --session-command=command
               Same as -c, but do not create a new session. (Discouraged.)
               Please note security advice about TIOCSTI vulnerability below.

           -T, --no-pty
               Do not create a pseudo-terminal, opposite of --pty and -P.
               Please note security advice about TIOCSTI vulnerability below.

           -w, --whitelist-environment list
               Don’t reset the environment variables specified in the
               comma-separated list when clearing the environment for
               --login. The whitelist is ignored for the environment
               variables HOME, SHELL, USER, LOGNAME, and PATH.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#SIGNALS)SIGNALS

           Upon receiving either SIGINT, SIGQUIT or SIGTERM, su terminates
           its child and afterwards terminates itself with the received
           signal. The child is terminated by SIGTERM, after unsuccessful
           attempt and 2 seconds of delay the child is killed by SIGKILL.

## [](#CONFIG_FILES)CONFIG FILES

           su reads the /etc/default/su and /etc/login.defs configuration
           files. The following configuration items are relevant for su:

           FAIL_DELAY (number)
               Delay in seconds in case of an authentication failure. The
               number must be a non-negative integer.

           ENV_PATH (string)
               Defines the PATH environment variable for a regular user. The
               default value is /usr/local/bin:/bin:/usr/bin.

           ENV_ROOTPATH (string), ENV_SUPATH (string)
               Defines the PATH environment variable for root. ENV_SUPATH
               takes precedence. The default value is
               /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin.

           ALWAYS_SET_PATH (boolean)
               If set to yes and --login and --preserve-environment were not
               specified su initializes PATH.

               The environment variable PATH may be different on systems
               where /bin and /sbin are merged into /usr; this variable is
               also affected by the --login command-line option and the PAM
               system setting (e.g., pam_env(8)).

## [](#EXIT_STATUS)EXIT STATUS

           su normally returns the exit status of the command it executed. If
           the command was killed by a signal, su returns the number of the
           signal plus 128.

           Exit status generated by su itself:

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

           /etc/pam.d/su
               default PAM configuration file

           /etc/pam.d/su-l
               PAM configuration file if --login is specified

           /etc/default/su
               command specific logindef config file

           /etc/login.defs
               global logindef config file

## [](#SECURITY_NOTES)SECURITY NOTES

           If su shares a terminal with the original session, it is
           potentially vulnerable to privilege escalation through
           TIOCSTI/TIOCLINUX ioctl command injection. There are two built-in
           ways to prevent this: Either you can use su with the -c option,
           which starts a new session via setsid(2) without a controlling
           terminal. Or, if your use case requires a controlling terminal,
           for example an interactive session, you can instruct su to use a
           pseudoterminal with the --pty or -P option.

           For security reasons, su always logs failed log-in attempts to the
           btmp file, but it does not write to the lastlog file at all. This
           solution can be used to control su behavior by PAM configuration.
           If you want to use the pam_lastlog(8) module to print warning
           message about failed log-in attempts then pam_lastlog(8) has to be
           configured to update the lastlog file as well. For example by:

              session required pam_lastlog.so nowtmp

## [](#HISTORY)HISTORY

           This su command was derived from coreutils' su, which was based on
           an implementation by David MacKenzie. The util-linux version has
           been refactored by Karel Zak.

## [](#SEE_ALSO)SEE ALSO

           setpriv(1), login.defs(5), shells(5), pam(8), runuser(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The su command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                          SU(1)

------------------------------------------------------------------------

Pages that refer to this page: [flock(1)](../man1/flock.1.html),  [homectl(1)](../man1/homectl.1.html),  [login(1)](../man1/login.1.html),  [login(1@@shadow-utils)](../man1/login.1@@shadow-utils.html),  [machinectl(1)](../man1/machinectl.1.html),  [newgrp(1)](../man1/newgrp.1.html),  [runuser(1)](../man1/runuser.1.html),  [setpriv(1)](../man1/setpriv.1.html),  [sg(1)](../man1/sg.1.html),  [updatedb(1)](../man1/updatedb.1.html),  [pam(3)](../man3/pam.3.html),  [pts(4)](../man4/pts.4.html),  [crontab(5)](../man5/crontab.5.html),  [login.defs(5)](../man5/login.defs.5.html),  [passwd(5)](../man5/passwd.5.html),  [passwd(5@@shadow-utils)](../man5/passwd.5@@shadow-utils.html),  [shadow(5)](../man5/shadow.5.html),  [credentials(7)](../man7/credentials.7.html),  [environ(7)](../man7/environ.7.html),  [PAM(8)](../man8/PAM.8.html),  [pam_rootok(8)](../man8/pam_rootok.8.html),  [pam_xauth(8)](../man8/pam_xauth.8.html)

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
