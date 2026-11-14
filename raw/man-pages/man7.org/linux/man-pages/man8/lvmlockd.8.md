---
{"title": "lvmlockd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lvmlockd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvmlockd(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SETUP](#SETUP) \| [SETUP DETAILS](#SETUP_DETAILS) \| [TOPICS](#TOPICS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVMLOCKD(8)              System Manager's Manual              LVMLOCKD(8)

## [](#NAME)NAME

           lvmlockd — LVM locking daemon

## [](#SYNOPSIS)SYNOPSIS

           lvmlockd [options]

## [](#DESCRIPTION)DESCRIPTION

           A shared Volume Group is a VG placed on shared storage devices,
           e.g. from a SAN, that can be used by all the hosts that can access
           the devices.  A shared VG requires the use of lvmlockd, and an
           external lock manager.

           Different hosts may activate and use LVs in the same shared VG,
           and different hosts can create, extend, or remove LVs in the VG.
           Locking, through lvmlockd, ensures this is all done safely and
           consistently.  LVM commands request locks from lvmlockd, which
           passes the lock requests to an external lock manager.  Each shared
           VG has a locktype attribute, specifying the external lock manager
           to use for the VG.

           The lock manager options are: sanlock which places locks on
           storage space reserved within the VG, and dlm which uses a network
           locking protocol, and has additional clustering requirements.

           There are three types of locking performed through lvmlockd:
           • per-VG locks protect changes to the VG metadata.
           • LV locks limit LV activation to one host at a time.
           • A Global lock protects unused PVs and the VG namespace.

## [](#OPTIONS)OPTIONS

           lvmlockd daemon command line options:

           -h|--help
                  Show this help information.

           -V|--version
                  Show version of lvmlockd.

           -T|--test
                  Test mode, do not call lock manager.

           -f|--foreground
                  Don't fork.

           -D|--daemon-debug
                  Don't fork and print debugging to stdout.

           -p|--pid-file path
                  Set path to the pid file.

           -s|--socket-path path
                  Set path to the socket to listen on.

           --adopt-file path
                  Set path to the adopt file.

           -S|--syslog-priority err|warning|debug
                  Write log messages from this level up to syslog.

           -g|--gl-type sanlock|dlm
                  Set global lock type to be sanlock or dlm.

           -i|--host-id num
                  Set the local sanlock host id.

           -F|--host-id-file path
                  A file containing the local sanlock host_id.

           -o|--sanlock-timeout seconds
                  Override the default sanlock I/O timeout.

           -A|--adopt 0|1
                  Enable (1) or disable (0) lock adoption.

## [](#SETUP)SETUP

           The following steps provide a quick overview of how to use shared
           VGs.  More details can be found under SETUP DETAILS.

           Devices

           Identify the shared device(s) that will be used in the shared VG,
           and add them to each host's devices file (local device names often
           differ, unless a WWN-based name from /dev/disk/by-id is used.)
           $ lvmdevices --adddev device

           Configuration

           Edit lvm.conf, setting use_lvmlockd=1 on each host using a shared
           VG.

           Edit lvmlocal.conf, setting host_id on each host (only required
           when using sanlock.)  The host_id is a unique integer for each
           host between 1 and 2000.

           Locking

           Start lvmlockd and the external lock manager (sanlock or dlm) on
           each host.

           VG

           Create a shared VG from one host (uses the running lock manager):
           $ vgcreate --shared VG devices

           Include vgcreate options to use Persistent Reservations (sanlock
           only):
           --setpersist y --setlockargs persist,notimeout

           Start Persistent Reservations for the VG (if they are used):
           $ vgchange --persist start VG

           Start the lockspace for the shared VG on all hosts:
           $ vgchange --lockstart VG

           Usage

           Begin using the VG, e.g. creating LVs.

           Regular shutdown steps:
               $ vgchange -an VG
               $ vgchange --lockstop [--persist stop] VG
               $ stop lvmlockd and lock manager

           Regular startup steps:
               $ start lvmlockd and lock manager
               $ vgchange --lockstart [--persist start] VG

## [](#SETUP_DETAILS)SETUP DETAILS

           Identifying devices
           Devices often have different local names on each host, e.g.
           /dev/sda on one host is named /dev/sdb on another. One method to
           identify the same device on each host is to run the command lsblk
           -o+WWN on each host, looking for the same WWN, and its
           corresponding local device name.  Or, the WWN-based device
           symlinks under /dev/disk/by-id/ can be a useful way to
           consistently identify a device across multiple hosts.

           Device access
           On each host, LVM needs to be given access to the shared devices
           by adding them to the local system.devices file (unless the
           devices file feature has been disabled.) Use the local device name
           identified in the previous step, or a WWN-based device symlink,
           and run the command lvmdevices --adddev device_path to add each of
           the shared devices to the local system.devices file.
           Alternatively, after the shared VG has been created from one host,
           other hosts can run the command vgimportdevices VG to add devices
           from VG to system.devices.  See lvmdevices(8) for more
           information.

           Config files
           After /etc/lvm/lvm.conf use_lvmlockd has been set to 1, lvm
           commands will begin attempting to acquire locks from lvmlockd.
           Failures to acquire the global lock from lvmlockd may appear until
           the first shared VG is operational. These warnings won't interfere
           with lvm commands doing read operations, but lvm commands
           attempting to write may fail with a global lock error.

           The /etc/lvm/lvmlocal.conf host_id setting is only required when
           using VGs with lock type sanlock. Each host using sanlock VGs must
           be configured with a unique host_id value. Valid host_ids are
           integers in the range 1-2000. (The lvmlocal.conf descriptions of
           host_id and sanlock_align_size mention special cases with 4K disks
           in which the valid host_id range can be smaller, e.g. 1-250.)

           Lock managers
           A specific build of LVM may exclude support for sanlock or dlm
           lock managers. To check this, run the command "lvm version" and
           look for "--enable-lvmlockd-sanlock" or "--enable-lvmlockd-dlm".

           With the --shared option, vgcreate searches for a running lock
           manager (dlm or sanlock), and uses the result for the VG lock
           type.  In place of --shared, vgcreate --locktype sanlock|dlm can
           be specified directly.

           When using lvmlockd in a cluster which already uses corosync and
           dlm, then the dlm lock type should be used for shared VGs.
           Otherwise, using sanlock is usually more straight forward.

           Details on starting or setting up each lock manager are outside
           the scope of LVM. sanlock can usually be started with a simple
           "systemctl start wdmd sanlock". Steps for setting up and starting
           corosync and dlm can be more complicated.

           Lock start
           Shared VGs must be started before they are used via vgchange
           --lockstart VG. Starting the VG performs lock manager
           initialization that is necessary to begin using locks (i.e.
           creating and joining a lockspace). Starting the VG may take some
           time, and until the start completes the VG may not be modified or
           activated. When shutting down, the lockspace is stopped with
           vgchange --lockstop VG.

           Persistent Reservations
           A shared VG with locktype sanlock can take advantage of Persistent
           Reservations (PR) for faster and more reliable recovery. This
           requires all of the devices in the VG to support PR.  Test if PR
           is supported by a device with the command:
           $ lvmpersist devtest --device device

           The vgcreate command options when enabling PR-based recovery with
           sanlock:
           $ vgcreate --shared --setpersist y --setlockargs persist,notimeout

           When enabled, PR needs to be started for the VG before lockstart:
           $ vgchange --persist start VG

           Or start PR and locking with one command:
           $ vgchange --persist start --lockstart VG

           Atomic leases
           sanlock can use atomic leases when devices support the SCSI
           COMPARE AND WRITE (CAW) command (sometimes referred to as atomic
           test and set.)  Atomic/CAW leases are faster and more efficient
           than the lease algorithms used without CAW (disk-paxos for
           resource leases, and time-delay leases for lockspace leases.)

           sanlock leases are configured to use CAW when they are initialized
           during vgcreate.  CAW usage depends on the sanlock configuration,
           device COMPARE AND WRITE support, and vgcreate --setlockargs
           options:

           --setlockargs caw
           Use CAW if supported by the device and allowed by the sanlock
           configuration.

           --setlockargs nocaw
           Do not use CAW, even if supported by the device and the sanlock
           configuration.

           If neither option is specified, CAW usage will depend on the
           sanlock configuration and device support.

## [](#TOPICS)TOPICS

       Displaying shared VGs
           The vgs command shows the letter s in the last (sixth) attr
           position for a shared VG:

           $ vgs
             VG    #PV #LV #SN Attr   VSize   VFree
             vgfoo   1   0   0 wz--ns 992.00m 736.00m

           Or, the shared attribute can be displayed as a vgs reporting
           field:

           $ vgs -o+shared
             VG    #PV #LV #SN Attr   VSize   VFree   Shared
             vgfoo   1   0   0 wz--ns 992.00m 736.00m  shared

           The vgs command can also display the lock type:

           $ vgs -o+locktype
             VG    #PV #LV #SN Attr   VSize   VFree   LockType
             vgfoo   1   0   0 wz--ns 992.00m 736.00m sanlock

           On hosts that are attached to the shared devices, but do not have
           lvmlockd enabled, the vgs command will not display shared VGs
           unless the --shared option is added:

           $ vgs --shared
             VG    #PV #LV #SN Attr   VSize   VFree
             vgfoo   1   0   0 wz--ns 992.00m 736.00m

       Persistent Reservations
           PR-based lock recovery for a shared VG is possible when using
           sanlock.  In the standard form of this feature, lvmlockd removes
           the PR key of a failed host, and then permits sanlock to grant
           locks that had been held by the failed host.  LVM commands on
           other hosts can then acquire those locks, e.g. activate LVs that
           the failed host had active at the time it failed.  Removal of PR
           keys for failed hosts can be considered a form of "fencing".  For
           more information on using PR with LVM in general, see
           lvmpersist(8).

           Enabling
           The vgcreate options to enable PR-based lock recovery in a new VG
           (also shown above) are:
           $ vgcreate --shared --setpersist y --setlockargs persist,notimeout
           ...

           Use vgchange to enable PR-based lock recovery in an existing VG.
           First enable PR for the VG (if not already done), then change the
           VG lock args.  Note that changing lock args can involve
           stopping/starting both PR and the lockspace at different stages.
           Changing the PR or lock args settings requires the VG to be
           stopped on all other nodes.

           Example enabling using vgchange:
           $ vgcreate --shared VG devices
           $ vgchange --setpersist y VG
           $ vgchange --persist start VG
           $ vgchange --setlockargs persist,notimeout VG
           $ vgchange --persist start --lockstart VG

           Display the VG attributes configured by setpersist and
           setlockargs:
           $ vgs -o+persist VG
           $ vgs -o+lockargs VG

           Starting
           When PR is enabled for a shared VG (the --setpersist y option),
           LVM requires a specific startup sequence before the VG can be
           used: PR must be started first (this step registers the local PR
           key and acquires a reservation on the VG devices), and the lock
           manager must be started second (this enables distributed locks to
           be acquired for the VG.)  These startup steps must complete
           successfully before VG modifications or LV activations are
           allowed.  PR and locking can be started in separate commands, or
           with a single command:

           $ vgchange --persist start VG; vgchange --lockstart VG
           $ vgchange --persist start --lockstart VG

           Variations
           The sanlock lock manager can be configured to handle recovery of
           failed hosts in different ways.  The first variation
           (persist,notimeout) is considered the standard form of PR-based
           lock recovery.  The second variation (nopersist,timeout) is the
           default behavior of lvmlockd/sanlock when no setlockargs value is
           specified (the default settings "nopersist" and "timeout" do not
           appear in the lockargs reporting field.)

           • --setlockargs persist,notimeout
             persist: lvmlockd will remove the PR key of a failed host when a
             lock request fails due to a lock owned by a failed host.  After
             PR key removal, sanlock is permitted to grant the lock.
             notimeout: a failed host's locks will not expire and be granted
             to another host after a timeout (i.e. after the time when the
             failed host's watchdog has fired.)
             Removal of the PR key is the only mechanism by which a failed
             host's locks are recovered.

           • --setlockargs nopersist,timeout
             nopersist: lvmlockd will not remove a PR key of a failed host
             when a lock request fails due to a lock owned by a failed host.
             (PR does not need to be enabled for the VG.)
             timeout: a failed host's locks will expire and be granted to
             another host after a timeout indicates the failed host's
             watchdog has fired.
             Watchdog expiration of a failed host is the only mechanism by
             which a failed host's locks are recovered.

           • --setlockargs persist,timeout
             persist: lvmlockd will remove the PR key of a failed host when a
             lock request fails due to a lock owned by a failed host.  After
             PR key removal, sanlock is permitted to grant the lock.
             timeout: a failed host's locks will expire and be granted to
             another host after a timeout indicates the failed host's
             watchdog has fired.
             Removal of the PR key, or watchdog expiration will both allow a
             failed host's locks to be recovered.

           • --setlockargs nopersist,notimeout
             nopersist: lvmlockd will not remove a PR key of a failed host
             when a lock request fails due to a lock owned by a failed host.
             (PR does not need to be enabled for the VG.)
             notimeout: a failed host's locks will not expire and be granted
             to another host after a timeout (i.e. after the time when the
             failed host's watchdog has fired.)
             There is no automated recovery of locks with this configuration.
             A user is responsible for manually resetting/fencing a failed
             host, and then manually notifying sanlock that the host is dead,
             which will allow the failed host's locks to be granted.

           nowatchdog
           With notimeout, lock recovery does not depend on the watchdog
           device, so nowatchdog can be included with notimeout in the lock
           args.  With nowatchdog, hosts will not connect to the watchdog
           device (or wdmd) when starting the VG lockspace, so a host will
           not be reset by a watchdog if it loses access to VG storage.

           • --setlockargs persist,notimeout,nowatchdog

           The nowatchdog behavior can also be requested per-host without
           writing it in the lock args (in VG metadata):
           $ vgchange --lockstart --lockopt nowatchdog VG

           Retrying
           If PR fencing fails (e.g. due to a missing device in the VG),
           lvmlockd caches the failure for the target host.  Subsequent lock
           requests for the same failed host_id+generation will reuse the
           cached failure without re-attempting PR fencing.  After resolving
           the cause of the failure (e.g.  restoring the missing device), use
           --lockopt force in the activation command re-attempt the PR
           fencing. e.g.
           $ lvchange -ay --lockopt force VG/LV

       System ID
           In contrast to a shared VG, a local VG can only be used by one
           host at a time, and does not use lvmlockd or a lock manager.  If a
           local VG is located on shared devices, then the LVM system ID
           feature should be used to assign one host ownership of the VG. See
           lvmsystemid(7).

           For additional protection, the shared devices in a local VG can be
           excluded from the devices file (system.devices) on all hosts
           except for the host that owns the VG.

       Creating the first sanlock VG
           When use_lvmlockd is first enabled in lvm.conf, and before the
           first sanlock VG is created, no global lock will exist.  In this
           initial state, LVM commands try and fail to acquire the global
           lock, producing a warning, and some commands are disallowed.  Once
           the first sanlock VG is created, the global lock will be
           available, and LVM will be fully operational.

           When a new sanlock VG is created, its lockspace is automatically
           started on the host that creates it.  Other hosts need to run
           'vgchange --lockstart' to start the new VG before they can use it.

           Creating the first sanlock VG is not protected by locking, so it
           requires special attention.  This is because sanlock locks exist
           on storage within the VG, so they are not available until after
           the VG is created.  The first sanlock VG that is created will
           automatically contain the "global lock".  Be aware of the
           following special considerations:

           • The first vgcreate command needs to be given the path to a
             device that has not yet been initialized with pvcreate.  The
             pvcreate initialization will be done by vgcreate.  This is
             because the pvcreate command requires the global lock, which
             will not be available until after the first sanlock VG is
             created.

           • Because the first sanlock VG will contain the global lock, this
             VG needs to be accessible to all hosts that will use sanlock
             shared VGs.  All hosts will need to use the global lock from the
             first sanlock VG.

           • The device and VG name used by the initial vgcreate will not be
             protected from concurrent use by another vgcreate on another
             host.

           See below for more information about managing the sanlock global
           lock.

       Removing a shared VG
           Removing a shared VG will fail if other hosts have the VG started
           (it must be started on the host running vgremove.)  Run vgchange
           --lockstop <vgname> on all other hosts before vgremove.  (It may
           take several seconds before vgremove recognizes that all hosts
           have stopped a sanlock VG.)

       Starting and stopping VGs
           Starting a shared VG (vgchange --lockstart) causes the lock
           manager to start (join) the lockspace for the VG on the host where
           it is run.  This makes locks for the VG available to LVM commands
           on the host.  Before a VG is started, only LVM commands that
           read/display the VG are allowed to continue without locks (and
           with a warning).

           Stopping a shared VG (vgchange --lockstop) causes the lock manager
           to stop (leave) the lockspace for the VG on the host where it is
           run.  This makes locks for the VG inaccessible to the host.  A VG
           cannot be stopped while it has active LVs.

           When using the lock type sanlock, starting a VG can take a long
           time (potentially minutes if the host was previously shut down
           without cleanly stopping the VG.)

           To make vgchange not wait for start to complete:
           vgchange --lockstart --lockopt nowait ...

           lvmlockd can be asked directly to stop all lockspaces:
           lvmlockctl -S|--stop-lockspaces

       Internal command locking
           To optimize the use of LVM with lvmlockd, be aware of the three
           kinds of locks and when they are used:

           Global lock
                  The global lock is associated with global information,
                  which is information not isolated to a single VG.  This
                  includes:

                  • The global VG namespace.

                  • The set of orphan PVs and unused devices.

                  • The properties of orphan PVs, e.g. PV size.

                  The global lock is acquired in shared mode by commands that
                  read this information, or in exclusive mode by commands
                  that change it.  For example, the command 'vgs' acquires
                  the global lock in shared mode because it reports the list
                  of all VG names, and the vgcreate command acquires the
                  global lock in exclusive mode because it creates a new VG
                  name, and it takes a PV from the list of unused PVs.

                  When an LVM command is given a tag argument, or uses
                  select, it must read all VGs to match the tag or selection,
                  which causes the global lock to be acquired.

           VG lock
                  A VG lock is associated with each shared VG.  The VG lock
                  is acquired in shared mode to read the VG and in exclusive
                  mode to change the VG or activate LVs.  This lock
                  serializes access to a VG with all other LVM commands
                  accessing the VG from all hosts.

                  The command 'vgs <vgname>' does not acquire the global lock
                  (it does not need the list of all VG names), but will
                  acquire the VG lock on each VG name argument.

           LV lock
                  An LV lock is acquired before the LV is activated, and is
                  released after the LV is deactivated.  If the LV lock
                  cannot be acquired, the LV is not activated.  (LV locks are
                  persistent and remain in place when the activation command
                  is done.  Global and VG locks are transient, and are held
                  only while an LVM command is running.)

           lock retries
                  If a request for a global or VG lock fails due to a lock
                  conflict with another host, the LVM command will retry the
                  lock request a number of times specified by
                  global/lvmlockd_lock_retries before failing.  If a request
                  for an LV lock fails due to a lock conflict, the command
                  fails immediately.

           The retries value specifies the number of retries per lock owner.
           If the lock owner (host_id) changes between retries, the per-owner
           retry count resets to zero, allowing the command to wait while the
           lock cycles through multiple hosts in a busy cluster.  A ceiling
           of retries*10 total attempts prevents indefinite delays.  With the
           default retries=6, the lock can cycle through up to 10 different
           owners (60 seconds) before failing.

           The --lockopt option can include a "retries=N" value to override
           the number of lock retries for a single command.  This applies to
           global, VG, and LV lock requests, replacing the
           global/lvmlockd_lock_retries config value for global and VG locks,
           and adding retry capability for LV locks which otherwise have
           none.  Each retry waits one second before repeating the lock
           request.

           When a host in a shared VG fails, its locks are not immediately
           available to other hosts.  The sanlock host_dead_seconds interval
           (usually 80 seconds) must pass before another host can acquire
           those locks.  Using "--lockopt retries=N" with a sufficiently
           large value allows an activation command to wait for this
           interval.
             lvchange -ay --lockopt retries=80 vg/lv

           Shared lock contention during autoactivation can also cause
           transient failures when multiple nodes start simultaneously and
           attempt to acquire shared locks on the same LV.  Using retries
           allows the command to wait and reattempt:
             lvchange -asy --lockopt retries=10 vg/lv

       Managing the global lock in sanlock VGs
           The global lock exists in one of the sanlock VGs.  The first
           sanlock VG created will contain the global lock.  Subsequent
           sanlock VGs will each contain a disabled global lock that can be
           enabled later if necessary.

           The VG containing the global lock must be visible to all hosts
           using sanlock VGs.  For this reason, it can be useful to create a
           small sanlock VG, visible to all hosts, and dedicated to just
           holding the global lock.  While not required, this strategy can
           help to avoid difficulty in the future if VGs are moved or
           removed.

           The vgcreate command typically acquires the global lock, but in
           the case of the first sanlock VG, there will be no global lock to
           acquire until the first vgcreate is complete.  So, creating the
           first sanlock VG is a special case that skips the global lock.

           vgcreate determines that it's creating the first sanlock VG when
           no other sanlock VGs are visible on the system.  It is possible
           that other sanlock VGs do exist, but are not visible when vgcreate
           checks for them.  In this case, vgcreate will create a new sanlock
           VG with the global lock enabled.  When another VG containing a
           global lock appears, lvmlockd will then see more than one VG with
           a global lock enabled.  LVM commands will report that there are
           duplicate global locks.

           If the situation arises where more than one sanlock VG contains a
           global lock, the global lock should be manually disabled in all
           but one of them with the command:

           lvmlockctl --gl-disable <vgname>

           (The one VG with the global lock enabled must be visible to all
           hosts.)

           An opposite problem can occur if the VG holding the global lock is
           removed.  In this case, no global lock will exist following the
           vgremove, and subsequent LVM commands will fail to acquire it.  In
           this case, the global lock needs to be manually enabled in one of
           the remaining sanlock VGs with the command:

           lvmlockctl --gl-enable <vgname>

           (Using a small sanlock VG dedicated to holding the global lock can
           avoid the case where the global lock must be manually enabled
           after a vgremove.)

       Internal lvmlock LV
           A sanlock VG contains a hidden LV called "lvmlock" that holds the
           sanlock locks.  vgreduce cannot yet remove the PV holding the
           lvmlock LV.  To remove this PV, change the VG lock type to "none",
           run vgreduce, then change the VG lock type back to "sanlock".
           Similarly, pvmove cannot be used on a PV used by the lvmlock LV.

           To place the lvmlock LV on a specific device, create the VG with
           only that device, then use vgextend to add other devices.

       LV activation
           In a shared VG, LV activation involves locking through lvmlockd,
           and the following values are possible with lvchange/vgchange -a:

           y|ey   The command activates the LV in exclusive mode, allowing a
                  single host to activate the LV.  Before activating the LV,
                  the command uses lvmlockd to acquire an exclusive lock on
                  the LV.  If the lock cannot be acquired, the LV is not
                  activated and an error is reported.  This would happen if
                  the LV is active on another host.

           sy     The command activates the LV in shared mode, allowing
                  multiple hosts to activate the LV concurrently.  Before
                  activating the LV, the command uses lvmlockd to acquire a
                  shared lock on the LV.  If the lock cannot be acquired, the
                  LV is not activated and an error is reported.  This would
                  happen if the LV is active exclusively on another host.  If
                  the LV type prohibits shared access, such as a snapshot,
                  the command will report an error and fail.  The shared mode
                  is intended for a multi-host/cluster application or file
                  system.  LV types that cannot be used concurrently from
                  multiple hosts include thin, cache, raid, mirror, and
                  snapshot.

           n      The command deactivates the LV.  After deactivating the LV,
                  the command uses lvmlockd to release the current lock on
                  the LV.

       Manually repairing a shared VG
           Some failure conditions may not be repairable while the VG has a
           shared lock type.  In these cases, it may be possible to repair
           the VG by forcibly changing the lock type to "none".  This is done
           by adding "--lockopt force" to the normal command for changing the
           lock type: vgchange --locktype none VG.  The VG lockspace should
           first be stopped on all hosts, and be certain that no hosts are
           using the VG before this is done.

       Recover from lost PV holding sanlock locks
           In a sanlock VG, the sanlock locks are held on the hidden
           "lvmlock" LV.  If the PV holding this LV is lost, a new lvmlock LV
           needs to be created.  To do this, ensure no hosts are using the
           VG, then forcibly change the lock type to "none" (see above).
           Then change the lock type back to "sanlock" with the normal
           command for changing the lock type:

           # vgchange --locktype sanlock VG

           This recreates the internal lvmlock LV with the necessary locks.

       Locking system failures
           lvmlockd failure

           If lvmlockd fails or is killed while holding locks, the locks are
           orphaned in the lock manager.  Orphaned locks must be cleared or
           adopted before the associated resources can be accessed normally.
           If lock adoption is enabled, lvmlockd keeps a record of locks in
           the adopt-file.  A subsequent instance of lvmlockd will then adopt
           locks orphaned by the previous instance.  Adoption must be enabled
           in both instances (-A|--adopt 1).  Without adoption, the lock
           manager or host would require a reset to clear orphaned lock
           state.

           dlm/corosync failure

           If dlm or corosync fail, the clustering system will fence the host
           using a method configured within the dlm/corosync clustering
           environment.

           LVM commands on other hosts will be blocked from acquiring any
           locks until the dlm/corosync recovery process is complete.

           sanlock lease storage failure

           If the PV under a sanlock VG's lvmlock LV is disconnected,
           unresponsive or too slow, sanlock cannot renew the lease for the
           VG's locks.  After some time, the lease will expire, and locks
           that the host owns in the VG can be acquired by other hosts.  The
           VG must be forcibly deactivated on the host with the expiring
           lease before other hosts can acquire its locks.  This is necessary
           for data protection.

           When the sanlock daemon detects that VG storage is lost and the VG
           lease is expiring, it runs the command lvmlockctl --kill <vgname>.
           This command emits a syslog message stating that storage is lost
           for the VG, and that LVs in the VG must be immediately
           deactivated.

           If no LVs are active in the VG, then the VG lockspace will be
           removed, and errors will be reported when trying to use the VG.
           Use the lvmlockctl --drop command to clear the stale lockspace
           from lvmlockd.

           If the VG has active LVs, they must be quickly deactivated before
           the locks expire.  After all LVs are deactivated, run lvmlockctl
           --drop <vgname> to clear the expiring lockspace from lvmlockd.

           If all LVs in the VG are not deactivated within about 40 seconds,
           sanlock uses wdmd and the local watchdog to reset the host.  The
           machine reset is effectively a severe form of "deactivating" LVs
           before they can be activated on other hosts.  The reset is
           considered a better alternative than having LVs used by multiple
           hosts at once, which could easily damage or destroy their content.

           sanlock lease storage failure automation

           When the sanlock daemon detects that the lease storage is lost, it
           runs the command lvmlockctl --kill <vgname>.  This lvmlockctl
           command can be configured to run another command to forcibly
           deactivate LVs, taking the place of the manual process described
           above.  The other command is configured in the lvm.conf(5)
           lvmlockctl_kill_command setting.  The VG name is appended to the
           end of the command specified.

           The lvmlockctl_kill_command should forcibly deactivate LVs in the
           VG, ensuring that existing writes to LVs in the VG are complete
           and that further writes to the LVs in the VG will be rejected.  If
           it is able to do this successfully, it should exit with success,
           otherwise it should exit with an error.  If lvmlockctl --kill gets
           a successful result from lvmlockctl_kill_command, it tells
           lvmlockd to drop locks for the VG (the equivalent of running
           lvmlockctl --drop).  If this completes in time, a machine reset
           can be avoided.

           One possible option is to create a script my_vg_kill_script.sh:

           #!/bin/bash
           VG=$1

           # replace dm table with the error target for top level LVs
           dmsetup wipe_table -S "uuid=~LVM && vgname=$VG && lv_layer=\"\""

           # check that the error target is in place
           dmsetup table -c -S "uuid=~LVM && vgname=$VG && lv_layer=\"\"" |grep -vw error
           if [[ $? -ne 0 ]] ; then
           exit 0
           fi
           exit 1

           Set in lvm.conf(5):

           lvmlockctl_kill_command="/usr/sbin/my_vg_kill_script.sh"

           (The script and dmsetup commands should be tested with the actual
           VG to ensure that all top level LVs are properly disabled.)

           If the lvmlockctl_kill_command is not configured, or fails,
           lvmlockctl --kill will emit syslog messages as described in the
           previous section, notifying the user to manually deactivate the VG
           before sanlock resets the machine.

           sanlock daemon failure

           If the sanlock daemon fails or exits while a lockspace is started,
           the local watchdog will reset the host.  This is necessary to
           protect any application resources that depend on sanlock leases.

       Changing dlm cluster name
           When a dlm VG is created, the cluster name is saved in the VG
           metadata.  To use the VG, a host must be in the named dlm cluster.
           If the dlm cluster name changes, or the VG is moved to a new
           cluster, the dlm cluster name saved in the VG must also be
           changed.

           To see the dlm cluster name saved in the VG, use the command:

           # vgs -o+locktype,lockargs <vgname>

           To change the dlm cluster name in the VG when the VG is still used
           by the original cluster:

           • Start the VG on the host changing the lock type
             vgchange --lockstart <vgname>

           • Stop the VG on all other hosts:
             vgchange --lockstop <vgname>

           • Change the VG lock type to none on the host where the VG is
             started:
             vgchange --locktype none <vgname>

           • Change the dlm cluster name on the hosts or move the VG to the
             new cluster.  The new dlm cluster must now be running on the
             host.  Verify the new name by:
             cat /sys/kernel/config/dlm/cluster/cluster_name

           • Change the VG lock type back to dlm which sets the new cluster
             name:
             vgchange --locktype dlm <vgname>

           • Start the VG on hosts to use it:
             vgchange --lockstart <vgname>

           To change the dlm cluster name in the VG when the dlm cluster name
           has already been changed on the hosts, or the VG has already moved
           to a different cluster:

           • Ensure the VG is not being used by any hosts.

           • The new dlm cluster must be running on the host making the
             change.  The current dlm cluster name can be seen by:
             cat /sys/kernel/config/dlm/cluster/cluster_name

           • Change the VG lock type to none:
             vgchange --locktype none --lockopt force <vgname>

           • Change the VG lock type back to dlm which sets the new cluster
             name:
             vgchange --locktype dlm <vgname>

           • Start the VG on hosts to use it:
             vgchange --lockstart <vgname>

       Changing a local VG to a shared VG
           All LVs must be inactive to change the lock type.

           lvmlockd must be configured and running as described in USAGE.

           • Change a local VG to a shared VG with the command:
             vgchange --locktype sanlock|dlm <vgname>

           • Start the VG on hosts to use it:
             vgchange --lockstart <vgname>

           If lvmlockd or the cluster manager are not available, the lock
           type can be forcibly changed with:
           vgchange --locktype sanlock|dlm --lockopt force <vgname>

       Changing a shared VG to a local VG
           All LVs must be inactive to change the lock type.

           • Start the VG on the host making the change:
             vgchange --lockstart <vgname>

           • Stop the VG on all other hosts:
             vgchange --lockstop <vgname>

           • Change the VG lock type to none on the host where the VG is
             started:
             vgchange --locktype none <vgname>

           If the VG cannot be started with the previous lock type, then the
           lock type can be forcibly changed to none with:
           vgchange --locktype none --lockopt force <vgname>

           To change a VG from one lock type to another (i.e. between sanlock
           and dlm), first change it to a local VG, then to the new type.

       Changing a clvm/clustered VG to a shared VG
           All LVs must be inactive to change the lock type.

           First change the clvm/clustered VG to a local VG.  Within a
           running clvm cluster, change a clustered VG to a local VG with the
           command:

           vgchange -cn <vgname>

           If the clvm cluster is no longer running on any nodes, then extra
           options can be used to forcibly make the VG local.  Caution: this
           is only safe if all nodes have stopped using the VG:

           vgchange --locktype none --lockopt force <vgname>

           After the VG is local, follow the steps described in "changing a
           local VG to a shared VG".

       Extending an LV active on multiple hosts
           With lvmlockd and dlm, a special clustering procedure is used to
           refresh a shared LV on remote cluster nodes after it has been
           extended on one node.

           When an LV holding gfs2 or ocfs2 is active on multiple hosts with
           a shared lock, lvextend is permitted to run with an existing
           shared LV lock in place of the normal exclusive LV lock.

           After lvextend has finished extending the LV, it sends a remote
           request to other nodes running the dlm to run 'lvchange --refresh'
           on the LV.  This uses dlm_controld and corosync features.

           Some special --lockopt values can be used to modify this process.
           "shupdate" permits the lvextend update with an existing shared
           lock if it isn't otherwise permitted.  "norefresh" prevents the
           remote refresh operation.

       Limitations of shared VGs
           Commands that cannot be run on shared VGs:

           • splitting snapshots from LVs

           • splitting mirrors in sanlock VGs

           • pvmove of entire PVs, or under LVs activated with shared locks

           • vgsplit and vgmerge (convert to a local VG to do this)

       lvmlockd changes from clvmd
           Prior to the introduction of lvmlockd, clvmd (CLVM) existed with
           similar capabilities, but a very different design.  Some of the
           visible usage differences between shared VGs (using lvmlockd) and
           cluster VGs (using clvmd):

           • lvm.conf(5) is configured to use lvmlockd by setting
             use_lvmlockd=1.
             clvmd used locking_type=3.

           • vgcreate --shared creates a shared VG.  vgcreate --clustered y
             created a clvm/clustered VG.

           • lvmlockd adds the option of using sanlock for locking, avoiding
             the need for network clustering.

           • lvmlockd defaults to the exclusive activation mode whenever the
             activation mode is unspecified, i.e. -ay means -aey, not -asy.

           • lvmlockd commands always apply to the local host, and never have
             an effect on a remote host.  (The activation option 'l' is not
             used.)

           • lvmlockd saves the cluster name for a shared VG using dlm.  Only
             hosts in the matching cluster can use the VG.

           • lvmlockd requires starting/stopping shared VGs with vgchange
             --lockstart and --lockstop.

           • vgremove of a sanlock VG may fail indicating that all hosts have
             not stopped the VG lockspace.  Stop the VG on all hosts using
             vgchange --lockstop.

           • vgreduce or pvmove of a PV in a sanlock VG will fail if it holds
             the internal "lvmlock" LV that holds the sanlock locks.

           • lvmlockd uses lock retries instead of lock queueing.  The per-
             owner retry count resets when the lock owner changes, so
             clusters with many nodes generally do not require increasing
             global/lvmlockd_lock_retries.  Using "--lockopt retries=N" can
             override the retry count for a single command if needed.

           • lvmlockd includes VG reporting options lock_type and lock_args,
             and LV reporting option lock_args to view the corresponding
             metadata fields.

           • In the vgs(8) command's sixth VG attr field, "s" for "shared" is
             displayed for shared VGs.

           • If lvmlockd fails or is killed while in use, locks it held
             remain but are orphaned in the lock manager.  lvmlockd can be
             restarted with an option to adopt the orphan locks from the
             previous instance of lvmlockd.

           • The lvs(8) command does not report any remote state, because
             lvmlockd is unable to passively check the remote active or lock
             state of an LV.

## [](#SEE_ALSO)SEE ALSO

           lvmlockctl(8), sanlock(8), dlm_controld(8)

## [](#COLOPHON)COLOPHON

           This page is part of the lvm2 (Logical Volume Manager 2) project.
           Information about the project can be found at 
           ⟨http://www.sourceware.org/lvm2/⟩.  If you have a bug report for
           this manual page, see ⟨https://github.com/lvmteam/lvm2/issues⟩.
           This page was obtained from the project's upstream Git repository
           ⟨git://sourceware.org/git/lvm2.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15)       LVMLOCKD(8)

------------------------------------------------------------------------

Pages that refer to this page: [lvmsystemid(7)](../man7/lvmsystemid.7.html),  [cmirrord(8)](../man8/cmirrord.8.html),  [lvchange(8)](../man8/lvchange.8.html),  [lvconvert(8)](../man8/lvconvert.8.html),  [lvcreate(8)](../man8/lvcreate.8.html),  [lvdisplay(8)](../man8/lvdisplay.8.html),  [lvextend(8)](../man8/lvextend.8.html),  [lvm(8)](../man8/lvm.8.html),  [lvmconfig(8)](../man8/lvmconfig.8.html),  [lvmdevices(8)](../man8/lvmdevices.8.html),  [lvmdiskscan(8)](../man8/lvmdiskscan.8.html),  [lvm-fullreport(8)](../man8/lvm-fullreport.8.html),  [lvmlockctl(8)](../man8/lvmlockctl.8.html),  [lvm-lvpoll(8)](../man8/lvm-lvpoll.8.html),  [lvreduce(8)](../man8/lvreduce.8.html),  [lvremove(8)](../man8/lvremove.8.html),  [lvrename(8)](../man8/lvrename.8.html),  [lvresize(8)](../man8/lvresize.8.html),  [lvs(8)](../man8/lvs.8.html),  [lvscan(8)](../man8/lvscan.8.html),  [pvchange(8)](../man8/pvchange.8.html),  [pvck(8)](../man8/pvck.8.html),  [pvcreate(8)](../man8/pvcreate.8.html),  [pvdisplay(8)](../man8/pvdisplay.8.html),  [pvmove(8)](../man8/pvmove.8.html),  [pvremove(8)](../man8/pvremove.8.html),  [pvresize(8)](../man8/pvresize.8.html),  [pvs(8)](../man8/pvs.8.html),  [pvscan(8)](../man8/pvscan.8.html),  [vgcfgbackup(8)](../man8/vgcfgbackup.8.html),  [vgcfgrestore(8)](../man8/vgcfgrestore.8.html),  [vgchange(8)](../man8/vgchange.8.html),  [vgck(8)](../man8/vgck.8.html),  [vgconvert(8)](../man8/vgconvert.8.html),  [vgcreate(8)](../man8/vgcreate.8.html),  [vgdisplay(8)](../man8/vgdisplay.8.html),  [vgexport(8)](../man8/vgexport.8.html),  [vgextend(8)](../man8/vgextend.8.html),  [vgimport(8)](../man8/vgimport.8.html),  [vgimportclone(8)](../man8/vgimportclone.8.html),  [vgimportdevices(8)](../man8/vgimportdevices.8.html),  [vgmerge(8)](../man8/vgmerge.8.html),  [vgmknodes(8)](../man8/vgmknodes.8.html),  [vgreduce(8)](../man8/vgreduce.8.html),  [vgremove(8)](../man8/vgremove.8.html),  [vgrename(8)](../man8/vgrename.8.html),  [vgs(8)](../man8/vgs.8.html),  [vgscan(8)](../man8/vgscan.8.html),  [vgsplit(8)](../man8/vgsplit.8.html)

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
