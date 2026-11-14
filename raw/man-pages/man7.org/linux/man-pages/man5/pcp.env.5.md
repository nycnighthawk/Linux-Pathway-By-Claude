---
{"title": "pcp.env(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/pcp.env.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcp.env(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCP.ENV(5)                 File Formats Manual                 PCP.ENV(5)

## [](#NAME)NAME

           pcp.env - script to set Performance Co-Pilot run-time environment
           variables

## [](#SYNOPSIS)SYNOPSIS

           /etc/pcp.env

## [](#DESCRIPTION)DESCRIPTION

           The pcp.env script is sourced by assorted Performance Co-Pilot
           (PCP) scripts and utilities to define the PCP operating
           environment variables.  The conjugate for executable programs
           using the PCP libraries is the pmGetConfig(3) function.

           Typical usage of pcp.env in a script is as follows :

                    #! /bin/sh

                    # source the PCP environment variables
                    . /etc/pcp.env
                    rest of script ...

           The full syntax and semantics of the pcp.conf file and the
           pmGetConfig function are described in their respective reference
           pages.

           If the file $HOME/.pcp/pcp.conf exists then this will be processed
           after the system-wide pcp.conf file.  This provides a mechanism to
           selectively modify or augment the environment settings for PCP
           scripts, which maybe useful if the scripts are run with sudo(1)
           which cleans the environment of important settings that are
           required to ensure the correct execution of the PCP scripts, e.g.
           $PATH or $PERL5LIB.

## [](#ENVIRONMENT)ENVIRONMENT

           The PCP_CONF environment variable specifies an alternative path to
           the pcp.conf file.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), sudo(1), PCPIntro(3), PMAPI(3), pmGetConfig(3) and
           pcp.conf(5).

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

    Performance Co-Pilot               PCP                         PCP.ENV(5)

------------------------------------------------------------------------

Pages that refer to this page: [atop-daily(1)](../man1/atop-daily.1.html),  [chkhelp(1)](../man1/chkhelp.1.html),  [collectl2pcp(1)](../man1/collectl2pcp.1.html),  [dbpmda(1)](../man1/dbpmda.1.html),  [genpmda(1)](../man1/genpmda.1.html),  [mkaf(1)](../man1/mkaf.1.html),  [newhelp(1)](../man1/newhelp.1.html),  [pcp(1)](../man1/pcp.1.html),  [pcp-check(1)](../man1/pcp-check.1.html),  [pcp-geolocate(1)](../man1/pcp-geolocate.1.html),  [pcpintro(1)](../man1/pcpintro.1.html),  [pcp-iostat(1)](../man1/pcp-iostat.1.html),  [pcp-kube-pods(1)](../man1/pcp-kube-pods.1.html),  [pcp-reboot-init(1)](../man1/pcp-reboot-init.1.html),  [pcp-tapestat(1)](../man1/pcp-tapestat.1.html),  [pmafm(1)](../man1/pmafm.1.html),  [pmcd(1)](../man1/pmcd.1.html),  [pmcd_wait(1)](../man1/pmcd_wait.1.html),  [pmclient(1)](../man1/pmclient.1.html),  [pmconfig(1)](../man1/pmconfig.1.html),  [pmcpp(1)](../man1/pmcpp.1.html),  [pmdaamdgpu(1)](../man1/pmdaamdgpu.1.html),  [pmdaapache(1)](../man1/pmdaapache.1.html),  [pmdabtrfs(1)](../man1/pmdabtrfs.1.html),  [pmdacisco(1)](../man1/pmdacisco.1.html),  [pmdadenki(1)](../man1/pmdadenki.1.html),  [pmdadocker(1)](../man1/pmdadocker.1.html),  [pmdajbd2(1)](../man1/pmdajbd2.1.html),  [pmdakernel(1)](../man1/pmdakernel.1.html),  [pmdalmsensors(1)](../man1/pmdalmsensors.1.html),  [pmdalogger(1)](../man1/pmdalogger.1.html),  [pmdalustrecomm(1)](../man1/pmdalustrecomm.1.html),  [pmdamailq(1)](../man1/pmdamailq.1.html),  [pmdammv(1)](../man1/pmdammv.1.html),  [pmdamounts(1)](../man1/pmdamounts.1.html),  [pmdanvidia(1)](../man1/pmdanvidia.1.html),  [pmdaoverhead(1)](../man1/pmdaoverhead.1.html),  [pmdaperfevent(1)](../man1/pmdaperfevent.1.html),  [pmdapipe(1)](../man1/pmdapipe.1.html),  [pmdapodman(1)](../man1/pmdapodman.1.html),  [pmdaproc(1)](../man1/pmdaproc.1.html),  [pmdaresctrl(1)](../man1/pmdaresctrl.1.html),  [pmdasample(1)](../man1/pmdasample.1.html),  [pmdasimple(1)](../man1/pmdasimple.1.html),  [pmdastatsd(1)](../man1/pmdastatsd.1.html),  [pmdasystemd(1)](../man1/pmdasystemd.1.html),  [pmdate(1)](../man1/pmdate.1.html),  [pmdaxfs(1)](../man1/pmdaxfs.1.html),  [pmdazfs(1)](../man1/pmdazfs.1.html),  [pmdbg(1)](../man1/pmdbg.1.html),  [pmdiff(1)](../man1/pmdiff.1.html),  [pmerr(1)](../man1/pmerr.1.html),  [pmfind(1)](../man1/pmfind.1.html),  [pmgenmap(1)](../man1/pmgenmap.1.html),  [pmgetopt(1)](../man1/pmgetopt.1.html),  [pmhostname(1)](../man1/pmhostname.1.html),  [pmie(1)](../man1/pmie.1.html),  [pmiestatus(1)](../man1/pmiestatus.1.html),  [pminfo(1)](../man1/pminfo.1.html),  [pmjson(1)](../man1/pmjson.1.html),  [pmlc(1)](../man1/pmlc.1.html),  [pmlogcheck(1)](../man1/pmlogcheck.1.html),  [pmlogconf(1)](../man1/pmlogconf.1.html),  [pmlogdump(1)](../man1/pmlogdump.1.html),  [pmlogextract(1)](../man1/pmlogextract.1.html),  [pmlogger(1)](../man1/pmlogger.1.html),  [pmloglabel(1)](../man1/pmloglabel.1.html),  [pmlogpush(1)](../man1/pmlogpush.1.html),  [pmlogredact(1)](../man1/pmlogredact.1.html),  [pmlogreduce(1)](../man1/pmlogreduce.1.html),  [pmlogrewrite(1)](../man1/pmlogrewrite.1.html),  [pmnsadd(1)](../man1/pmnsadd.1.html),  [pmnscomp(1)](../man1/pmnscomp.1.html),  [pmnsdel(1)](../man1/pmnsdel.1.html),  [pmnsmerge(1)](../man1/pmnsmerge.1.html),  [pmpost(1)](../man1/pmpost.1.html),  [pmprobe(1)](../man1/pmprobe.1.html),  [pmproxy(1)](../man1/pmproxy.1.html),  [pmrepconf(1)](../man1/pmrepconf.1.html),  [pmsignal(1)](../man1/pmsignal.1.html),  [pmstat(1)](../man1/pmstat.1.html),  [pmval(1)](../man1/pmval.1.html),  [pcpintro(3)](../man3/pcpintro.3.html),  [pmapi(3)](../man3/pmapi.3.html),  [pmdiscoverservices(3)](../man3/pmdiscoverservices.3.html),  [pmdiscoversetup(3)](../man3/pmdiscoversetup.3.html),  [pmgetarchiveend(3)](../man3/pmgetarchiveend.3.html),  [pmgetarchivelabel(3)](../man3/pmgetarchivelabel.3.html),  [pmgetchildren(3)](../man3/pmgetchildren.3.html),  [pmgetchildrenstatus(3)](../man3/pmgetchildrenstatus.3.html),  [pmgetconfig(3)](../man3/pmgetconfig.3.html),  [pmgetcontexthostname(3)](../man3/pmgetcontexthostname.3.html),  [pmgetindom(3)](../man3/pmgetindom.3.html),  [pmgetindomarchive(3)](../man3/pmgetindomarchive.3.html),  [pmgetpmnslocation(3)](../man3/pmgetpmnslocation.3.html),  [pmidstr(3)](../man3/pmidstr.3.html),  [pmindomstr(3)](../man3/pmindomstr.3.html),  [pmloadasciinamespace(3)](../man3/pmloadasciinamespace.3.html),  [pmloadnamespace(3)](../man3/pmloadnamespace.3.html),  [pmlocaltime(3)](../man3/pmlocaltime.3.html),  [pmlookupdesc(3)](../man3/pmlookupdesc.3.html),  [pmlookupindom(3)](../man3/pmlookupindom.3.html),  [pmlookupindomarchive(3)](../man3/pmlookupindomarchive.3.html),  [pmlookupindomtext(3)](../man3/pmlookupindomtext.3.html),  [pmlookupname(3)](../man3/pmlookupname.3.html),  [pmlookuptext(3)](../man3/pmlookuptext.3.html),  [pmnameall(3)](../man3/pmnameall.3.html),  [pmnameid(3)](../man3/pmnameid.3.html),  [pmnameindom(3)](../man3/pmnameindom.3.html),  [pmnameindomarchive(3)](../man3/pmnameindomarchive.3.html),  [pmnewcontext(3)](../man3/pmnewcontext.3.html),  [pmnewcontextzone(3)](../man3/pmnewcontextzone.3.html),  [pmnewzone(3)](../man3/pmnewzone.3.html),  [LOGARCHIVE(5)](../man5/LOGARCHIVE.5.html),  [mmv(5)](../man5/mmv.5.html),  [pcp.conf(5)](../man5/pcp.conf.5.html),  [pmns(5)](../man5/pmns.5.html)

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
