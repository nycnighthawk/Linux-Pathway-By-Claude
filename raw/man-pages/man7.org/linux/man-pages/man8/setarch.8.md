---
{"title": "setarch(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/setarch.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setarch(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SETARCH(8)                System Administration                SETARCH(8)

## [](#NAME)NAME

           setarch - change reported architecture in new program environment
           and/or set personality flags

## [](#SYNOPSIS)SYNOPSIS

           setarch [arch] [options] [program [argument...]]

           arch [options] [program [argument...]]

## [](#DESCRIPTION)DESCRIPTION

           setarch modifies the execution domain and process personality
           flags.

           The execution domain currently only affects the output of uname
           -m. For example, on an AMD64 system, running setarch i386 program
           will cause program to see i686 instead of x86_64 as the machine
           type. The default program is /bin/sh.

           Since version 2.33, the arch command-line argument is optional and
           setarch may be used to change personality flags (ADDR_LIMIT_3GB,
           SHORT_INODE, etc) without modification of the execution domain.

## [](#OPTIONS)OPTIONS

           --list
               List the architectures that setarch knows about. Whether
               setarch can actually set each of these architectures depends
               on the running kernel.

           --show[=personality]
               Show the currently active personality and flags. If the
               personality argument is provided, that personality is shown
               instead of the current one. personality is a hexadecimal
               number whose possible values are described in
               sys/personality.h.

           -p, --pid=pid
               When used with --show, show the personality and flags of the
               specified process.

           --uname-2.6
               Causes the specified program to see a kernel version number
               beginning with 2.6. Turns on UNAME26.

           -v, --verbose
               Be verbose.

           -3, --3gb
               The specified program should use a maximum of 3GB of address
               space. Supported on x86. Turns on ADDR_LIMIT_3GB.

           --4gb
               This option has no effect. It is retained for backward
               compatibility only, and may be removed in future releases.

           -B, --32bit
               Limit the address space to 32 bits to emulate hardware.
               Supported on ARM and Alpha. Turns on ADDR_LIMIT_32BIT.

           -F, --fdpic-funcptrs
               Treat user-space function pointers to signal handlers as
               pointers to address descriptors. This option has no effect on
               architectures that do not support FDPIC ELF binaries. In
               kernel v4.14 support is limited to ARM, Blackfin, Fujitsu
               FR-V, and SuperH CPU architectures.

           -I, --short-inode
               Obsolete bug emulation flag. Turns on SHORT_INODE.

           -L, --addr-compat-layout
               Provide legacy virtual address space layout. Use when the
               program binary does not have PT_GNU_STACK ELF header. Turns on
               ADDR_COMPAT_LAYOUT.

           -R, --addr-no-randomize
               Disables randomization of the virtual address space. Turns on
               ADDR_NO_RANDOMIZE.

           -S, --whole-seconds
               Obsolete bug emulation flag. Turns on WHOLE_SECONDS.

           -T, --sticky-timeouts
               This makes select(2), pselect(2), and ppoll(2) system calls
               preserve the timeout value instead of modifying it to reflect
               the amount of time not slept when interrupted by a signal
               handler. Use when program depends on this behavior. For more
               details see the timeout description in select(2) manual page.
               Turns on STICKY_TIMEOUTS.

           -X, --read-implies-exec
               If this is set then mmap(2) PROT_READ will also add the
               PROT_EXEC bit - as expected by legacy x86 binaries. Notice
               that the ELF loader will automatically set this bit when it
               encounters a legacy binary. Turns on READ_IMPLIES_EXEC.

           -Z, --mmap-page-zero
               SVr4 bug emulation that will set mmap(2) page zero as
               read-only. Use when program depends on this behavior, and the
               source code is not available to be fixed. Turns on
               MMAP_PAGE_ZERO.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXAMPLES)EXAMPLES

               setarch --addr-no-randomize mytestprog
               setarch ppc32 rpmbuild --target=ppc --rebuild foo.src.rpm
               setarch ppc32 -vL3 rpmbuild --target=ppc --rebuild bar.src.rpm
               setarch ppc32 --32bit rpmbuild --target=ppc --rebuild foo.src.rpm
               setarch --show
               setarch --show=$(cat /proc/9284/personality)
               setarch --show --pid 9284

## [](#AUTHORS)AUTHORS

           Elliot Lee <sopwith@redhat.com>, Jindrich Novy <jnovy@redhat.com>,
           Karel Zak <kzak@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           personality(2), select(2), proc_pid_personality(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The setarch command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                     SETARCH(8)

------------------------------------------------------------------------

Pages that refer to this page: [personality(2)](../man2/personality.2.html)

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
