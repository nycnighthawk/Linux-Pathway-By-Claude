---
{"title": "Openswan L2TP/IPsec VPN client setup", "url": "https://wiki.archlinux.org/title/Openswan_L2TP/IPsec_VPN_client_setup", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Openswan L2TP/IPsec VPN client setup

Related articles

-   [strongSwan](../../en/StrongSwan.html "StrongSwan")

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../../en/Help:Style.html "Help:Style") for reference.**

**Reason:** This article needs language improvements, do not write in first person (Discuss in [Talk:Openswan L2TP/IPsec VPN client setup](../../en/Talk:Openswan_L2TP/IPsec_VPN_client_setup.html))

This article describes how to configure and use a L2TP/IPsec Virtual Private Network client on Arch Linux. It covers the installation and setup of several needed software packages. L2TP refers to the [Layer 2 Tunneling Protocol](https://en.wikipedia.org/wiki/Layer_2_Tunneling_Protocol "wikipedia:Layer 2 Tunneling Protocol"), and for [IPsec](https://en.wikipedia.org/wiki/IPsec "wikipedia:IPsec"), the [Openswan](https://www.openswan.org/) implementation is employed.

This guide is primarily targeted for clients connecting to a Windows Server machine, as it uses some settings that are specific to the Microsoft implementation of L2TP/IPsec. However, it is adaptable with any other common L2TP/IPsec setup. The [Openswan wiki](https://github.com/xelerance/Openswan/wiki/L2tp-ipsec-configuration-using-openswan-and-xl2tpd) features instructions to set up a corresponding L2TP/IPSec Linux server.

## Installation {#Installation}

To use with NetworkManager, [install](../../en/Help:Reading.html#Installation_of_packages "Install") the [networkmanager-l2tp](https://archlinux.org/packages/?name=networkmanager-l2tp) and [strongswan](https://archlinux.org/packages/?name=strongswan) packages.

Otherwise [install](../../en/Help:Reading.html#Installation_of_packages "Install") the [xl2tpd](https://archlinux.org/packages/?name=xl2tpd) and [openswan](https://aur.archlinux.org/packages/openswan/)^AUR^ packages.

## Configuration {#Configuration}

### NetworkManager {#NetworkManager}

Open the NetworkManager UI, then:

1.  Go to Network \> VPN. Click \"+\"
2.  Select \"Layer 2 Tunneling Protocol (L2TP).\"
3.  You can choose a name for the VPN.
4.  Enter Your VPN Server IP for the Gateway.
5.  Enter Your VPN Username for the User name.
6.  Right-click the ? in the Password field, select Store the password only for this user. (If this option gives you trouble, you might want to use \"Store password for all users\")
7.  Enter Your VPN Password for the Password.
8.  Leave the NT Domain field blank.
9.  Click the IPsec Settings\... button.
10. Check the Enable IPsec tunnel to L2TP host checkbox.
11. Leave the Gateway ID field blank.
12. Enter Your VPN IPsec PSK for the Pre-shared key.
13. OK, then click Add to save the VPN connection information.

Now you should be able to start the VPN, by switching the Toggle-Button on.

### OpenSwan {#OpenSwan}

Edit `/etc/ipsec.conf` to contain the following lines:

    config setup
         virtual_private=%v4:10.0.0.0/8,%v4:192.168.0.0/16,%v4:172.16.0.0/12
         nat_traversal=yes
         protostack=netkey            # default is auto, which will try netkey first
         plutoopts="--interface=eth0" # Replace eth0 with your network interface or use %defaultroute to use default route

    conn L2TP-PSK
         authby=secret
         pfs=no
         auto=add
         keyingtries=3
         dpddelay=30
         dpdtimeout=120
         dpdaction=clear
         rekey=yes
         ikelifetime=8h
         keylife=1h
         type=transport
         left=192.168.0.123           # Replace with your local IP address (private, behind NAT IP is okay as well)
         leftprotoport=17/1701
         right=68.68.32.79            # Replace with your VPN server's IP
         rightprotoport=17/1701

This file contains the basic information to establish a secure IPsec tunnel to the VPN server. It enables NAT Traversal for if your machine is behind a NAT\'ing router (most people are), and various other options that are necessary to connect correctly to the remote IPsec server. The next file contains your pre-shared key (PSK) for the server.

Create the file `/etc/ipsec.secrets`: It should contain the following line:

    192.168.0.123 68.68.32.79 : PSK "your_pre_shared_key"

Remember to replace the local (`192.168.0.123`) and remote (`68.68.32.79`) IP addresses with the correct numbers for your location. The pre-shared key will be supplied by the VPN provider and will need to be placed in this file in cleartext form. You may find this file already exists and already have some data, try to back it up and create a new file only with your PSK if you will see `Can't authenticate: no preshared key found for ...` when enabling connection in next section. Do not forget to set proper permissions (600) for this file or you will get error message `We cannot identify ourselves with either end of this connection.`.

Add the connection, so it is available to use:

    # ipsec auto --add L2TP-PSK

At this point the IPsec configuration is complete and we can move on to the L2TP configuration.

#### Running Openswan in a container {#Running_Openswan_in_a_container}

Do not forget to add CAP_SYS_MODULE capability and access to host module tree. Example for nspawn:

    --bind=/lib/modules --capability=CAP_SYS_MODULE

### xl2tpd

Edit `/etc/xl2tpd/xl2tpd.conf` so it has the following contents:

    [lac vpn-connection]
    lns = 68.68.32.79
    ppp debug = yes
    pppoptfile = /etc/ppp/options.l2tpd.client
    length bit = yes

This file configures xl2tpd with the connection name, server IP address (which again, please remember to change to your servers address) and various options that will be passed to pppd once the tunnel is set up.

Now create `/etc/ppp/options.l2tpd.client` with the following contents:

    ipcp-accept-local
    ipcp-accept-remote
    refuse-eap
    require-mschap-v2
    noccp
    noauth
    idle 1800
    mtu 1410
    mru 1410
    defaultroute
    usepeerdns
    debug
    connect-delay 5000
    name your_vpn_username
    password your_password

Place your assigned username and password for the VPN server in this file. A lot of these options are for interoperability with Windows Server L2TP servers. If your VPN server uses PAP authentication, replace `require-mschap-v2` with `require-pap`.

This concludes the configuration of the applicable software suites to connect to a L2TP/IPsec server. To start the connection do the following:

[Start](../../en/Help:Reading.html#Control_of_systemd_units "Start") `openswan.service` and `xl2tpd.service`.

    # ipsec auto --up L2TP-PSK
    # echo "c vpn-connection" > /var/run/xl2tpd/l2tp-control

At this point the tunnel is up and you should be able to see the interface for it if you type:

    $ ip link

You should see a `pppX` device that represents the tunnel. Right now, nothing is going to get routed through it. You need to add some routing rules to make it work right:

## Routing {#Routing}

### Routing traffic to a single IP address or subnet through the tunnel {#Routing_traffic_to_a_single_IP_address_or_subnet_through_the_tunnel}

This is as easy as adding a routing rule to your kernel table:

    # ip route add xxx.xxx.xxx.xxx via yyy.yyy.yyy.yyy dev pppX

Note xxx.xxx.xxx.xxx is the specific ip address (e.g. 192.168.3.10) or subnet (e.g. 192.168.3.0/24) that you wish to communicate with through the tunnel device (e.g. ppp0).

Note yyy.yyy.yyy.yyy is \"peer ip\" of your pppX device used to route traffic to tunnel destination xxx.xxx.xxx.xxx.

\
See example below for command to identify tunnel device name and peer ip and then add route. :

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ip address
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
4: ppp0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1400 qdisc fq_codel state UNKNOWN group default qlen 3
    link/ppp 
    inet 10.192.168.40 peer 192.0.2.1/32 scope global ppp0
       valid_lft forever preferred_lft forever
```

    # ip route add 192.168.3.0/24 via 192.0.2.1 dev ppp0

### Routing all traffic through the tunnel {#Routing_all_traffic_through_the_tunnel}

This is a lot more complex, but all your traffic will travel through the tunnel. Start by adding a special route for the actual VPN server through your current gateway:

    # ip route add 68.68.32.79 via 192.168.1.1 dev eth0

This will ensure that once the default gateway is changed to the ppp interface that your network stack can still find the VPN server by routing around the tunnel. If you miss this step you will lose connectivity to the Internet and the tunnel will collapse. Now add a default route that routes to the PPP remote end:

    # ip route add default via yyy.yyy.yyy.yyy dev pppX

The remote PPP end can be discovered by following the step in the previous section. Now to ensure that ALL traffic is routing through the tunnel, delete the original default route:

    # ip route delete default via 192.168.1.1 dev eth0

To restore your system to the previous state, you can reboot or reverse all of the above steps.

The route creation can also be automated by placing a script in /etc/ppp/ip-up.d.

## Troubleshooting {#Troubleshooting}

**Issue:** [journalctl](../../en/Systemd/Journal.html "Journalctl") logs **VPN connection: failed to connect: \'Could not restart the ipsec service.**

**Solution** Make sure you have strongswan installed

**Note** The first step may be to use the **ipsec verify** command to check the configuration of the installed IPSEC.

**Issue:** I get a message from pppd saying \"Failed to authenticate ourselves to peer\" and I have verified my password is correct. What could be wrong?

**Solution 1:** If you see the following in your /var/log/daemon.log:

    Dec 20 15:14:03 myhost pppd[26529]: rcvd [CHAP Challenge id=0x1 <some_or_another_hash>, name = "SonicWALL"]
    Dec 20 15:14:03 myhost pppd[26529]: sent [CHAP Response id=0x1 <some_or_another_hash>, name = "your_vpn_username"]
    Dec 20 15:14:03 myhost pppd[26529]: rcvd [LCP EchoRep id=0x0 magic=0x45c269c6]
    Dec 20 15:14:03 myhost pppd[26529]: rcvd [CHAP Failure id=0x1 ""]
    Dec 20 15:14:03 myhost pppd[26529]: CHAP authentication failed
    Dec 20 15:14:03 myhost pppd[26529]: CHAP authentication failed
    Dec 20 15:14:03 myhost pppd[26529]: sent [LCP TermReq id=0x3 "Failed to authenticate ourselves to peer"]
    Dec 20 15:14:03 myhost pppd[26529]: rcvd [LCP TermReq id=0x2]
    Dec 20 15:14:03 myhost pppd[26529]: sent [LCP TermAck id=0x2]
    Dec 20 15:14:03 myhost pppd[26529]: rcvd [LCP TermAck id=0x3]

then you are authenticating against a SonicWALL LNS that does not know how to handle CHAP-style authentication correctly.

The solution to this is to add the following to your options.l2tp.client file:

       refuse-chap

This will cause the SonicWALL to default to the next authentication mechanism, namely MSCHAP-v2. This should authenticate successfully, and from this point xl2tpd should successfully construct a tunnel between you and the remote L2TP server.

**Solution 2:** If you see the following in your journal after running `journalctl -ru xl2tpd` as root:

    vas. 03 12:31:21 myhost pppd[8922]: rcvd [LCP EchoRep id=0x0 magic=<some_or_another_hash>]
    vas. 03 12:31:21 myhost pppd[8922]: rcvd [CHAP Failure id=0x1 "E=691 R=0 C=<some_or_another_hash> V=3 M=bad username or password"]
    vas. 03 12:31:21 myhost pppd[8922]: MS-CHAP authentication failed: bad username or password
    vas. 03 12:31:21 myhost pppd[8922]: CHAP authentication failed

Try adding domain name in front of username in your options.l2tpd.client file (note the double backslash), i.e:

    …
    name DOMAIN\\your_vpn_username
    password your_password

**Issue:** **cannot initiate connection with ID wildcards (kind=CK_TEMPLATE)** after running `ipsec auto --ad L2TP-PSK` when using Openswan 3.0.0.

Determine the private IP of the VPN server in the target network behind the VPN, and add the corresponding line to `/etc/ipsec.conf`:

    rightid = private IP of VPN server

## Tips and tricks {#Tips_and_tricks}

### Script start up and shut down {#Script_start_up_and_shut_down}

You can create some scripts either in your home directory or elsewhere(remember where you put them) to bring up the tunnel then shut it back down.

First, a utility script to automatically discover PPP distant ends:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
getip.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/bash

ifconfig $1 | grep "P-t-P" | gawk -F: '{print $2}' | gawk '{print $1}'
```

Next, the script to bring the tunnel up. This will replace the default route, so all traffic will pass via the tunnel:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
startvpn.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/bash

systemctl start openswan
sleep 2                                                   #delay to ensure that IPsec is started before overlaying L2TP
systemctl start xl2tpd
ipsec auto --up L2TP-PSK                        
echo "c vpn-connection" > /var/run/xl2tpd/l2tp-control     
sleep 2                                                   #delay again to make that the PPP connection is up.
PPP_GW_ADD=`./getip.sh ppp0`

ip route add 68.68.32.79 via 192.168.1.1 dev eth0
ip route add default via $PPP_GW_ADD
ip route del default via 192.168.1.1
```

Finally, the shutdown script, it simply reverses the process:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
stopvpn.sh
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
#!/bin/bash

ipsec auto --down L2TP-PSK
echo "d vpn-connection" > /var/run/xl2tpd/l2tp-control
systemctl stop xl2tpd
systemctl stop openswan

ip route del 68.68.32.79 via 192.168.1.1 dev eth0
ip route add default via 192.168.1.1
```

### A further script {#A_further_script}

Above script really help me work. And notice the script use fixed ip, and someone like me may change net vpn addr, i would like to put my further script below(not sure how to add attachment, so just raw ):

    #!/bin/bash
    if [ $# != 1 ] ; then
        echo "Usage: (sudo) sh $0 {init|start|stop}" 
        exit 1;
    fi

    VPN_ADDR=XXX
    IFACE=wlan0

    function getIP(){
        ip addr show $1 | grep "inet " | awk '{print $2}' | sed 's:/.*::'       
    }

    function getGateWay(){
        ip route show default | awk '/default/ {print $3}'
    }
    function getVPNGateWay(){
        ip route | grep -m 1 "$VPN_ADDR" | awk '{print $3}'
    }

    GW_ADDR=$(getGateWay)  

    function init(){
        cp ./options.l2tpd.client /etc/ppp/
        cp ./ipsec.conf /etc/
        cp ./ipsec.secrets /etc/
        cp ./xl2tpd.conf /etc/xl2tpd/
    }

    function start(){
        sed -i "s/^lns =.*/lns = $VPN_ADDR/g" /etc/xl2tpd/xl2tpd.conf
        sed -i "s/plutoopts=.*/plutoopts=\"--interface=$IFACE\"/g" /etc/ipsec.conf
        sed -i "s/left=.*$/left=$(getIP $IFACE)/g" /etc/ipsec.conf
        sed -i "s/right=.*$/right=$VPN_ADDR/g" /etc/ipsec.conf
        sed -i "s/^.*: PSK/$(getIP $IFACE) $VPN_ADDR : PSK/g" /etc/ipsec.secrets
        systemctl start openswan
        sleep 2    #delay to ensure that IPsec is started before overlaying L2TP

        systemctl start xl2tpd
        ipsec auto --up L2TP-PSK                        
        echo "c vpn-connection" > /var/run/xl2tpd/l2tp-control     
        sleep 2    #delay again to make that the PPP connection is up.

            ip route add $VPN_ADDR via $GW_ADDR dev $IFACE
            ip route add default via $(getIP ppp0)
            ip route del default via $GW_ADDR
    }

    function stop(){
        ipsec auto --down L2TP-PSK
        echo "d vpn-connection" > /var/run/xl2tpd/l2tp-control
        systemctl stop xl2tpd
        systemctl stop openswan
        
        VPN_GW=$(getVPNGateWay)
            ip route del $VPN_ADDR via $VPN_GW dev $IFACE
            ip route add default via $VPN_GW
    }

    $1
    exit 0

### Script to resolve dns names and connect {#Script_to_resolve_dns_names_and_connect}

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../../en/Help:Style.html "Help:Style") for reference.**

**Reason:** The wiki should not host scripts. (Discuss in [Talk:Openswan L2TP/IPsec VPN client setup](../../en/Talk:Openswan_L2TP/IPsec_VPN_client_setup.html))

Very useful if you have dynamic IP for the server.

    #!/bin/python

    from os import system
    from socket import gethostbyname
    from netifaces import ifaddresses, AF_INET
    from time import sleep

    # netifaces is a library installed with pip, not part of default insatllation of python
    # The script is useful if you have dynamic IP, or need to use a domain for the vpn server
    # gist: https://gist.github.com/physicalit/bf9e27c7ecbc12843cd68e442358616c
    # The template files are identical to the examples from the link above, except they use the sign `<` as placeholder for the server ip
    # can be added to cron, do not forghet to modify your domain and the ip/subnet from the `ip add route ...`

    ip = gethostbyname('your.domain.tld')

    file_list = ['/etc/xl2tpd/xl2tpd.conf_tmp', '/etc/ipsec.secrets_tmp', '/etc/ipsec.conf_tmp']

    def read_file(file):
        with open(file, 'r') as f:
            result = f.readlines()
            #result = [l.rstrip('\n') for l in result]  # l.split('_')[0] 
            return result

    def write_ip(ip):
        for l in file_list:
            result = [ip.join(e.split('<')) if "<" in e else e for e in read_file(l)]
            with open(l.split('_')[0], 'w') as f:
                for e in result:
                    f.write(e)

    if __name__ == "__main__":
        write_ip(ip)
        [ system('systemctl restart {}'.format(l)) for l in ['openswan', 'xl2tpd']]
        vpn = system('ipsec auto --up L2TP-PSK')
        system('echo "c vpn-connection" > /var/run/xl2tpd/l2tp-control')
        sleep(2) # very important or is not going to see ppp0 interface
        if not vpn:
            peer = ifaddresses('ppp0')[AF_INET][0]['peer']
            route = system('ip route add 192.168.88.0/24 via {0} dev ppp0'.format(peer))
            if not route:
                print("VPN sucesfully connected. Route created.")
            else:
                print("VPN KO")

## See also {#See_also}

-   [https://openswan.org/](https://openswan.org/)
-   [https://github.com/hwdsl2/setup-ipsec-vpn/blob/master/docs/clients.md#ubuntu-linux](https://github.com/hwdsl2/setup-ipsec-vpn/blob/master/docs/clients.md#ubuntu-linux)
-   [https://github.com/xelerance/xl2tpd](https://github.com/xelerance/xl2tpd)
-   [https://web.archive.org/web/20130129212118/https://strongvpn.com/forum/viewtopic.php?pid=1844](https://web.archive.org/web/20130129212118/https://strongvpn.com/forum/viewtopic.php?pid=1844) ([archive link](https://web.archive.org/web/20130129212118/https://strongvpn.com/forum/viewtopic.php?pid=1844)) --- The main source used to write the initial revisions of this article.
