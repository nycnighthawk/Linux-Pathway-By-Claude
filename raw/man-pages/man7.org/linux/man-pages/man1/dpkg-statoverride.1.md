---
{"title": "dpkg-statoverride(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-statoverride.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-statoverride(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-statoverride(1)            dpkg suite           dpkg-statoverride(1)

## [](#NAME)NAME

           dpkg-statoverride - override ownership and mode of files

## [](#SYNOPSIS)SYNOPSIS

           dpkg-statoverride [option...] command

## [](#DESCRIPTION)DESCRIPTION

           “stat overrides” are a way to tell dpkg(1) to use a different
           owner or mode for a path when a package is installed (this applies
           to any filesystem object that dpkg handles, including directories,
           devices, etc.).  This can be used to force programs that are
           normally setuid to be install without a setuid flag, or only
           executable by a certain group.

           dpkg-statoverride is a utility to manage the list of stat
           overrides.  It has three basic functions: adding, removing and
           listing overrides.

## [](#COMMANDS)COMMANDS

           --add user group mode path
               Add an override for path.  path does not need to exist nor be
               known to dpkg when this command is used; the override will be
               stored and used later.  Users and groups can be specified by
               their name (for example root or nobody), or by their number by
               prepending the number with a ‘#’ (for example #0 or #65534).
               The mode needs to be specified in octal.

               If --update is specified and path exists, it is immediately
               set to the new owner and mode.

           --remove path
               Remove an override for path, the status of path is left
               unchanged by this command.

           --list [glob-pattern]
               List all overrides.  If a glob pattern is specified restrict
               the output to overrides which match the glob.

           --help
               Show the usage message and exit.

           --force-help
               Give help about the --force-thing options.

               Supported since dpkg 1.19.5.

           --version
               Show the version and exit.

## [](#OPTIONS)OPTIONS

           --admindir directory
               Set the administrative directory to directory.  This is where
               the statoverride file is stored.  Defaults to
               «/usr/local/var/lib/dpkg» if DPKG_ADMINDIR has not been set.

           --instdir directory
               Set the installation directory, which refers to the directory
               where packages get installed.  Defaults to «/» if DPKG_ROOT
               has not been set.

               Supported since dpkg 1.19.2.

           --root directory
               Set the root directory to directory, which sets the
               installation directory to «directory» and the administrative
               directory to «directory/usr/local/var/lib/dpkg» if DPKG_ROOT
               has not been set.

               Supported since dpkg 1.19.2.

           --force-things
           --no-force-things, --refuse-things
               Force or refuse (no-force and refuse mean the same thing) to
               do some things.  things is a comma separated list of things
               specified below.  --force-help displays a message describing
               them.  Things marked with (*) are forced by default.

               Supported since dpkg 1.19.5.

               Warning: These options are mostly intended to be used by
               experts only.  Using them without fully understanding their
               effects may break your whole system.

               all:
                   Turns on (or off) all force options.

               statoverride-add:
                   Overwrite an existing stat override when adding it.

                   Supported since dpkg 1.19.5.

               statoverride-remove:
                   Ignore a missing stat override when removing it.

                   Supported since dpkg 1.19.5.

               security-mac(*):
                   Use platform-specific Mandatory Access Controls (MAC)
                   based security when installing files into the filesystem.
                   On Linux systems the implementation uses SELinux.

                   Supported since dpkg 1.19.5.

               not-root:
                   Try to (de)install things even when not root.

                   Supported since dpkg 1.21.8.

           --force
               Force an action, even if a sanity check would otherwise
               prohibit it.  This is necessary to override an existing
               override.

               Deprecated since dpkg 1.19.5, replaced by --force-all.

           --update
               Immediately try to change the path to the new owner and mode
               if it exists.

           --quiet
               Be less verbose about what we do.

## [](#EXIT_STATUS)EXIT STATUS

           0   The requested action was successfully performed.

           1   For --list, if there are no overrides or none match the
               supplied glob.

           2   Fatal or unrecoverable error due to invalid command-line
               usage, or interactions with the system, such as accesses to
               the database, memory allocations, etc.

## [](#ENVIRONMENT)ENVIRONMENT

           DPKG_ROOT
               If set and the --instdir or --root options have not been
               specified, it will be used as the filesystem root directory.

               Supported since dpkg 1.19.2.

           DPKG_ADMINDIR
               If set and the --admindir or --root options have not been
               specified, it will be used as the dpkg data directory.

           DPKG_DEBUG
               Sets the debug mask from an octal value.  The currently
               accepted flags are described in the dpkg --debug option, but
               not all these flags might have an effect on this program.

               Supported since dpkg 1.21.10.

           DPKG_FORCE
               If set and none of the --force-... options have been
               specified, it will be used as the force options to use.

               Supported since dpkg 1.19.5.

           DPKG_COLORS
               Sets the color mode.  The currently accepted values are: auto
               (default), always and never.

               Supported since dpkg 1.18.5.

           DPKG_NLS
               If set, it will be used to decide whether to activate Native
               Language Support, also known as internationalization (or i18n)
               support.  The accepted values are: 0 and 1 (default).

               Supported since dpkg 1.22.7.

           DPKG_PATH_PASSWD
               Sets the pathname for the system passwd file.  This path is
               relative to the --root directory.  The default is /etc/passwd.

               Supported since dpkg 1.22.16.

           DPKG_PATH_GROUP
               Sets the pathname for the system group file.  This path is
               relative to the --root directory.  The default is /etc/group.

               Supported since dpkg 1.22.16.

## [](#FILES)FILES

           /usr/local/var/lib/dpkg/statoverride
               File which contains the current list of stat overrides of the
               system.  It is located in the dpkg administration directory,
               along with other files important to dpkg, such as status or
               available.

               Note: dpkg-statoverride preserves the old copy of this file,
               with extension “-old”, before replacing it with the new one.

## [](#SEE_ALSO)SEE ALSO

           dpkg(1).

## [](#COLOPHON)COLOPHON

           This page is part of the dpkg (Debian Package Manager) project.
           Information about the project can be found at 
           ⟨https://wiki.debian.org/Teams/Dpkg/⟩.  If you have a bug report
           for this manual page, see
           ⟨http://bugs.debian.org/cgi-bin/pkgreport.cgi?src=dpkg⟩.  This
           page was obtained from the project's upstream Git repository ⟨git
           clone https://git.dpkg.org/git/dpkg/dpkg.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.23.7-216-gff7e9               2026-03-07           dpkg-statoverride(1)

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
