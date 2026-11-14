---
{"title": "dpkg-trigger(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-trigger.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-trigger(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                       |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-trigger(1)                 dpkg suite                dpkg-trigger(1)

## [](#NAME)NAME

           dpkg-trigger - a package trigger utility

## [](#SYNOPSIS)SYNOPSIS

           dpkg-trigger [option...] trigger-name

           dpkg-trigger [option...] command

## [](#DESCRIPTION)DESCRIPTION

           dpkg-trigger is a tool to explicitly activate triggers and check
           for its support on the running dpkg.

           This can be used by maintainer scripts in complex and conditional
           situations where the file triggers, or the declarative activate
           triggers control file directive, are insufficiently rich.  It can
           also be used for testing and by system administrators (but note
           that the triggers won't actually be run by dpkg-trigger).

           Unrecognized trigger name syntaxes are an error for dpkg-trigger.

           This program was introduced in dpkg 1.14.17.

## [](#COMMANDS)COMMANDS

           --check-supported
               Check if the running dpkg supports triggers (usually called
               from a postinst).  Will exit 0 if a triggers-capable dpkg has
               run, or 1 with an error message to stderr if not.  Normally,
               however, it is better just to activate the desired trigger
               with dpkg-trigger.

           -?, --help
               Show the usage message and exit.

           --version
               Show the version and exit.

## [](#OPTIONS)OPTIONS

           --admindir=dir
               Change the location of the dpkg database.  Defaults to
               /usr/local/var/lib/dpkg if DPKG_ADMINDIR has not been set.

           --root=directory
               Set the root directory to directory, which sets the
               administrative directory to
               «directory/usr/local/var/lib/dpkg».

               Supported since dpkg 1.21.0.

           --by-package=package
               Override trigger awaiter (normally set by dpkg through the
               DPKG_MAINTSCRIPT_PACKAGE environment variable of the
               maintainer scripts, naming the package to which the script
               belongs, and this will be used by default).

           --no-await
               This option arranges that the calling package T (if any) need
               not await the processing of this trigger; the interested
               package(s) I, will not be added to T's trigger processing
               awaited list and T's status is unchanged.  T may be considered
               installed even though I may not yet have processed the
               trigger.

           --await
               This option does the inverse of --no-await.  If the interested
               package has declared a “noawait” directive, then this option
               will not be effective.  It is currently the default behavior.

               Supported since dpkg 1.17.21.

           --no-act
               Just test, do not actually change anything.

## [](#EXIT_STATUS)EXIT STATUS

           0   The requested action was successfully performed.  Or a check
               or assertion command returned true.

           1   A check or assertion command returned false.

           2   Fatal or unrecoverable error due to invalid command-line
               usage, or interactions with the system, such as accesses to
               the database, memory allocations, etc.

## [](#ENVIRONMENT)ENVIRONMENT

           DPKG_ROOT
               If set and the --root option has not been specified, it will
               be used as the filesystem root directory.

               Supported since dpkg 1.21.0.

           DPKG_ADMINDIR
               If set and the --admindir option has not been specified, it
               will be used as the dpkg data directory.

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

## [](#SEE_ALSO)SEE ALSO

           dpkg(1), deb-triggers(5),
           /usr/local/share/doc/dpkg/spec/triggers.txt.

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

    1.23.7-216-gff7e9               2026-03-07                dpkg-trigger(1)

------------------------------------------------------------------------

Pages that refer to this page: [deb-triggers(5)](../man5/deb-triggers.5.html)

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
