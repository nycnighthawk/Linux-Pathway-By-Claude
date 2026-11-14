---
{"title": "hostnamectl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/hostnamectl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# hostnamectl(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    HOSTNAMECTL(1)                 hostnamectl                 HOSTNAMECTL(1)

## [](#NAME)NAME

           hostnamectl - Control the system hostname

## [](#SYNOPSIS)SYNOPSIS

           hostnamectl [OPTIONS...] {COMMAND}

## [](#DESCRIPTION)DESCRIPTION

           hostnamectl may be used to query and change the system hostname
           and related settings.

           systemd-hostnamed.service(8) and this tool distinguish three
           different hostnames: the high-level "pretty" hostname which might
           include all kinds of special characters (e.g. "Lennart's Laptop"),
           the "static" hostname which is the user-configured hostname (e.g.
           "lennarts-laptop"), and the transient hostname which is a fallback
           value received from network configuration (e.g. "node12345678").
           If a static hostname is set to a valid value, then the transient
           hostname is not used.

           Note that the pretty hostname has little restrictions on the
           characters and length used, while the static and transient
           hostnames are limited to the usually accepted characters of
           Internet domain names, and 64 characters at maximum (the latter
           being a Linux limitation).

           Use systemd-firstboot(1) to initialize the system hostname for
           mounted (but not booted) system images.

## [](#COMMANDS)COMMANDS

           The following commands are understood:

           status
               Show system hostname and related information. If no command is
               specified, this is the implied default.

               Added in version 195.

           hostname [NAME]
               If no argument is given, print the system hostname. If an
               optional argument NAME is provided then the command changes
               the system hostname to NAME. By default, this will alter the
               pretty, the static, and the transient hostname alike; however,
               if one or more of --static, --transient, --pretty are used,
               only the selected hostnames are changed. If the pretty
               hostname is being set, and static or transient are being set
               as well, the specified hostname will be simplified in regards
               to the character set used before the latter are updated. This
               is done by removing special characters and spaces. This
               ensures that the pretty and the static hostname are always
               closely related while still following the validity rules of
               the specific name. This simplification of the hostname string
               is not done if only the transient and/or static hostnames are
               set, and the pretty hostname is left untouched.

               The static and transient hostnames must each be either a
               single DNS label (a string composed of 7-bit ASCII lower-case
               characters and no spaces or dots, limited to the format
               allowed for DNS domain name labels), or a sequence of such
               labels separated by single dots that forms a valid DNS FQDN.
               The hostname must be at most 64 characters, which is a Linux
               limitation (DNS allows longer names).

               If the question mark character "?"  appears in the hostname,
               it is automatically substituted by a hexadecimal character
               derived from the machine-id(5) when applied, securely and
               deterministically by cryptographic hashing. Example:
               "foobar-????-????"  will automatically expand to
               "foobar-92a9-061c" or similar, depending on the local machine
               ID.

               Added in version 249.

           icon-name [NAME]
               If no argument is given, print the icon name of the system. If
               an optional argument NAME is provided then the command changes
               the icon name to NAME. The icon name is used by some graphical
               applications to visualize this host. The icon name should
               follow the Icon Naming Specification[1].

               Added in version 249.

           chassis [TYPE]
               If no argument is given, print the chassis type. If an
               optional argument TYPE is provided then the command changes
               the chassis type to TYPE. The chassis type is used by some
               graphical applications to visualize the host or alter user
               interaction. Currently, the following chassis types are
               defined: "desktop", "laptop", "convertible", "server",
               "tablet", "handset", "watch", "embedded", as well as the
               special chassis types "vm" and "container" for virtualized
               systems that lack an immediate physical chassis.

               Added in version 249.

           deployment [ENVIRONMENT]
               If no argument is given, print the deployment environment. If
               an optional argument ENVIRONMENT is provided then the command
               changes the deployment environment to ENVIRONMENT. Argument
               ENVIRONMENT must be a single word without any control
               characters. One of the following is suggested: "development",
               "integration", "staging", "production".

               Added in version 249.

           location [LOCATION]
               If no argument is given, print the location string for the
               system. If an optional argument LOCATION is provided then the
               command changes the location string for the system to
               LOCATION. Argument LOCATION should be a human-friendly,
               free-form string describing the physical location of the
               system, if it is known and applicable. This may be as generic
               as "Berlin, Germany" or as specific as "Left Rack, 2nd Shelf".

               Added in version 249.

           tags [TAG...]
               If no argument is given, print the machine tags currently
               configured, as a colon-separated list. If one or more TAG
               arguments are provided then the command replaces the
               configured tags with the specified ones. Each argument may
               itself be a colon-separated list of tags, so that the tags may
               be specified either as multiple arguments or as a single
               colon-separated argument, or any combination thereof.
               Duplicate tags are removed and the resulting list is sorted
               before being stored. To remove all tags, invoke the command
               with a single empty string argument.

               Alternatively, each argument may be prefixed with "+" or "-"
               to incrementally update the configured tags rather than
               replacing them: an argument prefixed with "+" adds all of its
               (colon-separated) tags to the list, one prefixed with "-"
               removes them. For example, hostnamectl tags +foo:bar -quux:ooo
               adds the tags "foo" and "bar" and removes "quux" and "ooo".
               The prefix applies to the whole argument, i.e. to every tag
               listed within it. Prefixed and unprefixed arguments may not be
               combined in a single invocation.

               Machine tags are short labels that may be used to classify and
               group machines for management purposes, for example to
               identify the role a machine plays in a deployment, the fleet
               or organizational unit it belongs to, or any other
               administrator-defined attribute. Each individual tag must be
               1...255 characters long and consist only of ASCII alphanumeric
               characters, "-", "."  and "=". A tag may optionally be
               parameterized with a value, in the form "key=value", in which
               case the same key may not be assigned more than one distinct
               value. The tags are stored in the TAGS= field of
               /etc/machine-info; see machine-info(5) for details. They may
               also be matched against with the
               ConditionMachineTag=/AssertMachineTag= unit settings, see
               systemd.unit(5).

               Added in version 261.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --static, --transient, --pretty
               If status is invoked (or no explicit command is given) and one
               of these switches is specified, hostnamectl will print out
               just this selected hostname.

               This selection does not apply to JSON output: with --json=,
               status always prints the full status object.

               If used with hostname, only the selected hostnames will be
               updated. When more than one of these switches are specified,
               all the specified hostnames will be updated.

               Added in version 195.

           -H, --host=
               Execute the operation remotely. Specify a hostname, or a
               username and hostname separated by "@", to connect to. The
               hostname may optionally be suffixed by a port ssh is listening
               on, separated by ":", and then a container name, separated by
               "/", which connects directly to a specific container on the
               specified host. This will use SSH to talk to the remote
               machine manager instance. Container names may be enumerated
               with machinectl -H HOST. Put IPv6 addresses in brackets.

           -M, --machine=
               Execute operation on a local container. Specify a container
               name to connect to, optionally prefixed by a user name to
               connect as and a separating "@" character. If the special
               string ".host" is used in place of the container name, a
               connection to the local system is made (which is useful to
               connect to a specific user's user bus: "--user
               --machine=lennart@.host"). If the "@" syntax is not used, the
               connection is made as root user. If the "@" syntax is used
               either the left hand side or the right hand side may be
               omitted (but not both) in which case the local user name and
               ".host" are implied.

           --no-ask-password
               Do not query the user for authentication for privileged
               operations.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

           --json=MODE
               Shows output formatted as JSON. Expects one of "short" (for
               the shortest possible output without any redundant whitespace
               or line breaks), "pretty" (for a pretty version of the same,
               with indentation and line breaks) or "off" (to turn off JSON
               output, the default).

           -j
               Equivalent to --json=pretty if running on a terminal, and
               --json=short otherwise.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), hostname(1), hostname(5), machine-info(5),
           systemctl(1), systemd-hostnamed.service(8), systemd-firstboot(1)

## [](#NOTES)NOTES

            1. Icon Naming Specification
               https://specifications.freedesktop.org/icon-naming/latest

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

    systemd 262~devel                                          HOSTNAMECTL(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [hostname(5)](../man5/hostname.5.html),  [machine-info(5)](../man5/machine-info.5.html),  [org.freedesktop.hostname1(5)](../man5/org.freedesktop.hostname1.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-hostnamed.service(8)](../man8/systemd-hostnamed.service.8.html),  [systemd-machined.service(8)](../man8/systemd-machined.service.8.html),  [systemd-machine-tag@.service(8)](../man8/systemd-machine-tag@.service.8.html)

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
