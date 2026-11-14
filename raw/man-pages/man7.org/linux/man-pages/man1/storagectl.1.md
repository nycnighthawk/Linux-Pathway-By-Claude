---
{"title": "storagectl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/storagectl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# storagectl(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [USE AS A MOUNT HELPER](#USE_AS_A_MOUNT_HELPER) \| [EXAMPLES](#EXAMPLES) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    STORAGECTL(1)                   storagectl                  STORAGECTL(1)

## [](#NAME)NAME

           storagectl, mount.storage - Enumerate and mount storage volumes
           provided by storage providers

## [](#SYNOPSIS)SYNOPSIS

           storagectl [OPTIONS...] {COMMAND} [NAME...]

           mount -t storage PROVIDER:VOLUME DIRECTORY

           mount -t storage.FSTYPE PROVIDER:VOLUME DIRECTORY

## [](#DESCRIPTION)DESCRIPTION

           storagectl may be used to inspect storage providers and the
           storage volumes they expose. A storage provider is a service
           implementing the io.systemd.StorageProvider Varlink[1] interface,
           registered as an AF_UNIX socket below the well-known socket
           directory /run/systemd/io.systemd.StorageProvider/ (in system
           mode) or $XDG_RUNTIME_DIR/systemd/io.systemd.StorageProvider/ (in
           user mode). The two storage providers shipped with systemd are
           systemd-storage-block@.service(8), which exposes the system's
           block devices, and systemd-storage-fs@.service(8), which exposes
           regular files and directories from a backing file system.

           The tool also provides a mount(8) helper for the file system type
           "storage", which permits mounting storage volumes to arbitrary
           places. See "Use as a mount helper" below for details.

## [](#COMMANDS)COMMANDS

           The following commands are understood:

           volumes [GLOB]
               List storage volumes provided by all storage providers running
               on the system (or, with --user, in the user runtime). The
               optional GLOB argument is a shell-style pattern (see
               fnmatch(3)) that filters the result by volume name. The output
               is a table containing the providing service, the volume name,
               its type ("blk", "reg" or "dir"), whether it is read-only, and
               — if known — its size and the number of bytes used.

               This is the default command if none is specified.

               Added in version 261.

           templates [GLOB]
               List volume templates supported by the running storage
               providers. Templates encapsulate a configuration to use when
               creating volumes on-the-fly, when they are acquired. Template
               support is an optional feature for providers, and only applies
               to providers that allow creation of volumes on-the-fly. See
               the respective provider documentation for details, for example
               systemd-storage-fs@.service(8). The optional GLOB argument
               filters by template name. Storage providers that do not
               implement template-based volume creation (such as the
               block-device provider) do not contribute to this output.

               Added in version 261.

           providers
               List the storage providers known to the system. This is
               determined by scanning the well-known socket directory for
               AF_UNIX sockets that look like io.systemd.StorageProvider
               endpoints. For each provider it is also reported whether the
               socket can currently be connected to.

               Added in version 261.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --system
               Operate on system-wide storage providers. Sockets are looked
               for in /run/systemd/io.systemd.StorageProvider/. This is the
               default.

               Added in version 261.

           --user
               Operate on per-user storage providers. Sockets are looked for
               in $XDG_RUNTIME_DIR/systemd/io.systemd.StorageProvider/.

               Added in version 261.

           --json=MODE
               Shows output formatted as JSON. Expects one of "short" (for
               the shortest possible output without any redundant whitespace
               or line breaks), "pretty" (for a pretty version of the same,
               with indentation and line breaks) or "off" (to turn off JSON
               output, the default).

           --no-pager
               Do not pipe output into a pager.

           --no-legend
               Do not print the legend, i.e. column headers and the footer
               with hints.

           --no-ask-password
               Do not query the user for authentication for privileged
               operations.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#USE_AS_A_MOUNT_HELPER)USE AS A MOUNT HELPER

           The tool provides the /sbin/mount.storage alias, implementing the
           mount(8) "external helper" interface, allowing storage volumes to
           be mounted with the regular mount command. The volume to mount is
           encoded as the source of the mount, in the form "PROVIDER:VOLUME",
           where PROVIDER is the name of a storage provider (as listed by
           storagectl providers) and VOLUME is the volume name. Two file
           system type spellings are recognized:

           "storage"
               Acquires a directory volume and bind-mounts its directory tree
               onto the target.

               Added in version 261.

           "storage.FSTYPE"
               Acquires a regular file or block device volume and mounts it
               as a file system of type FSTYPE (for example "storage.ext4",
               "storage.btrfs", ...).

               Added in version 261.

           The standard -o mount options are forwarded to mount. In addition,
           the following "storage."-prefixed options are interpreted by
           mount.storage itself and stripped from the forwarded list:

           storage.create=MODE
               Takes one of "any" (open if it exists, otherwise create — the
               default), "open" (fail if the volume does not yet exist) or
               "new" (fail if the volume already exists).

               Added in version 261.

           storage.template=NAME
               The template to use when creating a new volume, if it is
               missing and the provider supports on-the-fly creation of
               volumes.

               Added in version 261.

           storage.create-size=BYTES
               When creating a new volume on-the-fly, the size in bytes to
               allocate. Accepts the usual "K"/"M"/"G"/"T" suffixes (base
               1024). Required when creating a regular file volume.

               Added in version 261.

## [](#EXAMPLES)EXAMPLES

           Example 1. Enumerate available storage providers, volumes and
           templates

               $ storagectl providers
               $ storagectl volumes
               $ storagectl volumes '*foo*'
               $ storagectl templates

           Example 2. Mount a directory volume from the file system provider

               # mount -t storage fs:myvol /mnt/myvol

           If the volume "myvol" does not yet exist, it will be created using
           the default "subvolume" template.

           Example 3. Create and mount an ext4 file system from a regular
           file.

               # mount -t storage.ext4 fs:scratch /mnt/scratch -o loop

           Example 4. Mount a block device volume read-only

               # mount -t storage.ext4 -o ro block:/dev/disk/by-id/usb-foo /mnt/foo

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#ENVIRONMENT)ENVIRONMENT

           $SYSTEMD_LOG_LEVEL
               The maximum log level of emitted messages (messages with a
               higher log level, i.e. less important ones, will be
               suppressed). Takes a comma-separated list of values. A value
               may be either one of (in order of decreasing importance)
               emerg, alert, crit, err, warning, notice, info, debug, or an
               integer in the range 0...7. See syslog(3) for more
               information. Each value may optionally be prefixed with one of
               console, syslog, kmsg or journal followed by a colon to set
               the maximum log level for that specific log target (e.g.
               SYSTEMD_LOG_LEVEL=debug,console:info specifies to log at debug
               level except when logging to the console which should be at
               info level). Note that the global maximum log level takes
               priority over any per target maximum log levels.

           $SYSTEMD_LOG_COLOR
               A boolean. If true, messages written to the tty will be
               colored according to priority.

               This setting is only useful when messages are written directly
               to the terminal, because journalctl(1) and other tools that
               display logs will color messages based on the log level on
               their own.

           $SYSTEMD_LOG_TIME
               A boolean. If true, console log messages will be prefixed with
               a timestamp.

               This setting is only useful when messages are written directly
               to the terminal or a file, because journalctl(1) and other
               tools that display logs will attach timestamps based on the
               entry metadata on their own.

           $SYSTEMD_LOG_LOCATION
               A boolean. If true, messages will be prefixed with a filename
               and line number in the source code where the message
               originates.

               Note that the log location is often attached as metadata to
               journal entries anyway. Including it directly in the message
               text can nevertheless be convenient when debugging programs.

           $SYSTEMD_LOG_TID
               A boolean. If true, messages will be prefixed with the current
               numerical thread ID (TID).

               Note that the this information is attached as metadata to
               journal entries anyway. Including it directly in the message
               text can nevertheless be convenient when debugging programs.

           $SYSTEMD_LOG_TARGET
               The destination for log messages. One of console (log to the
               attached tty), console-prefixed (log to the attached tty but
               with prefixes encoding the log level and "facility", see
               syslog(3), kmsg (log to the kernel circular log buffer),
               journal (log to the journal), journal-or-kmsg (log to the
               journal if available, and to kmsg otherwise), auto (determine
               the appropriate log target automatically, the default), null
               (disable log output).

           $SYSTEMD_LOG_RATELIMIT_KMSG
               Whether to ratelimit kmsg or not. Takes a boolean. Defaults to
               "true". If disabled, systemd will not ratelimit messages
               written to kmsg.

           $SYSTEMD_PAGER, $PAGER
               Pager to use when --no-pager is not given.  $SYSTEMD_PAGER is
               used if set; otherwise $PAGER is used. If neither
               $SYSTEMD_PAGER nor $PAGER are set, a set of well-known pager
               implementations is tried in turn, including less(1) and
               more(1), until one is found. If no pager implementation is
               discovered, no pager is invoked. Setting those environment
               variables to an empty string or the value "cat" is equivalent
               to passing --no-pager.

               Note: if $SYSTEMD_PAGERSECURE is not set, $SYSTEMD_PAGER and
               $PAGER can only be used to disable the pager (with "cat" or
               ""), and are otherwise ignored.

           $SYSTEMD_LESS
               Override the options passed to less (by default "FRSXMK").

               Users might want to change two options in particular:

               K
                   This option instructs the pager to exit immediately when
                   Ctrl+C is pressed. To allow less to handle Ctrl+C itself
                   to switch back to the pager command prompt, unset this
                   option.

                   If the value of $SYSTEMD_LESS does not include "K", and
                   the pager that is invoked is less, Ctrl+C will be ignored
                   by the executable, and needs to be handled by the pager.

               X
                   This option instructs the pager to not send termcap
                   initialization and deinitialization strings to the
                   terminal. It is set by default to allow command output to
                   remain visible in the terminal even after the pager exits.
                   Nevertheless, this prevents some pager functionality from
                   working, in particular paged output cannot be scrolled
                   with the mouse.

               Note that setting the regular $LESS environment variable has
               no effect for less invocations by systemd tools.

               See less(1) for more discussion.

           $SYSTEMD_LESSCHARSET
               Override the charset passed to less (by default "utf-8", if
               the invoking terminal is determined to be UTF-8 compatible).

               Note that setting the regular $LESSCHARSET environment
               variable has no effect for less invocations by systemd tools.

           $SYSTEMD_PAGERSECURE
               Common pager commands like less(1), in addition to "paging",
               i.e. scrolling through the output, support opening of or
               writing to other files and running arbitrary shell commands.
               When commands are invoked with elevated privileges, for
               example under sudo(8) or pkexec(1), the pager becomes a
               security boundary. Care must be taken that only programs with
               strictly limited functionality are used as pagers, and
               unintended interactive features like opening or creation of
               new files or starting of subprocesses are not allowed. "Secure
               mode" for the pager may be enabled as described below, if the
               pager supports that (most pagers are not written in a way that
               takes this into consideration). It is recommended to either
               explicitly enable "secure mode" or to completely disable the
               pager using --no-pager or PAGER=cat when allowing untrusted
               users to execute commands with elevated privileges.

               This option takes a boolean argument. When set to true, the
               "secure mode" of the pager is enabled. In "secure mode",
               LESSSECURE=1 will be set when invoking the pager, which
               instructs the pager to disable commands that open or create
               new files or start new subprocesses. Currently only less(1) is
               known to understand this variable and implement "secure mode".

               When set to false, no limitation is placed on the pager.
               Setting SYSTEMD_PAGERSECURE=0 or not removing it from the
               inherited environment may allow the user to invoke arbitrary
               commands.

               When $SYSTEMD_PAGERSECURE is not set, systemd tools attempt to
               automatically figure out if "secure mode" should be enabled
               and whether the pager supports it. "Secure mode" is enabled if
               the effective UID is not the same as the owner of the login
               session, see geteuid(2) and sd_pid_get_owner_uid(3), or when
               running under sudo(8) or similar tools ($SUDO_UID is set [2]).
               In those cases, SYSTEMD_PAGERSECURE=1 will be set and pagers
               which are not known to implement "secure mode" will not be
               used at all. Note that this autodetection only covers the most
               common mechanisms to elevate privileges and is intended as
               convenience. It is recommended to explicitly set
               $SYSTEMD_PAGERSECURE or disable the pager.

               Note that if the $SYSTEMD_PAGER or $PAGER variables are to be
               honoured, other than to disable the pager,
               $SYSTEMD_PAGERSECURE must be set too.

           $SYSTEMD_COLORS
               Takes a boolean argument, or a special value. By default
               (unset), systemd and related utilities will use colors in
               their output if possible. If $COLORTERM is set to "truecolor"
               or "24bit", 24-bit colors will be enabled, 256 colors
               otherwise, unless $NO_COLOR or $TERM indicates colors are
               disabled.

               true
                   Same as unset, except that $NO_COLOR is ignored.

               false
                   The output will be monochrome.

               "16", "256", "24bit"
                   Always use the base 16 ANSI colors, 256 colors, or 24 bit
                   color, respectively.

               "auto-16", "auto-256", "auto-24bit"
                   Use the given quantity of colours, subject to $TERM, and
                   what the console is connected to.

           $SYSTEMD_URLIFY
               The value must be a boolean. Controls whether clickable links
               should be generated in the output for terminal emulators
               supporting this. This can be specified to override the
               decision that systemd makes based on $TERM and other
               conditions.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-storage-block@.service(8),
           systemd-storage-fs@.service(8), varlinkctl(1), mount(8)

## [](#NOTES)NOTES

            1. Varlink
               https://varlink.org/

            2. It is recommended for other tools to set and check $SUDO_UID
               as appropriate, treating it is a common interface.

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

    systemd 262~devel                                           STORAGECTL(1)

------------------------------------------------------------------------

Pages that refer to this page: [machinectl(1)](../man1/machinectl.1.html),  [systemd-vmspawn(1)](../man1/systemd-vmspawn.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-storage-block@.service(8)](../man8/systemd-storage-block@.service.8.html),  [systemd-storage-fs@.service(8)](../man8/systemd-storage-fs@.service.8.html)

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
