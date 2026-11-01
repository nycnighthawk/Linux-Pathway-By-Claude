---
{"title": "NFS/Troubleshooting", "url": "https://wiki.archlinux.org/title/NFS/Troubleshooting", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# NFS/Troubleshooting

Related articles

-   [NFS](../../en/NFS.html "NFS")

**This article or section is out of date.**

**Reason:** Not all sections are up-to-date with NFSv4 changes. (Discuss in [Talk:NFS/Troubleshooting](../../en/Talk:NFS/Troubleshooting.html))

Dedicated article for common problems and solutions.

## Server-side issues {#Server-side_issues}

### exportfs: /etc/exports:2: syntax error: bad option list {#exportfs:_/etc/exports:2:_syntax_error:_bad_option_list}

Make sure to delete all space from the option list in `/etc/exports`.

### exportfs: requires fsid= for NFS export {#exportfs:_requires_fsid=_for_NFS_export}

As not all filesystems are stored on devices and not all filesystems have UUIDs (e.g. [FUSE](../../en/FUSE.html "FUSE")), it is sometimes necessary to explicitly tell NFS how to identify a filesystem. This is done with the `fsid` option:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/exports
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/srv/nfs client(rw,sync,crossmnt,fsid=0)
/srv/nfs/music client(rw,sync,fsid=10)
```

### Group/GID permissions issues {#Group/GID_permissions_issues}

If NFS shares mount fine, and are fully accessible to the owner, but not to group members; check the number of groups that user belongs to. NFS has a limit of 16 on the number of groups a user can belong to. If you have users with more than this, you need to enable the `manage-gids` start-up flag on the NFS server:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nfs.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[mountd]
manage-gids=y
```

### \"Permission denied\" when trying to write files as root {#\"Permission_denied\"_when_trying_to_write_files_as_root}

-   If you need to mount shares as root, and have full r/w access from the client, add the no_root_squash option to the export in `/etc/exports`:

&nbsp;

    /var/cache/pacman/pkg 192.168.1.0/24(rw,no_subtree_check,no_root_squash)

-   You must also add no_root_squash to the first line in `/etc/exports`:

&nbsp;

    / 192.168.1.0/24(rw,fsid=root,no_root_squash,no_subtree_check)

### \"RPC: Program not registered\" when showmount -e command issued {#\"RPC:_Program_not_registered\"_when_showmount_-e_command_issued}

Make sure that `nfs-server.service` and `rpcbind.service` are running on the server site, see [systemd](../../en/Systemd.html "Systemd"). If they are not, start and enable them.

Also make sure NFSv3 is enabled. *showmount* does **not** work with NFSv4-only servers.

### UDP mounts not working {#UDP_mounts_not_working}

*nfs-utils* disabled serving NFS over UDP in version 2.2.1. Arch core updated to 2.3.1 on 21 Dec 2017 (skipping over 2.2.1.) If UDP stopped working then, add `udp=y` under `[nfsd]` in `/etc/nfs.conf`. Then restart `nfs-server.service`.

### Timeout with big directories {#Timeout_with_big_directories}

Since *nfs-utils* version 1.0.x, every subdirectory is checked for permissions. This can lead to timeout on directories with a \"large\" number of subdirectories, even a few hundreds.

To disable this behaviour, add the option `no_subtree_check` to `/etc/exports` to the share directory.

## Client-side issues {#Client-side_issues}

### mount.nfs4: No such device {#mount.nfs4:_No_such_device}

Make sure the `nfsd` [kernel module](../../en/Kernel_module.html "Kernel module") has been loaded. This may also occur if you [have not rebooted](../../en/General_troubleshooting.html#Cannot_use_some_peripherals_after_kernel_upgrade "General troubleshooting") after a kernel update.

### mount.nfs4: Invalid argument {#mount.nfs4:_Invalid_argument}

[Enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") and [start](../../en/Help:Reading.html#Control_of_systemd_units "Start") `nfs-client.target` and make sure the appropriate daemons (nfs-idmapd, rpc-gssd, etc) are running on the server.

### mount.nfs4: Network is unreachable {#mount.nfs4:_Network_is_unreachable}

Users making use of [systemd-networkd](../../en/Systemd-networkd.html "Systemd-networkd") or [NetworkManager](../../en/NetworkManager.html "NetworkManager") might notice [NFS](../../en/NFS.html "NFS") mounts are not mounted when booting.

Force the network to be completely configured by [enabling](../../en/Help:Reading.html#Control_of_systemd_units "Enabling") `systemd-networkd-wait-online.service` or `NetworkManager-wait-online.service`. This may slow down the boot-process because fewer services run in parallel.

**Tip** If the NFS server is only expecting IPV4 addresses, and you are using `NetworkManager-wait-online.service`, set `ipv4.may-fail=no` in your network profile to make sure that an IPV4 address is acquired before the `NetworkManager-wait-online.service` is reached.

### mount.nfs4: an incorrect mount option was specified {#mount.nfs4:_an_incorrect_mount_option_was_specified}

This can happen if using the `sec=krb5` option without `nfs-client.target` and/or `rpc-gssd.service` running. Starting and enabling those services should resolve the issue.

### Unable to connect from OS X clients {#Unable_to_connect_from_OS_X_clients}

When trying to connect from an OS X client, you will see that everything is ok in the server logs, but OS X will refuse to mount your NFS share. You can do one of two things to fix this:

-   On the NFS server, add the `insecure` option to the share in `/etc/exports` and re-run `exportfs -r`.

\... **OR** \...

-   On the OS X client, add the `resvport` option to the `mount` command line. You can also set `resvport` as a default client mount option in `/etc/nfs.conf`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/nfs.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
nfs.client.mount.options = resvport
```

Using the default client mount option should also affect mounting the share from Finder via \"Connect to Server\...\".

### Unreliable connection from OS X clients {#Unreliable_connection_from_OS_X_clients}

OS X\'s NFS client is optimized for OS X Servers and might present some issues with Linux servers. If you are experiencing slow performance, frequent disconnects and problems with international characters edit the default mount options by adding the line `nfs.client.mount.options = intr,locallocks,nfc` to `/etc/nfs.conf` on your Mac client. More information about the mount options can be found in the OS X [mount_nfs(8)](https://www.unix.com/man-page/osx/8/mount_nfs/).

### Intermittent client freezes when copying large files {#Intermittent_client_freezes_when_copying_large_files}

If you copy large files from your client machine to the NFS server, the transfer speed is *very* fast, but after some seconds the speed drops and your client machine intermittently locks up completely for some time until the transfer is finished.

Try adding `sync` as a mount option on the client (e.g. in `/etc/fstab`) to fix this problem.

### mount.nfs: Operation not permitted {#mount.nfs:_Operation_not_permitted}

#### NFSv4 {#NFSv4}

If you use [Kerberos](../../en/Kerberos.html "Kerberos") (`sec=krb5*`), make sure the client and server clocks are correct. Using [ntpd](../../en/Network_Time_Protocol_daemon.html "Ntpd") or [systemd-timesyncd](../../en/Systemd-timesyncd.html "Systemd-timesyncd") is recommended. Also, check that the canonical name for the server as resolved on the client (see [Domain name resolution](../../en/Domain_name_resolution.html "Domain name resolution")) matches the name in the server\'s NFS principal.

#### NFSv3 and earlier {#NFSv3_and_earlier}

*nfs-utils* versions 1.2.1-2 or higher use NFSv4 by default, resulting in NFSv3 shares failing on upgrade. The problem can be solved by using either mount option `'vers=3'` or `'nfsvers=3'` on the command line:

    # mount.nfs remote target directory -o ...,vers=3,...
    # mount.nfs remote target directory -o ...,nfsvers=3,...

or in `/etc/fstab`:

    remote target directory nfs ...,vers=3,... 0 0
    remote target directory nfs ...,nfsvers=3,... 0 0

### mount.nfs: Protocol not supported {#mount.nfs:_Protocol_not_supported}

This error occurs when you include the export root in the path of the NFS source. For example:

    # mount SERVER:/srv/nfs4/media /mnt
    mount.nfs4: Protocol not supported

Use the relative path instead:

    # mount SERVER:/media /mnt

### Permissions issues {#Permissions_issues}

If you find that you cannot set the permissions on files properly, make sure the [user](../../en/Users_and_groups.html "User")/[user group](../../en/User_group.html "User group") are **both** on the client and server.

If all your files are owned by `nobody`, and you are using NFSv4, on both the client and server, you should ensure that the `nfs-idmapd.service` has been started.

On some systems detecting the domain from FQDN minus hostname does not seem to work reliably. If files are still showing as `nobody` after the above changes, edit `/etc/idmapd.conf`, ensure that `Domain` is set to `FQDN minus hostname`. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/idmapd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[General]
Domain = domain.ext

[Mapping]

Nobody-User = nobody
Nobody-Group = nobody

[Translation]

Method = nsswitch
```

### Problems with Vagrant and synced_folders {#Problems_with_Vagrant_and_synced_folders}

If you get an error about unuspported protocol, you need to enable NFS over UDP on your host (or make Vagrant use NFS over TCP.) See [#UDP mounts not working](#UDP_mounts_not_working).

If Vagrant scripts are unable to mount folders over NFS, installing the *net-tools* package may solve the issue.

### fstab entry not mounted on boot {#fstab_entry_not_mounted_on_boot}

If you have an NFS filesystem mount entry in `/etc/fstab` but the filesystem is not mounted after the system is booted up, verify the status of `remote-fs.target`: it should be [enabled](../../en/Help:Reading.html#Control_of_systemd_units "Enable").

## Performance issues {#Performance_issues}

This [NFS Howto page](https://nfs.sourceforge.net/nfs-howto/ar01s05.html) has some useful information regarding performance. Here are some further tips:

### Diagnose the problem {#Diagnose_the_problem}

-   **Htop** should be your first port of call. The most obvious symptom will be a maxed-out CPU.
-   Press F2, and under \"Display options\", enable \"Detailed CPU time\". Press F1 for an explanation of the colours used in the CPU bars. In particular, is the CPU spending most of its time responding to IRQs, or in Wait-IO (wio)?

### Close-to-open/flush-on-close {#Close-to-open/flush-on-close}

**Symptoms:** Your clients are writing many small files. The server CPU is not maxed out, but there is very high wait-IO, and the server disk seems to be churning more than you might expect.

In order to ensure data consistency across clients, the NFS protocol requires that the client\'s cache is flushed (all data is pushed to the server) whenever a file is closed after writing. Because the server is not allowed to buffer disk writes (if it crashes, the client will not realise the data was not written properly), the data is written to disk immediately before the client\'s request is completed. When you are writing lots of small files from the client, this means that the server spends most of its time waiting for small files to be written to its disk, which can cause a significant reduction in throughput.

See [this excellent article](https://docstore.mik.ua/orelly/networking_2ndEd/nfs/ch07_04.htm) or the **nfs** manpage for more details on the close-to-open policy. There are several approaches to solving this problem:

#### The nocto mount option {#The_nocto_mount_option}

**Warning** The Linux kernel does not seem to honor this option properly. Files are still flushed when they are closed.

If all of the following conditions are satisfied:

-   The export you have mounted on the client is only going to be used by the one client.
-   It does not matter too much if a file written on one client does not immediately appear on other clients.
-   It does not matter if after a client has written a file, and the client thinks the file has been saved, and then the client crashes, the file may be lost.

Use the **nocto** mount option, which will disable the close-to-open behavior.

#### The async export option {#The_async_export_option}

Does your situation match these conditions?

-   It is important that when a file is closed after writing on one client, it is:
    -   Immediately visible on all the other clients.
    -   Safely stored on the server, even if the client crashes immediately after closing the file.
-   It is not important to you that if the server crashes:
    -   You may lose the files that were most recently written by clients.
    -   When the server is restarted, the clients will believe their recent files exist, even though they were actually lost.

In this situation, you can use `async` instead of `sync` in the server\'s `/etc/exports` file for those specific exports. See the **exports** manual page for details. In this case, it does not make sense to use the `nocto` mount option on the client.

### Buffer cache size and MTU {#Buffer_cache_size_and_MTU}

**Symptoms:** High kernel or IRQ CPU usage, a very high packet count through the network card.

This is a trickier optimisation. Make sure this is definitely the problem before spending too much time on this. The default values are usually fine for most situations.

See [this article](https://docstore.mik.ua/orelly/networking_2ndEd/nfs/ch07_03.htm) for information about I/O buffering in NFS. Essentially, data is accumulated into buffers before being sent. The size of the buffer will affect the way data is transmitted over the network. The Maximum Transmission Unit (MTU) of the network equipment will also affect throughput, as the buffers need to be split into MTU-sized chunks before they are sent over the network. If your buffer size is too big, the kernel or hardware may spend too much time splitting it into MTU-sized chunks. If the buffer size is too small, there will be overhead involved in sending a very large number of small packets. You can use the **rsize** and **wsize** mount options on the client to alter the buffer cache size. To achieve the best throughput, you need to experiment and discover the best values for your setup.

It is possible to change the MTU of many network cards. If your clients are on a separate subnet (e.g. for a Beowulf cluster), it may be safe to configure all of the network cards to use a high MTU. This should be done in very-high-bandwidth environments.

See [NFS#Performance tuning](../../en/NFS.html#Performance_tuning "NFS") for more information.

## Debugging {#Debugging}

### Using rpcdebug {#Using_rpcdebug}

Using `rpcdebug` is the easiest way to manipulate the kernel interfaces in place of echoing bitmasks to /proc.

  ------------- ---------------------------------------------------------------------------------------------------------
  Option        Description
  -c            Clear the given debug flags
  -s            Set the given debug flags
  -m *module*   Specify which module\'s flags to set or clear.
  -v            Increase the verbosity of rpcdebug\'s output
  -h            Print a help message and exit. When combined with the -v option, also prints the available debug flags.
  ------------- ---------------------------------------------------------------------------------------------------------

For the **-m** option, the available modules are:

  -------- ---------------------------------------------------------------------
  Module   Description
  nfsd     The NFS server
  nfs      The NFS client
  nlm      The Network Lock Manager, in either an NFS client or server
  rpc      The Remote Procedure Call module, in either an NFS client or server
  -------- ---------------------------------------------------------------------

Examples:

    rpcdebug -m rpc -s all    # sets all debug flags for RPC
    rpcdebug -m rpc -c all    # clears all debug flags for RPC

    rpcdebug -m nfsd -s all   # sets all debug flags for NFS Server
    rpcdebug -m nfsd -c all   # clears all debug flags for NFS Server

Once the flags are set you can tail the journal for the debug output, usually by running `journalctl -fl` as root or similar.

### Using mountstats {#Using_mountstats}

The [nfs-utils](https://archlinux.org/packages/?name=nfs-utils) package contains the `mountstats` tool, which can retrieve a lot of statistics about NFS mounts, including average timings and packet size.

    $ mountstats 
    Stats for example:/tank mounted on /tank:
      NFS mount options: rw,sync,vers=4.2,rsize=524288,wsize=524288,namlen=255,acregmin=3,acregmax=60,acdirmin=30,acdirmax=60,soft,proto=tcp,port=0,timeo=15,retrans=2,sec=sys,clientaddr=xx.yy.zz.tt,local_lock=none
      NFS server capabilities: caps=0xfbffdf,wtmult=512,dtsize=32768,bsize=0,namlen=255
      NFSv4 capability flags: bm0=0xfdffbfff,bm1=0x40f9be3e,bm2=0x803,acl=0x3,sessions,pnfs=notconfigured
      NFS security flavor: 1  pseudoflavor: 0

    NFS byte counts:
      applications read 248542089 bytes via read(2)
      applications wrote 0 bytes via write(2)
      applications read 0 bytes via O_DIRECT read(2)
      applications wrote 0 bytes via O_DIRECT write(2)
      client read 171375125 bytes via NFS READ
      client wrote 0 bytes via NFS WRITE

    RPC statistics:
      699 RPC requests sent, 699 RPC replies received (0 XIDs not found)
      average backlog queue length: 0

    READ:
        338 ops (48%) 
        avg bytes sent per op: 216  avg bytes received per op: 507131
        backlog wait: 0.005917  RTT: 548.736686     total execute time: 548.775148 (milliseconds)
    GETATTR:
        115 ops (16%) 
        avg bytes sent per op: 199  avg bytes received per op: 240
        backlog wait: 0.008696  RTT: 15.756522  total execute time: 15.843478 (milliseconds)
    ACCESS:
        93 ops (13%) 
        avg bytes sent per op: 203  avg bytes received per op: 168
        backlog wait: 0.010753  RTT: 2.967742   total execute time: 3.032258 (milliseconds)
    LOOKUP:
        32 ops (4%) 
        avg bytes sent per op: 220  avg bytes received per op: 274
        backlog wait: 0.000000  RTT: 3.906250   total execute time: 3.968750 (milliseconds)
    OPEN_NOATTR:
        25 ops (3%) 
        avg bytes sent per op: 268  avg bytes received per op: 350
        backlog wait: 0.000000  RTT: 2.320000   total execute time: 2.360000 (milliseconds)
    CLOSE:
        24 ops (3%) 
        avg bytes sent per op: 224  avg bytes received per op: 176
        backlog wait: 0.000000  RTT: 30.250000  total execute time: 30.291667 (milliseconds)
    DELEGRETURN:
        23 ops (3%) 
        avg bytes sent per op: 220  avg bytes received per op: 160
        backlog wait: 0.000000  RTT: 6.782609   total execute time: 6.826087 (milliseconds)
    READDIR:
        4 ops (0%) 
        avg bytes sent per op: 224  avg bytes received per op: 14372
        backlog wait: 0.000000  RTT: 198.000000     total execute time: 198.250000 (milliseconds)
    SERVER_CAPS:
        2 ops (0%) 
        avg bytes sent per op: 172  avg bytes received per op: 164
        backlog wait: 0.000000  RTT: 1.500000   total execute time: 1.500000 (milliseconds)
    FSINFO:
        1 ops (0%) 
        avg bytes sent per op: 172  avg bytes received per op: 164
        backlog wait: 0.000000  RTT: 2.000000   total execute time: 2.000000 (milliseconds)
    PATHCONF:
        1 ops (0%) 
        avg bytes sent per op: 164  avg bytes received per op: 116
        backlog wait: 0.000000  RTT: 1.000000   total execute time: 1.000000 (milliseconds)

### Kernel Interfaces {#Kernel_Interfaces}

A bitmask of the debug flags can be echoed into the interface to enable output to syslog; 0 is the default:

    /proc/sys/sunrpc/nfsd_debug
    /proc/sys/sunrpc/nfs_debug
    /proc/sys/sunrpc/nlm_debug
    /proc/sys/sunrpc/rpc_debug

Sysctl controls are registered for these interfaces, so they can be used instead of echo:

    sysctl -w sunrpc.rpc_debug=1023
    sysctl -w sunrpc.rpc_debug=0

    sysctl -w sunrpc.nfsd_debug=1023
    sysctl -w sunrpc.nfsd_debug=0

At runtime the server holds information that can be examined:

    grep . /proc/net/rpc/*/content
    cat /proc/fs/nfs/exports
    cat /proc/net/rpc/nfsd
    ls -l /proc/fs/nfsd

A rundown of `/proc/net/rpc/nfsd` (the userspace tool `nfsstat` pretty-prints this info):

    * rc (reply cache): <hits> <misses> <nocache>
    - hits: client it's retransmitting
    - misses: a operation that requires caching
    - nocache: a operation that no requires caching

    * fh (filehandle): <stale> <total-lookups> <anonlookups> <dir-not-in-cache> <nodir-not-in-cache>
    - stale: file handle errors
    - total-lookups, anonlookups, dir-not-in-cache, nodir-not-in-cache
      . always seem to be zeros

    * io (input/output): <bytes-read> <bytes-written>
    - bytes-read: bytes read directly from disk
    - bytes-written: bytes written to disk

    * th (threads): <threads> <fullcnt> <10%-20%> <20%-30%> ... <90%-100%> <100%>
      DEPRECATED:  All fields after <threads> are hard-coded to 0
    - threads: number of nfsd threads
    - fullcnt: number of times that the last 10% of threads are busy
    - 10%-20%, 20%-30% ... 90%-100%: 10 numbers representing 10-20%, 20-30% to 100%
      . Counts the number of times a given interval are busy

    * ra (read-ahead): <cache-size> <10%> <20%> ... <100%> <not-found>
    - cache-size: always the double of number threads
    - 10%, 20% ... 100%: how deep it found what was looking for
    - not-found: not found in the read-ahead cache

    * net: <netcnt> <netudpcnt> <nettcpcnt> <nettcpconn>
    - netcnt: counts every read
    - netudpcnt: counts every UDP packet it receives
    - nettcpcnt: counts every time it receives data from a TCP connection
    - nettcpconn: count every TCP connection it receives

    * rpc: <rpccnt> <rpcbadfmt+rpcbadauth+rpcbadclnt> <rpcbadfmt> <rpcbadauth> <rpcbadclnt>
    - rpccnt: counts all rpc operations
    - rpcbadfmt: counts if while processing a RPC it encounters the following errors:
      . err_bad_dir, err_bad_rpc, err_bad_prog, err_bad_vers, err_bad_proc, err_bad
    - rpcbadauth: bad authentication
      . does not count if you try to mount from a machine that it's not in your exports file
    - rpcbadclnt: unused

    * procN (N = vers): <vs_nproc> <null> <getattr> <setattr> <lookup> <access> <readlink> <read> <write> <create> <mkdir> <symlink> <mknod> <remove> <rmdir> <rename> <link> <readdir> <readdirplus> <fsstat> <fsinfo> <pathconf> <commit>
    - vs_nproc: number of procedures for NFS version
      . v2: nfsproc.c, 18
      . v3: nfs3proc.c, 22
      - v4, nfs4proc.c, 2
    - statistics: generated from NFS operations at runtime

    * proc4ops: <ops> <x..y>
    - ops: the definition of LAST_NFS4_OP, OP_RELEASE_LOCKOWNER = 39, plus 1 (so 40); defined in nfs4.h
    - x..y: the array of nfs_opcount up to LAST_NFS4_OP (nfsdstats.nfs4_opcount[i])

### NFSD debug flags {#NFSD_debug_flags}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/usr/include/linux/nfsd/debug.h
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/*
 * knfsd debug flags
 */
#define NFSDDBG_SOCK            0x0001
#define NFSDDBG_FH              0x0002
#define NFSDDBG_EXPORT          0x0004
#define NFSDDBG_SVC             0x0008
#define NFSDDBG_PROC            0x0010
#define NFSDDBG_FILEOP          0x0020
#define NFSDDBG_AUTH            0x0040
#define NFSDDBG_REPCACHE        0x0080
#define NFSDDBG_XDR             0x0100
#define NFSDDBG_LOCKD           0x0200
#define NFSDDBG_ALL             0x7FFF
#define NFSDDBG_NOCHANGE        0xFFFF
```

### NFS debug flags {#NFS_debug_flags}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/usr/include/linux/nfs_fs.h
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/*
 * NFS debug flags
 */
#define NFSDBG_VFS              0x0001
#define NFSDBG_DIRCACHE         0x0002
#define NFSDBG_LOOKUPCACHE      0x0004
#define NFSDBG_PAGECACHE        0x0008
#define NFSDBG_PROC             0x0010
#define NFSDBG_XDR              0x0020
#define NFSDBG_FILE             0x0040
#define NFSDBG_ROOT             0x0080
#define NFSDBG_CALLBACK         0x0100
#define NFSDBG_CLIENT           0x0200
#define NFSDBG_MOUNT            0x0400
#define NFSDBG_FSCACHE          0x0800
#define NFSDBG_PNFS             0x1000
#define NFSDBG_PNFS_LD          0x2000
#define NFSDBG_STATE            0x4000
#define NFSDBG_ALL              0xFFFF
```

### NLM debug flags {#NLM_debug_flags}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/usr/include/linux/lockd/debug.h
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/*
 * Debug flags
 */
#define NLMDBG_SVC      0x0001
#define NLMDBG_CLIENT       0x0002
#define NLMDBG_CLNTLOCK     0x0004
#define NLMDBG_SVCLOCK      0x0008
#define NLMDBG_MONITOR      0x0010
#define NLMDBG_CLNTSUBS     0x0020
#define NLMDBG_SVCSUBS      0x0040
#define NLMDBG_HOSTCACHE    0x0080
#define NLMDBG_XDR      0x0100
#define NLMDBG_ALL      0x7fff
```

### RPC debug flags {#RPC_debug_flags}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/usr/include/linux/sunrpc/debug.h
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/*
 * RPC debug facilities
 */
#define RPCDBG_XPRT             0x0001
#define RPCDBG_CALL             0x0002
#define RPCDBG_DEBUG            0x0004
#define RPCDBG_NFS              0x0008
#define RPCDBG_AUTH             0x0010
#define RPCDBG_BIND             0x0020
#define RPCDBG_SCHED            0x0040
#define RPCDBG_TRANS            0x0080
#define RPCDBG_SVCXPRT          0x0100
#define RPCDBG_SVCDSP           0x0200
#define RPCDBG_MISC             0x0400
#define RPCDBG_CACHE            0x0800
#define RPCDBG_ALL              0x7fff
```

### See also {#See_also}

-   [rpcdebug(8)](https://man.archlinux.org/man/rpcdebug.8)
-   [http://utcc.utoronto.ca/\~cks/space/blog/linux/NFSClientDebuggingBits](https://cns.utoronto.ca/~cks/space/blog/linux/NFSClientDebuggingBits)
-   [http://www.novell.com/support/kb/doc.php?id=7011571](https://www.novell.com/support/kb/doc.php?id=7011571)
-   [http://stromberg.dnsalias.org/\~strombrg/NFS-troubleshooting-2.html](https://stromberg.dnsalias.org/~strombrg/NFS-troubleshooting-2.html)
-   [https://lore.kernel.org/linux-nfs/471D17F8.5060709@cesca.es/](https://lore.kernel.org/linux-nfs/471D17F8.5060709@cesca.es/)
