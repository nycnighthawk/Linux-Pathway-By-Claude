---
{"title": "io_uring_registered_buffers(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/io_uring_registered_buffers.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# io_uring_registered_buffers(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    io_uring...d_buffers(7) Linux Programmer's Manual io_uring...d_buffers(7)

## [](#NAME)NAME

           io_uring_registered_buffers - io_uring registered buffers overview

## [](#DESCRIPTION)DESCRIPTION

           Registered buffers are a performance optimization feature of
           io_uring that allows applications to pre-register a set of buffers
           with the kernel.  When buffers are registered, the kernel pins the
           memory and creates long-term mappings, eliminating the overhead of
           mapping and unmapping buffer memory for each I/O operation.

       Why use registered buffers?
           For every I/O operation that transfers data between user space and
           the kernel, the kernel must perform several operations on the
           buffer memory:

           • Verify the memory is accessible to the process

           • Pin the pages in memory to prevent them from being swapped out

           • Set up kernel mappings to access the memory

           These operations, while individually fast, add up when performing
           many small I/O operations. By registering buffers once upfront,
           these costs are paid only once, and subsequent I/O operations can
           use the pre-mapped buffers directly.

           Registered buffers are most beneficial for applications that:

           • Perform many small I/O operations

           • Reuse the same buffers repeatedly

           • Need the lowest possible per-I/O overhead

       Registering buffers
           Buffers are registered using io_uring_register_buffers(3) or
           io_uring_register_buffers_tags(3).  The buffers are described
           using an array of struct iovec structures:

               struct iovec iovecs[2];
               iovecs[0].iov_base = buf1;
               iovecs[0].iov_len = 4096;
               iovecs[1].iov_base = buf2;
               iovecs[1].iov_len = 8192;

               ret = io_uring_register_buffers(ring, iovecs, 2);

           The buffers must be anonymous memory (allocated via malloc(3),
           mmap(2) with MAP_ANONYMOUS, or similar). File-backed memory is not
           supported.

           There is a limit of 1 GiB per individual buffer. Huge pages are
           supported and the entire huge page will be pinned even if only
           part of it is used.

           The buffers are charged against the user's RLIMIT_MEMLOCK resource
           limit on kernels before 5.12. On kernel 5.12 and later with
           IORING_FEAT_NATIVE_WORKERS support, cgroup memory accounting is
           used instead and no memlock limit applies.

           Unless running as root, if buffer registration fails with ENOMEM,
           the memlock limit may need to be increased. The current limit can
           be checked with:

               ulimit -l

           The limit can be increased for the current shell session with:

               ulimit -l unlimited

           For a permanent change, edit /etc/security/limits.conf or use
           setrlimit(2) programmatically with RLIMIT_MEMLOCK.

       Using registered buffers
           To use a registered buffer in an I/O operation, use the fixed
           buffer variants of the prep functions:

           • io_uring_prep_read_fixed(3) instead of io_uring_prep_read(3)

           • io_uring_prep_write_fixed(3) instead of io_uring_prep_write(3)

           • io_uring_prep_readv_fixed(3) instead of io_uring_prep_readv(3)

           • io_uring_prep_writev_fixed(3) instead of io_uring_prep_writev(3)

           Zero-copy send operations can also use registered buffers:

           • io_uring_prep_send_zc(3) with IORING_RECVSEND_FIXED_BUF

           • io_uring_prep_sendmsg_zc(3) with IORING_RECVSEND_FIXED_BUF

           These functions take a buf_index parameter that specifies which
           registered buffer to use (0-indexed into the array passed to
           io_uring_register_buffers(3)).

           The memory range used for the I/O operation must fall within the
           bounds of the registered buffer. It is valid to use only a portion
           of a registered buffer for an operation.

               /* Use first 1024 bytes of registered buffer 0 */
               io_uring_prep_read_fixed(sqe, fd, buf1, 1024, offset, 0);

               /* Use registered buffer 1 */
               io_uring_prep_write_fixed(sqe, fd, buf2, 2048, offset, 1);

       Sparse buffer registration
           Applications can register a sparse buffer table using
           io_uring_register_buffers_sparse(3).  This creates a table with
           empty slots that can be filled in later using
           io_uring_register_buffers_update_tag(3).  This is useful when the
           full set of buffers is not known at registration time.

               /* Create sparse table with 10 slots */
               ret = io_uring_register_buffers_sparse(ring, 10);

               /* Later, fill in slot 3 */
               struct iovec iov = { .iov_base = buf, .iov_len = 4096 };
               ret = io_uring_register_buffers_update_tag(ring, 3, &iov, NULL, 1);

       Buffer tagging
           When using io_uring_register_buffers_tags(3) or
           io_uring_register_buffers_update_tag(3), each buffer can be
           associated with a tag value. When a buffer is unregistered (either
           explicitly or by replacing it), and there are no more in-flight
           operations using that buffer, a completion queue entry is posted
           with user_data set to the tag value and all other fields zeroed.

           This allows applications to know when it is safe to free or reuse
           the buffer memory.

       Updating registered buffers
           Registered buffers can be updated in place using
           io_uring_register_buffers_update_tag(3).  This can:

           • Replace an existing buffer with a new one

           • Fill in a sparse slot

           • Remove a buffer by setting the iovec to zero length

           Updating buffers does not immediately free resources. The old
           buffer remains valid until all in-flight operations complete.

       Unregistering buffers
           Buffers are unregistered using io_uring_unregister_buffers(3).
           This releases all registered buffers. Buffers are also
           automatically unregistered when the io_uring instance is
           destroyed.

           Applications do not need to explicitly unregister buffers before
           shutting down the ring. However, page unpinning may happen
           asynchronously, so pages may not be immediately available after
           ring destruction.

       Cloning buffers
           Registered buffers can be cloned from one ring to another using
           io_uring_clone_buffers(3) or io_uring_clone_buffers_offset(3).
           This allows multiple rings to share the same set of registered
           buffers without re-registering them.

## [](#NOTES)NOTES

           • Registered buffers provide the most benefit for small, frequent
             I/O operations where the per-operation overhead is significant.

           • For large I/O operations, the buffer mapping overhead is small
             relative to the actual I/O time, so registered buffers may not
             provide much benefit.

           • The maximum number of registered buffers is limited by available
             kernel memory and the RLIMIT_MEMLOCK limit (on older kernels).

           • Registered buffers cannot be used with provided buffer rings
             (IOSQE_BUFFER_SELECT).  These are separate mechanisms for
             different use cases.

## [](#SEE_ALSO)SEE ALSO

           io_uring(7), io_uring_registered_files(7), setrlimit(2),
           io_uring_register_buffers(3), io_uring_register_buffers_tags(3),
           io_uring_register_buffers_sparse(3),
           io_uring_register_buffers_update_tag(3),
           io_uring_unregister_buffers(3), io_uring_prep_read_fixed(3),
           io_uring_prep_write_fixed(3), io_uring_prep_send_zc(3),
           io_uring_prep_sendmsg_zc(3), io_uring_clone_buffers(3)

## [](#COLOPHON)COLOPHON

           This page is part of the liburing (A library for io_uring)
           project.  Information about the project can be found at 
           ⟨https://github.com/axboe/liburing⟩.  If you have a bug report for
           this manual page, send it to io-uring@vger.kernel.org.  This page
           was obtained from the project's upstream Git repository
           ⟨https://github.com/axboe/liburing⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-28.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux                        January 18, 2025     io_uring...d_buffers(7)

------------------------------------------------------------------------

Pages that refer to this page: [io_uring_registered_files(7)](../man7/io_uring_registered_files.7.html),  [io_uring_sqpoll(7)](../man7/io_uring_sqpoll.7.html)

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
