---
{"title": "stappaths(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/stappaths.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# stappaths(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STAP(7)              Miscellaneous Information Manual             STAP(7)

## [](#NAME)NAME

           stappaths - systemtap configurable file paths

## [](#DESCRIPTION)DESCRIPTION

           This manual page was generated for systemtap 5.6.  The following
           section will list the main paths in systemtap that are important
           to know and may be required to reference.

           /usr/local/share/systemtap/tapset/
                  The directory for the standard probe-alias / function
                  tapset library, unless overridden by the SYSTEMTAP_TAPSET
                  environment variable or the XDG_DATA_DIRS environment
                  variable.  These are described in the stapprobes(3stap),
                  probe::*(3stap), and function::*(3stap) manual pages.

           /usr/local/share/systemtap/runtime/
                  The runtime sources, unless overridden by the
                  SYSTEMTAP_RUNTIME environment variable.

           /usr/local/bin/staprun
                  The auxiliary program supervising module loading,
                  interaction, and unloading.

           ${prefix}/etc/stap-exporter
                  The default directory to search for *.stp files, for
                  exporting to HTTP.

           ${exec_prefix}/libexec/systemtap/stapio
                  The auxiliary program for module input and output handling.

           /usr/include/sys/sdt.h
                  Location of the <sys/sdt.h> headers.

           Kernel debuginfo Path: /usr/lib/debug/lib/modules/$(uname -r)/
                  The location of kernel debugging information when packaged
                  into the kernel-debuginfo RPM, unless overridden by the
                  SYSTEMTAP_DEBUGINFO_PATH environment variable.  The default
                  value for this variable is +:.debug:/usr/lib/debug:build.
                  elfutils searches vmlinux in this path and it interprets
                  the path as a base directory of which various
                  subdirectories will be searched for finding debuginfo for
                  the kernel, kernel modules, and user-space binaries.  By
                  default, systemtap will also look for vmlinux in these
                  locations:

                  /boot/vmlinux-`uname -r`
                  /lib/modules/`uname -r`/vmlinux
                  /lib/modules/`uname -r`/vmlinux.debug
                  /lib/modules/`uname -r`/build/vmlinux
                  /lib/modules/`uname -r`/.debug/vmlinux.debug
                  /usr/lib/debug/lib/modules/`uname -r`/vmlinux.debug
                  /var/cache/abrt-di/usr/debug/lib/modules/`uname -r`/
                  /var/cache/abrt-di/usr/lib/debug/lib/modules/`uname -r`/vmlinux.debug

                  Corresponding source files are usually located under
                  /usr/src/debug/.  Further file information on user-space
                  applications can be determined per-basis using rpm -ql
                  <package>-debuginfo. For supported user-space applications
                  information please visit the systemtap wiki.

                  With elfutils version >0.178, systemtap can automatically
                  download debugging information from debuginfod servers.
                  You can try it by setting an environment variable or two:
                  export DEBUGINFOD_URLS=https://debuginfod.elfutils.org/
                  export DEBUGINFOD_PROGRESS=1

           $HOME/.systemtap
                  Systemtap data directory for cached systemtap files, unless
                  overridden by the SYSTEMTAP_DIR environment variable.

           /tmp/stapXXXXXX
                  Temporary directory for systemtap files, including trans‐
                  lated C code and kernel object.

           /lib/modules/VERSION/build
                  The location of kernel module building infrastructure.

           /usr/local/share/doc/systemtap*/examples
                  Examples with greater detail can be found here. Each exam‐
                  ple comes with a .txt or .meta file explaining what the ex‐
                  ample, sample or demo does and how it is ordinarily run.
                  See also online at:
                  https://sourceware.org/systemtap/examples/ 

           $SYSTEMTAP_DIR/ssl/server
                  User's server-side SSL certificate database. If SYSTEM‐
                  TAP_DIR is not set, the default is $HOME/.systemtap.

           $SYSTEMTAP_DIR/ssl/client
                  User's private client-side SSL certificate database. If
                  SYSTEMTAP_DIR is not set, the default is $HOME/.systemtap.

           ${prefix}/etc/systemtap/ssl/client
                  Global client-side SSL certificate database.

           ${prefix}/etc/systemtap/staprun/
                  staprun's trusted signer certificate database.

           ${prefix}/etc/sysconfig/stap-server
                  stap-server service global configuration file.

           ${prefix}/etc/sysconfig/stap-exporter
                  stap-exporter service global configuration file.

           ${prefix}/var/run/stap-server/
                  stap-server service default location of status files for
                  running servers.

           ${prefix}/var/log/stap-server/log
                  stap-server service default log file.

## [](#SEE_ALSO)SEE ALSO

           stapprobes(3stap),
           staprun(8),
           stapvars(3stap),
           stapex(3stap),
           stap-server(8),
           awk(1),
           gdb(1)
           http://sourceware.org/elfutils/Debuginfod.html 

## [](#BUGS)BUGS

           Use the Bugzilla link of the project web page or our mailing list.
           http://sourceware.org/systemtap/ ,<systemtap@sourceware.org>.

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

                                  Systemtap Team                      STAP(7)

------------------------------------------------------------------------

Pages that refer to this page: [dtrace(1)](../man1/dtrace.1.html),  [stap(1)](../man1/stap.1.html),  [stap-merge(1)](../man1/stap-merge.1.html),  [stapex(3stap)](../man3/stapex.3stap.html),  [stapvars(3stap)](../man3/stapvars.3stap.html),  [warning::debuginfo(7stap)](../man7/warning::debuginfo.7stap.html),  [warning::symbols(7stap)](../man7/warning::symbols.7stap.html),  [stapbpf(8)](../man8/stapbpf.8.html),  [stap-exporter(8)](../man8/stap-exporter.8.html),  [stap-server(8)](../man8/stap-server.8.html)

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
