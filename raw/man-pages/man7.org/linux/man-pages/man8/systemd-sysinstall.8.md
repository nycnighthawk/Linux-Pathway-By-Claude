---
{"title": "systemd-sysinstall(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-sysinstall.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-sysinstall(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-SYSINSTALL(8)       systemd-sysinstall      SYSTEMD-SYSINSTALL(8)

## [](#NAME)NAME

           systemd-sysinstall, systemd-sysinstall.service - Simple OS
           installer

## [](#SYNOPSIS)SYNOPSIS

           systemd-sysinstall [OPTIONS...] [BLOCKDEVICE]

           systemd-sysinstall.service

## [](#DESCRIPTION)DESCRIPTION

           systemd-sysinstall is a simple terminal and command line based
           operating system installer tool. Its primary use-case is to act as
           an automatically started interactive interface when booting from
           an installer medium (e.g. a USB stick), in order to install an OS
           onto a target disk. However, it may also be invoked directly from
           a shell. It executes the following steps:

            1. It prompts the user for the target disk to install the OS on.
               (Unless the block device is already specified on the command
               line.)

            2. It validates whether the disk is suitable (i.e. large enough,
               and with enough free/unpartitioned space) for an OS
               installation. If it is generally suitable the user is prompted
               if they want to erase the disk before installation, or if the
               OS shall be added to the existing partitions on the disk (the
               latter only if enough free/unpartitioned disk space is
               available).

            3. It prompts the user whether to register the newly installed OS
               with the firmware boot option menu.

            4. It requests confirmation from the user, after showing a
               summary of the planned OS installation.

            5. It invokes systemd-creds(1)'s encrypt command in order to
               generate encrypted (TPM locked, if available) system
               credential files for a few, very basic system settings of the
               currently booted system (locale, keymap, timezone), which it
               will install on the target disk, parameterizing the invoked
               kernel. (Or in other words, it prepares that some settings
               already in effect on the installer system are propagated
               securely onto the new installation.)

            6. It invokes systemd-repart(8) with a definitions directory of
               /usr/lib/repart.sysinstall.d/ (only if populated – if not will
               use the default of /usr/lib/repart.d/). This is supposed to
               set up the basic OS partition structure on the target disk and
               copies in basic OS partitions (most importantly the /usr/
               hierarchy).

            7. It invokes bootctl(1)'s link command to install an OS kernel
               image onto the target disk's ESP/XBOOTLDR, together with the
               credential files prepared earlier.

            8. It invokes bootctl(1)'s install command to install the
               systemd-boot(7) boot loader onto the target disk's ESP.

            9. After confirmation, it reboots the system.

           Note that the prompts/confirmation may be disabled via the command
           line, enabling fully automatic, non-interactive installation. See
           below.

           Note this tool does not interactively query the user for a user to
           create or a root password to be set on the target system, under
           the assumption these questions are better prompted from within the
           newly installed system's first boot process, for example via the
           systemd-firstboot(1) or systemd-homed-firstboot.service
           components. Note that if required such settings may be propagated
           explicitly via the --load-credential= switch below.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --definitions=
               Overrides the directory where systemd-repart shall read its
               partition definitions from, in place of the default of
               /usr/lib/repart.sysinstall.d/.

               Added in version 261.

           --welcome=
               Takes a boolean argument. Controls whether to show the brief
               welcome text normally displayed at the beginning of the
               installation. Defaults to true.

               Added in version 261.

           --chrome=
               Takes a boolean argument. Controls whether to show the colored
               bars at the top and bottom of the terminal interface. Defaults
               to true.

               Added in version 261.

           --erase=
               Takes a boolean argument. Controls whether to erase the
               current contents of the target disk. If this switch is not
               used the user is prompted.

               Added in version 261.

           --confirm=
               Takes a boolean argument. Controls whether to interactively
               query the user for confirmation before initiating the OS
               installation. Defaults to true.

               Added in version 261.

           --reboot=
               Takes a boolean argument. Controls whether to reboot the
               system after completing the installation. Defaults to false.

               Added in version 261.

           --variables=
               Takes a boolean argument. Controls whether to register the
               installed boot loader in the firmware's boot options database.
               If not specified the user will be prompted.

               Added in version 261.

           --summary=
               Takes a boolean argument. Controls whether to show a summary
               of the choices made before asking for confirmation to proceed
               with the OS installation. Defaults to true.

               Added in version 261.

           --kernel=
               Takes a path to a unified kernel image (UKI). Explicitly
               selects the kernel image to install on the target disk. If
               unspecified the currently booted kernel image is installed on
               the target disk.

               Added in version 261.

           --set-credential=id:value
               Accepts an additional system credential to encrypt (with a key
               generated on the local TPM, if available, and the null key
               otherwise) and place next to the installed kernel image in the
               ESP. This may be used to parameterize the installed kernel
               with arbitrary system credentials. Do not use this switch for
               sensitive data (such as passwords), use --load-credential=
               instead, see below. May be used multiple times to configure
               multiple credentials.

               Note that three system credentials are propagated in similar
               fashion to the target system: the locale, keymap and timezone.
               This may be controlled by the relevant --copy-locale=,
               --copy-keymap= and --copy-timezone= options below.

               See systemd.system-credentials(7) for a list of well-known
               system credentials that may be propagated this way. (Note that
               you may pass arbitrary additional credentials this way, that
               can be consumed by any service of your choice, via the usual
               system credentials logic.)

               Added in version 261.

           --load-credential=id:path
               Similar to --set-credential= but reads the credential value
               from a file on disk or an AF_UNIX socket in the file system.
               This is generally preferable for sensitive data, such as
               passwords.

               Added in version 261.

           --copy-locale=, --copy-keymap=, --copy-timezone=
               These options take boolean parameters. They control whether
               the indicated system settings shall be propagated from the
               currently running system into the new target OS installation.
               These options default to true.

               Typically, these three settings are the minimal settings that
               need to be configured during early boot of an installer medium
               in order to make the installer tool accessible to the user.
               The systemd-firstboot(1) tool may be used to query the user
               interactively when the OS install medium is booted for these
               properties. By propagating these settings to the target
               installation via system credentials they do not need to be
               queried again on first boot of the new installation.

               Added in version 261.

           --mute-console=
               Takes a boolean argument. Controls whether to disable kernel
               and service manager log output to the console the installer is
               invoked on temporarily while running, in order to avoid
               interleaved output. Defaults to false.

               Added in version 261.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, and a non-zero failure code otherwise.

## [](#EXAMPLE)EXAMPLE

           Example 1. Invoke the tool for a fully automatic non-interactive
           OS installation

               systemd-sysinstall \
                       /dev/disk/by-id/nvme-Micron_MTFDKBA1T0TFH_214532D0CDA5 \
                       --erase=yes \
                       --confirm=no \
                       --variables=yes \
                       --load-credential=ssh.authorized_keys.root:my-ssh-key

           This installs the OS on the selected disk, erasing any previous
           contents, without confirmation, registers it in the firmware, and
           drops in the SSH key for the root user, read from the my-ssh-key
           file in the current directory.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-creds(1), systemd-repart(8), bootctl(1),
           systemd-firstboot(1), systemd-boot(7),
           systemd.system-credentials(7)

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

    systemd 262~devel                                   SYSTEMD-SYSINSTALL(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
