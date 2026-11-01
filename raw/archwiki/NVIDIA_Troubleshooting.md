---
{"title": "NVIDIA/Troubleshooting", "url": "https://wiki.archlinux.org/title/NVIDIA/Troubleshooting", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# NVIDIA/Troubleshooting

## Failure to start {#Failure_to_start}

### System will not boot after driver was installed {#System_will_not_boot_after_driver_was_installed}

If after installing the [NVIDIA](../../en/NVIDIA.html "NVIDIA") driver your system becomes stuck before reaching the display manager, try to [disable kernel mode setting](../../en/Kernel_mode_setting.html#Disabling_modesetting "Kernel mode setting").

### Xorg fails to load or Red Screen of Death {#Xorg_fails_to_load_or_Red_Screen_of_Death}

If you get a red screen and use GRUB, disable the GRUB framebuffer by editing `/etc/default/grub` and uncomment `GRUB_TERMINAL_OUTPUT=console`. For more information see [GRUB/Tips and tricks#Disable framebuffer](../../en/GRUB/Tips_and_tricks.html#Disable_framebuffer "GRUB/Tips and tricks").

### Black screen at X startup / Machine poweroff at X shutdown {#Black_screen_at_X_startup_/_Machine_poweroff_at_X_shutdown}

If you have installed an update of NVIDIA and your screen stays black after launching Xorg, or if shutting down Xorg causes a machine poweroff, try the below workarounds:

-   Prepend `xrandr --auto` to your [xinitrc](../../en/Xinit.html#xinitrc "Xinitrc")
-   Use the `rcutree.gp_init_delay=1` [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter").
-   You can also try to add the `nvidia` module directly to your [mkinitcpio.conf](../../en/Mkinitcpio.html#Configuration "Mkinitcpio.conf").

### Screen(s) found, but none have a usable configuration {#Screen(s)_found,_but_none_have_a_usable_configuration}

Sometimes the NVIDIA driver and X have trouble finding the active screen. If your graphics card has multiple outputs try plugging your monitor into the other ones. On a laptop it may be because your graphics card has VGA/TV out. `Xorg.0.log` will provide more info.

Another thing to try is adding an invalid `Option "ConnectedMonitor"` to `Section "Device"` to force Xorg throw an error and show you how to correct it. See [the documentation](https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/xconfigoptions.html#ConnectedMonitor) for more information about the ConnectedMonitor setting.

After re-running X, see `Xorg.0.log` to get valid CRT-x,DFP-x,TV-x values.

`nvidia-xconfig --query-gpu-info` could be helpful.

### X fails with \"Failing initialization of X screen\" {#X_fails_with_\"Failing_initialization_of_X_screen\"}

If `/var/log/Xorg.0.log` says the X server failed to initialize screen:

    (EE) NVIDIA(G0): GPU screens are not yet supported by the NVIDIA driver
    (EE) NVIDIA(G0): Failing initialization of X screen

and *nvidia-smi* says `No running processes found`, then the solution is to first update to the latest [nvidia-utils](https://archlinux.org/packages/?name=nvidia-utils), and then copy the file `10-nvidia-drm-outputclass.conf` (located in `/usr/share/X11/xorg.conf.d/`) to `/etc/X11/xorg.conf.d/`. Afterwards, edit the copied file and add the line `Option "PrimaryGPU" "yes"`. Finally, restart the computer. The problem should now be gone.

### Xorg fails during boot, but otherwise starts fine {#Xorg_fails_during_boot,_but_otherwise_starts_fine}

On very fast booting systems, [systemd](../../en/Systemd.html "Systemd") may attempt to start the display manager before the NVIDIA driver has fully initialized. You will see a message like the following in your logs only when Xorg runs during boot:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/var/log/Xorg.0.log
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[     1.807] (EE) NVIDIA(0): Failed to initialize the NVIDIA kernel module. Please see the
[     1.807] (EE) NVIDIA(0):     system's kernel log for additional error messages and
[     1.808] (EE) NVIDIA(0):     consult the NVIDIA README for details.
[     1.808] (EE) NVIDIA(0):  *** Aborting ***
```

In this case you will need to establish an ordering dependency from the display manager to the DRI device. First create device units for DRI devices by creating a new udev rules file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/udev/rules.d/99-systemd-dri-devices.rules
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
ACTION=="add", KERNEL=="card*", SUBSYSTEM=="drm", TAG+="systemd"
```

Then create dependencies from the display manager to the device(s):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/display-manager.service.d/10-wait-for-dri-devices.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Wants=dev-dri-card0.device
After=dev-dri-card0.device
```

If you have additional cards needed for the desktop then list them in Wants and After seperated by spaces.

### Black screen on systems with integrated GPU {#Black_screen_on_systems_with_integrated_GPU}

If you have a system with an integrated GPU (e.g. Intel HD 4000, VIA VX820 Chrome 9 or AMD Cezanne) and have installed the [nvidia-580xx-dkms](https://aur.archlinux.org/packages/nvidia-580xx-dkms/)^AUR^ or earlier package, you may experience a black screen on boot, when changing virtual terminal, or when exiting an X session. This may be caused by a conflict between the graphics modules. This is solved by blacklisting the relevant GPU modules. Create the file `/etc/modprobe.d/blacklist.conf` and prevent the relevant modules from loading on boot:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/blacklist.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
install i915 /usr/bin/false
install intel_agp /usr/bin/false
install viafb /usr/bin/false
install radeon /usr/bin/false
install amdgpu /usr/bin/false
```

### X fails with \"no screens found\" when using multiple GPUs {#X_fails_with_\"no_screens_found\"_when_using_multiple_GPUs}

In situations where you might have multiple GPUs on a system and X fails to start with:

    [ 76.633] (EE) No devices detected.
    [ 76.633] Fatal server error:
    [ 76.633] no screens found

then you need to add your discrete card\'s BusID to your X configuration. This can happen on systems with an Intel CPU and an integrated GPU or if you have more than one NVIDIA card connected. Find your BusID:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# lspci -d ::03xx
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
00:02.0 VGA compatible controller: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor Graphics Controller (rev 09)
01:00.0 VGA compatible controller: NVIDIA Corporation GK107 [GeForce GTX 650] (rev a1)
08:00.0 3D controller: NVIDIA Corporation GM108GLM [Quadro K620M / Quadro M500M] (rev a2)
```

Then you fix it by adding it to the card\'s Device section in your X configuration. The following illustrates how the section should look (replace the values with your own configuration):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/X11/xorg.conf.d/10-nvidia.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Section "Device"
    Identifier     "Device0"
    Driver         "nvidia"
    VendorName     "NVIDIA Corporation"
    BusID          "PCI:1:0:0"
EndSection
```

**Note** BusID formatting is important!

In the example above `01:00.0` is stripped to be written as `1:0:0`. However, some conversions can be more complicated. `lspci` output is in hex format, but in configuration files the BusID\'s are in decimal format! This means that in cases where the BusID is greater than 9 you will need to convert it to decimal! For instance: `5e:00.0` from `lspci` becomes `PCI:94:0:0`.

### Modprobe Error: \"Could not insert \'nvidia\': No such device\" on linux \>=4.8 {#Modprobe_Error:_\"Could_not_insert_'nvidia':_No_such_device\"_on_linux_>=4.8}

With linux 4.8, one can get the following errors when trying to use the discrete card:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# modprobe nvidia -vv
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
modprobe: INFO: custom logging function 0x409c10 registered
modprobe: INFO: Failed to insert module '/lib/modules/4.8.6-1-ARCH/extramodules/nvidia.ko.gz': No such device
modprobe: ERROR: could not insert 'nvidia': No such device
modprobe: INFO: context 0x24481e0 released
insmod /lib/modules/4.8.6-1-ARCH/extramodules/nvidia.ko.gz
```

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# dmesg
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
NVRM: The NVIDIA GPU 0000:01:00.0 (PCI ID: 10de:139b)
NVRM: installed in this system is not supported by the 370.28
NVRM: NVIDIA Linux driver release.  Please see 'Appendix
NVRM: A - Supported NVIDIA GPU Products' in this release's
NVRM: README, available on the Linux driver download page
NVRM: at www.nvidia.com.
...
```

This problem is caused by bad commits pertaining to PCIe power management in the Linux Kernel (as documented in [this NVIDIA DevTalk thread](https://devtalk.nvidia.com/default/topic/971733/-370-28-with-kernel-4-8-on-gt-2015-machines-driver-claims-card-not-supported-if-nvidia-is-not-primary-card/)).

The workaround is to add `pcie_port_pm=off` to your [kernel parameters](../../en/Kernel_parameters.html "Kernel parameters"). Note that this disables PCIe power management for all devices.

### System does not return from suspend {#System_does_not_return_from_suspend}

What you see in the log:

    kernel: nvidia-modeset: ERROR: GPU:0: Failed detecting connected display devices
    kernel: nvidia-modeset: ERROR: GPU:0: Failed detecting connected display devices
    kernel: nvidia-modeset: WARNING: GPU:0: Failure processing EDID for display device DELL U2412M (DP-0).
    kernel: nvidia-modeset: WARNING: GPU:0: Unable to read EDID for display device DELL U2412M (DP-0)
    kernel: nvidia-modeset: ERROR: GPU:0: Failure reading maximum pixel clock value for display device DELL U2412M (DP-0).

A possible solution based on [\[1\]](https://forums.developer.nvidia.com/t/solution-for-nvidia-sleep-wake-issue-in-linux/110911):

Run this command to get the *`version`* string:

    # strings /sys/firmware/acpi/tables/DSDT | grep -i 'windows ' | sort | tail -1

Add the `acpi_osi=! "acpi_osi=`*`version`*`"` [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter") to your [boot loader](../../en/Boot_loader.html "Boot loader") configuration.

Another possible cause to the issue could be the use of the [nvidia-open](https://archlinux.org/packages/?name=nvidia-open) package, as described here:

-   [https://bbs.archlinux.org/viewtopic.php?pid=2047692](https://bbs.archlinux.org/viewtopic.php?pid=2047692)
-   [https://github.com/NVIDIA/open-gpu-kernel-modules/issues/450](https://github.com/NVIDIA/open-gpu-kernel-modules/issues/450)
-   [https://github.com/NVIDIA/open-gpu-kernel-modules/issues/223](https://github.com/NVIDIA/open-gpu-kernel-modules/issues/223)
-   [https://github.com/NVIDIA/open-gpu-kernel-modules/issues/94](https://github.com/NVIDIA/open-gpu-kernel-modules/issues/94)

### Black screen returning from suspend {#Black_screen_returning_from_suspend}

If experiencing black screen issues and logs containing:

    archlinux kernel: NVRM: GPU at PCI:0000:08:00: GPU-926ecdb0-adb1-6ee9-2fad-52e7214c5011
    archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='<unknown>', name=<unknown>, Graphi>
    archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='<unknown>', name=<unknown>, Graphi>
    archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='<unknown>', name=<unknown>, Graphi>
    archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='<unknown>', name=<unknown>, Graphi>
    archlinux kernel: NVRM: Xid (PCI:0000:08:00): 13, pid='<unknown>', name=<unknown>, Graphi>

You need to enable the NVIDIA suspend, hibernate and sleep services as explained in [NVIDIA/Tips and tricks#Preserve video memory after suspend](../../en/NVIDIA/Tips_and_tricks.html#Preserve_video_memory_after_suspend "NVIDIA/Tips and tricks").

### One or more monitors not working in multi-monitor setup in Xorg {#One_or_more_monitors_not_working_in_multi-monitor_setup_in_Xorg}

If one or more of your monitors is not outputting anything in Xorg and is showing up as \"Disabled\" in the `nvidia-settings` control panel, then your current Xorg configuration may be incompatible. The proprietary NVIDIA driver should not require a X configuration to simply function. See [NVIDIA#Xorg configuration](../../en/NVIDIA.html#Xorg_configuration "NVIDIA").

Simply move or rename the `/etc/X11/xorg.conf` file and any configuration files in `xorg.conf.d` pertaining to the NVIDIA driver. Only files ending in `.conf` will be read by Xorg.

    $ mv /etc/X11/xorg.conf /etc/X11/xorg.conf.old

After disabling the old NVIDIA Xorg configuration you may want to use `nvidia-xconfig` to generate a new NVIDIA Xorg configuration suited to your hardware. This shouldn\'t however be necessary to get the driver to work.

    $ nvidia-xconfig

**Note** `nvidia-xconfig` does create a backup file as `/etc/X11/xorg.conf.backup`, but this file may be overwritten by running `nvidia-xconfig` multiple times.

## Crashes and hangs {#Crashes_and_hangs}

### Crashing in general {#Crashing_in_general}

-   Try [disabling the GSP firmware](#GSP_firmware).
-   Try disabling `RenderAccel` in xorg.conf.
-   If Xorg outputs an error about `"conflicting memory type"` or `"failed to allocate primary buffer: out of memory"`, or crashes with a \"Signal 11\" while using nvidia-96xx drivers, add `nopat` to your [kernel parameters](../../en/Kernel_parameters.html "Kernel parameters").
-   If the NVIDIA compiler complains about different versions of GCC between the current one and the one used for compiling the kernel, add in `/etc/profile`:

&nbsp;

    export IGNORE_CC_MISMATCH=1

-   If fullscreen applications are freezing or crashing, try enabling `Display Compositing` and `Direct fullscreen rendering` options in your desktop environment\'s settings.

### Bad support of mesh shaders {#Bad_support_of_mesh_shaders}

This bug is present only for new games that depend on them, like Final Fantasy VII Rebirth. This is reflected in the absence of environments when using NVIDIA GPUs even with latest beta drivers. [\[2\]](https://github.com/ValveSoftware/Proton/issues/8408)

However, [pyroveil](https://github.com/ValveSoftware/Proton/issues/8408#issuecomment-2657340142) allows you to get around the problem with SPIR-V, while waiting for a fix from NVIDIA.

You need to compile and install the tool by following [the tutorial on GitHub](https://github.com/HansKristian-Work/pyroveil#pyroveil), then run the game with the `PYROVEIL=1` and `PYROVEIL_CONFIG=`*`/path/to/pyroveil`*`/hacks/`*`ffvii-rebirth-nvidia`*`/pyroveil.json` [environment variables](../../en/Environment_variables.html "Environment variables").

### Visual glitches, hangs and errors in OpenGL applications {#Visual_glitches,_hangs_and_errors_in_OpenGL_applications}

If you are using a recent CPU (Intel Sandy Bridge (2011) and later or AMD Zen (2017) and later) it has a micro operations cache. Using a micro op cache can lead to problems with NVIDIA\'s driver in OpenGL due to Cache Aliasing [\[3\]](https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/knownissues.html). You usually are able to disable the micro op cache in your systems BIOS, but this comes at the cost of performance [\[4\]](https://chipsandcheese.com/2021/07/03/how-zen-2s-op-cache-affects-performance/). Disabling the micro op cache also helps with the most severe graphical glitches in Xwayland applications, although it does not solve the problem fully [\[5\]](https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/wayland-issues.html).

### Kernel panic when updating and/or rebooting the system {#Kernel_panic_when_updating_and/or_rebooting_the_system}

This is a known bug that is present in the NVIDIA 550 series drivers. [\[6\]](https://forums.developer.nvidia.com/t/series-550-freezes-laptop/284772) As of yet the cause is unknown however it only appears to affect laptops. See [BBS#293400](https://bbs.archlinux.org/viewtopic.php?id=293400&p=3) for more details.

To workaround this issue, switch to [nvidia-open-dkms](https://archlinux.org/packages/?name=nvidia-open-dkms) if supported by the hardware, otherwise use [nvidia-535xx-dkms](https://aur.archlinux.org/packages/nvidia-535xx-dkms/)^AUR^ instead.

### GSP firmware {#GSP_firmware}

The use of the [GSP firmware](https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/gsp.html), enabled by default since version 555 of the NVIDIA driver released in June 2024, is known to cause [a range of issues](https://bbs.archlinux.org/viewtopic.php?pid=2181317) including [Vulkan](../../en/Vulkan.html "Vulkan") failures and system crashes.

To disable it, use the `NVreg_EnableGpuFirmware=0` [module parameter](../../en/Module_parameter.html "Module parameter") for the `nvidia` kernel module. This only works with the proprietary NVIDIA driver: see [NVIDIA#Installation](../../en/NVIDIA.html#Installation "NVIDIA") if switching from the open source driver.

Do not forget to [regenerate the initramfs](../../en/Regenerate_the_initramfs.html "Regenerate the initramfs") if needed. To have this new kernel module option take effect, reboot.

### Crashes related to VRR and TTY-switching {#Crashes_related_to_VRR_and_TTY-switching}

If the driver crashes while switching between a desktop environment and TTY\'s and the journal contains:

    archlinux kernel: [drm:nv_drm_atomic_commit [nvidia_drm]] *ERROR* [nvidia-drm] [GPU ID [...]] Flip event timeout
    archlinux kernel: nvidia-modeset: ERROR: GPU:0: Idling display engine timed out: [...]

Try disabling the monitor\'s [variable refresh rate](../../en/Variable_refresh_rate.html "Variable refresh rate") (VRR) function via it\'s OSD.

Another workaround is to hide the driver\'s VRR (G-Sync / FreeSync) capability from the display subsystem, preventing any application or compositor from enabling VRR: set [Kernel parameters](../../en/Kernel_parameters.html "Kernel parameters") to `nvidia_modeset.conceal_vrr_caps=1`, which enforces a fixed refresh rate.

### Xid 79, GPU has fallen off the bus {#Xid_79,_GPU_has_fallen_off_the_bus}

If you find this crash in the [journal](../../en/Systemd/Journal.html "Journal"), it may be due to different reasons, including a bad power supply, cables or PCI connection problems.

However, it is also reported as an [NVIDIA driver issue](https://github.com/NVIDIA/open-gpu-kernel-modules/issues/1151), which mentions a [work-around](https://github.com/NVIDIA/open-gpu-kernel-modules/issues/1151#issuecomment-5502412431) of limiting the memory clock.

First, get the available memory clocks by executing:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ nvidia-smi -q -d SUPPORTED_CLOCKS | grep Memory
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
        Memory                                         : 9501 MHz
        Memory                                         : 9251 MHz
        Memory                                         : 5001 MHz
        Memory                                         : 810 MHz
        Memory                                         : 405 MHz
```

Then, set the minimum clock to the smallest allowed clock frequency, and the maximum clock one below the maximum value, specified as a *`min`*`,`*`max`* pair, using the `--lock-memory-clocks` option (or `-lmc`), e.g.:

    # nvidia-smi --lock-memory-clocks 405,9251

This defines a range of allowed clock frequencies, which stops forcing the device to always use the highest. Setting the upper bound of the range to the maximum value also works, but increases power draw even when card is not used.

**Note** According to the [documentation](https://docs.nvidia.com/deploy/nvidia-smi/index.html), the `--lock-memory-clocks` option does not work on devices based on NVIDIA Hopper architectures. If that\'s your case, use the `--lock-memory-clocks-deferred` (or `-lmcd`) option instead, which takes in a single desired value instead of a range.

## Visual issues {#Visual_issues}

### Avoid screen tearing on Xorg {#Avoid_screen_tearing_on_Xorg}

**Note**

-   This has been reported to reduce the performance of some OpenGL applications and may produce issues in WebGL. It also drastically increases the time the driver needs to clock down after load ([NVIDIA Support Thread](https://forums.developer.nvidia.com/t/if-you-have-gpu-clock-boost-problems-please-try-gl-experimentalperfstrategy-1/71762)).
-   `ForceFullCompositionPipeline` is known [to break some games](https://github.com/ValveSoftware/Proton/issues/6869) using Vulkan under Proton with NVIDIA driver 535.
-   `ForceCompositionPipeline` is known to cause some fullscreen applications to immediately freeze, making the system unresponsive until tabbing out. One workaround is to run the program in [Gamescope](../../en/Gamescope.html "Gamescope") as a borderless window (`-b`) and leaving at least one other thing on the screen (which may be the taskbar or any graphical application).

The NVIDIA driver conditionally applies a [composition pipeline](https://www.reddit.com/r/linux_gaming/comments/6voivr/comment/dm1uz2j/) to prepare the image for display. This is not to be confused with a [composite manager](../../en/Composite_manager.html "Composite manager"), which takes over window presentation (and can also mitigate screen tearing, via VSync). By default, the composition pipeline is only applied if the current screen transformations require it. The pipeline uses the GPU\'s specialized display engine if possible, then the more general graphics engine. There are a couple of options to control this:

-   `ForceCompositionPipeline` forces usage of the pipeline (further discussed in [#Multi-monitor](#Multi-monitor)).
-   `ForceFullCompositionPipeline` forces usage of the pipeline, and forces it to all be done with the graphics engine.

Tearing on Xorg can be avoided by setting `ForceFullCompositionPipeline=On`. To test whether this option will work, run:

    $ nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"

Or click on the *Advanced* button that is available on the *X Server Display Configuration* menu option. Select either *Force Composition Pipeline* or *Force Full Composition Pipeline* and click on *Apply*.

In order to make the change permanent, it must be added to the `"Screen"` section of the [Xorg](../../en/Xorg.html "Xorg") configuration file. When making this change, `TripleBuffering` should be enabled and `AllowIndirectGLXProtocol` should be disabled in the driver configuration as well. See example configuration below:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/X11/xorg.conf.d/20-nvidia.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Section "Device"
        Identifier "NVIDIA Card"
        Driver     "nvidia"
        VendorName "NVIDIA Corporation"
        BoardName  "GeForce GTX 1050 Ti"
EndSection

Section "Screen"
    Identifier     "Screen0"
    Device         "Device0"
    Monitor        "Monitor0"
    Option         "ForceFullCompositionPipeline" "on"
    Option         "AllowIndirectGLXProtocol" "off"
    Option         "TripleBuffer" "on"
EndSection
```

If you do not have a Xorg configuration file, you can create one for your present hardware using `nvidia-xconfig` (see [NVIDIA#Automatic configuration](../../en/NVIDIA.html#Automatic_configuration "NVIDIA")) and move it from `/etc/X11/xorg.conf` to the preferred location `/etc/X11/xorg.conf.d/20-nvidia.conf`.

**Note** Many of the configuration options produced in `20-nvidia.conf` by using `nvidia-xconfig` are set automatically by the driver and are not needed. To only use this file for enabling composition pipeline, only the section `"Screen"` containing lines with values for `Identifier` and `Option` is necessary. Other sections may be removed from this file.

#### Multi-monitor {#Multi-monitor}

For multi-monitor setup you will need to specify `ForceCompositionPipeline=On` for each display. For example:

    $ nvidia-settings --assign CurrentMetaMode="DP-2: nvidia-auto-select +0+0 {ForceCompositionPipeline=On}, DP-4: nvidia-auto-select +3840+0 {ForceCompositionPipeline=On}"

Without doing this, the `nvidia-settings` command will disable your secondary display.

The above line is for two 3840x2160 monitors connected to DP-2 and DP-4. You will need to read the correct `CurrentMetaMode` by exporting `xorg.conf` and append `ForceCompositionPipeline` to each of your displays. Setting `ForceCompositionPipeline` only affects the targeted display.

You can get the current screen names and offsets using `--query`:

    $ nvidia-settings --query CurrentMetaMode

**Tip** In multi-monitor setups that use different models, the monitors may have slightly different refresh rates. If V-Sync is enabled by the driver it will sync to only one of these refresh rates which can cause the appearance of screen tearing on incorrectly synced monitors. With that in mind, prefer syncing to your primarily used monitor, which is configurable either in `~/.nvidia-settings-rc` as `0/XVideoSyncToDisplayID=` or by installing [nvidia-settings](https://archlinux.org/packages/?name=nvidia-settings) and using the graphical configuration options.

### Screen corruption after resuming from suspend or hibernation {#Screen_corruption_after_resuming_from_suspend_or_hibernation}

This also applies if an external monitor does not wake up after suspend or hibernation.

See [NVIDIA/Tips and tricks#Preserve video memory after suspend](../../en/NVIDIA/Tips_and_tricks.html#Preserve_video_memory_after_suspend "NVIDIA/Tips and tricks")

A corruption after suspend bug when using [GDM](../../en/GDM.html "GDM") service was solved as of driver version 515.43.04 [\[7\]](https://forums.developer.nvidia.com/t/corrupted-graphics-upon-resume-gnome-41-x-org-495-44-driver/194565/18).

### Corrupted screen: \"Six screens\" Problem {#Corrupted_screen:_\"Six_screens\"_Problem}

For some users, using GeForce GT 100M\'s, the screen gets corrupted after X starts, divided into 6 sections with a resolution limited to 640x480. The same problem has been reported with Quadro 2000 and hi-res displays.

To solve this problem, enable the Validation Mode `NoTotalSizeCheck` in section `Device`:

    Section "Device"
     ...
     Option "ModeValidation" "NoTotalSizeCheck"
     ...
    EndSection

### Invisible text and icons with nvidia-470 {#Invisible_text_and_icons_with_nvidia-470}

An update of GTK4 brought an issue for users relying on the nvidia-470 driver for legacy cards. After the update text and icons randomly disappear and re-appear only after hovering with the mouse over the windows.[\[8\]](https://forums.developer.nvidia.com/t/multiple-apps-do-not-invalidate-repaint-screen-correctly-with-geforce-gt-730-and-v470-driver-on-ubuntu-24-04/291106/2)

A workaround is to set the renderer:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/environment
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
GSK_RENDERER=vulkan
```

### Fix graphical corruption in GNOME Shell when resuming from sleep {#Fix_graphical_corruption_in_GNOME_Shell_when_resuming_from_sleep}

If you are facing strange fonts and/or having weird graphical glitches in [GNOME Shell](../../en/GNOME_Shell.html "GNOME Shell") when resuming from sleep, try setting the following [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter") to enable power management:

    nvidia.NVreg_DynamicPowerManagement=0x02

More info: [https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/dynamicpowermanagement.html](https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/dynamicpowermanagement.html)

### System freeze when the display powers off or on resume {#System_freeze_when_the_display_powers_off_or_on_resume}

If the system freezes or crashes right after the desktop environment turns off the display (DPMS) or when resuming from suspend, and dmesg/journal shows a GSP timeout like:

    NVRM: _kgspLogXid119: ********************************* GSP Timeout **********************************
    NVRM: Xid (PCI:0000:01:00): 119, Timeout after 6s of waiting for RPC response from GPU0 GSP! Expected function 76 (GSP_RM_CONTROL) sequence 1321 

the GPU may be dropping to an unstable low clock state during these power transitions.

Workaround: lock a higher minimum GPU/memory clock with nvidia-smi.

Prerequisites:

[Enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable")/[start](../../en/Help:Reading.html#Control_of_systemd_units "Start") the `nvidia-persistenced.service`.

Find supported clock values (use these to pick valid min/max pairs):

    nvidia-smi -q -d SUPPORTED_CLOCKS
    nvidia-smi -q -d CLOCK

Set minimum clocks (example values; adjust to your GPU's max supported clocks):

    nvidia-smi -lgc 800,2100
    nvidia-smi -lmc 800,10000

Test DPMS and suspend/resume to see if the issue is resolved. To revert:

    nvidia-smi -rgc
    nvidia-smi -rmc

For permanent configuration (systemd), create a unit such as `nvidia-clocks.service`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/nvidia-clocks.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=Set NVIDIA GPU minimum clocks to avoid  GSP timeouts
Requires=nvidia-persistenced.service
After=nvidia-persistenced.service 

[Service]
Type=oneshot
ExecStart=/usr/bin/nvidia-smi -lgc 500,2100
ExecStart=/usr/bin/nvidia-smi -lmc 500,10000
RemainAfterExit=yes 

[Install]
WantedBy=multi-user.target
```

You can adjust the minimum clock so they are lower than the 800 mentioned earlier to lower idle power consumption; just be aware that setting them to low will cause the issue to occur again.

Then [enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable")/[start](../../en/Help:Reading.html#Control_of_systemd_units "Start") `nvidia-clocks.service`.

## Performance issues {#Performance_issues}

### Bad performance after installing a new driver version {#Bad_performance_after_installing_a_new_driver_version}

**The factual accuracy of this article or section is disputed.**

**Reason:** We should be trying to find the root cause (read dmesg, dkms logs etc.), not mindlessly downgrading the driver. (Discuss in [Talk:NVIDIA/Troubleshooting](../../en/Talk:NVIDIA/Troubleshooting.html))

If FPS have dropped in comparison with older drivers, check if direct rendering is enabled (`glxinfo` is included in [mesa-utils](https://archlinux.org/packages/?name=mesa-utils)):

    $ glxinfo | grep direct

If the command prints:

    direct rendering: No

A possible solution could be to regress to the previously installed driver version and rebooting afterwards.

### Extreme lag on Xorg {#Extreme_lag_on_Xorg}

**The factual accuracy of this article or section is disputed.**

**Reason:** According to [an NVIDIA developer](https://gitlab.gnome.org/GNOME/mutter/-/issues/2233#note_1538392) this issue is not specific to GNOME and the rest of the comments on the issue do not mention multi-monitor setups. (Discuss in [Talk:NVIDIA/Troubleshooting](../../en/Talk:NVIDIA/Troubleshooting.html))

A common issue with Mutter is that [animations, video playback and gaming cause extreme desktop lag on Xorg](https://gitlab.gnome.org/GNOME/mutter/-/issues/2233).

See [NVIDIA/Tips and tricks#Preserve video memory after suspend](../../en/NVIDIA/Tips_and_tricks.html#Preserve_video_memory_after_suspend "NVIDIA/Tips and tricks").

This should resolve this issue, however if it did not, you are most likely out of luck. One way you can remedy this issue is by adding these options:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/environment
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
CLUTTER_DEFAULT_FPS=YOUR_MAIN_DISPLAY_REFRESHRATE
__GL_SYNC_DISPLAY_DEVICE=YOUR_MAIN_DISPLAY_OUTPUT_NAME
```

turning *Sync to VBlank* and *Allow flipping* off within NVIDIA Settings, and configuring NVIDIA Settings to launch on startup using the flag `--load-config-only`. This will still result in a laggy desktop behavior, in particular on an eventual second (or third) monitor, but it should be much better.

### CPU spikes with 400 series cards {#CPU_spikes_with_400_series_cards}

If you are experiencing intermittent CPU spikes with a 400 series card, it may be caused by PowerMizer constantly changing the GPU\'s clock frequency. Switching PowerMizer\'s setting from Adaptive to Performance, add the following to the `Device` section of your Xorg configuration:

If you have a desktop:

     Option "RegistryDwords" "PowerMizerEnable=0x1; PerfLevelSrc=0x2222; PowerMizerDefaultAC=0x1"

If you have a laptop:

     Option "RegistryDwords" "PowerMizerEnable=0x1; PerfLevelSrc=0x3322; PowerMizerDefaultAC=0x1"

## Other issues {#Other_issues}

### Vulkan error on applications start {#Vulkan_error_on_applications_start}

**The factual accuracy of this article or section is disputed.**

**Reason:** Need confirmation by other users (Discuss in [Talk:NVIDIA/Troubleshooting](../../en/Talk:NVIDIA/Troubleshooting.html))

On executing an application that require Vulkan acceleration, if you get this error

    Vulkan call failed: -4

try to delete the `~/.nv` or `~/.cache/nvidia` directory.

### No audio over HDMI {#No_audio_over_HDMI}

Sometimes NVIDIA HDMI audio devices are not shown when you do

    $ aplay -l

On some new machines, the audio chip on the NVIDIA GPU is disabled at boot. Read more on [NVIDIA\'s website](https://devtalk.nvidia.com/default/topic/1024022/linux/gtx-1060-no-audio-over-hdmi-only-hda-intel-detected-azalia/?offset=4) and a [forum post](https://bbs.archlinux.org/viewtopic.php?id=230125).

You need to reload the NVIDIA device with audio enabled. In order to do that make sure that your GPU is on (in case of laptops/Bumblebee) and that you are not running X on it, because it is going to reset:

    # setpci -s 01:00.0 0x488.l=0x2000000:0x2000000
    # rmmod nvidia-drm nvidia-modeset nvidia
    # echo 1 > /sys/bus/pci/devices/0000:01:00.0/remove
    # echo 1 > /sys/bus/pci/devices/0000:00:01.0/rescan
    # modprobe nvidia-drm
    # xinit -- -retro

If you are running your TTY on NVIDIA, put the lines in a script so you do not end up with no screen.

### Backlight is not turning off in some occasions {#Backlight_is_not_turning_off_in_some_occasions}

By default, DPMS should turn off backlight with the timeouts set or by running xset. However, probably due to a bug in the proprietary NVIDIA drivers the result is a blank screen with no powersaving whatsoever. To workaround it, until the bug has been fixed you can use the `vbetool` as root.

Install the [vbetool](https://archlinux.org/packages/?name=vbetool) package.

Turn off your screen on demand and then by pressing a random key backlight turns on again:

    vbetool dpms off && read -n1; vbetool dpms on

Alternatively, xrandr is able to disable and re-enable monitor outputs without requiring root.

    xrandr --output DP-1 --off; read -n1; xrandr --output DP-1 --auto

#### HardDPMS {#HardDPMS}

**This article or section needs expansion.**

**Reason:** Add references for the \"user reports\". (Discuss in [Talk:NVIDIA/Troubleshooting](../../en/Talk:NVIDIA/Troubleshooting.html))

Proprietary driver 415 includes a new feature called [HardDPMS](https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/xconfigoptions.html#HardDPMS). This is reported by some users to solve the issues with suspending monitors connected over DisplayPort. It is enabled by default since 440.26. If you are using an older driver, the `HardDPMS` option can be set in the `Device` or `Screen` sections. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/X11/xorg.conf.d/20-nvidia.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Section "Device"
    ...
    Option         "HardDPMS" "true"
    ...
EndSection

Section "Screen"
    ...
    Option         "HardDPMS" "true"
    ...
EndSection
```

`HardDPMS` will trigger on screensaver settings like `BlankTime`. The following `ServerFlags` will set your monitor(s) to suspend after 10 minutes of inactivity:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/X11/xorg.conf.d/20-nvidia.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Section "ServerFlags"
    Option     "BlankTime" "10"
EndSection
```

### xrandr BadMatch {#xrandr_BadMatch}

If you are trying to configure a WQHD monitor such as DELL U2515H using [xrandr](../../en/Xrandr.html "Xrandr") and `xrandr --addmode` gives you the error `X Error of failed request: BadMatch`, it might be because the proprietary NVIDIA driver clips the pixel clock maximum frequency of HDMI output to 225 MHz or lower. To set the monitor to maximum resolution you have to install [nouveau](../../en/Nouveau.html "Nouveau") drivers. You can force nouveau to use a specific pixel clock frequency by setting `nouveau.hdmimhz=297` (or `330`) in your [Kernel parameters](../../en/Kernel_parameters.html "Kernel parameters").

Alternatively, it may be that your monitor\'s EDID is incorrect. See [#Override EDID](#Override_EDID).

Another reason could be that by default current NVIDIA drivers will only allow modes explicitly reported by EDID, but sometimes refresh rates and/or resolutions are desired which are not reported by the monitor (although the EDID information is correct; it is just that current NVIDIA drivers are too restrictive).

If this happens, you may want to add an option to `xorg.conf` to allow non-EDID modes:

    Section "Device"
        Identifier     "Device0"
        Driver         "nvidia"
        VendorName     "NVIDIA Corporation"
    ...
        Option         "ModeValidation" "AllowNonEdidModes"
    ...
    EndSection

This can be set per-output. See [README - Appendix B. X Config Options](https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/xconfigoptions.html#ModeValidation) for more information.

### Override EDID {#Override_EDID}

See [Kernel mode setting#Forcing modes and EDID](../../en/Kernel_mode_setting.html#Forcing_modes_and_EDID "Kernel mode setting"), [Xrandr#Troubleshooting](../../en/Xrandr.html#Troubleshooting "Xrandr") and [Qnix QX2710#Fixing X11 with Nvidia](../../en/Qnix_QX2710.html#Fixing_X11_with_Nvidia "Qnix QX2710").

### Overclocking with nvidia-settings GUI not working {#Overclocking_with_nvidia-settings_GUI_not_working}

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../../en/Help:Style.html "Help:Style") for reference.**

**Reason:** Duplication, vague \"not working\" (Discuss in [Talk:NVIDIA/Troubleshooting](../../en/Talk:NVIDIA/Troubleshooting.html))

Workaround is to use nvidia-settings CLI to query and set certain variables after enabling overclocking (as explained in [NVIDIA/Tips and tricks#Enabling overclocking in nvidia-settings](../../en/NVIDIA/Tips_and_tricks.html#Enabling_overclocking_in_nvidia-settings "NVIDIA/Tips and tricks"), see [nvidia-settings(1)](https://man.archlinux.org/man/nvidia-settings.1) for more information).

Example to query all variables:

     nvidia-settings -q all

Example to set PowerMizerMode to prefer performance mode:

     nvidia-settings -a [gpu:0]/GPUPowerMizerMode=1

Example to set fan speed to fixed 21%:

    nvidia-settings -a [gpu:0]/GPUFanControlState=1 -a [fan:0]/GPUTargetFanSpeed=21

Example to set multiple variables at once (overclock GPU by 50MHz, overclock video memory by 50MHz, increase GPU voltage by 100mV):

     nvidia-settings -a GPUGraphicsClockOffsetAllPerformanceLevels=50 -a GPUMemoryTransferRateOffsetAllPerformanceLevels=50 -a GPUOverVoltageOffset=100

### Overclocking not working with Unknown Error {#Overclocking_not_working_with_Unknown_Error}

If you are running Xorg as a non-root user and trying to overclock your NVIDIA GPU, you will get an error similar to this one:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ nvidia-settings -a "[gpu:0]/GPUGraphicsClockOffset[3]=10"
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
ERROR: Error assigning value 10 to attribute 'GPUGraphicsClockOffset' (trinity-zero:1[gpu:0]) as specified in assignment
        '[gpu:0]/GPUGraphicsClockOffset[3]=10' (Unknown Error).
```

To avoid this issue, Xorg has to be run as the root user. See [Xorg#Rootless Xorg](../../en/Xorg.html#Rootless_Xorg "Xorg") for details.

### Power draw {#Power_draw}

**This article or section needs expansion.**

**Reason:** What is the point of this section? (Discuss in [Talk:NVIDIA/Troubleshooting](../../en/Talk:NVIDIA/Troubleshooting.html))

Check driver usage:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# lsof /dev/nvidia*
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
kwin_wayl  867      user   17u   CHR   195,0      0t0  418 /dev/nvidia
kwin_wayl  867      user   18u   CHR   195,0      0t0  418 /dev/nvidiactl
```

If power save is configured on the kernel module:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ grep . /sys/bus/pci/devices/0000:01:00.0/power/*
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/sys/bus/pci/devices/0000:01:00.0/power/control:auto
/sys/bus/pci/devices/0000:01:00.0/power/runtime_active_time:445933
/sys/bus/pci/devices/0000:01:00.0/power/runtime_status:active
/sys/bus/pci/devices/0000:01:00.0/power/runtime_suspended_time:1266
/sys/bus/pci/devices/0000:01:00.0/power/wakeup:disabled
```

    # rmmod nvidia_drm

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ grep . /sys/bus/pci/devices/0000:01:00.0/power/*
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/sys/bus/pci/devices/0000:01:00.0/power/control:auto
/sys/bus/pci/devices/0000:01:00.0/power/runtime_active_time:461023
/sys/bus/pci/devices/0000:01:00.0/power/runtime_status:suspended
/sys/bus/pci/devices/0000:01:00.0/power/runtime_suspended_time:1064192
/sys/bus/pci/devices/0000:01:00.0/power/wakeup:disabled
```

### Test software GL {#Test_software_GL}

The binary NVIDIA driver will not adhere to the Mesa environment variable `LIBGL_ALWAYS_SOFTWARE=1` but you can direct libglvnd and EGL to use Mesa by setting the following [environment variables](../../en/Environment_variables.html "Environment variables"):

    __GLX_VENDOR_LIBRARY_NAME=mesa
    __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json

which will result in the Mesa libgl being used for software GLX and EGL rendering, and thus may be useful to test whether a bug is related to the NVIDIA GL library.

### Refresh-rate limited to 120Hz {#Refresh-rate_limited_to_120Hz}

Newer versions of the driver (after 550xx) [seem to](https://bbs.archlinux.org/viewtopic.php?id=302969) waste bandwidth on 8bpc outputs, likely pushing the signal above specification limits and the result is a failure to apply modes with higher refresh rates that otherwise would be within the specification of the output. Add `nvidia-modeset.hdmi_deepcolor=0` to the [kernel parameters](../../en/Kernel_parameters.html "Kernel parameters") or set the option via [modprobe](../../en/Kernel_module.html "Modprobe"). Notice that deep color will however be required for HDR monitors.

### Wrong color space on 60Hz on Wayland with HDMI {#Wrong_color_space_on_60Hz_on_Wayland_with_HDMI}

In some cases (like using a HDMI cable with a 1660 Super graphics card with 60Hz), the driver seems to wrongly assume the color space for the output. This leads to the colors looking darker than normal. Because of there being no easy way to explicitly set the color space on Wayland, as a workaround you can add `nvidia-modeset.debug_force_color_space=2` to the [kernel parameters](../../en/Kernel_parameters.html "Kernel parameters") or set the option via [modprobe](../../en/Kernel_module.html "Modprobe").
