---
{"title": "pmgetopt(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmgetopt.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmgetopt(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIGURATION](#CONFIGURATION) \| [EXAMPLES](#EXAMPLES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMGETOPT(1)              General Commands Manual              PMGETOPT(1)

## [](#NAME)NAME

           pmgetopt - Performance Co-Pilot shell script option parser

## [](#SYNOPSIS)SYNOPSIS

           $PCP_BINADM_DIR/pmgetopt [-u?]  [-c file] [-D debug] [-p name]
           [--] [parameters]

## [](#DESCRIPTION)DESCRIPTION

           pmgetopt is used to perform command line option parsing for shell
           scripts used in the Performance Co-Pilot (PCP toolkit).  It is
           also used to generate usage messages for those scripts.

           The parameters given to pmgetopt take two forms: initially,
           options specific to pmgetopt itself are passed in, and terminated
           using the -- mechanism.  Thereafter, all of the parameters passed
           into the shell script should be passed (usually this is simply the
           "$@" variable).

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -c=file, --config=file
                A configuration file in the format described below is passed
                to pmconfig using this option.  If this option is omitted,
                then pmconfig will read its configuration from the standard
                input stream.

           -p=name, --progname=name
                When parsing the calling shell scripts parameters, error and
                usage messages will contain the given program name rather
                than referring to pmgetopt itself as the source of the error.

           -u, --usage
                A usage message appropriate for the calling shell script to
                present as its own can be generated using the option.

           -?, --help
                Display the usage message for pmgetopt itself and exit.

           pmgetopt parses the given parameters, and produces output in a
           format suitable for sourcing in the calling shell script.  When
           both short and long forms of an argument are allowed by the
           specification, pmgetopt will always indicate the short form for
           simpler shell processing.  If arguments are presented that do not
           match the configuration, a request for a usage message (-?) will
           be generated for the calling script to respond to.  Any non-option
           parameters will be echoed back to the calling script preceded by
           the double-hyphen delimiter.  Thus a script should stop handling
           options when this delimiter is detected, and begin the handling of
           any non-option arguments.

           Unlike with the shell built-in getopt command, variables like
           $OPTARG are not set and the calling script will typically employ
           use of the shell built-in eval, set and positional shift commands
           to ensure option processing occurs correctly.

## [](#CONFIGURATION)CONFIGURATION

           The configuration format used by pmgetopt is intended to closely
           reflect the usage message which would be generated in the presence
           of invalid arguments (or the -?, --help option).

           There are primarily two types of configuration line - commands and
           options.  Commands allow metadata to be passed into the option
           processing process, and options are the allowable command line
           options that the shell script will accept.  Command lines are
           preceded by the hash character, whereas option lines will always
           begin with a hyphen (either single or double).  Any other line in
           the configuration, which may include usage headers or descriptive
           text, has no impact on the option parsing and will be copied
           unmodified into the usage message.

           The set of commands is: getopt (provide short-argument option
           specification manually, if not present this will be generated from
           the options presented), usage (provide short one-line summary used
           at the head of the usage message, which will be prefixed by the
           progname before reporting), and end which informs pmgetopt to stop
           processing further commands and options - any subsequent text
           encountered will be simply appended to the usage message.

           A short-hand notation exists for each of the standard PCP options,
           as described in PCPIntro(1).  If any of these options (e.g --host)
           appears as a single word on any line, it will be transformed into
           the appropriate option for the shell script, including all
           metadata about that option (whether it accepts an argument, both
           short and long option forms, and so on).

           Use of the equals symbol ("=") indicates the presence of a
           required argument to any option, for both short and long forms.
           Any non-standard option must be accompanied by a non-empty
           description of that argument.

## [](#EXAMPLES)EXAMPLES

           As an example, the following is a valid configuration:

                # Usage: [options] node...

                Options:
                    --archive
                    -d, --delay            pause between updates for archive replay
                    --host
                    --interval
                    -i=INST, --insts=INST  comma-separated metrics instance list
                    -r                     output raw counters (no rate conversion)
                    --width=N              set the width of each column of output
                    --timezone
                    --help

           This configuration will produce the following usage message, when
           run as shown.

                $ pmgetopt --usage --progname=clusterstat -- "$@"
                Usage: clusterstat [options] node...

                Options:
                  -a FILE, --archive=FILE
                                        metrics source is a PCP archive
                  -d, --delay           pause between updates for archive replay
                  -h HOST, --host=HOST  metrics source is PMCD on host
                  -t DELTA, --interval=DELTA
                                        sampling interval
                  -i INST, --insts=INST comma-separated metrics instance list
                  -r                    output raw counters (no rate conversion)
                  --width=N             set the width of each column of output
                  -Z TZ, --timezone=TZ  set reporting timezone
                  -?, --help            show this usage message and exit

           Several examples of pmgetopt use form part of the PCP toolkit, in
           particular the pcp(1) and pmlogmv(1) scripts provide good
           reference examples.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           pcp(1), pmlogmv(1), pmgetopt_r(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                        PMGETOPT(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-xsos(1)](../man1/pcp-xsos.1.html)

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
