---
{"title": "Active Directory integration", "url": "https://wiki.archlinux.org/title/Active_Directory_integration", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Active Directory integration

Related articles

-   [Samba](../en/Samba.html "Samba")
-   [Samba/Active Directory domain controller](../en/Samba/Active_Directory_domain_controller.html "Samba/Active Directory domain controller")
-   [SOGo](../en/SOGo.html "SOGo")

**This article or section needs expansion.**

**Reason:** This page is currently being updated. The original page has been left intact until the rewrite is complete, see the section labeled **Old Wiki Article** for the original contents. Sections using the ~~strikethrough~~ in the title, have already been covered in the new sections. (Discuss in [Talk:Active Directory integration](../en/Talk:Active_Directory_integration.html))

From [Wikipedia](https://en.wikipedia.org/wiki/Active_Directory "w:Active Directory"):

Active Directory (AD) is a [directory service](https://en.wikipedia.org/wiki/directory_service "wikipedia:directory service") that Microsoft developed for [Windows domain](https://en.wikipedia.org/wiki/Windows_domain "wikipedia:Windows domain") networks.

This article describes how to integrate an Arch Linux system with an existing Windows domain network using [Samba](../en/Samba.html "Samba").

Before continuing, you must have an existing Active Directory domain, and have a user with the appropriate rights within the domain to: query users and add computer accounts (Domain Join).

This document is not an intended as a complete guide to Active Directory nor Samba. Refer to the resources section for additional information.

## Introduction {#Introduction}

This article explains how to configure an Arch Linux system to participate in an Active Directory domain. This article was written and tested on a fresh installation, and it is assumed that all configuration files are in their unmodified, post-installation state. For the duration of the article, the example Active Directory domain will use the following configuration:

-   NetBIOS domain name: **INTERNAL**
-   DNS domain name: **internal.domain.tld**
-   Kerberos realm: **INTERNAL.DOMAIN.TLD**
-   First DC: **server1.internal.domain.tld** with IP address **192.168.1.1**
-   Second DC: **server2.internal.domain.tld** with IP address **192.168.1.2**

In most small networks, the DCs (domain controllers) also hold the DNS server role. This may not be true in larger networks. Generally, DCs also hold the NTP role, but not always. Consult your network administrator to verify correct values for DNS and NTP servers.

## Needed software {#Needed_software}

In order to use samba effectively, you will need to install the following packages: [samba](https://archlinux.org/packages/?name=samba), [smbclient](https://archlinux.org/packages/?name=smbclient), and [ntp](https://archlinux.org/packages/?name=ntp). ([timedatectl](../en/System_time.html "Timedatectl") can be used as an alternative to *ntp*.)

Additionally, while not required, the following packages will be useful for testing and troubleshooting: [bind](https://archlinux.org/packages/?name=bind), [krb5](https://archlinux.org/packages/?name=krb5), and if a printing is desired (whether you want to share printers, or use printers on another Samba/Windows host), [cups](https://archlinux.org/packages/?name=cups).

## Initial configuration of services {#Initial_configuration_of_services}

### DNS configuration {#DNS_configuration}

Active Directory depends entirely on DNS for name resolution. It is imperative that the `/etc/resolv.conf` file is configured with both the correct DNS servers and a domain search suffix. Whether configured via DHCP or static configuration, ensure that these values are correct for your domain. For the example domain configuration, the following contents are appropriate (be sure to replace **192.168.1.1**, **192.168.1.2**, and **internal.domain.tld** with appropriate values for your network):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/resolv.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
nameserver 192.168.1.1
nameserver 192.168.1.2
search internal.domain.tld
```

If you elected to install the [bind](https://archlinux.org/packages/?name=bind) package, you can test DNS configuration with the following commands (be sure to replace **server1** and **internal.domain.tld** with appropriate values for your network):

    $ nslookup -type=SRV _kerberos._tcp.internal.domain.tld.
    $ nslookup -type=SRV _ldap._tcp.internal.domain.tld.
    $ nslookup server1.internal.domain.tld.

You should get output similar to the following (adjust appropriately for only one DC, or more than two):

    Server:        192.168.1.1
    Address:       192.168.1.1#53

    _kerberos._tcp.internal.domain.tld service = 0 100 88 server1.internal.domain.tld.
    _kerberos._tcp.internal.domain.tld service = 0 100 88 server2.internal.domain.tld.
    ...
    _ldap._tcp.internal.domain.tld     service = 0 100 389 server1.internal.domain.tld.
    _ldap._tcp.internal.domain.tld     service = 0 100 389 server2.internal.domain.tld.
    ...
    Name:   server1.internal.domain.tld
    Address: 192.168.1.1

### NTP configuration {#NTP_configuration}

In an Active Directory domain, more specifically for Kerberos ticketing, it is imperative that time is synchronized with all other hosts on the network. A margin of error no more than five minutes is required. For the example domain configuration, an appropriate `/etc/ntp.conf` file should have the following contents (be sure to replace **server1**, **server2**, and **internal.domain.tld** with appropriate values for your network):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ntp.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# Use your domain's NTP servers 
server server1.internal.domain.tld
server server2.internal.domain.tld

# Restrictions
restrict default kod limited nomodify nopeer noquery notrap
restrict 127.0.0.1
restrict ::1

# Location of drift file
driftfile /var/lib/ntp/ntpd.drift
```

Enable and start the `ntpd.service` unit.

### Kerberos configuration {#Kerberos_configuration}

The Samba documentation recommends a minimal Kerberos configuration, with just enough information in the **\[libdefaults\]** section to hand off the work of discovering domain details to DNS. Unfortunately, this does not work well in practice. Continuing with the example domain configuration, modify the `/etc/krb5.conf` file with the following contents (be sure to replace instances of **INTERNAL**, **internal.domain.tld**, **SERVER1**, and **INTERNAL.DOMAIN.TLD** with appropriate values for your network):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/krb5.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[libdefaults]
   default_realm = INTERNAL.DOMAIN.TLD
   dns_lookup_realm = false
   dns_lookup_kdc = true

[realms]
   INTERNAL.DOMAIN.TLD = {
      kdc = SERVER1.INTERNAL.DOMAIN.TLD
      default_domain = INTERNAL.DOMAIN.TLD
      admin_server = SERVER1.INTERNAL.DOMAIN.TLD
   }
   INTERNAL = {
      kdc = SERVER1.INTERNAL.DOMAIN.TLD
      default_domain = INTERNAL.DOMAIN.TLD
      admin_server = SERVER1.INTERNAL.DOMAIN.TLD
   }

[domain_realm]
    .internal.domain.tld = INTERNAL.DOMAIN.TLD

[appdefaults]
    pam = {
        ticket_lifetime = 1d
        renew_lifetime = 1d
        forwardable = true
        proxiable = false
        minimum_uid = 1
    }
```

### Samba configuration {#Samba_configuration}

#### Base Samba configuration file {#Base_Samba_configuration_file}

A default installation of [samba](https://archlinux.org/packages/?name=samba) does not ship with an example `/etc/samba/smb.conf` file. For our example domain configuration, use the following base settings (replace instances of **INTERNAL** and **INTERNAL.DOMAIN.TLD** with appropriate values for your network):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[global]
   workgroup = INTERNAL
   security = ADS
   realm = INTERNAL.DOMAIN.TLD

   winbind refresh tickets = Yes
   vfs objects = acl_xattr
   map acl inherit = Yes
   store dos attributes = Yes

   # Allow a single, unified keytab to store obtained Kerberos tickets
   dedicated keytab file = /etc/krb5.keytab
   kerberos method = secrets and keytab

   # Do not require that login usernames include the default domain
   winbind use default domain = yes
```

If you do not wish to share local printers configured in [cups](https://archlinux.org/packages/?name=cups), then add the following to the \[Global\] section of the `/etc/samba/smb.conf` file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Global]
...
   load printers = no
   printing = bsd
   printcap name = /dev/null
   disable spoolss = yes
...
```

The remainder of the configuration depends on whether your domain supports RFC2307 Unix/NFS Attributes. Consult with your domain administrator if unsure.

##### Adding the idmap configuration for domains with RFC2307 extensions {#Adding_the_idmap_configuration_for_domains_with_RFC2307_extensions}

Be certain that the values below do not overlap with system values, and that all users have at least the *uidNubmer* attribute, and that those users\' *PrimaryGroup* has a *gid* attribute. Append to the following to the \[Global\] section of the `/etc/samba/smb.conf` file (replace **INTERNAL** with the NetBIOS domain name):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Global]
...

   # UID/GID mapping for local users
   idmap config * : backend = tdb
   idmap config * : range = 3000-7999

   # UID/GID mapping for domain users
   idmap config INTERNAL : backend = ad
   idmap config INTERNAL : schema_mode = rfc2307
   idmap config INTERNAL : range = 10000-999999
   idmap config INTERNAL : unix_nss_info = yes

   # Template settings for users without ''unixHomeDir'' and ''loginShell'' attributes 
   template shell = /bin/bash
   template homedir = /home/%U

   # Allow offline/cached credentials and ticket refresh
   winbind offline logon = yes
   winbind refresh tickets = yes
...
```

Additionally, if user accounts in AD have a *gidNumber* attribute, you can use it instead of the RID for the user\'s *Primary Group* by appending the following setting (again in the \[Global\] section):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Global]
...
   idmap config INTERNAL:unix_primary_group = yes
...
```

##### Adding the idmap configuration for domains without RFC2307 extensions {#Adding_the_idmap_configuration_for_domains_without_RFC2307_extensions}

If your administrator has not extended the AD schema to include the RFC2307 attributes, use the following idmap configuration in the \[Global\] section of the `/etc/samba/smb.conf` file (replace **INTERNAL** with the NetBIOS domain name):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Global]
...
   # UID/GID mapping for local users
   idmap config * : backend = tdb
   idmap config * : range = 3000-7999

   # UID/GID mapping for domain users
   idmap config INTERNAL : backend = rid
   idmap config INTERNAL : range = 10000-999999

   # Template settings for users
   template shell = /bin/bash
   template homedir = /home/%U

   # Allow offline/cached credentials and ticket refresh
   winbind offline logon = yes
   winbind refresh tickets = yes
...
```

## Joining the domain {#Joining_the_domain}

To join the AD domain, simply issue the following command (be sure to replace **Administrator** with a user that has privileges to join the AD domain).

    # net ads join -U Administrator

## Start the individual Samba services {#Start_the_individual_Samba_services}

Enable and start the `smb.service`, `nmb.service`, and `winbind.service` services.

## Configure NSS {#Configure_NSS}

Modify the `/etc/nsswitch.conf` file to allow Samba to map names to uid and gid:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nsswitch.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
passwd: files winbind mymachines systemd
group: files winbind mymachines systemd
...
```

### Testing NSS {#Testing_NSS}

Verify connectivity by listing the AD domain users and groups that system is aware of:

    # wbinfo -u
    # wbinfo -g

You should get a list of AD users followed by AD groups.

## Configuring PAM authentication {#Configuring_PAM_authentication}

Rather than configuring options directly in the *Linux-PAM* configuration files, set defaults for the *pam_winbind* module in `/etc/security/pam_winbind.conf`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/security/pam_winbind.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Global]
   debug = no
   debug_state = no
   try_first_pass = yes
   krb5_auth = yes
   krb5_ccache_type = FILE:/run/user/%u/krb5cc
   cached_login = yes
   silent = no
   mkhomedir = yes
```

For most services, it will be sufficient to modify only the `/etc/pam.d/system-auth` file. Any configuration for programs that do not include this file will also need to be modified directly. Create a backup of the `/etc/pam.d/system-auth` file and use the following configuration:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pam.d/system-auth
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#%PAM-1.0

auth       required                    pam_faillock.so      preauth
# Optionally use requisite above if you do not want to prompt for the password
# on locked accounts.
-auth      [success=3 default=ignore]  pam_systemd_home.so
auth       [success=2 default=ignore]  pam_winbind.so
auth       [success=1 default=bad]     pam_unix.so          try_first_pass nullok
auth       [default=die]               pam_faillock.so      authfail
auth       optional                    pam_permit.so
auth       required                    pam_env.so
auth       required                    pam_faillock.so      authsucc
# If you drop the above call to pam_faillock.so the lock will be done also
# on non-consecutive authentication failures.

-account   [success=2 default=ignore]  pam_systemd_home.so
account    [success=1 default=ignore]  pam_winbind.so
account    required                    pam_unix.so
account    optional                    pam_permit.so
account    required                    pam_time.so

-password  [success=2 default=ignore]  pam_systemd_home.so
password   [success=1 default=ignore]  pam_winbind.so
password   required                    pam_unix.so          try_first_pass nullok shadow sha512
password   optional                    pam_permit.so

-session   optional                    pam_systemd_home.so
session    required                    pam_mkhomedir.so skel=/etc/skel/ umask=0022
session    required                    pam_limits.so
session    required                    pam_winbind.so
session    required                    pam_unix.so
session    optional                    pam_permit.so
```

If you have other services that do not include the `/etc/pam.d/system-auth` file, modify the configuration to mirror all *pam_unix.so* entries for *pam_winbind.so* and change all *required* to *sufficient*. A good example is the su configuration. Create a backup of the `/etc/pam.d/su` file and use the following in its place:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pam.d/su
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#%PAM-1.0

auth      sufficient  pam_rootok.so
# Uncomment the following line to implicitly trust users in the "wheel" group.
#auth     required    pam_wheel.so   trust use_uid
# Uncomment the following line to require a user to be in the "wheel" group.
#auth     required    pam_wheel.so    use_uid
auth      sufficient  pam_winbind.so
auth      required    pam_unix.so
account   sufficient  pam_winbind.so
account   required    pam_unix.so
session   sufficient  pam_winbind.so
session   required    pam_unix.so
```

The above pam_winbind configuration will not use the default location of the Kerberos ticket (`KRB5CCNAME`), which is at `/tmp/krb5cc_`*`UID`*. Instead, it stores the automatically refreshed Kerberos ticket to `/run/user/`*`UID`*`/krb5cc`. Append the following to your krb5.conf to let Kerberos know your new location:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/krb5.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[libdefaults]
   ...
   default_ccache_name = /run/user/%{uid}/krb5cc
   ...
```

To test your changes, start a **new** console or ssh session (do not exit your existing session until you have tested thoroughly) and try to login using the AD credentials. The domain name is optional, as this was set in the Winbind configuration as \'default realm\'. Please note that in the case of ssh, you will need to modify the `/etc/ssh/sshd_config` file to allow kerberos authentication (see below).

Run **klist** to verify that you have received a kerberos ticket. You should see something similar to:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ klist
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Ticket cache: FILE:/run/user/20000/krb5cc
Default principal: administrator@INTERNAL.DOMAIN.TLD

Valid starting       Expires              Service principal
12/25/2020 03:35:21  12/25/2020 13:35:21  krbtgt/INTERNAL.DOMAIN.TLD@INTERNAL.DOMAIN.TLD
        renew until 12/26/2020 03:35:15
```

Finally, you should test login as both the root user and a local unprivileged user before logging out of your existing (working) session.

## Old Wiki Article {#Old_Wiki_Article}

Active Directory serves as a central location for network administration and security. It is responsible for authenticating and authorizing all users and computers within a Windows domain network, assigning and enforcing security policies for all computers in a network and installing or updating software on network computers. For example, when a user logs into a computer that is part of a Windows domain, it is Active Directory that verifies their password and specifies whether they are a system administrator or normal user. Server computers on which Active Directory is running are called domain controllers.

Active Directory uses [Lightweight Directory Access Protocol (LDAP)](https://en.wikipedia.org/wiki/Ldap "wikipedia:Ldap") versions 2 and 3, Microsoft\'s version of [Kerberos](../en/Kerberos.html "Kerberos") and DNS.

### Terminology {#Terminology}

If you are not familiar with Active Directory, there are a few keywords that are helpful to know.

-   **Domain** : The name used to group computers and accounts.
-   **SID** : Each computer that joins the domain as a member must have a unique SID or System Identifier.
-   **SMB** : Server Message Block.
-   **NETBIOS**: Network naming protocol used as an alternative to DNS. Mostly legacy, but still used in Windows Networking.
-   **WINS**: Windows Information Naming Service. Used for resolving Netbios names to windows hosts.
-   **Winbind**: Protocol for windows authentication.

### Active Directory configuration {#Active_Directory_configuration}

This section works with the default configuration of Windows Server 2012 R2.

#### ~~GPO considerations~~ {#GPO_considerations}

Digital signing is enabled by default in Windows Server, and must be enabled at both the client and server level. For certain versions of Samba, Linux clients may experience issues connecting to the domain and/or shares. It is recommended you add the following parameters to your `smb.conf` file:

    client signing = auto 
    server signing = auto

If that is not successful, you can disable *Digital Sign Communication (Always)* in the AD group policies. In your AD Group Policy editor, locate:

Under *Local policies \> Security policies \> Microsoft Network Server \> Digital sign communication (Always)* activate *define this policy* and use the *disable* radio button.

If you use Windows Server 2008 R2, you need to modify that in *GPO for Default Domain Controller Policy \> Computer Setting \> Policies \> Windows Setting \> Security Setting \> Local Policies \> Security Option \> Microsoft network client: Digitally sign communications (always)*.

Please note that disabling this GPO affects the security of all members of the domain.

### ~~Linux host configuration~~ {#Linux_host_configuration}

The next few steps will begin the process of configuring the Host. You will need root or sudo access to complete these steps.

#### ~~Installation~~ {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the following packages:

-   [samba](https://archlinux.org/packages/?name=samba), see also [Samba](../en/Samba.html "Samba")
-   [pam-krb5](https://archlinux.org/packages/?name=pam-krb5)
-   [ntp](https://archlinux.org/packages/?name=ntp) or [openntpd](https://archlinux.org/packages/?name=openntpd), see also [NTPd](../en/Network_Time_Protocol_daemon.html "NTPd") or [OpenNTPD](../en/OpenNTPD.html "OpenNTPD")

#### ~~Updating DNS~~ {#Updating_DNS}

Active Directory is heavily dependent upon DNS. You will need to update `/etc/resolv.conf` to use one or more of the Active Directory domain controllers:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/resolv.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
nameserver <IP1>
nameserver <IP2>
```

Replacing \<IP1\> and \<IP2\> with valid IP addresses for the AD servers. If your AD domains do not permit DNS forwarding or recursion, you may need to add additional resolvers.

**Note**

-   The DNS entry 127.0.0.53 in the /etc/resolv.conf file refers to the local DNS resolver provided by systemd-resolved. If you have configured your DNS Servers using Network manager this step is unnecessary and can cause issues if you modify the resolv.conf as suggested.
-   If your machine dual boots Windows and Linux, you should use a different DNS hostname and netbios name for the linux configuration if both operating systems will be members of the same domain.

#### ~~Configuring NTP~~ {#Configuring_NTP}

Read [System time#Time synchronization](../en/System_time.html#Time_synchronization "System time") to configure an NTP service.

On the NTP servers configuration, use the IP addresses for the AD servers, as they typically run NTP as a service. Alternatively, you can use other known NTP servers provided the Active directory servers sync to the same stratum.

Ensure that the service is configured to sync the time automatically very early on startup.

#### ~~Kerberos~~ {#Kerberos}

Let us assume that your AD is named example.com. Let us further assume your AD is ruled by two domain controllers, the primary and secondary one, which are named PDC and BDC, pdc.example.com and bdc.example.com respectively. Their IP adresses will be 192.168.1.2 and 192.168.1.3 in this example. Take care to watch your syntax; upper-case is very important here.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/krb5.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[libdefaults]
        default_realm   =   EXAMPLE.COM
    clockskew   =   300
    ticket_lifetime =   1d
        forwardable     =       true
        proxiable       =       true
        dns_lookup_realm =      true
        dns_lookup_kdc  =       true
    
[realms]
    EXAMPLE.COM = {
        kdc     =   PDC.EXAMPLE.COM
        kdc     =   PDC2.EXAMPLE.COM
        admin_server = PDC.EXAMPLE.COM
        admin_server = PDC2.EXAMPLE.COM
        default_domain = EXAMPLE.COM
    }
    
[domain_realm]
        .kerberos.server = EXAMPLE.COM
    .example.com = EXAMPLE.COM
    example.com = EXAMPLE.COM
    example = EXAMPLE.COM

[appdefaults]
    pam = {
    ticket_lifetime     = 1d
    renew_lifetime      = 1d
    forwardable         = true
    proxiable       = false
    retain_after_close  = false
    minimum_uid         = 0
    debug           = false
    }

[logging]
    default         = FILE:/var/log/krb5libs.log
    kdc             = FILE:/var/log/kdc.log
        admin_server            = FILE:/var/log/kadmind.log
```

**Note** Heimdal 1.3.1 deprecated DES encryption which is required for AD authentication before Windows Server 2008. You will probably have to add

    allow_weak_crypto = true

to the `[libdefaults]` section.

##### ~~Creating a Kerberos ticket~~ {#Creating_a_Kerberos_ticket}

**Note** The keys and commands are user specific: sudo will be root, so your non-elevated account can connect to a different AD user with a separate key. If you only have one domain, it is not necessary to type \@EXAMPLE.COM

Now you can query the AD domain controllers and request a kerberos ticket (**uppercase is necessary**):

    kinit administrator@EXAMPLE.COM

**Note** The suggested `smb.conf`, including `winbind use default domain = yes` cannot use `@EXAMPLE.COM` in the username. `kinit administrator` will bring in the `DOMAINNAME` from `smb.conf`.

You can use any username that has rights as a Domain Administrator.

##### ~~Validating the Ticket~~ {#Validating_the_Ticket}

Run **klist** to verify you did receive the token. You should see something similar to:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# klist
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
 Ticket cache: FILE:/tmp/krb5cc_0
 Default principal: administrator@EXAMPLE.COM
 
 Valid starting    Expires           Service principal 
 02/04/12 21:27:47 02/05/12 07:27:42 krbtgt/EXAMPLE.COM@EXAMPLE.COM
         renew until 02/05/12 21:27:47
```

#### ~~pam_winbind.conf~~

If you get errors stating that /etc/security/pam_winbind.conf was not found, create the file and add the following:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/security/pam_winbind.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[global]
  debug = no
  debug_state = no
  try_first_pass = yes
  krb5_auth = yes
  krb5_ccache_type = FILE
  cached_login = yes
  silent = no
  mkhomedir = yes
```

With this setup, winbind will create user keytabs on the fly (krb5_ccache_type = FILE) at login and maintain them. You can verify this by simply running klist in a shell after logging in as an AD user but without needing to run kinit. You may need to set additional permissions on /etc/krb5.keytab eg 640 instead of 600 to get this to work (see [FS#52621](https://bugs.archlinux.org/task/52621) for example)

#### ~~Samba~~ {#Samba}

Samba is a free software re-implementation of the SMB/CIFS networking protocol. It also includes tools for Linux machines to act as Windows networking servers and clients.

**Note** The configuration can vary greatly depending on how the Windows environment is deployed. Be prepared to troubleshoot and research

In this section, we will focus on getting Authentication to work first by editing the \'Global\' section first. Later, we will go back and add shares.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Global]
  netbios name = MYARCHLINUX
  workgroup = EXAMPLE
  realm = EXAMPLE.COM
  server string = %h Arch Linux Host
  security = ads
  encrypt passwords = yes
  password server = pdc.example.com
  client signing = auto
  server signing = auto

  idmap config * : backend = tdb
  idmap config * : range = 10000-20000

  winbind use default domain = Yes
  winbind enum users = Yes
  winbind enum groups = Yes
  winbind nested groups = Yes
  winbind separator = +
  winbind refresh tickets = yes
  winbind offline logon = yes
  winbind cache time = 300

  template shell = /bin/bash
  template homedir = /home/%D/%U
   
  preferred master = no
  dns proxy = no
  wins server = pdc.example.com
  wins proxy = no

  inherit acls = Yes
  map acl inherit = Yes
  acl group control = yes

  load printers = no
  debug level = 3
  use sendfile = no
```

#### ~~Join the domain~~ {#Join_the_domain}

You need an AD Administrator account to do this. Let us assume this is named Administrator. The command is \'net ads join\'

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# net ads join -U Administrator
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Administrator's password: xxx
Using short domain name -- EXAMPLE
Joined 'MYARCHLINUX' to realm 'EXAMPLE.COM'
```

### ~~Starting and testing services~~ {#Starting_and_testing_services}

#### ~~Starting Samba~~ {#Starting_Samba}

Hopefully, you have not rebooted yet! Fine. If you are in an X-session, quit it, so you can test login into another console, while you are still logged in.

Enable and start the individual Samba daemons `smbd.service`, `nmbd.service`, and `winbindd.service`.

**Note** In [samba](https://archlinux.org/packages/?name=samba) 4.8.0-1, the Samba daemon units have been renamed from `smbd.service`, `nmbd.service`, and `winbindd.service` to `smb.service`, `nmb.service`, and `winbind.service`.

Next we will need to modify the NSSwitch configuration, which tells the Linux host how to retrieve information from various sources and in which order to do so. In this case, we are appending Active Directory as additional sources for Users, Groups, and Hosts.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nsswitch.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
 passwd:            files winbind
 shadow:            files winbind
 group:             files winbind 
 
 hosts:             files dns wins
```

#### ~~Testing Winbind~~ {#Testing_Winbind}

Let us check if winbind is able to query the AD. The following command should return a list of AD users:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# wbinfo -u
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
administrator
guest
krbtgt
test.user
```

-   Note we created an Active Directory user called \'test.user\' on the domain controller

We can do the same for AD groups:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# wbinfo -g
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
domain computers
domain controllers
schema admins
enterprise admins
cert publishers
domain admins
domain users
domain guests
group policy creator owners
ras and ias servers
allowed rodc password replication group
denied rodc password replication group
read-only domain controllers
enterprise read-only domain controllers
dnsadmins
dnsupdateproxy
```

#### ~~Testing nsswitch~~ {#Testing_nsswitch}

To ensure that our host is able to query the domain for users and groups, we test nsswitch settings by issuing the \'getent\' command.

The following output shows what a stock Arch Linux install looks like:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# getent passwd
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/bin/false
daemon:x:2:2:daemon:/sbin:/bin/false
mail:x:8:12:mail:/var/spool/mail:/bin/false
ftp:x:14:11:ftp:/srv/ftp:/bin/false
http:x:33:33:http:/srv/http:/bin/false
nobody:x:99:99:nobody:/:/bin/false
dbus:x:81:81:System message bus:/:/bin/false
ntp:x:87:87:Network Time Protocol:/var/empty:/bin/false
avahi:x:84:84:avahi:/:/bin/false
administrator:*:10001:10006:Administrator:/home/EXAMPLE/administrator:/bin/bash
guest:*:10002:10007:Guest:/home/EXAMPLE/guest:/bin/bash
krbtgt:*:10003:10006:krbtgt:/home/EXAMPLE/krbtgt:/bin/bash
test.user:*:10000:10006:Test User:/home/EXAMPLE/test.user:/bin/bash
```

And for groups:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# getent group
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
root:x:0:root
bin:x:1:root,bin,daemon
daemon:x:2:root,bin,daemon
sys:x:3:root,bin
adm:x:4:root,daemon
tty:x:5:
disk:x:6:root
lp:x:7:daemon
mem:x:8:
kmem:x:9:
wheel:x:10:root
ftp:x:11:
mail:x:12:
uucp:x:14:
log:x:19:root
utmp:x:20:
locate:x:21:
rfkill:x:24:
smmsp:x:25:
http:x:33:
games:x:50:
network:x:90:
video:x:91:
audio:x:92:
optical:x:93:
floppy:x:94:
storage:x:95:
scanner:x:96:
power:x:98:
nobody:x:99:
users:x:100:
dbus:x:81:
ntp:x:87:
avahi:x:84:
domain computers:x:10008:
domain controllers:x:10009:
schema admins:x:10010:administrator
enterprise admins:x:10011:administrator
cert publishers:x:10012:
domain admins:x:10013:test.user,administrator
domain users:x:10006:
domain guests:x:10007:
group policy creator owners:x:10014:administrator
ras and ias servers:x:10015:
allowed rodc password replication group:x:10016:
denied rodc password replication group:x:10017:krbtgt
read-only domain controllers:x:10018:
enterprise read-only domain controllers:x:10019:
dnsadmins:x:10020:
dnsupdateproxy:x:10021:
```

#### Testing Samba commands {#Testing_Samba_commands}

Try out some net commands to see if Samba can communicate with AD:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# net ads info
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[2012/02/05 20:21:36.473559,  0] param/loadparm.c:7599(lp_do_parameter)
  Ignoring unknown parameter "idmapd backend"
LDAP server: 192.168.1.2
LDAP server name: PDC.example.com
Realm: EXAMPLE.COM
Bind Path: dc=EXAMPLE,dc=COM
LDAP port: 389
Server time: Sun, 05 Feb 2012 20:21:33 CST
KDC server: 192.168.1.2
Server time offset: -3
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# net ads lookup
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[2012/02/05 20:22:39.298823,  0] param/loadparm.c:7599(lp_do_parameter)
  Ignoring unknown parameter "idmapd backend"
Information for Domain Controller: 192.168.1.2

Response Type: LOGON_SAM_LOGON_RESPONSE_EX
GUID: 2a098512-4c9f-4fe4-ac22-8f9231fabbad
Flags:
        Is a PDC:                                   yes
        Is a GC of the forest:                      yes
        Is an LDAP server:                          yes
        Supports DS:                                yes
        Is running a KDC:                           yes
        Is running time services:                   yes
        Is the closest DC:                          yes
        Is writable:                                yes
        Has a hardware clock:                       yes
        Is a non-domain NC serviced by LDAP server: no
        Is NT6 DC that has some secrets:            no
        Is NT6 DC that has all secrets:             yes
Forest:                 example.com
Domain:                 example.com
Domain Controller:      PDC.example.com
Pre-Win2k Domain:       EXAMPLE
Pre-Win2k Hostname:     PDC
Server Site Name :              Office
Client Site Name :              Office
NT Version: 5
LMNT Token: ffff
LM20 Token: ffff
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# net ads status -U administrator%password | less
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
objectClass: computer
cn: myarchlinux
distinguishedName: CN=myarchlinux,CN=Computers,DC=leafscale,DC=inc
instanceType: 4
whenCreated: 20120206043413.0Z
whenChanged: 20120206043414.0Z
uSNCreated: 16556
uSNChanged: 16563
name: myarchlinux
objectGUID: 2c24029c-8422-42b2-83b3-a255b9cb41b3
userAccountControl: 69632
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 129729780312632000
localPolicyFlags: 0
pwdLastSet: 129729764538848000
primaryGroupID: 515
objectSid: S-1-5-21-719106045-3766251393-3909931865-1105
...<snip>...
```

### ~~Configuring PAM~~ {#Configuring_PAM}

Now we will change various rules in PAM to allow Active Directory users to use the system for things like login and sudo access. When changing the rules, note the order of these items and whether they are marked as **required** or **sufficient** is critical to things working as expected. You should not deviate from these rules unless you know how to write PAM rules.

In case of logins, PAM should first ask for AD accounts, and for local accounts if no matching AD account was found. Therefore, we add entries to include `pam_winbind.so` into the authentication process.

The Arch Linux PAM configuration keeps the central auth process in `/etc/pam.d/system-auth`. Starting with the stock configuration from `pambase`, change it like this:

#### ~~system-auth~~

##### ~~\"auth\" section~~ {#\"auth\"_section}

Find the line:

    auth required pam_unix.so ...

Delete it, and replace with:

    auth [success=1 default=ignore] pam_localuser.so
    auth [success=2 default=die] pam_winbind.so
    auth [success=1 default=die] pam_unix.so nullok
    auth requisite pam_deny.so

##### ~~\"account\" section~~ {#\"account\"_section}

Find the line:

    account required pam_unix.so

Keep it, and add this below:

    account [success=1 default=ignore] pam_localuser.so
    account required pam_winbind.so

##### ~~\"password\" section~~ {#\"password\"_section}

Find the line:

    password required pam_unix.so ...

Delete it, and replace with:

    password [success=1 default=ignore] pam_localuser.so
    password [success=2 default=die] pam_winbind.so
    password [success=1 default=die] pam_unix.so sha512 shadow
    password requisite pam_deny.so

##### ~~\"session\" section~~ {#\"session\"_section}

Find the line:

    session required pam_unix.so

Keep it, and add this line immediately above it:

    session required pam_mkhomedir.so skel=/etc/skel/ umask=0022

Below the pam_unix line, add these:

    session [success=1 default=ignore] pam_localuser.so
    session required pam_winbind.so

#### ~~passwd~~

##### ~~\"password\" section~~ {#\"password\"_section_2}

In order for logged-in Active Directory users to be able to change their passwords with the \'passwd\' command, the file `/etc/pam.d/passwd` must include the information from system-auth.

Find the line:

    password required pam_unix.so sha512 shadow nullok

Delete it, and replace with:

    password include system-auth

#### ~~Testing login~~ {#Testing_login}

Now, start a new console session (or ssh) and try to login using the AD credentials. The domain name is optional, as this was set in the Winbind configuration as \'default realm\'. Please note that in the case of ssh, you will need to modify the `/etc/ssh/sshd_config` file to allow kerberos authentication `(KerberosAuthentication yes)`.

    test.user
    EXAMPLE+test.user

Both should work. You should notice that `/home/example/test.user` will be automatically created. **Log into another session using an linux account. Check that you still be able to log in as root - but keep in mind to be logged in as root in at least one session!**

### Configuring Shares {#Configuring_Shares}

Earlier we skipped configuration of the shares. Now that things are working, go back to `/etc/samba/smb.conf`, and add the exports for the host that you want available on the windows network.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[MyShare]
  comment = Example Share
  path = /srv/exports/myshare
  read only = no
  browseable = yes
  valid users = @NETWORK+"Domain Admins" NETWORK+test.user
```

In the above example, the keyword **NETWORK** is to be used. Do not mistakenly substitute this with your domain name. For adding groups, prepend the \'@\' symbol to the group. Note that `Domain Admins` is encapsulated in quotes so Samba correctly parses it when reading the configuration file.

### Adding a machine keytab file and activating password-free kerberized ssh to the machine {#Adding_a_machine_keytab_file_and_activating_password-free_kerberized_ssh_to_the_machine}

This explains how to generate a machine keytab file which you will need e.g. to enable password-free kerberized ssh to your machine from other machines in the domain. The scenario in mind is that you have a bunch of systems in your domain and you just added a server/workstation using the above description to your domain onto which a lot of users need to ssh in order to work - e.g. GPU workstation or an OpenMP compute node, etc. In this case you might not want to type your password every time you log in. On the other hand the key authentication used by many users in this case can not give you the necessary credentials to e.g. mount kerberized NFSv4 shares. So this will help you to enable password-free logins from your clients to the machine in question using kerberos ticket forwarding.

#### ~~Creating a machine key tab file~~ {#Creating_a_machine_key_tab_file}

run \'net ads keytab create -U administrator\' as root to create a machine keytab file in /etc/krb5.keytab. It will prompt you with a warning that we need to enable keytab authentication in our configuration file, so we will do that in the next step. In my case it had problems when a key tab file is already in place - the command just did not come back it hang \... In that case you should rename the existing /etc/krb5.keytab and run the command again - it should work now.

    # net ads keytab create -U administrator

verify the content of your keytab by running:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# klist -k /etc/krb5.keytab
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Keytab name: FILE:/etc/krb5.keytab
KVNO Principal
---- --------------------------------------------------------------------------
   4 host/myarchlinux.example.com@EXAMPLE.COM
   4 host/myarchlinux.example.com@EXAMPLE.COM
   4 host/myarchlinux.example.com@EXAMPLE.COM
   4 host/myarchlinux.example.com@EXAMPLE.COM
   4 host/myarchlinux.example.com@EXAMPLE.COM
   4 host/MYARCHLINUX@EXAMPLE.COM
   4 host/MYARCHLINUX@EXAMPLE.COM
   4 host/MYARCHLINUX@EXAMPLE.COM
   4 host/MYARCHLINUX@EXAMPLE.COM
   4 host/MYARCHLINUX@EXAMPLE.COM
   4 MYARCHLINUX$@EXAMPLE.COM
   4 MYARCHLINUX$@EXAMPLE.COM
   4 MYARCHLINUX$@EXAMPLE.COM
   4 MYARCHLINUX$@EXAMPLE.COM
   4 MYARCHLINUX$@EXAMPLE.COM
```

#### ~~Enabling keytab authentication~~ {#Enabling_keytab_authentication}

Now you need to tell winbind to use the file by adding these lines to the /etc/samba/smb.conf:

     kerberos method = secrets and keytab
     dedicated keytab file = /etc/krb5.keytab

It should look something like this:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/samba/smb.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Global]
  netbios name = MYARCHLINUX
  workgroup = EXAMPLE
  realm = EXAMPLE.COM
  server string = %h Arch Linux Host
  security = ads
  encrypt passwords = yes
  password server = pdc.example.com
  kerberos method = secrets and keytab
  dedicated keytab file = /etc/krb5.keytab

  idmap config * : backend = tdb
  idmap config * : range = 10000-20000

  winbind use default domain = Yes
  winbind enum users = Yes
  winbind enum groups = Yes
  winbind nested groups = Yes
  winbind separator = +
  winbind refresh tickets = yes

  template shell = /bin/bash
  template homedir = /home/%D/%U
   
  preferred master = no
  dns proxy = no
  wins server = pdc.example.com
  wins proxy = no

  inherit acls = Yes
  map acl inherit = Yes
  acl group control = yes

  load printers = no
  debug level = 3
  use sendfile = no
```

[Restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") the `winbindd.service`

Check if everything works by getting a machine ticket for your system by running

    # kinit MYARCHLINUX$ -kt /etc/krb5.keytab

This should not give you any feedback but running \'klist\' should show you sth like:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# klist
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
 Ticket cache: FILE:/tmp/krb5cc_0
 Default principal: MYARCHLINUX$@EXAMPLE.COM
 
 Valid starting    Expires           Service principal 
 02/04/12 21:27:47 02/05/12 07:27:42 krbtgt/EXAMPLE.COM@EXAMPLE.COM
         renew until 02/05/12 21:27:47
```

Some common mistakes here are a) forgetting the trailing \$ or b) ignoring case sensitivity - it needs to look exactly like the entry in the keytab (usually you cannot to much wrong with all capital)

#### Preparing sshd on server {#Preparing_sshd_on_server}

Add these options to the `sshd_config` and [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `sshd.service` after making the changes.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# Change to no to disable s/key passwords
ChallengeResponseAuthentication no

# Kerberos options
KerberosAuthentication yes
#KerberosOrLocalPasswd yes
KerberosTicketCleanup yes
KerberosGetAFSToken yes

# GSSAPI options
GSSAPIAuthentication yes
GSSAPICleanupCredentials yes
```

#### Adding necessary options on client {#Adding_necessary_options_on_client}

First we need to make sure that the tickets on our client are forwardable. This is usually standard but we better check anyways. You have to look for the `forwardable` option and set it to \'true\' in the Kerberos configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/krb5.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
forwardable     =       true
```

Secondly we need to add the following options to the user-specific SSH client configuration file to tell [ssh(1)](https://man.archlinux.org/man/ssh.1) to use these options - alternatively they can be invoked using the `-o` options directly.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
GSSAPIAuthentication yes
GSSAPIDelegateCredentials yes
```

#### Testing the setup {#Testing_the_setup}

On Client:

make sure you have a valid ticket - if in doubt run \'kinit\'

then use ssh to connect to you machine

    $ ssh myarchlinux.example.com

you should get connected without needing to enter your password.

if you have key authentication additionally activated then you should perform

    $ ssh -v myarchlinux.example.com

to see which authentication method it actually uses.

For debugging you can enable DEBUG3 on the server and look into the journal using [journalctl](../en/Systemd/Journal.html "Journalctl").

#### Nifty fine-tuning for complete password-free kerberos handling. {#Nifty_fine-tuning_for_complete_password-free_kerberos_handling.}

In case your clients are not using domain accounts on their local machines (for whatever reason) it can be hard to actually teach them to kinit before ssh to the workstation. Therefore I came up with a nice workaround:

### Generating user Keytabs which are accepted by AD {#Generating_user_Keytabs_which_are_accepted_by_AD}

On a system let the user run:

    ktutil
    addent -password -p ''username@EXAMPLE.COM'' -k 1 -e RC4-HMAC
    - enter password for username -
    wkt username.keytab
    q

Now test the file by invoking:

    $ kinit username@EXAMPLE.COM -kt username.keytab

It should not prompt you to give your password nor should it give any other feedback. If it worked you are basically done - just put the line above into e.g your [shell configuration file](../en/Command-line_shell.html#Configuration_files "Command-line shell") - you can now get kerberos tickets without typing a password and with that you can connect to your workstation without typing a password while being completely kerberized and able to authenticate against NFSv4 and CIFS via tickets.

#### Nice to know {#Nice_to_know}

The file \'username.keytab\' is not machinespecific and can therefore be copied around. E.g. we created the files on a linux machine and copied them to our Mac clients as the commands on Macs are different \...

### See also {#See_also}

-   [Wikipedia - Active Directory](https://en.wikipedia.org/wiki/Active_Directory "wikipedia:Active Directory")
-   [Wikipedia - Samba](https://en.wikipedia.org/wiki/Samba_(software) "wikipedia:Samba (software)")
-   [Wikipedia - Kerberos](https://en.wikipedia.org/wiki/Kerberos_(protocol) "wikipedia:Kerberos (protocol)")
-   [Samba - Documentation](https://www.samba.org/samba/docs)
-   [Directory on Samba Wiki](https://wiki.samba.org/index.php?search=active+directory%7CActive)
-   [Samba Wiki - Samba, Active Directory & LDAP](https://wiki.samba.org/index.php?title=Samba,_Active_Directory_%26_LDAP&direction=next&oldid=4082)
-   [smb.conf(5)](https://man.archlinux.org/man/smb.conf.5)

#### Using SSSD {#Using_SSSD}

[sssd](https://archlinux.org/packages/?name=sssd) can be used instead of Samba to integrate with AD. See [SSSD documentation](https://sssd.io/docs/ad/ad-introduction.html).

#### Commercial solutions {#Commercial_solutions}

-   Centrify
-   Likewise

#### OpenSource version {#OpenSource_version}

-   [PowerBroker Identity Services Open](https://github.com/BeyondTrust/pbis-open/): formerly Likewise acquired by BeyondTrust
-   [Centrify Express for Linux](https://www.centrify.com/express/linux/)
