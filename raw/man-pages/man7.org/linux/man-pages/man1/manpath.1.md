---
{"title": "manpath(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/manpath.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# manpath(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MANPATH(1)                  Manual pager utils                 MANPATH(1)

## [](#NAME)NAME

           manpath - determine search path for manual pages

## [](#SYNOPSIS)SYNOPSIS

           manpath [-qgdc?V] [-m system[,...]] [-C file]

## [](#DESCRIPTION)DESCRIPTION

           If $MANPATH is set, manpath will simply display its contents and
           issue a warning.  If not, manpath will determine a suitable manual
           page hierarchy search path and display the results.

           The colon-delimited path is determined using information gained
           from the man-db configuration file – (/usr/local/etc/man_db.conf)
           and the user's environment.

## [](#OPTIONS)OPTIONS

           -q, --quiet
                  Do not issue warnings.

           -d, --debug
                  Print debugging information.

           -c, --catpath
                  Produce a catpath as opposed to a manpath.  Once the
                  manpath is determined, each path element is converted to
                  its relative catpath.

           -g, --global
                  Produce a manpath consisting of all paths named as "global"
                  within the man-db configuration file.

           -m system[,...], --systems=system[,...]
                  If this system has access to other operating systems'
                  manual hierarchies, this option can be used to include them
                  in the output of manpath.  To include NewOS's manual page
                  hierarchies use the option -m NewOS.

                  The system specified can be a combination of comma
                  delimited operating system names.  To include the native
                  operating system's manual page hierarchies, the system name
                  man must be included in the argument string.  This option
                  will override the $SYSTEM environment variable.

           -C file, --config-file=file
                  Use this user configuration file rather than the default of
                  ~/.manpath.

           -?, --help
                  Print a help message and exit.

           --usage
                  Print a short usage message and exit.

           -V, --version
                  Display version information.

## [](#ENVIRONMENT)ENVIRONMENT

           MANPATH
                  If $MANPATH is set, manpath displays its value rather than
                  determining it on the fly.

                  See the SEARCH PATH section of manpath(5) for the default
                  behaviour and details of how this environment variable is
                  handled.

           SYSTEM If $SYSTEM is set, it will have the same effect as if it
                  had been specified as the argument to the -m option.

## [](#FILES)FILES

           /usr/local/etc/man_db.conf
                  man-db configuration file.

## [](#SEE_ALSO)SEE ALSO

           apropos(1), man(1), whatis(1)

## [](#AUTHOR)AUTHOR

           Wilf. (G.Wilford@ee.surrey.ac.uk).
           Fabrizio Polacco (fpolacco@debian.org).
           Colin Watson (cjwatson@debian.org).

## [](#BUGS)BUGS

           https://gitlab.com/man-db/man-db/-/issues
           https://savannah.nongnu.org/bugs/?group=man-db

## [](#COLOPHON)COLOPHON

           This page is part of the man-db (manual pager suite) project.
           Information about the project can be found at 
           ⟨http://www.nongnu.org/man-db/⟩.  If you have a bug report for this
           manual page, send it to man-db-devel@nongnu.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://gitlab.com/cjwatson/man-db⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-13.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    2.13.1                          2025-05-02                     MANPATH(1)

------------------------------------------------------------------------

Pages that refer to this page: [man(1)](../man1/man.1.html)

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
