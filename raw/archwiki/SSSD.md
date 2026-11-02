---
{"title": "SSSD", "url": "https://wiki.archlinux.org/title/SSSD", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# SSSD

Related articles

-   [LDAP authentication](../en/LDAP_authentication.html "LDAP authentication")
-   [Identity management](../en/Identity_management.html "Identity management")

[SSSD](https://en.wikipedia.org/wiki/System_Security_Services_Daemon "wikipedia:System Security Services Daemon") is a system daemon. Its primary function is to provide access to identity and authentication remote resource through a common framework that can provide caching and offline support to the system. It provides PAM and NSS modules, and in the future will D-BUS based interfaces for extended user information. It provides also a better database to store local users as well as extended user data.

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [sssd](https://archlinux.org/packages/?name=sssd) package.

## Configuration {#Configuration}

### LDAP {#LDAP}

See [LDAP authentication#SSSD configuration](../en/LDAP_authentication.html#SSSD_configuration "LDAP authentication").

### PAM proxy {#PAM_proxy}

If you would like software running as a non-root user to be able to use `pam_unix.so` for authentication, you can run SSSD as a PAM proxy for this by creating the following files.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/sssd/sssd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[sssd]
services = pam
domains = local

[domain/local]
id_provider = proxy
proxy_lib_name = files
proxy_pam_target = sssd-shadowutils
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pam.d/sssd
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#%PAM-1.0

auth      required  pam_sss.so
account   required  pam_sss.so
password  required  pam_sss.so
session   required  pam_sss.so
```

Now specify `sssd` as the PAM service name in your software\'s configuration.

#### Run SSSD as root {#Run_SSSD_as_root}

**The factual accuracy of this article or section is disputed.**

**Reason:** If an override is always needed, it requires further packaging changes. How about the simpler change in the talk to replace it? (Discuss in [Talk:SSSD#Alternate to running the sssd service as root](../en/Talk:SSSD.html#Alternate_to_running_the_sssd_service_as_root "Talk:SSSD"))

**Note** See [archlinux/packaging/packages/sssd/#5](https://gitlab.archlinux.org/archlinux/packaging/packages/sssd//-/issues/5) for negative impacts of overriding.

SSSD 2.10 and above runs as a non-root user by default, but here it needs to run as root in order to access `/etc/shadow`. [Override the unit](../en/Override_the_unit.html "Override the unit") `sssd.service` exactly like this:

    [Service]
    Environment=DEBUG_LOGGER=--logger=files
    EnvironmentFile=-/etc/sysconfig/sssd
    ExecStartPre=+-/bin/chown -f root:sssd /etc/sssd
    ExecStartPre=+-/bin/chown -f root:sssd /etc/sssd/sssd.conf
    ExecStartPre=+-/bin/chown -f -R root:sssd /etc/sssd/conf.d
    ExecStartPre=+-/bin/chown -f -R root:sssd /etc/sssd/pki
    ExecStartPre=+-/bin/sh -c "/bin/chown -f root:sssd /var/lib/sss/db/*.ldb"
    ExecStartPre=+-/bin/sh -c "/bin/chown -f root:sssd /var/lib/sss/gpo_cache/*"
    ExecStartPre=+-/bin/sh -c "/bin/chown -f root:sssd /var/log/sssd/*.log"
    ExecStart=/usr/bin/sssd -i ${DEBUG_LOGGER}
    Type=notify
    NotifyAccess=main
    Restart=on-abnormal
    CapabilityBoundingSet= CAP_CHOWN CAP_DAC_OVERRIDE CAP_SETGID CAP_SETUID CAP_DAC_READ_SEARCH 
    #SecureBits=noroot noroot-locked
    User=root
    Group=sssd
    # If service configured to be run under "root", uncomment "SupplementaryGroups"
    #SupplementaryGroups=sssd

Note that SSSD wants its files like `/var/log/sssd` and `/etc/sssd` to have the same owner as the user running SSSD, so you have to `chown` those files to be root-owned. Additionally, delete and add `/usr/lib/tmpfiles.d/sssd-perms.conf` to `NoExtract` in `/etc/pacman.conf` to prevent systemd-tmpfiles from reverting the permissions of SSSD files.

Finally, [enable/start](../en/Help:Reading.html#Control_of_systemd_units "Enable/start") `sssd.service`.

## Tips and tricks {#Tips_and_tricks}

### Prevent logins with empty passwords {#Prevent_logins_with_empty_passwords}

If using SSSD as a PAM proxy, by default it allows logging into accounts with empty passwords, which could be undesirable. To fix this, remove `nullok` from `/etc/pam.d/sssd-shadowutils`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pam.d/sssd-shadowutils
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#%PAM-1.0
auth        [success=done ignore=ignore default=die] pam_unix.so try_first_pass
auth        required      pam_deny.so

account     required      pam_unix.so
account     required      pam_permit.so
```

Then add that file to `NoUpgrade` in `/etc/pacman.conf`.

## See also {#See_also}

-   [Official website](https://sssd.io/)
