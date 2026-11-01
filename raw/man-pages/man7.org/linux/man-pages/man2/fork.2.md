---
{"title": "fork(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/fork.2.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# fork(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    fork(2)                    System Calls Manual                    fork(2)

## [](#NAME)NAME

           fork - create a child process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           pid_t fork(void);

## [](#DESCRIPTION)DESCRIPTION

           fork() creates a new process by duplicating the calling process.
           The new process is referred to as the child process.  The calling
           process is referred to as the parent process.

           The child process and the parent process run in separate memory
           spaces.  At the time of fork() both memory spaces have the same
           content.  Memory writes, file mappings (mmap(2)), and unmappings
           (munmap(2)) performed by one of the processes do not affect the
           other.

           The child process is an exact duplicate of the parent process
           except for the following points:

           •  The child has its own unique process ID, and this PID does not
              match the ID of any existing process group (setpgid(2)) or
              session.

           •  The child's parent process ID is the same as the parent's
              process ID.

           •  The child does not inherit its parent's memory locks (mlock(2),
              mlockall(2)).

           •  Process resource utilizations (getrusage(2)) and CPU time
              counters (times(2)) are reset to zero in the child.

           •  The child's set of pending signals is initially empty
              (sigpending(2)).

           •  The child does not inherit semaphore adjustments from its
              parent (semop(2)).

           •  The child does not inherit process-associated record locks from
              its parent (fcntl(2)).  (On the other hand, it does inherit
              fcntl(2) open file description locks and flock(2) locks from
              its parent.)

           •  The child does not inherit timers from its parent
              (setitimer(2), alarm(2), timer_create(2)).

           •  The child does not inherit outstanding asynchronous I/O
              operations from its parent (aio_read(3), aio_write(3)), nor
              does it inherit any asynchronous I/O contexts from its parent
              (see io_setup(2)).

           The process attributes in the preceding list are all specified in
           POSIX.1.  The parent and child also differ with respect to the
           following Linux-specific process attributes:

           •  The child does not inherit directory change notifications
              (dnotify) from its parent (see the description of F_NOTIFY in
              fcntl(2)).

           •  The prctl(2) PR_SET_PDEATHSIG setting is reset so that the
              child does not receive a signal when its parent terminates.

           •  The default timer slack value is set to the parent's current
              timer slack value.  See the description of PR_SET_TIMERSLACK in
              prctl(2).

           •  Memory mappings that have been marked with the madvise(2)
              MADV_DONTFORK flag are not inherited across a fork().

           •  Memory in address ranges that have been marked with the
              madvise(2) MADV_WIPEONFORK flag is zeroed in the child after a
              fork().  (The MADV_WIPEONFORK setting remains in place for
              those address ranges in the child.)

           •  The termination signal of the child is always SIGCHLD (see
              clone(2)).

           •  The port access permission bits set by ioperm(2) are not
              inherited by the child; the child must turn on any bits that it
              requires using ioperm(2).

           Note the following further points:

           •  The child process is created with a single thread—the one that
              called fork().  The entire virtual address space of the parent
              is replicated in the child, including the states of mutexes,
              condition variables, and other pthreads objects; the use of
              pthread_atfork(3) may be helpful for dealing with problems that
              this can cause.

           •  After a fork() in a multithreaded program, the child can safely
              call only async-signal-safe functions (see signal-safety(7))
              until such time as it calls execve(2).

           •  The child inherits copies of the parent's set of open file
              descriptors.  Each file descriptor in the child refers to the
              same open file description (see open(2)) as the corresponding
              file descriptor in the parent.  This means that the two file
              descriptors share open file status flags, file offset, and
              signal-driven I/O attributes (see the description of F_SETOWN
              and F_SETSIG in fcntl(2)).

           •  The child inherits copies of the parent's set of open message
              queue descriptors (see mq_overview(7)).  Each file descriptor
              in the child refers to the same open message queue description
              as the corresponding file descriptor in the parent.  This means
              that the two file descriptors share the same flags (mq_flags).

           •  The child inherits copies of the parent's set of open directory
              streams (see opendir(3)).  POSIX.1 says that the corresponding
              directory streams in the parent and child may share the
              directory stream positioning; on Linux/glibc they do not.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the PID of the child process is returned in the
           parent, and 0 is returned in the child.  On failure, -1 is
           returned in the parent, no child process is created, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EAGAIN A system-imposed limit on the number of threads was
                  encountered.  There are a number of limits that may trigger
                  this error:

                  •  the RLIMIT_NPROC soft resource limit (set via
                     setrlimit(2)), which limits the number of processes and
                     threads for a real user ID, was reached;

                  •  the kernel's system-wide limit on the number of
                     processes and threads, /proc/sys/kernel/threads-max, was
                     reached (see proc(5));

                  •  the maximum number of PIDs, /proc/sys/kernel/pid_max,
                     was reached (see proc(5)); or

                  •  the PID limit (pids.max) imposed by the cgroup "process
                     number" (PIDs) controller was reached.

           EAGAIN The caller is operating under the SCHED_DEADLINE scheduling
                  policy and does not have the reset-on-fork flag set.  See
                  sched(7).

           ENOMEM fork() failed to allocate the necessary kernel structures
                  because memory is tight.

           ENOMEM An attempt was made to create a child process in a PID
                  namespace whose "init" process has terminated.  See
                  pid_namespaces(7).

           ENOSYS fork() is not supported on this platform (for example,
                  hardware without a Memory-Management Unit).

           ERESTARTNOINTR (since Linux 2.6.17)
                  System call was interrupted by a signal and will be
                  restarted.  (This can be seen only during a trace.)

## [](#VERSIONS)VERSIONS

       C library/kernel differences
           Since glibc 2.3.3, rather than invoking the kernel's fork() system
           call, the glibc fork() wrapper that is provided as part of the
           NPTL threading implementation invokes clone(2) with flags that
           provide the same effect as the traditional system call.  (A call
           to fork() is equivalent to a call to clone(2) specifying flags as
           just SIGCHLD.)  The glibc wrapper invokes any fork handlers that
           have been established using pthread_atfork(3).

       Async-signal safety
           _Fork(3) is an async-signal safe variant of fork(2).

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           4.3BSD, SVr4, POSIX.1-1988.

## [](#NOTES)NOTES

           Under Linux, fork() is implemented using copy-on-write pages, so
           the only penalty that it incurs is the time and memory required to
           duplicate the parent's page tables, and to create a unique task
           structure for the child.

## [](#EXAMPLES)EXAMPLES

           See pipe(2) and wait(2) for more examples.

           #include <signal.h>
           #include <stdint.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <sys/types.h>
           #include <unistd.h>

           int
           main(void)
           {
               pid_t pid;

               if (signal(SIGCHLD, SIG_IGN) == SIG_ERR) {
                   perror("signal");
                   exit(EXIT_FAILURE);
               }
               pid = fork();
               switch (pid) {
               case -1:
                   perror("fork");
                   exit(EXIT_FAILURE);
               case 0:
                   puts("Child exiting.");
                   fflush(stdout);
                   _exit(EXIT_SUCCESS);
               default:
                   printf("Child is PID %jd\n", (intmax_t) pid);
                   puts("Parent exiting.");
                   exit(EXIT_SUCCESS);
               }
           }

## [](#SEE_ALSO)SEE ALSO

           clone(2), execve(2), exit(2), _exit(3), setrlimit(2), unshare(2),
           vfork(2), wait(2), daemon(3), _Fork(3), pthread_atfork(3),
           capabilities(7), credentials(7)

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

    Linux man-pages 6.19            2026-06-05                        fork(2)

------------------------------------------------------------------------

Pages that refer to this page: [chrt(1)](../man1/chrt.1.html),  [dbpmda(1)](../man1/dbpmda.1.html),  [pmcd(1)](../man1/pmcd.1.html),  [setsid(1)](../man1/setsid.1.html),  [strace(1)](../man1/strace.1.html),  [xargs(1)](../man1/xargs.1.html),  [alarm(2)](../man2/alarm.2.html),  [arch_prctl(2)](../man2/arch_prctl.2.html),  [bpf(2)](../man2/bpf.2.html),  [chdir(2)](../man2/chdir.2.html),  [chroot(2)](../man2/chroot.2.html),  [clone(2)](../man2/clone.2.html),  [eventfd(2)](../man2/eventfd.2.html),  [execve(2)](../man2/execve.2.html),  [fcntl_locking(2)](../man2/fcntl_locking.2.html),  [F_GETDELEG(2const)](../man2/F_GETDELEG.2const.html),  [F_GETFD(2const)](../man2/F_GETFD.2const.html),  [F_GETFL(2const)](../man2/F_GETFL.2const.html),  [F_GETLEASE(2const)](../man2/F_GETLEASE.2const.html),  [flock(2)](../man2/flock.2.html),  [fork(2)](../man2/fork.2.html),  [getitimer(2)](../man2/getitimer.2.html),  [getpid(2)](../man2/getpid.2.html),  [getpriority(2)](../man2/getpriority.2.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [gettid(2)](../man2/gettid.2.html),  [ioperm(2)](../man2/ioperm.2.html),  [iopl(2)](../man2/iopl.2.html),  [kcmp(2)](../man2/kcmp.2.html),  [KEYCTL_SET_REQKEY_KEYRING(2const)](../man2/KEYCTL_SET_REQKEY_KEYRING.2const.html),  [lseek(2)](../man2/lseek.2.html),  [madvise(2)](../man2/madvise.2.html),  [memfd_create(2)](../man2/memfd_create.2.html),  [memfd_secret(2)](../man2/memfd_secret.2.html),  [mlock(2)](../man2/mlock.2.html),  [mmap(2)](../man2/mmap.2.html),  [mount(2)](../man2/mount.2.html),  [nice(2)](../man2/nice.2.html),  [open(2)](../man2/open.2.html),  [perf_event_open(2)](../man2/perf_event_open.2.html),  [pidfd_open(2)](../man2/pidfd_open.2.html),  [pipe(2)](../man2/pipe.2.html),  [PR_MPX_ENABLE_MANAGEMENT(2const)](../man2/PR_MPX_ENABLE_MANAGEMENT.2const.html),  [PR_SET_CHILD_SUBREAPER(2const)](../man2/PR_SET_CHILD_SUBREAPER.2const.html),  [PR_SET_IO_FLUSHER(2const)](../man2/PR_SET_IO_FLUSHER.2const.html),  [PR_SET_MDWE(2const)](../man2/PR_SET_MDWE.2const.html),  [PR_SET_NO_NEW_PRIVS(2const)](../man2/PR_SET_NO_NEW_PRIVS.2const.html),  [PR_SET_PDEATHSIG(2const)](../man2/PR_SET_PDEATHSIG.2const.html),  [PR_SET_SYSCALL_USER_DISPATCH(2const)](../man2/PR_SET_SYSCALL_USER_DISPATCH.2const.html),  [PR_SET_TAGGED_ADDR_CTRL(2const)](../man2/PR_SET_TAGGED_ADDR_CTRL.2const.html),  [PR_SET_THP_DISABLE(2const)](../man2/PR_SET_THP_DISABLE.2const.html),  [PR_SET_TIMERSLACK(2const)](../man2/PR_SET_TIMERSLACK.2const.html),  [PR_SVE_SET_VL(2const)](../man2/PR_SVE_SET_VL.2const.html),  [ptrace(2)](../man2/ptrace.2.html),  [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [sched_setattr(2)](../man2/sched_setattr.2.html),  [sched_setscheduler(2)](../man2/sched_setscheduler.2.html),  [seccomp(2)](../man2/seccomp.2.html),  [select_tut(2)](../man2/select_tut.2.html),  [semop(2)](../man2/semop.2.html),  [set_mempolicy(2)](../man2/set_mempolicy.2.html),  [setns(2)](../man2/setns.2.html),  [setpgid(2)](../man2/setpgid.2.html),  [setsid(2)](../man2/setsid.2.html),  [shmop(2)](../man2/shmop.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [sigaltstack(2)](../man2/sigaltstack.2.html),  [signalfd(2)](../man2/signalfd.2.html),  [sigpending(2)](../man2/sigpending.2.html),  [sigprocmask(2)](../man2/sigprocmask.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [timer_create(2)](../man2/timer_create.2.html),  [timerfd_create(2)](../man2/timerfd_create.2.html),  [UFFDIO_API(2const)](../man2/UFFDIO_API.2const.html),  [UFFDIO_MOVE(2const)](../man2/UFFDIO_MOVE.2const.html),  [umask(2)](../man2/umask.2.html),  [unshare(2)](../man2/unshare.2.html),  [userfaultfd(2)](../man2/userfaultfd.2.html),  [vfork(2)](../man2/vfork.2.html),  [wait(2)](../man2/wait.2.html),  [wait4(2)](../man2/wait4.2.html),  [atexit(3)](../man3/atexit.3.html),  [cap_launch(3)](../man3/cap_launch.3.html),  [daemon(3)](../man3/daemon.3.html),  [exec(3)](../man3/exec.3.html),  [\_exit(3)](../man3/_exit.3.html),  [\_Fork(3)](../man3/_Fork.3.html),  [ibv_fork_init(3)](../man3/ibv_fork_init.3.html),  [ibv_is_fork_initialized(3)](../man3/ibv_is_fork_initialized.3.html),  [id_t(3type)](../man3/id_t.3type.html),  [io_uring_register_bpf_filter(3)](../man3/io_uring_register_bpf_filter.3.html),  [io_uring_register_bpf_filter_task(3)](../man3/io_uring_register_bpf_filter_task.3.html),  [io_uring_ring_dontfork(3)](../man3/io_uring_ring_dontfork.3.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [on_exit(3)](../man3/on_exit.3.html),  [openpty(3)](../man3/openpty.3.html),  [pam_end(3)](../man3/pam_end.3.html),  [pam_set_data(3)](../man3/pam_set_data.3.html),  [\_\_pmprocessexec(3)](../man3/__pmprocessexec.3.html),  [\_\_pmprocesspipe(3)](../man3/__pmprocesspipe.3.html),  [popen(3)](../man3/popen.3.html),  [posix_spawn(3)](../man3/posix_spawn.3.html),  [pthread_atfork(3)](../man3/pthread_atfork.3.html),  [sd_bus_creds_get_pid(3)](../man3/sd_bus_creds_get_pid.3.html),  [sd_varlink_connect_address(3)](../man3/sd_varlink_connect_address.3.html),  [sem_init(3)](../man3/sem_init.3.html),  [system(3)](../man3/system.3.html),  [core(5)](../man5/core.5.html),  [proc_pid_oom_score(5)](../man5/proc_pid_oom_score.5.html),  [proc_sys_kernel(5)](../man5/proc_sys_kernel.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [cgroups(7)](../man7/cgroups.7.html),  [cpuset(7)](../man7/cpuset.7.html),  [credentials(7)](../man7/credentials.7.html),  [environ(7)](../man7/environ.7.html),  [epoll(7)](../man7/epoll.7.html),  [mq_overview(7)](../man7/mq_overview.7.html),  [persistent-keyring(7)](../man7/persistent-keyring.7.html),  [pid_namespaces(7)](../man7/pid_namespaces.7.html),  [pipe(7)](../man7/pipe.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [sched(7)](../man7/sched.7.html),  [session-keyring(7)](../man7/session-keyring.7.html),  [signal(7)](../man7/signal.7.html),  [thread-keyring(7)](../man7/thread-keyring.7.html),  [user-keyring(7)](../man7/user-keyring.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [user-session-keyring(7)](../man7/user-session-keyring.7.html),  [btrfs-balance(8)](../man8/btrfs-balance.8.html),  [lslocks(8)](../man8/lslocks.8.html),  [lttng-sessiond(8)](../man8/lttng-sessiond.8.html),  [trafgen(8)](../man8/trafgen.8.html)

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
