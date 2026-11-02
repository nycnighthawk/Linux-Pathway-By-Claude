---
{"title": "FreeIPA", "url": "https://wiki.archlinux.org/title/FreeIPA", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# FreeIPA

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** Is this article only about the client? If so it should say so. (Discuss in [Talk:FreeIPA](../en/Talk:FreeIPA.html))

**This article or section needs expansion.**

**Reason:** How do you install the client? There is [freeipa-client](https://aur.archlinux.org/packages/freeipa-client/)^AUR^. (Discuss in [Talk:FreeIPA](../en/Talk:FreeIPA.html))

[FreeIPA](https://www.freeipa.org/) is an open-source Identity, Policy and Audit (IPA) suite, sponsored by Red Hat, which provides services similar to Microsoft\'s Active Directory

## Manual configuration as IPA client {#Manual_configuration_as_IPA_client}

Make sure your clocks are synchronized. Kerberos will not work otherwise. [NTP](../en/Network_Time_Protocol_daemon.html "Network Time Protocol daemon") is recommended.

Instead of using `ipa-client-install` script for automated client configuration and enrollment, the following sections describe a manual procedure for enrolling the client `client.example.com` to the FreeIPA server `ipaserver.example.com` in the `example.com` domain.

### Configure SSSD and Kerberos {#Configure_SSSD_and_Kerberos}

Follow the LDAP auth instructions to [setup SSSD](../en/LDAP_authentication.html#Online_and_offline_authentication_with_SSSD "LDAP authentication"). Use a SSSD configuration similar to the following, substituting the requisite fields:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/sssd/sssd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[sssd]
config_file_version = 2
services = nss, pam, sudo, ssh
domains = EXAMPLE.COM
#debug_level = 9

[domain/EXAMPLE.COM]
#debug_level = 9
cache_credentials = true
krb5_store_password_if_offline = true
id_provider = ipa
auth_provider = ipa
access_provider = ipa
chpass_provider = ipa
#ipa_domain=example.com  # Optional if you set SRV records in DNS
#ipa_server=ipaserver.example.com  # Optional if you set SRV records in DNS
ipa_hostname=client.example.com
```

Configure pam in similar way to [LDAP](../en/LDAP_authentication.html#PAM_configuration "LDAP authentication"), replacing `pam_ldap.so` with `pam_sss.so`.

Create an `/etc/krb5.conf` file for your domain:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/krb5.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[libdefaults]
        default_realm = EXAMPLE.COM
        dns_lookup_realm = false
        dns_lookup_kdc = false
        rdns = false
        ticket_lifetime = 24h
        forwardable = yes
        #allow_weak_crypto = yes  # Only if absolutely necessary. Currently FreeIPA supports strong crypto.

[realms]
        EXAMPLE.COM = {
                admin_server = freeipaserver.example.com
                kdc = freeipaserver.example.com:749
                default_admin = example.com
        }

[domain_realm]
        example.com = EXAMPLE.COM
        .example.com = EXAMPLE.COM

[logging]
        default = FILE:/var/log/krb5libs.log
        kdc = FILE:/var/log/krb5kdc.log
        admin_server = FILE:/var/log/kadmin.log
```

### Enroll the client {#Enroll_the_client}

On FreeIPA server, add the client to the IPA server ([From Fedora documentation](https://fedoraproject.org/wiki/FreeIPA_step_by_step)):

1.  Login and request and admin session

        $ kinit admin

2.  Create a host entry

        $ ipa host-add --force --ip-address=192.168.166.31 client.example.com

    if the host does not have a static IP, use

        $ ipa host-add client.example.com

3.  Set the client to be managed by IPA

        $ ipa host-add-managedby --hosts=ipaserver.example.com client.example.com

4.  Generate keytab for the client

        # ipa-getkeytab -s ipaserver.example.com  -p host/client.example.com -k /tmp/client1.keytab

Install the keytab on the client:

    $ scp user@ipaserver.example.com:/tmp/client1.keytab krb5.keytab
    # mv krb5.keytab /etc/krb5.keytab

### SSH integration {#SSH_integration}

#### authorized_keys

You can configure SSHD to fetch users SSH public key from the LDAP directory by uncommenting those lines in `/etc/ssh/sshd_config`:

    AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys
    AuthorizedKeysCommandUser nobody

Then [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `sshd.service`.

You can add your ssh key to your FreeIPA user account through the web interface or use the `-sshpubkey='ssh-rsa AAAA...'` argument to the `ipa user-mod` or `ipa user-create` commands.

Test it:

    $ sudo -u nobody sss_ssh_authorizedkeys <username>

You should see your ssh public key on standard output and no error message on standard error.

#### known_hosts

You can configure SSH to fetch hosts public key information from their directory entries in FreeIPA by adding those lines in `/etc/ssh/ssh_config`:

    GlobalKnownHostsFile /var/lib/sss/pubconf/known_hosts
    ProxyCommand /usr/bin/sss_ssh_knownhostsproxy -p %p %h

#### Kerberos/GSS API Authentication {#Kerberos/GSS_API_Authentication}

You can enabled Kerberos / GSS API Authentication for the SSH Client to FreeIPA member hosts by uncommenting and changing the following lines in `/etc/ssh/ssh_config`:

    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials yes

### See also {#See_also}

-   [Wikipedia:FreeIPA](https://en.wikipedia.org/wiki/FreeIPA "wikipedia:FreeIPA")
-   [Freeipa30_SSSD_OpenSSH_integration.pdf](https://github.com/freeipa/freeipa.github.io/blob/main/src/page/Freeipa30_SSSD_OpenSSH_integration.pdf)
