---
{"title": "environ(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/environ.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# environ(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    environ(7)           Miscellaneous Information Manual          environ(7)

## [](#NAME)NAME

           environ - user environment

## [](#SYNOPSIS)SYNOPSIS

           extern char **environ;

## [](#DESCRIPTION)DESCRIPTION

           The variable environ points to an array of pointers to strings
           called the "environment".  The last pointer in this array has the
           value NULL.  This array of strings is made available to the
           process by the execve(2) call when a new program is started.  When
           a child process is created via fork(2), it inherits a copy of its
           parent's environment.

           By convention, the strings in environ have the form "name=value".
           The name is case-sensitive and may not contain the character "=".
           The value can be anything that can be represented as a string.
           The name and the value may not contain an embedded null byte
           ('\0'), since this is assumed to terminate the string.

           Environment variables may be placed in the shell's environment by
           the export command in sh(1), or by the setenv command if you use
           csh(1).

           The initial environment of the shell is populated in various ways,
           such as definitions from /etc/environment that are processed by
           pam_env(8) for all users at login time (on systems that employ
           pam(8)).  In addition, various shell initialization scripts, such
           as the system-wide /etc/profile script and per-user initialization
           scripts may include commands that add variables to the shell's
           environment; see the manual page of your preferred shell for
           details.

           Bourne-style shells support the syntax

               NAME=value command

           to create an environment variable definition only in the scope of
           the process that executes command.  Multiple variable definitions,
           separated by white space, may precede command.

           Arguments may also be placed in the environment at the point of an
           exec(3).  A C program can manipulate its environment using the
           functions getenv(3), putenv(3), setenv(3), and unsetenv(3).

           What follows is a list of environment variables typically seen on
           a system.  This list is incomplete and includes only common
           variables seen by average users in their day-to-day routine.
           Environment variables specific to a particular program or library
           function are documented in the ENVIRONMENT section of the
           appropriate manual page.

           USER   The name of the logged-in user (used by some BSD-derived
                  programs).  Set at login time; see section NOTES below.

           LOGNAME
                  The name of the logged-in user (used by some System-V
                  derived programs).  Set at login time; see section NOTES
                  below.

           HOME   A user's login directory.  Set at login time; see section
                  NOTES below.

           LANG   The name of a locale to use for locale categories when not
                  overridden by LC_ALL or more specific environment variables
                  such as LC_COLLATE, LC_CTYPE, LC_MESSAGES, LC_MONETARY,
                  LC_NUMERIC, and LC_TIME (see locale(7) for further details
                  of the LC_* environment variables).

           PATH   The sequence of directory prefixes that sh(1) and many
                  other programs employ when searching for an executable file
                  that is specified as a simple filename (i.a., a pathname
                  that contains no slashes).  The prefixes are separated by
                  colons (:).  The list of prefixes is searched from
                  beginning to end, by checking the pathname formed by
                  catenating a prefix, a slash, and the filename, until a
                  file with execute permission is found.

                  As a legacy feature, a zero-length prefix (specified as two
                  adjacent colons, or an initial or terminating colon) is
                  interpreted to mean the current working directory.
                  However, use of this feature is deprecated, and POSIX notes
                  that a conforming application shall use an explicit
                  pathname (e.g., .)  to specify the current working
                  directory.

                  Analogously to PATH, one has CDPATH, used by some shells to
                  find the target of a change directory command, MANPATH used
                  by man(1) to find manual pages, and so on.

           PWD    Absolute path to the current working directory; required to
                  be partially canonical (no . or .. components).

           SHELL  The absolute pathname of the user's login shell.  Set at
                  login time, see section NOTES below.

           TERM   The terminal type for which output is to be prepared.

           PAGER  The user's preferred utility to display text files.  Any
                  string acceptable as a command-string operand to the sh -c
                  command shall be valid.  If PAGER is null or is not set,
                  then applications that launch a pager will default to a
                  program such as less(1) or more(1).

           EDITOR/VISUAL
                  The user's preferred utility to edit text files.  Any
                  string acceptable as a command_string operand to the sh -c
                  command shall be valid.

           Note that the behavior of many programs and library routines is
           influenced by the presence or value of certain environment
           variables.  Examples include the following:

           •  The variables LANG, LANGUAGE, NLSPATH, LOCPATH, LC_ALL,
              LC_MESSAGES, and so on influence locale handling; see
              catopen(3), gettext(3), and locale(7).

           •  TMPDIR influences the path prefix of names created by
              tempnam(3) and other routines, and the temporary directory used
              by sort(1) and other programs.

           •  LD_LIBRARY_PATH, LD_PRELOAD, and other LD_* variables influence
              the behavior of the dynamic loader/linker.  See also ld.so(8).

           •  POSIXLY_CORRECT makes certain programs and library routines
              follow the prescriptions of POSIX.

           •  The behavior of malloc(3) is influenced by MALLOC_* variables.

           •  The variable HOSTALIASES gives the name of a file containing
              aliases to be used with gethostbyname(3).

           •  TZ and TZDIR give timezone information used by tzset(3) and
              through that by functions like ctime(3), localtime(3),
              mktime(3), strftime(3).  See also tzselect(8).

           •  TERMCAP gives information on how to address a given terminal
              (or gives the name of a file containing such information).

           •  COLUMNS and LINES tell applications about the window size,
              possibly overriding the actual size.

           •  PRINTER or LPDEST may specify the desired printer to use.  See
              lpr(1).

## [](#NOTES)NOTES

           Historically and by standard, environ must be declared in the user
           program.  However, as a (nonstandard) programmer convenience,
           environ is declared in the header file <unistd.h> if the
           _GNU_SOURCE feature test macro is defined (see
           feature_test_macros(7)).

           The prctl(2) PR_SET_MM_ENV_START and PR_SET_MM_ENV_END operations
           can be used to control the location of the process's environment.

           The HOME, LOGNAME, SHELL, and USER variables are set when the user
           is changed via a session management interface, typically by a
           program such as login(1) from a user database (such as passwd(5)).
           (Switching to the root user using su(1) may result in a mixed
           environment where LOGNAME and USER are retained from old user; see
           the su(1) manual page.)

## [](#BUGS)BUGS

           Clearly there is a security risk here.  Many a system command has
           been tricked into mischief by a user who specified unusual values
           for IFS or LD_LIBRARY_PATH.

           There is also the risk of name space pollution.  Programs like
           make and autoconf allow overriding of default utility names from
           the environment with similarly named variables in all caps.  Thus
           one uses CC to select the desired C compiler (and similarly MAKE,
           AR, AS, FC, LD, LEX, RM, YACC, etc.).  However, in some
           traditional uses, such an environment variable gives options for
           the program instead of a pathname.  Thus, one has MORE and LESS.
           Such usage is considered mistaken, and to be avoided in new
           programs.

## [](#SEE_ALSO)SEE ALSO

           bash(1), csh(1), env(1), login(1), printenv(1), sh(1), su(1),
           tcsh(1), execve(2), clearenv(3), exec(3), getenv(3), putenv(3),
           setenv(3), unsetenv(3), locale(7), ld.so(8), pam_env(8)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2026-02-08                     environ(7)

------------------------------------------------------------------------

Pages that refer to this page: [login(1)](../man1/login.1.html),  [pcp2arrow(1)](../man1/pcp2arrow.1.html),  [pcp2json(1)](../man1/pcp2json.1.html),  [pcp2openmetrics(1)](../man1/pcp2openmetrics.1.html),  [pcp2opentelemetry(1)](../man1/pcp2opentelemetry.1.html),  [pcp2template(1)](../man1/pcp2template.1.html),  [pcp2xlsx(1)](../man1/pcp2xlsx.1.html),  [pcp2xml(1)](../man1/pcp2xml.1.html),  [pcp-atopsar(1)](../man1/pcp-atopsar.1.html),  [pcp-buddyinfo(1)](../man1/pcp-buddyinfo.1.html),  [pcp-free(1)](../man1/pcp-free.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pcp-meminfo(1)](../man1/pcp-meminfo.1.html),  [pcp-mpstat(1)](../man1/pcp-mpstat.1.html),  [pcp-netstat(1)](../man1/pcp-netstat.1.html),  [pcp-nfsiostat(1)](../man1/pcp-nfsiostat.1.html),  [pcp-pidstat(1)](../man1/pcp-pidstat.1.html),  [pcp-ps(1)](../man1/pcp-ps.1.html),  [pcp-rocestat(1)](../man1/pcp-rocestat.1.html),  [pcp-slabinfo(1)](../man1/pcp-slabinfo.1.html),  [pcp-uptime(1)](../man1/pcp-uptime.1.html),  [pcp-xsos(1)](../man1/pcp-xsos.1.html),  [pcp-zoneinfo(1)](../man1/pcp-zoneinfo.1.html),  [pmchart(1)](../man1/pmchart.1.html),  [pmclient(1)](../man1/pmclient.1.html),  [pmdiff(1)](../man1/pmdiff.1.html),  [pmdumptext(1)](../man1/pmdumptext.1.html),  [pmie(1)](../man1/pmie.1.html),  [pminfo(1)](../man1/pminfo.1.html),  [pmlc(1)](../man1/pmlc.1.html),  [pmlogcheck(1)](../man1/pmlogcheck.1.html),  [pmlogdump(1)](../man1/pmlogdump.1.html),  [pmlogextract(1)](../man1/pmlogextract.1.html),  [pmloglabel(1)](../man1/pmloglabel.1.html),  [pmlogreduce(1)](../man1/pmlogreduce.1.html),  [pmlogsummary(1)](../man1/pmlogsummary.1.html),  [pmprobe(1)](../man1/pmprobe.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [pmseries(1)](../man1/pmseries.1.html),  [pmstat(1)](../man1/pmstat.1.html),  [pmval(1)](../man1/pmval.1.html),  [pmview(1)](../man1/pmview.1.html),  [tset(1)](../man1/tset.1.html),  [execve(2)](../man2/execve.2.html),  [clearenv(3)](../man3/clearenv.3.html),  [exec(3)](../man3/exec.3.html),  [getenv(3)](../man3/getenv.3.html),  [intro(3)](../man3/intro.3.html),  [pmgetconfig(3)](../man3/pmgetconfig.3.html),  [pmnewcontextzone(3)](../man3/pmnewcontextzone.3.html),  [pmnewzone(3)](../man3/pmnewzone.3.html),  [putenv(3)](../man3/putenv.3.html),  [sd_bus_default(3)](../man3/sd_bus_default.3.html),  [setenv(3)](../man3/setenv.3.html),  [udev_device_new_from_syspath(3)](../man3/udev_device_new_from_syspath.3.html),  [localtime(5)](../man5/localtime.5.html),  [nfs.conf(5)](../man5/nfs.conf.5.html),  [pam_env.conf(5)](../man5/pam_env.conf.5.html),  [proc_pid_environ(5)](../man5/proc_pid_environ.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd-system.conf(5)](../man5/systemd-system.conf.5.html),  [pam_env(8)](../man8/pam_env.8.html)

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
