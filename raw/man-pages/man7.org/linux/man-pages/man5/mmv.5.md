---
{"title": "mmv(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/mmv.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mmv(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MMV(5)                     File Formats Manual                     MMV(5)

## [](#NAME)NAME

           mmv - Memory Mapped Values for Performance Co-Pilot

## [](#SYNOPSIS)SYNOPSIS

           $PCP_TMP_DIR/mmv/<file>

## [](#DESCRIPTION)DESCRIPTION

           The files in $PCP_TMP_DIR/mmv are generated either by the
           mmv_stats_init(3) and mmv_stats2_init(3) functions from the
           libpcp_mmv library, or by a native language module such as Parfait
           (Java), Speed (Golang) or Hornet (Rust).

           There could be multiple files in this directory, each file
           representing a single source of the performance metrics.  The
           metrics are harvested by pmdammv(1) which exports them to the rest
           of the Performance Co-Pilot infrastructure.

## [](#FILE_FORMAT)FILE FORMAT

           Each file starts with the following header:
                    ┌────────┬────────┬──────────────────────────┐
                    │ Offset │ Length │           Name           │
                    ├────────┼────────┼──────────────────────────┤
                    │    0   │   4    │ tag == "MMV\0"           │
                    ├────────┼────────┼──────────────────────────┤
                    │    4   │   4    │ Version (1 or 2)         │
                    ├────────┼────────┼──────────────────────────┤
                    │    8   │   8    │ Generation 1             │
                    ├────────┼────────┼──────────────────────────┤
                    │   16   │   8    │ Generation 2             │
                    ├────────┼────────┼──────────────────────────┤
                    │   24   │   4    │ Number of TOC entries    │
                    ├────────┼────────┼──────────────────────────┤
                    │   28   │   4    │ Flags                    │
                    ├────────┼────────┼──────────────────────────┤
                    │   32   │   4    │ Process identifier (PID) │
                    ├────────┼────────┼──────────────────────────┤
                    │   36   │   4    │ Cluster identifier       │
                    └────────┴────────┴──────────────────────────┘

           The version number specifies which mapping layout format is in
           use.  There are two, both are very similar, as described below.
           The sole purpose of the MMV version 2 format is to allow the use
           of longer metric and instance names.  If names longer than
           MMV_NAMEMAX are not in use, it is best to use MMV version 1 format
           as this allows older versions of PCP to also consume the data.
           Support for v2 format was added in the pcp-3.11.4 release.

           The generation numbers are timestamps at the time of file
           creation, and must match for the file to be considered by the MMV
           PMDA.

           The flags can specify ways in which the client would like the MMV
           PMDA to behave - e.g. the MMV_FLAG_PROCESS flag specifies that
           only if the process identified by PID is currently running should
           those values be exported.

           Finally, if set, the cluster identifier is a hint to the MMV PMDA
           as to what cluster should be used with this application when
           forming the individual metric identifiers.  A performance metric
           identifier (see PMDA(3)) consists of the PMDA domain number, the
           cluster number, and the individual item numbers described in the
           Metrics section.

           The header is followed by at least 2 TOC sections: one section for
           metrics and another for values.  The TOC section has the following
           format:
           ┌────────┬────────┬─────────────────────────────────────────────┐
           │ Offset │ Length │                    Value                    │
           ├────────┼────────┼─────────────────────────────────────────────┤
           │   0    │   4    │ Section Type (see mmv_stats.h)              │
           ├────────┼────────┼─────────────────────────────────────────────┤
           │   4    │   4    │ Number of entries in the section            │
           ├────────┼────────┼─────────────────────────────────────────────┤
           │   8    │   8    │ Section's offset from the start of the file │
           └────────┴────────┴─────────────────────────────────────────────┘

           The section types are:

                  1: Indoms (instance domain definitions)

                  2: Instances

                  3: Metrics (metric definitions)

                  4: Values

                  5: String

                  6: Labels

           The only mandatory sections are Metrics and Values.  Indoms and
           Instances sections of either version only appear if there are
           metrics with multiple instances.  String sections only appear if
           there are metrics with string values, when Metrics or Indoms are
           defined with help text, or in v2 MMV format where metric names and
           instance names are stored in string sections (providing
           significantly more space than v1 MMV format for these names).
           Label sections only appear if there are metrics annotated with
           labels (name/value pairs).  Labels are supported in v3 MMV format.

           The entries in the Indoms sections have the following format:
              ┌────────┬────────┬───────────────────────────────────────┐
              │ Offset │ Length │                 Value                 │
              ├────────┼────────┼───────────────────────────────────────┤
              │    0   │   4    │ Unique serial number for this domain  │
              ├────────┼────────┼───────────────────────────────────────┤
              │    4   │   4    │ Number of entries in the domain       │
              ├────────┼────────┼───────────────────────────────────────┤
              │    8   │   8    │ Offset to first Instance or Instance2 │
              ├────────┼────────┼───────────────────────────────────────┤
              │   16   │   8    │ Short help text offset                │
              ├────────┼────────┼───────────────────────────────────────┤
              │   24   │   8    │ Long help text offset                 │
              └────────┴────────┴───────────────────────────────────────┘

           The entries in the Instances (v1) section have the following
           format:
                  ┌────────┬────────┬───────────────────────────────┐
                  │ Offset │ Length │             Value             │
                  ├────────┼────────┼───────────────────────────────┤
                  │    0   │    8   │ Offset into the indom section │
                  ├────────┼────────┼───────────────────────────────┤
                  │    8   │    4   │ Unused padding (zero filled)  │
                  ├────────┼────────┼───────────────────────────────┤
                  │   12   │    4   │ Internal instance identifier  │
                  ├────────┼────────┼───────────────────────────────┤
                  │   16   │   64   │ External instance identifier  │
                  └────────┴────────┴───────────────────────────────┘

           The entries in the Instances (v2) section have the following
           format:
           ┌────────┬────────┬────────────────────────────────────────────┐
           │ Offset │ Length │                   Value                    │
           ├────────┼────────┼────────────────────────────────────────────┤
           │    0   │   8    │ Offset into the indom section              │
           ├────────┼────────┼────────────────────────────────────────────┤
           │    8   │   4    │ Unused padding (zero filled)               │
           ├────────┼────────┼────────────────────────────────────────────┤
           │   12   │   4    │ Internal instance identifier               │
           ├────────┼────────┼────────────────────────────────────────────┤
           │   16   │   8    │ External instance identifier string offset │
           └────────┴────────┴────────────────────────────────────────────┘

           The entries in the Metrics (v1) section have the following format:
                  ┌────────┬────────┬───────────────────────────────┐
                  │ Offset │ Length │             Value             │
                  ├────────┼────────┼───────────────────────────────┤
                  │    0   │   64   │ Metric Name                   │
                  ├────────┼────────┼───────────────────────────────┤
                  │   64   │    4   │ Metric Item (see PMDA(3))     │
                  ├────────┼────────┼───────────────────────────────┤
                  │   68   │    4   │ Metric Type (see mmv_stats.h) │
                  ├────────┼────────┼───────────────────────────────┤
                  │   72   │    4   │ Semantics (see PMAPI(3))      │
                  ├────────┼────────┼───────────────────────────────┤
                  │   76   │    4   │ Dimensions (see PMAPI(3))     │
                  ├────────┼────────┼───────────────────────────────┤
                  │   80   │    4   │ Instance Domain ID            │
                  ├────────┼────────┼───────────────────────────────┤
                  │   84   │    4   │ Unused padding (zero filled)  │
                  ├────────┼────────┼───────────────────────────────┤
                  │   88   │    8   │ Short help text offset        │
                  ├────────┼────────┼───────────────────────────────┤
                  │   96   │    8   │ Long help text offset         │
                  └────────┴────────┴───────────────────────────────┘

           The entries in the Metrics (v2) section have the following format:
                  ┌────────┬────────┬───────────────────────────────┐
                  │ Offset │ Length │             Value             │
                  ├────────┼────────┼───────────────────────────────┤
                  │    0   │   8    │ Metric Name string offset     │
                  ├────────┼────────┼───────────────────────────────┤
                  │    8   │   4    │ Metric Item (see PMDA(3))     │
                  ├────────┼────────┼───────────────────────────────┤
                  │   12   │   4    │ Metric Type (see mmv_stats.h) │
                  ├────────┼────────┼───────────────────────────────┤
                  │   16   │   4    │ Semantics (see PMAPI(3))      │
                  ├────────┼────────┼───────────────────────────────┤
                  │   20   │   4    │ Dimensions (see PMAPI(3))     │
                  ├────────┼────────┼───────────────────────────────┤
                  │   24   │   4    │ Instance Domain ID            │
                  ├────────┼────────┼───────────────────────────────┤
                  │   28   │   4    │ Unused padding (zero filled)  │
                  ├────────┼────────┼───────────────────────────────┤
                  │   32   │   8    │ Short help text offset        │
                  ├────────┼────────┼───────────────────────────────┤
                  │   40   │   8    │ Long help text offset         │
                  └────────┴────────┴───────────────────────────────┘

           The entries in the Values section have the following format:
               ┌────────┬────────┬────────────────────────────────────┐
               │ Offset │ Length │               Value                │
               ├────────┼────────┼────────────────────────────────────┤
               │    0   │   8    │ pmAtomValue (see PMAPI(3))         │
               ├────────┼────────┼────────────────────────────────────┤
               │    8   │   8    │ Extra space for STRING and ELAPSED │
               ├────────┼────────┼────────────────────────────────────┤
               │   16   │   8    │ Offset into the Metrics section    │
               ├────────┼────────┼────────────────────────────────────┤
               │   24   │   8    │ Offset into the Instances section  │
               └────────┴────────┴────────────────────────────────────┘

           Each entry in the strings section is a 256 byte character array,
           containing a single NULL-terminated character string.  So each
           string has a maximum length of 256 bytes, which includes the
           terminating NULL.

           The entries in the Labels (v3) section have the following format:
                       ┌────────┬────────┬────────────────────┐
                       │ Offset │ Length │       Value        │
                       ├────────┼────────┼────────────────────┤
                       │    0   │    4   │ Flags - PM_LABEL_  │
                       │        │        │ CLUSTER, ITEM,     │
                       │        │        │ INDOM, INSTANCES   │
                       │        │        │ and OPTIONAL       │
                       ├────────┼────────┼────────────────────┤
                       │    4   │    4   │ Identifier for     │
                       │        │        │ given type (indom, │
                       │        │        │ cluster or item)   │
                       ├────────┼────────┼────────────────────┤
                       │    8   │    4   │ Internal Instance  │
                       │        │        │ or PM_IN_NULL      │
                       ├────────┼────────┼────────────────────┤
                       │   12   │  244   │ Payload (Name and  │
                       │        │        │ Value JSONB        │
                       │        │        │ String)            │
                       └────────┴────────┴────────────────────┘

           Each entry in the payload is a 244 byte (maximum) character array,
           containing a single NULL-terminated name:value pair in JSON
           format.  Insignificant whitespace must not be present.  Label
           names consist only of alphanumeric characters or underscores, and
           must begin with an alphabetic.  Upper and lower case characters
           are considered distinct.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmdammv(1), PMAPI(3), PMDA(3), mmv_stats_registry(3),
           pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot                                               MMV(5)

------------------------------------------------------------------------

Pages that refer to this page: [pmdammv(1)](../man1/pmdammv.1.html),  [mmv_inc_value(3)](../man3/mmv_inc_value.3.html),  [mmv_lookup_value_desc(3)](../man3/mmv_lookup_value_desc.3.html),  [mmv_set_value(3)](../man3/mmv_set_value.3.html),  [mmv_stats_init(3)](../man3/mmv_stats_init.3.html),  [mmv_stats_registry(3)](../man3/mmv_stats_registry.3.html)

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
