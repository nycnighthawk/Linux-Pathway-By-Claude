---
{"title": "NFS/Kerberos", "url": "https://wiki.archlinux.org/title/NFS/Kerberos", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# NFS/Kerberos

[Kerberos](../../en/Kerberos.html "Kerberos") is one of the few security mechanisms available for [NFS](../../en/NFS.html "NFS"). It provides strong per-user authentication, strong data encryption, and (with NFSv4) removes the requirement for matching UIDs/GIDs between client and server.

NFSv4 is recommended for Kerberos. Although it is possible to enable Kerberos in NFSv3, it will not provide 100% coverage as the auxiliary NFSv3 protocols (e.g. the \"mount\" protocol) remain insecure, and the lack of idmapping in NFSv3 severely reduces the usability of Kerberos as well.

## Prerequisites {#Prerequisites}

Kerberos requires a **KDC** (Key Distribution Center) service to be running somewhere. The `krb5-kdc.service` that comes with MIT Kerberos ([krb5](https://archlinux.org/packages/?name=krb5)) is a good option for small setups that do not warrant the complexity of Active Directory or FreeIPA. The second option is Heimdal, found on some BSDs and as [heimdal](https://aur.archlinux.org/packages/heimdal/)^AUR^ on Arch.

NFSv4 **idmapping** becomes much more important to have with Kerberos. Both the server and the clients should have the same idmapping domain configured:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/idmapd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[General]
Domain = example.com
```

## Server configuration {#Server_configuration}

Each NFS server needs a Kerberos principal for `nfs/`*`server.fqdn`* to be created on the KDC, and its keys added to the server\'s `/etc/krb5.keytab`.

**Note**

**This article or section needs expansion.**

**Reason:** Why? (Discuss in [Talk:NFS/Kerberos](../../en/Talk:NFS/Kerberos.html))

It is recommended to *also* have the standard `host/` principal there as well, for other purposes.

    fileserv# kadmin -p frob/admin
    Password for frob/admin@EXAMPLE.COM: *********
    kadmin:  addprinc -nokey nfs/fs.example.com
    kadmin:  ktadd nfs/fs.example.com

`gssproxy.service` must be [enabled](../../en/Help:Reading.html#Control_of_systemd_units "Enable") and [started](../../en/Help:Reading.html#Control_of_systemd_units "Start") on the server.

**Tip** Earlier systems used `rpc.svcgssd`, but it is no longer present in modern nfs-utils and has been fully superseded by gssproxy.

gssproxy comes pre-configured with NFS server support (the `/etc/gssproxy/24-nfs-server.conf` file is part of the standard package) and does not need any tweaking, other than placing the NFS service keytab in the standard location.

Your `/etc/exports` should offer the Kerberos authentication flavors in the `sec=` option:

    /home    *(rw,sec=krb5p)
    /usr     10.147.0.0/16(rw,sec=krb5p:krb5i:krb5:sys) *(rw,sec=krb5p)

**Note** Do not use the obsolete `gss/krb5p(...)` syntax. It still works, but you should not be using it anymore.

The available flavors are:

-   `krb5p` provides \'privacy\' (Kerberos-based encryption). It is sufficiently secure to be used over Internet, but might provide poor throughput over a LAN -- consider using `krb5` inside RPC-with-TLS instead.
-   `krb5i` provides \'integrity\' (Kerberos-based MAC) but *not* encryption. It might be useful for serving static data as it still protects against packet tampering.
-   `krb5` provides *only* authentication, without data integrity or encryption. It is a good choice if you have RPC-over-TLS enabled via `xprtsec=` *or* if Kerberos is being run over an otherwise \"secure\" LAN (e.g. over a WireGuard tunnel), but certainly not in the clear over public networks.
-   `sys` is the traditional UID-based (non-Kerberos) NFS security mode.

## Client configuration {#Client_configuration}

In addition to users, each NFS client should have a *machine* Kerberos principal in `/etc/krb5.keytab`, which will be used in situations where user Kerberos tickets are not yet available -- in particular, it will be needed to actually mount the filesystem at boot time before any users have logged in yet (or if mounting is done via autofs). More generally, all operations done \"as root\" will be authenticated as the machine principal.

**Tip** The machine identity is also mandatory for some internal NFS operations if NFSv4.0 or NFSv4.1 are used, although no longer mandatory in NFSv4.2.

Unlike in the server case, the client machine does not need an `nfs/` principal specifically -- it is enough to have the generic `host/`*`the.fqdn`* principal. (See the rpc.gssd manual page for what it looks for.)

The client must have `rpc-gssd.service` active (i.e. the `rpc.gssd` daemon).

Options used when mounting the filesystems are very similar to the options used in `/etc/exports`; you can specify one or more flavors using the `sec=` option. Although the client will automatically use the strongest mode offered, it is nevertheless recommended to explicitly require e.g. `sec=krb5p` to prevent downgrade attacks.

Once the filesystem has been mounted, root may already access it (using the machine\'s Kerberos credentials), but **every** non-root user needs their own Kerberos tickets to be present. This means either having the user manually run `kinit` for themselves, or setting up [pam-krb5](https://archlinux.org/packages/?name=pam-krb5) to acquire tickets during login (which only works for password-based logins), or using `gssproxy` or [k5start(1)](https://manned.org/k5start.1) (from [kstart](https://aur.archlinux.org/packages/kstart/)^AUR^) to acquire tickets from a keytab file.

**Tip** You will likely need to set up k5start to *renew* tickets as they expire a few hours after being acquired.
