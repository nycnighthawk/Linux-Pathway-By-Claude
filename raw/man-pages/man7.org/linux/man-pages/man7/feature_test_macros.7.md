---
{"title": "feature_test_macros(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/feature_test_macros.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# feature_test_macros(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    featur..._macros(7)  Miscellaneous Information Manual featur..._macros(7)

## [](#NAME)NAME

           feature_test_macros - feature test macros

## [](#DESCRIPTION)DESCRIPTION

           Feature test macros allow the programmer to control the
           definitions that are exposed by system header files when a program
           is compiled.

           NOTE: In order to be effective, a feature test macro must be
           defined before including any header files.  This can be done
           either in the compilation command (cc -DMACRO=value) or by
           defining the macro within the source code before including any
           headers.  The requirement that the macro must be defined before
           including any header file exists because header files may freely
           include one another.  Thus, for example, in the following lines,
           defining the _GNU_SOURCE macro may have no effect because the
           header <abc.h> itself includes <xyz.h> (POSIX explicitly allows
           this):

               #include <abc.h>
               #define _GNU_SOURCE
               #include <xyz.h>

           Some feature test macros are useful for creating portable
           applications, by preventing nonstandard definitions from being
           exposed.  Other macros can be used to expose nonstandard
           definitions that are not exposed by default.

           The precise effects of each of the feature test macros described
           below can be ascertained by inspecting the <features.h> header
           file.  Note: applications do not need to directly include
           <features.h>; indeed, doing so is actively discouraged.  See
           NOTES.

       Specification of feature test macro requirements in manual pages
           When a function requires that a feature test macro is defined, the
           manual page SYNOPSIS typically includes a note of the following
           form (this example from the acct(2) manual page):

                  #include <unistd.h>

                  int acct(const char *filename);

              Feature Test Macro Requirements for glibc (see
              feature_test_macros(7)):

                  acct(): _BSD_SOURCE || (_XOPEN_SOURCE && _XOPEN_SOURCE <
                  500)

           The || means that in order to obtain the declaration of acct(2)
           from <unistd.h>, either of the following macro definitions must be
           made before including any header files:

               #define _BSD_SOURCE
               #define _XOPEN_SOURCE        /* or any value < 500 */

           Alternatively, equivalent definitions can be included in the
           compilation command:

               cc -D_BSD_SOURCE
               cc -D_XOPEN_SOURCE           # Or any value < 500

           Note that, as described below, some feature test macros are
           defined by default, so that it may not always be necessary to
           explicitly specify the feature test macro(s) shown in the
           SYNOPSIS.

           In a few cases, manual pages use a shorthand for expressing the
           feature test macro requirements (this example from readahead(2)):

               #define _GNU_SOURCE
               #define _FILE_OFFSET_BITS 64
               #include <fcntl.h>

               ssize_t readahead(int fd, off_t *offset, size_t count);

           This format is employed when the feature test macros ensure that
           the proper function declarations are visible, and the macros are
           not defined by default.

       Feature test macros understood by glibc
           The paragraphs below explain how feature test macros are handled
           in glibc 2.x, x > 0.

           First, though, a summary of a few details for the impatient:

           •  The macros that you most likely need to use in modern source
              code are _POSIX_C_SOURCE (for definitions from various versions
              of POSIX.1), _XOPEN_SOURCE (for definitions from various
              versions of SUS), _GNU_SOURCE (for GNU and/or Linux specific
              stuff), and _DEFAULT_SOURCE (to get definitions that would
              normally be provided by default).

           •  Certain macros are defined with default values.  Thus, although
              one or more macros may be indicated as being required in the
              SYNOPSIS of a man page, it may not be necessary to define them
              explicitly.  Full details of the defaults are given later in
              this man page.

           glibc understands the following feature test macros:

           __STRICT_ANSI__
                  ISO Standard C.  This macro is implicitly defined by gcc(1)
                  when invoked with, for example, the -std=c99 or -ansi flag.

           _POSIX_C_SOURCE
                  Defining this macro causes header files to expose
                  definitions conforming to the following standards,
                  depending on the value.

                  >= 1   POSIX.1-1990.  POSIX.1-1990 implies ISO C90.

                  >= 2   POSIX.2-1992.

                  >= 199309L
                         POSIX.1b (real-time extensions).

                  199506L  (since glibc 2.1)
                         POSIX.1c (threads).

                  200112L  (since glibc 2.3.3)
                         POSIX.1-2001 (excluding the XSI extension).
                         POSIX.1-2001 implies ISO C99.

                  200809L  (since glibc 2.10)
                         POSIX.1-2008 (excluding the XSI extension).
                         POSIX.1-2008 implies ISO C99.

           _POSIX_SOURCE  [[deprecated]]
                  Equivalent to -D_POSIX_C_SOURCE=1.

           _XOPEN_SOURCE
                  Defining this macro causes header files to expose
                  definitions conforming to the following standards,
                  depending on the value.

                  1      POSIX.1, POSIX.2, XPG4.

                  500    SUSv2 (Issue 5).

                  600  (since glibc 2.2)
                         SUSv3 (Issue 6).  SUSv3 is POSIX.1-2001 plus the XSI
                         extension.

                  700  (since glibc 2.10)
                         SUSv4 (Issue 7).  SUSv4 is POSIX.1-2008 plus the XSI
                         extension.

           _XOPEN_SOURCE_EXTENDED  [[deprecated]]
                  Defining this macro causes header files to expose
                  definitions conforming to SUSv1.

           _ISOCxx_SOURCE
                  Defining one of these macros causes header files to expose
                  definitions conforming to corresponding version of the ISO
                  C standard.

                  They should not be defined by programmers.  Instead, the
                  language version should be specified with the corresponding
                  compiler flag.

                  _ISOC99_SOURCE  (since glibc 2.1.3)
                         C99.  Use -std=c99 or -std=gnu99 instead.

                  _ISOC11_SOURCE  (since glibc 2.16)
                         C11.  Use -std=c11 or -std=gnu11 instead.

                  _ISOC23_SOURCE  (since glibc 2.40)
                  _ISOC2X_SOURCE  (since glibc 2.31)  [[deprecated]]
                         C23.  Use -std=c23 or -std=gnu23 instead.  Exposes
                         declarations consistent with the ISO C23 standard.

           _LARGEFILE64_SOURCE  [[deprecated]]
                  Expose definitions for the alternative API specified by the
                  LFS (Large File Summit) as a "transitional extension" to
                  the Single UNIX Specification.  (See
                  ⟨http://opengroup.org/platform/lfs.html⟩.)  The alternative
                  API consists of a set of new objects (i.e., functions and
                  types) whose names are suffixed with "64" (e.g., off64_t
                  versus off_t, lseek64() versus lseek(), etc.).  New
                  programs should not employ this macro; instead
                  _FILE_OFFSET_BITS=64 should be employed.

           _LARGEFILE_SOURCE  [[deprecated]]
                  This macro was historically used to expose certain
                  functions (specifically, fseeko(3) and ftello(3)) that
                  address limitations of earlier APIs (fseek(3) and ftell(3))
                  that use long for file offsets.  These functions are now
                  part of SUSv2; use _XOPEN_SOURCE instead.  Alternatively,
                  defining _FILE_OFFSET_BITS with the value 64 also serves
                  for this.

           _FILE_OFFSET_BITS
                  Defining this macro with the value 64 automatically
                  converts references to 32-bit functions and data types
                  related to file I/O and filesystem operations into
                  references to their 64-bit counterparts.  This is useful
                  for performing I/O on large files (> 2 Gigabytes) on 32-bit
                  systems.  It is also useful when calling functions like
                  copy_file_range(2) that were added more recently and that
                  come only in 64-bit flavors.  (Defining this macro permits
                  correctly written programs to use large files with only a
                  recompilation being required.)

                  64-bit systems naturally permit file sizes greater than 2
                  Gigabytes, and on those systems this macro has no effect.

           _TIME_BITS
                  Defining this macro with the value 64 changes the width of
                  time_t(3type) to 64-bit which allows handling of timestamps
                  beyond 2038.  It is closely related to _FILE_OFFSET_BITS
                  and depending on implementation, may require it set.  This
                  macro is available as of glibc 2.34.

           _BSD_SOURCE  [[deprecated]]
                  Defining this macro with any value causes header files to
                  expose BSD-derived definitions.

                  In glibc versions up to and including 2.18, defining this
                  macro also causes BSD definitions to be preferred in some
                  situations where standards conflict, unless one or more of
                  _SVID_SOURCE, _POSIX_SOURCE, _POSIX_C_SOURCE,
                  _XOPEN_SOURCE, _XOPEN_SOURCE_EXTENDED, or _GNU_SOURCE is
                  defined, in which case BSD definitions are disfavored.
                  Since glibc 2.19, _BSD_SOURCE no longer causes BSD
                  definitions to be preferred in case of conflicts.

                  Since glibc 2.20, this macro is deprecated.  It now has the
                  same effect as defining _DEFAULT_SOURCE, but generates a
                  compile-time warning (unless _DEFAULT_SOURCE is also
                  defined).  Use _DEFAULT_SOURCE instead.  To allow code that
                  requires _BSD_SOURCE in glibc 2.19 and earlier and
                  _DEFAULT_SOURCE in glibc 2.20 and later to compile without
                  warnings, define both _BSD_SOURCE and _DEFAULT_SOURCE.

           _SVID_SOURCE  [[deprecated]]
                  Defining this macro with any value causes header files to
                  expose System V-derived definitions.  (SVID == System V
                  Interface Definition; see standards(7).)

                  Since glibc 2.20, this macro is deprecated in the same
                  fashion as _BSD_SOURCE.

           _DEFAULT_SOURCE (since glibc 2.19)
                  This macro can be defined to ensure that the "default"
                  definitions are provided even when the defaults would
                  otherwise be disabled, as happens when individual macros
                  are explicitly defined, or the compiler is invoked in one
                  of its "standard" modes (e.g., cc -std=c99).  Defining
                  _DEFAULT_SOURCE without defining other individual macros or
                  invoking the compiler in one of its "standard" modes has no
                  effect.

                  The "default" definitions comprise those required by
                  POSIX.1-2008 and ISO C99, as well as various definitions
                  originally derived from BSD and System V.  On glibc 2.19
                  and earlier, these defaults were approximately equivalent
                  to explicitly defining the following:

                      cc -D_BSD_SOURCE -D_SVID_SOURCE -D_POSIX_C_SOURCE=200809

           _ATFILE_SOURCE (since glibc 2.4)
                  Defining this macro with any value causes header files to
                  expose declarations of a range of functions with the suffix
                  "at"; see openat(2).  Since glibc 2.10, this macro is also
                  implicitly defined if _POSIX_C_SOURCE is defined with a
                  value greater than or equal to 200809L.

           _GNU_SOURCE
                  Defining this macro (with any value) implicitly defines
                  _ATFILE_SOURCE, _LARGEFILE64_SOURCE, _ISOC99_SOURCE,
                  _XOPEN_SOURCE_EXTENDED, _POSIX_SOURCE, _POSIX_C_SOURCE with
                  the value 200809L (200112L before glibc 2.10; 199506L
                  before glibc 2.5; 199309L before glibc 2.1) and
                  _XOPEN_SOURCE with the value 700 (600 before glibc 2.10;
                  500 before glibc 2.2).  In addition, various GNU-specific
                  extensions are also exposed.

                  Since glibc 2.19, defining _GNU_SOURCE also has the effect
                  of implicitly defining _DEFAULT_SOURCE.  Before glibc 2.20,
                  defining _GNU_SOURCE also had the effect of implicitly
                  defining _BSD_SOURCE and _SVID_SOURCE.

           _REENTRANT  [[deprecated]]
                  Historically, on various C libraries it was necessary to
                  define this macro in all multithreaded code.  (Some C
                  libraries may still require this.)  In glibc, this macro
                  also exposed definitions of certain reentrant functions.

                  However, glibc has been thread-safe by default for many
                  years; since glibc 2.3, the only effect of defining
                  _REENTRANT has been to enable one or two of the same
                  declarations that are also enabled by defining
                  _POSIX_C_SOURCE with a value of 199506L or greater.

                  _REENTRANT is now obsolete.  In glibc 2.25 and later,
                  defining _REENTRANT is equivalent to defining
                  _POSIX_C_SOURCE with the value 199506L.  If a higher POSIX
                  conformance level is selected by any other means (such as
                  _POSIX_C_SOURCE itself, _XOPEN_SOURCE, _DEFAULT_SOURCE, or
                  _GNU_SOURCE), then defining _REENTRANT has no effect.

                  This macro is automatically defined if one compiles with
                  cc -pthread.

           _THREAD_SAFE  [[deprecated]]
                  Synonym for _REENTRANT, provided for compatibility with
                  some other implementations.

           _FORTIFY_SOURCE (since glibc 2.3.4)
                  Defining this macro causes some lightweight checks to be
                  performed to detect some buffer overflow errors when
                  employing various string and memory manipulation functions
                  (for example, memcpy(3), memset(3), stpcpy(3), strcpy(3),
                  strncpy(3), strcat(3), strncat(3), sprintf(3), snprintf(3),
                  vsprintf(3), vsnprintf(3), gets(3), and wide character
                  variants thereof).  For some functions, argument
                  consistency is checked; for example, a check is made that
                  open(2) has been supplied with a mode argument when the
                  specified flags include O_CREAT.  Not all problems are
                  detected, just some common cases.

                  If _FORTIFY_SOURCE is set to 1, with compiler optimization
                  level 1 (gcc -O1) and above, checks that shouldn't change
                  the behavior of conforming programs are performed.  With
                  _FORTIFY_SOURCE set to 2, some more checking is added, but
                  some conforming programs might fail.

                  Some of the checks can be performed at compile time (via
                  macros logic implemented in header files), and result in
                  compiler warnings; other checks take place at run time, and
                  result in a run-time error if the check fails.

                  With _FORTIFY_SOURCE set to 3, additional checking is added
                  to intercept some function calls used with an argument of
                  variable size where the compiler can deduce an upper bound
                  for its value.  For example, a program where malloc(3)'s
                  size argument is variable can now be fortified.

                  Use of this macro requires compiler support, available
                  since gcc 4.0 and clang 2.6.  Use of _FORTIFY_SOURCE set to
                  3 requires gcc 12.0 or later, or clang 9.0 or later, in
                  conjunction with glibc 2.33 or later.

       Default definitions, implicit definitions, and combining definitions
           If no feature test macros are explicitly defined, then the
           following feature test macros are defined by default: _BSD_SOURCE
           (in glibc 2.19 and earlier), _SVID_SOURCE (in glibc 2.19 and
           earlier), _DEFAULT_SOURCE (since glibc 2.19), _POSIX_SOURCE, and
           _POSIX_C_SOURCE=200809L (200112L before glibc 2.10; 199506L before
           glibc 2.4; 199309L before glibc 2.1).

           If any of __STRICT_ANSI__, _ISOC99_SOURCE, _ISOC11_SOURCE (since
           glibc 2.18), _ISOC23_SOURCE (since glibc 2.40), _POSIX_SOURCE,
           _POSIX_C_SOURCE, _XOPEN_SOURCE, _XOPEN_SOURCE_EXTENDED (in glibc
           2.11 and earlier), _BSD_SOURCE (in glibc 2.19 and earlier), or
           _SVID_SOURCE (in glibc 2.19 and earlier) is explicitly defined,
           then _BSD_SOURCE, _SVID_SOURCE, and _DEFAULT_SOURCE are not
           defined by default.

## [](#STANDARDS)STANDARDS

           POSIX.1 specifies _POSIX_C_SOURCE, _POSIX_SOURCE, and
           _XOPEN_SOURCE.

           _FILE_OFFSET_BITS is not specified by any standard, but is
           employed on some other implementations.

           _BSD_SOURCE, _SVID_SOURCE, _DEFAULT_SOURCE, _ATFILE_SOURCE,
           _GNU_SOURCE, _FORTIFY_SOURCE, _REENTRANT, and _THREAD_SAFE are
           specific to glibc.

## [](#HISTORY)HISTORY

           _XOPEN_SOURCE_EXTENDED was specified by XPG4v2 (aka SUSv1), but is
           not present in SUSv2 and later.

## [](#NOTES)NOTES

           <features.h> is a Linux/glibc-specific header file.  Other systems
           have an analogous file, but typically with a different name.  This
           header file is automatically included by other header files as
           required: it is not necessary to explicitly include it in order to
           employ feature test macros.

           According to which of the above feature test macros are defined,
           <features.h> internally defines various other macros that are
           checked by other glibc header files.  These macros have names
           prefixed by two underscores (e.g., __USE_MISC).  Programs should
           never define these macros directly: instead, the appropriate
           feature test macro(s) from the list above should be employed.

## [](#EXAMPLES)EXAMPLES

           The program below can be used to explore how the various feature
           test macros are set depending on the glibc version and what
           feature test macros are explicitly set.  The following shell
           session, on a system with glibc 2.10, shows some examples of what
           we would see:

               $ cc ftm.c
               $ ./a.out
               _POSIX_SOURCE defined
               _POSIX_C_SOURCE defined: 200809L
               _BSD_SOURCE defined
               _SVID_SOURCE defined
               _ATFILE_SOURCE defined
               $ cc -D_XOPEN_SOURCE=500 ftm.c
               $ ./a.out
               _POSIX_SOURCE defined
               _POSIX_C_SOURCE defined: 199506L
               _XOPEN_SOURCE defined: 500
               $ cc -D_GNU_SOURCE ftm.c
               $ ./a.out
               _POSIX_SOURCE defined
               _POSIX_C_SOURCE defined: 200809L
               _ISOC99_SOURCE defined
               _XOPEN_SOURCE defined: 700
               _XOPEN_SOURCE_EXTENDED defined
               _LARGEFILE64_SOURCE defined
               _BSD_SOURCE defined
               _SVID_SOURCE defined
               _ATFILE_SOURCE defined
               _GNU_SOURCE defined

       Program source

           /* ftm.c */

           #include <stdint.h>
           #include <stdio.h>
           #include <unistd.h>
           #include <stdlib.h>

           int
           main(int argc, char *argv[])
           {
           #ifdef _POSIX_SOURCE
               printf("_POSIX_SOURCE defined\n");
           #endif

           #ifdef _POSIX_C_SOURCE
               printf("_POSIX_C_SOURCE defined: %jdL\n",
                       (intmax_t) _POSIX_C_SOURCE);
           #endif

           #ifdef _ISOC99_SOURCE
               printf("_ISOC99_SOURCE defined\n");
           #endif

           #ifdef _ISOC11_SOURCE
               printf("_ISOC11_SOURCE defined\n");
           #endif

           #ifdef _ISOC23_SOURCE
               printf("_ISOC23_SOURCE defined\n");
           #endif

           #ifdef _XOPEN_SOURCE
               printf("_XOPEN_SOURCE defined: %d\n", _XOPEN_SOURCE);
           #endif

           #ifdef _XOPEN_SOURCE_EXTENDED
               printf("_XOPEN_SOURCE_EXTENDED defined\n");
           #endif

           #ifdef _LARGEFILE64_SOURCE
               printf("_LARGEFILE64_SOURCE defined\n");
           #endif

           #ifdef _FILE_OFFSET_BITS
               printf("_FILE_OFFSET_BITS defined: %d\n", _FILE_OFFSET_BITS);
           #endif

           #ifdef _TIME_BITS
               printf("_TIME_BITS defined: %d\n", _TIME_BITS);
           #endif

           #ifdef _BSD_SOURCE
               printf("_BSD_SOURCE defined\n");
           #endif

           #ifdef _SVID_SOURCE
               printf("_SVID_SOURCE defined\n");
           #endif

           #ifdef _DEFAULT_SOURCE
               printf("_DEFAULT_SOURCE defined\n");
           #endif

           #ifdef _ATFILE_SOURCE
               printf("_ATFILE_SOURCE defined\n");
           #endif

           #ifdef _GNU_SOURCE
               printf("_GNU_SOURCE defined\n");
           #endif

           #ifdef _REENTRANT
               printf("_REENTRANT defined\n");
           #endif

           #ifdef _THREAD_SAFE
               printf("_THREAD_SAFE defined\n");
           #endif

           #ifdef _FORTIFY_SOURCE
               printf("_FORTIFY_SOURCE defined\n");
           #endif

               exit(EXIT_SUCCESS);
           }

## [](#SEE_ALSO)SEE ALSO

           libc(7), standards(7), system_data_types(7)

           The section "Feature Test Macros" under info libc.

           /usr/include/features.h

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

    Linux man-pages 6.19            2026-06-24            featur..._macros(7)

------------------------------------------------------------------------

Pages that refer to this page: [access(2)](../man2/access.2.html),  [acct(2)](../man2/acct.2.html),  [brk(2)](../man2/brk.2.html),  [chdir(2)](../man2/chdir.2.html),  [chmod(2)](../man2/chmod.2.html),  [chown(2)](../man2/chown.2.html),  [chroot(2)](../man2/chroot.2.html),  [clock_getres(2)](../man2/clock_getres.2.html),  [clock_nanosleep(2)](../man2/clock_nanosleep.2.html),  [fcntl(2)](../man2/fcntl.2.html),  [fsync(2)](../man2/fsync.2.html),  [futimesat(2)](../man2/futimesat.2.html),  [getdomainname(2)](../man2/getdomainname.2.html),  [getgroups(2)](../man2/getgroups.2.html),  [gethostname(2)](../man2/gethostname.2.html),  [getpagesize(2)](../man2/getpagesize.2.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [getsid(2)](../man2/getsid.2.html),  [gettimeofday(2)](../man2/gettimeofday.2.html),  [intro(2)](../man2/intro.2.html),  [kill(2)](../man2/kill.2.html),  [link(2)](../man2/link.2.html),  [madvise(2)](../man2/madvise.2.html),  [mincore(2)](../man2/mincore.2.html),  [mkdir(2)](../man2/mkdir.2.html),  [mknod(2)](../man2/mknod.2.html),  [nanosleep(2)](../man2/nanosleep.2.html),  [nice(2)](../man2/nice.2.html),  [open(2)](../man2/open.2.html),  [posix_fadvise(2)](../man2/posix_fadvise.2.html),  [pread(2)](../man2/pread.2.html),  [process_vm_readv(2)](../man2/process_vm_readv.2.html),  [readlink(2)](../man2/readlink.2.html),  [readv(2)](../man2/readv.2.html),  [rename(2)](../man2/rename.2.html),  [select(2)](../man2/select.2.html),  [semop(2)](../man2/semop.2.html),  [seteuid(2)](../man2/seteuid.2.html),  [setpgid(2)](../man2/setpgid.2.html),  [setreuid(2)](../man2/setreuid.2.html),  [sigaction(2)](../man2/sigaction.2.html),  [sigaltstack(2)](../man2/sigaltstack.2.html),  [signal(2)](../man2/signal.2.html),  [sigpending(2)](../man2/sigpending.2.html),  [sigprocmask(2)](../man2/sigprocmask.2.html),  [sigsuspend(2)](../man2/sigsuspend.2.html),  [sigwaitinfo(2)](../man2/sigwaitinfo.2.html),  [stat(2)](../man2/stat.2.html),  [stime(2)](../man2/stime.2.html),  [symlink(2)](../man2/symlink.2.html),  [sync(2)](../man2/sync.2.html),  [syscall(2)](../man2/syscall.2.html),  [timer_create(2)](../man2/timer_create.2.html),  [timer_delete(2)](../man2/timer_delete.2.html),  [timer_getoverrun(2)](../man2/timer_getoverrun.2.html),  [timer_settime(2)](../man2/timer_settime.2.html),  [truncate(2)](../man2/truncate.2.html),  [unlink(2)](../man2/unlink.2.html),  [utimensat(2)](../man2/utimensat.2.html),  [vfork(2)](../man2/vfork.2.html),  [vhangup(2)](../man2/vhangup.2.html),  [wait(2)](../man2/wait.2.html),  [wait4(2)](../man2/wait4.2.html),  [a64l(3)](../man3/a64l.3.html),  [abs(3)](../man3/abs.3.html),  [acos(3)](../man3/acos.3.html),  [acosh(3)](../man3/acosh.3.html),  [addseverity(3)](../man3/addseverity.3.html),  [adjtime(3)](../man3/adjtime.3.html),  [aligned_alloc(3)](../man3/aligned_alloc.3.html),  [asin(3)](../man3/asin.3.html),  [asinh(3)](../man3/asinh.3.html),  [atan2(3)](../man3/atan2.3.html),  [atan(3)](../man3/atan.3.html),  [atanh(3)](../man3/atanh.3.html),  [atoi(3)](../man3/atoi.3.html),  [bsd_signal(3)](../man3/bsd_signal.3.html),  [cbrt(3)](../man3/cbrt.3.html),  [ceil(3)](../man3/ceil.3.html),  [cfree(3)](../man3/cfree.3.html),  [clearenv(3)](../man3/clearenv.3.html),  [clock_getcpuclockid(3)](../man3/clock_getcpuclockid.3.html),  [confstr(3)](../man3/confstr.3.html),  [copysign(3)](../man3/copysign.3.html),  [cos(3)](../man3/cos.3.html),  [cosh(3)](../man3/cosh.3.html),  [crypt(3)](../man3/crypt.3.html),  [ctermid(3)](../man3/ctermid.3.html),  [ctime(3)](../man3/ctime.3.html),  [daemon(3)](../man3/daemon.3.html),  [dirfd(3)](../man3/dirfd.3.html),  [div(3)](../man3/div.3.html),  [drand48(3)](../man3/drand48.3.html),  [drand48_r(3)](../man3/drand48_r.3.html),  [duplocale(3)](../man3/duplocale.3.html),  [dysize(3)](../man3/dysize.3.html),  [ecvt(3)](../man3/ecvt.3.html),  [ecvt_r(3)](../man3/ecvt_r.3.html),  [endian(3)](../man3/endian.3.html),  [erf(3)](../man3/erf.3.html),  [erfc(3)](../man3/erfc.3.html),  [exec(3)](../man3/exec.3.html),  [\_exit(3)](../man3/_exit.3.html),  [exp2(3)](../man3/exp2.3.html),  [exp(3)](../man3/exp.3.html),  [expm1(3)](../man3/expm1.3.html),  [fabs(3)](../man3/fabs.3.html),  [fdim(3)](../man3/fdim.3.html),  [fexecve(3)](../man3/fexecve.3.html),  [ffs(3)](../man3/ffs.3.html),  [fgetc(3)](../man3/fgetc.3.html),  [fgetgrent(3)](../man3/fgetgrent.3.html),  [fgetpwent(3)](../man3/fgetpwent.3.html),  [fileno(3)](../man3/fileno.3.html),  [finite(3)](../man3/finite.3.html),  [flockfile(3)](../man3/flockfile.3.html),  [floor(3)](../man3/floor.3.html),  [fma(3)](../man3/fma.3.html),  [fmax(3)](../man3/fmax.3.html),  [fmemopen(3)](../man3/fmemopen.3.html),  [fmin(3)](../man3/fmin.3.html),  [fmod(3)](../man3/fmod.3.html),  [fopen(3)](../man3/fopen.3.html),  [fpclassify(3)](../man3/fpclassify.3.html),  [frexp(3)](../man3/frexp.3.html),  [fseeko(3)](../man3/fseeko.3.html),  [ftw(3)](../man3/ftw.3.html),  [futimes(3)](../man3/futimes.3.html),  [fwide(3)](../man3/fwide.3.html),  [gamma(3)](../man3/gamma.3.html),  [gcvt(3)](../man3/gcvt.3.html),  [getaddrinfo(3)](../man3/getaddrinfo.3.html),  [getcwd(3)](../man3/getcwd.3.html),  [getdate(3)](../man3/getdate.3.html),  [getdirentries(3)](../man3/getdirentries.3.html),  [getdtablesize(3)](../man3/getdtablesize.3.html),  [getentropy(3)](../man3/getentropy.3.html),  [getenv(3)](../man3/getenv.3.html),  [getgrent(3)](../man3/getgrent.3.html),  [getgrent_r(3)](../man3/getgrent_r.3.html),  [getgrnam(3)](../man3/getgrnam.3.html),  [getgrouplist(3)](../man3/getgrouplist.3.html),  [gethostbyname(3)](../man3/gethostbyname.3.html),  [gethostid(3)](../man3/gethostid.3.html),  [getline(3)](../man3/getline.3.html),  [getloadavg(3)](../man3/getloadavg.3.html),  [getlogin(3)](../man3/getlogin.3.html),  [getmntent(3)](../man3/getmntent.3.html),  [getnameinfo(3)](../man3/getnameinfo.3.html),  [getnetent_r(3)](../man3/getnetent_r.3.html),  [getopt(3)](../man3/getopt.3.html),  [getpass(3)](../man3/getpass.3.html),  [getprotoent_r(3)](../man3/getprotoent_r.3.html),  [getpwent(3)](../man3/getpwent.3.html),  [getpwent_r(3)](../man3/getpwent_r.3.html),  [getpwnam(3)](../man3/getpwnam.3.html),  [getrpcent_r(3)](../man3/getrpcent_r.3.html),  [gets(3)](../man3/gets.3.html),  [getservent_r(3)](../man3/getservent_r.3.html),  [getspnam(3)](../man3/getspnam.3.html),  [getsubopt(3)](../man3/getsubopt.3.html),  [getusershell(3)](../man3/getusershell.3.html),  [getutent(3)](../man3/getutent.3.html),  [getw(3)](../man3/getw.3.html),  [grantpt(3)](../man3/grantpt.3.html),  [group_member(3)](../man3/group_member.3.html),  [gsignal(3)](../man3/gsignal.3.html),  [hypot(3)](../man3/hypot.3.html),  [ilogb(3)](../man3/ilogb.3.html),  [inet(3)](../man3/inet.3.html),  [inet_net_pton(3)](../man3/inet_net_pton.3.html),  [initgroups(3)](../man3/initgroups.3.html),  [insque(3)](../man3/insque.3.html),  [intro(3)](../man3/intro.3.html),  [isalpha(3)](../man3/isalpha.3.html),  [isfdtype(3)](../man3/isfdtype.3.html),  [isgreater(3)](../man3/isgreater.3.html),  [iswblank(3)](../man3/iswblank.3.html),  [j0(3)](../man3/j0.3.html),  [killpg(3)](../man3/killpg.3.html),  [ldexp(3)](../man3/ldexp.3.html),  [lgamma(3)](../man3/lgamma.3.html),  [lockf(3)](../man3/lockf.3.html),  [log10(3)](../man3/log10.3.html),  [log1p(3)](../man3/log1p.3.html),  [log2(3)](../man3/log2.3.html),  [log(3)](../man3/log.3.html),  [logb(3)](../man3/logb.3.html),  [lrint(3)](../man3/lrint.3.html),  [lround(3)](../man3/lround.3.html),  [malloc(3)](../man3/malloc.3.html),  [mbsnrtowcs(3)](../man3/mbsnrtowcs.3.html),  [mkdtemp(3)](../man3/mkdtemp.3.html),  [mkfifo(3)](../man3/mkfifo.3.html),  [mkstemp(3)](../man3/mkstemp.3.html),  [mktemp(3)](../man3/mktemp.3.html),  [modf(3)](../man3/modf.3.html),  [mq_receive(3)](../man3/mq_receive.3.html),  [mq_send(3)](../man3/mq_send.3.html),  [nan(3)](../man3/nan.3.html),  [newlocale(3)](../man3/newlocale.3.html),  [nextafter(3)](../man3/nextafter.3.html),  [nl_langinfo(3)](../man3/nl_langinfo.3.html),  [off_t(3type)](../man3/off_t.3type.html),  [on_exit(3)](../man3/on_exit.3.html),  [opendir(3)](../man3/opendir.3.html),  [open_memstream(3)](../man3/open_memstream.3.html),  [perror(3)](../man3/perror.3.html),  [popen(3)](../man3/popen.3.html),  [posix_fallocate(3)](../man3/posix_fallocate.3.html),  [posix_madvise(3)](../man3/posix_madvise.3.html),  [posix_memalign(3)](../man3/posix_memalign.3.html),  [posix_openpt(3)](../man3/posix_openpt.3.html),  [pow(3)](../man3/pow.3.html),  [printf(3)](../man3/printf.3.html),  [profil(3)](../man3/profil.3.html),  [psignal(3)](../man3/psignal.3.html),  [pthread_attr_setstack(3)](../man3/pthread_attr_setstack.3.html),  [pthread_cleanup_push_defer_np(3)](../man3/pthread_cleanup_push_defer_np.3.html),  [pthread_kill(3)](../man3/pthread_kill.3.html),  [pthread_mutexattr_setrobust(3)](../man3/pthread_mutexattr_setrobust.3.html),  [pthread_mutex_consistent(3)](../man3/pthread_mutex_consistent.3.html),  [pthread_rwlockattr_setkind_np(3)](../man3/pthread_rwlockattr_setkind_np.3.html),  [pthread_sigmask(3)](../man3/pthread_sigmask.3.html),  [pthread_sigqueue(3)](../man3/pthread_sigqueue.3.html),  [pthread_spin_init(3)](../man3/pthread_spin_init.3.html),  [pthread_spin_lock(3)](../man3/pthread_spin_lock.3.html),  [ptsname(3)](../man3/ptsname.3.html),  [putenv(3)](../man3/putenv.3.html),  [putpwent(3)](../man3/putpwent.3.html),  [qecvt(3)](../man3/qecvt.3.html),  [qsort(3)](../man3/qsort.3.html),  [rand(3)](../man3/rand.3.html),  [random(3)](../man3/random.3.html),  [random_r(3)](../man3/random_r.3.html),  [rcmd(3)](../man3/rcmd.3.html),  [readdir_r(3)](../man3/readdir_r.3.html),  [realpath(3)](../man3/realpath.3.html),  [remainder(3)](../man3/remainder.3.html),  [remquo(3)](../man3/remquo.3.html),  [rint(3)](../man3/rint.3.html),  [round(3)](../man3/round.3.html),  [rpmatch(3)](../man3/rpmatch.3.html),  [scalb(3)](../man3/scalb.3.html),  [scalbln(3)](../man3/scalbln.3.html),  [scandir(3)](../man3/scandir.3.html),  [scanf(3)](../man3/scanf.3.html),  [sched_getcpu(3)](../man3/sched_getcpu.3.html),  [seekdir(3)](../man3/seekdir.3.html),  [sem_wait(3)](../man3/sem_wait.3.html),  [setbuf(3)](../man3/setbuf.3.html),  [setenv(3)](../man3/setenv.3.html),  [setjmp(3)](../man3/setjmp.3.html),  [setnetgrent(3)](../man3/setnetgrent.3.html),  [siginterrupt(3)](../man3/siginterrupt.3.html),  [signbit(3)](../man3/signbit.3.html),  [significand(3)](../man3/significand.3.html),  [sigpause(3)](../man3/sigpause.3.html),  [sigqueue(3)](../man3/sigqueue.3.html),  [sigset(3)](../man3/sigset.3.html),  [sigsetops(3)](../man3/sigsetops.3.html),  [sigvec(3)](../man3/sigvec.3.html),  [sigwait(3)](../man3/sigwait.3.html),  [sin(3)](../man3/sin.3.html),  [sinh(3)](../man3/sinh.3.html),  [snprintf(3)](../man3/snprintf.3.html),  [sockatmark(3)](../man3/sockatmark.3.html),  [sprintf(3)](../man3/sprintf.3.html),  [sqrt(3)](../man3/sqrt.3.html),  [sscanf(3)](../man3/sscanf.3.html),  [stat(3type)](../man3/stat.3type.html),  [stpcpy(3)](../man3/stpcpy.3.html),  [stpncpy(3)](../man3/stpncpy.3.html),  [strcpy(3)](../man3/strcpy.3.html),  [strdup(3)](../man3/strdup.3.html),  [strerror(3)](../man3/strerror.3.html),  [strfromd(3)](../man3/strfromd.3.html),  [strncat(3)](../man3/strncat.3.html),  [strndup(3)](../man3/strndup.3.html),  [strnlen(3)](../man3/strnlen.3.html),  [strsep(3)](../man3/strsep.3.html),  [strsignal(3)](../man3/strsignal.3.html),  [strtod(3)](../man3/strtod.3.html),  [strtok_r(3)](../man3/strtok_r.3.html),  [strtol(3)](../man3/strtol.3.html),  [strtoul(3)](../man3/strtoul.3.html),  [syslog(3)](../man3/syslog.3.html),  [tan(3)](../man3/tan.3.html),  [tanh(3)](../man3/tanh.3.html),  [telldir(3)](../man3/telldir.3.html),  [tempnam(3)](../man3/tempnam.3.html),  [termios(3type)](../man3/termios.3type.html),  [tgamma(3)](../man3/tgamma.3.html),  [timegm(3)](../man3/timegm.3.html),  [timeradd(3)](../man3/timeradd.3.html),  [timespec_get(3)](../man3/timespec_get.3.html),  [time_t(3type)](../man3/time_t.3type.html),  [tm(3type)](../man3/tm.3type.html),  [tmpnam(3)](../man3/tmpnam.3.html),  [toascii(3)](../man3/toascii.3.html),  [toupper(3)](../man3/toupper.3.html),  [towlower(3)](../man3/towlower.3.html),  [towupper(3)](../man3/towupper.3.html),  [trunc(3)](../man3/trunc.3.html),  [ttyslot(3)](../man3/ttyslot.3.html),  [tzset(3)](../man3/tzset.3.html),  [ualarm(3)](../man3/ualarm.3.html),  [unlocked_stdio(3)](../man3/unlocked_stdio.3.html),  [unlockpt(3)](../man3/unlockpt.3.html),  [uselocale(3)](../man3/uselocale.3.html),  [usleep(3)](../man3/usleep.3.html),  [valloc(3)](../man3/valloc.3.html),  [wcpcpy(3)](../man3/wcpcpy.3.html),  [wcpncpy(3)](../man3/wcpncpy.3.html),  [wcscasecmp(3)](../man3/wcscasecmp.3.html),  [wcsdup(3)](../man3/wcsdup.3.html),  [wcsnlen(3)](../man3/wcsnlen.3.html),  [wcsnrtombs(3)](../man3/wcsnrtombs.3.html),  [wordexp(3)](../man3/wordexp.3.html),  [wprintf(3)](../man3/wprintf.3.html),  [y0(3)](../man3/y0.3.html),  [environ(7)](../man7/environ.7.html),  [feature_test_macros(7)](../man7/feature_test_macros.7.html),  [libc(7)](../man7/libc.7.html),  [man-pages(7)](../man7/man-pages.7.html),  [standards(7)](../man7/standards.7.html),  [system_data_types(7)](../man7/system_data_types.7.html)

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
