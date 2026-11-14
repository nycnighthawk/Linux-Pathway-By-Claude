---
{"title": "lvm.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/lvm.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lvm.conf(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SYNTAX](#SYNTAX) \| [SETTINGS](#SETTINGS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LVM.CONF(5)                File Formats Manual                LVM.CONF(5)

## [](#NAME)NAME

           lvm.conf — Configuration file for LVM2

## [](#SYNOPSIS)SYNOPSIS

           /etc/lvm/lvm.conf

## [](#DESCRIPTION)DESCRIPTION

           lvm.conf is loaded during the initialisation phase of lvm(8).
           This file can in turn lead to other files being loaded - settings
           read in later override earlier settings.  File timestamps are
           checked between commands and if any have changed, all the files
           are reloaded.

           For a description of each lvm.conf(5) setting, run:

           lvmconfig --typeconfig default --withcomments --withspaces

           The settings defined in lvm.conf can be overridden by any of these
           extended configuration methods:

           direct config override on command line
                  The --config ConfigurationString command line option takes
                  the ConfigurationString as direct string representation of
                  the configuration to override the existing configuration.
                  The ConfigurationString is of exactly the same format as
                  used in any LVM configuration file.

           profile config
                  A profile is a set of selected customizable configuration
                  settings that are aimed to achieve a certain
                  characteristics in various environments or uses. It's used
                  to override existing configuration.  Normally, the name of
                  the profile should reflect that environment or use.

           There are two groups of profiles recognised: command profiles and
           metadata profiles.

           The command profile is used to override selected configuration
           settings at global LVM command level - it is applied at the very
           beginning of LVM command execution and it is used throughout the
           whole time of LVM command execution. The command profile is
           applied by using the --commandprofile ProfileName command line
           option that is recognised by all LVM2 commands.

           The metadata profile is used to override selected configuration
           settings at Volume Group/Logical Volume level - it is applied
           independently for each Volume Group/Logical Volume that is being
           processed. As such, each Volume Group/Logical Volume can store the
           profile name used in its metadata so next time the Volume
           Group/Logical Volume is processed, the profile is applied
           automatically. If Volume Group and any of its Logical Volumes have
           different profiles defined, the profile defined for the Logical
           Volume is preferred. The metadata profile can be attached/detached
           by using the lvchange and vgchange commands and their
           --metadataprofile ProfileName and --detachprofile options or the
           --metadataprofile option during creation when using vgcreate or
           lvcreate command.  The vgs and lvs reporting commands provide -o
           vg_profile and -o lv_profile output options to show the metadata
           profile currently attached to a Volume Group or a Logical Volume.

           The set of options allowed for command profiles is mutually
           exclusive when compared to the set of options allowed for metadata
           profiles. The settings that belong to either of these two sets
           can't be mixed together and LVM tools will reject such profiles.

           LVM itself provides a few predefined configuration profiles.
           Users are allowed to add more profiles with different values if
           needed.  For this purpose, there's the
           command_profile_template.profile (for command profiles) and
           metadata_profile_template.profile (for metadata profiles) which
           contain all settings that are customizable by profiles of certain
           type. Users are encouraged to copy these template profiles and
           edit them as needed. Alternatively, the lvmconfig --file
           <ProfileName.profile> --type profilable-command <section> or
           lvmconfig --file <ProfileName.profile> --type profilable-metadata
           <section> can be used to generate a configuration with profilable
           settings in either of the type for given section and save it to
           new ProfileName.profile (if the section is not specified, all
           profilable settings are reported).

           The profiles are stored in /etc/lvm/profile directory by default.
           This location can be changed by using the config/profile_dir
           setting.  Each profile configuration is stored in
           ProfileName.profile file in the profile directory. When
           referencing the profile, the .profile suffix is left out.

           tag config
                  See tags configuration setting description below.

           When several configuration methods are used at the same time and
           when LVM looks for the value of a particular setting, it traverses
           this config cascade from left to right:

           direct config override on command line → command profile config →
           metadata profile config → tag config → lvmlocal.conf → lvm.conf

           No part of this cascade is compulsory. If there's no setting value
           found at the end of the cascade, a default value is used for that
           setting.  Use lvmconfig to check what settings are in use and what
           the default values are.

## [](#SYNTAX)SYNTAX

           This section describes the configuration file syntax.

           Whitespace is not significant unless it is within quotes.  This
           provides a wide choice of acceptable indentation styles.  Comments
           begin with # and continue to the end of the line.  They are
           treated as whitespace.

           Here is an informal grammar:

           file = value*
                  A configuration file consists of a set of values.

           value = section | assignment
                  A value can either be a new section, or an assignment.

           section = identifier '{' value* '}'
                  A section groups associated values together. If the same
                  section is encountered multiple times, the contents of all
                  instances are concatenated together in the order of
                  appearance.
                  It is denoted by a name and delimited by curly brackets.
                  e.g.
                  backup {
                         ...
                  }

           assignment = identifier '=' ( array | type )
                  An assignment associates a type with an identifier. If the
                  identifier contains forward slashes, those are interpreted
                  as path delimiters. The statement section/key = value is
                  equivalent to section { key = value }. If multiple
                  instances of the same key are encountered, only the last
                  value is used (and a warning is issued).
                  e.g.   level = 7

           array =  '[' ( type ',')* type ']' | '[' ']'
                  Inhomogeneous arrays are supported.
                  Elements must be separated by commas.
                  An empty array is acceptable.
                  An array with one element will be correctly interpreted if
                  the array brackets are missing.

           type = integer|float|string integer = [0-9]*
                  float = [0-9]*'.'[0-9]*
                  string = '"' .* '"'

                  Strings with spaces must be enclosed in double quotes,
                  single words that start with a letter can be left unquoted.

## [](#SETTINGS)SETTINGS

           The lvmconfig command prints the LVM configuration settings in
           various ways.  See the man page lvmconfig(8).

           Command to print a list of all possible config settings, with
           their default values:
           lvmconfig --type default

           Command to print a list of all possible config settings, with
           their default values, and a full description of each as a comment:
           lvmconfig --type default --withcomments

           Command to print a list of all possible config settings, with
           their current values (configured, non-default values are shown):
           lvmconfig --type current

           Command to print all config settings that have been configured
           with a different value than the default (configured, non-default
           values are shown):
           lvmconfig --type diff

           Command to print a single config setting, with its default value,
           and a full description, where "Section" refers to the config
           section, e.g. global, and "Setting" refers to the name of the
           specific setting, e.g. umask:
           lvmconfig --type default --withcomments Section/Setting

## [](#FILES)FILES

           /etc/lvm/lvm.conf
           /etc/lvm/lvmlocal.conf
           /etc/lvm/archive
           /etc/lvm/backup
           /etc/lvm/cache/.cache
           /etc/lvm/profile
           /run/lock/lvm

## [](#SEE_ALSO)SEE ALSO

           lvm(8), lvmconfig(8)

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

    Red Hat, Inc.     LVM TOOLS 2.03.42(2)-git (2026-05-15)       LVM.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [lvm.conf(5)](../man5/lvm.conf.5.html),  [lvmautoactivation(7)](../man7/lvmautoactivation.7.html),  [lvmcache(7)](../man7/lvmcache.7.html),  [lvmraid(7)](../man7/lvmraid.7.html),  [lvmsystemid(7)](../man7/lvmsystemid.7.html),  [lvmthin(7)](../man7/lvmthin.7.html),  [lvmvdo(7)](../man7/lvmvdo.7.html),  [dmeventd(8)](../man8/dmeventd.8.html),  [fsadm(8)](../man8/fsadm.8.html),  [lvchange(8)](../man8/lvchange.8.html),  [lvconvert(8)](../man8/lvconvert.8.html),  [lvcreate(8)](../man8/lvcreate.8.html),  [lvdisplay(8)](../man8/lvdisplay.8.html),  [lvextend(8)](../man8/lvextend.8.html),  [lvm(8)](../man8/lvm.8.html),  [lvmconfig(8)](../man8/lvmconfig.8.html),  [lvmdevices(8)](../man8/lvmdevices.8.html),  [lvmdiskscan(8)](../man8/lvmdiskscan.8.html),  [lvm-fullreport(8)](../man8/lvm-fullreport.8.html),  [lvm_import_vdo(8)](../man8/lvm_import_vdo.8.html),  [lvmlockd(8)](../man8/lvmlockd.8.html),  [lvm-lvpoll(8)](../man8/lvm-lvpoll.8.html),  [lvmpolld(8)](../man8/lvmpolld.8.html),  [lvreduce(8)](../man8/lvreduce.8.html),  [lvremove(8)](../man8/lvremove.8.html),  [lvrename(8)](../man8/lvrename.8.html),  [lvresize(8)](../man8/lvresize.8.html),  [lvs(8)](../man8/lvs.8.html),  [lvscan(8)](../man8/lvscan.8.html),  [pvchange(8)](../man8/pvchange.8.html),  [pvck(8)](../man8/pvck.8.html),  [pvcreate(8)](../man8/pvcreate.8.html),  [pvdisplay(8)](../man8/pvdisplay.8.html),  [pvmove(8)](../man8/pvmove.8.html),  [pvremove(8)](../man8/pvremove.8.html),  [pvresize(8)](../man8/pvresize.8.html),  [pvs(8)](../man8/pvs.8.html),  [pvscan(8)](../man8/pvscan.8.html),  [vgcfgbackup(8)](../man8/vgcfgbackup.8.html),  [vgcfgrestore(8)](../man8/vgcfgrestore.8.html),  [vgchange(8)](../man8/vgchange.8.html),  [vgck(8)](../man8/vgck.8.html),  [vgconvert(8)](../man8/vgconvert.8.html),  [vgcreate(8)](../man8/vgcreate.8.html),  [vgdisplay(8)](../man8/vgdisplay.8.html),  [vgexport(8)](../man8/vgexport.8.html),  [vgextend(8)](../man8/vgextend.8.html),  [vgimport(8)](../man8/vgimport.8.html),  [vgimportclone(8)](../man8/vgimportclone.8.html),  [vgimportdevices(8)](../man8/vgimportdevices.8.html),  [vgmerge(8)](../man8/vgmerge.8.html),  [vgmknodes(8)](../man8/vgmknodes.8.html),  [vgreduce(8)](../man8/vgreduce.8.html),  [vgremove(8)](../man8/vgremove.8.html),  [vgrename(8)](../man8/vgrename.8.html),  [vgs(8)](../man8/vgs.8.html),  [vgscan(8)](../man8/vgscan.8.html),  [vgsplit(8)](../man8/vgsplit.8.html)

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
