---
{"title": "raid6check(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/raid6check.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# raid6check(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RAID6CHECK(8)            System Manager's Manual            RAID6CHECK(8)

## [](#NAME)NAME

           raid6check - check MD RAID6 device for errors aka Linux Software
           RAID

## [](#SYNOPSIS)SYNOPSIS

           raid6check <raid6_device> <start_stripe> <number_of_stripes>
           [autorepair]

           raid6check <raid6_device> repair <stripe> <failed_slot_1>
           <failed_slot_2>

## [](#DESCRIPTION)DESCRIPTION

           RAID6 devices in which one single component drive has errors can
           use the double parity in order to find out which component drive.
           The "raid6check" tool has two modes: check mode and repair mode.

           "raid6check" requires a non-degraded RAID6 MD device as first
           parameter. If the given MD device is not a RAID6, "raid6check"
           will, of course, not continue.

           If the RAID6 MD device is degraded, "raid6check" will report an
           error and it will not proceed further.

       Check mode
           In the check mode, the "raid6check" tool checks, for each stripe,
           the double parity consistency, reports mismatches and, if
           possible, which component drive has the mismatch.  Since it works
           at stripe level, it can report different drives with mismatches at
           different stripes.

           In addition to the MD device, "raid6check" requries a starting
           stripe (usually 0) and the number of stripes to be checked.  If
           this third parameter is also 0, it will check the array up to the
           end.  If the fourth parameter is "autorepair", it will overwrite
           single-slot errors.

           "raid6check" will start printing information about the RAID6, then
           for each stripe, it will report the parity rotation status.  In
           case of parity mismatches, "raid6check" reports, if possible,
           which component drive could be responsible.  Otherwise it reports
           that it is not possible to find the component drive.

           No write operations are performed on the array or the components,
           unless "autorepair" is specified.  Furthermore, the checked array
           can be online and in use during the operation of "raid6check".

       Repair mode
           In the repair mode, the "raid6check" tool checks the given stripe.
           If inconsistencies are found, it attempts to repair the strip
           assuming that the two given slots are incorrect.

           -1 may be used to specify parity P and -2 parity Q.

## [](#EXAMPLES)EXAMPLES

             raid6check /dev/md0 0 0
           This will check /dev/md0 from start to end.

             raid6check /dev/md3 0 1 autorepair
           This will check the first stripe of /dev/md3.  Any error will be
           reported, and if single-slot, repaired.

             raid6check /dev/md3 0 repair 1 -1 -2
           This will check the first stripe of /dev/md3.  If any
           inconsistencies are found, repair is performed assuming the two
           parities are incorrect.

             raid6check /dev/md1 1000 0
           This will check /dev/md1 from stripe 1000 up to the end.

             raid6check /dev/m127 128 256
           This will check 256 stripes of /dev/md127 starting from stripe
           128.

             raid6check /dev/md0 0 0 | grep -i error > md0_err.log
           This will check /dev/md0 completely and create a log file only
           with errors, if any.

## [](#FILES)FILES

           "raid6check" uses directly the component drives as found in /dev.
           Furthermore, the sysfs interface is needed in order to find out
           the RAID6 parameters.

## [](#BUGS)BUGS

           Negative stripe parameters can lead to unexpected results due to
           strtoull.  (Negative slot numbers should work for Q [-1] and P
           [-2] but currently involve compiler-defined behavior.)

           It is not clear what will happen if the RAID6 MD device gets
           degraded during the check.

           The latest version of raid6check should always be available from

                  https://www.kernel.org/pub/linux/utils/raid/mdadm/ 

           Related man pages:

           mdadm(8) mdmon(8), mdadm.conf(5), md(4).

## [](#COLOPHON)COLOPHON

           This page is part of the mdadm (Tool for managing md arrays in
           Linux) project.  Information about the project can be found at 
           ⟨http://neil.brown.name/blog/mdadm⟩.  If you have a bug report for
           this manual page, send it to linux-raid@vger.kernl.org.  This page
           was obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/utils/mdadm/mdadm.git/⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-22.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    v1.0.0                                                      RAID6CHECK(8)

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
