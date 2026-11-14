---
{"title": "updatedb(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/updatedb.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# updatedb(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [BUGS](#BUGS) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                 |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UPDATEDB(1)              General Commands Manual              UPDATEDB(1)

## [](#NAME)NAME

           updatedb - update a file name database

## [](#SYNOPSIS)SYNOPSIS

           updatedb [options]

## [](#DESCRIPTION)DESCRIPTION

           This manual page documents the GNU version of updatedb, which
           updates file name databases used by GNU locate.  The file name
           databases contain lists of files that were in particular directory
           trees when the databases were last updated.  The file name of the
           default database is determined when locate and updatedb are
           configured and installed.  The frequency with which the databases
           are updated and the directories for which they contain entries
           depend on how often updatedb is run, and with which arguments.

           In networked environments, it often makes sense to build a
           database at the root of each filesystem, containing the entries
           for that filesystem.  updatedb is then run for each filesystem on
           the fileserver where that filesystem is on a local disk, to
           prevent thrashing the network.  Users can select which databases
           locate searches using an environment variable or command line
           option; see locate(1).  Databases cannot be concatenated together.

           The LOCATE02 database format was introduced in GNU findutils
           version 4.0 in order to allow machines with different byte
           orderings to share the databases.  GNU locate can read both the
           old and LOCATE02 database formats, though support for the old
           pre-4.0 database format will be removed shortly.

## [](#OPTIONS)OPTIONS

           --findoptions='-option1 -option2...'
                  Global options to pass on to find.  The environment
                  variable FINDOPTIONS also sets this value.  Default is
                  none.

           --localpaths='path1 path2...'
                  Non-network directories to put in the database.  Default is
                  /.

           --netpaths='path1 path2...'
                  Network (NFS, AFS, RFS, etc.) directories to put in the
                  database.  The environment variable NETPATHS also sets this
                  value.  Default is none.

           --prunepaths='path1 path2...'
                  Directories to not put in the database, which would
                  otherwise be.  Remove any trailing slashes from the path
                  names, otherwise updatedb won't recognise the paths you
                  want to omit (because it uses them as regular expression
                  patterns).  The environment variable PRUNEPATHS also sets
                  this value.  Default is /tmp /usr/tmp /var/tmp /afs.

           --prunefs='path...'
                  File systems to not put in the database, which would
                  otherwise be.  Note that files are pruned when a file
                  system is reached; any file system mounted under an
                  undesired file system will be ignored.  The environment
                  variable PRUNEFS also sets this value.  Default is nfs NFS
                  proc.

           --output=dbfile
                  The database file to build.  Default is system-dependent.
                  In Debian GNU/Linux, the default is
                  /var/cache/locate/locatedb.

           --localuser=user
                  The user to search non-network directories as, using su(1).
                  Default is to search the non-network directories as the
                  current user.  You can also use the environment variable
                  LOCALUSER to set this user.

           --netuser=user
                  The user to search network directories as, using su(1).
                  Default is daemon.  You can also use the environment
                  variable NETUSER to set this user.

           --dbformat=F
                  Create the database in format F.  The default format is
                  called LOCATE02.  Alternatively the slocate format is also
                  supported.  When the slocate format is in use, the database
                  produced is marked as having security level 1.  If you want
                  to build a system-wide slocate database, you may want to
                  run updatedb as root.

           --version
                  Print the version number of updatedb and exit.

           --help Print a summary of the options to updatedb and exit.

## [](#BUGS)BUGS

           The updatedb program correctly handles filenames containing
           newlines, but only if the system's sort command has a working -z
           option.  If you suspect that locate may need to return filenames
           containing newlines, consider using its --null option.

## [](#REPORTING_BUGS)REPORTING BUGS

           GNU findutils online help:
           <https://www.gnu.org/software/findutils/#get-help>
           Report any translation bugs to
           <https://translationproject.org/team/>

           Report any other issue via the form at the GNU Savannah bug
           tracker:
                  <https://savannah.gnu.org/bugs/?group=findutils>
           General topics about the GNU findutils package are discussed at
           the bug-findutils mailing list:
                  <https://lists.gnu.org/mailman/listinfo/bug-findutils>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 1994–2026 Free Software Foundation, Inc.  License
           GPLv3+: GNU GPL version 3 or later
           <https://gnu.org/licenses/gpl.html>.
           This is free software: you are free to change and redistribute it.
           There is NO WARRANTY, to the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           find(1), locate(1), xargs(1), locatedb(5)

           Full documentation
           <https://www.gnu.org/software/findutils/updatedb>
           or available locally via: info updatedb

## [](#COLOPHON)COLOPHON

           This page is part of the findutils (find utilities) project.
           Information about the project can be found at 
           ⟨http://www.gnu.org/software/findutils/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://savannah.gnu.org/bugs/?group=findutils⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.savannah.gnu.org/findutils.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-23.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    findutils                       2023-11-10                    UPDATEDB(1)

------------------------------------------------------------------------

Pages that refer to this page: [find(1)](../man1/find.1.html),  [locate(1)](../man1/locate.1.html),  [xargs(1)](../man1/xargs.1.html)

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
