---
{"title": "landlock_restrict_self(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/landlock_restrict_self.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# landlock_restrict_self(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    landlock_restrict_self(2)  System Calls Manual  landlock_restrict_self(2)

## [](#NAME)NAME

           landlock_restrict_self - enforce a Landlock ruleset

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/landlock.h>  /* Definition of LANDLOCK_* constants */
           #include <sys/syscall.h>     /* Definition of SYS_* constants */

           int syscall(SYS_landlock_restrict_self, int ruleset_fd,
                       uint32_t flags);

## [](#DESCRIPTION)DESCRIPTION

           Once a Landlock ruleset is populated with the desired rules, the
           landlock_restrict_self() system call enforces this ruleset on the
           calling thread.  See landlock(7) for a global overview.

           A thread can be restricted with multiple rulesets that are then
           composed together to form the thread's Landlock domain.  This can
           be seen as a stack of rulesets but it is implemented in a more
           efficient way.  A domain can only be updated in such a way that
           the constraints of each past and future composed rulesets will
           restrict the thread and its future children for their entire life.
           It is then possible to gradually enforce tailored access control
           policies with multiple independent rulesets coming from different
           sources (e.g., init system configuration, user session policy,
           built-in application policy).  However, most applications should
           only need one call to landlock_restrict_self() and they should
           avoid arbitrary numbers of such calls because of the composed
           rulesets limit.  Instead, developers are encouraged to build a
           single tailored ruleset with multiple calls to
           landlock_add_rule(2).

           In order to enforce a ruleset, either the caller must have the
           CAP_SYS_ADMIN capability in its user namespace, or the thread must
           already have the no_new_privs bit set.  As for seccomp(2), this
           avoids scenarios where unprivileged processes can affect the
           behavior of privileged children (e.g., because of set-user-ID
           binaries).  If that bit was not already set by an ancestor of this
           thread, the thread must make the following call:

                  prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0);

           ruleset_fd is a Landlock ruleset file descriptor obtained with
           landlock_create_ruleset(2) and fully populated with a set of calls
           to landlock_add_rule(2).

           By default, denied accesses originating from programs that sandbox
           themselves are logged via the audit subsystem.  Such events
           typically indicate unexpected behavior, such as bugs or
           exploitation attempts.  However, to avoid excessive logging,
           access requests denied by a domain not created by the originating
           program are not logged by default.  The rationale is that programs
           should know their own behavior, but not necessarily the behavior
           of other programs.  This default configuration is suitable for
           most programs that sandbox themselves.  For specific use cases,
           the following flags allow programs to modify this default logging
           behavior.

           The LANDLOCK_RESTRICT_SELF_LOG_SAME_EXEC_OFF and
           LANDLOCK_RESTRICT_SELF_LOG_NEW_EXEC_ON flags apply to the newly
           created Landlock domain.

           LANDLOCK_RESTRICT_SELF_LOG_SAME_EXEC_OFF  (since Landlock ABI
           version 7)
                  Disables logging of denied accesses originating from the
                  thread creating the Landlock domain, as well as its
                  children, as long as they continue running the same
                  executable code (i.e., without an intervening execve(2)
                  call).  This is intended for programs that execute unknown
                  code without invoking execve(2), such as script
                  interpreters.  Programs that only sandbox themselves should
                  not set this flag, so users can be notified of unauthorized
                  access attempts via system logs.

           LANDLOCK_RESTRICT_SELF_LOG_NEW_EXEC_ON  (since Landlock ABI
           version 7)
                  Enables logging of denied accesses after an execve(2) call,
                  providing visibility into unauthorized access attempts by
                  newly executed programs within the created Landlock domain.
                  This flag is recommended only when all potential
                  executables in the domain are expected to comply with the
                  access restrictions, as excessive audit log entries could
                  make it more difficult to identify critical events.

           LANDLOCK_RESTRICT_SELF_LOG_SUBDOMAINS_OFF  (since Landlock ABI
           version 7)
                  Disables logging of denied accesses originating from nested
                  Landlock domains created by the caller or its descendants.
                  This flag should be set according to runtime configuration,
                  not hardcoded, to avoid suppressing important security
                  events.  It is useful for container runtimes or sandboxing
                  tools that may launch programs which themselves create
                  Landlock domains and could otherwise generate excessive
                  logs.  Unlike LANDLOCK_RESTRICT_SELF_LOG_SAME_EXEC_OFF,
                  this flag only affects future nested domains, not the one
                  being created.  It can also be used with a ruleset_fd value
                  of -1 to mute subdomain logs without creating a domain.

           The following flag supports policy enforcement in multithreaded
           processes:

           LANDLOCK_RESTRICT_SELF_TSYNC  (since Landlock ABI version 8)
                  Applies the new Landlock configuration atomically to all
                  threads of the current process, including the Landlock
                  domain and logging configuration.  This overrides the
                  Landlock configuration of sibling threads, irrespective of
                  previously established Landlock domains and logging
                  configurations on those threads.

                  If the calling thread is running with no_new_privs, this
                  operation enables no_new_privs on the sibling threads as
                  well.

## [](#RETURN_VALUE)RETURN VALUE

           On success, landlock_restrict_self() returns 0.  On error, -1 is
           returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           landlock_restrict_self() can fail for the following reasons:

           E2BIG  The maximum number of composed rulesets is reached for the
                  calling thread.  This limit is currently 64.

           EBADF  ruleset_fd is not a file descriptor for the current thread.

           EBADFD ruleset_fd is not a ruleset file descriptor.

           EINVAL Invalid value in flags.

           EOPNOTSUPP
                  Landlock is supported by the kernel but disabled at boot
                  time.

           EPERM  ruleset_fd has no read access to the underlying ruleset, or
                  the calling thread is not running with no_new_privs, or it
                  doesn't have the CAP_SYS_ADMIN in its user namespace.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 5.13.

## [](#EXAMPLES)EXAMPLES

           See landlock(7).

## [](#SEE_ALSO)SEE ALSO

           landlock_create_ruleset(2), landlock_add_rule(2), landlock(7)

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

    Linux man-pages 6.19            2026-05-04      landlock_restrict_self(2)

------------------------------------------------------------------------

Pages that refer to this page: [landlock_add_rule(2)](../man2/landlock_add_rule.2.html),  [landlock_create_ruleset(2)](../man2/landlock_create_ruleset.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [landlock(7)](../man7/landlock.7.html)

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
