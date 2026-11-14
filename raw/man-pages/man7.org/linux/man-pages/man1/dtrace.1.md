---
{"title": "dtrace(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dtrace.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dtrace(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEMAPHORES](#SEMAPHORES) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DTRACE(1)                General Commands Manual                DTRACE(1)

## [](#NAME)NAME

           dtrace - Dtrace compatible user application static probe
           generation tool.

## [](#SYNOPSIS)SYNOPSIS

           dtrace -s file [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           The dtrace command converts probe descriptions defined in file.d
           into a probe header file via the -h option or a probe description
           file via the -G option.

## [](#OPTIONS)OPTIONS

           -h     generate a systemtap header file.

           -G     generate a systemtap probe definition object file.  This
                  invokes the C compiler with a sensible set of compiler
                  flags.  If you need to add more, flags found in the CFLAGS
                  environment variable will be transcribed to the compiler.
                  If this is not enough control, use the -k option to capture
                  the generated C file and compile as needed.

           -o file
                  is the name of the output file.  If the -G option is given
                  then the output file will be called file.o; if the -h
                  option is given then the output file will be called file.h.

           -C     run the cpp preprocessor on the input file when the -h
                  option is given.

           -I file
                  give this include path to cpp when the -C option is given.

           -k     keep temporary files, for example the C language source for
                  the -G option.

## [](#EXAMPLES)EXAMPLES

           Systemtap is source compatible with dtrace user application static
           probe support.  Given a file test.d containing:

                  provider sdt_probes
                  {
                    probe test_0 (int type);
                    probe test_1 (struct astruct node);
                  };
                  struct astruct {int a; int b;};

           Then the command "dtrace -s test.d -G" will create the probe defi‐
           nition file test.o and the command "dtrace -stest.d -h" will cre‐
           ate the probe header file test.h Subsequently the application can
           use the generated macros this way:

                  #include "test.h"
                   ...
                  struct astruct s;
                   ...
                  SDT_PROBES_TEST_0(value);
                   ...
                  if (SDT_PROBES_TEST_1_ENABLED())
                      SDT_PROBES_TEST_1(expensive_function(s));

## [](#SEMAPHORES)SEMAPHORES

           Semaphores are flag variables used by probes as a way of bypassing
           potentially costly processing to prepare arguments for probes that
           may not even be active.  They are automatically set/cleared by
           systemtap when a relevant script is running, so the argument setup
           cost is only paid when necessary.  These semaphore variables are
           defined within the the "test.o" object file, which must therefore
           be linked into an application.

           Sometimes, semaphore variables are not necessary nor helpful.
           Skipping them can simplify the build process, by omitting the ex‐
           tra "test.o" file.  To skip dependence upon semaphore variables,
           include "<sys/sdt.h>" within the application before "test.h":

                  #include <sys/sdt.h>
                  #include "test.h"
                   ...
                  struct astruct s;
                   ...
                  SDT_PROBES_TEST_0(value);
                   ...
                  if (SDT_PROBES_TEST_1_ENABLED())
                     SDT_PROBES_TEST_1(cheap_function(s));

           In this mode, the ENABLED() test is fixed at 1.

## [](#SEE_ALSO)SEE ALSO

           stap(1),
           stappaths(7)

## [](#BUGS)BUGS

           Use the Bugzilla link of the project web page or our mailing list.
           http://sourceware.org/systemtap/ , <systemtap@sourceware.org>.

           error::reporting(7stap),
           https://sourceware.org/systemtap/wiki/HowToReportBugs 

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

                                                                    DTRACE(1)

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
