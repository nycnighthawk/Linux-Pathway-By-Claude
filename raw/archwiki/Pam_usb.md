---
{"title": "Pam usb", "url": "https://wiki.archlinux.org/title/Pam_usb", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Pam usb

Related articles

-   [Security](../en/Security.html "Security")
-   [pam_mount](../en/Pam_mount.html "Pam mount")
-   [pam_abl](../en/Pam_abl.html "Pam abl")
-   [pam_oath](../en/Pam_oath.html "Pam oath")

[pam_usb](https://github.com/mcdope/pam_usb/) (active fork of the [original repo](https://github.com/aluzzardi/pam_usb)) provides hardware authentication for Linux using ordinary USB Flash Drives.

It works with any application supporting [PAM](../en/PAM.html "PAM"), such as [su](../en/Su.html "Su") and [Display manager](../en/Display_manager.html "Display manager").

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [pam_usb](https://aur.archlinux.org/packages/pam_usb/)^AUR^ package.

## Configuration {#Configuration}

Setting up pam_usb requires the following, once pam_usb is installed:

1.  Set up devices and users
2.  Configuring PAM for system authentication

### Setting up Devices and Users {#Setting_up_Devices_and_Users}

Once you have connected your USB device to the computer, use pamusb-conf to add it to the configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# pamusb-conf --add-device MyDevice
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Please select the device you wish to add.
* Using "SanDisk Corp. Cruzer Titanium (SNDKXXXXXXXXXXXXXXXX)" (only option)
Which volume would you like to use for storing data ?
* Using "/dev/sda1 (UUID: <6F6B-42FC>)" (only option)
Name            : MyDevice
Vendor          : SanDisk Corp.
Model           : Cruzer Titanium
Serial          : SNDKXXXXXXXXXXXXXXXX
Volume UUID     : 6F6B-42FC (/dev/sda1)
Save to /etc/pamusb.conf ?
[Y/n] y
Done.
```

Note that `MyDevice` can be any arbitrary name you would like. Also, you can add as many devices as you want.

Next, configure users you want to be able to authenticate with pam_usb:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# pamusb-conf --add-user root
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
      
Which device would you like to use for authentication ?
* Using "MyDevice" (only option)
User            : root
Device          : MyDevice
Save to /etc/pamusb.conf ?
[Y/n] y
Done.
```

### Check the configuration {#Check_the_configuration}

You can run `pamusb-check` anytime to check if everything is correctly worked. This tool will simulate an authentication request (requires your device to be connected, otherwise it will fail).

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# pamusb-check root
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
* Authentication request for user "root" (pamusb-check)
* Device "MyDevice" is connected (good).
* Performing one time pad verification...
* Verification match, updating one time pads...
* Access granted.
```

### Setting up the PAM module {#Setting_up_the_PAM_module}

To add pam_usb into the system authentication process, we need to edit `/etc/pam.d/system-auth`

The default PAM configuration file should include the following line:

    auth    [success=2 default=ignore]        pam_unix.so try_first_pass nullok_secure

Change it to:

    auth    sufficient                    pam_usb.so
    auth    [success=2 default=ignore]    pam_unix.so nullok_secure

The `sufficient` keyword means that if pam_usb allows the authentication, then no password will be asked. If the authentication fails, then the default password-based authentication will be used as fallback.

If you change it to `required`, it means that both the USB flash drive and the password will be required to grant access to the system.

Now you should be able to authenticate with the relevant USB device plugged-in.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ su
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
* pam_usb v.SVN
* Authentication request for user "root" (su)
* Device "MyDevice" is connected (good).
* Performing one time pad verification...
* Verification match, updating one time pads...
* Access granted.
```

### Enabling events management {#Enabling_events_management}

pam_usb provides support for *lock* and *unlock* events that can trigger a user-defined list of commands along with custom environment variables. For instance, it can be used to instruct pam_usb to automatically lock the current session upon removal of a configured USB device, via the *lock* event.

There are two pre-requisites for the configured events to be triggered upon a configured USB device insertion/removal:

1.  The *lock* and/or *unlock* events configuration must be added to the pam_usb configuration file;
2.  The `pamusb-agent` must be running.

Both topics above are fully descibed in the [pam_usb](https://github.com/mcdope/pam_usb/wiki/Configuration#agent)\'s wiki.

Here is an example of events configuration for a given user. Note that it also takes care of passing the DISPLAY and dbus environment details to the commands to be executed upon events. Both `<env>` and `<cmd>` elements content should be changed according to the target environment:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/security/pam_usb.conf abstract
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
<user id="auser">
    <device>MyUSBKey</device>
    <agent event="lock">
      <cmd>xfce4-screensaver-command --lock</cmd>
      <env>DISPLAY=:0.0</env>
      <env>DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus</env>
    </agent>
    <agent event="unlock">
      <cmd>xfce4-screensaver-command --deactivate</cmd>
      <env>DISPLAY=:0.0</env>
      <env>DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus</env>
    </agent>
</user>
...
```

Note that although the [pam_usb](https://aur.archlinux.org/packages/pam_usb/)^AUR^ package installs pamusb-agent, it does not configure the system to either manage or start it automatically, this has to be taken care of manually post-installation as a service or simply as a session program, e.g. via Xfce *Session and Startup* \'s *Application Autostart* control panel.

## Troubleshooting {#Troubleshooting}

### su fails to use pam_usb {#su_fails_to_use_pam_usb}

If you set:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pam.d/system-auth
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
auth          sufficient   pam_usb.so
```

and `su` prompts for a password, and does not use pam_usb, add the same line at the beginning of `/etc/pam.d/su`. This may be required for other pam-aware applications as well.

### pamusb-check only works with elevated privileges (sudo) {#pamusb-check_only_works_with_elevated_privileges_(sudo)}

To confirm that this is the same problem, run `pamusb-check --debug <non-root-user>`. Check that the output contains the line `Cannot open device file: Permission denied`.

By default the `device pad` is only accessible to privileged users/processes. To use the device to elevate your privileges, the `device pad` needs to be accessible to you.

To solve this:

1.  Create a new group that will have access to the file `sudo groupadd pamusb`.
2.  Add all users, who should be able to use the device, to the group with `sudo usermod -aG pamusb <username>` e.g.
    1.  Your own user.
    2.  Any system users which will authenticate you, like for instance `sddm`
    3.  etc.
3.  Mount the device and navigate to it (The next steps assume the working directory is the root of the device).
4.  Change the ownership of the `.pamusb` directory and the `device pad` file to the `pamusb` group.
    -   `sudo chown -R <user>:pamusb .pamusb`
    -   Any user added to the `pamusb` group should work.
5.  Add permissions so that any one in the group can read, write and execute everything in the `.pamusb` directory.
    -   `sudo chmod -R u+rwx,g+rwx .pamusb`

`pamusb-check --debug <non-root-user>` should now work without elevated privileges.

## See also {#See_also}

-   [Github repository](https://github.com/mcdope/pam_usb)
-   [Github wiki](https://github.com/mcdope/pam_usb/wiki)
