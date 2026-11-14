---
{"title": "elfdeps(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/elfdeps.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# elfdeps(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPERATIONS](#OPERATIONS) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [OUTPUT](#OUTPUT) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ELFDEPS(1)               General Commands Manual               ELFDEPS(1)

## [](#NAME)NAME

           elfdeps - Dependency generator for ELF binaries

## [](#SYNOPSIS)SYNOPSIS

           elfdeps <operation> [options]

           elfdeps <operation> [options] [FILE] ...

## [](#DESCRIPTION)DESCRIPTION

           elfdeps is a dependency generator for ELF executables and dynamic
           shared object (DSO) files. The filenames can be received on the
           standard input (when used as a generator), or command line
           arguments for testing convenience.

           elfdeps encodes information stored in ELF files into a format
           suitable for use in RPM dependencies. The main interest areas are
           DT_SONAME, DT_NEEDED fields of the SHT_DYNAMIC section, and symbol
           versioning information in the SHT_GNU_verdef and SHT_GNU_verneed
           sections.

           elfdeps is not normally invoked directly, but doing so can be
           useful for troubleshooting dependency generation and developing
           new dependency generators. The installation directory of elfdeps
           can be determined with rpm -E "%{_rpmconfigdir}".

           This man page describes the options specific to this generator,
           see rpm-dependency-generators(7) for information about the overall
           mechanism.

## [](#OPERATIONS)OPERATIONS

           -P, --provides,
               Print the provides dependencies.

           -R, --requires
               Print the requires dependencies.

## [](#ARGUMENTS)ARGUMENTS

           FILE
               An ELF file. Other file types are silently ignored.

## [](#OPTIONS)OPTIONS

           --no-fake-soname
               Do not emit a fake soname for DSOs that don't set DT_SONAME.
               By default, elfdeps generates a soname from the filename for
               DSOs that do not have one. Only effective when printing
               provides dependencies.

           --no-filter-soname
               Do not filter sonames. By default, elfdeps does some sanity
               checking to filter out redundant and/or invalid soname
               entries. Only effective when printing provides dependencies.

           -m, --multifile
               Use multifile protocol for output. See
               rpm-dependency-generators(7).

           --require-interp
               Emit a requires dependency for the ELF interpreter
               (PT_INTERP), if there is one. Only effective when printing
               requires dependencies.

           --soname-only
               Emit only the soname (DT_SONAME) of a DSO, omitting any symbol
               versioning information. Only effective when printing provides
               dependencies.

## [](#OUTPUT)OUTPUT

           See Protocols in rpm-dependency-generators(7). By default,
           singlefile protocol is used, but the multifile protocol can be
           enabled with the --multifile option.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           elfdeps --requires /bin/ls
               Print ELF-level requires dependencies of the /bin/ls
               executable.

           find mylib-1.0-build/BUILDROOT --name "*.so*" | elfdeps -P
           --multifile
               Print ELF-level provides dependencies of all shared libraries
               inside the mylib-1.0-build/BUILDROOT directory, using the
               multifile generator protocol.

## [](#SEE_ALSO)SEE ALSO

           rpmbuild(1) rpm-dependency-generators(7) elf(5) readelf(1)

           http://www.rpm.org/ 

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03                     ELFDEPS(1)

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
