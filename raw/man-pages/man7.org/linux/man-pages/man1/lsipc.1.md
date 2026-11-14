---
{"title": "lsipc(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lsipc.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lsipc(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXIT STATUS](#EXIT_STATUS) \| [HISTORY](#HISTORY) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LSIPC(1)                      User Commands                      LSIPC(1)

## [](#NAME)NAME

           lsipc - show information on IPC facilities currently employed in
           the system

## [](#SYNOPSIS)SYNOPSIS

           lsipc [options]

## [](#DESCRIPTION)DESCRIPTION

           lsipc shows information on the POSIX and System V inter-process
           communication facilities for which the calling process has read
           access.

           The default output, as well as the default output from options
           with predefined output columns (like --shmems, etc.), is subject
           to change. So whenever possible, you should avoid using default
           outputs in your scripts. Always explicitly define expected columns
           by using --output columns-list in environments where a stable
           output is required.

## [](#OPTIONS)OPTIONS

           -i, --id id
               Show full details on just the one resource element (System V)
               identified by id. This option needs to be combined with one of
               the three resource options: -m, -q or -s. It is possible to
               override the default output format for this option with the
               --list, --raw, --json or --export option.

           -N, --name name
               Show full details on just the one resource element (POSIX)
               identified by name. This option needs to be combined with one
               of the three resource options: -M, -Q or -S. It is possible to
               override the default output format for this option with the
               --list, --raw, --json or --export option.

           -g, --global
               Show system-wide usage and limits of IPC resources. This
               option may be combined with one of the three resource options:
               -m, -q or -s. The default is to show information about all
               resources.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

       Resource options
           -m, --shmems
               Write information about active System V shared memory
               segments.

           -M, --posix-shmems
               Write information about active POSIX shared memory segments.

           -q, --queues
               Write information about active System V message queues.

           -Q, --posix-mqueues
               Write information about active POSIX message queues.

           -s, --semaphores
               Write information about active System V semaphore sets.

           -S, --posix-semaphores
               Write information about active POSIX named semaphores.

       Output formatting
           -c, --creator
               Show creator and owner.

           -e, --export
               Produce output in the form of key="value" pairs. All
               potentially unsafe value characters are hex-escaped
               (\x<code>). See also option --shell.

           -J, --json
               Use the JSON output format.

           -l, --list
               Use the list output format. This is the default, except when
               --id is used.

           -n, --newline
               Display each piece of information on a separate line.

           --noheadings
               Do not print a header line.

           --notruncate
               Don’t truncate output.

           -o, --output list
               Specify which output columns to print. Use --help to get a
               list of all supported columns.

           -b, --bytes
               Print size in bytes rather than in human readable format.

           -r, --raw
               Raw output (no columnation).

           -t, --time
               Write time information. The time of the last control operation
               that changed the access permissions for all facilities, the
               time of the last msgsnd(2) and msgrcv(2) operations on message
               queues, the time of the last shmat(2) and shmdt(2) operations
               on shared memory, and the time of the last semop(2) operation
               on semaphores.

           --time-format type
               Display dates in short, full or iso format. The default is
               short, this time format is designed to be space efficient and
               human readable.

           -P, --numeric-perms
               Print numeric permissions in PERMS column.

           -y, --shell
               The column name will be modified to contain only characters
               allowed for shell variable identifiers. This is usable, for
               example, with --export. Note that this feature has been
               automatically enabled for --export in version 2.37, but due to
               compatibility issues, now it’s necessary to request this
               behavior by --shell.

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

## [](#EXIT_STATUS)EXIT STATUS

           0
               if OK,

           1
               if incorrect arguments specified,

           2
               if a serious error occurs.

## [](#HISTORY)HISTORY

           The lsipc utility is inspired by the ipcs(1) utility.

## [](#AUTHORS)AUTHORS

           Ondrej Oprala <ooprala@redhat.com>, Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           ipcmk(1), ipcrm(1), msgrcv(2), msgsnd(2), semget(2), semop(2),
           shmat(2), shmdt(2), shmget(2), sysvipc(7)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The lsipc command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                       LSIPC(1)

------------------------------------------------------------------------

Pages that refer to this page: [ipcmk(1)](../man1/ipcmk.1.html),  [ipcrm(1)](../man1/ipcrm.1.html),  [sysvipc(7)](../man7/sysvipc.7.html)

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
