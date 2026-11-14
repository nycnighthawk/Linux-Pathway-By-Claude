---
{"title": "prctl(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/prctl.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# prctl(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    prctl(2)                   System Calls Manual                   prctl(2)

## [](#NAME)NAME

           prctl - operations on a process or thread

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(int op, ...);

## [](#DESCRIPTION)DESCRIPTION

           prctl() manipulates various aspects of the behavior of the calling
           thread or process.

           prctl() is called with a first argument describing what to do, and
           further arguments with a significance depending on the first one.
           The first argument can be:

           PR_CAP_AMBIENT
           PR_CAPBSET_READ
           PR_CAPBSET_DROP
           PR_SET_CHILD_SUBREAPER
           PR_GET_CHILD_SUBREAPER
           PR_SET_DUMPABLE
           PR_GET_DUMPABLE
           PR_SET_ENDIAN
           PR_GET_ENDIAN
           PR_SET_FP_MODE
           PR_GET_FP_MODE
           PR_SET_FPEMU
           PR_GET_FPEMU
           PR_SET_FPEXC
           PR_GET_FPEXC
           PR_SET_IO_FLUSHER
           PR_GET_IO_FLUSHER
           PR_SET_KEEPCAPS
           PR_GET_KEEPCAPS
           PR_MCE_KILL
           PR_MCE_KILL_GET
           PR_SET_MM
           PR_SET_VMA
           PR_MPX_ENABLE_MANAGEMENT
           PR_MPX_DISABLE_MANAGEMENT
           PR_SET_NAME
           PR_GET_NAME
           PR_SET_NO_NEW_PRIVS
           PR_GET_NO_NEW_PRIVS
           PR_PAC_RESET_KEYS
           PR_SET_PDEATHSIG
           PR_GET_PDEATHSIG
           PR_SET_PTRACER
           PR_SET_SECCOMP
           PR_GET_SECCOMP
           PR_SET_SECUREBITS
           PR_GET_SECUREBITS
           PR_GET_SPECULATION_CTRL
           PR_SET_SPECULATION_CTRL
           PR_SVE_SET_VL
           PR_SVE_GET_VL
           PR_SET_SYSCALL_USER_DISPATCH
           PR_SET_TAGGED_ADDR_CTRL
           PR_GET_TAGGED_ADDR_CTRL
           PR_TASK_PERF_EVENTS_DISABLE
           PR_TASK_PERF_EVENTS_ENABLE
           PR_SET_THP_DISABLE
           PR_GET_THP_DISABLE
           PR_GET_TID_ADDRESS
           PR_SET_TIMERSLACK
           PR_GET_TIMERSLACK
           PR_SET_TIMING
           PR_GET_TIMING
           PR_SET_TSC
           PR_GET_TSC
           PR_SET_UNALIGN
           PR_GET_UNALIGN
           PR_GET_AUXV
           PR_SET_MDWE
           PR_GET_MDWE
           PR_RISCV_SET_ICACHE_FLUSH_CTX
           PR_FUTEX_HASH

## [](#RETURN_VALUE)RETURN VALUE

           On success, a nonnegative value is returned.  On error, -1 is
           returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL The value of op is not recognized, or not supported on this
                  system.

           EINVAL An unused argument is nonzero.

## [](#VERSIONS)VERSIONS

           IRIX has a prctl() system call (also introduced in Linux 2.1.44 as
           irix_prctl on the MIPS architecture), with prototype

               ptrdiff_t prctl(int op, int arg2, int arg3);

           and operations to get the maximum number of processes per user,
           get the maximum number of processors the calling process can use,
           find out whether a specified process is currently blocked, get or
           set the maximum stack size, and so on.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.1.57, glibc 2.0.6

## [](#CAVEATS)CAVEATS

           The prototype of the libc wrapper uses a variadic argument list.
           This makes it necessary to pass the arguments with the right
           width.  When passing numeric constants, such as 0, use a suffix:
           0L.

           Careless use of some prctl() operations can confuse the user-space
           run-time environment, so these operations should be used with
           care.

## [](#SEE_ALSO)SEE ALSO

           signal(2), PR_CAP_AMBIENT(2const), PR_CAPBSET_READ(2const),
           PR_CAPBSET_DROP(2const), PR_SET_CHILD_SUBREAPER(2const),
           PR_GET_CHILD_SUBREAPER(2const), PR_SET_DUMPABLE(2const),
           PR_GET_DUMPABLE(2const), PR_SET_ENDIAN(2const),
           PR_GET_ENDIAN(2const), PR_SET_FP_MODE(2const),
           PR_GET_FP_MODE(2const), PR_SET_FPEMU(2const),
           PR_GET_FPEMU(2const), PR_SET_FPEXC(2const), PR_GET_FPEXC(2const),
           PR_SET_IO_FLUSHER(2const), PR_GET_IO_FLUSHER(2const),
           PR_SET_KEEPCAPS(2const), PR_GET_KEEPCAPS(2const),
           PR_MCE_KILL(2const), PR_MCE_KILL_GET(2const), PR_SET_MM(2const),
           PR_SET_VMA(2const), PR_MPX_ENABLE_MANAGEMENT(2const),
           PR_MPX_DISABLE_MANAGEMENT(2const), PR_SET_NAME(2const),
           PR_GET_NAME(2const), PR_SET_NO_NEW_PRIVS(2const),
           PR_GET_NO_NEW_PRIVS(2const), PR_PAC_RESET_KEYS(2const),
           PR_SET_PDEATHSIG(2const), PR_GET_PDEATHSIG(2const),
           PR_SET_PTRACER(2const), PR_SET_SECCOMP(2const),
           PR_GET_SECCOMP(2const), PR_SET_SECUREBITS(2const),
           PR_GET_SECUREBITS(2const), PR_SET_SPECULATION_CTRL(2const),
           PR_GET_SPECULATION_CTRL(2const), PR_SVE_SET_VL(2const),
           PR_SVE_GET_VL(2const), PR_SET_SYSCALL_USER_DISPATCH(2const),
           PR_SET_TAGGED_ADDR_CTRL(2const), PR_GET_TAGGED_ADDR_CTRL(2const),
           PR_TASK_PERF_EVENTS_DISABLE(2const),
           PR_TASK_PERF_EVENTS_ENABLE(2const), PR_SET_THP_DISABLE(2const),
           PR_GET_THP_DISABLE(2const), PR_GET_TID_ADDRESS(2const),
           PR_SET_TIMERSLACK(2const), PR_GET_TIMERSLACK(2const),
           PR_SET_TIMING(2const), PR_GET_TIMING(2const), PR_SET_TSC(2const),
           PR_GET_TSC(2const), PR_SET_UNALIGN(2const),
           PR_GET_UNALIGN(2const), PR_GET_AUXV(2const), PR_SET_MDWE(2const),
           PR_GET_MDWE(2const), PR_RISCV_SET_ICACHE_FLUSH_CTX(2const),
           PR_FUTEX_HASH(2const), core(5)

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

    Linux man-pages 6.19            2026-02-08                       prctl(2)

------------------------------------------------------------------------

Pages that refer to this page: [capsh(1)](../man1/capsh.1.html),  [setpriv(1)](../man1/setpriv.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [arch_prctl(2)](../man2/arch_prctl.2.html),  [execve(2)](../man2/execve.2.html),  [fork(2)](../man2/fork.2.html),  [getpid(2)](../man2/getpid.2.html),  [madvise(2)](../man2/madvise.2.html),  [perf_event_open(2)](../man2/perf_event_open.2.html),  [PR_CAP_AMBIENT(2const)](../man2/PR_CAP_AMBIENT.2const.html),  [PR_CAP_AMBIENT_CLEAR_ALL(2const)](../man2/PR_CAP_AMBIENT_CLEAR_ALL.2const.html),  [PR_CAP_AMBIENT_IS_SET(2const)](../man2/PR_CAP_AMBIENT_IS_SET.2const.html),  [PR_CAP_AMBIENT_LOWER(2const)](../man2/PR_CAP_AMBIENT_LOWER.2const.html),  [PR_CAP_AMBIENT_RAISE(2const)](../man2/PR_CAP_AMBIENT_RAISE.2const.html),  [PR_CAPBSET_DROP(2const)](../man2/PR_CAPBSET_DROP.2const.html),  [PR_CAPBSET_READ(2const)](../man2/PR_CAPBSET_READ.2const.html),  [PR_FUTEX_HASH(2const)](../man2/PR_FUTEX_HASH.2const.html),  [PR_FUTEX_HASH_GET_SLOTS(2const)](../man2/PR_FUTEX_HASH_GET_SLOTS.2const.html),  [PR_FUTEX_HASH_SET_SLOTS(2const)](../man2/PR_FUTEX_HASH_SET_SLOTS.2const.html),  [PR_GET_AUXV(2const)](../man2/PR_GET_AUXV.2const.html),  [PR_GET_CHILD_SUBREAPER(2const)](../man2/PR_GET_CHILD_SUBREAPER.2const.html),  [PR_GET_DUMPABLE(2const)](../man2/PR_GET_DUMPABLE.2const.html),  [PR_GET_ENDIAN(2const)](../man2/PR_GET_ENDIAN.2const.html),  [PR_GET_FPEMU(2const)](../man2/PR_GET_FPEMU.2const.html),  [PR_GET_FPEXC(2const)](../man2/PR_GET_FPEXC.2const.html),  [PR_GET_FP_MODE(2const)](../man2/PR_GET_FP_MODE.2const.html),  [PR_GET_IO_FLUSHER(2const)](../man2/PR_GET_IO_FLUSHER.2const.html),  [PR_GET_MDWE(2const)](../man2/PR_GET_MDWE.2const.html),  [PR_GET_NO_NEW_PRIVS(2const)](../man2/PR_GET_NO_NEW_PRIVS.2const.html),  [PR_GET_SECCOMP(2const)](../man2/PR_GET_SECCOMP.2const.html),  [PR_GET_SECUREBITS(2const)](../man2/PR_GET_SECUREBITS.2const.html),  [PR_GET_SPECULATION_CTRL(2const)](../man2/PR_GET_SPECULATION_CTRL.2const.html),  [PR_GET_TAGGED_ADDR_CTRL(2const)](../man2/PR_GET_TAGGED_ADDR_CTRL.2const.html),  [PR_GET_THP_DISABLE(2const)](../man2/PR_GET_THP_DISABLE.2const.html),  [PR_GET_TID_ADDRESS(2const)](../man2/PR_GET_TID_ADDRESS.2const.html),  [PR_GET_TIMING(2const)](../man2/PR_GET_TIMING.2const.html),  [PR_GET_TSC(2const)](../man2/PR_GET_TSC.2const.html),  [PR_GET_UNALIGN(2const)](../man2/PR_GET_UNALIGN.2const.html),  [PR_MCE_KILL(2const)](../man2/PR_MCE_KILL.2const.html),  [PR_MCE_KILL_CLEAR(2const)](../man2/PR_MCE_KILL_CLEAR.2const.html),  [PR_MCE_KILL_GET(2const)](../man2/PR_MCE_KILL_GET.2const.html),  [PR_MCE_KILL_SET(2const)](../man2/PR_MCE_KILL_SET.2const.html),  [PR_MPX_ENABLE_MANAGEMENT(2const)](../man2/PR_MPX_ENABLE_MANAGEMENT.2const.html),  [PR_PAC_RESET_KEYS(2const)](../man2/PR_PAC_RESET_KEYS.2const.html),  [PR_RISCV_SET_ICACHE_FLUSH_CTX(2const)](../man2/PR_RISCV_SET_ICACHE_FLUSH_CTX.2const.html),  [PR_SET_CHILD_SUBREAPER(2const)](../man2/PR_SET_CHILD_SUBREAPER.2const.html),  [PR_SET_DUMPABLE(2const)](../man2/PR_SET_DUMPABLE.2const.html),  [PR_SET_ENDIAN(2const)](../man2/PR_SET_ENDIAN.2const.html),  [PR_SET_FPEMU(2const)](../man2/PR_SET_FPEMU.2const.html),  [PR_SET_FPEXC(2const)](../man2/PR_SET_FPEXC.2const.html),  [PR_SET_FP_MODE(2const)](../man2/PR_SET_FP_MODE.2const.html),  [PR_SET_IO_FLUSHER(2const)](../man2/PR_SET_IO_FLUSHER.2const.html),  [PR_SET_KEEPCAPS(2const)](../man2/PR_SET_KEEPCAPS.2const.html),  [PR_SET_MDWE(2const)](../man2/PR_SET_MDWE.2const.html),  [PR_SET_MM(2const)](../man2/PR_SET_MM.2const.html),  [PR_SET_MM_ARG_START(2const)](../man2/PR_SET_MM_ARG_START.2const.html),  [PR_SET_MM_AUXV(2const)](../man2/PR_SET_MM_AUXV.2const.html),  [PR_SET_MM_BRK(2const)](../man2/PR_SET_MM_BRK.2const.html),  [PR_SET_MM_EXE_FILE(2const)](../man2/PR_SET_MM_EXE_FILE.2const.html),  [PR_SET_MM_MAP(2const)](../man2/PR_SET_MM_MAP.2const.html),  [PR_SET_MM_START_BRK(2const)](../man2/PR_SET_MM_START_BRK.2const.html),  [PR_SET_MM_START_CODE(2const)](../man2/PR_SET_MM_START_CODE.2const.html),  [PR_SET_MM_START_DATA(2const)](../man2/PR_SET_MM_START_DATA.2const.html),  [PR_SET_MM_START_STACK(2const)](../man2/PR_SET_MM_START_STACK.2const.html),  [PR_SET_NAME(2const)](../man2/PR_SET_NAME.2const.html),  [PR_SET_NO_NEW_PRIVS(2const)](../man2/PR_SET_NO_NEW_PRIVS.2const.html),  [PR_SET_PDEATHSIG(2const)](../man2/PR_SET_PDEATHSIG.2const.html),  [PR_SET_PTRACER(2const)](../man2/PR_SET_PTRACER.2const.html),  [PR_SET_SECCOMP(2const)](../man2/PR_SET_SECCOMP.2const.html),  [PR_SET_SECUREBITS(2const)](../man2/PR_SET_SECUREBITS.2const.html),  [PR_SET_SPECULATION_CTRL(2const)](../man2/PR_SET_SPECULATION_CTRL.2const.html),  [PR_SET_SYSCALL_USER_DISPATCH(2const)](../man2/PR_SET_SYSCALL_USER_DISPATCH.2const.html),  [PR_SET_TAGGED_ADDR_CTRL(2const)](../man2/PR_SET_TAGGED_ADDR_CTRL.2const.html),  [PR_SET_THP_DISABLE(2const)](../man2/PR_SET_THP_DISABLE.2const.html),  [PR_SET_TIMERSLACK(2const)](../man2/PR_SET_TIMERSLACK.2const.html),  [PR_SET_TIMING(2const)](../man2/PR_SET_TIMING.2const.html),  [PR_SET_TSC(2const)](../man2/PR_SET_TSC.2const.html),  [PR_SET_UNALIGN(2const)](../man2/PR_SET_UNALIGN.2const.html),  [PR_SET_VMA(2const)](../man2/PR_SET_VMA.2const.html),  [PR_SVE_GET_VL(2const)](../man2/PR_SVE_GET_VL.2const.html),  [PR_SVE_SET_VL(2const)](../man2/PR_SVE_SET_VL.2const.html),  [PR_TASK_PERF_EVENTS_DISABLE(2const)](../man2/PR_TASK_PERF_EVENTS_DISABLE.2const.html),  [ptrace(2)](../man2/ptrace.2.html),  [seccomp(2)](../man2/seccomp.2.html),  [seccomp_unotify(2)](../man2/seccomp_unotify.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [wait(2)](../man2/wait.2.html),  [capng_change_id(3)](../man3/capng_change_id.3.html),  [capng_lock(3)](../man3/capng_lock.3.html),  [exit(3)](../man3/exit.3.html),  [\_exit(3)](../man3/_exit.3.html),  [io_uring_register_bpf_filter(3)](../man3/io_uring_register_bpf_filter.3.html),  [io_uring_register_bpf_filter_task(3)](../man3/io_uring_register_bpf_filter_task.3.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [pthread_setname_np(3)](../man3/pthread_setname_np.3.html),  [sd_event_add_time(3)](../man3/sd_event_add_time.3.html),  [core(5)](../man5/core.5.html),  [proc_pid(5)](../man5/proc_pid.5.html),  [proc_pid_cmdline(5)](../man5/proc_pid_cmdline.5.html),  [proc_pid_comm(5)](../man5/proc_pid_comm.5.html),  [proc_pid_environ(5)](../man5/proc_pid_environ.5.html),  [proc_pid_maps(5)](../man5/proc_pid_maps.5.html),  [proc_pid_seccomp(5)](../man5/proc_pid_seccomp.5.html),  [proc_pid_status(5)](../man5/proc_pid_status.5.html),  [proc_pid_timerslack_ns(5)](../man5/proc_pid_timerslack_ns.5.html),  [proc_sys_fs(5)](../man5/proc_sys_fs.5.html),  [proc_sys_vm(5)](../man5/proc_sys_vm.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd-system.conf(5)](../man5/systemd-system.conf.5.html),  [systemd.timer(5)](../man5/systemd.timer.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [credentials(7)](../man7/credentials.7.html),  [environ(7)](../man7/environ.7.html),  [pid_namespaces(7)](../man7/pid_namespaces.7.html),  [time(7)](../man7/time.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [mount.fuse3(8)](../man8/mount.fuse3.8.html),  [systemd-coredump(8)](../man8/systemd-coredump.8.html)

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
