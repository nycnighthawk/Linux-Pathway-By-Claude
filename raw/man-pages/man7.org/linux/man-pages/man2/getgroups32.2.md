---
{"title": "getgroups(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/getgroups32.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getgroups(2) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    getgroups(2)               System Calls Manual               getgroups(2)

## [](#NAME)NAME

           getgroups, setgroups - get/set list of supplementary group IDs

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int getgroups(int size, gid_t list[_Nullable size]);

           #include <grp.h>

           int setgroups(size_t size, const gid_t list[size]);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           setgroups():
               Since glibc 2.19:
                   _DEFAULT_SOURCE
               glibc 2.19 and earlier:
                   _BSD_SOURCE

## [](#DESCRIPTION)DESCRIPTION

           getgroups() returns the supplementary group IDs of the calling
           process in list.  The argument size should be set to the maximum
           number of items that can be stored in the buffer pointed to by
           list.  If the calling process is a member of more than size
           supplementary groups, then an error results.

           It is unspecified whether the effective group ID of the calling
           process is included in the returned list.  (Thus, an application
           should also call getegid(2) and add or remove the resulting
           value.)

           If size is zero, list is not modified, but the total number of
           supplementary group IDs for the process is returned.  This allows
           the caller to determine the size of a dynamically allocated list
           to be used in a further call to getgroups().

           setgroups() sets the supplementary group IDs for the calling
           process.  Appropriate privileges are required (see the description
           of the EPERM error, below).  The size argument specifies the
           number of supplementary group IDs in the buffer pointed to by
           list.  A process can drop all of its supplementary groups with the
           call:

               setgroups(0, (gid_t [0]){});

## [](#RETURN_VALUE)RETURN VALUE

           On success, getgroups() returns the number of supplementary group
           IDs.  On error, -1 is returned, and errno is set to indicate the
           error.

           On success, setgroups() returns 0.  On error, -1 is returned, and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT list has an invalid address.

           getgroups() can additionally fail with the following error:

           EINVAL size is less than the number of supplementary group IDs,
                  but is not zero.

           setgroups() can additionally fail with the following errors:

           EINVAL size is greater than NGROUPS_MAX (32 before Linux 2.6.4;
                  65536 since Linux 2.6.4).

           ENOMEM Out of memory.

           EPERM  The calling process has insufficient privilege (the caller
                  does not have the CAP_SETGID capability in the user
                  namespace in which it resides).

           EPERM (since Linux 3.19)
                  The use of setgroups() is denied in this user namespace.
                  See the description of /proc/pid/setgroups in
                  user_namespaces(7).

## [](#VERSIONS)VERSIONS

       C library/kernel differences
           At the kernel level, user IDs and group IDs are a per-thread
           attribute.  However, POSIX requires that all threads in a process
           share the same credentials.  The NPTL threading implementation
           handles the POSIX requirements by providing wrapper functions for
           the various system calls that change process UIDs and GIDs.  These
           wrapper functions (including the one for setgroups()) employ a
           signal-based technique to ensure that when one thread changes
           credentials, all of the other threads in the process also change
           their credentials.  For details, see nptl(7).

## [](#STANDARDS)STANDARDS

           getgroups()
                  POSIX.1-2024.

           setgroups()
                  None.

## [](#HISTORY)HISTORY

           getgroups()
                  4.3BSD, SVr4, POSIX.1-1988.

           setgroups()
                  SVr4, 4.3BSD.  Since setgroups() requires privilege, it is
                  not covered by POSIX.1.

           The original Linux getgroups() system call supported only 16-bit
           group IDs.  Subsequently, Linux 2.4 added getgroups32(),
           supporting 32-bit IDs.  The glibc getgroups() wrapper function
           transparently deals with the variation across kernel versions.

## [](#NOTES)NOTES

           A process can have up to NGROUPS_MAX supplementary group IDs in
           addition to the effective group ID.  The constant NGROUPS_MAX is
           defined in <limits.h>.  The set of supplementary group IDs is
           inherited from the parent process, and preserved across an
           execve(2).

           The maximum number of supplementary group IDs can be found at run
           time using sysconf(3):

               long ngroups_max;
               ngroups_max = sysconf(_SC_NGROUPS_MAX);

           The maximum return value of getgroups() cannot be larger than one
           more than this value.  Since Linux 2.6.4, the maximum number of
           supplementary group IDs is also exposed via the Linux-specific
           read-only file, /proc/sys/kernel/ngroups_max.

## [](#EXAMPLES)EXAMPLES

           #include <err.h>
           #include <stddef.h>
           #include <stdint.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <sys/types.h>
           #include <unistd.h>

           #define MALLOC(n, T)  ((T *) reallocarray(NULL, n, sizeof(T)))

           static gid_t *agetgroups(size_t *ngids);

           int
           main(void)
           {
               gid_t   *gids;
               size_t  n;

               gids = agetgroups(&n);
               if (gids == NULL)
                   err(EXIT_FAILURE, "agetgroups");

               if (n != 0) {
                   printf("%jd", (intmax_t) gids[0]);
                   for (size_t i = 1; i < n; i++)
                       printf(" %jd", (intmax_t) gids[i]);
               }
               puts("");

               free(gids);
               exit(EXIT_SUCCESS);
           }

           static gid_t *
           agetgroups(size_t *ngids)
           {
               int    n;
               gid_t  *gids;

               n = getgroups(0, NULL);
               if (n == -1)
                   return NULL;

               gids = MALLOC(n, gid_t);
               if (gids == NULL)
                   return NULL;

               n = getgroups(n, gids);
               if (n == -1) {
                   free(gids);
                   return NULL;
               }

               *ngids = n;
               return gids;
           }

## [](#SEE_ALSO)SEE ALSO

           getgid(2), setgid(2), getgrouplist(3), group_member(3),
           initgroups(3), capabilities(7), credentials(7)

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

    Linux man-pages 6.19            2026-02-08                   getgroups(2)

------------------------------------------------------------------------

Pages that refer to this page: [capsh(1)](../man1/capsh.1.html),  [ps(1)](../man1/ps.1.html),  [unshare(1)](../man1/unshare.1.html),  [syscalls(2)](../man2/syscalls.2.html),  [cap_get_proc(3)](../man3/cap_get_proc.3.html),  [getgrouplist(3)](../man3/getgrouplist.3.html),  [group_member(3)](../man3/group_member.3.html),  [id_t(3type)](../man3/id_t.3type.html),  [initgroups(3)](../man3/initgroups.3.html),  [credentials(7)](../man7/credentials.7.html),  [nptl(7)](../man7/nptl.7.html),  [path_resolution(7)](../man7/path_resolution.7.html),  [signal-safety(7)](../man7/signal-safety.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
