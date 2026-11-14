---
{"title": "landlock_create_ruleset(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/landlock_create_ruleset.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# landlock_create_ruleset(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    landlock_create_ruleset(2) System Calls Manual landlock_create_ruleset(2)

## [](#NAME)NAME

           landlock_create_ruleset - create a new Landlock ruleset

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/landlock.h>  /* Definition of LANDLOCK_* constants */
           #include <sys/syscall.h>     /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_landlock_create_ruleset,
                       const struct landlock_ruleset_attr *attr,
                       size_t size , uint32_t flags);

## [](#DESCRIPTION)DESCRIPTION

           A Landlock ruleset identifies a set of rules (i.e., actions on
           objects).  This landlock_create_ruleset() system call creates a
           new file descriptor which identifies a ruleset.  This file
           descriptor can then be used by landlock_add_rule(2) and
           landlock_restrict_self(2).  See landlock(7) for a global overview.

           attr specifies the properties of the new ruleset.  It points to
           the following structure:

                      struct landlock_ruleset_attr {
                          __u64 handled_access_fs;
                          __u64 handled_access_net;
                          __u64 scoped;
                      };

                  handled_access_fs is a bitmask of handled filesystem
                  actions (see Filesystem actions in landlock(7)).

                  handled_access_net is a bitmask of handled network actions
                  (see Network actions in landlock(7)).

                  scoped is a bitmask of scope flags (see Scope flags in
                  landlock(7)).

                  This structure defines a set of handled access rights, a
                  set of actions on different object types, which should be
                  denied by default when the ruleset is enacted.  Vice versa,
                  access rights that are not specifically listed here are not
                  going to be denied by this ruleset when it is enacted.

                  For historical reasons, the LANDLOCK_ACCESS_FS_REFER right
                  is always denied by default, even when its bit is not set
                  in handled_access_fs.  In order to add new rules with this
                  access right, the bit must still be set explicitly (see
                  Filesystem actions in landlock(7)).

                  The explicit listing of handled access rights is required
                  for backwards compatibility reasons.  In most use cases,
                  processes that use Landlock will handle a wide range or all
                  access rights that they know about at build time (and that
                  they have tested with a kernel that supported them all).

                  This structure can grow in future Landlock versions.

           size must be specified as sizeof(struct landlock_ruleset_attr) for
           compatibility reasons.

           flags must be 0 if attr is used.  Otherwise, flags can be set to:

           LANDLOCK_CREATE_RULESET_VERSION
                  Return the highest supported Landlock ABI version (starting
                  at 1).  This version can be used for a best-effort security
                  approach, which is encouraged when user space is not pinned
                  to a specific kernel version.

                  Unless noted otherwise, all features documented in these
                  manual pages are available with the version 1.

           LANDLOCK_CREATE_RULESET_ERRATA
                  Return a bitmask of fixed issues for the current Landlock
                  ABI version.  If bit N is set (i.e.,
                  errata & (1 << (N - 1))), then erratum N has been fixed in
                  the running kernel.

                  In addition to ABI versions, Landlock's errata mechanism
                  tracks fixes for issues that may affect backwards
                  compatibility or require userspace awareness.

                  Only check errata if your application specifically relies
                  on behavior that changed due to the fix.

                  The full list of Landlock errata is available at
                  ⟨https://docs.kernel.org/userspace-api/landlock.html#landlock-errata⟩.

                  This flag is available on all Linux versions where Landlock
                  errata were fixed.  This specifically includes all newest
                  bugfix releases of stable kernels where Landlock is
                  supported.

           If LANDLOCK_CREATE_RULESET_VERSION or
           LANDLOCK_CREATE_RULESET_ERRATA is set, then attr must be NULL and
           size must be 0.

## [](#RETURN_VALUE)RETURN VALUE

           On success, landlock_create_ruleset() returns a new Landlock
           ruleset file descriptor, a Landlock ABI version, or a Landlock
           errata bitmask, according to flags.

           On error, -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           landlock_create_ruleset() can fail for the following reasons:

           E2BIG  size is too big.

           EFAULT attr was not a valid address.

           EINVAL Unknown flags, or unknown access, or unknown scope, or too
                  small size.

           EINVAL Non-NULL attr or non-zero size in combination with
                  LANDLOCK_CREATE_RULESET_VERSION or
                  LANDLOCK_CREATE_RULESET_ERRATA.

           ENOMSG Empty accesses (i.e., attr did not specify any access
                  rights to restrict).

           EOPNOTSUPP
                  Landlock is supported by the kernel but disabled at boot
                  time.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 5.13.

## [](#EXAMPLES)EXAMPLES

           See landlock(7).

## [](#SEE_ALSO)SEE ALSO

           landlock_add_rule(2), landlock_restrict_self(2), landlock(7)

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

    Linux man-pages 6.19            2026-04-21     landlock_create_ruleset(2)

------------------------------------------------------------------------

Pages that refer to this page: [landlock_add_rule(2)](../man2/landlock_add_rule.2.html),  [landlock_restrict_self(2)](../man2/landlock_restrict_self.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [landlock(7)](../man7/landlock.7.html)

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
