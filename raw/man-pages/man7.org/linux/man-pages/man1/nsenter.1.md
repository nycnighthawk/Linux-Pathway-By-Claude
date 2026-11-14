---
{"title": "nsenter(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/nsenter.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nsenter(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NSENTER(1)                    User Commands                    NSENTER(1)

## [](#NAME)NAME

           nsenter - run program in different namespaces

## [](#SYNOPSIS)SYNOPSIS

           nsenter [options] [program [arguments]]

## [](#DESCRIPTION)DESCRIPTION

           The nsenter command executes program in the namespace(s) that are
           specified in the command-line options (described below). If
           program is not given, then "${SHELL}" is run. If SHELL is not set,
           the shell from the user’s passwd(5) entry is used. If no shell is
           defined there either, /bin/sh is used as the fallback.

           Enterable namespaces are:

           mount namespace
               Mounting and unmounting filesystems will not affect the rest
               of the system, except for filesystems which are explicitly
               marked as shared (with mount --make-shared; see
               /proc/self/mountinfo for the shared flag). For further
               details, see mount_namespaces(7) and the discussion of the
               CLONE_NEWNS flag in clone(2).

           UTS namespace
               Setting hostname or domainname will not affect the rest of the
               system. For further details, see uts_namespaces(7).

           IPC namespace
               The process will have an independent namespace for POSIX
               message queues as well as System V message queues, semaphore
               sets and shared memory segments. For further details, see
               ipc_namespaces(7).

           network namespace
               The process will have independent IPv4 and IPv6 stacks, IP
               routing tables, firewall rules, the /proc/net and
               /sys/class/net directory trees, sockets, etc. For further
               details, see network_namespaces(7).

           PID namespace
               Children will have a set of PID to process mappings separate
               from the nsenter process. nsenter will fork by default if
               changing the PID namespace, so that the new program and its
               children share the same PID namespace and are visible to each
               other. If --no-fork is used, the new program will be exec’ed
               without forking. For further details, see pid_namespaces(7).

           user namespace
               The process will have a distinct set of UIDs, GIDs and
               capabilities. For further details, see user_namespaces(7).

           cgroup namespace
               The process will have a virtualized view of /proc/self/cgroup,
               and new cgroup mounts will be rooted at the namespace cgroup
               root. For further details, see cgroup_namespaces(7).

           time namespace
               The process can have a distinct view of CLOCK_MONOTONIC and/or
               CLOCK_BOOTTIME which can be changed using
               /proc/self/timens_offsets. For further details, see
               time_namespaces(7).

           If you want to create a new namespace, use unshare(1). Once
           created, you can run a program in it using nsenter.

## [](#OPTIONS)OPTIONS

           Various of the options below that relate to namespaces take an
           optional file argument. This should be one of the /proc/[pid]/ns/*
           files described in namespaces(7), or the pathname of a bind mount
           that was created on one of those files.

           -a, --all
               Enter all namespaces of the target process by the default
               /proc/<pid>/ns/* namespace paths. The default paths to the
               target process namespaces may be overridden by
               namespace-specific options (e.g., --all --mount=path).

               The user namespace will be ignored if it is the same as the
               caller’s current user namespace. It prevents a caller that has
               dropped capabilities from regaining those capabilities via a
               call to setns(2). See the man page for more details.

           -t, --target PID[:inode]
               Specify a target process to get contexts from. The paths to
               the contexts specified by PID are:

                  /proc/pid/ns/mnt
                      the mount namespace

                  /proc/pid/ns/uts
                      the UTS namespace

                  /proc/pid/ns/ipc
                      the IPC namespace

                  /proc/pid/ns/net
                      the network namespace

                  /proc/pid/ns/pid
                      the PID namespace

                  /proc/pid/ns/user
                      the user namespace

                  /proc/pid/ns/cgroup
                      the cgroup namespace

                  /proc/pid/ns/time
                      the time namespace

                  /proc/pid/root
                      the root directory

                  /proc/pid/cwd
                      the working directory respectively

               Optionally, a process can be addressed with the format
               PID:inode. The inode identifies the unique process’s file
               descriptor. To retrieve a process’s inode number you can use
               the getino(1) utility.

           -m, --mount[=file|=:nsid]
               Enter the mount namespace. If no argument is specified, enter
               the mount namespace of the target process. If file or :nsid is
               specified, enter the mount namespace specified by file or
               nsid.

           -u, --uts[=file|=:nsid]
               Enter the UTS namespace. If no argument is specified, enter
               the UTS namespace of the target process. If file or :nsid is
               specified, enter the UTS namespace specified by file or nsid.

           -i, --ipc[=file|=:nsid]
               Enter the IPC namespace. If no argument is specified, enter
               the IPC namespace of the target process. If file or :nsid is
               specified, enter the IPC namespace specified by file or nsid.

           -n, --net[=file|=:nsid]
               Enter the network namespace. If no argument is specified,
               enter the network namespace of the target process. If file or
               :nsid is specified, enter the network namespace specified by
               file or nsid.

           -N, --net-socket fd
               Enter the network namespace of the target process’s socket. It
               requires --target process specified. Supported since Linux
               5.6.

           -p, --pid[=file|=:nsid]
               Enter the PID namespace. If no argument is specified, enter
               the PID namespace of the target process. If file or :nsid is
               specified, enter the PID namespace specified by file or nsid.

           -U, --user[=file|=:nsid]
               Enter the user namespace. If no argument is specified, enter
               the user namespace of the target process. If file or :nsid is
               specified, enter the user namespace specified by file or nsid.
               See also the --setuid and --setgid options.

           --user-parent
               Enter the parent user namespace. Parent user namespace will be
               acquired from any other enabled namespace. If combined with
               --user option the parent user namespace will be fetched from
               the user namespace and replace it.

           -C, --cgroup[=file|=:nsid]
               Enter the cgroup namespace. If no argument is specified, enter
               the cgroup namespace of the target process. If file or :nsid
               is specified, enter the cgroup namespace specified by file or
               nsid.

           -T, --time[=file|=:nsid]
               Enter the time namespace. If no argument is specified, enter
               the time namespace of the target process. If file or :nsid is
               specified, enter the time namespace specified by file or nsid.

           -G, --setgid gid
               Set the group ID which will be used in the entered namespace
               and drop supplementary groups. nsenter always sets GID for
               user namespaces, the default is 0. If the argument "follow" is
               specified the GID of the target process is used.

           -S, --setuid uid
               Set the user ID which will be used in the entered namespace.
               nsenter always sets UID for user namespaces, the default is 0.
               If the argument "follow" is specified the UID of the target
               process is used.

           --keep-caps
               When the --user option is given, ensure that capabilities
               granted in the user namespace are preserved in the child
               process.

           --preserve-credentials
               Don’t modify UID and GID when entering the user namespace. The
               default is to drop supplementary groups and set GID and UID to
               0.

           -r, --root[=directory]
               Set the root directory. If no directory is specified, set the
               root directory to the root directory of the target process. If
               directory is specified, set the root directory to the
               specified directory. The specified directory is opened before
               switching to the requested namespaces.

           -w, --wd[=directory]
               Set the working directory. If no directory is specified, set
               the working directory to the working directory of the target
               process. If directory is specified, set the working directory
               to the specified directory. The specified directory is opened
               before switching to the requested namespaces, which means the
               specified directory works as a "tunnel" to the current
               namespace. See also --wdns.

           -W, --wdns[=directory]
               Set the working directory. The directory is opened after
               switching to the requested namespaces and after calling
               chroot(2). The options --wd and --wdns are mutually exclusive.

           -e, --env
               Pass environment variables from the target process to the new
               process being created. If this option is not provided, the
               environment variables will remain the same as in the current
               namespace.

           -F, --no-fork
               Do not fork before exec’ing the specified program. By default,
               when entering a PID namespace, nsenter calls fork before
               calling exec so that any children will also be in the newly
               entered PID namespace.

           -Z, --follow-context
               Set the SELinux security context used for executing a new
               process according to the already running process specified by
               --target PID. (The util-linux has to be compiled with SELinux
               support otherwise the option is unavailable.)

           -c, --join-cgroup
               Add the initiated process to the cgroup of the target process.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           SHELL
               The default shell to run when no program is specified. If
               SHELL is not set, the shell from the user’s passwd(5) entry is
               used. If no shell is defined there either, /bin/sh is used as
               the fallback.

## [](#NOTES)NOTES

           The --user-parent option requires Linux 4.9 or higher, older
           kernels will raise inappropriate ioctl for device error.

           Specifying namespaces by nsid requires Linux 6.19 or higher. If a
           namespace file name starts with a colon, prepend ./ for
           disambiguation.

## [](#AUTHORS)AUTHORS

           Eric Biederman <biederm@xmission.com>, Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           unshare(1), lsns(8), clone(2), setns(2), namespaces(7) getino(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The nsenter command is part of the util-linux package which can be
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                     NSENTER(1)

------------------------------------------------------------------------

Pages that refer to this page: [unshare(1)](../man1/unshare.1.html),  [setns(2)](../man2/setns.2.html),  [ipc_namespaces(7)](../man7/ipc_namespaces.7.html),  [mount_namespaces(7)](../man7/mount_namespaces.7.html),  [namespaces(7)](../man7/namespaces.7.html),  [network_namespaces(7)](../man7/network_namespaces.7.html),  [time_namespaces(7)](../man7/time_namespaces.7.html),  [uts_namespaces(7)](../man7/uts_namespaces.7.html),  [lsns(8)](../man8/lsns.8.html)

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
