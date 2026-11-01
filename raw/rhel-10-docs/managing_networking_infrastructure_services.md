---
{"title": "Managing networking infrastructure services", "guide": "managing_networking_infrastructure_services", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_networking_infrastructure_services/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Managing networking infrastructure services {#managing-networking-infrastructure-services .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## A guide to managing networking infrastructure services {#a-guide-to-managing-networking-infrastructure-services .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140640921023456)

**Abstract**

This document describes how to set up and manage networking core infrastructure services, such as DNS and DHCP, on Red Hat Enterprise Linux.

------------------------------------------------------------------------

## [Providing feedback on Red Hat documentation](#providing-feedback-on-red-hat-documentation) {#providing-feedback-on-red-hat-documentation .title}

We are committed to providing high-quality documentation and value your feedback. To help us improve, you can submit suggestions or report errors through the Red Hat Jira tracking system.

**Procedure**

1.  Log in to the [Jira](https://redhat.atlassian.net/jira/software/c/projects/RHELDOCS/issues/) website.

    If you do not have an account, select the option to create one.

2.  Click **Create** in the top navigation bar.

3.  Enter a descriptive title in the **Summary** field.

4.  Enter your suggestion for improvement in the **Description** field. Include links to the relevant parts of the documentation.

5.  Click **Create** at the bottom of the window.

## [Chapter 1. Configuring a BIND DNS server](#setting-up-and-configuring-a-bind-dns-server) {#chapter-1.-configuring-a-bind-dns-server .title}

To manage Domain Name System (DNS) services, configure the BIND DNS server. BIND is fully compliant with the Internet Engineering Task Force (IETF) DNS standards and draft standards.

You can use BIND as a caching DNS server in the local network, an authoritative DNS server for zones, and a secondary server to provide high availability for zones.

### [1.1. Considerations about protecting BIND with SELinux or running it in a change-root environment](#considerations-about-protecting-bind-with-selinux-or-running-it-in-a-change-root-environment) {#considerations-about-protecting-bind-with-selinux-or-running-it-in-a-change-root-environment .title}

To secure a BIND installation, you can run the `named`{.literal} service without a change-root (chroot) environment or the `named-chroot`{.literal} service in a change-root environment.

-   Run the `named`{.literal} service without a change-root environment. In this case, SELinux in the `enforcing`{.literal} mode prevents exploitation of known BIND security vulnerabilities. By default, Red Hat Enterprise Linux (RHEL) uses SELinux in the `enforcing`{.literal} mode.

    Important

    Running BIND on RHEL with SELinux in the `enforcing`{.literal} mode is more secure than running BIND in a change-root environment.

-   Run the `named-chroot`{.literal} service in a change-root environment.

    By using the change-root feature, you can define that the root directory of a process and its sub-processes is different from the `/`{.literal} directory. When you start the `named-chroot`{.literal} service, BIND switches its root directory to `/var/named/chroot/`{.literal}. As a consequence, the service uses `mount --bind`{.literal} command to make the files and directories listed in `/etc/named-chroot.files`{.literal} available in `/var/named/chroot/`{.literal}, and the process has no access to files outside of `/var/named/chroot/`{.literal}.

If you want to use BIND:

-   In the normal mode, use the `named`{.literal} service.
-   In the change-root environment, use the `named-chroot`{.literal} service. For this, install the `named-chroot`{.literal} package.

### [1.2. Configuring BIND as a caching DNS server](#configuring-bind-as-a-caching-dns-server) {#configuring-bind-as-a-caching-dns-server .title}

To resolve and cache successful and failed lookups, and answer requests to the same records from its cache, configure BIND as a caching DNS server. This improves the speed of DNS lookups.

**Prerequisites**

-   You have the administrative privileges.
-   The IP address of the server is static.

**Procedure**

1.  Install the `bind`{.literal} and `bind-utils`{.literal} packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install bind bind-utils
    ```

2.  If you want to run BIND in a change-root environment install the `bind-chroot`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install bind-chroot
    ```

    Note that running BIND on a host with SELinux in `enforcing`{.literal} mode, which is default, is more secure.

3.  Edit the `/etc/named.conf`{.literal} file, and make the following changes in the `options`{.literal} statement:

    a.  Update the `listen-on`{.literal} and `listen-on-v6`{.literal} statements to specify on which IPv4 and IPv6 interfaces BIND should listen:

        ``` {.language-plaintext tabindex="-1"}
        listen-on port 53 { 127.0.0.1; 192.0.2.1; };
        ```

        ``` {.language-plaintext tabindex="-1"}
        listen-on-v6 port 53 { ::1; 2001:db8:1::1; };
        ```

    b.  Update the `allow-query`{.literal} statement to configure from which IP addresses and ranges clients can query this DNS server:

        ``` {.language-plaintext tabindex="-1"}
        allow-query { localhost; 192.0.2.0/24; 2001:db8:1::/64; };
        ```

    c.  Add an `allow-recursion`{.literal} statement to define from which IP addresses and ranges BIND accepts recursive queries:

        ``` {.language-plaintext tabindex="-1"}
        allow-recursion { localhost; 192.0.2.0/24; 2001:db8:1::/64; };
        ```

        Warning

        Do not allow recursion on public IP addresses of the server. Otherwise, the server can become part of large-scale DNS amplification attacks.

    d.  By default, BIND resolves queries by recursively querying from the root servers to an authoritative DNS server. However, you can configure BIND to forward queries to other DNS servers, such as the ones of your provider. In this case, add a `forwarders`{.literal} statement with the list of IP addresses of the DNS servers that BIND should forward queries to:

        ``` {.language-plaintext tabindex="-1"}
        forwarders { 198.51.100.1; 203.0.113.5; };
        ```

        As a fall-back behavior, BIND resolves queries recursively if the forwarder servers do not respond. To disable this behavior, add a `forward only;`{.literal} statement.

4.  Verify the syntax of the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkconf
    ```

    If the command displays no output, the syntax is correct.

5.  Update the `firewalld`{.literal} rules to allow incoming DNS traffic:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=dns
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

6.  Start and enable BIND:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now named
    ```

    If you want to run BIND in a change-root environment, use the `systemctl enable --now named-chroot`{.literal} command to enable and start the service.

**Verification**

1.  Use the newly set up DNS server to resolve a domain:

    ``` {.language-plaintext tabindex="-1"}
    # dig @localhost www.example.org
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    __www.example.org.__    __86400__    IN    A    __198.51.100.34__

    ;; Query time: __917 msec__
    ...
    ```

    This example assumes that BIND runs on the same host and responds to queries on the `localhost`{.literal} interface.

    After querying a record for the first time, BIND adds the entry to its cache.

2.  Repeat the previous query:

    ``` {.language-plaintext tabindex="-1"}
    # dig @localhost www.example.org
    ```

    ``` {.language-plaintext tabindex="-1"}
    __www.example.org.__    __85332__    IN    A    __198.51.100.34__

    ;; Query time: __1 msec__
    ...
    ```

    Because of the cached entry, further requests for the same record are significantly faster until the entry expires.

    For details, see the `named.conf(5)`{.literal} man page and the `/usr/share/doc/bind/sample/etc/named.conf`{.literal} file on your system.

### [1.3. Configuring logging on a BIND DNS server](#configuring-logging-on-a-bind-dns-server) {#configuring-logging-on-a-bind-dns-server .title}

To write different events with a defined severity to separate files, configure logging on a BIND DNS server. By default for the bind package, the configuration in the `/etc/named.conf`{.literal} file uses the `default_debug`{.literal} channel and logs messages to the `/var/named/data/named.run`{.literal} file.

The `default_debug`{.literal} channel only logs entries when the server's debug level is non zero. By using different channels and categories, you can configure BIND to write different events with a defined severity to separate files.

**Prerequisites**

-   You have already configured BIND as a caching name server.
-   You have started the `named`{.literal} or `named-chroot`{.literal} service.

**Procedure**

1.  Edit the `/etc/named.conf`{.literal} file and add `category`{.literal} and `channel`{.literal} phrases to the `logging`{.literal} statement, for example:

    ``` {.language-plaintext tabindex="-1"}
    logging {
        ...

        category notify { zone_transfer_log; };
        category xfer-in { zone_transfer_log; };
        category xfer-out { zone_transfer_log; };
        channel zone_transfer_log {
            file "/var/named/log/transfer.log" versions 10 size 50m;
            print-time yes;
            print-category yes;
            print-severity yes;
            severity info;
         };

         ...
    };
    ```

    In this example configuration

    -   BIND logs messages related to zone transfers to `/var/named/log/transfer.log`{.literal}.
    -   BIND creates up to 10 versions of the log file and rotates them if they reach a maximum size of 50 MB.
    -   The `category`{.literal} phrase defines to which channels BIND sends messages of a category.
    -   The `channel`{.literal} phrase defines the destination of log messages including the number of versions, the maximum file size, and the severity level BIND should log to a channel. Additional settings, such as enabling logging the timestamp, category, and severity of an event are optional, but useful for debugging purposes.

2.  Create the log directory if it does not exist and grant write permissions to the `named`{.literal} user on this directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /var/named/log/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chown named:named /var/named/log/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 700 /var/named/log/
    ```

3.  Verify the syntax of the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkconf
    ```

    No output indicates that the syntax is correct.

4.  Restart BIND:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart named
    ```

    If you run BIND in a change-root environment, use the `systemctl restart named-chroot`{.literal} command to restart the service.

**Verification**

-   Display the content of the log file:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/named/log/transfer.log
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    __06-Jul-2022 15:08:51.261 xfer-out: info: client @0x7fecbc0b0700 192.0.2.2#36121/key example-transfer-key (example.com): transfer of 'example.com/IN': AXFR started: TSIG example-transfer-key (serial 2022070603)__
    __06-Jul-2022 15:08:51.261 xfer-out: info: client @0x7fecbc0b0700 192.0.2.2#36121/key example-transfer-key (example.com): transfer of 'example.com/IN': AXFR ended__
    ```

    For details, see the `named.conf(5)`{.literal} man page on your system.

### [1.4. Writing BIND access control lists](#writing-bind-acls) {#writing-bind-access-control-lists .title}

Controlling access to certain features of BIND can prevent unauthorized access and attacks, such as denial of service (DoS). BIND access control list (ACL) statements are lists of IP addresses and ranges.

Each ACL has a nickname that you can use in several statements, such as `allow-query`{.literal} that refer to the specified IP addresses and ranges.

Warning

BIND uses only the first matching entry in an ACL. For example, if you define an ACL `{ 192.0.2/24; !192.0.2.1; }`{.literal} and the host with IP address `192.0.2.1`{.literal} connects, BIND grants access even if the second entry excludes this address.

BIND has the following built-in ACLs:

-   `none`{.literal}: Matches no hosts.
-   `any`{.literal}: Matches all hosts.
-   `localhost`{.literal}: Matches the loopback addresses `127.0.0.1`{.literal} and `::1`{.literal}, and the IP addresses of all interfaces on the server that runs BIND.
-   `localnets`{.literal}: Matches the loopback addresses `127.0.0.1`{.literal} and `::1`{.literal}, and all subnets the server that runs BIND is directly connected to.

**Prerequisites**

-   You have configured BIND as a caching name server.
-   The `named`{.literal} or `named-chroot`{.literal} service is running.

**Procedure**

1.  Edit the `/etc/named.conf`{.literal} file and make the following changes:

    a.  Add `acl`{.literal} statements to the file. For example, to create an ACL named `internal-networks`{.literal} for `127.0.0.1`{.literal}, `192.0.2.0/24`{.literal}, and `2001:db8:1::/64`{.literal}, enter:

        ``` {.language-plaintext tabindex="-1"}
        acl internal-networks { 127.0.0.1; 192.0.2.0/24; 2001:db8:1::/64; };
        acl dmz-networks { 198.51.100.0/24; 2001:db8:2::/64; };
        ```

    b.  Use the ACL's nickname in statements that support them, for example:

        ``` {.language-plaintext tabindex="-1"}
        allow-query { internal-networks; dmz-networks; };
        allow-recursion { internal-networks; };
        ```

2.  Verify the syntax of the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkconf
    ```

    No output indicates that the syntax is correct.

3.  Reload BIND:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload named
    ```

    If you run BIND in a change-root environment, use the `systemctl reload named-chroot`{.literal} command to reload the service.

**Verification**

-   Execute an action that triggers a feature, which uses the configured ACL. For example, the ACL allows only recursive queries from the defined IP addresses. In this case, enter the following command on a host that is not within the ACL's definition to try to resolve an external domain:

    ``` {.language-plaintext tabindex="-1"}
    # dig +short @192.0.2.1 www.example.com
    ```

    If the command returns no output, BIND is denied access, and the ACL works. For a verbose output on the client, use the command without `+short`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # dig @192.0.2.1 www.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    ;; WARNING: recursion requested but not available
    ...
    ```

### [1.5. Configuring zones on a BIND DNS server](#configuring-zones-on-a-bind-dns-server) {#configuring-zones-on-a-bind-dns-server .title}

To manage domain name resolution for the `example.com`{.literal} domain, you can configure a zone on a DNS BIND server. A DNS zone is a database with resource records for a specific sub-tree in the domain space.

For example, if you are responsible for the `example.com`{.literal} domain, you can set up a zone for it in BIND. As a result, clients can resolve `www.example.com`{.literal} to the IP address configured in this zone.

#### [1.5.1. The start of authority record in zone files](#the-soa-record-in-zone-files) {#the-start-of-authority-record-in-zone-files .title}

To manage several DNS servers authoritative for a zone and DNS resolvers, you can use the start of authority (SOA) record. This record is essential in a DNS zone.

A SOA record in BIND has the following syntax:

``` {.language-plaintext tabindex="-1"}
name class type mname rname serial refresh retry expire minimum
```

For better readability, you need to split the record in zone files into several lines with comments that start with a semicolon (`;`{.literal}). Note that, if you split a SOA record, parentheses keep the record together:

``` {.language-plaintext tabindex="-1"}
@ IN SOA ns1.example.com. hostmaster.example.com. (
                          2022070601 ; serial number
                          1d         ; refresh period
                          3h         ; retry period
                          3d         ; expire time
                          3h )       ; minimum TTL
```

Important

Note the trailing dot at the end of the fully-qualified domain names (FQDNs). FQDNs consist of several domain labels, separated by dots. Because the DNS root has an empty label, FQDNs end with a dot. Therefore, BIND appends the zone name to names without a trailing dot.

A hostname without a trailing dot, for example, `ns1.example.com`{.literal} expands to `ns1.example.com.example.com.`{.literal}, which is not the correct address of the primary name server.

These are the fields in a SOA record:

-   `name`{.literal}: The name of the zone, the so-called `origin`{.literal}. If you set this field to `@`{.literal}, BIND expands it to the zone name defined in `/etc/named.conf`{.literal}.

-   `class`{.literal}: In SOA records, you must set this field always to Internet (`IN`{.literal}).

-   `type`{.literal}: In SOA records, you must set this field always to `SOA`{.literal}.

-   `mname`{.literal} (master name): The hostname of the primary name server of this zone.

-   `rname`{.literal} (responsible name): The email address of who is responsible for this zone. Note that the format is different. You must replace the at sign (`@`{.literal}) with a dot (`.`{.literal}).

-   `serial`{.literal}: The version number of this zone file. Secondary name servers only update their copies of the zone if the serial number on the primary server is higher.

    The format can be any numeric value. A commonly-used format is `<year><month><day><two_digit_number>`{.literal}. With this format, you can, theoretically, change the zone file up to a hundred times per day.

-   `refresh`{.literal}: The amount of time secondary servers should wait before checking the primary server if the zone update is completed.

-   `retry`{.literal}: The amount of time after that a secondary server retries to query the primary server if the zone updation failed.

-   `expire`{.literal}: The amount of time after that a secondary server stops querying the primary server, if all earlier attempts failed.

-   `minimum`{.literal}: How long resolvers cache negative answers (such as `NXDOMAIN`{.literal} responses) for a zone, as defined in RFC 2308. This value is also known as the negative caching time to live (TTL).

Note

A numeric value in the `refresh`{.literal}, `retry`{.literal}, `expire`{.literal}, and `minimum`{.literal} fields define a time in seconds. However, for better readability, use time suffixes, such as `m`{.literal} for minute, `h`{.literal} for hours, and `d`{.literal} for days. For example, `3h`{.literal} stands for 3 hours.

#### [1.5.2. Configuring a forward zone on a BIND primary server](#setting-up-a-forward-zone-on-a-bind-primary-server) {#configuring-a-forward-zone-on-a-bind-primary-server .title}

To enable mapping domain names to IP addresses and other information, you can set up a forward zone on a BIND primary server. For example, if you are responsible for the domain `example.com`{.literal}, you can set up a forward zone in BIND to resolve names, such as `www.example.com`{.literal}.

**Prerequisites**

-   You have installed the `bind`{.literal} package on the server.
-   You have configured the server to run as a caching name server.
-   The `named`{.literal} or `named-chroot`{.literal} service is running.

**Procedure**

1.  Add a zone definition to the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    zone "example.com" {
        type master;
        file "example.com.zone";
        allow-query { any; };
        allow-transfer { none; };
    };
    ```

    These settings define:

    -   This server is the primary server (`type master`{.literal}) for the `example.com`{.literal} zone.
    -   The `/var/named/example.com.zone`{.literal} file is the zone file. If you set a relative path, as in this example, this path is relative to the directory you set in `directory`{.literal} in the `options`{.literal} statement.
    -   Any host can query this zone. However, you can specify IP ranges or BIND access control list (ACL) nicknames to limit the access.
    -   No host can transfer the zone. Allow zone transfers only when you set up secondary servers and only for the IP addresses of the secondary servers.

2.  Verify the syntax of the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkconf
    ```

    No output indicates that the syntax is correct.

3.  Create the `/var/named/example.com.zone`{.literal} file, for example, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    $TTL 8h
    @ IN SOA ns1.example.com. hostmaster.example.com. (
                              2022070601 ; serial number
                              1d         ; refresh period
                              3h         ; retry period
                              3d         ; expire time
                              3h )       ; minimum TTL

                      IN NS   ns1.example.com.
                      IN MX   10 mail.example.com.

    www               IN A    192.0.2.30
    www               IN AAAA 2001:db8:1::30
    ns1               IN A    192.0.2.1
    ns1               IN AAAA 2001:db8:1::1
    mail              IN A    192.0.2.20
    mail              IN AAAA 2001:db8:1::20
    ```

    This zone file:

    -   Sets the default time-to-live (TTL) value for resource records to 8 hours. Without a time suffix, such as `h`{.literal} for hour, BIND interprets the value as seconds.
    -   Has the required Start of Authority (SOA) resource record with details about the zone.
    -   Sets `ns1.example.com`{.literal} as an authoritative DNS server for this zone. To be functional, a zone requires at least one name server (`NS`{.literal}) record. However, to be compliant with RFC 1912, you require at least two name servers.
    -   Sets `mail.example.com`{.literal} as the mail exchanger (`MX`{.literal}) of the `example.com`{.literal} domain. The numeric value in front of the hostname is the priority of the record. Entries with a lower value have a higher priority.
    -   Sets the IPv4 and IPv6 addresses of `www.example.com`{.literal}, `mail.example.com`{.literal}, and `ns1.example.com`{.literal}.

4.  Set secure permissions on the zone file that allow only the `named`{.literal} group to read it:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:named /var/named/example.com.zone
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 640 /var/named/example.com.zone
    ```

5.  Verify the syntax of the `/var/named/example.com.zone`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkzone example.com /var/named/example.com.zone
    ```

    ``` {.language-plaintext tabindex="-1"}
    zone example.com/IN: loaded serial 2022070601
    OK
    ```

6.  Reload BIND:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload named
    ```

    If you run BIND in a change-root environment, use the `systemctl reload named-chroot`{.literal} command to reload the service.

**Verification**

-   Query different records from the `example.com`{.literal} zone, and verify that the output matches the records you have configured in the zone file:

    ``` {.language-plaintext tabindex="-1"}
    # dig +short @localhost AAAA www.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    2001:db8:1::30
    ```

    ``` {.language-plaintext tabindex="-1"}
    # dig +short @localhost NS example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    ns1.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    # dig +short @localhost A ns1.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    192.0.2.1
    ```

    This example assumes that BIND runs on the same host and responds to queries on the `localhost`{.literal} interface.

**Additional resources**

-   [The SOA record in zone files](#the-soa-record-in-zone-files "1.5.1. The start of authority record in zone files")
-   [Writing BIND ACLs](#writing-bind-acls "1.4. Writing BIND access control lists")
-   [RFC 1912 - Common DNS operational and configuration errors](https://datatracker.ietf.org/doc/html/rfc1912)

#### [1.5.3. Configuring a reverse zone on a BIND primary server](#setting-up-a-reverse-zone-on-a-bind-primary-server) {#configuring-a-reverse-zone-on-a-bind-primary-server .title}

To map IP addresses to names, you can set up a reverse zone on a BIND primary server. For example, if you have the `192.0.2.0/24`{.literal} IP range, you can set up a reverse zone in BIND to resolve IP addresses from this range to hostnames.

Note

If you create a reverse zone for `classful`{.literal} IP addresses for a specific network, name the zone likewise. For example, for the class C network `192.0.2.0/24`{.literal}, the name of the zone is `2.0.192.in-addr.arpa`{.literal}. If you want to create a reverse zone for a different network size, for example `192.0.2.0/28`{.literal}, the name of the zone is `28-2.0.192.in-addr.arpa`{.literal}.

**Prerequisites**

-   You have configured BIND as a caching name server.
-   The `named`{.literal} or `named-chroot`{.literal} service is running.
-   You have administrative privileges.

**Procedure**

1.  Add a zone definition to the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    zone "2.0.192.in-addr.arpa" {
        type master;
        file "2.0.192.in-addr.arpa.zone";
        allow-query { any; };
        allow-transfer { none; };
    };
    ```

    These settings define:

    -   This server is the primary server (`type master`{.literal}) for the `2.0.192.in-addr.arpa`{.literal} reverse zone.
    -   The `/var/named/2.0.192.in-addr.arpa.zone`{.literal} file is the zone file. If you set a relative path, as in this example, this path is relative to the directory you set in `directory`{.literal} in the `options`{.literal} statement.
    -   Any host can query this zone. However, you can specify IP ranges or BIND access control list (ACL) nicknames to limit the access.
    -   No host can transfer the zone. Allow zone transfers only when you set up secondary servers and only for the IP addresses of the secondary servers.

2.  Verify the syntax of the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkconf
    ```

    If the command displays no output, the syntax is correct.

3.  Create the `/var/named/2.0.192.in-addr.arpa.zone`{.literal} file, for example, with the following content:

    ``` {.language-plaintext tabindex="-1"}
    $TTL 8h
    @ IN SOA ns1.example.com. hostmaster.example.com. (
                              2022070601 ; serial number
                              1d         ; refresh period
                              3h         ; retry period
                              3d         ; expire time
                              3h )       ; minimum TTL

                      IN NS   ns1.example.com.

    1                 IN PTR  ns1.example.com.
    30                IN PTR  www.example.com.
    ```

    This zone file:

    -   Sets the default time-to-live (TTL) value for resource records to 8 hours. Without a time suffix, such as `h`{.literal} for hour, BIND interprets the value as seconds.
    -   Has the required Start of Authority (SOA) resource record with details about the zone.
    -   Sets `ns1.example.com`{.literal} as an authoritative DNS server for this reverse zone. To be functional, a zone requires at least one name server (`NS`{.literal}) record. However, to be compliant with RFC 1912, you require at least two name servers.
    -   Sets the pointer (`PTR`{.literal}) record for the `192.0.2.1`{.literal} and `192.0.2.30`{.literal} addresses.

4.  Set secure permissions on the zone file that only allow the `named`{.literal} group to read it:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:named /var/named/2.0.192.in-addr.arpa.zone
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 640 /var/named/2.0.192.in-addr.arpa.zone
    ```

5.  Verify the syntax of the `/var/named/2.0.192.in-addr.arpa.zone`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkzone 2.0.192.in-addr.arpa /var/named/2.0.192.in-addr.arpa.zone
    ```

    ``` {.language-plaintext tabindex="-1"}
    zone __2.0.192.in-addr.arpa/IN__: loaded serial __2022070601__
    OK
    ```

6.  Reload BIND:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload named
    ```

    If you run BIND in a change-root (chroot) environment, use the `systemctl reload named-chroot`{.literal} command to reload the service.

**Verification**

-   Query different records from the reverse zone, and verify that the output matches the records you have configured in the zone file:

    ``` {.language-plaintext tabindex="-1"}
    # dig +short @localhost -x 192.0.2.1
    ```

    ``` {.language-plaintext tabindex="-1"}
    ns1.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    # dig +short @localhost -x 192.0.2.30
    ```

    ``` {.language-plaintext tabindex="-1"}
    www.example.com
    ```

    This example assumes that BIND runs on the same host and responds to queries on the `localhost`{.literal} interface.

**Additional resources**

-   [The SOA record in zone files](#the-soa-record-in-zone-files "1.5.1. The start of authority record in zone files")
-   [Writing BIND ACLs](#writing-bind-acls "1.4. Writing BIND access control lists")
-   [RFC 1912 - Common DNS operational and configuration errors](https://datatracker.ietf.org/doc/html/rfc1912)

#### [1.5.4. Updating a BIND zone file](#updating-a-bind-zone-file) {#updating-a-bind-zone-file .title}

To update several DNS servers authoritative for a zone, update a zone file only on the primary server. For example, if you change the IP address of a server, you need to update the zone file. Other DNS servers that store a copy of the zone receive the update through a zone transfer.

**Prerequisites**

-   You have configured a zone.
-   You have started the `named`{.literal} or `named-chroot`{.literal} service.
-   You have the administrative privileges.

**Procedure**

1.  Optional: Identify the path to the zone file in the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    options {
        ...
        directory       "/var/named";
    }

    zone "example.com" {
        ...
        file "example.com.zone";
    };
    ```

    You find the path to the zone file in the `file`{.literal} statement in the zone's definition. A relative path is relative to the directory set in `directory`{.literal} in the `options`{.literal} statement.

2.  Edit the zone file:

    a.  Make the required changes.

    b.  Increment the serial number in the start of authority (SOA) record.

        Important

        If the serial number is equal to or lower than the former value, secondary servers will not update their copy of the zone.

3.  Verify the syntax of the zone file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkzone example.com /var/named/example.com.zone
    ```

    ``` {.language-plaintext tabindex="-1"}
    zone __example.com/IN__: loaded serial __2022062802__
    OK
    ```

4.  Reload BIND:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload named
    ```

    If you run BIND in a change-root (chroot) environment, use the `systemctl reload named-chroot`{.literal} command to reload the service.

**Verification**

-   Query the record you have added, modified, or removed, for example:

    ``` {.language-plaintext tabindex="-1"}
    # dig +short @localhost A ns2.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    192.0.2.2
    ```

    This example assumes that BIND runs on the same host and responds to queries on the `localhost`{.literal} interface.

**Additional resources**

-   [The SOA record in zone files](#the-soa-record-in-zone-files "1.5.1. The start of authority record in zone files")
-   [Configuring a forward zone on a BIND primary server](#setting-up-a-forward-zone-on-a-bind-primary-server "1.5.2. Configuring a forward zone on a BIND primary server")
-   [Configuring a reverse zone on a BIND primary server](#setting-up-a-reverse-zone-on-a-bind-primary-server "1.5.3. Configuring a reverse zone on a BIND primary server")

#### [1.5.5. Signing a DNSSEC zone by using the automated key generation and zone maintenance features](#dnssec-zone-signing-using-the-automated-key-generation-and-zone-maintenance-features) {#signing-a-dnssec-zone-by-using-the-automated-key-generation-and-zone-maintenance-features .title}

To ensure authentication and data integrity, you can sign zones with Domain Name System Security Extensions (DNSSEC). Signed zones contain additional resource records. Clients can use them to verify the authenticity of the zone information.

When you enable the DNSSEC policy feature for a zone, Berkeley Internet Name Domain (BIND) automatically performs the actions. It includes creating the keys, signing the zone, and maintaining the zone, including re-signing and periodically replacing the keys.

Important

To enable external DNS servers to verify the authenticity of a zone, you must add the public key of the zone to the parent zone. Contact your domain provider or registry for further details.

You can use the built-in `default`{.literal} DNSSEC policy in BIND. This policy uses single `ECDSAP256SHA`{.literal} key signatures. However, create your own policy to use custom keys, algorithms, and timings.

**Prerequisites**

-   You have installed the `bind`{.literal} package on the server.
-   You have configured the zone for which you want to enable DNSSEC.
-   The `named`{.literal} or `named-chroot`{.literal} service is running.
-   You have configured the server to synchronize the time with a time server. Always check for the correct system time before enabling DNSSEC validation.

**Procedure**

1.  Add the `dnssec-policy default;`{.literal} and `inline-signing yes;`{.literal} in the `/etc/named.conf`{.literal} file to enable DNNSSEC for the zone:

    ``` {.language-plaintext tabindex="-1"}
    zone "example.com" {
        ...
        dnssec-policy default;
        inline-signing yes;
    };
    ```

    -   The `dnssec-policy default;`{.literal} statement enables BIND's automated DNSSEC key management and zone signing for this zone.
    -   The `inline-signing yes;`{.literal} statement makes BIND to automatically sign the zone's records and maintain the signed zone file.

2.  Reload BIND:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload named
    ```

    If you run BIND in a change-root environment, use the `systemctl reload named-chroot`{.literal} command to reload the service.

3.  BIND stores the public key in the `/var/named/K`{.literal}*`<zone_name>`{.literal}*`.+`{.literal}*`<algorithm>`{.literal}*`+`{.literal}*`<key_ID>`{.literal}*`.key`{.literal} file. Use this file to display the public key of the zone in the format that the parent zone requires:

    -   DS record format:

        ``` {.language-plaintext tabindex="-1"}
        # dnssec-dsfromkey /var/named/Kexample.com.+013+61141.key
        ```

        ``` {.language-plaintext tabindex="-1"}
        example.com. IN DS 61141 13 2 3E184188CF6D2521EDFDC3F07CFEE8D0195AACBD85E68BAE0620F638B4B1B027
        ```

    -   DNSKEY format:

        ``` {.language-plaintext tabindex="-1"}
        # grep DNSKEY /var/named/Kexample.com.+013+61141.key
        ```

        ``` {.language-plaintext tabindex="-1"}
        example.com. 3600 IN DNSKEY 257 3 13 sjzT3jNEp120aSO4mPEHHSkReHUf7AABNnT8hNRTzD5cKMQSjDJin2I3 5CaKVcWO1pm+HltxUEt+X9dfp8OZkg==
        ```

4.  Request to add the public key of the zone to the parent zone. Contact your domain provider or registry for further details on how to do this.

**Verification**

1.  Query your own DNS server for a record from the zone for which you enabled DNSSEC signing:

    ``` {.language-plaintext tabindex="-1"}
    # dig +dnssec +short @localhost A www.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    192.0.2.30
    A 13 3 28800 20220718081258 20220705120353 61141 example.com. e7Cfh6GuOBMAWsgsHSVTPh+JJSOI/Y6zctzIuqIU1JqEgOOAfL/Qz474 M0sgi54m1Kmnr2ANBKJN9uvOs5eXYw==
    ```

    This example assumes that BIND runs on the same host and responds to queries on the `localhost`{.literal} interface.

2.  After the server adds the public key to the parent zone and propagates it to other servers, verify that the server sets the authenticated data (`ad`{.literal}) flag on queries to the signed zone:

    ``` {.language-plaintext tabindex="-1"}
    # dig @localhost example.com +dnssec
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    ;; flags: qr rd ra **ad**; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1
    ...
    ```

**Additional resources**

-   [Configuring a forward zone on a BIND primary server](#setting-up-a-forward-zone-on-a-bind-primary-server "1.5.2. Configuring a forward zone on a BIND primary server")
-   [Configuring a reverse zone on a BIND primary server](#setting-up-a-reverse-zone-on-a-bind-primary-server "1.5.3. Configuring a reverse zone on a BIND primary server")

### [1.6. Configuring zone transfers among BIND DNS servers](#configuring-zone-transfers-among-bind-dns-servers) {#configuring-zone-transfers-among-bind-dns-servers .title}

To ensure that all DNS servers that have a copy of the zone to have up-to-date data, configure zone transfers among BIND DNS servers.

**Prerequisites**

-   You have the administrative privileges.
-   On the future primary server, the zone for which you want to set up zone transfers is already configured.
-   On the future secondary server, BIND is already configured as a caching name server.
-   On both servers, the `named`{.literal} or `named-chroot`{.literal} service is running.

**Procedure**

1.  On the existing primary server:

    a.  Generate a shared key and append it to the `/etc/named.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # tsig-keygen example-transfer-key | tee -a /etc/named.conf
        ```

        ``` {.language-plaintext tabindex="-1"}
        key "__example-transfer-key__" {
                algorithm hmac-sha256;
                secret "__q7ANbnyliDMuvWgnKOxMLi313JGcTZB5ydMW5CyUGXQ=__";
        };
        ```

        Output appends to the `/etc/named.conf`{.literal} file.

        You will require this output later on the secondary server as well.

    b.  In the `allow-transfer`{.literal} statement, configure the zone in the `/etc/named.conf`{.literal} file to require the key for transfers:

        ``` {.language-plaintext tabindex="-1"}
        zone "example.com" {
            ...
            allow-transfer { key example-transfer-key; };
        };
        ```

        Define that servers must have the key specified in the `example-transfer-key`{.literal} statement to transfer a zone. However, you can use BIND access control list (ACL) nicknames in the `allow-transfer`{.literal} statement.

    c.  Configure the zone to display the secondary server IP addresses:

        ``` {.language-plaintext tabindex="-1"}
        zone "example.com" {
            ...
            also-notify { 192.0.2.2; 2001:db8:1::2; };
        };
        ```

        By default, after updating a zone, BIND notifies all name servers that have a name server (`NS`{.literal}) record in this zone. If you do not plan to add an `NS`{.literal} record for the secondary server to the zone, you can configure that BIND notifies this server anyway. For that, add the `also-notify`{.literal} statement with the IP addresses of this secondary server to the zone:

    d.  Verify the syntax of the `/etc/named.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # named-checkconf
        ```

        If the command displays no output, the syntax is correct.

    e.  Reload BIND:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl reload named
        ```

        If you run BIND in a change-root environment, use the `systemctl reload named-chroot`{.literal} command to reload the service.

2.  On the future secondary server:

    a.  Add the shared key block to `/etc/named.conf`{.literal} (same as the primary server):

        ``` {.language-plaintext tabindex="-1"}
        key "example-transfer-key" {
                algorithm hmac-sha256;
                secret "q7ANbnyliDMuvWgnKOxMLi313JGcTZB5ydMW5CyUGXQ=";
        };
        ```

        i.  Add the secondary zone definition to the `/etc/named.conf`{.literal} file:

            ``` {.language-plaintext tabindex="-1"}
            zone "example.com" {
                type slave;
                file "slaves/example.com.zone";
                allow-query { any; };
                allow-transfer { none; };
                masters {
                  192.0.2.1 key example-transfer-key;
                  2001:db8:1::1 key example-transfer-key;
                };
            };
            ```

            -   This server is a secondary server (`type slave`{.literal}) for the `example.com`{.literal} zone.
            -   The `/var/named/slaves/example.com.zone`{.literal} file is the zone file. If you set a relative path, as in this example, this path is relative to the directory you set in `directory`{.literal} in the `options`{.literal} statement. To separate zone files for which this server is secondary from primary ones, you can store them, for example, in the `/var/named/slaves/`{.literal} directory.
            -   Any host can query this zone. However, you can specify IP ranges or ACL nicknames to limit the access.
            -   No host can transfer the zone from this server.
            -   The IP addresses of the primary server of this zone are `192.0.2.1`{.literal} and `2001:db8:1::2`{.literal}. However, you can specify ACL nicknames. This secondary server will use the key named `example-transfer-key`{.literal} to authenticate to the primary server.

    b.  Verify the syntax of the `/etc/named.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # named-checkconf
        ```

    c.  Reload BIND:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl reload named
        ```

        If you run BIND in a change-root environment, use the `systemctl reload named-chroot`{.literal} command to reload the service.

3.  Optional: Add an `NS`{.literal} record for the new secondary server to the zone file on the primary server.

**Verification**

-   On the secondary server:

    -   Display the `systemd`{.literal} journal entries of the `named`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # journalctl -u named
        ```

        ``` {.language-plaintext tabindex="-1"}
        ...
        Jul 06 15:08:51 ns2.example.com named[2024]: zone example.com/IN: Transfer started.

        Jul 06 15:08:51 ns2.example.com named[2024]: transfer of 'example.com/IN' from 192.0.2.1#53: connected using 192.0.2.2#45803

        Jul 06 15:08:51 ns2.example.com named[2024]: zone example.com/IN: transferred serial 2022070101

        Jul 06 15:08:51 ns2.example.com named[2024]: transfer of 'example.com/IN' from 192.0.2.1#53: Transfer status: success

        Jul 06 15:08:51 ns2.example.com named[2024]: transfer of 'example.com/IN' from 192.0.2.1#53: Transfer completed: 1 messages, 29 records, 2002 bytes, 0.003 secs (667333 bytes/sec)
        ```

        If you run BIND in a change-root environment, use the `journalctl -u named-chroot`{.literal} command to display the journal entries.

    -   Verify that BIND created the zone file:

        ``` {.language-plaintext tabindex="-1"}
        # ls -l /var/named/slaves/
        ```

        ``` {.language-plaintext tabindex="-1"}
        total 4
        -rw-r--r--. 1 named named 2736 Jul  6 15:08 example.com.zone
        ```

        Note that, by default, secondary servers store zone files in a binary raw format.

    -   Query a record of the transferred zone from the secondary server:

        ``` {.language-plaintext tabindex="-1"}
        # dig +short @192.0.2.2 AAAA www.example.com
        ```

        ``` {.language-plaintext tabindex="-1"}
        2001:db8:1::30
        ```

        This example assumes that the secondary server you set up in this procedure listens on IP address `192.0.2.2`{.literal}.

**Additional resources**

-   [Configuring a forward zone on a BIND primary server](#setting-up-a-forward-zone-on-a-bind-primary-server "1.5.2. Configuring a forward zone on a BIND primary server")
-   [Configuring a reverse zone on a BIND primary server](#setting-up-a-reverse-zone-on-a-bind-primary-server "1.5.3. Configuring a reverse zone on a BIND primary server")
-   [Writing BIND ACLs](#writing-bind-acls "1.4. Writing BIND access control lists")
-   [Updating a BIND zone file](#updating-a-bind-zone-file "1.5.4. Updating a BIND zone file")

### [1.7. Configuring response policy zones in BIND to override DNS records](#configuring-response-policy-zones-in-bind-to-override-dns-records) {#configuring-response-policy-zones-in-bind-to-override-dns-records .title}

You can rewrite a DNS response to block access to certain domains or hosts by using DNS blocking and filtering. In BIND, response policy zones (RPZ) have this functionality. You can configure different actions for blocked entries, such as returning an `NXDOMAIN`{.literal} error or not responding to the query.

If you have several DNS servers, you can configure the RPZ on the primary server, and later configure zone transfers to make the RPZ available on the secondary servers.

**Prerequisites**

-   You have configured BIND as a caching name server.
-   The `named`{.literal} or `named-chroot`{.literal} service is running.
-   You have administrative privileges.

**Procedure**

1.  Edit the `/etc/named.conf`{.literal} file to add a `response-policy`{.literal} definition to the `options`{.literal} statement:

    ``` {.language-plaintext tabindex="-1"}
    options {
        ...

        response-policy {
            zone "rpz.local";
        };

        ...
    }
    ```

    You can set a custom name for the RPZ in the `zone`{.literal} statement in `response-policy`{.literal}. However, you must use the same name in the zone definition in the next step.

2.  Add a `zone`{.literal} definition for the RPZ you set in the previous step:

    ``` {.language-plaintext tabindex="-1"}
    zone "rpz.local" {
        type master;
        file "rpz.local";
        allow-query { localhost; 192.0.2.0/24; 2001:db8:1::/64; };
        allow-transfer { none; };
    };
    ```

    -   This server is the primary server (`type master`{.literal}) for the RPZ named `rpz.local`{.literal}.
    -   The `/var/named/rpz.local`{.literal} file is the zone file. In this example, if you set a relative path, this path is relative to the directory you set in `directory`{.literal} in the `options`{.literal} statement.
    -   Any hosts defined in `allow-query`{.literal} can query this RPZ. However, specify IP ranges or BIND access control list (ACL) nicknames to limit the access.
    -   No host can transfer the zone. Allow zone transfers only when you set up secondary servers and only for the IP addresses of the secondary servers.

3.  Verify the syntax of the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkconf
    ```

    No output indicates that the syntax is correct.

4.  Create the `/var/named/rpz.local`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    $TTL 10m
    @ IN SOA ns1.example.com. hostmaster.example.com. (
                              2022070601 ; serial number
                              1h         ; refresh period
                              1m         ; retry period
                              3d         ; expire time
                              1m )       ; minimum TTL

                     IN NS    ns1.example.com.

    example.org      IN CNAME .
    *.example.org    IN CNAME .
    example.net      IN CNAME rpz-drop.
    *.example.net    IN CNAME rpz-drop.
    ```

    This zone file:

    -   Sets the default time-to-live (TTL) value for resource records to 10 minutes. Without a time suffix, such as `h`{.literal} for hour, BIND interprets the value as seconds.
    -   Has the required start of authority (SOA) resource record with details about the zone.
    -   Sets `ns1.example.com`{.literal} as an authoritative DNS server, a server that holds the actual DNS records for a domain, for this zone. To be functional, a zone requires at least one name server (`NS`{.literal}) record. However, to be compliant with RFC 1912, you require at least two name servers.
    -   Return an `NXDOMAIN`{.literal} error for queries to `example.org`{.literal} and hosts in this domain.
    -   Drop queries to `example.net`{.literal} and hosts in this domain.

5.  Verify the syntax of the `/var/named/rpz.local`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # named-checkzone rpz.local /var/named/rpz.local
    ```

    ``` {.language-plaintext tabindex="-1"}
    zone __rpz.local/IN__: loaded serial __2022070601__
    OK
    ```

6.  Reload BIND:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload named
    ```

    If you run BIND in a change-root (chroot) environment, use the `systemctl reload named-chroot`{.literal} command to reload the service.

**Verification**

1.  Try to resolve a host in the `example.org`{.literal} domain that the RPZ is configured to return an `NXDOMAIN`{.literal} error:

    ``` {.language-plaintext tabindex="-1"}
    # dig @localhost www.example.org
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    ;; ->>HEADER<<- opcode: QUERY, status: **NXDOMAIN**, id: 30286
    ...
    ```

    This example assumes that BIND runs on the same host and responds to queries on the `localhost`{.literal} interface.

2.  Try to resolve a host in the `example.net`{.literal} domain that the RPZ is configured to drop queries:

    ``` {.language-plaintext tabindex="-1"}
    # dig @localhost www.example.net
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    ;; connection timed out; no servers could be reached
    ...
    ```

**Additional resources**

-   [IETF draft: DNS Response Policy Zones (RPZ)](https://datatracker.ietf.org/doc/html/draft-vixie-dnsop-dns-rpz-00)

### [1.8. Recording DNS queries by using dnstap](#recording-dns-queries-by-using-dnstap) {#recording-dns-queries-by-using-dnstap .title}

To analyze Domain Name System (DNS) traffic patterns, monitor DNS server performance, and troubleshoot DNS issues, you can record DNS details by using the `dnstap`{.literal} interface.

To monitor and log details of incoming name queries, `dnstap`{.literal} interface records sent messages from the `named`{.literal} service. You can capture and record DNS queries to collect details about websites or IP addresses.

**Prerequisites**

-   You have the administrative privileges.
-   You have installed the `bind`{.literal} package.

Warning

If you already have a `BIND`{.literal} version installed and running, adding a new version of `BIND`{.literal} overwrites the existing version.

**Procedure**

1.  Enable `dnstap`{.literal} and the target file in the `options`{.literal} block of the `/etc/named.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    options
    {
    # ...
    dnstap { all; }; # Configure filter
    dnstap-output file "/var/named/data/dnstap.bin" versions 2;
    # ...
    };
    # end of options
    ```

2.  Add `dnstap`{.literal} filters to the `dnstap`{.literal} block in the `/etc/named.conf`{.literal} file to specify which types of DNS traffic you want to log. You can use the following filters:

    -   `auth`{.literal}: Authoritative zone response or answer.

    -   `client`{.literal}: Internal client query or answer.

    -   `forwarder`{.literal}: Forwarded query or response from it.

    -   `resolver`{.literal}: Iterative resolution query or response.

    -   `update`{.literal}: Dynamic zone update requests.

    -   `all`{.literal}: Any from the previous options.

    -   `query`{.literal} or `response`{.literal}: If you do not specify a `query`{.literal} or a `response`{.literal} keyword, `dnstap`{.literal} records both.

        Note

        The `dnstap`{.literal} filter has several definitions delimited by a semicolon (`;`{.literal}) in the `dnstap {}`{.literal} block with the following syntax: `dnstap { ( all | auth | client | forwarder | resolver | update ) [ ( query | response ) ]; …​ };`{.literal}

3.  Change the `dnstap-output`{.literal} option by adding additional parameters to customize the behavior of the `dnstap`{.literal} utility on the recorded packets:

    -   `size`{.literal} (unlimited \| \<size\>): Enable automatic rolling over of the `dnstap`{.literal} file when its size reaches the specified limit.

    -   `versions`{.literal} (unlimited \| \<integer\>): Specify the number of automatically rolled files to keep.

    -   `suffix`{.literal} (increment \| timestamp ): Choose the naming convention for rolled out files. By default, the increment starts with `.0`{.literal}. However, you can use the UNIX timestamp by setting the `timestamp`{.literal} value.

        The following example requests `auth`{.literal} responses only, `client`{.literal} queries, and both queries and responses of dynamic `updates`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        Example:

        dnstap {auth response; client query; update;};
        ```

4.  To apply your changes, restart the `named`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart named.service
    ```

5.  Configure a periodic rollout for active logs:

    ``` {.language-plaintext tabindex="-1"}
    # sudoedit /etc/cron.daily/dnstap
    ```

    ``` {.language-plaintext tabindex="-1"}
    #!/bin/sh
    rndc dnstap -roll 3
    mv /var/named/data/dnstap.bin.1 /var/log/named/dnstap/dnstap-$(date -I).bin

    # use dnstap-read to analyze saved logs
    sudo chmod a+x /etc/cron.daily/dnstap
    ```

    -   The `cron`{.literal} scheduler runs the contents of the user-edited script only one time in a day.
    -   The `roll`{.literal} option with the value `3`{.literal} specifies that `dnstap`{.literal} can create up to three backup log files.
    -   The value `3`{.literal} overrides the `version`{.literal} parameter of the `dnstap-output`{.literal} variable. This value limits the number of backup log files to three. Also, this option moves the binary log file to another directory and renames it. It never reaches the `.2`{.literal} suffix, even if three backup log files already exist.
    -   You can skip this step if automatic rolling of binary logs based on size limit is enough.

6.  Use the `dnstap-read`{.literal} utility to read and print output logs in a human-readable format such as a `YAML`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # dnstap-read -p /var/named/data/dnstap.bin
    ```

## [Chapter 2. Configuring an unbound DNS server](#setting-up-an-unbound-dns-server) {#chapter-2.-configuring-an-unbound-dns-server .title}

To securely validate, resolve, and cache Domain Name System (DNS) queries, configure the `unbound`{.literal} DNS service. This service provides a lightweight caching DNS server with DNS Security Extensions (DNSSEC) validation enabled by default and stronger protection against DNS spoofing attacks.

### [2.1. Configuring Unbound as a caching DNS server](#configuring-unbound-as-a-caching-dns-server) {#configuring-unbound-as-a-caching-dns-server .title}

To resolve and cache successful and failed lookups, and answer requests to the same records from its cache, configure the `unbound`{.literal} DNS service.

**Prerequisites**

-   You have the administrative privileges.

**Procedure**

1.  Install the `unbound`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install unbound
    ```

2.  Edit the `/etc/unbound/unbound.conf`{.literal} file, and make the following changes in the `server`{.literal} clause:

    a.  Add `interface`{.literal} parameters to configure on which IP addresses the `unbound`{.literal} service listens for queries, for example:

        ``` {.language-plaintext tabindex="-1"}
        interface: 127.0.0.1
        interface: 192.0.2.1
        interface: 2001:db8:1::1
        ```

        With these settings, `unbound`{.literal} only listens on the specified IPv4 and IPv6 addresses.

        Limiting the interfaces to the required ones prevents clients from unauthorized networks, such as the internet, from sending queries to this DNS server.

    b.  Add `access-control`{.literal} parameters to configure from which subnets clients can query the DNS service, for example:

        ``` {.language-plaintext tabindex="-1"}
        access-control: 127.0.0.0/8 allow
        access-control: 192.0.2.0/24 allow
        access-control: 2001:db8:1::/64 allow
        ```

3.  Create private keys and certificates for remotely managing the `unbound`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart unbound-keygen
    ```

    Note

    If you skip this step, verifying the configuration in the next step will report the missing files. However, the `unbound`{.literal} service automatically creates the files if they are missing.

4.  Verify the configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # unbound-checkconf
    ```

    ``` {.language-plaintext tabindex="-1"}
    unbound-checkconf: no errors in /etc/unbound/unbound.conf
    ```

5.  Update the firewalld rules to allow incoming DNS traffic:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=dns
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

6.  Enable and start the `unbound`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now unbound
    ```

**Verification**

1.  Query the `unbound`{.literal} DNS server listening on the `localhost`{.literal} interface to resolve a domain:

    ``` {.language-plaintext tabindex="-1"}
    # dig @localhost www.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    __www.example.com.__    __86400__    IN    A    __198.51.100.34__

    ;; Query time: __330 msec__
    ...
    ```

    After querying a record for the first time, `unbound`{.literal} adds the entry to its cache.

2.  Repeat the previous query:

    ``` {.language-plaintext tabindex="-1"}
    # dig @localhost www.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    __www.example.com.__    __85332__    IN    A    __198.51.100.34__

    ;; Query time: __1 msec__
    ...
    ```

    Because of the cached entry, further requests for the same record are significantly faster until the entry expires.

    For details, see `unbound.conf(5)`{.literal} man page on your system.

## [Chapter 3. Providing DHCP services](#providing-dhcp-services) {#chapter-3.-providing-dhcp-services .title}

To automatically assign IP addresses and other network settings to client devices, use the dynamic host configuration protocol (DHCP). You can configure Kea as a DHCP server to centrally manage network configurations for your clients.

### [3.1. The difference between static and dynamic IP addressing](#the-difference-between-static-and-dynamic-ip-addressing) {#the-difference-between-static-and-dynamic-ip-addressing .title}

To manage how devices receive their unique network addresses, you can select between two methods: static and dynamic IP addressing.

Static IP addressing

:   When you assign a static IP address to a device, the address does not change over time unless you change it manually. Use static IP addressing if you want:

    -   To ensure network address consistency for servers such as DNS, and authentication servers.
    -   To use out-of-band management devices that work independently of other network infrastructure.

Dynamic IP addressing

:   When you configure a device to use a dynamic IP address, the address can change over time. For this reason, dynamic addresses are typically used for devices that connect to the network occasionally because the IP address can be different after rebooting the host.

    Dynamic IP addresses are more flexible, easier to set up, and administer. DHCP is a traditional method of dynamically assigning network configurations to hosts.

Note

There is no strict rule defining when to use static or dynamic IP addresses. It depends on your needs, preferences, and the network environment.

### [3.2. DHCP transaction phases](#dhcp-transaction-phases) {#dhcp-transaction-phases .title}

DHCP works in four phases: Discovery, Offer, Request, Acknowledgment, also called the DORA process. DHCP uses this process to assign IP addresses to clients.

Discovery
:   The DHCP client sends a message to discover the DHCP server in the network. The client broadcasts this message at the network and data link layer.

Offer
:   The DHCP server receives the client's message and offers an IP address to the client. The server unicasts this message at the data link layer and broadcasts it at the network layer.

Request
:   The DHCP client requests the offered IP address from the DHCP server. The client unicasts this message at the data link layer and broadcasts it at the network layer.

Acknowledgment
:   The DHCP server sends an acknowledgment to the client. The server unicasts this message at the data link layer and broadcasts it at the network layer. This acknowledgment is the final message in the DHCP DORA process.

### [3.3. Overview of using Kea for DHCPv4 and DHCPv6](#overview-of-using-kea-for-dhcpv4-and-dhcpv6) {#overview-of-using-kea-for-dhcpv4-and-dhcpv6 .title}

To manage both DHCPv4 and DHCPv6 services independently, use Kea. Kea is an open source DHCP server with a modular design. Each protocol has its own configuration file, you can use it to run a DHCPv4 server, a DHCPv6 server, or both to meet network requirements.

For each protocol, Kea uses a separate configuration file and service:

DHCPv4

:   -   Configuration file: `/etc/kea/kea-dhcp4.conf`{.literal}
    -   Systemd service name: `kea-dhcp4`{.literal}

DHCPv6

:   -   Configuration file: `/etc/kea/kea-dhcp6.conf`{.literal}
    -   Systemd service name: `kea-dhcp6`{.literal}

### [3.4. The Kea lease database](#the-kea-lease-database) {#the-kea-lease-database .title}

A DHCP lease is the period for which Kea allocates a network address to a client. The lease databases contain information about the allocated leases, such as the IP address assigned to a media access control (MAC) address or the timestamp when the lease expires.

All timestamps in the lease databases are in Coordinated Universal Time (UTC).

Kea supports the following lease databases:

`memfile`{.literal} (default)

:   A text-based file stored on the disk. By default, Kea stores the DHCP leases in the following files:

    -   For DHCPv4: `/var/lib/kea/kea-leases4.csv`{.literal}

    -   For DHCPv6: `/var/lib/kea/kea-leases6.csv`{.literal}

        Warning

        Manually updating the files can cause inconsistencies and file corruption. For performance reasons, Kea stores the lease data in memory and does not monitor the lease files during runtime. Manual edits can be overridden by the next time Kea updates the files.

`mysql`{.literal}
:   A MySQL database.

`pgsql`{.literal}
:   A PostgreSQL database.

Kea updates the lease database in the following cases:

-   On lease updates
-   On graceful shutdown
-   During periodic lease file cleanup (LFC) processes
-   By requests through the API

### [3.5. Configuring a Kea DHCP server](#setting-up-a-kea-dhcp-server) {#configuring-a-kea-dhcp-server .title}

To avoid errors due to manual DHCP configurations, use the Kea DHCP server to automatically assign IP addresses and other network settings to client devices.

**Prerequisites**

-   You have installed the `kea`{.literal} package.
-   You have the administrative privileges.

**Procedure**

1.  If you are configuring an IPv4 network:

    a.  Edit the `/etc/kea/kea-dhcp4.conf`{.literal} file, and use the following configuration:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp4": {
            // Global settings that apply to all subnets unless overridden.
            "valid-lifetime": 86400,
            "option-data": [
              {
                "name": "domain-name",
                "data": "example.com"
              },
              {
                "name": "domain-name-servers",
                "data": "192.0.2.53"
              }
            ],

            // The network interfaces on which Kea will listen for DHCP traffic.

            "interfaces-config": {
              "interfaces": [ "enp1s0" ]
            },
            "subnet4": [
              // A definition of a subnet that is directly connected to the server
              {
                "id": 1,
                "subnet": "192.0.2.0/24",
                "pools": [
                  { "pool": "192.0.2.20  - 192.0.2.100" },
                  { "pool": "192.0.2.150 - 192.0.2.200" }
                ],
                "option-data": [
                  { "name": "routers", "data": "192.0.2.1" }
                ]
              },

              // A definition of a remote subnet served through a DHCP relay
              {
                "id": 2,
                "subnet": "198.51.100.0/24",
                "pools": [
                  { "pool": "198.51.100.20 - 198.51.100.100" }
                ],
                // Allowed DHCP relay agents
              "relay": {
                  "ip-addresses": [ "198.51.100.5" ]
                },
                "option-data": [
                  { "name": "routers", "data": "198.51.100.1" },
                  { "name": "domain-name-servers", "data": "198.51.100.53" }
                ]
              }
            ]
          }
        }
        ```

        This example configures Kea to serve two subnets: one directly connected to the server and a remote one that uses a DHCP relay agent.

        `interfaces`{.literal}
        :   Defines the network interfaces on which Kea listens for DHCP requests. If a subnet is not directly connected to the server, ensure to list the interface through which the subnet can be reached.

        `id`{.literal}
        :   Defines a unique integer for the subnet, if you define more than one subnet.

        `subnet`{.literal}
        :   Defines the subnet in Classless Inter-Domain Routing (CIDR) format.

        `pools`{.literal}
        :   Defines the IP address ranges from which Kea can assign addresses to clients.

        `option-data`{.literal}
        :   Defines DHCP options sent to clients, such as the default gateway and DNS servers. Per-subnet option-data settings override global settings.

        `relay`{.literal}
        :   Defines the IP addresses of DHCP relay agents. While this setting is optional for remote subnets, it improves the security to limit forwarded requests to trusted agents. Do not use this parameter for directly-connected subnets.

    b.  Verify the syntax of the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
        ```

        If the command returns `Syntax check failed`{.literal}, fix the errors shown in the report.

    c.  Update the `firewalld`{.literal} rules to allow incoming DHCPv4 traffic:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service=dhcp
        ```

    d.  Reload the firewall configuration to apply the changes:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --reload
        ```

    e.  Enable and start the service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now kea-dhcp4
        ```

2.  If you are configuring an IPv6 network:

    a.  Edit the `/etc/kea/kea-dhcp6.conf`{.literal} file, and use the following configuration:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp6": {
            // Global settings that apply to all subnets unless overridden.
            "valid-lifetime": 86400,
            "option-data": [
              {
                "name": "domain-name",
                "data": "example.com"
              },
              {
                "name": "dns-servers",
                "data": "2001:db8:0:1::53"
              }
            ],

            // The network interfaces on which Kea will listen for DHCP traffic.
            "interfaces-config": {
              "interfaces": [ "enp1s0" ]
            },

            "subnet6": [
              // A definition of a subnet that is directly connected to the server
              {
                "id": 1,
                "subnet": "2001:db8:0:1::/64",
                "pools": [
                  { "pool": "2001:db8:0:1::1000 - 2001:db8:0:1::2000" },
                  { "pool": "2001:db8:0:1::4000 - 2001:db8:0:1::5000" }
                ]
              },

              // A definition of a remote subnet served through a DHCP relay
              {
                "id": 2,
                "subnet": "2001:db8:0:2::/64",
                "pools": [
                  { "pool": "2001:db8:0:2::1000 - 2001:db8:0:2::2000" }
                ],
                // Allowed DHCP relay agents
                "relay": {
                  "ip-addresses": [ "2001:db8:0:2::5" ]
                },
                "option-data": [
                  { "name": "dns-servers", "data": "2001:db8:0:1::53" }
                ]
              }
            ]
          }
        }
        ```

        This example configures Kea to serve two subnets: one directly connected to the server and a remote one that uses a DHCP relay agent.

    b.  Verify the syntax of the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # kea-dhcp6 -t /etc/kea/kea-dhcp6.conf
        ```

        If the command returns `Syntax check failed`{.literal}, fix the errors shown in the report.

    c.  Update the `firewalld`{.literal} rules to allow incoming DHCPv6 traffic:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service=dhcpv6
        ```

    d.  Reload the firewall configuration to apply the changes:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --reload
        ```

    e.  Enable and start the `service`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now kea-dhcp6
        ```

**Verification**

1.  Configure a network connection with DHCP on a client. See [Configuring an Ethernet connection by using `nmcli`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_networking/configuring-an-ethernet-connection#configuring-an-ethernet-connection-by-using-nmcli).

2.  Connect the client to the network.

3.  Check if the client received an IP address from the DHCP server:

    ``` {.language-plaintext tabindex="-1"}
    # ip address show <interface>
    ```

    ``` {.language-plaintext tabindex="-1"}
    2: enp1s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether 52:54:00:17:b8:b6 brd ff:ff:ff:ff:ff:ff
        inet 192.0.2.20/24 brd 192.0.2.255 scope global noprefixroute enp1s0
           valid_lft forever preferred_lft forever
        inet6 2001:db8:1::1000/64 scope global noprefixroute
           valid_lft forever preferred_lft forever
    ```

**Troubleshooting**

-   Check the IPv4 and IPv6 addresses Kea is listening on:

    ``` {.language-plaintext tabindex="-1"}
    # ss -lunp | grep -E ':(67|547)'
    ```

    If Kea does not listen on all interfaces you configured, check the `interfaces-config`{.literal} setting in the Kea configuration files.

**Next steps**

-   [Configure logging](#configuring-loggers-in-kea "3.6. Configuring loggers in Kea")

### [3.6. Configuring loggers in Kea](#configuring-loggers-in-kea) {#configuring-loggers-in-kea .title}

To customize log settings depending on priority, such as the severity level, configure `loggers`{.literal} in Kea. By default, Kea writes log messages to the systemd journal and the `/var/log/messages`{.literal} files, if the `rsyslogd`{.literal} service is running.

**Prerequisites**

-   You have installed the `kea`{.literal} package on the server.
-   You have started the `kea-dhcp4`{.literal} and `kea-dhcp6`{.literal} services.
-   You have administrative privileges.

**Procedure**

1.  To configure an IPv4 network, edit the `/etc/kea/kea-dhcp4.conf`{.literal} file:

    a.  Add the `loggers`{.literal} configuration to the `Dhcp4`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp4": {
            ...,
            "loggers":[
              {
                "name":"kea-dhcp4",
                "output-options":[
                   {
                    "output":"kea-dhcp4.log",
                    "maxsize":104857600,
                    "maxver":5
                   }
                ],
                "severity":"INFO",
              }
            ],
            ...
        ```

        The settings specified in the example are:

        `name`{.literal}
        :   Defines the name of the binary the `logger`{.literal} settings apply to.

        `output`{.literal}
        :   Sets the log file name in the `/var/lib/kea/`{.literal} directory.

        `maxsize`{.literal}
        :   Sets the maximum size of the log file before Kea rotates it. The default value is `10240000`{.literal} bytes.

        `maxver`{.literal}
        :   Sets the maximum number of rotated versions Kea will keep. Note that a `maxsize`{.literal} value less than `204800`{.literal} bytes disables rotation.

        `severity`{.literal}
        :   Specifies the category of messages logged. You can set one of the following values: `NONE`{.literal}, `FATAL`{.literal}, `ERROR`{.literal}, `WARN`{.literal}, `INFO`{.literal}, and `DEBUG`{.literal}. Kea logs only messages of the configured severity and those with a higher level.

    b.  Verify the syntax of the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
        ```

        If the command returns `Syntax check failed`{.literal}, fix the errors shown in the report.

    c.  Restart the `kea-dhcp4`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart kea-dhcp4
        ```

2.  To configure an IPv6 network, edit the `/etc/kea/kea-dhcp6.conf`{.literal} file:

    a.  Add the `loggers`{.literal} configuration to the `Dhcp6`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp6": {
            ...,
            "loggers":[
              {
                "name":"kea-dhcp6",
                "output-options":[
                   {
                    "output":"kea-dhcp6.log",
                    "maxsize":104857600,
                    "maxver":5
                   }
                ],
                "severity":"INFO",
              }
            ],
            ...
        ```

    b.  Verify the syntax of the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # kea-dhcp6 -t /etc/kea/kea-dhcp6.conf
        ```

        If the command returns `Syntax check failed`{.literal}, fix the errors shown in the report.

    c.  Restart the `kea-dhcp6`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart kea-dhcp6
        ```

**Verification**

-   Monitor the log file to check if it displays messages of the expected severity.

### [3.7. Assigning a static address to a host by using DHCP](#assigning-a-static-address-to-a-host-by-using-dhcp) {#assigning-a-static-address-to-a-host-by-using-dhcp .title}

To assign a fixed IP address to a media access control (MAC), a DHCP unique identifier (DUID), or other identifiers, use a reservation inside a subnet definition in Kea. Kea is an open source DHCP server. For example, use this method to always assign the same IP address to a server or network device.

**Prerequisites**

-   You have configured the `kea-dhcp4`{.literal} and `kea-dhcp6`{.literal} services.
-   You have the administrative privileges.

**Procedure**

1.  If you are configuring an IPv4 network:

    a.  Edit the `/etc/kea/kea-dhcp4.conf`{.literal} file, and add a reservation to the `subnet4`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp4": {
            "subnet4": [
              {
                "subnet": "192.0.2.0/24",
                  ...,
                "reservations": [
                  {
                    "hw-address": "52:54:00:72:2f:6e",
                    "ip-address": "192.0.2.130"
                  }
                ],
                  ...
        ```

        This example configures Kea to always assign the `192.0.2.130`{.literal} IP address to the host with the `52:54:00:72:2f:6e`{.literal} MAC address.

        For further examples, see the `/usr/share/doc/kea/examples/kea4/reservations.json`{.literal} file provided by the `kea-doc`{.literal} package.

    b.  Verify the syntax of the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
        ```

        If the command returns `Syntax check failed`{.literal}, fix the errors shown in the report.

    c.  Restart the `kea-dhcp4`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart kea-dhcp4
        ```

2.  If you are configuring an IPv6 network:

    a.  Edit the `/etc/kea/kea-dhcp6.conf`{.literal} file, and add a reservation to the `subnet6`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp6": {
            "subnet6": [
              {
                "subnet": "2001:db8:0:1::/64",
                ...,
                "reservations": [
                  {
                    "hw-address": "52:54:00:72:2f:6e",
                    "ip-address": "2001:db8:0:1::99"
                  }
                ];
                ...
        ```

        This example configures Kea to always assign the `2001:db8:0:1::99`{.literal} IP address to the host with the `52:54:00:72:2f:6e`{.literal} MAC address.

        For further examples, see the `/usr/share/doc/kea/examples/kea6/reservations.json`{.literal} file provided by the `kea-doc`{.literal} package.

    b.  Verify the syntax of the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # kea-dhcp6 -t /etc/kea/kea-dhcp6.conf
        ```

        If the command returns `Syntax check failed`{.literal}, fix the errors shown in the report.

    c.  Restart the `kea-dhcp6`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart kea-dhcp6
        ```

### [3.8. Classifying clients in Kea](#classifying-clients-in-kea) {#classifying-clients-in-kea .title}

To group clients based on specific criteria and allow for granular control over network configuration, use Kea client classes. You can apply special processing rules or assign different DHCP options to clients.

You can create a client class that assigns Voice over IP (`VoIP`{.literal}) devices to a specific IP pool. This is to ensure that `VoIP`{.literal} phones get different IP addresses than other devices on the network. For example, in IPv4 networks, you can use a `substring`{.literal} expression to test for the first 3 octets of their media access control (MAC) address. In IPv6 networks where the MAC address is not a reliable indicator, you can test for a sub-string of the DHCPv6 vendor class option.

**Prerequisites**

-   You have configured the `kea-dhcp4`{.literal} and `kea-dhcp6`{.literal} services and are active.
-   You have administrative privileges.

**Procedure**

1.  To configure an IPv4 network, edit the `/etc/kea/kea-dhcp4.conf`{.literal} file

    a.  Add client classes to the `Dhcp4`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp4": {
            ...
            "client-classes": [
              {
                  "name": "VoIP-Phones",
                  "test": "substring(pkt4.mac, 0, 3) == 0x525400"
              },
              {
                  "name": "Others",
                  "test": "not member('VoIP-Phones')"
              }
            ],
            ...
        ```

        In this example, devices with a MAC address starting with `52:54:00`{.literal} match the `VoIP-Phones`{.literal} client class. The `Others`{.literal} client class includes devices that do not match the rule.

    b.  Assign the client classes to your `pool`{.literal} definitions:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp4": {
            "subnet4": [
              {
                "subnet": "192.0.2.0/24",
            "pools": [
                  {
                    "pool": "192.0.2.20  - 192.0.2.100",
                    "client-class": "Others"
                  },
                  {
                    "pool": "192.0.2.150 - 192.0.2.200",
                    "client-class": "VoIP-Phones"
                  }
                ],
                ...
        ```

        Depending on which client class a host matches, Kea assigns an IP address from the corresponding pool.

    c.  Verify the syntax of the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
        ```

        If the command returns `Syntax check failed`{.literal}, fix the errors shown in the report.

    d.  Restart the `kea-dhcp4`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart kea-dhcp4
        ```

2.  To configure an IPv6 network, edit the `/etc/kea/kea-dhcp6.conf`{.literal} file:

    a.  Add client classes to the `Dhcp6`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp6": {
            ...
            "client-classes": [
              {
                  "name": "VoIP-Phones",
                  "test": "option[16].exists and (substring(option[16].hex, 0, 8) == '00000009')",
              },
              {
                  "name": "Others",
                  "test": "not member('VoIP-Phones')"
              }
            ],
            ...
        ```

        In this example, devices that send a DHCPv6 vendor class option (option 16) where the hexadecimal value begins with `00000009`{.literal} match the `VoIP-Phones`{.literal} client class. The `Others`{.literal} client class includes devices that do not match the rule.

    b.  Assign the client classes to your `pool`{.literal} definitions:

        ``` {.language-plaintext tabindex="-1"}
        {
          "Dhcp6": {
            "subnet6": [
              {
                "subnet": "2001:db8:0:1::/64",
            "pools": [
                  {
                    "pool": "2001:db8:0:1::1000 - 2001:db8:0:1::2000",
                    "client-class": "Others"
                  },
                  {
                    "pool": "2001:db8:0:1::4000 - 2001:db8:0:1::5000",
                    "client-class": "VoIP-Phones"
                  }
                ],
                ...
        ```

        Depending on which client class a host matches, Kea assigns an IP from the corresponding pool.

    c.  Verify the syntax of the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # kea-dhcp6 -t /etc/kea/kea-dhcp6.conf
        ```

        If the command returns `Syntax check failed`{.literal}, fix the errors shown in the report.

    d.  Restart the `kea-dhcp6`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart kea-dhcp6
        ```

**Verification**

-   Connect clients that match the rules in the client classes and verify that Kea assigned an IP address from the associated pool.

### [3.9. Comparison of DHCPv6 to radvd](#comparison-of-dhcpv6-to-radvd) {#comparison-of-dhcpv6-to-radvd .title}

To use DHCPv6 in subnets that require a default gateway setting, configure an additional router advertisement service, such as Router Advertisement Daemon (`radvd`{.literal}).

In an IPv6 network, only router advertisement messages have information about the IPv6 default gateway. The `radvd`{.literal} service uses flags in router advertisement packets to announce the availability of a DHCPv6 server.

The following table compares features of DHCPv6 and `radvd`{.literal}:

+-------------------------------------------------------------+-------------+-------------------+
| Functionality                                               | DHCPv6      | `radvd`{.literal} |
+:============================================================+:============+:==================+
| Provides information about the default gateway              | no          | yes               |
+-------------------------------------------------------------+-------------+-------------------+
| Guarantees random addresses to protect privacy              | yes         | no                |
+-------------------------------------------------------------+-------------+-------------------+
| Sends further network configuration options                 | yes         | no                |
+-------------------------------------------------------------+-------------+-------------------+
| Maps media access control (MAC) addresses to IPv6 addresses | yes         | no                |
+-------------------------------------------------------------+-------------+-------------------+

: Table 3.1. Comparison of DHCPv6 and radvd features

Show more

### [3.10. Configuring the radvd service for IPv6 routers](#configuring-the-radvd-service-for-ipv6-routers) {#configuring-the-radvd-service-for-ipv6-routers .title}

To manage router advertisement messages, configure the router advertisement daemon (`radvd`{.literal}) service. This service sends router advertisement messages for IPv6 stateless auto-configuration. You can configure addresses, settings, routes, and select a default router based on these advertisements.

Note

You can only set `/64`{.literal} prefixes in the `radvd`{.literal} service. To use other prefixes, use DHCPv6.

**Prerequisites**

-   You have the administrative privileges.

**Procedure**

1.  Install the `radvd`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install radvd
    ```

2.  Edit the `/etc/radvd.conf`{.literal} file to configure `radvd`{.literal} with the following parameters:

    ``` {.language-plaintext tabindex="-1"}
    interface enp1s0
    {
      AdvSendAdvert on;
      AdvManagedFlag on;
      AdvOtherConfigFlag on;

      prefix 2001:db8:0:1::/64 {
      };
    };
    ```

    -   Send router advertisement messages on the `enp1s0`{.literal} interface for the `2001:db8:0:1::/64`{.literal} subnet.
    -   The `AdvManagedFlag on`{.literal} flag defines that the client should receive the IP address from a DHCP server.
    -   The `AdvOtherConfigFlag`{.literal} flag defines that clients should receive non-address information from the DHCP server as well.

3.  Enable `radvd`{.literal} to start automatically when the system boots:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now radvd
    ```

    For details, see `radvd.conf(5)`{.literal} man page and `/usr/share/doc/radvd/radvd.conf.example`{.literal} file on your system.

**Verification**

-   Display the content of router advertisement packages and the configured values `radvd`{.literal} sends:

    ``` {.language-plaintext tabindex="-1"}
    # radvdump
    ```

**Additional resources**

-   [Can I use a prefix length other than 64 bits in IPv6 Router Advertisements? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/1175913)

## [Legal Notice](#idm140640921023456) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
