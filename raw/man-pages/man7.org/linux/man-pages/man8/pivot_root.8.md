---
{"title": "pivot_root(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pivot_root.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pivot_root(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PIVOT_ROOT(8)             System Administration             PIVOT_ROOT(8)

## [](#NAME)NAME

           pivot_root - change the root filesystem

## [](#SYNOPSIS)SYNOPSIS

           pivot_root new_root put_old

## [](#DESCRIPTION)DESCRIPTION

           pivot_root moves the root filesystem of the calling process to the
           directory put_old and makes new_root the new root filesystem.
           Since pivot_root(8) simply calls pivot_root(2), we refer to the
           man page of the latter for further details.

           Note that, depending on the implementation of pivot_root, root and
           current working directory of the caller may or may not change. The
           following is a sequence for invoking pivot_root that works in
           either case, assuming that pivot_root and chroot are in the
           current PATH:

               cd new_root
               pivot_root . put_old
               exec chroot . command

           Note that chroot must be available under the old root and under
           the new root, because pivot_root may or may not have implicitly
           changed the root directory of the shell.

           Note that exec chroot changes the running executable, which is
           necessary if the old root directory should be unmounted
           afterwards. Also note that standard input, output, and error may
           still point to a device on the old root filesystem, keeping it
           busy. They can easily be changed when invoking chroot (see below;
           note the absence of leading slashes to make it work whether
           pivot_root has changed the shell’s root or not).

## [](#OPTIONS)OPTIONS

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#EXAMPLE)EXAMPLE

           Change the root filesystem to /dev/hda1 from an interactive shell:

               mount /dev/hda1 /new-root
               cd /new-root
               pivot_root . old-root
               exec chroot . sh <dev/console >dev/console 2>&1
               umount /old-root

           Mount the new root filesystem over NFS from 10.0.0.1:/my_root and
           run init:

               ifconfig lo 127.0.0.1 up   # for portmap
               # configure Ethernet or such
               portmap   # for lockd (implicitly started by mount)
               mount -o ro 10.0.0.1:/my_root /mnt
               killall portmap   # portmap keeps old root busy
               cd /mnt
               pivot_root . old_root
               exec chroot . sh -c 'umount /old_root; exec /sbin/init' \
                 <dev/console >dev/console 2>&1

## [](#SEE_ALSO)SEE ALSO

           chroot(1), pivot_root(2), mount(8), switch_root(8), umount(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The pivot_root command is part of the util-linux package which can
           be downloaded from Linux Kernel Archive
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

    util-linux 2.43.devel-739-eee2e 2026-05-24                  PIVOT_ROOT(8)

------------------------------------------------------------------------

Pages that refer to this page: [pivot_root(2)](../man2/pivot_root.2.html),  [initrd(4)](../man4/initrd.4.html),  [lxc.container.conf(5)](../man5/lxc.container.conf.5.html),  [mount_namespaces(7)](../man7/mount_namespaces.7.html),  [pivot_root(8)](../man8/pivot_root.8.html)

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
