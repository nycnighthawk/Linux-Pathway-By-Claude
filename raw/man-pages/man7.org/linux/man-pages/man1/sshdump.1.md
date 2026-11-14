---
{"title": "sshdump(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/sshdump.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sshdump(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SSHDUMP(1)                                                     SSHDUMP(1)

## [](#NAME)NAME

           sshdump - Provide interfaces to capture packets from a remote host
           through SSH using a remote capture binary.

## [](#SYNOPSIS)SYNOPSIS

           sshdump [ --help ] [ --version ] [ --extcap-interfaces ] [
           --extcap-dlts ] [ --extcap-interface=<interface> ] [
           --extcap-config ] [ --extcap-capture-filter=<capture filter> ] [
           --capture ] [ --fifo=<path to file or pipe> ] [ --remote-host=<IP
           address> ] [ --remote-port=<TCP port> ] [
           --remote-username=<username> ] [ --remote-password=<password> ] [
           --sshkey=<private key path> ] [ --sshkey-passphrase=<private key
           passphrase> ] [ --proxycommand=<SSH proxy command> ] [
           --remote-interface=<interface> ] [
           --remote-capture-command-select=<capture command selection> ] [
           --remote-capture-command=<capture command> ] [
           --remote-priv=<privilege elevation command selection> ] [
           --remote-priv-user=<privileged user name> ] [ --remote-noprom ] [
           --remote-filter=<remote capture filter> ] [
           --remote-count=<number> ]

           sshdump --extcap-interfaces

           sshdump --extcap-interface=<interface> --extcap-dlts

           sshdump --extcap-interface=<interface> --extcap-config

           sshdump --extcap-interface=<interface> --fifo=<path to file or
           pipe> --capture --remote-host=myremotehost --remote-port=22
           --remote-username=user --remote-interface=eth2
           --remote-capture-command='tcpdump -U -i eth0 -w-'

## [](#DESCRIPTION)DESCRIPTION

           Sshdump is an extcap tool that allows one to run a remote capture
           tool over a SSH connection. The requirement is that the capture
           executable must have the capabilities to capture from the wanted
           interface.

           The feature is functionally equivalent to run commands like

               $ ssh remoteuser@remotehost -p 22222 'tcpdump -U -i IFACE -w -' > FILE &
               $ wireshark FILE

               $ ssh remoteuser@remotehost '/sbin/dumpcap -i IFACE -P -w - -f "not port 22"' > FILE &
               $ wireshark FILE

               $ ssh somehost dumpcap -P -w - -f udp | tshark -i -

           Typically sshdump is not invoked directly. Instead it can be
           configured through the Wireshark graphical user interface or its
           command line. The following will start Wireshark and start
           capturing from host remotehost:

               $ wireshark '-oextcap.sshdump.remotehost:"remotehost"' -i sshdump -k

           To explicitly control the remote capture command:

               $ wireshark '-oextcap.sshdump.remotehost:"remotehost"' \
                           '-oextcap.sshdump.remotecapturecommand:"tcpdump -i eth0 -Uw- not port 22"' \
                           -i sshdump -k

           Supported interfaces:

            1. sshdump

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

           --extcap-capture-filter=<capture filter>
               The capture filter. It corresponds to the value provided via
               the tshark -f option, and the Capture Filter field next to the
               interfaces list in the Wireshark interface.

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
               The username for SSH authentication.

           --remote-password=<password>
               The password to use (if not ssh-agent and pubkey are used).
               WARNING: the passwords are stored in plaintext and visible to
               all users on this system. It is recommended to use keyfiles
               with a SSH agent.

           --sshkey=<SSH private key path>
               The path to a private key for authentication. NOTE: Only
               OPENSSH key/value pair format is supported.

           --sshkey-passphrase=<SSH private key passphrase>
               The passphrase for the private key for authentication.

           --proxycommand=<proxy command>
               The command to use as proxy for the SSH connection.

           --remote-interface=<remote interface>
               The remote network interface to capture from.

           --remote-capture-command-select=<capture command-selection>

               The selection of the build-in support for remote capture
               commands. Either dumpcap for a remote capture command using
               dumpcap, tcpdump for a remote capture command using tcpdump,
               or other, where the remote capture command is to be given with
               the --remote-capture-command option.

               Note that selecting dumpcap allows for specifying multiple
               capture interfaces as a whitespace separated list, while
               tcpdump does not.

           --remote-capture-command=<capture command>

               A custom remote capture command that produces the remote
               stream that is shown in Wireshark. The command must be able to
               produce a PCAP stream written to STDOUT. See below for more
               examples.

               If using tcpdump, use the -w- option to ensure that packets
               are written to standard output (stdout). Include the -U option
               to write packets as soon as they are received.

               When specified, this command will be used as is, options such
               as the capture filter (--extcap-capture-filter) will not be
               appended.

           --remote-priv=<privilege elevation command selection>
               The command to use to achieve privilege elevation to capture
               on the remote host. Either none, sudo or doas.

           --remote-priv-user=<privileged user name>
               If a command is used to achieve privilege elevation to capture
               on the remote host this may require a user name. If needed use
               this option to give that user name.

           --remote-filter=<capture filter>
               The remote capture filter. It corresponds to the value
               provided via the tshark -f option, and the Capture Filter
               field next to the interfaces list in the Wireshark interface.

           --remote-count=<number>
               The number of packets to capture.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               sshdump --help

           To see program version:

               sshdump --version

           To see interfaces:

               sshdump --extcap-interfaces

           Only one interface (sshdump) is supported.

           Example output

               interface {value=sshdump}{display=SSH remote capture}

           To see interface DLTs:

               sshdump --extcap-interface=sshdump --extcap-dlts

           Example output

               dlt {number=147}{name=sshdump}{display=Remote capture dependent DLT}

           To see interface configuration options:

               sshdump --extcap-interface=sshdump --extcap-config

           Example output

               arg {number=0}{call=--remote-host}{display=Remote SSH server address}{type=string}
                   {tooltip=The remote SSH host. It can be both an IP address or a hostname}{required=true}{group=Server}
               arg {number=1}{call=--remote-port}{display=Remote SSH server port}{type=unsigned}{default=22}
                   {tooltip=The remote SSH host port (1-65535)}{range=1,65535}{group=Server}
               arg {number=2}{call=--remote-username}{display=Remote SSH server username}{type=string}
                   {tooltip=The remote SSH username. If not provided, the current user will be used}{group=Authentication}
               arg {number=3}{call=--remote-password}{display=Remote SSH server password}{type=password}
                   {tooltip=The SSH password, used when other methods (SSH agent or key files) are unavailable.}{group=Authentication}
               arg {number=4}{call=--sshkey}{display=Path to SSH private key}{type=fileselect}
                   {tooltip=The path on the local filesystem of the private SSH key (OpenSSH format)}{mustexist=true}{group=Authentication}
               arg {number=5}{call=--sshkey-passphrase}{display=SSH key passphrase}{type=password}
                   {tooltip=Passphrase to unlock the SSH private key}{group=Authentication}
               arg {number=6}{call=--proxycommand}{display=ProxyCommand}{type=string}
                   {tooltip=The command to use as proxy for the SSH connection}{group=Authentication}
               arg {number=7}{call=--remote-interface}{display=Remote interface}{type=string}
                   {tooltip=The remote network interface used for capture}{group=Capture}
               arg {number=8}{call=--remote-capture-command-select}{display=Remote capture command selection}{type=radio}
                   {tooltip=The remote capture command to build a command line for}{group=Capture}
                   value {arg=8}{value=dumpcap}{display=dumpcap}
                   value {arg=8}{value=tcpdump}{display=tcpdump}{default=true}
                   value {arg=8}{value=other}{display=Other:}
               arg {number=9}{call=--remote-capture-command}{display=Remote capture command}{type=string}
                   {tooltip=The remote command used to capture}{group=Capture}
               arg {number=10}{call=--remote-priv}{display=Gain capture privilege on the remote machine}{type=radio}
                   {tooltip=Optionally prepend the capture command with sudo or doas on the remote machine}{group=Capture}
                   value {arg=10}{value=none}{display=none}{default=true}
                   value {arg=10}{value=sudo}{display=sudo}
                   value {arg=10}{value=doas -n}{display=doas}
               arg {number=11}{call=--remote-priv-user}{display=Privileged user name for sudo or doas}{type=string}
                   {tooltip=User name of privileged user to execute the capture command on the remote machine}{group=Capture}
               arg {number=12}{call=--remote-noprom}{display=No promiscuous mode}{type=boolflag}
                   {tooltip=Don't use promiscuous mode on the remote machine}{group=Capture}
               arg {number=13}{call=--remote-filter}{display=Remote capture filter}{type=string}
                   {tooltip=The remote capture filter}{default=not ((host myhost) and port 22)}{group=Capture}
               arg {number=14}{call=--remote-count}{display=Packets to capture}{type=unsigned}{default=0}
                   {tooltip=The number of remote packets to capture. (Default: inf)}{group=Capture}
               arg {number=15}{call=--log-level}{display=Set the log level}{type=selector}
                   {tooltip=Set the log level}{required=false}{group=Debug}
                   value {arg=14}{value=message}{display=Message}{default=true}
                   value {arg=14}{value=info}{display=Info}
                   value {arg=14}{value=debug}{display=Debug}
                   value {arg=14}{value=noisy}{display=Noisy}
               arg {number=16}{call=--log-file}{display=Use a file for logging}{type=fileselect}
                   {tooltip=Set a file where log messages are written}{required=false}{group=Debug}

           To capture:

               sshdump --extcap-interface=sshdump --fifo=/tmp/ssh.pcap --capture --remote-host 192.168.1.10
               --remote-username user --remote-filter "not port 22"

           To use different capture binaries:

               sshdump --extcap-interface=sshdump --fifo=/tmp/ssh.pcap --capture --remote-host 192.168.1.10
               --remote-username user --remote-priv sudo --remote-capture-command-select tcpdump
               --remote-interface eth0 --remote-noprom

               sshdump --extcap-interface=sshdump --fifo=/tmp/ssh.pcap --capture --remote-host 192.168.1.10
               --remote-capture-command='dumpcap -i eth0 -P -w -'

               sshdump --extcap-interface=sshdump --fifo=/tmp/ssh.pcap --capture --remote-host 192.168.1.10
               --remote-capture-command='sudo tcpdump -i eth0 -U -w -'

               Note

               To stop capturing CTRL+C/kill/terminate the application.

           The sshdump binary can be renamed to support multiple instances.
           For instance if we want sshdump to show up twice in wireshark (for
           instance to handle multiple profiles), we can copy sshdump to
           sshdump-host1 and sshdump-host2. Each binary will show up an
           interface name same as the executable name. Those executables not
           being "sshdump" will show up as "custom version" in the interface
           description.

## [](#SEE_ALSO)SEE ALSO

           wireshark(1), tshark(1), dumpcap(1), extcap(4), tcpdump(1)

## [](#NOTES)NOTES

           Sshdump is part of the Wireshark distribution. The latest version
           of Wireshark can be found at https://www.wireshark.org.

           HTML versions of the Wireshark project man pages are available at
           https://www.wireshark.org/docs/man-pages.

## [](#AUTHORS)AUTHORS

           Original Author
           Dario Lombardo <lomato[AT]gmail.com>.SH COLOPHON This page is part
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

                                    2025-03-07                     SSHDUMP(1)

------------------------------------------------------------------------

Pages that refer to this page: [ciscodump(1)](../man1/ciscodump.1.html),  [extcap(4)](../man4/extcap.4.html)

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
