---
{"title": "perfevent.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/perfevent.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# perfevent.conf(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PERFEVENT.CONF(5)          File Formats Manual          PERFEVENT.CONF(5)

## [](#NAME)NAME

           perfevent.conf - the Performance Co-Pilot perfevent PMDA
           configuration file

## [](#SYNOPSIS)SYNOPSIS

           $PCP_PMDAS_DIR/perfevent/perfevent.conf

## [](#DESCRIPTION)DESCRIPTION

           The perfevent.conf configuration file defines which hardware
           performance counters are enabled by the perfevent PMDA.

           The configuration file contains a list of events that should be
           enabled for each PMU. The perfevent PMDA detects which PMUs
           present and programs the configured events. If multiple PMUs are
           available, the perfevent PMDA uses the order of the entries in the
           configuration file to determine which PMU settings to use. The
           entries at the top of the configuration file have higher
           precedence.  Only one PMU configuration setting is used. The
           configuration file may also contain perf derived events. A derived
           event has a list of events which must be listed as base events.
           The values for the counters in the derived events are aggregated
           and displayed.

## [](#FILE_FORMAT)FILE FORMAT

           The file consists of one or more groups of PMUs and the events
           that go with them.

           The PMU identification string is enclosed in brackets and one or
           more events are listed below, one per line.

                  ["PMU identification string"]
                  EVENT_NAME [CPU OPTION]
                  ...

           For derived events, one or more groups of events can be specified
           where, counters in one group can be specific to one architecture
           and the counters in other group can be specific to some other
           architecture. Else, only one group can be specified. EVENT_NAME_1,
           EVENT_NAME_2 etc. belong to group 1 and EVENT_NAME_3, EVENT_NAME_4
           belong to group 2 and so on. If any of the event in the first
           group is not available, entire group will be discarded. And, the
           next group will be checked. The first group with all the events
           available will be activated and monitored. The derived perf event
           is enclosed in brackets along with :derived as a suffix. Note that
           the EVENT_NAME listed under derived event must be present as a
           base event in the configuration file. And, all the events under a
           particular derived perf event group must have the same CPU_OPTION.
           || acts as a separator for different groups inside a single
           derived event. The syntax is :

                  [event:derived]
                  EVENT_NAME_1 [CPU_OPTION] [scale]
                  EVENT_NAME_2 [CPU_OPTION] [scale]
                  ...
                  ||
                  EVENT_NAME_3 [CPU_OPTION] [scale]
                  EVENT_NAME_4 [CPU_OPTION] [scale]
                  ...

                  The available event cpu options are as follows:

                  cpu    to add the counter to all cpus in the system

                  cpu_rr to add to one of the cpus in a round-robin
                         allocation strategy

                  node   to add the counter to the first cpu in each numa
                         node

                  node_rr
                         to add the counter to the cpus in each numa node in
                         a round-robin allocation strategy

                  [N]    where N is the numerical digit of the CPU index

                  if the CPU option is absent then the event is programmed on
                  all cpus.

                  scale is applicable for the counters in derived events. If
                  scale is given, the counters will be scaled to their
                  respective values. The options are as follows :

                  a float value
                         Can be a simple float value, or a value in
                         scientific notation.

                  perf_scale
                         The scale will be taken from the kernel sysfs scale
                         file entry for that event. Its generally specified
                         in
                         /sys/bus/event_source/device/events/<event_name>.scale

                  If no scale is given, the default scale will be taken as
                  1.0.

                  Blank lines are ignored. Lines that begin with the # sign
                  are ignored.

                  Multiple, comma separated, PMUs may be specified in the PMU
                  definition.

## [](#SEE_ALSO)SEE ALSO

           pmdaperfevent(1).

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

    Performance Co-Pilot               PCP                  PERFEVENT.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [pmdaperfevent(1)](../man1/pmdaperfevent.1.html)

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
