---
{"title": "wifidump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/wifidump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# wifidump(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    WIFIDUMP(1)                                                   WIFIDUMP(1)

## [](#NAME)NAME

           wifidump - Provides an interface to capture Wi-Fi frames from a
           remote host through SSH.

## [](#SYNOPSIS)SYNOPSIS

           wifidump [ --help ] [ --version ] [ --extcap-interfaces ] [
           --extcap-dlts ] [ --extcap-interface=<interface> ] [
           --extcap-config ] [ --extcap-capture-filter=<capture filter> ] [
           --capture ] [ --fifo=<path to file or pipe> ] [ --remote-host=<IP
           address> ] [ --remote-port=<TCP port> ] [
           --remote-username=<username> ] [ --remote-password=<password> ] [
           --sshkey=<public key path> ] [ --remote-interface=<interface> ] [
           --remote-channel-frequency=<channel frequency> ] [
           --remote-channel-width=<channel width> ]

           wifidump --extcap-interfaces

           wifidump --extcap-interface=<interface> --extcap-dlts

           wifidump --extcap-interface=<interface> --extcap-config

           wifidump --extcap-interface=<interface> --fifo=<path to file or
           pipe> --capture --remote-host=myremotehost --remote-port=22
           --remote-username=user --remote-interface=eth2
           --remote-channel-frequency=5180 --remote-channel-width=40

## [](#DESCRIPTION)DESCRIPTION

           Wifidump is an extcap tool that allows you to capture Wi-Fi
           traffic from a remote host over an SSH connection using tcpdump.
           The requirement to capture Wi-Fi frames is that the remote host
           must have the necessary binaries to manage and put the wanted
           interface into monitor mode. Such binaries include: ip, iw, and
           iwconfig. Also, because using monitor mode and managing the Wi-Fi
           interface requires root privileges, the system must be configured
           to allow the wanted user to run these binaries using sudo without
           entering a password.

           Typically wifidump is not invoked directly. Instead it can be
           configured through the Wireshark graphical user interface or its
           command line. The following will start Wireshark and start
           capturing from host remotehost:

               $ wireshark '-oextcap.wifidump.remotehost:remotehost' -i wifidump -k

           To explicitly control the remote capture command:

               $ wireshark '-oextcap.wifidump.remotehost:remotehost' \
                           '-oextcap.wifidump.remotechannelfrequency:5180' \
                           '-oextcap.wifidump.remotechannelwidth:40' \
                           -i wifidump -k

           Supported interfaces:

            1. wifidump

## [](#OPTIONS)OPTIONS

           --help
               Print program arguments.

           --version
               Print program version.

           --extcap-interfaces
               List available interfaces.

           --extcap-interface=<interface>
               Use specified interfaces.

           --extcap-dlts
               List DLTs of specified interface.

           --extcap-config
               List configuration options of specified interface.

           --capture
               Start capturing from specified interface and write raw packet
               data to the location specified by --fifo.

           --fifo=<path to file or pipe>
               Save captured packet to file or send it through pipe.

           --remote-host=<remote host>
               The address of the remote host for capture.

           --remote-port=<remote port>
               The SSH port of the remote host.

           --remote-username=<username>
               The username for ssh authentication.

           --remote-password=<password>
               The password to use (if not ssh-agent and pubkey are used).
               WARNING: the passwords are stored in plaintext and visible to
               all users on this system. It is recommended to use keyfiles
               with a SSH agent.

           --sshkey=<SSH private key path>
               The path to a private key for authentication.

           --remote-interface=<remote interface>
               The remote network interface to capture from.

           --remote-channel-frequency=<channel frequency>
               The remote channel frequency in MHz.

           --remote-channel-width=<channel width>
               The remote channel width in MHz.

           --extcap-capture-filter=<capture filter>
               The capture filter. It corresponds to the value provided via
               the tshark -f option, and the Capture Filter field next to the
               interfaces list in the Wireshark interface.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               wifidump --help

           To see program version:

               wifidump --version

           To see interfaces:

               wifidump --extcap-interfaces

           Only one interface (wifidump) is supported.

           Example output

               interface {value=wifidump}{display=Wi-Fi remote capture}

           To see interface DLTs:

               wifidump --extcap-interface=wifidump --extcap-dlts

           Example output

               dlt {number=147}{name=wifidump}{display=Remote capture dependent DLT}

           To see interface configuration options:

               wifidump --extcap-interface=wifidump --extcap-config

           Example output

               arg {number=0}{call=--remote-host}{display=Remote SSH server address}{type=string}
                   {tooltip=The remote SSH host. It can be both an IP address or a hostname}{required=true}{group=Server}
               arg {number=1}{call=--remote-port}{display=Remote SSH server port}{type=unsigned}
                   {tooltip=The remote SSH host port (1-65535)}{range=1,65535}{group=Server}
               arg {number=2}{call=--remote-username}{display=Remote SSH server username}{type=string}
                   {tooltip=The remote SSH username. If not provided, the current user will be used}{group=Authentication}
               arg {number=3}{call=--remote-password}{display=Remote SSH server password}{type=password}
                   {tooltip=The SSH password, used when other methods (SSH agent or key files) are unavailable.}{group=Authentication}
               arg {number=4}{call=--sshkey}{display=Path to SSH private key}{type=fileselect}
                   {tooltip=The path on the local filesystem of the private ssh key}{mustexist=true}{group=Authentication}
               arg {number=5}{call=--sshkey-passphrase}{display=SSH key passphrase}{type=password}
                   {tooltip=Passphrase to unlock the SSH private key}{group=Authentication}
               arg {number=6}{call=--remote-interface}{display=Remote interface}{type=string}
                   {tooltip=The remote network interface used to capture}{default=auto}{group=Capture}
               arg {number=7}{call=--remote-channel-frequency}{display=Remote channel}{type=selector}
                   {tooltip=The remote channel used to capture}{group=Capture}
               arg {number=8}{call=--remote-channel-width}{display=Remote channel width}{type=selector}
                   {tooltip=The remote channel width used to capture}{group=Capture}
               arg {number=9}{call=--remote-filter}{display=Remote capture filter}{type=string}
                   {tooltip=The remote capture filter}{group=Capture}
               arg {number=10}{call=--remote-count}{display=Packets to capture}{type=unsigned}
                   {tooltip=The number of remote packets to capture.}{group=Capture}
               arg {number=11}{call=--log-level}{display=Set the log level}{type=selector}
                   {tooltip=Set the log level}{required=false}{group=Debug}
               arg {number=12}{call=--log-file}{display=Use a file for logging}{type=fileselect}
                   {tooltip=Set a file where log messages are written}{required=false}{group=Debug}

           To capture:

               wifidump --extcap-interface=wifidump --fifo=/tmp/wifidump.pcap --capture --remote-host 192.168.1.10 --remote-username user --remote-channel-frequency 5180 --remote-channel-width 40

               Note

               To stop capturing CTRL+C/kill/terminate application.

           The wifidump binary can be renamed to support multiple instances.
           For instance if we want wifidump to show up twice in wireshark
           (for instance to handle multiple profiles), we can copy wifidump
           to wifidump-host1 and wifidump-host2. Each binary will show up an
           interface name same as the executable name. Those executables not
           being "wifidump" will show up as "custom version" in the interface
           description.

## [](#SEE_ALSO)SEE ALSO

           wireshark(1), tshark(1), extcap(4), tcpdump(1)

## [](#NOTES)NOTES

           Wifidump is part of the Wireshark distribution. The latest version
           of Wireshark can be found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Adrian Granados <adrian[AT]intuitibits.com>.SH COLOPHON This page
           is part of the wireshark (Interactively dump and analyze network
           traffic) project. Information about the project can be found at 
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

                                    2025-03-07                    WIFIDUMP(1)

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
