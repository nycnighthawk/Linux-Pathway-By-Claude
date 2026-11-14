---
{"title": "tunables.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/tunables.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tunables.conf(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    tunables.conf(5)           File Formats Manual           tunables.conf(5)

## [](#NAME)NAME

           tunables.conf - tunables configuration file

## [](#SYNOPSIS)SYNOPSIS

           /etc/tunables.conf

## [](#DESCRIPTION)DESCRIPTION

           Tunables are a feature in the GNU C Library that allows
           application authors and distribution maintainers to alter the
           runtime library behavior to match their workload.

           The file is parsed by ldconfig(8) and the results stored in
           /etc/ld.so.cache.  The resulting data is read when the program
           starts execution.

           Each line in the file /etc/tunables.conf specifies a tunable, a
           directive, or a filter.

       Tunables
           A tunable is specified with a string of the form name=value.

           For a list of supported tunables, please consult the glibc manual
           that corresponds to your installed version of glibc, or run the
           following command:

               $ ld.so --list-tunables;

       Directives
           include path
                  The syntax allows lines to start with the keyword include
                  followed by a glob(7) pattern.  Files matching that pattern
                  will be processed as if their contents were included at
                  that point.

       Modifiers
           Each line may include zero or more keywords or symbols at the
           beginning, which affect how each tunable affects each processes.
           The keywords must be separated by whitespace, but the symbols need
           not be.

           overridable
           +      Allow the tunable to be overridden by the GLIBC_TUNABLES
                  environment variable when the process runs (this is the
                  default).

           nonoverridable
           -      Do not allow the tunable to be overridden by the
                  environment variable.

           onlysecure
           @      The tunable applies only to AT_SECURE processes, such as
                  one started from a set-user-ID program, or one with
                  elevated capabilities.

           nonsecure
           $      The tunable applies only to non-AT_SECURE processes (this
                  is the default).

           anysecure
           *      The tunable applies to both AT_SECURE and non-AT_SECURE
                  processes.

       Filters
           Filters limit the tunables following it.  The effects of a filter
           are terminated by any of the following:

           •  The end of the file.
           •  The end of an included file.
           •  An include directive.
           •  A new (possibly empty) filter.

           The syntax is:

               [filter:pattern]

           proc   The proc filter limits the following tunables to processes
                  whose name matches the pattern.  The pattern may be an
                  absolute path or just the base name.

           A filter can also be empty: [].  Such a filter has no effects.

## [](#FILES)FILES

           /etc/tunables.conf

           /etc/ld.so.cache
                  Cached copy of tunables.

## [](#EXAMPLES)EXAMPLES

           Example configuration file:

               glibc.malloc.arenas_max=5
               onlysecure glibc.malloc.arenas_max=1
               -glibc.pthread.rseq=1
               [proc:/bin/bad.program]
               -glibc.pthread.rseq=0
               [proc:some.program]
               -glibc.malloc.mmap_threshold=65536

## [](#SEE_ALSO)SEE ALSO

           ld.so(8), ldconfig(8)

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

    Linux man-pages 6.19            2026-08-25               tunables.conf(5)

------------------------------------------------------------------------

Pages that refer to this page: [ldconfig(8)](../man8/ldconfig.8.html)

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
