---
{"title": "process-keyring(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/process-keyring.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# process-keyring(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    process-keyring(7)   Miscellaneous Information Manual  process-keyring(7)

## [](#NAME)NAME

           process-keyring - per-process shared keyring

## [](#DESCRIPTION)DESCRIPTION

           The process keyring is a keyring used to anchor keys on behalf of
           a process.  It is created only when a process requests it.  The
           process keyring has the name (description) _pid.

           A special serial number value, KEY_SPEC_PROCESS_KEYRING, is
           defined that can be used in lieu of the actual serial number of
           the calling process's process keyring.

           From the keyctl(1) utility, '@p' can be used instead of a numeric
           key ID in much the same way, but since keyctl(1) is a program run
           after forking, this is of no utility.

           A thread created using the clone(2) CLONE_THREAD flag has the same
           process keyring as the caller of clone(2).  When a new process is
           created using fork() it initially has no process keyring.  A
           process's process keyring is cleared on execve(2).  The process
           keyring is destroyed when the last thread that refers to it
           terminates.

           If a process doesn't have a process keyring when it is accessed,
           then the process keyring will be created if the keyring is to be
           modified; otherwise, the error ENOKEY results.

## [](#SEE_ALSO)SEE ALSO

           keyctl(1), keyctl(3), keyrings(7), persistent-keyring(7),
           session-keyring(7), thread-keyring(7), user-keyring(7),
           user-session-keyring(7)

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

    Linux man-pages 6.19            2026-02-08             process-keyring(7)

------------------------------------------------------------------------

Pages that refer to this page: [add_key(2)](../man2/add_key.2.html),  [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_GET_KEYRING_ID(2const)](../man2/KEYCTL_GET_KEYRING_ID.2const.html),  [KEYCTL_SET_REQKEY_KEYRING(2const)](../man2/KEYCTL_SET_REQKEY_KEYRING.2const.html),  [request_key(2)](../man2/request_key.2.html),  [keyrings(7)](../man7/keyrings.7.html),  [keyutils(7)](../man7/keyutils.7.html),  [persistent-keyring(7)](../man7/persistent-keyring.7.html),  [session-keyring(7)](../man7/session-keyring.7.html),  [thread-keyring(7)](../man7/thread-keyring.7.html),  [user-keyring(7)](../man7/user-keyring.7.html),  [user-session-keyring(7)](../man7/user-session-keyring.7.html)

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
