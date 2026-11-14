---
{"title": "systemd.automount(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/systemd.automount.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.automount(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTOMATIC DEPENDENCIES](#AUTOMATIC_DEPENDENCIES) \| [FSTAB](#FSTAB) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD.AUTOMOUNT(5)        systemd.automount        SYSTEMD.AUTOMOUNT(5)

## [](#NAME)NAME

           systemd.automount - Automount unit configuration

## [](#SYNOPSIS)SYNOPSIS

           automount.automount

## [](#DESCRIPTION)DESCRIPTION

           A unit configuration file whose name ends in ".automount" encodes
           information about a file system automount point controlled and
           supervised by systemd. Automount units may be used to implement
           on-demand mounting as well as parallelized mounting of file
           systems.

           This man page lists the configuration options specific to this
           unit type. See systemd.unit(5) for the common options of all unit
           configuration files. The common configuration items are configured
           in the generic [Unit] and [Install] sections. The automount
           specific configuration options are configured in the [Automount]
           section.

           Automount units must be named after the automount directories they
           control. Example: the automount point /home/lennart must be
           configured in a unit file home-lennart.automount. For details
           about the escaping logic used to convert a file system path to a
           unit name see systemd.unit(5). Note that automount units cannot be
           templated, nor is it possible to add multiple names to an
           automount unit by creating symlinks to its unit file.

           For each automount unit file a matching mount unit file (see
           systemd.mount(5) for details) must exist which is activated when
           the automount path is accessed. Example: if an automount unit
           home-lennart.automount is active and the user accesses
           /home/lennart the mount unit home-lennart.mount will be activated.

           Note that automount units are separate from the mount itself, so
           you should not set After= or Requires= for mount dependencies
           here. For example, you should not set After=network-online.target
           or similar on network filesystems. Doing so may result in an
           ordering cycle.

           Note that automount support on Linux is privileged, automount
           units are hence only available in the system service manager (and
           root's user service manager), but not in unprivileged users'
           service managers.

           Note that automount units should not be nested. (The establishment
           of the inner automount point would unconditionally pin the outer
           mount point, defeating its purpose.)

## [](#AUTOMATIC_DEPENDENCIES)AUTOMATIC DEPENDENCIES

       Implicit Dependencies
           The following dependencies are implicitly added:

           •   If an automount unit is beneath another mount unit in the file
               system hierarchy, a requirement and ordering dependencies are
               created to the on the unit higher in the hierarchy.

           •   An implicit Before= dependency is created between an automount
               unit and the mount unit it activates.

       Default Dependencies
           The following dependencies are added unless DefaultDependencies=no
           is set:

           •   Automount units acquire automatic Before= and Conflicts= on
               umount.target in order to be stopped during shutdown.

           •   Automount units automatically gain an After= dependency on
               local-fs-pre.target, and a Before= dependency on
               local-fs.target.

## [](#FSTAB)FSTAB

           Automount units may either be configured via unit files, or via
           /etc/fstab (see fstab(5) for details).

           For details how systemd parses /etc/fstab see systemd.mount(5).

           If an automount point is configured in both /etc/fstab and a unit
           file, the configuration in the latter takes precedence.

## [](#OPTIONS)OPTIONS

           Automount unit files may include [Unit] and [Install] sections,
           which are described in systemd.unit(5).

           Automount unit files must include an [Automount] section, which
           carries information about the file system automount points it
           supervises. The options specific to the [Automount] section of
           automount units are the following:

           Where=
               Takes an absolute path of a directory of the automount point.
               If the automount point does not exist at time that the
               automount point is installed, it is created. This string must
               be reflected in the unit filename. (See above.) This option is
               mandatory.

           ExtraOptions=
               Extra mount options to use when creating the autofs
               mountpoint. This takes a comma-separated list of options. This
               setting is optional. Note that the usual specifier expansion
               is applied to this setting, literal percent characters should
               hence be written as "%%".

               Added in version 250.

           DirectoryMode=
               Directories of automount points (and any parent directories)
               are automatically created if needed. This option specifies the
               file system access mode used when creating these directories.
               Takes an access mode in octal notation. Defaults to 0755.

           TimeoutIdleSec=
               Configures an idle timeout. Once the mount has been idle for
               the specified time, systemd will attempt to unmount. Takes a
               unit-less value in seconds, or a time span value such as "5min
               20s". Pass 0 to disable the timeout logic. The timeout is
               disabled by default.

               Added in version 220.

           Check systemd.unit(5), systemd.exec(5), and systemd.kill(5) for
           more settings.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemctl(1), systemd.unit(5), systemd.mount(5),
           mount(8), automount(8), systemd.directives(7)

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

    systemd 262~devel                                    SYSTEMD.AUTOMOUNT(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd(1)](../man1/systemd.1.html),  [systemd-mount(1)](../man1/systemd-mount.1.html),  [systemd.mount(5)](../man5/systemd.mount.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.syntax(7)](../man7/systemd.syntax.7.html)

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
