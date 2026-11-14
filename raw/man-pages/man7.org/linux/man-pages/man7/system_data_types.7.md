---
{"title": "system_data_types(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/system_data_types.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# system_data_types(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    system_data_types(7) Miscellaneous Information Manualsystem_data_types(7)

## [](#NAME)NAME

           system_data_types - overview of system data types

## [](#DESCRIPTION)DESCRIPTION

           siginfo_t
                  Include: <signal.h>.  Alternatively, <sys/wait.h>.

                  typedef struct {
                      int      si_signo;  /* Signal number */
                      int      si_code;   /* Signal code */
                      pid_t    si_pid;    /* Sending process ID */
                      uid_t    si_uid;    /* Real user ID of sending process */
                      void    *si_addr;   /* Memory location which caused fault */
                      int      si_status; /* Exit value or signal */
                      union sigval si_value;  /* Signal value */
                  } siginfo_t;

                  Information associated with a signal.  For further details
                  on this structure (including additional, Linux-specific
                  fields), see sigaction(2).

                  Conforming to: POSIX.1-2001 and later.

                  See also: pidfd_send_signal(2), rt_sigqueueinfo(2),
                  sigaction(2), sigwaitinfo(2), psiginfo(3)

           sigset_t
                  Include: <signal.h>.  Alternatively, <spawn.h>, or
                  <sys/select.h>.

                  This is a type that represents a set of signals.  According
                  to POSIX, this shall be an integer or structure type.

                  Conforming to: POSIX.1-2001 and later.

                  See also: epoll_pwait(2), ppoll(2), pselect(2),
                  sigaction(2), signalfd(2), sigpending(2), sigprocmask(2),
                  sigsuspend(2), sigwaitinfo(2), signal(7)

## [](#NOTES)NOTES

           The structures described in this manual page shall contain, at
           least, the members shown in their definition, in no particular
           order.

           Most of the integer types described in this page don't have a
           corresponding length modifier for the printf(3) and the scanf(3)
           families of functions.  To print a value of an integer type that
           doesn't have a length modifier, it should be converted to intmax_t
           or uintmax_t by an explicit cast.  To scan into a variable of an
           integer type that doesn't have a length modifier, an intermediate
           temporary variable of type intmax_t or uintmax_t should be used.
           When copying from the temporary variable to the destination
           variable, the value could overflow.  If the type has upper and
           lower limits, the user should check that the value is within those
           limits, before actually copying the value.  The example below
           shows how these conversions should be done.

       Conventions used in this page
           In "Conforming to" we only concern ourselves with C99 and later
           and POSIX.1-2001 and later.  Some types may be specified in
           earlier versions of one of these standards, but in the interests
           of simplicity we omit details from earlier standards.

           In "Include", we first note the "primary" header(s) that define
           the type according to either the C or POSIX.1 standards.  Under
           "Alternatively", we note additional headers that the standards
           specify shall define the type.

## [](#EXAMPLES)EXAMPLES

           The program shown below scans from a string and prints a value
           stored in a variable of an integer type that doesn't have a length
           modifier.  The appropriate conversions from and to intmax_t, and
           the appropriate range checks, are used as explained in the notes
           section above.

           #include <stdint.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <sys/types.h>

           int
           main (void)
           {
               static const char *const str = "500000 us in half a second";
               suseconds_t us;
               intmax_t    tmp;

               /* Scan the number from the string into the temporary variable.  */

               sscanf(str, "%jd", &tmp);

               /* Check that the value is within the valid range of suseconds_t.  */

               if (tmp < -1 || tmp > 1000000) {
                   fprintf(stderr, "Scanned value outside valid range!\n");
                   exit(EXIT_FAILURE);
               }

               /* Copy the value to the suseconds_t variable 'us'.  */

               us = tmp;

               /* Even though suseconds_t can hold the value -1, this isn't
                  a sensible number of microseconds.  */

               if (us < 0) {
                   fprintf(stderr, "Scanned value shouldn't be negative!\n");
                   exit(EXIT_FAILURE);
               }

               /* Print the value.  */

               printf("There are %jd microseconds in half a second.\n",
                       (intmax_t) us);

               exit(EXIT_SUCCESS);
           }

## [](#SEE_ALSO)SEE ALSO

           feature_test_macros(7), standards(7)

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

    Linux man-pages 6.19            2026-02-08           system_data_types(7)

------------------------------------------------------------------------

Pages that refer to this page: [intro(2)](../man2/intro.2.html),  [intro(3)](../man3/intro.3.html),  [sigevent(3type)](../man3/sigevent.3type.html),  [credentials(7)](../man7/credentials.7.html),  [feature_test_macros(7)](../man7/feature_test_macros.7.html),  [standards(7)](../man7/standards.7.html)

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
