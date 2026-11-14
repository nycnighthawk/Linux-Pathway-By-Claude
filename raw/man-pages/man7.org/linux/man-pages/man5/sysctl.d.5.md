---
{"title": "sysctl.d(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/sysctl.d.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sysctl.d(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION FORMAT](#CONFIGURATION_FORMAT) \| [CONFIGURATION DIRECTORIES AND PRECEDENCE](#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSCTL.D(5)                      sysctl.d                     SYSCTL.D(5)

## [](#NAME)NAME

           sysctl.d - Configure kernel parameters at boot

## [](#SYNOPSIS)SYNOPSIS

               /etc/sysctl.d/*.conf
               /run/sysctl.d/*.conf
               /usr/local/lib/sysctl.d/*.conf
               /usr/lib/sysctl.d/*.conf

           key.name.under.proc.sys = some value
           key/name/under/proc/sys = some value
           key/middle.part.with.dots/foo = 123
           key.middle/part/with/dots.foo = 123
           -key.that.will.not.fail = value
           key.pattern.*.with.glob = whatever
           -key.pattern.excluded.with.glob
           key.pattern.overridden.with.glob = custom

## [](#DESCRIPTION)DESCRIPTION

           At boot, systemd-sysctl.service(8) reads configuration files from
           the above directories to configure sysctl(8) kernel parameters.

## [](#CONFIGURATION_FORMAT)CONFIGURATION FORMAT

           The configuration files contain a list of variable assignments,
           separated by newlines. Empty lines and lines whose first
           non-whitespace character is "#" or ";" are ignored.

           Note that either "/" or "."  may be used as separators within
           sysctl variable names. If the first separator is a slash,
           remaining slashes and dots are left intact. If the first separator
           is a dot, dots and slashes are interchanged.
           "kernel.domainname=foo" and "kernel/domainname=foo" are equivalent
           and will cause "foo" to be written to /proc/sys/kernel/domainname.
           Either "net.ipv4.conf.enp3s0/200.forwarding" or
           "net/ipv4/conf/enp3s0.200/forwarding" may be used to refer to
           /proc/sys/net/ipv4/conf/enp3s0.200/forwarding. A glob glob(7)
           pattern may be used to write the same value to all matching keys.
           Keys for which an explicit pattern exists will be excluded from
           any glob matching. In addition, a key may be explicitly excluded
           from being set by any matching glob patterns by specifying the key
           name prefixed with a "-" character and not followed by "=", see
           SYNOPSIS.

           Any access permission errors and attempts to write variables not
           present on the local system are logged at debug level and do not
           cause the service to fail. Other types of errors when setting
           variables are logged with higher priority and cause the service to
           return failure at the end (after processing other variables). As
           an exception, if a variable assignment is prefixed with a single
           "-" character, failure to set the variable for any reason will be
           logged at debug level and will not cause the service to fail.

           The settings configured with sysctl.d files will be applied early
           on boot. The network interface-specific options will also be
           applied individually for each network interface as it shows up in
           the system. (More specifically, net.ipv4.conf.*, net.ipv6.conf.*,
           net.ipv4.neigh.*  and net.ipv6.neigh.*).

           Many sysctl parameters only become available when certain kernel
           modules are loaded. Modules are usually loaded on demand, e.g.
           when certain hardware is plugged in or network brought up. This
           means that systemd-sysctl.service(8) which runs during early boot
           will not configure such parameters if they become available after
           it has run. To set such parameters, it is recommended to add an
           udev(7) rule to set those parameters when they become available.
           Alternatively, a slightly simpler and less efficient option is to
           add the module to modules-load.d(5), causing it to be loaded
           statically before sysctl settings are applied (see example below).

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

## [](#EXAMPLES)EXAMPLES

           Example 1. Set kernel YP domain name

           /etc/sysctl.d/domain-name.conf:

               kernel.domainname=example.com

           Example 2. Apply settings available only when a certain module is
           loaded (method one)

           /etc/udev/rules.d/99-bridge.rules:

               ACTION=="add", SUBSYSTEM=="module", KERNEL=="br_netfilter", \
                     RUN+="/usr/lib/systemd/systemd-sysctl --prefix=/net/bridge"

           /etc/sysctl.d/bridge.conf:

               net.bridge.bridge-nf-call-ip6tables = 0
               net.bridge.bridge-nf-call-iptables = 0
               net.bridge.bridge-nf-call-arptables = 0

           This method applies settings when the module is loaded. Please
           note that, unless the br_netfilter module is loaded, bridged
           packets will not be filtered by Netfilter (starting with kernel
           3.18), so simply not loading the module is sufficient to avoid
           filtering.

           Example 3. Apply settings available only when a certain module is
           loaded (method two)

           /etc/modules-load.d/bridge.conf:

               br_netfilter

           /etc/sysctl.d/bridge.conf:

               net.bridge.bridge-nf-call-ip6tables = 0
               net.bridge.bridge-nf-call-iptables = 0
               net.bridge.bridge-nf-call-arptables = 0

           This method forces the module to be always loaded. Please note
           that, unless the br_netfilter module is loaded, bridged packets
           will not be filtered with Netfilter (starting with kernel 3.18),
           so simply not loading the module is sufficient to avoid filtering.

           Example 4. Set network routing properties for all interfaces

           /etc/sysctl.d/20-rp_filter.conf:

               net.ipv4.conf.default.rp_filter = 2
               net.ipv4.conf.*.rp_filter = 2
               -net.ipv4.conf.all.rp_filter
               net.ipv4.conf.hub0.rp_filter = 1

           The rp_filter key will be set to "2" for all interfaces, except
           "hub0". We set net.ipv4.conf.default.rp_filter first, so any
           interfaces which are added later will get this value (this also
           covers any interfaces detected while we're running). The glob
           matches any interfaces which were detected earlier. The glob will
           also match net.ipv4.conf.all.rp_filter, which we do not want to
           set at all, so it is explicitly excluded. And "hub0" is excluded
           from the glob because it has an explicit setting.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-sysctl.service(8), systemd-delta(1),
           sysctl(8), sysctl.conf(5), modprobe(8)

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

    systemd 262~devel                                             SYSCTL.D(5)

------------------------------------------------------------------------

Pages that refer to this page: [sysctl.conf(5)](../man5/sysctl.conf.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-coredump(8)](../man8/systemd-coredump.8.html),  [systemd-sysctl.service(8)](../man8/systemd-sysctl.service.8.html)

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
