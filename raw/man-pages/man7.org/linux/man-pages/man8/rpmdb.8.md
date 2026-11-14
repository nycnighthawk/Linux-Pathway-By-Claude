---
{"title": "rpmdb(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rpmdb.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpmdb(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPERATIONS](#OPERATIONS) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                               |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPMDB(8)                 System Manager's Manual                 RPMDB(8)

## [](#NAME)NAME

           rpmdb - RPM Database Tool

## [](#SYNOPSIS)SYNOPSIS

       Maintenance
           rpmdb [options] {--initdb|--rebuilddb|--parkdb}

       Diagnostics
           rpmdb [options] {--verifydb}

       Migration
           rpmdb [options] {--exportdb|--importdb}

## [](#DESCRIPTION)DESCRIPTION

           The rpmdb tool is used for low-level rpm database operations.

## [](#OPERATIONS)OPERATIONS

       Maintenance
           --initdb
               Create a new database if one doesn't already exist. An
               existing database is not overwritten.

           --rebuilddb
               Rebuild the database from the installed package headers.
               Discards any unreadable (corrupt) headers and compacts the
               database in case it has grown large over time.

               Can also be used to convert between different rpmdb formats.

           --parkdb
               Park the database. Prepares and optimizes the database for
               inclusion on read-only media, such as immutable OS images.

               Write operations, such as RPM transactions, will unpark the
               database and continue normally, leaving the database unparked
               when finished. Thus, to unpark manually, use --rebuilddb.

               Depending on the backend used, this operation may include the
               removal of auxiliary, backend-specific files from disk, such
               as the write-ahead log or shared memory index, and thus
               facilitate bit-for-bit reproducible OS images.

       Diagnostics
           --verifydb
               Perform a low-level integrity check on the database. Rarely
               useful, for system health rpm --verify -a is a far more
               meaningful operation.

       Migration
           --exportdb
               Export the database in header-list format, suitable for
               transporting to another host or database type. The data is
               output to standard output.

           --importdb
               Imports a database from a header-list format as created by
               --exportdb. The data is read from standard input.

## [](#OPTIONS)OPTIONS

           See rpm-common(8) for the options common to all rpm executables.

## [](#CONFIGURATION)CONFIGURATION

           There are several configurables affecting the rpmdb operations,
           but in particular the following (see rpm-config(5) for details):
           •   %_dbpath
           •   %_db_backend

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           rpmdb --initdb --dbpath /tmp/testdb
               Initialize a new database in /tmp/testdb directory.

           rpmdb --rebuilddb
               Rebuild the system database.

           rpmdb --parkdb
               Park the system database prior to inclusion on read-only
               media.

           rpmdb --verifydb --root /mnt
               Verify the system database of a system image mounted at /mnt.

           rpmdb --exportdb > /tmp/headers
               Export the system database to /tmp/headers file.

           rpmdb --importdb --define "_db_backend ndb" --dbpath /tmp/newdb <
           /tmp/headers
               Import contents of /tmp/headers header list to a (new) ndb-
               format database in /tmp/newdb.

## [](#OPTIONS)OPTIONS

           See rpm-common(8) for the options common to all operations.

## [](#SEE_ALSO)SEE ALSO

           popt(3), rpm(8), rpm-common(8)

           rpmdb --help - as rpm(8) supports customizing the options via popt
           aliases it's impossible to guarantee that what's described in the
           manual matches what's available.

           http://www.rpm.org/ 

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03                       RPMDB(8)

------------------------------------------------------------------------

Pages that refer to this page: [yum-ovl(1)](../man1/yum-ovl.1.html),  [rpm(8)](../man8/rpm.8.html),  [rpm-common(8)](../man8/rpm-common.8.html)

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
