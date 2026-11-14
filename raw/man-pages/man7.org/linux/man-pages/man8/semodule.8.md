---
{"title": "semodule(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/semodule.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semodule(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [MODES](#MODES) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SEMODULE(8)              System Manager's Manual              SEMODULE(8)

## [](#NAME)NAME

           semodule - Manage SELinux policy modules.

## [](#SYNOPSIS)SYNOPSIS

           semodule [option]... MODE...

## [](#DESCRIPTION)DESCRIPTION

           semodule is the tool used to manage SELinux policy modules,
           including installing, upgrading, listing and removing modules.
           semodule may also be used to force a rebuild of policy from the
           module store and/or to force a reload of policy without performing
           any other transaction.  semodule acts on module packages created
           by semodule_package.  Conventionally, these files have a .pp
           suffix (policy package), although this is not mandated in any way.

## [](#MODES)MODES

           -R, --reload
                  force a reload of policy

           -B, --build
                  force a rebuild of policy (also reloads unless -n is used)

           --refresh
                  Like --build, but reuses existing linked policy if no
                  changes to module files are detected (by comparing with
                  checksum from the last transaction).  One can use this
                  instead of -B to ensure that any changes to the module
                  store done by an external tool (e.g. a package manager) are
                  applied, while automatically skipping the module re-linking
                  if there are no module changes.

           -D, --disable_dontaudit
                  Temporarily remove dontaudits from policy.  Reverts
                  whenever policy is rebuilt

           -i,--install=MODULE_PKG
                  install/replace a module package

           -u,--upgrade=MODULE_PKG
                  deprecated, alias for --install

           -b,--base=MODULE_PKG
                  deprecated, alias for --install

           -r,--remove=MODULE_NAME
                  remove existing module at desired priority (defaults to -X
                  400)

           -l[KIND],--list-modules[=KIND]
                  display list of installed modules (other than base)

           KIND:

           standard
                  list highest priority, enabled, non-base modules

           full   list all modules

           -X,--priority=PRIORITY
                  set priority for following operations (1-999)

           -e,--enable=MODULE_NAME
                  enable module

           -d,--disable=MODULE_NAME
                  disable module

           -E,--extract=MODULE_PKG
                  Extract a module from the store as an HLL or CIL file to
                  the current directory.  A module is extracted as HLL by
                  default. The name of the module written is <module-
                  name>.<lang_ext>

## [](#OPTIONS)OPTIONS

           -s,--store
                  name of the store to operate on

           -n,--noreload,-N
                  do not reload policy after commit

           -h,--help
                  prints help message and quit

           -P,--preserve_tunables
                  Preserve tunables in policy

           -C,--ignore-module-cache
                  Recompile CIL modules built from HLL files

           -g,--config=PATH
                  use an alternate path for the semanage config

           -p,--path
                  Use an alternate path for the policy root

           -S,--store-path
                  Use an alternate path for the policy store root

           -v,--verbose
                  be verbose

           -c,--cil
                  Extract module as a CIL file. This only affects the
                  --extract option and only modules listed in --extract after
                  this option.

           -H,--hll
                  Extract module as an HLL file. This only affects the
                  --extract option and only modules listed in --extract after
                  this option.

           -m,--checksum
                  Add SHA256 checksum of modules to the list output.

## [](#EXAMPLE)EXAMPLE

           # Install or replace a base policy package.
           $ semodule -b base.pp
           # Install or replace a non-base policy package.
           $ semodule -i httpd.pp
           # Install or replace all non-base modules in the current directory.
           # This syntax can be used with -i/u/r/E, but no other option can be entered after the module names
           $ semodule -i *.pp
           # Install or replace all modules in the current directory.
           $ ls *.pp | grep -Ev "base.pp|enableaudit.pp" | xargs /usr/sbin/semodule -b base.pp -i
           # List non-base modules.
           $ semodule -l
           # List all modules including priorities
           $ semodule -lfull
           # Remove a module at priority 100
           $ semodule -X 100 -r wireshark
           # Turn on all AVC Messages for which SELinux currently is "dontaudit"ing.
           $ semodule -DB
           # Turn "dontaudit" rules back on.
           $ semodule -B
           # Disable a module (all instances of given module across priorities will be disabled).
           $ semodule -d alsa
           # Install a module at a specific priority.
           $ semodule -X 100 -i alsa.pp
           # Set an alternate path for the policy root
           $ semodule -B -p "/tmp"
           # Set an alternate path for the policy store root
           $ semodule -B -S "/tmp/var/lib/selinux"
           # Write the HLL version of puppet and the CIL version of wireshark
           # modules at priority 400 to the current working directory
           $ semodule -X 400 --hll -E puppet --cil -E wireshark
           # Check whether a module in "localmodule.pp" file is same as installed module "localmodule"
           $ /usr/libexec/selinux/hll/pp localmodule.pp | sha256sum
           $ semodule -l -m | grep localmodule
           # Translate binary module file into CIL (useful for debugging installation errors)
           $ /usr/libexec/selinux/hll/pp alsa.pp > alsa.cil

## [](#SEE_ALSO)SEE ALSO

           checkmodule(8), semodule_package(8)

## [](#AUTHORS)AUTHORS

           This manual page was written by Dan Walsh <dwalsh@redhat.com>.
           The program was written by Karl MacMillan <kmacmillan@tresys.com>, Joshua Brindle <jbrindle@tresys.com>, Jason Tang <jtang@tresys.com>

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Security Enhanced Linux          Nov 2005                     SEMODULE(8)

------------------------------------------------------------------------

Pages that refer to this page: [selabel_file(5)](../man5/selabel_file.5.html),  [checkmodule(8)](../man8/checkmodule.8.html),  [genhomedircon(8)](../man8/genhomedircon.8.html),  [semanage-module(8)](../man8/semanage-module.8.html)

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
