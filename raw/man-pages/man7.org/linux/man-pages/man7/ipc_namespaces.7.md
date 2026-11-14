---
{"title": "ipc_namespaces(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/ipc_namespaces.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ipc_namespaces(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    ipc_namespaces(7)    Miscellaneous Information Manual   ipc_namespaces(7)

## [](#NAME)NAME

           ipc_namespaces - overview of Linux IPC namespaces

## [](#DESCRIPTION)DESCRIPTION

           IPC namespaces isolate certain IPC resources, namely, System V IPC
           objects (see sysvipc(7)) and (since Linux 2.6.30) POSIX message
           queues (see mq_overview(7)).  The common characteristic of these
           IPC mechanisms is that IPC objects are identified by mechanisms
           other than filesystem pathnames.

           Each IPC namespace has its own set of System V IPC identifiers and
           its own POSIX message queue filesystem.  Objects created in an IPC
           namespace are visible to all other processes that are members of
           that namespace, but are not visible to processes in other IPC
           namespaces.

           The following /proc interfaces are distinct in each IPC namespace:

           •  The POSIX message queue interfaces in /proc/sys/fs/mqueue.

           •  The System V IPC interfaces in /proc/sys/kernel, namely:
              msgmax, msgmnb, msgmni, sem, shmall, shmmax, shmmni, and
              shm_rmid_forced.

           •  The System V IPC interfaces in /proc/sysvipc.

           When an IPC namespace is destroyed (i.e., when the last process
           that is a member of the namespace terminates), all IPC objects in
           the namespace are automatically destroyed.

           Use of IPC namespaces requires a kernel that is configured with
           the CONFIG_IPC_NS option.

## [](#SEE_ALSO)SEE ALSO

           nsenter(1), unshare(1), clone(2), setns(2), unshare(2),
           mq_overview(7), namespaces(7), sysvipc(7)

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

    Linux man-pages 6.19            2026-02-08              ipc_namespaces(7)

------------------------------------------------------------------------

Pages that refer to this page: [getino(1)](../man1/getino.1.html),  [nsenter(1)](../man1/nsenter.1.html),  [unshare(1)](../man1/unshare.1.html),  [clone(2)](../man2/clone.2.html),  [lttng-ust(3)](../man3/lttng-ust.3.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [mq_overview(7)](../man7/mq_overview.7.html),  [namespaces(7)](../man7/namespaces.7.html),  [sysvipc(7)](../man7/sysvipc.7.html)

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
