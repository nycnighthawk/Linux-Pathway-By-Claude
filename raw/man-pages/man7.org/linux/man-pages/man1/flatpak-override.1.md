---
{"title": "flatpak-override(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-override.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-override(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK OVERRIDE(1)          flatpak override         FLATPAK OVERRIDE(1)

## [](#NAME)NAME

           flatpak-override - Override application requirements

## [](#SYNOPSIS)SYNOPSIS

           flatpak override [OPTION...] [APP]

## [](#DESCRIPTION)DESCRIPTION

           Overrides the application specified runtime requirements. This can
           be used to grant a sandboxed application more or less resources
           than it requested.

           By default the application gets access to the resources it
           requested when it is started. But the user can override it on a
           particular instance by specifying extra arguments to flatpak run,
           or every time by using flatpak override.

           The application overrides are saved in text files residing in
           $XDG_DATA_HOME/flatpak/overrides in user mode.

           If the application ID APP is not specified then the overrides
           affect all applications, but the per-application overrides can
           override the global overrides.

           Unless overridden with the --user or --installation options, this
           command changes the default system-wide installation.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               Update a per-user installation.

           --system
               Update the default system-wide installation.

           --installation=NAME
               Updates a system-wide installation specified by NAME among
               those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --share=SUBSYSTEM
               Share a subsystem with the host session. This overrides the
               Context section from the application metadata.  SUBSYSTEM must
               be one of: network, ipc. This option can be used multiple
               times.

           --unshare=SUBSYSTEM
               Don't share a subsystem with the host session. This overrides
               the Context section from the application metadata.  SUBSYSTEM
               must be one of: network, ipc. This option can be used multiple
               times.

           --share-if=SUBSYSTEM:CONDITION
               Share a subsystem with the host session conditionally, only
               when the specified condition is met at runtime. This overrides
               to the Context section from the application metadata.
               SUBSYSTEM must be one of: network, ipc.  CONDITION must be one
               of: true, false, has-input-device, has-wayland,
               has-usb-device, has-usb-portal. Conditions can be negated with
               !, for example !has-input-device. This option can be used
               multiple times. Available since 1.17.

               See the Conditional Permissions section in flatpak-metadata(5)
               for more details.

           --socket=SOCKET
               Expose a well-known socket to the application. This overrides
               to the Context section from the application metadata.  SOCKET
               must be one of: x11, wayland, fallback-x11, pulseaudio,
               system-bus, session-bus, ssh-auth, pcsc, cups, gpg-agent,
               inherit-wayland-socket. This option can be used multiple
               times.

           --nosocket=SOCKET
               Don't expose a well-known socket to the application. This
               overrides to the Context section from the application
               metadata.  SOCKET must be one of: x11, wayland, fallback-x11,
               pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups,
               gpg-agent, inherit-wayland-socket. This option can be used
               multiple times.

           --socket-if=SOCKET:CONDITION
               Expose a well-known socket to the application conditionally,
               only when the specified condition is met at runtime. This
               overrides to the Context section from the application
               metadata.  SOCKET must be one of: x11, wayland, fallback-x11,
               pulseaudio, system-bus, session-bus, ssh-auth, pcsc, cups,
               gpg-agent, inherit-wayland-socket.  CONDITION must be one of:
               true, false, has-input-device, has-wayland, has-usb-device,
               has-usb-portal. Conditions can be negated with !, for example
               !has-wayland. This option can be used multiple times.
               Available since 1.17.

               See the Conditional Permissions section in flatpak-metadata(5)
               for more details.

           --device=DEVICE
               Expose a device to the application. This overrides to the
               Context section from the application metadata.  DEVICE must be
               one of: dri, input, usb, kvm, shm, all. This option can be
               used multiple times.

           --nodevice=DEVICE
               Don't expose a device to the application. This overrides to
               the Context section from the application metadata.  DEVICE
               must be one of: dri, input, usb, kvm, shm, all. This option
               can be used multiple times.

           --device-if=DEVICE:CONDITION
               Expose a device to the application conditionally, only when
               the specified condition is met at runtime. This overrides to
               the Context section from the application metadata.  DEVICE
               must be one of: dri, input, usb, kvm, shm, all.  CONDITION
               must be one of: true, false, has-input-device, has-wayland,
               has-usb-device, has-usb-portal. Conditions can be negated with
               !, for example !has-input-device. This option can be used
               multiple times. Available since 1.17.

               See the Conditional Permissions section in flatpak-metadata(5)
               for more details.

           --allow=FEATURE
               Allow access to a specific feature. This updates the [Context]
               group in the metadata.  FEATURE must be one of: devel,
               multiarch, bluetooth, canbus, per-app-dev-shm. This option can
               be used multiple times.

               See flatpak-build-finish(1) for the meaning of the various
               features.

           --disallow=FEATURE
               Disallow access to a specific feature. This updates the
               [Context] group in the metadata.  FEATURE must be one of:
               devel, multiarch, bluetooth, canbus, per-app-dev-shm. This
               option can be used multiple times.

           --allow-if=FEATURE:CONDITION
               Allow access to a specific feature conditionally, only when
               the specified condition is met at runtime. This overrides to
               the Context section from the application metadata.  FEATURE
               must be one of: devel, multiarch, bluetooth.  CONDITION must
               be one of: true, false, has-input-device, has-wayland,
               has-usb-device, has-usb-portal. Conditions can be negated with
               !, for example !has-input-device. This option can be used
               multiple times. Available since 1.17.

               See the Conditional Permissions section in flatpak-metadata(5)
               for more details.

           --filesystem=FILESYSTEM
               Allow the application access to a subset of the filesystem.
               This overrides to the Context section from the application
               metadata.  FILESYSTEM can be one of: home, host, host-os,
               host-etc, host-root, xdg-desktop, xdg-documents, xdg-download,
               xdg-music, xdg-pictures, xdg-public-share, xdg-templates,
               xdg-videos, xdg-run, xdg-config, xdg-cache, xdg-data, an
               absolute path, or a homedir-relative path like ~/dir or paths
               relative to the xdg dirs, like xdg-download/subdir. The
               optional :ro suffix indicates that the location will be
               read-only. The optional :create suffix indicates that the
               location will be read-write and created if it doesn't exist.
               This option can be used multiple times. See the "[Context]
               filesystems" list in flatpak-metadata(5) for details of the
               meanings of these filesystems.

           --nofilesystem=FILESYSTEM
               Undo the effect of a previous --filesystem=FILESYSTEM in the
               app's manifest or a lower-precedence layer of overrides,
               and/or remove a previous --filesystem=FILESYSTEM from this
               layer of overrides. This overrides the Context section of the
               application metadata.  FILESYSTEM can take the same values as
               for --filesystem, but the :ro and :create suffixes are not
               used here. This option can be used multiple times.

               This option does not prevent access to a more narrowly-scoped
               --filesystem. For example, if an application has the
               equivalent of --filesystem=xdg-config/MyApp in its manifest or
               as a system-wide override, and flatpak override --user
               --nofilesystem=home as a per-user override, then it will be
               prevented from accessing most of the home directory, but it
               will still be allowed to access $XDG_CONFIG_HOME/MyApp.

               As a special case, --nofilesystem=host:reset will ignore all
               --filesystem permissions inherited from the app manifest or a
               lower-precedence layer of overrides, in addition to having the
               behaviour of --nofilesystem=host.

           --add-policy=SUBSYSTEM.KEY=VALUE
               Add generic policy option. For example,
               "--add-policy=subsystem.key=v1 --add-policy=subsystem.key=v2"
               would map to this metadata:

                   [Policy subsystem]
                   key=v1;v2;

               This option can be used multiple times.

           --remove-policy=SUBSYSTEM.KEY=VALUE
               Remove generic policy option. This option can be used multiple
               times.

           --env=VAR=VALUE
               Set an environment variable in the application. This overrides
               to the Context section from the application metadata. This
               option can be used multiple times.

           --unset-env=VAR
               Unset an environment variable in the application. This
               overrides the unset-environment entry in the [Context] group
               of the metadata, and the [Environment] group. This option can
               be used multiple times.

           --env-fd=FD
               Read environment variables from the file descriptor FD, and
               set them as if via --env. This can be used to avoid
               environment variables and their values becoming visible to
               other users.

               Each environment variable is in the form VAR=VALUE followed by
               a zero byte. This is the same format used by env -0 and
               /proc/*/environ.

           --own-name=NAME
               Allow the application to own the well-known name NAME on the
               session bus. This overrides to the Context section from the
               application metadata. This option can be used multiple times.

           --talk-name=NAME
               Allow the application to talk to the well-known name NAME on
               the session bus. This overrides to the Context section from
               the application metadata. This option can be used multiple
               times.

           --no-talk-name=NAME
               Don't allow the application to talk to the well-known name
               NAME on the session bus. This overrides to the Context section
               from the application metadata. This option can be used
               multiple times.

           --system-own-name=NAME
               Allow the application to own the well known name NAME on the
               system bus. If NAME ends with .*, it allows the application to
               own all matching names. This overrides to the Context section
               from the application metadata. This option can be used
               multiple times.

           --system-talk-name=NAME
               Allow the application to talk to the well known name NAME on
               the system bus. If NAME ends with .*, it allows the
               application to talk to all matching names. This overrides to
               the Context section from the application metadata. This option
               can be used multiple times.

           --system-no-talk-name=NAME
               Don't allow the application to talk to the well known name
               NAME on the system bus. If NAME ends with .*, it allows the
               application to talk to all matching names. This overrides to
               the Context section from the application metadata. This option
               can be used multiple times.

           --persist=FILENAME
               If the application doesn't have access to the real homedir,
               make the (homedir-relative) path FILENAME a bind mount to the
               corresponding path in the per-application directory, allowing
               that location to be used for persistent data. This overrides
               to the Context section from the application metadata. This
               option can be used multiple times.

           --reset
               Remove overrides. If an APP is given, remove the overrides for
               that application, otherwise remove the global overrides.

           --show
               Shows overrides. If an APP is given, shows the overrides for
               that application, otherwise shows the global overrides.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak override --nosocket=wayland org.gnome.gedit

           $ flatpak override --filesystem=home org.mozilla.Firefox

           $ flatpak override --socket-if=x11:!has-wayland org.example.App

           Grant X11 socket access only when not running in a Wayland
           session.

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-run(1)

## [](#COLOPHON)COLOPHON

           This page is part of the flatpak (a tool for building and
           distributing desktop applications on Linux) project.  Information
           about the project can be found at ⟨http://flatpak.org/⟩.  It is
           not known how to report bugs for this man page; if you know,
           please send a mail to man-pages@man7.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/flatpak/flatpak⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    flatpak                                               FLATPAK OVERRIDE(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-config(1)](../man1/flatpak-config.1.html),  [flatpak-run(1)](../man1/flatpak-run.1.html),  [flatpak-metadata(5)](../man5/flatpak-metadata.5.html)

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
