---
{"title": "Systemd/FAQ", "url": "https://wiki.archlinux.org/title/Systemd/FAQ", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Systemd/FAQ

Related articles

-   [systemd](../../en/Systemd.html "Systemd")
-   [systemd/User](../../en/Systemd/User.html "Systemd/User")

## FAQ {#FAQ}

For an up-to-date list of known issues, look at the upstream [TODO](https://github.com/systemd/systemd/blob/main/TODO).

### Why do I get log messages on my console? {#Why_do_I_get_log_messages_on_my_console?}

You must set the kernel loglevel yourself. Historically, `/etc/rc.sysinit` did this for us and set [dmesg](../../en/Core_utilities.html#Essentials "Dmesg")\'s loglevel to `3`, which was a reasonably quiet loglevel. Either add `loglevel=3` or `quiet` to your [kernel parameters](../../en/Kernel_parameters.html "Kernel parameters").

### How do I change the default number of gettys? {#How_do_I_change_the_default_number_of_gettys?}

Currently, only one getty is launched by default. If you switch to another TTY, a getty will be launched there (socket-activation style). In other words, `Ctl+Alt+F2` will launch a new getty on tty2.

By default, the number of auto-activated gettys is capped at six. Thus `F7` through `F12` will not launch a getty.

If you want to change this behavior, then edit `/etc/systemd/logind.conf` and change the value of `NAutoVTs`. If you want all `F`*`x`* keys to start a getty, increase the value of `NAutoVTs` to `12`. If you are [forwarding journald to tty12](../../en/Systemd/Journal.html#Forward_journald_to_/dev/tty12 "Systemd/Journal"), increase the value of `NAutoVTs` to `11` (thus leaving tty12 free).

You can also pre-activate gettys which will be running from boot.

To add another pre-activated getty, [enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") and [start](../../en/Help:Reading.html#Control_of_systemd_units "Start") `getty@tty`*`X`*`.service`.

To remove a getty, [disable](../../en/Help:Reading.html#Control_of_systemd_units "Disable") and [stop](../../en/Help:Reading.html#Control_of_systemd_units "Stop") the relevant `getty@tty`*`X`*`.service`.

systemd does not use the `/etc/inittab` file.

### How do I get more verbose output during boot? {#How_do_I_get_more_verbose_output_during_boot?}

If you see no output at all in console after the initram message, this means you have the `quiet` parameter in your kernel line. It is best to remove it, at least the first time you boot with systemd, to see if everything is ok. Then, you will see a list `[ OK ]` in green or `[ FAILED ]` in red.

Any messages are logged to the system log and if you want to find out about the status of your system, use [systemctl](../../en/Systemd.html#Basic_systemctl_usage "Systemctl") or look at the boot/system log with [journalctl](../../en/Systemd/Journal.html "Journalctl").

### How do I avoid clearing the console after boot? {#How_do_I_avoid_clearing_the_console_after_boot?}

See [getty#Have boot messages stay on tty1](../../en/Getty.html#Have_boot_messages_stay_on_tty1 "Getty").

### What kernel options are required for systemd? {#What_kernel_options_are_required_for_systemd?}

Kernels prior to 3.0 are unsupported.

If you use a custom kernel, you will need to make sure that systemd\'s options are selected.

If you are compiling a new kernel for use with an installed version of systemd, the required and recommended options are listed in the systemd README file `/usr/share/doc/systemd/README`.

If you are preparing to install a new version of systemd and are running a custom kernel, the most recent version of the file can be found in the [systemd GitHub repository](https://github.com/systemd/systemd/blob/main/README).

### What other units does a unit depend on? {#What_other_units_does_a_unit_depend_on?}

For example, if you want to figure out which services a target like `multi-user.target` pulls in, use something like this:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ systemctl show -p "Wants" multi-user.target
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Wants=rc-local.service avahi-daemon.service rpcbind.service NetworkManager.service acpid.service dbus.service atd.service crond.service auditd.service ntpd.service udisks.service bluetooth.service org.cups.cupsd.service wpa_supplicant.service getty.target modem-manager.service portreserve.service abrtd.service yum-updatesd.service upowerd.service test-first.service pcscd.service rsyslog.service haldaemon.service remote-fs.target plymouth-quit.service systemd-update-utmp-runlevel.service sendmail.service lvm2-monitor.service cpuspeed.service udev-post.service mdmonitor.service iscsid.service livesys.service livesys-late.service irqbalance.service iscsi.service
```

Instead of `Wants` you might also try `WantedBy`, `Requires`, `RequiredBy`, `Conflicts`, `ConflictedBy`, `Before`, `After` for the respective types of dependencies and their inverse.

### My computer shuts down, but the power stays on {#My_computer_shuts_down,_but_the_power_stays_on}

Use `systemctl poweroff` instead of `systemctl halt`.

### How can I make a script start during the boot process? {#How_can_I_make_a_script_start_during_the_boot_process?}

Create a new file as `/etc/systemd/system/`*`myscript`*`.service` and add the following contents:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/myscript.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=My script
 
[Service]
ExecStart=/usr/bin/my-script
 
[Install]
WantedBy=multi-user.target
```

This example assumes you want your script to start up when the target multi-user is launched. Make sure the script is [executable](../../en/Help:Reading.html#Make_executable "Executable").

[Enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") *`myscript`*`.service` to start the service at boot.

**Note** In case you want to start a shell script, make sure you have `#!/bin/sh` in the first line of the script. Do **not** write something like `ExecStart=/bin/sh /path/to/script.sh` because that will not work.

### Service unit active state is \"active (exited)\" in green {#Service_unit_active_state_is_\"active_(exited)\"_in_green}

This is the expected behaviour for oneshot services that also use `RemainAfterExit=yes`. See [systemd.service(5) § OPTIONS](https://man.archlinux.org/man/systemd.service.5#OPTIONS) for more information. Some examples of oneshot services that behave this way are `systemd-user-sessions.services`, `nftables.service`, and `iptables.service`.

### Failure to enable unit due to preexisting symlink {#Failure_to_enable_unit_due_to_preexisting_symlink}

You may encounter the following error when attempting to [enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") a unit:

    Failed to enable unit: File /etc/systemd/system/symlink already exists and is a symlink to file.

This can occur when the *`symlink`* created by enabling a unit already exists in `/etc/systemd/system/`. This typically happens when switching from one display manager to another one (for instance [GDM](../../en/GDM.html "GDM") to [SDDM](../../en/SDDM.html "SDDM"), which can be enabled with `gdm.service` and `sddm.service`, respectively) and the corresponding symlink `/etc/systemd/system/display-manager.service` already exists.

To solve this problem, either first disable the relevant display manager before enabling the new one, or use the `-f`/`--force` option when enabling the new one to overwrite any existing conflicting symlinks (per [systemctl(1) § OPTIONS](https://man.archlinux.org/man/systemctl.1#OPTIONS)).
