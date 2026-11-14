---
{"title": "gdbinit(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/gdbinit.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gdbinit(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GDBINIT(5)                GNU Development Tools                GDBINIT(5)

## [](#NAME)NAME

           gdbinit - GDB initialization scripts

## [](#SYNOPSIS)SYNOPSIS

           ~/.config/gdb/gdbinit

           ~/.gdbinit

           ./.gdbinit

## [](#DESCRIPTION)DESCRIPTION

           These files contain GDB commands to automatically execute during
           GDB startup.  The lines of contents are canned sequences of
           commands, described in the GDB manual in node "Sequences" -- shell
           command "info -f gdb -n Sequences".

           Please read more in the GDB manual in node "Startup" -- shell
           command "info -f gdb -n Startup".

           (not enabled with "--with-system-gdbinit" during compilation)
               System-wide initialization file.  It is executed unless user
               specified GDB option "-nx" or "-n".  See more in the GDB
               manual in node "System-wide configuration" -- shell command
               "info -f gdb -n 'System-wide configuration'".

           (not enabled with "--with-system-gdbinit-dir" during compilation)
               System-wide initialization directory.  All files in this
               directory are executed on startup unless user specified GDB
               option "-nx" or "-n", as long as they have a recognized file
               extension.  See more in the GDB manual in node "System-wide
               configuration" -- shell command "info -f gdb -n 'System-wide
               configuration'".

           [1m~/.config/gdb/gdbinit[24m or ~/.gdbinit
               User initialization file.  It is executed unless user
               specified GDB options "-nx", "-n" or "-nh".

           .gdbinit
               Initialization file for current directory.  It may need to be
               enabled with GDB security command "set auto-load
               local-gdbinit".  See more in the GDB manual in node "Init File
               in the Current Directory" -- shell command "info -f gdb -n
               'Init File in the Current Directory'".

## [](#OPTIONS)OPTIONS

## [](#ENVIRONMENT)ENVIRONMENT

## [](#SEE_ALSO)SEE ALSO

           gdb(1), "info -f gdb -n Startup"

           The full documentation for GDB is maintained as a Texinfo manual.
           If the "info" and "gdb" programs and GDB's Texinfo documentation
           are properly installed at your site, the command

                   info gdb

           should give you access to the complete manual.

           Using GDB: A Guide to the GNU Source-Level Debugger, Richard M.
           Stallman and Roland H. Pesch, July 1991.

## [](#COPYRIGHT)COPYRIGHT

           Copyright (c) 1988-2025 Free Software Foundation, Inc.

           Permission is granted to copy, distribute and/or modify this
           document under the terms of the GNU Free Documentation License,
           Version 1.3 or any later version published by the Free Software
           Foundation; with the Invariant Sections being "Free Software" and
           "Free Software Needs Free Documentation", with the Front-Cover
           Texts being "A GNU Manual," and with the Back-Cover Texts as in
           (a) below.

           (a) The FSF's Back-Cover Text is: "You are free to copy and modify
           this GNU Manual.  Buying copies from GNU Press supports the FSF in
           developing GNU and promoting software freedom."

## [](#COLOPHON)COLOPHON

           This page is part of the gdb (GNU debugger) project.  Information
           about the project can be found at 
           ⟨http://www.gnu.org/software/gdb/⟩.  If you have a bug report for
           this manual page, see ⟨http://www.gnu.org/software/gdb/bugs/⟩.
           This page was obtained from the tarball gdb-17.2.tar.gz fetched
           from ⟨https://ftp.gnu.org/gnu/gdb/⟩ on 2026-08-03.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    gdb-17.2                        2026-05-10                     GDBINIT(5)

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
