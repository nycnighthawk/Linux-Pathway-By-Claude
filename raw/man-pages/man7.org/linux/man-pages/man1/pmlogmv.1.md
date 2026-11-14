---
{"title": "pmlogmv(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogmv.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogmv(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DIAGNOSTICS](#DIAGNOSTICS) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGMV(1)               General Commands Manual               PMLOGMV(1)

## [](#NAME)NAME

           pmlogmv, pmlogcp, pmlogls - move (rename), copy or list
           Performance Co-Pilot archive files

## [](#SYNOPSIS)SYNOPSIS

           pmlogmv [-cfNV?] [-D debug] srcname dstname
           pmlogcp [-cfNV?] [-D debug] srcname dstname
           pmlogls [-V?] [-D debug] srcname

## [](#DESCRIPTION)DESCRIPTION

           A Performance Co-Pilot (PCP) archive consists of multiple files as
           created by pmlogger(1).  pmlogmv allows all the files of a single
           PCP archive to be moved or renamed as a group in a single
           operation.  Similarly pmlogcp copies all the files of single PCP
           archive in a single operation.

           pmlogls is a convenience application that lists the names of all
           the files in a single PCP archive and then exits.

           The srcname argument identifies the target archive, and may be
           either the basename that is common to all files in that archive or
           one of the archive's files.

           For pmlogmv or pmlogcp, the new archive's basename is dstname,
           except when dstname is an existing directory, in which case the
           files are moved or copied into dstname using the same archive
           basename as srcname.

           Because PCP archives are important records of system activity,
           special care is taken to ensure the integrity of an archive's
           files.  For recoverable problems encountered during the execution
           of pmlogmv or pmlogcp, all the files associated with srcname will
           be preserved, and no new files with the dstname prefix will be
           created.  ``Recoverable problems'' include signals that can be
           caught (such as SIGHUP, SIGINT, SIGQUIT and SIGTERM), permissions
           issues, new files already existing, file system full events, etc.

           The implementation of pmlogmv tries to use hard links (and
           unlinking) in the file system to avoid file copying and so follows
           the semantic restrictions of link(2), which for most systems means
           the directories containing both the srcname and the dstname PCP
           archive files need to be within the same file system.  When this
           is not possible, pmlogmv falls back to to file copying.

           pmlogcp always uses file copying.

## [](#OPTIONS)OPTIONS

           The available command line options are:

           -c, --checksum
                Paranoid checking mode when file copying is needed and each
                file's checksum is computed for the original file and the
                copied file, and the checksums must match before the copy is
                considered acceptable.  The checksum command is chosen by
                trying the following in turn until one is found to be
                executable: md5sum(1), sha256sum(1), sha1sum(1) and sum(1).
                If no executable checksum command is found, a warning is
                issued and the checksum check is skipped.

           -f, --force
                Normally pmlogmv and pmlogcp take a conservative view in
                respect of dstname and will not proceed if dstname contains
                any characters that are likely to cause a problem for sh(1).
                This includes ``glob'' characters like ``?'', ``*'' and
                ``['', shell syntax meta characters like ``('', ``|'', ``;''
                and ``&'', shell I/O redirection characters like ``<'' and
                ``>'', the dollar sign, a space, etc.

                The -f flag forces the rename or copy to proceed, even if
                dstname contains any of these ``unsafe'' characters.

           -N, --showme
                Perform a dry-run, checking and reporting what changes would
                be made without making any changes.

           -V, --verbose
                Enable verbose mode.

           -?, --help
                Display usage message and exit.

## [](#DIAGNOSTICS)DIAGNOSTICS

           All error and warning messages are intended to be easily
           understood and errors produce a non-zero exit status.

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1), md5sum(1), pmlogger(1), sha1sum(1), sha256sum(1),
           link(2) and LOGARCHIVE(5).

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

    Performance Co-Pilot               PCP                         PMLOGMV(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmgetopt(1)](../man1/pmgetopt.1.html),  [pmlogger_daily(1)](../man1/pmlogger_daily.1.html)

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
