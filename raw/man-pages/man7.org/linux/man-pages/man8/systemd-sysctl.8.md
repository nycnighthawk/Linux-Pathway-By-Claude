---
{"title": "systemd-sysctl.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-sysctl.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-sysctl.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CREDENTIALS](#CREDENTIALS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-SYSCTL.SERVICE(8) systemd-sysctl.serviceSYSTEMD-SYSCTL.SERVICE(8)

## [](#NAME)NAME

           systemd-sysctl.service, systemd-sysctl - Configure kernel
           parameters at boot

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/systemd-sysctl [OPTIONS...] [CONFIGFILE...]

           systemd-sysctl.service

## [](#DESCRIPTION)DESCRIPTION

           systemd-sysctl.service is an early boot service that configures
           sysctl(8) kernel parameters by invoking
           /usr/lib/systemd/systemd-sysctl.

           When invoked with no arguments, /usr/lib/systemd/systemd-sysctl
           applies all directives from configuration files listed in
           sysctl.d(5). When invoked with positional arguments, the
           configuration specified by the command line arguments is executed.
           If the string "-" is specified instead of a filename, the
           configuration is read from standard input. If the argument is a
           file name (without any slashes), all configuration directories are
           searched for a matching file and the file found that has the
           highest priority is executed. If the argument is a path, that file
           is used directly without searching the configuration directories
           for any other matching file.

           In addition, --prefix= option may be used to limit which sysctl
           settings are applied.

           See sysctl.d(5) for information about the configuration of sysctl
           settings. After sysctl configuration is changed on disk, it must
           be written to the files in /proc/sys/ before it takes effect. It
           is possible to update specific settings, or simply to reload all
           configuration, see Examples below.

## [](#OPTIONS)OPTIONS

           --prefix=
               Only apply rules with the specified prefix.

               Added in version 230.

           --strict=
               Always return non-zero exit code on failure (including invalid
               sysctl variable name and insufficient permissions), unless the
               sysctl variable name is prefixed with a "-" character.

               Added in version 252.

           --inline
               Treat each positional argument as a separate configuration
               line instead of a file name.

               Added in version 259.

           --cat-config
               Copy the contents of config files to standard output. Before
               each file, the filename is printed as a comment.

           --tldr
               Copy the contents of config files to standard output. Only the
               "interesting" parts of the configuration files are printed,
               comments and empty lines are skipped. Before each file, the
               filename is printed as a comment.

           --no-pager
               Do not pipe output into a pager.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#CREDENTIALS)CREDENTIALS

           systemd-sysctl supports the service credentials logic as
           implemented by ImportCredential=/LoadCredential=/SetCredential=
           (see systemd.exec(5) for details). The following credentials are
           used when passed in:

           sysctl.extra
               The contents of this credential may contain additional lines
               to operate on. The credential contents should follow the same
               format as any other sysctl.d/ drop-in configuration file. If
               this credential is passed it is processed after all of the
               drop-in files read from the file system. The settings
               configured in the credential hence take precedence over those
               in the file system.

               Added in version 252.

           Note that by default the systemd-sysctl.service unit file is set
           up to inherit the "sysctl.extra" credential from the service
           manager.

## [](#EXAMPLES)EXAMPLES

           Example 1. Reset all sysctl settings

               systemctl restart systemd-sysctl

           Example 2. View coredump handler configuration

               # sysctl kernel.core_pattern
               kernel.core_pattern = |/usr/libexec/abrt-hook-ccpp %s %c %p %u %g %t %P %I

           Example 3. Update coredump handler configuration

               # /usr/lib/systemd/systemd-sysctl --prefix kernel.core_pattern

           This searches all the directories listed in sysctl.d(5) for
           configuration files and writes /proc/sys/kernel/core_pattern.

           Example 4. Update coredump handler configuration according to a
           specific file

               # /usr/lib/systemd/systemd-sysctl 50-coredump.conf

           This applies all the settings found in 50-coredump.conf. Either
           /etc/sysctl.d/50-coredump.conf, or /run/sysctl.d/50-coredump.conf,
           or /usr/lib/sysctl.d/50-coredump.conf will be used, in the order
           of preference.

           See sysctl(8) for various ways to directly apply sysctl settings.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), sysctl.d(5), sysctl(8)

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

    systemd 262~devel                               SYSTEMD-SYSCTL.SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [sysctl.conf(5)](../man5/sysctl.conf.5.html),  [sysctl.d(5)](../man5/sysctl.d.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-coredump(8)](../man8/systemd-coredump.8.html)

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
