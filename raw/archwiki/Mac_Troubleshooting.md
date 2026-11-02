---
{"title": "Mac/Troubleshooting", "url": "https://wiki.archlinux.org/title/Mac/Troubleshooting", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Mac/Troubleshooting

Related articles

-   [Mac](../../en/Mac.html "Mac")
-   [General troubleshooting](../../en/General_troubleshooting.html "General troubleshooting")
-   [Laptop/Apple](../../en/Laptop/Apple.html "Laptop/Apple")

This page contains troubleshooting solutions for Apple Macs. Most models have their own section in [Laptop/Apple](../../en/Laptop/Apple.html "Laptop/Apple") for even more specific issues.

## Video {#Video}

Different Mac models have different graphic cards. To see which graphics card you have type:

    $ lspci -nnd ::03xx

-   If it returns a string containing `Intel`, read [Intel graphics](../../en/Intel_graphics.html "Intel graphics").
-   If it returns `NVIDIA`, read [NVIDIA](../../en/NVIDIA.html "NVIDIA").
-   If it returns two lines, with both `NVIDIA` and `Intel`, your Mac has dual graphics. See [MacBookPro10,x#Graphics](../../en/MacBookPro10,x.html#Graphics "MacBookPro10,x") for an example of one such setup that might apply in other cases.

**Warning** Despite lots of confusion in online forums, the dual graphics on Mac are [not](https://arstechnica.com/gadgets/2010/04/inside-apples-automatic-gpu-switching/) [Optimus](../../en/NVIDIA_Optimus.html "Optimus")-based, and treating them as such will break your graphics. See instead [MacBookPro10,x#Switching to/from GPUs with gpu-switch](../../en/MacBookPro10,x.html#Switching_to/from_GPUs_with_gpu-switch "MacBookPro10,x") or your laptop\'s specific article for instructions on setting up graphics switching.

-   Otherwise if it returns `ATI` or `AMD`, read [ATI](../../en/ATI.html "ATI") or [AMDGPU](../../en/AMDGPU.html "AMDGPU").

### NVIDIA {#NVIDIA}

If you boot in EFI mode and NVIDIA binary drivers are working only in BIOS mode (e.g. you get black screen on EFI boot), try the approach described on [Ask Ubuntu](https://askubuntu.com/a/613573).

For the backlight to work properly you may need the [nvidia-bl-dkms](https://aur.archlinux.org/packages/nvidia-bl-dkms/)^AUR^ package. If backlight control does not work afterwards, you should [blacklist](../../en/Kernel_module.html#Blacklisting "Blacklist") the `apple_bl` kernel module. If backlight control does not work even this way, try setting `options nvidia_bl max_level=0x1ffff shift=11` in `/etc/modprobe.d/nvidia_bl.conf`.

Alternatively, you can choose to use the [pommed-light](https://aur.archlinux.org/packages/pommed-light/)^AUR^ package. If you do so, you may wish to change the step settings in `/etc/pommed.conf.mactel` to something around 5000-10000 depending on how many levels of brightness you desire (the max brightness is around 80000).

If the brightness does not function correctly through pommed, make sure you have installed the [nvidia-bl-dkms](https://aur.archlinux.org/packages/nvidia-bl-dkms/)^AUR^ package and insert

    $ find . -name "*" -exec sed -i 's/mbp_backlight/nvidia_backlight/' '{}' \;

into the second line of the pommed PKGBUILD build() function and rebuild the package. See the following [forum post](https://bbs.archlinux.org/viewtopic.php?id=105091) for details.

Another possible solution is:

    $ find . -name "*" -exec sed -i 's/nvidia_backlight/apple_backlight/' '{}' \;

Alternatively, run *nvidia-settings*, edit `/etc/X11/xorg.conf` and add this line into the `Device` section:

    Option "RegistryDwords" "EnableBrightnessControl=1"

Save, reboot and check if the backlight control works. See Ubuntu\'s [Wiki page for the MacBookPro5,5](https://help.ubuntu.com/community/MacBookPro5-5/Precise#LCD) for details.

## Touchpad {#Touchpad}

The touchpad should have basic functionality by default. A true multitouch driver which behaves very similarly to native macOS is included in the [xf86-input-mtrack-git](https://aur.archlinux.org/packages/xf86-input-mtrack-git/)^AUR^ package. Configuration options are documented in the [readme](https://github.com/p2rkw/xf86-input-mtrack/blob/master/README.md).

The following mtrack options work well on a MacBook7,1:

    Option "Thumbsize" "50"
    Option "ScrollDistance" "100"

Probably, you also need to add:

    MatchDevicePath "/dev/input/event10"

To disable tap-to-click (that is, to press down to click) by default, add the following to your mtrack configuration section

    Option "TapButton1" "0"  
    Option "TapButton2" "0"
    Option "TapButton3" "0"

### Natural scrolling {#Natural_scrolling}

To configure natural two finger scrolling similar to [macOS](https://support.apple.com/en-us/HT204895), refer to [Touchpad Synaptics#Natural scrolling](../../en/Touchpad_Synaptics.html#Natural_scrolling "Touchpad Synaptics").

If you are using [xf86-input-mtrack-git](https://aur.archlinux.org/packages/xf86-input-mtrack-git/)^AUR^, you can simply swap the scroll up and scroll down buttons (along with the scroll left and scroll right):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/X11/xorg.conf.d/10-mtrack.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Option "ScrollUpButton" "5"
Option "ScrollDownButton" "4"
Option "ScrollLeftButton" "7"
Option "ScrollRightButton" "6"
```

**Tip** For users looking to add more of macOS\'s multitouch gestures to Arch, [xSwipe](https://github.com/iberianpig/xSwipe) for [Synaptics](../../en/Touchpad_Synaptics.html "Synaptics") or [fusuma](https://github.com/iberianpig/fusuma) for [libinput](../../en/Libinput.html "Libinput") provide these functions.

### Older MacBook models {#Older_MacBook_models}

On older MacBook models (pre-multitouch, e.g. MacBook2,1), the touchpad will not function properly until you [install](../../en/Help:Reading.html#Installation_of_packages "Install") [xf86-input-synaptics](https://archlinux.org/packages/?name=xf86-input-synaptics). See [Touchpad Synaptics](../../en/Touchpad_Synaptics.html "Touchpad Synaptics") for details.

**Tip** [gpointing-device-settings](https://aur.archlinux.org/packages/gpointing-device-settings/)^AUR^ provides a simple GUI for configuring Synaptics.

## Keyboard {#Keyboard}

Mac keyboards work by default. For swapping `Fn` keys with `F`*`x`* keys see [Apple Keyboard](../../en/Apple_Keyboard.html "Apple Keyboard").

Map them with [xbindkeys](../../en/Xbindkeys.html "Xbindkeys") or through [desktop environment](../../en/Desktop_environment.html "Desktop environment") preferences. Alternatively, [install](../../en/Help:Reading.html#Installation_of_packages "Install") the [pommed-light](https://aur.archlinux.org/packages/pommed-light/)^AUR^ package.

Edit the `/etc/pommed.conf` according to your hardware, building it from `/etc/pommed.conf.mac` or `/etc/pommed.conf.ppc` example files.

Note that you can also run it without a configuration file, the defaults may work for you. Then [enable/start](../../en/Help:Reading.html#Control_of_systemd_units "Enable/start") `pommed.service`.

**Note** See the [Xorg input hotplugging](../../en/Xorg_input_hotplugging.html "Xorg input hotplugging") page for other configuration information.

### Keyboard backlight {#Keyboard_backlight}

The keyboard backlight is controlled by `/sys/class/leds/smc::kbd_backlight`. Write the desired value to `brightness` in that directory. See [Keyboard backlight](../../en/Keyboard_backlight.html "Keyboard backlight") for detailed information. Common choices for backlight control are [brightnessctl](https://archlinux.org/packages/?name=brightnessctl) and [light](https://aur.archlinux.org/packages/light/)^AUR^.

**Ensuring the keyboard backlight is on when entering the LUKS decryption password**

This can be done via [initcpio hooks](../../en/Mkinitcpio.html#HOOKS "Mkinitcpio"). First, [create](../../en/Help:Reading.html#Append,_add,_create,_edit "Create") an [executable](../../en/Help:Reading.html#Make_executable "Executable") install script:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/initcpio/install/mac_kb_backlight
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/usr/bin/env bash

build() {
  add_module applesmc
  add_runscript
}
```

Next, create an executable hook:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/initcpio/hooks/mac_kb_backlight
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/usr/bin/env bash

run_hook() {
  if [ -f "/sys/class/leds/smc::kbd_backlight/brightness" ]; then
    echo 100 > "/sys/class/leds/smc::kbd_backlight/brightness"
  fi
}
```

Finally, add this custom hook to the `HOOKS` array in `/etc/mkinitcpio.conf`, and ensure it is placed before the `encrypt` hook:

    HOOKS=(... mac_kb_backlight encrypt ...)

Remember to [regenerate the initramfs](../../en/Regenerate_the_initramfs.html "Regenerate the initramfs") images after these steps to include the custom script.

## Wi-Fi {#Wi-Fi}

Different Mac models have different wireless cards.

Check what card you have:

    # lspci -nnd ::0280

-   If you have an Atheros card, all should work out-of-the-box.
-   If you have a Broadcom card, follow [Broadcom wireless#Installation](../../en/Broadcom_wireless.html#Installation "Broadcom wireless").
-   5.0 and 6.0 generation Macs may have a BCM43xx, follow [Broadcom wireless#broadcom-wl](../../en/Broadcom_wireless.html#broadcom-wl "Broadcom wireless").
    -   If you have the correct Broadcom DKMS driver (i.e. [broadcom-wl-dkms](https://archlinux.org/packages/?name=broadcom-wl-dkms)) installed and your Wi-Fi card is still not being recognized, try rebuilding the driver (See [Dynamic Kernel Module Support](../../en/Dynamic_Kernel_Module_Support.html "Dynamic Kernel Module Support")).

**Note**

-   If your connection frequently drops, you may have to turn off Wi-Fi power management.
-   Eduroam or similar may crash your network manager. Simply delaying the connection after login should do the trick.

## Fan Control {#Fan_Control}

[macfand-git](https://aur.archlinux.org/packages/macfand-git/)^AUR^ is a fan control daemon that supports most Intel Macs, its configuration file is located at `/etc/macfand.conf`.

[mbpfan-git](https://aur.archlinux.org/packages/mbpfan-git/)^AUR^ is available for MacBook Pro users.

## Power management {#Power_management}

[TLP](../../en/TLP.html "TLP") is a very simple set of scripts that will maximize your battery duration. A MacBook Air 2013 with TLP provides about 11 hours of light usage with just TLP installed. All the usual [power management](../../en/Power_management.html "Power management") recommendations apply as well.

### Disabling Thunderbolt {#Disabling_Thunderbolt}

Linux still has poor power management for Thunderbolt adapters on Macs. This can cause the TB adapter(s) to be always-on and prevent the CPU from going into the deepest power-saving states [\[1\]](https://bugzilla.kernel.org/show_bug.cgi?id=92111), drawing ca. 2W additional power even when not in use [\[2\]](https://github.com/Dunedan/mbp-2016-linux/issues/24#issuecomment-310952415). An easy way to see the CPU states is using powertop. The problem arises when the CPU does not go below C3 as a package (Pkg%pc3).

One workaround is to add `acpi_osi=!Darwin` to the [kernel parameters](../../en/Kernel_parameters.html "Kernel parameters"), thereby telling the firmware that the system is not compatible with macOS [\[3\]](https://docs.kernel.org/firmware-guide/acpi/osi.html). This should disable the TB adapter (at least on older Macs), and thus reduce power consumption greatly, but will probably come with side-effects (e.g. no Thunderbolt, maybe others?).

It is also possible to [blacklist](../../en/Kernel_module.html#Blacklisting "Blacklist") the thunderbolt module and then putting the controllers to sleep with

    # echo auto > /sys/bus/pci/devices/0000:07:00.0/power/control

Check the correct device number with lspci. This can also be [automated](../../en/Systemd.html#systemd-tmpfiles_-_temporary_files "Systemd"). This method reduces power consumption slightly, but still consumes 0.9 W more than the previous method on a MacBook Air 2013.

### Suspend and hibernate {#Suspend_and_hibernate}

Issues were reported where the machine would \"suspend immediately after resume\" in certain conditions when suspending by closing the lid. This was solved by setting the option \"sleep-inactive-ac-type\" to \"nothing\" using dconf-editor, option path: org → gnome → settings-daemon → plugins → power).

See [Suspend and hibernate](../../en/Suspend_and_hibernate.html "Suspend and hibernate") for details on how to configure hibernation. Noticeably, you will need a swap partition or file (see the mentioned article for further instructions).

Slow wake ups from a suspend state can be resolved by disabling Thunderbolt. See [#Disabling Thunderbolt](#Disabling_Thunderbolt).

On some Mac models, such as the 2015 iMac (model iMac16,2), resume from sleep only works using s2idle rather than deep. To test if this is an issue for your machine:

\

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ cat /sys/power/mem_sleep
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
s2idle [deep]
```

    # echo s2idle > /sys/power/mem_sleep

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ cat /sys/power/mem_sleep
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[s2idle] deep
```

\
Then suspend and resume. If it now works, add ` mem_sleep_default=s2idle ` to your kernel parameters to select s2idle as the persistent default.

### Wake up after suspend {#Wake_up_after_suspend}

Occasionally a Mac laptop may wake up immediately after suspending. This may not be immediately evident as the screen may stay off despite the system being awake, and can be checked by seeing whether the keyboard backlight stays on.

In `/proc/acpi/wakeup`, check to see that XHC1 and LID0 are enabled. If they are, one can temporarily disable just LID0 with the following to see if the issue resolves

    # echo LID0 > /proc/acpi/wakeup

To make the change persistent, [create](../../en/Help:Reading.html#Append,_add,_create,_edit "Create"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/suspend-fix.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=Fix for the suspend issue
[Service]
Type=oneshot
ExecStart=/bin/sh -c "echo LID0 > /proc/acpi/wakeup"
[Install]
WantedBy=multi-user.target
```

And then [enable/start](../../en/Help:Reading.html#Control_of_systemd_units "Enable/start") `suspend-fix.service`. To wake the system from this point, use the keyboard.

If this does not resolve the issue, XHC1 may be the issue and one can disable both it and LID0 temporarily with the following to see if it goes away.

    # echo XHC1 > /proc/acpi/wakeup && echo LID0 > /proc/acpi/wakeup

Disabling only XHC1 is not recommended if you have this bug, since it may result in glitchy behavior. Disable both on every boot as follows:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/suspend-fix.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=Fix for the suspend issue
[Service]
Type=oneshot
ExecStart=/bin/sh -c "echo XHC1 > /proc/acpi/wakeup && echo LID0 > /proc/acpi/wakeup"
[Install]
WantedBy=multi-user.target
```

To wake the system from this point, only the power button can be used.

## Light sensor {#Light_sensor}

The values can be read from `/sys/devices/platform/applesmc.768/light`: it returns two-tuples like (4,0).

If you want to use the built in light sensor to automatically adjust screen and keyboard backlight brightness:

-   **macbook-lighter** --- Macbook screen/keyboard backlight CLI and auto-adjust on ambient light.

[https://github.com/harttle/macbook-lighter](https://github.com/harttle/macbook-lighter) \|\| [macbook-lighter](https://aur.archlinux.org/packages/macbook-lighter/)^AUR^

## Sound {#Sound}

First of all follow [ALSA](../../en/Advanced_Linux_Sound_Architecture.html "ALSA") wiki page, then if something does not work correctly, continue reading this part.

### Kernel options {#Kernel_options}

Edit your `/etc/modprobe.d/50-sound.conf` or `/etc/modprobe.d/modprobe.conf` appending this line:

    options snd_hda_intel model=intel-mac-auto

This should automatically specify the codec in your Mac.

**Warning** Every time you change `/etc/modprobe.d`, test it by rebooting.

Specific models may need more help. You can try specifying other options according to your hardware. All possible settings are listed in Kernel Documentation, available online:

-   [Advanced Linux Sound Architecture - Driver Configuration guide](https://docs.kernel.org/sound/alsa-configuration.html)
-   [HD-Audio](https://docs.kernel.org/sound/hd-audio/index.html)
-   [HD-Audio Codec-Specific Models](https://docs.kernel.org/sound/hd-audio/models.html)

#### Model-specifics {#Model-specifics}

**This article or section is a candidate for merging with [Laptop/Apple](../../en/Laptop/Apple.html "Laptop/Apple").**

**Notes:** This should be moved to the model-specific page. (Discuss in [Talk:Mac/Troubleshooting](../../en/Talk:Mac/Troubleshooting.html))

For example, if you have a MacBookPro12,1, you might need

    options snd-hda-intel index=1,0

instead. Alternatively, for MacBookPro5,X, you can use:

    options snd_hda_intel model=mb5

(note that the jack output is controlled with \"HP\").

If you have an iMac8,1, you should instead use

    options snd-hda-intel model=mbp3 position_fix=2

For Aluminium iMacs, see [iMac Aluminium#Getting sound to work right](../../en/IMac_Aluminium.html#Getting_sound_to_work_right "IMac Aluminium")

For MacBook2,1 (late 2008/early 2009)s with a [SigmaTel STAC9221 A1](https://docs.kernel.org/sound/hd-audio/models.html#stac9220-9221) chip, use

    options snd_hda_intel model=macbook

### Disabling S/PDIF {#Disabling_S/PDIF}

Some (most?) Mac models have an optical S/PDIF audio jack in the same jack as the headphone jack. You can see it when it is active as a red light glowing out of the headphone jack. It can trick PulseAudio into preferring it and routing all your audio out it.

If you are not getting any sound in or out, confirm that `pavucontrol` \> Configuration \> Profile says \"Analog Stereo Duplex\" instead of \"Digital\"

or just run

    $ pacmd set-card-profile 0 output:analog-stereo+input:analog-stereo

Also check if you need to edit `/usr/share/alsa-card-profile/mixer/paths/` to workaround faulty plug detection causing PulseAudio to failover to \"Digital\".

See [Laptop/Apple#Microphone](../../en/Laptop/Apple.html#Microphone "Laptop/Apple") for how to edit this to get the MacBook2,1\'s microphone to work.

### Auto-Mute Mode {#Auto-Mute_Mode}

The internal speaker might not be disabled when using the headphone jack. To solve this, enable \"Auto-Mute Mode\".

You can either do this using `alsamixer`:

1.  Run `alsamixer`
2.  Press `F6` and pick `default:0 HDA Intel` to get more detailed controls
3.  Use the arrow keys to select \"Auto-Mute Mode\"
4.  Press `Space` to enable it

or with `amixer`:

    $ amixer -c 0 cset name='Auto-Mute Mode' 1

Optionally, run `alsactl store` as root to make the change permanent.

### USB audio interface {#USB_audio_interface}

In some cases, it can actually be easier to set up sound using a USB audio interface rather than the jack directly.

With [pavucontrol](https://archlinux.org/packages/?name=pavucontrol), go to `Configuration`, choose `Off` for all devices and choose `Analog Stereo Duplex` for your USB device. You can then use the headphone jack on the USB device for speakers or headphones. This should work immediately and on startup.

## Bluetooth {#Bluetooth}

Bluetooth should work out-of-the box. See the article on [Bluetooth](../../en/Bluetooth.html "Bluetooth") to install and configure all software needed.

## Magic Mouse {#Magic_Mouse}

If you use a magic mouse you will find it works nicely out of the box. You might want to tweak some settings such as *scroll-speed* or *acceleration*. There is no GUI for this at this time. The only way to set these settings is to instruct the kernel driver (`hid_magicmouse`) with parameters. Create a modprobe config file for your mouse.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/magicmouse.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
options hid_magicmouse scroll-speed=55 scroll-acceleration=1 emulate_3button=0
```

This will instruct the driver to have a fast scroll-speed, do exponential acceleration and do not emulate a 3 button mouse. You can find an overview of all parameters and their current settings in `/sys/module/hid_magicmouse/parameters`.

To try different settings without rebooting you can also set them through the command line:

    # echo 55 > /sys/module/hid_magicmouse/parameters/scroll_speed

## Webcam {#Webcam}

### iSight {#iSight}

**Note** Linux kernel from 2.6.26 includes the Linux UVC driver natively. **MBP 6,2+ (Kernel \~2.6.37+) iSight works out of the box** without the need to use firmware from macOS. Only use `isight-firmware-tools` if it does not work normally.

iSight webcams on MacBooks or pre 6,2 MacBook Pros (6,2 came out around 2010) require the Apple\'s proprietary firmware that cannot be redistributed. It must be extracted from macOS and loaded onto Arch.

There is a pre-extracted copy available in the form of the [isight-firmware](https://aur.archlinux.org/packages/isight-firmware/)^AUR^ package.

If you want to do it yourself you will need to install [isight-firmware-tools](https://aur.archlinux.org/packages/isight-firmware-tools/)^AUR^ to extract the firmware. This package also includes a udev rule and ELF binary that are necessary, even once you have extracted the firmware file into `/lib/firmware/isight.fw`, for the file to be loaded every time you boot your computer (namely `/etc/udev/rules.d/isight.rules` which uses `/usr/lib/udev/ift-load`).

Instructions:

First you need to get the firmware out of a particular file located on your macOS install. It is located in `/System/Library/Extensions/IOUSBFamily.kext/Contents/PlugIns/AppleUSBVideoSupport.kext/Contents/MacOS/AppleUSBVideoSupport`.

**Tip** The `AppleUSBVideoSupport` file from a OS X 10.6 (Snow Leopard) installation may not work properly. If possible, use the file from OS X 10.5 or earlier.

To mount the macOS drive if multi-booting:

    # mkdir /media/macOS
    # mount -t hfsplus /dev/sda2 /media/macOS

You can also download a copy of the file from [https://archive.org/details/AppleUSBVideoSupport](https://archive.org/details/AppleUSBVideoSupport).

Then, install the [isight-firmware-tools](https://aur.archlinux.org/packages/isight-firmware-tools/)^AUR^ package.

Locate the `AppleUSBVideoSupport` file in the macOS directory listed above. Either copy it over to your Arch system (Any macOS installation should do, such as an iMac, not just one specific to your system) or, if multi-booting, mount the macOS drive and navigate to the directory. (On 10.6 (Snow Leopard) and 10.7 (Lion) the directory is `/System/Library/Extensions/IOUSBFamily.kext/Contents/PlugIns/AppleUSBVideoSupport.kext/Contents/MacOS`.) In that directory you can go ahead and extract the driver:

    # ift-extract --apple-driver AppleUSBVideoSupport

When it is done, check that the firmware has been found:

    # ls /usr/lib/firmware/isight.fw

Once successful, completely **shutdown** your Mac and start it back up again (to clear the hardware state of the webcam). Do *not* reboot.

It should be automatically loaded at boot; if it is not you can load the `uvcvideo` module [manually or load it at boot](../../en/Kernel_modules.html "Kernel modules").

### FaceTime HD Camera {#FaceTime_HD_Camera}

Macbooks after 2011 introduced a new camera connected by PCIe, which does not work out of the box. To check which type of webcam you are using, look for \"FaceTime HD Camera\" in the output of `lspci`. To support these webcams, install [facetimehd-dkms](https://aur.archlinux.org/packages/facetimehd-dkms/)^AUR^ and [facetimehd-firmware](https://aur.archlinux.org/packages/facetimehd-firmware/)^AUR^. To check if the module is loaded, run `dkms status` and `lsmod` to confirm that the `facetimehd` kernel module has been loaded.

Optionally, install [facetimehd-data](https://aur.archlinux.org/packages/facetimehd-data/)^AUR^ to calibrate the webcam colors. For more documentation, see the [upstream documentation on GitHub](https://github.com/patjak/facetimehd).

## Temperature sensors {#Temperature_sensors}

For reading temperature just install [lm_sensors](https://archlinux.org/packages/?name=lm_sensors). See [lm_sensors](../../en/Lm_sensors.html "Lm sensors") for more information.

## Avoid long EFI wait before booting {#Avoid_long_EFI_wait_before_booting}

If your Mac spends 30 seconds with \"white screen\" before booting you need to tell the firmware where the booting partition is. This is done via the `bless` utility in MacOS.

Boot macOS and open a terminal. If you do not have MacOS installed, you have several alternatives:

-   boot the Mac into the MacOS recovery
-   use the MacOS install DVD
-   boot from another Mac (connect the two computers via firewire or thunderbolt, start the other Mac while holding the T button, boot your Mac while holding the Options button (alt)).

Either way, once you have got a macOS terminal running on your Mac you need to execute the following command if the booting partition is EFI:

    # bless --device /dev/diskXsY --file=/Volumes/efi/EFI/BOOT/BOOTX64.EFI --setBoot

or if the booting partition is not EFI:

    # bless --device /dev/diskXsY --setBoot --legacy

To know the value to put in `--device` you can print a list of the partitions with the `diskutil list` command, and find your boot partition.

See also [https://bbs.archlinux.org/viewtopic.php?pid=833215](https://bbs.archlinux.org/viewtopic.php?pid=833215).

## kworker using high CPU {#kworker_using_high_CPU}

Sometime with the addition of Yosemite, some users found that kworker CPU usage will spike, as discussed [here](https://bbs.archlinux.org/viewtopic.php?id=171883&p=11). This is sometimes the result of runaway ACPI interrupts.

To check and see, you can count the number of recent ACPI interrupts and see if any of them are out of control.

    $ grep . -r /sys/firmware/acpi/interrupts/

If you see that one particular interrupt is out of control (possibly GPE66), i.e., registering hundreds of thousands of lines, you can try disabling it (replace XX with the runaway interrupt):

    # echo "disable" > /sys/firmware/acpi/interrupts/gpeXX

Disabling random ACPI interrupts could cause all kinds of problems, so do this at your own risk. If this fixes the problem, there is discussion about how to make a systemd service that automatically disables an interrupt at every boot [here](https://bbs.archlinux.org/viewtopic.php?pid=1488371).

## Mavericks upgrade breaks Arch boot option {#Mavericks_upgrade_breaks_Arch_boot_option}

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../../en/Help:Style.html "Help:Style") for reference.**

**Reason:** Partially duplicates [mkinitcpio](../../en/Mkinitcpio.html "Mkinitcpio") and [GRUB](../../en/GRUB.html "GRUB"). (Discuss in [Talk:Mac/Troubleshooting](../../en/Talk:Mac/Troubleshooting.html))

For some multi-boot users who utilize a separate Linux boot partition, the OS X Mavericks upgrade may overwrite the boot partition with Apple\'s own recovery boot filesystem. This breaks the Arch Linux boot option in rEFIt/rEFInd. The best way to proceed in this situation is to abandon a separate boot partition and use the EFI system partition (ESP) to install the boot loader of your choice. It is also recommended that you use rEFInd instead of rEFIt as development on the latter has halted.

Assuming grub2 as the boot loader:

Use the Arch LiveCD to boot to a shell and [chroot](../../en/Chroot.html "Chroot") to your broken Arch Linux environment.

Mount the ESP on `/boot`.

Edit the fstab and remove the old boot partition and make ESP the new boot partition. Now mount the ESP as the new `/boot` partition.

    # mount -a

[Reinstall](../../en/Help:Reading.html#Installation_of_packages "Install") the [linux](https://archlinux.org/packages/?name=linux) package.

Create a new initramfs and vmlinuz in /boot.

    # mkinitcpio -p linux

Install grub.

    # grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub --recheck --debug

Create a new grub.cfg file.

    # grub-mkconfig -o /boot/EFI/grub/grub.cfg

Make sure that grub.cfg is in the same directory as grubx64.efi.

Generate a new refind_linux.conf file in /boot simply by running mkrlconf.sh which comes with rEFInd.

Exit the chroot environment.

Reboot. You should see a new entry for Arch Linux in rEFInd and it should boot to your Arch Linux installation.
