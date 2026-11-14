---
{"title": "lxc-attach(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lxc-attach.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-attach(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMON OPTIONS](#COMMON_OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [COMPATIBILITY](#COMPATIBILITY) \| [NOTES](#NOTES) \| [SECURITY](#SECURITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-attach(1)                                               lxc-attach(1)

## [](#NAME)NAME

           lxc-attach - start a process inside a running container.

## [](#SYNOPSIS)SYNOPSIS

           lxc-attach {-n, --name name} [-f, --rcfile config_file] [-a,
                      --arch arch] [-e, --elevated-privileges privileges]
                      [-s, --namespaces namespaces] [-R, --remount-sys-proc]
                      [--keep-env] [--clear-env] [-v, --set-var variable]
                      [--keep-var variable] [-u, --uid uid] [-g, --gid gid]
                      [-- command]

## [](#DESCRIPTION)DESCRIPTION

           lxc-attach  runs the specified command inside the container speci‐
           fied by name. The container has to be running already.

           If no command is specified, the current default shell of the  user
           running lxc-attach will be looked up inside the container and exe‐
           cuted.  This will fail if no such user exists inside the container
           or the container does not have a working nsswitch mechanism.

           Previous versions of lxc-attach simply attached to  the  specified
           namespaces of a container and ran a shell or the specified command
           without first allocating a pseudo terminal. This made them vulner‐
           able  to input faking via a TIOCSTI ioctl call after switching be‐
           tween userspace execution contexts with different  privilege  lev‐
           els.  Newer  versions  of lxc-attach will try to allocate a pseudo
           terminal file descriptor pair on the host and attach any  standard
           file  descriptors  which refer to a terminal to the container side
           of the pseudo terminal before executing a shell or command.  Note,
           that  if none of the standard file descriptors refer to a terminal
           lxc-attach will not try to allocate a pseudo terminal. Instead  it
           will simply attach to the containers namespaces and run a shell or
           the specified command.

## [](#OPTIONS)OPTIONS

           -f, --rcfile config_file
                  Specify the configuration file to configure the virtualiza‐
                  tion and isolation functionalities for the container.

                  This configuration file if present will be used even if
                  there is already a configuration file present in the previ‐
                  ously created container (via lxc-create).

           -a, --arch arch
                  Specify the architecture which the kernel should appear to
                  be running as to the command executed. This option will ac‐
                  cept the same settings as the lxc.arch option in container
                  configuration files, see lxc.conf(5). By default, the cur‐
                  rent architecture of the running container will be used.

           -e, --elevated-privileges privileges
                  Do not drop privileges when running command inside the con‐
                  tainer. If this option is specified, the new process will
                  not be added to the container's cgroup(s) and it will not
                  drop its capabilities before executing.

                  You may specify privileges, in case you do not want to ele‐
                  vate all of them, as a pipe-separated list, e.g.
                  CGROUP|LSM. Allowed values are CGROUP, CAP and LSM repre‐
                  senting cgroup, capabilities and restriction privileges re‐
                  spectively. (The pipe symbol needs to be escaped, e.g.
                  CGROUP\|LSM or quoted, e.g.  "CGROUP|LSM".)

                  Warning: This may leak privileges into the container if the
                  command starts subprocesses that remain active after the
                  main process that was attached is terminated. The
                  (re-)starting of daemons inside the container is problemat‐
                  ic, especially if the daemon starts a lot of subprocesses
                  such as cron or sshd.  Use with great care.

           -s, --namespaces namespaces
                  Specify the namespaces to attach to, as a pipe-separated
                  list, e.g. NETWORK|IPC. Allowed values are MOUNT, PID, UT‐
                  SNAME, IPC, USER and NETWORK. This allows one to change the
                  context of the process to e.g. the network namespace of the
                  container while retaining the other namespaces as those of
                  the host. (The pipe symbol needs to be escaped, e.g.
                  MOUNT\|PID or quoted, e.g.  "MOUNT|PID".)

                  Important: This option implies -e.

           -R, --remount-sys-proc
                  When using -s and the mount namespace is not included, this
                  flag will cause lxc-attach to remount /proc and /sys to re‐
                  flect the current other namespace contexts.

                  Please see the Notes section for more details.

                  This option will be ignored if one tries to attach to the
                  mount namespace anyway.

           --keep-env
                  Keep the current environment for attached programs. This is
                  the current default behaviour (as of version 0.9), but is
                  is likely to change in the future, since this may leak un‐
                  desirable information into the container. If you rely on
                  the environment being available for the attached program,
                  please use this option to be future-proof. In addition to
                  current environment variables, container=lxc will be set.

           --clear-env
                  Clear the environment before attaching, so no undesired en‐
                  vironment variables leak into the container. The variable
                  container=lxc will be the only environment with which the
                  attached program starts.

           -v, --set-var variable
                  Set an additional environment variable that is seen by the
                  attached program in the container. It is specified in the
                  form of "VAR=VALUE", and can be specified multiple times.

           --keep-var variable
                  Keep a specified environment variable. It can only be spec‐
                  ified in conjunction with --clear-env, and can be specified
                  multiple times.

           -u, --uid uid
                  Executes the command with user ID (use numerical value) uid
                  inside the container.

           --g, --gid gid
                  Executes the command with group ID (use numerical value)
                  gid inside the container.

## [](#COMMON_OPTIONS)COMMON OPTIONS

           These options are common to most of lxc commands.

           -?, -h, --help
                  Print a longer usage message than normal.

           --usage
                  Give the usage message

           -q, --quiet
                  mute on

           -P, --lxcpath=PATH
                  Use an alternate container path. The default is
                  /var/lib/lxc.

           -o, --logfile=FILE
                  Output to an alternate log FILE. The default is no log.

           -l, --logpriority=LEVEL
                  Set log priority to LEVEL. The default log priority is ER‐
                  ROR. Possible values are : FATAL, ALERT, CRIT, WARN, ERROR,
                  NOTICE, INFO, DEBUG, TRACE.

                  Note that this option is setting the priority of the events
                  log in the alternate log file. It do not have effect on the
                  ERROR events log on stderr.

           -n, --name=NAME
                  Use container identifier NAME.  The container identifier
                  format is an alphanumeric string.

           --rcfile=FILE
                  Specify the configuration file to configure the virtualiza‐
                  tion and isolation functionalities for the container.

                  This configuration file if present will be used even if
                  there is already a configuration file present in the previ‐
                  ously created container (via lxc-create).

           --version
                  Show the version number.

## [](#EXAMPLES)EXAMPLES

           To spawn a new shell running inside an existing container, use

                     lxc-attach -n container

           To restart the cron service of a running Debian container, use

                     lxc-attach -n container -- /etc/init.d/cron restart

           To deactivate the network link eth1 of a running container that
           does not have the NET_ADMIN capability, use either the -e option
           to use increased capabilities, assuming the ip tool is installed:

                     lxc-attach -n container -e -- /sbin/ip link delete eth1

           Or, alternatively, use the -s to use the tools installed on the
           host outside the container:

                     lxc-attach -n container -s NETWORK -- /sbin/ip link delete eth1

## [](#COMPATIBILITY)COMPATIBILITY

           Attaching completely (including the pid and mount namespaces) to a
           container requires a kernel of version 3.8 or higher, or a patched
           kernel, please see the lxc website for details. lxc-attach will
           fail in that case if used with an unpatched kernel of version 3.7
           and prior.

           Nevertheless, it will succeed on an unpatched kernel of version
           3.0 or higher if the -s option is used to restrict the namespaces
           that the process is to be attached to to one or more of NETWORK,
           IPC and UTSNAME.

           Attaching to user namespaces is supported by kernel 3.8 or higher
           with enabling user namespace.

## [](#NOTES)NOTES

           The Linux /proc and /sys filesystems contain information about
           some quantities that are affected by namespaces, such as the di‐
           rectories named after process ids in /proc or the network inter‐
           face information in /sys/class/net. The namespace of the process
           mounting the pseudo-filesystems determines what information is
           shown, not the namespace of the process accessing /proc or /sys.

           If one uses the -s option to only attach to the pid namespace of a
           container, but not its mount namespace (which will contain the
           /proc of the container and not the host), the contents of /proc
           will reflect that of the host and not the container. Analogously,
           the same issue occurs when reading the contents of /sys/class/net
           and attaching to just the network namespace.

           To work around this problem, the -R flag provides the option to
           remount /proc and /sys in order for them to reflect the net‐
           work/pid namespace context of the attached process. In order not
           to interfere with the host's actual filesystem, the mount name‐
           space will be unshared (like lxc-unshare does) before this is
           done, essentially giving the process a new mount namespace, which
           is identical to the hosts's mount namespace except for the /proc
           and /sys filesystems.

           Previous versions of lxc-attach suffered a bug whereby a user
           could attach to a containers namespace without being placed in a
           writeable cgroup for some critical subsystems. Newer versions of
           lxc-attach will check whether a user is in a writeable cgroup for
           those critical subsystems. lxc-attach might thus fail unexpectedly
           for some users (E.g. on systems where an unprivileged user is not
           placed in a writeable cgroup in critical subsystems on login.).
           However, this behavior is correct and more secure.

## [](#SECURITY)SECURITY

           The -e and -s options should be used with care, as it may break
           the isolation of the containers if used improperly.

## [](#SEE_ALSO)SEE ALSO

           lxc(7), lxc-create(1), lxc-copy(1), lxc-destroy(1), lxc-start(1),
           lxc-stop(1), lxc-execute(1), lxc-console(1), lxc-monitor(1),
           lxc-wait(1), lxc-cgroup(1), lxc-ls(1), lxc-info(1), lxc-freeze(1),
           lxc-unfreeze(1), lxc-attach(1), lxc.conf(5)

## [](#COLOPHON)COLOPHON

           This page is part of the lxc (Linux containers) project.  Informa‐
           tion about the project can be found at 
           ⟨http://linuxcontainers.org/⟩.  If you have a bug report for this
           manual page, send it to lxc-devel@lists.linuxcontainers.org.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/lxc/lxc.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-23.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2026-04-29                  lxc-attach(1)

------------------------------------------------------------------------

Pages that refer to this page: [lxc-attach(1)](../man1/lxc-attach.1.html),  [lxc-autostart(1)](../man1/lxc-autostart.1.html),  [lxc-cgroup(1)](../man1/lxc-cgroup.1.html),  [lxc-checkconfig(1)](../man1/lxc-checkconfig.1.html),  [lxc-checkpoint(1)](../man1/lxc-checkpoint.1.html),  [lxc-config(1)](../man1/lxc-config.1.html),  [lxc-console(1)](../man1/lxc-console.1.html),  [lxc-copy(1)](../man1/lxc-copy.1.html),  [lxc-create(1)](../man1/lxc-create.1.html),  [lxc-destroy(1)](../man1/lxc-destroy.1.html),  [lxc-device(1)](../man1/lxc-device.1.html),  [lxc-execute(1)](../man1/lxc-execute.1.html),  [lxc-freeze(1)](../man1/lxc-freeze.1.html),  [lxc-info(1)](../man1/lxc-info.1.html),  [lxc-ls(1)](../man1/lxc-ls.1.html),  [lxc-monitor(1)](../man1/lxc-monitor.1.html),  [lxc-snapshot(1)](../man1/lxc-snapshot.1.html),  [lxc-start(1)](../man1/lxc-start.1.html),  [lxc-stop(1)](../man1/lxc-stop.1.html),  [lxc-top(1)](../man1/lxc-top.1.html),  [lxc-unfreeze(1)](../man1/lxc-unfreeze.1.html),  [lxc-unshare(1)](../man1/lxc-unshare.1.html),  [lxc-update-config(1)](../man1/lxc-update-config.1.html),  [lxc-usernsexec(1)](../man1/lxc-usernsexec.1.html),  [lxc-wait(1)](../man1/lxc-wait.1.html),  [lxc.container.conf(5)](../man5/lxc.container.conf.5.html),  [lxc.system.conf(5)](../man5/lxc.system.conf.5.html),  [lxc(7)](../man7/lxc.7.html)

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
