---
{"title": "pmlogbasename(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pmlogbasename.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pmlogbasename(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DEBUGGING OPTIONS](#DEBUGGING_OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                    |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PMLOGBASENAME(1)         General Commands Manual         PMLOGBASENAME(1)

## [](#NAME)NAME

           pmlogbasename - basename of a PCP archive

## [](#SYNOPSIS)SYNOPSIS

           pmlogbasename [-D debug] name

## [](#DESCRIPTION)DESCRIPTION

           pmlogbasename takes name (usually the name of one of the physical
           files in a PCP archive) and strips it of any compression suffixes
           then strips it of any PCP archive component suffixes, then reports
           the result (the basename of a PCP archive) on standard output.

           The compression suffixes known to PCP are: .xz, .lzma, .bz2, .bz,
           .gz, .Z and .z.

           The PCP archive component suffixes are: .meta, .index and .<n> for
           any integer <n>.

           For the most part the stripping is purely textual and is done
           without tests for the existence of any of the associated files,
           although if name does not match the pattern of a valid file name
           for a PCP archive then the output is name without any stripping.

           The one exception is when name ends with .N where N is a sequence
           of 1 or more digits, in which case an ambiguity occurs.  For
           example consider name to be 20241125.05.48, where this could mean
           the archive basename is really 20241125.05.48 or it could mean
           this refers to volume 48 of the archive basename 20241125.05.  In
           the former case, the file name.meta (or one of the compressed
           versions of this) should exist and pmlogbasename probes the
           filesystem to determine if such a file exists.

## [](#DEBUGGING_OPTIONS)DEBUGGING OPTIONS

           The -D or --debug option enables the output of additional
           diagnostics on stderr to help triage problems, although the
           information is sometimes cryptic and primarily intended to provide
           guidance for developers rather end-users.  debug is a comma
           separated list of debugging options; use pmdbg(1) with the -l
           option to obtain a list of the available debugging options and
           their meaning.

           Debugging options specific to pmlogbasename are as follows:
           ┌────────┬───────────────────────────────────────────────────────┐
           │ Option │ Description                                           │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl0  │ report the name of each file that exists and          │
           │        │ potentially matches name                              │
           ├────────┼───────────────────────────────────────────────────────┤
           │ appl1  │ report the name of each file that does not exist but  │
           │        │ was probed looking for matches with name              │
           └────────┴───────────────────────────────────────────────────────┘

## [](#SEE_ALSO)SEE ALSO

           PCPIntro(1) and LOGARCHIVE(5).

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

    Performance Co-Pilot               PCP                   PMLOGBASENAME(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlogcompress(1)](../man1/pmlogcompress.1.html)

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
