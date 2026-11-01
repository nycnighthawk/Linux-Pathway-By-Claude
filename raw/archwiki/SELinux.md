---
{"title": "SELinux", "url": "https://wiki.archlinux.org/title/SELinux", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# SELinux

Related articles

-   [Security](../en/Security.html "Security")
-   [AppArmor](../en/AppArmor.html "AppArmor")
-   [TOMOYO Linux](../en/TOMOYO_Linux.html "TOMOYO Linux")

Security-Enhanced Linux (SELinux) is a Linux kernel feature set that provides a variety of security policies and mechanisms, including U.S. Department of Defense style [Mandatory Access Control](../en/Mandatory_Access_Control.html "Mandatory Access Control") (MAC), through the use of Linux Security Modules (LSM). It is not a Linux distribution, but a set of modifications that can be applied to the kernel.

Using SELinux requires three things: An SELinux enabled kernel, SELinux userspace tools and libraries, and SELinux policies (mostly based on the project\'s reference policy). Some common Linux programs will also need to be patched/compiled with SELinux features. It uses [extended attributes](../en/Extended_attributes.html "Extended attributes") to maintain the MAC metadata. To get an overview of its techniques and terminology, see the comprehensive [gentoo:SELinux/Quick introduction](https://wiki.gentoo.org/wiki/SELinux/Quick_introduction "gentoo:SELinux/Quick introduction") article.

## Current status in Arch Linux {#Current_status_in_Arch_Linux}

SELinux is not officially supported (see [\[1\]](https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/message/4LXUXQSFEPVLN7S2DDBIGVUS7L7ES5S2/)[\[2\]](https://lists.archlinux.org/archives/list/arch-general@lists.archlinux.org/message/VM72SI36VDX4PVUP4ZZEDIOSBVYTI7OG/)). The status of unofficial support is:

  --------------------------------------- ---------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                    Status                                                                                                                       Available at
  SELinux enabled kernel                  Implemented for all [officially supported kernels](../en/Kernel.html#Officially_supported_kernels "Kernel")                  Available in official repositories since [4.18.8](https://gitlab.archlinux.org/archlinux/packaging/packages/linux/-/commit/3a29867f8266250b10aa9fa8368abc4306fa9c4b).
  SELinux Userspace tools and libraries   Implemented in AUR: [https://aur.archlinux.org/packages/?O=0&K=selinux](https://aur.archlinux.org/packages/?O=0&K=selinux)   Work is done at [https://github.com/archlinuxhardened/selinux](https://github.com/archlinuxhardened/selinux)
  SELinux Policy                          Work in progress, using [Reference Policy](https://github.com/SELinuxProject/refpolicy) as upstream                          Upstream: [https://github.com/SELinuxProject/refpolicy](https://github.com/SELinuxProject/refpolicy) (since release 20170805 the policy has integrated support for systemd and single-/usr/bin directory)
  --------------------------------------- ---------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Summary of changes in AUR as compared to official core packages:

  --------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                          Status and comments
  linux, linux-lts, linux-zen, linux-hardened   Need to [set the lsm= kernel parameter](#Enable_SELinux_LSM)
  coreutils                                     Need a rebuild with `--with-selinux` flag to link with libselinux
  cronie                                        Need a rebuild with `--with-selinux` flag
  dbus                                          Need a rebuild with `--enable-libaudit` and `--enable-selinux` flags
  findutils                                     Need a rebuild with libselinux installed to enable SELinux-specific options
  iproute2                                      Need a rebuild with `--with-selinux` flag
  logrotate                                     Need a rebuild with `--with-selinux` flag
  openssh                                       Need a rebuild with `--with-selinux` flag
  pam                                           Need a rebuild with `--enable-selinux` flag for Linux-PAM ; Need a patch for pam_unix2, which only removes a function already implemented in a recent versions of libselinux
  pambase                                       Configuration changes to add pam_selinux.so to `/etc/pam.d/system-login`
  psmisc                                        Need a rebuild with `--with-selinux` flag
  shadow                                        Need a rebuild with `--with-selinux` flags
  sudo                                          Need a rebuild with `--with-selinux` flag
  systemd                                       Need a rebuild with `--enable-audit` and `--enable-selinux` flags
  util-linux                                    Need a rebuild with `--with-selinux` flag
  uutils-coreutils                              Need a rebuild with `USE=selinux` make flag to link with libselinux
  --------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All of the other SELinux-related packages may be included without changes nor risks.

## Concepts: Mandatory Access Controls {#Concepts:_Mandatory_Access_Controls}

**This article or section is a candidate for merging with [Security#Mandatory access control](../en/Security.html#Mandatory_access_control "Security").**

**Notes:** This is general conceptual explanatory content that should be elaborated in the main entry or the general encyclopedia entry [Wikipedia:Mandatory access control](https://en.wikipedia.org/wiki/Mandatory_access_control "wikipedia:Mandatory access control") (Discuss in [Talk:SELinux](../en/Talk:SELinux.html))

**Note** This section is meant for beginners. If you know what SELinux does and how it works, feel free to skip ahead to the installation.

Before you enable SELinux, it is worth understanding what it does. Simply and succinctly, SELinux enforces *Mandatory Access Controls (MACs)* on Linux. In contrast to SELinux, the traditional user/group/rwx permissions are a form of *Discretionary Access Control (DAC)*. MACs are different from DACs because security policy and its execution are completely separated.

An example would be the use of the *sudo* command. When DACs are enforced, sudo allows temporary privilege escalation to root, giving the process so spawned unrestricted systemwide access. However, when using MACs, if the security administrator deems the process to have access only to a certain set of files, then no matter what the kind of privilege escalation used, unless the security policy itself is changed, the process will remain constrained to simply that set of files. So if *sudo* is tried on a machine with SELinux running in order for a process to gain access to files its policy does not allow, it will fail.

Another set of examples are the traditional (-rwxr-xr-x) type permissions given to files. When under DAC, these are user-modifiable. However, under MAC, a security administrator can choose to freeze the permissions of a certain file by which it would become impossible for any user to change these permissions until the policy regarding that file is changed.

As you may imagine, this is particularly useful for processes which have the potential to be compromised, i.e. web servers and the like. If DACs are used, then there is a particularly good chance of havoc being wreaked by a compromised program which has access to privilege escalation.

For further information, visit [Wikipedia:Mandatory access control](https://en.wikipedia.org/wiki/Mandatory_access_control "wikipedia:Mandatory access control").

## Installing SELinux {#Installing_SELinux}

### Package description {#Package_description}

All SELinux related packages belong to the *selinux* group in the AUR. Before you manually install any of these, read [#Installation](#Installation) to see recommended options for a comprehensive installation.

#### SELinux aware system utilities {#SELinux_aware_system_utilities}

[coreutils-selinux](https://aur.archlinux.org/packages/coreutils-selinux/)^AUR^
:   Modified coreutils package compiled with SELinux support enabled. It replaces the [coreutils](https://archlinux.org/packages/?name=coreutils) package.

[cronie-selinux](https://aur.archlinux.org/packages/cronie-selinux/)^AUR^
:   Fedora fork of Vixie cron with SELinux enabled. It replaces the [cronie](https://archlinux.org/packages/?name=cronie) package.

[dbus-selinux](https://aur.archlinux.org/packages/dbus-selinux/)^AUR^
:   An SELinux aware version of [D-Bus](../en/D-Bus.html "D-Bus"). It replaces the [dbus](https://archlinux.org/packages/?name=dbus) package.

[findutils-selinux](https://aur.archlinux.org/packages/findutils-selinux/)^AUR^
:   Patched findutils package compiled with SELinux support to make searching of files with specified security context possible. It replaces the [findutils](https://archlinux.org/packages/?name=findutils) package.

[iproute2-selinux](https://aur.archlinux.org/packages/iproute2-selinux/)^AUR^
:   iproute2 package compiled with SELinux support; for example, it adds the `-Z` option to `ss`. It replaces the [iproute2](https://archlinux.org/packages/?name=iproute2) package.

[logrotate-selinux](https://aur.archlinux.org/packages/logrotate-selinux/)^AUR^
:   Logrotate package compiled with SELinux support. It replaces the [logrotate](https://archlinux.org/packages/?name=logrotate) package.

[openssh-selinux](https://aur.archlinux.org/packages/openssh-selinux/)^AUR^
:   [OpenSSH](../en/OpenSSH.html "OpenSSH") package compiled with SELinux support to set security context for user sessions. It replaces the [openssh](https://archlinux.org/packages/?name=openssh) package.

[pam-selinux](https://aur.archlinux.org/packages/pam-selinux/)^AUR^ and [pambase-selinux](https://aur.archlinux.org/packages/pambase-selinux/)^AUR^
:   PAM package with pam_selinux.so. and the underlying base package. They replace the [pam](https://archlinux.org/packages/?name=pam) and [pambase](https://archlinux.org/packages/?name=pambase) packages respectively.

[psmisc-selinux](https://aur.archlinux.org/packages/psmisc-selinux/)^AUR^
:   Psmisc package compiled with SELinux support; for example, it adds the `-Z` option to `killall`. It replaces the [psmisc](https://archlinux.org/packages/?name=psmisc) package.

[shadow-selinux](https://aur.archlinux.org/packages/shadow-selinux/)^AUR^
:   Shadow package compiled with SELinux support; contains a modified `/etc/pam.d/login` file to set correct security context for user after login. It replaces the [shadow](https://archlinux.org/packages/?name=shadow) package.

[sudo-selinux](https://aur.archlinux.org/packages/sudo-selinux/)^AUR^
:   Modified [sudo](../en/Sudo.html "Sudo") package compiled with SELinux support which sets the security context correctly. It replaces the [sudo](https://archlinux.org/packages/?name=sudo) package.

[systemd-selinux](https://aur.archlinux.org/packages/systemd-selinux/)^AUR^
:   An SELinux aware version of [systemd](../en/Systemd.html "Systemd"). It replaces the [systemd](https://archlinux.org/packages/?name=systemd) package.

[util-linux-selinux](https://aur.archlinux.org/packages/util-linux-selinux/)^AUR^
:   Modified util-linux package compiled with SELinux support enabled. It replaces the [util-linux](https://archlinux.org/packages/?name=util-linux) package.

#### SELinux userspace utilities {#SELinux_userspace_utilities}

[checkpolicy](https://aur.archlinux.org/packages/checkpolicy/)^AUR^
:   Tools to build SELinux policy

[mcstrans](https://aur.archlinux.org/packages/mcstrans/)^AUR^
:   Daemon which is used by libselinux to translate MCS labels

[libselinux](https://aur.archlinux.org/packages/libselinux/)^AUR^
:   Library for security-aware applications. Python bindings needed for *semanage* and *setools* now included.

[libsemanage](https://aur.archlinux.org/packages/libsemanage/)^AUR^
:   Library for policy management. Python bindings needed for *semanage* and *setools* now included.

[libsepol](https://aur.archlinux.org/packages/libsepol/)^AUR^
:   Library for binary policy manipulation.

[policycoreutils](https://aur.archlinux.org/packages/policycoreutils/)^AUR^
:   SELinux core utils such as newrole, setfiles, etc.

[restorecond](https://aur.archlinux.org/packages/restorecond/)^AUR^
:   Daemon which maintains the label of some files

[secilc](https://aur.archlinux.org/packages/secilc/)^AUR^
:   Compiler for SELinux policies written in CIL (Common Intermediate Language)

[selinux-dbus-config](https://aur.archlinux.org/packages/selinux-dbus-config/)^AUR^
:   DBus service which allows managing SELinux configuration

[selinux-gui](https://aur.archlinux.org/packages/selinux-gui/)^AUR^
:   SELinux GUI tools (system-config-selinux)

[selinux-python](https://aur.archlinux.org/packages/selinux-python/)^AUR^
:   SELinux python tools and libraries (semanage, sepolgen, sepolicy, etc.)

[selinux-sandbox](https://aur.archlinux.org/packages/selinux-sandbox/)^AUR^
:   Sandboxing tool for SELinux

[semodule-utils](https://aur.archlinux.org/packages/semodule-utils/)^AUR^
:   Tools to handle SELinux modules when building a policy

#### SELinux policy packages {#SELinux_policy_packages}

**This article or section needs expansion.**

**Reason:** It is unclear which packages are alternatives (Discuss in [Talk:SELinux#Refpolicy instructions are unclear / out-of-date](../en/Talk:SELinux.html#Refpolicy_instructions_are_unclear_/_out-of-date "Talk:SELinux"))

[selinux-refpolicy-src](https://aur.archlinux.org/packages/selinux-refpolicy-src/)^AUR^
:   Reference policy sources

[selinux-refpolicy-git](https://aur.archlinux.org/packages/selinux-refpolicy-git/)^AUR^
:   Reference policy git master ([https://github.com/SELinuxProject/refpolicy](https://github.com/SELinuxProject/refpolicy)) built with configuration specific for Arch Linux

[selinux-refpolicy-arch](https://aur.archlinux.org/packages/selinux-refpolicy-arch/)^AUR^
:   Precompiled modular Reference policy with headers and documentation but without sources. Development Arch Linux Refpolicy patches included, which fixes issues related to path labeling and systemd support. These patches are also sent to Reference Policy maintainers and their inclusion in [selinux-refpolicy-arch](https://aur.archlinux.org/packages/selinux-refpolicy-arch/)^AUR^ is mainly a way to perform updates between Refpolicy releases.

#### Other SELinux tools {#Other_SELinux_tools}

[setools](https://aur.archlinux.org/packages/setools/)^AUR^
:   CLI and GUI tools to manage SELinux

[selinux-alpm-hook](https://aur.archlinux.org/packages/selinux-alpm-hook/)^AUR^
:   pacman hook to label files accordingly to SELinux policy when installing and updating packages

### Installation {#Installation}

There are three methods to install the requisite SELinux packages.

#### Via binary package on GitHub {#Via_binary_package_on_GitHub}

All packages are available from the [selinux](../en/Unofficial_user_repositories.html#selinux "Unofficial user repositories") unofficial repository. the *base* package can be replaced with *base-selinux* during the `arch-bootstrap` stage of system installation.

**Warning** Currently this repository does not provide signed packages, meaning that the binary it downloads will not be verified by pacman. This presents a security risk; proceed with caution.

#### Via build script from GitHub {#Via_build_script_from_GitHub}

This repository also contains a script named `build_and_install_all.sh` which builds and installs (or updates) all packages in the needed order. Here is an example of a way this script can be used in a user shell to install all packages (with downloading the GPG keys which are used to verify the source tarballs of the package):

    $ git clone https://github.com/archlinuxhardened/selinux.git
    $ cd selinux
    $ ./recv_gpg_keys.sh
    $ ./build_and_install_all.sh

Of course, it is possible to modify the content of `build_and_install_all.sh` before running it, for example if you already have SELinux support in your kernel.

#### Via AUR {#Via_AUR}

-   First, install SELinux userspace tools and libraries, in this order (because of the dependencies): [libsepol](https://aur.archlinux.org/packages/libsepol/)^AUR^, [libselinux](https://aur.archlinux.org/packages/libselinux/)^AUR^, [checkpolicy](https://aur.archlinux.org/packages/checkpolicy/)^AUR^, [secilc](https://aur.archlinux.org/packages/secilc/)^AUR^, [setools](https://aur.archlinux.org/packages/setools/)^AUR^, [libsemanage](https://aur.archlinux.org/packages/libsemanage/)^AUR^, [semodule-utils](https://aur.archlinux.org/packages/semodule-utils/)^AUR^, [policycoreutils](https://aur.archlinux.org/packages/policycoreutils/)^AUR^, [selinux-python](https://aur.archlinux.org/packages/selinux-python/)^AUR^ (which depends on [python-ipy](https://aur.archlinux.org/packages/python-ipy/)^AUR^), [mcstrans](https://aur.archlinux.org/packages/mcstrans/)^AUR^ and [restorecond](https://aur.archlinux.org/packages/restorecond/)^AUR^.
-   Then install [pambase-selinux](https://aur.archlinux.org/packages/pambase-selinux/)^AUR^ and [pam-selinux](https://aur.archlinux.org/packages/pam-selinux/)^AUR^ and make sure you can login again after the installation completed, because files in `/etc/pam.d/` got removed and created when [pambase](https://archlinux.org/packages/?name=pambase) got replaced with [pambase-selinux](https://aur.archlinux.org/packages/pambase-selinux/)^AUR^.
-   Next you can recompile some core packages by installing: [coreutils-selinux](https://aur.archlinux.org/packages/coreutils-selinux/)^AUR^, [findutils-selinux](https://aur.archlinux.org/packages/findutils-selinux/)^AUR^, [iproute2-selinux](https://aur.archlinux.org/packages/iproute2-selinux/)^AUR^, [logrotate-selinux](https://aur.archlinux.org/packages/logrotate-selinux/)^AUR^, [openssh-selinux](https://aur.archlinux.org/packages/openssh-selinux/)^AUR^, [psmisc-selinux](https://aur.archlinux.org/packages/psmisc-selinux/)^AUR^, [shadow-selinux](https://aur.archlinux.org/packages/shadow-selinux/)^AUR^, [cronie-selinux](https://aur.archlinux.org/packages/cronie-selinux/)^AUR^
-   Next, backup your `/etc/sudoers` file if you are not using [its drop-in files](../en/Sudo.html#Configuration "Sudo"). Install [sudo-selinux](https://aur.archlinux.org/packages/sudo-selinux/)^AUR^ and restore your `/etc/sudoers` (it is overridden when this package is installed as a replacement of [sudo](https://archlinux.org/packages/?name=sudo)).
-   Next come util-linux and systemd. Because of a cyclic makedepends between these two packages which will not be fixed ([FS#39767](https://bugs.archlinux.org/task/39767)), you need to build the source package [systemd-selinux](https://aur.archlinux.org/packages/systemd-selinux/)^AUR^, install [systemd-libs-selinux](https://aur.archlinux.org/packages/systemd-libs-selinux/)^AUR^, build and install [util-linux-selinux](https://aur.archlinux.org/packages/util-linux-selinux/)^AUR^ (with [util-linux-libs-selinux](https://aur.archlinux.org/packages/util-linux-libs-selinux/)^AUR^) and rebuild and install [systemd-selinux](https://aur.archlinux.org/packages/systemd-selinux/)^AUR^.
-   Next, install [dbus-selinux](https://aur.archlinux.org/packages/dbus-selinux/)^AUR^.
-   Next, install [selinux-alpm-hook](https://aur.archlinux.org/packages/selinux-alpm-hook/)^AUR^ in order to run restorecon every time pacman installs a package.

After all these steps, you can install a SELinux kernel (like [linux](https://archlinux.org/packages/?name=linux)) and a policy (like [selinux-refpolicy-arch](https://aur.archlinux.org/packages/selinux-refpolicy-arch/)^AUR^ or [selinux-refpolicy-git](https://aur.archlinux.org/packages/selinux-refpolicy-git/)^AUR^).

### Enable SELinux LSM {#Enable_SELinux_LSM}

To enable SELinux as default security model on every boot, set the following [kernel parameter](../en/Kernel_parameter.html "Kernel parameter"):

    lsm=landlock,lockdown,yama,integrity,selinux,bpf

**Note** The `lsm=` kernel parameter sets the initialization order of Linux security modules. The kernel\'s configured `lsm=` value can be found with `zgrep CONFIG_LSM= /proc/config.gz` and the current value with `cat /sys/kernel/security/lsm`.

-   Make sure that `selinux` is the first \"major\" module in the list.[\[3\]](https://docs.kernel.org/admin-guide/LSM/index.html) Examples of valid values and their order can be found in [security/Kconfig](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/security/Kconfig).
-   `capability` should be omitted from `lsm=` as it will always get included automatically.

#### Custom kernel {#Custom_kernel}

When [compiling the kernel](../en/Kernel.html#Compilation "Kernels"), it is required to set at least the following options:

    CONFIG_SECURITY_SELINUX=y
    CONFIG_AUDIT=y

To enable the SELinux Linux security model by default and omit the need to set kernel parameters, additionally set the `CONFIG_LSM` option and specify `selinux` as the first \"major\" module in the list:

    CONFIG_LSM="landlock,lockdown,yama,integrity,selinux,bpf"

### Checking PAM {#Checking_PAM}

A correctly set-up [PAM](../en/PAM.html "PAM") is important to get the proper security context after login. Check for the presence of the following lines in `/etc/pam.d/system-login`:

    # pam_selinux.so close should be the first session rule
    session         required        pam_selinux.so close

    # pam_selinux.so open should only be followed by sessions to be executed in the user context
    session         required        pam_selinux.so open

### Installing a policy {#Installing_a_policy}

**Warning** The reference policy as given by [SELinuxProject](https://github.com/SELinuxProject/refpolicy/wiki) is not very good for Arch Linux. Most people submitting patches to improve the policy use an other distribution (Debian, Gentoo, RHEL, etc.), therefore the compatibility with Arch Linux packages is not perfect (for example the policy may not support the most recent features of a program).

Policies are the mainstay of SELinux. They are what govern its behaviour. The only policy currently available in the AUR is the Reference Policy. In order to install it, you should use the source files, which may be got from the package [selinux-refpolicy-src](https://aur.archlinux.org/packages/selinux-refpolicy-src/)^AUR^ or by downloading the latest release on [https://github.com/SELinuxProject/refpolicy/wiki/DownloadRelease#current-release](https://github.com/SELinuxProject/refpolicy/wiki/DownloadRelease#current-release). When using the AUR package, navigate to `/etc/selinux/refpolicy/src/policy` and run the following commands:

    # make bare
    # make conf
    # make install

to install the reference policy as it is. Those who know how to write SELinux policies can tweak them to their heart\'s content before running the commands written above. The command takes a while to do its job and taxes one core of your system completely, so do not worry. Just sit back and let the command run for as long as it takes.

To load the reference policy run:

    # make load

Then, make the file `/etc/selinux/config` with the following contents (Only works if you used the defaults as mentioned above. If you decided to change the name of the policy, you need to tweak the file):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/selinux/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#       enforcing - SELinux security policy is enforced.
#                   Set this value once you know for sure that SELinux is configured the way you like it and that your system is ready for deployment
#       permissive - SELinux prints warnings instead of enforcing.
#                    Use this to customise your SELinux policies and booleans prior to deployment. Recommended during policy development.
#       disabled - No SELinux policy is loaded.
#                  This is not a recommended setting, for it may cause problems with file labelling
SELINUX=permissive
# SELINUXTYPE= takes the name of SELinux policy to
# be used. Current options are:
#       refpolicy (vanilla reference policy)
#       <custompolicy> - Substitute <custompolicy> with the name of any custom policy you choose to load
SELINUXTYPE=refpolicy
```

Now, you may reboot. After rebooting, run:

    # restorecon -r /

to label your filesystem.

Now, make a file `requiredmod.te` with the contents:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
requiredmod.te
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
module requiredmod 1.0;

require {
        type devpts_t;
        type kernel_t;
        type device_t;
        type var_run_t;
        type udev_t;
        type hugetlbfs_t;
        type udev_tbl_t;
        type tmpfs_t;
        class sock_file write;
        class unix_stream_socket { read write ioctl };
        class capability2 block_suspend;
        class dir { write add_name };
        class filesystem associate;
}

#============= devpts_t ==============
allow devpts_t device_t:filesystem associate;

#============= hugetlbfs_t ==============
allow hugetlbfs_t device_t:filesystem associate;

#============= kernel_t ==============
allow kernel_t self:capability2 block_suspend;

#============= tmpfs_t ==============
allow tmpfs_t device_t:filesystem associate;

#============= udev_t ==============
allow udev_t kernel_t:unix_stream_socket { read write ioctl };
allow udev_t udev_tbl_t:dir { write add_name };
allow udev_t var_run_t:sock_file write;
```

and run the following commands:

    # checkmodule -m -o requiredmod.mod requiredmod.te
    # semodule_package -o requiredmod.pp -m requiredmod.mod
    # semodule -i requiredmod.pp

This is required to remove a few messages from `/var/log/audit/audit.log` which are a nuisance to deal with in the reference policy. This is an ugly hack and it should be made very clear that the policy so installed simply patches the reference policy in order to hide the effects of incorrect labelling.

### Testing in a Vagrant virtual machine {#Testing_in_a_Vagrant_virtual_machine}

It is possible to use [Vagrant](../en/Vagrant.html "Vagrant") to provision a virtual Arch Linux machine with SELinux configured. This is a convenient way to test an Arch Linux system running SELinux without modifying a current system. Here are commands which can be used to achieve this:

    $ git clone https://github.com/archlinuxhardened/selinux.git
    $ cd selinux/_vagrant
    $ vagrant up
    $ vagrant ssh

## Post-installation steps {#Post-installation_steps}

You can check that SELinux is working with `sestatus`. You should get something like:

    SELinux status:                 enabled
    SELinuxfs mount:                /sys/fs/selinux
    SELinux root directory:         /etc/selinux
    Loaded policy name:             refpolicy
    Current mode:                   permissive
    Mode from config file:          permissive
    Policy MLS status:              disabled
    Policy deny_unknown status:     allowed
    Max kernel policy version:      28

To maintain correct context, you can [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") `restorecond.service`.

To switch to enforcing mode without rebooting, you can use:

    # echo 1 > /sys/fs/selinux/enforce

### Swapfiles {#Swapfiles}

If you have a swap file instead of a swap partition, issue the following commands in order to set the appropriate security context:

    # semanage fcontext -a -t swapfile_t "/path/to/swapfile"
    # restorecon /path/to/swapfile

## Working with SELinux {#Working_with_SELinux}

SELinux defines security using a different mechanism than traditional Unix access controls. The best way to understand it is by example. For example, the SELinux security context of the apache homepage looks like the following:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ls -lZ /var/www/html/index.html
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
-rw-r--r--  username username system_u:object_r:httpd_sys_content_t /var/www/html/index.html
```

The first three and the last columns should be familiar to any (Arch) Linux user. The fourth column is new and has the format:

    user:role:type[:level]

To explain:

1.  **User:** The SELinux user identity. This can be associated to one or more roles that the SELinux user is allowed to use.
2.  **Role:** The SELinux role. This can be associated to one or more types the SELinux user is allowed to access.
3.  **Type:** When a type is associated with a process, it defines what processes (or domains) the SELinux user (the subject) can access. When a type is associated with an object, it defines what access permissions the SELinux user has to that object.
4.  **Level:** This optional field can also be know as a range and is only present if the policy supports MCS or MLS.

This is important in case you wish to understand how to build your own policies, for these are the basic building blocks of SELinux. However, for most purposes, there is no need to, for the reference policy is sufficiently mature. However, if you are a power user or someone with very specific needs, then it might be ideal for you to learn how to make your own SELinux policies.

[This](https://web.archive.org/web/20210310014356/http://www.fosteringlinux.com/tag/selinux/) is a great series of articles for someone seeking to understand how to work with SELinux.

## Troubleshooting {#Troubleshooting}

The place to look for SELinux errors is the [systemd journal](../en/Systemd_journal.html "Systemd journal"). In order to see SELinux messages related to the label `system_u:system_r:policykit_t:s0` (for example), you would need to run:

    # journalctl _SELINUX_CONTEXT=system_u:system_r:policykit_t:s0

### Useful tools {#Useful_tools}

There are some tools/commands that can greatly help with SELinux.

restorecon
:   Restores the context of a file/directory (or recursively with `-R`) based on any policy rules

chcon
:   Change the context on a specific file

### Reporting issues {#Reporting_issues}

Please report issues on GitHub: [https://github.com/archlinuxhardened/selinux/issues](https://github.com/archlinuxhardened/selinux/issues)

## See also {#See_also}

-   [Security Enhanced Linux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux "wikipedia:Security-Enhanced Linux")
-   [Gentoo:SELinux](https://wiki.gentoo.org/wiki/SELinux "gentoo:SELinux")
-   [Fedora:SELinux](https://fedoraproject.org/wiki/SELinux "fedora:SELinux")
-   [NSA\'s Official SELinux Homepage](https://web.archive.org/web/20201022103915/https://www.nsa.gov/what-we-do/research/selinux/)
-   [SELinux Project Homepage](https://github.com/SELinuxProject)
    -   [Reference Policy Homepage](https://github.com/SELinuxProject/refpolicy/wiki)
    -   [SETools Homepage](https://github.com/SELinuxProject/setools/wiki)
-   [ArchLinux, SELinux and You (archived)](https://web.archive.org/web/20140816115906/http://jamesthebard.net/archlinux-selinux-and-you-a-trip-down-the-rabbit-hole/)
