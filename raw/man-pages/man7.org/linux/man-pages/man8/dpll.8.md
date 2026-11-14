---
{"title": "dpll(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dpll.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpll(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [DEVICE COMMANDS](#DEVICE_COMMANDS) \| [PIN COMMANDS](#PIN_COMMANDS) \| [MONITOR COMMAND](#MONITOR_COMMAND) \| [EXAMPLES](#EXAMPLES) \| [PHASE ADJUSTMENT](#PHASE_ADJUSTMENT) \| [CAPABILITIES](#CAPABILITIES) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DPLL(8)                           Linux                           DPLL(8)

## [](#NAME)NAME

           dpll - Digital Phase Locked Loop (DPLL) subsystem management

## [](#SYNOPSIS)SYNOPSIS

           dpll [ OPTIONS ] device { COMMAND | help }

           dpll [ OPTIONS ] pin { COMMAND | help }

           dpll [ OPTIONS ] monitor

           OPTIONS := { -V | --Version | -j | --json | -p | --pretty | -t |
                   --timestamp | --tshort }

## [](#DESCRIPTION)DESCRIPTION

           The dpll utility is used to configure and monitor Digital Phase
           Locked Loop (DPLL) devices and pins. DPLLs are used for clock
           synchronization in various hardware, particularly in
           telecommunications and networking equipment.

           A DPLL device can lock to one or more input pins and provide
           synchronized output. Pins can be physical external signals (like
           GNSS 1PPS, SyncE), or internal oscillators.

## [](#OPTIONS)OPTIONS

           -V, --Version
                  Print the version of the dpll utility and exit.

           -j, --json
                  Output results in JavaScript Object Notation (JSON).

           -p, --pretty
                  When combined with -j, generates a pretty JSON output with
                  indentation and newlines for better human readability.

           -t, --timestamp
                  When used with the monitor object, print a Timestamp: line
                  before each received notification, in the same format used
                  by ip monitor.

           --tshort
                  Like -t, but emits a more compact, ISO 8601 inline prefix
                  “[YYYY-MM-DDTHH:MM:SS.uuuuuu]” in front of each
                  notification instead of a separate Timestamp: line.

## [](#DEVICE_COMMANDS)DEVICE COMMANDS

       dpll device show [ id ID ] [ module-name NAME ] [ clock-id ID ] [ type
           TYPE ] [ mode MODE ] [ lock-status STATUS ]
           Display information about DPLL devices. If no arguments are
           specified, shows all devices in the system.

           id ID  Show only the device with the specified numeric identifier.

           module-name NAME
                  Show only devices provided by the specified kernel module.

           clock-id ID
                  Show only devices with the specified 64-bit clock
                  identifier.

           type TYPE
                  Show only devices of the specified type: pps or eec.

           mode MODE
                  Show only devices in the specified operating mode: manual
                  or automatic.

           lock-status STATUS
                  Show only devices with the specified lock status: unlocked,
                  locked, locked-ho-acq, holdover.

           Output includes:

                  • Device ID

                  • Module name providing the device

                  • Clock ID (unique identifier)

                  • Operating mode (manual, automatic)

                  • Lock status (unlocked, locked, locked-ho-acq, holdover)

                  • Lock status error (if present)

                  • Clock quality level (if supported)

                  • Temperature (if supported)

                  • Type (PPS or EEC)

                  • Supported modes

                  • Phase offset monitor status (enable/disable)

                  • Phase offset averaging factor

                  • Frequency monitor status (enable/disable)

       dpll device set id ID [ PARAMETER VALUE ] ...
           Configure DPLL device parameters.

           id ID  Specifies which device to configure (required).

           mode { automatic | manual }
                  Set the operating mode of the DPLL device.  In automatic
                  mode, the DPLL autonomously selects the best available
                  input source based on priority and quality. In manual mode,
                  the input source must be explicitly configured and the DPLL
                  will not automatically switch sources.

           phase-offset-monitor { enable | disable }
                  Enable or disable phase offset monitoring between the
                  device and its pins.  When enabled, the kernel continuously
                  measures and reports phase differences.

           phase-offset-avg-factor FACTOR
                  Set the averaging factor (1-255) applied to phase offset
                  calculations.  Higher values provide smoother but slower-
                  responding measurements.

           frequency-monitor { enable | disable }
                  Enable or disable frequency monitoring on the device. When
                  enabled, the kernel continuously measures and reports
                  actual pin frequencies, which can be read via the measured-
                  frequency field in pin show output.

       dpll device id-get [ module-name NAME ] [ clock-id ID ] [ type TYPE ]
           Retrieve the device ID based on identifying attributes. Useful for
           scripting when you need to find a device's numeric ID. At least
           one attribute should be specified to identify the device.

           module-name NAME
                  Kernel module name.

           clock-id ID
                  64-bit clock identifier in decimal or hex (0x prefix).

           type TYPE
                  Device type: pps or eec.

## [](#PIN_COMMANDS)PIN COMMANDS

       dpll pin show [ id ID ] [ parent-device DEVICE_ID ] [ parent-pin
           PIN_ID ] [ module-name NAME ] [ clock-id ID ] [ board-label LABEL
           ] [ panel-label LABEL ] [ package-label LABEL ] [ type TYPE ] [
           direction DIR ] [ state STATE ] [ operstate OPERSTATE ]
           Display information about DPLL pins. If no arguments are
           specified, shows all pins in the system.

           id ID  Show only the pin with the specified numeric identifier.

           parent-device DEVICE_ID
                  Show only pins that have the specified DPLL device as a
                  parent.

           parent-pin PIN_ID
                  Show only pins that have the specified pin as a parent (mux
                  pins).

           module-name NAME
                  Show only pins provided by the specified kernel module.

           clock-id ID
                  Show only pins with the specified 64-bit clock identifier.

           board-label LABEL
                  Show only pins with the specified board label.

           panel-label LABEL
                  Show only pins with the specified panel label.

           package-label LABEL
                  Show only pins with the specified package label.

           type TYPE
                  Show only pins of the specified type: mux, ext, synce-eth-
                  port, int-oscillator, gnss.

           direction DIR
                  Show only pins that have a parent-device relationship with
                  the specified direction: input, output.  When combined with
                  parent-device, only the specified parent-device
                  relationship is checked.

           state STATE
                  Show only pins that have a parent-device relationship with
                  the specified state: connected, disconnected, selectable.
                  When combined with parent-device, only the specified
                  parent-device relationship is checked.

           operstate OPERSTATE
                  Show only pins that have a parent-device relationship with
                  the specified operational state: active, standby, no-
                  signal, qual-failed.  When combined with parent-device,
                  only the specified parent-device relationship is checked.

           Output includes:

                  • Pin ID

                  • Module name

                  • Clock ID

                  • Board label (hardware label from device tree or ACPI)

                  • Panel label

                  • Package label

                  • Pin type (mux, ext, synce-eth-port, int-oscillator, gnss)

                  • Configured frequency and supported frequency ranges

                  • Measured frequency in Hz (when frequency monitoring is
                    enabled)

                  • Capabilities (state-can-change, priority-can-change,
                    direction-can-change)

                  • Phase adjustment range, granularity, and current value

                  • Fractional frequency offset

                  • Parent device relationships (direction, priority, state,
                    phase offset)

                  • Parent pin relationships

                  • Reference sync information

                  • Esync frequency and pulse support (if applicable)

       dpll pin set id ID [ PARAMETER VALUE ] ...
           Configure DPLL pin parameters. Multiple parameters can be
           specified in a single command.

           id ID  Specifies which pin to configure (required).

           frequency FREQ
                  Set pin frequency in Hz. The pin must support the specified
                  frequency (check frequency-supported ranges in pin show
                  output).

           phase-adjust ADJUSTMENT
                  Set phase adjustment in picoseconds. This value fine-tunes
                  the phase of the output signal. Negative values shift the
                  phase backwards, positive values shift it forwards. The
                  value must be within the phase-adjust-min and phase-adjust-
                  max range.

           esync-frequency FREQUENCY
                  Set enhanced SyncE (Synchronous Ethernet) frequency in Hz
                  for capable pins.

           parent-device DEVICE_ID [ direction DIR ] [ prio PRIO ] [ state
           STATE ]
                  Configure the relationship between this pin and a parent
                  DPLL device.

                  direction { input | output }
                         Set the pin's direction relative to the parent
                         device.

                  prio PRIORITY
                         Set priority (0-255) for this pin on the parent
                         device.

                  state { connected | disconnected | selectable }
                         Set the pin's state on the parent device.

           parent-pin PIN_ID [ state STATE ]
                  Configure the relationship to a parent pin.

           reference-sync PIN_ID [ state STATE ]
                  Configure reference sync relationship with another pin.

       dpll pin id-get [ SELECTOR ] ...
           Retrieve a pin ID based on identifying attributes.

           module-name NAME
                  Filter by kernel module name.

           clock-id ID
                  Filter by 64-bit clock identifier.

           board-label LABEL
                  Filter by board label (hardware identifier).

           panel-label LABEL
                  Filter by panel label.

           package-label LABEL
                  Filter by package label.

           type TYPE
                  Filter by pin type: mux, ext, synce-eth-port, int-
                  oscillator, gnss.

## [](#MONITOR_COMMAND)MONITOR COMMAND

       dpll monitor
           Monitor DPLL subsystem events in real-time. Displays notifications
           about:

                  • Device creation, deletion, and configuration changes

                  • Pin creation, deletion, and configuration changes

                  • Lock status changes

                  • Phase offset updates

                  • Frequency changes

           Events are prefixed with their type: [DEVICE_CREATE],
           [DEVICE_CHANGE], [DEVICE_DELETE], [PIN_CREATE], [PIN_CHANGE],
           [PIN_DELETE].

           Press Ctrl+C to stop monitoring.

## [](#EXAMPLES)EXAMPLES

       Show all DPLL devices
           dpll device show

       Show specific device in JSON format
           dpll -j device show id 0

       Set device 0 to manual mode
           dpll device set id 0 mode manual

       Enable phase offset monitoring on device 0
           dpll device set id 0 phase-offset-monitor enable

       Enable frequency monitoring on device 0
           dpll device set id 0 frequency-monitor enable

       Show all EEC devices
           dpll device show type eec

       Show devices from specific module in JSON
           dpll -jp device show module-name ice

       Show all pins
           dpll pin show

       Show all GNSS pins
           dpll pin show type gnss

       Show GNSS pins from specific module
           dpll pin show type gnss module-name ice

       Show pin with pretty JSON output
           dpll -jp pin show id 5

       Show connected input pins on device 0
           dpll pin show parent-device 0 direction input state connected

       Set pin frequency to 10 MHz
           dpll pin set id 0 frequency 10000000

       Configure pin relationship to parent device
           dpll pin set id 1 parent-device 0 prio 10 direction input state connected

       Adjust phase by -1000 picoseconds
           dpll pin set id 2 phase-adjust -1000

       Set multiple pin parameters at once
           dpll pin set id 3 frequency 10000000 phase-adjust -1000

       Monitor DPLL events
           dpll monitor

       Monitor events in JSON format
           dpll -jp monitor

       Get device ID by module name
           dpll device id-get module-name ice

       Get pin ID by board label
           dpll pin id-get board-label GNSS-1PPS

## [](#PHASE_ADJUSTMENT)PHASE ADJUSTMENT

           Phase adjustment is specified in picoseconds (1e-12 seconds) and
           allows fine-tuning of signal phase. This is crucial for precise
           time synchronization applications like 5G networks and high-
           frequency trading.

           Important considerations:

                  • Check phase-adjust-min and phase-adjust-max before
                    setting values

                  • Some hardware requires values to be multiples of phase-
                    adjust-gran

                  • Negative values shift phase backwards (earlier in time)

                  • Positive values shift phase forwards (later in time)

                  • The kernel validates all phase adjustment requests

## [](#CAPABILITIES)CAPABILITIES

           Pins may have various capabilities that determine which operations
           are allowed:

           state-can-change
                  The pin's state (connected/disconnected/selectable) can be
                  modified.

           priority-can-change
                  The pin's priority can be modified. This may apply to top-
                  level priority or priority within parent-device
                  relationships.

           direction-can-change
                  The pin's direction (input/output) can be modified.

           Use dpll pin show to check which capabilities a pin supports
           before attempting configuration changes.

## [](#EXIT_STATUS)EXIT STATUS

           0      Success

           1      Failure

## [](#NOTES)NOTES

           • The DPLL subsystem requires kernel support (CONFIG_DPLL=y or m)

           • Hardware support varies by device and driver

           • Some operations require specific hardware capabilities

           • Phase offset values are measured by hardware and cannot be set
             directly

           • Changes to device/pin configuration may affect system clock
             synchronization

## [](#SEE_ALSO)SEE ALSO

           ip(8), devlink(8), ethtool(8)

           Linux kernel documentation: Documentation/driver-api/dpll.rst

           Netlink specification: Documentation/netlink/specs/dpll.yaml

## [](#AUTHOR)AUTHOR

           dpll was written by Arkadiusz Kubalewski, Vadim Fedorenko, and
           others.

           This manual page was written by Petr Oros.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to <netdev@vger.kernel.org>

## [](#COLOPHON)COLOPHON

           This page is part of the iproute2 (utilities for controlling
           TCP/IP networking and traffic) project.  Information about the
           project can be found at 
           ⟨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2⟩.
           If you have a bug report for this manual page, send it to
           netdev@vger.kernel.org, shemminger@osdl.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/network/iproute2/iproute2.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iproute2                     23 October 2025                      DPLL(8)

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
