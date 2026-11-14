---
{"title": "cfdisk(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/cfdisk.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cfdisk(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMANDS](#COMMANDS) \| [COLORS](#COLORS) \| [ENVIRONMENT](#ENVIRONMENT) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CFDISK(8)                 System Administration                 CFDISK(8)

## [](#NAME)NAME

           cfdisk - display or manipulate a disk partition table

## [](#SYNOPSIS)SYNOPSIS

           cfdisk [options] [device]

## [](#DESCRIPTION)DESCRIPTION

           cfdisk is a curses-based program for partitioning any block
           device. The default device is /dev/sda.

           Note that cfdisk provides basic partitioning functionality with a
           user-friendly interface. If you need advanced features, use
           fdisk(8) instead.

           All disk label changes will remain in memory only, and the disk
           will be unmodified until you decide to write your changes. Be
           careful before using the write command.

           Since version 2.25 cfdisk supports MBR (DOS), GPT, SUN and SGI
           disk labels, but no longer provides any functionality for CHS
           (Cylinder-Head-Sector) addressing. CHS has never been important
           for Linux, and this addressing concept does not make any sense for
           new devices.

           Since version 2.25 cfdisk also does not provide a 'print' command
           any more. This functionality is provided by the utilities partx(8)
           and lsblk(8) in a very comfortable and rich way.

           If you want to remove an old partition table from a device, use
           wipefs(8).

## [](#OPTIONS)OPTIONS

           -L, --color[=when]
               Colorize the output. The optional argument when can be auto,
               never or always. If the when argument is omitted, it defaults
               to auto. The colors can be disabled, for the current built-in
               default see --help output. See also the COLORS section.

           --lock[=mode]
               Use an exclusive BSD lock for the device or file that is
               operated upon. The optional argument mode can be yes (1), no
               (0), or nonblock. If the mode argument is omitted, it defaults
               to yes. This option overrides the environment variable
               $LOCK_BLOCK_DEVICE. The default is to not use any lock at all,
               but using a lock is recommended to avoid collisions with
               systemd-udevd(8) or other tools.

           -r, --read-only
               Forced open in read-only mode.

           -b, --sector-size sectorsize
               Specify the sector size of the disk. Valid values are 512,
               1024, 2048, and 4096. The kernel is aware of the sector size
               for regular block devices. Use this option only on very old
               kernels, when working with disk images, or to override the
               kernel’s default sector size. Since util-linux-2.17, fdisk
               distinguishes between logical and physical sector size. This
               option changes both sector sizes to the specified sectorsize.

           -z, --zero
               Start with an in-memory zeroed partition table. This option
               does not zero the partition table on the disk; rather, it
               simply starts the program without reading the existing
               partition table. This option allows you to create a new
               partition table from scratch or from an sfdisk(8)-compatible
               script.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#COMMANDS)COMMANDS

           The commands for cfdisk can be entered by pressing the
           corresponding key (pressing Enter after the command is not
           necessary). Here is a list of the available commands:

           b
               Toggle the bootable flag of the current partition. This allows
               you to select which primary partition is bootable on the
               drive. This command may not be available for all partition
               label types.

           d
               Delete the current partition. This will convert the current
               partition into free space and merge it with any free space
               immediately surrounding the current partition. A partition
               already marked as free space or marked as unusable cannot be
               deleted.

           h
               Show the help screen.

           n
               Create a new partition from free space. cfdisk then prompts
               you for the size of the partition you want to create. The
               default size is equal to the entire available free space at
               the current position.

               The size may be followed by a multiplicative suffix: KiB
               (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB,
               ZiB and YiB (the "iB" is optional, e.g., "K" has the same
               meaning as "KiB").

           q
               Quit the program. This will exit the program without writing
               any data to the disk.

           r
               Reduce or enlarge the current partition. cfdisk then prompts
               you for the new size of the partition. The default size is the
               current size. A partition marked as free space or marked as
               unusable cannot be resized.

               Note that reducing the size of a partition might destroy data
               on that partition.

           s
               Sort the partitions in ascending start-sector order. When
               deleting and adding partitions, it is likely that the
               numbering of the partitions will no longer match their order
               on the disk. This command restores that match.

           t
               Change the partition type. By default, new partitions are
               created as Linux partitions.

           u
               Dump the current in-memory partition table to an
               sfdisk(8)-compatible script file.

               The script files are compatible between cfdisk, fdisk(8)
               sfdisk(8) and other libfdisk applications. For more details
               see sfdisk(8).

               It is also possible to load an sfdisk-script into cfdisk if
               there is no partition table on the device or when you start
               cfdisk with the --zero command-line option.

           W
               Write the partition table to disk (you must enter an uppercase
               W). Since this might destroy data on the disk, you must either
               confirm or deny the write by entering `yes' or `no'. If you
               enter `yes', cfdisk will write the partition table to disk and
               then tell the kernel to re-read the partition table from the
               disk.

               The re-reading of the partition table does not always work. In
               such a case you need to inform the kernel about any new
               partitions by using partprobe(8) or partx(8), or by rebooting
               the system.

           x
               Toggle extra information about a partition.

           Up Arrow, Down Arrow
               Move the cursor to the previous or next partition. If there
               are more partitions than can be displayed on a screen, you can
               display the next (previous) set of partitions by moving down
               (up) at the last (first) partition displayed on the screen.

           Left Arrow, Right Arrow
               Select the preceding or the next menu item. Hitting Enter will
               execute the currently selected item.

           All commands can be entered with either uppercase or lowercase
           letters (except for Write). When in a submenu or at a prompt, you
           can hit the Esc key to return to the main menu.

## [](#COLORS)COLORS

           The output colorization is implemented by terminal-colors.d(5)
           functionality. Implicit coloring can be disabled by an empty file

              /etc/terminal-colors.d/cfdisk.disable

           for the cfdisk command or for all tools by

              /etc/terminal-colors.d/disable

           Since version 2.41, the $NO_COLOR environment variable is also
           supported to disable output colorization unless explicitly enabled
           by a command-line option.

           The user-specific $XDG_CONFIG_HOME/terminal-colors.d or
           $HOME/.config/terminal-colors.d overrides the global setting.

           Note that the output colorization may be enabled by default, and
           in this case terminal-colors.d directories do not have to exist
           yet.

           cfdisk does not support color customization with a color-scheme
           file.

## [](#ENVIRONMENT)ENVIRONMENT

           CFDISK_DEBUG=all
               Enable cfdisk debug output.

           LIBBLKID_DEBUG=all
               Enable libblkid debug output.

           LIBFDISK_DEBUG=all
               Enable libfdisk debug output.

           LIBSMARTCOLS_DEBUG=all
               Enable libsmartcols debug output.

           LIBSMARTCOLS_DEBUG_PADDING=on
               Use visible padding characters.

           LOCK_BLOCK_DEVICE=<mode>
               Use exclusive BSD lock. The mode is "1" or "0". See --lock for
               more details.

## [](#AUTHORS)AUTHORS

           Karel Zak <kzak@redhat.com>

           The current cfdisk implementation is based on the original cfdisk
           from Kevin E. Martin <martin@cs.unc.edu>.

## [](#SEE_ALSO)SEE ALSO

           fdisk(8), parted(8), partprobe(8), partx(8), sfdisk(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The cfdisk command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                      CFDISK(8)

------------------------------------------------------------------------

Pages that refer to this page: [fdisk(8)](../man8/fdisk.8.html),  [sfdisk(8)](../man8/sfdisk.8.html)

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
