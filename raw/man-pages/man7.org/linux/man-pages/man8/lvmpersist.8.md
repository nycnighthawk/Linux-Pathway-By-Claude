---
{"title": "lvmpersist(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lvmpersist.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvmpersist(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [USAGE](#USAGE) \| [EXAMPLES](#EXAMPLES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVMPERSIST(8)            System Manager's Manual            LVMPERSIST(8)

## [](#NAME)NAME

           lvmpersist — Manage persistent reservations on a group of block
           devices

## [](#DESCRIPTION)DESCRIPTION

           Persistent reservations (PRs) provide a mechanism to control
           access to shared storage devices, typically to protect the devices
           from being modified by hosts that should not be writing to the
           shared devices.  This is usually a concern in SAN or clustered
           environments, where multiple hosts have access to the same storage
           devices.

           If an LVM Volume Group (VG) contains PR-capable devices, then LVM
           commands can be used to manage PR at the VG level, applying PR to
           each Physical Volume (PV) in the VG.  (All PVs in the VG must
           support PR.)

           lvmpersist is a low level utility used to perform PR operations on
           individual block devices.  LVM also provides a higher level PR
           management interface through a standard LVM command interface:
           vgchange --setpersist, vgchange --persist

           lvmpersist is a script that does not implement the common LVM
           command line options or capabilities.  The script uses sg_persist,
           mpathpersist, and nvme commands to perform PR operations on block
           devices.  Higher level LVM commands (e.g. vgchange) run the
           lvmpersist script.

       Device types
           SCSI or SCSI-like (e.g. iSCSI, SAS, Fibre Channel), dm-multipath,
           and NVME devices are supported.  PRs were introduced with the SCSI
           Primary Commands Version 3 standard (SPC-3).

           When multipath devices are used, multipath.conf must be configured
           with "reservation_key file".  (Run mpathconf --option
           reservation_key:file, and restart multipathd.)

       Persistent reservation types
           LVM uses PR type "Write Exclusive" (WE) for devices in a local VG,
           and "Write Exclusive - all registrants" (WEAR) for devices in a
           shared VG.  One exception is dm-multipath devices, for which WEAR
           is used in both local and shared VGs (this is needed for all paths
           to remain usable.)

           The lvmpersist command has two options for specifying the PR type:

           --access ex|sh
                  Set access to "ex" (exclusive) if the devices should be
                  accessed by only one host (i.e. the devices are part of a
                  local VG.)  Set access to "sh" (shared) if the devices are
                  meant to be accessed concurrently by multiple hosts (i.e.
                  the devices are part of a shared VG.)  lvmpersist will
                  choose the appropriate PR type for each device (usually WE
                  for "ex", and WEAR for "sh".)

           --prtype PRTYPE
                  When a PRTYPE value is specified, lvmpersist will use only
                  that type for all devices.

           PR types and the abbreviations used in interfaces/messages:

           WE Write Exclusive
           EA Exclusive Access
           WERO Write Exclusive - registrants only
           EARO Exclusive Access - registrants only
           WEAR Write Exclusive - all registrants
           EAAR Exclusive Access - all registrants

           (WERO and EARO types are not yet supported.)

       Persistent reservation keys
           PR keys can be up to 8 bytes long, and are represented with up to
           16 hex characters with a "0x" prefix.  Leading 0s are not
           permitted, e.g.  use 0x1234abcd, not 0x000000001234abcd.  A
           decimal key value (without a 0x prefix) is accepted as input, but
           will appear as hex in output.

           Each host using shared devices must use a unique PR key.

           PR keys must be configured on each host in /etc/lvm/lvmlocal.conf
           (see Local Settings below.)

## [](#USAGE)USAGE

           The basic command set and options for managing PR:

           Device-level PR utility (change device PR state):
           lvmpersist start|stop|remove|clear|read [OPTIONS] DEST

           VG PR configuration (change VG metadata):
           vgchange --setpersist y|n VG

           VG PR operations (change device PR state):
           vgchange --persist start|stop|remove|clear|read|check VG

       lvmpersist commands
           lvmpersist start --ourkey KEY DEST

           "start" registers the local key and reserves devices.  If a
           different key from the same host is still registered, it will be
           replaced with the specified key.  When --access or --prtype is not
           specified, access "ex" is used.

           lvmpersist stop --ourkey KEY DEST

           "stop" unregisters the local key, which also removes a local
           reservation.

           lvmpersist remove --ourkey KEY --removekey REMKEY DEST

           "remove" removes another registered host's key.  The host with the
           removed key loses the ability to write to the devices.  (This
           command applies to shared VGs, where multiple hosts are started at
           once.)

           lvmpersist start --ourkey KEY --removekey REMKEY DEST

           "start" with removekey registers the local key and takes the
           reservation from another host (using preempt-abort).  The other
           host loses the ability to write to the devices.  (This command
           applies to local VGs, for which a single host can be started at
           once.)

           lvmpersist clear --ourkey KEY DEST

           "clear" removes all keys and reservations from the devices.

           lvmpersist devtest|read|read-keys|read-reservation DEST

           These commands are used to test if devices support PR, and display
           current PR keys and reservations.

           lvmpersist check-key --key KEY DEST

           Check if a specified key is registered.

           OPTIONS:

           --ourkey KEY
                  The local PR key, e.g. 0x123abc

           --removekey REMKEY
                  Another host's PR key.

           --key KEY
                  Any key to check.

           --access ex|sh
                  Use a PR type for exclusive or shared device access.

           --prtype PRTYPE
                  Use the specified reservation type (alternative to
                  --access.)

           --ptpl
                  Enable persist through power loss during start (register.)

           DEST:

           --device PATH ...
                  One or more devices to operate on.

           --vg VGNAME
                  One VG to operate on (all PVs in the VG.)

           --vg VGNAME --device PATH ...
                  One or more devices to operate on, and a VG name to use as
                  an identifier for the set of devices.

           lvmpersist requires either the names of specific devices, each
           specified as --device /dev/name, or the name of a VG, specified
           with --vg VGNAME.  When a VG is specified, with no individual
           block devices, lvmpersist runs PR commands on each PV in the VG.
           When devices are specified, and a VG is also provided with --vg,
           then the VG name is simply used in log messages to identify the
           set of devices as a whole.  When lvmpersist is run by higher level
           LVM commands, each device is specified with --device, and the VG
           name is specified with --vg.

       VG metadata commands
           vgchange --setpersist is used to configure the automation and
           enforcement of PR in relation to the broader use of the VG.  The
           configuration is stored in the VG metadata.

           vgchange --setpersist y|n VG

           Enable or disable default automation and enforcement of PR for the
           VG, setting or clearing both "autostart" and "require" PR settings
           (and potentially other future settings.)

           vgchange --setpersist autostart|noautostart|require|norequire VG

           Individually set or clear the autostart and require settings.

           When "autostart" is set, autoactivation and auto-lockstart
           commands (vgchange -aay, vgchange --lockstart --lockopt auto) will
           first start PR on the VG.  If PR start fails, these commands stop
           and not attempt activation or lockstart.

           When "require" is set, lvm commands that write or activate a VG
           require PR to be started before attempting to write or activate.

           vgs -o persist VG

           Display the settings.

       VG PR commands
           vgchange --persist is used to perform PR operations on the VG's
           devices.

           vgchange --persist start VG

           Start PR on VG devices.  Registers the local key and acquires a
           reservation.

           vgchange --persist stop VG

           Stop PR on VG devices.  Unregisters the local key, which releases
           a reservation if one is held by the key.

           vgchange --persist remove --removekey remkey VG

           Remove the PR key of another host from a shared VG's devices,
           immediately disabling the ability of the other host to write to
           the devices.  (This command applies to shared VGs, for which
           multiple hosts are started at once.)

           vgchange --persist start --removekey remkey VG

           Start PR on VG devices, while at the same time removing another
           host's key and reservation from the VG devices, disabling the
           ability of the other host to write to the devices.  (This command
           applies to local VGs, for which a single host can be started at
           once.)

           vgchange --persist check VG

           Check if PR is started (the local key and reservation exists on
           all devices.)  The command exits with success if PR is started on
           all VG devices.

           vgchange --persist read VG

           Display the PR registrations and reservations on each of the VG's
           devices.

           vgchange --persist clear VG

           Clear all PR keys and reservations on the VG devices.

           vgchange --persist autostart VG

           Start PR on VG devices if the autostart is set.  This is meant to
           be used by system automation, like autoactivation and auto-
           lockstart.

       Supplementary PR start
           The --persist start option can be added to other commands so that
           these commands will first attempt to start PR (regardless of the
           autostart setting.)

           vgchange -ay --persist start
           vgchange -aay --persist start
           vgchange --lockstart --persist start
           vgchange --setpersist y|require|autostart --persist start
           vgimport --persist start
           vgchange --systemid <local_id> --persist start

       Local VG usage
           When using a local VG, only one host is started at a time, and a
           WE (Write Exclusive) reservation is typically held on the devices.

           Using PR with local VGs protects VG devices from being written to
           in error by another host with access to the same devices.  It is
           complementary to using the VG system ID to control the intended
           owner of a VG, but adds enforced device-level protection, in case
           another host is not using the LVM system ID feature.

           If one host would like to forcibly take over a local VG that is
           currently in use by another host, it can use vgchange --persist
           start --removekey remkey VG, where "remkey" is the PR key of the
           currently started host.

       Shared VG usage
           For a shared VG, the VG metadata is configured by one host using
           the vgchange --setpersist command, which writes the desired PR
           configuration to the VG metadata.  The vgchange --setpersist
           command requires VG locking to be started.  All hosts use the
           vgchange --persist commands to start/stop/check the state of their
           own PR on disk.  These are not VG metadata operations, but send PR
           commands to change PR state on disk (typically via lvmpersist.)

           When using a shared VG, all hosts using the VG will perform a
           start command, and a WEAR (Write Exclusive - all registrants)
           reservation will be held on the devices.

           PR should be started before locking is started (vgchange --persist
           start followed by vgchange --lockstart, or a combined vgchange
           --persist start --lockstart.)

           If one host would like to forcibly stop another host from writing
           to the shared VG devices, it can use vgchange --persist remove
           --removekey remkey where "remkey" is the PR key of the other host.

       Local Settings
           Each host using PR is required to have a PR key that is unique
           among all hosts using the same VG.  There are two approaches to
           setting a key value, which are set in /etc/lvm/lvmlocal.conf:

           local/pr_key

           The local persistent reservation key in hexadecimal.  The max
           length is 16 hex characters (8 bytes), plus an optional 0x prefix.
           The pr_key setting is used for local VGs.  Shared VGs use PR keys
           that are based on the host_id, and ignore this pr_key setting.

           local/host_id

           A unique host identifier, used for sanlock shared VGs, and for
           persistent reservation keys. Accepted values are 1-2000, except
           when sanlock_align_size is configured to 1, 2 or 4, which
           correspond to max host_id values of 250, 500, or 1000.  PR keys
           for sanlock VGs are a combination of the host_id and the sanlock
           generation number. Local VGs will use the host_id as a PR key only
           when local/pr_key is not set.

           For a local VG, or a dlm shared VG, a key using host_id has the
           form:

           0x100000000000XXXX where XXXX are the hex digits for the host_id
           value.

           For a sanlock shared VG, the key is based on host_id and a
           generation number (taken from the sanlock lease), and has the
           form:

           0x100000YYYYYYXXXX where XXXX are the hex digits for the host_id
           value, and YYYYYY are the hex digits for the generation number.

           The sanlock generation number increases in value each time the
           host starts the VG, so a host will use a new key each time it
           starts.  In some instances, PR may be started with a key that
           includes the incorrect generation number, in which case the
           lockstart command will update the key with the correct value (the
           generation number is officially determined during lockstart.)

       vgcreate
           PR features can be enabled when creating a new VG:

           vgcreate --setpersist y VG PVs

           For local VGs, --persist start can be included to also start PR on
           the new VG.

           Creating new shared VGs with --setpersist works differently.  PR
           is always started for a new shared VG, even without --persist
           start.  First, an exclusive PR (typically WE mode) is acquired for
           the new VG devices.  The devices are then initialized, and the new
           VG metadata is written.  The exclusive PR is then removed, and a
           shared PR (typically WEAR mode) is acquired for normal sharing of
           the VG.  Finally, the VG lockspace is started.

       vgextend
           For local VGs, vgextend starts PR on the new devices before adding
           them to the VG (the require or autostart setting must be enabled.)
           For shared VGs, the user must use lvmpersist to start PR on the
           new devices, from all hosts, before running vgextend.  vgextend
           verifies that the reservation and keys on the new devices match
           the existing devices.

       vgremove
           The vgremove command stops PR on the VG's devices only if
           "require" or "autostart" settings have been set using vgchange
           --setpersist.  If PR has been started independent of any
           setpersist settings, then vgremove will not automatically stop PR
           on the devices.

       vgexport/vgimport
           vgexport --persist stop stops PR after exporting the VG, and
           vgimport --persist start starts PR before importing the VG.
           Writing VG metadata for export happens before stopping PR, and
           writing VG metadata for import happens after starting PR.

       vgchange --systemid
           PR can be started together with taking ownership of a VG's system
           ID, or PR can be stopped together with giving up ownership of a
           VG's system ID (see lvmsystemid(7) for more information.)

           vgchange --systemid local_system_id --persist start VG

           This command is used to take ownership of a foreign-owned VG.  PR
           is started, and if successful, the system ID of the VG will be set
           to the local system ID.  (Note: the foreign system ID of the VG
           needs to be included in local extra_system_ids to gain access to a
           foreign VG.)  To forcibly remove (preempt-abort) PR held by
           another host on the VG, --removekey remkey can be included, where
           remkey is the PR key of the current PR holder.

           vgchange --systemid foreign_system_id --persist stop VG

           This command is used to give up ownership of a locally owned VG.
           The system ID of the VG is updated to the new value, and then PR
           is stopped.

       Persist Through Power Loss
           To enable the use of "persist through power loss", in which PR
           state is retained on a device if it is power cycled, turn on the
           ptpl setting:

           vgchange --setpersist ptpl VG

           The PTPL setting is applied during key registration (part of PR
           start), so it will take effect for each host on the next start.
           It is applied to all PVs in the VG, so each device must support
           PTPL.  The PTPL setting is not enabled by "--setpersist y".

           Either of the following will clear the PTPL setting:

           vgchange --setpersist noptpl VG
           vgchange --setpersist n VG

## [](#EXAMPLES)EXAMPLES

       Local VG usage
           host1:
           $ lvmconfig local/host_id
           host_id=1
           $ vgcreate vg /dev/sda /dev/sdb
             Physical volume "/dev/sda" successfully created.
             Physical volume "/dev/sdb" successfully created.
             Volume group "vg" successfully created
           $ vgchange --setpersist y vg
             Volume group "vg" successfully changed.
           $ vgchange --persist start vg
             lvmpersist: started vg with key 0x1000000000000001.
           $ vgchange --persist check vg
             key for local host is registered: 0x1000000000000001
             reservation WE for local host
             PR is started.
           $ lvcreate -l1 -n lvol0 vg
             Logical volume "lvol0" created.
           $ vgchange -an vg
             0 logical volume(s) in volume group "vg" now active
           $ vgchange --persist stop vg
             lvmpersist: stopped vg with key 0x1000000000000001.
           $ vgchange -ay vg
             persistent reservation is not started.
             Cannot access VG vg without persistent reservation.
           $ lvcreate -l1 -n lvol1 vg
             persistent reservation is not started.
             Cannot access VG vg without persistent reservation.
           $ vgchange --persist start vg
             lvmpersist: started vg with key 0x1000000000000001.
           $ vgchange -ay vg
             1 logical volume(s) in volume group "vg" now active
           $ lvcreate -l1 -n lvol1 vg
             Logical volume "lvol1" created.

           host2 foricibly takes VG from host1:
           $ lvmconfig local/host_id
           host_id=2
           $ vgchange -ay vg
             persistent reservation is not started.
             Cannot access VG vg without persistent reservation.
           $ vgchange --persist start vg
             persistent reservation is started by another host
           $ vgchange --persist check vg
             key for local host is not registered (host_id 2)
             key for other host is registered: 0x1000000000000001
             reservation WE for other host
             PR is not started.
           $ dd if=/dev/zero of=/dev/sda
           dd: error writing '/dev/sda': Input/output error
           $ vgchange --persist start --removekey 0x1000000000000001 vg
             lvmpersist: started vg with key 0x1000000000000002.
           $ vgchange -ay vg
             2 logical volume(s) in volume group "vg" now active
           $ vgchange --persist check vg
             key for local host is registered: 0x1000000000000002
             reservation WE for local host
             PR is started.

           host1 can no longer write:
           $ dd if=/dev/zero of=/dev/vg/lvol0
           dd: error writing '/dev/vg/lvol0': Input/output error
           $ lvcreate -l1 -n lvol1 vg
             persistent reservation is not started.
             Cannot access VG vg without persistent reservation.
           $ vgchange --persist check vg
             key for local host is not registered (host_id 1)
             key for other host is registered: 0x1000000000000002
             reservation WE for other host
             PR is not started.

       Shared VG usage
           host1:
           $ lvmconfig local/host_id
           host_id=1
           $ vgcreate --shared vg /dev/sda /dev/sdb
             Enabling sanlock global lock
             Physical volume "/dev/sda" successfully created.
             Physical volume "/dev/sdb" successfully created.
             Logical volume "lvmlock" created.
             Volume group "vg" successfully created
             VG vg starting sanlock lockspace
             Starting locking.  Waiting until locks are ready...
           $ vgchange --setpersist y vg
             Volume group "vg" successfully changed.
           $ vgchange --persist start vg
             lvmpersist: started vg with key 0x1000000000010001.
           $ vgchange --persist check vg
             key for local host is registered: 0x1000000000010001
             keys for all registered hosts: 0x1000000000010001
             reservation WEAR for registered hosts
             PR is started.
           $ lvcreate -l1 -n lvol0 vg
             Logical volume "lvol0" created.

           host2:
           $ lvmconfig local/host_id
           host_id=2
           $ vgchange --persist start vg
             lvmpersist: started vg with key 0x1000000000010002.
           $ vgchange --lockstart vg
             VG vg starting sanlock lockspace
             Starting locking.  Waiting for sanlock...
           $ vgchange --persist check vg
             key for local host is registered: 0x1000000000010002
             keys for all registered hosts: 0x1000000000010001 0x1000000000010002
             reservation WEAR for registered hosts
             PR is started.
           $ lvcreate -l1 -n lvol1 vg
             Logical volume "lvol1" created.
           $ lvchange -ay vg/lvol0
             LV locked by other host: vg/lvol0 (host_id 1)
             Failed to lock logical volume vg/lvol0.
           $ vgchange -an vg
             0 logical volume(s) in volume group "vg" now active
           $ vgchange --lockstop vg
           $ vgchange --persist stop vg
             lvmpersist: stopped ee with key 0x1000000000010002.
           $ vgchange --persist check vg
             key for local host is not registered (host_id 2)
             keys for all registered hosts: 0x1000000000010001
             reservation WEAR for registered hosts
             PR is not started.
           $ dd if=/dev/zero of=/dev/sda
           dd: error writing '/dev/sda': Input/output error

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

    Red Hat, Inc      LVM TOOLS 2.03.42(2)-git (2026-05-15)     LVMPERSIST(8)

------------------------------------------------------------------------

Pages that refer to this page: [lvmlockd(8)](../man8/lvmlockd.8.html)

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
