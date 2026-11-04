---
{"title": "Samba/Active Directory domain controller", "url": "https://wiki.archlinux.org/title/Samba/Active_Directory_domain_controller", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Samba/Active Directory domain controller

Related articles

-   [Active Directory Integration](../../en/Active_Directory_Integration.html "Active Directory Integration")
-   [Samba](../../en/Samba.html "Samba")
-   [SOGo](../../en/SOGo.html "SOGo")

This article explains how to setup an Active Directory domain controller using [Samba](../../en/Samba.html "Samba"). It is assumed that all configuration files are in their unmodified, post-installation state. This article was written and tested on a fresh installation, with no modifications other than setting up a static IPv4 network connection (required). Finally, most of the commands below will require elevated privileges. Despite conventional wisdom, it may be easier to run these short few commands from a root session as opposed to obtaining rights on an as needed basis.

## Installation {#Installation}

**Note** Make sure you can access the machines in your network via their hostname. See [Network configuration#Local network hostname resolution](../../en/Network_configuration.html#Local_network_hostname_resolution "Network configuration") for more information.

A fully functional samba domain controller requires several programs beyond those included with the Samba distribution. [Install](../../en/Help:Reading.html#Installation_of_packages "Install") the [krb5](https://archlinux.org/packages/?name=krb5), [ntp](https://archlinux.org/packages/?name=ntp), [python-cryptography](https://archlinux.org/packages/?name=python-cryptography), [python-dnspython](https://archlinux.org/packages/?name=python-dnspython), [python-markdown](https://archlinux.org/packages/?name=python-markdown), [openresolv](https://archlinux.org/packages/?name=openresolv) and [samba](https://archlinux.org/packages/?name=samba) packages from the official repositories.

Samba contains its own fully functional DNS server, but if you need to maintain DNS zones for external domains, you are strongly encouraged to use [BIND](../../en/BIND.html "BIND") instead. If you need to share printers, you will also need [CUPS](../../en/CUPS.html "CUPS"). If needed, install the [bind](https://archlinux.org/packages/?name=bind) and/or [cups](https://archlinux.org/packages/?name=cups) packages.

## Creating a new directory {#Creating_a_new_directory}

### Provisioning {#Provisioning}

The first step to creating an Active Directory domain is provisioning. This involves setting up the internal [LDAP](../../en/OpenLDAP.html "LDAP"), [Kerberos](../../en/Kerberos.html "Kerberos"), and DNS servers and performing all of the basic configuration needed for the directory. If you have set up a directory server before, you are undoubtedly aware of the potential for errors in making these individual components work together as a single unit. The difficulty in doing so is the very reason that the Samba developers chose to provide internal versions of these programs. The server packages above were installed only for the client utilities. Provisioning is quite a bit easier with Samba. Just issue the following command:

    # samba-tool domain provision --use-rfc2307 --interactive

#### Argument explanations {#Argument_explanations}

\--use-rfc2307
:   this argument adds POSIX attributes (UID/GID) to the AD Schema. This will be necessary if you intend to authenticate Linux, BSD, or macOS clients (including the local machine) in addition to Microsoft Windows.

&nbsp;

\--interactive
:   this parameter forces the provision script to run interactively.

Alternately, you can review the help for the provision step by running `samba-tool domain provision --help`.

#### Interactive provision explanations {#Interactive_provision_explanations}

Realm
:   **INTERNAL.DOMAIN.COM** - This should be the same as the DNS domain in all caps. It is common to use an internal-only sub-domain to separate your internal domain from your external DNS domains, but it is not required.

&nbsp;

Domain
:   **INTERNAL** - This will be the NetBIOS domain name, usually the leftmost DNS sub-domain but can be anything you like. For example, the name INTERNAL would not be very descriptive. Perhaps company name or initials would be appropriate. This should be entered in all caps, and should have a 15 character maximum length for compatibility with older clients.

&nbsp;

Server Role
:   **dc** - This article assumes that your are installing the first DC in a new domain. If you select anything different, the rest of this article will likely be useless to you.

&nbsp;

DNS Backend
:   **BIND9_DLZ** or **SAMBA_INTERNAL** - This is down to personal preference of the server admin. Again, if you are hosting DNS for external domains, you are strongly encouraged to use the **BIND9_DLZ** backend so that flat zone files can continue to be used and existing transfer rules can co-exist with the internal DNS server. If unsure, use the **SAMBA_INTERNAL** backend.

&nbsp;

DNS forwarder IP address
:   **xxx.xxx.xxx.xxx** or **none** - This option is only presented when using the SAMBA_INTERNAL DNS backend. Supply the IP address of a DNS server for forwarding non local DNS queries, or use the string **none** to always do root lookups.

&nbsp;

Administrator password
:   **xxxxxxxx** - You must select a *strong* password for the administrator account. The minimum requirements are one uppercase letter, one number, and at least eight characters. If you attempt to use a password that does not meet the complexity requirements, provisioning will fail.

### Configuring daemons {#Configuring_daemons}

#### NTPD {#NTPD}

Create a suitable NTP configuration for your network time server. See [Network Time Protocol daemon](../../en/Network_Time_Protocol_daemon.html "Network Time Protocol daemon") for explanations of, and additional configuration options.

Modify the `/etc/ntp.conf` file with the following contents:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ntp.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# Please consider joining the pool:
#
#     http://www.pool.ntp.org/join.html
#
# For additional information see:
# - https://wiki.archlinux.org/index.php/Network_Time_Protocol_daemon
# - http://support.ntp.org/bin/view/Support/GettingStarted
# - the ntp.conf man page

# Associate to Arch's NTP pool
server 0.arch.pool.ntp.org
server 1.arch.pool.ntp.org
server 2.arch.pool.ntp.org
server 3.arch.pool.ntp.org

# Restrictions
restrict default kod limited nomodify notrap nopeer mssntp
restrict 127.0.0.1
restrict ::1
restrict 0.arch.pool.ntp.org mask 255.255.255.255 nomodify notrap nopeer noquery
restrict 1.arch.pool.ntp.org mask 255.255.255.255 nomodify notrap nopeer noquery
restrict 2.arch.pool.ntp.org mask 255.255.255.255 nomodify notrap nopeer noquery
restrict 3.arch.pool.ntp.org mask 255.255.255.255 nomodify notrap nopeer noquery

# Location of drift file
driftfile /var/lib/ntp/ntpd.drift

# Location of the update directory
ntpsigndsocket /var/lib/samba/ntp_signd/
```

Create the state directory and set permissions:

    # install -d /var/lib/samba/ntp_signd
    # chown root:ntp /var/lib/samba/ntp_signd
    # chmod 0750 /var/lib/samba/ntp_signd

Enable and start the `ntpd.service` unit.

#### BIND {#BIND}

If you elected to use the **BIND9_DLZ** DNS backend, [Install](../../en/Help:Reading.html#Installation_of_packages "Install") the [bind](https://archlinux.org/packages/?name=bind) package and create the following BIND configuration. See [BIND](../../en/BIND.html "BIND") for explanations of, and additional configuration options. Be sure to replace the **x** characters with suitable values:

Create the `/etc/named.conf` file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/named.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
// vim:set ts=4 sw=4 et:
acl local-networks {
    127.0.0.0/8;
    xxx.xxx.xxx.xxx/xx;
// Uncomment the following line(s) if using IPv6
    //::1/128;
    //xxxx:xxxx:xxxx:xxxx::/64;
};

options {
    directory "/var/named";
    pid-file "/run/named/named.pid";
    session-keyfile "/run/named/session.key";

    // Uncomment this line to enable IPv6 connections support
    //  listen-on-v6 { any; };
    // Add this for no IPv4:
    //  listen-on { none; };

    // Add any subnets or hosts you want to allow to the local-networks acl
    allow-query       { local-networks; };
    allow-recursion   { local-networks; };
    allow-query-cache { local-networks; };
    allow-transfer    { none; };
    allow-update      { none; };

    version none;
    hostname none;
    server-id none;

    auth-nxdomain yes;
    datasize default;
    empty-zones-enable no;
    tkey-gssapi-keytab "/var/lib/samba/bind-dns/dns.keytab";

    // Uncomment if you wish to use ISP forwarders
    //  forwarders { xxx.xxx.xxx.xxx; xxx.xxx.xxx.xxx; };
};

zone "localhost" IN {
    type master;
    file "localhost.zone";
};

zone "0.0.127.in-addr.arpa" IN {
    type master;
    file "127.0.0.zone";
};

zone "1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa" {
    type master;
    file "localhost.ip6.zone";
};

// Load AD integrated zones
include "/var/lib/samba/bind-dns/named.conf";

//zone "example.org" IN {
//    type slave;
//    file "example.zone";
//    masters {
//        192.168.1.100;
//    };
//    allow-query { any; };
//    allow-transfer { any; };
//};

logging {
    channel xfer-log {
        file "/var/log/named.log";
            print-category yes;
            print-severity yes;
            severity info;
        };
        category xfer-in { xfer-log; };
        category xfer-out { xfer-log; };
        category notify { xfer-log; };
};
```

Set permissions:

    # chgrp named /var/lib/samba/private/dns.keytab
    # chmod g+r /var/lib/samba/private/dns.keytab
    # touch /var/log/named.log
    # chown root:named /var/log/named.log
    # chmod 664 /var/log/named.log

Enable and start the `named.service` unit.

Good values for forwarders are your ISP\'s DNS servers. Google (8.8.8.8, 8.8.4.4, 2001:4860:4860::8888, and 2001:4860:4860::8844) and OpenDNS (208.67.222.222, 208.67.220.220, 2620:0:ccc::2 and 2620:0:ccd::2) provide suitable public DNS servers free of charge. Appropriate values for subnets are specific to your network.

#### Kerberos client utilities {#Kerberos_client_utilities}

The provisioning step above created a perfectly valid krb5.conf file for use with a Samba domain controller. Install it with the following commands:

    # mv /etc/krb5.conf{,.default}
    # cp /var/lib/samba/private/krb5.conf /etc

#### DNS {#DNS}

You will need to begin using the local DNS server now. Reconfigure resolvconf to use only localhost for DNS lookups. Create the `/etc/resolv.conf.tail` (do not forget to substitute **internal.domain.tld** with your internal domain):

    # Samba configuration
    search internal.domain.tld
    # If using IPv6, uncomment the following line
    #nameserver ::1
    nameserver 127.0.0.1

Set permissions and regenerate the new `/etc/resolv.conf` file:

    # chmod 644 /etc/resolv.conf.tail
    # resolvconf -u

#### Samba {#Samba}

Enable and start the `samba.service` unit. If you intend to use the LDB utilities, you will also need create the `/etc/profile.d/sambaldb.sh` file to set **LDB_MODULES_PATH**:

    export LDB_MODULES_PATH="${LDB_MODULES_PATH}:/usr/lib/samba/ldb"

Set permissions on the file and source it:

    # chmod 0755 /etc/profile.d/sambaldb.sh
    # . /etc/profile.d/sambaldb.sh

### Testing the installation {#Testing_the_installation}

#### DNS {#DNS_2}

First, verify that DNS is working as expected. Execute the following commands substituting appropriate values for **internal.domain.com** and **server**:

    # host -t SRV _ldap._tcp.internal.domain.com.
    # host -t SRV _kerberos._udp.internal.domain.com.
    # host -t A server.internal.domain.com.

You should receive output similar to the following:

    _ldap._tcp.internal.domain.com has SRV record 0 100 389 server.internal.domain.com.
    _kerberos._udp.internal.domain.com has SRV record 0 100 88 server.internal.domain.com.
    server.internal.domain.com has address xxx.xxx.xxx.xxx

#### NT authentication {#NT_authentication}

Next, verify that password authentication is working as expected:

    # smbclient //localhost/netlogon -U Administrator -c 'ls'

You will be prompted for a password (the one you selected earlier), and will get a directory listing like the following:

      .                                   D        0  Wed Nov 27 23:59:07 2013
      ..                                  D        0  Wed Nov 27 23:59:12 2013

            50332 blocks of size 2097152. 47185 blocks available

#### Kerberos {#Kerberos}

Now verify that the KDC is working as expected. Be sure to replace **INTERNAL.DOMAIN.COM** and use uppercase letters:

    # kinit administrator@INTERNAL.DOMAIN.COM

You should be prompted for a password and get output similar to the following:

    Warning: Your password will expire in 41 days on Wed 08 Jan 2014 11:59:11 PM CST

Verify that you actually got a ticket:

    # klist

You should get output similar to below:

    Ticket cache: FILE:/tmp/krb5cc_0
    Default principal: administrator@INTERNAL.DOMAIN.COM

    Valid starting       Expires              Service principal
    11/28/2013 00:22:17  11/28/2013 10:22:17  krbtgt/INTERNAL.DOMAIN.COM@INTERNAL.DOMAIN.COM
        renew until 11/29/2013 00:22:14

As a final test, use smbclient with your recently acquired ticket. Replace **server** with the correct server name:

    # smbclient //server/netlogon --use-kerberos=required -c 'ls'

The output should be the same as when testing password authentication above.

### Additional configuration {#Additional_configuration}

#### DNS {#DNS_3}

You will also need to create a reverse lookup zone for each subnet in your environment in DNS. It is important that this is kept in Samba\'s DNS as opposed to BIND to allow for dynamic updates by cleints. For each subnet, create a reverse lookup zone with the following commands. Replace **server**.**internal**.**domain**.**tld** and **xxx**.**xxx**.**xxx** with appropriate values. For **xxx**.**xxx**.**xxx**, use the first three octets of the subnet in reverse order (for example: 192.168.0.0/24 becomes 0.168.192):

    # samba-tool dns zonecreate server.internal.domain.tld xxx.xxx.xxx.in-addr.arpa -U Administrator

Now, add a record for you server (if your server is multi-homed, add for each subnet) again substituting appropriate values as above. **zzz** will be replaced by the fourth octet of the IP for the server:

    # samba-tool dns add server.internal.domain.tld xxx.xxx.xxx.in-addr.arpa zzz PTR server.internal.domain.tld -U Administrator

Finally, test the lookup. Replace **xxx**.**xxx**.**xxx**.**xxx** with the IP of your server:

    # host -t PTR xxx.xxx.xxx.xxx

You should get output similar to the following:

    xxx.xxx.xxx.xxx.in-addr.arpa domain name pointer server.internal.domain.tld.

#### TLS {#TLS}

TLS support is not enabled by default, however, a default certificate was created when the DC was brought up. With the release of Samba 4.3.8 and 4.2.2, unsecured LDAP binds are disabled by default, and you must configure TLS to use Samba as an authentication source (without reducing the security of your Samba installation). To use the default keys, append the following lines to the \"\[global\]\" section of the `/etc/samba/smb.conf` file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[global]
tls enabled  = yes
tls keyfile  = tls/key.pem
tls certfile = tls/cert.pem
tls cafile   = tls/ca.pem
```

If a trusted certificate is needed, create a signing key and a certificate request (see [OpenSSL](../../en/OpenSSL.html "OpenSSL") for detailed instructions). Get the request signed by your chosen certificate authority, and put into this directory. If your certificate authority also needs an intermediate certificate, concatenate the certs (server cert first, then intermediate) and leave **tls cafile** blank.

Restart `samba` for the changes to take effect.

## Adding a second domain controller to an existing domain {#Adding_a_second_domain_controller_to_an_existing_domain}

### Prerequisites {#Prerequisites}

As with the provisioning setup when setting up a new domain, you must have [ntp](https://archlinux.org/packages/?name=ntp) configured per [the above instructions](#NTPD). Additionally, some of the arguments and parameters on the original domain setup must be replicated here.

#### Argument explanations {#Argument_explanations_2}

\--option=\'idmap_ldb:use rfc2307 = yes\'
:   this is required if you elected to include Unix UID/GID support on your existing domain (using the **\--use-rfc2307** option for Samba\'s provision step or applied the RFC 2307 schema extensions).

&nbsp;

\--dns-backend=**DNSTYPE**
:   replace **DNSTYPE** with **BIND9_DLZ** or **SAMBA_INTERNAL** - This is again down to personal preference of the server admin. If using **BIND9_DLZ** backend, you will need to configure [bind](https://archlinux.org/packages/?name=bind) as per [the above instructions](#BIND) after joining the domain.

&nbsp;

\--option=\"dns forwarder=\"**xxx.xxx.xxx.xxx**\"
:   this is only valid for the SAMBA_INTERNAL DNS backend which allows you to specify a DNS forwarder. Replace **xxx.xxx.xxx.xxx** with appropriate value.

&nbsp;

\--site=**SITE**
:   if you have multiple sites defined, use this to join directly in that site.

See the output of `samba-tool domain join --help` for additional options.

### Joining an existing domain as a new DC {#Joining_an_existing_domain_as_a_new_DC}

Execute the following command (adding any necessary parameters above to the end of the command):

    # samba-tool domain join internal.domain.tld DC -Uadministrator <other options>

Now copy the `krb5.conf`:

    # cp /var/lib/samba/private/krb5.conf /etc/krb5.conf

Enable and start the `samba.service` unit.

If using BIND9_DLZ DNS backend, run the following command:

    # samba_upgradedns --dns-backend=BIND9_DLZ

You\'ll need to follow the [BIND](#BIND) section above then restart the `named.service`.

Update the DNS records with the following command:

    # samba_dnsupdate --all-names --use-samba-tool --verbose

Now set the local server as the first nameserver in the `resolv.conf` and proceed with LDB configuration and testing as with a new domain [here](#Samba).

### Transferring the FSMO roles {#Transferring_the_FSMO_roles}

If this is intended to replace an existing domain controller, you will need to transfer the FSMO roles before demoting the existing DC. This is currently outside the scope of this document. See the Samba wiki [here](https://wiki.samba.org/index.php/Transferring_and_Seizing_FSMO_Roles).

## Additional Services {#Additional_Services}

### Printing {#Printing}

By default, a Samba server, when configured as a domain controller, does not enable printing by default. You will need to add the following lines to the global section of the `/etc/samba/smb.conf` file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[global]
...
        rpc_server:spoolss = external
        rpc_daemon:spoolssd = fork
        printing = CUPS
...
[printers]
       path = /var/spool/samba/
       printable = yes
```

The above configuration will enable automatic sharing of all CUPS print queues. If you wish to share only specific print queues, you will want to add the following additional lines (removing the **\[printers\]** share above):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[global]
...
        load printers = no
...
# Add an example print share
[HPDJ3050]
       path = /var/spool/samba/
       printable = yes
       printer name = hpdj3050
```

## Tips and tricks {#Tips_and_tricks}

### DHCP with dynamic DNS updates {#DHCP_with_dynamic_DNS_updates}

**This article or section needs expansion.**

**Reason:** This section needs to be updated for the newer [kea](https://archlinux.org/packages/?name=kea) DHCP server. (Discuss in [Talk:Samba/Active Directory domain controller](../../en/Talk:Samba/Active_Directory_domain_controller.html))

It should be noted that using this method will affect functionality of windows clients, as they will still attempt to update DNS on their own. When this occurs, the machine will be denied permission to do so as the record will be owned by the dhcp user rather than the machine account. While this is essentially harmless, it will generate warnings in the system log of the offending machine. You should create a GPO to overcome this, but unfortunately, Samba does not yet have a command line utility to modify GPOs. You will need a Windows PC with the RSAT tools installed. Simply create a dedicated GPO with the Group Policy Editor, and apply only to OUs that contain workstations using DHCP (so that Samba/Windows servers and statically configured Samba/Windows clients can still update using \'ipconfig /registerdns\') and configure the following settings:

    Computer Configuration
      Policies
        Administrative Templates
          Network
            DNS Client
              Dynamic Update = Disabled
              Register PTR Records = Disabled

[Install](../../en/Help:Reading.html#Installation_of_packages "Install") the [dhcp](https://archlinux.org/packages/?name=dhcp), [sudo](https://archlinux.org/packages/?name=sudo), and the [samba-dhcpd-update](https://aur.archlinux.org/packages/samba-dhcpd-update/)^AUR^ packages.

Create an unprivileged user in AD for performing the updates. When prompted for password, use a secure password. 63 random, mixed case, alpha-numeric characters is sufficient. Optionally samba-tool also takes a random argument:

    # samba-tool user create dhcp --description="Unprivileged user for DNS updates via DHCP server"

Since this is a service account, disabling password expiration on the user account is recommended, but not required:

    # samba-tool user setexpiry dhcp --noexpiry

Give the user privileges to administer DNS:

    # samba-tool group addmembers DnsAdmins dhcp

Create an SPN and export the users credentials to a private keytab:

    # samba-tool spn add server/server.internal.domain.tld@INTERNAL.DOMAIN.TLD dhcp
    # samba-tool domain exportkeytab --principal=dhcp@INTERNAL.DOMAIN.TLD dhcpd.keytab
    # install -vdm 755 /etc/dhcpd
    # mv dhcpd.keytab /etc/dhcpd
    # chown root:root /etc/dhcpd/dhcpd.keytab
    # chmod 400 /etc/dhcpd/dhcpd.keytab

Modify the `dhcpd-update-samba-dns.conf` file with the following commands (substituting correct values for **server**, **internal**.**domain**.**tld**, and **INTERNAL**.**DOMAIN**.**TLD**):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/dhcpd/dhcpd-update-samba-dns.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# Variables
KRB5CC="/tmp/dhcpd4.krb5cc"
KEYTAB="/etc/dhcpd/dhcpd.keytab"
DOMAIN="internal.domain.tld"
REALM="INTERNAL.DOMAIN.TLD"
PRINCIPAL="dhcp@${REALM}"
NAMESERVER="server.${DOMAIN}"
ZONE="${DOMAIN}"
```

Grant the dhcp user account permissions to run the update script without a password prompt (replace **server** with the hostname of the server):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/sudoers.d/dhcp-update
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
dhcp server = (root) NOPASSWD: /usr/bin/dhcpd-update-samba-dns.sh
```

Configure the dhcpd server following the [dhcpd](../../en/Dhcpd.html "Dhcpd") article and add the following to all subnet declarations in the `/etc/dhcpd.conf` file that provide DHCP service:

      on commit {
        set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
        set ClientName = pick-first-value(option host-name, host-decl-name);
        execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "add", ClientIP, ClientName);
      }

      on release {
        set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
        set ClientName = pick-first-value(option host-name, host-decl-name);
        execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "delete", ClientIP, ClientName);
      }

        on expiry {
        set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
        set ClientName = pick-first-value(option host-name, host-decl-name);
        execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "delete", ClientIP, ClientName);

Here is a complete example `/etc/dhcpd.conf` file for reference:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/dhcpd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}

subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.199;
  option subnet-mask 255.255.255.0;
  option routers 192.168.1.254;
  option domain-name "internal.domain.tld";
  option domain-name-servers 192.168.1.1;
  option broadcast-address 192.168.1.255;
  default-lease-time 28800;
  max-lease-time 43200;
  authoritative;

  on commit {
    set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
    set ClientName = pick-first-value(option host-name, host-decl-name);
    execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "add", ClientIP, ClientName);
  }

  on release {
    set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
    set ClientName = pick-first-value(option host-name, host-decl-name);
    execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "delete", ClientIP, ClientName);
  }

    on expiry {
    set ClientIP = binary-to-ascii(10, 8, ".", leased-address);
    set ClientName = pick-first-value(option host-name, host-decl-name);
    execute("/usr/bin/sudo", "/usr/bin/dhcpd-update-samba-dns.sh", "delete", ClientIP, ClientName);
  }
}
```

Finally, enable and start (or restart) the `dhcpd4` service.

### Transferring users from one directory to another {#Transferring_users_from_one_directory_to_another}

Unfortunately, there is no built-in utility to export users from one directory to another. This is one way, albeit exceptionally ugly, to get the user specific fields out of your existing SAM and into a suitable LDIF format for ldbmodify:

    # ldbsearch -H /var/lib/samba/private/sam.ldb \
        -s sub -b cn=Users,dc=internal,dc=domain,dc=tld '(objectClass=user)' | \
        grep -e "^\# record" -e "^accountExpires:" -e "^c:" -e "^cn:" -e "^co:" -e "^codePage:" \
             -e "^comment:" -e "^company:" -e "^countryCode:" -e "^department:" \
             -e "^description:" -e "^displayName" -e "^displayNamePrintable:" \
             -e "^distinguishedName" -e "^division:" -e "^dn:" -e "^employeeID:" \
             -e "^facsimileTelephoneNumber:" -e "^generationQualifier:" \
             -e "^givenName" -e "^homeDirectory:" -e "^homeDrive:" -e "^homePhone:" \
             -e "^homePostalAddress:" -e "^info:" -e "^initials:" \
             -e "^internationalISDNNumber:" -e "^ipPhone:" -e "^l:" -e "^mail:" \
             -e "^manager:" -e "^middleName:" -e "^mobile:" -e "^name:" -e "^o:" \
             -e "^objectClass" -e "^otherFacsimileTelephoneNumber:" \
             -e "^otherHomePhone:" -e "^otherIpPhone:" -e "^otherMailbox:" \
             -e "^otherMobile:" -e "^otherPager:" -e "^otherTelephone:" -e "^pager:" \
             -e "^personalTitle:" -e "^physicalDeliveryOfficeName:" -e "^postalAddress:" \
             -e "^postalCode:" -e "^postOfficeBox:" -e "^proxyAddresses\: SMTP" \
             -e "^proxyAddresses: smtp" -e "^referredDeliveryMethod:" \
             -e "^primaryInternationalISDNNumber:" -e "^primaryTelexNumber:" \
             -e "^profilePath:" -e "^registeredAddress:" -e "^sAMAccountName:" \
             -e "^scriptPath:" -e "^sn:" -e "^st:" -e "^street:" -e "^streetAddress:" \
             -e "^telephoneNumber:" -e "^teletexTerminalIdentifier:" \
             -e "^telexNumber:" -e "^title:" -e "^userAccountControl:" -e "^userPrincipalName:"\
             -e "^url:" -e "^userSharedFolder:" -e "^userSharedFolderOther:" -e "^wWWHomePage:" | \
        sed '/^dn:.*/ a\changetype: add' | sed '/^# record/ i\\n' > user-export.ldif

Explanation: Run an ldbsearch in the users container only, using sub-tree search for objectclass=user. If you need the whole directory, you can modify the search base to use the root or some other OU. The output from ldbsearch is then piped into a really long grep command that returns only appropriate attributes to keep in the new directory. This is obviously subjective, and probably should be tailored to your specific use case. Finally, we use sed to insert the changetype line (needed to tell ldbmodify that we are adding a user), and prefix with a blank line (to make it easier to read) for each exported object.

**Note** You will need to modify the output file and remove any objects that you do not want transferred. The output file will contain objects (service users, built-ins, etc.) that can break your new directory if you fail to remove them! It will also contain the old domain in both the \"dn\" and \"distinguishedName\" attributies that must be changed before import.

To import, after editing the file and transferring to the new server, simply run the following command on your new samba domain controller:

    # ldbmodify -H /var/lib/samba/private/sam.ldb user-export.ldif

### Password Complexity {#Password_Complexity}

By default, Samba requires strong passwords. To disable the complexity check, issue the following command:

    # samba-tool domain passwordsettings set --complexity=off

Set [Password Settings Objects](https://wiki.samba.org/index.php/Password_Settings_Objects) in the Samba wiki for more information
