---
{"title": "gethostname(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/gethostname.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gethostname(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    gethostname(2)             System Calls Manual             gethostname(2)

## [](#NAME)NAME

           gethostname, sethostname - get/set hostname

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <unistd.h>

           int gethostname(char *name, size_t size);
           int sethostname(const char *name, size_t size);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           gethostname():
               _XOPEN_SOURCE >= 500 || _POSIX_C_SOURCE >= 200112L
                   || /* glibc 2.19 and earlier */ _BSD_SOURCE

           sethostname():
               Since glibc 2.21:
                   _DEFAULT_SOURCE
               In glibc 2.19 and 2.20:
                   _DEFAULT_SOURCE || (_XOPEN_SOURCE && _XOPEN_SOURCE < 500)
               Up to and including glibc 2.19:
                   _BSD_SOURCE || (_XOPEN_SOURCE && _XOPEN_SOURCE < 500)

## [](#DESCRIPTION)DESCRIPTION

           These system calls are used to access or to change the system
           hostname.  More precisely, they operate on the hostname associated
           with the calling process's UTS namespace.

           sethostname() sets the hostname to the value given in the
           character array name.  The size argument specifies the number of
           bytes in name.  (Thus, name does not require a terminating null
           byte.)

           gethostname() returns the null-terminated hostname in the
           character array name, which has a size of size bytes.  If the
           null-terminated hostname is too large to fit, then the name is
           truncated, and no error is returned (but see VERSIONS below).
           POSIX.1 says that if such truncation occurs, then it is
           unspecified whether the returned buffer includes a terminating
           null byte.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, -1 is returned, and errno
           is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT name is an invalid address.

           EINVAL size is negative or, for sethostname(), size is larger than
                  the maximum allowed size.

           ENAMETOOLONG
                  (glibc gethostname()) size is smaller than the actual size.
                  (Before glibc 2.1, glibc uses EINVAL for this case.)

           EPERM  For sethostname(), the caller did not have the
                  CAP_SYS_ADMIN capability in the user namespace associated
                  with its UTS namespace (see namespaces(7)).

## [](#VERSIONS)VERSIONS

           SUSv2 guarantees that "Host names are limited to 255 bytes".
           POSIX.1 guarantees that "Host names (not including the terminating
           null byte) are limited to HOST_NAME_MAX bytes".  On Linux,
           HOST_NAME_MAX is defined with the value 64, which has been the
           limit since Linux 1.0 (earlier kernels imposed a limit of 8
           bytes).

       C library/kernel differences
           The GNU C library does not employ the gethostname() system call;
           instead, it implements gethostname() as a library function that
           calls uname(2) and copies up to size bytes from the returned
           nodename field into name.  Having performed the copy, the function
           then checks if the length of the nodename was greater than or
           equal to size, and if it is, then the function returns -1 with
           errno set to ENAMETOOLONG; in this case, a terminating null byte
           is not included in the returned name.

## [](#STANDARDS)STANDARDS

           gethostname()
                  POSIX.1-2024.

           sethostname()
                  None.

## [](#HISTORY)HISTORY

           gethostname()
                  4.2BSD, SVr4, POSIX.1-2001.

           sethostname()
                  4.2BSD, SVr4.

           Versions of glibc before glibc 2.2 handle the case where the
           length of the nodename was greater than or equal to size
           differently: nothing is copied into name and the function returns
           -1 with errno set to ENAMETOOLONG.

## [](#SEE_ALSO)SEE ALSO

           hostname(1), getdomainname(2), setdomainname(2), uname(2),
           uts_namespaces(7)

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

    Linux man-pages 6.19            2026-02-08                 gethostname(2)

------------------------------------------------------------------------

Pages that refer to this page: [crontab(1)](../man1/crontab.1.html),  [hostname(1)](../man1/hostname.1.html),  [logger(1)](../man1/logger.1.html),  [pmhostname(1)](../man1/pmhostname.1.html),  [getdomainname(2)](../man2/getdomainname.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [uname(2)](../man2/uname.2.html),  [gethostid(3)](../man3/gethostid.3.html),  [rcmd(3)](../man3/rcmd.3.html),  [sysconf(3)](../man3/sysconf.3.html),  [hostname(5)](../man5/hostname.5.html),  [org.freedesktop.hostname1(5)](../man5/org.freedesktop.hostname1.5.html),  [resolv.conf(5)](../man5/resolv.conf.5.html),  [rpmbuild-config(5)](../man5/rpmbuild-config.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [capabilities(7)](../man7/capabilities.7.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [uts_namespaces(7)](../man7/uts_namespaces.7.html),  [cron(8)](../man8/cron.8.html),  [lsof(8)](../man8/lsof.8.html),  [nss-myhostname(8)](../man8/nss-myhostname.8.html),  [systemd-hostnamed.service(8)](../man8/systemd-hostnamed.service.8.html)

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
