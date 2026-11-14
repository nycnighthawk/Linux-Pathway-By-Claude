---
{"title": "arch_prctl(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/arch_prctl.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# arch_prctl(2) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                    |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    arch_prctl(2)              System Calls Manual              arch_prctl(2)

## [](#NAME)NAME

           arch_prctl - set architecture-specific thread state

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <asm/prctl.h>        /* Definition of ARCH_* constants */
           #include <sys/syscall.h>      /* Definition of SYS_* constants */
           #include <unistd.h>

           int syscall(SYS_arch_prctl, int op, unsigned long addr);
           int syscall(SYS_arch_prctl, int op, unsigned long *addr);

           Note: glibc provides no wrapper for arch_prctl(), necessitating
           the use of syscall(2).

## [](#DESCRIPTION)DESCRIPTION

           arch_prctl() sets architecture-specific process or thread state.
           op selects an operation and passes argument addr to it; addr is
           interpreted as either an unsigned long for the "set" operations,
           or as an unsigned long *, for the "get" operations.

           Subfunctions for both x86 and x86-64 are:

           ARCH_SET_CPUID (since Linux 4.12)
                  Enable (addr != 0) or disable (addr == 0) the cpuid
                  instruction for the calling thread.  The instruction is
                  enabled by default.  If disabled, any execution of a cpuid
                  instruction will instead generate a SIGSEGV signal.  This
                  feature can be used to emulate cpuid results that differ
                  from what the underlying hardware would have produced
                  (e.g., in a paravirtualization setting).

                  The ARCH_SET_CPUID setting is preserved across fork(2) and
                  clone(2) but reset to the default (i.e., cpuid enabled) on
                  execve(2).

           ARCH_GET_CPUID (since Linux 4.12)
                  Return the setting of the flag manipulated by
                  ARCH_SET_CPUID as the result of the system call (1 for
                  enabled, 0 for disabled).  addr is ignored.

           Subfunctions for x86-64 only are:

           ARCH_SET_FS
                  Set the 64-bit base for the FS register to addr.

           ARCH_GET_FS
                  Return the 64-bit base value for the FS register of the
                  calling thread in the unsigned long pointed to by addr.

           ARCH_SET_GS
                  Set the 64-bit base for the GS register to addr.

           ARCH_GET_GS
                  Return the 64-bit base value for the GS register of the
                  calling thread in the unsigned long pointed to by addr.

## [](#RETURN_VALUE)RETURN VALUE

           On success, arch_prctl() returns 0; on error, -1 is returned, and
           errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EFAULT addr points to an unmapped address or is outside the
                  process address space.

           EINVAL op is not a valid operation.

           ENODEV ARCH_SET_CPUID was requested, but the underlying hardware
                  does not support CPUID faulting.

           EPERM  addr is outside the process address space.

## [](#STANDARDS)STANDARDS

           Linux/x86-64.

## [](#NOTES)NOTES

           arch_prctl() is supported only on Linux/x86-64 for 64-bit programs
           currently.

           The 64-bit base changes when a new 32-bit segment selector is
           loaded.

           ARCH_SET_GS is disabled in some kernels.

           Context switches for 64-bit segment bases are rather expensive.
           As an optimization, if a 32-bit TLS base address is used,
           arch_prctl() may use a real TLS entry as if set_thread_area(2) had
           been called, instead of manipulating the segment base register
           directly.  Memory in the first 2 GB of address space can be
           allocated by using mmap(2) with the MAP_32BIT flag.

           Because of the aforementioned optimization, using arch_prctl() and
           set_thread_area(2) in the same thread is dangerous, as they may
           overwrite each other's TLS entries.

           FS may be already used by the threading library.  Programs that
           use ARCH_SET_FS directly are very likely to crash.

## [](#SEE_ALSO)SEE ALSO

           mmap(2), modify_ldt(2), prctl(2), set_thread_area(2)

           AMD X86-64 Programmer's manual

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

    Linux man-pages 6.19            2026-02-08                  arch_prctl(2)

------------------------------------------------------------------------

Pages that refer to this page: [clone(2)](../man2/clone.2.html),  [modify_ldt(2)](../man2/modify_ldt.2.html),  [set_thread_area(2)](../man2/set_thread_area.2.html),  [syscalls(2)](../man2/syscalls.2.html)

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
