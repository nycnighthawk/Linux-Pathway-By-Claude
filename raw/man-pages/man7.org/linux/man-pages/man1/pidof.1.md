---
{"title": "pidof(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pidof.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pidof(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PIDOF(1)                 General Commands Manual                 PIDOF(1)

## [](#NAME)NAME

           pidof - find the process ID of a running program

## [](#SYNOPSIS)SYNOPSIS

           pidof [-s] [-c] [-q] [-w] [-x] [-o omitpid[,...]] ... [-t] [-S
           separator] program ...

## [](#DESCRIPTION)DESCRIPTION

           Pidof finds the process id's (pids) of the named programs. It
           prints those id's on the standard output.

## [](#OPTIONS)OPTIONS

           -s     Single shot - this instructs the program to only return one
                  pid.

           -c     Only return process ids that are running with the same root
                  directory.  This option is ignored for non-root users, as
                  they will be unable to check the current root directory of
                  processes they do not own.

           -q     Quiet mode, suppress any output and only sets the exit
                  status accordingly.

           -w     Show also processes that do not have visible command line
                  (e.g. kernel worker threads).

           -x     Scripts too - this causes the program to also return
                  process id's of shells running the named scripts.

           -o omitpid
                  Tells pidof to omit processes with that process id. The
                  special pid %PPID can be used to name the parent process of
                  the pidof program, in other words the calling shell or
                  shell script.

           -t     Shows all thread ids instead of pids.

           -S separator
                  Use separator as a separator put between pids. Used only
                  when more than one pids are printed for the program.  The
                  -d option is an alias for this option for sysvinit pidof
                  compatibility.

## [](#EXIT_STATUS)EXIT STATUS

           0      At least one program was found with the requested name.

           1      No program was found with the requested name.

## [](#BUGS)BUGS

           When using the -x option, pidof only has a simple method for
           detecting scripts and will miss scripts that, for example, use
           env. This limitation is due to how the scripts look in the proc
           filesystem.

## [](#SEE_ALSO)SEE ALSO

           pgrep(1), pkill(1)

## [](#AUTHOR)AUTHOR

           Jaromir Capik ⟨jcapik@redhat.com⟩

## [](#COLOPHON)COLOPHON

           This page is part of the procps-ng (/proc filesystem utilities)
           project.  Information about the project can be found at 
           ⟨https://gitlab.com/procps-ng/procps⟩.  If you have a bug report
           for this manual page, see
           ⟨https://gitlab.com/procps-ng/procps/blob/master/Documentation/bugs.md⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://gitlab.com/procps-ng/procps.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    procps-ng                       2023-01-16                       PIDOF(1)

------------------------------------------------------------------------

Pages that refer to this page: [killall(1)](../man1/killall.1.html),  [lsfd(1)](../man1/lsfd.1.html),  [unshare(1)](../man1/unshare.1.html)

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
