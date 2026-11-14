---
{"title": "fuservicemount3(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/fuservicemount3.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fuservicemount3(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    fuservicemount3(8)       System Manager's Manual       fuservicemount3(8)

## [](#NAME)NAME

           fuservicemount3 - mount a FUSE filesystem that runs as a system
           socket service

## [](#SYNOPSIS)SYNOPSIS

           fuservicemount3 source mountpoint -t fstype [ -o options ]

           fuservicemount3 -t fstype --check

## [](#DESCRIPTION)DESCRIPTION

           Mount a filesystem using a FUSE server that runs as a socket
           service.  These servers can be contained using the platform's
           service management framework.

           The second form checks if there is a FUSE service available for
           the given filesystem type.

## [](#AUTHORS)AUTHORS

           The author of the fuse socket service code is Darrick J. Wong
           <djwong@kernel.org>.  Debian GNU/Linux distribution.

## [](#SEE_ALSO)SEE ALSO

           fusermount3(1) fusermount(1) mount(8) fuse(4)

## [](#COLOPHON)COLOPHON

           This page is part of the libfuse (Filesystem in Userspace)
           project.  Information about the project can be found at 
           ⟨https://github.com/libfuse/libfuse⟩.  If you have a bug report for
           this manual page, see ⟨https://github.com/libfuse/libfuse/issues⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/libfuse/libfuse.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                           fuservicemount3(8)

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
