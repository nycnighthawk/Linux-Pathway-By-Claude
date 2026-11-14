---
{"title": "hostname(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/hostname.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# hostname(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    HOSTNAME(1)        Linux System Administrator's Manual        HOSTNAME(1)

## [](#NAME)NAME

           hostname - show or set the system's host name
           dnsdomainname - show the system's DNS domain name
           domainname - show or set the system's NIS/YP domain name
           nisdomainname - show or set system's NIS/YP domain name
           nodename - show or set the system's DECnet node name
           ypdomainname - show or set the system's NIS/YP domain name

## [](#SYNOPSIS)SYNOPSIS

           hostname [-v] [-a|--alias] [-d|--domain] [-f|--fqdn|--long]
                    [-i|--ip-address] [-s|--short]

           hostname [-v] [-y|--yp|--nis] [-n|--node]

           hostname [-v] [-F filename |--file filename|newname]
           domainname [-v] [-F filename |--file filename|newname]
           nodename [-v] [-F filename |--file filename|newname]

           dnsdomainname [-v]
           nisdomainname [-v]
           ypdomainname [-v]

           hostname [-h|--help] [-V|--version]

## [](#DESCRIPTION)DESCRIPTION

           Hostname is the program that is used to either set or display the
           current host, domain or node name of the system.  These names are
           used by many of the networking programs to identify the machine.
           The domain name is also used by NIS/YP.

       GET NAME
           When called without any arguments, the program displays the
           current names:

           hostname will print the name of the system as returned by the
           gethostname(2) function.

           domainname, nisdomainname, ypdomainname will print the name of the
           system as returned by the getdomainname(2) function. This is also
           known as the YP/NIS domain name of the system.

           nodename will print the DECnet node name of the system as returned
           by the getnodename(2) function.

           dnsdomainname will print the domain part of the FQDN (Fully
           Qualified Domain Name). The complete FQDN of the system is
           returned with hostname --fqdn.

       SET NAME
           When called with one argument or with the --file option, the
           commands set the host name, the NIS/YP domain name or the node
           name.

           Note, that only the super-user can change the names.

           It is not possible to set the FQDN or the DNS domain name with the
           dnsdomainname command (see THE FQDN below).

           The host name is usually set once at system startup by reading the
           contents of a file which contains the host name, e.g.
           /etc/hostname).

       THE FQDN
           You can't change the FQDN (as returned by hostname --fqdn) or the
           DNS domain name (as returned by dnsdomainname) with this command.
           The FQDN of the system is the name that the resolver(3) returns
           for the host name.

           Technically: The FQDN is the canonical name returned by
           gethostbyname2(2) when resolving the result of the gethostname(2)
           name. The DNS domain name is the part after the first dot..LP
           Therefore it depends on the configuration (usually in
           /etc/host.conf) how you can change it. If hosts is the first
           lookup method, you can change the FQDN in /etc/hosts.

## [](#OPTIONS)OPTIONS

           -a, --alias
                  Display the alias name of the host (if used).

           -d, --domain
                  Display the name of the DNS domain (this is the FQDN
                  without the segment up to the first dot). This is
                  equivalent to using the dnsdomainname command.

           -F, --file filename
                  Read the new host name from the specified file. Comments
                  (lines starting with a `#') are ignored.

           -f, --fqdn, --long
                  Display the FQDN (Fully Qualified Domain Name). A FQDN
                  consists of name including the DNS domain.

           -h, --help
                  Print a usage message and exit.

           -i, --ip-address
                  Display the IP address(es) of the host.

           -n, --node
                  Display the DECnet node name. If a parameter is given (or
                  --file name ) the root can also set a new node name.

           -s, --short
                  Display the short host name. This is the host name cut at
                  the first dot.

           -V, --version
                  Print version information on standard output and exit
                  successfully.

           -v, --verbose
                  Be verbose and tell what's going on.

           -y, --yp, --nis
                  Display the NIS domain name. If a parameter is given (or
                  --file name ) then root can also set a new NIS domain.

## [](#FILES)FILES

           /etc/hostname /etc/hosts /etc/host.conf

## [](#SEE_ALSO)SEE ALSO

           Homepage of the net-tools project: 
           ⟨https://net-tools.sourceforge.io⟩

           hostname(5), hostname(7), hosts(5)
           hostnamectl(8) if systemd is used.

## [](#AUTHOR)AUTHOR

           Peter Tobias <tobias@et-inf.fho-emden.de>,
           Bernd Eckenfels <net-tools@lina.inka.de> (NIS support),
           Steve Whitehouse <SteveW@ACM.org> (DECnet support).

## [](#COLOPHON)COLOPHON

           This page is part of the net-tools (networking utilities) project.
           Information about the project can be found at 
           ⟨http://net-tools.sourceforge.net/⟩.  If you have a bug report for
           this manual page, see ⟨http://net-tools.sourceforge.net/⟩.  This
           page was obtained from the project's upstream Git repository
           ⟨git://git.code.sf.net/p/net-tools/code⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-12.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    net-tools                       2025-09-10                    HOSTNAME(1)

------------------------------------------------------------------------

Pages that refer to this page: [hostnamectl(1)](../man1/hostnamectl.1.html),  [ippeveprinter(1)](../man1/ippeveprinter.1.html),  [gethostname(2)](../man2/gethostname.2.html),  [cupsd.conf(5)](../man5/cupsd.conf.5.html),  [hostname(5)](../man5/hostname.5.html),  [hosts(5)](../man5/hosts.5.html),  [proc_sys_kernel(5)](../man5/proc_sys_kernel.5.html)

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
