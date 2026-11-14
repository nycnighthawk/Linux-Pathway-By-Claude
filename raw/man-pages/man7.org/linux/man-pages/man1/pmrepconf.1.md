---
{"title": "pmrepconf(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmrepconf.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmrepconf(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SETUP GROUP FILES](#SETUP_GROUP_FILES) \| [OPTIONS](#OPTIONS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMREPCONF(1)             General Commands Manual             PMREPCONF(1)

## [](#NAME)NAME

           pmrepconf - create/edit a pmrep configuration file

## [](#SYNOPSIS)SYNOPSIS

           pmrepconf [-crvV?]  [-D debug] [-d groupsdir] [-g grouptag] [-o
           option] [-h host] configfile

## [](#DESCRIPTION)DESCRIPTION

           pmrepconf may be used to create and modify a generic configuration
           file for pmrep(1) and related utilities in the pmrep.conf(5)
           format.

           If configfile does not exist, pmrepconf will create a generic
           configuration file with a set of discovered metrics in a [metrics]
           section.

           Once created, configfile may be used with the -c option to
           pmrep(1) and related utilities such as pcp2elasticsearch(2) and
           pcp2spark(2).

           If configfile does exist, pmrepconf will prompt for input from the
           user to enable or disable groups of related performance metrics.

           Group selection requires a simple y (yes) or n (no) response to
           the prompt Log this group?.

           Other responses at this point may be used to select additional
           control functions as follows:

           m         Report the names of the metrics in the current group.

           q         Finish with group selection (quit) and make no further
                     changes to this group or any subsequent group.

           /pattern  Make no change to this group but search for a group
                     containing pattern in the description of the group or
                     the names of the associated metrics.

           When run from automated setup processes, the -c option is used to
           indicate that pmrepconf is in auto-create mode and no interactive
           dialog takes place.  The output configfile has an additional
           comment message and timestamp indicating this fact, so that it can
           be identified and subsequently updated using -c again.  This
           option is not appropriate for interactive use of the tool.

           More verbose output may be enabled with the -v option.

## [](#SETUP_GROUP_FILES)SETUP GROUP FILES

           When an initial configfile is created, the default specifications
           come from a set of group files below the groupsdir specified with
           the -d option (the default groupsdir is
           $PCP_VAR_DIR/config/pmlogconf which is most commonly correct, so
           the -d option is rarely used in practice).

           The directory structure and format of files below groupsdir is
           shared with the pmlogconf(1) utility, and described in detail on
           that manual page.  When used by pmrepconf all interval settings
           are ignored.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -c   Enable non-interactive, auto-create mode.

           -d groupsdir, --groups=groupsdir
                Specify the path to the groupsdir directory.

           -g grouptag, --group=grouptag
                Query logging state for the specific group named grouptag.

           -h host, --host=host
                Performance metrics source is pmcd(1) on host, rather than on
                the default localhost.

           -o option, --option=option
                Specify an option to be added to the [option] section of the
                generated pmrep.conf(5) file.  This command line option can
                be presented multiple times in order to added multiple lines
                in the [option] section.

           -r, --reprobe
                Reconsider every group for inclusion in the configfile.

           -v, --verbose
                Enable verbose mode.

           -V, --version
                Display version number and exit.

           -?, --help
                Display usage message and exit.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           pmrepconf overrides any $PCP_DERIVED_CONFIG environment variable
           to an empty string, for performance reasons.

           pmrepconf honours the $PMCD_WAIT_TIMEOUT environment variable when
           probing and creating new pmrep configuration files.  It uses a
           default timeout value of 10 seconds for this, in the absence of an
           environment setting.

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           pcp2elasticsearch(1), pcp2spark(1), pmcd(1), pmlogconf(1),
           pmrep(1), pcp.conf(5), pcp.env(5) and pmrep.conf(5)

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

    Performance Co-Pilot               PCP                       PMREPCONF(1)

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
