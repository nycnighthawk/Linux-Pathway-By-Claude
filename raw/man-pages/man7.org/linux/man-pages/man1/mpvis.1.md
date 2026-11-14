---
{"title": "mpvis(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mpvis.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mpvis(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMAND LINE OPTIONS](#COMMAND_LINE_OPTIONS) \| [LAUNCH](#LAUNCH) \| [FILES](#FILES) \| [PCP ENVIRONMENT](#PCP_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                         |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MPVIS(1)                 General Commands Manual                 MPVIS(1)

## [](#NAME)NAME

           mpvis - visualize cpu utilization/performance

## [](#SYNOPSIS)SYNOPSIS

           mpvis [-biV] [-r rowlength] [-R rowlength] [pmview options] [cpuid
           ...]

## [](#DESCRIPTION)DESCRIPTION

           mpvis displays a three dimensional bar chart of CPU utilization.
           The display is updated with new values retrieved from the target
           host or archive every interval seconds (default is 2 seconds).

           The height of the bars is proportional to the CPU utilization in
           each of the modes idle (with no I/O pending), wait (idle, but
           waiting for I/O - only visible in IRIX), intr (interrupt
           processing - only visible in IRIX), nice (nice state - only
           visible in Linux), sys (in the kernel) and user.

           The number of CPUs per row in the scene is governed by the default
           maximum row length, and the options -b, -r and -R.  If none of
           these flags are specified, mpvis uses the default maximum row
           length to calculate the actual number of rows and columns in the
           view, according to:

                nrows = (ncpus + maxrowlen - 1) / maxrowlen
                ncols = (ncpus + nrows - 1) / nrows.

           The -r option uses the above algorithm, but allows the user to
           override the maximum row length.

           The CPUs are sorted in ascending order.  They are displayed from
           left to right, and front to back (in the case where there is more
           than one row of CPUs).

           The user can specify a list of CPUs as cpuid arguments using the
           naming scheme reported by
              $ pminfo -f kernel.percpu.cpu.user
           i.e. cpuN or cpuA:B depending on the operating system version and
           platform.  Alternatively, if the cpuid argument contains one of
           the characters ^ or .  or [ then cpuid will be treated as a
           regular expression in the style of egrep(1) and the matching set
           of CPU names will be used instead of cpuid.

           If one or more cpuid arguments is specified, then only the CPUs in
           this list are displayed in the view.  The list of CPUs is sorted
           into ascending CPU number and they are displayed from left to
           right, and front to back (in the case where there is more than one
           row of CPUs).

           mpvis generates a pmview(1) configuration file, and passes most
           command line options to pmview(1).  Therefore, the command line
           options -A, -a, -C, -h, -n, -O, -p, -S, -t, -T, -Z and -z, and the
           user interface are described in the pmview(1) man page.

## [](#COMMAND_LINE_OPTIONS)COMMAND LINE OPTIONS

           The mpvis specific options are:

           -b  Use a ratio for row:column of 1:8.  This option is best for
               large numbers of CPUs.  If the row length is not a factor of
               the number of CPUs, then the last row will be shorter than all
               other rows.  This option ignores the maximum row length.

           -i  Label each CPU column with the CPU number.

           -r  Split the view into a number of rows, where each row has a
               maximum length of n CPUs.  This is a soft limit.  The actual
               row length is calculated by an algorithm (see above) which
               prduces a balanced view with no more than n CPUs per row.

           -R  Split the view into a number of rows, where each row has a
               length of n CPUs.  This is a hard limit.  If the row length is
               not a factor of the number of CPUs, then the last row will be
               shorter than all other rows.

           -V  Verbose mode - output the generated pmview(1) configuration
               file.

## [](#LAUNCH)LAUNCH

           The behavior of pmchart(1) when launched from mpvis is dependent
           on the number of CPUs in each row.  If there are more than 6 CPUs
           in a row then each chart will contain a separate metric, otherwise
           each chart will contain a separate CPU instance.

## [](#FILES)FILES

           $PCP_VAR_DIR/config/pmlogger/config.mpvis
                  A pmlogger(1) configuration file for mpvis metrics.
           $PCP_SHARE_DIR/lib/pmview-args
                  Shell procedures for parsing pmview(1) command line
                  options.

## [](#PCP_ENVIRONMENT)PCP ENVIRONMENT

           Environment variables with the prefix PCP_ are used to
           parameterize the file and directory names used by PCP.  On each
           installation, the file /etc/pcp.conf contains the local values for
           these variables.  The $PCP_CONF variable may be used to specify an
           alternative configuration file, as described in pcp.conf(4).

## [](#SEE_ALSO)SEE ALSO

           dkvis(1), nfsvis(1), pmcd(1), pmchart(1), pmlogger(1) and
           pmview(1).

           The CPU view for pmchart(1).

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

    Performance Co-Pilot                                             MPVIS(1)

------------------------------------------------------------------------

Pages that refer to this page: [clustervis(1)](../man1/clustervis.1.html),  [dkvis(1)](../man1/dkvis.1.html),  [nfsvis(1)](../man1/nfsvis.1.html),  [pmview(1)](../man1/pmview.1.html)

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
