---
{"title": "sar2pcp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/sar2pcp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sar2pcp(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [NOTES](#NOTES) \| [CAVEATS](#CAVEATS) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SAR2PCP(1)               General Commands Manual               SAR2PCP(1)

## [](#NAME)NAME

           sar2pcp - import sar data and create a PCP archive

## [](#SYNOPSIS)SYNOPSIS

           sar2pcp infile outfile

## [](#DESCRIPTION)DESCRIPTION

           sar2pcp is intended to read a binary System Activity Reporting
           (sar) data file as created by sadc(1) (infile) and translate this
           into a Performance Co-Pilot (PCP) archive with the basename
           outfile.

           However, if infile has the suffix ``.xml'', then it will be
           considered already in XML format and sar2pcp will operate directly
           on it.

           The resultant PCP achive may be used with all the PCP client tools
           to graph subsets of the data using pmchart(1), perform data
           reduction and reporting, filter with the PCP inference engine
           pmie(1), etc.

           A series of physical files will be created with the prefix
           outfile.  These are outfile.0 (the performance data), outfile.meta
           (the metadata that describes the performance data) and
           outfile.index (a temporal index to improve efficiency of replay
           operations for the archive).  If any of these files exists
           already, then sar2pcp will not overwrite them and will exit with
           an error message of the form

           _&__pmLogNewFile: ``blah.0'' already exists, not over-written

           sar2pcp is a Perl script that uses the PCP::LogImport Perl wrapper
           around the PCP libpcp_import library, and as such could be used as
           an example to develop new tools to import other types of
           performance data and create PCP archives.  A Python wrapper module
           is also available.

## [](#NOTES)NOTES

           As of sysstat version 12.0.5, sadc(1) has added functionality to
           directly write PCP archive files.  To produce archive files from
           sar run:

           $ sadf -l -O pcparchive=ARCHIVE_NAME sar.dat -- -A

## [](#CAVEATS)CAVEATS

           When not using the XML input option, sar2pcp requires infile to
           have been created by a version of sadc(1) from
           http://sebastien.godard.pagesperso-orange.fr/ which includes the
           sadf(1) utility to translate infile into an XML stream (any since
           version 6); sar2pcp will automatically run sadf(1) and translate
           the resultant XML into a PCP archive.

           When using binary sadc files it is important to ensure the
           installed sadf is compatible with the version of sadc that
           originally generated the binary files.  Simply assuming a newer
           installed version will work is unfortunately far too optimistic,
           and nor should one assume that binary data from different
           platforms (e.g. different endianness) will work - these issues are
           due to limitations in sadc and sadf, and not in sar2pcp itself.

           Fortunately, the sadf message indicating that an incompatibility
           has been detected is consistent across versions, and is always
           prefixed

           Invalid system activity file

           Using an XML infile has the advantage that the installed version
           of sadf is completely bypassed.  sar2pcp undertakes to transform
           any valid XML produced by any of the different variations of sadf
           into a valid PCP archive.  Any version of PCP will be able to
           interpret the archive files produced by any version of sar2pcp,
           and you are also free to move the binary PCP archive between
           different platforms, different hardware, even different operating
           systems - it Just Works (TM).

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(5).

           For environment variables affecting PCP tools, see
           pmGetOptions(3).

## [](#SEE_ALSO)SEE ALSO

           pmie(1), pmchart(1), pmlogger(1), pmlogextract(1),
           pmlogsummary(1), sadc(1), sadf(1), sar(1), Date::Parse(3pm),
           Date::Format(3pm), PCP::LogImport(3pm), XML::TokeParser(3pm) and
           LOGIMPORT(3).

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

    Performance Co-Pilot               PCP                         SAR2PCP(1)

------------------------------------------------------------------------

Pages that refer to this page: [pcpcompat(1)](../man1/pcpcompat.1.html)

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
