---
{"title": "ldd(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ldd.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ldd(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ldd(1)                   General Commands Manual                   ldd(1)

## [](#NAME)NAME

           ldd - print shared object dependencies

## [](#SYNOPSIS)SYNOPSIS

           ldd [option ...] file ...

## [](#DESCRIPTION)DESCRIPTION

           ldd prints the shared objects (shared libraries) required by each
           program or shared object specified on the command line.  An
           example of its use and output is the following:

               $ ldd /bin/ls;
                   linux-vdso.so.1 (0x00007ffcc3563000)
                   libselinux.so.1 => /lib64/libselinux.so.1 (0x00007f87e5459000)
                   libcap.so.2 => /lib64/libcap.so.2 (0x00007f87e5254000)
                   libc.so.6 => /lib64/libc.so.6 (0x00007f87e4e92000)
                   libpcre.so.1 => /lib64/libpcre.so.1 (0x00007f87e4c22000)
                   libdl.so.2 => /lib64/libdl.so.2 (0x00007f87e4a1e000)
                   /lib64/ld-linux-x86-64.so.2 (0x00005574bf12e000)
                   libattr.so.1 => /lib64/libattr.so.1 (0x00007f87e4817000)
                   libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f87e45fa000)

           In the usual case, ldd invokes the standard dynamic linker (see
           ld.so(8)) with the LD_TRACE_LOADED_OBJECTS environment variable
           set to 1.  This causes the dynamic linker to inspect the program's
           dynamic dependencies, and find (according to the rules described
           in ld.so(8)) and load the objects that satisfy those dependencies.
           For each dependency, ldd displays the location of the matching
           object and the (hexadecimal) address at which it is loaded.  (The
           linux-vdso and ld-linux shared dependencies are special; see
           vdso(7) and ld.so(8).)

       Security
           Be aware that in some circumstances (e.g., where the program
           specifies an ELF interpreter other than ld-linux.so), some
           versions of ldd may attempt to obtain the dependency information
           by attempting to directly execute the program, which may lead to
           the execution of whatever code is defined in the program's ELF
           interpreter, and perhaps to execution of the program itself.
           (Before glibc 2.27, the upstream ldd implementation did this for
           example, although most distributions provided a modified version
           that did not.)

           Thus, you should never employ ldd on an untrusted executable,
           since this may result in the execution of arbitrary code.  A safer
           alternative when dealing with untrusted executables is:

               $ objdump -p /path/to/program | grep NEEDED;

           Note, however, that this alternative shows only the direct
           dependencies of the executable, while ldd shows the entire
           dependency tree of the executable.

## [](#OPTIONS)OPTIONS

           --version
                  Print the version number of ldd.

           --verbose
           -v     Print all information, including, for example, symbol
                  versioning information.

           --unused
           -u     Print unused direct dependencies.  (Since glibc 2.3.4.)

           --data-relocs
           -d     Perform relocations and report any missing objects (ELF
                  only).

           --function-relocs
           -r     Perform relocations for both data objects and functions,
                  and report any missing objects or functions (ELF only).

           --help Usage information.

## [](#BUGS)BUGS

           ldd does not work on a.out shared libraries.

           ldd does not work with some extremely old a.out programs which
           were built before ldd support was added to the compiler releases.
           If you use ldd on one of these programs, the program will attempt
           to run with argc = 0 and the results will be unpredictable.

## [](#SEE_ALSO)SEE ALSO

           pldd(1), sprof(1), ld.so(8), ldconfig(8)

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

    Linux man-pages 6.19            2026-02-08                         ldd(1)

------------------------------------------------------------------------

Pages that refer to this page: [pldd(1)](../man1/pldd.1.html),  [sprof(1)](../man1/sprof.1.html),  [uselib(2)](../man2/uselib.2.html),  [dl_iterate_phdr(3)](../man3/dl_iterate_phdr.3.html),  [dlopen(3)](../man3/dlopen.3.html),  [babeltrace2-filter.lttng-utils.debug-info(7)](../man7/babeltrace2-filter.lttng-utils.debug-info.7.html),  [rtld-audit(7)](../man7/rtld-audit.7.html),  [vdso(7)](../man7/vdso.7.html),  [ldconfig(8)](../man8/ldconfig.8.html),  [ld.so(8)](../man8/ld.so.8.html)

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
