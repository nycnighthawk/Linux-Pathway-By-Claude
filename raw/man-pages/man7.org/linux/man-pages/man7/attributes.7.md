---
{"title": "attributes(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/attributes.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# attributes(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    attributes(7)        Miscellaneous Information Manual       attributes(7)

## [](#NAME)NAME

           attributes - POSIX safety concepts

## [](#DESCRIPTION)DESCRIPTION

           Note: the text of this man page is based on the material taken
           from the "POSIX Safety Concepts" section of the GNU C Library
           manual.  Further details on the topics described here can be found
           in that manual.

           Various function manual pages include a section ATTRIBUTES that
           describes the safety of calling the function in various contexts.
           This section annotates functions with the following safety
           markings:

           MT-Safe
                  MT-Safe or Thread-Safe functions are safe to call in the
                  presence of other threads.  MT, in MT-Safe, stands for
                  Multi Thread.

                  Being MT-Safe does not imply a function is atomic, nor that
                  it uses any of the memory synchronization mechanisms POSIX
                  exposes to users.  It is even possible that calling MT-Safe
                  functions in sequence does not yield an MT-Safe
                  combination.  For example, having a thread call two MT-Safe
                  functions one right after the other does not guarantee
                  behavior equivalent to atomic execution of a combination of
                  both functions, since concurrent calls in other threads may
                  interfere in a destructive way.

                  Whole-program optimizations that could inline functions
                  across library interfaces may expose unsafe reordering, and
                  so performing inlining across the GNU C Library interface
                  is not recommended.  The documented MT-Safety status is not
                  guaranteed under whole-program optimization.  However,
                  functions defined in user-visible headers are designed to
                  be safe for inlining.

           MT-Unsafe
                  MT-Unsafe functions are not safe to call in a multithreaded
                  programs.

           Other keywords that appear in safety notes are defined in
           subsequent sections.

       Conditionally safe features
           For some features that make functions unsafe to call in certain
           contexts, there are known ways to avoid the safety problem other
           than refraining from calling the function altogether.  The
           keywords that follow refer to such features, and each of their
           definitions indicates how the whole program needs to be
           constrained in order to remove the safety problem indicated by the
           keyword.  Only when all the reasons that make a function unsafe
           are observed and addressed, by applying the documented
           constraints, does the function become safe to call in a context.

           init   Functions marked with init as an MT-Unsafe feature perform
                  MT-Unsafe initialization when they are first called.

                  Calling such a function at least once in single-threaded
                  mode removes this specific cause for the function to be
                  regarded as MT-Unsafe.  If no other cause for that remains,
                  the function can then be safely called after other threads
                  are started.

           race   Functions annotated with race as an MT-Safety issue operate
                  on objects in ways that may cause data races or similar
                  forms of destructive interference out of concurrent
                  execution.  In some cases, the objects are passed to the
                  functions by users; in others, they are used by the
                  functions to return values to users; in others, they are
                  not even exposed to users.

           const  Functions marked with const as an MT-Safety issue non-
                  atomically modify internal objects that are better regarded
                  as constant, because a substantial portion of the GNU C
                  Library accesses them without synchronization.  Unlike
                  race, which causes both readers and writers of internal
                  objects to be regarded as MT-Unsafe, this mark is applied
                  to writers only.  Writers remain MT-Unsafe to call, but the
                  then-mandatory constness of objects they modify enables
                  readers to be regarded as MT-Safe (as long as no other
                  reasons for them to be unsafe remain), since the lack of
                  synchronization is not a problem when the objects are
                  effectively constant.

                  The identifier that follows the const mark will appear by
                  itself as a safety note in readers.  Programs that wish to
                  work around this safety issue, so as to call writers, may
                  use a non-recursive read-write lock associated with the
                  identifier, and guard all calls to functions marked with
                  const followed by the identifier with a write lock, and all
                  calls to functions marked with the identifier by itself
                  with a read lock.

           sig    Functions marked with sig as a MT-Safety issue may
                  temporarily install a signal handler for internal purposes,
                  which may interfere with other uses of the signal,
                  identified after a colon.

                  This safety problem can be worked around by ensuring that
                  no other uses of the signal will take place for the
                  duration of the call.  Holding a non-recursive mutex while
                  calling all functions that use the same temporary signal;
                  blocking that signal before the call and resetting its
                  handler afterwards is recommended.

           term   Functions marked with term as an MT-Safety issue may change
                  the terminal settings in the recommended way, namely: call
                  tcgetattr(3), modify some flags, and then call
                  tcsetattr(3), this creates a window in which changes made
                  by other threads are lost.  Thus, functions marked with
                  term are MT-Unsafe.

                  It is thus advisable for applications using the terminal to
                  avoid concurrent and reentrant interactions with it, by not
                  using it in signal handlers or blocking signals that might
                  use it, and holding a lock while calling these functions
                  and interacting with the terminal.  This lock should also
                  be used for mutual exclusion with functions marked with
                  race:tcattr(fd), where fd is a file descriptor for the
                  controlling terminal.  The caller may use a single mutex
                  for simplicity, or use one mutex per terminal, even if
                  referenced by different file descriptors.

       Other safety remarks
           Additional keywords may be attached to functions, indicating
           features that do not make a function unsafe to call, but that may
           need to be taken into account in certain classes of programs:

           locale Functions annotated with locale as an MT-Safety issue read
                  from the locale object without any form of synchronization.
                  Functions annotated with locale called concurrently with
                  locale changes may behave in ways that do not correspond to
                  any of the locales active during their execution, but an
                  unpredictable mix thereof.

                  We do not mark these functions as MT-Unsafe, however,
                  because functions that modify the locale object are marked
                  with const:locale and regarded as unsafe.  Being unsafe,
                  the latter are not to be called when multiple threads are
                  running or asynchronous signals are enabled, and so the
                  locale can be considered effectively constant in these
                  contexts, which makes the former safe.

           env    Functions marked with env as an MT-Safety issue access the
                  environment with getenv(3) or similar, without any guards
                  to ensure safety in the presence of concurrent
                  modifications.

                  We do not mark these functions as MT-Unsafe, however,
                  because functions that modify the environment are all
                  marked with const:env and regarded as unsafe.  Being
                  unsafe, the latter are not to be called when multiple
                  threads are running or asynchronous signals are enabled,
                  and so the environment can be considered effectively
                  constant in these contexts, which makes the former safe.

           hostid Functions marked with hostid as an MT-Safety issue read
                  from the system-wide data structures that hold the "host
                  ID" of the machine.  These data structures cannot generally
                  be modified atomically.  Since it is expected that the
                  "host ID" will not normally change, the function that reads
                  from it (gethostid(3)) is regarded as safe, whereas the
                  function that modifies it (sethostid(3)) is marked with
                  const:hostid, indicating it may require special care if it
                  is to be called.  In this specific case, the special care
                  amounts to system-wide (not merely intra-process)
                  coordination.

           sigintr
                  Functions marked with sigintr as an MT-Safety issue access
                  the GNU C Library _sigintr internal data structure without
                  any guards to ensure safety in the presence of concurrent
                  modifications.

                  We do not mark these functions as MT-Unsafe, however,
                  because functions that modify this data structure are all
                  marked with const:sigintr and regarded as unsafe.  Being
                  unsafe, the latter are not to be called when multiple
                  threads are running or asynchronous signals are enabled,
                  and so the data structure can be considered effectively
                  constant in these contexts, which makes the former safe.

           cwd    Functions marked with cwd as an MT-Safety issue may
                  temporarily change the current working directory during
                  their execution, which may cause relative pathnames to be
                  resolved in unexpected ways in other threads or within
                  asynchronous signal or cancelation handlers.

                  This is not enough of a reason to mark so-marked functions
                  as MT-Unsafe, but when this behavior is optional (e.g.,
                  nftw(3) with FTW_CHDIR), avoiding the option may be a good
                  alternative to using full pathnames or file descriptor-
                  relative (e.g., openat(2)) system calls.

           :identifier
                  Annotations may sometimes be followed by identifiers,
                  intended to group several functions that, for example,
                  access the data structures in an unsafe way, as in race and
                  const, or to provide more specific information, such as
                  naming a signal in a function marked with sig.  It is
                  envisioned that it may be applied to lock and corrupt as
                  well in the future.

                  In most cases, the identifier will name a set of functions,
                  but it may name global objects or function arguments, or
                  identifiable properties or logical components associated
                  with them, with a notation such as, for example, :buf(arg)
                  to denote a buffer associated with the argument arg, or
                  :tcattr(fd) to denote the terminal attributes of a file
                  descriptor fd.

                  The most common use for identifiers is to provide logical
                  groups of functions and arguments that need to be protected
                  by the same synchronization primitive in order to ensure
                  safe operation in a given context.

           /condition
                  Some safety annotations may be conditional, in that they
                  only apply if a boolean expression involving arguments,
                  global variables or even the underlying kernel evaluates to
                  true.  For example, /!ps and /one_per_line indicate the
                  preceding marker only applies when argument ps is NULL, or
                  global variable one_per_line is nonzero.

                  When all marks that render a function unsafe are adorned
                  with such conditions, and none of the named conditions
                  hold, then the function can be regarded as safe.

## [](#SEE_ALSO)SEE ALSO

           pthreads(7), signal-safety(7)

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

    Linux man-pages 6.19            2026-02-08                  attributes(7)

------------------------------------------------------------------------

Pages that refer to this page: [adjtimex(2)](../man2/adjtimex.2.html),  [clock_getres(2)](../man2/clock_getres.2.html),  [eventfd(2)](../man2/eventfd.2.html),  [getrlimit(2)](../man2/getrlimit.2.html),  [getrusage(2)](../man2/getrusage.2.html),  [mmap(2)](../man2/mmap.2.html),  [sigaltstack(2)](../man2/sigaltstack.2.html),  [utimensat(2)](../man2/utimensat.2.html),  [a64l(3)](../man3/a64l.3.html),  [abort(3)](../man3/abort.3.html),  [abs(3)](../man3/abs.3.html),  [acos(3)](../man3/acos.3.html),  [acosh(3)](../man3/acosh.3.html),  [addseverity(3)](../man3/addseverity.3.html),  [adjtime(3)](../man3/adjtime.3.html),  [aio_cancel(3)](../man3/aio_cancel.3.html),  [aio_error(3)](../man3/aio_error.3.html),  [aio_fsync(3)](../man3/aio_fsync.3.html),  [aio_read(3)](../man3/aio_read.3.html),  [aio_return(3)](../man3/aio_return.3.html),  [aio_suspend(3)](../man3/aio_suspend.3.html),  [aio_write(3)](../man3/aio_write.3.html),  [aligned_alloc(3)](../man3/aligned_alloc.3.html),  [alloca(3)](../man3/alloca.3.html),  [aprintf(3)](../man3/aprintf.3.html),  [arc4random(3)](../man3/arc4random.3.html),  [argz_add(3)](../man3/argz_add.3.html),  [asin(3)](../man3/asin.3.html),  [asinh(3)](../man3/asinh.3.html),  [asprintf(3)](../man3/asprintf.3.html),  [assert(3)](../man3/assert.3.html),  [assert_perror(3)](../man3/assert_perror.3.html),  [atan2(3)](../man3/atan2.3.html),  [atan(3)](../man3/atan.3.html),  [atanh(3)](../man3/atanh.3.html),  [atexit(3)](../man3/atexit.3.html),  [atof(3)](../man3/atof.3.html),  [atoi(3)](../man3/atoi.3.html),  [backtrace(3)](../man3/backtrace.3.html),  [basename(3)](../man3/basename.3.html),  [bcopy(3)](../man3/bcopy.3.html),  [bindresvport(3)](../man3/bindresvport.3.html),  [bsd_signal(3)](../man3/bsd_signal.3.html),  [bsearch(3)](../man3/bsearch.3.html),  [btowc(3)](../man3/btowc.3.html),  [byteorder(3)](../man3/byteorder.3.html),  [bzero(3)](../man3/bzero.3.html),  [cabs(3)](../man3/cabs.3.html),  [cacos(3)](../man3/cacos.3.html),  [cacosh(3)](../man3/cacosh.3.html),  [canonicalize_file_name(3)](../man3/canonicalize_file_name.3.html),  [carg(3)](../man3/carg.3.html),  [casin(3)](../man3/casin.3.html),  [casinh(3)](../man3/casinh.3.html),  [catan(3)](../man3/catan.3.html),  [catanh(3)](../man3/catanh.3.html),  [catgets(3)](../man3/catgets.3.html),  [catopen(3)](../man3/catopen.3.html),  [cbrt(3)](../man3/cbrt.3.html),  [ccos(3)](../man3/ccos.3.html),  [ceil(3)](../man3/ceil.3.html),  [cexp(3)](../man3/cexp.3.html),  [cfmakeraw(3)](../man3/cfmakeraw.3.html),  [cfree(3)](../man3/cfree.3.html),  [cfsetspeed(3)](../man3/cfsetspeed.3.html),  [cimag(3)](../man3/cimag.3.html),  [clearenv(3)](../man3/clearenv.3.html),  [clock(3)](../man3/clock.3.html),  [clock_getcpuclockid(3)](../man3/clock_getcpuclockid.3.html),  [clog10(3)](../man3/clog10.3.html),  [clog(3)](../man3/clog.3.html),  [closedir(3)](../man3/closedir.3.html),  [confstr(3)](../man3/confstr.3.html),  [conj(3)](../man3/conj.3.html),  [copysign(3)](../man3/copysign.3.html),  [cos(3)](../man3/cos.3.html),  [cosh(3)](../man3/cosh.3.html),  [cpow(3)](../man3/cpow.3.html),  [cproj(3)](../man3/cproj.3.html),  [creal(3)](../man3/creal.3.html),  [crypt(3)](../man3/crypt.3.html),  [csin(3)](../man3/csin.3.html),  [csinh(3)](../man3/csinh.3.html),  [csqrt(3)](../man3/csqrt.3.html),  [ctan(3)](../man3/ctan.3.html),  [ctanh(3)](../man3/ctanh.3.html),  [ctermid(3)](../man3/ctermid.3.html),  [ctime(3)](../man3/ctime.3.html),  [daemon(3)](../man3/daemon.3.html),  [des_crypt(3)](../man3/des_crypt.3.html),  [difftime(3)](../man3/difftime.3.html),  [dirfd(3)](../man3/dirfd.3.html),  [div(3)](../man3/div.3.html),  [dladdr(3)](../man3/dladdr.3.html),  [dlerror(3)](../man3/dlerror.3.html),  [dlinfo(3)](../man3/dlinfo.3.html),  [dl_iterate_phdr(3)](../man3/dl_iterate_phdr.3.html),  [dlopen(3)](../man3/dlopen.3.html),  [dlsym(3)](../man3/dlsym.3.html),  [drand48(3)](../man3/drand48.3.html),  [drand48_r(3)](../man3/drand48_r.3.html),  [dysize(3)](../man3/dysize.3.html),  [ecvt(3)](../man3/ecvt.3.html),  [ecvt_r(3)](../man3/ecvt_r.3.html),  [encrypt(3)](../man3/encrypt.3.html),  [envz_add(3)](../man3/envz_add.3.html),  [erf(3)](../man3/erf.3.html),  [erfc(3)](../man3/erfc.3.html),  [err(3)](../man3/err.3.html),  [error(3)](../man3/error.3.html),  [ether_aton(3)](../man3/ether_aton.3.html),  [euidaccess(3)](../man3/euidaccess.3.html),  [exec(3)](../man3/exec.3.html),  [exit(3)](../man3/exit.3.html),  [exp10(3)](../man3/exp10.3.html),  [exp2(3)](../man3/exp2.3.html),  [exp(3)](../man3/exp.3.html),  [explicit_bzero(3)](../man3/explicit_bzero.3.html),  [expm1(3)](../man3/expm1.3.html),  [fabs(3)](../man3/fabs.3.html),  [fclose(3)](../man3/fclose.3.html),  [fcloseall(3)](../man3/fcloseall.3.html),  [fdim(3)](../man3/fdim.3.html),  [fenv(3)](../man3/fenv.3.html),  [ferror(3)](../man3/ferror.3.html),  [fexecve(3)](../man3/fexecve.3.html),  [fflush(3)](../man3/fflush.3.html),  [ffs(3)](../man3/ffs.3.html),  [fgetc(3)](../man3/fgetc.3.html),  [fgetgrent(3)](../man3/fgetgrent.3.html),  [fgetpwent(3)](../man3/fgetpwent.3.html),  [fgets(3)](../man3/fgets.3.html),  [fgetwc(3)](../man3/fgetwc.3.html),  [fgetws(3)](../man3/fgetws.3.html),  [fileno(3)](../man3/fileno.3.html),  [finite(3)](../man3/finite.3.html),  [flockfile(3)](../man3/flockfile.3.html),  [floor(3)](../man3/floor.3.html),  [fma(3)](../man3/fma.3.html),  [fmax(3)](../man3/fmax.3.html),  [fmemopen(3)](../man3/fmemopen.3.html),  [fmin(3)](../man3/fmin.3.html),  [fmod(3)](../man3/fmod.3.html),  [fmtmsg(3)](../man3/fmtmsg.3.html),  [fnmatch(3)](../man3/fnmatch.3.html),  [fopen(3)](../man3/fopen.3.html),  [fopencookie(3)](../man3/fopencookie.3.html),  [fpathconf(3)](../man3/fpathconf.3.html),  [fpclassify(3)](../man3/fpclassify.3.html),  [fpurge(3)](../man3/fpurge.3.html),  [fputwc(3)](../man3/fputwc.3.html),  [fputws(3)](../man3/fputws.3.html),  [fread(3)](../man3/fread.3.html),  [frexp(3)](../man3/frexp.3.html),  [fseek(3)](../man3/fseek.3.html),  [fseeko(3)](../man3/fseeko.3.html),  [ftime(3)](../man3/ftime.3.html),  [ftok(3)](../man3/ftok.3.html),  [fts(3)](../man3/fts.3.html),  [ftw(3)](../man3/ftw.3.html),  [futimes(3)](../man3/futimes.3.html),  [gamma(3)](../man3/gamma.3.html),  [gcvt(3)](../man3/gcvt.3.html),  [getaddrinfo(3)](../man3/getaddrinfo.3.html),  [getaddrinfo_a(3)](../man3/getaddrinfo_a.3.html),  [getauxval(3)](../man3/getauxval.3.html),  [getcontext(3)](../man3/getcontext.3.html),  [getcwd(3)](../man3/getcwd.3.html),  [getdate(3)](../man3/getdate.3.html),  [getdirentries(3)](../man3/getdirentries.3.html),  [getdtablesize(3)](../man3/getdtablesize.3.html),  [getenv(3)](../man3/getenv.3.html),  [getfsent(3)](../man3/getfsent.3.html),  [getgrent(3)](../man3/getgrent.3.html),  [getgrent_r(3)](../man3/getgrent_r.3.html),  [getgrnam(3)](../man3/getgrnam.3.html),  [getgrouplist(3)](../man3/getgrouplist.3.html),  [gethostbyname(3)](../man3/gethostbyname.3.html),  [gethostid(3)](../man3/gethostid.3.html),  [getifaddrs(3)](../man3/getifaddrs.3.html),  [getline(3)](../man3/getline.3.html),  [getloadavg(3)](../man3/getloadavg.3.html),  [getlogin(3)](../man3/getlogin.3.html),  [getmntent(3)](../man3/getmntent.3.html),  [getnameinfo(3)](../man3/getnameinfo.3.html),  [getnetent(3)](../man3/getnetent.3.html),  [getnetent_r(3)](../man3/getnetent_r.3.html),  [get_nprocs(3)](../man3/get_nprocs.3.html),  [getopt(3)](../man3/getopt.3.html),  [getopt_long(3)](../man3/getopt_long.3.html),  [getopt_long_only(3)](../man3/getopt_long_only.3.html),  [getpass(3)](../man3/getpass.3.html),  [getprotoent(3)](../man3/getprotoent.3.html),  [getprotoent_r(3)](../man3/getprotoent_r.3.html),  [getpt(3)](../man3/getpt.3.html),  [getpw(3)](../man3/getpw.3.html),  [getpwent(3)](../man3/getpwent.3.html),  [getpwent_r(3)](../man3/getpwent_r.3.html),  [getpwnam(3)](../man3/getpwnam.3.html),  [getrpcent(3)](../man3/getrpcent.3.html),  [getrpcent_r(3)](../man3/getrpcent_r.3.html),  [getrpcport(3)](../man3/getrpcport.3.html),  [gets(3)](../man3/gets.3.html),  [getservent(3)](../man3/getservent.3.html),  [getservent_r(3)](../man3/getservent_r.3.html),  [getspnam(3)](../man3/getspnam.3.html),  [getsubopt(3)](../man3/getsubopt.3.html),  [getttyent(3)](../man3/getttyent.3.html),  [getusershell(3)](../man3/getusershell.3.html),  [getutent(3)](../man3/getutent.3.html),  [getutmp(3)](../man3/getutmp.3.html),  [getw(3)](../man3/getw.3.html),  [getwchar(3)](../man3/getwchar.3.html),  [glob(3)](../man3/glob.3.html),  [gnu_get_libc_version(3)](../man3/gnu_get_libc_version.3.html),  [grantpt(3)](../man3/grantpt.3.html),  [gsignal(3)](../man3/gsignal.3.html),  [hsearch(3)](../man3/hsearch.3.html),  [hypot(3)](../man3/hypot.3.html),  [iconv(3)](../man3/iconv.3.html),  [iconv_close(3)](../man3/iconv_close.3.html),  [iconv_open(3)](../man3/iconv_open.3.html),  [if_nameindex(3)](../man3/if_nameindex.3.html),  [if_nametoindex(3)](../man3/if_nametoindex.3.html),  [ilogb(3)](../man3/ilogb.3.html),  [inet(3)](../man3/inet.3.html),  [inet_ntop(3)](../man3/inet_ntop.3.html),  [inet_pton(3)](../man3/inet_pton.3.html),  [initgroups(3)](../man3/initgroups.3.html),  [insque(3)](../man3/insque.3.html),  [isalpha(3)](../man3/isalpha.3.html),  [isatty(3)](../man3/isatty.3.html),  [isgreater(3)](../man3/isgreater.3.html),  [iswalnum(3)](../man3/iswalnum.3.html),  [iswalpha(3)](../man3/iswalpha.3.html),  [iswblank(3)](../man3/iswblank.3.html),  [iswcntrl(3)](../man3/iswcntrl.3.html),  [iswctype(3)](../man3/iswctype.3.html),  [iswdigit(3)](../man3/iswdigit.3.html),  [iswgraph(3)](../man3/iswgraph.3.html),  [iswlower(3)](../man3/iswlower.3.html),  [iswprint(3)](../man3/iswprint.3.html),  [iswpunct(3)](../man3/iswpunct.3.html),  [iswspace(3)](../man3/iswspace.3.html),  [iswupper(3)](../man3/iswupper.3.html),  [iswxdigit(3)](../man3/iswxdigit.3.html),  [j0(3)](../man3/j0.3.html),  [key_setsecret(3)](../man3/key_setsecret.3.html),  [ldexp(3)](../man3/ldexp.3.html),  [lio_listio(3)](../man3/lio_listio.3.html),  [localeconv(3)](../man3/localeconv.3.html),  [lockf(3)](../man3/lockf.3.html),  [log10(3)](../man3/log10.3.html),  [log1p(3)](../man3/log1p.3.html),  [log2(3)](../man3/log2.3.html),  [log(3)](../man3/log.3.html),  [logb(3)](../man3/logb.3.html),  [login(3)](../man3/login.3.html),  [lrint(3)](../man3/lrint.3.html),  [lround(3)](../man3/lround.3.html),  [lsearch(3)](../man3/lsearch.3.html),  [lseek64(3)](../man3/lseek64.3.html),  [makecontext(3)](../man3/makecontext.3.html),  [makedev(3)](../man3/makedev.3.html),  [mallinfo(3)](../man3/mallinfo.3.html),  [malloc(3)](../man3/malloc.3.html),  [malloc_get_state(3)](../man3/malloc_get_state.3.html),  [malloc_info(3)](../man3/malloc_info.3.html),  [malloc_stats(3)](../man3/malloc_stats.3.html),  [malloc_trim(3)](../man3/malloc_trim.3.html),  [malloc_usable_size(3)](../man3/malloc_usable_size.3.html),  [matherr(3)](../man3/matherr.3.html),  [mblen(3)](../man3/mblen.3.html),  [mbrlen(3)](../man3/mbrlen.3.html),  [mbrtowc(3)](../man3/mbrtowc.3.html),  [mbsinit(3)](../man3/mbsinit.3.html),  [mbsnrtowcs(3)](../man3/mbsnrtowcs.3.html),  [mbsrtowcs(3)](../man3/mbsrtowcs.3.html),  [mbstowcs(3)](../man3/mbstowcs.3.html),  [mbtowc(3)](../man3/mbtowc.3.html),  [mcheck(3)](../man3/mcheck.3.html),  [memalign(3)](../man3/memalign.3.html),  [memccpy(3)](../man3/memccpy.3.html),  [memchr(3)](../man3/memchr.3.html),  [memcmp(3)](../man3/memcmp.3.html),  [memcpy(3)](../man3/memcpy.3.html),  [memeq(3)](../man3/memeq.3.html),  [memfrob(3)](../man3/memfrob.3.html),  [memmem(3)](../man3/memmem.3.html),  [memmove(3)](../man3/memmove.3.html),  [mempcpy(3)](../man3/mempcpy.3.html),  [memrchr(3)](../man3/memrchr.3.html),  [memset(3)](../man3/memset.3.html),  [memset_explicit(3)](../man3/memset_explicit.3.html),  [mkdtemp(3)](../man3/mkdtemp.3.html),  [mkfifo(3)](../man3/mkfifo.3.html),  [mkstemp(3)](../man3/mkstemp.3.html),  [mktemp(3)](../man3/mktemp.3.html),  [modf(3)](../man3/modf.3.html),  [mq_close(3)](../man3/mq_close.3.html),  [mq_getattr(3)](../man3/mq_getattr.3.html),  [mq_notify(3)](../man3/mq_notify.3.html),  [mq_open(3)](../man3/mq_open.3.html),  [mq_receive(3)](../man3/mq_receive.3.html),  [mq_send(3)](../man3/mq_send.3.html),  [mq_unlink(3)](../man3/mq_unlink.3.html),  [mtrace(3)](../man3/mtrace.3.html),  [nan(3)](../man3/nan.3.html),  [nextafter(3)](../man3/nextafter.3.html),  [nextup(3)](../man3/nextup.3.html),  [nl_langinfo(3)](../man3/nl_langinfo.3.html),  [ntp_gettime(3)](../man3/ntp_gettime.3.html),  [on_exit(3)](../man3/on_exit.3.html),  [opendir(3)](../man3/opendir.3.html),  [open_memstream(3)](../man3/open_memstream.3.html),  [openpty(3)](../man3/openpty.3.html),  [perror(3)](../man3/perror.3.html),  [popen(3)](../man3/popen.3.html),  [posix_fallocate(3)](../man3/posix_fallocate.3.html),  [posix_memalign(3)](../man3/posix_memalign.3.html),  [posix_openpt(3)](../man3/posix_openpt.3.html),  [pow10(3)](../man3/pow10.3.html),  [pow(3)](../man3/pow.3.html),  [\_\_ppc_set_ppr_med(3)](../man3/__ppc_set_ppr_med.3.html),  [\_\_ppc_yield(3)](../man3/__ppc_yield.3.html),  [printf(3)](../man3/printf.3.html),  [profil(3)](../man3/profil.3.html),  [psignal(3)](../man3/psignal.3.html),  [pthread_attr_init(3)](../man3/pthread_attr_init.3.html),  [pthread_attr_setaffinity_np(3)](../man3/pthread_attr_setaffinity_np.3.html),  [pthread_attr_setdetachstate(3)](../man3/pthread_attr_setdetachstate.3.html),  [pthread_attr_setguardsize(3)](../man3/pthread_attr_setguardsize.3.html),  [pthread_attr_setinheritsched(3)](../man3/pthread_attr_setinheritsched.3.html),  [pthread_attr_setschedparam(3)](../man3/pthread_attr_setschedparam.3.html),  [pthread_attr_setschedpolicy(3)](../man3/pthread_attr_setschedpolicy.3.html),  [pthread_attr_setscope(3)](../man3/pthread_attr_setscope.3.html),  [pthread_attr_setsigmask_np(3)](../man3/pthread_attr_setsigmask_np.3.html),  [pthread_attr_setstack(3)](../man3/pthread_attr_setstack.3.html),  [pthread_attr_setstackaddr(3)](../man3/pthread_attr_setstackaddr.3.html),  [pthread_attr_setstacksize(3)](../man3/pthread_attr_setstacksize.3.html),  [pthread_cancel(3)](../man3/pthread_cancel.3.html),  [pthread_cleanup_push(3)](../man3/pthread_cleanup_push.3.html),  [pthread_create(3)](../man3/pthread_create.3.html),  [pthread_detach(3)](../man3/pthread_detach.3.html),  [pthread_equal(3)](../man3/pthread_equal.3.html),  [pthread_exit(3)](../man3/pthread_exit.3.html),  [pthread_getattr_default_np(3)](../man3/pthread_getattr_default_np.3.html),  [pthread_getattr_np(3)](../man3/pthread_getattr_np.3.html),  [pthread_getcpuclockid(3)](../man3/pthread_getcpuclockid.3.html),  [pthread_join(3)](../man3/pthread_join.3.html),  [pthread_kill(3)](../man3/pthread_kill.3.html),  [pthread_kill_other_threads_np(3)](../man3/pthread_kill_other_threads_np.3.html),  [pthread_self(3)](../man3/pthread_self.3.html),  [pthread_setaffinity_np(3)](../man3/pthread_setaffinity_np.3.html),  [pthread_setcancelstate(3)](../man3/pthread_setcancelstate.3.html),  [pthread_setconcurrency(3)](../man3/pthread_setconcurrency.3.html),  [pthread_setname_np(3)](../man3/pthread_setname_np.3.html),  [pthread_setschedparam(3)](../man3/pthread_setschedparam.3.html),  [pthread_setschedprio(3)](../man3/pthread_setschedprio.3.html),  [pthread_sigmask(3)](../man3/pthread_sigmask.3.html),  [pthread_sigqueue(3)](../man3/pthread_sigqueue.3.html),  [pthread_testcancel(3)](../man3/pthread_testcancel.3.html),  [pthread_tryjoin_np(3)](../man3/pthread_tryjoin_np.3.html),  [pthread_yield(3)](../man3/pthread_yield.3.html),  [ptsname(3)](../man3/ptsname.3.html),  [putenv(3)](../man3/putenv.3.html),  [putgrent(3)](../man3/putgrent.3.html),  [putpwent(3)](../man3/putpwent.3.html),  [puts(3)](../man3/puts.3.html),  [putwchar(3)](../man3/putwchar.3.html),  [pvalloc(3)](../man3/pvalloc.3.html),  [qecvt(3)](../man3/qecvt.3.html),  [qsort(3)](../man3/qsort.3.html),  [raise(3)](../man3/raise.3.html),  [rand(3)](../man3/rand.3.html),  [random(3)](../man3/random.3.html),  [random_r(3)](../man3/random_r.3.html),  [rawmemchr(3)](../man3/rawmemchr.3.html),  [rcmd(3)](../man3/rcmd.3.html),  [readdir(3)](../man3/readdir.3.html),  [readdir_r(3)](../man3/readdir_r.3.html),  [realpath(3)](../man3/realpath.3.html),  [re_comp(3)](../man3/re_comp.3.html),  [regex(3)](../man3/regex.3.html),  [remainder(3)](../man3/remainder.3.html),  [remove(3)](../man3/remove.3.html),  [remquo(3)](../man3/remquo.3.html),  [resolver(3)](../man3/resolver.3.html),  [rewinddir(3)](../man3/rewinddir.3.html),  [rexec(3)](../man3/rexec.3.html),  [rint(3)](../man3/rint.3.html),  [round(3)](../man3/round.3.html),  [rpc(3)](../man3/rpc.3.html),  [rpmatch(3)](../man3/rpmatch.3.html),  [rtime(3)](../man3/rtime.3.html),  [scalb(3)](../man3/scalb.3.html),  [scalbln(3)](../man3/scalbln.3.html),  [scandir(3)](../man3/scandir.3.html),  [scanf(3)](../man3/scanf.3.html),  [sched_getcpu(3)](../man3/sched_getcpu.3.html),  [seekdir(3)](../man3/seekdir.3.html),  [sem_close(3)](../man3/sem_close.3.html),  [sem_destroy(3)](../man3/sem_destroy.3.html),  [sem_getvalue(3)](../man3/sem_getvalue.3.html),  [sem_init(3)](../man3/sem_init.3.html),  [sem_open(3)](../man3/sem_open.3.html),  [sem_post(3)](../man3/sem_post.3.html),  [sem_unlink(3)](../man3/sem_unlink.3.html),  [sem_wait(3)](../man3/sem_wait.3.html),  [setaliasent(3)](../man3/setaliasent.3.html),  [setbuf(3)](../man3/setbuf.3.html),  [setenv(3)](../man3/setenv.3.html),  [setjmp(3)](../man3/setjmp.3.html),  [setlocale(3)](../man3/setlocale.3.html),  [setlogmask(3)](../man3/setlogmask.3.html),  [setnetgrent(3)](../man3/setnetgrent.3.html),  [shm_open(3)](../man3/shm_open.3.html),  [siginterrupt(3)](../man3/siginterrupt.3.html),  [signbit(3)](../man3/signbit.3.html),  [significand(3)](../man3/significand.3.html),  [sigpause(3)](../man3/sigpause.3.html),  [sigqueue(3)](../man3/sigqueue.3.html),  [sigset(3)](../man3/sigset.3.html),  [sigsetops(3)](../man3/sigsetops.3.html),  [sigvec(3)](../man3/sigvec.3.html),  [sigwait(3)](../man3/sigwait.3.html),  [sin(3)](../man3/sin.3.html),  [sincos(3)](../man3/sincos.3.html),  [sinh(3)](../man3/sinh.3.html),  [sleep(3)](../man3/sleep.3.html),  [snprintf(3)](../man3/snprintf.3.html),  [sockatmark(3)](../man3/sockatmark.3.html),  [sprintf(3)](../man3/sprintf.3.html),  [sqrt(3)](../man3/sqrt.3.html),  [sscanf(3)](../man3/sscanf.3.html),  [statvfs(3)](../man3/statvfs.3.html),  [stdarg(3)](../man3/stdarg.3.html),  [stdio_ext(3)](../man3/stdio_ext.3.html),  [stpcpy(3)](../man3/stpcpy.3.html),  [stpncpy(3)](../man3/stpncpy.3.html),  [strcasecmp(3)](../man3/strcasecmp.3.html),  [strcasestr(3)](../man3/strcasestr.3.html),  [strchr(3)](../man3/strchr.3.html),  [strchrnul(3)](../man3/strchrnul.3.html),  [strcmp(3)](../man3/strcmp.3.html),  [strcoll(3)](../man3/strcoll.3.html),  [strcpy(3)](../man3/strcpy.3.html),  [strdup(3)](../man3/strdup.3.html),  [strdupa(3)](../man3/strdupa.3.html),  [streq(3)](../man3/streq.3.html),  [strerror(3)](../man3/strerror.3.html),  [strfmon(3)](../man3/strfmon.3.html),  [strfromd(3)](../man3/strfromd.3.html),  [strfry(3)](../man3/strfry.3.html),  [strftime(3)](../man3/strftime.3.html),  [strlen(3)](../man3/strlen.3.html),  [strncasecmp(3)](../man3/strncasecmp.3.html),  [strncat(3)](../man3/strncat.3.html),  [strncmp(3)](../man3/strncmp.3.html),  [strncpy(3)](../man3/strncpy.3.html),  [strndup(3)](../man3/strndup.3.html),  [strndupa(3)](../man3/strndupa.3.html),  [strnlen(3)](../man3/strnlen.3.html),  [strnul(3)](../man3/strnul.3.html),  [strpbrk(3)](../man3/strpbrk.3.html),  [strptime(3)](../man3/strptime.3.html),  [strrchr(3)](../man3/strrchr.3.html),  [strsep(3)](../man3/strsep.3.html),  [strsignal(3)](../man3/strsignal.3.html),  [strspn(3)](../man3/strspn.3.html),  [strstr(3)](../man3/strstr.3.html),  [strtod(3)](../man3/strtod.3.html),  [strtoimax(3)](../man3/strtoimax.3.html),  [strtok(3)](../man3/strtok.3.html),  [strtok_r(3)](../man3/strtok_r.3.html),  [strtol(3)](../man3/strtol.3.html),  [strtoul(3)](../man3/strtoul.3.html),  [strverscmp(3)](../man3/strverscmp.3.html),  [strxfrm(3)](../man3/strxfrm.3.html),  [swab(3)](../man3/swab.3.html),  [sysconf(3)](../man3/sysconf.3.html),  [syslog(3)](../man3/syslog.3.html),  [system(3)](../man3/system.3.html),  [sysv_signal(3)](../man3/sysv_signal.3.html),  [tan(3)](../man3/tan.3.html),  [tanh(3)](../man3/tanh.3.html),  [tcdrain(3)](../man3/tcdrain.3.html),  [tcflow(3)](../man3/tcflow.3.html),  [tcflush(3)](../man3/tcflush.3.html),  [tcgetpgrp(3)](../man3/tcgetpgrp.3.html),  [tcgetsid(3)](../man3/tcgetsid.3.html),  [tcsendbreak(3)](../man3/tcsendbreak.3.html),  [tcsetattr(3)](../man3/tcsetattr.3.html),  [telldir(3)](../man3/telldir.3.html),  [tempnam(3)](../man3/tempnam.3.html),  [tgamma(3)](../man3/tgamma.3.html),  [timegm(3)](../man3/timegm.3.html),  [timespec_get(3)](../man3/timespec_get.3.html),  [tmpfile(3)](../man3/tmpfile.3.html),  [tmpnam(3)](../man3/tmpnam.3.html),  [toascii(3)](../man3/toascii.3.html),  [toupper(3)](../man3/toupper.3.html),  [towctrans(3)](../man3/towctrans.3.html),  [towlower(3)](../man3/towlower.3.html),  [towupper(3)](../man3/towupper.3.html),  [trunc(3)](../man3/trunc.3.html),  [tsearch(3)](../man3/tsearch.3.html),  [ttyname(3)](../man3/ttyname.3.html),  [ttyslot(3)](../man3/ttyslot.3.html),  [tzset(3)](../man3/tzset.3.html),  [ualarm(3)](../man3/ualarm.3.html),  [ulimit(3)](../man3/ulimit.3.html),  [ungetwc(3)](../man3/ungetwc.3.html),  [unlocked_stdio(3)](../man3/unlocked_stdio.3.html),  [unlockpt(3)](../man3/unlockpt.3.html),  [updwtmp(3)](../man3/updwtmp.3.html),  [usleep(3)](../man3/usleep.3.html),  [valloc(3)](../man3/valloc.3.html),  [wcpcpy(3)](../man3/wcpcpy.3.html),  [wcpncpy(3)](../man3/wcpncpy.3.html),  [wcrtomb(3)](../man3/wcrtomb.3.html),  [wcscasecmp(3)](../man3/wcscasecmp.3.html),  [wcscat(3)](../man3/wcscat.3.html),  [wcschr(3)](../man3/wcschr.3.html),  [wcscmp(3)](../man3/wcscmp.3.html),  [wcscpy(3)](../man3/wcscpy.3.html),  [wcscspn(3)](../man3/wcscspn.3.html),  [wcsdup(3)](../man3/wcsdup.3.html),  [wcslen(3)](../man3/wcslen.3.html),  [wcsncat(3)](../man3/wcsncat.3.html),  [wcsncmp(3)](../man3/wcsncmp.3.html),  [wcsncpy(3)](../man3/wcsncpy.3.html),  [wcsnlen(3)](../man3/wcsnlen.3.html),  [wcsnrtombs(3)](../man3/wcsnrtombs.3.html),  [wcspbrk(3)](../man3/wcspbrk.3.html),  [wcsrchr(3)](../man3/wcsrchr.3.html),  [wcsrtombs(3)](../man3/wcsrtombs.3.html),  [wcsspn(3)](../man3/wcsspn.3.html),  [wcsstr(3)](../man3/wcsstr.3.html),  [wcstoimax(3)](../man3/wcstoimax.3.html),  [wcstok(3)](../man3/wcstok.3.html),  [wcstombs(3)](../man3/wcstombs.3.html),  [wcswidth(3)](../man3/wcswidth.3.html),  [wctob(3)](../man3/wctob.3.html),  [wctomb(3)](../man3/wctomb.3.html),  [wctrans(3)](../man3/wctrans.3.html),  [wctype(3)](../man3/wctype.3.html),  [wcwidth(3)](../man3/wcwidth.3.html),  [wmemchr(3)](../man3/wmemchr.3.html),  [wmemcmp(3)](../man3/wmemcmp.3.html),  [wmemcpy(3)](../man3/wmemcpy.3.html),  [wmemmove(3)](../man3/wmemmove.3.html),  [wmempcpy(3)](../man3/wmempcpy.3.html),  [wmemset(3)](../man3/wmemset.3.html),  [wordexp(3)](../man3/wordexp.3.html),  [wprintf(3)](../man3/wprintf.3.html),  [xcrypt(3)](../man3/xcrypt.3.html),  [xdr(3)](../man3/xdr.3.html),  [y0(3)](../man3/y0.3.html),  [man-pages(7)](../man7/man-pages.7.html),  [pthreads(7)](../man7/pthreads.7.html),  [standards(7)](../man7/standards.7.html)

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
