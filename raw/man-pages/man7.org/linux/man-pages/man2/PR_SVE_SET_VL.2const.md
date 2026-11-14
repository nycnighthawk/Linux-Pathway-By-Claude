---
{"title": "PR_SVE_SET_VL(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/PR_SVE_SET_VL.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# PR_SVE_SET_VL(2const) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [FILES](#FILES) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [CAVEATS](#CAVEATS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PR_SVE_SET_VL(2const)                               PR_SVE_SET_VL(2const)

## [](#NAME)NAME

           PR_SVE_SET_VL - set the thread's SVE vector length

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/prctl.h>  /* Definition of PR_* constants */
           #include <sys/prctl.h>

           int prctl(PR_SVE_SET_VL, unsigned long val);

## [](#DESCRIPTION)DESCRIPTION

           Configure the thread's SVE vector length, as specified by val.

           The bits of val corresponding to PR_SVE_VL_LEN_MASK must be set to
           the desired vector length in bytes.  This is interpreted as an
           upper bound: the kernel will select the greatest available vector
           length that does not exceed the value specified.  In particular,
           specifying SVE_VL_MAX (defined in <asm/sigcontext.h>) for the
           PR_SVE_VL_LEN_MASK bits requests the maximum supported vector
           length.

           In addition, the other bits of val must be set to one of the
           following combinations of flags:

           0L     Perform the change immediately.  At the next execve(2) in
                  the thread, the vector length will be reset to the value
                  configured in /proc/sys/abi/sve_default_vector_length.

           PR_SVE_VL_INHERIT
                  Perform the change immediately.  Subsequent execve(2) calls
                  will preserve the new vector length.

           PR_SVE_SET_VL_ONEXEC
                  Defer the change, so that it is performed at the next
                  execve(2) in the thread.  Further execve(2) calls will
                  reset the vector length to the value configured in /proc/
                  sys/abi/sve_default_vector_length.

           PR_SVE_SET_VL_ONEXEC | PR_SVE_VL_INHERIT
                  Defer the change, so that it is performed at the next
                  execve(2) in the thread.  Further execve(2) calls will
                  preserve the new vector length.

           In all cases, any previously pending deferred change is canceled.

           On success, a nonnegative value is returned that describes the
           selected configuration.  If PR_SVE_SET_VL_ONEXEC was included in
           val, then the configuration described by the return value will
           take effect at the next execve(2).  Otherwise, the configuration
           is already in effect when the PR_SVE_SET_VL call returns.  In
           either case, the value is encoded in the same way as the return
           value of PR_SVE_GET_VL.  Note that there is no explicit flag in
           the return value corresponding to PR_SVE_SET_VL_ONEXEC.

           The configuration (including any pending deferred change) is
           inherited across fork(2) and clone(2).

## [](#RETURN_VALUE)RETURN VALUE

           On success, PR_SVE_SET_VL returns the nonnegative value described
           above.  On error, -1 is returned, and errno is set to indicate the
           error.

## [](#ERRORS)ERRORS

           EINVAL SVE is not available on this platform.

           EINVAL The value in the bits of val corresponding to
                  PR_SVE_VL_LEN_MASK is outside the range [SVE_VL_MIN,
                  SVE_VL_MAX] or is not a multiple of 16.

           EINVAL The other bits of val are invalid or unsupported.

## [](#FILES)FILES

           /proc/sys/abi/sve_default_vector_length

## [](#STANDARDS)STANDARDS

           Linux.  arm64 only.

## [](#HISTORY)HISTORY

           Linux 4.15 (arm64).

## [](#CAVEATS)CAVEATS

           Because the compiler or run-time environment may be using SVE,
           using this call without the PR_SVE_SET_VL_ONEXEC flag may crash
           the calling process.  The conditions for using it safely are
           complex and system-dependent.  Don't use it unless you really know
           what you are doing.

## [](#SEE_ALSO)SEE ALSO

           prctl(2), PR_SVE_GET_VL(2const)

           For more information, see the kernel source file
           Documentation/arch/arm64/sve.rst.

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

    Linux man-pages 6.19            2026-02-08          PR_SVE_SET_VL(2const)

------------------------------------------------------------------------

Pages that refer to this page: [prctl(2)](../man2/prctl.2.html),  [PR_SVE_GET_VL(2const)](../man2/PR_SVE_GET_VL.2const.html)

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
