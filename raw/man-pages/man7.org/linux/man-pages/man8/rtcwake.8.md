---
{"title": "rtcwake(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/rtcwake.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rtcwake(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [FILES](#FILES) \| [HISTORY](#HISTORY) \| [AUTHORS](#AUTHORS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RTCWAKE(8)                System Administration                RTCWAKE(8)

## [](#NAME)NAME

           rtcwake - enter a system sleep state until specified wakeup time

## [](#SYNOPSIS)SYNOPSIS

           rtcwake [options] [-d device] [-m standby_mode] {-s seconds|-t
           time_t}

## [](#DESCRIPTION)DESCRIPTION

           This program is used to enter a system sleep state and to
           automatically wake from it at a specified time.

           This uses cross-platform Linux interfaces to enter a system sleep
           state, and leave it no later than a specified time. It uses any
           RTC framework driver that supports standard driver model wakeup
           flags.

           This is normally used like the old apmsleep utility, to wake from
           a suspend state like ACPI S1 (standby) or S3 (suspend-to-RAM).
           Most platforms can implement those without analogues of BIOS, APM,
           or ACPI.

           On some systems, this can also be used like nvram-wakeup, waking
           from states like ACPI S4 (suspend to disk). Not all systems have
           persistent media that are appropriate for such suspend modes.

           Note that alarm functionality depends on hardware; not every RTC
           is able to set up an alarm up to 24 hours in the future.

           The suspend setup may be interrupted by active hardware; for
           example wireless USB input devices that continue to send events
           for some fraction of a second after the return key is pressed.
           rtcwake tries to avoid this problem and it waits to the terminal
           to settle down before entering a system sleep.

## [](#OPTIONS)OPTIONS

           -A, --adjfile file
               Specify an alternative path to the adjust file.

           -a, --auto
               Read the clock mode (whether the hardware clock is set to UTC
               or local time) from the adjtime file, where hwclock(8) stores
               that information. This is the default.

           --date timestamp
               Set the wakeup time to the value of this timestamp. The format
               of timestamp can be any of the following:

                    YYYYMMDDhhmmss
                    "YYYY-MM-DD hh:mm:ss"
                    "YYYY-MM-DD hh:mm"      (seconds is 00)
                    YYYY-MM-DD              (time is 00:00:00)
                    hh:mm:ss                (date is today)
                    hh:mm                   (date is today, seconds is 00)
                    +number[smhd]           (seconds/minutes/hours/days after now)
                    tomorrow                (time is 00:00:00)

               Examples of the +number[smhd] format are: +5m, +6h, +2d. The
               unit specifier may be longer: +5min, +6hours, +2days.

           -d, --device device
               Use the specified device instead of rtc0 as real-time clock.
               This option is only relevant if your system has more than one
               RTC. You may specify rtc1, rtc2, ... here.

           -l, --local
               Assume that the hardware clock is set to local time,
               regardless of the contents of the adjtime file.

           --list-modes
               List available --mode option arguments.

           -m, --mode mode
               Go into the given standby state. Valid values for mode are:

               standby
                   ACPI state S1. This state offers minimal, though real,
                   power savings, while providing a very low-latency
                   transition back to a working system. This is the default
                   mode.

               freeze
                   The processes are frozen, all the devices are suspended
                   and all the processors idled. This state is a general
                   state that does not need any platform-specific support,
                   but it saves less power than Suspend-to-RAM, because the
                   system is still in a running state. (Available since Linux
                   3.9.)

               mem
                   ACPI state S3 (Suspend-to-RAM). This state offers
                   significant power savings as everything in the system is
                   put into a low-power state, except for memory, which is
                   placed in self-refresh mode to retain its contents.

               disk
                   ACPI state S4 (Suspend-to-disk). This state offers the
                   greatest power savings, and can be used even in the
                   absence of low-level platform support for power
                   management. This state operates similarly to
                   Suspend-to-RAM, but includes a final step of writing
                   memory contents to disk.

               off
                   ACPI state S5 (Poweroff). This is done by calling
                   '/sbin/shutdown'. Not officially supported by ACPI, but it
                   usually works.

               no
                   Don’t suspend, only set the RTC wakeup time.

               on
                   Don’t suspend, but read the RTC device until an alarm time
                   appears. This mode is useful for debugging.

               disable
                   Disable a previously set alarm.

               show
                   Print alarm information in format: "alarm: off|on <time>".
                   The time is in ctime(3) output format, e.g., "alarm: on
                   Tue Nov 16 04:48:45 2010".

           -n, --dry-run
               This option does everything apart from actually setting up the
               alarm, suspending the system, or waiting for the alarm.

           -s, --seconds seconds
               Set the wakeup time to seconds in the future from now.

           -t, --time time_t
               Set the wakeup time to the absolute time time_t. time_t is the
               time in seconds since 1970-01-01, 00:00 UTC. Use the date(1)
               tool to convert between human-readable time and time_t.

           -u, --utc
               Assume that the hardware clock is set to UTC (Universal Time
               Coordinated), regardless of the contents of the adjtime file.

           -v, --verbose
               Be verbose.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#NOTES)NOTES

           Some PC systems can’t currently exit sleep states such as mem
           using only the kernel code accessed by this driver. They need help
           from userspace code to make the framebuffer work again.

## [](#FILES)FILES

           /etc/adjtime

## [](#HISTORY)HISTORY

           The program was posted several times on LKML and other lists
           before appearing in kernel commit message for Linux 2.6 in the GIT
           commit 87ac84f42a7a580d0dd72ae31d6a5eb4bfe04c6d.

## [](#AUTHORS)AUTHORS

           The program was written by David Brownell
           <dbrownell@users.sourceforge.net> and improved by Bernhard Walle
           <bwalle@suse.de>.

## [](#COPYRIGHT)COPYRIGHT

           This is free software. You may redistribute copies of it under the
           terms of the GNU General Public License
           <http://www.gnu.org/licenses/gpl.html>. There is NO WARRANTY, to
           the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           adjtime_config(5), hwclock(8), date(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The rtcwake command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                     RTCWAKE(8)

------------------------------------------------------------------------

Pages that refer to this page: [adjtime_config(5)](../man5/adjtime_config.5.html),  [hwclock(8)](../man8/hwclock.8.html)

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
