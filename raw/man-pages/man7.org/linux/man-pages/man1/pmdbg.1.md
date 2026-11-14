---
{"title": "pmdbg(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmdbg.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmdbg(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [COMPATIBILITY](#COMPATIBILITY) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMDBG(1)                 General Commands Manual                 PMDBG(1)

## [](#NAME)NAME

           pmdbg - report Performance Co-Pilot debug options

## [](#SYNOPSIS)SYNOPSIS

           pmdbg [-l]

## [](#DESCRIPTION)DESCRIPTION

           The components of the Performance Co-Pilot (PCP) use a global
           mechanism to control diagnostic and debug output.

           pmdbg prints out all the available debug options with the name of
           the option and some descriptive text.

           The -l option does nothing, but is included for backwards
           compatibility with older versions of pmdbg.

           Most applications using the facilities of the PCP support a -D
           name[,name ...]  command-line syntax to enable debug control using
           the name(s) of the desired debug options.

           Alternatively the initial value of the debug control flags may be
           set to a comma-separated list if option name(s) using the
           environment variable $PCP_DEBUG, provided the applications use
           pmGetOptions(3) to process command line options and arguments.  If
           both mechanisms are used the effect is additive, so the resultant
           flags are those set via $PCP_DEBUG combined with those set via any
           -D command line options.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#COMPATIBILITY)COMPATIBILITY

           Prior to PCP 7.0 debug options were maintained in a dual state
           with an old-style binary encoded integer (plus macro name for
           programmers), and a new-style character string name for each debug
           option.

           In PCP 7.0 support for the the old-style was dropped.

           The table below documents the equivalence for those debugging
           options that appeared in both the the old and the new styles.
           ┌─────────────────────────────────────────────────┬─────────────┐
           │                    Old Style                    │  New Style  │
           ├───────────────────────┬────────────┬────────────┼─────────────┤
           │ Symbolic Name         │       Mask │      Value │ Name        │
           ├───────────────────────┼────────────┼────────────┼─────────────┤
           │ DBG_TRACE_PDU         │ 0x00000001 │          1 │ pdu         │
           │ DBG_TRACE_FETCH       │ 0x00000002 │          2 │ fetch       │
           │ DBG_TRACE_PROFILE     │ 0x00000004 │          4 │ profile     │
           │ DBG_TRACE_VALUE       │ 0x00000008 │          8 │ value       │
           │ DBG_TRACE_CONTEXT     │ 0x00000010 │         16 │ context     │
           │ DBG_TRACE_INDOM       │ 0x00000020 │         32 │ indom       │
           │ DBG_TRACE_PDUBUF      │ 0x00000040 │         64 │ pdubuf      │
           │ DBG_TRACE_LOG         │ 0x00000080 │        128 │ log         │
           │ DBG_TRACE_LOGMETA     │ 0x00000100 │        256 │ logmeta     │
           │ DBG_TRACE_OPTFETCH    │ 0x00000200 │        512 │ optfetch    │
           │ DBG_TRACE_AF          │ 0x00000400 │       1024 │ af          │
           │ DBG_TRACE_APPL0       │ 0x00000800 │       2048 │ appl0       │
           │ DBG_TRACE_APPL1       │ 0x00001000 │       4096 │ appl1       │
           │ DBG_TRACE_APPL2       │ 0x00002000 │       8192 │ appl2       │
           │ DBG_TRACE_PMNS        │ 0x00004000 │      16384 │ pmns        │
           │ DBG_TRACE_LIBPMDA     │ 0x00008000 │      32768 │ libpmda     │
           │ DBG_TRACE_TIMECONTROL │ 0x00001000 │      65536 │ timecontrol │
           │ DBG_TRACE_PMC         │ 0x00002000 │     131072 │ pmc         │
           │ DBG_TRACE_DERIVE      │ 0x00004000 │     262144 │ derive      │
           │ DBG_TRACE_LOCK        │ 0x00008000 │     524288 │ lock        │
           │ DBG_TRACE_INTERP      │ 0x00010000 │    1048576 │ interp      │
           │ DBG_TRACE_CONFIG      │ 0x00020000 │    2097152 │ config      │
           │ DBG_TRACE_PMAPI       │ 0x00040000 │    4194304 │ pmapi       │
           │ DBG_TRACE_FAULT       │ 0x00080000 │    8388608 │ fault       │
           │ DBG_TRACE_AUTH        │ 0x00100000 │   16777216 │ auth        │
           │ DBG_TRACE_DISCOVERY   │ 0x00200000 │   33554432 │ discovery   │
           │ DBG_TRACE_ATTR        │ 0x00400000 │   67108864 │ attr        │
           │ DBG_TRACE_HTTP        │ 0x00800000 │  134217728 │ http        │
           │ DBG_TRACE_DESPERATE   │ 0x04000000 │ 1073741824 │ desperate   │
           └───────────────────────┴────────────┴────────────┴─────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), PMAPI(3), pmClearDebug(3), pmGetDebug(3),
           pmGetOptions(3), pmSetDebug(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                           PMDBG(1)

------------------------------------------------------------------------

Pages that refer to this page: [chkhelp(1)](../man1/chkhelp.1.html),  [collectl2pcp(1)](../man1/collectl2pcp.1.html),  [dbpmda(1)](../man1/dbpmda.1.html),  [ganglia2pcp(1)](../man1/ganglia2pcp.1.html),  [newhelp(1)](../man1/newhelp.1.html),  [pcp(1)](../man1/pcp.1.html),  [pcp2arrow(1)](../man1/pcp2arrow.1.html),  [pcp2elasticsearch(1)](../man1/pcp2elasticsearch.1.html),  [pcp2graphite(1)](../man1/pcp2graphite.1.html),  [pcp2influxdb(1)](../man1/pcp2influxdb.1.html),  [pcp2json(1)](../man1/pcp2json.1.html),  [pcp2openmetrics(1)](../man1/pcp2openmetrics.1.html),  [pcp2opentelemetry(1)](../man1/pcp2opentelemetry.1.html),  [pcp2spark(1)](../man1/pcp2spark.1.html),  [pcp2template(1)](../man1/pcp2template.1.html),  [pcp2xml(1)](../man1/pcp2xml.1.html),  [pcp2zabbix(1)](../man1/pcp2zabbix.1.html),  [pcp-atop(1)](../man1/pcp-atop.1.html),  [pcp-atopsar(1)](../man1/pcp-atopsar.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pcp-iostat(1)](../man1/pcp-iostat.1.html),  [pcp-tapestat(1)](../man1/pcp-tapestat.1.html),  [pcp-verify(1)](../man1/pcp-verify.1.html),  [pmcd(1)](../man1/pmcd.1.html),  [pmcd_wait(1)](../man1/pmcd_wait.1.html),  [pmchart(1)](../man1/pmchart.1.html),  [pmclient(1)](../man1/pmclient.1.html),  [pmdaamdgpu(1)](../man1/pmdaamdgpu.1.html),  [pmdaapache(1)](../man1/pmdaapache.1.html),  [pmdabash(1)](../man1/pmdabash.1.html),  [pmdabpf(1)](../man1/pmdabpf.1.html),  [pmdabtrfs(1)](../man1/pmdabtrfs.1.html),  [pmdacifs(1)](../man1/pmdacifs.1.html),  [pmdacisco(1)](../man1/pmdacisco.1.html),  [pmdadarwin(1)](../man1/pmdadarwin.1.html),  [pmdadenki(1)](../man1/pmdadenki.1.html),  [pmdadm(1)](../man1/pmdadm.1.html),  [pmdadocker(1)](../man1/pmdadocker.1.html),  [pmdafarm(1)](../man1/pmdafarm.1.html),  [pmdagfs2(1)](../man1/pmdagfs2.1.html),  [pmdahacluster(1)](../man1/pmdahacluster.1.html),  [pmdaib(1)](../man1/pmdaib.1.html),  [pmdajbd2(1)](../man1/pmdajbd2.1.html),  [pmdakernel(1)](../man1/pmdakernel.1.html),  [pmdakvm(1)](../man1/pmdakvm.1.html),  [pmdalogger(1)](../man1/pmdalogger.1.html),  [pmdalustrecomm(1)](../man1/pmdalustrecomm.1.html),  [pmdamailq(1)](../man1/pmdamailq.1.html),  [pmdammv(1)](../man1/pmdammv.1.html),  [pmdamounts(1)](../man1/pmdamounts.1.html),  [pmdanvidia(1)](../man1/pmdanvidia.1.html),  [pmdaopentelemetry(1)](../man1/pmdaopentelemetry.1.html),  [pmdaoverhead(1)](../man1/pmdaoverhead.1.html),  [pmdapipe(1)](../man1/pmdapipe.1.html),  [pmdapodman(1)](../man1/pmdapodman.1.html),  [pmdaproc(1)](../man1/pmdaproc.1.html),  [pmdaresctrl(1)](../man1/pmdaresctrl.1.html),  [pmdaroot(1)](../man1/pmdaroot.1.html),  [pmdasample(1)](../man1/pmdasample.1.html),  [pmdasendmail(1)](../man1/pmdasendmail.1.html),  [pmdashping(1)](../man1/pmdashping.1.html),  [pmdasimple(1)](../man1/pmdasimple.1.html),  [pmdasmart(1)](../man1/pmdasmart.1.html),  [pmdasockets(1)](../man1/pmdasockets.1.html),  [pmdastatsd(1)](../man1/pmdastatsd.1.html),  [pmdasummary(1)](../man1/pmdasummary.1.html),  [pmdasystemd(1)](../man1/pmdasystemd.1.html),  [pmdatrace(1)](../man1/pmdatrace.1.html),  [pmdatrivial(1)](../man1/pmdatrivial.1.html),  [pmdatxmon(1)](../man1/pmdatxmon.1.html),  [pmdaweblog(1)](../man1/pmdaweblog.1.html),  [pmdaxfs(1)](../man1/pmdaxfs.1.html),  [pmdazfs(1)](../man1/pmdazfs.1.html),  [pmdumptext(1)](../man1/pmdumptext.1.html),  [pmfind(1)](../man1/pmfind.1.html),  [pmgetopt(1)](../man1/pmgetopt.1.html),  [pmhostname(1)](../man1/pmhostname.1.html),  [pmie(1)](../man1/pmie.1.html),  [pminfo(1)](../man1/pminfo.1.html),  [pmjson(1)](../man1/pmjson.1.html),  [pmlc(1)](../man1/pmlc.1.html),  [pmlogbasename(1)](../man1/pmlogbasename.1.html),  [pmlogcheck(1)](../man1/pmlogcheck.1.html),  [pmlogconf(1)](../man1/pmlogconf.1.html),  [pmlogdump(1)](../man1/pmlogdump.1.html),  [pmlogextract(1)](../man1/pmlogextract.1.html),  [pmlogger(1)](../man1/pmlogger.1.html),  [pmloglabel(1)](../man1/pmloglabel.1.html),  [pmlogmv(1)](../man1/pmlogmv.1.html),  [pmlogpush(1)](../man1/pmlogpush.1.html),  [pmlogredact(1)](../man1/pmlogredact.1.html),  [pmlogreduce(1)](../man1/pmlogreduce.1.html),  [pmlogrewrite(1)](../man1/pmlogrewrite.1.html),  [pmlogsize(1)](../man1/pmlogsize.1.html),  [pmlogsummary(1)](../man1/pmlogsummary.1.html),  [pmnsdel(1)](../man1/pmnsdel.1.html),  [pmnsmerge(1)](../man1/pmnsmerge.1.html),  [pmpost(1)](../man1/pmpost.1.html),  [pmprobe(1)](../man1/pmprobe.1.html),  [pmproxy(1)](../man1/pmproxy.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [pmrepconf(1)](../man1/pmrepconf.1.html),  [pmsearch(1)](../man1/pmsearch.1.html),  [pmseries(1)](../man1/pmseries.1.html),  [pmstat(1)](../man1/pmstat.1.html),  [pmstore(1)](../man1/pmstore.1.html),  [pmtime(1)](../man1/pmtime.1.html),  [pmval(1)](../man1/pmval.1.html),  [pmview(1)](../man1/pmview.1.html),  [runaspcp(1)](../man1/runaspcp.1.html),  [\_\_pmcheckattribute(3)](../man3/__pmcheckattribute.3.html),  [\_\_pmcleanmapdir(3)](../man3/__pmcleanmapdir.3.html),  [pmda(3)](../man3/pmda.3.html),  [pmdagetoptions(3)](../man3/pmdagetoptions.3.html),  [pmprintf(3)](../man3/pmprintf.3.html),  [pmregisterderived(3)](../man3/pmregisterderived.3.html),  [pmsetdebug(3)](../man3/pmsetdebug.3.html)

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
