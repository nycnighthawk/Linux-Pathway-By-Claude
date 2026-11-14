---
{"title": "pmstore(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmstore.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmstore(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMSTORE(1)               General Commands Manual               PMSTORE(1)

## [](#NAME)NAME

           pmstore - modify performance metric values

## [](#SYNOPSIS)SYNOPSIS

           pmstore [-fFLV?]  [-D debug] [-h host] [-i instances] [-K spec]
           [-n pmnsfile] metricname value

## [](#DESCRIPTION)DESCRIPTION

           Under certain circumstances, it is useful to be able to modify the
           values of performance metrics, for example to re-initialize
           counters or to assign new values to metrics that act as control
           variables.

           pmstore changes the current values for the nominated instances of
           a single performance metric, as identified by metricname and the
           list of instance identifiers following the -i argument.  instances
           must be a single argument, with elements of the list separated by
           commas and/or white space.  By default all instances of metricname
           will be updated.

           Normally pmstore operates on the default Performance Metrics Name
           Space (PMNS), see PMNS(5), however if the -n option is specified
           an alternative namespace is loaded from the file pmnsfile.

           Unless directed to another host by the -h option, pmstore will
           interact with the Performance Metric Collector Daemon (PMCD) on
           the local host.

           The -L option causes pmstore to use a local context to store to
           metrics from PMDAs on the local host without PMCD.  Only some
           metrics are available in this mode.  The -h and -L options are
           mutually exclusive.

           The -f option forces the given value to be stored, even if there
           is no current value set.

           The interpretation of value is dependent on the syntax used in its
           specification and the underlying data type of metricname, as
           follows.

           1.  If the metric has an integer type, then value should be an
               optional leading hyphen, followed either by decimal digits or
               ``0x'' and some hexadecimal digits.  ``0X'' is also acceptable
               in lieu of ``0x''.  See strtol(3) and the related routines.

           2.  If the metric has a floating point type, then value should be
               either in the form of an integer described above, or a fixed
               point number, or a number in scientific notation.  See
               strtod(3).

           3.  If the metric has a string type, then value is interpreted as
               a literal string of ASCII characters.

           4.  If the metric has any other type (i.e.  PM_TYPE_EVENT or
               PM_TYPE_AGGREGATE) then no encoding of value from the command
               line makes sense, and the values of these metrics cannot be
               modified with pmstore.

           The output reports the old value and the new value for each
           updated instance of the requested metric.

           When using the -L option to fetch metrics from a local context,
           the -K option may be used to control the DSO PMDAs that should be
           made accessible.  The spec argument conforms to the syntax
           described in pmSpecLocalPMDA(3).  More than one -K option may be
           used.

           Normally pmstore will report the old value (as initially retrieved
           using pmFetch(3)) and the new value from the command line.  The -F
           option forces another pmFetch(3) after the pmStore(3) and the
           returned value is reported as the new value.  This is useful in
           cases where metricname is a metric that provides different
           semantics for the store operation, e.g. to increment the current
           value or reset a counter (independent of the value from the
           command line).

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -f, --force
                Store the value even if no current value set.

           -F, --fetch
                Report the metric value after setting it.

           -i insts, --insts=insts
                Restrict store to the comma-separated list of instances.

           -h host, --host=host
                Connect to pmcd(1) on host, rather than on the default
                localhost.

           -K spec, --spec-local=spec
                When fetching metrics from a local context (see -L), the -K
                option may be used to control the DSO PMDAs that should be
                made accessible.  The spec argument conforms to the syntax
                described in pmSpecLocalPMDA(3).  More than one -K option may
                be used.

           -L, --local-PMDA
                Use a local context to collect metrics from DSO PMDAs on the
                local host without PMCD.  See also -K.

           -n pmnsfile, --namespace=pmnsfile
                Normally pmcd loads the default Performance Metrics Name
                Space (PMNS) from $PCP_VAR_DIR/pmns/root, however if the -n
                option is specified an alternative namespace is loaded from
                the file pmnsfile.

           -V, --version
                Display version number and exit.

           -?, --help
                Display usage message and exit.

## [](#DIAGNOSTICS)DIAGNOSTICS

           Two messages indicate a mismatch between the internal data type
           for metricname and the value provided.

           The value "???" is out of range for the data type (PM_TYPE_...)

           The value "???" is incompatible with the data type (PM_TYPE_...)

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

           pmcd(1), pminfo(1), pmval(1), PMAPI(3), pmFetch(3),
           pmSpecLocalPMDA(3), pmStore(3), strtod(3), strtol(3) and PMNS(5).

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

    Performance Co-Pilot               PCP                         PMSTORE(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-ss(1)](../man1/pcp-ss.1.html),  [pmcd(1)](../man1/pmcd.1.html),  [pmdacifs(1)](../man1/pmdacifs.1.html),  [pmdadm(1)](../man1/pmdadm.1.html),  [pmdagfs2(1)](../man1/pmdagfs2.1.html),  [pmdagluster(1)](../man1/pmdagluster.1.html),  [pmdahacluster(1)](../man1/pmdahacluster.1.html),  [pmdaopenmetrics(1)](../man1/pmdaopenmetrics.1.html),  [pmdaopentelemetry(1)](../man1/pmdaopentelemetry.1.html),  [pmdaoracle(1)](../man1/pmdaoracle.1.html),  [pmdaproc(1)](../man1/pmdaproc.1.html),  [pmdasockets(1)](../man1/pmdasockets.1.html),  [pmdaweblog(1)](../man1/pmdaweblog.1.html),  [pmdaxfs(1)](../man1/pmdaxfs.1.html),  [pcpintro(3)](../man3/pcpintro.3.html),  [pmdastore(3)](../man3/pmdastore.3.html)

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
