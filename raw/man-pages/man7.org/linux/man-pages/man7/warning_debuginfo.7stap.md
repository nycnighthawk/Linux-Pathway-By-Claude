---
{"title": "warning::debuginfo(7stap) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/warning::debuginfo.7stap.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# warning::debuginfo(7stap) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [OTHER AUTOMATION](#OTHER_AUTOMATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                         |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WARNING::DEBUGINFO(7stap)                       WARNING::DEBUGINFO(7stap)

## [](#NAME)NAME

           warning::debuginfo - systemtap missing-debuginfo warnings

## [](#DESCRIPTION)DESCRIPTION

           For many symbolic probing operations, systemtap needs DWARF
           debuginfo for the relevant binaries.  This often includes
           resolving function/statement probes, or $context variables in
           related handlers.  DWARF debuginfo is created by the compiler when
           using CFLAGS -g, and may be found in the original binaries built
           during compilation, or may have been split into separate files.
           The SYSTEMTAP_DEBUGINFO_PATH environment variable affects where
           systemtap looks for these files.

           If your operating system came from a distributor, check with them
           if debuginfo packages or variants are available.  If your
           distributor does not have debuginfo-equipped binaries at all, you
           may need to rebuild it.

           Systemtap uses the elfutils library to process ELF/DWARF files.
           The version of elfutils used by systemtap is the number after the
           slash in the -V output:

                  % stap -V
                  Systemtap translator/driver (version 4.2/0.178, rpm 4.2-1.fc30)
                  Copyright (C) 2005-2019 Red Hat, Inc. and others
                  [...]

           This indicates systemtap version 4.2 with elfutils version 0.178.

           New enough versions of elfutils (0.178+) enable systemtap to auto‐
           matically download correct debuginfo from servers run by you, your
           organization, and/or someone on the public internet.  Try:

                  % export DEBUGINFOD_URLS=https://debuginfod.elfutils.org/
                  % export DEBUGINFOD_PROGRESS=1   # for progress messages, if you like

           and rerun systemtap.  It might just work.  If it doesn't, read on.

           kernel debuginfo
                  For scripts that target the kernel, systemtap may search
                  for the vmlinux file created during its original build.
                  This is distinct from the boot-loader's compressed/stripped
                  vmlinuz file, and much larger.  If you have a hand-built
                  kernel, make sure it was built with the CONFIG_DEBUG_INFO=y
                  option.  Some Linux distributions may include several ker‐
                  nel variants, including a confusingly named kernel-debug
                  (an alternative kernel, with its own kernel-debug-debuginfo
                  package), which is not the same thing as the kernel-debug‐
                  info (DWARF data for the base kernel).  The stap-prep pro‐
                  gram can help install the right set.

           process debuginfo
                  For scripts that target user-space, systemtap may search
                  for debuginfo.  If you have hand-built binaries, use
                  CFLAGS=-g -O2 to compile them.

           minidebuginfo
                  On some systems, binaries may be compiled with a subset of
                  debuginfo useful for function tracing and backtraces.  This
                  'Minidebuginfo' is a xz compressed section labeled .gnu_de‐
                  bugdata.  Support for minidebuginfo relies on elfutils ver‐
                  sion 0.156 or later.

           compressed debuginfo
                  On some systems, debuginfo may be available, but compressed
                  into .zdebug_* sections.  Support for compressed debuginfo
                  relies on elfutils version 0.153 or later.

           unnecessary debuginfo
                  In some cases, a script may be altered to avoid requiring
                  debuginfo.  For example, as script that uses probe
                  syscall.*  probes could try instead probe nd_syscall.*
                  (for non-DWARF syscall): these work similarly, and use more
                  intricate (fragile) tapset functions to extract system call
                  arguments.  Another option is use of compiled-in instrumen‐
                  tation such as kernel tracepoints or user-space <sys/sdt.h>
                  markers in libraries or executables, which do not require
                  debuginfo.  If debuginfo was required for resolving a com‐
                  plicated $var->foo->bar expression, it may be possible to
                  use @cast(var,"foo","foo.h")->foo->bar to synthesize debug‐
                  info for that type from a header file.

## [](#OTHER_AUTOMATION)OTHER AUTOMATION

           On some platforms, systemtap may advise what commands to run, in
           order to download needed debuginfo.  Another possibility is to in‐
           voke systemtap with the --download-debuginfo flag, which uses
           ABRT.  The stap-prep script included with systemtap may be able to
           download the appropriate kernel debuginfo.  Another possibility is
           to install and use a stap-server remote-compilation instance on a
           machine on your network, where debuginfo and compilation resources
           can be centralized.  Try the stap --use-server option, in case
           such a server is already running.

## [](#SEE_ALSO)SEE ALSO

           gcc(1),
           stap(1),
           stappaths(7),
           stap-server(8),
           stap-prep(1),
           strip(1),
           warning::symbols(7stap),
           error::dwarf(7stap),
           error::reporting(7stap),
           error::contextvars(7stap),
           debuginfod(8),
           http://elfutils.org/ ,
           https://sourceware.org/elfutils/Debuginfod.html ,
           http://fedoraproject.org/wiki/Features/MiniDebugInfo 

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

                                                    WARNING::DEBUGINFO(7stap)

------------------------------------------------------------------------

Pages that refer to this page: [error::dwarf(7stap)](../man7/error::dwarf.7stap.html),  [error::pass2(7stap)](../man7/error::pass2.7stap.html),  [warning::buildid(7stap)](../man7/warning::buildid.7stap.html),  [warning::symbols(7stap)](../man7/warning::symbols.7stap.html)

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
