---
{"title": "error::sdt(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/error::sdt.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# error::sdt(7stap) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    ERROR::SDT(7stap)                                       ERROR::SDT(7stap)

## [](#NAME)NAME

           error::sdt - <sys/sdt.h> marker failures

## [](#DESCRIPTION)DESCRIPTION

           Systemtap's <sys/sdt.h> probes are modeled after the dtrace USDT
           API, but are implemented differently.  They leave a only a NOP
           instruction in the userspace program's text segment, and add an
           ELF note to the binary with metadata.  This metadata describes the
           marker's name and parameters.  This encoding is designed to be
           parseable by multiple tools (not just systemtap: GDB, the GNU
           Debugger, also contains support).  These allow the tools to find
           parameters and their types, wherever they happen to reside, even
           without DWARF debuginfo.

           The reason finding parameters is tricky is because the STAP_PROBE
           / DTRACE_PROBE markers store an assembly language expression for
           each operand, as a result of use of gcc inline-assembly
           directives.  The compiler is given a broad gcc operand constraint
           string ("nor") for the operands, which usually works well.
           Usually, it does not force the compiler to load the parameters
           into or out of registers, which would slow down an instrumented
           program.  However, some instrumentation sites with some parameters
           do not work well with the default "nor" constraint.

           unresolveable at run-time
                  GCC may emit strings that an assembler could resolve (from
                  the context of compiling the original program), but a run-
                  time tool cannot.  For example, the operand string might
                  refer to a label of a local symbol that is not emitted into
                  the ELF object file at all, which leaves no trace for the
                  run-time.  Reference to such parameters from within
                  systemtap can result in "SDT asm not understood" errors.

           too complicated expression
                  GCC might synthesize very complicated assembly addressing
                  modes from complex C data types / pointer expressions.
                  systemtap or gdb may not be able to parse some valid but
                  complicated expressions.  Reference to such parameters from
                  within systemtap can result in "SDT asm not understood"
                  errors.

           overly restrictive constraint
                  GCC might not be able to even compile the original program
                  with the default "nor" constraint due to shortage of
                  registers or other reasons.  A compile-time gcc error such
                  as "asm operand has impossible constraints" may result.

           There are two general workarounds to this family of problems.

           change the constraints
                  While compiling the original instrumented program, set the
                  STAP_SDT_ARG_CONSTRAINT macro to different constraint
                  strings.  See the GCC manual about various options.  For
                  example, on many machine architectures, "r" forces operands
                  into registers, and "g" leaves operands essentially
                  unconstrained.

           revert to debuginfo
                  As long as the instrumented program compiles, it may be
                  fine simply to keep using <sys/sdt.h> but eschew extraction
                  of a few individual parameters.  In the worst case, disable
                  <sys/sdt.h> macros entirely to eschew the compiled-in
                  instrumentation.  If DWARF debuginfo was generated and
                  preserved, a systemtap script could refer to the underlying
                  source context variables instead of the positional
                  STAP_PROBE parameters.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           stapprobes(3stap),
           error::dwarf(7stap),
           http://gcc.gnu.org/onlinedocs/gcc/Constraints.html ,
           http://sourceware.org/systemtap/wiki/UserSpaceProbeImplementation ,
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

                                                            ERROR::SDT(7stap)

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
