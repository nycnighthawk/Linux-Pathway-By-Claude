---
{"title": "OpenSSH", "url": "https://wiki.archlinux.org/title/OpenSSH", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# OpenSSH

Related articles

-   [SSH keys](../en/SSH_keys.html "SSH keys")
-   [Pam abl](../en/Pam_abl.html "Pam abl")
-   [fail2ban](../en/Fail2ban.html "Fail2ban")
-   [sshguard](../en/Sshguard.html "Sshguard")
-   [Sshfs](../en/SSHFS.html "Sshfs")
-   [Syslog-ng](../en/Syslog-ng.html "Syslog-ng")
-   [SFTP chroot](../en/SFTP_chroot.html "SFTP chroot")
-   [SCP and SFTP](../en/SCP_and_SFTP.html "SCP and SFTP")
-   [VPN over SSH](../en/VPN_over_SSH.html "VPN over SSH")

[OpenSSH](https://en.wikipedia.org/wiki/OpenSSH "wikipedia:OpenSSH") (OpenBSD Secure Shell) is a set of computer programs providing encrypted communication sessions over a computer network using the [Secure Shell](../en/Secure_Shell.html "Secure Shell") (SSH) protocol. It was created as an open source alternative to the proprietary Secure Shell software suite offered by SSH Communications Security. OpenSSH is developed as part of the OpenBSD project, which is led by Theo de Raadt.

OpenSSH is occasionally confused with the similarly-named OpenSSL; however, the projects have different purposes and are developed by different teams, the similar name is drawn only from similar goals.

## Installation {#Installation}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") the [openssh](https://archlinux.org/packages/?name=openssh) package.

## Client usage {#Client_usage}

To connect to a server, run:

    $ ssh -p port user@server-address

If the server only allows public-key authentication, follow [SSH keys](../en/SSH_keys.html "SSH keys").

### Configuration {#Configuration}

You can configure OpenSSH by putting options into `~/.ssh/config` for the current user or `/etc/ssh/ssh_config` for all users. You can also use `/etc/ssh/ssh_config.d/*.conf` drop-in files to split configuration concerns.

The client can be configured to store common options and hosts. All options can be declared globally or restricted to specific hosts. For example:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# global options
User user1

# host-specific options
Host myserver
    Hostname server-address
    Port     port
    User     user2
```

With such a configuration, the following commands are equivalent

    $ ssh -p port user2@server-address
    $ ssh myserver

See [ssh_config(5)](https://man.archlinux.org/man/ssh_config.5) for more information.

Some options do not have command line switch equivalents, but you can specify configuration options on the command line with `-o`. For example `-oKexAlgorithms=+diffie-hellman-group1-sha1`.

## Server usage {#Server_usage}

`sshd` is the OpenSSH server daemon, configured with `/etc/ssh/sshd_config` or `/etc/ssh/sshd_config.d/*.conf` drop-in files, and managed by `sshd.service`. Whenever changing the configuration, use `sshd` in test mode before restarting the service to ensure it will be able to start cleanly. Valid configurations produce no output.

    # sshd -t

### Configuration {#Configuration_2}

To allow access only for some users, add this line:

    AllowUsers    user1 user2

To allow access only for some groups:

    AllowGroups   group1 group2

To add a nice welcome message (e.g. from the `/etc/issue` file), configure the `Banner` option:

    Banner /etc/issue

Public and private host keys are automatically generated in `/etc/ssh/` by `sshdgenkeys.service` and regenerated if missing even if `HostKeyAlgorithms` option in `sshd_config` allows only some. Four key pairs are provided based on the algorithms [ed25519, mldsa44-ed25519, ecdsa and rsa](../en/SSH_keys.html#Choosing_the_authentication_key_type "SSH keys"). To have sshd use a particular key, specify the following option:

    HostKey /etc/ssh/ssh_host_ed25519_key

If the server is to be exposed to the WAN, it is recommended to change the default port from 22 to a random higher one like this:

    Port 39901

**Tip**

-   To help select an alternative port that is not already assigned to a common service, review the [list of TCP and UDP port numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers "wikipedia:List of TCP and UDP port numbers"). You can also find port information locally in `/etc/services`. A port change from default port 22 will reduce the number of log entries caused by automated authentication attempts but will not eliminate them. See [Port knocking](../en/Port_knocking.html "Port knocking") for related information.
-   It is recommended to disable password logins entirely. This will greatly increase security, see [#Force public key authentication](#Force_public_key_authentication) for more information. See [#Protection](#Protection) for more recommend security methods.
-   OpenSSH can listen to multiple ports simply by having multiple `Port `*`port_number`* lines in the configuration file.
-   New (or missing) host key pairs can be generated by removing the pair(s) that you want to replace from `/etc/ssh` and running `ssh-keygen -A` as root.

### Daemon management {#Daemon_management}

[Start/enable](../en/Help:Reading.html#Control_of_systemd_units "Start/enable") `sshd.service`. It will keep the SSH daemon permanently active and fork for each incoming connection.

#### Socket activation {#Socket_activation}

[openssh](https://archlinux.org/packages/?name=openssh) 8.0p1-3 removed `sshd.socket` that used systemd\'s socket activation due to it being susceptible to denial of service. See [FS#62248](https://bugs.archlinux.org/task/62248) for details. If `sshd.socket` is enabled when updating to [openssh](https://archlinux.org/packages/?name=openssh) 8.0p1-3, the `sshd.socket` and `sshd@.service` units will be copied to `/etc/systemd/system/` and [reenabled](../en/Help:Reading.html#Control_of_systemd_units "Reenable"). This is only done to not break existing setups; users are still advised to migrate to `sshd.service`.

**Warning** If you continue using `sshd.socket`, be aware of its issues:

-   `sshd.socket` unit may fail (e.g. due to out-of-memory situation) and `Restart=always` cannot be specified on socket units. See [systemd issue 11553](https://github.com/systemd/systemd/issues/11553).
-   Using socket activation can result in denial of service, as too many connections can cause refusal to further activate the service. See [FS#62248](https://bugs.archlinux.org/task/62248).

Using `sshd.socket` negates the `ListenAddress` setting, so it will allow connections over any address. To achieve the effect of setting `ListenAddress`, you must specify the port *and* IP for `ListenStream` (e.g. `ListenStream=192.168.1.100:22`) by [editing](../en/Systemd.html#Editing_provided_units "Edit") `sshd.socket`. You must also add `FreeBind=true` under `[Socket]` or else setting the IP address will have the same drawback as setting `ListenAddress`: the socket will fail to start if the network is not up in time.

When using socket activation, a transient instance of `sshd@.service` will be started for each connection (with different instance names). Therefore, neither `sshd.socket` nor the daemon\'s regular `sshd.service` allow to monitor connection attempts in the log. The logs of socket-activated instances of SSH can be seen by running `journalctl -u "sshd@*"` as root or by running `journalctl /usr/bin/sshd` as root.

### Protection {#Protection}

Allowing remote log-on through SSH is good for administrative purposes, but can pose a threat to your server\'s security. Often the target of brute force attacks, SSH access needs to be limited properly to prevent third parties gaining access to your server.

[ssh-audit](https://archlinux.org/packages/?name=ssh-audit) offers an automated analysis of server and client configuration. Several other good guides and tools are available on the topic, for example:

-   [Article by Mozilla Infosec Team](https://infosec.mozilla.org/guidelines/openssh.html)
-   [SSH Hardening Guides](https://www.ssh-audit.com/hardening_guides.html)

#### Force public key authentication {#Force_public_key_authentication}

If a client cannot authenticate through a public key, by default, the SSH server falls back to password authentication, thus allowing a malicious user to attempt to gain access by [brute-forcing](#Protecting_against_brute_force_attacks) the password. One of the most effective ways to protect against this attack is to disable password logins entirely, and force the use of [SSH keys](../en/SSH_keys.html "SSH keys"). This can be accomplished by setting the following options in the daemon configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config.d/20-force_publickey_auth.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
PasswordAuthentication no
AuthenticationMethods publickey
```

**Warning** Before adding this to your configuration, make sure that all accounts which require SSH access have public-key authentication set up in the corresponding `authorized_keys` files. See [SSH keys#Copying the public key to the remote server](../en/SSH_keys.html#Copying_the_public_key_to_the_remote_server "SSH keys") for more information.

#### Two-factor authentication and public keys {#Two-factor_authentication_and_public_keys}

SSH can be set up to require multiple ways of authentication; you can tell which authentication methods are required using the `AuthenticationMethods` option. This enables you to use public keys as well as a two-factor authorization.

##### Authentication providers {#Authentication_providers}

See [Google Authenticator](../en/Google_Authenticator.html "Google Authenticator") to set up Google Authenticator.

For [Duo](https://duo.com/), [install](../en/Help:Reading.html#Installation_of_packages "Install") [duo_unix](https://aur.archlinux.org/packages/duo_unix/)^AUR^ which will supply the `pam_duo.so` module. Read the [Duo Unix documentation](https://duo.com/docs/duounix) for instructions on how to setup the necessary Duo credentials (Integration Key, Secret Key, API Hostname).

##### PAM setup {#PAM_setup}

**The factual accuracy of this article or section is disputed.**

**Reason:** The distribution defaults to `KbdInteractiveAuthentication no` since [\[1\]](https://gitlab.archlinux.org/archlinux/packaging/packages/openssh/-/commit/1d834b1fb688e148797c39cffd95eac3404ef894). Later, the lexical order of the defaults was adjusted due to [FS#79285](https://bugs.archlinux.org/task/79285) to allow for higher priority user snippets, which would match below `20-pam.conf`. However, a [BBS thread](https://bbs.archlinux.org/viewtopic.php?id=300451) appears to be resolved by ordering custom after `99-archlinux.conf` defaults only. (Discuss in [Talk:OpenSSH](../en/Talk:OpenSSH.html))

To use [PAM](../en/PAM.html "PAM") with OpenSSH, edit the following files:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config.d/20-pam.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
KbdInteractiveAuthentication yes
AuthenticationMethods publickey keyboard-interactive:pam
```

Then you can log in with either a publickey **or** the user authentication as required by your PAM setup.

If, on the other hand, you want to authenticate the user on both a publickey **and** the user authentication as required by your PAM setup, use a comma instead of a space to separate the AuthenticationMethods:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config.d/20-pam.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
KbdInteractiveAuthentication yes
AuthenticationMethods publickey,keyboard-interactive:pam
```

With required pubkey **and** pam authentication, you may wish to disable the password requirement:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/pam.d/sshd
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
auth      required  pam_securetty.so     #disable remote root
#Require google authenticator
auth      required  pam_google_authenticator.so
#But not password
#auth      include   system-remote-login
account   include   system-remote-login
password  include   system-remote-login
session   include   system-remote-login
```

#### Protecting against brute force attacks {#Protecting_against_brute_force_attacks}

Brute forcing is a simple concept: one continuously tries to log in to a webpage or server log-in prompt like SSH with a high number of random username and password combinations.

See [ufw#Rate limiting with ufw](../en/Uncomplicated_Firewall.html#Rate_limiting_with_ufw "Ufw") or [Simple stateful firewall#Bruteforce attacks](../en/Simple_stateful_firewall.html#Bruteforce_attacks "Simple stateful firewall") for [iptables](../en/Iptables.html "Iptables").

Since 9.8 a basic protection similar to [fail2ban](../en/Fail2ban.html "Fail2ban") is implemented: the option `PerSourcePenalties` is set with reasonable default values. Penalties for various conditions are enforced against a client on its source address, resulting in a refused connection for a time period.

Alternatively, you can protect yourself from brute force attacks by using an automated script that blocks anybody trying to brute force their way in.

-   Only allow incoming SSH connections from trusted locations
-   Use [fail2ban](../en/Fail2ban.html "Fail2ban") or [sshguard](../en/Sshguard.html "Sshguard") to automatically block IP addresses that fail password authentication too many times.
-   Use [pam_shield](https://github.com/h0tw1r3/pam_shield) to block IP addresses that perform too many login attempts within a certain period of time. In contrast to [fail2ban](../en/Fail2ban.html "Fail2ban") or [sshguard](../en/Sshguard.html "Sshguard"), this program does not take login success or failure into account.

#### Limit root login {#Limit_root_login}

**This article or section is out of date.**

**Reason:** Root login has been disabled by default upstream in the current version. Unclear to me what parts of this section and subsections are redundant. (Discuss in [Talk:OpenSSH](../en/Talk:OpenSSH.html))

It is generally considered bad practice to allow the root user to log in without restraint over SSH. There are two methods by which SSH root access can be restricted for increased security.

##### Deny {#Deny}

Sudo selectively provides root rights for actions requiring these without requiring authenticating against the root account. This allows locking the root account against access via SSH and potentially functions as a security measure against brute force attacks, since now an attacker must guess the account name in addition to the password.

SSH can be configured to deny remote logins with the root user by editing the \"Authentication\" section in the daemon configuration file. Simply set `PermitRootLogin` to `no`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config.d/20-deny_root.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
PermitRootLogin no
```

Next, [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") the SSH daemon.

You will now be unable to log in through SSH under root, but will still be able to log in with your normal user and use [su](../en/Su.html "Su") or [sudo](../en/Sudo.html "Sudo") to do system administration.

##### Restrict {#Restrict}

Some automated tasks such as remote, full-system backup require full root access. To allow these in a secure way, instead of disabling root login via SSH, it is possible to only allow root logins for selected commands. This can be achieved by editing `~root/.ssh/authorized_keys`, by prefixing the desired key, e.g. as follows:

    command="rrsync -ro /" ssh-ed25519 ...

This will allow any login with this specific key only to execute the command specified between the quotes.

The increased attack surface created by exposing the root user name at login can be compensated by adding the following to `sshd_config`:

    PermitRootLogin forced-commands-only

This setting will not only restrict the commands which root may execute via SSH, but it will also disable the use of passwords, forcing use of public key authentication for the root account.

A slightly less restrictive alternative will allow any command for root, but makes brute force attacks infeasible by enforcing public key authentication. For this option, set:

    PermitRootLogin prohibit-password

#### Locking the authorized_keys file {#Locking_the_authorized_keys_file}

**Warning** Locking this file only protects against user mistakes and a particular naive in-person attack. It **does not** provide any protection against malicious programs or breaches. Use multi-factor authentication, firewalling and practice defence in depth to prevent breaches in the first place.

If, for whatever reason, you think that the user in question should not be able to add or change existing keys, you can prevent them from manipulating the file.

On the server, make the `authorized_keys` file read-only for the user and deny all other permissions:

    $ chmod 400 ~/.ssh/authorized_keys

To prevent the user from simply changing the permissions back, [set the immutable bit](../en/File_permissions_and_attributes.html#File_attributes "File permissions and attributes") on the `authorized_keys` file. To prevent the user from renaming the `~/.ssh` directory and creating a new `~/.ssh` directory and `authorized_keys` file, set the immutable bit on the `~/.ssh` directory too. To add or remove keys, you will have to remove the immutable bit from `authorized_keys` and make it writable temporarily.

**Tip** It is recommended to log changes to any `authorized_keys` file via e.g [auditd](../en/Audit_framework.html#Audit_files_and_directories_access "Audit framework").

#### SSH certificates {#SSH_certificates}

While common SSH keys and manual fingerprint verification may be easy to use with a handful of hosts that are managed by a single administrator, this method of authentication does not scale at all. When a number of servers need to be accessed through SSH by several users, manually verifying ssh public key fingerprints of every host becomes nearly impossible to do securely and reliably.

The solution for this is to use SSH certificates that provide automatic verification of public key identities through a chain of trust that scales significantly better than the default trust-on-first-use approach of SSH. SSH certificates are basically nothing else than normal public SSH keys, but with an additional signature from a trusted certificate authority that verifies the key identity.

##### Create a host certificate authority key for your infrastructure {#Create_a_host_certificate_authority_key_for_your_infrastructure}

    $ ssh-keygen -t ed25519 -f ~/.ssh/ca_host_key -C 'Host certificate authority for *.example.com'

The private certificate authority key should be stored securely, ideally on a smartcard or hardware token that prevents key extraction like the [Nitrokey](../en/Nitrokey.html "Nitrokey") or [YubiKey](../en/YubiKey.html "YubiKey").

##### Sign a server\'s public SSH host key {#Sign_a_server's_public_SSH_host_key}

Copy the public server key to your local system containing the private certificate authority key to sign it:

    $ ssh-keygen -h -s ~/.ssh/ca_key -I certLabel -n server01.example.com ./ssh_host_ed25519_key.pub

##### Move the new certificate and configure sshd to use it {#Move_the_new_certificate_and_configure_sshd_to_use_it}

The generated certificate `ssh_host_ed25519_key-cert.pub` should be copied to the server at `/etc/ssh/`.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config.d/20-ed25519_key.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
HostCertificate /etc/ssh/ssh_host_ed25519_key-cert.pub
```

##### Configure all clients to trust the certificate authority {#Configure_all_clients_to_trust_the_certificate_authority}

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/known_hosts
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
@cert-authority  *.example.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKL8gB/pjuff005YNazwMCqJpgsXAbQ3r4VStd/CRKwU Host certificate authority for *.example.com
```

**Warning** When a server does not provide a certificate for identification, public key authentication is used as fallback by default.

##### SSH user certificates {#SSH_user_certificates}

Depending on the number of users and method of deployment, SSH User keys can also be used with Certificates. For organizations with many ssh users, this is strongly advised to manage User key deployment securely.

The deployment of user certificates works basically the same as for server identities. More details and instructions can be found at [Wikibooks:OpenSSH/Cookbook/Certificate-based Authentication](https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Certificate-based_Authentication "wikibooks:OpenSSH/Cookbook/Certificate-based Authentication").

##### Certificate deployment automation {#Certificate_deployment_automation}

Automated deployment of SSH certificates can be provided by a number of open source tools. Popular examples are:

-   [Ansible - openssh_cert module](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssh_cert_module.html)
-   [privacyIDEA - authentication server](https://www.privacyidea.org/)
-   [Theo App - authorized keys manager](https://theoapp.readthedocs.io/en/latest/)

#### SSHFP record {#SSHFP_record}

The [Secure Shell fingerprint record (SSHFP)](https://en.wikipedia.org/wiki/SSHFP_record "wikipedia:SSHFP record") is an optional resource record in the domain name system that associates SSH keys to a host name. It can be used to verify the SSH fingerprint on public servers via [DANE](../en/DANE.html "DANE") instead of deploying trusted CA certificates, which allows even unmanaged clients to verify the validity of key fingerprints.

**Note** The DNS zone (domain) must be signed with DNSSEC.

##### Generate record entry {#Generate_record_entry}

To generate the required hexadecimal key fingerprint to be stored in the DNS record, create the hash on the target server.

    $ ssh-keygen -r host.example.com

This will read all available SSH keys for the specified domain and output valid SSHFP records that can then be stored in the DNS entries of the affected domain.

##### Client configuration {#Client_configuration}

In order to automatically retrieve and trust SSH key fingerprints stored as SSHFP records, add the following to your ssh client configuration file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# global options
Match all
    VerifyHostKeyDNS yes
```

If the target host has a valid SSHFP record and this record is verified with a valid DNSSEC signature, the fingerprint is automatically accepted without prompting the user to verify the hosts identity. In case the DNS record is not verified by DNSSEC, the user will be prompted to verify the fingerprint instead as usual.

**Note** For SSHFP records to work, make sure that `trust-ad` option is set in `/etc/resolv.conf`.

##### Generate SSHFP records {#Generate_SSHFP_records}

To determine the SSH fingerprint of a specific domain, use *ssh-keyscan* to retrieve the ssh fingerprints in a valid DNS record format. (Note that by default fingerprints for every available key type is provided as both SHA1 and SHA256.)

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ssh-keyscan -D github.com
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
; github.com:22 SSH-2.0-babeld-57ca1323
; github.com:22 SSH-2.0-babeld-57ca1323
github.com IN SSHFP 1 1 6f4c60375018bae0918e37d9162bc15ba40e6365
github.com IN SSHFP 1 2 b8d895ced92c0ac0e171cd2ef5ef01ba3417554a4a6480d331ccc2be3ded0f6b
; github.com:22 SSH-2.0-babeld-57ca1323
github.com IN SSHFP 3 1 3358ab5dd3e306c461c840f7487e93b697e30600
github.com IN SSHFP 3 2 a764003173480b54c96167883adb6b55cf7cfd1d415055aedff2e2c8a8147d03
; github.com:22 SSH-2.0-babeld-57ca1323
github.com IN SSHFP 4 1 e9619e2ed56c2f2a71729db80bacc2ce9ccce8d4
github.com IN SSHFP 4 2 f83898df0bef57a4ee24985ba598ac17fccb0c0d333cc4af1dd92be14bc23aa5
; github.com:22 SSH-2.0-babeld-57ca1323
```

Since the SSHFP record stores the key fingerprints as hexadecimal values while the common output for SSH fingerprints is the base64 encoded SHA256 hash of the public key, it is necessary to convert the record back to the base64 format in order to compare it with values in the known_hosts file or other documentation that commonly stores fingerprints as SHA256.

    $ echo "SSHFP-fingerprint" | xxd -r -p | base64

Example for github.com using the hex value for the sha256 fingerprint of the key type ed25519

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ echo "f83898df0bef57a4ee24985ba598ac17fccb0c0d333cc4af1dd92be14bc23aa5" | xxd -r -p | base64
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU=
```

Compare with known_hosts entries:

    $ ssh-keygen -l -f ~/.ssh/known_hosts

##### Manually retrieve SSHFP records from DNS {#Manually_retrieve_SSHFP_records_from_DNS}

    $ dig SSHFP targetdomain.tld +short

## Tips and tricks {#Tips_and_tricks}

### Encrypted SOCKS tunnel {#Encrypted_SOCKS_tunnel}

This can be useful for laptop users connect to unsafe wireless connections. The only requirement is an SSH server running at a somewhat secure location, like your home or at work. It might be useful to use a dynamic DNS service like [DynDNS](https://dyn.com/dns/) so you do not have to remember your IP address.

#### Start the connection {#Start_the_connection}

    $ ssh -TND 4711 user@host

The `N` flag disables the interactive prompt, and the `D` flag specifies the local port on which to listen on (you can choose any port number). The `T` flag disables pseudo-tty allocation.

Perhaps add the verbose (`-v`) flag, to verify the connection.

#### Configure your browser (or other programs) {#Configure_your_browser_(or_other_programs)}

The above step is useful only in combination with a web browser or another program. Since SSH supports both SOCKS v4 and SOCKS v5, you can use either.

-   For Firefox:

1.  Go to *Preferences \> General \> Network Settings* and click on *Settings\...*.
2.  In the new window, check the *Manual proxy configuration* option and enter `localhost` in the *SOCKS host* text field, and the port number in the *Port* text field (`4711` in the example above).
3.  Restart Firefox.

**Note** Firefox does not automatically make DNS requests through the SOCKS tunnel. This can be mitigated by checking the *Proxy DNS when using SOCKS vN* (v4 or v5).

-   For Chromium:

1.  You can set the SOCKS settings as environment variables or as command line options. For example, add one of the following functions to your `.bashrc`:

        secure_chromium() {
            local port=4711
            export SOCKS_SERVER=localhost:$port
            export SOCKS_VERSION=5
            (chromium > /dev/null 2>&1 &)
        }

        secure_chromium() {
            local port=4711
            (chromium --proxy-server="socks://localhost:$port" > /dev/null 2>&1 &)
        }

2.  Open a terminal and run:

        $ secure_chromium

#### Set up a local TUN interface {#Set_up_a_local_TUN_interface}

This is more complicated initially, but results in you not having to manually configure every application to use the SOCKS proxy. It requires setting up a local TUN interface and routing traffic through it.

See [VPN over SSH#Set up badvpn and tunnel interface](../en/VPN_over_SSH.html#Set_up_badvpn_and_tunnel_interface "VPN over SSH").

### X11 forwarding {#X11_forwarding}

X11 forwarding is a mechanism that allows graphical interfaces of X11 programs running on a remote system to be displayed on a local client machine. For X11 forwarding the remote host does not need to have a full X11 system installed; however, it needs at least to have *xauth* installed. *xauth* is a utility that maintains `Xauthority` configurations used by server and client for authentication of X11 session ([source](http://xmodulo.com/2012/11/how-to-enable-x11-forwarding-using-ssh.html)).

**Warning** X11 forwarding has important security implications which should be at least acknowledged by reading relevant sections of [ssh(1)](https://man.archlinux.org/man/ssh.1), [sshd_config(5)](https://man.archlinux.org/man/sshd_config.5), and [ssh_config(5)](https://man.archlinux.org/man/ssh_config.5) manual pages. See also [this StackExchange question.](https://security.stackexchange.com/questions/14815/security-concerns-with-x11-forwarding)

#### Setup {#Setup}

##### Remote {#Remote}

-   [install](../en/Help:Reading.html#Installation_of_packages "Install") the [xorg-xauth](https://archlinux.org/packages/?name=xorg-xauth) packages
-   in `/etc/ssh/ssh`**`d`**`_config`:
    -   set `X11Forwarding` to *yes*
    -   verify that `AllowTcpForwarding` and `X11UseLocalhost` options are set to *yes*, and that `X11DisplayOffset` is set to *10* (those are the default values if nothing has been changed, see [sshd_config(5)](https://man.archlinux.org/man/sshd_config.5))
-   then [restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") the [*sshd* daemon](#Daemon_management).

##### Client {#Client}

-   [install](../en/Help:Reading.html#Installation_of_packages "Install") the [xorg-xauth](https://archlinux.org/packages/?name=xorg-xauth) package
-   enable the `ForwardX11` option by either specifying the `-X` switch on the command line for opportunistic connections, or by setting `ForwardX11` to *yes* in the [client\'s configuration](#Configuration).

**Tip** You can enable the `ForwardX11Trusted` option (`-Y` switch on the command line) if GUI is drawing badly or you receive errors; this will prevent X11 forwardings from being subjected to the [X11 SECURITY extension](https://www.x.org/wiki/Development/Documentation/Security/) controls. Be sure you have read [the warning](#X11_forwarding) at the beginning of this section if you do so.

#### Usage {#Usage}

Log on to the remote machine normally, specifying the `-X` switch if *ForwardX11* was not enabled in the client\'s configuration file:

    $ ssh -X user@host

If you receive errors trying to run graphical applications, try *ForwardX11Trusted* instead:

    $ ssh -Y user@host

Given the output `X11 forwarding request failed`, redo the setup for your remote machine. Once the X11 forwarding request succeeds, you can start any X program on the remote server, and it will be forwarded to your local session:

    $ xclock

Error output containing `Can't open display` indicates that `DISPLAY` is improperly set.

Be careful with some applications as they check for a running instance on the local machine. [Firefox](../en/Firefox.html "Firefox") is an example: either close the running Firefox instance or use the following start parameter to start a remote instance on the local machine:

    $ firefox --no-remote

If you get \"X11 forwarding request failed on channel 0\" when you connect (and the server `/var/log/errors.log` shows \"Failed to allocate internet-domain X11 display socket\"), make sure package [xorg-xauth](https://archlinux.org/packages/?name=xorg-xauth) is installed. If its installation is not working, try to either:

-   enable the `AddressFamily any` option in `ssh`**`d`**`_config` on the *server*, or
-   set the `AddressFamily` option in `ssh`**`d`**`_config` on the *server* to inet.

Setting it to inet may fix problems with Ubuntu clients on IPv4.

For running X applications as another user on the SSH server, you need to `xauth add` the authentication line taken from `xauth list` of the SSH logged in user.

**Tip** [Here](https://unix.stackexchange.com/a/12772) are [some](https://unix.stackexchange.com/a/46748) useful [links](https://superuser.com/a/805060) for troubleshooting `X11 Forwarding` issues.

### Forwarding other ports {#Forwarding_other_ports}

In addition to SSH\'s built-in support for X11, it can also be used to securely tunnel any TCP connection, by use of local forwarding or remote forwarding.

Local forwarding opens a port on the local machine, connections to which will be forwarded to the remote host and from there on to a given destination. Very often, the forwarding destination will be the same as the remote host, thus providing a secure shell and, e.g. a secure [VNC](../en/List_of_applications/Internet.html#Remote_desktop "VNC") connection, to the same machine. Local forwarding is accomplished by means of the `-L` switch and it is accompanying forwarding specification in the form of `<tunnel port>:<destination address>:<destination port>`.

Thus:

    $ ssh -L 1000:mail.google.com:25 192.168.0.100

will use SSH to login to and open a shell on `192.168.0.100`, and will also create a tunnel from the local machine\'s TCP port 1000 to mail.google.com on port 25. Once established, connections to `localhost:1000` will connect to the Gmail SMTP port. To Google, it will appear that any such connection (though not necessarily the data conveyed over the connection) originated from `192.168.0.100`, and such data will be secure between the local machine and 192.168.0.100, but not between `192.168.0.100` and Google, unless other measures are taken.

Similarly:

    $ ssh -L 2000:192.168.0.100:6001 192.168.0.100

will allow connections to `localhost:2000` which will be transparently sent to the remote host on port 6001. The preceding example is useful for VNC connections using the vncserver utility\--part of the [tightvnc](../en/TigerVNC.html "Tightvnc") package\--which, though very useful, is explicit about its lack of security.

Remote forwarding allows the remote host to connect to an arbitrary host via the SSH tunnel and the local machine, providing a functional reversal of local forwarding, and is useful for situations where, e.g., the remote host has limited connectivity due to firewalling. It is enabled with the `-R` switch and a forwarding specification in the form of `<tunnel port>:<destination address>:<destination port>`.

Thus:

    $ ssh -R 3000:irc.libera.chat:6667 192.168.0.200

will bring up a shell on `192.168.0.200`, and connections from `192.168.0.200` to itself on port 3000 (the remote host\'s `localhost:3000`) will be sent over the tunnel to the local machine and then on to irc.libera.chat on port 6667, thus, in this example, allowing the use of IRC programs on the remote host to be used, even if port 6667 would normally be blocked to it.

Both local and remote forwarding can be used to provide a secure \"gateway\", allowing other computers to take advantage of an SSH tunnel, without actually running SSH or the SSH daemon by providing a bind-address for the start of the tunnel as part of the forwarding specification, e.g. `<tunnel address>:<tunnel port>:<destination address>:<destination port>`. The `<tunnel address>` can be any address on the machine at the start of the tunnel. The address `localhost` allows connections via the `localhost` or loopback interface, and an empty address or `*` allow connections via any interface. By default, forwarding is limited to connections from the machine at the \"beginning\" of the tunnel, i.e. the `<tunnel address>` is set to `localhost`. Local forwarding requires no additional configuration; however, remote forwarding is limited by the remote server\'s SSH daemon configuration. See the `GatewayPorts` option in [sshd_config(5)](https://man.archlinux.org/man/sshd_config.5) and `-L address` option in [ssh(1)](https://man.archlinux.org/man/ssh.1) for more information about remote forwarding and local forwarding, respectively.

### Jump hosts {#Jump_hosts}

In certain scenarios, there might not be a direct connection to your target SSH daemon, and the use of a jump server (or [bastion server](https://en.wikipedia.org/wiki/bastion_host "wikipedia:bastion host")) is required. Thus, we attempt to connect together two or more SSH tunnels, and assuming your local keys are authorized against each server in the chain. This is possible using SSH agent forwarding (`-A`) and pseudo-terminal allocation (`-t`) which forwards your local key with the following syntax:

    $ ssh -A -t -l user1 bastion1 \
      ssh -A -t -l user2 intermediate2 \
      ssh -A -t -l user3 target

This can be automated with the ProxyCommand option:

    $ ssh -o ProxyCommand="ssh -W %h:%p bastion.example.org" targetserver.example.org

An easier and more secure way to do this is using the ProxyJump option with the `-J` flag:

    $ ssh -J user1@bastion1,user2@intermediate2 user3@target

Multiple hosts in the `-J` directive can be separated with a comma; they will be connected to in the order listed. The `user...@` part is not required, but can be used. The host specifications for `-J` use the ssh configuration file, so specific per-host options can be set there, if needed.

The main difference between the ProxyCommand and ProxyJump options is that the later does not require a shell on the jumphost. Consequently, this also means that the jumpserver does not require access to the users login credentials or SSH agent forwarding. With the ProxyJump option, the ssh client connects through the jumpserver directly to the target server, establishing an end-to-end encrypted channel between client and target server.

An equivalent of the `-J` flag in the configuration file is the `ProxyJump` option; see [ssh_config(5)](https://man.archlinux.org/man/ssh_config.5) for details.

### Reverse SSH through a relay {#Reverse_SSH_through_a_relay}

**This article or section needs language, wiki syntax or style improvements. See [Help:Style](../en/Help:Style.html "Help:Style") for reference.**

**Reason:** The idea of SSH tunneling is classic, so some references for detailed explanation would be nice. E.g. [\[2\]](https://unix.stackexchange.com/questions/46235/how-does-reverse-ssh-tunneling-work/118650#118650) which includes other scenarios. (Discuss in [Talk:OpenSSH](../en/Talk:OpenSSH.html))

The idea is that the client connects to the server via another relay while the server is connected to the same relay using a reverse SSH tunnel. This is useful when the server is behind a NAT, and the relay is a publicly accessible SSH server used as a proxy to which the user has access. Therefore, the prerequisite is that the client\'s keys are authorized against both the relay and the server, and the server needs to be authorized against the relay as well for the reverse SSH connection.

The following configuration example assumes that *`user1`* is the user account used on client, *`user2`* on relay and *`user3`* on server. First, assuming we will use port 2222, the server needs to establish the reverse tunnel with:

    $ ssh -R 2222:localhost:22 -N user2@relay

Which can also be automated with a startup script, systemd service, [autossh](#Autossh_-_automatically_restarts_SSH_sessions_and_tunnels) or [sidedoor](https://aur.archlinux.org/packages/sidedoor/)^AUR^.

At the client side, the connection is established with:

    $ ssh -t user2@relay ssh user3@localhost -p 2222

**Note** `ssh `*`user3`*`@`*`relay`*` -p 2222` would require you to open this port in the firewall of your relay server, as well as to allow connections to this port from other addresses.

The remote command to establish the connection to reverse tunnel can also be defined in relay\'s `authorized_keys` file by including the `command` field as follows:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/authorized_keys
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
command="ssh user3@localhost -p 2222" ssh-ed25519 KEY2 user1@client
```

In this case the connection is established with:

    $ ssh user2@relay

Alternatively, you can add an entry to your ssh configuration that specifies both `RemoteCommand` and `RequestTTY`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Host jump-destination
    Hostname relay
    User user2
    RemoteCommand ssh user3@localhost -p 2222
    RequestTTY yes
```

Which will reduce connecting to:

    $ ssh jump-destination

**Note** SCP\'s autocomplete function in client\'s terminal will not work and even the SCP transfers themselves are not working under some configurations.

### Multiplexing {#Multiplexing}

The SSH daemon usually listens on port 22. However, it is common practice for many public internet hotspots to block all traffic that is not on the regular HTTP/S ports (80 and 443, respectively), thus effectively blocking SSH connections. The immediate solution for this is to have `sshd` listen additionally on one of the whitelisted ports:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Port 22
Port 443
```

However, it is likely that port 443 is already in use by a web server serving HTTPS content, in which case it is possible to use a multiplexer, such as [sslh](https://archlinux.org/packages/?name=sslh), which listens on the multiplexed port and can intelligently forward packets to many services.

### Speeding up SSH {#Speeding_up_SSH}

**This article or section needs expansion.**

**Reason:** Changing cipher from default might introduce security implications and must be noted here *if applicable* (Discuss in [Talk:OpenSSH#Trading_security_for_performance?](../en/Talk:OpenSSH.html#Trading_security_for_performance? "Talk:OpenSSH"))

There are several [client configuration](#Configuration) options which can speed up connections either globally or for specific hosts. See [ssh_config(5)](https://man.archlinux.org/man/ssh_config.5) for full descriptions of these options.

-   *Use a faster cipher*: on modern CPUs with AESNI instructions, `aes128-gcm@openssh.com` and `aes256-gcm@openssh.com` should offer significantly better performance over openssh\'s default preferred cipher, usually `chacha20-poly1305@openssh.com`. Cipher can be selected with the `-c` flag. For a permanent effect, put `Ciphers` option in your `~/.ssh/config` with ciphers in new preferred order, e.g.:

        Ciphers aes128-gcm@openssh.com,aes256-gcm@openssh.com,chacha20-poly1305@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr

&nbsp;

-   *Enable or disable compression*: compression can increase speed on slow connections; it is enabled with the `Compression yes` option or the `-C` flag. However, the compression algorithm used is the relatively slow [gzip(1)](https://man.archlinux.org/man/gzip.1) which becomes the bottleneck on fast networks. In order to speed up the connection, one should use the `Compression no` option on local or fast networks.

&nbsp;

-   *Connection sharing*: you can make all sessions to the same host share a single connection using these options:

        ControlMaster auto
        ControlPersist yes
        ControlPath ~/.ssh/sockets/socket-%r@%h:%p

where `~/.ssh/sockets` can be any directory not writable by other users.

-   `ControlPersist` specifies how long the master should wait in the background for new clients after the initial client connection has been closed. Possible values are either:
    -   `no` to close the connection immediately after the last client disconnects,
    -   a time in seconds,
    -   `yes` to wait forever, the connection will never be closed automatically.

&nbsp;

-   Login time can be shortened by bypassing IPv6 lookup using the `AddressFamily inet` option or `-4` flag.

&nbsp;

-   Last, if you intend to use SSH for SFTP or SCP, [High Performance SSH/SCP](https://www.psc.edu/index.php/hpn-ssh) can significantly increase throughput by dynamically raising the SSH buffer sizes. Install the package [openssh-hpn](https://aur.archlinux.org/packages/openssh-hpn/)^AUR^ to use a patched version of OpenSSH with this enhancement.

### Mounting a remote filesystem with SSHFS {#Mounting_a_remote_filesystem_with_SSHFS}

Please refer to the [SSHFS](../en/SSHFS.html "SSHFS") article to mount a SSH-accessible remote system to a local directory, so you will be able to do any operation on the mounted files with any tool (copy, rename, edit with vim, etc.). *sshfs* is generally preferred over *shfs*, the latter has not been updated since 2004.

### Keep alive {#Keep_alive}

By default, the SSH session automatically logs out if it has been idle for a certain time. To keep the session up, the client can send a keep-alive signal to the server if no data has been received for some time, or symmetrically the server can send messages at regular intervals if it has not heard from the client.

-   On the **server** side, `ClientAliveInterval` sets the timeout in seconds after which if no data has been received from the client, *sshd* will send a request for response. The default is 0, no message is sent. For example to request a response every 60 seconds from the client, set the `ClientAliveInterval 60` option in your [server configuration](#Configuration_2). See also the `ClientAliveCountMax` and `TCPKeepAlive` options.
-   On the **client** side, `ServerAliveInterval` controls the interval between the requests for response sent from the client to the server. For example to request a response every 120 seconds from the server, add the `ServerAliveInterval 120` option to your [client configuration](#Configuration). See also the `ServerAliveCountMax` and `TCPKeepAlive` options.

**Note** To ensure a session is kept alive, only one of either the client or the server needs to send keep alive requests. If ones control both the servers and the clients, a reasonable choice is to only configure the clients that require a persistent session with a positive `ServerAliveInterval` and leave other clients and servers in their default configuration.

### Automatically restart SSH tunnels with systemd {#Automatically_restart_SSH_tunnels_with_systemd}

[systemd](../en/Systemd.html "Systemd") can automatically start SSH connections on boot/login *and* restart them when they fail. This makes it a useful tool for maintaining SSH tunnels.

The following service can start an SSH tunnel on login using the connection settings in your [ssh configuration](#Configuration). If the connection closes for any reason, it waits 10 seconds before restarting it:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.config/systemd/user/tunnel.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=SSH tunnel to myserver

[Service]
Type=simple
Restart=always
RestartSec=10
ExecStart=/usr/bin/ssh -F %h/.ssh/config -N myserver
```

Then [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") and [start](../en/Help:Reading.html#Control_of_systemd_units "Start") the [user unit](../en/User_unit.html "User unit"). See [#Keep alive](#Keep_alive) for how to prevent the tunnel from timing out. If you wish to start the tunnel on boot, you might want to [rewrite the unit](../en/Systemd.html#Writing_unit_files "Systemd") as a system service.

### Autossh - automatically restarts SSH sessions and tunnels {#Autossh_-_automatically_restarts_SSH_sessions_and_tunnels}

When a session or tunnel cannot be kept alive, for example due to bad network conditions causing client disconnections, you can use [autossh](https://archlinux.org/packages/?name=autossh) to automatically restart them.

Usage examples:

    $ autossh -M 0 -o "ServerAliveInterval 45" -o "ServerAliveCountMax 2" username@example.com

Combined with [SSHFS](../en/SSHFS.html "SSHFS"):

    $ sshfs -o reconnect,compression=yes,transform_symlinks,ServerAliveInterval=45,ServerAliveCountMax=2,ssh_command='autossh -M 0' username@example.com: /mnt/example 

Connecting through a SOCKS-proxy set by [Proxy settings](../en/Proxy_settings.html "Proxy settings"):

    $ autossh -M 0 -o "ServerAliveInterval 45" -o "ServerAliveCountMax 2" -NCD 8080 username@example.com 

With the `-f` option autossh can be made to run as a background process. Running it this way however means the passphrase cannot be entered interactively.

The session will end once you type `exit` in the session, or the autossh process receives a SIGTERM, SIGINT of SIGKILL signal.

#### Run autossh automatically at boot via systemd {#Run_autossh_automatically_at_boot_via_systemd}

If you want to automatically start autossh, you can create a systemd unit file:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/autossh.service
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
Description=AutoSSH service for port 2222
After=network.target

[Service]
Environment="AUTOSSH_GATETIME=0"
ExecStart=/usr/bin/autossh -M 0 -NL 2222:localhost:2222 -o TCPKeepAlive=yes foo@bar.com

[Install]
WantedBy=multi-user.target
```

Here `AUTOSSH_GATETIME=0` is an environment variable specifying how long ssh must be up before autossh considers it a successful connection, setting it to 0 autossh also ignores the first run failure of ssh. This may be useful when running autossh at boot. Other environment variables are available at [autossh(1)](https://man.archlinux.org/man/autossh.1). Of course, you can make this unit more complex if necessary (see the systemd documentation for details), and obviously you can use your own options for autossh, but note that the `-f` implying `AUTOSSH_GATETIME=0` does not work with systemd.

Remember to [start](../en/Help:Reading.html#Control_of_systemd_units "Start") and/or [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") the service afterwards.

You may also need to disable `ControlMaster`:

    ExecStart=/usr/bin/autossh -M 0 -o ControlMaster=no -NL 2222:localhost:2222 -o TCPKeepAlive=yes foo@bar.com

**Tip** It is also easy to maintain several autossh processes, to keep several tunnels alive. Just create multiple service files with different names.

### Alternative service should SSH daemon fail {#Alternative_service_should_SSH_daemon_fail}

For remote or headless servers which rely exclusively on SSH, a failure to start the SSH daemon (e.g., after a system upgrade) may prevent administration access. [systemd](../en/Systemd.html "Systemd") offers a simple solution via `OnFailure` option.

Let us suppose the server runs `sshd` and [telnet](../en/Telnet.html "Telnet") is the fail-safe alternative of choice. Create a file as follows. Do **not** [enable](../en/Help:Reading.html#Control_of_systemd_units "Enable") `telnet.socket`!

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/systemd/system/sshd.service.d/override.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[Unit]
OnFailure=telnet.socket
```

That\'s it. Telnet is not available when `sshd` is running. Should `sshd` fail to start, a telnet session can be opened for recovery.

### Terminal background color based on host {#Terminal_background_color_based_on_host}

To better distinguish when you are on different hosts, you can set a [different background color based on the kind of host](https://bryangilbert.com/post/etc/term/dynamic-ssh-terminal-background-colors/).

This solution works, but is not universal (ZSH only).

### Network specific configuration {#Network_specific_configuration}

You can use host configuration specific to the network you are connected to using a `Match exec`.

For example, when using [nmcli(1)](https://man.archlinux.org/man/nmcli.1), and the connection is configured (manually or through DHCP) to use a search-domain:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Match exec "nmcli | grep domains: | grep example.com"
  CanonicalDomains example.com
  # Should you use a different username on this network
  #User username
  # Use a different known_hosts file (for private network or synchronisation)
  #UserKnownHostsFile <network>_known_hosts
```

Another example for `Match host ... exec "..."`: Consider that connecting to `internal.example.com` requires a bastion/proxy (via `ProxyJump`) unless you are already connected via VPN. The fragment `!exec "host internal.example.com"` applies only when `internal.example.com` cannot be looked up via DNS. Various alternatives are discussed at [\[3\]](https://serverfault.com/q/536043/117525).

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Match host internal.example.com !exec "host internal.example.com"
  ProxyJump bastion.example.com
Host internal.example.com
  User foobar
```

### Private networks hostkeys verification {#Private_networks_hostkeys_verification}

Because different servers on different networks are likely to share a common private IP address, you might want to handle them differently.

**The factual accuracy of this article or section is disputed.**

**Reason:** The best solution would not need a warning to use something else in practice. (Discuss in [Talk:OpenSSH](../en/Talk:OpenSSH.html))

The best solution is to use the [#Network specific configuration](#Network_specific_configuration) to use a different `UserKnownHostsFile` depending on the network you are on. The second solution, best used as default when you are working on new/prototype networks, would be to simply ignore hostkeys for private networks:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Host 10.* 192.168.*.* 172.31.* 172.30.* 172.2?.* 172.1?.*
    # Disable HostKey verification
    # Trust HostKey automatically
    StrictHostKeyChecking no
    # Do not save the HostKey
    UserKnownHostsFile=/dev/null
    # Do not display: "Warning: Permanently Added ..."
    LogLevel Error
```

**The factual accuracy of this article or section is disputed.**

**Reason:** The `known_hosts` file records an IP address even when you use hostname to access the server. (Discuss in [Talk:OpenSSH](../en/Talk:OpenSSH.html))

**Warning** In a production environment, make sure to either use the hostname to access the host and/or to use network specific known_hosts files.

### Run command at login {#Run_command_at_login}

If you are using an interactive session, there are multiple ways to execute a command on login:

-   use the `authorized_keys` file on the remote host (see [sshd(8) § AUTHORIZED_KEYS FILE FORMAT](https://man.archlinux.org/man/sshd.8#AUTHORIZED_KEYS_FILE_FORMAT)).
-   use `~/.ssh/rc` on the remote host if the server has enabled the `PermitUserRC` option.
-   use your [shell configuration file](../en/Command-line_shell.html#Configuration_files "Command-line shell") on the remote host. `SSH_CONNECTION` and similar [environment variables](../en/Environment_variables.html "Environment variables") can be used for detecting a SSH session, see [ssh(1) § ENVIRONMENT](https://man.archlinux.org/man/ssh.1#ENVIRONMENT).

### Agent forwarding {#Agent_forwarding}

SSH agent forwarding allows you to use your local keys when connected to a server. It is [recommended](https://security.stackexchange.com/questions/7480/risks-of-ssh-to-an-untrusted-host#7504) to only enable agent forwarding for selected hosts.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Host myserver.com
    ForwardAgent yes
```

Next, configure an [SSH agent](../en/SSH_agent.html "SSH agent") and add your local key with *ssh-add*.

If you now connect to a remote server you will be able to connect to other services using your local keys.

### Generating new keys {#Generating_new_keys}

New server private keys can be generated by:

1.  Deleting all the keys, e.g.:

        # rm /etc/ssh/ssh_host_*_key*

2.  [Restarting](../en/Help:Reading.html#Control_of_systemd_units "Restart") `sshdgenkeys.service` or running `ssh-keygen -A` as root.

A more graceful alternative is to transition. First, generate the new host keys:

    # ssh-keygen -t rsa -b 4096 -f /etc/ssh/ssh_host_rsa_key.new
    # ssh-keygen -t ecdsa -b 521 -f /etc/ssh/ssh_host_ecdsa_key.new
    # ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key.new

Add both old and new keys to `/etc/ssh/sshd_config.d/10-hostkeys.conf`:

    HostKey /etc/ssh/ssh_host_ecdsa_key
    HostKey /etc/ssh/ssh_host_ecdsa_key.new
    HostKey /etc/ssh/ssh_host_ed25519_key
    HostKey /etc/ssh/ssh_host_ed25519_key.new
    HostKey /etc/ssh/ssh_host_rsa_key
    HostKey /etc/ssh/ssh_host_rsa_key.new

[Restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `sshd.service`.

Clients will learn the host\'s new key fingerprints and add them to `~/.ssh/known-hosts` the next time they connect to the server.

After a while, the old keys can be removed from `/etc/ssh/sshd_config.d/10-hostkeys.conf`, leaving only the new keys:

    HostKey /etc/ssh/ssh_host_ecdsa_key.new
    HostKey /etc/ssh/ssh_host_ed25519_key.new
    HostKey /etc/ssh/ssh_host_rsa_key.new

[Restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `sshd.service`, then physically remove the old keys:

    # rm /etc/ssh/ssh_host_{ecdsa,ed25519,rsa}_key

Again, clients will automatically adjust `~/.ssh/known-hosts` to remove fingerprints corresponded to the old keys.

### Run sshd as non-privileged user {#Run_sshd_as_non-privileged_user}

You may want to run `sshd` as non-privileged user in containers, or for testing, etc.

Since non-privileged user cannot read host keys in `/etc/ssh`, new host keys must be generated:

    $ ssh-keygen -q -N "" -t rsa -b 4096 -f /path/to/host/keys/ssh_host_rsa_key
    $ ssh-keygen -q -N "" -t ecdsa -f /path/to/host/keys/ssh_host_ecdsa_key
    $ ssh-keygen -q -N "" -t ed25519 -f /path/to/host/keys/ssh_host_ed25519_key

Create an `sshd_config` file. The example below uses a port higher than 1024, provides a new path to the host keys and disables PAM:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/path/to/sshd_config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Port 2022
HostKey /path/to/host/keys/ssh_host_rsa_key
HostKey /path/to/host/keys/ssh_host_ecdsa_key
HostKey /path/to/host/keys/ssh/ssh_host_ed25519_key
UsePAM no
```

Run *sshd* with the created config. The `-D` flag disables daemon mode and `-e` redirects output to stderr to allow easy monitoring.

    $ sshd -f /path/to/sshd_config -D -e

## Troubleshooting {#Troubleshooting}

### Checklist {#Checklist}

Check these simple issues before you look any further.

1.  The configuration directory `~/.ssh`, its contents should be accessible only by the user (check this on both the client and the server), and the user\'s home directory should only be writable by the user:

        $ chmod go-w ~
        $ chmod 700 ~/.ssh
        $ chmod 600 ~/.ssh/*
        $ chown -R $USER ~/.ssh

2.  Check that the client\'s public key (e.g. `id_ed25519.pub`) is in `~/.ssh/authorized_keys` on the server.

3.  Check that you did not limit SSH access with `AllowUsers` or `AllowGroups` in the [server config](#Configuration_2).

4.  Check if the user has set a password. Sometimes new users who have not yet logged in to the server do not have a password.

5.  [Append](../en/Help:Reading.html#Append,_add,_create,_edit "Append") `LogLevel DEBUG` to `/etc/ssh/sshd_config`.

6.  Run `journalctl -xe` as root for possible (error) messages.

7.  [Restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") `sshd` and logout/login on both client and server.

### Connection refused or timeout problem {#Connection_refused_or_timeout_problem}

#### Port forwarding {#Port_forwarding}

If you are behind a NAT mode/router (which is likely unless you are on a VPS or publicly addressed host), make sure that your router is forwarding incoming ssh connections to your machine. Find the server\'s internal IP address with `ip addr` and set up your router to forward TCP on your SSH port to that IP. [portforward.com](https://portforward.com) can help with that.

#### Is SSH running and listening? {#Is_SSH_running_and_listening?}

The [ss](../en/Network_configuration.html#Investigate_sockets "Ss") utility shows all the processes listening to a TCP port with the following command line:

    $ ss --tcp --listening

If the above command do not show the system is listening to the port `ssh`, then SSH is not running: check the [journal](../en/Systemd/Journal.html "Journal") for errors etc.

#### Are there firewall rules blocking the connection? {#Are_there_firewall_rules_blocking_the_connection?}

[Iptables](../en/Iptables.html "Iptables") may be blocking connections on port `22`. Check this with:

    # iptables -nvL

and look for rules that might be dropping packets on the `INPUT` chain. Then, if necessary, unblock the port with a command like:

    # iptables -I INPUT 1 -p tcp --dport 22 -j ACCEPT

For more help configuring firewalls, see [firewalls](../en/Category:Firewalls.html "Firewalls").

#### Is the traffic even getting to your computer? {#Is_the_traffic_even_getting_to_your_computer?}

Start a traffic dump on the computer you are having problems with:

    # tcpdump -lnn -i any port ssh and tcp-syn

This should show some basic information, then wait for any matching traffic to happen before displaying it. Try your connection now. If you do not see any output when you attempt to connect, then something outside of your computer is blocking the traffic (e. g., hardware firewall, NAT router etc.).

#### Your ISP or a third party blocking default port? {#Your_ISP_or_a_third_party_blocking_default_port?}

**Note** Try this step if you **know** you are not running any firewalls and you know you have configured the router for DMZ or have forwarded the port to your computer and it still does not work. Here you will find diagnostic steps and a possible solution.

In some cases, your ISP might block the default port (SSH port 22) so whatever you try (opening ports, hardening the stack, defending against flood attacks, et al) ends up useless. To confirm this, create a server on all interfaces (0.0.0.0) and connect remotely.

If you get an error message comparable to this:

    ssh: connect to host www.inet.hr port 22: Connection refused

That means the port is **not** being blocked by the ISP, but the server does not run SSH on that port (See [security through obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity "wikipedia:Security through obscurity")).

However, if you get an error message comparable to this:

    ssh: connect to host 111.222.333.444 port 22: Operation timed out 

That means that something is rejecting your TCP traffic on port 22. Basically that port is stealth, either by your firewall or 3rd party intervention (like an ISP blocking and/or rejecting incoming traffic on port 22). If you know you are not running any firewall on your computer, and you know that Gremlins are not growing in your routers and switches, then your ISP is blocking the traffic.

To double check, you can run Wireshark on your server and listen to traffic on port 22. Since Wireshark is a Layer 2 Packet Sniffing utility, and TCP/UDP are Layer 3 and above (see [IP Network stack](https://en.wikipedia.org/wiki/Internet_protocol_suite "wikipedia:Internet protocol suite")), if you do not receive anything while connecting remotely, a third party is most likely to be blocking the traffic on that port to your server.

##### Diagnosis {#Diagnosis}

[Install](../en/Help:Reading.html#Installation_of_packages "Install") either [tcpdump](https://archlinux.org/packages/?name=tcpdump) or Wireshark with the [wireshark-cli](https://archlinux.org/packages/?name=wireshark-cli) package.

For tcpdump:

    # tcpdump -ni interface "port 22"

For Wireshark:

    $ tshark -f "tcp port 22" -i interface

where *`interface`* is the network interface for a WAN connection (see `ip a` to check). If you are not receiving any packets while trying to connect remotely, you can be very sure that your ISP is blocking the incoming traffic on port 22.

##### Possible solution {#Possible_solution}

The solution is just to use some other port that the ISP is not blocking. Open the `/etc/ssh/sshd_config` and configure the file to use different ports. For example, add:

    Port 22
    Port 1234

Also make sure that other \"Port\" configuration lines in the file are commented out. Just commenting \"Port 22\" and putting \"Port 1234\" will not solve the issue because then sshd will only listen on port 1234. Use both lines to run the SSH server on both ports.

[Restart](../en/Help:Reading.html#Control_of_systemd_units "Restart") the server `sshd.service` and you are almost done. You still have to configure your client(s) to use the other port instead of the default port. There are numerous solutions to that problem, but let us cover two of them here.

#### Read from socket failed: connection reset by peer {#Read_from_socket_failed:_connection_reset_by_peer}

Recent versions of OpenSSH sometimes fail with the above error message when connecting to older ssh servers. This can be worked around by setting various [client options](#Configuration) for that host. See [ssh_config(5)](https://man.archlinux.org/man/ssh_config.5) for more information about the following options.

The problem could be the `ecdsa-sha2-nistp*-cert-v01@openssh` elliptical host key algorithms. These can be disabled by setting `HostKeyAlgorithms` to a list excluding those algorithms. On the client side, the `HostKeyAlgorithms` that the client wants to use can also be set by preceding the `HostKeyAlgorithms` list with a `-` to remove the specified algorithms (including wildcards) from the default set (see [ssh_config(5)](https://man.archlinux.org/man/ssh_config.5)). You can check the actually used host key algorithm with `ssh -v server_to_connect_to` in the line that contains `kex: host key algorithm:`.

If that does not work, it could be that the list of ciphers is too long. Set the `Ciphers` option to a shorter list (fewer than 80 characters should be enough). Similarly, you can also try shortening the list of `MACs`.

See also the [discussion](https://web.archive.org/web/20161201015151/https://www.gossamer-threads.com/lists/openssh/dev/51339) on the OpenSSH bug forum.

### \"\[your shell\]: No such file or directory\" / ssh_exchange_identification problem {#\"[your_shell]:_No_such_file_or_directory\"_/_ssh_exchange_identification_problem}

One possible cause for this is the need of certain SSH clients to find an absolute path (one returned by `whereis -b [your shell]`, for instance) in `$SHELL`, even if the shell\'s binary is located in one of the `$PATH` entries.

### \"Terminal unknown\" or \"Error opening terminal\" error message {#\"Terminal_unknown\"_or_\"Error_opening_terminal\"_error_message}

If you receive the above errors upon logging in, this means the server does not recognize your terminal. ncurses applications like nano may fail with the message `Error opening terminal`.

The correct solution is to install the client terminal\'s terminfo file on the server. This tells console programs on the server how to correctly interact with your terminal. You can get info about current terminfo using `infocmp` and then find out [which package owns it](../en/Pacman.html#Querying_package_databases "Pacman").

If you cannot [install](../en/Help:Reading.html#Installation_of_packages "Install") it normally, you can copy your terminfo to your home directory on the server:

    $ ssh myserver mkdir -p  ~/.terminfo/${TERM:0:1}
    $ scp /usr/share/terminfo/${TERM:0:1}/$TERM myserver:~/.terminfo/${TERM:0:1}/

After logging in and out from the server the problem should be fixed.

#### TERM hack {#TERM_hack}

**Note** This should only be used as a last resort.

Alternatively, you can simply set `TERM=xterm` in your environment on the server (e.g. in `.bash_profile`). This will silence the error and allow ncurses applications to run again, but you may experience strange behavior and graphical glitches unless your terminal\'s control sequences exactly match xterm\'s.

### Connection closed by x.x.x.x \[preauth\] {#Connection_closed_by_x.x.x.x_[preauth]}

If you are seeing this error in your sshd logs, make sure you have set a valid `HostKey`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
HostKey /etc/ssh/ssh_host_ed25519_key
```

### subsystem request failed {#subsystem_request_failed}

Since *OpenSSH* 8.8, *scp* uses *SFTP* as the default protocol for data transfers by requesting the subsystem named `sftp`. If you run *scp* in verbose mode, `scp -v`, you can determine which subsystem your client is using (e.g. `Sending subsystem: <subsystem-name>`). Errors such as `subsystem request failed on channel 0` may be fixed by configuring the server\'s Subsystem settings: [sshd_config(5) § Subsystem](https://man.archlinux.org/man/sshd_config.5#Subsystem). The server configuration should resemble the example below.

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/sshd_config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
...
Subsystem subsystem-name /path/to/subsystem-executable
...
```

### id_dsa refused {#id_dsa_refused}

OpenSSH 7.0 deprecated DSA public keys for security reasons and OpenSSH 9.8 is built without support for DSA keys by default. The first OpenSSH release of 2025 will remove DSA support entirely. For now, if you absolutely must use them, you will need to rebuild [openssh](https://archlinux.org/packages/?name=openssh) while passing `--enable-dsa-keys` to `configure`.[\[4\]](https://marc.info/?l=openssh-unix-dev&m=171982945528949&w=2)

### No matching key exchange method found by OpenSSH 7.0 {#No_matching_key_exchange_method_found_by_OpenSSH_7.0}

OpenSSH 7.0 deprecated the diffie-hellman-group1-sha1 key algorithm because it is weak and within theoretical range of the so-called Logjam attack (see [https://www.openssh.com/legacy.html](https://www.openssh.com/legacy.html)). If the key algorithm is needed for a particular host, ssh will produce an error message like this:

    Unable to negotiate with 127.0.0.1: no matching key exchange method found.
    Their offer: diffie-hellman-group1-sha1

The best resolution for these failures is to upgrade/configure the server to not use deprecated algorithms. If that is not possible, you can force the client to reenable the algorithm with the [client option](#Configuration) `KexAlgorithms +diffie-hellman-group1-sha1`.

### tmux/screen session killed when disconnecting from SSH {#tmux/screen_session_killed_when_disconnecting_from_SSH}

**The factual accuracy of this article or section is disputed.**

**Reason:** The caveat must be solved because `logind` is used by default. (Discuss in [Talk:OpenSSH](../en/Talk:OpenSSH.html))

Paraphrased from [a unix stackexchange answer](https://unix.stackexchange.com/a/176292):

If your processes are killed at the end of the ssh session, it is possible that you are using socket activation. Your process is killed by [systemd](https://archlinux.org/packages/?name=systemd) when it notices that the SSH session process exited. In that case there are two solutions:

-   Avoid using socket activation by migrating to `sshd.service` (recommended, see [#Socket activation](#Socket_activation)), or
-   Set `KillMode=process` in the `[Service]` section of `sshd@.service`.

Though not necessary, setting `KillMode=process` in `sshd.service` may also be useful as it avoids killing the SSH session process and its [screen](https://archlinux.org/packages/?name=screen) or [tmux](https://archlinux.org/packages/?name=tmux) process when the server is stopped or restarted.

Note the caveat that this may not work with `logind`.

### SSH session stops responding {#SSH_session_stops_responding}

SSH responds to [flow control commands](https://en.wikipedia.org/wiki/Software_flow_control "wikipedia:Software flow control") `XON` and `XOFF`. It will freeze/hang/stop responding when you hit `Ctrl+s`. Use `Ctrl+q` to resume your session.

### Broken pipe {#Broken_pipe}

If you attempt to create a connection which results in a `Broken pipe` response for `packet_write_wait`, you should reattempt the connection in debug mode and see if the output ends in error:

    debug3: send packet: type 1
    packet_write_wait: Connection to A.B.C.D port 22: Broken pipe

The `send packet` line above indicates that the reply packet was never received. So, it follows that this is a *QoS* issue. To decrease the likely-hood of a packet being dropped, set `IPQoS`:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/ssh/ssh_config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Match all
    IPQoS reliability
```

The `reliability` (`0x04`) type-of-service should resolve the issue, as well as `0x00` and `throughput` (`0x08`).

### Terminate unresponsive SSH connection {#Terminate_unresponsive_SSH_connection}

If a client session is no longer responding and cannot be terminated by instructing the running program (e.g. [shell](../en/Command-line_shell.html "Shell")), you can still terminate the session by pressing `Enter`, `~` and `.` one after another in that order.

The `~` is a pseudo-terminal escape character (see [ssh(1) § ESCAPE CHARACTERS](https://man.archlinux.org/man/ssh.1#ESCAPE_CHARACTERS)), which can be added multiple times depending on the client session to terminate. For example, if you connected from A to B and then from B to C and the session from B to C freezes, you can terminate it by pressing `Enter` and typing `~~.`, which will leave you in a working session on B.

### WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! {#WARNING:_REMOTE_HOST_IDENTIFICATION_HAS_CHANGED!}

If the client warns that the key of an ssh server has changed, you should verify that the newly offered key really belongs to the server operator via an authenticated (not necessarily encrypted) channel. Then remove the old key from the `known_hosts` file with `ssh-keygen -R $SSH_HOST` and accept the new key as if it was a new server.

### Connecting to a remote without the appropriate terminfo entry {#Connecting_to_a_remote_without_the_appropriate_terminfo_entry}

When connecting to hosts that do not have a terminfo entry for your terminal, for example, when using a terminal emulator whose terminfo entry is not shipped with [ncurses](https://archlinux.org/packages/?name=ncurses) (e.g. [kitty](../en/Kitty.html "Kitty") and [rxvt-unicode](../en/Rxvt-unicode.html "Rxvt-unicode")), or when connecting to hosts with a limited terminfo database (e.g. systems running [OpenWrt](https://en.wikipedia.org/wiki/OpenWrt "wikipedia:OpenWrt")), various issues will occur with software that relies on [terminfo(5)](https://man.archlinux.org/man/terminfo.5).

A proper solution is to place the appropriate terminfo entry on the host. If that is not feasible, an alternative is to set `TERM` to a value that is both supported by the remote host and compatible with the terminal.

Since OpenSSH 8.7, a custom `TERM` environment variable can be passed to remote hosts with a simple configuration snippet:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
~/.ssh/config
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Host example.com
  SetEnv TERM=xterm-256color
```

### Connection through jump host fails with \"bash: No such file or directory\" {#Connection_through_jump_host_fails_with_\"bash:_No_such_file_or_directory\"}

If you do not have the `SHELL` environment variable set to a full valid path (on the jump server), connection will fail with an error message simmilar to this one:

    bash: No such file or directory
    kex_exchange_identification: Connection closed by remote host
    Connection closed by UNKNOWN port 65535

You can simply solve this by setting your `SHELL` to a full path name of a shell that will also be valid on the jump server or by setting a specific `SHELL` variable for each server in your `~/.ssh/config` file.

\

## See also {#See_also}

-   [Wikibooks:OpenSSH](https://en.wikibooks.org/wiki/OpenSSH "wikibooks:OpenSSH")
-   [Defending against brute force ssh attacks](https://www.la-samhna.de/library/brutessh.html)
-   OpenSSH key management: [Part 1](https://www.ibm.com/developerworks/library/l-keyc/index.html) on IBM developerWorks, [Part 2](https://www.funtoo.org/OpenSSH_Key_Management,_Part_2 "funtoo:OpenSSH Key Management, Part 2"), [Part 3](https://www.funtoo.org/OpenSSH_Key_Management,_Part_3 "funtoo:OpenSSH Key Management, Part 3") on funtoo.org
-   [Secure Secure Shell](https://stribika.github.io/2015/01/04/secure-secure-shell.html)
