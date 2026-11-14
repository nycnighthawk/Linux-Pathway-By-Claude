---
{"title": "LOGARCHIVE(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/LOGARCHIVE.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# LOGARCHIVE(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [COMMON FEATURES](#COMMON_FEATURES) \| [ARCHIVE VOLUME (.0, .1, \...) RECORDS](#ARCHIVE_VOLUME_(.0,_.1,_...)_RECORDS) \| [METADATA FILE (.meta) RECORDS](#METADATA_FILE_(.meta)_RECORDS) \| [INDEX FILE (.index) RECORDS](#INDEX_FILE_(.index)_RECORDS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LOGARCHIVE(5)              File Formats Manual              LOGARCHIVE(5)

## [](#NAME)NAME

           LOGARCHIVE - Performance Co-Pilot archive formats

## [](#DESCRIPTION)DESCRIPTION

           Performance Co-Pilot (PCP) archives store historical values about
           arbitrary metrics recorded from a single host.  Archives are
           machine independent and self-contained - all metric data and
           metadata required for off-line or off-site analysis is held within
           an archive.

           The format is stable in order to allow long-term historical
           storage and processing by PMAPI(3) client tools.  However some
           format variants are supported over time, and currently Versions 2
           and 3 are supported.  The mandate is that PCP will provide long-
           term backwards compatibility, so an archive created on any version
           of PCP can be read on that version of PCP and all subsequent
           versions of PCP.  The exception is Version 1 that was retired in
           the PCP Version 2.0 release in May 1998.

           Archives may be read by most PCP client tools, using the
           -a/--archive NAME option, or dumped raw by pmlogdump(1).  Archives
           are created primarily by pmlogger(1), however they can also be
           created using the LOGIMPORT(3) programming interface.

           Archives may be merged, analyzed, modified and subsampled using
           pmlogreduce(1), pmlogsummary(1), pmlogrewrite(1) and
           pmlogextract(1).  In addition, PCP archives may be examined in
           sets or grouped together into ``archive folios'', which are
           created and managed by the mkaf(1) and pmafm(1) tools.

           An archive consists of several physical files that share a common
           arbitrary prefix, e.g.  myarchive.

           myarchive.0, myarchive.1, ...
                  One or more data volumes containing the metric values and
                  any error codes encountered during metric sampling.
                  Typically the largest of the files and may grow very
                  rapidly, depending on the selection of metrics to be logged
                  by pmlogger(1) and the sampling intervals being used.

           myarchive.meta
                  Information for PMAPI functions such as pmLookupName(3),
                  pmLookupDesc(3), pmLookupLabels(3) and pmLookupInDom(3).
                  The metadata file may grow sporadically as logged metrics,
                  instance domains and labels vary over time.

           myarchive.index
                  A temporal index, mapping timestamps to byte offsets in the
                  other files.

## [](#COMMON_FEATURES)COMMON FEATURES

           All three types of files have a similar record-based structure, a
           convention of network byte-order (big-endian) encoding, and 32-bit
           fields for tagging/padding for those records.  Strings are stored
           as 8-bit characters without assuming a specific encoding, so
           normally ASCII.  See also the __pmLog* types in
           src/include/pcp/libpcp.h.

       RECORD FRAMING
           The volume and .meta files are divided into self-identifying
           records.
           ┌────────┬────────┬──────────────────────────────────────────────┐
           │ Offset │ Length │                     Name                     │
           ├────────┼────────┼──────────────────────────────────────────────┤
           │      0 │      4 │ N, length of record, in bytes, including     │
           │        │        │ this field                                   │
           │      4 │    N-8 │ record payload, usually starting with a      │
           │        │        │ 32-bit record type tag                       │
           │    N-4 │      4 │ N, length of record (again)                  │
           └────────┴────────┴──────────────────────────────────────────────┘

       ARCHIVE LABEL
           All three types of files begin with an ``archive label'' header,
           which identifies the host name, starting timestamp and timezone
           information; all referring to the host that was the source of the
           performance data (which may be different to the host where
           pmlogger(1) was running).

           The ``archive label'' format differs between Version 2 and Version
           3, with the latter providing enhanced timestamps (64-bit encoding
           of the seconds part and nanosecond precision) and some additional
           fields.

           ┌────────────────────────────────────────────────────────────────┐
           │                           Version 2                            │
           ├────────┬────────┬──────────────────────────────────────────────┤
           │ Offset │ Length │                     Name                     │
           ├────────┼────────┼──────────────────────────────────────────────┤
           │      0 │      4 │ tag, PM_LOG_MAGIC | PM_LOG_VERS02=0x50052602 │
           │      4 │      4 │ process id (PID) of pmlogger process that    │
           │        │        │ wrote file                                   │
           │      8 │      4 │ archive start time, seconds part (past UNIX  │
           │        │        │ epoch)                                       │
           │     12 │      4 │ archive start time, microseconds part        │
           │     16 │      4 │ current archive volume number (or -1=.meta,  │
           │        │        │ -2=.index)                                   │
           │     20 │     64 │ name of collection host                      │
           │     80 │     40 │ time zone string for collection host ($TZ    │
           │        │        │ environment variable)                        │
           └────────┴────────┴──────────────────────────────────────────────┘

           ┌────────────────────────────────────────────────────────────────┐
           │                           Version 3                            │
           ├────────┬────────┬──────────────────────────────────────────────┤
           │ Offset │ Length │                     Name                     │
           ├────────┼────────┼──────────────────────────────────────────────┤
           │      0 │      4 │ tag, PM_LOG_MAGIC | PM_LOG_VERS03=0x50052603 │
           │      4 │      4 │ PID of pmlogger process that wrote file      │
           │      8 │      8 │ archive start time, seconds part (past UNIX  │
           │        │        │ epoch)                                       │
           │     16 │      4 │ archive start time, nanoseconds part         │
           │     20 │      4 │ current archive volume number (or -1=.meta,  │
           │        │        │ -2=.index)                                   │
           │     24 │      4 │ archive feature bits                         │
           │     28 │      4 │ reserved for future use                      │
           │     32 │    256 │ name of collection host                      │
           │    288 │    256 │ timezone string for collection host ($TZ     │
           │        │        │ environment variable), e.g. AEDT-11          │
           │    544 │    256 │ timezone zoneinfo string for collection      │
           │        │        │ host, e.g. :Australia/Melbourne              │
           └────────┴────────┴──────────────────────────────────────────────┘

           The ``archive feature bits'' are intended to encode possible
           future extensions or differences to the on-disk structure or the
           the archive semantics.  At this stage there are no such features,
           but if they are introduced at some point in the future, there will
           be associated PM_LOG_FEATURE_XXX macros added to the <pcp/pmapi.h>
           header file.

           All fields, except for the ``current archive volume number'',
           match for all files in a single PCP archive.

## [](#ARCHIVE_VOLUME_(.0,_.1,_...)_RECORDS)ARCHIVE VOLUME (.0, .1, \...) RECORDS

       pmResult
           After the archive label record, an archive volume file contains
           one or more records, each providing metric values corresponding to
           the pmResult from one pmFetch(3) operation.  The record size may
           vary according to number of metrics being fetched and the number
           of instances in the associated instance domains.

           For Version 2 the file size is limited to 2GiB, due to storage of
           32-bit byte offsets within the temporal index.  For Version 3 the
           file size is limited to 8191PiB, due to storage of 62-bit byte
           offsets within the temporal index.

           The pmResult format differs between Version 2 and Version 3, with
           the latter providing enhanced timestamps (64-bit encoding of the
           seconds part and nanosecond precision).

           ┌──────────────────────────────────────────────────────────────┐
           │                          Version 2                           │
           ├─────────┬────────┬───────────────────────────────────────────┤
           │ Offset  │ Length │                   Name                    │
           ├─────────┼────────┼───────────────────────────────────────────┤
           │       0 │      4 │ timestamp, seconds part (past UNIX epoch) │
           │       4 │      4 │ timestamp, microseconds part              │
           │       8 │      4 │ number of metrics with data following     │
           │      12 │      M │ pmValueSet #0                             │
           │    12+M │      N │ pmValueSet #1                             │
           │  12+M+N │    ... │ ...                                       │
           │     NOP │      X │ pmValueBlock #0                           │
           │   NOP+X │      Y │ pmValueBlock #1                           │
           │ NOP+X+Y │    ... │ ...                                       │
           └─────────┴────────┴───────────────────────────────────────────┘

           ┌──────────────────────────────────────────────────────────────┐
           │                          Version 3                           │
           ├─────────┬────────┬───────────────────────────────────────────┤
           │ Offset  │ Length │                   Name                    │
           ├─────────┼────────┼───────────────────────────────────────────┤
           │       0 │      8 │ timestamp, seconds part (past UNIX epoch) │
           │       8 │      4 │ timestamp, nanoseconds part               │
           │      12 │      4 │ number of metrics with data following     │
           │      16 │      M │ pmValueSet #0                             │
           │    16+M │      N │ pmValueSet #1                             │
           │  16+M+N │    ... │ ...                                       │
           │     NOP │      X │ pmValueBlock #0                           │
           │   NOP+X │      Y │ pmValueBlock #1                           │
           │ NOP+X+Y │    ... │ ...                                       │
           └─────────┴────────┴───────────────────────────────────────────┘

           Records with a ``number of metrics'' equal to zero are ``mark
           records'', and represent interruptions, missing data, or time
           discontinuities in logging.

       pmValueSet
           This subrecord represents the values for one metric at one point
           in time.
          ┌────────┬────────┬────────────────────────────────────────────────┐
          │ Offset │ Length │                      Name                      │
          ├────────┼────────┼────────────────────────────────────────────────┤
          │      0 │      4 │ Performance Metrics Identifier (PMID)          │
          │      4 │      4 │ number of values                               │
          │      8 │      4 │ value format, PM_VAL_INSITU=0 or PM_VAL_DPTR=1 │
          │     12 │      M │ pmValue #0                                     │
          │   12+M │      N │ pmValue #1                                     │
          │ 12+M+N │    ... │ ...                                            │
          └────────┴────────┴────────────────────────────────────────────────┘

           The metadata describing metrics is found in the .meta file where
           the entries are not timestamped, as the metadata is assumed to be
           unchanging throughout an archive.

       pmValue
           This subrecord represents one value for one instance of a metric
           at one point in time.  It is a variant type, depending on the
           parent pmValueSet's value format field.  This allows small numbers
           to be encoded compactly, but retain flexibility for larger or
           variable length data to be stored later in the pmResult record in
           a pmValueBlock subrecord.
           ┌────────┬────────┬───────────────────────────────────────────────┐
           │ Offset │ Length │                     Name                      │
           ├────────┼────────┼───────────────────────────────────────────────┤
           │      0 │      4 │ internal instance identifier (or              │
           │        │        │ PM_IN_NULL=-1 for singular metrics)           │
           │      4 │      4 │ value (INSITU) or                             │
           │        │        │ offset in pmResult to our pmValueBlock (DPTR) │
           └────────┴────────┴───────────────────────────────────────────────┘

           The metadata describing the instance domain for metrics is found
           in the .meta file.  Since the numeric mappings may change during
           the lifetime of the logging session, it is important to match up
           the timestamp of the measurement record with the corresponding
           instance domain record.  That is, the instance domain
           corresponding to a measurement at time T is the instance domain
           observation for the metric's instance domain with largest
           timestamp T' <= T.

       pmValueBlock
           Instances of this subrecord are placed at the end of the
           pmValueSet, after all the pmValue subrecords.  If (and only if)
           needed, they are padded at the end to the next 32-bit boundary.
          ┌────────┬────────┬────────────────────────────────────────────────┐
          │ Offset │ Length │                      Name                      │
          ├────────┼────────┼────────────────────────────────────────────────┤
          │      0 │      1 │ value type (same as pmDesc.type)               │
          │      1 │      3 │ 4 + N, the length of the subrecord             │
          │      4 │      N │ bytes that make up the raw value               │
          │    4+N │    0-3 │ padding (not included in the 4+N length field) │
          └────────┴────────┴────────────────────────────────────────────────┘

           Note that for PM_TYPE_STRING, the length includes an explicit NULL
           terminator byte.  For PM_TYPE_EVENT, the value byte string is
           further structured.  Refer to PMDAEVENTARRAY(3) for more
           information about how arrays of event records are packed inside a
           pmResult container.

## [](#METADATA_FILE_(.meta)_RECORDS)METADATA FILE (.meta) RECORDS

           After the archive label record, the metadata file contains
           interleaved metric description records, timestamped instance
           domain records, timestamped label records (for context, instance
           domain and metric labels) and (help) text records.  Unlike the
           data volumes, these records are not forced to 32-bit alignment.

           For Version 2 the file size is limited to 2GiB, due to storage of
           32-bit byte offsets within the temporal index.  For Version 3 the
           file size is limited to 8191PiB, due to storage of 62-bit byte
           offsets within the temporal index.

           See also libpcp/src/logmeta.c.

       Metric Descriptions
           Instances of this (pmDesc) record provide the description or
           metadata for each metric appearing in the PCP archive.  This
           metadata includes the metric's PMID, data type, data semantics,
           instance domain identifier (or PM_INDOM_NULL for singular metrics
           with only one value) and a set of (1 or more) names.
           ┌────────┬────────┬──────────────────────────────────────────────┐
           │ Offset │ Length │                     Name                     │
           ├────────┼────────┼──────────────────────────────────────────────┤
           │      0 │      4 │ tag, TYPE_DESC=1                             │
           │      4 │      4 │ PMID                                         │
           │      8 │      4 │ data type (PM_TYPE_*)                        │
           │     12 │      4 │ instance domain identifier                   │
           │     16 │      4 │ metric semantics (PM_SEM_*)                  │
           │     20 │      4 │ units: bit-packed pmUnits                    │
           │      4 │      4 │ number of alternative names for this PMID    │
           │     28 │      4 │ N: number of bytes in this name              │
           │     32 │      N │ bytes of the name, no NULL terminator nor    │
           │        │        │ padding                                      │
           │   32+N │      4 │ N2: number of bytes in next name             │
           │   36+N │     N2 │ bytes of the name, no NULL terminator nor    │
           │        │        │ padding                                      │
           │    ... │    ... │ ...                                          │
           └────────┴────────┴──────────────────────────────────────────────┘

       Instance Domains
           A set-valued metric is defined over an instance domain, which
           consists of an instance domain identifier (will have already been
           mentioned in a prior pmDesc record), a count of the number of
           instances and a map that defines the association between internal
           instance identifiers (integers) and external instance names
           (strings).

           Because instance domains can change over time, the instance domain
           also requires a timestamp, and the same instance domain can occur
           multiple times within the .meta file.  The timestamps are used to
           search for the temporally correct instance domain when decoding
           pmResult records from the archive data volumes, or answering
           metadata queries against the instance domain.

           The instance domain format differs markedly between Version 2 and
           Version 3.  Version 3 provides enhanced timestamps (64-bit
           encoding of the seconds part and nanosecond precision) and
           introduces a new ``delta'' instance domain format that encodes
           differences between the previous observation of the instance
           domain and the current state of the instance domain.

         ┌───────────────────────────────────────────────────────────────────┐
         │                 Full Instance Domain - Version 2                  │
         ├──────────┬────────┬───────────────────────────────────────────────┤
         │  Offset  │ Length │                     Name                      │
         ├──────────┼────────┼───────────────────────────────────────────────┤
         │        0 │      4 │ tag, TYPE_INDOM_V2=2                          │
         │        4 │      4 │ timestamp, seconds part (past UNIX epoch)     │
         │        8 │      4 │ timestamp, microseconds part                  │
         │       12 │      4 │ instance domain number                        │
         │       16 │      4 │ N: number of instances in domain, normally >0 │
         │       20 │      4 │ first instance number                         │
         │       24 │      4 │ second instance number (if appropriate)       │
         │      ... │    ... │ ...                                           │
         │   20+4*N │      4 │ first offset into string table (see below)    │
         │ 20+4*N+4 │      4 │ second offset into string table (etc.)        │
         │      ... │    ... │ ...                                           │
         │   20+8*N │      M │ base of string table, containing              │
         │          │        │ packed, NULL-terminated instance names        │
         └──────────┴────────┴───────────────────────────────────────────────┘

         ┌───────────────────────────────────────────────────────────────────┐
         │                 Full Instance Domain - Version 3                  │
         ├──────────┬────────┬───────────────────────────────────────────────┤
         │  Offset  │ Length │                     Name                      │
         ├──────────┼────────┼───────────────────────────────────────────────┤
         │        0 │      4 │ tag, TYPE_INDOM=5                             │
         │        4 │      8 │ timestamp, seconds part (past UNIX epoch)     │
         │       12 │      4 │ timestamp, nanoseconds part                   │
         │       16 │      4 │ instance domain number                        │
         │       20 │      4 │ N: number of instances in domain, normally >0 │
         │       24 │      4 │ first instance number                         │
         │       28 │      4 │ second instance number (if appropriate)       │
         │      ... │    ... │ ...                                           │
         │   24+4*N │      4 │ first offset into string table (see below)    │
         │ 24+4*N+4 │      4 │ second offset into string table (etc.)        │
         │      ... │    ... │ ...                                           │
         │   24+8*N │      M │ base of string table, containing              │
         │          │        │ packed, NULL-terminated instance names        │
         └──────────┴────────┴───────────────────────────────────────────────┘

           The ``delta'' instance domain record in Version 3 uses the same
           physical structure as the ``full'' instance domain above with the
           following differences:
           *  The tag is TYPE_INDOM_DELTA=6.
           *  The ``number of instances in domain'' field becomes the sum of
              the number of instances added and the number of instances
              deleted.
           *  Deleted instances are encoded with the string offset set to -1
              and there is no corresponding string table entry.
           *  Added instances are encoded exactly the same way.

           The ``delta'' instance domain format is used to provide a more
           compact on-disk encoding for instance domains that have a large
           number of instances and are subject to frequent small changes,
           e.g. the instance domain of process ids, as exported by
           pmdaproc(1).

           For ``full'' instance domain records the instance domain replace
           the previous instance domain: prior records are not searched for
           instance domain metadata queries after this timestamp.

           Each instance domain in a Version 3 archive must have an initial
           ``full'' instance domain record.  Subsequent records for the same
           instance domain can be the `full'' or the ``delta'' variant.  Any
           instance mentioned in the prior observation of an instance domain
           that is not mentioned in the ``delta'' instance domain record is
           assumed to continue to exist for the current observation of the
           instance domain.

       Labels for Contexts, Instance Domains and Metrics
           Instances of this (pmLogLabelSet) record provide sets of label-
           name:label-value pairs associated with labels of the context,
           instance domains and individual performance metrics - refer to
           pmLookupLabels(3) for further details.

           Any instance domain identifier will have already been mentioned in
           a prior pmDesc record.

           As new labels can appear during an archiving session, these
           records are timestamped and must be searched when decoding
           pmResult records from the archive data volumes.  The pmLogLabelSet
           format differs between Version 2 and Version 3, with the latter
           providing enhanced timestamps (64-bit encoding of the seconds part
           and nanosecond precision).

           ┌────────────────────────────────────────────────────────────────┐
           │                           Version 2                            │
           ├──────────────────────────────────┬────────┬────────────────────┤
           │              Offset              │ Length │        Name        │
           ├──────────────────────────────────┼────────┼────────────────────┤
           │                                0 │      4 │ tag,               │
           │                                  │        │ TYPE_LABEL_V2=3    │
           │                                4 │      4 │ timestamp, seconds │
           │                                  │        │ part (past UNIX    │
           │                                  │        │ epoch)             │
           │                                8 │      4 │ timestamp,         │
           │                                  │        │ microseconds part  │
           │                               12 │      4 │ label type         │
           │                                  │        │ (PM_LABEL_* type   │
           │                                  │        │ macros.)           │
           │                               16 │      4 │ numeric identifier │
           │                                  │        │ - domain, PMID,    │
           │                                  │        │ etc or             │
           │                                  │        │ PM_IN_NULL=-1 for  │
           │                                  │        │ context labels     │
           │                               20 │      4 │ N: number of label │
           │                                  │        │ sets in this       │
           │                                  │        │ record, usually 1  │
           │                                  │        │ except in the case │
           │                                  │        │ of instances       │
           │                               24 │      4 │ offset to the      │
           │                                  │        │ start of the JSONB │
           │                                  │        │ labels string      │
           │                               28 │     L1 │ first T{           │
           │ labelset array entry (see below) │        │                    │
           │                               T} │        │                    │
           │                              ... │    ... │ ...                │
           │                            28+L1 │     LN │ N-th T{            │
           │ labelset array entry (see below) │        │                    │
           │                               T} │        │                    │
           │                              ... │    ... │ ...                │
           │                      28+L1+...LN │      M │ concatenated JSONB │
           │                                  │        │ strings for all    │
           │                                  │        │ labelsets          │
           └──────────────────────────────────┴────────┴────────────────────┘

           ┌────────────────────────────────────────────────────────────────┐
           │                           Version 3                            │
           ├─────────────┬────────┬─────────────────────────────────────────┤
           │   Offset    │ Length │                  Name                   │
           ├─────────────┼────────┼─────────────────────────────────────────┤
           │           0 │      4 │ tag, TYPE_LABEL=7                       │
           │           4 │      8 │ timestamp, seconds part (past UNIX      │
           │             │        │ epoch)                                  │
           │          12 │      4 │ timestamp, nanoseconds part             │
           │          16 │      4 │ label type (PM_LABEL_* type macros.)    │
           │          20 │      4 │ numeric identifier - domain, PMID, etc  │
           │             │        │ or PM_IN_NULL=-1 for context labels     │
           │          24 │      4 │ N: number of label sets in this record, │
           │             │        │ usually 1 except in the case of         │
           │             │        │ instances                               │
           │          28 │      4 │ offset to the start of the JSONB labels │
           │             │        │ string                                  │
           │          32 │     L1 │ first labelset array entry (see below)  │
           │         ... │    ... │ ...                                     │
           │       32+L1 │     LN │ N-th labelset array entry (see below)   │
           │         ... │    ... │ ...                                     │
           │ 32+L1+...LN │      M │ concatenated JSONB strings for all      │
           │             │        │ labelsets                               │
           └─────────────┴────────┴─────────────────────────────────────────┘

           Records of this form replace the existing labels for a given label
           type: prior records are not searched for resolving that class of
           label in measurements after this timestamp.

           The individual labelset array entries are variable length,
           depending on the number of labels present within that set.  These
           entries contain the instance identifiers (in the case of type
           PM_LABEL_INSTANCES labels), lengths and offsets of each label name
           and value, and also any flags set for each label.
            ┌────────┬────────┬───────────────────────────────────────────┐
            │ Offset │ Length │                   Name                    │
            ├────────┼────────┼───────────────────────────────────────────┤
            │      0 │      4 │ instance identifier (or PM_IN_NULL=-1)    │
            │      4 │      4 │ length of JSONB label string              │
            │      8 │      4 │ N: number of labels in this labelset      │
            │     12 │      2 │ first label name offset                   │
            │     14 │      1 │ first label name length                   │
            │     15 │      1 │ first label flags (e.g. optionality)      │
            │     16 │      2 │ first label value offset                  │
            │     18 │      2 │ first label value length                  │
            │     20 │      2 │ second label name offset (if appropriate) │
            │    ... │    ... │ ...                                       │
            └────────┴────────┴───────────────────────────────────────────┘

       Help Text
           This (pmLogText) record stores help text associated with a metric
           or an instance domain - as provided by pmLookupText(3) and
           pmLookupInDomText(3).

           The metric identifier and instance domain identifier will have
           already been mentioned in a prior pmDesc record.

           ┌────────┬────────┬──────────────────────────────────────────────┐
           │ Offset │ Length │                     Name                     │
           ├────────┼────────┼──────────────────────────────────────────────┤
           │      0 │      4 │ tag, TYPE_TEXT=4                             │
           │      4 │      4 │ text and identifier type (PM_TEXT_* macros.) │
           │      8 │      4 │ numeric identifier - PMID or instance domain │
           │     12 │      M │ help text string, arbitrary text             │
           └────────┴────────┴──────────────────────────────────────────────┘

## [](#INDEX_FILE_(.index)_RECORDS)INDEX FILE (.index) RECORDS

           After the archive label record, the temporal index file contains a
           plainly concatenated, unframed group of tuples, which relate
           timestamps to the byte offsets in the volume and .meta files.
           These records are fixed size, fixed format, and are not enclosed
           in the standard length/payload/length wrapper: they take up the
           entire remainder of the .index file after the archive label
           record.

           The temporal index file provides a rapid way of seeking to a
           particular point of time within an archive for both the
           performance metric values and the associated metadata.

           See also libpcp/src/logutil.c.

           The index format differs between Version 2 and Version 3, with the
           latter providing enhanced timestamps (64-bit encoding of the
           seconds part and nanosecond precision) and 64-bit byte offsets.

            ┌─────────────────────────────────────────────────────────────┐
            │                          Version 2                          │
            ├────────┬────────┬───────────────────────────────────────────┤
            │ Offset │ Length │                   Name                    │
            ├────────┼────────┼───────────────────────────────────────────┤
            │      0 │      4 │ timestamp, seconds part (past UNIX epoch) │
            │      4 │      4 │ timestamp, microseconds part              │
            │      8 │      4 │ archive volume number (0...N)             │
            │     12 │      4 │ byte offset in .meta file                 │
            │     16 │      4 │ byte offset in archive volume file        │
            └────────┴────────┴───────────────────────────────────────────┘

            ┌─────────────────────────────────────────────────────────────┐
            │                          Version 3                          │
            ├────────┬────────┬───────────────────────────────────────────┤
            │ Offset │ Length │                   Name                    │
            ├────────┼────────┼───────────────────────────────────────────┤
            │      0 │      8 │ timestamp, seconds part (past UNIX epoch) │
            │      8 │      4 │ timestamp, nanoseconds part               │
            │     12 │      4 │ archive volume number (0...N)             │
            │     16 │      8 │ byte offset in .meta file                 │
            │     24 │      8 │ byte offset in archive volume file        │
            └────────┴────────┴───────────────────────────────────────────┘

           Since the temporal index is optional, and exists only to speed up
           time-based random access to metrics and their metadata, the index
           records are emitted only intermittently.  An archive reader
           program should not presume any particular rate of data flow into
           the index.  However, common events that may trigger a new temporal
           index record include changes in instance domains, switching over
           to a new archive volume, and starting or stopping logging.  One
           reliable invariant however is that, for each index entry, there
           are to be no meta or archive volume records with a timestamp after
           that in the index, but physically before the associated byte
           offset in the index.

## [](#FILES)FILES

           Several PCP tools create archives in standard locations:

           $HOME/.pcp/pmlogger
                  default location for the interactive chart recording mode
                  in pmchart(1)
           $PCP_LOG_DIR/pmlogger
                  default location for pmlogger_daily(1) and
                  pmlogger_check(1) scripts

## [](#SEE_ALSO)SEE ALSO

           mkaf(1), PCPIntro(1), pmafm(1), pmchart(1), pmdaproc(1),
           pmlogdump(1), pmlogger(1), pmlogger_check(1), pmlogger_daily(1),
           pmlogreduce(1), pmlogrewrite(1), pmlogsummary(1), LOGIMPORT(3),
           PMAPI(3), pmLookupDesc(3), pmLookupInDom(3), pmLookupInDomText(3),
           pmLookupLabels(3), pmLookupName(3), pmLookupText(3), pcp.conf(5)
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

    Performance Co-Pilot                                        LOGARCHIVE(5)

------------------------------------------------------------------------

Pages that refer to this page: [guidellm2pcp(1)](../man1/guidellm2pcp.1.html),  [pcp2arrow(1)](../man1/pcp2arrow.1.html),  [pcp2elasticsearch(1)](../man1/pcp2elasticsearch.1.html),  [pcp2graphite(1)](../man1/pcp2graphite.1.html),  [pcp2influxdb(1)](../man1/pcp2influxdb.1.html),  [pcp2json(1)](../man1/pcp2json.1.html),  [pcp2openmetrics(1)](../man1/pcp2openmetrics.1.html),  [pcp2opentelemetry(1)](../man1/pcp2opentelemetry.1.html),  [pcp2spark(1)](../man1/pcp2spark.1.html),  [pcp2template(1)](../man1/pcp2template.1.html),  [pcp2xlsx(1)](../man1/pcp2xlsx.1.html),  [pcp2xml(1)](../man1/pcp2xml.1.html),  [pcp2zabbix(1)](../man1/pcp2zabbix.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pmlogbasename(1)](../man1/pmlogbasename.1.html),  [pmlogcompress(1)](../man1/pmlogcompress.1.html),  [pmlogger(1)](../man1/pmlogger.1.html),  [pmlogmv(1)](../man1/pmlogmv.1.html),  [pmlogrewrite(1)](../man1/pmlogrewrite.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [vllmbench2pcp(1)](../man1/vllmbench2pcp.1.html),  [pmgetarchivelabel(3)](../man3/pmgetarchivelabel.3.html),  [pmwebapi(3)](../man3/pmwebapi.3.html)

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
