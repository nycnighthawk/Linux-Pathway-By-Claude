---
{"title": "proc(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    proc(5)                    File Formats Manual                    proc(5)

## [](#NAME)NAME

           proc - process information, system information, and sysctl pseudo-
           filesystem

## [](#DESCRIPTION)DESCRIPTION

           The proc filesystem is a pseudo-filesystem which provides an
           interface to kernel data structures.  It is commonly mounted at
           /proc.  Typically, it is mounted automatically by the system, but
           it can also be mounted manually using a command such as:

               mount -t proc proc /proc

           Most of the files in the proc filesystem are read-only, but some
           files are writable, allowing kernel variables to be changed.

       Mount options
           The proc filesystem supports the following mount options:

           hidepid=n (since Linux 3.3)
                  This option controls who can access the information in
                  /proc/pid directories.  The argument, n, is one of the
                  following values:

                  0   Everybody may access all /proc/pid directories.  This
                      is the traditional behavior, and the default if this
                      mount option is not specified.

                  1   Users may not access files and subdirectories inside
                      any /proc/pid directories but their own (the /proc/pid
                      directories themselves remain visible).  Sensitive
                      files such as /proc/pid/cmdline and /proc/pid/status
                      are now protected against other users.  This makes it
                      impossible to learn whether any user is running a
                      specific program (so long as the program doesn't
                      otherwise reveal itself by its behavior).

                  2   As for mode 1, but in addition the /proc/pid
                      directories belonging to other users become invisible.
                      This means that /proc/pid entries can no longer be used
                      to discover the PIDs on the system.  This doesn't hide
                      the fact that a process with a specific PID value
                      exists (it can be learned by other means, for example,
                      by "kill -0 $PID"), but it hides a process's UID and
                      GID, which could otherwise be learned by employing
                      stat(2) on a /proc/pid directory.  This greatly
                      complicates an attacker's task of gathering information
                      about running processes (e.g., discovering whether some
                      daemon is running with elevated privileges, whether
                      another user is running some sensitive program, whether
                      other users are running any program at all, and so on).

                  gid=gid (since Linux 3.3)
                      Specifies the ID of a group whose members are
                      authorized to learn process information otherwise
                      prohibited by hidepid (i.e., users in this group behave
                      as though /proc was mounted with hidepid=0).  This
                      group should be used instead of approaches such as
                      putting nonroot users into the sudoers(5) file.

           subset=pid (since Linux 5.8)
                  Show only the specified subset of procfs, hiding all top
                  level files and directories in the procfs that are not
                  related to tasks.

       Overview
           Underneath /proc, there are the following general groups of files
           and subdirectories:

           /proc/pid subdirectories
                  See proc_pid(5).

                  Each one of these subdirectories contains files and
                  subdirectories exposing information about the process with
                  the corresponding process ID.

                  Underneath each of the /proc/pid directories, a task
                  subdirectory contains subdirectories of the form task/tid,
                  which contain corresponding information about each of the
                  threads in the process, where tid is the kernel thread ID
                  of the thread.

                  The /proc/pid subdirectories are visible when iterating
                  through /proc with getdents(2) (and thus are visible when
                  one uses ls(1) to view the contents of /proc).

           /proc/tid subdirectories
                  See proc_tid(5).

                  Each one of these subdirectories contains files and
                  subdirectories exposing information about the thread with
                  the corresponding thread ID.  The contents of these
                  directories are the same as the corresponding
                  /proc/pid/task/tid directories.

                  The /proc/tid subdirectories are not visible when iterating
                  through /proc with getdents(2) (and thus are not visible
                  when one uses ls(1) to view the contents of /proc).

           /proc/self
                  See proc_self(5).

                  When a process accesses this magic symbolic link, it
                  resolves to the process's own /proc/pid directory.

           /proc/thread-self
                  See proc_thread-self(5).

                  When a thread accesses this magic symbolic link, it
                  resolves to the process's own /proc/self/task/tid
                  directory.

           /proc/[a-z]*

                  Various other files and subdirectories under /proc expose
                  system-wide information.

                  See also:

                  proc_apm(5)
                  proc_buddyinfo(5)
                  proc_bus(5)
                  proc_cgroups(5)
                  proc_cmdline(5)
                  proc_config.gz(5)
                  proc_cpuinfo(5)
                  proc_crypto(5)
                  proc_devices(5)
                  proc_diskstats(5)
                  proc_dma(5)
                  proc_driver(5)
                  proc_execdomains(5)
                  proc_fb(5)
                  proc_filesystems(5)
                  proc_fs(5)
                  proc_ide(5)
                  proc_interrupts(5)
                  proc_iomem(5)
                  proc_ioports(5)
                  proc_kallsyms(5)
                  proc_kcore(5)
                  proc_key-users(5)
                  proc_keys(5)
                  proc_kmsg(5)
                  proc_kpagecgroup(5)
                  proc_kpagecount(5)
                  proc_kpageflags(5)
                  proc_ksyms(5)
                  proc_loadavg(5)
                  proc_locks(5)
                  proc_malloc(5)
                  proc_meminfo(5)
                  proc_modules(5)
                  proc_mounts(5)
                  proc_mtrr(5)
                  proc_net(5)
                  proc_partitions(5)
                  proc_pci(5)
                  proc_profile(5)
                  proc_scsi(5)
                  proc_slabinfo(5)
                  proc_stat(5)
                  proc_swaps(5)
                  proc_sys(5)
                  proc_sysrq-trigger(5)
                  proc_sysvipc(5)
                  proc_timer_list(5)
                  proc_timer_stats(5)
                  proc_tty(5)
                  proc_uptime(5)
                  proc_version(5)
                  proc_vmstat(5)
                  proc_zoneinfo(5)

## [](#NOTES)NOTES

           Many files contain strings (e.g., the environment and command
           line) that are in the internal format, with subfields terminated
           by null bytes ('\0').  When inspecting such files, you may find
           that the results are more readable if you use a command of the
           following form to display them:

               $ cat file | tr '\000' '\n'

## [](#SEE_ALSO)SEE ALSO

           cat(1), dmesg(1), find(1), free(1), htop(1), init(1), ps(1),
           pstree(1), tr(1), uptime(1), chroot(2), mmap(2), readlink(2),
           syslog(2), slabinfo(5), sysfs(5), hier(7), namespaces(7), time(7),
           arp(8), hdparm(8), ifconfig(8), lsmod(8), lspci(8), mount(8),
           netstat(8), procinfo(8), route(8), sysctl(8)

           The Linux kernel source files: Documentation/filesystems/proc.rst,
           Documentation/admin-guide/sysctl/fs.rst,
           Documentation/admin-guide/sysctl/kernel.rst,
           Documentation/admin-guide/sysctl/net.rst, and
           Documentation/admin-guide/sysctl/vm.rst.

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

    Linux man-pages 6.19            2026-02-08                        proc(5)

------------------------------------------------------------------------

Pages that refer to this page: [choom(1)](../man1/choom.1.html),  [htop(1)](../man1/htop.1.html),  [kill(1)](../man1/kill.1.html),  [lsfd(1)](../man1/lsfd.1.html),  [ps(1)](../man1/ps.1.html),  [pstree(1)](../man1/pstree.1.html),  [strace(1)](../man1/strace.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [unshare(1)](../man1/unshare.1.html),  [chroot(2)](../man2/chroot.2.html),  [close_range(2)](../man2/close_range.2.html),  [delete_module(2)](../man2/delete_module.2.html),  [eventfd(2)](../man2/eventfd.2.html),  [execve(2)](../man2/execve.2.html),  [fork(2)](../man2/fork.2.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [init_module(2)](../man2/init_module.2.html),  [ioctl_nsfs(2)](../man2/ioctl_nsfs.2.html),  [kcmp(2)](../man2/kcmp.2.html),  [mlock(2)](../man2/mlock.2.html),  [mmap(2)](../man2/mmap.2.html),  [mount(2)](../man2/mount.2.html),  [mount_setattr(2)](../man2/mount_setattr.2.html),  [msgctl(2)](../man2/msgctl.2.html),  [open(2)](../man2/open.2.html),  [openat2(2)](../man2/openat2.2.html),  [pidfd_open(2)](../man2/pidfd_open.2.html),  [posix_fadvise(2)](../man2/posix_fadvise.2.html),  [seccomp(2)](../man2/seccomp.2.html),  [seccomp_unotify(2)](../man2/seccomp_unotify.2.html),  [semctl(2)](../man2/semctl.2.html),  [shmctl(2)](../man2/shmctl.2.html),  [signalfd(2)](../man2/signalfd.2.html),  [statx(2)](../man2/statx.2.html),  [symlink(2)](../man2/symlink.2.html),  [sysctl(2)](../man2/sysctl.2.html),  [sysfs(2)](../man2/sysfs.2.html),  [sysinfo(2)](../man2/sysinfo.2.html),  [timer_create(2)](../man2/timer_create.2.html),  [vfork(2)](../man2/vfork.2.html),  [errno(3)](../man3/errno.3.html),  [fexecve(3)](../man3/fexecve.3.html),  [getauxval(3)](../man3/getauxval.3.html),  [getloadavg(3)](../man3/getloadavg.3.html),  [malloc(3)](../man3/malloc.3.html),  [mallopt(3)](../man3/mallopt.3.html),  [procps(3)](../man3/procps.3.html),  [procps_misc(3)](../man3/procps_misc.3.html),  [procps_pids(3)](../man3/procps_pids.3.html),  [program_invocation_name(3)](../man3/program_invocation_name.3.html),  [pthread_create(3)](../man3/pthread_create.3.html),  [sd_bus_creds_get_pid(3)](../man3/sd_bus_creds_get_pid.3.html),  [acct(5)](../man5/acct.5.html),  [core(5)](../man5/core.5.html),  [filesystems(5)](../man5/filesystems.5.html),  [proc_apm(5)](../man5/proc_apm.5.html),  [proc_buddyinfo(5)](../man5/proc_buddyinfo.5.html),  [proc_bus(5)](../man5/proc_bus.5.html),  [proc_cgroups(5)](../man5/proc_cgroups.5.html),  [proc_cmdline(5)](../man5/proc_cmdline.5.html),  [proc_config.gz(5)](../man5/proc_config.gz.5.html),  [proc_cpuinfo(5)](../man5/proc_cpuinfo.5.html),  [proc_crypto(5)](../man5/proc_crypto.5.html),  [proc_devices(5)](../man5/proc_devices.5.html),  [proc_diskstats(5)](../man5/proc_diskstats.5.html),  [proc_dma(5)](../man5/proc_dma.5.html),  [proc_driver(5)](../man5/proc_driver.5.html),  [proc_execdomains(5)](../man5/proc_execdomains.5.html),  [proc_fb(5)](../man5/proc_fb.5.html),  [proc_filesystems(5)](../man5/proc_filesystems.5.html),  [proc_fs(5)](../man5/proc_fs.5.html),  [proc_ide(5)](../man5/proc_ide.5.html),  [proc_interrupts(5)](../man5/proc_interrupts.5.html),  [proc_iomem(5)](../man5/proc_iomem.5.html),  [proc_ioports(5)](../man5/proc_ioports.5.html),  [proc_kallsyms(5)](../man5/proc_kallsyms.5.html),  [proc_kcore(5)](../man5/proc_kcore.5.html),  [proc_keys(5)](../man5/proc_keys.5.html),  [proc_kmsg(5)](../man5/proc_kmsg.5.html),  [proc_kpagecgroup(5)](../man5/proc_kpagecgroup.5.html),  [proc_kpagecount(5)](../man5/proc_kpagecount.5.html),  [proc_kpageflags(5)](../man5/proc_kpageflags.5.html),  [proc_loadavg(5)](../man5/proc_loadavg.5.html),  [proc_locks(5)](../man5/proc_locks.5.html),  [proc_malloc(5)](../man5/proc_malloc.5.html),  [proc_meminfo(5)](../man5/proc_meminfo.5.html),  [proc_modules(5)](../man5/proc_modules.5.html),  [proc_mtrr(5)](../man5/proc_mtrr.5.html),  [proc_partitions(5)](../man5/proc_partitions.5.html),  [proc_pci(5)](../man5/proc_pci.5.html),  [proc_pid(5)](../man5/proc_pid.5.html),  [proc_pid_attr(5)](../man5/proc_pid_attr.5.html),  [proc_pid_autogroup(5)](../man5/proc_pid_autogroup.5.html),  [proc_pid_auxv(5)](../man5/proc_pid_auxv.5.html),  [proc_pid_cgroup(5)](../man5/proc_pid_cgroup.5.html),  [proc_pid_clear_refs(5)](../man5/proc_pid_clear_refs.5.html),  [proc_pid_cmdline(5)](../man5/proc_pid_cmdline.5.html),  [proc_pid_comm(5)](../man5/proc_pid_comm.5.html),  [proc_pid_coredump_filter(5)](../man5/proc_pid_coredump_filter.5.html),  [proc_pid_cpuset(5)](../man5/proc_pid_cpuset.5.html),  [proc_pid_cwd(5)](../man5/proc_pid_cwd.5.html),  [proc_pid_environ(5)](../man5/proc_pid_environ.5.html),  [proc_pid_exe(5)](../man5/proc_pid_exe.5.html),  [proc_pid_fd(5)](../man5/proc_pid_fd.5.html),  [proc_pid_fdinfo(5)](../man5/proc_pid_fdinfo.5.html),  [proc_pid_io(5)](../man5/proc_pid_io.5.html),  [proc_pid_limits(5)](../man5/proc_pid_limits.5.html),  [proc_pid_map_files(5)](../man5/proc_pid_map_files.5.html),  [proc_pid_maps(5)](../man5/proc_pid_maps.5.html),  [proc_pid_mem(5)](../man5/proc_pid_mem.5.html),  [proc_pid_mountinfo(5)](../man5/proc_pid_mountinfo.5.html),  [proc_pid_mounts(5)](../man5/proc_pid_mounts.5.html),  [proc_pid_mountstats(5)](../man5/proc_pid_mountstats.5.html),  [proc_pid_net(5)](../man5/proc_pid_net.5.html),  [proc_pid_ns(5)](../man5/proc_pid_ns.5.html),  [proc_pid_numa_maps(5)](../man5/proc_pid_numa_maps.5.html),  [proc_pid_oom_score(5)](../man5/proc_pid_oom_score.5.html),  [proc_pid_oom_score_adj(5)](../man5/proc_pid_oom_score_adj.5.html),  [proc_pid_pagemap(5)](../man5/proc_pid_pagemap.5.html),  [proc_pid_personality(5)](../man5/proc_pid_personality.5.html),  [proc_pid_projid_map(5)](../man5/proc_pid_projid_map.5.html),  [proc_pid_root(5)](../man5/proc_pid_root.5.html),  [proc_pid_seccomp(5)](../man5/proc_pid_seccomp.5.html),  [proc_pid_setgroups(5)](../man5/proc_pid_setgroups.5.html),  [proc_pid_smaps(5)](../man5/proc_pid_smaps.5.html),  [proc_pid_stack(5)](../man5/proc_pid_stack.5.html),  [proc_pid_stat(5)](../man5/proc_pid_stat.5.html),  [proc_pid_statm(5)](../man5/proc_pid_statm.5.html),  [proc_pid_status(5)](../man5/proc_pid_status.5.html),  [proc_pid_syscall(5)](../man5/proc_pid_syscall.5.html),  [proc_pid_task(5)](../man5/proc_pid_task.5.html),  [proc_pid_timers(5)](../man5/proc_pid_timers.5.html),  [proc_pid_timerslack_ns(5)](../man5/proc_pid_timerslack_ns.5.html),  [proc_pid_uid_map(5)](../man5/proc_pid_uid_map.5.html),  [proc_pid_wchan(5)](../man5/proc_pid_wchan.5.html),  [proc_profile(5)](../man5/proc_profile.5.html),  [proc_scsi(5)](../man5/proc_scsi.5.html),  [proc_slabinfo(5)](../man5/proc_slabinfo.5.html),  [proc_stat(5)](../man5/proc_stat.5.html),  [proc_swaps(5)](../man5/proc_swaps.5.html),  [proc_sys(5)](../man5/proc_sys.5.html),  [proc_sys_abi(5)](../man5/proc_sys_abi.5.html),  [proc_sys_debug(5)](../man5/proc_sys_debug.5.html),  [proc_sys_dev(5)](../man5/proc_sys_dev.5.html),  [proc_sys_fs(5)](../man5/proc_sys_fs.5.html),  [proc_sys_kernel(5)](../man5/proc_sys_kernel.5.html),  [proc_sys_net(5)](../man5/proc_sys_net.5.html),  [proc_sys_net_ipv4(5)](../man5/proc_sys_net_ipv4.5.html),  [proc_sys_proc(5)](../man5/proc_sys_proc.5.html),  [proc_sysrq-trigger(5)](../man5/proc_sysrq-trigger.5.html),  [proc_sys_sunrpc(5)](../man5/proc_sys_sunrpc.5.html),  [proc_sys_user(5)](../man5/proc_sys_user.5.html),  [proc_sysvipc(5)](../man5/proc_sysvipc.5.html),  [proc_sys_vm(5)](../man5/proc_sys_vm.5.html),  [proc_tid_children(5)](../man5/proc_tid_children.5.html),  [proc_timer_list(5)](../man5/proc_timer_list.5.html),  [proc_timer_stats(5)](../man5/proc_timer_stats.5.html),  [proc_tty(5)](../man5/proc_tty.5.html),  [proc_uptime(5)](../man5/proc_uptime.5.html),  [proc_version(5)](../man5/proc_version.5.html),  [proc_vmstat(5)](../man5/proc_vmstat.5.html),  [proc_zoneinfo(5)](../man5/proc_zoneinfo.5.html),  [sysfs(5)](../man5/sysfs.5.html),  [systemd.mount(5)](../man5/systemd.mount.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [cgroup_namespaces(7)](../man7/cgroup_namespaces.7.html),  [cpuset(7)](../man7/cpuset.7.html),  [credentials(7)](../man7/credentials.7.html),  [epoll(7)](../man7/epoll.7.html),  [fanotify(7)](../man7/fanotify.7.html),  [hier(7)](../man7/hier.7.html),  [inotify(7)](../man7/inotify.7.html),  [libc(7)](../man7/libc.7.html),  [mount_namespaces(7)](../man7/mount_namespaces.7.html),  [namespaces(7)](../man7/namespaces.7.html),  [netdevice(7)](../man7/netdevice.7.html),  [network_namespaces(7)](../man7/network_namespaces.7.html),  [pid_namespaces(7)](../man7/pid_namespaces.7.html),  [pkeys(7)](../man7/pkeys.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [pty(7)](../man7/pty.7.html),  [signal(7)](../man7/signal.7.html),  [symlink(7)](../man7/symlink.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [vdso(7)](../man7/vdso.7.html),  [migratepages(8)](../man8/migratepages.8.html),  [netstat(8)](../man8/netstat.8.html),  [numactl(8)](../man8/numactl.8.html),  [sysctl(8)](../man8/sysctl.8.html),  [systemd-coredump(8)](../man8/systemd-coredump.8.html)

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
