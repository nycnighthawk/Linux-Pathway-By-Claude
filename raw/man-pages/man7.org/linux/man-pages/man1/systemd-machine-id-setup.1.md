---
{"title": "systemd-machine-id-setup(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-machine-id-setup.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-machine-id-setup(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-M...-ID-SETUP(1) systemd-machine-id-setupSYSTEMD-M...-ID-SETUP(1)

## [](#NAME)NAME

           systemd-machine-id-setup - Initialize the machine ID in
           /etc/machine-id

## [](#SYNOPSIS)SYNOPSIS

           systemd-machine-id-setup

## [](#DESCRIPTION)DESCRIPTION

           systemd-machine-id-setup may be used by system installer tools to
           initialize the machine ID stored in /etc/machine-id at install
           time, with a provisioned or randomly generated ID. See
           machine-id(5) for more information about this file.

           If the tool is invoked without the --commit switch,
           /etc/machine-id is initialized with a valid, new machine ID if it
           is missing or empty. The new machine ID will be acquired in the
           following fashion:

            1. If a valid machine ID is stored in /run/machine-id, the
               machine ID is copied and used to initialize the machine ID in
               /etc/machine-id. This step is skipped if --root= is specified
               or running in a chroot environment.

            2. If a valid D-Bus machine ID is already configured for the
               system, the D-Bus machine ID is copied and used to initialize
               the machine ID in /etc/machine-id.

            3. If a valid machine ID is provided through system.machine_id
               credential, the machine ID is copied and used to initialize
               the machine ID in /etc/machine-id. This step is skipped if
               --root= is specified or running in a chroot environment.

            4. If run inside a KVM virtual machine and a UUID is configured
               (via the -uuid option), this UUID is used to initialize the
               machine ID. The caller must ensure that the UUID passed is
               sufficiently unique and is different for every booted instance
               of the VM. This step is skipped if --root= is specified or
               running in a chroot environment.

            5. Similarly, if run inside a Linux container environment and a
               UUID is configured for the container, this is used to
               initialize the machine ID. For details, see the documentation
               of the Container Interface[1]. This step is skipped if --root=
               is specified or running in a chroot environment.

            6. Otherwise, a new ID is randomly generated.

           The --commit switch may be used to commit a transient machined ID
           to disk, making it persistent. For details, see below.

           Use systemd-firstboot(1) to initialize the machine ID on mounted
           (but not booted) system images.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --root=path
               Takes a directory path as argument. All paths operated on will
               be prefixed with the given alternate root path, including the
               path for /etc/machine-id itself.

               Added in version 212.

           --image=path
               Takes a path to a device node or regular file as argument.
               This is similar to --root= as described above, but operates on
               a disk image instead of a directory tree.

               Added in version 249.

           --image-policy=policy
               Takes an image policy string as argument, as per
               systemd.image-policy(7). The policy is enforced when operating
               on the disk image specified via --image=, see above. If not
               specified, defaults to the "*" policy, i.e. all recognized
               file systems in the image are used.

           --commit
               Commit a transient machine ID to disk. This command may be
               used to convert a transient machine ID into a persistent one.
               A transient machine ID file is one that was bind mounted from
               a memory file system (usually "tmpfs") to /etc/machine-id
               during the early phase of the boot process. This may happen
               because /etc/ is initially read-only and was missing a valid
               machine ID file at that point.

               This command will execute no operation if /etc/machine-id is
               not mounted from a memory file system, or if /etc/ is
               read-only. The command will write the current transient
               machine ID to disk and unmount the /etc/machine-id mount point
               in a race-free manner to ensure that this file is always valid
               and accessible for other processes.

               This command is primarily used by the
               systemd-machine-id-commit.service(8) early boot service.

               Added in version 227.

           --print
               Print the machine ID generated or committed after the
               operation is complete.

               Added in version 231.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), machine-id(5), systemd-machine-id-commit.service(8),
           dbus-uuidgen(1), systemd-firstboot(1)

## [](#NOTES)NOTES

            1. Container Interface
               https://systemd.io/CONTAINER_INTERFACE

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

    systemd 262~devel                                SYSTEMD-M...-ID-SETUP(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [machine-id(5)](../man5/machine-id.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-machine-id-commit.service(8)](../man8/systemd-machine-id-commit.service.8.html)

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
