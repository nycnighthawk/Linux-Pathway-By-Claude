---
{"title": "Network configuration/Ethernet", "url": "https://wiki.archlinux.org/title/Network_configuration/Ethernet", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# Network configuration/Ethernet

This article describes [Ethernet](https://en.wikipedia.org/wiki/Ethernet "wikipedia:Ethernet") specifics, general network configuration is covered in [Network configuration](../../en/Network_configuration.html "Network configuration").

## Device driver {#Device_driver}

### Check the status {#Check_the_status}

[udev](../../en/Udev.html "Udev") should detect your [network interface controller](https://en.wikipedia.org/wiki/Network_interface_controller "wikipedia:Network interface controller") (NIC) and automatically load the necessary [kernel module](../../en/Kernel_module.html "Kernel module") at startup. Check the output of `lspci -knnd ::0200` (where `::0200` means the \"[Ethernet controller](https://admin.pci-ids.ucw.cz/read/PD/02/00)\" subclass of the \"Network controller\" PCI device class) . It should tell you which kernel module contains the driver for your network device. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ lspci -knnd ::0200
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
01:00.1 Ethernet controller [0200]: Intel Corporation 82599ES 10-Gigabit SFI/SFP+ Network Connection [8086:10fb] (rev 01)
    Subsystem: Intel Corporation Ethernet Server Adapter X520-2 [8086:000c]
    Kernel driver in use: ixgbe
    Kernel modules: ixgbe
```

Next, check that the driver was loaded by running `dmesg | grep `*`module_name`* as root. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# dmesg | grep ixgbe
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
ixgbe: Intel(R) 10 Gigabit PCI Express Network Driver
...
ixgbe 0000:01:00.1: enabling device (0000 -> 0002)
...
ixgbe 0000:01:00.1: Intel(R) 10 Gigabit Network Connection
...
```

Skip the next section if the driver was loaded successfully. Otherwise, you will need to know which module is needed for your particular model.

### Load the module {#Load_the_module}

Search the internet for the right module/driver for your chipset. Some common modules are `8139too` for cards with a Realtek chipset, or `sis900` for cards with a SiS chipset. Once you know which module to use, try to [load it manually](../../en/Kernel_modules.html#Manual_module_handling "Kernel modules"). If you get an error saying that the module was not found, verify first if you recently upgraded the kernel (see [General troubleshooting#Cannot use some peripherals after kernel upgrade](../../en/General_troubleshooting.html#Cannot_use_some_peripherals_after_kernel_upgrade "General troubleshooting")). Alternatively, it is possible that the driver is not included in the Arch kernel. You may search the [AUR](../../en/Arch_User_Repository.html "AUR") for the module name.

If udev is not detecting and loading the proper module automatically during bootup, you can explicitly [load the module at boot](../../en/Load_the_module_at_boot.html "Load the module at boot").

## Tips and tricks {#Tips_and_tricks}

### ifplugd for laptops {#ifplugd_for_laptops}

**Tip** [dhcpcd](../../en/Dhcpcd.html "Dhcpcd") provides the same feature out of the box.

[ifplugd](https://archlinux.org/packages/?name=ifplugd) is a daemon which will automatically configure your Ethernet device when a cable is plugged in and automatically unconfigure it if the cable is pulled. This is useful on laptops with onboard network adapters, since it will only configure the interface when a cable is really connected. Another use is when you just need to restart the network but do not want to restart the computer or do it from the shell.

By default it is configured to work for the `eth0` device. This and other settings like delays can be configured in `/etc/ifplugd/ifplugd.conf`.

**Note** [netctl](../../en/Netctl.html "Netctl") includes `netctl-ifplugd@.service`, otherwise you can use `ifplugd@.service` from the [ifplugd](https://archlinux.org/packages/?name=ifplugd) package. For example, [enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") `ifplugd@eth0.service`.

### Reduce link speed {#Reduce_link_speed}

**The factual accuracy of this article or section is disputed.**

**Reason:** It is not clear on what hardware and workload the \~1W power difference was measured. There are other [power saving](../../en/Power_saving.html "Power saving") methods that affect Ethernet NICs. (Discuss in [Talk:Network configuration/Ethernet](../../en/Talk:Network_configuration/Ethernet.html))

Forcing 100Mbps or 10Mbps full-duplex speed on a gigabit ethernet NIC can save a lot of power (\~1W) on most network workloads. This also reduces components temperature.

Using `ethtool -s eth0 autoneg off speed 100` on every boot is inconvenient.

Boot time initialization of lower ethernet NIC speed is possible through [systemd.link files](../../en/Network_configuration.html#Network_interfaces "Network configuration"). The actual setup is performed by the `net_setup_link` udev builtin. Add the `AutoNegotiation` option to the network link file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/network/50-wired.link
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Match]
MACAddress=aa:bb:cc:dd:ee:ff

[Link]
NamePolicy=kernel database onboard slot path
AutoNegotiation=no
Duplex=full
BitsPerSecond=100M
```

Also see [systemd.link(5)](https://man.archlinux.org/man/systemd.link.5) for more information.

**Note**

-   `AutoNegotiation` must be set, to `no`, otherwise there will be a Speed/Duplex setting not supported error and the link will not initialize.
-   Only the first matching file is applied. The content of the default link file `/usr/lib/systemd/network/99-default.link` shipped with systemd has to be included, otherwise the interface might be misconfigured.
-   To be considered, the file name should alphabetically come before the default `99-default.link`. For example `50-wired.link` works.
-   This configuration applies only to the link-level, and is independent of network-level daemons such as [NetworkManager](../../en/NetworkManager.html "NetworkManager") or [systemd-networkd](../../en/Systemd-networkd.html "Systemd-networkd").
-   In the `Match` section, `OriginalName=` can also be used to identify the interface.

## Troubleshooting {#Troubleshooting}

### Swapping computers on the cable modem {#Swapping_computers_on_the_cable_modem}

Some cable ISPs (Vidéotron for example) have the cable modem configured to recognize only one client PC, by the MAC address of its network interface. Once the cable modem has learned the MAC address of the first PC or equipment that talks to it, it will not respond to another MAC address in any way. Thus if you swap one PC for another (or for a router), the new PC (or router) will not work with the cable modem, because the new PC (or router) has a MAC address different from the old one. To reset the cable modem so that it will recognise the new PC, you must power the cable modem off and on again. Once the cable modem has rebooted and gone fully online again (indicator lights settled down), reboot the newly connected PC so that it makes a DHCP request, or manually make it request a new DHCP lease.

If this method does not work, you will need to clone the MAC address of the original machine. See also [MAC address spoofing](../../en/MAC_address_spoofing.html "MAC address spoofing").

### Explicit Congestion Notification {#Explicit_Congestion_Notification}

[Explicit Congestion Notification](https://en.wikipedia.org/wiki/Explicit_Congestion_Notification "wikipedia:Explicit Congestion Notification") (ECN) may cause traffic problems with old/bad routers [\[1\]](https://bbs.archlinux.org/viewtopic.php?id=239892). As of [systemd 240](https://github.com/systemd/systemd/pull/20535), it is enabled for incoming connections that request it (kernel default).

To enable ECN for both incoming and outgoing connections:

    # sysctl net.ipv4.tcp_ecn=1

To enable ECN only when requested by incoming connections (the reasonably safe, kernel default):

    # sysctl net.ipv4.tcp_ecn=2

To disable ECN completely (to e.g. test whether ECN was causing problems):

    # sysctl net.ipv4.tcp_ecn=0

See also the [kernel documentation](https://docs.kernel.org/networking/ip-sysctl.html).

### Broadcom BCM57780 {#Broadcom_BCM57780}

This Broadcom chipset sometimes does not behave well unless you specify the order of the modules to be loaded. The modules are `broadcom` and `tg3`, the former needing to be loaded first.

These steps should help if your computer has this chipset:

-   Find your NIC in *lspci* output:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ lspci -nnd ::0200
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
02:00.0 Ethernet controller [0200]: Broadcom Corporation NetLink BCM57780 Gigabit Ethernet PCIe [14e4:1692] (rev 01)
```

-   If your wired networking is not functioning in some way or another, unplug your cable then do the following:

&nbsp;

    # modprobe -r tg3
    # modprobe broadcom
    # modprobe tg3

-   Plug your network cable back in and check whether the module succeeded with:

&nbsp;

    # dmesg | grep tg3

-   If this procedure solved the issue you can make it permanent by adding `broadcom` and `tg3` (in this order) to the `MODULES` array:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/mkinitcpio.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
MODULES=(.. broadcom tg3 ..)
```

-   [Regenerate the initramfs](../../en/Regenerate_the_initramfs.html "Regenerate the initramfs")
-   Alternatively, you can create an `/etc/modprobe.d/broadcom.conf`:

&nbsp;

    softdep tg3 pre: broadcom

**Note** These methods may work for other chipsets, such as BCM57760.

### Realtek no link / WOL problem {#Realtek_no_link_/_WOL_problem}

Users with Realtek 8168 8169 8101 8111(C) 8156B based NICs (cards / and on-board) may notice a problem where the NIC seems to be disabled on boot and has no Link light. This can usually be found on a dual boot system where Windows is also installed. It seems that using the official Realtek drivers (dated anything after May 2007) under Windows is the cause. These newer drivers disable the Wake-On-LAN feature by disabling the NIC at Windows shutdown time, where it will remain disabled until the next time Windows boots. You will be able to notice if this problem is affecting you if the Link light remains off until Windows boots up; during Windows shutdown the Link light will switch off. Normal operation should be that the link light is always on as long as the system is on, even during POST. This problem will also affect other operating systems without newer drivers (eg. Live CDs). Here are a few fixes for this problem.

#### Enable the NIC directly in Linux {#Enable_the_NIC_directly_in_Linux}

Follow [Network configuration#Enabling and disabling network interfaces](../../en/Network_configuration.html#Enabling_and_disabling_network_interfaces "Network configuration") to enable the interface.

#### Rollback/change Windows driver {#Rollback/change_Windows_driver}

You can roll back your Windows NIC driver to the Microsoft provided one (if available), or roll back/install an official Realtek driver pre-dating May 2007 (may be on the CD that came with your hardware).

#### Enable WOL in Windows driver {#Enable_WOL_in_Windows_driver}

Probably the best and the fastest fix is to change this setting in the Windows driver. This way it should be fixed system-wide and not only under Arch (eg. live CDs, other operating systems). In Windows, under Device Manager, find your Realtek network adapter and double-click it. Under the \"Advanced\" tab, change \"Wake-on-LAN after shutdown\" to \"Enable\".

**Note** Newer Realtek Windows drivers (tested with *Realtek 8111/8169 LAN Driver v5.708.1030.2008*, dated 2009/01/22, available from GIGABYTE) may refer to this option slightly differently, like *Shutdown Wake-On-LAN \> Enable*. It seems that switching it to `Disable` has no effect (you will notice the Link light still turns off upon Windows shutdown). One rather dirty workaround is to boot to Windows and just reset the system (perform an ungraceful restart/shutdown) thus not giving the Windows driver a chance to disable LAN. The Link light will remain on and the LAN adapter will remain accessible after POST - that is until you boot back to Windows and shut it down properly again.

#### Enable LAN Boot ROM in BIOS/CMOS {#Enable_LAN_Boot_ROM_in_BIOS/CMOS}

It appears that setting *Integrated Peripherals \> Onboard LAN Boot ROM \> Enabled* in BIOS/CMOS reactivates the Realtek LAN chip on system boot-up, despite the Windows driver disabling it on OS shutdown.

**Note** This was tested several times on a GIGABYTE GA-G31M-ES2L motherboard, BIOS version F8 released on 2009/02/05.

#### Disable USB AutoSuspend {#Disable_USB_AutoSuspend}

When using power saving features, specifically USB autosuspend, the device can fail to load correctly, resulting in a *NO-CARRIER* state (tested with RT8156B), and no established link.

To resolve, see [Power management#USB autosuspend](../../en/Power_management.html#USB_autosuspend "Power management") for details on blacklisting a device for USB autosuspend manually, or [TLP documentation on USB devices](https://linrunner.de/tlp/settings/usb.html) if using [TLP](../../en/TLP.html "TLP"); then reconnect the device.

### Realtek RTL8111/8168B {#Realtek_RTL8111/8168B}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# lspci -nnd ::0200
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
03:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168B PCI Express Gigabit Ethernet controller [10ec:8168] (rev 02)
```

The adapter should be recognized by the `r8169` module. However, with some chip revisions the connection may go off and on all the time. The alternative [r8168](https://aur.archlinux.org/packages/r8168/)^AUR^ should be used for a reliable connection in this case. [Blacklist](../../en/Kernel_module.html#Blacklisting "Blacklist") `r8169`, if [r8168](https://aur.archlinux.org/packages/r8168/)^AUR^ is not automatically loaded by [udev](../../en/Udev.html "Udev"), you can explicitly [load the module at boot](../../en/Load_the_module_at_boot.html "Load the module at boot").

**The factual accuracy of this article or section is disputed.**

**Reason:** \"some revisions\", no proof the driver is the cause, and not e.g poorly configured DNS servers (Discuss in [Talk:Network configuration/Ethernet](../../en/Talk:Network_configuration/Ethernet.html))

Another fault in the drivers for some revisions of this adapter is poor IPv6 support. [IPv6#Disable functionality](../../en/IPv6.html#Disable_functionality "IPv6") can be helpful if you encounter issues such as hanging webpages and slow speeds.

### Gigabyte Motherboard with Realtek 8111/8168/8411 {#Gigabyte_Motherboard_with_Realtek_8111/8168/8411}

With motherboards such as the *Gigabyte GA-990FXA-UD3*, booting with [IOMMU](../../en/PCI_passthrough_via_OVMF.html#Setting_up_IOMMU "IOMMU") off (which can be the default) will cause the network interface to be unreliable, often failing to connect or connecting but allowing no throughput. This will apply to the onboard NIC and to any other pci-NIC in the box because the IOMMU setting affects the entire network interface on the board. Enabling IOMMU and booting with the install media will throw AMD I-10/xhci page faults for a second, but then boots normally, resulting in a fully functional onboard NIC (even with the r8169 module).

When configuring the boot process for your installation, add `iommu=soft` as a [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter") to eliminate the error messages on boot and restore USB3.0 functionality.

### MicroStar Motherboard with Realtek 8111/8168/8411 {#MicroStar_Motherboard_with_Realtek_8111/8168/8411}

With motherboards such as the \"MicroStar B450M MORTAR TITANIUM\", unpluging/pluging Ethernet cables or restarting router\'s DHCP server would cause `r8169` to enter a downshifted status, and downgrade the 1000 Mbit/s Ethernet speed to 100 Mbit/s. The kernel log will show:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# dmesg | grep r8169
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Generic FE-GE Realtek PHY r8169-2200:00: Downshift occurred from negotiated speed 1Gbps to actual speed 100Mbps, check cabling!
r8169 0000:22:00.0 enp34s0: Link is Up - 100Mbps/Full (downshifted) - flow control rx/tx
```

In this case, restart the adapter (set it down and up). For example:

    # ip link set dev enp34s0 down
    # ip link set dev enp34s0 up

### Realtek RTL8153 Tx timeout {#Realtek_RTL8153_Tx_timeout}

USB Network Adapters with the following controller will often hang and stop transmit until its link is reset. This is accompanied with `Tx status -2` or `Tx status -71` errors in the kernel log. This can be fixed by setting `USB_QUIRK_NO_LPM`.

The quirk can be set at boot by adding the [kernel parameter](../../en/Kernel_parameter.html "Kernel parameter") `usbcore.quirks=2357:0601:k`. It can also be set immediately via the sysfs by

    # echo 2357:0601:k > /sys/module/usbcore/parameters/quirks

Note that `2357:0601` should be replaced with your own device\'s USB ID which can be found using *lsusb*.
