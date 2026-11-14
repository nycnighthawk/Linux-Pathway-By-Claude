---
{"title": "trace-cmd-attach(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/trace-cmd-attach.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# trace-cmd-attach(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [RESOURCES](#RESOURCES) \| [COPYING](#COPYING) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    TRACE-CMD-ATTACH(1)         libtracefs Manual         TRACE-CMD-ATTACH(1)

## [](#NAME)NAME

           trace-cmd-attach - attach a guest trace.dat file to a host
           trace.dat file

## [](#SYNOPSIS)SYNOPSIS

           trace-cmd attach [OPTIONS] host-trace-file guest-trace-file
           guest-pid [guest-pid ...]

## [](#DESCRIPTION)DESCRIPTION

           The trace-cmd(1) attach is used to take a trace.dat file created
           on a guest and attach it to a trace.dat file that was created on
           the host. In most cases, trace-cmd-agent(1) can be used to
           automate this, but if for some reason, the agent isn’t
           appropriate, it may be required to start trace-cmd recording on
           the guest with trace-cmd-record(1). If the host recording is
           activated at the same time, one can use trace-cmd attach(1) to
           connect the guest and host files as if they were created by the
           trace-cmd agent.

           host-trace-file
               The trace.dat file created by the host. Must have kvm_exit and
               kvm_entry events, and use the "tsc2nsec" clock.

           guest-trace-file
               The trace.dat file created by the guest. Must use the
               "x86-tsc" clock. For now, this is only supported on x86, it
               may support other achitectures later.

           guest-pid
               The process ID of the host thread that represents the guests
               threads. Each process ID that represents all of the guest
               vCPUs should be listed. Note, you can add more than just the
               threads that represent the guest vCPUs, as the tool will
               search the host-trace-file for kvm_exit and kvm_entry events
               to match these PIDs with the vCPUs that they represent.

## [](#OPTIONS)OPTIONS

           -c cpus
               Specify a the number of CPUS the guest has.

           -s timeshift
               A comma separated list of the format
               offset,scale,frac,timestamp These values map to what are given
               in /sys/kernel/kvm/<pid>/vcpu/*

                   *offset*: Is the offset of the guest. "tsc-offest" in the directory. Note
                             that the value listed here is the negative of what is listed in
                             the directory.

                   *scale*:  The scaling factor. "tsc-scaling-ratio"

                   *frac*:   The fraction bits. "tsc-scaling-ratio-frac-bits"

                   *timestamp*: The timestamp to start using the above. In some cases, the
                             values may change over time. By adding a timestamp, it will
                             take effect after the timestamp has been hit. Normally
                             this would be zero.

                   Currently, only one timeshift is given per CPU. One *-s* option should be
                   given for each CPU. If there are less options than CPUs, then the last option
                   given will be used for the rest of the CPUs. If only one option is given, then
                   the values for that option will be used for all CPUs.

## [](#EXAMPLES)EXAMPLES

           Enable all events for tracing:

                 $ # find the process for a given guest
                 $ ps aux |grep qemu
                libvirt+   63170  5.6  1.6 13994848 4257540 ?    Sl   May02 2884:49 /usr/bin/qemu-system-x86_64...

                 $ # Use 63170 to find all the PIDs for the give guest
                 $ ls /proc/63170/task
                1541591  63170  63198  63209  63211  63213  63214  63215  63216  63217  63218  63219  63234

                 $ # Find the tsc offset
                 $ su
                 # cat /sys/kernel/debug/kvm/63170-15/vcpu0/tsc-offset
                -27950965013436847

                 # trace-cmd record -C tsc2nsec -e kvm -e sched -e irq -e timer

               # on guest:

                 # trace-cmd record -C x86-tsc -e sched -e irq -e timer sleep 10

               # back on host, hit Ctrl^C to stop tracing after the guest is done

                 # # Make the trace.dat user owned by your user account.
                 # chown user.user trace.dat
                 # exit

                 $ scp root@guest:trace.dat trace-guest.dat

                 $ # now attach the two files (guest has 8 CPUs)
                 $ trace-cmd attach -c 8 -s 27950965013436847 trace.dat trace-guest.dat 1541591  63170  63198  63209  63211  63213  63214  63215  63216  63217  63218  63219  63234

                 $ trace-cmd report -i trace.dat -i trace-guest.dat
                 $ # now you should see the guest trace interleaved within the host trace.

## [](#SEE_ALSO)SEE ALSO

           trace-cmd(1), trace-cmd-report(1), trace-cmd-start(1),
           trace-cmd-stop(1), trace-cmd-extract(1), trace-cmd-reset(1),
           trace-cmd-split(1), trace-cmd-list(1), trace-cmd-listen(1),
           trace-cmd-profile(1)

## [](#AUTHOR)AUTHOR

           Written by Steven Rostedt (Google) <rostedt@goodmis.org[1]>

## [](#RESOURCES)RESOURCES

           https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/ 

## [](#COPYING)COPYING

           Copyright (C) 2010 Red Hat, Inc. Free use of this software is
           granted under the terms of the GNU Public License (GPL).

## [](#NOTES)NOTES

            1. rostedt@goodmis.org
               mailto:rostedt@goodmis.org

## [](#COLOPHON)COLOPHON

           This page is part of the trace-cmd (a front-end for Ftrace)
           project.  Information about the project can be found at 
           ⟨https://www.trace-cmd.org/⟩.  If you have a bug report for this
           manual page, see ⟨https://www.trace-cmd.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-05-29.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    libtracefs                      08/09/2025            TRACE-CMD-ATTACH(1)

------------------------------------------------------------------------

Pages that refer to this page: [trace-cmd(1)](../man1/trace-cmd.1.html)

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
