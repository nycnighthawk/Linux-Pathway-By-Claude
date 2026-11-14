---
{"title": "androiddump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/androiddump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# androiddump(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    ANDROIDDUMP(1)                                             ANDROIDDUMP(1)

## [](#NAME)NAME

           androiddump - Provide interfaces to capture from Android devices

## [](#SYNOPSIS)SYNOPSIS

           androiddump [ --help ] [ --version ] [ --extcap-version ] [
           --debug ] [ --extcap-interfaces ] [ --extcap-dlts ] [
           --extcap-interface=<interface> ] [ --extcap-config ] [
           --extcap-capture-filter=<capture filter> ] [ --capture ] [
           --fifo=<path to file or pipe> ] [ --adb-server-ip=<IP address> ] [
           --adb-server-tcp-port=<TCP port> ] [ --logcat-text=<TRUE or FALSE>
           ] [ --bt-server-tcp-port=<TCP port> ] [ --bt-forward-socket=<TRUE
           or FALSE> ] [ --bt-local-ip=<IP address> ] [
           --bt-local-tcp-port=<TCP port> ]

           androiddump --extcap-interfaces [ --adb-server-ip=<IP address> ] [
           --adb-server-tcp-port=<TCP port> ]

           androiddump --extcap-interface=<interface> [ --extcap-dlts ]

           androiddump --extcap-interface=<interface> [ --extcap-config ]

           androiddump --extcap-interface=<interface> --fifo=<path to file or
           pipe> --capture

## [](#DESCRIPTION)DESCRIPTION

           Androiddump is a extcap tool that provide interfaces to capture
           from an Android device. There are only two requirements:

            1. You must have the Android SDK and add it to your PATH
               environment variable. PATH should contain directory with tools
               like "adb" and "android". Android SDK for various platform are
               available on:
               https://developer.android.com/sdk/index.html#Other

            2. You must have permission to capture from the Android device.
               Some Android devices require on-screen authentication.

           Supported interfaces:

            1. Logcat Main (binary [<=Jelly Bean] or text)

            2. Logcat System (binary [<=Jelly Bean] or text)

            3. Logcat Events (binary [<=Jelly Bean] or text)

            4. Logcat Radio (binary [<=Jelly Bean] or text)

            5. Logcat Crash (text; from Lollipop)

            6. Bluetooth Hcidump [<=Jelly Bean]

            7. Bluetooth Bluedroid External Parser [Kitkat]

            8. Bluetooth BtsnoopNet [>=Lollipop]

            9. WiFi/Ethernet tcpdump [needs tcpdump on phone]

           Please note that Androiddump will work also for FirefoxOS or other
           Android-based operating systems.

## [](#OPTIONS)OPTIONS

           --help
               Print program arguments.

           --version
               Print program version.

           --extcap-version
               Print extcapized version.

           --debug
               Print additional messages.

           --extcap-interfaces
               List available interfaces.

           --extcap-interface=<interface>
               Use specified interfaces.

           --extcap-dlts
               List DLTs of specified interface.

           --extcap-config
               List configuration options of specified interface.

           --extcap-capture-filter=<capture filter>
               The capture filter. It corresponds to the value provided via
               the tshark -f option, and the Capture Filter field next to the
               interfaces list in the Wireshark interface.

                   Note

                   This is only respected for Wifi/Ethernet (tcpdump)
                   capturing, not for Bluetooth or logcat.

           --capture
               Start capturing from the specified interface and save it in
               the location specified with --fifo.

           --fifo=<path to file or pipe>
               Save captured packet to file or send it through pipe.

           --adb-server-ip=<IP address>
               Use other than default (127.0.0.1) ADB daemon’s IP address.

           --adb-server-tcp-port=<TCP port>
               Use other than default (5037) ADB daemon’s TCP port.

           --logcat-text=<TRUE or FALSE>

               If TRUE then use text logcat rather than binary. This option
               only has an effect on Logcat interfaces. This have no effect
               from Lollipop where is no binary Logcat available.

               Defaults to FALSE.

           --bt-server-tcp-port=<TCP port>

               Use other than default Bluetooth server TCP port on Android
               side. On Lollipop defaults is 8872, earlier 4330.

           --bt-forward-socket=<TRUE or FALSE>

               If TRUE then socket from Android side is forwarded to host
               side.

               Defaults to FALSE.

           --bt-local-ip=<IP address>
               Use other than default (127.0.0.1) IP address on host side for
               forwarded socket.

           --bt-local-tcp-port=<TCP port>
               Specify port to be used on host side for forwarded socket.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               androiddump --help

           To see program version:

               androiddump --version

           To see interfaces:

               androiddump --extcap-interfaces

           Example output

               interface {display=Android Logcat Main unknown MSM7627A}{value=android-logcat-main-MSM7627A}
               interface {display=Android Logcat System unknown MSM7627A}{value=android-logcat-system-MSM7627A}
               interface {display=Android Logcat Radio unknown MSM7627A}{value=android-logcat-radio-MSM7627A}
               interface {display=Android Logcat Events unknown MSM7627A}{value=android-logcat-events-MSM7627A}
               interface {display=Android Bluetooth Hcidump unknown MSM7627A}{value=android-bluetooth-hcidump-MSM7627A}

           Human-readable display name of interfaces contains interface type,
           one of:

               android-logcat-main (Android Logcat Main)
               android-logcat-system (Android Logcat System)
               android-logcat-radio (Android Logcat Radio)
               android-logcat-events (Android Logcat Events)
               android-logcat-text-main (Android Logcat Main)
               android-logcat-text-system (Android Logcat System)
               android-logcat-text-radio (Android Logcat Radio)
               android-logcat-text-events (Android Logcat Events)
               android-logcat-text-crash (Android Logcat Crash)
               android-bluetooth-hcidump (Android Bluetooth Hcidump)
               android-bluetooth-external-parser (Android Bluetooth External Parser)
               android-bluetooth-btsnoop-net (Android Bluetooth Btsnoop Net)
               android-tcpdump (Android tcpdump)

           For tcpdump this is followed by target network device name (like
           eth0).

           Then Android Device’s name if available, otherwise unknown.

           Last part of it is DeviceID - the identifier of the device
           provided by Android SDK (see adb devices).

           For example: Android Logcat Main unknown MSM7627A

           •   Android Logcat Main - user-friendly type of interface

           •   unknown - name of Android Device

           •   MSM7627A - device ID

           To see interface DLTs:

               androiddump --extcap-interface=android-bluetooth-hcidump-MSM7627A --extcap-dlts

           Example output

               dlt {number=99}{name=BluetoothH4}{display=Bluetooth HCI UART transport layer plus pseudo-header}

           To see interface configuration options:

               androiddump --extcap-interface=android-bluetooth-hcidump-MSM7627A --extcap-config

           Example output

               arg {number=0}{call=--adb-server-ip}{display=ADB Server IP Address}{type=string}{default=127.0.0.1}
               arg {number=1}{call=--adb-server-tcp-port}{display=ADB Server TCP Port}{type=integer}{range=0,65535}{default=5037}

           To capture:

               androiddump --extcap-interface=android-bluetooth-hcidump-MSM7627A --fifo=/tmp/bluetooth.pcapng --capture

               Note

               To stop capturing CTRL+C/kill/terminate the application.

## [](#SEE_ALSO)SEE ALSO

           wireshark(1), tshark(1), dumpcap(1), extcap(4)

## [](#NOTES)NOTES

           Androiddump is part of the Wireshark distribution. The latest
           version of Wireshark can be found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Michal Labedzki <michal.labedzki[AT]tieto.com>

           Contributors
           Roland Knall <rknall[AT]gmail.com>.SH COLOPHON This page is part
           of the wireshark (Interactively dump and analyze network traffic)
           project. Information about the project can be found at 
           ⟨https://www.wireshark.org/⟩. If you have a bug report for this
           manual page, see
           ⟨https://gitlab.com/wireshark/wireshark/-/issues⟩. This page was
           obtained from the project's upstream Git repository
           ⟨https://gitlab.com/wireshark/wireshark.git⟩ on 2026-08-04. (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.) If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2026-01-15                 ANDROIDDUMP(1)

------------------------------------------------------------------------

Pages that refer to this page: [extcap(4)](../man4/extcap.4.html)

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
