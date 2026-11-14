---
{"title": "proc_sys(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_sys.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_sys(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_sys(5)                File Formats Manual                proc_sys(5)

## [](#NAME)NAME

           /proc/sys/ - system information, and sysctl pseudo-filesystem

## [](#DESCRIPTION)DESCRIPTION

           /proc/sys/
                  This directory (present since Linux 1.3.57) contains a
                  number of files and subdirectories corresponding to kernel
                  variables.  These variables can be read and in some cases
                  modified using the /proc filesystem, and the (deprecated)
                  sysctl(2) system call.

                  String values may be terminated by either '\0' or '\n'.

                  Integer and long values may be written either in decimal or
                  in hexadecimal notation (e.g., 0x3FFF).  When writing
                  multiple integer or long values, these may be separated by
                  any of the following whitespace characters: ' ', '\t', or
                  '\n'.  Using other separators leads to the error EINVAL.

                  See also:

                  proc_sys_abi(5)
                  proc_sys_debug(5)
                  proc_sys_dev(5)
                  proc_sys_fs(5)
                  proc_sys_kernel(5)
                  proc_sys_net(5)
                  proc_sys_net_ipv4(5)
                  proc_sys_proc(5)
                  proc_sys_sunrpc(5)
                  proc_sys_user(5)
                  proc_sys_vm(5)

## [](#SEE_ALSO)SEE ALSO

           proc(5)

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

    Linux man-pages 6.19            2026-02-08                    proc_sys(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc(5)](../man5/proc.5.html),  [proc_sys_abi(5)](../man5/proc_sys_abi.5.html),  [proc_sys_debug(5)](../man5/proc_sys_debug.5.html),  [proc_sys_dev(5)](../man5/proc_sys_dev.5.html),  [proc_sys_fs(5)](../man5/proc_sys_fs.5.html),  [proc_sys_kernel(5)](../man5/proc_sys_kernel.5.html),  [proc_sys_proc(5)](../man5/proc_sys_proc.5.html),  [proc_sys_sunrpc(5)](../man5/proc_sys_sunrpc.5.html),  [proc_sys_user(5)](../man5/proc_sys_user.5.html),  [proc_sys_vm(5)](../man5/proc_sys_vm.5.html)

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
