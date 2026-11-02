---
{"title": "Secure Shell", "url": "https://wiki.archlinux.org/title/Secure_Shell", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Secure Shell

Related articles

-   [SSHFS](../en/SSHFS.html "SSHFS")
-   [Mosh](../en/Mosh.html "Mosh")
-   [Tailscale](../en/Tailscale.html "Tailscale")
-   [VPN over SSH](../en/VPN_over_SSH.html "VPN over SSH")

**This article or section is a candidate for merging with [OpenSSH](../en/OpenSSH.html "OpenSSH").**

**Notes:** Ambiguation of questionable value (Discuss in [Talk:Secure_Shell#Remove ambiguation](../en/Talk:Secure_Shell.html#Remove_ambiguation "Talk:Secure Shell"))

According to [Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell "wikipedia:Secure Shell"):

Secure Shell (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network. Its most notable applications are remote login and command-line execution.

Examples of services that can use SSH are [Git](../en/Git.html "Git"), [rsync](../en/Rsync.html "Rsync") and [X11 forwarding](../en/X11_forwarding.html "X11 forwarding"). Services that always use SSH are [SCP and SFTP](../en/SCP_and_SFTP.html "SCP and SFTP").

An SSH server, by default, listens on the standard TCP port 22. An SSH client program is typically used for establishing connections to an *sshd* daemon accepting remote connections. Both are commonly present on most modern operating systems, including macOS, GNU/Linux, Solaris and OpenVMS. Proprietary, freeware and open source versions of various levels of complexity and completeness exist.

## Software {#Software}

-   **[Dropbear](../en/Dropbear.html "Dropbear")** --- Lightweight SSH server. The command-line SSH client is named [dbclient(1)](https://man.archlinux.org/man/dbclient.1).

[https://matt.ucc.asn.au/dropbear/dropbear.html](https://matt.ucc.asn.au/dropbear/dropbear.html) \|\| [dropbear](https://archlinux.org/packages/?name=dropbear)

-   **[OpenSSH](../en/OpenSSH.html "OpenSSH")** --- Premier connectivity tool for remote login with the SSH protocol

[https://www.openssh.com/portable.html](https://www.openssh.com/portable.html) \|\| [openssh](https://archlinux.org/packages/?name=openssh)

### Server only {#Server_only}

-   **TinySSH** --- A minimalistic SSH server which implements only a subset of SSHv2 features; glibc as its single dependency.

[https://tinyssh.org/](https://tinyssh.org/) \|\| [tinyssh](https://archlinux.org/packages/?name=tinyssh)

### Client only {#Client_only}

-   **[PuTTY](../en/PuTTY.html "PuTTY")** --- A terminal integrated SSH/Telnet client

[https://www.chiark.greenend.org.uk/\~sgtatham/putty/](https://www.chiark.greenend.org.uk/~sgtatham/putty/) \|\| [putty](https://archlinux.org/packages/?name=putty)

## Securing {#Securing}

See [Security#SSH](../en/Security.html#SSH "Security").

## See also {#See_also}

-   [Terminal multiplexers](../en/Terminal_multiplexer.html "Terminal multiplexer") (often used over SSH)
-   [Wikipedia:Comparison of SSH clients](https://en.wikipedia.org/wiki/Comparison_of_SSH_clients "wikipedia:Comparison of SSH clients")
-   [Wikipedia:Comparison of SSH servers](https://en.wikipedia.org/wiki/Comparison_of_SSH_servers "wikipedia:Comparison of SSH servers")
-   [SSH Key Fingerprint formats](https://blog.webernetz.net/ssh-key-fingerprints/)
