---
{"title": "FAT_IOCTL_GET_VOLUME_ID(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/FAT_IOCTL_GET_VOLUME_ID.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# FAT_IOCTL_GET_VOLUME_ID(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FAT_IOCTL_GET_VOLUME_ID(2const)           FAT_IOCTL_GET_VOLUME_ID(2const)

## [](#NAME)NAME

           FAT_IOCTL_GET_VOLUME_ID - read the volume ID in a FAT filesystem

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/msdos_fs.h>  /* Definition of FAT_* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, FAT_IOCTL_GET_VOLUME_ID, uint32_t *id);

## [](#DESCRIPTION)DESCRIPTION

           FAT filesystems are identified by a volume ID.  The volume ID can
           be read with FAT_IOCTL_GET_VOLUME_ID.

           The fd argument can be a file descriptor for any file or directory
           of the filesystem.  It is sufficient to create the file descriptor
           by calling open(2) with the O_RDONLY flag.

           The id argument is a pointer to the field that will be filled with
           the volume ID.  Typically the volume ID is displayed to the user
           as a group of two 16-bit fields:

               printf("Volume ID %04x-%04x\n", id >> 16, id & 0xFFFF);

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 3.11.

## [](#EXAMPLES)EXAMPLES

           The following program demonstrates the use of ioctl(2) to display
           the volume ID of a FAT filesystem.

           The following output was recorded when applying the program for
           directory /mnt/user:

               $ ./display_fat_volume_id /mnt/user
               Volume ID 6443-6241

       Program source (display_fat_volume_id.c)

           #include <fcntl.h>
           #include <linux/msdos_fs.h>
           #include <stdint.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <sys/ioctl.h>
           #include <unistd.h>

           int
           main(int argc, char *argv[])
           {
               int       fd;
               int       ret;
               uint32_t  id;

               if (argc != 2) {
                   printf("Usage: %s FILENAME\n", argv[0]);
                   exit(EXIT_FAILURE);
               }

               fd = open(argv[1], O_RDONLY);
               if (fd == -1) {
                   perror("open");
                   exit(EXIT_FAILURE);
               }

               /*
                * Read volume ID.
                */
               ret = ioctl(fd, FAT_IOCTL_GET_VOLUME_ID, &id);
               if (ret == -1) {
                   perror("ioctl");
                   exit(EXIT_FAILURE);
               }

               /*
                * Format the output as two groups of 16 bits each.
                */
               printf("Volume ID %04x-%04x\n", id >> 16, id & 0xFFFF);

               close(fd);

               exit(EXIT_SUCCESS);
           }

## [](#SEE_ALSO)SEE ALSO

           ioctl(2), ioctl_fat(2)

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

    Linux man-pages 6.19            2025-05-17FAT_IOCTL_GET_VOLUME_ID(2const)

------------------------------------------------------------------------

Pages that refer to this page: [ioctl_fat(2)](../man2/ioctl_fat.2.html)

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
