---
{"title": "pmafm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmafm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmafm(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                   |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMAFM(1)                 General Commands Manual                 PMAFM(1)

## [](#NAME)NAME

           pmafm - Performance Co-Pilot archive folio manager

## [](#SYNOPSIS)SYNOPSIS

           pmafm folioname [command [arg ...]]

## [](#DESCRIPTION)DESCRIPTION

           A collection of one or more Performance Co-Pilot (PCP) archives
           may be combined with a control file to produce a PCP archive
           folio.  Archive folios are created using either mkaf(1) or the
           interactive ``record mode'' services of PCP clients like
           pmchart(1).

           pmafm provides a number of services that may be used to process
           folios.  In particular, it provides support for execution of PCP
           tools using one or more of the component archives within an
           archive folio.

           The target folio is identified by the folio control file
           folioname.  The syntax for a folio control file is described in
           mkaf(1).

           If present, the command and arguments following folioname are
           interpreted and executed as a single command, otherwise commands
           are read from standard input.

           The following commands are supported.

           archives
                  Subsequent commands apply to all archives in the folio.

           archives N[,...]
                  Archives within a folio are numbered 1, 2, etc.  Subsequent
                  commands are restricted to apply only to the designated
                  archives.

           archives name[,...]
                  Archives within a folio have unique names.  Subsequent
                  commands are restricted to apply only to the designated
                  archives.

           check  Validate the presence and format of each file in the folio
                  and the component archives.

           help
                  A brief reminder of the command syntax.  ?  is a synonym
                  for help.

           hosts
                  Subsequent commands apply to all archives in the folio.

           hosts hostname[,...]
                  Subsequent commands are restricted to apply only to those
                  archives that match the designated hostnames.

           list [verbose]
                  Display the contents of the folio.  By default the control
                  header and the ordinal number, hostname and archive base
                  name for each archive in the folio.  The verbose option
                  causes pmafm to dump the label record from each archive
                  using pmlogdump -l.

                  The first named archive in the folio is assumed to be
                  associated with the default host for any tool that tries to
                  replay multiple archives from the folio.

           quit
                  Exit pmafm.

           remove
                  Echo on standard output the sh(1) commands required to
                  remove all of the physical files associated with this
                  archive folio.

           repeat tool [arg ...]
                  Execute the known PCP tool once per selected archive.  For
                  example, the command
                       repeat pmval -t60 kernel.all.load
                  would run pmval(1) once per archive, with an appropriate -a
                  argument.

           replay
                  Some archive folios are created by tools (e.g. pmchart(1))
                  that provide sufficient information to allow all of the
                  information in all of the archives of a folio to be
                  replayed.

           [run] tool [arg ...]
                  Execute the known PCP tool on the selected archives.  Some
                  PCP tools are able to process multiple concurrent archives,
                  and in this case the tool is run once with the list of all
                  selected archives passed via a -a argument.  Otherwise,
                  this command is synonymous with repeat.

           selections
                  Display those archives that would be selected for
                  processing with a repeat, replay or run command.

           The restrictions via any hosts and archives commands are
           conjuncted.  These restrictions serve to limit the specific
           archives processed in the subsequent repeat, replay, run and
           selections commands.  By default, all archives are selected.

           Keywords in commands may be abbreviated provided no ambiguity is
           introduced, e.g.  help, hel and he are synonymous, but h is
           ambiguous.

## [](#FILES)FILES

           $PCP_VAR_DIR/config/pmafm/*
                control files that define the behavior of each PCP tool known
                to pmafm.  This information may be customized or extended,
                see $PCP_VAR_DIR/config/pmafm/pcp for documentation of the
                syntax and semantics of these files.

           $HOME/.pcp/pmafm/*
                User customization of the control files.  All files in this
                directory are treated in the same manner as control files in
                the $PCP_VAR_DIR/config/pmafm directory.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

## [](#SEE_ALSO)SEE ALSO

           mkaf(1), pcp-atop(1), pmchart(1), pmlogdump(1), PMAPI(3),
           pmRecordSetup(3), pcp.conf(5) and pcp.env(5).

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

    Performance Co-Pilot               PCP                           PMAFM(1)

------------------------------------------------------------------------

Pages that refer to this page: [mkaf(1)](../man1/mkaf.1.html),  [pmchart(1)](../man1/pmchart.1.html),  [pmsnap(1)](../man1/pmsnap.1.html),  [pmview(1)](../man1/pmview.1.html),  [pmrecord(3)](../man3/pmrecord.3.html),  [LOGARCHIVE(5)](../man5/LOGARCHIVE.5.html)

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
