---
{"title": "systemd.v(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/systemd.v.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.v(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILTERING AND SORTING](#FILTERING_AND_SORTING) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD.V(7)                    systemd.v                    SYSTEMD.V(7)

## [](#NAME)NAME

           systemd.v - Directory with Versioned Resources

## [](#DESCRIPTION)DESCRIPTION

           In various places systemd components accept paths whose trailing
           components have the ".v/" suffix, pointing to a directory. These
           components will then automatically look for suitable files inside
           the directory, do a version comparison and open the newest file
           found (by version). Available since version v256. Specifically,
           two expressions are supported:

           •   When looking for files with a suffix .SUFFIX, and a path
               ...PATH/NAME.SUFFIX.v/ is specified, then all files
               ...PATH/NAME.SUFFIX.v/NAME_*.SUFFIX are enumerated, filtered,
               sorted and the newest file used. The primary sorting key is
               the variable part, here indicated by the wildcard "*".

           •   When a path ...PATH.v/NAME___.SUFFIX is specified (i.e. the
               penultimate component of the path ends in ".v" and the final
               component contains a triple underscore), then all files
               ...PATH.v/NAME_*.SUFFIX are enumerated, filtered, sorted and
               the newest file used (again, by the variable part, here
               indicated by the wildcard "*").

           To illustrate this in an example, consider a directory
           /var/lib/machines/mymachine.raw.v/, which is populated with three
           files:

           •   mymachine_7.5.13.raw

           •   mymachine_7.5.14.raw

           •   mymachine_7.6.0.raw

           Invoke a tool such as systemd-nspawn(1) with a command line like
           the following:

               # systemd-nspawn --image=/var/lib/machines/mymachine.raw.v --boot

           Then this would automatically be resolved to the equivalent of:

               # systemd-nspawn --image=/var/lib/machines/mymachine.raw.v/mymachine_7.6.0.raw --boot

           Much of systemd's functionality that expects a path to a disk
           image or OS directory hierarchy support the ".v/" versioned
           directory mechanism, for example systemd-nspawn(1),
           systemd-dissect(1) or the RootDirectory=/RootImage= settings of
           service files (see systemd.exec(5)).

           Use the systemd-vpick(1) tool to resolve ".v/" paths from the
           command line, for example for usage in shell scripts.

## [](#FILTERING_AND_SORTING)FILTERING AND SORTING

           The variable part of the filenames in the ".v/" directories are
           filtered and compared primarily with a version comparison,
           implementing UAPI.10 Version Format Specification[1]. However,
           additional rules apply:

           •   If the variable part is suffixed by one or two integer values
               ("tries left" and "tries done") in the formats +LEFT or
               +LEFT-DONE, then these indicate usage attempt counters. The
               idea is that each time before a file is attempted to be used,
               its "tries left" counter is decreased, and the "tries done"
               counter increased (simply by renaming the file). When the file
               is successfully used (which for example could mean for an OS
               image: successfully booted) the counters are removed from the
               file name, indicating that the file has been validated to work
               correctly. This mechanism mirrors the boot assessment counters
               defined by Automatic Boot Assessment[2]. Any filenames with no
               boot counters or with a non-zero "tries left" counter are
               sorted before filenames with a zero "tries left" counter.

           •   Preceding the use counters (if they are specified), an
               optional CPU architecture identifier may be specified in the
               filename (separated from the version with an underscore), as
               defined in the architecture vocabulary of the
               ConditionArchitecture= unit file setting, as documented in
               systemd.unit(5). Files whose name indicates an architecture
               not supported locally are filtered and not considered for the
               version comparison.

           •   The rest of the variable part is the version string.

           Or in other words, the files in the ".v/" directories should
           follow one of these naming structures:

           •   NAME_VERSION.SUFFIX

           •   NAME_VERSION_ARCHITECTURE.SUFFIX

           •   NAME_VERSION+LEFT.SUFFIX

           •   NAME_VERSION+LEFT-DONE.SUFFIX

           •   NAME_VERSION_ARCHITECTURE+LEFT.SUFFIX

           •   NAME_VERSION_ARCHITECTURE+LEFT-DONE.SUFFIX

## [](#EXAMPLE)EXAMPLE

           Here's a more comprehensive example, further extending the one
           described above. Consider a directory
           /var/lib/machines/mymachine.raw.v/, which is populated with the
           following files:

           •   mymachine_7.5.13.raw

           •   mymachine_7.5.14_x86-64.raw

           •   mymachine_7.6.0_arm64.raw

           •   mymachine_7.7.0_x86-64+0-5.raw

           Now invoke the following command on an x86-64 machine:

               $ systemd-vpick --suffix=.raw /var/lib/machines/mymachine.raw.v/

           This would resolve the specified path to
           /var/lib/machines/mymachine.raw.v/mymachine_7.5.14_x86-64.raw.
           Explanation: even though mymachine_7.7.0_x86-64+0-5.raw has the
           newest version, it is not preferred because its tries left counter
           is zero. And even though mymachine_7.6.0_arm64.raw has the second
           newest version it is also not considered in this case, because we
           operate on an x86_64 system and the image is intended for arm64
           CPUs. Finally, the mymachine_7.5.13.raw image is not considered
           because it is older than mymachine_7.5.14_x86-64.raw.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-vpick(1), systemd-nspawn(1),
           systemd-dissect(1), systemd.exec(5), systemd-sysupdate(8)

## [](#NOTES)NOTES

            1. UAPI.10 Version Format Specification
               https://uapi-group.org/specifications/specs/version_format_specification/

            2. Automatic Boot Assessment
               https://systemd.io/AUTOMATIC_BOOT_ASSESSMENT/

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                            SYSTEMD.V(7)

------------------------------------------------------------------------

Pages that refer to this page: [bootctl(1)](../man1/bootctl.1.html),  [portablectl(1)](../man1/portablectl.1.html),  [systemd-dissect(1)](../man1/systemd-dissect.1.html),  [systemd-mstack(1)](../man1/systemd-mstack.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [systemd-vpick(1)](../man1/systemd-vpick.1.html),  [org.freedesktop.portable1(5)](../man5/org.freedesktop.portable1.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.mstack(7)](../man7/systemd.mstack.7.html)

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
