---
{"title": "CUPS/Troubleshooting", "url": "https://wiki.archlinux.org/title/CUPS/Troubleshooting", "retrieved": "2026-11-02", "license": "GFDL-1.3-or-later"}
---

# CUPS/Troubleshooting

Related articles

-   [CUPS](../../en/CUPS.html "CUPS")
-   [CUPS/Printer-specific problems](../../en/CUPS/Printer-specific_problems.html "CUPS/Printer-specific problems")

This article covers all non-specific (ie, not related to any one printer) troubleshooting of CUPS and printing drivers (but not problems related to printer sharing), including methods of determining the exact nature of the problem, and of solving the identified problem.

## Debug log {#Debug_log}

The best way to get printing working is to enable debug logging:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/cups/cupsd.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
LogLevel debug
```

And then viewing the output from `/var/log/cups/error_log` like this:

    # tail -n 100 -f /var/log/cups/error_log

The characters at the left of the output stand for:

-   D=Debug
-   E=Error
-   I=Information
-   And so on

These files may also prove useful:

-   `/var/log/cups/page_log` - Echoes a new entry each time a print is successful
-   `/var/log/cups/access_log` - Lists all cupsd http1.1 server activity

Print a document and watch `error_log` to get a more detailed and correct image of the printing process.

## Problems resulting from upgrades {#Problems_resulting_from_upgrades}

*Issues that appeared after CUPS and related program packages underwent a version increment*

### CUPS stops working {#CUPS_stops_working}

The chances are that a new configuration file is needed for the new version to work properly. Messages such as \"404 - page not found\" may result from trying to manage CUPS via localhost:631, for example.

To use the new configuration, copy `/etc/cups/cupsd.conf.default` to `/etc/cups/cupsd.conf` (backup the old configuration if needed) and restart CUPS to employ the new settings.

### All jobs are \"stopped\" {#All_jobs_are_\"stopped\"}

**The factual accuracy of this article or section is disputed.**

**Reason:** This seems a rather brute-force way of fixing this; maybe the printer is simply disabled? (Discuss in [Talk:CUPS/Troubleshooting](../../en/Talk:CUPS/Troubleshooting.html))

If all jobs sent to the printer become \"stopped\", first check the error log at `/var/log/cups/error_log`. If it does not yield any useful hints to what is the source of the issue, delete the printer and add it again. Using the [CUPS web interface](http://localhost:631), go to Printers \> Delete Printer.

To check the printer\'s settings go to *Printers*, then *Modify Printer*. Copy down the information displayed, click \'Modify Printer\' to proceed to the next page(s), and so on.

### All jobs are \"The printer is not responding\" {#All_jobs_are_\"The_printer_is_not_responding\"}

On networked printers, you should check that the hostname in the printer\'s URI resolves to the printer\'s IP address via DNS, e.g. if your printer\'s connection looks like this:

    lpd://BRN_020554/BINARY_P1

then the hostname \'BRN_020554\' needs to resolve to the printer\'s IP from the server running CUPS. If [Avahi](../../en/Avahi.html "Avahi") is being used, ensure that [Avahi\'s hostname resolution](../../en/Avahi.html#Hostname_resolution "Avahi") is working.

Alternatively, replace the hostname used in the URI with the printer\'s IP address.

### The PPD version is not compatible with gutenprint {#The_PPD_version_is_not_compatible_with_gutenprint}

Run:

    # /usr/bin/cups-genppdupdate

And restart CUPS (as pointed out in gutenprint\'s post-install message).

## Networking issues {#Networking_issues}

### Unable to add printer or message \"print in progress\" but nothing happens {#Unable_to_add_printer_or_message_\"print_in_progress\"_but_nothing_happens}

In GNOME Printer settings for example, you could find troubles adding your printer, even though you have installed the drivers. You can try installing [system-config-printer](https://archlinux.org/packages/?name=system-config-printer) and executing it via terminal, and adding the printer from there (for instance using LPD/LPR queue \'PASSTHRU\').

### Unable to locate printer {#Unable_to_locate_printer}

Even if CUPS can detect networked printers, you may still end up with an \"Unable to locate printer\" error when trying to print something. The solution to this problem is to enable Avahi\'s [.local hostname resolution](../../en/Avahi.html#Hostname_resolution "Avahi"). See [CUPS#Network](../../en/CUPS.html#Network "CUPS") for details.

This problem may also arise when you have a firewall. You may need to disable your firewall or set the right rules. Using *system-config-printer* to detect network printers will do that automatically.

Similarly, being connected to a VPN may also cause CUPS to be unable to locate the printer. Disabling any VPN connections temporarily for printing can help fixing it.

### Old CUPS server {#Old_CUPS_server}

As of CUPS version 1.6, the client defaults to IPP 2.0. If the server uses CUPS \<= 1.5 / IPP \<= 1.1, the client does not downgrade the protocol automatically and thus cannot communicate with the server. A workaround is to append the `version=1.1` option documented at [\[1\]](https://www.cups.org/doc/network.html#TABLE2) to the URI.

### Unable to locate PPD file {#Unable_to_locate_PPD_file}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/var/log/cups/error_log
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Cannot connect to remote printer ipp://HP079676.local
copy_model: empty PPD file
```

Make sure [Avahi](../../en/Avahi.html "Avahi") is set up correctly. In particular, make sure [nss-mdns](https://archlinux.org/packages/?name=nss-mdns) is installed and set up in `/etc/nsswitch.conf`.

### Finding URIs for Windows print servers {#Finding_URIs_for_Windows_print_servers}

Sometimes Windows is a little less than forthcoming about exact device URIs (device locations). If having trouble specifying the correct device location in CUPS, run the following command to list all shares available to a certain windows username:

    $ smbtree -U windowsusername

This will list every share available to a certain Windows username on the local area network subnet, as long as Samba is set up and running properly. It should return something like this:

     WORKGROUP
        \\REGULATOR-PC          
            \\REGULATOR-PC\Z                
            \\REGULATOR-PC\Public           
            \\REGULATOR-PC\print$           Printer Drivers
            \\REGULATOR-PC\G                
            \\REGULATOR-PC\EPSON Stylus CX8400 Series   EPSON Stylus CX8400 Series

What is needed here is first part of the last line, the resource matching the printer description. So to print to the EPSON Stylus printer, one would enter:

    smb://username:password@REGULATOR-PC/EPSON%20Stylus%20CX8400%20Series

as the URI into CUPS.

## USB printers {#USB_printers}

### Conflict with SANE {#Conflict_with_SANE}

If you are also running [SANE](../../en/SANE.html "SANE"), it is possible that it is conflicting with CUPS. To fix this create a [Udev](../../en/Udev.html "Udev") rule marking the device as matched by libsane:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/udev/rules.d/99-printer.rules
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
ATTRS{idVendor}=="vendor id", ATTRS{idProduct}=="product id", MODE="0664", GROUP="lp", ENV{libsane_matched}="yes"
```

### Conflict with usblp {#Conflict_with_usblp}

USB printers can be accessed using two methods: The usblp kernel module and libusb. The former is the classic way. It is simple: data is sent to the printer by writing it to a device file as a simple serial data stream. Reading the same device file allows bi-di access, at least for things like reading out ink levels, status, or printer capability information (PJL). It works very well for simple printers, but for multi-function devices (printer/scanner) it is not suitable and manufacturers like HP supply their own backends. Source: [here](https://web.archive.org/web/20240915141016/https://lists.linuxfoundation.org/pipermail/printing-architecture/2012/002412.html).

**Warning** As of [cups](https://archlinux.org/packages/?name=cups) version 1.6.0, it should no longer be necessary to blacklist the `usblp` kernel module. If you find out this is the only way to fix a remaining issue please report this upstream to the CUPS bug tracker and maybe also get in contact with Till Kamppeter (Debian CUPS maintainer). See [upstream bug](https://github.com/apple/cups/issues/4128) for more info.

If you have problems getting your USB printer to work, you can try [blacklisting](../../en/Kernel_module.html#Blacklisting "Blacklisting") the `usblp` [kernel module](../../en/Kernel_module.html "Kernel module"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/blacklistusblp.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
blacklist usblp
```

Custom kernel users may need to manually load the `usbcore` [kernel module](../../en/Kernel_module.html "Kernel module") before proceeding.

Once the modules are installed, run:

    # journalctl -f

Then plug in the printer and inspect the output to see if it was detected.

If you are using `usblp`, the output should indicate that the printer has been detected like so:

    Feb 19 20:17:11 kernel: printer.c: usblp0: USB Bidirectional
    printer dev 2 if 0 alt 0 proto 2 vid 0x04E8 pid 0x300E
    Feb 19 20:17:11 kernel: usb.c: usblp driver claimed interface cfef3920
    Feb 19 20:17:11 kernel: printer.c: v0.13: USB Printer Device Class driver

If you blacklisted `usblp`, you will see something like:

    usb 3-2: new full speed USB device using uhci_hcd and address 3
    usb 3-2: configuration #1 chosen from 1 choice

### USB autosuspend {#USB_autosuspend}

The Linux kernel automatically suspends USB devices when there is driver support and the devices are not in use. This can save power, but some USB printers think that they are disconnected when the kernel suspends the USB port, preventing printing. This can be fixed by deactivating autosuspend for the specific device, see [Power management#USB autosuspend](../../en/Power_management.html#USB_autosuspend "Power management").

### Bad permissions {#Bad_permissions}

Check the permissions of the printer USB device. Get the bus and device number from `lsusb`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ lsusb
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Bus <BUSID> Device <DEVID>: ID <VENDOR>:<PRINTERID> Hewlett-Packard DeskJet D1360
```

Check the ownership by looking in devfs:

    # ls -l /dev/bus/usb/BUSID/DEVID

The cups daemon runs as user \"cups\" and belongs to group \"lp\", so either this user or group needs read & write access to the USB device. If you think the permissions look wrong, you can change the group and permission temporarily:

    # chgrp lp /dev/bus/usb/BUSID/DEVID
    # chmod 664 /dev/bus/usb/BUSID/DEVID

Then check if cups can now see the USB device correctly.

To make a persistent permission change that will be triggered automatically each time the USB device is attached, add the following line:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/udev/rules.d/10-local.rules
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
SUBSYSTEM=="usb", ATTRS{idVendor}=="VENDOR", ATTRS{idProduct}=="PRINTERID", GROUP:="lp", MODE:="0664"
```

After editing, reload the udev rules with this command:

    # udevadm control --reload-rules

Each system may vary, so consult [udev#List the attributes of a device](../../en/Udev.html#List_the_attributes_of_a_device "Udev") wiki page.

## HP issues {#HP_issues}

**This article or section is a candidate for merging with [CUPS/Printer-specific problems#HP](../../en/CUPS/Printer-specific_problems.html#HP "CUPS/Printer-specific problems").**

**Notes:** There should not be two different places for these issues. (Discuss in [Talk:CUPS/Troubleshooting](../../en/Talk:CUPS/Troubleshooting.html))

### CUPS: \"/usr/lib/cups/backend/hp failed\" {#CUPS:_\"/usr/lib/cups/backend/hp_failed\"}

Try adding the printer as a Network Printer using the http:// protocol.

**Note** There might need to set permissions issues right.

### CUPS: Job is shown as complete but the printer does nothing {#CUPS:_Job_is_shown_as_complete_but_the_printer_does_nothing}

This happens on HP printers when you select the (old) hpijs driver (e.g. the Deskjet D1600 series). Use the hpcups driver instead.

Some HP printers require their firmware to be downloaded from the computer every time the printer is switched on. If there is an issue with udev (or equivalent) and the firmware download rule is never fired, you may experience this issue. As a workaround, you can manually download the firmware to the printer. Ensure the printer is plugged in and switched on, then run:

    # hp-firmware -n

### CUPS: \'\"foomatic-rip\" not available/stopped with status 3\' {#CUPS:_'\"foomatic-rip\"_not_available/stopped_with_status_3'}

If receiving any of the following error messages in `/var/log/cups/error_log` while using a HP printer, with jobs appearing to be processed while they all end up not being completed with their status set to \'stopped\':

    Filter "foomatic-rip" for printer printer_name not available: No such file or director

or:

    PID pid (/usr/lib/cups/filter/foomatic-rip) stopped with status 3!

make sure [hplip](https://archlinux.org/packages/?name=hplip) has been [installed](../../en/Help:Reading.html#Installation_of_packages "Install").

### CUPS: \"Filter failed\" {#CUPS:_\"Filter_failed\"}

A \"filter failed\" error can be caused by any number of issues. The CUPS error log (by default `/var/log/cups/error_log`) should record which filter failed and why.

#### Missing ghostscript {#Missing_ghostscript}

Install [ghostscript](https://archlinux.org/packages/?name=ghostscript) (`/usr/lib/cups/filter/gstoraster` needs it to run).

#### Missing foomatic-db {#Missing_foomatic-db}

Install [foomatic-db](https://archlinux.org/packages/?name=foomatic-db) and [foomatic-db-ppds](https://archlinux.org/packages/?name=foomatic-db-ppds). This fixes it in some cases.

#### Avahi not enabled {#Avahi_not_enabled}

[Start](../../en/Help:Reading.html#Control_of_systemd_units "Start") and [enable](../../en/Help:Reading.html#Control_of_systemd_units "Enable") `avahi-daemon.service`.

#### Out-of-date plugin {#Out-of-date_plugin}

This error can also indicate that the plugin is out of date (version is mismatched) and may occur after a system upgrade, possibly showing up as a `Plugin error` message in the logs. If you have installed [hplip-plugin](https://aur.archlinux.org/packages/hplip-plugin/)^AUR^ you will need to update the package, otherwise re-run `hp-setup -i` to install the latest version of the plugin.

#### Outdated printer configuration {#Outdated_printer_configuration}

As of [hplip-plugin](https://aur.archlinux.org/packages/hplip-plugin/)^AUR^ v3.17.11, *hpijs* is no longer available. If you have printers using hpijs they will fail to print. You must modify them and select the new *hpcups* driver instead.

You can check if this is your case looking at cups error_log:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ grep hpijs /var/log/cups/error_log
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
D [09/Jan/2018:14:32:58 +0000] [Job 97] sh: hpijs: command not found
...
```

#### Client and host both run CUPS with hpcups {#Client_and_host_both_run_CUPS_with_hpcups}

**Note** The following issue has been described on FreeBSD forum. [Read more here](https://forums.freebsd.org/threads/filter-failed-cups-hp-psc-2350-series.60222/).

A bug seems to affect CUPS when a host shares a physically connected HP printer using hpcups drivers from [hplip](https://archlinux.org/packages/?name=hplip), and a client adds the shared printer in is own CUPS server through [IPP](https://en.wikipedia.org/wiki/Internet_Printing_Protocol "wikipedia:Internet Printing Protocol"), using hpcups driver too. On every attempt to print a page from the client, the jobs page from the client returns indefinitely *\"Sending data to printer\"* while the same page from the host returns *\"Filter failed\"*. It appears that the job runs through the CUPS filter twice: a first time on client-side, and a second time on host-side, which makes it fails on host-side. The same bug should not be observed when printing from a Windows client, or when printing directly on the host. There are some workarounds here (use only one method):

-   Use **Generic IPP Everywhere Printer** driver on the client. When selecting the driver in the CUPS Web Interface, you should find it in the *Generic* manufacturer.
-   Modify the **PPD used on the client side** so the job does not goes through the filter client-side. Find the right PPD in `/usr/share/ppd/HP` and copy it in your home directory. Edit the copy : replace the line `*cupsFilter: "application/vnd.cups-raster 0 hpcups"` with `*cupsFilter: "*/* 0 -"`. Now, add your printer on the client CUPS, selecting your custom PPD located in your home directory.
-   Create a **raw queue** on the host: when you add the printer in the CUPS interface of the host, do not select the specific PPD of your printer, but choose *Raw queue* from *Raw* manufacturer. You should be able to add this shared printer on the client, using this time the specific PPD of the printer. With this method, the host is not able to print directly a document because it does not run the filter. However, if the host is a small headless embedded device such as a Raspberry Pi, you might notice an important decrease of the response time with this method compared to the two previous ones, especially with large documents, because it saves a lot a CPU usage.

### CUPS: prints only an empty or a single page and an error-message page on HP LaserJet {#CUPS:_prints_only_an_empty_or_a_single_page_and_an_error-message_page_on_HP_LaserJet}

There is a bug that causes CUPS to fail when printing images on HP LaserJet (Seen for LasertJet 3380, and for LaserJet 1300 as recently as July 2024). The bug has been reported and fixed by [Ubuntu](https://bugs.launchpad.net/ubuntu/+source/cups-filters/+bug/998087). The first page is empty, the second page contains the following error message:

     ERROR:
     invalidaccess
     OFFENDING COMMAND:
     filter
     STACK:
     /SubFileDecode
     endstream
     ...

This problem can also present itself differently, where it will take a long time before starting to print, then print a single page, followed by another page containing the following error message:

     ERROR:
     typecheck
     OFFENDING COMMAND:
     idiv
     STACK:
     50000
     --nostringval--
     --nostringval--
     -mark-
     -mark-
     -mark-
     -mark-

In order to fix these issues, run the following command as root:

    # lpadmin -p printer -o pdftops-renderer-default=pdftops

### CUPS: \"File \"/usr/lib/cups/filter/rastertospl\" not available {#CUPS:_\"File_\"/usr/lib/cups/filter/rastertospl\"_not_available}

After the printer is connected by other means to the network, setting up the HP 107w Laser printer is possible through the CUPS web interface; but this error prevents printing.

It seems that support for this printer is not provided by hplip. However, drivers can be installed using HP\'s install scripts and PPD file found at the HP [downloads](https://support.hp.com/us-en/drivers/selfservice/hp-laser-100-printer-series/24494339/model/24494342) page.

Extract the .zip and read this [gist](https://gist.github.com/taniwallach/f1f6c81ce19b7d68f74d4b71d1db57a2) for further details and instructions.

In case this problem appeared after a PPD package (like *foomatic-\**) update, check if there are new PPDs for the printer, and try to use the new ones.

As of January 2022, the new driver for Samsung M283x has PXL in the name and the PPD does not reference rastertospl, and the printer works again. Fetching the rastertospl via the above method did not work because the arguments are passed in the wrong order.

### HPLIP 3.13: Plugin is installed, but HP Device Manager complains it is not {#HPLIP_3.13:_Plugin_is_installed,_but_HP_Device_Manager_complains_it_is_not}

The issue might have to do with the file permission change that had been made to `/var/lib/hp/hplip.state`. To correct the issue, a simple `chmod 644 /var/lib/hp/hplip.state` and `chmod 755 /var/lib/hp` should be sufficient. For further information, please read this [link](https://bugs.launchpad.net/hplip/+bug/1131596).

### hp-toolbox: \"Unable to communicate with device\" {#hp-toolbox:_\"Unable_to_communicate_with_device\"}

    # hp-toolbox
    # error: Unable to communicate with device (code=12): hp:/usb/printer id

#### Virtual CDROM printers {#Virtual_CDROM_printers}

This can also be caused by printers such as the P1102 that provide a virtual CD-ROM drive for MS Windows drivers. The `lp` appears in `/dev/` and then disappears. In that case, try the [usb_modeswitch](https://archlinux.org/packages/?name=usb_modeswitch) package, that lets one switch off the \"Smart Drive\" (udev rules included in said package).

#### Networked printers {#Networked_printers}

This can also occur with network attached printers using dynamic hostnames if the [avahi-daemon](../../en/Avahi.html "Avahi") is not running. Another possibility is that *hp-setup* failed to locate the printer because the IP address of the printer changed due to DHCP. If this is the case, consider adding a DHCP reservation for the printer in the DHCP server\'s configuration. If the printer already has a static IP and comes with an own webserver check if SNMP is turned on by calling the printers ip address in a browser: Networking \> SNMP.

### hp-setup asks to specify the PPD file for the discovered printer {#hp-setup_asks_to_specify_the_PPD_file_for_the_discovered_printer}

Furthermore, when selecting a PPD file in hp-setup\'s graphical mode, the field does not update and no error message is shown.

Or, if in interactive (console) mode, you may encounter something similar to this even when providing a correct path to a valid ppd file:

     Please enter the full filesystem path to the PPD file to use (q=quit) :/usr/share/ppd/HP/hp-deskjet_2050_j510_series.ppd.gz
     Traceback (most recent call last):
       File "/usr/bin/hp-setup", line 536, in <module>
         desc = nickname_pat.search(nickname).group(1)
     TypeError: cannot use a string pattern on a bytes-like object

The solution is to install and start [cups](https://archlinux.org/packages/?name=cups) before running `hp-setup`.

### hp-setup: \"Qt/PyQt 5 initialization failed\" {#hp-setup:_\"Qt/PyQt_5_initialization_failed\"}

[Install](../../en/Help:Reading.html#Installation_of_packages "Install") [python-pyqt5](https://archlinux.org/packages/?name=python-pyqt5), which is an optdepend of [hplip](https://archlinux.org/packages/?name=hplip). Alternatively, to run hp-setup with the command line interface, use the `-i` flag.

### hp-setup: finds the printer automatically but reports \"Unable to communicate with device\" when printing test page immediately afterwards {#hp-setup:_finds_the_printer_automatically_but_reports_\"Unable_to_communicate_with_device\"_when_printing_test_page_immediately_afterwards}

This at least happens to hplip 3.13.5-2 for HP Officejet 6500A through local network connection. To solve the problem, specify the IP address of the HP printer for hp-setup to locate the printer.

### hp-setup: \"KeyError: \'family-class\'\" {#hp-setup:_\"KeyError:_'family-class'\"}

If adding a printer fails silently in the UI or you receive a `KeyError: 'family-class'` traceback from `hp-setup`, the `/usr/share/hplip/data/models/models.dat` may need to be manually updated. Check if `family-class=Undefined` is defined the section for your printer, if not add it:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/usr/share/hplip/data/models/models.dat
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[hp_laserjet_pro_mfp_m225dw]
...
family-class=Undefined
```

### Broken pipe {#Broken_pipe}

If `/var/log/cups/error_log` contains the `HTTP_STATE_WAITING Closing for error 32 (Broken pipe)` error, you probably need to install the [hplip-plugin](https://aur.archlinux.org/packages/hplip-plugin/)^AUR^ and restarts the cups service.

## Other {#Other}

### Printer \"Paused\" or \"Stopped\" with Status \"Rendering completed\" {#Printer_\"Paused\"_or_\"Stopped\"_with_Status_\"Rendering_completed\"}

#### Low ink {#Low_ink}

When low on ink, some printers will get stuck in \"Rendering completed\" status and, if it is a network printer, the printer may even become unreachable from CUPS\' perspective despite being properly connected to the network. Replacing the low/depleted ink cartridge(s) in this setting will return the printer to \"Ready\" status and, if it is a network printer, will make the printer available to CUPS again.

**Note** If you use third-party ink cartridges, the ink levels reported by the printer may be inaccurate. If you use third-party ink and your printer used to work fine but is now getting stuck on \"Rendering completed\" status, replace the ink cartridges regardless of the reported ink levels before trying other fixes.

### Printing fails with unauthorised error {#Printing_fails_with_unauthorised_error}

If a remote printer requests authentication CUPS will automatically add an `AuthInfoRequired` directive to the printer in `/etc/cups/printers.conf`. However, some graphical applications (for instance, some versions of [LibreOffice](../../en/LibreOffice.html "LibreOffice") [\[2\]](https://bugs.documentfoundation.org/show_bug.cgi?id=53029)) have no way to prompt for credentials, so printing fails. To fix this include the required username and password in the URI. See [\[3\]](https://bugs.launchpad.net/ubuntu/+source/cups/+bug/283811), [\[4\]](https://bbs.archlinux.org/viewtopic.php?id=61826).

### Unknown supported format: application/postscript {#Unknown_supported_format:_application/postscript}

Comment the lines:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/cups/mime.convs
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
application/octet-stream        application/vnd.cups-raw        0      -
```

and:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/cups/mime.types
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
application/octet-stream
```

### Print-Job client-error-document-format-not-supported {#Print-Job_client-error-document-format-not-supported}

Try installing the foomatic packages and use a foomatic driver.

**The factual accuracy of this article or section is disputed.**

**Reason:** Implying that the user has a wrong driver installed does not make sense (is not relevant to this section). (Discuss in [Talk:CUPS/Troubleshooting](../../en/Talk:CUPS/Troubleshooting.html))

If that does not fix, you maybe have to remove the printer from your printer list, then manually search for your printer driver (usually you can find it on AUR), and then add the printer again.

### Unable to get list of printer drivers {#Unable_to_get_list_of_printer_drivers}

(Also applicable to error \"-1 not supported!\")

Try to remove Foomatic drivers or refer to [CUPS/Printer-specific problems#HPLIP](../../en/CUPS/Printer-specific_problems.html#HPLIP "CUPS/Printer-specific problems") for a workaround.

### lp: Error - Scheduler Not Responding {#lp:_Error_-_Scheduler_Not_Responding}

If you get this error, ensure [CUPS](../../en/CUPS.html "CUPS") is running, the [environment variable](../../en/Environment_variable.html "Environment variable") `CUPS_SERVER` is unset, and that `/etc/cups/client.conf` is correct.

### \"Using invalid Host\" error message {#\"Using_invalid_Host\"_error_message}

Try adding `ServerAlias *` into `/etc/cups/cupsd.conf`.

### Cannot print from LibreOffice {#Cannot_print_from_LibreOffice}

If you can print a test page from the [CUPS](../../en/CUPS.html "CUPS") web interface, but not from [LibreOffice](../../en/LibreOffice.html "LibreOffice"), try to [install](../../en/Help:Reading.html#Installation_of_packages "Install") the [a2ps](https://archlinux.org/packages/?name=a2ps) package.

### Printer output shifted {#Printer_output_shifted}

This seems to be caused by the wrong page size being set in [CUPS](../../en/CUPS.html "CUPS").

### Printer becomes stuck after a problem {#Printer_becomes_stuck_after_a_problem}

When an issue arises during printing, the printer in CUPS may become unresponsive. `lpq` reports that the printer `is not ready`, and it can be reactivated using `cupsenable`. In the CUPS web interface, the printer is shown as *Paused*, and can be reactivated by *resuming* the printer.

To automatically have CUPS reactivate the printer, change [ErrorPolicy](https://www.cups.org/doc/man-cupsd.conf.html?TOPIC=Man+Pages#ErrorPolicy) from the default `stop-printer` to `retry-current-job`.

### Samsung: URF ERROR - Incomplete Session by time out {#Samsung:_URF_ERROR_-_Incomplete_Session_by_time_out}

This error is usually encountered when printing files over the network through IPP to a Samsung printer, and is solved by using the [samsung-unified-driver](https://aur.archlinux.org/packages/samsung-unified-driver/)^AUR^ package.

**Note** The corresponding error code 11-1112 corresponds to an internal wiring problem with the printer, so contacting Samsung\'s tech support is futile.

### Brother: Printer prints multiple copies {#Brother:_Printer_prints_multiple_copies}

Sometimes the printer will print multiple copies of a document (for instance a MFC-9330CDW printed 10 copies). The solution is to [update the printer firmware](../../en/CUPS/Printer-specific_problems.html#Updating_the_firmware "CUPS/Printer-specific problems").

### Regular user cannot change properties of the printer or remove certain jobs {#Regular_user_cannot_change_properties_of_the_printer_or_remove_certain_jobs}

If a regular user needs to be able to change the printers properties or manage the printer queue, the user may need to be added to the `sys` group.

### Cannot login into web interface {#Cannot_login_into_web_interface}

Check if there is more than one `cupsd` process running. If this is the case then [stop](../../en/Help:Reading.html#Control_of_systemd_units "Stop") `cups.service`, kill all processes named `cupsd` and [start](../../en/Help:Reading.html#Control_of_systemd_units "Start") `cups.service` again.

### Virtual PDF printer stops jobs {#Virtual_PDF_printer_stops_jobs}

If the virtual PDF printer (driver: `Generic CUPS-PDF Printer (w/ options)`) keeps stopping print jobs and the error log shows `Unable to auto-configure PostScript Printer - no bidirectional I/O available!`, re[installing](../../en/Help:Reading.html#Installation_of_packages "Install") [cups-filters](https://archlinux.org/packages/?name=cups-filters) may help.

### No suitable destination found {#No_suitable_destination_found}

**The factual accuracy of this article or section is disputed.**

**Reason:** The exact way of doing this, i.e. if it is enough to just wipe `/etc/cups/printers/ssl` or if you need to stop CUPS and/or remove the affected printer first, is lost in history - please feel free to add this information (Discuss in [Talk:CUPS/Troubleshooting](../../en/Talk:CUPS/Troubleshooting.html))

If a printer prefers ipps (ipp-secure), CUPS will store the printer\'s certificate in `/etc/cups/printers/ssl`. However, these certificates are never removed, even if invalid. There are several ways for a certificate to become invalid, apart from expiring: for example, if you switch from standard, self signed, printer certificates to official SSL-certificates; if your printer software is upgraded and it generates a new certificate; or if a printer is simply changed for a new one with the old name. In any of these situations, CUPS will not renew the cached certificate, but will only complain with a rather generic message \"no suitable destination found\".

This is, unfortunately, not fixed by removing and re-installing the printer: even then, the invalid certificates are kept on the file system. The only way to fix this is to manually remove the certificates.
