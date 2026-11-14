---
{"title": "UFFDIO_API(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/UFFDIO_API.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# UFFDIO_API(2const) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [BUGS](#BUGS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UFFDIO_API(2const)                                     UFFDIO_API(2const)

## [](#NAME)NAME

           UFFDIO_API - enable operation of the userfaultfd and perform API
           handshake

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/userfaultfd.h>  /* Definition of UFFD* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, UFFDIO_API, struct uffdio_api *argp);

           #include <linux/userfaultfd.h>

           struct uffdio_api {
               __u64 api;       /* Requested API version (input) */
               __u64 features;  /* Requested features (input/output) */
               __u64 ioctls;    /* Available ioctl() operations (output) */
           };

## [](#DESCRIPTION)DESCRIPTION

           Enable operation of the userfaultfd and perform API handshake.

           The api field denotes the API version requested by the
           application.  The kernel verifies that it can support the
           requested API version, and sets the features and ioctls fields to
           bit masks representing all the available features and the generic
           ioctl(2) operations available.

           Before Linux 4.11, the features field must be initialized to zero
           before the call to UFFDIO_API, and zero (i.e., no feature bits) is
           placed in the features field by the kernel upon return from
           ioctl(2).

           Since Linux 4.11, userfaultfd supports features that need to be
           enabled explicitly.  To enable any of the features, one needs to
           set the corresponding feature bits in features when issuing the
           UFFDIO_API ioctl.

           For historical reasons, a temporary userfaultfd is needed to probe
           what userfaultfd features the kernel supports.  The application
           needs to create a temporary userfaultfd, issue an UFFDIO_API ioctl
           with features set to zero.  After the UFFDIO_API ioctl returns
           successfully, features should contain all the userfaultfd features
           that the kernel supports.  The temporary userfaultfd can be safely
           closed after the probe.

           If the application sets unsupported feature bits, the kernel will
           zero out the returned uffdio_api structure and return EINVAL.

           The following feature bits may be set:

           UFFD_FEATURE_EVENT_FORK (since Linux 4.11)
                  When this feature is enabled, the userfaultfd objects
                  associated with a parent process are duplicated into the
                  child process during fork(2) and a UFFD_EVENT_FORK event is
                  delivered to the userfaultfd monitor

           UFFD_FEATURE_EVENT_REMAP (since Linux 4.11)
                  If this feature is enabled, when the faulting process
                  invokes mremap(2), the userfaultfd monitor will receive an
                  event of type UFFD_EVENT_REMAP.

           UFFD_FEATURE_EVENT_REMOVE (since Linux 4.11)
                  If this feature is enabled, when the faulting process calls
                  madvise(2) with the MADV_DONTNEED or MADV_REMOVE advice
                  value to free a virtual memory area the userfaultfd monitor
                  will receive an event of type UFFD_EVENT_REMOVE.

           UFFD_FEATURE_EVENT_UNMAP (since Linux 4.11)
                  If this feature is enabled, when the faulting process
                  unmaps virtual memory either explicitly with munmap(2), or
                  implicitly during either mmap(2) or mremap(2), the
                  userfaultfd monitor will receive an event of type
                  UFFD_EVENT_UNMAP.

           UFFD_FEATURE_MISSING_HUGETLBFS (since Linux 4.11)
                  If this feature bit is set, the kernel supports registering
                  userfaultfd ranges on hugetlbfs virtual memory areas

           UFFD_FEATURE_MISSING_SHMEM (since Linux 4.11)
                  If this feature bit is set, the kernel supports registering
                  userfaultfd ranges on shared memory areas.  This includes
                  all kernel shared memory APIs: System V shared memory,
                  tmpfs(5), shared mappings of /dev/zero, mmap(2) with the
                  MAP_SHARED flag set, memfd_create(2), and so on.

           UFFD_FEATURE_SIGBUS (since Linux 4.14)
                  If this feature bit is set, no page-fault events
                  (UFFD_EVENT_PAGEFAULT) will be delivered.  Instead, a
                  SIGBUS signal will be sent to the faulting process.
                  Applications using this feature will not require the use of
                  a userfaultfd monitor for processing memory accesses to the
                  regions registered with userfaultfd.

           UFFD_FEATURE_THREAD_ID (since Linux 4.14)
                  If this feature bit is set, uffd_msg.pagefault.feat.ptid
                  will be set to the faulted thread ID for each page-fault
                  message.

           UFFD_FEATURE_PAGEFAULT_FLAG_WP (since Linux 5.10)
                  If this feature bit is set, userfaultfd supports write-
                  protect faults for anonymous memory.  (Note that shmem /
                  hugetlbfs support is indicated by a separate feature.)

           UFFD_FEATURE_MINOR_HUGETLBFS (since Linux 5.13)
                  If this feature bit is set, the kernel supports registering
                  userfaultfd ranges in minor mode on hugetlbfs-backed memory
                  areas.

           UFFD_FEATURE_MINOR_SHMEM (since Linux 5.14)
                  If this feature bit is set, the kernel supports registering
                  userfaultfd ranges in minor mode on shmem-backed memory
                  areas.

           UFFD_FEATURE_EXACT_ADDRESS (since Linux 5.18)
                  If this feature bit is set, uffd_msg.pagefault.address will
                  be set to the exact page-fault address that was reported by
                  the hardware, and will not mask the offset within the page.
                  Note that old Linux versions might indicate the exact
                  address as well, even though the feature bit is not set.

           UFFD_FEATURE_WP_HUGETLBFS_SHMEM (since Linux 5.19)
                  If this feature bit is set, userfaultfd supports write-
                  protect faults for hugetlbfs and shmem / tmpfs memory.

           UFFD_FEATURE_WP_UNPOPULATED (since Linux 6.4)
                  If this feature bit is set, the kernel will handle
                  anonymous memory the same way as file memory, by allowing
                  the user to write-protect unpopulated page table entries.

           UFFD_FEATURE_POISON (since Linux 6.6)
                  If this feature bit is set, the kernel supports resolving
                  faults with the UFFDIO_POISON ioctl.

           UFFD_FEATURE_WP_ASYNC (since Linux 6.7)
                  If this feature bit is set, the write protection faults
                  would be asynchronously resolved by the kernel.

           UFFD_FEATURE_MOVE (since Linux 6.8)
                  If this feature bit is set, the kernel supports resolving
                  faults with the UFFDIO_MOVE ioctl.

           UFFD_FEATURE_RWP (since Linux 7.2)
                  If this feature bit is set, the kernel supports read-write-
                  protection tracking, and the UFFDIO_REGISTER_MODE_RWP
                  registration mode and the UFFDIO_RWPROTECT ioctl become
                  available.

           UFFD_FEATURE_RWP_ASYNC (since Linux 7.2)
                  If this feature bit is set, the kernel will resolve read-
                  write-protect faults in place without delivering a
                  notification, automatically restoring page permissions and
                  letting the faulted thread continue.  This bit requires
                  UFFD_FEATURE_RWP to be set in the same UFFDIO_API call.
                  The async mode can also be toggled at runtime using the
                  UFFDIO_SET_MODE(2const) ioctl.

           The returned argp->ioctls field can contain the following bits:

           1 << _UFFDIO_API
                  The UFFDIO_API operation is supported.

           1 << _UFFDIO_REGISTER
                  The UFFDIO_REGISTER operation is supported.

           1 << _UFFDIO_UNREGISTER
                  The UFFDIO_UNREGISTER operation is supported.

           1 << _UFFDIO_SET_MODE (since Linux 7.2)
                  The UFFDIO_SET_MODE operation is supported.  This is a
                  file-descriptor-level ioctl and is reported once per
                  userfaultfd, independent of any registered range.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.

           On error, -1 is returned and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT argp refers to an address that is outside the calling
                  process's accessible address space.

           EINVAL The API version requested in the api field is not supported
                  by this kernel, or the features field passed to the kernel
                  includes feature bits that are not supported by the current
                  kernel version.

           EINVAL A previous UFFDIO_API call already enabled one or more
                  features for this userfaultfd.  Calling UFFDIO_API twice,
                  the first time with no features set, is explicitly allowed
                  as per the two-step feature detection handshake.

           EPERM  The UFFD_FEATURE_EVENT_FORK feature was enabled, but the
                  calling process doesn't have the CAP_SYS_PTRACE capability.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 4.3.

## [](#CAVEATS)CAVEATS

           If an error occurs, the kernel may zero the provided uffdio_api
           structure.  The caller should treat its contents as unspecified,
           and reinitialize it before re-attempting another UFFDIO_API call.

## [](#BUGS)BUGS

           In order to detect available userfault features and enable some
           subset of those features the userfaultfd file descriptor must be
           closed after the first UFFDIO_API operation that queries features
           availability and reopened before the second UFFDIO_API operation
           that actually enables the desired features.

## [](#EXAMPLES)EXAMPLES

           See userfaultfd(2).

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_userfaultfd(2), mmap(2), userfaultfd(2)

           linux.git/Documentation/admin-guide/mm/userfaultfd.rst

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

    Linux man-pages 6.19            2026-06-04             UFFDIO_API(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_userfaultfd(2)](../man2/ioctl_userfaultfd.2.html),  [UFFDIO_SET_MODE(2const)](../man2/UFFDIO_SET_MODE.2const.html),  [userfaultfd(2)](../man2/userfaultfd.2.html)

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
