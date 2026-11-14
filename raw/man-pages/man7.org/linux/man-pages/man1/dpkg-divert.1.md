---
{"title": "dpkg-divert(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-divert.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-divert(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-divert(1)                  dpkg suite                 dpkg-divert(1)

## [](#NAME)NAME

           dpkg-divert - override a package's version of a file

## [](#SYNOPSIS)SYNOPSIS

           dpkg-divert [option...]  command

## [](#DESCRIPTION)DESCRIPTION

           dpkg-divert is the utility used to set up and update the list of
           diversions.

           File diversions are a way of forcing dpkg(1) not to install a file
           into its location, but to a diverted location.  Diversions can be
           used through the package maintainer scripts to move a file away
           when it causes a conflict.  System administrators can also use it
           to override some package's configuration file, or whenever some
           files (which aren't marked as “conffiles”) need to be preserved by
           dpkg, when installing a newer version of a package which contains
           those files.

## [](#COMMANDS)COMMANDS

           [--add] file
               Add a diversion for file.  The file is currently not renamed,
               see --rename.

           --remove file
               Remove a diversion for file.  The file is currently not
               renamed, see --rename.

           --list [glob-pattern]
               List all diversions, or ones matching glob-pattern.

           --listpackage file
               Print the name of the package that diverts file.  Prints LOCAL
               if file is locally diverted and nothing if file is not
               diverted.

               Supported since dpkg 1.15.0.

           --truename file
               Print the real name for a diverted file.

## [](#OPTIONS)OPTIONS

           --admindir directory
               Set the administrative directory to directory.  Defaults to
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

           --divert divert-to
               divert-to is the location where the versions of file, as
               provided by other packages, will be diverted.

           --local
               Specifies that all packages' versions of this file are
               diverted.  This means, that there are no exceptions, and
               whatever package is installed, the file is diverted.  This can
               be used by an admin to install a locally modified version.

           --package package
               package is the name of a package whose copy of file will not
               be diverted.  i.e. file will be diverted for all packages
               except package.

           --quiet
               Quiet mode, i.e. no verbose output.

           --rename
               Actually move the file aside (or back).  dpkg-divert will
               abort operation in case the destination file already exists.
               This is the common behavior used for diversions of files from
               the non-Essential package set (see --no-rename for more
               details).

           --no-rename
               Specifies that the file should not be renamed while adding or
               removing the diversion into the database.  This is intended
               for diversions of files from the Essential package set, where
               the temporary disappearance of the original file is not
               acceptable, as it can render the system non-functional.  This
               is the default behavior, which will change once there are no
               known users, but not before the dpkg 1.23.x release cycle.

               Supported since dpkg 1.19.1.

           --test
               Test mode, i.e. don't actually perform any changes, just
               demonstrate.

           -?, --help
               Show the usage message and exit.

           --version
               Show the version and exit.

## [](#EXIT_STATUS)EXIT STATUS

           0   The requested action was successfully performed.

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

           DPKG_MAINTSCRIPT_PACKAGE
               If set and the --local and --package options have not been
               specified, dpkg-divert will use it as the package name.

           DPKG_DEBUG
               Sets the debug mask from an octal value.  The currently
               accepted flags are described in the dpkg --debug option, but
               not all these flags might have an effect on this program.

               Supported since dpkg 1.21.10.

           DPKG_COLORS
               Sets the color mode.  The currently accepted values are: auto
               (default), always and never.

               Supported since dpkg 1.18.5.

           DPKG_NLS
               If set, it will be used to decide whether to activate Native
               Language Support, also known as internationalization (or i18n)
               support.  The accepted values are: 0 and 1 (default).

               Supported since dpkg 1.22.7.

## [](#FILES)FILES

           /usr/local/var/lib/dpkg/diversions
               File which contains the current list of diversions of the
               system.  It is located in the dpkg administration directory,
               along with other files important to dpkg, such as status or
               available.

               Note: dpkg-divert preserves the old copy of this file, with
               extension -old, before replacing it with the new one.

## [](#NOTES)NOTES

           When adding, default is --local and --divert original.distrib.
           When removing, --package or --local and --divert must match if
           specified.

           Directories can't be diverted with dpkg-divert.

           Care should be taken when diverting shared libraries, ldconfig(8)
           creates a symbolic link based on the DT_SONAME field embedded in
           the library.  Because ldconfig does not honor diverts (only dpkg
           does), the symlink may end up pointing at the diverted library, if
           a diverted library has the same SONAME as the undiverted one.

## [](#EXAMPLES)EXAMPLES

           To divert all copies of a /usr/bin/example to
           /usr/bin/example.foo, i.e. directs all packages providing
           /usr/bin/example to install it as /usr/bin/example.foo, performing
           the rename if required:

            dpkg-divert --divert /usr/bin/example.foo --rename /usr/bin/example

           To remove that diversion:

            dpkg-divert --rename --remove /usr/bin/example

           To divert any package trying to install /usr/bin/example to
           /usr/bin/example.foo, except your own wibble package:

            dpkg-divert --package wibble --divert /usr/bin/example.foo \
               --rename /usr/bin/example

           To remove that diversion:

            dpkg-divert --package wibble --rename --remove /usr/bin/example

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

    1.23.7-216-gff7e9               2026-03-07                 dpkg-divert(1)

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
