---
{"title": "error::dwarf(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/error::dwarf.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# error::dwarf(7stap) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [ALTERNATIVES](#ALTERNATIVES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ERROR::DWARF(7stap)                                   ERROR::DWARF(7stap)

## [](#NAME)NAME

           error::dwarf - dwarf debuginfo quality problems

## [](#DESCRIPTION)DESCRIPTION

           Systemtap sometimes relies on ELF/DWARF debuginfo for programs
           being instrumented to locate places to probe, or context variables
           to read/write, just like a symbolic debugger does.  Even though
           examination of the program's source code may show variables or
           lines where probes may be desired, the compiler must preserve
           information about them for systemtap (or a debugger such as gdb)
           to get pinpoint access to the desired information.  If a script
           requires such data, but the compiler did not preserve enough of
           it, pass-2 errors may result.

           Common conditions that trigger these problems include:

           debuginfo missing or mismatching
                  Sometimes debuginfo is installed, but does not match the
                  binaries being probed.  See the warning::debuginfo man page
                  for more help for locating correct debuginfo.

           compiler version
                  Prior to GCC version 4.5, debuginfo quality was fairly
                  limited.  Often developers were advised to build their
                  programs with -O0 -g flags to disable optimization.  GCC
                  version 4.5 introduced a facility called "variable-tracking
                  assignments" that allows it to generate high-quality
                  debuginfo under full -O2 -g optimization.  It is not
                  perfect, but much better than before.  Note that, due to
                  another gcc bug (PR51358) -O0 -g can actually sometimes
                  make debuginfo quality worse than for -O2 -g.

                  Another related problem involves debuginfo quality for the
                  prologue area of a function (PR15123), wherein a program
                  compiled with CFLAGS=-mfentry (especially the kernel, for
                  ftrace) may lack accurate debuginfo for the entry
                  instructions for gcc prior to version 4.8.  If able,
                  arrange to compile your programs with -grecord-gcc-switches
                  CFLAGS, and/or try rerunning systemtap with
                  $PR15123_ASSUME_MFENTRY=1.

           linux kbuild damaging debuginfo quality
                  An upstream kernel commit #2062afb4f804a put
                  -fno-var-tracking-assignments into KCFLAGS, dramatically
                  reducing debuginfo quality, which can cause debuginfo fail‐
                  ures. The simplest fix is to erase, excise, nay, eradicate
                  this line from the top level linux Makefile:

                  KBUILD_CFLAGS += [...] -fno-var-tracking-assignments [...]

           function inlining
                  Even modern gcc sometimes has problems with parameters for
                  inlined functions.  It may be necessary to change the
                  script to probe at a slightly different place.  Try a
                  .statement() probe, instead of a .function() probe, some‐
                  where a few source lines into the body of the inlined func‐
                  tion.  Or try putting a probe at the call site of the in‐
                  lined function.  Or use the if @defined($var) { ... }
                  script language construct to test for the resolvability of
                  the context variable before using it.

           instruction reordering
                  Heavily optimized code often smears the instructions from
                  multiple source statements together.  This can leave sys‐
                  temtap with no place to choose to place a probe, especially
                  a statement probe specified by line number.  Systemtap may
                  advise to try a nearby line number, but these may not work
                  well either.  Consider placing a probe by a statement wild‐
                  card or line number range.

           elfutils configuration
                  It is possible that the DWARF debuginfo being sought is
                  available, but not in a format acceptable to the copy of
                  elfutils used by systemtap.  For example, your copy of gcc
                  might produce compressed debuginfo (.zdebug_* ELF sections
                  or .xz files) while your copy of elfutils might lack appro‐
                  priate decompression capabilities.  Unfortunately, there is
                  no easy way to tell if this is the problem.  If you're
                  building your own copy of elfutils, ensure all decompres‐
                  sion library headers/libraries are available at build time.

           debuginfo configuration
                  Some tools may generate debuginfo that is unsupported by
                  systemtap, such as the linux kernel CONFIG_DEBUG_INFO_SPLIT
                  (.dwo files) option.  Stick with plain ELF/DWARF (optinally
                  split, Fedora-style), if possible.

## [](#ALTERNATIVES)ALTERNATIVES

           In order to reduce reliance on ELF/DWARF debuginfo, consider the
           use of statically compiled-in instrumentation, such as kernel tra‐
           cepoints, or <sys/sdt.h> userspace markers.  Such instrumentation
           hook sites are relatively low cost (just one NOP instruction for
           sdt.h), and nearly guarantee the availability of parameter data
           and a reliable probe site, all without reliance on debuginfo.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           http://dwarfstd.org/ ,
           http://sourceware.org/systemtap/wiki/TipContextVariables ,
           http://gcc.gnu.org/wiki/Var_Tracking_Assignments ,
           warning::debuginfo(7stap),
           warning::buildid(7stap),
           error::reporting(7stap)

## [](#COLOPHON)COLOPHON

           This page is part of the systemtap (a tracing and live-system
           analysis tool) project.  Information about the project can be
           found at ⟨https://sourceware.org/systemtap/⟩.  If you have a bug
           report for this manual page, send it to systemtap@sourceware.org.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/systemtap.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                          ERROR::DWARF(7stap)

------------------------------------------------------------------------

Pages that refer to this page: [error::pass2(7stap)](../man7/error::pass2.7stap.html),  [error::sdt(7stap)](../man7/error::sdt.7stap.html),  [warning::debuginfo(7stap)](../man7/warning::debuginfo.7stap.html),  [warning::pass5(7stap)](../man7/warning::pass5.7stap.html),  [warning::symbols(7stap)](../man7/warning::symbols.7stap.html)

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
