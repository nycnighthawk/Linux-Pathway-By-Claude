---
{"title": "oprofile(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/oprofile.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# oprofile(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPERF](#OPERF) \| [OCOUNT](#OCOUNT) \| [OPREPORT](#OPREPORT) \| [OPANNOTATE](#OPANNOTATE) \| [OPARCHIVE](#OPARCHIVE) \| [OPGPROF](#OPGPROF) \| [PROFILE SPECIFICATIONS](#PROFILE_SPECIFICATIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [FILES](#FILES) \| [VERSION](#VERSION) \| [SEE ALSO](#SEE_ALSO) \| [COPYRIGHT](#COPYRIGHT) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    OPROFILE(1)              General Commands Manual              OPROFILE(1)

## [](#NAME)NAME

           oprofile - a statistical profiler for Linux systems, capable of
           profiling all running code at low overhead; also included is a set
           of post-profiling analysis tools, as well as a simple event
           counting tool

## [](#SYNOPSIS)SYNOPSIS

           operf [ options ]
           ocount [ options ]
           opreport [ options ] [ profile specification ]
           opannotate [ options ] [ profile specification ]
           oparchive [ options ] [ profile specification ]
           opgprof [ options ] [ profile specification ]

## [](#DESCRIPTION)DESCRIPTION

           OProfile is a profiling system for systems running Linux 2.6.31
           and greater. OProfile makes use of the hardware performance
           counters provided on Intel, AMD, and other processors.  OProfile
           can profile a selected program or process or the whole system.
           OProfile can also be used to collect cumulative event counts at
           the application, process, or system level.
           For a gentle guide to using OProfile, please read the HTML
           documentation listed in SEE ALSO.

## [](#OPERF)OPERF

           operf is a performance profiler tool for Linux.

## [](#OCOUNT)OCOUNT

           ocount is an event counting tool for Linux.

## [](#OPREPORT)OPREPORT

           opreport gives image and symbol-based profile summaries for the
           whole system or a subset of binary images.

## [](#OPANNOTATE)OPANNOTATE

           opannotate can produce annotated source or mixed source and
           assembly output.

## [](#OPARCHIVE)OPARCHIVE

           oparchive produces oprofile archive for offline analysis

## [](#OPGPROF)OPGPROF

           opgprof can produce a gprof-format profile for a single binary.

## [](#PROFILE_SPECIFICATIONS)PROFILE SPECIFICATIONS

           Various optional profile specifications may be used with the post-
           profiling tools. A profile specification is some combination of
           the parameters listed below. ( Note: Enclosing part of a profile
           specification in curly braces { } can be used for differential
           profiles with opreport, but the braces must be surrounded by
           whitespace.)

           archive:archive
                  Path to the archive to inspect, as generated by oparchive

           session:sessionlist
                  A comma-separated list of session names to resolve in.
                  Absence of this tag, unlike all others, means "the current
                  session", equivalent to specifying "session:current".

           session-exclude:sessionlist
                  A comma-separated list of sessions to exclude.

           image:imagelist
                  A comma-separated list of image names to resolve. Each
                  entry may be relative path, glob-style name, or full path,
                  e.g.  opreport 'image:/usr/bin/operf,*op*,./oprofpp'

           image-exclude:imagelist
                  Same as image:, but the matching images are excluded.

           lib-image:imagelist
                  Same as image:, but only for images that are for a
                  particular primary binary image (namely, an application).
                  This only makes sense to use if you're using --separate.
                  This includes kernel modules and the kernel when using
                  --separate=kernel.

           lib-image-exclude:imagelist
                  Same as <option>lib-image:</option>, but the matching
                  images are excluded.

           event:eventname
                  The symbolic event name to match on, e.g.
                  event:DATA_MEM_REFS.

           count:eventcount
                  The event count to match on, e.g. event:DATA_MEM_REFS
                  count:30000.

           unit-mask:maskvalue
                  The unit mask value of the event to match on, e.g. unit-
                  mask:1.

           cpu:cpulist
                  Only consider profiles for the given numbered CPU (starting
                  from zero).  This is only useful when using CPU profile
                  separation.

           tgid:pidlist
                  Only consider profiles for the given task groups. Unless
                  some program is using threads, the task group ID of a
                  process is the same as its process ID. This option
                  corresponds to the POSIX notion of a thread group. This is
                  only useful when using per-process profile separation.

           tid:tidlist
                  Only consider profiles for the given threads. When using
                  recent thread libraries, all threads in a process share the
                  same task group ID, but have different thread IDs. You can
                  use this option in combination with tgid: to restrict the
                  results to particular threads within a process.  This is
                  only useful when using per-process profile separation.

## [](#ENVIRONMENT)ENVIRONMENT

           No special environment variables are recognized by OProfile.

## [](#FILES)FILES

           /usr/local/share/doc/oprofile/oprofile.html
                  OProfile user guide.

           /usr/local/share/doc/oprofile/opreport.xsd
                  Schema file for opreport XML output.

           /usr/local/share/doc/oprofile/ophelp.xsd
                  Schema file for ophelp XML output.

           /usr/local/share/oprofile/
                  Event description files used by OProfile.

           <session-dir>/samples/operf.log
                  The profiler log file.

           <session-dir>/samples/current
                  The location of the generated sample files.

## [](#VERSION)VERSION

           This man page is current for oprofile-1.5.0git.

## [](#SEE_ALSO)SEE ALSO

           /usr/local/share/doc/oprofile/, operf(1), ocount(1), opreport(1),
           opannotate(1), oparchive(1), opgprof(1), gprof(1), CPU vendor
           architecture manuals

## [](#COPYRIGHT)COPYRIGHT

           oprofile is Copyright (C) 1998-2004 University of Manchester, UK,
           John Levon, and others.  OProfile is released under the GNU
           General Public License, Version 2, or (at your option) any later
           version.

## [](#AUTHORS)AUTHORS

           John Levon <levon@movementarian.org> is the primary author. See
           the documentation for other contributors.

## [](#COLOPHON)COLOPHON

           This page is part of the oprofile (a system-wide profiler for
           Linux) project.  Information about the project can be found at 
           ⟨http://oprofile.sourceforge.net/news/⟩.  If you have a bug report
           for this manual page, see ⟨http://oprofile.sourceforge.net/bugs/⟩.
           This page was obtained from the project's upstream Git repository
           ⟨git://git.code.sf.net/p/oprofile/oprofile⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2024-12-10.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    4th Berkeley Distribution    Sun 24 May 2026                  OPROFILE(1)

------------------------------------------------------------------------

Pages that refer to this page: [oparchive(1)](../man1/oparchive.1.html),  [opjitconv(1)](../man1/opjitconv.1.html),  [lookup_dcookie(2)](../man2/lookup_dcookie.2.html)

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
