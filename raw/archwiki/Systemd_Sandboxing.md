---
{"title": "Systemd/Sandboxing", "url": "https://wiki.archlinux.org/title/Systemd/Sandboxing", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Systemd/Sandboxing

Related articles

-   [Firejail](../../en/Firejail.html "Firejail")
-   [AppArmor](../../en/AppArmor.html "AppArmor")
-   [cgroups](../../en/Cgroups.html "Cgroups")

systemd enables users to harden and sandbox system service units. Because of technical limitations, and ironically security reasons, user units can not be hardened or sandboxed properly since this would make privilege escalation issues possible. This does not affect system units which use the `User=` directive.

**Tip** [Firejail](../../en/Firejail.html "Firejail") can sandbox applications run as an unprivileged and explicitly allowed user but uses a SUID binary, which is in theory susceptible to privilege escalation vulnerabilities.

Because of the nature of other unit types, only service units can be hardened/sandboxed in the traditional sense. See [systemd.exec(5)](https://man.archlinux.org/man/systemd.exec.5) and [systemd.resource-control(5)](https://man.archlinux.org/man/systemd.resource-control.5) for more information.

## General {#General}

Since hardening/sandboxing effectively restricts an application, it is not possible to use all the sandboxing directives. A web server for example should not use `PrivateNetwork=true` since it usually needs network access.

`systemd-analyze security `*`unit`* generates a score for the unit showing all the used directives, which can be helpful to determine what settings to try next.

**Note** The score is slightly misleading. Only a simple `Hello world` can achieve a near perfect score. No application can use *all* the sandboxing settings.

Unfortunately, systemd\'s error messages on misconfiguration relating to sandboxing are sometimes vague and/or misleading. Setting the log level temporarily to `debug` may help getting actually relevant information.

    # systemctl log-level debug

## Capabilities {#Capabilities}

[capabilities(7)](https://man.archlinux.org/man/capabilities.7) are used to grant a process certain elevated privileges. For example, `CAP_NET_BIND_SERVICE` can be used so that an otherwise unprivileged process can bind ports below 1024, eliminating the need for it to start with root privileges at all. Another notable example is `CAP_DAC_READ_SEARCH` to grant a backup program unrestricted read access to all locations.

**Tip**

-   It is good practice to *always* use `CapabilityBoundingSet` and `AmbientCapabilities` together.
-   `systemd-analyze capability` provides a list of capabilities which can be used with systemd. This can be useful should you run an experimental kernel which adds capabilities.

In service units, you can accomplish this by using `AmbientCapabilities=` to grant it capabilities and `CapabilityBoundingSet=` to ensure nothing beyond the intended scope is granted:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
example.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
AmbientCapabilities=CAP_NET_BIND_SERVICE
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
```

It is also possible to remove capabilities from PID 1 and its children by using `CapabilityBoundingSet=` in `/etc/systemd/system.conf` or with a drop-in in `/etc/systemd/system.conf.d`. However, most of the capabilities are actually used, so they should not be removed.

## Common directives {#Common_directives}

Most of these directives can be applied to most applications without causing too many problems.

**Note** \"Impact\" and \"Potential for breakage\" are all *relative* since they depend on the environment and the unit.

### Without special configuration {#Without_special_configuration}

Simple boolean settings which can either be enabled or not. They can not be configured.

  -------------------------- ----------- ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Directive                  Impact^1^   Breakage^2^   Notes
  `LockPersonality`          Medium      Low           
  `MemoryDenyWriteExecute`   Medium      Medium        Incompatible with dynamically generated code at runtime, including JIT, executable stacks, C compiler code \"trampoline\". Can be enhanced with `SystemCallFilter`.
  `NoNewPrivileges`          High        Low           
  `PrivateDevices`           Medium      Low           `/dev/null` and similar will still be there.
  `PrivateNetwork`           High        Very high     Disallows *any* network access.
  `PrivateTmp`               Medium      Low           
  `PrivateUsers`             High        High          
  `RestrictRealtime`         Low         Low           May prevent denial-of-service situations.
  `RestrictSUIDSGID`         Medium      Low           Best used with `NoNewPrivileges`.
  -------------------------- ----------- ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  How effective the directive is
2.  How likely the directive is to break something

### Configurable directives {#Configurable_directives}

Most of these directives are quite powerful and will affect a lot. It is recommended to consider using at least some of them.

  --------------------------- -------------------------------- ----------- ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------
  Directive                   Value                            Impact^1^   Breakage^2^   Notes
  `ProtectSystem`             `strict`                         Very high   Very high     Usually used with `ReadWritePaths=`
                              `full`                           High        Medium        May break e.g web servers using [ACME](../../en/Transport_Layer_Security.html#ACME_clients "ACME") to renew their own keys which *may* be in `/etc`
                              `true`                           High        Medium        There are in theory few applications which write to `/boot` and `/usr`
  `ProtectHome`               `true`                           High        Medium        Some applications may need persistent data stored in `XDG_CONFIG_HOME`^3^
                              `tmpfs`                          High        Medium        Home directories contain a lot of sensitive data and using either `tmpfs` or `true` may prevent leaks.^4^
                              `read-only`                      Low         Low           Ideal for backup services
  `ProtectProc`^5^            `invisible`                      High        Medium        
                              `noaccess`                       Medium      Medium        
  `RestrictAddressFamilies`   e.g `AF_UNIX AF_INET AF_INET6`   Low         Low           Takes a space-separated list of address families, [address_families(7)](https://man.archlinux.org/man/address_families.7).
  --------------------------- -------------------------------- ----------- ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------

1.  How effective the directive is
2.  How likely the directive is to break something
3.  `StateDirectory=` can be used to mitigate some of the negative consequences
4.  This also makes `/run/user/` inaccessible, preventing leakage using IPC sockets. In theory, there may also be sockets elsewhere, e.g `/tmp`.
5.  Defaults to the [hidepid](../../en/Security.html#hidepid "Hidepid") value of the `/proc` mount when directive is omitted, which is usually `0` (unrestricted)

## Advanced directives {#Advanced_directives}

These directives are not useful for most units and are thus used more rarely.

  ---------------------------- ---------------------------------------------------- -------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Directive                    Value                                                Impact   Breakage   Notes
  `DynamicUser`                Boolean, e.g `true`                                  Medium   Medium     Needs to be combined with `StateDirectory=`, `RuntimeDirectory=`, `CacheDirectory=`, `LogsDirectory=` and `ConfigurationDirectory=`.[\[1\]](https://0pointer.net/blog/dynamic-users-with-systemd.html)
  `ProtectClock`^1,2^          Boolean                                              Low      Medium     Some users reported `smartctl` can not run when this is set, but this should be relatively safe.
  `ProtectControlGroups`^1^    Boolean                                              Medium   Low        
  `ProtectHostname`^1,2^       Boolean                                              Low      Low        
  `ProtectKernelLogs`^1^       Boolean                                              Low      Low        All official kernels have `SECURITY_DMESG_RESTRICT` set to `y`, but this is still defense in depth.
  `ProtectKernelModules`^1^    Boolean                                              Medium   Low        
  `ProtectKernelTunables`^1^   Boolean                                              Low      Low        
  `RestrictFileSystems`        e.g `ext4 tmpfs`                                     Medium   Medium     Takes a space-separated list of file systems or a set, e.g `@network`. See `systemd-analyze filesystems` for a full list.
  `SystemCallArchitectures`    e.g `native`                                         Low      Low        See also [#Disabling non-native syscalls](#Disabling_non-native_syscalls) - prefer using this to opt out a unit from the system default instead.
  `SystemCallFilter`           e.g `@system-service`                                Medium   High       See [systemd.exec(5) § SYSTEM CALL FILTERING](https://man.archlinux.org/man/systemd.exec.5#SYSTEM_CALL_FILTERING) - forgetting just a single syscall will lead to your application segfaulting at possibly inopportune times.
  `SocketBindAllow/Deny`       e.g `SocketBindAllow=ipv4:22` `SocketBindDeny=any`   Medium   Medium     Best combined with `CAP_NET_BIND_SERVICE` to ensure the privileged context can only bind to desired ports.
  ---------------------------- ---------------------------------------------------- -------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Redundant and unnecessary to specify if the service unit does not run with elevated privileges resulting from use of e.g `AmbientCapabilities=` or running as root. If a service unit is running as another normal and unprivileged `User=`, these settings are entirely superfluous and can be safely omitted.
2.  Restricts issuing corresponding syscalls only, but not access to IPC services shipped by systemd (namely *systemd-timedated* and *systemd-hostnamed*).[\[2\]](https://github.com/systemd/systemd/pull/35447#issuecomment-2512361567) Care must be taken to block the D-Bus/Varlink methods involved if absolute security is demanded.

### chroot jail {#chroot_jail}

**Warning** While this works in practice, it is partly relying on undocumented side effects of directives and can break at any time with new versions of systemd. For these reasons, it is considered unsupported by the developers of systemd. A feature request has been filed to make this an intended and supported functionality.[\[3\]](https://github.com/systemd/systemd/issues/33688)

It is possible to severely restrict what a process can see by specifying `TemporaryFileSystem=/:ro` and mounting required paths into this chroot-like jail. `RootDirectory` requires a directory to be present, whereas `TemporaryFileSystem` does not and will override `/` seamlessly. Both, and especially the latter, appear to be secure chroot-like directives, which can not be broken out easily, as they do not use the `chroot` syscall.

**Warning** `ProtectSystem` and `ProtectHome` are incompatible with `TemporaryFileSystem=/:ro` and will cause the latter to be undone, making `/` visible again. However, these directives are not needed since paths will be whitelisted anyways. See the warning above, this happens because interactions between these directives were never considered/supported.

All required paths must be mounted into this jail via `BindReadOnlyPaths` and `BindPaths`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
example_jailed_unit.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=Example unit

[Service]
ExecStart=/home/someuser/executable
User=someuser
Group=someuser
TemporaryFileSystem=/:ro
PrivateTmp=true
BindReadOnlyPaths=/usr/lib /lib64 /lib
BindPaths=/home/someuser/executable
```

This is a minimal example and most application will need more paths whitelisted. Some common paths include:

-   `/etc/ca-certificates`, `/etc/ssl`
-   `/etc/resolv.conf`
-   `/usr/share/zoneinfo`
-   Any sockets you need, e.g `/var/run/mysqld/mysqld.sock`

It will be likely that debugging is at some point necessary when trying to sandbox a unit for the first time. If a unit can not be started at all and fails with `status=203/EXEC`, either the executable itself or required libraries are not accessible. Starting with broad paths at first (e.g allowing the entirety of `/usr`) and narrowing it down later can help, too.

## system.conf

Changes to `/etc/systemd/system.conf` are global, so they will affect every unit. See [systemd-system.conf(5)](https://man.archlinux.org/man/systemd-system.conf.5)

### Disabling non-native syscalls {#Disabling_non-native_syscalls}

Non-native binaries, in almost all cases 32-bit binaries, may partially compromise the security of the system because they [do not have access to more hardening](../../en/Security.html#Userspace_ASLR_comparison "Security"). There have been some relatively minor vulnerabilities, like [CVE-2009-0835](https://www.cvedetails.com/cve/CVE-2009-0835/), which affected non-native syscalls.

**Note** This **will** break 32-bit binaries. Trying to execute such a binary will result in a file not found error.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
SystemCallArchitectures=native
```

This works well on most systems, but it needs to be at least partially disabled if e.g [multilib](../../en/Official_repositories.html#multilib "Multilib") is in use. Especially gaming with [Wine](../../en/Wine.html "Wine") may be impacted. Using `systemd-run` or modifying the session slice to override `SystemCallArchitectures` can be used to disable restrictions partially.

### Enabling more unit statistics {#Enabling_more_unit_statistics}

systemd does not track all resource usage of a unit by default. Enable `Default*Accounting` to get more statistics in the `systemctl status` output and the journal. This is not strictly a security setting, but it will certainly make debugging easier and can provide useful insights into resource usage.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
DefaultIOAccounting=yes
DefaultIPAccounting=yes
DefaultMemoryAccounting=yes
DefaultTasksAccounting=yes
```

## See also {#See_also}

[https://docs.rockylinux.org/10/guides/security/systemd_hardening/](https://docs.rockylinux.org/10/guides/security/systemd_hardening/)
