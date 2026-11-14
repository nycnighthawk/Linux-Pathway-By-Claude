---
{"title": "lslocks(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lslocks.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lslocks(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [OUTPUT](#OUTPUT) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LSLOCKS(8)                System Administration                LSLOCKS(8)

## [](#NAME)NAME

           lslocks - list local system locks

## [](#SYNOPSIS)SYNOPSIS

           lslocks [options]

## [](#DESCRIPTION)DESCRIPTION

           lslocks lists information about all the currently held file locks
           in a Linux system.

## [](#OPTIONS)OPTIONS

           -b, --bytes
               Print sizes in bytes rather than in human-readable form.

               By default, sizes are shown in units that are powers of 1024
               bytes. The formal abbreviations for these units (KiB, MiB,
               GiB, ...) are further shortened to just their first letter: K,
               M, G, ....

           -H, --list-columns
               List the columns that can be specified with the --output
               option. Can be used with --json or --raw to get the list in a
               machine-readable format.

           -i, --noinaccessible
               Ignore lock files which are inaccessible for the current user.

           -J, --json
               Use JSON output format.

           -n, --noheadings
               Do not print a header line.

           -o, --output list
               Specify which output columns to print. Use --help to get a
               list of all supported columns.

               The default list of columns may be extended if list is
               specified in the format +list (e.g., lslocks -o +BLOCKER).

           --output-all
               Output all available columns.

           -p, --pid pid
               Display only the locks held by the process with this pid.

           -Q, --filter expr
               Print only the locks that meet the conditions specified by the
               expr.

               This feature is EXPERIMENTAL. See also scols-filter(5). For
               example exclude POSIX type locks, but print all READ mode ones
               locks on files with .qcow2 as extension:

                  lslocks --filter 'TYPE != "POSIX" and MODE == "READ" and PATH =~ ".*\.qcow2"'

           --pager
               Pipe output into a pager (by default less(1)). The pager
               freezes the header line so column names stay visible while
               scrolling. The PAGER environment variable overrides the
               default pager program. Mutually exclusive with --json and
               --raw.

           --nopager
               Do not pipe output into a pager. Overrides the PAGER_ENABLE
               environment variable.

           -r, --raw
               Use the raw output format.

           -u, --notruncate
               Do not truncate text in columns.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

           LIBSMARTCOLS_JSON=compact|lines
               Control JSON output format when using --json. Supported values
               are compact for JSON output with minimal whitespace, and lines
               for JSON Lines format (one JSON object per line). If unset or
               set to any other value, pretty-printed JSON is used.

           LSLOCKS_COLUMNS=
               Specify a comma-separated list of output columns to print. All
               columns listed by --list-columns can be used.

           PAGER_ENABLE=
               If set to a recognized boolean value (e.g. "yes", "true",
               "on", "1"), automatically pipe output through a pager. The
               --pager and --nopager command-line options override this
               variable. Ignored when standard output is not a terminal, and
               in privileged (setuid/setgid) contexts. This is a
               project-independent variable; other tools may support it as
               well.

## [](#OUTPUT)OUTPUT

           COMMAND
               The command name of the process holding the lock.

           PID
               The process ID of the process.

           TYPE
               The type of lock; can be LEASE (created with fcntl(2)), FLOCK
               (created with flock(2)), POSIX (created with fcntl(2) and
               lockf(3)) or OFDLCK (created with fcntl(2)).

           SIZE
               Size of the locked file.

           INODE
               The inode number.

           MAJ:MIN
               The major:minor device number.

           MODE
               The lock’s access permissions (read, write). If the process is
               blocked and waiting for the lock, then the mode is postfixed
               with an '*' (asterisk).

           M
               Whether the lock is mandatory; 0 means no (meaning the lock is
               only advisory), 1 means yes. (See fcntl(2).)

           START
               Relative byte offset of the lock.

           END
               Ending offset of the lock.

           PATH
               Full path of the lock. If none is found, or there are no
               permissions to read the path, it will fall back to the
               device’s mountpoint and "..." is appended to the path. The
               path might be truncated; use --notruncate to get the full
               path.

           BLOCKER
               The PID of the process which blocks the lock.

           HOLDERS
               The holder(s) of the lock. The format of the holder is
               PID,COMMAND,FD. If a lock is an open file description-oriented
               lock, there can be more than one holder for the lock. See the
               NOTES below.

## [](#NOTES)NOTES

           The lslocks command is meant to replace the lslk(8) command,
           originally written by Victor A. Abell <abe@purdue.edu> and
           unmaintained since 2001.

           "The process holding the lock" for leases, FLOCK locks, and OFD
           locks is a fake-concept. They are associated with the open file
           description on which they are acquired. With fork(2) and/or
           cmsg(3), multiple processes can share an open file description. So
           the holder process of a lease (or a lock) is not uniquely
           determined. lslocks shows the one of the holder processes in
           COMMAND and PID columns.

           The default output is subject to change. So whenever possible, you
           should avoid using default output in your scripts.

           For OFD locks, the PID column may show -1. Such lines cannot be
           selected by the filter, because the current filter engine does not
           support negative numbers.

## [](#AUTHORS)AUTHORS

           Davidlohr Bueso <dave@gnu.org> Christian Goeschel Ndjomouo
           <cgoesc2@wgu.edu>

## [](#SEE_ALSO)SEE ALSO

           flock(1), fcntl(2), lockf(3), scols-filter(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The lslocks command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     LSLOCKS(8)

------------------------------------------------------------------------

Pages that refer to this page: [lsfd(1)](../man1/lsfd.1.html),  [fcntl(2)](../man2/fcntl.2.html),  [fcntl_locking(2)](../man2/fcntl_locking.2.html),  [flock(2)](../man2/flock.2.html),  [proc_locks(5)](../man5/proc_locks.5.html)

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
