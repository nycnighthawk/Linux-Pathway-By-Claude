---
{"title": "s390_sthyi(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/s390_sthyi.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# s390_sthyi(2) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    s390_sthyi(2)              System Calls Manual              s390_sthyi(2)

## [](#NAME)NAME

           s390_sthyi - emulate STHYI instruction

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/sthyi.h>        /* Definition of STHYI_* constants */
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_s390_sthyi, unsigned long function_code,
                       void *resp_buffer, uint64_t *return_code,
                       unsigned long flags);

           Note: glibc provides no wrapper for s390_sthyi(), necessitating
           the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           The s390_sthyi() system call emulates the STHYI (Store Hypervisor
           Information) instruction.  It provides hardware resource
           information for the machine and its virtualization levels.  This
           includes CPU type and capacity, as well as the machine model and
           other metrics.

           The function_code argument indicates which function to perform.
           The following code(s) are supported:

           STHYI_FC_CP_IFL_CAP
                  Return CP (Central Processor) and IFL (Integrated Facility
                  for Linux) capacity information.

           The resp_buffer argument specifies the address of a response
           buffer.  When the function_code is STHYI_FC_CP_IFL_CAP, the buffer
           must be one page (4K) in size.  If the system call returns 0, the
           response buffer will be filled with CPU capacity information.
           Otherwise, the response buffer's content is unchanged.

           The return_code argument stores the return code of the STHYI
           instruction, using one of the following values:

           0      Success.

           4      Unsupported function code.

           For further details about return_code, function_code, and
           resp_buffer, see the reference given in NOTES.

           The flags argument is provided to allow for future extensions and
           currently must be set to 0.

## [](#RETURN_VALUE)RETURN VALUE

           On success (that is: emulation succeeded), the return value of
           s390_sthyi() matches the condition code of the STHYI instructions,
           which is a value in the range [0..3].  A return value of 0
           indicates that CPU capacity information is stored in *resp_buffer.
           A return value of 3 indicates "unsupported function code" and the
           content of *resp_buffer is unchanged.  The return values 1 and 2
           are reserved.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT The value specified in resp_buffer or return_code is not a
                  valid address.

           EINVAL The value specified in flags is nonzero.

           ENOMEM Allocating memory for handling the CPU capacity information
                  failed.

           EOPNOTSUPP
                  The value specified in function_code is not valid.

## [](#STANDARDS)STANDARDS

           Linux on s390.

## [](#HISTORY)HISTORY

           Linux 4.15.

## [](#NOTES)NOTES

           For details of the STHYI instruction, see the documentation page
           ⟨https://www.ibm.com/support/knowledgecenter/SSB27U_6.3.0/com.ibm.zvm.v630.hcpb4/hcpb4sth.htm⟩.

           When the system call interface is used, the response buffer
           doesn't have to fulfill alignment requirements described in the
           STHYI instruction definition.

           The kernel caches the response (for up to one second, as of Linux
           4.16).  Subsequent system call invocations may return the cached
           response.

## [](#SEE_ALSO)SEE ALSO

           syscall(2)

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

    Linux man-pages 6.19            2026-02-08                  s390_sthyi(2)

------------------------------------------------------------------------

Pages that refer to this page: [syscalls(2)](../man2/syscalls.2.html)

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
