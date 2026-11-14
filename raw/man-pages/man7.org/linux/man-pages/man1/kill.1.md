---
{"title": "kill(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/kill.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# kill(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    KILL(1)                       User Commands                       KILL(1)

## [](#NAME)NAME

           kill - terminate a process

## [](#SYNOPSIS)SYNOPSIS

           kill  [-signal|-s signal|-p]  [-q value] [-a] [--timeout
           milliseconds signal] [--] PID[:_inode_]...

           kill  [-signal|-s signal] PID[:_inode_]...

           kill -l [number|0xsigmask] | -L

           kill -d PID[:_inode_]

## [](#DESCRIPTION)DESCRIPTION

           The command kill sends the specified signal to the specified
           processes or process groups.

           If no signal is specified, the TERM signal is sent. The default
           action for this signal is to terminate the process. This signal
           should be used in preference to the KILL signal (number 9), since
           a process may install a handler for the TERM signal in order to
           perform clean-up steps before terminating in an orderly fashion.
           If a process does not terminate after a TERM signal has been sent,
           then the KILL signal may be used; be aware that the latter signal
           cannot be caught, and so does not give the target process the
           opportunity to perform any clean-up before terminating.

           Most modern shells have a built-in kill command, with a usage
           rather similar to that of the command described here. The --all,
           --pid, and --queue options, and the possibility to specify
           processes by command name, are local extensions.

           If signal is 0, then no actual signal is sent, but error checking
           is still performed.

## [](#ARGUMENTS)ARGUMENTS

           The list of processes to be signaled can be a mixture of names and
           PIDs.

           PID
               Each PID can be expressed in one of the following ways:

               n
                   where n is larger than 0. The process with PID n is
                   signaled.

               0
                   All processes in the calling process group are signaled.

               -1
                   All processes with a PID larger than 1 are signaled.

               -n
                   where n is larger than 1. All processes in process group n
                   are signaled. When an argument of the form '-n' is given,
                   and it is meant to denote a process group, either a signal
                   must be specified first, or the argument must be preceded
                   by a '--' option, otherwise it will be taken as the signal
                   to send.

           PID:_inode_
               A process can be referenced with the format PID:inode, where
               the inode uniquely identifies the process identity in the
               pidfs. This feature enables race-free process signalling and
               requires kernel version 6.9 or later. Note that this only
               works for the option --signal and the -signal notation.
               Lastly, to retrieve a process’s inode number you can use the
               getino(1) utility.

           name
               All processes invoked using this name will be signaled.

## [](#OPTIONS)OPTIONS

           -s, --signal signal
               The signal to send. It may be given as a name or a number.

           -l, --list [number|0xsigmask]
               Print a list of signal names, convert the given signal number
               to a name, or convert the given signal mask to names. The
               signals can be found in /usr/include/linux/signal.h.

                   $ ps s $$
                     UID     PID          PENDING          BLOCKED          IGNORED           CAUGHT STAT TTY        TIME COMMAND
                    1000 1608069 0000000000000000 0000000000000002 0000000000384000 0000000008013003 Ss   pts/44     0:02 zsh
                   $ kill -l 0x0000000000384000
                   TERM
                   TSTP
                   TTIN
                   TTOU

               If neither NUMBER nor 0xSIGMASK is given, list all signal
               names. In that case, print one signal per line when the output
               is not a terminal.

           -L, --table
               Similar to -l, but it will print signal names and their
               corresponding numbers. Print one signal per line when the
               output is not a terminal.

           -a, --all
               Do not restrict the command-name-to-PID conversion to
               processes with the same UID as the present process.

           -p, --pid
               Only print the process ID (PID) of the named processes, do not
               send any signals.

           -r, --require-handler
               Do not send the signal if it is not caught in userspace by the
               signalled process.

           --verbose
               Print PID(s) that will be signaled with kill along with the
               signal.

           -q, --queue value
               Send the signal using sigqueue(3) rather than kill(2). The
               value argument is an integer that is sent along with the
               signal. If the receiving process has installed a handler for
               this signal using the SA_SIGINFO flag to sigaction(2), then it
               can obtain this data via the si_sigval field of the siginfo_t
               structure.

           --timeout milliseconds signal
               Send a signal defined in the usual way to a process, followed
               by an additional signal after a specified delay. The --timeout
               option causes kill to wait for a period defined in
               milliseconds before sending a follow-up signal to the process.
               This feature is implemented using the Linux kernel PID file
               descriptor feature in order to guarantee that the follow-up
               signal is sent to the same process or not sent if the process
               no longer exists.

               Note that the operating system may re-use PIDs and
               implementing an equivalent feature in a shell using kill and
               sleep would be subject to races whereby the follow-up signal
               might be sent to a different process that used a recycled PID.

               The --timeout option can be specified multiple times: the
               signals are sent sequentially with the specified timeouts. The
               --timeout option can be combined with the --queue option.

               As an example, the following command sends the signals QUIT,
               TERM and KILL in sequence and waits for 1000 milliseconds
               between sending the signals:

                   kill --verbose --timeout 1000 TERM --timeout 1000 KILL \
                           --signal QUIT 12345

           -d, --show-process-state pid
               Decode signal related fields in /proc/pid/status.

                   $ kill -d $$
                   Blocked: INT
                   Ignored: TERM TSTP TTIN TTOU
                   Caught: HUP INT PIPE ALRM CHLD WINCH

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           kill has the following exit status values:

           0
               success

           1
               failure

           64
               partial success (when more than one process specified)

## [](#NOTES)NOTES

           Although it is possible to specify the TID (thread ID, see
           gettid(2)) of one of the threads in a multithreaded process as the
           argument of kill, the signal is nevertheless directed to the
           process (i.e., the entire thread group). In other words, it is not
           possible to send a signal to an explicitly selected thread in a
           multithreaded process. The signal will be delivered to an
           arbitrarily selected thread in the target process that is not
           blocking the signal. For more details, see signal(7) and the
           description of CLONE_THREAD in clone(2).

           Various shells provide a built-in kill command that is preferred
           in relation to the kill(1) executable described by this manual.
           The easiest way to ensure one is executing the command described
           in this page is to use the full path when calling the command, for
           example: /bin/kill --version

## [](#AUTHORS)AUTHORS

           Salvatore Valente <svalente@mit.edu>, Karel Zak <kzak@redhat.com>

           The original version was taken from BSD 4.4.

## [](#SEE_ALSO)SEE ALSO

           bash(1), tcsh(1), getino(1), sigaction(2), kill(2), sigqueue(3),
           signal(7), proc(5), proc_pid_status(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The kill command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                        KILL(1)

------------------------------------------------------------------------

Pages that refer to this page: [fuser(1)](../man1/fuser.1.html),  [getino(1)](../man1/getino.1.html),  [kill(1)](../man1/kill.1.html),  [killall(1)](../man1/killall.1.html),  [pgrep(1)](../man1/pgrep.1.html),  [pmsignal(1)](../man1/pmsignal.1.html),  [skill(1)](../man1/skill.1.html),  [tcpdump(1)](../man1/tcpdump.1.html),  [timeout(1)](../man1/timeout.1.html),  [xargs(1)](../man1/xargs.1.html),  [kill(2)](../man2/kill.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [signal(2)](../man2/signal.2.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [signal(7)](../man7/signal.7.html),  [ldattach(8)](../man8/ldattach.8.html),  [lsof(8)](../man8/lsof.8.html),  [systemd-coredump(8)](../man8/systemd-coredump.8.html),  [tcpdump(8)](../man8/tcpdump.8.html)

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
