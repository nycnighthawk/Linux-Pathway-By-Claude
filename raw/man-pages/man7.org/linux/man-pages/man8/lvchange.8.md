---
{"title": "lvchange(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/lvchange.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvchange(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [USAGE](#USAGE) \| [OPTIONS](#OPTIONS) \| [VARIABLES](#VARIABLES) \| [ENVIRONMENT VARIABLES](#ENVIRONMENT_VARIABLES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                          |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVCHANGE(8)              System Manager's Manual              LVCHANGE(8)

## [](#NAME)NAME

           lvchange — Change the attributes of logical volume(s)

## [](#SYNOPSIS)SYNOPSIS

           lvchange option_args position_args
               [ option_args ]

            -a|--activate y|n|ay
               --activationmode partial|degraded|complete
               --addtag Tag
               --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit
            -A|--autobackup y|n
               --cachemode writethrough|writeback|passthrough
               --cachepolicy String
               --cachesettings String
               --commandprofile String
               --compression y|n
               --config String
            -C|--contiguous y|n
            -d|--debug
               --deduplication y|n
               --deltag Tag
               --detachprofile
               --devices PV
               --devicesfile String
               --discards passdown|nopassdown|ignore
               --driverloaded y|n
               --errorwhenfull y|n
            -f|--force
            -h|--help
            -K|--ignoreactivationskip
               --ignorelockingfailure
               --ignoremonitoring
               --journal String
               --lockopt String
               --longhelp
            -j|--major Number
               --[raid]maxrecoveryrate Size[k|UNIT]
               --metadataprofile String
               --minor Number
               --[raid]minrecoveryrate Size[k|UNIT]
               --monitor y|n
               --nohints
               --nolocking
               --noudevsync
            -P|--partial
            -p|--permission rw|r
            -M|--persistent y|n
               --poll y|n
               --profile String
            -q|--quiet
            -r|--readahead auto|none|Number
               --readonly
               --rebuild PV
               --refresh
               --reportformat basic|json
               --resync
            -S|--select String
            -k|--setactivationskip y|n
               --setautoactivation y|n
               --[raid]syncaction check|repair
               --sysinit
            -t|--test
            -v|--verbose
               --version
               --[raid]writebehind Number
               --[raid]writemostly PV[:t|n|y]
            -y|--yes
            -Z|--zero y|n

## [](#DESCRIPTION)DESCRIPTION

           lvchange changes LV attributes in the VG, changes LV activation in
           the kernel, and includes other utilities for LV maintenance.

## [](#USAGE)USAGE

           Change a general LV attribute.
           For options listed in parentheses, any one is
           required, after which the others are optional.

           lvchange
               ( -C|--contiguous y|n
                 -p|--permission rw|r
                 -r|--readahead auto|none|Number
                 -k|--setactivationskip y|n
                 -Z|--zero y|n
                 -M|--persistent n
                    --addtag Tag
                    --deltag Tag
                    --alloc   contiguous|cling|cling_by_tags|normal|anywhere|
               inherit
                    --compression y|n
                    --deduplication y|n
                    --detachprofile
                    --metadataprofile String
                    --profile String
                    --setautoactivation y|n
                    --errorwhenfull y|n
                    --discards passdown|nopassdown|ignore
                    --cachemode writethrough|writeback|passthrough
                    --cachepolicy String
                    --cachesettings String
                    --[raid]minrecoveryrate Size[k|UNIT]
                    --[raid]maxrecoveryrate Size[k|UNIT]
                    --[raid]writebehind Number
                    --[raid]writemostly PV[:t|n|y] )
                VG|LV|Tag|Select ...
               [ -a|--activate y|n|ay ]
               [    --poll y|n ]
               [    --monitor y|n ]
               [ COMMON_OPTIONS ]

           —

           Resyncronize a mirror or raid LV.
           Use to reset 'R' attribute on a not initially synchronized LV.

           lvchange --resync VG|LV1|Tag|Select ...
               [ -a|--activate y|n|ay ]
               [ COMMON_OPTIONS ]

               LV1 types: mirror raid

           —

           Resynchronize or check a raid LV.

           lvchange --syncaction check|repair VG|LV1|Tag|Select ...
               [ COMMON_OPTIONS ]

               LV1 types: raid

           —

           Reconstruct data on specific PVs of a raid LV.

           lvchange --rebuild PV VG|LV1|Tag|Select ...
               [ COMMON_OPTIONS ]

               LV1 types: raid

           —

           Activate or deactivate an LV.

           lvchange -a|--activate y|n|ay VG|LV|Tag|Select ...
               [ -P|--partial ]
               [ -K|--ignoreactivationskip ]
               [    --activationmode partial|degraded|complete ]
               [    --poll y|n ]
               [    --monitor y|n ]
               [    --ignorelockingfailure ]
               [    --sysinit ]
               [    --readonly ]
               [ COMMON_OPTIONS ]

           —

           Reactivate an LV using the latest metadata.

           lvchange --refresh VG|LV|Tag|Select ...
               [ -P|--partial ]
               [    --activationmode partial|degraded|complete ]
               [    --poll y|n ]
               [    --monitor y|n ]
               [ COMMON_OPTIONS ]

           —

           Start or stop monitoring an LV from dmeventd.

           lvchange --monitor y|n VG|LV|Tag|Select ...
               [ COMMON_OPTIONS ]

           —

           Start or stop processing an LV conversion.

           lvchange --poll y|n VG|LV|Tag|Select ...
               [    --monitor y|n ]
               [ COMMON_OPTIONS ]

           —

           Make the minor device number persistent for an LV.

           lvchange -M|--persistent y --minor Number LV
               [ -j|--major Number ]
               [ -a|--activate y|n|ay ]
               [    --poll y|n ]
               [    --monitor y|n ]
               [ COMMON_OPTIONS ]

           —

           Common options for command:
               [ -A|--autobackup y|n ]
               [ -f|--force ]
               [ -S|--select String ]
               [    --ignoremonitoring ]
               [    --noudevsync ]
               [    --reportformat basic|json ]

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

           -a|--activate y|n|ay
                  Change the active state of LVs.  An active LV can  be  used
                  through  a  block device, allowing data on the LV to be ac‐
                  cessed.  y makes LVs active, or available.  n makes LVs in‐
                  active, or unavailable.  The block device  for  the  LV  is
                  added or removed from the system using device-mapper in the
                  kernel.  A symbolic link /dev/VGName/LVName pointing to the
                  device  node  is  also  added/removed.   All  software  and
                  scripts should access the device through the symbolic  link
                  and  present  this as the name of the device.  The location
                  and name of the underlying device node may  depend  on  the
                  distribution,  configuration  (e.g.  udev), or release ver‐
                  sion.  ay specifies autoactivation, which is used  by  sys‐
                  tem-generated activation commands.  By default, LVs are au‐
                  toactivated.  An autoactivation property can be set on a VG
                  or  LV  to  disable autoactivation, see --setautoactivation
                  y|n in vgchange, lvchange, vgcreate, and lvcreate.  Display
                  the property with vgs  or  lvs  "-o  autoactivation".   The
                  lvm.conf(5)  auto_activation_volume_list  includes names of
                  VGs or LVs that should be autoactivated, and  anything  not
                  listed  is  not  autoactivated.   When auto_activation_vol‐
                  ume_list is undefined (the default), it has no effect.   If
                  auto_activation_volume_list  is  defined  and empty, no LVs
                  are autoactivated.  Items included by  auto_activation_vol‐
                  ume_list  will  not  be autoactivated if the autoactivation
                  property has been disabled.  See lvmlockd(8) for  more  in‐
                  formation  about  activation  options  ey and sy for shared
                  VGs.

           --activationmode partial|degraded|complete
                  Determines if LV activation is allowed when PVs  are  miss‐
                  ing,  e.g.  because of a device failure.  complete only al‐
                  lows LVs with no missing PVs to be activated,  and  is  the
                  most restrictive mode.  degraded allows RAID LVs with miss‐
                  ing  PVs to be activated.  (This does not include the "mir‐
                  ror" type, see "raid1" instead.)   partial  allows  any  LV
                  with  missing  PVs to be activated, and should only be used
                  for recovery or repair.  For default, see lvm.conf(5) acti‐
                  vation_mode.  See lvmraid(7) for more information.

           --addtag Tag
                  Adds a tag to a PV, VG or LV. This option can  be  repeated
                  to  add  multiple  tags at once. See lvm(8) for information
                  about tags.

           --alloc contiguous|cling|cling_by_tags|normal|anywhere|inherit
                  Determines the allocation policy when a  command  needs  to
                  allocate Physical Extents (PEs) from the VG. Each VG and LV
                  has   an  allocation  policy  which  can  be  changed  with
                  vgchange/lvchange, or overridden on the command line.  nor‐
                  mal applies common sense rules such as not placing parallel
                  stripes on the same PV.  inherit applies the VG  policy  to
                  an  LV.   contiguous requires new PEs be placed adjacent to
                  existing PEs.  cling places new PEs on the same PV  as  ex‐
                  isting PEs in the same stripe of the LV.  If there are suf‐
                  ficient  PEs  for  an  allocation,  but normal does not use
                  them, anywhere will use them even  if  it  reduces  perfor‐
                  mance, e.g. by placing two stripes on the same PV.  Option‐
                  al  positional PV args on the command line can also be used
                  to limit which PVs the command  will  use  for  allocation.
                  See lvm(8) for more information about allocation.

           -A|--autobackup y|n
                  Specifies if metadata should be backed up automatically af‐
                  ter  a  change.   Enabling  this  is  strongly advised! See
                  vgcfgbackup(8) for more information.

           --cachemode writethrough|writeback|passthrough
                  Specifies when writes to a cache LV  should  be  considered
                  complete.   writeback considers a write complete as soon as
                  it is stored in the cache pool.   writethough  considers  a
                  write  complete  only  when  it has been stored in both the
                  cache pool and on the origin LV.  While writethrough may be
                  slower for writes, it is more resilient if something should
                  happen to a device associated with the cache pool LV.  With
                  passthrough,  all  reads are served from the origin LV (all
                  reads miss the cache) and all writes are forwarded  to  the
                  origin  LV;  additionally, write hits cause cache block in‐
                  validates. See lvmcache(7) for more information.

           --cachepolicy String
                  Specifies the cache policy for a cache LV.  See lvmcache(7)
                  for more information.

           --cachesettings String
                  Specifies tunable values for a cache LV in  "Key  =  Value"
                  form.  Repeat this option to specify multiple values.  (The
                  default  values  should  usually be adequate.)  The special
                  string value default switches settings back  to  their  de‐
                  fault  kernel values and removes them from the list of set‐
                  tings stored in LVM metadata.  See lvmcache(7) for more in‐
                  formation.

           --commandprofile String
                  The command profile to use for command configuration.   See
                  lvm.conf(5) for more information about profiles.

           --compression y|n
                  Controls  whether compression is enabled or disable for VDO
                  volume.  See lvmvdo(7) for more information about  VDO  us‐
                  age.

           --config String
                  Config settings for the command. These override lvm.conf(5)
                  settings.    The   String  arg  uses  the  same  format  as
                  lvm.conf(5),  or  may  use   section/field   syntax.    See
                  lvm.conf(5) for more information about config.

           -C|--contiguous y|n
                  Sets  or  resets  the contiguous allocation policy for LVs.
                  Default is no contiguous allocation based on  a  next  free
                  principle.   It is only possible to change a non-contiguous
                  allocation policy to contiguous if  all  of  the  allocated
                  physical extents in the LV are already contiguous.

           -d|--debug ...
                  Set  debug  level. Repeat from 1 to 6 times to increase the
                  detail of messages sent to the log file and/or  syslog  (if
                  configured).

           --deduplication y|n
                  Controls  whether  deduplication  is enabled or disable for
                  VDO volume.  See lvmvdo(7) for more information  about  VDO
                  usage.

           --deltag Tag
                  Deletes  a  tag from a PV, VG or LV. This option can be re‐
                  peated to delete multiple tags at once. See lvm(8) for  in‐
                  formation about tags.

           --detachprofile
                  Detaches   a  metadata  profile  from  a  VG  or  LV.   See
                  lvm.conf(5) for more information about profiles.

           --devices PV
                  Devices that the command can use. This option  can  be  re‐
                  peated  or  accepts a comma separated list of devices. This
                  overrides the devices file.

           --devicesfile String
                  A file listing devices that LVM should use.  The file  must
                  exist   in   /etc/lvm/devices/  and  is  managed  with  the
                  lvmdevices(8) command.  This overrides the lvm.conf(5)  de‐
                  vices/devicesfile and devices/use_devicesfile settings.

           --discards passdown|nopassdown|ignore
                  Specifies how the device-mapper thin pool layer in the ker‐
                  nel should handle discards.  ignore causes the thin pool to
                  ignore  discards.   nopassdown  causes  the  thin  pool  to
                  process discards itself to allow reuse of unneeded  extents
                  in the thin pool.  passdown causes the thin pool to process
                  discards  itself (like nopassdown) and pass the discards to
                  the underlying device.  See lvmthin(7)  for  more  informa‐
                  tion.

           --driverloaded y|n
                  If  set  to no, the command will not attempt to use device-
                  mapper.  For testing and debugging.

           --errorwhenfull y|n
                  Specifies thin pool behavior when data space is  exhausted.
                  When  yes,  device-mapper  will immediately return an error
                  when a thin pool is full and an I/O request requires space.
                  When no, device-mapper will queue these I/O requests for  a
                  period  of time to allow the thin pool to be extended.  Er‐
                  rors are returned if no space is available after the  time‐
                  out.    (Also   see   dm-thin-pool   kernel  module  option
                  no_space_timeout.)  See lvmthin(7) for more information.

           -f|--force ...
                  Override various  checks,  confirmations  and  protections.
                  Use with extreme caution.

           -h|--help
                  Display help text.

           -K|--ignoreactivationskip
                  Ignore  the  "activation skip" LV flag during activation to
                  allow LVs with the flag set to be activated.

           --ignorelockingfailure
                  Allows a command to continue with read-only metadata opera‐
                  tions after locking failures.

           --ignoremonitoring
                  Do not interact with dmeventd unless  --monitor  is  speci‐
                  fied.   Do not use this if dmeventd is already monitoring a
                  device.

           --journal String
                  Record information in the systemd journal.   This  informa‐
                  tion  is in addition to information enabled by the lvm.conf
                  log/journal setting.  command: record information about the
                  command.  output: record the default command  output.   de‐
                  bug: record full command debugging.

           --lockopt String
                  Used  to  pass  options for special cases to lvmlockd.  See
                  lvmlockd(8) for more information.

           --longhelp
                  Display long help text.

           -j|--major Number
                  Sets the major number of an LV block device.

           --[raid]maxrecoveryrate Size[k|UNIT]
                  Sets the maximum recovery rate for a  RAID  LV.   The  rate
                  value  is  an  amount of data per second for each device in
                  the array.  Setting the rate to 0 means it will be unbound‐
                  ed.  See lvmraid(7) for more information.

           --metadataprofile String
                  The metadata profile to use for command configuration.  See
                  lvm.conf(5) for more information about profiles.

           --minor Number
                  Sets the minor number of an LV block device.

           --[raid]minrecoveryrate Size[k|UNIT]
                  Sets the minimum recovery rate for a  RAID  LV.   The  rate
                  value  is  an  amount of data per second for each device in
                  the array.  Setting the rate to 0 means it will be unbound‐
                  ed.  See lvmraid(7) for more information.

           --monitor y|n
                  Start (yes) or stop (no) monitoring an  LV  with  dmeventd.
                  dmeventd monitors kernel events for an LV, and performs au‐
                  tomated  maintenance  for  the  LV  in  reponse to specific
                  events.  See dmeventd(8) for more information.

           --nohints
                  Do not use the hints file to locate devices for PVs. A com‐
                  mand may read more devices to find PVs when hints  are  not
                  used. The command will still perform standard hint file in‐
                  validation where appropriate.

           --nolocking
                  Disable locking.

           --noudevsync
                  Disables  udev  synchronisation.  The process will not wait
                  for notification from udev. It will  continue  irrespective
                  of any possible udev processing in the background. Only use
                  this  if  udev  is not running or has rules that ignore the
                  devices LVM creates.

           -P|--partial
                  Commands will do their best to activate LVs with missing PV
                  extents.  Missing extents may be replaced with error or ze‐
                  ro segments according to  the   missing_stripe_filler  set‐
                  ting.  Metadata may not be changed with this option.

           -p|--permission rw|r
                  Set  access permission to read only r or read and write rw.

           -M|--persistent y|n
                  When yes, makes the specified minor number persistent.

           --poll y|n
                  When yes, start the background transformation of an LV.  An
                  incomplete transformation, e.g. pvmove or lvconvert  inter‐
                  rupted  by  reboot or crash, can be restarted from the last
                  checkpoint with --poll y.  When no, background  transforma‐
                  tion  of  an LV will not occur, and the transformation will
                  not complete. It may not be appropriate to immediately poll
                  an LV after activation, in which case --poll n can be  used
                  to defer polling until a later --poll y command.

           --profile String
                  An alias for --commandprofile or --metadataprofile, depend‐
                  ing on the command.

           -q|--quiet ...
                  Suppress  output  and  log  messages. Overrides --debug and
                  --verbose.  Repeat once to also suppress any  prompts  with
                  answer 'no'.

           -r|--readahead auto|none|Number
                  Sets read ahead sector count of an LV.  auto is the default
                  which allows the kernel to choose a suitable value automat‐
                  ically.  none is equivalent to zero.

           --readonly
                  Run the command in a special read-only mode which will read
                  on-disk  metadata  without  needing to take any locks. This
                  can be used to peek inside metadata used by a  virtual  ma‐
                  chine  image  while  the virtual machine is running. No at‐
                  tempt will be made to communicate  with  the  device-mapper
                  kernel  driver,  so this option is unable to report whether
                  or not LVs are actually in use.

           --rebuild PV
                  Selects a PV to rebuild in a raid LV. Multiple PVs  can  be
                  rebuilt by repeating this option.  Use this option in place
                  of  --resync  or --syncaction repair when the PVs with cor‐
                  rupted data are known, and  their  data  should  be  recon‐
                  structed  rather than reconstructing default (rotating) da‐
                  ta.  See lvmraid(7) for more information.

           --refresh
                  If the LV is active, reload its metadata.  This is not nec‐
                  essary in normal operation, but may be useful if  something
                  has gone wrong, or if some form of manual LV sharing is be‐
                  ing used.

           --reportformat basic|json
                  Overrides  current  output  format for reports which is de‐
                  fined  globally  by  the  report/output_format  setting  in
                  lvm.conf(5).  basic is the original format with columns and
                  rows.   If  there is more than one report per command, each
                  report is prefixed with the report name for identification.
                  json  produces  report   output   in   JSON   format.   See
                  lvmreport(7) for more information.

           --resync
                  Initiates mirror synchronization. Synchronization generally
                  happens  automatically,  but  this option forces it to run.
                  Also see --rebuild to synchronize a  specific  PV.   During
                  synchronization,  data  is read from the primary mirror de‐
                  vice and copied to the others. This can  take  considerable
                  time,  during  which the LV is without a complete redundant
                  copy of the data.  See lvmraid(7) for more information.

           -S|--select String
                  Select objects for processing and reporting based on speci‐
                  fied criteria.  The criteria syntax is described  by  --se‐
                  lect  help  and  lvmreport(7).  For reporting commands, one
                  row is displayed for each  object  matching  the  criteria.
                  See  --options help for selectable object fields.  Rows can
                  be displayed with an additional "selected"  field  (-o  se‐
                  lected)  showing  1  if the row matches the selection and 0
                  otherwise.  For non-reporting commands  which  process  LVM
                  entities, the selection is used to choose items to process.

           -k|--setactivationskip y|n
                  Persistently  sets  (yes)  or  clears  (no) the "activation
                  skip" flag on an LV.  An LV with this flag set is not acti‐
                  vated unless the --ignoreactivationskip option is  used  by
                  the activation command.  This flag is set by default on new
                  thin  snapshot  LVs.   The flag is not applied to deactiva‐
                  tion.  The current value of the flag is  indicated  in  the
                  lvs lv_attr bits.

           --setautoactivation y|n
                  Set the autoactivation property on a VG or LV.  Display the
                  property with vgs or lvs "-o autoactivation".  When the au‐
                  toactivation property is disabled, the VG or LV will not be
                  activated  by  a  command  doing  autoactivation (vgchange,
                  lvchange, or pvscan using -aay.)  If autoactivation is dis‐
                  abled on a VG, no LVs will be autoactivated in that VG, and
                  the LV autoactivation property has no effect.  If autoacti‐
                  vation is enabled on a VG, autoactivation can  be  disabled
                  for individual LVs.

           --[raid]syncaction check|repair
                  Initiate  different  types  of  RAID synchronization.  This
                  causes the RAID LV to read all data and  parity  blocks  in
                  the  array  and check for discrepancies (mismatches between
                  mirrors or incorrect parity values).  check will count  but
                  not  correct discrepancies.  repair will correct discrepan‐
                  cies.  See lvs(8) for reporting discrepancies found or  re‐
                  paired.

           --sysinit
                  Indicates that vgchange/lvchange is being invoked from ear‐
                  ly  system  initialisation  scripts  (e.g. rc.sysinit or an
                  initrd), before  writable  filesystems  are  available.  As
                  such,  some functionality needs to be disabled and this op‐
                  tion acts as a shortcut which selects an appropriate set of
                  options. Currently, this is equivalent to  using  --ignore‐
                  lockingfailure,  --ignoremonitoring,  --poll n, and setting
                  env       var        LVM_SUPPRESS_LOCKING_FAILURE_MESSAGES.
                  vgchange/lvchange  skip autoactivation, and defer to pvscan
                  autoactivation.

           -t|--test
                  Run in test mode. Commands will not update metadata.   This
                  is implemented by disabling all metadata writing but never‐
                  theless returning success to the calling function. This may
                  lead to unusual error messages in multi-stage operations if
                  a  tool  relies  on  reading  back metadata it believes has
                  changed but hasn't.

           -v|--verbose ...
                  Set verbose level. Repeat from 1 to 4 times to increase the
                  detail of messages sent to stdout and stderr.

           --version
                  Display version information.

           --[raid]writebehind Number
                  The maximum number of outstanding writes that  are  allowed
                  to devices in a RAID1 LV that is marked write-mostly.  Once
                  this value is exceeded, writes become synchronous (i.e. all
                  writes  to the constituent devices must complete before the
                  array signals the write has completed). Setting  the  value
                  to  zero  clears  the  preference  and allows the system to
                  choose the value arbitrarily.

           --[raid]writemostly PV[:t|n|y]
                  Mark a device in a RAID1 LV as write-mostly.  All reads  to
                  these  drives  will be avoided unless absolutely necessary.
                  This keeps the number of I/Os to the drive  to  a  minimum.
                  The  default  behavior is to set the write-mostly attribute
                  for the specified PV.  It is also possible  to  remove  the
                  write-mostly flag by adding the suffix :n at the end of the
                  PV  name, or to toggle the value with the suffix :t. Repeat
                  this option to change the attribute on multiple PVs.

           -y|--yes
                  Do not prompt for confirmation interactively but always as‐
                  sume the answer yes. Use with extreme caution.  (For  auto‐
                  matic no, see -qq.)

           -Z|--zero y|n
                  Set  zeroing  mode for thin pool. Note: already provisioned
                  blocks from pool in non-zero mode are not  cleared  in  un‐
                  written parts when setting --zero y.

## [](#VARIABLES)VARIABLES

           VG     Volume Group name.  See lvm(8) for valid names.

           LV     Logical Volume name.  See lvm(8) for valid names.  An LV
                  positional arg generally includes the VG name and LV name,
                  e.g. VG/LV.  LV1 indicates the LV must have a specific
                  type, where the accepted LV types are listed. (raid repre‐
                  sents raid<N> type).

           Tag    Tag name.  See lvm(8) for information about tag names and
                  using tags in place of a VG, LV or PV.

           Select Select indicates that a required positional parameter can
                  be omitted if the --select option is used.  No arg appears
                  in this position.

           String See the option description for information about the string
                  content.

           Size[UNIT]
                  Size is an input number that accepts an optional unit.  In‐
                  put units are always treated as base two values, regardless
                  of capitalization, e.g. 'k' and 'K' both refer to 1024.
                  The default input unit is specified by letter, followed by
                  |UNIT.  UNIT represents other possible input units: b|B is
                  bytes, s|S is sectors of 512 bytes, k|K is KiB, m|M is MiB,
                  g|G is GiB, t|T is TiB, p|P is PiB, e|E is EiB.  (This
                  should not be confused with the output control --units,
                  where capital letters mean multiple of 1000.)

## [](#ENVIRONMENT_VARIABLES)ENVIRONMENT VARIABLES

           See lvm(8) for information about environment variables used by
           lvm.  For example, LVM_VG_NAME can generally be substituted for a
           required VG parameter.

## [](#EXAMPLES)EXAMPLES

           Change LV permission to read-only:
           lvchange -pr vg00/lvol1

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

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15)       LVCHANGE(8)

------------------------------------------------------------------------

Pages that refer to this page: [lvmautoactivation(7)](../man7/lvmautoactivation.7.html),  [lvmcache(7)](../man7/lvmcache.7.html),  [lvmraid(7)](../man7/lvmraid.7.html),  [lvmthin(7)](../man7/lvmthin.7.html),  [lvmvdo(7)](../man7/lvmvdo.7.html),  [lvchange(8)](../man8/lvchange.8.html),  [lvconvert(8)](../man8/lvconvert.8.html),  [lvcreate(8)](../man8/lvcreate.8.html),  [lvdisplay(8)](../man8/lvdisplay.8.html),  [lvextend(8)](../man8/lvextend.8.html),  [lvm(8)](../man8/lvm.8.html),  [lvmconfig(8)](../man8/lvmconfig.8.html),  [lvmdevices(8)](../man8/lvmdevices.8.html),  [lvmdiskscan(8)](../man8/lvmdiskscan.8.html),  [lvm-fullreport(8)](../man8/lvm-fullreport.8.html),  [lvm-lvpoll(8)](../man8/lvm-lvpoll.8.html),  [lvmpolld(8)](../man8/lvmpolld.8.html),  [lvreduce(8)](../man8/lvreduce.8.html),  [lvremove(8)](../man8/lvremove.8.html),  [lvrename(8)](../man8/lvrename.8.html),  [lvresize(8)](../man8/lvresize.8.html),  [lvs(8)](../man8/lvs.8.html),  [lvscan(8)](../man8/lvscan.8.html),  [pvchange(8)](../man8/pvchange.8.html),  [pvck(8)](../man8/pvck.8.html),  [pvcreate(8)](../man8/pvcreate.8.html),  [pvdisplay(8)](../man8/pvdisplay.8.html),  [pvmove(8)](../man8/pvmove.8.html),  [pvremove(8)](../man8/pvremove.8.html),  [pvresize(8)](../man8/pvresize.8.html),  [pvs(8)](../man8/pvs.8.html),  [pvscan(8)](../man8/pvscan.8.html),  [vgcfgbackup(8)](../man8/vgcfgbackup.8.html),  [vgcfgrestore(8)](../man8/vgcfgrestore.8.html),  [vgchange(8)](../man8/vgchange.8.html),  [vgck(8)](../man8/vgck.8.html),  [vgconvert(8)](../man8/vgconvert.8.html),  [vgcreate(8)](../man8/vgcreate.8.html),  [vgdisplay(8)](../man8/vgdisplay.8.html),  [vgexport(8)](../man8/vgexport.8.html),  [vgextend(8)](../man8/vgextend.8.html),  [vgimport(8)](../man8/vgimport.8.html),  [vgimportclone(8)](../man8/vgimportclone.8.html),  [vgimportdevices(8)](../man8/vgimportdevices.8.html),  [vgmerge(8)](../man8/vgmerge.8.html),  [vgmknodes(8)](../man8/vgmknodes.8.html),  [vgreduce(8)](../man8/vgreduce.8.html),  [vgremove(8)](../man8/vgremove.8.html),  [vgrename(8)](../man8/vgrename.8.html),  [vgs(8)](../man8/vgs.8.html),  [vgscan(8)](../man8/vgscan.8.html),  [vgsplit(8)](../man8/vgsplit.8.html)

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
