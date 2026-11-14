---
{"title": "VFAT_IOCTL_READDIR_BOTH(2const) — Linux manual page", "url": "https://man7.org/linux/man-pages/man2/vfat_ioctl_readdir_both.2const.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# VFAT_IOCTL_READDIR_BOTH(2const) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [LIBRARY](#LIBRARY) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [RETURN VALUE](#RETURN_VALUE) \| [ERRORS](#ERRORS) \| [STANDARDS](#STANDARDS) \| [HISTORY](#HISTORY) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    VFAT_IOCTL_READDIR_BOTH(2const)           VFAT_IOCTL_READDIR_BOTH(2const)

## [](#NAME)NAME

           VFAT_IOCTL_READDIR_BOTH, VFAT_IOCTL_READDIR_SHORT - read filenames
           of a directory in a FAT filesystem

## [](#LIBRARY)LIBRARY

           Standard C library (libc, -lc)

## [](#SYNOPSIS)SYNOPSIS

           #include <linux/msdos_fs.h>  /* Definition of VFAT_* constants */
           #include <sys/ioctl.h>

           int ioctl(int fd, VFAT_IOCTL_READDIR_BOTH,
                     struct __fat_dirent entry[2]);
           int ioctl(int fd, VFAT_IOCTL_READDIR_SHORT,
                     struct __fat_dirent entry[2]);

## [](#DESCRIPTION)DESCRIPTION

           A file or directory on a FAT filesystem always has a short
           filename consisting of up to 8 capital letters, optionally
           followed by a period and up to 3 capital letters for the file
           extension.  If the actual filename does not fit into this scheme,
           it is stored as a long filename of up to 255 UTF-16 characters.

           The short filenames in a directory can be read with
           VFAT_IOCTL_READDIR_SHORT.  VFAT_IOCTL_READDIR_BOTH reads both the
           short and the long filenames.

           The fd argument must be a file descriptor for a directory.  It is
           sufficient to create the file descriptor by calling open(2) with
           the O_RDONLY flag.  The file descriptor can be used only once to
           iterate over the directory entries by calling ioctl(2) repeatedly.

           The entry argument is a two-element array of the following
           structures:

               struct __fat_dirent {
                   long            d_ino;
                   __kernel_off_t  d_off;
                   uint32_t short  d_reclen;
                   char            d_name[256];
               };

           The first entry in the array is for the short filename.  The
           second entry is for the long filename.

           The d_ino and d_off fields are filled only for long filenames.
           The d_ino field holds the inode number of the directory.  The
           d_off field holds the offset of the file entry in the directory.
           As these values are not available for short filenames, the user
           code should simply ignore them.

           The field d_reclen contains the length of the filename in the
           field d_name.  To keep backward compatibility, a length of 0 for
           the short filename signals that the end of the directory has been
           reached.  However, the preferred method for detecting the end of
           the directory is to test the ioctl(2) return value.  If no long
           filename exists, field d_reclen is set to 0 and d_name is a
           character string of length 0 for the long filename.

## [](#RETURN_VALUE)RETURN VALUE

           A return value of 1 signals that a new directory entry has been
           read and a return value of 0 signals that the end of the directory
           has been reached.

           On error, -1 is returned, and errno is set to indicate the error.

## [](#ERRORS)ERRORS

           ENOENT fd refers to a removed, but still open directory.

           ENOTDIR
                  fd does not refer to a directory.

## [](#STANDARDS)STANDARDS

           Linux.

## [](#HISTORY)HISTORY

           Linux 2.0.

## [](#EXAMPLES)EXAMPLES

           The following program demonstrates the use of ioctl(2) to list a
           directory.

           The following was recorded when applying the program to the
           directory /mnt/user:

               $ ./fat_dir /mnt/user;
               . -> ''
               .. -> ''
               ALONGF~1.TXT -> 'a long filename.txt'
               UPPER.TXT -> ''
               LOWER.TXT -> 'lower.txt'

       Program source
           #include <fcntl.h>
           #include <linux/msdos_fs.h>
           #include <stdio.h>
           #include <stdlib.h>
           #include <sys/ioctl.h>
           #include <unistd.h>

           int
           main(int argc, char *argv[])
           {
               int                  fd;
               int                  ret;
               struct __fat_dirent  entry[2];

               if (argc != 2) {
                   printf("Usage: %s DIRECTORY\n", argv[0]);
                   exit(EXIT_FAILURE);
               }

               /*
                * Open file descriptor for the directory.
                */
               fd = open(argv[1], O_RDONLY | O_DIRECTORY);
               if (fd == -1) {
                   perror("open");
                   exit(EXIT_FAILURE);
               }

               for (;;) {

                   /*
                    * Read next directory entry.
                    */
                   ret = ioctl(fd, VFAT_IOCTL_READDIR_BOTH, entry);

                   /*
                    * If an error occurs, the return value is -1.
                    * If the end of the directory list has been reached,
                    * the return value is 0.
                    * For backward compatibility the end of the directory
                    * list is also signaled by d_reclen == 0.
                    */
                   if (ret < 1)
                       break;

                   /*
                    * Write both the short name and the long name.
                    */
                   printf("%s -> '%s'\n", entry[0].d_name, entry[1].d_name);
               }

               if (ret == -1) {
                   perror("VFAT_IOCTL_READDIR_BOTH");
                   exit(EXIT_FAILURE);
               }

               /*
                * Close the file descriptor.
                */
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

    Linux man-pages 6.19            2025-09-21VFAT_IOCTL_READDIR_BOTH(2const)

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
