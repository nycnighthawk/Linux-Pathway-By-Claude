---
{"title": "F_GETSIG(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/F_SETOWN.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# F_GETSIG(2const) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    F_GETSIG(2const)                                         F_GETSIG(2const)

## [](#NAME)NAME

           F_GETOWN, F_SETOWN, F_GETOWN_EX, F_SETOWN_EX, F_GETSIG, F_SETSIG -
           managing signals

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <fcntl.h>

           int fcntl(int fd, F_GETOWN);
           int fcntl(int fd, F_SETOWN, int arg);

           #define _GNU_SOURCE
           #include <fcntl.h>

           int fcntl(int fd, F_GETOWN_EX, struct f_owner_ex *arg);
           int fcntl(int fd, F_SETOWN_EX, const struct f_owner_ex *arg);
           int fcntl(int fd, F_GETSIG);
           int fcntl(int fd, F_SETSIG, int arg);

## [](#DESCRIPTION)DESCRIPTION

           F_GETOWN, F_SETOWN, F_GETOWN_EX, F_SETOWN_EX, F_GETSIG, and
           F_SETSIG are used to manage I/O availability signals:

           F_GETOWN
                  Return (as the function result) the process ID or process
                  group ID currently receiving SIGIO and SIGURG signals for
                  events on file descriptor fd.  Process IDs are returned as
                  positive values; process group IDs are returned as negative
                  values (but see BUGS below).  arg is ignored.

           F_SETOWN
                  Set the process ID or process group ID that will receive
                  SIGIO and SIGURG signals for events on the file descriptor
                  fd.  The target process or process group ID is specified in
                  arg.  A process ID is specified as a positive value; a
                  process group ID is specified as a negative value.  Most
                  commonly, the calling process specifies itself as the owner
                  (that is, arg is specified as getpid(2)).

                  As well as setting the file descriptor owner, one must also
                  enable generation of signals on the file descriptor.  This
                  is done by using the F_SETFL(2const) operation to set the
                  O_ASYNC file status flag on the file descriptor.
                  Subsequently, a SIGIO signal is sent whenever input or
                  output becomes possible on the file descriptor.  The
                  fcntl() F_SETSIG operation can be used to obtain delivery
                  of a signal other than SIGIO.

                  Sending a signal to the owner process (group) specified by
                  F_SETOWN is subject to the same permissions checks as are
                  described for kill(2), where the sending process is the one
                  that employs F_SETOWN (but see BUGS below).  If this
                  permission check fails, then the signal is silently
                  discarded.  Note: The F_SETOWN operation records the
                  caller's credentials at the time of the fcntl() call, and
                  it is these saved credentials that are used for the
                  permission checks.

                  If the file descriptor fd refers to a socket, F_SETOWN also
                  selects the recipient of SIGURG signals that are delivered
                  when out-of-band data arrives on that socket.  (SIGURG is
                  sent in any situation where select(2) would report the
                  socket as having an "exceptional condition".)

                  The following was true in Linux 2.6.x up to and including
                  Linux 2.6.11:

                         If a nonzero value is given to F_SETSIG in a
                         multithreaded process running with a threading
                         library that supports thread groups (e.g., NPTL),
                         then a positive value given to F_SETOWN has a
                         different meaning: instead of being a process ID
                         identifying a whole process, it is a thread ID
                         identifying a specific thread within a process.
                         Consequently, it may be necessary to pass F_SETOWN
                         the result of gettid(2) instead of getpid(2) to get
                         sensible results when F_SETSIG is used.  (In current
                         Linux threading implementations, a main thread's
                         thread ID is the same as its process ID.  This means
                         that a single-threaded program can equally use
                         gettid(2) or getpid(2) in this scenario.)  Note,
                         however, that the statements in this paragraph do
                         not apply to the SIGURG signal generated for out-of-
                         band data on a socket: this signal is always sent to
                         either a process or a process group, depending on
                         the value given to F_SETOWN.

                  The above behavior was accidentally dropped in Linux
                  2.6.12, and won't be restored.  From Linux 2.6.32 onward,
                  use F_SETOWN_EX to target SIGIO and SIGURG signals at a
                  particular thread.

           F_GETOWN_EX
                  Return the current file descriptor owner settings as
                  defined by a previous F_SETOWN_EX operation.  The
                  information is returned in the structure pointed to by arg,
                  which has the following form:

                      struct f_owner_ex {
                          int   type;
                          pid_t pid;
                      };

                  The type field will have one of the values F_OWNER_TID,
                  F_OWNER_PID, or F_OWNER_PGRP.  The pid field is a positive
                  integer representing a thread ID, process ID, or process
                  group ID.  See F_SETOWN_EX for more details.

           F_SETOWN_EX
                  This operation performs a similar task to F_SETOWN.  It
                  allows the caller to direct I/O availability signals to a
                  specific thread, process, or process group.  The caller
                  specifies the target of signals via arg, which is a pointer
                  to a f_owner_ex structure.  The type field has one of the
                  following values, which define how pid is interpreted:

                  F_OWNER_TID
                         Send the signal to the thread whose thread ID (the
                         value returned by a call to clone(2) or gettid(2))
                         is specified in pid.

                  F_OWNER_PID
                         Send the signal to the process whose ID is specified
                         in pid.

                  F_OWNER_PGRP
                         Send the signal to the process group whose ID is
                         specified in pid.  (Note that, unlike with F_SETOWN,
                         a process group ID is specified as a positive value
                         here.)

           F_GETSIG
                  Return (as the function result) the signal sent when input
                  or output becomes possible.  A value of zero means SIGIO is
                  sent.  Any other value (including SIGIO) is the signal sent
                  instead, and in this case additional info is available to
                  the signal handler if installed with SA_SIGINFO.  arg is
                  ignored.

           F_SETSIG
                  Set the signal sent when input or output becomes possible
                  to the value given in arg.  A value of zero means to send
                  the default SIGIO signal.  Any other value (including
                  SIGIO) is the signal to send instead, and in this case
                  additional info is available to the signal handler if
                  installed with SA_SIGINFO.

                  By using F_SETSIG with a nonzero value, and setting
                  SA_SIGINFO for the signal handler (see sigaction(2)), extra
                  information about I/O events is passed to the handler in a
                  siginfo_t structure.  If the si_code field indicates the
                  source is SI_SIGIO, the si_fd field gives the file
                  descriptor associated with the event.  Otherwise, there is
                  no indication which file descriptors are pending, and you
                  should use the usual mechanisms (select(2), poll(2),
                  read(2) with O_NONBLOCK set etc.) to determine which file
                  descriptors are available for I/O.

                  Note that the file descriptor provided in si_fd is the one
                  that was specified during the F_SETSIG operation.  This can
                  lead to an unusual corner case.  If the file descriptor is
                  duplicated (dup(2) or similar), and the original file
                  descriptor is closed, then I/O events will continue to be
                  generated, but the si_fd field will contain the number of
                  the now closed file descriptor.

                  By selecting a real time signal (value >= SIGRTMIN),
                  multiple I/O events may be queued using the same signal
                  numbers.  (Queuing is dependent on available memory.)
                  Extra information is available if SA_SIGINFO is set for the
                  signal handler, as above.

                  Note that Linux imposes a limit on the number of real-time
                  signals that may be queued to a process (see getrlimit(2)
                  and signal(7)) and if this limit is reached, then the
                  kernel reverts to delivering SIGIO, and this signal is
                  delivered to the entire process rather than to a specific
                  thread.

           Using these mechanisms, a program can implement fully asynchronous
           I/O without using select(2) or poll(2) most of the time.

           The use of O_ASYNC is specific to BSD and Linux.  The only use of
           F_GETOWN and F_SETOWN specified in POSIX.1 is in conjunction with
           the use of the SIGURG signal on sockets.  (POSIX does not specify
           the SIGIO signal.)  F_GETOWN_EX, F_SETOWN_EX, F_GETSIG, and
           F_SETSIG are Linux-specific.  POSIX has asynchronous I/O and the
           aio_sigevent structure to achieve similar things; these are also
           available in Linux as part of the GNU C Library (glibc).

## [](#RETURN_VALUE)RETURN VALUE

           See fcntl(2).

           F_GETOWN
                  Value of file descriptor owner.

           F_GETSIG
                  Value of signal sent when read or write becomes possible,
                  or zero for traditional SIGIO behavior.

           F_SETOWN
           F_GETOWN_EX
           F_SETOWN_EX
           F_SETSIG
                  Zero.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           See fcntl(2).

           EINVAL op is F_SETSIG and arg is not an allowable signal number.

## [](#STANDARDS)STANDARDS

           F_GETOWN
           F_SETOWN
           F_GETOWN_EX
           F_SETOWN_EX
                  POSIX.1-2024.

           F_GETSIG
           F_SETSIG
                  Linux.  (Define the _GNU_SOURCE macro to obtain these
                  definitions.)

## [](#HISTORY)HISTORY

           F_GETOWN
           F_SETOWN
                  POSIX.1-2001.  (To get their definitions, define either
                  _XOPEN_SOURCE with the value 500 or greater, or
                  _POSIX_C_SOURCE with the value 200809L or greater.)

           F_GETOWN_EX
           F_SETOWN_EX
                  POSIX.1-2024.  Linux 2.6.32.

           F_GETSIG
           F_SETSIG
                  Linux.

## [](#BUGS)BUGS

       F_GETOWN
           A limitation of the Linux system call conventions on some
           architectures (notably i386) means that if a (negative) process
           group ID to be returned by F_GETOWN falls in the range -1 to
           -4095, then the return value is wrongly interpreted by glibc as an
           error in the system call; that is, the return value of fcntl()
           will be -1, and errno will contain the (positive) process group
           ID.  The Linux-specific F_GETOWN_EX operation avoids this problem.
           Since glibc 2.11, glibc makes the kernel F_GETOWN problem
           invisible by implementing F_GETOWN using F_GETOWN_EX.

       F_SETOWN
           In Linux 2.4 and earlier, there is bug that can occur when an
           unprivileged process uses F_SETOWN to specify the owner of a
           socket file descriptor as a process (group) other than the caller.
           In this case, fcntl() can return -1 with errno set to EPERM, even
           when the owner process (group) is one that the caller has
           permission to send signals to.  Despite this error return, the
           file descriptor owner is set, and signals will be sent to the
           owner.

## [](#SEE_ALSO)SEE ALSO

           fcntl(2)

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

    Linux man-pages 6.19            2025-12-31               F_GETSIG(2const)

------------------------------------------------------------------------

Pages that refer to this page: [fcntl(2)](../man2/fcntl.2.html),  [F_GETDELEG(2const)](../man2/F_GETDELEG.2const.html)

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
