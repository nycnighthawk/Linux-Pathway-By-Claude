---
{"title": "getino(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/getino.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getino(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GETINO(1)                     User Commands                     GETINO(1)

## [](#NAME)NAME

           getino - print the unique inode number associated to a process
           file descriptor or namespace for a given PID

## [](#SYNOPSIS)SYNOPSIS

           getino
           [--pidfs|--cgroupns|--ipcns|--netns|--mntns|--pidns|--timens|--userns|--utsns]
           [--print-pid|-p] PID[:inode]...

           getino [--print-pid|-p] PID[:inode]...

           getino PID[:inode]...

## [](#DESCRIPTION)DESCRIPTION

           getino is a simple command that prints the inode numbers
           associated with the process file descriptor (pidfd) or namespace
           for all PIDs passed to it as arguments.

           The kernel guarantees that the inode number associated with a
           process’s file descriptor is exempt from reuse during the current
           boot cycle; therefore, a process can be uniquely identified by its
           PID and the inode number, conveniently so with the format
           'PID:inode'. As an example, this enables race-free signalling of
           processes with kill(1), which accepts the aforementioned PID
           format.

           Inode numbers associated with a namespace for a given process are
           essentially namespace IDs, identical to the inode number reported
           by /proc/pid/ns/nstype, see namespaces(7) for more details.

## [](#OPTIONS)OPTIONS

           -p, --print-pid
               Print both the PID and pidfd/namespace inode separated by a
               colon ':', in respective order. This format convention can be
               used to address processes in a race-free manner, e.g. for
               signalling with the kill(1) command.

           --pidfs
               Print the unique inode number for a process’s pidfs file
               descriptor.

           --cgroupns
               Print the unique cgroup namespace inode number. See
               cgroup_namespaces(7)

           --ipcns
               Print the unique ipc namespace inode number. See
               ipc_namespaces(7)

           --netns
               Print the unique network namespace inode number. See
               network_namespaces(7)

           --mntns
               Print the unique mount namespace inode number. See
               mount_namespaces(7)

           --pidns
               Print the unique pid namespace inode number. See
               pid_namespaces(7)

           --timens
               Print the unique time namespace inode number. See
               time_namespaces(7)

           --userns
               Print the unique user namespace inode number. See
               user_namespaces(7)

           --utsns
               Print the unique uts namespace inode number. See
               uts_namespaces(7)

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           getino has the following exit status values:

           0
               success

           1
               unspecified failure

## [](#NOTES)NOTES

           getino requires support for the pidfs pseudo-filesystem
           (introduced in Linux version 6.9), to retrieve a valid inode for a
           process file descriptor.

## [](#AUTHORS)AUTHORS

           Christian Goeschel Ndjomouo <cgoesc2@wgu.edu>

## [](#SEE_ALSO)SEE ALSO

           kill(1), pidfd_open(2), namespaces(7)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The getino command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                      GETINO(1)

------------------------------------------------------------------------

Pages that refer to this page: [chrt(1)](../man1/chrt.1.html),  [kill(1)](../man1/kill.1.html),  [nsenter(1)](../man1/nsenter.1.html),  [prlimit(1)](../man1/prlimit.1.html),  [waitpid(1)](../man1/waitpid.1.html)

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
