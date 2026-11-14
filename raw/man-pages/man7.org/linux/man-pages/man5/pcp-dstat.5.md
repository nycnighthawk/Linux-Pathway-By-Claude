---
{"title": "pcp-dstat(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/pcp-dstat.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp-dstat(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP-DSTAT(5)               File Formats Manual               PCP-DSTAT(5)

## [](#NAME)NAME

           pcp-dstat - pcp-dstat configuration file

## [](#DESCRIPTION)DESCRIPTION

           pcp-dstat is a customizable performance metrics reporting tool.
           It has a ``plugin'' architecture, where a set of pre-defined
           plugins offer small sets of columnar metric reports, and pcp-dstat
           command line options select which of these plugins are used in the
           generated report.

           Each plugin is defined in a section of a configuration file.  A
           typical installation will provide many configuration files, and
           often multiple sections (plugins) within each file.

           Configuration files are read from both a system directory and the
           users home directory ($PCP_SYSCONF_DIR/dstat and
           $HOME/.pcp/dstat).

## [](#FILE_FORMAT)FILE FORMAT

           The configuration files have an ini-style syntax consisting of
           sections (plugins) and options within sections.  A section begins
           with the name of the plugin in square brackets and continues until
           the next section begins.  An example section with two options
           follows:

               [plugin]
               option = value
               metric.option = value2

           A line comment starts with a hash sign (``#'') or a semicolon
           (``;'').  Inline comments are not supported.

           There are some options which apply to the plugin as a whole, and
           anything else is considered to be a column definition.  Column
           definitions map directly to individual PCP metrics.

       The [plugin] options
           label (string)
               The overall title to be used for this plugin.  In the special
               case of metrics with instances being reported as a group (see
               grouptype below) this string may contain the %I pattern, which
               will be substituted with the name of the instance - refer to
               the cpu, disk, net and int(errupts) plugins for examples of
               this special syntax.  Undefined by default, set automatically
               to the section (plugin) name.

           width (integer)
               The column width used for metrics in this plugin.  The default
               is 5.

           precision (integer)
               The maximum precision to be used when reporting columns in
               floating point for this plugin.  Undefined by default, set
               automatically based on width.

           printtype (character)
               Indicates the reporting style for metric values in this
               plugin.  Possible settings are d(ecimal), f(loat), p(ercent),
               s(tring), b(its), t(ime).  By default a setting will be used
               based on the metric type and semantic - refer to PMAPI(3) for
               further details of PCP metric metadata.

           colorstep (integer)
               Indicates a ``step'' at which the next color will be
               transitioned to, when reporting metric values.  As metric
               values change on each sample, the colorstep is used to
               determine the increments beyond which a new color is to be
               selected.  Defaults to 1000.

           grouptype (integer)
               For plugins with metrics sharing the same instance domain, it
               is possible to request more complex grouping behaviour.  The
               default behaviour is to not use instance grouping, and to
               report each instance of the metric in a separate column (the
               load plugin is an example of this, using the kernel.all.load
               metric).

               The grouping can be set at three distinct levels - 1, 2, 3 or
               4.  Level 1 displays instances of metrics only (no totals) -
               this is the equivalent of using the --cpu plugin on the pcp-
               dstat command line with specific processors' utilization
               displayed, e.g. displaying CPU numbers 4, 5 and 12 (-C
               4,5,12).  Level 2 displays the total column - the sum of all
               instances for the specified metric(s) in this plugin.  Level 3
               is a combination of both modes, for example using the pcp-
               dstat --cpu plugin with options -C 4,5,12,total.  Level 4 is a
               top-like mode, where a special "top" expression is used to
               rank all instances - the top-most (largest) value will be
               displayed.

           instances (comma-separated-value string)
               Defines the instances to be reported for the metric.  The
               default is to report all instances for set-values metrics.

           cullinsts (regex pattern)
               An optional regular expression that can be used to cull metric
               instances from the aggregation ('total') in generated reports.
               For example it is common to exclude loopback devices from the
               network interface reports, this is achieved using this option.
               Default is to report on all instances (no culling).

           filtertype (string)
               Used for plugin metrics that allow command-line instance
               filtering options.  The value of the filtertype entry should
               be appropriate for the instance select option being used as
               listed in the table below.

               filtertype    instance select option
               ─────────────────────────────────────
               cpu           -C
               disk          -D
               dm            -L
               md            -M
               part          -P
               int           -I
               net           -N
               net-packets   -N
               swap          -S

       The [plugin] metrics
           Each plugin must have at least one metric associated with it.  Any
           key that is not one of the above global plugin options is
           considered to be a metric specification or a metric option.  These
           keys define the metrics and their report formatting.

           First and foremost, each column is typically represented by an
           individual metric (if the metric is set-valued - i.e. it has
           instances - this will result in multiple columns).  This is
           specified by a new key (column) being set to a metric
           specification.  The column (key) name is an arbitrary word using
           alphabetic characters.  The metric specification is any PCP metric
           name or derived metric specification, allowing basic arithmetic
           calculations to be used to form this individual column.  The
           derived metric syntax is described on the pmRegisterDerived(3)
           manual page.

           Some examples of both forms of metric specification are given
           below in the ``EXAMPLES'' section.  Once a column has been
           associated with a metric, other options specific to that column
           can be set using a dot-separated syntax.

           Metric options

           metric.label
               The subtitle to be used for the reported values of this
               metric.  The default label is the column name from the
               configuration file.

               When set-valued PCP metrics (i.e. with instances) are being
               used, it is often convenient to specify either the instance
               number or instance name in the heading.  This is achieved
               using format specifiers - ``%d'' or ``%i'' for instance
               numbers (e.g. replaced by ``6'' for the sixth processor), and
               ``%s'' or ``%I'' for instance names (e.g. replaced by ``eth0''
               for the ethernet interface).  Available instance names for any
               metric can be discovered via the pminfo(1) or pmprobe(1)
               commands.

           metric.width
               The column width to be used when reporting values for this
               metric.

           metric.unit (string)
               Defines the unit/scale conversion for the metric.  Needs to be
               dimension-compatible and is used with non-string metrics.  For
               allowed values, see pmrep(1).

           metric.type (string)
               If set to raw rate conversion for the metric will be disabled.

           metric.precision (integer)
               Defines precision for floating point values.

           metric.limit (string)
               Defines value limit filter for numeric metric values.

## [](#EXAMPLES)EXAMPLES

           The following example defines a virtual filesystem plugin, with
           two columns, defined using three PCP metrics - vfs.files.count,
           vfs.inodes.count and vfs.inodes.free.  The inodes metrics are
           combined using the derived metric notation.

               [vfs]
               width = 6
               label = filesystem
               files = vfs.files.count
               inode = vfs.inodes.count - vfs.inodes.free
               inode.label = inodes

           The system default pcp-dstat plugin files contain many more
           examples.

## [](#FILES)FILES

           $HOME/.pcp/dstat/
                  private per-user configuration files

           $PCP_SYSCONF_DIR/dstat/
                  system-wide configuration files

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pcp-dstat(1), pminfo(1), pmprobe(1), pmrep(1),
           PMAPI(3), pmGetOptions(3), pmRegisterDerived(3) and pmrep.conf(5).

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

    Performance Co-Pilot               PCP                       PCP-DSTAT(5)

------------------------------------------------------------------------

Pages that refer to this page: [pcp-dstat(1)](../man1/pcp-dstat.1.html)

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
