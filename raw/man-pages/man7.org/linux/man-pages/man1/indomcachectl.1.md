---
{"title": "indomcachectl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/indomcachectl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# indomcachectl(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OTHER MANAGEMENT OPTIONS](#OTHER_MANAGEMENT_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    INDOMCACHECTL(1)         General Commands Manual         INDOMCACHECTL(1)

## [](#NAME)NAME

           indomcachectl - manage instance domain cache files

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/indomcachectl [-w] -l indom

           $PCP_BINADM_DIR/indomcachectl [-w] [-m mode] [-g group] [-u user]
           indom

## [](#DESCRIPTION)DESCRIPTION

           indomcachectl assists in the management of the Instance Domain
           cache files that are stored in $PCP_VAR_DIR/config/pmda.

           The mandatory indom parameter uses a 2-dotted format to specify
           the domain and serial fields of the instance domain number.  The
           required values can be reported for a particular metric using the
           -d option to pminfo(1).

           The list of available options can be retrieved using the -?/--help
           option, which displays a usage message and exits.

           If the -l/--list option is specified the contents of the instance
           domain cache file are dumped on stdout and indomcachectl exits.

           Otherwise an empty instance domain cache file will be created.
           The user ownership of the created file is assigned to the uid of
           the caller, but may optionally assigned to the uid of user from
           the passwd(5) file if the -u/--user option is specified.  The
           group ownership of the created file is assigned to the gid of the
           caller, else the default gid of the user user if the -u option is
           specified, else the gid of group from the group(5) file if the
           -g/--group option is specified.

           The instance domain cache file is created with mode 0660 by
           default (some PMDAs use group read-write permission to access and
           update the contents of the file) - if this does not suit the
           -m/--mode option may be used to set the mode to the (octal) value
           mode.

           Because the indom cache files are precious to the associated PMDA
           indomcachectl will not over-write an existing indom cache file.

           Operation is usually silent, except for errors (or warnings if the
           -w/--warning option is used).  The exit status is 0 for success, 1
           for failure.

## [](#OTHER_MANAGEMENT_OPTIONS)OTHER MANAGEMENT OPTIONS

           The files in $PCP_VAR_DIR/config/pmda are all text files (one per
           cached instance domain) so judicious surgery may be used to make
           changes or even remove the files in extreme cases provided the
           PMDA is not executing.

           Here is an example for the instance domain number 60.17 that is
           associated with the network.interface.* metrics.

                $ cat /var/lib/pcp/config/pmda/60.17
                2 0 2147483647
                0 1712727825 ens33
                1 1712727825 virbr0
                2 1712727825 lo

           The first line is a magic header, do not change it.  Following
           that is one line per instance with the instance identifier (an
           integer) in the first field, some magic in the second field (do
           not change this) and the external instance name in the third
           field.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), chmod(1), pminfo(1), PMAPI(3), PMDA(3), pmdaCache(3),
           group(5) and passwd(5).

## [](#COLOPHON)COLOPHON

           This page is part of the PCP (Performance Co-Pilot) project.
           Information about the project can be found at 
           ⟨http://www.pcp.io/⟩.  If you have a bug report for this manual
           page, send it to pcp@groups.io.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/performancecopilot/pcp.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-08-04.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Performance Co-Pilot               PCP                   INDOMCACHECTL(1)

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
