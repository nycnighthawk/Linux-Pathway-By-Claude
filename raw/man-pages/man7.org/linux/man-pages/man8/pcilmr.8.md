---
{"title": "pcilmr(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pcilmr.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pcilmr(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [CONFIGURATION](#CONFIGURATION) \| [DESCRIPTION](#DESCRIPTION) \| [RESULTS GRADING](#RESULTS_GRADING) \| [HARDWARE QUIRKS SUPPORT](#HARDWARE_QUIRKS_SUPPORT) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PCILMR(8)                   The PCI Utilities                   PCILMR(8)

## [](#NAME)NAME

           pcilmr - margin PCIe Links

## [](#SYNOPSIS)SYNOPSIS

           pcilmr [--margin] [<common options>] <link port> [<link options>]
           [<link port> [<link options>] ...]
           pcilmr --full [<common options>]
           pcilmr --scan

## [](#CONFIGURATION)CONFIGURATION

           List of the requirements for links and system settings to run the
           margining test.

           BIOS settings (depends on the system, relevant for server
           baseboards with Xeon CPUs):

           •  Turn off PCIe Leaky Bucket Feature, Re-Equalization and Link
              Degradation;

           •  Set Error Thresholds to 0;

           •  Intel VMD for NVMe SSDs – in case of strange behavior of the
              pcilmr, try to run it with the VMD turned off.

           Device (link) requirements:

                  Configured by the user before running the utility, the
                  utility does not change them:

                  •  The current Link data rate must be 16.0 GT/s or higher
                     (right now utility supports 16 GT/s and 32 GT/s Links);

                  •  Link Downstream Component must be at D0 Power Management
                     State.

                  Configured by the utility during operation, utility set
                  them to their original state after receiving the results:

                  •  The ASPM must be disabled in both the Downstream Port
                     and Upstream Port;

                  •  The Hardware Autonomous Speed Disable bit of the Link
                     Control 2 register must be Set in both the Downstream
                     Port and Upstream Port;

                  •  The Hardware Autonomous Width Disable bit of the Link
                     Control register must be Set in both the Downstream Port
                     and Upstream Port.

## [](#DESCRIPTION)DESCRIPTION

           pcilmr utility allows you to take advantage of the PCIe Lane
           Margining at the Receiver capability which is mandatory for all
           Ports supporting a data rate of 16.0 GT/s or higher, including
           Pseudo Ports (Retimers). Lane Margining at Receiver enables system
           software to obtain the margin information of a given Receiver
           while the Link is in the L0 state. The margin information includes
           both voltage and time, in either direction from the current
           Receiver position. Margining support for timing is required, while
           support for voltage is optional at 16.0 GT/s and required at 32.0
           GT/s and higher data rates. Also, independent time margining and
           independent voltage margining is optional.

           Utility allows to get an approximation of the eye margin diagram
           in the form of a rhombus (by four points). Lane Margining at the
           Receiver capability enables users to margin PCIe links without a
           hardware debugger and without the need to stop the target system.
           Utility can be useful to debug link issues due to receiver
           margins.

           pcilmr requires root privileges (to access Extended Configuration
           Space), but during our testing there were no problems with the
           devices and they successfully returned to their normal initial
           state after the end of testing.

## [](#RESULTS_GRADING)RESULTS GRADING

           The PCIe specification provides reference values for the eye
           diagram, which are also used by the pcilmr to evaluate the
           results, but it seems that it makes sense to contact the
           manufacturer of a particular device for references.

           The utility uses values set in PCIe Base Spec Rev. 5.0 Section
           8.4.2 as the default eye width and height minimum references.
           Recommended values were taken from the PCIe Architecture PHY Test
           Spec Rev 5.0 (Transmitter Electrical Compliance).

           Reference grading values currently used by the utility are
           presented in the table below:

           ┌─────┬─────────────────────┬──────────────────────┐
           │     │  16 GT/s │(Gen 4)    │   32 GT/s │(Gen 5)    │
           │     │    EW    │   EH     │   EW      │   EH     │
           ├─────┼──────────┼──────────┼───────────┼──────────┤
           │ Min │ 18.75 ps │  15 mV   │ 9.375 ps  │  15 mV   │
           │     │ 30% UI   │          │ 30% UI    │          │
           ├─────┼──────────┼──────────┼───────────┼──────────┤
           │ Rec │ 23.75 ps │  21 mV   │10.157 ps  │19.75 mV  │
           │     │ 38% UI   │          │33% UI     │          │
           └─────┴──────────┴──────────┴───────────┴──────────┘

           pcilmr uses full eye width and height values to grade lanes.
           However, it is possible that device supports only one side
           margining. In such cases by default utility will calculate EW or
           EH as a double one side result.

           If info for specific device is available, you can configure
           grading criteria and tweak utility behavior in one-side only cases
           for your device using -g link specific option (see below).

## [](#HARDWARE_QUIRKS_SUPPORT)HARDWARE QUIRKS SUPPORT

           Thanks to testing or directly from the manufacturer's
           documentation, we know that some devices require special treatment
           during the margining.  Utility detects such devices based on their
           Vendor ID – Device ID pair.  Right now the list of special devices
           is hardcoded in margin_hw file. For such devices utility can
           automatically adjust port margining parameters or grading options.

           For example, for Ice Lake CPUs RC ports pcilmr will change device
           MaxVoltageOffset value and will force the use of 'one side is the
           whole' grading mode.

## [](#OPTIONS)OPTIONS

       Device Specifier
           You can specify Downstream or Upstream Port of the Link.

           <device/component>
                  [<domain>:]<bus>:<dev>.<func> (see lspci(8))

       Utility Modes
           --margin <downstream component> ...
                  Margin selected Links.

           --full Margin all ready for testing (in a meaning similar to the
                  --scan option) Links in the system (one by one).

           --scan Scan for Links with negotiated speed 16 GT/s or higher.
                  Mark "Ready" those of them in which at least one of the
                  Link sides have Margining Ready bit set meaning that these
                  Links are ready for testing and you can run utility on
                  them.

       Margining Common (for all specified links) options
           -c Print Device Lane Margining Capabilities only. Do not run
           margining.

           -e <errors>
                  Specify Error Count Limit for margining.
                  Default: 4.

           -o <directory>
                  Save margining results in csv form into the specified
                  directory. Utility will generate file with the name in form
                  of "lmr_<port>_Rx#_<timestamp>.csv" for each successfully
                  tested receiver.

           -d <time>
                  Specify dwell time in seconds for the margining step.
                  Default: 1 s

       Margining Link specific options
           -l <lane>[,<lane>...]
                  ®.br Remember that Device may use Lane Reversal for Lane
                  numbering. However, utility uses logical lane numbers in
                  arguments and for logging. Utility will automatically
                  determine Lane Reversal and tune its calls.
                  Default: all link lanes.

           -r <recvn>[,<recvn>...]
                  Specify Receivers to select margining targets.
                  Default: all available Receivers (including Retimers).

           -p <parallel_lanes>
                  Specify number of lanes to margin simultaneously.
                  According to spec it's possible for Receiver to margin up
                  to MaxLanes + 1 lanes simultaneously, but during testing,
                  performing margining on several lanes simultaneously led to
                  results that were different from sequential margining, so
                  this feature requires additional verification and -p option
                  right now is for experiments mostly.
                  Default: 1.

           Use only one of -T/-t options at the same time (same for -V/-v).
           Without these options utility will use MaxSteps from Device
           capabilities as test limit.

           -T     Time Margining will continue until the Error Count is no
                  more than an Error Count Limit. Use this option to find
                  Link limit.

           -t <steps>
                  Specify maximum number of steps for Time Margining.

           -V     Same as -T option, but for Voltage.

           -v <steps>
                  Specify maximum number of steps for Voltage Margining.

           -g <recvn>t=<criteria>{%|ps}[,f]

              <recvn>t=f[,<criteria>{%|ps}]

              <recvn>v=<criteria>[,f]

              <recvn>v=f[,<criteria>]
                  Specify pass/fail grading criteria for eye width (timing
                  -t) or height (voltage -v) for one of the link receivers.
                  For EW you must choose one of the units (% UI or ps), for
                  EH mV is used.
                  Additional flag f is for situations when port doesn't
                  support two side independent margining. In such cases by
                  default utility will calculate EW or EH as a double one
                  side result. You can add f flag for -g option to tell the
                  utility that the result in one direction is actually the
                  measurement of the full eye and it does not need to be
                  multiplied. This is so called 'one side is the whole'
                  grading mode.

## [](#EXAMPLES)EXAMPLES

           Utility syntax example:
                  pcilmr -o csv ab:0.0 -r 1,6 -g 1t=20% -g 1v=f,30 52:0.0 -l
                  0,1,2 -TV

           Examples of collected results on different systems.  
           ⟨https://gist.github.com/bombanya/f2b15263712757ffba1a11eea011c419⟩

## [](#SEE_ALSO)SEE ALSO

           lspci(8), PCI Express Base Specification (Lane Margining at
           Receiver)

## [](#COLOPHON)COLOPHON

           This page is part of the pciutils (PCI utilities) project.  Infor‐
           mation about the project can be found at 
           ⟨http://mj.ucw.cz/sw/pciutils/⟩.  If you have a bug report for this
           manual page, send it to linux-pci@vger.kernel.org.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/pciutils/pciutils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-08.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    pciutils-3.15.0                 2026-04-05                      PCILMR(8)

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
