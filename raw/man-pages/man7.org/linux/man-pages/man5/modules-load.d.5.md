---
{"title": "modules-load.d(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/modules-load.d.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# modules-load.d(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION FORMAT](#CONFIGURATION_FORMAT) \| [CONFIGURATION DIRECTORIES AND PRECEDENCE](#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MODULES-LOAD.D(5)             modules-load.d            MODULES-LOAD.D(5)

## [](#NAME)NAME

           modules-load.d - Configure kernel modules to load at boot

## [](#SYNOPSIS)SYNOPSIS

               /etc/modules-load.d/*.conf
               /run/modules-load.d/*.conf
               /usr/local/lib/modules-load.d/*.conf
               /usr/lib/modules-load.d/*.conf

## [](#DESCRIPTION)DESCRIPTION

           systemd-modules-load.service(8) reads files from the above
           directories which contain kernel modules to load during boot in a
           static list. Each configuration file is named in the style of
           /etc/modules-load.d/program.conf. Note that it is usually a better
           idea to rely on the automatic module loading by PCI IDs, USB IDs,
           DMI IDs or similar triggers encoded in the kernel modules
           themselves instead of static configuration like this. In fact,
           most modern kernel modules are prepared for automatic loading
           already.

## [](#CONFIGURATION_FORMAT)CONFIGURATION FORMAT

           The configuration files should simply contain a list of kernel
           module names to load, separated by newlines. Empty lines and lines
           whose first non-whitespace character is # or ; are ignored.

## [](#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE)CONFIGURATION DIRECTORIES AND PRECEDENCE

           Configuration files are read from directories in /etc/, /run/,
           /usr/local/lib/, and /usr/lib/, in order of precedence, as listed
           in the SYNOPSIS section above. Files must have the ".conf"
           extension. Files in /etc/ override files with the same name in
           /run/, /usr/local/lib/, and /usr/lib/. Files in /run/ override
           files with the same name under /usr/.

           All configuration files are sorted by their filename in
           lexicographic order, regardless of which of the directories they
           reside in. If multiple files specify the same option, the entry in
           the file with the lexicographically latest name will take
           precedence. Thus, the configuration in a certain file may either
           be replaced completely (by placing a file with the same name in a
           directory with higher priority), or individual settings might be
           changed (by specifying additional settings in a file with a
           different name that is ordered later).

           Packages should install their configuration files in /usr/lib/
           (distribution packages) or /usr/local/lib/ (local installs) [1].
           Files in /etc/ are reserved for the local administrator, who may
           use this logic to override the configuration files installed by
           vendor packages.

           It is recommended to prefix all filenames with a two-digit number
           and a dash to simplify the ordering. It is recommended to use the
           range 10-40 for configuration files in /usr/ and the range 60-90
           for configuration files in /etc/ and /run/, to make sure that
           local and transient configuration files will always take priority
           over configuration files shipped by the OS vendor.

           If the administrator wants to disable a configuration file
           supplied by the vendor, the recommended way is to place a symlink
           to /dev/null in the configuration directory in /etc/, with the
           same filename as the vendor configuration file. If the vendor
           configuration file is included in the initrd image, the image has
           to be regenerated.

## [](#EXAMPLE)EXAMPLE

           Example 1. /etc/modules-load.d/virtio-net.conf example:

               # Load virtio-net.ko at boot
               virtio-net

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-modules-load.service(8), systemd-delta(1),
           modprobe(8)

## [](#NOTES)NOTES

            1. 💣💥🧨💥💥💣 Please note that those configuration files must
               be available at all times. If /usr/local/ is a separate
               partition, it may not be available during early boot, and must
               not be used for configuration.

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

    systemd 262~devel                                       MODULES-LOAD.D(5)

------------------------------------------------------------------------

Pages that refer to this page: [sysctl.d(5)](../man5/sysctl.d.5.html),  [systemd.network(5)](../man5/systemd.network.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-modules-load.service(8)](../man8/systemd-modules-load.service.8.html)

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
