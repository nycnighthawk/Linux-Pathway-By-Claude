---
{"title": "fusermount3(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/fusermount3.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fusermount3(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [HOMEPAGE](#HOMEPAGE) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FUSERMOUNT3(1)        Filesystem in Userspace (FUSE)       FUSERMOUNT3(1)

## [](#NAME)NAME

           fusermount3 - mount and unmount FUSE filesystems

## [](#SYNOPSIS)SYNOPSIS

           fusermount3 [OPTIONS] MOUNTPOINT

## [](#DESCRIPTION)DESCRIPTION

           Filesystem in Userspace (FUSE) is a simple interface for userspace
           programs to export a virtual filesystem to the Linux kernel. It
           provides a secure method for non privileged users to create and
           mount their own filesystem implementations.

           fusermount3 is a program to mount and unmount FUSE filesystems. It
           should be called directly only for unmounting FUSE file systems.
           To allow mounting and unmounting by unprivileged users,
           fusermount3 needs to be installed set-uid root.

## [](#OPTIONS)OPTIONS

           -h  print help.

           -V  print version.

           -o OPTION[,OPTION...]
               mount options.

           -u  unmount.

           -q  quiet.

           -z  lazy unmount.

## [](#SEE_ALSO)SEE ALSO

           mount(8), mount.fuse3(8), fuse(4),

## [](#HOMEPAGE)HOMEPAGE

           More information about fusermount3 and the FUSE project can be
           found at <https://github.com/libfuse/ >.

## [](#AUTHORS)AUTHORS

           FUSE is currently maintained by Nikolaus Rath <Nikolaus@rath.org>

           The original author of FUSE is Miklos Szeredi <miklos@szeredi.hu>.

           This manual page was originally written by Daniel Baumann
           <daniel.baumann@progress-technologies.net>.

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

    2.8.6                           2011-10-23                 FUSERMOUNT3(1)

------------------------------------------------------------------------

Pages that refer to this page: [fuservicemount3(8)](../man8/fuservicemount3.8.html),  [mount.fuse3(8)](../man8/mount.fuse3.8.html)

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
