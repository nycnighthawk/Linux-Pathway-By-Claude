---
{"title": "session-keyring(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/session-keyring.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# session-keyring(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    session-keyring(7)   Miscellaneous Information Manual  session-keyring(7)

## [](#NAME)NAME

           session-keyring - session shared process keyring

## [](#DESCRIPTION)DESCRIPTION

           The session keyring is a keyring used to anchor keys on behalf of
           a process.  It is typically created by pam_keyinit(8) when a user
           logs in and a link will be added that refers to the
           user-keyring(7).  Optionally, PAM(7) may revoke the session
           keyring on logout.  (In typical configurations, PAM does do this
           revocation.)  The session keyring has the name (description) _ses.

           A special serial number value, KEY_SPEC_SESSION_KEYRING, is
           defined that can be used in lieu of the actual serial number of
           the calling process's session keyring.

           From the keyctl(1) utility, '@s' can be used instead of a numeric
           key ID in much the same way.

           A process's session keyring is inherited across clone(2), fork(2),
           and vfork(2).  The session keyring is preserved across execve(2),
           even when the executable is set-user-ID or set-group-ID or has
           capabilities.  The session keyring is destroyed when the last
           process that refers to it exits.

           If a process doesn't have a session keyring when it is accessed,
           then, under certain circumstances, the user-session-keyring(7)
           will be attached as the session keyring and under others a new
           session keyring will be created.  (See user-session-keyring(7) for
           further details.)

       Special operations
           The keyutils library provides the following special operations for
           manipulating session keyrings:

           keyctl_join_session_keyring(3)
                  This operation allows the caller to change the session
                  keyring that it subscribes to.  The caller can join an
                  existing keyring with a specified name (description),
                  create a new keyring with a given name, or ask the kernel
                  to create a new "anonymous" session keyring with the name
                  "_ses".  (This function is an interface to the keyctl(2)
                  KEYCTL_JOIN_SESSION_KEYRING operation.)

           keyctl_session_to_parent(3)
                  This operation allows the caller to make the parent
                  process's session keyring to the same as its own.  For this
                  to succeed, the parent process must have identical security
                  attributes and must be single threaded.  (This function is
                  an interface to the keyctl(2) KEYCTL_SESSION_TO_PARENT
                  operation.)

           These operations are also exposed through the keyctl(1) utility
           as:

               keyctl session
               keyctl session - [<prog> <arg1> <arg2> ...]
               keyctl session <name> [<prog> <arg1> <arg2> ...]

           and:

               keyctl new_session

## [](#SEE_ALSO)SEE ALSO

           keyctl(1), keyctl(3), keyctl_join_session_keyring(3),
           keyctl_session_to_parent(3), keyrings(7), PAM(7),
           persistent-keyring(7), process-keyring(7), thread-keyring(7),
           user-keyring(7), user-session-keyring(7), pam_keyinit(8)

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

    Linux man-pages 6.19            2026-02-08             session-keyring(7)

------------------------------------------------------------------------

Pages that refer to this page: [add_key(2)](../man2/add_key.2.html),  [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_GET_KEYRING_ID(2const)](../man2/KEYCTL_GET_KEYRING_ID.2const.html),  [KEYCTL_SET_REQKEY_KEYRING(2const)](../man2/KEYCTL_SET_REQKEY_KEYRING.2const.html),  [request_key(2)](../man2/request_key.2.html),  [keyctl_join_session_keyring(3)](../man3/keyctl_join_session_keyring.3.html),  [keyctl_session_to_parent(3)](../man3/keyctl_session_to_parent.3.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [keyrings(7)](../man7/keyrings.7.html),  [keyutils(7)](../man7/keyutils.7.html),  [persistent-keyring(7)](../man7/persistent-keyring.7.html),  [process-keyring(7)](../man7/process-keyring.7.html),  [thread-keyring(7)](../man7/thread-keyring.7.html),  [user-keyring(7)](../man7/user-keyring.7.html),  [user-session-keyring(7)](../man7/user-session-keyring.7.html),  [pam_keyinit(8)](../man8/pam_keyinit.8.html)

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
