---
{"title": "lxc-unshare(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lxc-unshare.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-unshare(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-unshare(1)                                             lxc-unshare(1)

## [](#NAME)NAME

           lxc-unshare - Run a task in a new set of namespaces.

## [](#SYNOPSIS)SYNOPSIS

           lxc-unshare {-s, --namespaces namespaces} [-u, --user user] [-H,
                       --hostname hostname] [-i, --ifname ifname] [-d,
                       --daemon] [-M, --remount] {command}

## [](#DESCRIPTION)DESCRIPTION

           lxc-unshare  can  be  used  to run a task in a cloned set of name‐
           spaces. This command is mainly provided for testing purposes.  De‐
           spite its name, it always uses clone rather than unshare to create
           the new task with fresh namespaces. Apart from testing kernel  re‐
           gressions this should make no difference.

## [](#OPTIONS)OPTIONS

           -s, --namespaces namespaces
                  Specify the namespaces to attach to, as a pipe-separated
                  list, e.g. NETWORK|IPC. Allowed values are MOUNT, PID, UT‐
                  SNAME, IPC, USER and NETWORK. This allows one to change the
                  context of the process to e.g. the network namespace of the
                  container while retaining the other namespaces as those of
                  the host. (The pipe symbol needs to be escaped, e.g.
                  MOUNT\|PID or quoted, e.g.  "MOUNT|PID".)

           -u, --user user
                  Specify a userid which the new task should become.

           -H, --hostname hostname
                  Set the hostname in the new container. Only allowed if the
                  UTSNAME namespace is set.

           -i, --ifname interfacename
                  Move the named interface into the container. Only allowed
                  if the NETWORK namespace is set. You may specify this argu‐
                  ment multiple times to move multiple interfaces into con‐
                  tainer.

           -d, --daemon
                  Daemonize (do not wait for the container to exit before ex‐
                  iting)

           -M, --remount
                  Mount default filesystems (/proc /dev/shm and /dev/mqueue)
                  in the container. Only allowed if MOUNT namespace is set.

## [](#EXAMPLES)EXAMPLES

           To spawn a new shell with its own UTS (hostname) namespace,

                     lxc-unshare -s UTSNAME /bin/bash

           If the hostname is changed in that shell, the change will not be
           reflected on the host.

           To spawn a shell in a new network, pid, and mount namespace,

                     lxc-unshare -s "NETWORK|PID|MOUNT" /bin/bash

           The resulting shell will have pid 1 and will see no network inter‐
           faces.  After re-mounting /proc in that shell,

                     mount -t proc proc /proc

           ps output will show there are no other processes in the namespace.

           To spawn a shell in a new network, pid, mount, and hostname name‐
           space.

                     lxc-unshare -s "NETWORK|PID|MOUNT|UTSNAME" -M -H myhostname -i veth1 /bin/bash

           The resulting shell will have pid 1 and will see two network in‐
           terfaces (lo and veth1). The hostname will be "myhostname" and
           /proc will have been remounted. ps output will show there are no
           other processes in the namespace.

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

                                    2026-04-29                 lxc-unshare(1)

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
