---
{"title": "NetworkManager", "url": "https://wiki.archlinux.org/title/NetworkManager", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# NetworkManager

Related articles

-   [Network configuration](../en/Network_configuration.html "Network configuration")
-   [Wireless network configuration](../en/Wireless_network_configuration.html "Wireless network configuration")

[NetworkManager](https://en.wikipedia.org/wiki/NetworkManager "wikipedia:NetworkManager") is a program for providing detection and configuration for systems to automatically connect to networks.

[NetworkManager](https://networkmanager.dev/) can be useful for both wireless and wired networks. For wireless networks, NetworkManager prefers known wireless networks and has the ability to switch to the most reliable network. NetworkManager-aware applications can switch from online and offline mode.

NetworkManager also prefers wired connections over wireless ones, has support for modem connections and certain types of VPN.

**Warning** By default, secrets---e.g. Wi-Fi passwords---are accessible to the root user in the filesystem and to users with access to settings via the GUI (e.g. via [#nm-applet](#nm-applet)). For more information, see [#Encrypted network keyphrases](#Encrypted_network_keyphrases).

## Installation {#Installation}

NetworkManager can be [installed](../en/Help:Reading.html#Installation_of_packages "Install") with the package [networkmanager](https://archlinux.org/packages/?name=networkmanager), which contains a daemon, a command line interface (*nmcli*) and a curses‐based interface (*nmtui*).

### Enable NetworkManager {#Enable_NetworkManager}

After installation, you should [start/enable](../en/Help:Reading.html#Control_of_systemd_units "Start/enable") `NetworkManager.service`. Once the NetworkManager daemon is started, it will automatically connect to any available \"system connections\" that have already been configured. Any \"user connections\" or unconfigured connections will need *nmcli* or an applet to configure and connect.

**Note**

-   Each network interface should be managed by only one [DHCP client or network manager](../en/Network_configuration.html#Network_managers "Network configuration"), so it is advised to run only one DHCP client or network manager on the system. Find a list of the currently running services with `systemctl --type=service` and then [stop](../en/Help:Reading.html#Control_of_systemd_units "Stop") or reconfigure those that conflict.
-   If [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved") is not [started](../en/Help:Reading.html#Control_of_systemd_units "Started"), an error message will start flooding your logs. See [#Unit dbus-org.freedesktop.resolve1.service not found](#Unit_dbus-org.freedesktop.resolve1.service_not_found) for more info.

### Additional interfaces {#Additional_interfaces}

-   [nm-connection-editor](https://archlinux.org/packages/?name=nm-connection-editor) for a graphical user interface,
-   [network-manager-applet](https://archlinux.org/packages/?name=network-manager-applet) for a system tray applet (see the [#nm-applet](#nm-applet) section).

### Mobile broadband support {#Mobile_broadband_support}

NetworkManager uses [ModemManager](../en/Mobile_broadband_modem.html#ModemManager "ModemManager") for mobile broadband connection support.

[Install](../en/Help:Reading.html#Installation_of_packages "Install") [modemmanager](https://archlinux.org/packages/?name=modemmanager) and [usb_modeswitch](https://archlinux.org/packages/?name=usb_modeswitch). Afterwards [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") and [start](../en/Help:Reading.html#Control_of_systemd_units "Start") `ModemManager.service`.

It may be necessary to [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `NetworkManager.service` for it to detect ModemManager. After you restart it, re-plug the modem again and it should be recognized.

Add connections from a front-end (e.g. [nm-connection-editor](https://archlinux.org/packages/?name=nm-connection-editor)) and select mobile broadband as the connection type. After selecting your ISP and billing plan, [APN](https://en.wikipedia.org/wiki/Access_Point_Name "wikipedia:Access Point Name") and other settings should be filled in automatically using information from [mobile-broadband-provider-info](https://archlinux.org/packages/?name=mobile-broadband-provider-info).

### PPPoE / DSL support {#PPPoE_/_DSL_support}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") [ppp](https://archlinux.org/packages/?name=ppp) package for PPPoE / DSL connection support. To actually add PPPoE connection, use `nm-connection-editor` and add new DSL/PPPoE connection.

### VPN support {#VPN_support}

NetworkManager since version 1.16 has native support for [WireGuard](../en/WireGuard.html "WireGuard"), all it needs is the `wireguard` kernel module. Read the [WireGuard in NetworkManager blog post](https://blogs.gnome.org/thaller/2019/03/15/wireguard-in-networkmanager/) for details.

Support for other VPN types is based on a plug-in system. They are provided in the following packages:

-   [networkmanager-openconnect](https://archlinux.org/packages/?name=networkmanager-openconnect) for [OpenConnect](../en/OpenConnect.html "OpenConnect")
-   [networkmanager-openvpn](https://archlinux.org/packages/?name=networkmanager-openvpn) for [OpenVPN](../en/OpenVPN.html "OpenVPN")
-   [networkmanager-pptp](https://archlinux.org/packages/?name=networkmanager-pptp) for [PPTP Client](../en/PPTP_Client.html "PPTP Client")
-   [networkmanager-strongswan](https://archlinux.org/packages/?name=networkmanager-strongswan) for [strongSwan](../en/StrongSwan.html "StrongSwan")
-   [networkmanager-vpnc](https://archlinux.org/packages/?name=networkmanager-vpnc)
-   [networkmanager-fortisslvpn](https://aur.archlinux.org/packages/networkmanager-fortisslvpn/)^AUR^
-   [networkmanager-iodine-git](https://aur.archlinux.org/packages/networkmanager-iodine-git/)^AUR^
-   [networkmanager-libreswan](https://aur.archlinux.org/packages/networkmanager-libreswan/)^AUR^
-   [networkmanager-l2tp](https://archlinux.org/packages/?name=networkmanager-l2tp)
-   [networkmanager-ssh](https://aur.archlinux.org/packages/networkmanager-ssh/)^AUR^
-   [network-manager-sstp](https://archlinux.org/packages/?name=network-manager-sstp)

**Warning** There are a lot of [bugs](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues?search=VPN&state=opened) related to VPN support. Check the daemon processes options set via the GUI correctly and double-check with each package release.

**Note**

-   To have fully functioning DNS resolution when using VPN, you should set up [conditional forwarding](#DNS_caching_and_conditional_forwarding).
-   These plug-ins may not have a documented command line interface, or may not work at all without an applet running. This is not an issue if you are using a regular desktop environment; if you are not, you should run [#nm-applet](#nm-applet) while configuring or activating the connection so that you get the necessary dialogues. [\[1\]](https://bbs.archlinux.org/viewtopic.php?id=246698)

## Usage {#Usage}

NetworkManager comes with [nmcli(1)](https://man.archlinux.org/man/nmcli.1) and [nmtui(1)](https://man.archlinux.org/man/nmtui.1).

### nmcli examples {#nmcli_examples}

List nearby Wi-Fi networks:

    $ nmcli device wifi list

Connect to a Wi-Fi network:

    $ nmcli device wifi connect SSID_or_BSSID password password

Connect to a hidden Wi-Fi network:

    $ nmcli device wifi connect SSID_or_BSSID password password hidden yes

Connect to a Wi-Fi on the `wlan1` interface:

    $ nmcli device wifi connect SSID_or_BSSID password password ifname wlan1 profile_name

Disconnect an interface:

    $ nmcli device disconnect ifname eth0

Get a list of connections with their names, UUIDs, types and backing devices:

    $ nmcli connection show

Activate a connection (i.e. connect to a network with an existing profile):

    $ nmcli connection up name_or_uuid

Show the `connection.autoconnect` field of a connection to determine if a connection will automatically connect.

    $ nmcli --fields connection.autoconnect connection show name_or_uuid

Set a connection to automatically connect.

    $ nmcli connection modify name_or_uuid connection.autoconnect yes

Delete a connection:

    $ nmcli connection delete name_or_uuid

See a list of network devices and their state:

    $ nmcli device

Turn off Wi-Fi:

    $ nmcli radio wifi off

### Edit a connection {#Edit_a_connection}

For a comprehensive list of settings, see [nm-settings(5)](https://man.archlinux.org/man/nm-settings.5).

Firstly, you need to get a list of connections:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ nmcli connection
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
NAME                UUID                                  TYPE      DEVICE
Wired connection 2  e7054040-a421-3bef-965d-bb7d60b7cecf  ethernet  enp5s0
Wired connection 1  997f2782-f0fc-301d-bfba-15421a2735d8  ethernet  enp0s25
MY-HOME-WIFI-5G     92a0f7b3-2eba-49ab-a899-24d83978f308  wifi       --
```

Here you can use the first column as connection-id used later. In this example, we pick `Wired connection 2` as a connection-id.

You have three methods to configure a connection `Wired connection 2` after it has been created:

nmcli interactive editor
:   `nmcli connection edit 'Wired connection 2'`.\
    Usage is well documented from the editor.

&nbsp;

nmcli command line interface
:   `nmcli connection modify 'Wired connection 2' `*`setting`*`.`*`property`*` `*`value`*. See [nmcli(1)](https://man.archlinux.org/man/nmcli.1) for usage. For example, you can change its IPv4 route metric to 200 using `nmcli connection modify 'Wired connection 2' ipv4.route-metric 200` command.

To remove a setting, pass an empty field (\"\") to it like this:

`nmcli connection modify 'Wired connection 2' `*`setting`*`.`*`property`*` ""`

Connection file
:   In `/etc/NetworkManager/system-connections/`, modify the corresponding `Wired connection 2.nmconnection` file .\
    Do not forget to reload the configuration file with `nmcli connection reload`.

### nmtui

NetworkManager ships a text user interface (TUI) for managing connections, the system hostname and radio switches. It can be launched by running `nmtui`.

## Front-ends {#Front-ends}

To provide integration with a [desktop environment](../en/Desktop_environment.html "Desktop environment"), most users will want to install an applet. This not only provides easy access to network selection and configuration, but also provides the agent necessary for securely storing secrets. Various desktop environments have their own applet; otherwise, you can use [#nm-applet](#nm-applet).

### GNOME {#GNOME}

[GNOME](../en/GNOME.html "GNOME") has a built-in tool, accessible from the Network settings.

### KDE Plasma {#KDE_Plasma}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [plasma-nm](https://archlinux.org/packages/?name=plasma-nm) package. After that, add it to the KDE taskbar via the *Panel options \> Add widgets \> Networks* menu.

### nm-applet

[network-manager-applet](https://archlinux.org/packages/?name=network-manager-applet) is a GTK 3 front-end which works under Xorg environments with a systray.

To store connection secrets install and configure an application which implements the [Secret Service D-Bus API](https://specifications.freedesktop.org/secret-service-spec/latest/) such as [GNOME/Keyring](../en/GNOME/Keyring.html "GNOME/Keyring"), [KDE Wallet](../en/KDE_Wallet.html "KDE Wallet"), or [KeePassXC](../en/KeePass.html "KeePassXC").

Be aware that after enabling the tick-box option `Make available to other users` for a connection, NetworkManager stores the password in plain-text, though the respective file is accessible only to root (or other users via `nm-applet`). See [#Encrypted network keyphrases](#Encrypted_network_keyphrases).

In order to run `nm-applet` without a systray, you can use [trayer](https://aur.archlinux.org/packages/trayer/)^AUR^ or [stalonetray](https://archlinux.org/packages/?name=stalonetray). For example, you can add a script like this one in your path:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
nmgui
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh
nm-applet    2>&1 > /dev/null &
stalonetray  2>&1 > /dev/null
killall nm-applet
```

When you close the *stalonetray* window, it closes `nm-applet` too, so no extra memory is used once you are done with network settings.

The applet can show notifications for events such as connecting to or disconnecting from a Wi-Fi network. For these notifications to display, ensure that you have a notification server installed - see [Desktop notifications](../en/Desktop_notifications.html "Desktop notifications"). If you use the applet without a notification server, you might see some messages in stdout/stderr, and the applet might hang. See [\[2\]](https://bugzilla.gnome.org/show_bug.cgi?id=788313).

In order to run `nm-applet` with such notifications disabled, start the applet with the following command:

    $ nm-applet --no-agent

**Tip** `nm-applet` might be started automatically with a [autostart desktop file](../en/XDG_Autostart.html "XDG Autostart"), to add the `--no-agent` option modify the Exec line there, i.e.

    Exec=nm-applet --no-agent

**Warning** On [i3](../en/I3.html "I3"), if nm-applet is started with the `--no-agent` option, it is not possible to connect to a new encrypted Wi-Fi network by clicking on the item list because no password input dialogue window will pop out. [journal](../en/Systemd/Journal.html "Journal") will show `no secrets: No agents were available for this request`.

#### Appindicator {#Appindicator}

As of version 1.18.0 Appindicator support is [available](https://gitlab.archlinux.org/archlinux/packaging/packages/network-manager-applet/-/commit/527448fb2a87d85055f504f463dfe961dccd75c3) in the official [network-manager-applet](https://archlinux.org/packages/?name=network-manager-applet) package. To use nm-applet in an Appindicator environment start the applet with the following command:

    $ nm-applet --indicator

### networkmanager-dmenu

Alternatively there is [networkmanager-dmenu](https://archlinux.org/packages/?name=networkmanager-dmenu) which is a small script to manage NetworkManager connections with [dmenu](../en/Dmenu.html "Dmenu") or [rofi](../en/Rofi.html "Rofi") instead of `nm-applet`. It provides all essential features such as connection to existing NetworkManager Wi-Fi or wired connections, connect to new Wi-Fi connections, requests passphrase if required, connect to existing VPN connections, enable/disable networking, launch *nm-connection-editor* GUI, connect to Bluetooth networks.

### switchboard

Pantheon\'s [switchboard](https://archlinux.org/packages/?name=switchboard) offers a desktop environment-agnostic way to configure NetworkManager when combined with [switchboard-plug-network](https://archlinux.org/packages/?name=switchboard-plug-network) and [nm-connection-editor](https://archlinux.org/packages/?name=nm-connection-editor). It can be ran with the following command:

    $ io.elementary.settings

### Network Manager Sidebar {#Network_Manager_Sidebar}

[Network Manager Sidebar](../en/Network_Manager_Sidebar.html "Network Manager Sidebar") is a GTK4/libadwaita front-end for NetworkManager on [Wayland](../en/Wayland.html "Wayland") compositors supporting layer-shell.

### wifitui

[wifitui](https://aur.archlinux.org/packages/wifitui/)^AUR^ is a TUI written in Go using bubbletea. It's inspired by impala and is similar to nmtui, but can scan wifi-networks directly and offers a nice UI.

## Configuration {#Configuration}

NetworkManager may require some additional steps to be able run properly. Make sure you have configured `/etc/hosts` as described in [Network configuration#Set the hostname](../en/Network_configuration.html#Set_the_hostname "Network configuration") section.

NetworkManager has a global configuration file at `/etc/NetworkManager/NetworkManager.conf`. Additional configuration files can be placed in `/etc/NetworkManager/conf.d/`. Usually no configuration needs to be done to the global defaults.

After editing a configuration file, the changes can be applied by running:

    # nmcli general reload

### NetworkManager-wait-online {#NetworkManager-wait-online}

Enabling `NetworkManager.service` also enables `NetworkManager-wait-online.service`, which is a oneshot system service that waits for the network to be configured. The latter has `WantedBy=network-online.target`, so it will finish only when `network-online.target` itself is enabled or pulled in by some other unit. See also [systemd#Running services after the network is up](../en/Systemd.html#Running_services_after_the_network_is_up "Systemd").

By default, `NetworkManager-wait-online.service` waits for NetworkManager startup to complete, rather than waiting for network connectivity specifically (see [nm-online(1)](https://man.archlinux.org/man/nm-online.1)). If `NetworkManager-wait-online.service` finishes before the network is really up, resulting in failed services on boot, [extend the unit](../en/Extend_the_unit.html "Extend the unit") to remove the `-s` from the `ExecStart` line:

    [Service]
    ExecStart=
    ExecStart=/usr/bin/nm-online -q

Be aware that this can cause [other issues](https://lists.fedoraproject.org/archives/list/users@lists.fedoraproject.org/thread/EGC324JD3HJCGVN7J55WYPRLFDA3TP7N/).

In some cases, the service will still fail to start successfully on boot due to the timeout setting being too short. [Edit](../en/Systemd.html#Editing_provided_units "Edit") the service to change `NM_ONLINE_TIMEOUT` from `60` to a higher value.

### Set up PolicyKit permissions {#Set_up_PolicyKit_permissions}

By default, all users in active local sessions are allowed to change most network settings without a password. See [General troubleshooting#Session permissions](../en/General_troubleshooting.html#Session_permissions "General troubleshooting") to check your session type. In most cases, everything should work out of the box.

Some actions (such as changing the system hostname) require an administrator password. In this case, you need to [add](../en/Users_and_groups.html#Group_management "Users and groups") yourself to the `wheel` group and run a [Polkit authentication agent](../en/Polkit.html#Authentication_agents "Polkit") which will prompt for your password.

For remote sessions (e.g. [headless VNC](../en/TigerVNC.html#Running_vncserver_for_virtual_(headless)_sessions "TigerVNC")), you have several options for obtaining the necessary privileges to use NetworkManager:

1.  [Add](../en/Users_and_groups.html#Group_management "Users and groups") yourself to the `wheel` group. You will have to enter your password for every action. Note that your user account may be granted other permissions as well, such as the ability to use [sudo](../en/Sudo.html "Sudo") without entering the root password.

2.  [Add](../en/Users_and_groups.html#Group_management "Users and groups") yourself to the `network` group and create `/etc/polkit-1/rules.d/50-org.freedesktop.NetworkManager.rules` with the following content:

        polkit.addRule(function(action, subject) {
          if (action.id.indexOf("org.freedesktop.NetworkManager.") == 0 && subject.isInGroup("network")) {
            return polkit.Result.YES;
          }
        });

    All users in the `network` group will be able to add and remove networks without a password (which means you do not have to run a Polkit authentication agent, so this option will also work in SSH sessions).

### Proxy settings {#Proxy_settings}

NetworkManager does support some proxy settings. While they can not be directly modified using *nmtui*, *nm-applet* and *nmcli* support those. See the proxy settings in [nm-settings-nmcli(5)](https://man.archlinux.org/man/nm-settings-nmcli.5).

Additionally, custom proxy commands can always be run using dispatcher scripts, see [#Dispatcher examples](#Dispatcher_examples).

See also [Proxy settings](../en/Proxy_settings.html "Proxy settings").

### Checking connectivity {#Checking_connectivity}

NetworkManager can try to reach a webserver after connecting to a network in order to determine if it is e.g behind a captive portal. The default host (configured in `/usr/lib/NetworkManager/conf.d/20-connectivity.conf`) is [ping.archlinux.org](https://ping.archlinux.org) (a CNAME alias of redirect.archlinux.org). To use a different webserver or to disable connectivity checking, create `/etc/NetworkManager/conf.d/20-connectivity.conf`, see [NetworkManager.conf(5) § CONNECTIVITY SECTION](https://man.archlinux.org/man/NetworkManager.conf.5#CONNECTIVITY_SECTION). Below is an example of using GNOME servers (it does not require the use of [GNOME](../en/GNOME.html "GNOME")):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/20-connectivity.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[connectivity]
uri=http://nmcheck.gnome.org/check_network_status.txt
```

To disable NetworkManager\'s connectivity check, use the following configuration. This can be useful when connected to a VPN that blocks connectivity checks.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/20-connectivity.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[connectivity]
enabled=false
```

**Note** Although automatic connectivity checks are a potential privacy leak, Arch Linux\'s default connectivity URL is committed to not logging any access. See [\[3\]](https://gitlab.archlinux.org/archlinux/infrastructure/-/commit/fabccd0f61e5dea3925e8a0c6a46d56d5750c121#a4f34381bbb18ea77bfb3dd11a8aeca707078fca_0_26) [\[4\]](https://gitlab.archlinux.org/archlinux/infrastructure/-/blob/master/roles/ping/templates/nginx.d.conf.j2).

### Captive portals {#Captive_portals}

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** Complex scripts should not be maintained on the wiki. (Discuss in [Talk:NetworkManager](../en/Talk:NetworkManager.html))

For those behind a [captive portal](https://en.wikipedia.org/wiki/Captive_portal "wikipedia:Captive portal"), the desktop manager may automatically open a window asking for credentials. If your desktop does not, you can use [capnet-assist](https://archlinux.org/packages/?name=capnet-assist) package (however, it currently has a broken NetworkManager dispatcher script). Alternatively, you can create a NetworkManager dispatcher script with the following content:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/90-open_captive_portal
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh -e
# Script to dispatch NetworkManager events
#
# Runs shows a login webpage on walled garden networks.
# See NetworkManager(8) for further documentation of the dispatcher events.

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

if [ -x "/usr/bin/logger" ]; then
    logger="/usr/bin/logger -s -t captive-portal"
else
    logger=":"
fi

wait_for_process() {
    PNAME=$1
    while [ -z "$(/usr/bin/pgrep $PNAME)" ]; do
        sleep 3;
    done
}

#launch the browser, but on boot we need to wait that nm-applet starts
start_browser() {
    local user="$1"
    local display="$2"

    export DISPLAY="$display"
    wait_for_process nm-applet

    export XAUTHORITY="/home/$user/.Xauthority"

    $logger "Running browser as '$user' with display '$display' to login in captive portal"
    sudo -u "$user" --preserve-env=DISPLAY,XAUTHORITY -H xdg-open http://capnet.elementary.io 2>&1 > /dev/null
}

# Run the right scripts
case "$2" in
    connectivity-change)
    $logger -p user.debug "dispatcher script triggered on connectivity change: $CONNECTIVITY_STATE"
    if [ "$CONNECTIVITY_STATE" = "PORTAL" ]; then
        # Match last column of who's output with ' :[at least one digit] '
        who | awk '$NF ~ /\(:[0-9]+\)/ { print $1 " " substr($NF, 2, length($NF)-2) };' | \
        while read user display; do
            start_browser $user $display || $logger -p user.err "Failed for user: '$user' display: '$display'"
        done
    fi
    ;;
    *)
    # In a down phase
    exit 0
    ;;
esac
```

Make the script [executable](../en/Help:Reading.html#Make_executable "Executable"). But that script assumes you use X and simply opens http page. It might not work for everyone.

You will need to [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `NetworkManager.service` or reboot for this to start working. Once you do, the dispatcher script should open a login window once it detects you are behind a captive portal.

Simple solution is [captive-portal-sh](https://github.com/Seme4eg/captive-portal-sh) - shell script that obtains captive portal URL and opens it in your default browser (for Wayland users only).

Another solution is [captive-browser-git](https://aur.archlinux.org/packages/captive-browser-git/)^AUR^ based on Google Chrome.

#### iwd support for captive portal support on legacy hardware {#iwd_support_for_captive_portal_support_on_legacy_hardware}

Some older Wi-Fi chips (e.g. Broadcom BCM4360) require the proprietary `wl` driver, which lacks support for the OWE/Elliptic-Curve handshake that many captive-portal hotspots use before presenting a login page. By switching NetworkManager's Wi-Fi backend to `iwd` (see [#Using iwd as the Wi-Fi backend](#Using_iwd_as_the_Wi-Fi_backend)), which implements the full OWE key exchange in userspace over the existing driver, you can complete the encrypted association, obtain a DHCP lease, and trigger the portal "PORTAL" state. Once that is done, any dispatcher script or browser-launcher will reliably pop up the login page on hardware that otherwise could never fully connect.

### DHCP client {#DHCP_client}

By default NetworkManager uses its internal DHCP client. The internal DHCPv4 plugin is based on the [nettools\' n-dhcp4](https://nettools.github.io/n-dhcp4/) library, while the internal DHCPv6 plugin is made from code based on systemd-networkd.

It is possible for NetworkManager to use [dhcpcd](../en/Dhcpcd.html "Dhcpcd") instead. Install [dhcpcd](https://archlinux.org/packages/?name=dhcpcd) and set the option `main.dhcp=dhcpcd` with a configuration file in `/etc/NetworkManager/conf.d/`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/dhcp-client.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[main]
dhcp=dhcpcd
```

**Note** Do not enable the systemd units shipped with the [dhcpcd](https://archlinux.org/packages/?name=dhcpcd) package. They will conflict with NetworkManager, see the note in [#Installation](#Installation) for details.

### DNS management {#DNS_management}

NetworkManager\'s DNS management is described in the GNOME project\'s wiki page---[Projects/NetworkManager/DNS](https://wiki.gnome.org/Projects/NetworkManager/DNS).

#### DNS caching and conditional forwarding {#DNS_caching_and_conditional_forwarding}

NetworkManager has a plugin to enable DNS caching and conditional forwarding ([previously](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/merge_requests/143) called \"split DNS\" in NetworkManager\'s documentation) using [dnsmasq](../en/Dnsmasq.html "Dnsmasq") or [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved"). The advantages of this setup is that DNS lookups will be cached, shortening resolve times, and DNS lookups of VPN hosts will be routed to the relevant VPN\'s DNS servers. This is especially useful if you are connected to more than one VPN.

**Note** If `/etc/resolv.conf` is a symlink to `/run/systemd/resolve/stub-resolv.conf`, `/run/systemd/resolve/resolv.conf`,`/lib/systemd/resolv.conf` or `/usr/lib/systemd/resolv.conf`, NetworkManager will choose systemd-resolved automatically. To use dnsmasq, you must first remove that symlink, then restart NetworkManager.

##### dnsmasq

Make sure [dnsmasq](https://archlinux.org/packages/?name=dnsmasq) has been installed. Then set `main.dns=dnsmasq` with a configuration file in `/etc/NetworkManager/conf.d/`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/dns.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[main]
dns=dnsmasq
```

Now run `nmcli general reload` as root. NetworkManager will automatically start dnsmasq and add `127.0.0.1` to `/etc/resolv.conf`. The original DNS servers can be found in `/run/NetworkManager/no-stub-resolv.conf`. You can verify dnsmasq is being used by doing the same DNS lookup twice with `drill example.com` and verifying the server and query times.

**Note**

-   You do not need to start `dnsmasq.service` or edit `/etc/dnsmasq.conf`. NetworkManager will start dnsmasq without using the systemd service and without reading the dnsmasq\'s default configuration file(s).
-   The dnsmasq instance started by NetworkManager will bind to `127.0.0.1:53`, you cannot run any other software (including `dnsmasq.service`) on the same address and port.

**Tip** To clear the DNS cache, [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `NetworkManager.service`.

###### Custom dnsmasq configuration {#Custom_dnsmasq_configuration}

Custom configurations can be created for *dnsmasq* by creating configuration files in `/etc/NetworkManager/dnsmasq.d/`. For example, to change the size of the DNS cache (which is stored in RAM):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dnsmasq.d/cache.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
cache-size=1000
```

You can check the configuration file syntax with:

    $ dnsmasq --test --conf-file=/dev/null --conf-dir=/etc/NetworkManager/dnsmasq.d

See [dnsmasq(8)](https://man.archlinux.org/man/dnsmasq.8) for all available options.

###### IPv6 {#IPv6}

**The factual accuracy of this article or section is disputed.**

**Reason:** This does not solve the issue because NetworkManager does not add `::1` to `/etc/resolv.conf`. Unless `@::1` is manually passed to drill, it will still fail with `Error: error sending query: No (valid) nameservers defined in the resolver`. (Discuss in [Talk:NetworkManager](../en/Talk:NetworkManager.html))

Enabling `dnsmasq` in NetworkManager may break IPv6-only DNS lookups (i.e. `drill -6 [hostname]`) which would otherwise work. In order to resolve this, creating the following file will configure *dnsmasq* to also listen to the IPv6 loopback:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dnsmasq.d/ipv6-listen.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
listen-address=::1
```

In addition, `dnsmasq` also does not prioritize upstream IPv6 DNS. Unfortunately NetworkManager does not do this ([Ubuntu Bug](https://bugs.launchpad.net/ubuntu/+source/network-manager/+bug/936712)). A workaround would be to disable IPv4 DNS in the NetworkManager config, assuming one exists.

###### DNSSEC {#DNSSEC}

The dnsmasq instance started by NetworkManager by default will not validate [DNSSEC](../en/DNSSEC.html "DNSSEC"). To enable DNSSEC validation, thus breaking DNS resolution with name servers that do not support it, create the following configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dnsmasq.d/dnssec.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
conf-file=/usr/share/dnsmasq/trust-anchors.conf
dnssec
```

##### systemd-resolved

**This article or section needs expansion.**

**Reason:** NetworkManager 1.16 adds a new setting `main.systemd-resolved`[\[5\]](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/commit/d4eb4cb45f41b1751cacf71da558bf8f0988f383) (enabled by default). It unconditionally sends DNS configuration to systemd-resolved. Related to \"Preserving resolv.conf\" from [systemd-resolved#DNS](../en/Systemd-resolved.html#DNS "Systemd-resolved")? (Discuss in [Talk:NetworkManager](../en/Talk:NetworkManager.html))

NetworkManager can use [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved") as a DNS resolver and cache. Make sure that *systemd-resolved* is properly configured and that `systemd-resolved.service` is [started](../en/Help:Reading.html#Control_of_systemd_units "Started") before using it.

systemd-resolved will be used automatically if `/etc/resolv.conf` is a [symlink](../en/Systemd-resolved.html#DNS "Systemd-resolved") to `/run/systemd/resolve/stub-resolv.conf`, `/run/systemd/resolve/resolv.conf` or `/usr/lib/systemd/resolv.conf`.

You can enable it explicitly by setting `main.dns=systemd-resolved` with a configuration file in `/etc/NetworkManager/conf.d/`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/dns.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[main]
dns=systemd-resolved
```

##### DNS resolver with an openresolv subscriber {#DNS_resolver_with_an_openresolv_subscriber}

If [openresolv](../en/Openresolv.html "Openresolv") has a subscriber for your local [DNS resolver](../en/DNS_resolver.html "DNS resolver"), set up the subscriber and [configure NetworkManager to use openresolv](#Use_openresolv).

Because NetworkManager advertises a single \"interface\" to *resolvconf*, it is not possible to implement conditional forwarding between two NetworkManager connections. See [NetworkManager issue 153](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues/153).

This can be partially mitigated if you set `private_interfaces="*"` in `/etc/resolvconf.conf`[\[6\]](https://roy.marples.name/projects/openresolv/configuration/). Any queries for domains that are not in search domain list will not get forwarded. They will be handled according to the local resolver\'s configuration, for example, forwarded to another DNS server or resolved recursively from the DNS root.

#### Custom DNS servers {#Custom_DNS_servers}

##### Setting custom global DNS servers {#Setting_custom_global_DNS_servers}

To set DNS servers for all connections, specify them in [NetworkManager.conf(5)](https://man.archlinux.org/man/NetworkManager.conf.5) using the syntax `servers=`*`serveripaddress1`*`,`*`serveripaddress2`*`,`*`serveripaddress3`* in a section named `[global-dns-domain-*]`. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/dns-servers.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[global-dns-domain-*]
servers=::1,127.0.0.1
```

**Note**

-   If you use [NetworkManager\'s dnsmasq or systemd-resolved plugin](#DNS_caching_and_conditional_forwarding) or [openresolv subscribers](#DNS_resolver_with_an_openresolv_subscriber), then do not specify loopback addresses with the `servers=` option, it can break DNS resolution.
-   The specified servers do not get sent to [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved"), the connection\'s DNS servers are used instead. See [NetworkManager issue 1366](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/issues/1366) and [systemd issue 33754](https://github.com/systemd/systemd/issues/33754).

##### Setting custom DNS servers in a connection {#Setting_custom_DNS_servers_in_a_connection}

###### Setting custom DNS servers in a connection (GUI) {#Setting_custom_DNS_servers_in_a_connection_(GUI)}

Setup will depend on the type of front-end used; the process usually involves right-clicking on the applet, editing (or creating) a profile, and then choosing DHCP type as *Automatic (specify addresses)*. The DNS addresses will need to be entered and are usually in this form: `127.0.0.1, `*`DNS-server-one`*`, ...`.

###### Setting custom DNS servers in a connection (nmcli / connection file) {#Setting_custom_DNS_servers_in_a_connection_(nmcli_/_connection_file)}

To set up DNS Servers per connection, you change the `ipv4.dns` and `ipv6.dns` settings (and their associated `dns-search` and `dns-options`) in the [connection settings](#Edit_a_connection).

If `method` is set to `auto` (when you use DHCP/RA), you need to set `ignore-auto-dns` to `yes`.

To use DNS over TLS ([requires systemd-resolved](#systemd-resolved)), specify the DNS servers using the syntax `dns=`*`ip.address`*`#`*`servername`*`;` and additionally set the `connection.dns-over-tls` setting to `2`. For example, to use Quad9:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/system-connections/Example Wi-Fi.nmconnection
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
[connection]
...
dns-over-tls=2

[ipv4]
...
dns=9.9.9.9#dns.quad9.net;149.112.112.112#dns.quad9.net;
ignore-auto-dns=true

[ipv6]
...
dns=2620:fe::fe#dns.quad9.net;2620:fe::9#dns.quad9.net;
ignore-auto-dns=true
```

**Note** This example uses Quad9. Replace it with a DNS resolver you trust. See [Domain name resolution#Third-party DNS services](../en/Domain_name_resolution.html#Third-party_DNS_services "Domain name resolution").

#### /etc/resolv.conf {#/etc/resolv.conf}

NetworkManager\'s `/etc/resolv.conf` management mode is configured with the `main.rc-manager` setting. [networkmanager](https://archlinux.org/packages/?name=networkmanager) sets it to `symlink` as opposed to the upstream default `auto`. The setting and its values are documented in the [NetworkManager.conf(5)](https://man.archlinux.org/man/NetworkManager.conf.5) man page.

**Tip** Using openresolv allows NetworkManager to coexist with other *resolvconf* supporting software or, for example, to run a local DNS caching and split-DNS resolver for which openresolv has a [subscriber](../en/Openresolv.html#Subscribers "Openresolv"). Note that conditional forwarding is [not yet fully supported](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/issues/153) when using NetworkManager with openresolv.

*NetworkManager* also offers hooks via so called dispatcher scripts that can be used to alter the `/etc/resolv.conf` after network changes. See [#Network services with NetworkManager dispatcher](#Network_services_with_NetworkManager_dispatcher) and [NetworkManager(8)](https://man.archlinux.org/man/NetworkManager.8) for more information.

**Note**

-   If NetworkManager is configured to use either [dnsmasq](#dnsmasq) or [systemd-resolved](#systemd-resolved), then the appropriate loopback addresses will be written to `/etc/resolv.conf`.
-   The `resolv.conf` file NetworkManager writes or would write to `/etc/resolv.conf` can be found at `/run/NetworkManager/resolv.conf`.
-   A `resolv.conf` file with the acquired name servers and search domains can be found at `/run/NetworkManager/no-stub-resolv.conf`.

##### Unmanaged /etc/resolv.conf {#Unmanaged_/etc/resolv.conf}

To stop NetworkManager from touching `/etc/resolv.conf`, set `main.dns=none` with a configuration file in `/etc/NetworkManager/conf.d/`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/dns.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[main]
dns=none
```

**Tip** You might also want to set `main.systemd-resolved=false`, so that NetworkManager does not send the DNS configuration to [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved").

**Note** See [#DNS caching and conditional forwarding](#DNS_caching_and_conditional_forwarding), to configure NetworkManager using other DNS backends like [dnsmasq](../en/Dnsmasq.html "Dnsmasq") and [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved"), instead of using `main.dns=none`.

After that `/etc/resolv.conf` might be a broken symlink that you will need to remove. Then, just create a new `/etc/resolv.conf` file.

##### Use openresolv {#Use_openresolv}

**Note** NetworkManager does not support using systemd-resolved\'s *resolvconf* interface ([resolvectl(1) § COMPATIBILITY WITH RESOLVCONF(8)](https://man.archlinux.org/man/resolvectl.1#COMPATIBILITY_WITH_RESOLVCONF(8))) which is provided by [systemd-resolvconf](https://archlinux.org/packages/?name=systemd-resolvconf).

-   Do not set `main.rc-manager=resolvconf` when using [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved"), instead make sure to [correctly create the /etc/resolv.conf symlink](../en/Systemd-resolved.html#DNS "Systemd-resolved") or [configure NetworkManager to use systemd-resolved explicitly](#systemd-resolved).
-   Make sure the [systemd-resolvconf](https://archlinux.org/packages/?name=systemd-resolvconf) package is not installed when systemd-resolved is not used. Unless `systemd-resolved.service` started, it will break all networking software (not just NetworkManager) that use resolvconf.

To configure NetworkManager to use [openresolv](../en/Openresolv.html "Openresolv"), set `main.rc-manager=resolvconf` with a configuration file in `/etc/NetworkManager/conf.d/`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/rc-manager.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[main]
rc-manager=resolvconf
```

### Firewall {#Firewall}

You can [assign a firewalld zone](../en/Firewalld.html#Using_NetworkManager_to_manage_zones "Firewalld") based on your current connection. For example a restrictive firewall when at work, and a less restrictive one when at home.

This can also be done with [NetworkManager dispatcher](#Network_services_with_NetworkManager_dispatcher).

## Network services with NetworkManager dispatcher {#Network_services_with_NetworkManager_dispatcher}

There are quite a few network services that you will not want running until NetworkManager brings up an interface. NetworkManager has the ability to start services when you connect to a network and stop them when you disconnect (e.g. when using [NFS](../en/NFS.html "NFS"), [SMB](../en/Samba.html "SMB") and [NTPd](../en/Network_Time_Protocol_daemon.html "NTPd")).

To activate the feature you need to [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") and [start](../en/Help:Reading.html#Control_of_systemd_units "Start") the `NetworkManager-dispatcher.service`.

Once the service is active, scripts can be added to the `/etc/NetworkManager/dispatcher.d` directory.

Scripts must be owned by **root**, otherwise the dispatcher will not execute them. For added security, set group [ownership](../en/File_permissions_and_attributes.html#Changing_ownership "Ownership") to root as well:

    # chown root:root /etc/NetworkManager/dispatcher.d/10-script.sh

Make sure the file is [executable](../en/Help:Reading.html#Make_executable "Executable").

The scripts will be run in alphabetical order at connection time, and in reverse alphabetical order at disconnect time. To ensure what order they come up in, it is common to use numerical characters prior to the name of the script (e.g. `10-portmap` or `30-netfs` (which ensures that the *portmapper* is up before NFS mounts are attempted).

Scripts will receive the following arguments:

-   **Interface name:** e.g. `eth0`
-   **Action:** *up*, *down*, *vpn-up*, *vpn-down*, \... (see [NetworkManager-dispatcher(8)](https://man.archlinux.org/man/NetworkManager-dispatcher.8) for the complete list)

**Warning** If you connect to foreign or public networks, be aware of what services you are starting and what servers you expect to be available for them to connect to. You could make a security hole by starting the wrong services while connected to a public network.

### Avoiding the dispatcher timeout {#Avoiding_the_dispatcher_timeout}

If the above is working, then this section is not relevant. However, there is a general problem related to running dispatcher scripts which take longer to be executed. Initially an internal timeout of three seconds only was used. If the called script did not complete in time, it was killed. Later the timeout was extended to about 20 seconds (see the [Bugtracker](https://bugzilla.redhat.com/show_bug.cgi?id=982734) for more information). If the timeout still creates the problem, a work around may be to use a [drop-in file](../en/Drop-in_file.html "Drop-in file") for the `NetworkManager-dispatcher.service` to remain active after exit:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/NetworkManager-dispatcher.service.d/remain_after_exit.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
RemainAfterExit=yes
```

Now start and enable the modified `NetworkManager-dispatcher` service.

**Warning** Adding the `RemainAfterExit` line to it will prevent the dispatcher from closing. Unfortunately, the dispatcher **has** to close before it can run your scripts again. With it the dispatcher will not time out but it also will not close, which means that the scripts will only run once per boot. Therefore, do not add the line unless the timeout is definitely causing a problem.

### Dispatcher examples {#Dispatcher_examples}

#### Automatically set the timezone {#Automatically_set_the_timezone}

Create a [NetworkManager dispatcher script](#Network_services_with_NetworkManager_dispatcher) and make it [executable](../en/Help:Reading.html#Make_executable "Executable"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/09-timezone
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh
case "$2" in
    up)
        timedatectl set-timezone "$(curl --fail https://ipapi.co/timezone)"
    ;;
esac
```

This alternative script does not block other dispatcher scripts, nor is it activated by loopback/shared connections:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/09-timezone
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/env sh

[ "$2" = up ] && [ "$1" != lo ] || exit 0
[ "$(nmcli -g ipv4.method connection show uuid "$CONNECTION_UUID" 2>/dev/null)" \ 
    != shared ] || exit 0
systemd-run --quiet --no-block --collect --unit=nm-timezone sh -c \
    'tz=$(curl -sS --fail --max-time 60 https://ipapi.co/timezone) && \ 
    timedatectl set-timezone "$tz"' 2>/dev/null || :
```

**Tip** Using `connectivity-change` instead of `up` can prevent timezone changes when connecting to VPNs with clients such as [OpenConnect](../en/OpenConnect.html "OpenConnect").

Alternatively, the tool [tzupdate](https://aur.archlinux.org/packages/tzupdate/)^AUR^ automatically sets the timezone based on the geolocation of the IP address. This [comparison of the most popular IP geolocation apis](https://medium.com/@ipdata_co/what-is-the-best-commercial-ip-geolocation-api-d8195cda7027) may be helpful in deciding which API to use in production.

#### Mount remote directory with sshfs {#Mount_remote_directory_with_sshfs}

As the script is run in a very restrictive environment, you have to export `SSH_AUTH_SOCK` in order to connect to your SSH agent. There are different ways to accomplish this, see [this message](https://bbs.archlinux.org/viewtopic.php?pid=1042030#p1042030) for more information. The example below works with [GNOME Keyring](../en/GNOME_Keyring.html "GNOME Keyring"), and will ask you for the password if not unlocked already. In case NetworkManager connects automatically on login, it is likely *gnome-keyring* has not yet started and the export will fail (hence the sleep). The `UUID` to match can be found with the command `nmcli connection status` or `nmcli connection list`.

    #!/bin/sh
    USER='username'
    REMOTE='user@host:/remote/path'
    LOCAL='/local/path'

    interface=$1 status=$2
    if [ "$CONNECTION_UUID" = "uuid" ]; then
      case $status in
        up)
          # sleep 10
          SSH_AUTH_SOCK=$(find /tmp -maxdepth 1 -type s -user "$USER" -name 'ssh')
          export SSH_AUTH_SOCK
          su "$USER" -c "sshfs $REMOTE $LOCAL"
          ;;
        down)
          fusermount -u "$LOCAL"
          ;;
      esac
    fi

#### Mounting of SMB shares {#Mounting_of_SMB_shares}

Some [SMB](../en/Samba.html "SMB") shares are only available on certain networks or locations (e.g. at home). You can use the dispatcher to only mount SMB shares that are present at your current location.

The following script will check if we connected to a specific network and mount shares accordingly:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/30-mount-smb.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

# Find the connection UUID with "nmcli connection show" in terminal.
# All NetworkManager connection types are supported: wireless, VPN, wired...
if [ "$2" = "up" ]; then
  if [ "$CONNECTION_UUID" = "uuid" ]; then
    mount /your/mount/point & 
    # add more shares as needed
  fi
fi
```

The following script will unmount all SMB shares before a software initiated disconnect from a specific network:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/pre-down.d/30-umount-smb.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

if [ "$CONNECTION_UUID" = "uuid" ]; then
  umount -a -l -t cifs
fi
```

**Note** Make sure this script is located in the `pre-down.d` sub-directory as shown above, otherwise it will unmount all shares on any connection state change.

The following script will attempt to unmount all SMB shares following an unexpected disconnect from a specific network:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/40-umount-smb.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

if [ "$CONNECTION_UUID" = "uuid" ]; then
  if [ "$2" = "down" ]; then
    umount -a -l -t cifs
  fi
fi
```

**Note**

-   Since NetworkManager 0.9.8, the *pre-down* and *down* events are not executed on shutdown or restart, see [this bug report](https://bugzilla.gnome.org/show_bug.cgi?id=701242) for more info.
-   The previous *umount* scripts are still prone to leaving applications actually accessing the mount to \'hang\'.

An alternative is to use the script as seen in [NFS#Using a NetworkManager dispatcher](../en/NFS.html#Using_a_NetworkManager_dispatcher "NFS"):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/30-smb.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

# Find the connection UUID with "nmcli con show" in terminal.
# All NetworkManager connection types are supported: wireless, VPN, wired...
WANTED_CON_UUID="CHANGE-ME-NOW-9c7eff15-010a-4b1c-a786-9b4efa218ba9"

if [ "$CONNECTION_UUID" = "$WANTED_CON_UUID" ]; then
    
    # Script parameter $1: network interface name, not used
    # Script parameter $2: dispatched event
    
    case "$2" in
        "up")
            mount -a -t cifs
            ;;
        "down"|"pre-down"|"vpn-pre-down")
            umount -l -a -t cifs >/dev/null
            ;;
    esac
fi
```

**Note** This script ignores mounts with the `noauto` option, remove this mount option or use `auto` to allow the dispatcher to manage these mounts.

Create a symlink inside `/etc/NetworkManager/dispatcher.d/pre-down/` to catch the `pre-down` events:

    # ln -s ../30-smb.sh /etc/NetworkManager/dispatcher.d/pre-down.d/30-smb.sh

#### Mounting of NFS shares {#Mounting_of_NFS_shares}

See [NFS#Using a NetworkManager dispatcher](../en/NFS.html#Using_a_NetworkManager_dispatcher "NFS").

#### Use dispatcher to automatically toggle wireless depending on LAN cable being plugged in {#Use_dispatcher_to_automatically_toggle_wireless_depending_on_LAN_cable_being_plugged_in}

The idea is to only turn Wi-Fi on when the LAN cable is unplugged (for example when detaching from a laptop dock), and for Wi-Fi to be automatically disabled, once a LAN cable is plugged in again.

Create the following dispatcher script[\[7\]](https://superuser.com/questions/233448/disable-wlan-if-wired-cable-network-is-available), replacing *`Your_Ethernet_Interface`* with your ethernet interface\'s device name.

**Note** You can get a list of interfaces using [nmcli](#nmcli_examples) (`nmcli d | grep ethernet`). The Ethernet interfaces start with `en` or `eth`, e.g. `enp0s5` or `eth0`.

Remember to make the script [executable](../en/Help:Reading.html#Make_executable "Executable"). You can verify that it works by [restarting](../en/Help:Reading.html#Control_of_systemd_units "Restart") `NetworkManager.service`, running `ip a`, and checking that `wlp3s0` (or whatever your Wi-Fi interface is called) is in `state DOWN`. If you encounter unexpected behavior, check the [journal](../en/Systemd/Journal.html "Journal") of `NetworkManager-dispatcher.service`.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/99-wifi-auto-toggle.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

LOG_PREFIX="WiFi Auto-Toggle"
ETHERNET_INTERFACE="Your_Ethernet_Interface"

if [ "$1" = "$ETHERNET_INTERFACE" ]; then
    case "$2" in
        up)
            echo "$LOG_PREFIX ethernet up"
            nmcli radio wifi off
            ;;
        down)
            echo "$LOG_PREFIX ethernet down"
            nmcli radio wifi on
            ;;
    esac
elif [ "$(nmcli -g GENERAL.STATE device show $ETHERNET_INTERFACE)" = "20 (unavailable)" ]; then
    echo "$LOG_PREFIX failsafe"
    nmcli radio wifi on
fi
```

**Note** There is a fail-safe for the case when the LAN interface was connected when the computer was last on, and then disconnected while the computer was off. That would mean the radio would still be off when the computer is turned back on, and with a disconnected LAN interface, you would have no network.

#### Use dispatcher to connect to a VPN after a network connection is established {#Use_dispatcher_to_connect_to_a_VPN_after_a_network_connection_is_established}

In this example we want to connect automatically to a previously defined VPN connection after connecting to a specific Wi-Fi network. First thing to do is to create the dispatcher script that defines what to do after we are connected to the network.

**The factual accuracy of this article or section is disputed.**

**Reason:** A scripting without `iwgetid` does work too and may be more reliable? (Discuss in [Talk:NetworkManager#Fixes for automatic VPN dispatcher script](../en/Talk:NetworkManager.html#Fixes_for_automatic_VPN_dispatcher_script "Talk:NetworkManager"))

**Note** This script will require [wireless_tools](https://archlinux.org/packages/?name=wireless_tools) in order to use `iwgetid`.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/vpn-up
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh
VPN_NAME="name of VPN connection defined in NetworkManager"
ESSID="Wi-Fi network ESSID (not connection name)"

interface=$1 status=$2
case $status in
  up|vpn-down)
    if iwgetid | grep -qs ":\"$ESSID\""; then
      nmcli connection up id "$VPN_NAME"
    fi
    ;;
  down)
    if iwgetid | grep -qs ":\"$ESSID\""; then
      if nmcli connection show --active | grep "$VPN_NAME"; then
        nmcli connection down id "$VPN_NAME"
      fi
    fi
    ;;
esac
```

If you would like to attempt to automatically connect to VPN for all Wi-Fi networks, you can use the following definition of the ESSID: `ESSID=$(iwgetid -r)`. Remember to set the script\'s permissions [accordingly](#Network_services_with_NetworkManager_dispatcher).

Trying to connect with the above script may still fail with `NetworkManager-dispatcher.service` complaining about \'no valid VPN secrets\', because of [the way VPN secrets are stored](https://developer.gnome.org/NetworkManager/0.9/secrets-flags.html). Fortunately, there are different options to give the above script access to your VPN password.

1: One of them requires editing the VPN connection configuration file to make NetworkManager store the secrets by itself rather than inside a keyring [that will be inaccessible for root](https://bugzilla.redhat.com/show_bug.cgi?id=710552): open up `/etc/NetworkManager/system-connections/`*`name of your VPN connection`*`.nmconnection` and change the `password-flags` and `secret-flags` from `1` to `0`.

If that alone does not work, you may have to create a `passwd-file` in a safe location with the same permissions and ownership as the dispatcher script, containing the following:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/path/to/passwd-file
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
vpn.secrets.password:YOUR_PASSWORD
```

The script must be changed accordingly, so that it gets the password from the file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/vpn-up
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh
VPN_NAME="name of VPN connection defined in NetworkManager"
ESSID="Wi-Fi network ESSID (not connection name)"

interface=$1 status=$2
case $status in
  up|vpn-down)
    if iwgetid | grep -qs ":\"$ESSID\""; then
      nmcli connection up id "$VPN_NAME" passwd-file /path/to/passwd-file
    fi
    ;;
  down)
    if iwgetid | grep -qs ":\"$ESSID\""; then
      if nmcli connection show --active | grep "$VPN_NAME"; then
        nmcli connection down id "$VPN_NAME"
      fi
    fi
    ;;
esac
```

2: Alternatively, change the `password-flags` and put the password directly in the configuration file adding the section `vpn-secrets`:

     [vpn]
     ....
     password-flags=0
     
     [vpn-secrets]
     password=your_password

**Note** It may now be necessary to re-open the NetworkManager connection editor and save the VPN passwords/secrets again.

#### Use dispatcher to disable IPv6 on VPN provider connections {#Use_dispatcher_to_disable_IPv6_on_VPN_provider_connections}

Many [commercial VPN providers](../en/Category:VPN_providers.html "Category:VPN providers") support only IPv4. That means all IPv6 traffic bypasses the VPN and renders it virtually useless. To avoid this, dispatcher can be used to disable all IPv6 traffic for the time a VPN connection is up.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/10-vpn-ipv6
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

case "$2" in
    vpn-up)
        echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6
        ;;
    vpn-down)
        echo 0 > /proc/sys/net/ipv6/conf/all/disable_ipv6
        ;;
esac
```

**Note** The above script does not work for WireGuard since NetworkManager does not send the `vpn-up/down` events for it. Instead you have to rely on generic events for your WireGuard interfaces as demonstrated in [\[8\]](https://gist.github.com/TheDcoder/85e1ec99a31180e20ba8e4896024f265).

As an alternative, dispatcher can be used to temporarily set the IPv6 mode of the device used by the VPN connection to `link-local`. This will avoid NetworkManager log spam about IPv6 being disabled. This script will not work if multiple devices or connections provide IPv6 connectivity, but could be adapted to iterate over multiple devices. Note that any change to the connection (using [nmcli(1)](https://man.archlinux.org/man/nmcli.1) or a [desktop environment](../en/Desktop_environment.html "Desktop environment")) will reapply the entire connection to the device and re-enable IPv6 (if it is enabled in the connection).

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/10-vpn-ipv6
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

case "$2" in
    vpn-up)
        nmcli device modify "${DEVICE_IFACE}" ipv6.method link-local
        ;;
    vpn-down)
        nmcli device reapply "${DEVICE_IFACE}"
        ;;
esac
```

#### OpenNTPD {#OpenNTPD}

See [OpenNTPD#Using NetworkManager dispatcher](../en/OpenNTPD.html#Using_NetworkManager_dispatcher "OpenNTPD").

#### Dynamically set NTP servers received via DHCP with systemd-timesyncd {#Dynamically_set_NTP_servers_received_via_DHCP_with_systemd-timesyncd}

When roaming between different networks (e.g. a company\'s LAN, Wi-Fi at home, various other Wi-Fi now and then) you might want to set the NTP server(s) used by timesyncd to those provided by DHCP. However, NetworkManager itself is not capable to communicate with systemd-timesyncd to set the NTP server(s).

The dispatcher can work around it.

[Create](../en/Help:Reading.html#Append,_add,_create,_edit "Create") the overlay directory for your systemd-timesyncd configuration `/etc/systemd/timesyncd.conf.d` if it does not already exist. Inside `/etc/NetworkManager/dispatcher.d`, put the following:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/dispatcher.d/10-update-timesyncd
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/sh

[ -z "$CONNECTION_UUID" ] && exit 0
INTERFACE="$1"
ACTION="$2"

case $ACTION in
up | dhcp4-change | dhcp6-change)
    # `DHCP6_DHCP6_NTP_SERVERS` with double `DHCP6` is the correct variable name as varified by `printenv` as of NetworkManager 1.56.0-1
    set -- ${DHCP6_DHCP6_NTP_SERVERS-} ${DHCP4_NTP_SERVERS-}
    servers=$*
    [ -n "$servers" ] || exit 0
    mkdir -p /etc/systemd/timesyncd.conf.d
    cat <<-THE_END >"/etc/systemd/timesyncd.conf.d/${CONNECTION_UUID}.conf"
        [Time]
        NTP=$servers
    THE_END
    systemctl restart systemd-timesyncd.service
    ;;
down)
    rm -f "/etc/systemd/timesyncd.conf.d/${CONNECTION_UUID}.conf"
    systemctl restart systemd-timesyncd.service
    ;;
esac
```

Every time NetworkManager sets up a new network connection (`ACTION=up`) or gets some update for an existing connection (`ACTION=dhcp4-change` or `ACTION=dhcp6-change`) and the provided connection data contains information about NTP server(s) (`DHCP6_DHCP6_NTP_SERVERS` and `DHCP4_NTP_SERVERS`), a connection specific overlay configuration file is written to `/etc/systemd/timesyncd.conf.d`, containing the provided NTP server(s). Whenever a connection is taken down (`ACTION=down`) the connection specific overlay file is removed. After each change to the configuration of systemd-timesyncd, this service is restarted to pick up the updated configuration. The use of connection specific configuration files is intentional so that when two or more connections are managed by NetworkManager in parallel the different NTP server names in the configuration are not overwritten as `up`, `dhcp4-change`, `dhcp6-change` and `down` actions might come in an arbitrary order.

**Note** `DHCP6_DHCP6_NTP_SERVERS` with double `DHCP6` is the correct variable name as varified by `printenv` as of NetworkManager 1.56.0-1

## Testing {#Testing}

NetworkManager applets are designed to load upon login so no further configuration should be necessary for most users. If you have already disabled your previous network settings and disconnected from your network, you can now test if NetworkManager will work. The first step is to [start](../en/Help:Reading.html#Control_of_systemd_units "Start") `NetworkManager.service`.

Some applets will provide you with a `.desktop` file so that the NetworkManager applet can be loaded through the application menu. If it does not, you are going to either have to discover the command to use or logout and login again to start the applet. Once the applet is started, it will likely begin polling network connections with for auto-configuration with a DHCP server.

To start the GNOME applet in non-xdg-compliant window managers like [awesome](../en/Awesome.html "Awesome"):

    nm-applet --sm-disable &

For static IP addresses, you will have to configure NetworkManager to understand them. The process usually involves right-clicking the applet and selecting something like \'Edit Connections\'.

## Tips and tricks {#Tips_and_tricks}

### Encrypted network keyphrases {#Encrypted_network_keyphrases}

By default, NetworkManager stores passwords in clear text in the connection files at `/etc/NetworkManager/system-connections/`. To print the stored passwords, use the following command:

    # grep -r '^psk=' /etc/NetworkManager/system-connections/

The passwords are accessible to the root user in the filesystem and to users with access to settings via the GUI (e.g. `nm-applet`).

It is preferable to save the passwords in encrypted form in a keyring instead of clear text. The downside to this is that the connections have to be set up for each user.

In order to read and write to the keyring, there must be a secret agent available. This can be one of:

-   `nmcli` with the `--ask` option
-   One of the graphical interfaces from [#Front-ends](#Front-ends)

If you make neither of these available, then authentication will fail with the error `no secrets: No agents were available for this request.`

On a single user machine, it is enough to set up encryption for root partition. See: [Dm-crypt](../en/Dm-crypt.html "Dm-crypt").

#### Using GNOME Keyring {#Using_GNOME_Keyring}

The keyring daemon has to be started and the keyring needs to be unlocked for the following to work.

Furthermore, NetworkManager needs to be configured not to store the password for all users. Using GNOME\'s [network-manager-applet](https://archlinux.org/packages/?name=network-manager-applet), run `nm-connection-editor` from a terminal, select a network connection, click *Edit*, select the *Wi-Fi Security* tab and click on the right icon of password and check *Store the password only for this user*.

#### Using KDE Wallet {#Using_KDE_Wallet}

Using KDE\'s [plasma-nm](https://archlinux.org/packages/?name=plasma-nm), click the applet, click on the top right *Settings* icon, click on a network connection, in the *General configuration* tab, untick *All users may connect to this network*. If the option is ticked, the passwords will still be stored in clear text, even if a keyring daemon is running.

If the option was selected previously and you un-tick it, you may have to use the `reset` option first to make the password disappear from the file. Alternatively, delete the connection first and set it up again.

### Sharing internet connection over Wi-Fi {#Sharing_internet_connection_over_Wi-Fi}

You can share your internet connection (e.g. 3G or wired) with a few clicks. Please note that a [firewall](../en/Category:Firewalls.html "Firewall") may interfere with internet sharing.

You will need a Wi-Fi card which supports AP mode, see [Software access point#Wi-Fi device must support AP mode](../en/Software_access_point.html#Wi-Fi_device_must_support_AP_mode "Software access point") for details.

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [dnsmasq](https://archlinux.org/packages/?name=dnsmasq) package to be able to actually share the connection. Note that NetworkManager starts its own instance of *dnsmasq*, independent of `dnsmasq.service`, as a DHCP server. See [#dnsmasq](#dnsmasq) for the caveats.

Create the shared connection:

-   Click on applet and choose *Create new wireless network*.
-   Follow wizard (choose WPA2 or higher, be sure to use at least 8 character long password, lower lengths will fail).
    -   Choose either [Hotspot](https://fedoraproject.org/wiki/Features/RealHotspot "fedora:Features/RealHotspot") or Ad-hoc as Wi-Fi mode.

The connection will be saved and remain stored for the next time you need it.

**Note** Android does not support connecting to Ad-hoc networks. To share a connection with Android use infrastructure mode (i.e. set Wi-Fi mode to \"Hotspot\").

### Sharing internet connection over Ethernet {#Sharing_internet_connection_over_Ethernet}

Scenario: your device has internet connection over Wi-Fi and you want to share the internet connection to other devices over Ethernet.

Requirements:

-   [Install](../en/Help:Reading.html#Installation_of_packages "Install") the [dnsmasq](https://archlinux.org/packages/?name=dnsmasq) and [nm-connection-editor](https://archlinux.org/packages/?name=nm-connection-editor) packages to be able to actually share the connection. Note that NetworkManager starts its own instance of *dnsmasq*, independent of `dnsmasq.service`, as a DHCP server. See [#dnsmasq](#dnsmasq) for the caveats.
-   Your internet connected device and the other devices are connected over a suitable Ethernet cable (this usually means a cross over cable or a switch in between).
-   Internet sharing is not blocked by a [firewall](../en/Category:Firewalls.html "Firewall").

Steps:

-   Run `nm-connection-editor` from terminal.
-   Add a new Ethernet connection.
-   Give it some sensible name. For example \"Shared Internet\"
-   Go to \"IPv4 Settings\".
-   For \"Method:\" select \"Shared to other computers\".
-   Save

Now you should have a new option \"Shared Internet\" under the Wired connections in NetworkManager.

### Checking if networking is up inside a cron job or script {#Checking_if_networking_is_up_inside_a_cron_job_or_script}

**This article or section is out of date.**

**Reason:** *nm-tool* was removed from NetworkManager for long time now[\[9\]](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/commit/bb8c75bd536d4f8fb80a4366025a279078f0ec81). *nmcli* should be used instead. (Discuss in [Talk:NetworkManager](../en/Talk:NetworkManager.html))

Some *cron* jobs require networking to be up to succeed. You may wish to avoid running these jobs when the network is down. To accomplish this, add an **if** test for networking that queries NetworkManager\'s *nm-tool* and checks the state of networking. The test shown here succeeds if any interface is up, and fails if they are all down. This is convenient for laptops that might be hardwired, might be on wireless, or might be off the network.

    if [ $(nm-tool|grep State|cut -f2 -d' ') == "connected" ]; then
        #Whatever you want to do if the network is online
    else
        #Whatever you want to do if the network is offline - note, this and the else above are optional
    fi

This is useful for a `cron.hourly` script that runs *fpupdate* for the F-Prot virus scanner signature update, as an example. Another way it might be useful, with a little modification, is to differentiate between networks using various parts of the output from *nm-tool*; for example, since the active wireless network is denoted with an asterisk, you could grep for the network name and then grep for a literal asterisk.

### Connect to network with secret on boot {#Connect_to_network_with_secret_on_boot}

By default, NetworkManager will not connect to networks requiring a secret automatically on boot. This is because it locks such connections to the user who makes it by default, only connecting after they have logged in. To change this, do the following:

1.  Right click on the `nm-applet` icon in your panel and select Edit Connections and open the Wireless tab
2.  Select the connection you want to work with and click the Edit button
3.  Check the boxes "Connect Automatically" and "Available to all users"
4.  Additionally, ensure that under \"Wi-Fi Security\", \"Store password for all users (not encrypted)\" is selected

Log out and log back in to complete.

### OpenConnect with password in KWallet {#OpenConnect_with_password_in_KWallet}

While you may type both values at connection time, [plasma-nm](https://archlinux.org/packages/?name=plasma-nm) 0.9.3.2-1 and above are capable of retrieving OpenConnect username and password directly from [KWallet](../en/KDE_Wallet.html "KWallet").

Open \"KDE Wallet Manager\" and look up your OpenConnect VPN connection under \"Network Management\|Maps\". Click \"Show values\" and enter your credentials in key \"VpnSecrets\" in this form (replace *username* and *password* accordingly):

    form:main:username%SEP%username%SEP%form:main:password%SEP%password

Next time you connect, username and password should appear in the \"VPN secrets\" dialog box.

### Ignore specific devices {#Ignore_specific_devices}

Sometimes it may be desired that NetworkManager ignores specific devices and does not try to configure addresses and routes for them. You can quickly and easily ignore devices by MAC or interface-name by using the following in `/etc/NetworkManager/conf.d/unmanaged.conf`:

    [keyfile]
    unmanaged-devices=mac:00:22:68:1c:59:b1;mac:00:1E:65:30:D1:C4;interface-name:eth0

After editing the file, run `nmcli general reload` as root. Afterwards you should be able to configure interfaces without NetworkManager altering what you have set.

### Configuring MAC address randomization {#Configuring_MAC_address_randomization}

See [MAC address spoofing#NetworkManager](../en/MAC_address_spoofing.html#NetworkManager "MAC address spoofing").

**Note** The iwd backend reportedly refuses MAC address randomisation. A workaround is available at [MAC address spoofing#NetworkManager](../en/MAC_address_spoofing.html#NetworkManager "MAC address spoofing").

### Turn off hostname sending {#Turn_off_hostname_sending}

NetworkManager by default sends the hostname to the DHCP server.

To disable sending your hostname to the DHCP server globally, set the `ipv4.dhcp-send-hostname=0` and `ipv6.dhcp-send-hostname=0` options with a configuration file in `/etc/NetworkManager/conf.d/`. E.g.:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/dhcp-send-hostname.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[connection]
ipv4.dhcp-send-hostname=0
ipv6.dhcp-send-hostname=0
```

To disable sending your hostname to the DHCP server for a specific connection (or alternatively, enable it for a connection if it is disabled globally), add the following to your network connection file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/system-connections/your_connection_file.nmconnection
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
[ipv4]
dhcp-send-hostname=false
...
[ipv6]
dhcp-send-hostname=false
...
```

**Note** These options are only honored by the default [internal DHCP client](#DHCP_client). To omit sending the hostname when using NetworkManager with dhcpcd, edit `/etc/dhcpcd.conf` and insert `anonymous` as the last line.

### Enable IPv6 Privacy Extensions {#Enable_IPv6_Privacy_Extensions}

See [IPv6#NetworkManager](../en/IPv6.html#NetworkManager "IPv6").

### Configure a unique DUID per connection {#Configure_a_unique_DUID_per_connection}

The DHCPv6 Unique Identifier (DUID) is a value used by the DHCPv6 client to identify itself to DHCPv6 servers. NetworkManager supports 3 types of DUID:

-   DUID-UUID ([RFC 6355](https://tools.ietf.org/html/rfc6355 "rfc:6355")): generated from an Universally Unique IDentifier (UUID).
-   DUID-LL ([RFC 3315](https://tools.ietf.org/html/rfc3315 "rfc:3315")): generated from the Link-Layer address (a.k.a. MAC address).
-   DUID-LLT ([RFC 3315](https://tools.ietf.org/html/rfc3315 "rfc:3315")): generated from the Link-Layer address plus a timestamp.

If the internal NetworkManager\'s DHCP client is in use (the default) it will identify itself with a global and permanent DUID-UUID generated from the machine-id (`/etc/machine-id`). This means that all connections share the same UUID, which may be a privacy breach.

Fortunately, NetworkManager is able to provide unique DUIDs per connection, derived from the connection\'s stable-id and a per-host unique key. You can enable that by adding the following configuration under `/etc/NetworkManager/conf.d`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/duid.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[connection]
ipv6.dhcp-duid=stable-uuid
```

The `stable-ll` and `stable-llt` values are also supported. For further information read the description for `dhcp-duid` in [nm-settings(5) § ipv6 setting](https://man.archlinux.org/man/nm-settings.5#ipv6_setting).

### Working with wired connections {#Working_with_wired_connections}

By default, NetworkManager generates a connection profile for each wired ethernet connection it finds. At the point when generating the connection, it does not know whether there will be more Ethernet adapters available. Hence, it calls the first wired connection \"Wired connection 1\". You can avoid generating this connection, by configuring `no-auto-default` (see [NetworkManager.conf(5)](https://man.archlinux.org/man/NetworkManager.conf.5)), or by simply deleting it. Then NetworkManager will remember not to generate a connection for this interface again.

You can also edit the connection (and persist it to disk) or delete it. NetworkManager will not re-generate a new connection. Then you can change the name to whatever you want. You can use something like [nm-connection-editor](https://archlinux.org/packages/?name=nm-connection-editor) for this task.

### Using iwd as the Wi-Fi backend {#Using_iwd_as_the_Wi-Fi_backend}

**Note**

-   Do not enable `iwd.service`. NetworkManager will start and manage [iwd](../en/Iwd.html "Iwd") itself.
-   Consider [existing issues](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/issues?scope=all&utf8=%E2%9C%93&state=opened&search=iwd) before switching to *iwd*.

To enable the [experimental iwd backend](https://archive.kernel.org/oldwiki/iwd.wiki.kernel.org/networkmanager.html), first [install](../en/Help:Reading.html#Installation_of_packages "Install") [iwd](https://archlinux.org/packages/?name=iwd) and then create the following configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/wifi_backend.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[device]
wifi.backend=iwd
```

Alternatively, [networkmanager-iwd](https://aur.archlinux.org/packages/networkmanager-iwd/)^AUR^ can be used to build NetworkManager to work exclusively with iwd, with the main difference being that it depends on [iwd](https://archlinux.org/packages/?name=iwd) instead of [wpa_supplicant](https://archlinux.org/packages/?name=wpa_supplicant).

To use MAC randomization with iwd see [MAC address spoofing#iwd](../en/MAC_address_spoofing.html#iwd "MAC address spoofing").

**Note** You may need to [convert existing NetworkManager network profiles](https://archive.kernel.org/oldwiki/iwd.wiki.kernel.org/networkmanager.html#converting_network_profiles) after switching to *iwd*.

NetworkManager will delegate the autoconnection for Wi-Fi networks to iwd by default. This may not work on some configurations. To have NetworkManager handle the reconnection, the following modification can be made:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/wifi_backend.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[device]
wifi.backend=iwd
wifi.iwd.autoconnect=false
```

### Running in a network namespace {#Running_in_a_network_namespace}

If you would like to run NetworkManager inside a network namespace (e.g., to manage a specific device which should be used by selected applications), bring the device down before moving it to the namespace:

    $ ip link set dev MY_DEVICE down
    $ ip link set dev MY_DEVICE netns MY_NAMESPACE
    $ ip netns exec MY_NAMESPACE NetworkManager
    ...
    $ ip netns exec MY_NAMESPACE killall NetworkManager

otherwise NetworkManager will later fail to establish the connection with a `device is strictly unmanaged` error.

### Automatically connect to VPN {#Automatically_connect_to_VPN}

NetworkManager can be set to automatically connect to a VPN when connecting to the internet, on a per network basis. The VPN connection itself can be added in GNOME\'s NetworkManager front-end, but to make it automatically use the VPN `nmcli` must be used. Other front-ends might not have this limitation.

First, make sure to make the VPN connection available to all users. In the GNOME this is a matter of checking a box under the `details` tab. Under the `Identity` tab, in the password field, click the icon on the right side in the field, and set it to `Store the password for all users`.

Then find the UUID of the VPN connection, and add that to `connection.secondaries` of the Internet connection:

    # UUID=$(nmcli --get-values connection.uuid connection show name-of-VPN-connection)
    # nmcli connection modify name-of-Internet-connection connection.secondaries "$UUID"

Now when NetworkManager is restarted and you connect to the Internet connection you have configured, you should automatically get connected to the VPN.

## Troubleshooting {#Troubleshooting}

### No prompt for password of secured Wi-Fi networks {#No_prompt_for_password_of_secured_Wi-Fi_networks}

When trying to connect to a secured Wi-Fi network, no prompt for a password is shown and no connection is established. This happens when no keyring package is installed. An easy solution is to install [gnome-keyring](https://archlinux.org/packages/?name=gnome-keyring). If you want the passwords to be stored in encrypted form, follow [GNOME Keyring](../en/GNOME_Keyring.html "GNOME Keyring") to set up the *gnome-keyring-daemon*.

### Network management disabled {#Network_management_disabled}

When NetworkManager shuts down but the pid (state) file is not removed, you will see a `Network management disabled` message. If this happens, remove the file manually:

    # rm /var/lib/NetworkManager/NetworkManager.state

### Problems with internal DHCP client {#Problems_with_internal_DHCP_client}

If you have problems with getting an IP address using the internal DHCP client, consider using another DHCP client, see [#DHCP client](#DHCP_client) for instructions. This workaround might solve problems in big wireless networks like eduroam.

### 3G modem not detected {#3G_modem_not_detected}

See [Mobile broadband modem#NetworkManager](../en/Mobile_broadband_modem.html#NetworkManager "Mobile broadband modem").

### Switching off WLAN on laptops {#Switching_off_WLAN_on_laptops}

Sometimes NetworkManager will not work when you disable your Wi-Fi adapter with a switch on your laptop and try to enable it again afterwards. This is often a problem with *rfkill*. To check if the driver notifies *rfkill* about the wireless adapter\'s status, use:

    $ watch -n1 rfkill list all

If one identifier stays blocked after you switch on the adapter you could try to manually unblock it with (where X is the number of the identifier provided by the above output):

    # rfkill event unblock X

### Static IP address settings revert to DHCP {#Static_IP_address_settings_revert_to_DHCP}

**This article or section is out of date.**

**Reason:** This section is [added in 2010](../Special:Diff/119236.html "Special:Diff/119236") and describes an ancient version of *nm-applet*. Is this still relevant in 2024? (Discuss in [Talk:NetworkManager](../en/Talk:NetworkManager.html))

Due to an unresolved bug, when changing default connections to a static IP address, `nm-applet` may not properly store the configuration change, and will revert to automatic DHCP.

To work around this issue you have to edit the default connection (e.g. \"Auto eth0\") in `nm-applet`, change the connection name (e.g. \"my eth0\"), uncheck the \"Available to all users\" checkbox, change your static IP address settings as desired, and click **Apply**. This will save a new connection with the given name.

Next, you will want to make the default connection not connect automatically. To do so, run `nm-connection-editor` (**not** as root). In the connection editor, edit the default connection (e.g. \"Auto eth0\") and uncheck \"Connect automatically\". Click **Apply** and close the connection editor.

### Cannot edit connections as normal user {#Cannot_edit_connections_as_normal_user}

See [#Set up PolicyKit permissions](#Set_up_PolicyKit_permissions).

### Forget hidden wireless network {#Forget_hidden_wireless_network}

Since hidden networks are not displayed in the selection list of the Wireless view, they cannot be forgotten (removed) with the GUI. You can delete one with the following command:

    # rm /etc/NetworkManager/system-connections/SSID.nmconnection

This also works for any other connection.

### VPN not working in GNOME {#VPN_not_working_in_GNOME}

When setting up OpenConnect or vpnc connections in NetworkManager while using GNOME, you will sometimes never see the dialog box pop up and the following error appears in `/var/log/errors.log`:

    localhost NetworkManager[399]: <error> [1361719690.10506] [nm-vpn-connection.c:1405] get_secrets_cb(): Failed to request VPN secrets #3: (6) No agents were available for this request.

This is caused by the GNOME NetworkManager Applet expecting dialog scripts to be at `/usr/lib/gnome-shell`, when NetworkManager\'s packages put them in `/usr/lib/networkmanager`. As a \"temporary\" fix (this bug has been around for a while now), make the following symlink(s):

-   For OpenConnect: `ln -s /usr/lib/nm-openconnect-auth-dialog /usr/lib/gnome-shell/`
-   For VPNC (i.e. Cisco VPN): `ln -s /usr/lib/nm-vpnc-auth-dialog /usr/lib/gnome-shell/`

This may need to be done for any other NetworkManager VPN plugins as well, but these are the two most common.

### Automatic connect to VPN on boot is not working {#Automatic_connect_to_VPN_on_boot_is_not_working}

The problem occurs when the system (i.e. NetworkManager running as the root user) tries to establish a VPN connection, but the password is not accessible because it is stored in the GNOME Keyring of a particular user.

A solution is to keep the password to your VPN in plaintext, as described in step (2.) of [#Use dispatcher to connect to a VPN after a network connection is established](#Use_dispatcher_to_connect_to_a_VPN_after_a_network_connection_is_established).

You do not need to use the dispatcher described in step (1.) to auto-connect anymore, if you use the new \"auto-connect VPN\" option from the `nm-applet` GUI.

### systemd bottleneck {#systemd_bottleneck}

Over time the log files (`/var/log/journal`) can become very large. This can have a big impact on boot performance when using NetworkManager, see: [systemd#Boot time increasing over time](../en/Systemd.html#Boot_time_increasing_over_time "Systemd").

### Regular network disconnects, latency and lost packets (Wi-Fi) {#Regular_network_disconnects,_latency_and_lost_packets_(Wi-Fi)}

NetworkManager does a scan every 2 minutes.

Some Wi-Fi drivers have issues when scanning for base stations whilst connected/associated. Symptoms include VPN disconnects/reconnects and lost packets, web pages failing to load and then refresh fine.

Running `journalctl -f` as root will indicate that this is taking place, messages like the following will be contained in the logs at regular intervals.

    NetworkManager[410]: <info>  (wlp3s0): roamed from BSSID 00:14:48:11:20:CF (my-wifi-name) to (none) ((none))

If roaming is not important, the periodic scanning behavior can be disabled by locking the BSSID of the access point in the Wi-Fi connection profile.

### Unable to turn on Wi-Fi with Lenovo laptop (IdeaPad, Legion, etc.) {#Unable_to_turn_on_Wi-Fi_with_Lenovo_laptop_(IdeaPad,_Legion,_etc.)}

There is an issue with the `ideapad_laptop` module on some Lenovo models due to the Wi-Fi driver incorrectly reporting a soft block. The card can still be manipulated with `netctl`, but managers like NetworkManager break. You can verify that this is the problem by checking the output of `rfkill list` after toggling your hardware switch and seeing that the soft block persists.

**The factual accuracy of this article or section is disputed.**

**Reason:** Try to use `rfkill.default_state` and `rfkill.master_switch_mode` (see [kernel-parameters.html](https://docs.kernel.org/admin-guide/kernel-parameters.html)) to fix the rfkill problem. (Discuss in [Talk:NetworkManager](../en/Talk:NetworkManager.html))

[Unloading](../en/Kernel_module.html "Modprobe") the `ideapad_laptop` module should fix this. (**warning**: this may disable the laptop keyboard and touchpad also!).

### nm-applet disappears in i3wm {#nm-applet_disappears_in_i3wm}

If you use the `xfce4-notifyd.service` for notifications you must [edit](../en/Systemd.html#Editing_provided_units "Edit") the unit and add the following:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/user/xfce4-notifyd.service.d/display_env.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Service]
Environment="DISPLAY=:0.0"
```

After reloading the daemons [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `xfce4-notifyd.service`. Exit i3 and start it back up again and the applet should show on the tray.

### Unit dbus-org.freedesktop.resolve1.service not found {#Unit_dbus-org.freedesktop.resolve1.service_not_found}

If `systemd-resolved.service` is not started, NetworkManager will try to start it using D-Bus and fail:

    dbus-daemon[991]: [system] Activating via systemd: service name='org.freedesktop.resolve1' unit='dbus-org.freedesktop.resolve1.service' requested by ':1.23' (uid=0 pid=1012 comm="/usr/bin/NetworkManager --no-daemon ")
    dbus-daemon[991]: [system] Activation via systemd failed for unit 'dbus-org.freedesktop.resolve1.service': Unit dbus-org.freedesktop.resolve1.service not found.
    dbus-daemon[991]: [system] Activating via systemd: service name='org.freedesktop.resolve1' unit='dbus-org.freedesktop.resolve1.service' requested by ':1.23' (uid=0 pid=1012 comm="/usr/bin/NetworkManager --no-daemon ")

This is because NetworkManager will try to send DNS information to [systemd-resolved](../en/Systemd-resolved.html "Systemd-resolved") regardless of the `main.dns=` setting in [NetworkManager.conf(5)](https://man.archlinux.org/man/NetworkManager.conf.5).[\[10\]](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/commit/d4eb4cb45f41b1751cacf71da558bf8f0988f383)

This can be disabled with a configuration file in `/etc/NetworkManager/conf.d/`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/no-systemd-resolved.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[main]
systemd-resolved=false
```

See [FS#62138](https://bugs.archlinux.org/task/62138).

### Secrets were required, but not provided {#Secrets_were_required,_but_not_provided}

If you received the following error when attempting to connect to a network:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ nmcli device wifi connect SSID password password
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Error: Connection activation failed: (7) Secrets were required, but not provided
```

This error can have numerous causes and you should read the [journal](../en/Systemd/Journal.html "Journal") (filter it with `-u NetworkManager`). For example, if NetworkManager took too long to establish connection, it will believe that the password is incorrect:

    NetworkManager[1372]: <warn>  [1643991888.3808] device (wlan0): Activation: (wifi) association took too long
    NetworkManager[1372]: <info>  [1643991888.3809] device (wlan0): state change: config -> need-auth (reason 'none', sys-iface-state: 'managed')
    NetworkManager[1372]: <warn>  [1643991888.3838] device (wlan0): Activation: (wifi) asking for new secrets

You can try deleting the connection profile and creating a new one:

    $ nmcli connection delete SSID
    $ nmcli device wifi connect SSID password password

You can also try disabling MAC address randomization:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/NetworkManager/conf.d/wifi_rand_mac.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[device]
wifi.scan-rand-mac-address=no
```

### Failed to request VPN secrets {#Failed_to_request_VPN_secrets}

If you get this error:

    Failed to request VPN secrets #1: No agents were available for this request.

It is either because the password is empty or you have to [set up PolicyKit permissions](#Set_up_PolicyKit_permissions).

### OpenVPN connections fail with OpenSSL \"ca md too weak\" error {#OpenVPN_connections_fail_with_OpenSSL_\"ca_md_too_weak\"_error}

Since [openssl](https://archlinux.org/packages/?name=openssl) was updated to version 3, certificates generated with legacy cryptographic algorithms are rejected by default. Attempting to use [networkmanager-openvpn](https://archlinux.org/packages/?name=networkmanager-openvpn) with such a setup can result in the following error in the logs:

    nm-openvpn[14359]: OpenSSL: error:0A00018E:SSL routines::ca md too weak
    nm-openvpn[14359]: Cannot load certificate file /home/archie/.local/share/networkmanagement/certificates/my_issued_cert.crt
    nm-openvpn[14359]: Exiting due to fatal error

The correct approach is to have the OpenVPN server administrator generate and re-issue more secure certificates. However, as an immediate work-around, OpenVPN requires `tls-cipher "DEFAULT:@SECLEVEL=0"`. This may not be possible through the plugin GUI, but it is possible with *nmcli*. Separately, you will also need to enable the *legacy* provider in OpenSSL.

Firstly, obtain the name of the VPN connection with the issue, from the output of the following:

    $ nmcli connection show

Assuming the connection name is *vpn.example.com*, use *nmcli* like so:

    $ nmcli connection modify vpn.example.com +vpn.data tls-cipher=DEFAULT:@SECLEVEL=0

The change should instantly be reflected in `/etc/NetworkManager/system-connections/vpn.example.com.nmconnection`.

As for OpenSSL, edit `/etc/ssl/openssl.cnf` as described on the [OpenSSL wiki](https://wiki.openssl.org/index.php/OpenSSL_3.0#Providers).

Specifically, at the end of the `[provider_sect]` section add `legacy = legacy_sect`. Under `[default_sect]` uncomment `activate = 1`. Lastly, add a new section `[legacy_sect]` that also contains the line `activate = 1`. Excluding most other preexisting configuration sections, the end result will look something like:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssl/openssl.cnf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
openssl_conf = openssl_init

[openssl_init]
providers = provider_sect

[provider_sect]
default = default_sect
legacy = legacy_sect

[default_sect]
activate = 1

[legacy_sect]
activate = 1
```

Finally, [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") the `NetworkManager.service` to have the new OpenSSL configuration take effect.

### WPA Enterprise connections fail to authenticate with OpenSSL \"unsupported protocol\" error {#WPA_Enterprise_connections_fail_to_authenticate_with_OpenSSL_\"unsupported_protocol\"_error}

Since [openssl](https://archlinux.org/packages/?name=openssl) was updated to version 3, \"SSL 3, TLS 1.0, TLS 1.1, and DTLS 1.0 only work at security level 0\" [by default](https://www.openssl.org/news/openssl-3.0-notes.html). Attempting to authenticate to a Wi-Fi network only supporting older standards results in the following error in the logs:

    wpa_supplicant[3320]: SSL: SSL3 alert: write (local SSL3 detected an error):fatal:protocol version
    wpa_supplicant[3320]: OpenSSL: openssl_handshake - SSL_connect error:0A000102:SSL routines::unsupported protocol
    wpa_supplicant[3320]: wlp3s0: CTRL-EVENT-EAP-FAILURE EAP authentication failed

The correct approach is to convince the institution\'s administrator to upgrade the encrypted networking tunnel protocol to TLS 1.3 and optionally drop support for deprecated security standards, including TLS 1.0/1.1, DTLS 1.0 and SSL 1-3. However, as an immediate workaround, there are multiple ways to allow TLS 1.0 and/or 1.1 by default. One way would be to manually patch or revert the breaking changes in OpenSSL ([\[11\]](https://github.com/openssl/openssl/commit/7bf2e4d7f0c7ae19b7a8c416910886a7171e9820)). As this also lowers security for all other programs using OpenSSL level 1, it is not recommended. Instead, one can directly set the level used by wpa_supplicant, like described in [BBS#286417](https://bbs.archlinux.org/viewtopic.php?id=286417#p2104492). To only change the affected connection, it is possible to set `phase1-auth-flags=32` or `phase1-auth-flags=64` in the `[802-1x]` section of the connection\'s configuration file. This may not be possible through GUIs, but it is possible with *nmcli*.

Firstly, obtain the name of the Wi-Fi connection with the issue, from the output of the following:

    $ nmcli connection show

Assuming the connection uses TLS 1.0 and its name is *Example Wi-Fi*, use *nmcli* like so:

    $ nmcli connection modify 'Example Wi-Fi' 802-1x.phase1-auth-flags 32

And for a TLS 1.1 connection, type \"64\" instead:

    $ nmcli connection modify 'Example Wi-Fi' 802-1x.phase1-auth-flags 64

**Note** The number you type in refers to the number you get from raising 2 to the power of **n**. Here, **n** is the index of the network authentication bit octet, read from right to left. Flipping the fifth bit enables TLS 1.0 **\[log(2) 32\]** and flipping the sixth bit enables TLS 1.1 **\[log(2) 64\]**.

The change should instantly be reflected in `/etc/NetworkManager/system-connections/Example Wi-Fi.nmconnection`.

Finally, [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") the `NetworkManager.service` to have the new OpenSSL configuration take effect.

## See also {#See_also}

-   [NetworkManager for Administrators Part 1](https://blogs.gnome.org/dcbw/2015/02/16/networkmanager-for-administrators-part-1/)
