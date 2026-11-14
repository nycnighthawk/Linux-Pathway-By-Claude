---
{"title": "sshdig(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/sshdig.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# sshdig(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [AUTHORS](#AUTHORS) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SSHDIG(1)                                                       SSHDIG(1)

## [](#NAME)NAME

           sshdig - Provide interfaces to capture system calls from a remote
           host through SSH using a remote capture binary.

## [](#SYNOPSIS)SYNOPSIS

           sshdig [ --help ] [ --version ] [ --extcap-interfaces ] [
           --extcap-dlts ] [ --extcap-interface=<interface> ] [
           --extcap-config ] [ --extcap-capture-filter=<capture filter> ] [
           --capture ] [ --fifo=<path to file or pipe> ] [ --remote-host=<IP
           address> ] [ --remote-port=<TCP port> ] [
           --remote-username=<username> ] [ --remote-password=<password> ] [
           --sshkey=<private key path> ] [ --sshkey-passphrase=<private key
           passphrase> ] [ --proxycommand=<SSH proxy command> ] [
           --remote-capture-command-select=<capture command selection> ] [
           --remote-capture-command=<capture command> ] [
           --remote-priv=<privilege elevation command selection> ] [
           --remote-priv-user=<privileged user name> ] [
           --remote-filter=<remote capture filter> ] [
           --remote-count=<number> ] [ --remote-modern-bpf ] [
           --remote-io-snaplen=<snapshot length> ]

           sshdig --extcap-interfaces

           sshdig --extcap-interface=<interface> --extcap-dlts

           sshdig --extcap-interface=<interface> --extcap-config

           sshdig --extcap-interface=<interface> --fifo=<path to file or
           pipe> --capture --remote-host=myremotehost --remote-port=22
           --remote-username=user --remote-capture-command='sysdig
           --unbuffered --write=-'

## [](#DESCRIPTION)DESCRIPTION

           Sshdig is an extcap tool that allows one to capture system calls
           over a SSH connection. You must have permission to capture system
           calls on the remote system.

           The feature is functionally equivalent to

               $ ssh remoteuser@remotehost -p 22222 'sysdig --unbuffered -w -' > FILE &
               $ stratoshark FILE

           Typically sshdig is not invoked directly. Instead it can be
           configured through the Stratoshark graphical user interface or its
           command line. The following will start Stratoshark and start
           capturing from host remotehost:

               $ stratoshark '-oextcap.sshdig.remotehost:myserver.home.arpa' -i sshdig -k

           Supported interfaces:

            1. sshdig

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
               interfaces list in the Stratoshark interface.

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

           --remote-capture-command-select=<capture command-selection>
               The command to run on the remote system. Either sysdig for a
               remote capture command using sysdig, or other, where the
               remote capture command must be provided with the
               --remote-capture-command option.

           --remote-capture-command=<capture command>
               A custom remote capture command that produces the remote
               stream that is shown in Stratoshark. The command must be able
               to produce a .scap stream written to STDOUT.

           --remote-priv=<privilege elevation command selection>
               The command to use to achieve privilege elevation to capture
               on the remote host. Either none, sudo or doas.

           --remote-priv-user=<privileged user name>
               If a command is used to achieve privilege elevation to capture
               on the remote host requires a user name it may be provided
               here.

           --remote-filter=<capture filter>
               The remote capture filter. This is passed to the remote
               capture program, and must comply with its syntax rules.

           --remote-count=<number>
               The number of events to capture.

           --remote-modern-bpf
               Capture using an eBPF probe instead of the kernel module.

           --remote-io-snaplen=<snapshot length>
               The number of bytes to capture in each I/O event.

## [](#EXAMPLES)EXAMPLES

           To see program arguments:

               sshdig --help

           To see program version:

               sshdig --version

           To see interfaces:

               sshdig --extcap-interfaces

           Only one interface (sshdig) is supported.

           Example output

               interface {value=sshdig}{display=SSH remote syscall capture}

           To see interface DLTs:

               sshdig --extcap-interface=sshdig --extcap-dlts

           Example output

               dlt {number=147}{name=sshdig}{display=Remote capture dependent DLT}

           To see interface configuration options:

               sshdig --extcap-interface=sshdig --extcap-config

           Example output

               arg {number=0}{call=--remote-host}{display=Remote SSH server address}{type=string}{tooltip=The remote SSH host. It can be both an IP address or a hostname}{required=true}{group=Server}
               arg {number=1}{call=--remote-port}{display=Remote SSH server port}{type=unsigned}{default=22}{tooltip=The remote SSH host port (1-65535)}{range=1,65535}{group=Server}
               arg {number=2}{call=--remote-username}{display=Remote SSH server username}{type=string}{tooltip=The remote SSH username. If not provided, the current user will be used}{group=Authentication}
               arg {number=3}{call=--remote-password}{display=Remote SSH server password}{type=password}{tooltip=The SSH password, used when other methods (SSH agent or key files) are unavailable.}{group=Authentication}
               arg {number=4}{call=--sshkey}{display=Path to SSH private key}{type=fileselect}{tooltip=The path on the local filesystem of the private SSH key (OpenSSH format)}{mustexist=true}{group=Authentication}
               arg {number=5}{call=--sshkey-passphrase}{display=SSH key passphrase}{type=password}{tooltip=Passphrase to unlock the SSH private key}{group=Authentication}
               arg {number=6}{call=--proxycommand}{display=ProxyCommand}{type=string}{tooltip=The command to use as proxy for the SSH connection}{group=Authentication}
               arg {number=7}{call=--ssh-sha1}{display=Support SHA-1 keys (deprecated)}{type=boolflag}{tooltip=Support keys and key exchange algorithms using SHA-1 (deprecated)}{group=Authentication}
               arg {number=8}{call=--remote-capture-command-select}{display=Remote capture command selection}{type=radio}{tooltip=The remote capture command to build a command line for}{group=Capture}
               value {arg=8}{value=sysdig}{display=sysdig}
               value {arg=8}{value=other}{display=Other:}
               arg {number=9}{call=--remote-capture-command}{display=Remote capture command}{type=string}{tooltip=The remote command used to capture}{group=Capture}
               arg {number=10}{call=--remote-priv}{display=Gain capture privilege on the remote machine}{type=radio}{tooltip=Optionally prepend the capture command with sudo or doas on the remote machine}{group=Capture}
               value {arg=10}{value=none}{display=none}{default=true}
               value {arg=10}{value=sudo}{display=sudo}
               value {arg=10}{value=doas -n}{display=doas}
               arg {number=11}{call=--remote-priv-user}{display=Privileged user name for sudo or doas}{type=string}{tooltip=User name of privileged user to execute the capture command on the remote machine}{group=Capture}
               {group=Capture}
               arg {number=12}{call=--remote-count}{display=Packets to capture}{type=unsigned}{default=0}{tooltip=The number of remote packets to capture. (Default: inf)}{group=Capture}
               arg {number=13}{call=--log-level}{display=Set the log level}{type=selector}{tooltip=Set the log level}{required=false}{group=Debug}
               value {arg=13}{value=message}{display=Message}{default=true}
               value {arg=13}{value=info}{display=Info}
               value {arg=13}{value=debug}{display=Debug}
               value {arg=13}{value=noisy}{display=Noisy}
               arg {number=14}{call=--log-file}{display=Use a file for logging}{type=fileselect}{tooltip=Set a file where log messages are written}{required=false}{group=Debug}

           To capture:

               sshdig --extcap-interface=sshdig --fifo=/tmp/ssh.scap --capture --remote-host 192.168.1.10
               --remote-username user

               Note

               CTRL + C should be used to stop the capture in order to ensure
               clean termination.

           The sshdig binary can be renamed to support multiple instances.
           For instance if we want sshdig to show up twice in Stratoshark
           (for instance to handle multiple profiles), we can copy sshdig to
           sshdig-host1 and sshdig-host2. Each binary will show up an
           interface name same as the executable name. Those executables not
           being "sshdig" will show up as "custom version" in the capture
           source description.

## [](#SEE_ALSO)SEE ALSO

           stratoshark(1), strato(1), dumpcap(1), extcap(4)

## [](#NOTES)NOTES

           Sshdig is part of the Stratoshark distribution. The latest version
           of Stratoshark can be found at https://www.wireshark.org.

           HTML versions of the Stratoshark project man pages are available
           at https://www.wireshark.org/docs/man-pages.

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

                                    2026-01-15                      SSHDIG(1)

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
