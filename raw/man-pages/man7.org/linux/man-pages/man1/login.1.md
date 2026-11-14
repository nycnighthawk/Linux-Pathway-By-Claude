---
{"title": "login(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/login.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# login(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIG FILE ITEMS](#CONFIG_FILE_ITEMS) \| [FILES](#FILES) \| [CREDENTIALS](#CREDENTIALS) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LOGIN(1)                      User Commands                      LOGIN(1)

## [](#NAME)NAME

           login - begin session on the system

## [](#SYNOPSIS)SYNOPSIS

           login [-p] [-s shell] [-h host] [-H] [[-f] username|UID]

## [](#DESCRIPTION)DESCRIPTION

           login is used when signing onto a system. If no argument is given,
           login prompts for the username.

           The user is then prompted for a password, where appropriate.
           Echoing is disabled to prevent revealing the password. Only a
           number of password failures are permitted before login exits and
           the communications link is severed. See LOGIN_RETRIES in the
           CONFIG FILE ITEMS section.

           If password aging has been enabled for the account, the user may
           be prompted for a new password before proceeding. In such a case,
           the old password must be provided and the new password entered
           before continuing. Please refer to passwd(1) for more information.

           The user and group ID will be set according to their values in the
           /etc/passwd file. There is one exception if the user ID is zero.
           In this case, only the primary group ID of the account is set.
           This should allow the system administrator to login even in case
           of network problems. The environment variable values for $HOME,
           $USER, $SHELL, $PATH, $LOGNAME, and $MAIL are set according to the
           appropriate fields in the password entry. $PATH defaults to
           /usr/local/bin:/bin:/usr/bin for normal users, and to
           /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin for
           root, if not otherwise configured.

           The environment variable $TERM will be preserved, if it exists,
           else it will be initialized to the terminal type on your tty. The
           environment variables $COLORTERM and $NO_COLOR will be preserved
           if they exist.

           Other environment variables are preserved if the -p option is
           given or if LOGIN_ENV_SAFELIST defined in /etc/login.defs (see
           below).

           The environment variables defined by PAM are always preserved.

           Then the user’s shell is started. If no shell is specified for the
           user with -s or in /etc/passwd, then /bin/sh is used. If the
           specified shell contains a space, it is treated as a shell script.
           If there is no home directory specified in /etc/passwd, then / is
           used, followed by .hushlogin check as described below.

           If the file .hushlogin exists, then a "quiet" login is performed.
           This disables the checking of mail and the printing of the last
           login time and message of the day. Otherwise, if /var/log/lastlog
           exists, the last login time is printed, and the current login is
           recorded.

## [](#OPTIONS)OPTIONS

           -p
               Used by getty(8) to tell login to preserve the environment.
               See also LOGIN_ENV_SAFELIST config file item.

           -f
               Used to skip a login authentication. This option is usually
               used by the getty(8) autologin feature.

           -h
               Used by other servers (such as telnetd(8) to pass the name of
               the remote host to login so that it can be placed in utmp and
               wtmp. Only the superuser is allowed use this option.

               Note that the -h option has an impact on the PAM service name.
               The standard service name is login, but with the -h option,
               the name is remote. It is necessary to create proper PAM
               config files (for example, /etc/pam.d/login and
               /etc/pam.d/remote).

           -H
               Used by other servers (for example, telnetd(8)) to tell login
               that printing the hostname should be suppressed in the login:
               prompt. See also LOGIN_PLAIN_PROMPT below.

           -s, --shell shell
               Specify a shell, other than the one defined in /etc/passwd, to
               log in to.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#CONFIG_FILE_ITEMS)CONFIG FILE ITEMS

           login reads the /etc/login.defs configuration file (see
           login.defs(5)). Note that the configuration file could be
           distributed with another package (usually shadow-utils). The
           following configuration items are relevant for login:

           MOTD_FILE (string)
               Specifies a ":" delimited list of "message of the day" files
               and directories to be displayed upon login. If the specified
               path is a directory then displays all files with .motd file
               extension in version-sort order from the directory.

               The default value is /usr/share/misc/motd:/run/motd:/etc/motd.
               If the MOTD_FILE item is empty or a quiet login is enabled,
               then the message of the day is not displayed. Note that the
               same functionality is also provided by the pam_motd(8) PAM
               module.

               The directories in the MOTD_FILE are supported since version
               2.36.

               Note that login does not implement any filenames overriding
               behavior like pam_motd (see also MOTD_FIRSTONLY), but all
               content from all files is displayed. It is recommended to keep
               extra logic in content generators and use /run/motd.d rather
               than rely on overriding behavior hardcoded in system tools.

           MOTD_FIRSTONLY (boolean)
               Forces login to stop display content specified by MOTD_FILE
               after the first accessible item in the list. Note that a
               directory is one item in this case. This option allows login
               semantics to be configured to be more compatible with
               pam_motd. The default value is no.

           LOGIN_ENV_SAFELIST (string)
               Forces login to protect the specified environment variables if
               -p is not used. The string value is a comma-separated list of
               variable names. For example: "LANG,LC_MESSAGES,LC_COLLATE".
               The safelist is ignored for the environment variables HOME,
               SHELL and USER.

           LOGIN_PLAIN_PROMPT (boolean)
               Tell login that printing the hostname should be suppressed in
               the login: prompt. This is an alternative to the -H command
               line option. The default value is no.

           LOGIN_TIMEOUT (number)
               Maximum time in seconds for login. The default value is 60.

           LOGIN_RETRIES (number)
               Maximum number of login retries in case of a bad password. The
               default value is 3.

           LOGIN_KEEP_USERNAME (boolean)
               Tell login to only re-prompt for the password if
               authentication failed, but the username is valid. The default
               value is no.

           FAIL_DELAY (number)
               Delay in seconds before being allowed another three tries
               after a login failure. The default value is 5.

           TTYPERM (string)
               The terminal permissions. The default value is 0600 or 0620 if
               tty group is used. See also mesg(1).

           TTYGROUP (string)
               The login tty will be owned by the TTYGROUP. The default value
               is tty. If the TTYGROUP does not exist, then the ownership of
               the terminal is set to the user’s primary group.

               The TTYGROUP can be either the name of a group or a numeric
               group identifier. See also mesg(1).

           HUSHLOGIN_FILE (string)
               If defined, this file can inhibit all the usual chatter during
               the login sequence. If a full pathname (for example,
               /etc/hushlogins) is specified, then hushed mode will be
               enabled if the user’s name or shell are found in the file. If
               this global hush login file is empty then the hushed mode will
               be enabled for all users.

               If a full pathname is not specified, then hushed mode will be
               enabled if the file exists in the user’s home directory.

               The default is to check /etc/hushlogins and if it does not
               exist then ~/.hushlogin.

               If the HUSHLOGIN_FILE item is empty, then all the checks are
               disabled.

           DEFAULT_HOME (boolean)
               Indicate if login is allowed if we cannot change directory to
               the home directory. If set to yes, the user will login in the
               root (/) directory if it is not possible to change directory
               to their home. The default value is yes.

           LASTLOG_UID_MAX (unsigned number)
               Highest user ID number for which the lastlog entries should be
               updated. As higher user IDs are usually tracked by remote user
               identity and authentication services there is no need to
               create a huge sparse lastlog file for them. No LASTLOG_UID_MAX
               option present in the configuration means that there is no
               user ID limit for writing lastlog entries. The default value
               is ULONG_MAX.

           LOG_UNKFAIL_ENAB (boolean)
               Enable display of unknown usernames when login failures are
               recorded. The default value is no.

               Note that logging unknown usernames may be a security issue if
               a user enters their password instead of their login name.

           ENV_PATH (string)
               If set, it will be used to define the PATH environment
               variable when a regular user logs in. The default value is
               /usr/local/bin:/bin:/usr/bin.

           ENV_ROOTPATH (string), ENV_SUPATH (string)
               If set, it will be used to define the PATH environment
               variable when the superuser logs in. ENV_ROOTPATH takes
               precedence. The default value is
               /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin.

           LOGIN_SHELL_FALLBACK (boolean)
               If set to yes, login will provide a valid shell from
               /etc/shells when the shell specified in /etc/passwd is invalid
               or inaccessible due to administrative errors. This ensures
               users can still log in. However, it may bypass intended shell
               restrictions, potentially causing unexpected behavior if the
               fallback shell differs from the configured one.

## [](#FILES)FILES

           /var/run/utmp, /var/log/wtmp, /var/log/lastlog, /var/spool/mail/*,
           /etc/motd, /etc/passwd, /etc/nologin, /etc/pam.d/login,
           /etc/pam.d/remote, /etc/hushlogins, $HOME/.hushlogin

## [](#CREDENTIALS)CREDENTIALS

           login supports configuration via systemd credentials (see
           https://systemd.io/CREDENTIALS/). login reads the following
           systemd credentials:

           login.noauth (boolean)
               If set, configures login to skip login authentication,
               similarly to the -f option.

## [](#BUGS)BUGS

           The undocumented BSD -r option is not supported. This may be
           required by some rlogind(8) programs.

           A recursive login, as used to be possible in the good old days, no
           longer works; for most purposes su(1) is a satisfactory
           substitute. Indeed, for security reasons, login does a vhangup(2)
           system call to remove any possible listening processes on the tty.
           This is to avoid password sniffing. If one uses the command login,
           then the surrounding shell gets killed by vhangup(2) because it’s
           no longer the true owner of the tty. This can be avoided by using
           exec login in a top-level shell or xterm.

## [](#AUTHORS)AUTHORS

           Derived from BSD login 5.40 (5/9/89) by Michael Glad
           <glad@daimi.dk> for HP-UX. Ported to Linux 0.12: Peter Orbaek
           <poe@daimi.aau.dk>. Rewritten to a PAM-only version by Karel Zak
           <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           mail(1), passwd(1), passwd(5), utmp(5), environ(7), getty(8),
           init(8), lastlog(8), shutdown(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The login command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                       LOGIN(1)

------------------------------------------------------------------------

Pages that refer to this page: [ac(1)](../man1/ac.1.html),  [bash(1)](../man1/bash.1.html),  [chsh(1)](../man1/chsh.1.html),  [last(1@@util-linux)](../man1/last.1@@util-linux.html),  [mesg(1)](../man1/mesg.1.html),  [newgrp(1)](../man1/newgrp.1.html),  [openvt(1)](../man1/openvt.1.html),  [sg(1)](../man1/sg.1.html),  [su(1@@shadow-utils)](../man1/su.1@@shadow-utils.html),  [ul(1)](../man1/ul.1.html),  [crypt(3)](../man3/crypt.3.html),  [pam(3)](../man3/pam.3.html),  [ttyslot(3)](../man3/ttyslot.3.html),  [group(5)](../man5/group.5.html),  [login.defs(5)](../man5/login.defs.5.html),  [motd(5)](../man5/motd.5.html),  [nologin(5)](../man5/nologin.5.html),  [passwd(5)](../man5/passwd.5.html),  [passwd(5@@shadow-utils)](../man5/passwd.5@@shadow-utils.html),  [proc_sys_vm(5)](../man5/proc_sys_vm.5.html),  [securetty(5)](../man5/securetty.5.html),  [shadow(5)](../man5/shadow.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [utmp(5)](../man5/utmp.5.html),  [environ(7)](../man7/environ.7.html),  [agetty(8)](../man8/agetty.8.html),  [faillog(8)](../man8/faillog.8.html),  [nologin(8)](../man8/nologin.8.html),  [nologin(8@@shadow-utils)](../man8/nologin.8@@shadow-utils.html),  [PAM(8)](../man8/PAM.8.html)

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
