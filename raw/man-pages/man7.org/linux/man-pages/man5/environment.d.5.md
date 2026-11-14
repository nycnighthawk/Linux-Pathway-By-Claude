---
{"title": "environment.d(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/environment.d.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# environment.d(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION DIRECTORIES AND PRECEDENCE](#CONFIGURATION_DIRECTORIES_AND_PRECEDENCE) \| [CONFIGURATION FORMAT](#CONFIGURATION_FORMAT) \| [APPLICABILITY](#APPLICABILITY) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ENVIRONMENT.D(5)              environment.d              ENVIRONMENT.D(5)

## [](#NAME)NAME

           environment.d - Definition of user service environment

## [](#SYNOPSIS)SYNOPSIS

               ~/.config/environment.d/*.conf
               /etc/environment.d/*.conf
               /run/environment.d/*.conf
               /usr/local/lib/environment.d/*.conf
               /usr/lib/environment.d/*.conf
               /etc/environment

## [](#DESCRIPTION)DESCRIPTION

           Configuration files in the environment.d/ directories contain
           lists of environment variable assignments passed to services
           started by the systemd user instance.
           systemd-environment-d-generator(8) parses them and updates the
           environment exported by the systemd user instance. See below for
           an discussion of which processes inherit those variables.

           The user-level configuration directory defaults to
           ~/.config/environment.d/. If $XDG_CONFIG_HOME is set to an
           absolute path in the user service manager environment (e.g. via
           PAM or /etc/environment), it takes precedence over ~/.config/.
           Note that this creates a bootstrapping consideration: variables
           set in environment.d/ files, including $XDG_CONFIG_HOME itself,
           are not available when the generator determines which directory to
           read.

           It is recommended to use numerical prefixes for file names to
           simplify ordering.

           For backwards compatibility, a symlink to /etc/environment is
           installed, so this file is also parsed.

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

## [](#CONFIGURATION_FORMAT)CONFIGURATION FORMAT

           The configuration files contain a list of "KEY=VALUE" environment
           variable assignments, separated by newlines. The right hand side
           of these assignments may reference previously defined environment
           variables, using the "${OTHER_KEY}" and "$OTHER_KEY" format. It is
           also possible to use "${FOO:-DEFAULT_VALUE}" to expand in the same
           way as "${FOO}" unless the expansion would be empty, in which case
           it expands to DEFAULT_VALUE, and use "${FOO:+ALTERNATE_VALUE}" to
           expand to ALTERNATE_VALUE as long as "${FOO}" would have expanded
           to a non-empty value. You can escape a literal dollar sign "$" by
           doubling it, as in "$$".

           A backslash character "\" followed by a newline acts as a line
           continuation (both characters are discarded); in all other cases,
           the backslash is consumed and the following character is included
           literally in the value. This can be used to preserve
           leading/trailing whitespace or include literal backslashes.

           You may optionally enclose the right hand side of assignments in
           pairs of either 'single quotes' or "double quotes"; these will be
           stripped from the value before saving it. Using either quoting
           style does not affect variable expansion; however, single quotes
           disable backslash escaping entirely, while double quoting removes
           backslashes that precede double quotes """, dollar signs "$",
           backslashes "\", backticks "`", and newlines, and leaves all other
           backslashes in place.

           Leading and trailing whitespace characters are stripped from both
           the left and right hand sides of the assignment. To preserve such
           spaces in the value, you can either enclose the entire value in
           quotes, or escape the space characters with backslashes. You can
           also include literal newlines in the value by enclosing it in
           quotes.

           Each KEY must be a valid variable name. Empty lines and lines
           beginning with the comment characters "#" or ";" are ignored. No
           other elements of shell syntax are supported.

       Examples
           Example 1. Setup environment to allow access to a program
           installed in /opt/foo

           /etc/environment.d/60-foo.conf:

               FOO_DEBUG=force-software-gl,log-verbose
               PATH=/opt/foo/bin:$PATH
               LD_LIBRARY_PATH=/opt/foo/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
               XDG_DATA_DIRS=/opt/foo/share:${XDG_DATA_DIRS:-/usr/local/share/:/usr/share/}

           Example 2. Escaping and variable expansion

           /etc/environment.d/70-bar.conf:

               # A comment
               test_var=(variable)
               ; Another comment
               test_comment=value # This is a part of the variable, and not a comment!

               test_none= \ before\
               after "" '' \${test_var}
               test_double=" \ before\
               after "" '' \${test_var}"
               test_single=' \ before\
               after "" '' \${test_var}'

               # The above example produces the following environment variables, written using
               # C-style string escapes:
               #
               # test_var="(variable)"
               # test_comment="value # This is a part of the variable, and not a comment!"
               # test_none=" beforeafter \"\" '' (variable)"
               # test_double=" \\ beforeafter  '' (variable)"
               # test_single=" \\ before\\\nafter \"\"  \\(variable)"

## [](#APPLICABILITY)APPLICABILITY

           Environment variables exported by the user service manager
           (systemd --user instance started in the user@uid.service system
           service) are passed to any services started by that service
           manager. In particular, this may include services which run user
           shells. For example in the GNOME environment, the graphical
           terminal emulator runs as the gnome-terminal-server.service user
           unit, which in turn runs the user shell, so that shell will
           inherit environment variables exported by the user manager. For
           other instances of the shell, not launched by the user service
           manager, the environment they inherit is defined by the program
           that starts them. Hint: in general, systemd.service(5) units
           contain programs launched by systemd, and systemd.scope(5) units
           contain programs launched by something else.

           Note that these files do not affect the environment block of the
           service manager itself, but exclusively the environment blocks
           passed to the services it manages. Environment variables set that
           way thus cannot be used to influence behaviour of the service
           manager. In order to make changes to the service manager's
           environment block the environment must be modified before the
           user's service manager is invoked, for example from the system
           service manager or via a PAM module.

           Specifically, for ssh logins, the sshd(8) service builds an
           environment that is a combination of variables forwarded from the
           remote system and defined by sshd, see the discussion in ssh(1). A
           graphical display session will have an analogous mechanism to
           define the environment. Note that some managers query the systemd
           user instance for the exported environment and inject this
           configuration into programs they start, using systemctl
           show-environment or the underlying D-Bus call.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-environment-d-generator(8),
           systemd.environment-generator(7)

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

    systemd 262~devel                                        ENVIRONMENT.D(5)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-environment-d-generator(8)](../man8/systemd-environment-d-generator.8.html)

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
