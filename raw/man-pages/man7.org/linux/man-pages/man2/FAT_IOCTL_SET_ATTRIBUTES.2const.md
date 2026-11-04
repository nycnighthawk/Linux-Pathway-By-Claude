---
{"title": "FAT_IOCTL_SET_ATTRIBUTES(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/FAT_IOCTL_SET_ATTRIBUTES.2const.html", "retrieved": "2026-11-01", "license": "various (per page)"}
---

# FAT_IOCTL_SET_ATTRIBUTES(2const) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FAT_IOCTL_SET_ATTRIBUTES(2const)         FAT_IOCTL_SET_ATTRIBUTES(2const)

## [](#NAME)NAME

           FAT_IOCTL_GET_ATTRIBUTES, FAT_IOCTL_SET_ATTRIBUTES - get and set
           file attributes in a FAT filesystem

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/msdos_fs.h>  /* Definition of FAT_* and
                                           ATTR_* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, FAT_IOCTL_GET_ATTRIBUTES, uint32_t *attr);
           int ioctl(int fd, FAT_IOCTL_SET_ATTRIBUTES, uint32_t *attr);

## [](#DESCRIPTION)DESCRIPTION

           Files and directories in the FAT filesystem possess an attribute
           bit mask that can be read with FAT_IOCTL_GET_ATTRIBUTES and
           written with FAT_IOCTL_SET_ATTRIBUTES.

           The fd argument contains a file descriptor for a file or
           directory.  It is sufficient to create the file descriptor by
           calling open(2) with the O_RDONLY flag.

           The attr argument contains a pointer to a bit mask.  The bits of
           the bit mask are:

           ATTR_RO
                  This bit specifies that the file or directory is read-only.

           ATTR_HIDDEN
                  This bit specifies that the file or directory is hidden.

           ATTR_SYS
                  This bit specifies that the file is a system file.

           ATTR_VOLUME
                  This bit specifies that the file is a volume label.  This
                  attribute is read-only.

           ATTR_DIR
                  This bit specifies that this is a directory.  This
                  attribute is read-only.

           ATTR_ARCH
                  This bit indicates that this file or directory should be
                  archived.  It is set when a file is created or modified.
                  It is reset by an archiving system.

           The zero value ATTR_NONE can be used to indicate that no attribute
           bit is set.

## [](#RETURN_VALUE)RETURN VALUE

           On success, 0 is returned.  On error, -1 is returned, and errno is
           set to indicate the error.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.6.12.

## [](#EXAMPLES)EXAMPLES

           The following program demonstrates the usage of ioctl(2) to
           manipulate file attributes.  The program reads and displays the
           archive attribute of a file.  After inverting the value of the
           attribute, the program reads and displays the attribute again.

           The following was recorded when applying the program for the file
           /mnt/user/foo:

               # ./toggle_fat_archive_flag /mnt/user/foo
               Archive flag is set
               Toggling archive flag
               Archive flag is not set

       Program source (toggle_fat_archive_flag.c)

           #include <fcntl.h>
           #include <linux/msdos_fs.h>
           #include <stdint.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <sys/ioctl.h>
           #include <unistd.h>

           /*
            * Read file attributes of a file on a FAT filesystem.
            * Output the state of the archive flag.
            */
           static uint32_t
           readattr(int fd)
           {
               int       ret;
               uint32_t  attr;

               ret = ioctl(fd, FAT_IOCTL_GET_ATTRIBUTES, &attr);
               if (ret == -1) {
                   perror("ioctl");
                   exit(EXIT_FAILURE);
               }

               if (attr & ATTR_ARCH)
                   printf("Archive flag is set\n");
               else
                   printf("Archive flag is not set\n");

               return attr;
           }

           int
           main(int argc, char *argv[])
           {
               int       fd;
               int       ret;
               uint32_t  attr;

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
                * Read and display the FAT file attributes.
                */
               attr = readattr(fd);

               /*
                * Invert archive attribute.
                */
               printf("Toggling archive flag\n");
               attr ^= ATTR_ARCH;

               /*
                * Write the changed FAT file attributes.
                */
               ret = ioctl(fd, FAT_IOCTL_SET_ATTRIBUTES, &attr);
               if (ret == -1) {
                   perror("ioctl");
                   exit(EXIT_FAILURE);
               }

               /*
                * Read and display the FAT file attributes.
                */
               readattr(fd);

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

    Linux man-pages 6.19            2025-05-17FAT_IOCTL_SET_ATTRIBUTES(2const)

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
