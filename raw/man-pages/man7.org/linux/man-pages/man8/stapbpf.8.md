---
{"title": "stapbpf(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/stapbpf.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stapbpf(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ARGUMENTS](#ARGUMENTS) \| [EXAMPLES](#EXAMPLES) \| [LIMITATIONS](#LIMITATIONS) \| [SAFETY AND SECURITY](#SAFETY_AND_SECURITY) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAPBPF(8)               System Manager's Manual               STAPBPF(8)

## [](#NAME)NAME

           stapbpf - systemtap bpf runtime

## [](#SYNOPSIS)SYNOPSIS

           stapbpf [ OPTIONS ] MODULE

## [](#DESCRIPTION)DESCRIPTION

           The stapbpf program is the BPF back-end of the Systemtap tool.  It
           expects a bpf-elf file produced by the front-end stap tool, when
           run with --runtime=bpf.

           Splitting the systemtap tool into a front-end and a back-end
           allows a user to compile a systemtap script on a development
           machine that has the debugging information needed to compile the
           script and then transfer the resulting shared object to a
           production machine that doesn't have any development tools or
           debugging information installed.

           Please refer to stappaths(7) for the version number, or run

            $ rpm -q systemtap # (for Fedora/RHEL)
            $ apt-get -v systemtap # (for Ubuntu)

## [](#OPTIONS)OPTIONS

           The stapbpf program supports the following options.  Any other
           option prints a list of supported options.

           -v     Verbose mode.

           -V     Print version number and exit.

           -w     Suppress warnings from the script.

           -h     Print help message.

           -x PID The '_stp_target' variable will be set to PID.

           -o FILE
                  Send output to FILE.

## [](#ARGUMENTS)ARGUMENTS

           MODULE is the path of a bpf-elf file produced by the front-end
           stap tool, when run with --runtime=bpf.

## [](#EXAMPLES)EXAMPLES

           Here is a very basic example of how to generate a stapbpf module.
           First, use stap to compile a script.  The stap program will report
           the name of the resulting module in the current working directory.

            $ stap --runtime=bpf -p4 -e 'probe begin { printf("Hello
           World!\n"); exit() }'
            stap_28784.bo

           Run stapbpf with the pathname to the module as an argument.

            $ stapbpf ./stap_28784.bo
            Hello World!

           If the -p4 option is omitted, stap will invoke stapbpf
           automatically.

## [](#LIMITATIONS)LIMITATIONS

           This runtime is in an early stage of development and it currently
           lacks support for a number of features available in the default
           runtime.  A subset of the following probe points is supported:

                  begin
                  end
                  kernel.*
                  process.*
                  timer.*
                  perf.*
                  procfs.*

           In general, probes based on the kprobes, uprobes, tracepoint and
           perf infrastructures are supported. See stapprobes(3stap) for more
           information on the probe points and which tracing infrastructures
           they are based on.

           for loops, foreach loops and while loops are usable only in begin
           and end probes.  try statements are not supported.

           There is limited support for string operations. String variables
           and literals are limited to 64 characters, except for printf for‐
           mat strings, which are limited to 256 characters.

           A subset of the statistical aggregate functionality is available,
           with support only for the @count(), @sum(), @avg() extractor func‐
           tions.

           The name of the bpf-elf file produced by the front-end stap tool
           should not be changed.

## [](#SAFETY_AND_SECURITY)SAFETY AND SECURITY

           See the stap(1) manual page for additional information on safety
           and security.

## [](#SEE_ALSO)SEE ALSO

           stap(1), stapprobes(3stap), staprun(8), stapex(3stap)

## [](#BUGS)BUGS

           Use the Bugzilla link of the project web page or our mailing list.
           http://sourceware.org/systemtap/ , <systemtap@sourceware.org>.

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

                                                                   STAPBPF(8)

------------------------------------------------------------------------

Pages that refer to this page: [stap(1)](../man1/stap.1.html)

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
