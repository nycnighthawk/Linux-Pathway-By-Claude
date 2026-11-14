---
{"title": "PR_SET_FP_MODE(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/pr_set_fp_mode.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SET_FP_MODE(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SET_FP_MODE(2const)                             PR_SET_FP_MODE(2const)

## [](#NAME)NAME

           PR_SET_FP_MODE - set the floating point mode of the calling
           process

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SET_FP_MODE, unsigned long mode);

## [](#DESCRIPTION)DESCRIPTION

           On the MIPS architecture, user-space code can be built using an
           ABI which permits linking with code that has more restrictive
           floating-point (FP) requirements.  For example, user-space code
           may be built to target the O32 FPXX ABI and linked with code built
           for either one of the more restrictive FP32 or FP64 ABIs.  When
           more restrictive code is linked in, the overall requirement for
           the process is to use the more restrictive floating-point mode.

           Because the kernel has no means of knowing in advance which mode
           the process should be executed in, and because these restrictions
           can change over the lifetime of the process, the PR_SET_FP_MODE
           operation is provided to allow control of the floating-point mode
           from user space.

           The mode argument is a bit mask describing the floating-point mode
           used:

           PR_FP_MODE_FR
                  When this bit is unset (so called FR=0 or FR0 mode), the 32
                  floating-point registers are 32 bits wide, and 64-bit
                  registers are represented as a pair of registers (even- and
                  odd- numbered, with the even-numbered register containing
                  the lower 32 bits, and the odd-numbered register containing
                  the higher 32 bits).

                  When this bit is set (on supported hardware), the 32
                  floating-point registers are 64 bits wide (so called FR=1
                  or FR1 mode).  Note that modern MIPS implementations (MIPS
                  R6 and newer) support FR=1 mode only.

                  Applications that use the O32 FP32 ABI can operate only
                  when this bit is unset (FR=0; or they can be used with FRE
                  enabled, see below).  Applications that use the O32 FP64
                  ABI (and the O32 FP64A ABI, which exists to provide the
                  ability to operate with existing FP32 code; see below) can
                  operate only when this bit is set (FR=1).  Applications
                  that use the O32 FPXX ABI can operate with either FR=0 or
                  FR=1.

           PR_FP_MODE_FRE
                  Enable emulation of 32-bit floating-point mode.  When this
                  mode is enabled, it emulates 32-bit floating-point
                  operations by raising a reserved-instruction exception on
                  every instruction that uses 32-bit formats and the kernel
                  then handles the instruction in software.  (The problem
                  lies in the discrepancy of handling odd-numbered registers
                  which are the high 32 bits of 64-bit registers with even
                  numbers in FR=0 mode and the lower 32-bit parts of odd-
                  numbered 64-bit registers in FR=1 mode.)  Enabling this bit
                  is necessary when code with the O32 FP32 ABI should operate
                  with code with compatible the O32 FPXX or O32 FP64A ABIs
                  (which require FR=1 FPU mode) or when it is executed on
                  newer hardware (MIPS R6 onwards) which lacks FR=0 mode
                  support when a binary with the FP32 ABI is used.

                  Note that this mode makes sense only when the FPU is in
                  64-bit mode (FR=1).

                  Note that the use of emulation inherently has a significant
                  performance hit and should be avoided if possible.

           In the N32/N64 ABI, 64-bit floating-point mode is always used, so
           FPU emulation is not required and the FPU always operates in FR=1
           mode.

           This operation is mainly intended for use by the dynamic linker
           (ld.so(8)).

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#ERRORS)ERRORS

           EOPNOTSUPP
                  mode has an invalid or unsupported value.

## [](#STANDARDS)STANDARDS

           Linux.  MIPS only.

## [](#HISTORY)HISTORY

           Linux 4.0 (MIPS).

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_GET_FP_MODE(2const)

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

    Linux man-pages 6.19            2026-02-08         PR_SET_FP_MODE(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_GET_FP_MODE(2const)](../man2/PR_GET_FP_MODE.2const.html)

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
