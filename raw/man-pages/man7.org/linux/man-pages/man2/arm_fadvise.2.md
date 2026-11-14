---
{"title": "posix_fadvise(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/arm_fadvise.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# posix_fadvise(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    posix_fadvise(2)           System Calls Manual           posix_fadvise(2)

## [](#NAME)NAME

           posix_fadvise - predeclare an access pattern for file data

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <fcntl.h>

           int posix_fadvise(int fd, off_t offset, off_t size, int advice);

       Feature Test Macro Requirements for glibc (see
       feature_test_macros(7)):

           posix_fadvise():
               _POSIX_C_SOURCE >= 200112L

## [](#DESCRIPTION)DESCRIPTION

           Programs can use posix_fadvise() to announce an intention to
           access file data in a specific pattern in the future, thus
           allowing the kernel to perform appropriate optimizations.

           The advice applies to a (not necessarily existent) region starting
           at offset and extending for size bytes (or until the end of the
           file if size is 0) within the file referred to by fd.  The advice
           is not binding; it merely constitutes an expectation on behalf of
           the application.

           Permissible values for advice include:

           POSIX_FADV_NORMAL
                  Indicates that the application has no advice to give about
                  its access pattern for the specified data.  If no advice is
                  given for an open file, this is the default assumption.

           POSIX_FADV_SEQUENTIAL
                  The application expects to access the specified data
                  sequentially (with lower offsets read before higher ones).

           POSIX_FADV_RANDOM
                  The specified data will be accessed in random order.

           POSIX_FADV_NOREUSE
                  The specified data will be accessed only once.

                  Before Linux 2.6.18, POSIX_FADV_NOREUSE had the same
                  semantics as POSIX_FADV_WILLNEED.  This was probably a bug;
                  from Linux 2.6.18 until Linux 6.2 this flag was a no-op.
                  Since Linux 6.3, POSIX_FADV_NOREUSE signals that the kernel
                  page replacement algorithm can ignore access to mapped page
                  cache marked by this flag.  This is useful, for example,
                  while streaming large files.

           POSIX_FADV_WILLNEED
                  The specified data will be accessed in the near future.

                  POSIX_FADV_WILLNEED initiates a nonblocking read of the
                  specified region into the page cache.  The amount of data
                  read may be decreased by the kernel depending on virtual
                  memory load.  (A few megabytes will usually be fully
                  satisfied, and more is rarely useful.)

           POSIX_FADV_DONTNEED
                  The specified data will not be accessed in the near future.

                  POSIX_FADV_DONTNEED attempts to free cached pages
                  associated with the specified region.  This is useful, for
                  example, while streaming large files.  A program may
                  periodically request the kernel to free cached data that
                  has already been used, so that more useful cached pages are
                  not discarded instead.

                  Requests to discard partial pages are ignored.  It is
                  preferable to preserve needed data than discard unneeded
                  data.  If the application requires that data be considered
                  for discarding, then offset and size must be page-aligned.

                  The implementation may attempt to write back dirty pages in
                  the specified region, but this is not guaranteed.  Any
                  unwritten dirty pages will not be freed.  If the
                  application wishes to ensure that dirty pages will be
                  released, it should call fsync(2) or fdatasync(2) first.

## [](#RETURN_VALUE)RETURN VALUE

           On success, zero is returned.  On error, an error number is
           returned.

## [](#ERRORS)ERRORS

           EBADF  The fd argument was not a valid file descriptor.

           EINVAL An invalid value was specified for advice.

           ESPIPE The specified file descriptor refers to a pipe or FIFO.
                  (ESPIPE is the error specified by POSIX, but before Linux
                  2.6.16, Linux returned EINVAL in this case.)

## [](#VERSIONS)VERSIONS

           Under Linux, POSIX_FADV_NORMAL sets the readahead window to the
           default size for the backing device; POSIX_FADV_SEQUENTIAL doubles
           this size, and POSIX_FADV_RANDOM disables file readahead entirely.
           POSIX_FADV_NOREUSE does not modify the readahead window size.
           These changes affect the entire file, not just the specified
           region (but other open file handles to the same file are
           unaffected).

       C library/kernel differences
           The name of the wrapper function in the C library is
           posix_fadvise().  The underlying system call is called fadvise64()
           (or, on some architectures, fadvise64_64()); the difference
           between the two is that the former system call assumes that the
           type of the size argument is size_t, while the latter expects
           loff_t there.

       Architecture-specific variants
           Some architectures require 64-bit arguments to be aligned in a
           suitable pair of registers (see syscall(2) for further detail).
           On such architectures, the call signature of posix_fadvise() shown
           in the SYNOPSIS would force a register to be wasted as padding
           between the fd and offset arguments.  Therefore, these
           architectures define a version of the system call that orders the
           arguments suitably, but is otherwise exactly the same as
           posix_fadvise().

           For example, since Linux 2.6.14, ARM has the following system
           call:

               long arm_fadvise64_64(int fd, int advice,
                                     loff_t offset, loff_t size);

           These architecture-specific details are generally hidden from
           applications by the glibc posix_fadvise() wrapper function, which
           invokes the appropriate architecture-specific system call.

## [](#STANDARDS)STANDARDS

           POSIX.1-2024.

## [](#HISTORY)HISTORY

           POSIX.1-2001.

           Kernel support first appeared in Linux 2.5.60; the underlying
           system call is called fadvise64().  Library support has been
           provided since glibc 2.2, via the wrapper function
           posix_fadvise().

           Since Linux 3.18, support for the underlying system call is
           optional, depending on the setting of the CONFIG_ADVISE_SYSCALLS
           configuration option.

           The type of the size argument was changed from size_t to off_t in
           POSIX.1-2001 TC1.

## [](#NOTES)NOTES

           The contents of the kernel buffer cache can be cleared via the
           /proc/sys/vm/drop_caches interface described in proc(5).

           One can obtain a snapshot of which pages of a file are resident in
           the buffer cache by opening a file, mapping it with mmap(2), and
           then applying mincore(2) to the mapping.

## [](#BUGS)BUGS

           Before Linux 2.6.6, if size was specified as 0, then this was
           interpreted literally as "zero bytes", rather than as meaning "all
           bytes through to the end of the file".

## [](#SEE_ALSO)SEE ALSO

           fincore(1), mincore(2), readahead(2), sync_file_range(2),
           posix_fallocate(3), posix_madvise(3)

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

    Linux man-pages 6.19            2026-02-08               posix_fadvise(2)

------------------------------------------------------------------------

Pages that refer to this page: [fadvise(1)](../man1/fadvise.1.html),  [strace(1)](../man1/strace.1.html),  [fsync(2)](../man2/fsync.2.html),  [io_uring_enter2(2)](../man2/io_uring_enter2.2.html),  [io_uring_enter(2)](../man2/io_uring_enter.2.html),  [mincore(2)](../man2/mincore.2.html),  [readahead(2)](../man2/readahead.2.html),  [syscall(2)](../man2/syscall.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [io_uring_prep_fadvise(3)](../man3/io_uring_prep_fadvise.3.html),  [io_uring_prep_fadvise64(3)](../man3/io_uring_prep_fadvise64.3.html),  [off_t(3type)](../man3/off_t.3type.html),  [posix_fallocate(3)](../man3/posix_fallocate.3.html),  [posix_madvise(3)](../man3/posix_madvise.3.html)

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
