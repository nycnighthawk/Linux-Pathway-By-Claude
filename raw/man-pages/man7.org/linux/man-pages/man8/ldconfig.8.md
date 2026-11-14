---
{"title": "ldconfig(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/ldconfig.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ldconfig(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ldconfig(8)              System Manager's Manual              ldconfig(8)

## [](#NAME)NAME

           ldconfig - configure dynamic linker run-time bindings

## [](#SYNOPSIS)SYNOPSIS

           /sbin/ldconfig [-nNvVX] [-C cache] [-f conf] [-r root]
                          [-t tunconf] directory ...

           /sbin/ldconfig -l [-v] library ...

           /sbin/ldconfig -p

## [](#DESCRIPTION)DESCRIPTION

           ldconfig creates the necessary links and cache to the most recent
           shared libraries found in the directories specified on the command
           line, in the file /etc/ld.so.conf, and in the trusted directories,
           /lib and /usr/lib.  On some 64-bit architectures such as x86-64,
           /lib and /usr/lib are the trusted directories for 32-bit
           libraries, while /lib64 and /usr/lib64 are used for 64-bit
           libraries.

           The cache is used by the run-time linker, ld.so or ld-linux.so.
           ldconfig checks the header and filenames of the libraries it
           encounters when determining which versions should have their links
           updated.  ldconfig should normally be run by the superuser as it
           may require write permission on some root owned directories and
           files.

           ldconfig will look only at files that are named lib*.so* (for
           regular shared objects) or ld-*.so* (for the dynamic loader
           itself).  Other files will be ignored.  Also, ldconfig expects a
           certain pattern to how the symbolic links are set up, like this
           example, where the middle file (libfoo.so.1 here) is the SONAME
           for the library:

               libfoo.so -> libfoo.so.1 -> libfoo.so.1.12

           Failure to follow this pattern may result in compatibility issues
           after an upgrade.

           If the file /etc/tunables.conf exists, it contains tunables to be
           applied to all processes.  These tunables are stored in the cache
           and applied to every process at its startup.

## [](#OPTIONS)OPTIONS

           --format=fmt
           -c fmt (Since glibc 2.2) Use cache format fmt, which is one of
                  old, new, or compat.  Since glibc 2.32, the default is new.
                  Before that, it was compat.

           -C cache
                  Use cache instead of /etc/ld.so.cache.

           -f conf
                  Use conf instead of /etc/ld.so.conf.

           --ignore-aux-cache
           -i     (Since glibc 2.7) Ignore auxiliary cache file.

           -l     (Since glibc 2.2) Interpret each operand as a library name
                  and configure its links.  Intended for use only by experts.

           -n     Process only the directories specified on the command line;
                  don't process the trusted directories, nor those specified
                  in /etc/ld.so.conf.  Implies -N.

           -N     Don't rebuild the cache.  Unless -X is also specified,
                  links are still updated.

           --print-cache
           -p     Print the lists of directories and candidate libraries
                  stored in the current cache.

           -r root
                  Change to and use root as the root directory.

           -t tunconf
                  Use tunconf instead of /etc/tunables.conf.

           --verbose
           -v     Verbose mode.  Print current version number, the name of
                  each directory as it is scanned, and any links that are
                  created.  Overrides quiet mode.

           --version
           -V     Print program version.

           -X     Don't update links.  Unless -N is also specified, the cache
                  is still rebuilt.

## [](#FILES)FILES

           /lib/ld.so
                  is the run-time linker/loader.
           /etc/ld.so.conf
                  See ld.so.conf(5).
           /etc/tunables.conf
                  See tunables.conf(5).
           /etc/ld.so.cache
                  contains an ordered list of libraries found in the
                  directories specified in /etc/ld.so.conf, as well as those
                  found in the trusted directories, and any tunables listed
                  in /etc/tunables.conf.

## [](#SEE_ALSO)SEE ALSO

           ldd(1), ld.so(8), ld.so.conf(5)

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

    Linux man-pages 6.19            2026-08-03                    ldconfig(8)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-divert(1)](../man1/dpkg-divert.1.html),  [ldd(1)](../man1/ldd.1.html),  [dlopen(3)](../man3/dlopen.3.html),  [ld.so.conf(5)](../man5/ld.so.conf.5.html),  [tunables.conf(5)](../man5/tunables.conf.5.html),  [rtld-audit(7)](../man7/rtld-audit.7.html),  [ld.so(8)](../man8/ld.so.8.html),  [sln(8)](../man8/sln.8.html)

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
