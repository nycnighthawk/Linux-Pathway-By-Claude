---
{"title": "machine-info(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/machine-info.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# machine-info(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MACHINE-INFO(5)                machine-info               MACHINE-INFO(5)

## [](#NAME)NAME

           machine-info - Local machine information file

## [](#SYNOPSIS)SYNOPSIS

           /etc/machine-info

## [](#DESCRIPTION)DESCRIPTION

           The /etc/machine-info file contains machine metadata.

           The format of machine-info is a newline-separated list of
           environment-like shell-compatible variable assignments, ignoring
           comments and empty lines. It is possible to source the
           configuration from shell scripts, however, beyond mere variable
           assignments no shell features are supported, allowing applications
           to read the file without implementing a shell compatible execution
           engine. See os-release(5) for a detailed description of the
           format.

           /etc/machine-info contains metadata about the machine that is set
           by the user or administrator. The settings configured here have
           the highest precedence. When not set, appropriate values may be
           determined automatically, based on the information about the
           hardware or other configuration files. It is thus completely fine
           for this file to not be present.

           You may use hostnamectl(1) to change the settings of this file
           from the command line.

## [](#OPTIONS)OPTIONS

           The following machine metadata parameters may be set using
           /etc/machine-info:

       Machine Information
           PRETTY_HOSTNAME=
               A pretty human-readable UTF-8 machine identifier string. This
               should contain a name like "Lennart's Laptop" which is useful
               to present to the user and does not suffer by the syntax
               limitations of internet domain names. If possible, the
               internet hostname as configured in /etc/hostname should be
               kept similar to this one. Example: if this value is "Lennart's
               Computer" an Internet hostname of "lennarts-computer" might be
               a good choice. If this parameter is not set, an application
               should fall back to the Internet hostname for presentation
               purposes.

           ICON_NAME=
               An icon identifying this machine according to the XDG Icon
               Naming Specification[1]. If this parameter is not set, an
               application should fall back to "computer" or a similar icon
               name.

           CHASSIS=
               The chassis type. Currently, the following chassis types are
               defined: "desktop", "laptop", "convertible", "server",
               "tablet", "handset", "watch", and "embedded", as well as the
               special chassis types "vm" and "container" for virtualized
               systems that lack an immediate physical chassis.

               Note that most systems allow detection of the chassis type
               automatically (based on firmware information or suchlike).
               This setting should only be used to override a misdetection or
               to manually configure the chassis type where automatic
               detection is not available.

               Added in version 197.

           DEPLOYMENT=
               Describes the system deployment environment. One of the
               following is suggested: "development", "integration",
               "staging", "testing", "production".

               Added in version 216.

           LOCATION=
               Describes the system location if applicable and known. Takes a
               human-friendly, free-form string. This may be as generic as
               "Berlin, Germany" or as specific as "Left Rack, 2nd Shelf".

               Added in version 216.

           TAGS=
               A colon-separated list of tags attached to this machine. Tags
               are short labels that may be used to classify and group
               machines for management purposes, for example to identify the
               role a machine plays in a deployment ("webserver",
               "database"), the fleet or organizational unit it belongs to,
               or any other administrator-defined attribute. Example:
               "TAGS=webserver:frontend:berlin".

               Each individual tag must be 1...255 characters long and may
               consist only of the ASCII alphanumeric characters, "-", "."
               and "=". The first character may not be "-", "."  or "=", and
               the last character may not be "-" or "."  (unless it takes the
               parameterized form, see below).

               A tag may optionally be parameterized with a value, in the
               form "key=value". The first "=" separates the key from the
               value; any further "=" characters are part of the value. The
               key (the part before the first "=") follows the same
               restrictions as an unparameterized tag, in particular it may
               not be empty and may not end in "-" or ".". The value (the
               part after the first "=") may be empty and is otherwise
               unrestricted within the allowed character set. Example:
               "TAGS=role=webserver:env=production:berlin". The same key may
               not be assigned more than one distinct value:
               "role=webserver:role=database" is refused (but a key may
               coexist with the corresponding unparameterized tag, e.g.
               "role:role=webserver").

               The configured tags may be matched against with the
               ConditionMachineTag= and AssertMachineTag= unit settings, see
               systemd.unit(5) for details. They may be queried and changed
               with the tags command of hostnamectl(1).

               Added in version 261.

           HARDWARE_VENDOR=
               Specifies the hardware vendor. If unspecified, the hardware
               vendor set in DMI or hwdb(7) will be used.

               Added in version 251.

           HARDWARE_MODEL=
               Specifies the hardware model. If unspecified, the hardware
               model set in DMI or hwdb(7) will be used.

               Added in version 251.

           HARDWARE_SKU=
               Specifies the hardware SKU (Stock-Keeping Unit). If
               unspecified, the hardware SKU set in DMI will be used.

               Added in version 258.

           HARDWARE_VERSION=
               Specifies the hardware version. If unspecified, the hardware
               version set in DMI will be used.

               Added in version 258.

       Custom Fields
           Operating system vendors and systemd administrators may extend the
           file format and introduce new fields. It is highly recommended to
           prefix new fields with an OS-specific name in order to avoid name
           clashes. Applications reading this file must ignore unknown
           fields.

           Example: "_LOCAL_EMERGENCY_CONTACT="user@example.org"".

## [](#EXAMPLE)EXAMPLE

               PRETTY_HOSTNAME="Lennart's Tablet"
               ICON_NAME=computer-tablet
               CHASSIS=tablet
               DEPLOYMENT=production
               TAGS=demo:berlin:role=webserver

## [](#SEE_ALSO)SEE ALSO

           systemd(1), os-release(5), hostname(5), machine-id(5),
           hostnamectl(1), systemd-hostnamed.service(8)

## [](#NOTES)NOTES

            1. XDG Icon Naming Specification
               https://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html

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

    systemd 262~devel                                         MACHINE-INFO(5)

------------------------------------------------------------------------

Pages that refer to this page: [hostnamectl(1)](../man1/hostnamectl.1.html),  [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [hostname(5)](../man5/hostname.5.html),  [machine-id(5)](../man5/machine-id.5.html),  [org.freedesktop.hostname1(5)](../man5/org.freedesktop.hostname1.5.html),  [os-release(5)](../man5/os-release.5.html),  [repart.d(5)](../man5/repart.d.5.html),  [systemd.link(5)](../man5/systemd.link.5.html),  [systemd.network(5)](../man5/systemd.network.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [sysusers.d(5)](../man5/sysusers.d.5.html),  [tmpfiles.d(5)](../man5/tmpfiles.d.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-hostnamed.service(8)](../man8/systemd-hostnamed.service.8.html),  [systemd-machine-tag@.service(8)](../man8/systemd-machine-tag@.service.8.html)

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
