---
{"title": "systemd-vpick(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-vpick.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-vpick(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-VPICK(1)              systemd-vpick              SYSTEMD-VPICK(1)

## [](#NAME)NAME

           systemd-vpick - Resolve paths to ".v/" versioned directories

## [](#SYNOPSIS)SYNOPSIS

           systemd-vpick [OPTIONS...] [PATH...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-vpick resolves a file system path referencing a ".v/"
           versioned directory to a path to the newest (by version) file
           contained therein. This tool provides a command line interface for
           the systemd.v(7) logic.

           The tool expects a path to a ".v/" directory as argument (either
           directly, or with a triple underscore pattern as final component).
           It then determines the newest file contained in that directory,
           and writes its path to standard output.

           Unless the triple underscore pattern is passed as last component
           of the path, it is typically necessary to at least specify the
           --suffix= switch to configure the file suffix to look for.

           If the specified path does not reference a ".v/" path (i.e.
           neither the final component ends in ".v", nor the penultimate does
           or the final one does contain a triple underscore) its specified
           path is written unmodified to standard output.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --basename=, -B
               Overrides the "basename" of the files to look for, i.e. the
               part to the left of the variable part of the filenames.
               Normally this is derived automatically from the filename of
               the ".v" component of the specified path, or from the triple
               underscore pattern in the last component of the specified
               path.

               Added in version 256.

           -V
               Explicitly configures the version to select. If specified, a
               filename with the specified version string will be looked for,
               instead of the newest version available.

               Added in version 256.

           -A
               Explicitly configures the architecture to select. If
               specified, a filename with the specified architecture
               identifier will be looked for. If not specified, only
               filenames with a locally supported architecture are
               considered, or those without any architecture identifier.

               Added in version 256.

           --suffix=, -S
               Configures the suffix of the filenames to consider. For the
               ".v/" logic it is necessary to specify the suffix to look for,
               and the ".v/" component must also carry the suffix immediately
               before ".v" in its name.

               Added in version 256.

           --type=, -t
               Configures the inode type to look for in the ".v/" directory.
               Takes one of "reg", "dir", "sock", "fifo", "blk", "chr", "lnk"
               as argument, each identifying an inode type. See inode(7) for
               details about inode types. If this option is used inodes not
               matching the specified type are filtered and not taken into
               consideration.

               Added in version 256.

           --print=, -p
               Configures what precisely to write to standard output. If not
               specified, prints the full, resolved path of the newest
               matching file in the ".v/" directory. This switch can be set
               to one of the following:

               •   If set to "filename", will print only the filename instead
                   of the full path of the resolved file.

               •   If set to "version", will print only the version of the
                   resolved file.

               •   If set to "type", will print only the inode type of the
                   resolved file (i.e. a string such as "reg" for regular
                   files, or "dir" for directories).

               •   If set to "arch", will print only the architecture of the
                   resolved file.

               •   If set to "tries", will print only the tries left/tries
                   done of the resolved file.

               •   If set to "all", will print all of the above in a simple
                   tabular output.

               Added in version 256.

           --resolve=
               Takes a boolean argument. If true the path to the versioned
               file is fully canonicalized (i.e. symlinks resolved, and
               redundant path components removed) before it is shown. If
               false (the default) this is not done, and the path is shown
               without canonicalization.

               Added in version 256.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXAMPLES)EXAMPLES

           Use a command like the following to automatically pick the newest
           raw disk image from a ".v/" directory:

               $ systemd-vpick --suffix=.raw --type=reg /var/lib/machines/quux.raw.v/

           This will enumerate all regular files matching
           /var/lib/machines/quux.raw.v/quux*.raw, filter and sort them
           according to the rules described in systemd.v(7), and then write
           the path to the newest (by version) file to standard output.

           Use a command like the following to automatically pick the newest
           OS directory tree from a ".v/" directory:

               $ systemd-vpick --type=dir /var/lib/machines/waldo.v/

           This will enumerate all directory inodes matching
           /var/lib/machines/waldo.v/waldo*, filter and sort them according
           to the rules described in systemd.v(7), and then write the path to
           the newest (by version) directory to standard output.

           For further examples see systemd.v(7).

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.v(7)

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                        SYSTEMD-VPICK(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.mstack(7)](../man7/systemd.mstack.7.html),  [systemd.v(7)](../man7/systemd.v.7.html)

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
