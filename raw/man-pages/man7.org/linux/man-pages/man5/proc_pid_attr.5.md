---
{"title": "proc_pid_attr(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/proc_pid_attr.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# proc_pid_attr(5) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    proc_pid_attr(5)           File Formats Manual           proc_pid_attr(5)

## [](#NAME)NAME

           /proc/pid/attr/ - security-related attributes

## [](#DESCRIPTION)DESCRIPTION

           /proc/pid/attr/
                  The files in this directory provide an API for security
                  modules.  The contents of this directory are files that can
                  be read and written in order to set security-related
                  attributes.  This directory was added to support SELinux,
                  but the intention was that the API be general enough to
                  support other security modules.  For the purpose of
                  explanation, examples of how SELinux uses these files are
                  provided below.

                  This directory is present only if the kernel was configured
                  with CONFIG_SECURITY.

           /proc/pid/attr/current (since Linux 2.6.0)
                  The contents of this file represent the current security
                  attributes of the process.

                  In SELinux, this file is used to get the security context
                  of a process.  Prior to Linux 2.6.11, this file could not
                  be used to set the security context (a write was always
                  denied), since SELinux limited process security transitions
                  to execve(2) (see the description of /proc/pid/attr/exec,
                  below).  Since Linux 2.6.11, SELinux lifted this
                  restriction and began supporting "set" operations via
                  writes to this node if authorized by policy, although use
                  of this operation is only suitable for applications that
                  are trusted to maintain any desired separation between the
                  old and new security contexts.

                  Prior to Linux 2.6.28, SELinux did not allow threads within
                  a multithreaded process to set their security context via
                  this node as it would yield an inconsistency among the
                  security contexts of the threads sharing the same memory
                  space.  Since Linux 2.6.28, SELinux lifted this restriction
                  and began supporting "set" operations for threads within a
                  multithreaded process if the new security context is
                  bounded by the old security context, where the bounded
                  relation is defined in policy and guarantees that the new
                  security context has a subset of the permissions of the old
                  security context.

                  Other security modules may choose to support "set"
                  operations via writes to this node.

           /proc/pid/attr/exec (since Linux 2.6.0)
                  This file represents the attributes to assign to the
                  process upon a subsequent execve(2).

                  In SELinux, this is needed to support role/domain
                  transitions, and execve(2) is the preferred point to make
                  such transitions because it offers better control over the
                  initialization of the process in the new security label and
                  the inheritance of state.  In SELinux, this attribute is
                  reset on execve(2) so that the new program reverts to the
                  default behavior for any execve(2) calls that it may make.
                  In SELinux, a process can set only its own
                  /proc/pid/attr/exec attribute.

           /proc/pid/attr/fscreate (since Linux 2.6.0)
                  This file represents the attributes to assign to files
                  created by subsequent calls to open(2), mkdir(2),
                  symlink(2), and mknod(2)

                  SELinux employs this file to support creation of a file
                  (using the aforementioned system calls) in a secure state,
                  so that there is no risk of inappropriate access being
                  obtained between the time of creation and the time that
                  attributes are set.  In SELinux, this attribute is reset on
                  execve(2), so that the new program reverts to the default
                  behavior for any file creation calls it may make, but the
                  attribute will persist across multiple file creation calls
                  within a program unless it is explicitly reset.  In
                  SELinux, a process can set only its own
                  /proc/pid/attr/fscreate attribute.

           /proc/pid/attr/keycreate (since Linux 2.6.18)
                  If a process writes a security context into this file, all
                  subsequently created keys (add_key(2)) will be labeled with
                  this context.  For further information, see the kernel
                  source file Documentation/security/keys/core.rst.

           /proc/pid/attr/prev (since Linux 2.6.0)
                  This file contains the security context of the process
                  before the last execve(2); that is, the previous value of
                  /proc/pid/attr/current.

           /proc/pid/attr/socketcreate (since Linux 2.6.18)
                  If a process writes a security context into this file, all
                  subsequently created sockets will be labeled with this
                  context.

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

    Linux man-pages 6.19            2026-02-08               proc_pid_attr(5)

------------------------------------------------------------------------

Pages that refer to this page: [proc_pid(5)](../man5/proc_pid.5.html)

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
