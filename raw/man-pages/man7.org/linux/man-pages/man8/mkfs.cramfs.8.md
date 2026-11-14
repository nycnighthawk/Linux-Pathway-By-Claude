---
{"title": "mkfs.cramfs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mkfs.cramfs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mkfs.cramfs(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MKFS.CRAMFS(8)            System Administration            MKFS.CRAMFS(8)

## [](#NAME)NAME

           mkfs.cramfs - make compressed ROM filesystem

## [](#SYNOPSIS)SYNOPSIS

           mkfs.cramfs [options] directory file

## [](#DESCRIPTION)DESCRIPTION

           Files on cramfs filesystems are zlib-compressed one page at a time
           to allow random read access. The metadata is not compressed, but
           is expressed in a terse representation that is more
           space-efficient than conventional filesystems.

           The filesystem is intentionally read-only to simplify its design;
           random write access for compressed files is difficult to
           implement. cramfs ships with a utility (mkcramfs(8)) to pack files
           into new cramfs images.

           File sizes are limited to less than 16 MB.

           Maximum filesystem size is a little under 272 MB. (The last file
           on the filesystem must begin before the 256 MB block, but can
           extend past it.)

## [](#ARGUMENTS)ARGUMENTS

           The directory is simply the root of the directory tree that we
           want to generate a compressed filesystem out of.

           The file will contain the cram filesystem, which later can be
           mounted.

## [](#OPTIONS)OPTIONS

           -v
               Enable verbose messaging.

           -E
               Treat all warnings as errors, which are reflected as command
               exit status.

           -b blocksize
               Use defined block size, which has to be divisible by page
               size.

           -e edition
               Use defined filesystem edition number in superblock.

           -N big|little|host
               Use the specified endianness. The default is host.

           -i file
               Insert a file to cramfs filesystem.

           -n name
               Set name of the cramfs filesystem.

           -p
               Pad by 512 bytes for boot code.

           -s
               This option is ignored. Originally the -s turned on directory
               entry sorting.

           -z
               Make explicit holes.

           -l[=mode]
               Use an exclusive BSD lock for the device or file that is
               operated upon. The optional argument mode can be yes (1), no
               (0), or nonblock. If the mode argument is omitted, it defaults
               to yes. This option overrides the environment variable
               $LOCK_BLOCK_DEVICE. The default is to not use any lock at all,
               but using a lock is recommended to avoid collisions with
               systemd-udevd(8) or other tools.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           LOCK_BLOCK_DEVICE=<mode>
               Use exclusive BSD lock. The mode is "1" or "0". See -l for
               more details.

## [](#EXIT_STATUS)EXIT STATUS

           0
               success

           8
               operation error, such as unable to allocate memory

## [](#SEE_ALSO)SEE ALSO

           fsck.cramfs(8), mount(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The mkfs.cramfs command is part of the util-linux package which
           can be downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                 MKFS.CRAMFS(8)

------------------------------------------------------------------------

Pages that refer to this page: [fsck.cramfs(8)](../man8/fsck.cramfs.8.html),  [systemd-makefs@.service(8)](../man8/systemd-makefs@.service.8.html)

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
