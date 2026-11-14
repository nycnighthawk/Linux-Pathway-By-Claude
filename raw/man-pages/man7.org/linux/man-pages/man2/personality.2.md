---
{"title": "personality(2) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/personality.2.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# personality(2) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    personality(2)             System Calls Manual             personality(2)

## [](#NAME)NAME

           personality - set the process execution domain

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/personality.h>

           int personality(unsigned long persona);

## [](#DESCRIPTION)DESCRIPTION

           Linux supports different execution domains, or personalities, for
           each process.  Among other things, execution domains tell Linux
           how to map signal numbers into signal actions.  The execution
           domain system allows Linux to provide limited support for binaries
           compiled under other UNIX-like operating systems.

           If persona is not 0xffffffff, then personality() sets the caller's
           execution domain to the value specified by persona.  Specifying
           persona as 0xffffffff provides a way of retrieving the current
           persona without changing it.

           A list of the available execution domains can be found in
           <sys/personality.h>.  The execution domain is a 32-bit value in
           which the top three bytes are set aside for flags that cause the
           kernel to modify the behavior of certain system calls so as to
           emulate historical or architectural quirks.  The least significant
           byte is a value defining the personality the kernel should assume.
           The flag values are as follows:

           ADDR_COMPAT_LAYOUT (since Linux 2.6.9)
                  With this flag set, provide legacy virtual address space
                  layout.

           ADDR_NO_RANDOMIZE (since Linux 2.6.12)
                  With this flag set, disable address-space-layout
                  randomization.

           ADDR_LIMIT_32BIT (since Linux 2.2)
                  Limit the address space to 32 bits.

           ADDR_LIMIT_3GB (since Linux 2.4.0)
                  With this flag set, use 0xc0000000 as the offset at which
                  to search a virtual memory chunk on mmap(2); otherwise use
                  0xffffe000.  Applies to 32-bit x86 processes only.

           FDPIC_FUNCPTRS (since Linux 2.6.11)
                  User-space function pointers to signal handlers point to
                  descriptors.  Applies only to ARM if BINFMT_ELF_FDPIC and
                  SuperH.

           MMAP_PAGE_ZERO (since Linux 2.4.0)
                  Map page 0 as read-only (to support binaries that depend on
                  this SVr4 behavior).

           READ_IMPLIES_EXEC (since Linux 2.6.8)
                  With this flag set, PROT_READ implies PROT_EXEC for
                  mmap(2).

           SHORT_INODE (since Linux 2.4.0)
                  No effect.

           STICKY_TIMEOUTS (since Linux 1.2.0)
                  With this flag set, select(2), pselect(2), and ppoll(2) do
                  not modify the returned timeout argument when interrupted
                  by a signal handler.

           UNAME26 (since Linux 3.1)
                  Have uname(2) report a 2.6.(40+x) version number rather
                  than a MAJOR.x version number.  Added as a stopgap measure
                  to support broken applications that could not handle the
                  kernel version-numbering switch from Linux 2.6.x to Linux
                  3.x.

           WHOLE_SECONDS (since Linux 1.2.0)
                  No effect.

           The available execution domains are:

           PER_BSD (since Linux 1.2.0)
                  BSD.  (No effects.)

           PER_HPUX (since Linux 2.4)
                  Support for 32-bit HP/UX.  This support was never complete,
                  and was dropped so that since Linux 4.0, this value has no
                  effect.

           PER_IRIX32 (since Linux 2.2)
                  IRIX 5 32-bit.  Never fully functional; support dropped in
                  Linux 2.6.27.  Implies STICKY_TIMEOUTS.

           PER_IRIX64 (since Linux 2.2)
                  IRIX 6 64-bit.  Implies STICKY_TIMEOUTS; otherwise no
                  effect.

           PER_IRIXN32 (since Linux 2.2)
                  IRIX 6 new 32-bit.  Implies STICKY_TIMEOUTS; otherwise no
                  effect.

           PER_ISCR4 (since Linux 1.2.0)
                  Implies STICKY_TIMEOUTS; otherwise no effect.

           PER_LINUX (since Linux 1.2.0)
                  Linux.

           PER_LINUX32 (since Linux 2.2)
                  uname(2) returns the name of the 32-bit architecture in the
                  machine field ("i686" instead of "x86_64", &c.).

                  Under ia64 (Itanium), processes with this personality don't
                  have the O_LARGEFILE open(2) flag forced.

                  Under 64-bit ARM, setting this personality is forbidden if
                  execve(2)ing a 32-bit process would also be forbidden (cf.
                  the allow_mismatched_32bit_el0 kernel parameter and
                  Documentation/arm64/asymmetric-32bit.rst).

           PER_LINUX32_3GB (since Linux 2.4)
                  Same as PER_LINUX32, but implies ADDR_LIMIT_3GB.

           PER_LINUX_32BIT (since Linux 2.0)
                  Same as PER_LINUX, but implies ADDR_LIMIT_32BIT.

           PER_LINUX_FDPIC (since Linux 2.6.11)
                  Same as PER_LINUX, but implies FDPIC_FUNCPTRS.

           PER_OSF4 (since Linux 2.4)
                  OSF/1 v4.  No effect since Linux 6.1, which removed a.out
                  binary support.  Before, on alpha, would clear top 32 bits
                  of iov_len in the user's buffer for compatibility with old
                  versions of OSF/1 where iov_len was defined as.  int.

           PER_OSR5 (since Linux 2.4)
                  SCO OpenServer 5.  Implies STICKY_TIMEOUTS and
                  WHOLE_SECONDS; otherwise no effect.

           PER_RISCOS (since Linux 2.3.7; macro since Linux 2.3.13)
                  Acorn RISC OS/Arthur (MIPS).  No effect.  Up to Linux 4.0,
                  would set the emulation altroot to /usr/gnemul/riscos (cf.
                  PER_SUNOS, below).  Before then, up to Linux 2.6.3, just
                  Arthur emulation.

           PER_SCOSVR3 (since Linux 1.2.0)
                  SCO UNIX System V Release 3.  Same as PER_OSR5, but also
                  implies SHORT_INODE.

           PER_SOLARIS (since Linux 2.4)
                  Solaris.  Implies STICKY_TIMEOUTS; otherwise no effect.

           PER_SUNOS (since Linux 2.4.0)
                  Sun OS.  Same as PER_BSD, but implies STICKY_TIMEOUTS.
                  Prior to Linux 2.6.26, diverted library and dynamic linker
                  searches to /usr/gnemul.  Buggy, largely unmaintained, and
                  almost entirely unused.

           PER_SVR3 (since Linux 1.2.0)
                  AT&T UNIX System V Release 3.  Implies STICKY_TIMEOUTS and
                  SHORT_INODE; otherwise no effect.

           PER_SVR4 (since Linux 1.2.0)
                  AT&T UNIX System V Release 4.  Implies STICKY_TIMEOUTS and
                  MMAP_PAGE_ZERO; otherwise no effect.

           PER_UW7 (since Linux 2.4)
                  UnixWare 7.  Implies STICKY_TIMEOUTS and MMAP_PAGE_ZERO;
                  otherwise no effect.

           PER_WYSEV386 (since Linux 1.2.0)
                  WYSE UNIX System V/386.  Implies STICKY_TIMEOUTS and
                  SHORT_INODE; otherwise no effect.

           PER_XENIX (since Linux 1.2.0)
                  XENIX.  Implies STICKY_TIMEOUTS and SHORT_INODE; otherwise
                  no effect.

## [](#RETURN_VALUE)RETURN VALUE

           On success, the previous persona is returned.  On error, -1 is
           returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           EINVAL The kernel was unable to change the personality.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 1.1.20, glibc 2.3.

## [](#SEE_ALSO)SEE ALSO

           setarch(8)

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

    Linux man-pages 6.19            2026-02-08                 personality(2)

------------------------------------------------------------------------

Pages that refer to this page: [mprotect(2)](../man2/mprotect.2.html),  [syscalls(2)](../man2/syscalls.2.html),  [proc_pid_personality(5)](../man5/proc_pid_personality.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [setarch(8)](../man8/setarch.8.html)

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
