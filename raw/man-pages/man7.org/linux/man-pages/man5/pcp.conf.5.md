---
{"title": "pcp.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/pcp.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp.conf(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP.CONF(5)                File Formats Manual                PCP.CONF(5)

## [](#NAME)NAME

           pcp.conf - the Performance Co-Pilot configuration and environment
           file

## [](#SYNOPSIS)SYNOPSIS

           /etc/pcp.conf

## [](#DESCRIPTION)DESCRIPTION

           When using Performance Co-Pilot (PCP) tools and utilities and when
           calling PCP library functions, a standard set of environment
           variables are defined in /etc/pcp.conf.  These variables are
           generally used to specify the location of various PCP pieces in
           the file system and may be loaded into shell scripts by sourcing
           the /etc/pcp.env(5) shell script and queried by C/C++ programs
           using the pmGetConfig(3) library function.  If a variable is
           already defined in the environment, the values in pcp.conf do not
           override those values, i.e. the values in pcp.conf serve as
           installation defaults only.

           Both the pcp.env and pcp.conf files are expected to be found in
           /etc by default.  If required, the pcp.conf file may be relocated
           and PCP_CONF set in the environment to specify the full path to
           the new location.  The pcp.env file can not be relocated (this is
           the only hard coded path required by PCP).

           The syntax rules for pcp.conf are as follows :

           1.  the general syntax is
                      PCP_VARIABLE_NAME=variable value to end of line

           2.  lines that begin with # and all blank lines are ignored.

           3.  all variables must be prefixed with PCP_.  This is a security
               issue - variables that do not have this prefix will be
               silently ignored.

           4.  there should be no space between the variable name and the
               literal = and no space between the = and the variable value
               (unless the value actually starts with a space).  This is
               required because the pcp.conf file may be sourced directly by
               Makefiles as well as interpreted by the pcp.env script and the
               pmGetConfig function.

           5.  variable values may contain spaces and should not be quoted.
               The pcp.env script automatically quotes all variable values
               from the character immediately following the = through to the
               end of the line.

           For further details and an explanation of the use of each
           variable, see the comments in the /etc/pcp.conf file itself.

## [](#ENVIRONMENT)ENVIRONMENT

           The PCP_CONF environment variable specifies an alternative path to
           the pcp.conf file.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), pmconfig(1), PCPIntro(3), PMAPI(3), pmGetConfig(3)
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

    Performance Co-Pilot               PCP                        PCP.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [atop-daily(1)](../man1/atop-daily.1.html),  [autofsd-probe(1)](../man1/autofsd-probe.1.html),  [chkhelp(1)](../man1/chkhelp.1.html),  [collectl2pcp(1)](../man1/collectl2pcp.1.html),  [dbpmda(1)](../man1/dbpmda.1.html),  [ganglia2pcp(1)](../man1/ganglia2pcp.1.html),  [genpmda(1)](../man1/genpmda.1.html),  [iostat2pcp(1)](../man1/iostat2pcp.1.html),  [mkaf(1)](../man1/mkaf.1.html),  [mrtg2pcp(1)](../man1/mrtg2pcp.1.html),  [newhelp(1)](../man1/newhelp.1.html),  [pcp(1)](../man1/pcp.1.html),  [pcp2arrow(1)](../man1/pcp2arrow.1.html),  [pcp2elasticsearch(1)](../man1/pcp2elasticsearch.1.html),  [pcp2graphite(1)](../man1/pcp2graphite.1.html),  [pcp2influxdb(1)](../man1/pcp2influxdb.1.html),  [pcp2json(1)](../man1/pcp2json.1.html),  [pcp2openmetrics(1)](../man1/pcp2openmetrics.1.html),  [pcp2opentelemetry(1)](../man1/pcp2opentelemetry.1.html),  [pcp2spark(1)](../man1/pcp2spark.1.html),  [pcp2template(1)](../man1/pcp2template.1.html),  [pcp2xlsx(1)](../man1/pcp2xlsx.1.html),  [pcp2xml(1)](../man1/pcp2xml.1.html),  [pcp2zabbix(1)](../man1/pcp2zabbix.1.html),  [pcp-atop(1)](../man1/pcp-atop.1.html),  [pcp-atopsar(1)](../man1/pcp-atopsar.1.html),  [pcp-buddyinfo(1)](../man1/pcp-buddyinfo.1.html),  [pcp-check(1)](../man1/pcp-check.1.html),  [pcp-dmcache(1)](../man1/pcp-dmcache.1.html),  [pcp-dstat(1)](../man1/pcp-dstat.1.html),  [pcp-free(1)](../man1/pcp-free.1.html),  [pcp-geolocate(1)](../man1/pcp-geolocate.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pcp-iostat(1)](../man1/pcp-iostat.1.html),  [pcp-ipcs(1)](../man1/pcp-ipcs.1.html),  [pcp-kube-pods(1)](../man1/pcp-kube-pods.1.html),  [pcp-meminfo(1)](../man1/pcp-meminfo.1.html),  [pcp-mpstat(1)](../man1/pcp-mpstat.1.html),  [pcp-netstat(1)](../man1/pcp-netstat.1.html),  [pcp-nfsiostat(1)](../man1/pcp-nfsiostat.1.html),  [pcp-numastat(1)](../man1/pcp-numastat.1.html),  [pcp-pidstat(1)](../man1/pcp-pidstat.1.html),  [pcp-ps(1)](../man1/pcp-ps.1.html),  [pcp-python(1)](../man1/pcp-python.1.html),  [pcp-reboot-init(1)](../man1/pcp-reboot-init.1.html),  [pcp-rocestat(1)](../man1/pcp-rocestat.1.html),  [pcp-shping(1)](../man1/pcp-shping.1.html),  [pcp-slabinfo(1)](../man1/pcp-slabinfo.1.html),  [pcp-ss(1)](../man1/pcp-ss.1.html),  [pcp-tapestat(1)](../man1/pcp-tapestat.1.html),  [pcp-uptime(1)](../man1/pcp-uptime.1.html),  [pcp-verify(1)](../man1/pcp-verify.1.html),  [pcp-xsos(1)](../man1/pcp-xsos.1.html),  [pcp-zoneinfo(1)](../man1/pcp-zoneinfo.1.html),  [pmafm(1)](../man1/pmafm.1.html),  [pmcd(1)](../man1/pmcd.1.html),  [pmcd_wait(1)](../man1/pmcd_wait.1.html),  [pmchart(1)](../man1/pmchart.1.html),  [pmclient(1)](../man1/pmclient.1.html),  [pmconfig(1)](../man1/pmconfig.1.html),  [pmcpp(1)](../man1/pmcpp.1.html),  [pmdaactivemq(1)](../man1/pmdaactivemq.1.html),  [pmdaamdgpu(1)](../man1/pmdaamdgpu.1.html),  [pmdaapache(1)](../man1/pmdaapache.1.html),  [pmdabash(1)](../man1/pmdabash.1.html),  [pmdabind2(1)](../man1/pmdabind2.1.html),  [pmdabonding(1)](../man1/pmdabonding.1.html),  [pmdabpf(1)](../man1/pmdabpf.1.html),  [pmdabpftrace(1)](../man1/pmdabpftrace.1.html),  [pmdabtrfs(1)](../man1/pmdabtrfs.1.html),  [pmdachrony(1)](../man1/pmdachrony.1.html),  [pmdacifs(1)](../man1/pmdacifs.1.html),  [pmdacisco(1)](../man1/pmdacisco.1.html),  [pmdadarwin(1)](../man1/pmdadarwin.1.html),  [pmdadb2(1)](../man1/pmdadb2.1.html),  [pmdadbping(1)](../man1/pmdadbping.1.html),  [pmdadenki(1)](../man1/pmdadenki.1.html),  [pmdadm(1)](../man1/pmdadm.1.html),  [pmdadocker(1)](../man1/pmdadocker.1.html),  [pmdads389(1)](../man1/pmdads389.1.html),  [pmdads389log(1)](../man1/pmdads389log.1.html),  [pmdaelasticsearch(1)](../man1/pmdaelasticsearch.1.html),  [pmdafarm(1)](../man1/pmdafarm.1.html),  [pmdagfs2(1)](../man1/pmdagfs2.1.html),  [pmdagluster(1)](../man1/pmdagluster.1.html),  [pmdagpfs(1)](../man1/pmdagpfs.1.html),  [pmdahacluster(1)](../man1/pmdahacluster.1.html),  [pmdahaproxy(1)](../man1/pmdahaproxy.1.html),  [pmdahdb(1)](../man1/pmdahdb.1.html),  [pmdajbd2(1)](../man1/pmdajbd2.1.html),  [pmdakernel(1)](../man1/pmdakernel.1.html),  [pmdakvm(1)](../man1/pmdakvm.1.html),  [pmdalibvirt(1)](../man1/pmdalibvirt.1.html),  [pmdalio(1)](../man1/pmdalio.1.html),  [pmdalmsensors(1)](../man1/pmdalmsensors.1.html),  [pmdalogger(1)](../man1/pmdalogger.1.html),  [pmdalustre(1)](../man1/pmdalustre.1.html),  [pmdalustrecomm(1)](../man1/pmdalustrecomm.1.html),  [pmdamailq(1)](../man1/pmdamailq.1.html),  [pmdamemcache(1)](../man1/pmdamemcache.1.html),  [pmdammv(1)](../man1/pmdammv.1.html),  [pmdamongodb(1)](../man1/pmdamongodb.1.html),  [pmdamounts(1)](../man1/pmdamounts.1.html),  [pmdamssql(1)](../man1/pmdamssql.1.html),  [pmdamysql(1)](../man1/pmdamysql.1.html),  [pmdanetcheck(1)](../man1/pmdanetcheck.1.html),  [pmdanetfilter(1)](../man1/pmdanetfilter.1.html),  [pmdanfsclient(1)](../man1/pmdanfsclient.1.html),  [pmdanginx(1)](../man1/pmdanginx.1.html),  [pmdanixl(1)](../man1/pmdanixl.1.html),  [pmdanutcracker(1)](../man1/pmdanutcracker.1.html),  [pmdanvidia(1)](../man1/pmdanvidia.1.html),  [pmdaopenmetrics(1)](../man1/pmdaopenmetrics.1.html),  [pmdaopenvswitch(1)](../man1/pmdaopenvswitch.1.html),  [pmdaoracle(1)](../man1/pmdaoracle.1.html),  [pmdaoverhead(1)](../man1/pmdaoverhead.1.html),  [pmdaperfevent(1)](../man1/pmdaperfevent.1.html),  [pmdapipe(1)](../man1/pmdapipe.1.html),  [pmdapodman(1)](../man1/pmdapodman.1.html),  [pmdapostfix(1)](../man1/pmdapostfix.1.html),  [pmdapostgresql(1)](../man1/pmdapostgresql.1.html),  [pmdaproc(1)](../man1/pmdaproc.1.html),  [pmdarabbitmq(1)](../man1/pmdarabbitmq.1.html),  [pmdaredis(1)](../man1/pmdaredis.1.html),  [pmdaresctrl(1)](../man1/pmdaresctrl.1.html),  [pmdaroot(1)](../man1/pmdaroot.1.html),  [pmdarsyslog(1)](../man1/pmdarsyslog.1.html),  [pmdasample(1)](../man1/pmdasample.1.html),  [pmdasendmail(1)](../man1/pmdasendmail.1.html),  [pmdashping(1)](../man1/pmdashping.1.html),  [pmdasimple(1)](../man1/pmdasimple.1.html),  [pmdaslurm(1)](../man1/pmdaslurm.1.html),  [pmdasmart(1)](../man1/pmdasmart.1.html),  [pmdasockets(1)](../man1/pmdasockets.1.html),  [pmdastatsd(1)](../man1/pmdastatsd.1.html),  [pmdasummary(1)](../man1/pmdasummary.1.html),  [pmdasystemd(1)](../man1/pmdasystemd.1.html),  [pmdate(1)](../man1/pmdate.1.html),  [pmdatrace(1)](../man1/pmdatrace.1.html),  [pmdatrivial(1)](../man1/pmdatrivial.1.html),  [pmdatxmon(1)](../man1/pmdatxmon.1.html),  [pmdaunbound(1)](../man1/pmdaunbound.1.html),  [pmdauwsgi(1)](../man1/pmdauwsgi.1.html),  [pmdavalkey(1)](../man1/pmdavalkey.1.html),  [pmdaweblog(1)](../man1/pmdaweblog.1.html),  [pmdaxfs(1)](../man1/pmdaxfs.1.html),  [pmdazfs(1)](../man1/pmdazfs.1.html),  [pmdazimbra(1)](../man1/pmdazimbra.1.html),  [pmdazswap(1)](../man1/pmdazswap.1.html),  [pmdbg(1)](../man1/pmdbg.1.html),  [pmdiff(1)](../man1/pmdiff.1.html),  [pmdumptext(1)](../man1/pmdumptext.1.html),  [pmerr(1)](../man1/pmerr.1.html),  [pmfind(1)](../man1/pmfind.1.html),  [pmfind_check(1)](../man1/pmfind_check.1.html),  [pmgenmap(1)](../man1/pmgenmap.1.html),  [pmgetopt(1)](../man1/pmgetopt.1.html),  [pmhostname(1)](../man1/pmhostname.1.html),  [pmie(1)](../man1/pmie.1.html),  [pmie2col(1)](../man1/pmie2col.1.html),  [pmie_check(1)](../man1/pmie_check.1.html),  [pmieconf(1)](../man1/pmieconf.1.html),  [pmiestatus(1)](../man1/pmiestatus.1.html),  [pminfo(1)](../man1/pminfo.1.html),  [pmjson(1)](../man1/pmjson.1.html),  [pmlc(1)](../man1/pmlc.1.html),  [pmlogcheck(1)](../man1/pmlogcheck.1.html),  [pmlogconf(1)](../man1/pmlogconf.1.html),  [pmlogctl(1)](../man1/pmlogctl.1.html),  [pmlogdump(1)](../man1/pmlogdump.1.html),  [pmlogextract(1)](../man1/pmlogextract.1.html),  [pmlogger(1)](../man1/pmlogger.1.html),  [pmlogger_check(1)](../man1/pmlogger_check.1.html),  [pmlogger_daily(1)](../man1/pmlogger_daily.1.html),  [pmlogger_daily_report(1)](../man1/pmlogger_daily_report.1.html),  [pmlogger_janitor(1)](../man1/pmlogger_janitor.1.html),  [pmlogger_merge(1)](../man1/pmlogger_merge.1.html),  [pmlogger_rewrite(1)](../man1/pmlogger_rewrite.1.html),  [pmloglabel(1)](../man1/pmloglabel.1.html),  [pmlogpaste(1)](../man1/pmlogpaste.1.html),  [pmlogpush(1)](../man1/pmlogpush.1.html),  [pmlogredact(1)](../man1/pmlogredact.1.html),  [pmlogreduce(1)](../man1/pmlogreduce.1.html),  [pmlogrewrite(1)](../man1/pmlogrewrite.1.html),  [pmlogsize(1)](../man1/pmlogsize.1.html),  [pmlogsummary(1)](../man1/pmlogsummary.1.html),  [pmnsadd(1)](../man1/pmnsadd.1.html),  [pmnscomp(1)](../man1/pmnscomp.1.html),  [pmnsdel(1)](../man1/pmnsdel.1.html),  [pmnsmerge(1)](../man1/pmnsmerge.1.html),  [pmpost(1)](../man1/pmpost.1.html),  [pmprobe(1)](../man1/pmprobe.1.html),  [pmproxy(1)](../man1/pmproxy.1.html),  [pmpython(1)](../man1/pmpython.1.html),  [pmquery(1)](../man1/pmquery.1.html),  [pmrep(1)](../man1/pmrep.1.html),  [pmrepconf(1)](../man1/pmrepconf.1.html),  [pmsearch(1)](../man1/pmsearch.1.html),  [pmseries(1)](../man1/pmseries.1.html),  [pmsignal(1)](../man1/pmsignal.1.html),  [pmstat(1)](../man1/pmstat.1.html),  [pmstore(1)](../man1/pmstore.1.html),  [pmtrace(1)](../man1/pmtrace.1.html),  [pmval(1)](../man1/pmval.1.html),  [pmview(1)](../man1/pmview.1.html),  [runaspcp(1)](../man1/runaspcp.1.html),  [sar2pcp(1)](../man1/sar2pcp.1.html),  [sheet2pcp(1)](../man1/sheet2pcp.1.html),  [telnet-probe(1)](../man1/telnet-probe.1.html),  [pcpintro(3)](../man3/pcpintro.3.html),  [pmapi(3)](../man3/pmapi.3.html),  [pmda(3)](../man3/pmda.3.html),  [pmdaopenlog(3)](../man3/pmdaopenlog.3.html),  [pmdatrace(3)](../man3/pmdatrace.3.html),  [pmdiscoverservices(3)](../man3/pmdiscoverservices.3.html),  [pmdiscoversetup(3)](../man3/pmdiscoversetup.3.html),  [pmgetarchiveend(3)](../man3/pmgetarchiveend.3.html),  [pmgetarchivelabel(3)](../man3/pmgetarchivelabel.3.html),  [pmgetchildren(3)](../man3/pmgetchildren.3.html),  [pmgetchildrenstatus(3)](../man3/pmgetchildrenstatus.3.html),  [pmgetconfig(3)](../man3/pmgetconfig.3.html),  [pmgetcontexthostname(3)](../man3/pmgetcontexthostname.3.html),  [pmgetindom(3)](../man3/pmgetindom.3.html),  [pmgetindomarchive(3)](../man3/pmgetindomarchive.3.html),  [pmgetoptions(3)](../man3/pmgetoptions.3.html),  [pmgetpmnslocation(3)](../man3/pmgetpmnslocation.3.html),  [pmidstr(3)](../man3/pmidstr.3.html),  [pmindomstr(3)](../man3/pmindomstr.3.html),  [pmloadasciinamespace(3)](../man3/pmloadasciinamespace.3.html),  [pmloadnamespace(3)](../man3/pmloadnamespace.3.html),  [pmlocaltime(3)](../man3/pmlocaltime.3.html),  [pmlookupdesc(3)](../man3/pmlookupdesc.3.html),  [pmlookupindom(3)](../man3/pmlookupindom.3.html),  [pmlookupindomarchive(3)](../man3/pmlookupindomarchive.3.html),  [pmlookupindomtext(3)](../man3/pmlookupindomtext.3.html),  [pmlookupname(3)](../man3/pmlookupname.3.html),  [pmlookuptext(3)](../man3/pmlookuptext.3.html),  [pmnameall(3)](../man3/pmnameall.3.html),  [pmnameid(3)](../man3/pmnameid.3.html),  [pmnameindom(3)](../man3/pmnameindom.3.html),  [pmnameindomarchive(3)](../man3/pmnameindomarchive.3.html),  [pmnewcontext(3)](../man3/pmnewcontext.3.html),  [pmnewcontextzone(3)](../man3/pmnewcontextzone.3.html),  [pmnewzone(3)](../man3/pmnewzone.3.html),  [LOGARCHIVE(5)](../man5/LOGARCHIVE.5.html),  [mmv(5)](../man5/mmv.5.html),  [pcp-dstat(5)](../man5/pcp-dstat.5.html),  [pcp.env(5)](../man5/pcp.env.5.html),  [pmlogger.control(5)](../man5/pmlogger.control.5.html),  [pmns(5)](../man5/pmns.5.html),  [pmrep.conf(5)](../man5/pmrep.conf.5.html)

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
