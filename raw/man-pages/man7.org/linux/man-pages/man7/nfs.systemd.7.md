---
{"title": "nfs.systemd(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/nfs.systemd.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nfs.systemd(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NFS.SYSTEMD(7)       Miscellaneous Information Manual      NFS.SYSTEMD(7)

## [](#NAME)NAME

           nfs.systemd - managing NFS services through systemd.

## [](#SYNOPSIS)SYNOPSIS

           nfs-utils.service
           nfs-server.service
           nfs-client.target
           etc

## [](#DESCRIPTION)DESCRIPTION

           The nfs-utils package provides a suite of systemd unit files and
           generators which allow the various services to be started and
           managed.  These unit files and generators ensure that the services
           are started in the correct order, and the prerequisites are active
           before dependant services start.  As there are quite a few unit
           files and generators, it is not immediately obvious how best to
           achieve certain results.  The following subsections attempt to
           cover the issues that are most likely to come up.

       Configuration
           The standard systemd unit files do not provide any easy way to
           pass any command line arguments to daemons so as to configure
           their behavior.  In many case such configuration can be performed
           by making changes to /etc/nfs.conf or other configuration files
           (see nfs.conf(5)).  When that is not convenient, a distribution
           might provide systemd "drop-in" files which replace the ExecStart=
           setting to start the program with different arguments.  For
           example a drop-in file systemd/system/nfs-
           mountd.service.d/local.conf containing
                  [Service]
                  EnvironmentFile=/etc/sysconfig/nfs
                  ExecStart=
                  ExecStart= /usr/sbin/rpc.mountd $RPCMOUNTDOPTS
           would cause the nfs-mountd.service unit to run the rpc.mountd
           program using, for arguments, the value given for RPCMOUNTDOPTS in
           /etc/sysconfig/nfs.  This allows for seamless integration with
           existing configuration tools.

       Enabling unit files
           There are three unit files which are designed to be manually
           enabled.  All others are automatically run as required.  The three
           are:

           nfs-client.target
                  This should be enabled on any host which ever serves as an
                  NFS client.  There is little cost in transparently enabling
                  it whenever NFS client software is installed.

           nfs-server.service
                  This must be enabled to provide NFS service to clients.  It
                  starts and configures the required daemons in the required
                  order.

           nfs-blkmap.service
                  The blkmapd daemon is only required on NFS clients which
                  are using pNFS (parallel NFS), and particularly using the
                  blocklayout layout protocol.  If you might use this
                  particular extension to NFS, the nfs-blkmap.service unit
                  should be enabled.

           Several other units which might be considered to be optional, such
           as rpc-gssd.service are careful to only start if the required
           configuration file exists.  rpc-gssd.service will not start if the
           krb5.keytab file does not exist (typically in /etc).

       Restarting NFS services
           Most NFS daemons can be restarted at any time.  They will reload
           any state that they need, and continue servicing requests.  This
           is rarely necessary though.

           When configuration changes are made, it can be hard to know
           exactly which services need to be restarted to ensure that the
           configuration takes effect.  The simplest approach, which is often
           the best, is to restart everything.  To help with this, the nfs-
           utils.service unit is provided.  It declares appropriate
           dependencies with other unit files so that
                  systemctl restart nfs-utils
           will restart all NFS daemons that are running.  This will cause
           all configuration changes to take effect except for changes to
           mount options lists in /etc/fstab or /etc/nfsmount.conf.  Mount
           options can only be changed by unmounting and remounting
           filesystem.  This can be a disruptive operation so it should only
           be done when the value justifies the cost.  The command
                  umount -a -t nfs; mount -a -t nfs
           should unmount and remount all NFS filesystems.

       Masking unwanted services
           Rarely there may be a desire to prohibit some services from
           running even though there are normally part of a working NFS
           system.  This may be needed to reduce system load to an absolute
           minimum, or to reduce attack surface by not running daemons that
           are not absolutely required.

           Three particular services which this can apply to are rpcbind,
           idmapd, and rpc-gssd.  rpcbind is not part of the nfs-utils
           package, but it used by several NFS services.  However it is not
           needed when only NFSv4 is in use.  If a site will never use NFSv3
           (or NFSv2) and does not want rpcbind to be running, the correct
           approach is to run
                  systemctl mask rpcbind
           This will disable rpcbind, and the various NFS services which
           depend on it (and are only needed for NFSv3) will refuse to start,
           without interfering with the operation of NFSv4 services.  In
           particular, rpc.statd will not run when rpcbind is masked.

           idmapd is only needed for NFSv4, and even then is not needed when
           the client and server agree to use user-ids rather than user-names
           to identify the owners of files.  If idmapd is not needed and not
           wanted, it can be masked with
                  systemctl mask idmapd
           rpc-gssd is assumed to be needed if the krb5.keytab file is
           present.  If a site needs this file present but does not want rpc-
           gssd running, it can be masked with
                  systemctl mask rpc-gssd

       Generators
           systemd unit generators are small executables placed in
           /usr/lib/systemd/system-generators/ to dynamically extend the unit
           file hierarchy.  The nfs-utils package provides three:

           nfsroot-generator
                  It creates the sysroot.mount unit to mount /sysroot via
                  NFSv4 in the initrd, if it detects one the following
                  options in the kernel command line:

                  root=/dev/nfs nfsroot=[<server>:]<path>[,<options>]

                         Defined in <kernel_source>/Documentation/admin-
                         guide/nfs/nfsroot.rst

                  root=nfs[4]:[<server>:]<path>[:<options>]

                         Defined in dracut.cmdline(7).

                         NOTE: Although "nfs" can be used as type indicator
                         for the mountpoint, the mount unit will use always
                         "nfs4".

           nfs-server-generator
                  It creates ordering dependencies between nfs-server.service
                  and various filesystem mounts: it should start before any
                  "nfs" mountpoints are mounted, in case they are loop-back
                  mounts, and after all exported filesystems are mounted, so
                  there is no risk of exporting the underlying directory.

           rpc-pipefs-generator
                  It creates ordering dependencies between NFS services and
                  the rpc_pipefs mountpoint.

## [](#FILES)FILES

           /etc/nfs.conf
           /etc/nfsmount.conf
           /etc/idmapd.conf

           Also similar files in /usr/etc and in related conf.d drop-in
           directories.

## [](#SEE_ALSO)SEE ALSO

           bootup(7), systemd.generator(7), systemd.unit(5), nfs.conf(5),
           nfsmount.conf(5).

## [](#COLOPHON)COLOPHON

           This page is part of the nfs-utils (NFS utilities) project.
           Information about the project can be found at 
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  If you have a bug
           report for this manual page, see
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.linux-nfs.org/projects/steved/nfs-utils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-23.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                                               NFS.SYSTEMD(7)

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
