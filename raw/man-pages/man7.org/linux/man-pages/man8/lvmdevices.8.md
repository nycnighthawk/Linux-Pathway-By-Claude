---
{"title": "lvmdevices(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lvmdevices.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvmdevices(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [USAGE](#USAGE) \| [OPTIONS](#OPTIONS) \| [VARIABLES](#VARIABLES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVMDEVICES(8)            System Manager's Manual            LVMDEVICES(8)

## [](#NAME)NAME

           lvmdevices — Manage the devices file

## [](#SYNOPSIS)SYNOPSIS

           lvmdevices option_args
               [ option_args ]

               --adddev PV
               --addpvid String
               --check
               --commandprofile String
               --config String
            -d|--debug
               --deldev PV
               --delpvid String
               --deviceidtype String
               --devices PV
               --devicesfile String
               --driverloaded y|n
            -h|--help
               --journal String
               --lockopt String
               --longhelp
               --nohints
               --nolocking
               --profile String
            -q|--quiet
            -t|--test
               --update
            -v|--verbose
               --version
            -y|--yes

## [](#DESCRIPTION)DESCRIPTION

           The LVM devices file is the list of devices that lvm commands will
           use.   It  is  located  at  /etc/lvm/devices/system.devices.   The
           lvmdevices(8) command manages the file, and is used to add, remove
           and list devices.

       Listing devices
           Run the lvmdevices command with no options or arguments to display
           the entries in system.devices:
           lvmdevices

           Each line begins with a  current  device  name  from  the  system,
           followed by its device ID from the devices file, followed by other
           device  details  used by lvm.  A line begins with "Device none" if
           no device on the system  matches  the  device  ID.   (Viewing  the
           system.devices  file  directly  does  not  indicate if a device is
           present on the system.)

       Adding devices
           To use a device with lvm, add it to the devices file with  one  of
           the following commands.

           Add a device by referencing its device path:
           lvmdevices --adddev device

           Add a device by referencing its PVID:
           lvmdevices --addpvid PVID

           Add a device by referencing its device ID:
           lvmdevices --addid IDNAME --deviceidtype IDTYPE

           Add all of the PVs in a VG:
           vgimportdevices VG

           Add all of the PVs in all visible VGs:
           vgimportdevices -a

           pvcreate, vgcreate, and vgextend also look outside of the existing
           devices  file  to find the target device, and automatically add it
           to the devices file.

       Removing devices
           Removing a device from the devices  file  will  prevent  lvm  from
           seeing  or  using  that  device.   Remove a device with one of the
           following commands.

           Remove a device by referencing its device path:
           lvmdevices --deldev device

           Remove a device by referencing its PVID:
           lvmdevices --delpvid PVID

           Remove a device by referencing its device ID:
           lvmdevices --delid IDNAME --deviceidtype IDTYPE

       device IDs
           LVM identifies devices in the devices file using hardware-specific
           IDs, such as the WWID or serial  number.   Subsystem-specific  IDs
           are used for virtual device types, which also aim to be unique and
           stable.   When no hardware or subsystem ID is available, lvm falls
           back using the device name as the device ID.  Using  device  names
           as  IDs is not optimal because they are not stable, and will often
           change after reboot.  When device names are used as IDs, lvm  must
           perform extra device scanning to locate devices if the device name
           changes.

           When  stable  device  IDs  are  used,  lvm will not access devices
           outside of those listed in the devices file.   When  device  names
           are used as IDs, lvm will scan devices outside the devices file to
           locate  PVs  on  devices  that  changed names.  The config setting
           search_for_devnames can be  used  to  control  lvm's  behavior  in
           locating renamed devname entries.

           A device ID has two parts: an IDTYPE and an IDNAME.

           The  IDTYPE  specifies the origin of the ID, and the IDNAME is the
           actual identifier.  There is a predefined set of IDTYPEs listed in
           the next section.  A devices file entry must have one of these  ID
           types.    When   adding   a   device  to  the  devices  file,  lvm
           automatically chooses the best IDTYPE,  which  can  be  overridden
           with   the   --deviceidtype   option   (this   is   not  generally
           recommended.)

           To display all of the possible device IDs for  a  device,  or  the
           value of one specific type, use the commands:

           lvmdevices --listids device
           lvmdevices --listids device --deviceidtype IDTYPE

       device ID types
           The available device ID types are:

           • sys_wwid uses the wwid reported by the wwid sysfs file. This is
             the first choice.

           • wwid_naa uses the naa wwid decoded from the vpd_pg83 sysfs file.

           • wwid_eui uses the eui wwid decoded from the vpd_pg83 sysfs file.

           • wwid_t10 uses the t10 wwid decoded from the vpd_pg83 sysfs file.

           • sys_serial uses the serial number reported by the serial sysfs
             file or the vpd_pg80 file. A serial number is used if no wwid is
             available.

           • mpath_uuid is used for dm multipath devices, reported by sysfs.

           • crypt_uuid is used for dm crypt devices, reported by sysfs.

           • md_uuid is used for md devices, reported by sysfs.

           • lvmlv_uuid is used if a PV is placed on top of an lvm LV,
             reported by sysfs.

           • loop_file is used for loop devices, the backing file name
             reported by sysfs.

           • devname the device name is used if no other type applies.

           • nvme_uuid, nvme_nguid, nvme_eui64 are not generally used, but
             may appear for nvme devices that report invalid wwid values.

       sysfs files
           Most of the device ID types read the device ID value from sysfs.
           Those sysfs values can also be read directly from the following
           paths:

           /sys/dev/block/major:minor/device/wwid
           /sys/dev/block/major:minor/device/serial
           /sys/dev/block/major:minor/wwid
           /sys/dev/block/major:minor/device/vpd_pg83 (binary)
           /sys/dev/block/major:minor/device/vpd_pg80 (binary)
           /sys/dev/block/major:minor/dm/uuid (lvm reads via ioctl)
           /sys/dev/block/major:minor/md/uuid
           /sys/dev/block/major:minor/loop/backing_file

           (Some sysfs values are modified before being used as the device
           ID, e.g. spaces omitted or replaced with underscores.)

       devices file contents
           LVM writes some additional information to the devices file in
           addition to the device IDs.  LVM commands automatically update
           this information if it changes.  This includes the last known
           device name, and the PV UUID (PVID) from the LVM disk header.

           Check if the devices file content needs to be updated:
           lvmdevices --check

           Update devices file fields that are outdated:
           lvmdevices --update

           The devices file is meant to be edited by lvm commands, not by the
           user.  The devices file contains a HASH value which lvm uses to
           detect if the file has been modified since lvm last wrote it.
           When lvm updates the devices file, the previous version is moved
           to /etc/lvm/devices/backup/.

           The following fields can be found in the devices file:
           VERSION: incremented for each file update.
           PRODUCT_UUID: a unique machine ID used to detect if the
           system.devices file has been moved to a new machine, and may
           require updating.  When not available, HOSTNAME is used.

           Device entry fields:
           IDTYPE: indicates the source of the device ID value in IDNAME.
           IDNAME: the unique device ID value.
           DEVNAME: the most recent device name associated with the device
           ID.
           PVID: the LVM PV UUID from the LVM disk header.
           PART: the partition number if a PV exists on a partition.

       device ID refresh
           When lvm writes system.devices, it includes a local machine ID in
           the system.devices file (as PRODUCT_UUID or HOSTNAME.)  When lvm
           reads system.devices, it compares this saved machine ID to the
           current machine, which allows lvm to detect when system.devices
           has been copied or restored onto a different machine.  When a
           machine change is detected, lvm enables a "device ID refresh" mode
           (configured by lvm.conf device_ids_refresh and
           device_ids_refresh_checks.)

           In refresh mode, a device in system.devices that is not found by
           its device ID will be located using its PVID.  LVM will scan all
           devices on the system to search for the missing PVIDs in
           system.devices.  If a PVID is found on a new device, the
           system.devices entry is updated with a new device ID matching the
           new device on which the PVID was found.  The refresh mode can be
           configured to run once, when the machine change is first detected,
           or can be enabled for period of time following the first refresh,
           or can be disabled entirely.

           device_ids_refresh = 0
           Disables refresh mode.

           device_ids_refresh = 1
           Enables one attempt to refresh device IDs when a machine change is
           first detected.

           device_ids_refresh = seconds
           The refresh mode is enabled for this number of seconds following
           the initial refresh attempt, or until all PVs in system.devices
           are found.  During this period, a REFRESH_UNTIL line appears in
           system.devices.  Accepted values are 10-600 seconds.

           In addition to the automated device ID refresh mode, refresh can
           be performed manually:

           Check if system.devices would be updated with new device IDs:
           lvmdevices --check --refresh

           Update system.devices with new device IDs if PVs are found on new
           devices:
           lvmdevices --update --refresh

           The machine ID used in system.devices will be either the DMI
           product_uuid from /sys/devices/virtual/dmi/id/product_uuid, or the
           hostname from uname(2).  See lvm.conf(5) device_ids_refresh_checks
           to configure this.

       custom devices files
           Multiple devices files can be kept in /etc/lvm/devices, which
           allows lvm to be used with different sets of devices.  For
           example, a given application may not need to access the system's
           devices, and the system may not need to access the application's
           devices.  In this case, system.devices could list only the
           system's devices and <application>.devices file could list only
           the application's devices.  The option --devicesfile <filename> is
           used to select the devices file to use with the command.  Without
           the option set, the default system.devices file is used.

           If the special devices file /etc/lvm/devices/dmeventd.devices
           exists, then dmeventd uses dmeventd.devices instead of
           system.devices.  Using dmeventd.devices is necessary if VGs from
           separate devices files require the services of dmeventd.  In this
           case, dmeventd.devices should list devices from all of the VGs
           that require dmeventd.

       disabling and overriding
           There are multiple ways that the devices file feature can be
           disabled or overridden:

           • no system.devices
             If the system.devices file does not exist, then the devices file
             feature is disabled.

           • use_devicesfile=0
             If lvm.conf use_devicesfile is set to 0, then the devices file
             feature is disabled, even if the system.devices file exists.

           • --devicesfile ""
             If an empty devices file name is specified on the command line,
             then that command will not use a devices file.

           • --devices device
             If specific devices are named on the command line with
             --devices, then the command will not use a devices file, and
             will only access the named devices.

           • pvs -A
             If given the -A or --allpvs option, the pvs(8) command will not
             use a devices file.

           When the devices file is disabled, lvm commands revert to using
           the lvm.conf filter.  When the devices file is used, lvm commands
           ignore the lvm.conf filter setting, except for vgimportdevices
           which does apply the regex filter to the set of devices on the
           system when looking for VGs to import to the devices file.

       VG metadata
           LVM commands that write VG metadata will include the device ID of
           each PV in the VG metadata.  The device ID can be displayed with
           the options:

           pvs -o deviceidtype,deviceid

           (Note that the lvmdevices command does not update VG metadata, but
           subsequent lvm commands modifying the metadata will include the
           device ID.)

       creating the devices file
           If the system.devices file does not yet exist, the pvcreate or
           vgcreate commands will create it only if they see no existing VGs
           on the system.  lvmdevices --adddev and vgimportdevices will
           always create a new devices file if it does not yet exist.

## [](#USAGE)USAGE

           Print devices in the devices file.

           lvmdevices
               [ COMMON_OPTIONS ]

           —

           Check the devices file and report incorrect values.

           lvmdevices --check
               [ COMMON_OPTIONS ]

           —

           Update the devices file to fix incorrect values.

           lvmdevices --update
               [ COMMON_OPTIONS ]

           —

           Add a device to the devices file.

           lvmdevices --adddev PV
               [    --deviceidtype String ]
               [ COMMON_OPTIONS ]

           —

           Remove a device from the devices file.

           lvmdevices --deldev PV
               [ COMMON_OPTIONS ]

           —

           Find  the  device  with  the  given PVID and add it to the devices
           file.

           lvmdevices --addpvid String
               [    --deviceidtype String ]
               [ COMMON_OPTIONS ]

           —

           Remove the devices file entry for the given PVID.

           lvmdevices --delpvid String
               [ COMMON_OPTIONS ]

           —

           Common options for lvm:
               [ -d|--debug ]
               [ -h|--help ]
               [ -q|--quiet ]
               [ -t|--test ]
               [ -v|--verbose ]
               [ -y|--yes ]
               [    --commandprofile String ]
               [    --config String ]
               [    --devices PV ]
               [    --devicesfile String ]
               [    --driverloaded y|n ]
               [    --journal String ]
               [    --lockopt String ]
               [    --longhelp ]
               [    --nohints ]
               [    --nolocking ]
               [    --profile String ]
               [    --version ]

## [](#OPTIONS)OPTIONS

           --adddev PV
                  Add a device to the devices file.

           --addpvid String
                  Find a device with the PVID  and  add  the  device  to  the
                  devices file.

           --check
                  Checks  the content of the devices file.  Reports incorrect
                  device names or PVIDs for entries.

           --commandprofile String
                  The command profile to use for command configuration.   See
                  lvm.conf(5) for more information about profiles.

           --config String
                  Config settings for the command. These override lvm.conf(5)
                  settings.    The   String  arg  uses  the  same  format  as
                  lvm.conf(5),  or  may  use   section/field   syntax.    See
                  lvm.conf(5) for more information about config.

           -d|--debug ...
                  Set  debug  level. Repeat from 1 to 6 times to increase the
                  detail of messages sent to the log file and/or  syslog  (if
                  configured).

           --deldev PV
                  Remove a device from the devices file.

           --delpvid String
                  Remove a device with the PVID from the devices file.

           --deviceidtype String
                  The  type  of  device  ID  to  use  for the device.  If the
                  specified type is available for the device,  then  it  will
                  override the default type that lvm would use.

           --devices PV
                  Devices  that  the  command  can  use.  This  option can be
                  repeated or accepts a comma separated list of devices. This
                  overrides the devices file.

           --devicesfile String
                  A file listing devices that LVM should use.  The file  must
                  exist   in   /etc/lvm/devices/  and  is  managed  with  the
                  lvmdevices(8)  command.   This  overrides  the  lvm.conf(5)
                  devices/devicesfile and devices/use_devicesfile settings.

           --driverloaded y|n
                  If  set  to no, the command will not attempt to use device-
                  mapper.  For testing and debugging.

           -h|--help
                  Display help text.

           --journal String
                  Record  information   in   the   systemd   journal.    This
                  information  is  in  addition to information enabled by the
                  lvm.conf log/journal setting.  command: record  information
                  about  the  command.   output:  record  the default command
                  output.  debug: record full command debugging.

           --lockopt String
                  Used to pass options for special cases  to  lvmlockd.   See
                  lvmlockd(8) for more information.

           --longhelp
                  Display long help text.

           --nohints
                  Do  not  use  the  hints  file to locate devices for PVs. A
                  command may read more devices to find PVs  when  hints  are
                  not used. The command will still perform standard hint file
                  invalidation where appropriate.

           --nolocking
                  Disable locking.

           --profile String
                  An   alias   for   --commandprofile  or  --metadataprofile,
                  depending on the command.

           -q|--quiet ...
                  Suppress output and log  messages.  Overrides  --debug  and
                  --verbose.   Repeat  once to also suppress any prompts with
                  answer 'no'.

           -t|--test
                  Run in test mode. Commands will not update metadata.   This
                  is  implemented  by  disabling  all  metadata  writing  but
                  nevertheless returning success  to  the  calling  function.
                  This  may  lead  to  unusual  error messages in multi-stage
                  operations if a tool relies on  reading  back  metadata  it
                  believes has changed but hasn't.

           --update
                  Update the content of the devices file.

           -v|--verbose ...
                  Set verbose level. Repeat from 1 to 4 times to increase the
                  detail of messages sent to stdout and stderr.

           --version
                  Display version information.

           -y|--yes
                  Do  not  prompt  for  confirmation interactively but always
                  assume the answer yes.  Use  with  extreme  caution.   (For
                  automatic no, see -qq.)

## [](#VARIABLES)VARIABLES

           String See the option description for information about the string
                  content.

           Size[UNIT]
                  Size is an input number that accepts an optional unit.
                  Input units are always treated as base two values,
                  regardless of capitalization, e.g. 'k' and 'K' both refer
                  to 1024.  The default input unit is specified by letter,
                  followed by |UNIT.  UNIT represents other possible input
                  units: b|B is bytes, s|S is sectors of 512 bytes, k|K is
                  KiB, m|M is MiB, g|G is GiB, t|T is TiB, p|P is PiB, e|E is
                  EiB.  (This should not be confused with the output control
                  --units, where capital letters mean multiple of 1000.)

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           See lvm(8) for information about environment variables used by
           lvm.  For example, LVM_VG_NAME can generally be substituted for a
           required VG parameter.

## [](#SEE_ALSO)SEE ALSO

           lvm(8), lvm.conf(5), lvmconfig(8), lvmdevices(8),

           pvchange(8), pvck(8), pvcreate(8), pvdisplay(8), pvmove(8),
           pvremove(8), pvresize(8), pvs(8), pvscan(8),

           vgcfgbackup(8), vgcfgrestore(8), vgchange(8), vgck(8),
           vgcreate(8), vgconvert(8), vgdisplay(8), vgexport(8), vgextend(8),
           vgimport(8), vgimportclone(8), vgimportdevices(8), vgmerge(8),
           vgmknodes(8), vgreduce(8), vgremove(8), vgrename(8), vgs(8),
           vgscan(8), vgsplit(8),

           lvcreate(8), lvchange(8), lvconvert(8), lvdisplay(8), lvextend(8),
           lvreduce(8), lvremove(8), lvrename(8), lvresize(8), lvs(8),
           lvscan(8),

           lvm-fullreport(8), lvm-lvpoll(8), blkdeactivate(8), lvmdump(8),

           dmeventd(8), lvmpolld(8), lvmlockd(8), lvmlockctl(8), cmirrord(8),
           lvmdbusd(8), fsadm(8),

           lvmsystemid(7), lvmreport(7), lvmcache(7), lvmraid(7), lvmthin(7),
           lvmvdo(7), lvmautoactivation(7)

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

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15)     LVMDEVICES(8)

------------------------------------------------------------------------

Pages that refer to this page: [lvchange(8)](../man8/lvchange.8.html),  [lvconvert(8)](../man8/lvconvert.8.html),  [lvcreate(8)](../man8/lvcreate.8.html),  [lvdisplay(8)](../man8/lvdisplay.8.html),  [lvextend(8)](../man8/lvextend.8.html),  [lvm(8)](../man8/lvm.8.html),  [lvmconfig(8)](../man8/lvmconfig.8.html),  [lvmdevices(8)](../man8/lvmdevices.8.html),  [lvmdiskscan(8)](../man8/lvmdiskscan.8.html),  [lvm-fullreport(8)](../man8/lvm-fullreport.8.html),  [lvmlockd(8)](../man8/lvmlockd.8.html),  [lvm-lvpoll(8)](../man8/lvm-lvpoll.8.html),  [lvreduce(8)](../man8/lvreduce.8.html),  [lvremove(8)](../man8/lvremove.8.html),  [lvrename(8)](../man8/lvrename.8.html),  [lvresize(8)](../man8/lvresize.8.html),  [lvs(8)](../man8/lvs.8.html),  [lvscan(8)](../man8/lvscan.8.html),  [pvchange(8)](../man8/pvchange.8.html),  [pvck(8)](../man8/pvck.8.html),  [pvcreate(8)](../man8/pvcreate.8.html),  [pvdisplay(8)](../man8/pvdisplay.8.html),  [pvmove(8)](../man8/pvmove.8.html),  [pvremove(8)](../man8/pvremove.8.html),  [pvresize(8)](../man8/pvresize.8.html),  [pvs(8)](../man8/pvs.8.html),  [pvscan(8)](../man8/pvscan.8.html),  [vgcfgbackup(8)](../man8/vgcfgbackup.8.html),  [vgcfgrestore(8)](../man8/vgcfgrestore.8.html),  [vgchange(8)](../man8/vgchange.8.html),  [vgck(8)](../man8/vgck.8.html),  [vgconvert(8)](../man8/vgconvert.8.html),  [vgcreate(8)](../man8/vgcreate.8.html),  [vgdisplay(8)](../man8/vgdisplay.8.html),  [vgexport(8)](../man8/vgexport.8.html),  [vgextend(8)](../man8/vgextend.8.html),  [vgimport(8)](../man8/vgimport.8.html),  [vgimportclone(8)](../man8/vgimportclone.8.html),  [vgimportdevices(8)](../man8/vgimportdevices.8.html),  [vgmerge(8)](../man8/vgmerge.8.html),  [vgmknodes(8)](../man8/vgmknodes.8.html),  [vgreduce(8)](../man8/vgreduce.8.html),  [vgremove(8)](../man8/vgremove.8.html),  [vgrename(8)](../man8/vgrename.8.html),  [vgs(8)](../man8/vgs.8.html),  [vgscan(8)](../man8/vgscan.8.html),  [vgsplit(8)](../man8/vgsplit.8.html)

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
