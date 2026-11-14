---
{"title": "pmlogconf(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogconf.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogconf(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SETUP GROUP FILES](#SETUP_GROUP_FILES) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [MIGRATION](#MIGRATION) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGCONF(1)             General Commands Manual             PMLOGCONF(1)

## [](#NAME)NAME

           pmlogconf - create/edit a pmlogger configuration file

## [](#SYNOPSIS)SYNOPSIS

           pmlogconf [-cqrvV?]  [-d groupsdir] [-D debug] [-g grouptag] [-h
           host] [-s groupfile] configfile

## [](#DESCRIPTION)DESCRIPTION

           pmlogconf may be used to create and modify a generic configuration
           file for the PCP archiver, pmlogger(1).

           If configfile does not exist, pmlogconf will create a generic
           configuration file with a default set of enabled metrics and
           logging intervals.

           Once created, configfile may be used with the -c option to
           pmlogger(1) to select performance metrics and specify logging
           intervals for a PCP archive.

           If configfile does exist, pmlogconf will prompt for input from the
           user to enable or disable groups of related performance metrics
           and to control the logging interval for each enabled group.

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

           A logging interval is specified by responding to the Logging
           interval?  prompt with the keywords once or default or a valid
           pmlogger(1) interval specification of the form ``every N
           timeunits'' or simply ``N timeunits '' (the every is optional)
           where N is an unsigned integer and timeunits is one of the
           keywords msec, millisecond, sec, second, min, minute, hour or the
           plural form of one of the keywords.

           When run from automated logging setup processes, the -c option is
           used to indicate that pmlogconf is in auto-create mode and no
           interactive dialog takes place.  The output configfile has an
           additional comment message and timestamp indicating this fact, so
           that it can be identified and subsequently updated using -c again.
           This option is not appropriate for interactive use of the tool.

           The -q option suppresses the logging interval dialog and preserves
           the current interval from configfile.

           More verbose output may be enabled with the -v option.

## [](#SETUP_GROUP_FILES)SETUP GROUP FILES

           When an initial configfile is created, the default specifications
           come from a set of group files below the groupsdir specified with
           the -d option (the default groupsdir is
           $PCP_VAR_DIR/config/pmlogconf which is most commonly correct, so
           the -d option is rarely used in practice).

           The directory structure below groupsdir is arbitrary as all
           regular files will be found by recursive descent and considered,
           so add-on products and PMDA developers can easily extend the
           available defaults to pmlogconf by adding new directories and/or
           group files below groupsdir.

           These group files are processed in the following ways:

           •  When a new configfile is created, all group files are
              processed.

           •  Whenever pmlogconf is run with an existing configfile,
              groupsdir is traversed to see if any new groups have been
              defined and should be considered for inclusion in configfile.

           •  When pmlogconf processes a group in configfile that is enabled,
              the list of metrics associated with the group is taken from the
              group file (and replaces any previous list of metrics
              associated with this group in configfile).

           •  When either the -r (reprobe) or the -c (auto-create) command
              line option is specified, every group (not just newly
              discovered ones) is reprocessed to see if it should be
              considered for inclusion in configfile.

           •  If a group is found in configfile but the corresponding group
              does not exist below groupsdir (as would be the case when a
              group is made obsolete by a PCP upgrade) then the handling of
              the group depends on the mode in which pmlogconf is being run.
              With -c the corresponding group is culled from configfile,
              otherwise the corresponding group is unchanged in configfile.
              In either case a warning is issued.

           Each group file is structured as follows:

           •  The first line must contain #pmlogconf-setup 2.0

           •  Other lines beginning with # are treated as comments.

           •  Blank lines are ignored.

           •  One or more lines starting with the keyword ident are used to
              provide the human-readable description of the group.

           •  Non-blank lines beginning with white space define metrics to be
              associated with this group, one per line.  Each metric
              specification follows the rules for a pmlogger(1)
              configuration, namely either the name of a non-leaf node in the
              PMNS (implying all descendent names in the PMNS), or the name
              of a leaf node in the PMNS optionally followed by one or more
              instance names enclosed by ``['' and ``]''.

           •  A control line starting with one of the keywords probe or force
              must be present.

           •  An optional logging interval control line begins with the
              keyword delta followed by one of the pmlogger(1) interval
              specification described above.

           •  An optional derived metric control lines begin with the keyword
              define and have the format:
                   define name expr
              where name is the name of a derived metric and expr is a
              derived metric expression.  Refer to pmRegisterDerived(3) for
              the syntactic and semantic descriptions of name and expr.  Once
              defined, name may be used as the metric in a subsequent probe
              control line, allowing the expression of more complex guards
              for conditional inclusion of metrics in configfile.

              Note that name needs to be unique across all group files and
              not collide with an existing name in the PMNS.  So some
              suitable naming convention may need to be adopted when the
              group files are created.

           •  probe control lines have the format:
                   probe metric [condition [state_rule] ]
              where metric is the name of a PCP metric (must be a leaf node
              in the PMNS, no instance specification is allowed, and it must
              not be a derived metric, other than one mentioned in a previous
              define control line) and the optional condition is the keyword
              exists (true if metric exists, i.e. is defined in the PMNS) or
              the keyword values (true if metric exists in the PMNS and has
              one or more current values) or an expression of the form
                   op val where op is one of the awk(1) operators (==, !=, >,
              >=, <, <=, ~ (regular expression match) or !~ (negated regular
              expression match)) and val is a value (arbitrary sequence of
              characters, excluding a space) and the condition is true if
              there is some instance of metric that makes the expression
              true.

              If the condition is missing, the default is exists.

              When an explicit condition is provided, there may also be an
              optional state_rule of the form
                   ? true_state : false_state where true_state (applies if
              condition is true) and false_state (applies if condition is
              false) are both taken from the keywords include (include and
              enable the group and the associated metrics in configfile),
              available (include and disable the group in configfile - a user
              action of y, as described above when configfile already exists,
              is needed to enable the group and add the associated metrics
              into configfile) or exclude (the group is not considered for
              inclusion in configfile).

              The default state_rule is
                   ? available : exclude

           •  force control lines begin with the keyword force followed by
              one of the states defined above, so one of the actions include,
              exclude or available is applied unconditionally to the group.

           Probing is only done when a new group is being added to configfile
           or when the -r command line option is specified.  The evaluation
           of the probing conditions is done by contacting pmcd(1) on
           hostname (defaults to local:).

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -c   Enable non-interactive, auto-create mode.

           -d groupsdir, --groups=groupsdir
                Specify the path to the groupsdir directory.

           -g grouptag, --group=grouptag
                Query logging state for the specific logging group named
                grouptag.

           -h host, --host=host
                Performance metrics source is pmcd(1) on host, rather than on
                the default localhost.

           -q, --quiet
                Quiet mode, suppress logging interval dialog.

           -r, --reprobe
                Reconsider every group for inclusion in the configfile.

           -s groupfile, --setup=groupfile
                Report the default logging state for the one logging group in
                groupfile.  This is equivalent output to that produced by the
                retired pmlogconf-setup shell script from earlier versions of
                PCP.

           -v, --verbose
                Enable verbose mode.

           -V, --version
                Display version number and exit.

           -?, --help
                Display usage message and exit.

## [](#EXAMPLES)EXAMPLES

           The following group file demonstrates most of the supported
           syntactic elements.

           #pmlogconf-setup 2.0
           ident   Example group file
           ident   ... more description
           delta   1 minute
           probe   sample.secret.foo.one values ? include : exclude
                   sample.secret.foo.one
                   sample.secret.foo.bar   # non-leaf in the PMNS
                   sample.colour [ red green ]

           In the following example (backslashes have been added for
           readability, the define clause is all on one line), the mumble
           metrics will be included in configfile if either the mumble.foo
           metric is known and has at least one instance (and value) or the
           mumble.bar metric is known and has at least one instance (and
           value):

           #pmlogconf-setup 2.0
           ident   Derived metric example with alternation
           define  mumble.check = \
                       (defined(mumble.foo) ? count(mumble.foo) : 0) + \
                       (defined(mumble.bar) ? count(mumble.bar) : 0)
           probe   mumble.check > 0 ? include : exclude
                   mumble

           The following example uses a derived metric to access one
           particular metric instance in a probe control line.

           #pmlogconf-setup 2.0
           ident   Derived metric example using a single metric instance
           define  fumble_log = fumble.control[verbose_log]
           probe   fumble_log > 0 ? include : exclude
                   fumble.detailed

## [](#MIGRATION)MIGRATION

           The current version of pmlogconf (2.0) supports a slightly
           different format for configfile compared to earlier versions.  If
           an old version configfile is presented to pmlogconf it will be
           converted to the new format.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           pmlogconf overrides any $PCP_DERIVED_CONFIG environment variable
           to an empty string, for performance reasons and to prevent the
           inclusion of derived metrics in configfile .

           pmlogconf honours the $PMCD_WAIT_TIMEOUT environment variable when
           probing and creating new pmlogger configuration files.  It uses a
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

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmlogconf are as follows:
           ┌────────┬───────────────────────────────────────────────────┐
           │ Option │ Description                                       │
           ├────────┼───────────────────────────────────────────────────┤
           │ appl0  │ group file operations                             │
           ├────────┼───────────────────────────────────────────────────┤
           │ appl1  │ metric probe operations                           │
           ├────────┼───────────────────────────────────────────────────┤
           │ appl2  │ verbose dumping of internal group data structures │
           └────────┴───────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           pmcd(1), pmlogger(1), PMAPI(3), pmRegisterDerived(3), pcp.conf(5)
           and pcp.env(5).

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

    Performance Co-Pilot               PCP                       PMLOGCONF(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp(1)](../man1/pcp.1.html),  [pcpcompat(1)](../man1/pcpcompat.1.html),  [pmdasockets(1)](../man1/pmdasockets.1.html),  [pmlogctl(1)](../man1/pmlogctl.1.html),  [pmlogger_check(1)](../man1/pmlogger_check.1.html),  [pmlogger_daily(1)](../man1/pmlogger_daily.1.html),  [pmrepconf(1)](../man1/pmrepconf.1.html)

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
