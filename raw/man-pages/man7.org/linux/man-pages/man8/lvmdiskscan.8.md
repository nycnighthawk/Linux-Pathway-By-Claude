---
{"title": "lvmdiskscan(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lvmdiskscan.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvmdiskscan(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [USAGE](#USAGE) \| [OPTIONS](#OPTIONS) \| [VARIABLES](#VARIABLES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVMDISKSCAN(8)           System Manager's Manual           LVMDISKSCAN(8)

## [](#NAME)NAME

           lvmdiskscan — List devices that may be used as physical volumes

## [](#SYNOPSIS)SYNOPSIS

           lvmdiskscan
               [ option_args ]

## [](#DESCRIPTION)DESCRIPTION

           lvmdiskscan scans all SCSI, (E)IDE disks, multiple devices and a
           bunch of other block devices in the system looking for LVM PVs.
           The size reported is the real device size. Define a filter in
           lvm.conf(5) to restrict the scan to avoid a CD ROM, for example.

           This command is deprecated, use pvs instead.

## [](#USAGE)USAGE

           lvmdiskscan
               [ -l|--lvmpartition ]
               [    --readonly ]
               [ COMMON_OPTIONS ]

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

           --commandprofile String
                  The  command profile to use for command configuration.  See
                  lvm.conf(5) for more information about profiles.

           --config String
                  Config settings for the command. These override lvm.conf(5)
                  settings.   The  String  arg  uses  the  same   format   as
                  lvm.conf(5),   or   may   use  section/field  syntax.   See
                  lvm.conf(5) for more information about config.

           -d|--debug ...
                  Set debug level. Repeat from 1 to 6 times to  increase  the
                  detail  of  messages sent to the log file and/or syslog (if
                  configured).

           --devices PV
                  Devices that the  command  can  use.  This  option  can  be
                  repeated or accepts a comma separated list of devices. This
                  overrides the devices file.

           --devicesfile String
                  A  file listing devices that LVM should use.  The file must
                  exist  in  /etc/lvm/devices/  and  is  managed   with   the
                  lvmdevices(8)  command.   This  overrides  the  lvm.conf(5)
                  devices/devicesfile and devices/use_devicesfile settings.

           --driverloaded y|n
                  If set to no, the command will not attempt to  use  device-
                  mapper.  For testing and debugging.

           -h|--help
                  Display help text.

           --journal String
                  Record   information   in   the   systemd   journal.   This
                  information is in addition to information  enabled  by  the
                  lvm.conf  log/journal setting.  command: record information
                  about the command.   output:  record  the  default  command
                  output.  debug: record full command debugging.

           --lockopt String
                  Used  to  pass  options for special cases to lvmlockd.  See
                  lvmlockd(8) for more information.

           --longhelp
                  Display long help text.

           -l|--lvmpartition
                  Only report PVs.

           --nohints
                  Do not use the hints file to  locate  devices  for  PVs.  A
                  command  may  read  more devices to find PVs when hints are
                  not used. The command will still perform standard hint file
                  invalidation where appropriate.

           --nolocking
                  Disable locking.

           --profile String
                  An  alias  for   --commandprofile   or   --metadataprofile,
                  depending on the command.

           -q|--quiet ...
                  Suppress  output  and  log  messages. Overrides --debug and
                  --verbose.  Repeat once to also suppress any  prompts  with
                  answer 'no'.

           --readonly
                  Run the command in a special read-only mode which will read
                  on-disk  metadata  without  needing to take any locks. This
                  can be used to peek  inside  metadata  used  by  a  virtual
                  machine  image  while  the  virtual  machine is running. No
                  attempt will be made to communicate with the  device-mapper
                  kernel  driver,  so this option is unable to report whether
                  or not LVs are actually in use.

           -t|--test
                  Run in test mode. Commands will not update metadata.   This
                  is  implemented  by  disabling  all  metadata  writing  but
                  nevertheless returning success  to  the  calling  function.
                  This  may  lead  to  unusual  error messages in multi-stage
                  operations if a tool relies on  reading  back  metadata  it
                  believes has changed but hasn't.

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

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15)    LVMDISKSCAN(8)

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
