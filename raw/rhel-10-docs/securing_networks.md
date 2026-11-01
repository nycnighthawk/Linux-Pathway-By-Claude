---
{"title": "Securing networks", "guide": "securing_networks", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/securing_networks/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Securing networks {#securing-networks .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Configuring secured networks and network communication {#configuring-secured-networks-and-network-communication .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140168172028816)

**Abstract**

Learn the tools and techniques to improve the security of your networks and lower the risks of data breaches and intrusions.

------------------------------------------------------------------------

## [Providing feedback on Red Hat documentation](#providing-feedback-on-red-hat-documentation) {#providing-feedback-on-red-hat-documentation .title}

We are committed to providing high-quality documentation and value your feedback. To help us improve, you can submit suggestions or report errors through the Red Hat Jira tracking system.

**Procedure**

1.  Log in to the [Jira](https://redhat.atlassian.net/jira/software/c/projects/RHELDOCS/issues/) website.

    If you do not have an account, select the option to create one.

2.  Click **Create** in the top navigation bar.

3.  Enter a descriptive title in the **Summary** field.

4.  Enter your suggestion for improvement in the **Description** field. Include links to the relevant parts of the documentation.

5.  Click **Create** at the bottom of the window.

## [Chapter 1. Using secure communications between two systems with OpenSSH](#using-secure-communications-between-two-systems-with-openssh) {#chapter-1.-using-secure-communications-between-two-systems-with-openssh .title}

Use OpenSSH to create secure communication between two systems. OpenSSH encrypts the connection. It protects remote login sessions from eavesdropping and intrusions.

### [1.1. SSH and OpenSSH](#ssh-and-openssh) {#ssh-and-openssh .title}

SSH (Secure Shell) is a program for remote machine login and command execution. The SSH protocol provides encrypted communication between two untrusted hosts over an insecure network. You can also forward X11 connections and arbitrary TCP/IP ports over the secure channel.

The SSH protocol reduces security threats when you use it for remote shell login or file copying. It prevents interception of communication between two systems. It also prevents impersonation of a particular host.

The SSH client and server use digital signatures to verify their identities. All communication between the client and server systems is encrypted.

A host key authenticates hosts in the SSH protocol. Host keys are cryptographic keys. They are generated automatically when OpenSSH starts for the first time or when the host boots for the first time.

OpenSSH is an implementation of the SSH protocol supported by Linux, UNIX, and similar operating systems. It includes the core files necessary for both the OpenSSH client and server. The OpenSSH suite consists of the following user-space tools:

-   `ssh`{.literal} is a remote login program (SSH client).
-   `sshd`{.literal} is an OpenSSH SSH daemon.
-   `scp`{.literal} is a secure remote file copy program.
-   `sftp`{.literal} is a secure file transfer program.
-   `ssh-agent`{.literal} is an authentication agent for caching private keys.
-   `ssh-add`{.literal} adds private key identities to `ssh-agent`{.literal}.
-   `ssh-keygen`{.literal} generates, manages, and converts authentication keys for `ssh`{.literal}.
-   `ssh-copy-id`{.literal} is a script that adds local public keys to the `authorized_keys`{.literal} file on a remote SSH server.
-   `ssh-keyscan`{.literal} gathers SSH public host keys.

For more information, use the `man -k ssh`{.literal} command.

Note

In RHEL 9 and later, SFTP replaces SCP by default. SCP has security issues such as CVE-2020-15778.

You can force the use of the original SCP/RCP protocol if SFTP is unavailable or incompatible in your scenario. Use the `scp`{.literal} command with the `-O`{.literal} option.

The OpenSSH suite in RHEL supports only SSH version 2. It has an enhanced key-exchange algorithm. This algorithm is not vulnerable to exploits known in the older version 1.

Red Hat Enterprise Linux includes the `openssh`{.literal}, `openssh-server`{.literal}, and `openssh-clients`{.literal} packages. These OpenSSH packages require the OpenSSL package `openssl-libs`{.literal}. This package contains cryptographic libraries for securing data exchange.

OpenSSH is one of the core cryptographic subsystems of RHEL. It uses system-wide cryptographic policies. This ensures that weak cipher suites and cryptographic algorithms are disabled in the default configuration.

To modify the policy, you can:

-   Use the `update-crypto-policies`{.literal} command to adjust the settings.
-   Manually opt out of the system-wide cryptographic policies.

The OpenSSH suite uses two sets of configuration files. One set is for client programs (`ssh`{.literal}, `scp`{.literal}, and `sftp`{.literal}). Another set is for the server (the `sshd`{.literal} daemon).

System-wide SSH configuration information is stored in the `/etc/ssh/`{.literal} directory. The `/etc/ssh/ssh_config`{.literal} file contains the client configuration. The `/etc/ssh/sshd_config`{.literal} file is the default OpenSSH server configuration file.

User-specific SSH configuration information is stored in `~/.ssh/`{.literal}. For a detailed list of OpenSSH configuration files, see the `FILES`{.literal} section in the `sshd(8)`{.literal} man page on your system.

**Additional resources**

-   [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies)
-   [Excluding an application from following system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies#excluding-an-application-from-following-systemwide-crypto-policies)
-   [OpenSSH SCP protocol deprecation in Red Hat Enterprise Linux 9](https://access.redhat.com/articles/6955319)
-   [CVE-2020-15778](https://access.redhat.com/security/cve/CVE-2020-15778)

### [1.2. Generating SSH key pairs](#generating-ssh-key-pairs) {#generating-ssh-key-pairs .title}

Generate an SSH key pair on your local system and copy the public key to the OpenSSH server to enable password-free login. Each user who wants to create a key must run this procedure.

To preserve generated key pairs after you reinstall the system, back up the `~/.ssh/`{.literal} directory before you create new keys. After reinstalling, copy it back to your home directory. You can do this for all users on your system, including `root`{.literal}.

**Prerequisites**

-   You are logged in as a user who wants to connect to the OpenSSH server by using keys.
-   The OpenSSH server is configured to allow key-based authentication.

**Procedure**

1.  Generate an ECDSA key pair:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh-keygen -t ecdsa
    Generating public/private ecdsa key pair.
    Enter file in which to save the key (/home/<username>/.ssh/id_ecdsa):
    Enter passphrase (empty for no passphrase): <password>
    Enter same passphrase again: <password>
    Your identification has been saved in /home/<username>/.ssh/id_ecdsa.
    Your public key has been saved in /home/<username>/.ssh/id_ecdsa.pub.
    The key fingerprint is:
    SHA256:Q/x+qms4j7PCQ0qFd09iZEFHA+SqwBKRNaU72oZfaCI <username>@<localhost.example.com>
    The key's randomart image is:
    +---[ECDSA 256]---+
    |.oo..o=++        |
    |.. o .oo .       |
    |. .. o. o        |
    |....o.+...       |
    |o.oo.o +S .      |
    |.=.+.   .o       |
    |E.*+.  .  . .    |
    |.=..+ +..  o     |
    |  .  oo*+o.      |
    +----[SHA256]-----+
    ```

    Alternative: Instead of ECDSA, you can generate:

    -   an RSA key pair by using the `ssh-keygen`{.literal} command without any parameter

    -   an Ed25519 key pair by entering the `ssh-keygen -t ed25519`{.literal} command

        Note that the Ed25519 algorithm is not FIPS-140-compliant, and OpenSSH does not work with Ed25519 keys in FIPS mode.

2.  Copy the public key to a remote machine:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh-copy-id <username>@<ssh-server-example.com>
    /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
    <username>@<ssh-server-example.com>'s password:
    …
    Number of key(s) added: 1

    Now try logging into the machine, with: "ssh '<username>@<ssh-server-example.com>'" and check to make sure that only the key(s) you wanted were added.
    ```

    Replace *`<username>`{.literal}*`@`{.literal}*`<ssh-server-example.com>`{.literal}* with your credentials.

    If you do not use `ssh-agent`{.literal}, the command copies the most recently modified `~/.ssh/id*.pub`{.literal} public key. To use a different public-key file, or to prefer keys from files over keys stored in memory by `ssh-agent`{.literal}, use the `ssh-copy-id`{.literal} command with the `-i`{.literal} option.

**Verification**

1.  Log in to the OpenSSH server by using the key file:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -o PreferredAuthentications=publickey <username>@<ssh-server-example.com>
    ```

### [1.3. Setting key-based authentication as the only method on an OpenSSH server](#setting-key-based-authentication-as-the-only-method-on-an-openssh-server) {#setting-key-based-authentication-as-the-only-method-on-an-openssh-server .title}

To improve system security, enforce key-based authentication by disabling password authentication on your OpenSSH server.

Warning

If you disable password authentication without ensuring that key-based authentication works correctly, you can lock yourself out of the server. Test your SSH key authentication thoroughly before applying this configuration, and keep a current session open while testing to revert changes if necessary.

**Prerequisites**

-   The `openssh-server`{.literal} package is installed.

-   The `sshd`{.literal} daemon is running on the server.

-   You can already connect to the OpenSSH server by using a key.

    See the [Generating SSH key pairs](#generating-ssh-key-pairs "1.2. Generating SSH key pairs") section for details.

**Procedure**

1.  Open the `/etc/ssh/sshd_config`{.literal} configuration in a text editor, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/ssh/sshd_config
    ```

2.  Change the `PasswordAuthentication`{.literal} option to `no`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    PasswordAuthentication no
    ```

3.  On a system other than a new default installation, check that the `PubkeyAuthentication`{.literal} parameter is either not set or set to `yes`{.literal}.

4.  Set the `KbdInteractiveAuthentication`{.literal} directive to `no`{.literal}.

    The corresponding entry is commented out in the configuration file and the default value is `yes`{.literal}.

5.  To use key-based authentication with NFS-mounted home directories, enable the `use_nfs_home_dirs`{.literal} SELinux boolean:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool -P use_nfs_home_dirs 1
    ```

6.  Reload the `sshd`{.literal} daemon to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload sshd
    ```

7.  If you are connected remotely, test the configuration by opening a new SSH session in a separate terminal while keeping your current session open. If the new connection fails, you can revert the changes in your existing session.

**Verification**

1.  Confirm that password authentication is disabled:

    ``` {.language-plaintext tabindex="-1"}
    # sshd -T | grep -i passwordauthentication
    passwordauthentication no
    ```

2.  Confirm that keyboard-interactive authentication is disabled:

    ``` {.language-plaintext tabindex="-1"}
    # sshd -T | grep -i kbdinteractiveauthentication
    kbdinteractiveauthentication no
    ```

3.  From a different system, attempt to connect using password authentication to verify it is rejected:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -o PreferredAuthentications=password <username>@<server>
    <username>@<server>: Permission denied (publickey).
    ```

    The connection is rejected because only public key authentication is allowed.

### [1.4. Authenticating by SSH keys stored on a smart card](#authenticating-by-ssh-keys-stored-on-a-smart-card) {#authenticating-by-ssh-keys-stored-on-a-smart-card .title}

Use SSH keys stored on a smart card for authentication to add a physical layer of protection to your credentials. This method provides enhanced security against unauthorized access.

You can create and store ECDSA and RSA keys on a smart card and authenticate by the smart card on an OpenSSH client. Smart-card authentication replaces the default password authentication.

**Prerequisites**

-   On the client side, the `opensc`{.literal} package is installed and the `pcscd`{.literal} service is running.

**Procedure**

1.  List all keys provided by the OpenSC PKCS #11 module including their PKCS #11 URIs and save the output to the `keys.pub`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh-keygen -D pkcs11: > keys.pub
    ```

2.  Transfer the public key to the remote server. Use the `ssh-copy-id`{.literal} command with the `keys.pub`{.literal} file created in the previous step:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh-copy-id -f -i keys.pub <username@ssh-server-example.com>
    ```

3.  Connect to *`<ssh-server-example.com>`{.literal}* by using the ECDSA key. You can use just a subset of the URI, which uniquely references your key, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i "pkcs11:id=%01?module-path=/usr/lib64/pkcs11/opensc-pkcs11.so" <ssh-server-example.com>
    Enter PIN for 'SSH key':
    [ssh-server-example.com] $
    ```

    Because OpenSSH uses the `p11-kit-proxy`{.literal} wrapper and the OpenSC PKCS #11 module is registered to the `p11-kit`{.literal} tool, you can simplify the previous command:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i "pkcs11:id=%01" <ssh-server-example.com>
    Enter PIN for 'SSH key':
    [ssh-server-example.com] $
    ```

    If you skip the `id=`{.literal} part of a PKCS #11 URI, OpenSSH loads all keys that are available in the proxy module. This can reduce the amount of typing required:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i pkcs11: <ssh-server-example.com>
    Enter PIN for 'SSH key':
    [ssh-server-example.com] $
    ```

4.  Optional: You can use the same URI string in the `~/.ssh/config`{.literal} file to make the configuration permanent:

    ``` {.language-plaintext tabindex="-1"}
    $ cat ~/.ssh/config
    IdentityFile "pkcs11:id=%01?module-path=/usr/lib64/pkcs11/opensc-pkcs11.so"
    $ ssh <ssh-server-example.com>
    Enter PIN for 'SSH key':
    [ssh-server-example.com] $
    ```

    The `ssh`{.literal} client utility now automatically uses this URI and the key from the smart card.

### [1.5. Making OpenSSH more secure](#making-openssh-more-secure) {#making-openssh-more-secure .title}

Harden your system security by modifying OpenSSH configurations, such as implementing stronger keys and restricting user access. This helps protect your server against various attacks.

To make SSH truly effective, prevent the use of insecure connection protocols and replace them with the OpenSSH suite. Otherwise, a user's password might be protected by SSH for one session only, only to be captured later when logging in through Telnet. Also, disabling passwords for authentication and allowing only key pairs reduces the attack surface.

In RHEL 10, the `PermitRootLogin`{.literal} option is set to `prohibit-password`{.literal} by default. This enforces key-based authentication instead of passwords for logging in as root and reduces risk by preventing brute-force attacks.

Warning

Enabling logging in as the root user is not a secure practice because the administrator cannot audit which users run which privileged commands. For using administrative commands, log in and use `sudo`{.literal} instead.

#### [1.5.1. Creating and enforcing stronger SSH key types](#creating-and-forcing-stronger-ssh-key-types) {#creating-and-enforcing-stronger-ssh-key-types .title}

Generate only ECDSA or Ed25519 keys to use their security and performance advantages over older algorithms. You can also configure the OpenSSH server to disable the automatic generation of RSA host keys and enforce the use of stronger key types.

You can instruct the `ssh-keygen`{.literal} command to generate Elliptic Curve Digital Signature Algorithm (ECDSA) or Edwards-Curve 25519 (Ed25519) keys by using the `-t`{.literal} option. The ECDSA offers better performance than RSA at the equivalent symmetric key strength. It also generates shorter keys. The Ed25519 public-key algorithm is an implementation of twisted Edwards curves that is more secure and also faster than RSA, DSA, and ECDSA.

Important

The Ed25519 algorithm is not FIPS-140-compliant, and OpenSSH does not work with Ed25519 keys in FIPS mode.

**Prerequisites**

-   The `openssh-server`{.literal} package is installed on your system.

**Procedure**

1.  To configure the host key creation in RHEL, use the `sshd-keygen@.service`{.literal} instantiated service. For example, to disable the automatic creation of the RSA key type:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl mask sshd-keygen@rsa.service
    ```

    Note

    In images with the `cloud-init`{.literal} method enabled, the `ssh-keygen`{.literal} units are automatically disabled. This is because the `ssh-keygen template`{.literal} service can interfere with the `cloud-init`{.literal} tool and cause problems with host key generation. To prevent these problems, the `etc/systemd/system/sshd-keygen@.service.d/disable-sshd-keygen-if-cloud-init-active.conf`{.literal} drop-in configuration file disables the `ssh-keygen`{.literal} units if `cloud-init`{.literal} is running.

2.  Because OpenSSH creates RSA, ECDSA, and Ed25519 server host keys automatically if they are missing, remove the keys with less secure cryptography:

    ``` {.language-plaintext tabindex="-1"}
    # rm -f /etc/ssh/ssh_host_rsa_key
    ```

3.  To allow only a particular key type for SSH connections, uncomment the relevant line in `/etc/ssh/sshd_config`{.literal}. For example, to allow only Ed25519 host keys, the corresponding lines must be as follows:

    ``` {.language-plaintext tabindex="-1"}
    # HostKey /etc/ssh/ssh_host_rsa_key
    # HostKey /etc/ssh/ssh_host_ecdsa_key
    HostKey /etc/ssh/ssh_host_ed25519_key
    ```

4.  Restart the `sshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sshd
    ```

**Verification**

-   Verify that only the configured host key types exist:

    ``` {.language-plaintext tabindex="-1"}
    # ls -l /etc/ssh/ssh_host_*_key
    ```

    The output shows only the key types you configured. If you enforce Ed25519 only, only `ssh_host_ed25519_key`{.literal} files appear.

-   Verify the SSH server uses only the configured key types by connecting from a client:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -v <server> 2>&1 | grep "Server host key"
    Server host key: ssh-ed25519 SHA256:...
    ```

#### [1.5.2. Customizing allowed cryptography on OpenSSH servers](#customizing-allowed-cryptography-on-openssh-servers) {#customizing-allowed-cryptography-on-openssh-servers .title}

You can specify the cryptography configuration of your OpenSSH server either by using the `/etc/ssh/sshd_config.d/`{.literal} directory or by applying a custom system-wide cryptographic policy. This enables you to harden or loosen SSH connections depending on your scenario.

To override the system-wide cryptographic policies for your OpenSSH server, specify the cryptographic policy in a drop-in configuration file located in `/etc/ssh/sshd_config.d/`{.literal}. Because the first match wins, name the file with a two-digit number prefix smaller than 50 and with a `.conf`{.literal} suffix, for example, `49-crypto-policy-override.conf`{.literal}. This way, it lexicographically precedes the `50-redhat.conf`{.literal} file and overrides the default configuration.

See the `sshd_config(5)`{.literal} man page for more information.

**Prerequisites**

-   The `openssh-server`{.literal} package is installed.
-   The `sshd`{.literal} daemon is running on the server.

**Procedure**

1.  Create a new configuration file with a name that lexicographically precedes `50-redhat.conf`{.literal}, for example:

    ``` {.language-plaintext tabindex="-1"}
    # touch /etc/ssh/sshd_config.d/49-crypto-policy-override.conf
    ```

2.  Open the file in a text editor, and specify ciphers and message authentication codes (MACs) you want to allow, for example:

    ``` {.language-plaintext tabindex="-1"}
    Ciphers aes256-gcm@openssh.com,aes128-gcm@openssh.com
    MACs hmac-sha2-512,hmac-sha2-256
    ```

3.  Save the changes, and reload the `sshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload sshd
    ```

**Verification**

-   Check ciphers and MACs allowed on your OpenSSH server in the output of the `sshd -T`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # sshd -T | grep -iE '(ciphers|macs)'
    ```

**Next steps**

-   You can also disable specific ciphers for the SSH protocol through system-wide cryptographic policies, specifically by creating and applying a custom subpolicy that uses the scopes concept. See the [Customizing system-wide cryptographic policies with subpolicies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies#customizing-systemwide-cryptographic-policies-with-subpolicies) section and the [How to disable specific cryptographic algorithms when using system-wide cryptographic policies](https://access.redhat.com/articles/7041246) Red Hat Knowledgebase article for more information.

**Additional resources**

-   [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies)
-   [How to disable specific algorithms and ciphers for the `ssh`{.literal} service only (Red Hat Knowledgebase)](https://access.redhat.com/solutions/4410591)

#### [1.5.3. Setting a non-default port for SSH](#setting-a-non-default-port-for-ssh) {#setting-a-non-default-port-for-ssh .title}

By default, the `sshd`{.literal} daemon listens on TCP port 22. Changing the port reduces the exposure of the system to attacks based on automated network scanning on the default port and therefore increases security through obscurity.

Note

Changing the SSH port provides only limited security benefits. An attacker performing a full port scan can discover the service regardless of the port number. Real security improvements come from disabling password authentication, using key-based authentication, and implementing proper access controls.

Important

After changing the SSH port, update client configurations to use the new port. This includes:

-   user SSH configuration files (`~/.ssh/config`{.literal})
-   automation tools and scripts that connect to the server
-   monitoring systems and backup tools
-   load balancers and proxy configurations

Without these updates, connections to the server fail.

**Prerequisites**

-   Commands that start with the `#`{.literal} command prompt require administrative privileges provided by `sudo`{.literal} or root user access. For information on how to configure `sudo`{.literal} access, see [Enabling unprivileged users to run certain commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access#enabling-unprivileged-users-to-run-certain-commands).
-   The `policycoreutils-python-utils`{.literal} package is installed on your system.

**Procedure**

1.  Open the `/etc/ssh/sshd_config`{.literal} configuration file in a text editor of your choice.

2.  Remove the `#`{.literal} character before the `Port`{.literal} directive and specify a port number different from 22, for example:

    ``` {.language-plaintext tabindex="-1"}
    Port <49286>
    ```

3.  Update the default SELinux policy to allow the use of a non-default port:

    ``` {.language-plaintext tabindex="-1"}
    # semanage port -a -t ssh_port_t -p tcp <49286>
    ```

4.  Update the `firewalld`{.literal} configuration:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port <49286>/tcp
    # firewall-cmd --remove-port=22/tcp
    # firewall-cmd --runtime-to-permanent
    ```

5.  Restart the `sshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sshd
    ```

**Verification**

-   Use a tool that displays port numbers of running services, for example:

    ``` {.language-plaintext tabindex="-1"}
    # ss -tulpn | grep sshd
    tcp   LISTEN 0      128             [::]:49286            [::]:*    users:(("sshd",pid=1784,fd=8))
    ```

    Check the output for the new port number.

#### [1.5.4. SSH access only for specific users, groups, or IP ranges](#ssh-access-only-for-specific-users-groups-or-ip-ranges) {#ssh-access-only-for-specific-users-groups-or-ip-ranges .title}

By using the `AllowUsers`{.literal} and `AllowGroups`{.literal} directives in the `/etc/ssh/sshd_config`{.literal} configuration file, you can permit only certain users, domains, or groups to connect to your OpenSSH server.

Warning

Misconfiguring `AllowUsers`{.literal} or `AllowGroups`{.literal} can lock you out of the server. Before applying these directives, verify that your user account and source IP match the restrictions. Test the configuration by opening a new SSH session while keeping your current session active, so you can revert changes if the new connection fails.

You can combine `AllowUsers`{.literal} and `AllowGroups`{.literal} to restrict access more precisely, for example:

``` {.language-plaintext tabindex="-1"}
AllowUsers *@192.168.1.* *@10.0.0.* !*@192.168.1.2
AllowGroups example-group
```

This configuration allows only connections if all of the following conditions are met:

-   The connection's source IP is within the 192.168.1.0/24 or 10.0.0.0/24 subnet.
-   The source IP is not 192.168.1.2.
-   The user is a member of the example-group group.

The OpenSSH server permits only connections that pass all `Allow`{.literal} and `Deny`{.literal} directives in `/etc/ssh/sshd_config`{.literal}. For example, if the `AllowUsers`{.literal} directive lists a user that is not part of a group listed in the `AllowGroups`{.literal} directive, then the user cannot log in.

Using allowlists (directives starting with `Allow`{.literal}) is more secure than using denylists (options starting with `Deny`{.literal}) because allowlists also block new unauthorized users or groups.

#### [1.5.5. X Security extension](#x-security-extension) {#x-security-extension .title}

Disable X11 forwarding in the OpenSSH server configuration if you do not need it to reduce your system's attack surface.

The X server in Red Hat Enterprise Linux clients does not provide the X Security extension. Without this extension, clients cannot request an additional security layer when connecting to untrusted SSH servers with X11 forwarding.

By default, the `ForwardX11Trusted`{.literal} option in the `/etc/ssh/ssh_config.d/50-redhat.conf`{.literal} file is set to `yes`{.literal}. This means the `ssh -X remote_machine`{.literal} and `ssh -Y remote_machine`{.literal} commands behave identically.

To disable X11 forwarding, set the `X11Forwarding`{.literal} directive to `no`{.literal} in the `/etc/ssh/sshd_config`{.literal} configuration file.

#### [1.5.6. Additional resources](#making-openssh-more-secure_156-additional-resources) {#additional-resources .title}

-   [Setting key-based authentication as the only method on an OpenSSH server](#setting-key-based-authentication-as-the-only-method-on-an-openssh-server "1.3. Setting key-based authentication as the only method on an OpenSSH server")
-   [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies)
-   [How to disable specific algorithms and ciphers for the `ssh`{.literal} service only (Red Hat Knowledgebase)](https://access.redhat.com/solutions/4410591)

### [1.6. Connecting to a remote server through an SSH jump host](#connecting-to-a-remote-server-through-an-ssh-jump-host) {#connecting-to-a-remote-server-through-an-ssh-jump-host .title}

Connect securely from your local system to a remote server by using a jump host as an intermediary. This approach manages connections between hosts located in different security zones.

**Prerequisites**

-   A jump host accepts SSH connections from your local system.
-   A remote server accepts SSH connections from the jump host.

**Procedure**

1.  Use the `ssh -J`{.literal} command to connect through one or more intermediary jump servers. Specify the jump servers directly in the command, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -J <jump-1.example.com>,<jump-2.example.com>,<jump-3.example.com> <target-server-1.example.com>
    ```

    Change the hostname-only notation if needed. Use this format when user names or SSH ports differ between the jump servers and the remote server, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -J <example.user.1>@<jump-1.example.com>:<75>,<example.user.2>@<jump-2.example.com>:<75>,<example.user.3>@<jump-3.example.com>:<75> <example.user.f>@<target-server-1.example.com>:<220>
    ```

2.  For regular connections through jump servers, store the configuration in your SSH configuration file:

    a.  Define the jump host by editing the `~/.ssh/config`{.literal} file on your local system, for example:

        ``` {.language-plaintext tabindex="-1"}
        Host <jump-server-1>
          HostName <jump-1.example.com>
        ```

        -   The `Host`{.literal} parameter defines a name or alias for the host you can use in `ssh`{.literal} commands. The value can match the real hostname, but can also be any string.
        -   The `HostName`{.literal} parameter sets the actual hostname or IP address of the jump host.

    b.  Add the remote server jump configuration with the `ProxyJump`{.literal} directive to `~/.ssh/config`{.literal} file on your local system, for example:

        ``` {.language-plaintext tabindex="-1"}
        Host <remote-server-1>
          HostName <target-server-1.example.com>
          ProxyJump <jump-server-1>
        ```

    c.  Use your local system to connect to the remote server through the jump server:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh <remote-server-1>
        ```

        This command is equivalent to the `ssh -J jump-server1 remote-server`{.literal} command if you omit the previous configuration steps.

### [1.7. Configuring the OpenSSH server and client by using RHEL system roles](#configuring-the-openssh-server-and-client-by-using-rhel-system-roles) {#configuring-the-openssh-server-and-client-by-using-rhel-system-roles .title}

You can use the `sshd`{.literal} RHEL system role to configure OpenSSH servers and the `ssh`{.literal} RHEL system role to configure OpenSSH clients consistently, in an automated fashion, and on any number of RHEL systems at the same time.

Such configurations are necessary for any system where secure remote interaction is needed, for example:

-   Remote system administration: securely connecting to your machine from another computer by using an SSH client.
-   Secure file transfers: the Secure File Transfer Protocol (SFTP) provided by OpenSSH securely transfers files between your local machine and a remote system.
-   Automated DevOps pipelines: automating software deployments that require secure connection to remote servers (CI/CD pipelines).
-   Tunneling and port forwarding: forwarding a local port to access a web service on a remote server behind a firewall. For example a remote database or a development server.
-   Key-based authentication: more secure alternative to password-based logins.
-   Certificate-based authentication: centralized trust management and better scalability.
-   Enhanced security: disabling root logins, restricting user access, enforcing strong encryption and other such forms of hardening ensures stronger system security.

#### [1.7.1. How the sshd RHEL system role maps settings from a playbook to the configuration file](#how-the-sshd-rhel-system-role-maps-settings-from-a-playbook-to-the-configuration-file) {#how-the-sshd-rhel-system-role-maps-settings-from-a-playbook-to-the-configuration-file .title}

In the `sshd`{.literal} RHEL system role playbook, you can define the parameters for the server SSH configuration file. If you do not specify these settings, the role produces the `sshd_config`{.literal} file that matches the RHEL defaults.

In all cases, booleans correctly render as `yes`{.literal} and `no`{.literal} in the final configuration on your managed nodes. You can use lists to define multi-line configuration items. For example:

``` {.language-yaml tabindex="-1"}
sshd_ListenAddress:
  - 0.0.0.0
  - '::'
```

renders as:

``` {.language-plaintext tabindex="-1"}
ListenAddress 0.0.0.0
ListenAddress ::
```

#### [1.7.2. Configuring OpenSSH servers by using the sshd RHEL system role](#configuring-openssh-servers-by-using-the-sshd-rhel-system-role) {#configuring-openssh-servers-by-using-the-sshd-rhel-system-role .title}

You can use the `sshd`{.literal} RHEL system role to configure multiple OpenSSH servers for secure remote access.

The role ensures secure communication environment for remote users by providing namely:

-   Management of incoming SSH connections from remote clients
-   Credentials verification
-   Secure data transfer and command execution

Note

You can use the `sshd`{.literal} RHEL system role alongside with other RHEL system roles that change SSHD configuration, for example the Identity Management in RHEL system roles. To prevent the configuration from being overwritten, ensure the `sshd`{.literal} RHEL system role uses namespaces (RHEL 8 and earlier versions) or a drop-in directory (RHEL 9 and later).

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: SSH server configuration
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure sshd to prevent root and password login except from particular subnet
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.sshd
          vars:
            sshd_config:
              PermitRootLogin: no
              PasswordAuthentication: no
              Match:
                - Condition: "Address 192.0.2.0/24"
                  PermitRootLogin: yes
                  PasswordAuthentication: yes
    ```

    The settings specified in the example playbook include the following:

    `PasswordAuthentication: yes|no`{.literal}
    :   Controls whether the OpenSSH server (`sshd`{.literal}) accepts authentication from clients that use the username and password combination.

    `Match:`{.literal}
    :   The match block allows the `root`{.literal} user to log in by using a password only from the subnet `192.0.2.0/24`{.literal}.

    For details about the role variables and the OpenSSH configuration options used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.sshd/README.md`{.literal} file and the `sshd_config(5)`{.literal} manual page on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

1.  Log in to the SSH server:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh <username>@<ssh_server>
    ```

2.  Verify the contents of the `sshd_config`{.literal} file on the SSH server:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /etc/ssh/sshd_config.d/00-ansible_system_role.conf
    #
    # Ansible managed
    #
    PasswordAuthentication no
    PermitRootLogin no
    Match Address 192.0.2.0/24
      PasswordAuthentication yes
      PermitRootLogin yes
    ```

3.  Check that you can connect to the server as root from the `192.0.2.0/24`{.literal} subnet:

    a.  Determine your IP address:

        ``` {.language-plaintext tabindex="-1"}
        $ hostname -I
        192.0.2.1
        ```

        If the IP address is within the `192.0.2.1`{.literal} - `192.0.2.254`{.literal} range, you can connect to the server.

    b.  Connect to the server as `root`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh root@<ssh_server>
        ```

**Troubleshooting**

-   If the playbook fails with syntax errors, validate the YAML structure:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

-   If the managed node is unreachable, verify SSH connectivity and authentication:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m ping
    ```

-   If the playbook completes but the SSH configuration is not applied, check the `sshd`{.literal} service status on the managed node:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m shell -a 'systemctl status sshd'
    ```

-   If configuration validation fails, check the sshd configuration test:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m shell -a 'sshd -t'
    ```

-   For detailed output during playbook execution, run with verbose mode:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook -vvv ~/playbook.yml
    ```

#### [1.7.3. Using the sshd RHEL system role for non-exclusive configuration](#using-the-sshd-rhel-system-role-for-non-exclusive-configuration) {#using-the-sshd-rhel-system-role-for-non-exclusive-configuration .title}

By default, applying the `sshd`{.literal} RHEL system role overwrites the entire configuration. This can be problematic if you have previously adjusted the configuration with a different playbook. You can use the non-exclusive configuration to apply changes only to selected configuration options.

You can apply a non-exclusive configuration:

-   In RHEL 8 and earlier by using a configuration snippet.
-   In RHEL 9 and later by using files in a drop-in directory. The default configuration file is already placed in the drop-in directory as `/etc/ssh/sshd_config.d/00-ansible_system_role.conf`{.literal}.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    -   For managed nodes that run RHEL 8 or earlier:

        ``` {.language-yaml tabindex="-1"}
        ---
        - name: Non-exclusive sshd configuration
          hosts: managed-node-01.example.com
          tasks:
            - name: Configure SSHD to accept environment variables
              ansible.builtin.include_role:
                name: redhat.rhel_system_roles.sshd
              vars:
                sshd_config_namespace: <my_application>
                sshd_config:
                  # Environment variables to accept
                  AcceptEnv:
                    LANG
                    LS_COLORS
                    EDITOR
        ```

    -   For managed nodes that run RHEL 9 or later:

        ``` {.language-yaml tabindex="-1"}
        - name: Non-exclusive sshd configuration
          hosts: managed-node-01.example.com
          tasks:
            - name: Configure sshd to accept environment variables
              ansible.builtin.include_role:
                name: redhat.rhel_system_roles.sshd
              vars:
                sshd_config_file: /etc/ssh/sshd_config.d/<42-my_application>.conf
                sshd_config:
                  # Environment variables to accept
                  AcceptEnv:
                    LANG
                    LS_COLORS
                    EDITOR
        ```

        The settings specified in the example playbooks include the following:

        `sshd_config_namespace: `{.literal}*`<my_application>`{.literal}*
        :   The role places the configuration that you specify in the playbook to configuration snippets in the existing configuration file under the given namespace. You need to select a different namespace when running the role from a different context.

        `sshd_config_file: /etc/ssh/sshd_config.d/`{.literal}*`<42-my_application>`{.literal}*`.conf`{.literal}
        :   In the `sshd_config_file`{.literal} variable, define the `.conf`{.literal} file into which the `sshd`{.literal} system role writes the configuration options. Use a two-digit prefix, for example *`42-`{.literal}* to specify the order in which the configuration files are applied.

        `AcceptEnv:`{.literal}

        :   Controls which environment variables the OpenSSH server (`sshd`{.literal}) accepts from a client:

            -   `LANG`{.literal}: defines the language and locale settings.
            -   `LS_COLORS`{.literal}: defines the displaying color scheme for the `ls`{.literal} command on the command line.
            -   `EDITOR`{.literal}: specifies the default text editor for the command-line programs that need to open an editor.

        For details about the role variables and the OpenSSH configuration options used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.sshd/README.md`{.literal} file and the `sshd_config(5)`{.literal} manual page on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Verify the configuration on the SSH server:

    -   For managed nodes that run RHEL 8 or earlier:

        ``` {.language-plaintext tabindex="-1"}
        # cat /etc/ssh/sshd_config
        ...
        # BEGIN sshd system role managed block: namespace <my_application>
        Match all
          AcceptEnv LANG LS_COLORS EDITOR
        # END sshd system role managed block: namespace <my_application>
        ```

    -   For managed nodes that run RHEL 9 or later:

        ``` {.language-plaintext tabindex="-1"}
        # cat /etc/ssh/sshd_config.d/42-my_application.conf
        # Ansible managed
        #
        AcceptEnv LANG LS_COLORS EDITOR
        ```

#### [1.7.4. Overriding the system-wide cryptographic policy on an SSH server by using the sshd RHEL system role](#overriding-the-system-wide-cryptographic-policy-on-an-ssh-server-by-using-the-sshd-rhel-system-role) {#overriding-the-system-wide-cryptographic-policy-on-an-ssh-server-by-using-the-sshd-rhel-system-role .title}

When the default cryptographic settings do not meet certain security or compatibility needs, you can override the system-wide cryptographic policy on the OpenSSH server by using the `sshd`{.literal} RHEL system role.

Override the system-wide cryptographic policy in the following notable situations:

-   Compatibility with older clients: necessity to use weaker-than-default encryption algorithms, key exchange protocols, or ciphers.
-   Enforcing stronger security policies: simultaneously, you can disable weaker algorithms. Such a measure could exceed the default system cryptographic policies, especially in the highly secure and regulated environments.
-   Performance considerations: the system defaults could enforce stronger algorithms that can be computationally intensive for some systems.
-   Customizing for specific security needs: adapting for unique requirements that are not covered by the default cryptographic policies.

Warning

It is not possible to override all aspects of the cryptographic policies from the `sshd`{.literal} RHEL system role. For example, SHA-1 signatures might be forbidden on a different layer so for a more generic solution, see [Setting a custom cryptographic policy by using RHEL system roles](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/setting-a-custom-cryptographic-policy-by-using-rhel-system-roles).

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    - name: Deploy SSH configuration for OpenSSH server
      hosts: managed-node-01.example.com
      tasks:
        - name: Overriding the system-wide cryptographic policy
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.sshd
          vars:
            sshd_sysconfig: true
            sshd_sysconfig_override_crypto_policy: true
            sshd_KexAlgorithms: ecdh-sha2-nistp521
            sshd_Ciphers: aes256-ctr
            sshd_MACs: hmac-sha2-512-etm@openssh.com
            sshd_HostKeyAlgorithms: rsa-sha2-512,rsa-sha2-256
    ```

    The settings specified in the example playbook include the following:

    `sshd_KexAlgorithms`{.literal}
    :   You can choose key exchange algorithms, for example, `ecdh-sha2-nistp256`{.literal}, `ecdh-sha2-nistp384`{.literal}, `ecdh-sha2-nistp521`{.literal},`diffie-hellman-group14-sha1`{.literal}, or `diffie-hellman-group-exchange-sha256`{.literal}.

    `sshd_Ciphers`{.literal}
    :   You can choose ciphers, for example, `aes128-ctr`{.literal}, `aes192-ctr`{.literal}, or `aes256-ctr`{.literal}.

    `sshd_MACs`{.literal}
    :   You can choose MACs, for example, `hmac-sha2-256`{.literal}, `hmac-sha2-512`{.literal}, or `hmac-sha1`{.literal}.

    `sshd_HostKeyAlgorithms`{.literal}
    :   You can choose a public key algorithm, for example, `ecdsa-sha2-nistp256`{.literal}, `ecdsa-sha2-nistp384`{.literal}, `ecdsa-sha2-nistp521`{.literal}, or `ssh-rsa`{.literal}.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.sshd/README.md`{.literal} file on the control node.

    Note

    On RHEL 9 managed nodes, the system role writes the configuration into the `/etc/ssh/sshd_config.d/00-ansible_system_role.conf`{.literal} file, where cryptographic options are applied automatically. You can change the file by using the `sshd_config_file`{.literal} variable. However, to ensure the configuration is effective, use a file name that lexicographically precedes the `/etc/ssh/sshd_config.d/50-redhat.conf`{.literal} file, which includes the configured crypto policies.

    On RHEL 8 managed nodes, you must enable override by setting the `sshd_sysconfig_override_crypto_policy`{.literal} and `sshd_sysconfig`{.literal} variables to `true`{.literal}.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   You can verify the success of the procedure by using the verbose SSH connection and check the defined variables in the following output:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -vvv <ssh_server>
    ...
    debug2: peer server KEXINIT proposal
    debug2: KEX algorithms: ecdh-sha2-nistp521
    debug2: host key algorithms: rsa-sha2-512,rsa-sha2-256
    debug2: ciphers ctos: aes256-ctr
    debug2: ciphers stoc: aes256-ctr
    debug2: MACs ctos: hmac-sha2-512-etm@openssh.com
    debug2: MACs stoc: hmac-sha2-512-etm@openssh.com
    ...
    ```

#### [1.7.5. How the ssh RHEL system role maps settings from a playbook to the configuration file](#how-the-ssh-rhel-system-role-maps-settings-from-a-playbook-to-the-configuration-file) {#how-the-ssh-rhel-system-role-maps-settings-from-a-playbook-to-the-configuration-file .title}

In the `ssh`{.literal} RHEL system role playbook, you can define the parameters for the client SSH configuration file. If you do not specify these settings, the role produces a global `ssh_config`{.literal} file that matches the RHEL defaults.

In all the cases, booleans correctly render as `yes`{.literal} or `no`{.literal} in the final configuration on your managed nodes. You can use lists to define multi-line configuration items. For example:

``` {.language-yaml tabindex="-1"}
LocalForward:
  - 22 localhost:2222
  - 403 localhost:4003
```

renders as:

``` {.language-plaintext tabindex="-1"}
LocalForward 22 localhost:2222
LocalForward 403 localhost:4003
```

Note

The configuration options are case sensitive.

#### [1.7.6. Configuring OpenSSH clients by using the ssh RHEL system role](#configuring-openssh-clients-by-using-the-ssh-rhel-system-role) {#configuring-openssh-clients-by-using-the-ssh-rhel-system-role .title}

You can use the `ssh`{.literal} RHEL system role to configure multiple OpenSSH clients.

OpenSSH clients establish a secure connection between the local user and the remote OpenSSH server. They ensure:

-   Secure connection initiation
-   Credentials provision
-   Negotiation with the OpenSSH server on the encryption method used for the secure communication channel
-   Ability to send files securely to and from the OpenSSH server

Note

You can use the `ssh`{.literal} RHEL system role alongside with other system roles that change SSH configuration, for example the Identity Management in RHEL system roles. To prevent the configuration from being overwritten, make sure that the `ssh`{.literal} RHEL system role uses a drop-in directory (default in RHEL 8 and later).

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: SSH client configuration
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure ssh clients
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.ssh
          vars:
            ssh_user: root
            ssh:
              Compression: true
              GSSAPIAuthentication: no
              ControlMaster: auto
              ControlPath: ~/.ssh/.cm%C
              Host:
                - Condition: example
                  Hostname: server.example.com
                  User: user1
            ssh_ForwardX11: no
    ```

    The settings specified in the example playbook include the following:

    `ssh_user: root`{.literal}
    :   Configures the `root`{.literal} user's SSH client preferences on the managed nodes with certain configuration specifics.

    `Compression: true`{.literal}
    :   Compression is enabled.

    `ControlMaster: auto`{.literal}
    :   ControlMaster multiplexing is set to `auto`{.literal}.

    `Host`{.literal}
    :   Creates alias `example`{.literal} for connecting to the `server.example.com`{.literal} host as a user called `user1`{.literal}.

    `ssh_ForwardX11: no`{.literal}
    :   X11 forwarding is disabled.

    For details about the role variables and the OpenSSH configuration options used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.ssh/README.md`{.literal} file and the `ssh_config(5)`{.literal} manual page on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Verify that the managed node has the correct configuration by displaying the SSH configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # cat ~/root/.ssh/config
    # Ansible managed
    Compression yes
    ControlMaster auto
    ControlPath ~/.ssh/.cm%C
    ForwardX11 no
    GSSAPIAuthentication no
    Host example
      Hostname example.com
      User user1
    ```

**Troubleshooting**

-   If the playbook fails with syntax errors, validate the YAML structure:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

-   If the managed node is unreachable, verify SSH connectivity and authentication:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m ping
    ```

-   If the SSH client configuration is not applied, verify that the configuration file was created in the correct location for the specified user.

-   For detailed output during playbook execution, run with verbose mode:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook -vvv ~/playbook.yml
    ```

### [1.8. Additional resources](#using-secure-communications-between-two-systems-with-openssh_18-additional-resources) {#additional-resources-1 .title}

-   [Configuring SELinux for applications and services with non-standard configurations](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/configuring-selinux-for-applications-and-services-with-non-standard-configurations)
-   [Controlling network traffic using firewalld](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/risk_reduction_and_recovery_operations/configuring-a-remote-logging-solution)

## [Chapter 2. Creating and managing TLS keys and certificates](#creating-and-managing-tls-keys-and-certificates) {#chapter-2.-creating-and-managing-tls-keys-and-certificates .title}

Create and manage TLS private keys and certificates by using toolkits such as OpenSSL and GnuTLS. Properly configuring these assets is critical for secure communication.

### [2.1. TLS certificates](#tls-certificates) {#tls-certificates .title}

TLS (Transport Layer Security) is a protocol that establishes encrypted data exchange between client/server applications. TLS uses a system of public and private key pairs to encrypt communication between clients and servers. TLS is the successor protocol to SSL (Secure Sockets Layer).

TLS uses X.509 certificates to bind identities, such as hostnames or organizations, to public keys using digital signatures. X.509 is a standard that defines the format of public key certificates.

Authentication of a secure application depends on the integrity of the public key value in the application's certificate. If an attacker replaces the public key with its own public key, it can impersonate the application and gain access to secure data. To prevent this type of attack, all certificates must be signed by a certification authority (CA).

A CA is a trusted node that confirms the integrity of the public key value in a certificate.

A CA signs a public key by adding its digital signature and issues a certificate. A digital signature is a message encoded with the CA's private key.

The CA's public key is made available to applications by distributing the certificate of the CA. Applications verify that certificates are validly signed by decoding the CA's digital signature with the CA's public key.

To have a certificate signed by a CA, you must generate a public key, and send it to a CA for signing. This is called a certificate signing request (CSR). A CSR also contains a distinguished name (DN) for the certificate.

The DN information can include a two-letter country code, state or province, city or town, organization name, email address, or be empty. Many current commercial CAs prefer the Subject Alternative Name extension and ignore DNs in CSRs.

RHEL contains two main toolkits for working with TLS certificates: GnuTLS and OpenSSL. You can create, read, sign, and verify certificates by using the `openssl`{.literal} utility from the `openssl`{.literal} package. The `certtool`{.literal} utility, included in the `gnutls-utils`{.literal} package, performs the same operations with a different syntax and a distinct set of back-end libraries.

See the `openssl(1)`{.literal}, `x509(1)`{.literal}, `ca(1)`{.literal}, `req(1)`{.literal}, and `certtool(1)`{.literal} man pages on your system for more information.

**Additional resources**

-   [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://datatracker.ietf.org/doc/html/rfc5280)

### [2.2. Post-quantum cryptography algorithms in OpenSSL](#post-quantum-cryptography-algorithms-in-openssl) {#post-quantum-cryptography-algorithms-in-openssl .title}

You can use the OpenSSL TLS toolkit to generate keys and certificates with post-quantum algorithms. This helps enhance security against emerging threats while maintaining compatibility with traditional algorithms.

Starting with RHEL 10.1, you can use OpenSSL for generating keys, signing messages, verifying signatures, and creating X.509 certificates with the ML-DSA post-quantum algorithms.

From OpenSSL 3.5, the hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism) method is preferred in TLS 1.3 handshakes. OpenSSL includes keys with both traditional algorithms and ML-KEM.

The use of ML-KEM causes a slight delay during TLS connection initiation. However, it does not affect performance after the handshake completes, as further communication uses a more efficient symmetric key.

**Example 2.1. Usage of ML-DSA for keys in OpenSSL**

`$ `{.literal}**`openssl genpkey -algorithm mldsa65 -out `{.literal}*`<mldsa-privatekey.pem>`{.literal}*** 
:   Create a private key with the ML-DSA-65 algorithm.

`$ `{.literal}**`openssl pkey -in `{.literal}*`<mldsa-privatekey.pem>`{.literal}*` -pubout -out `{.literal}*`<mldsa-publickey.pem>`{.literal}*** 
:   Create a public key based on the ML-DSA-65-encrypted private key.

`$ `{.literal}**`openssl dgst -sign `{.literal}*`<mldsa-privatekey.pem>`{.literal}*` -out `{.literal}*`<signature_message>`{.literal}*** 
:   Sign a message with the private key.

`$ `{.literal}**`openssl dgst -verify `{.literal}*`<mldsa-publickey.pem>`{.literal}*` -signature `{.literal}*`<signature_message>`{.literal}*** 
:   Verify the ML-DSA-65 signature with the public key.

**Example 2.2. Usage of ML-DSA for certificates in OpenSSL**

Because no public certificate authorities (CA) currently support post-quantum signatures, you can use only a local CA or self-signed certificates with ML-DSA signatures. For example:

``` {.language-plaintext tabindex="-1"}
$ openssl req \
    -x509 \
    -newkey mldsa65 \
    -keyout <localhost-mldsa.key> \
    -subj /CN=<localhost> \
    -addext subjectAltName=DNS:<localhost> \
    -days <30> \
    -nodes \
    -out <localhost-mldsa.crt>
```

**Example 2.3. Establishing a connection with PQC key exchange and PQC certificates**

An OpenSSL server and client can establish a post-quantum connection and a connection that uses only traditional algorithms.

``` {.language-plaintext tabindex="-1"}
$ openssl s_server \
    -cert <localhost-mldsa.crt> -key <localhost-mldsa.key> \
    -dcert <localhost-rsa.crt> -dkey <localhost-rsa.key> >/dev/null &

$ openssl s_client \
    -connect <localhost:4433> \
    -CAfile <localhost-mldsa.crt> </dev/null \
    |& grep -E '(Peer signature type|Negotiated TLS1.3 group)'
Peer signature type: mldsa65
Negotiated TLS1.3 group: X25519MLKEM768
```

**Example 2.4. Establishing a connection that uses only non-post-quantum cryptographic algorithms**

``` {.language-plaintext tabindex="-1"}
$ openssl s_client \
    -connect <localhost:4433> \
    -CAfile <localhost-rsa.crt> \
    -sigalgs 'rsa_pss_pss_sha256:rsa_pss_rsae_sha256' \
    -groups 'X25519:secp256r1:X448:secp521r1:secp384r1' </dev/null \
    |& grep -E '(Peer signature type|Server Temp Key)'
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
```

You can configure a server to simultaneously use traditional certificates (RSA, ECDSA, and EdDSA) and post-quantum certificates. The server automatically and transparently selects the certificates preferred and supported by clients. It uses post-quantum for new clients and traditional for legacy ones.

See the `openssl(1)`{.literal}, `openssl-genpkey(1)`{.literal}, `openssl-pkey(1)`{.literal}, `openssl-dgst(1)`{.literal}, and `openssl-verify(1)`{.literal} man pages on your system for more information.

**Additional resources**

-   [System-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies#system-wide-cryptographic-policies)
-   [Post-quantum cryptography in Red Hat Enterprise Linux 10 (Red Hat Blog)](https://www.redhat.com/en/blog/post-quantum-cryptography-red-hat-enterprise-linux-10)
-   [Interoperability of RHEL 10 post-quantum cryptography (Red Hat Knowledgebase)](https://access.redhat.com/articles/7119430)
-   [Red Hat's path to post-quantum cryptography (Red Hat Blog)](https://www.redhat.com/en/blog/red-hats-path-post-quantum-cryptography)
-   [How Red Hat is integrating post-quantum cryptography into our products (Red Hat Blog)](https://www.redhat.com/en/blog/how-red-hat-integrating-post-quantum-cryptography-our-products)

### [2.3. Creating a private CA by using OpenSSL](#creating-a-private-ca-using-openssl) {#creating-a-private-ca-by-using-openssl .title}

Private certificate authorities (CA) are useful when your scenario requires verifying entities within your internal network.

For example, use a private CA when you create a VPN gateway with authentication based on certificates signed by a CA under your control. You can also use a private CA when you do not want to pay a commercial CA. To sign certificates in such use cases, the private CA uses a self-signed certificate.

**Prerequisites**

-   You have `root`{.literal} privileges or permissions to enter administrative commands with `sudo`{.literal}. Commands that require such privileges are marked with `#`{.literal}.

**Procedure**

1.  Generate a private key for your CA. For example, the following command creates a 256-bit Elliptic Curve Digital Signature Algorithm (ECDSA) key:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl genpkey -algorithm ec -pkeyopt ec_paramgen_curve:P-256 -out <ca.key>
    ```

    The time for the key-generation process depends on the hardware and entropy of the host, the selected algorithm, and the length of the key.

2.  Create a certificate signed with the private key from the previous step:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl req -key <ca.key> -new -x509 -days 3650 -addext keyUsage=critical,keyCertSign,cRLSign -subj "/CN=<example_CA>" -out <ca.crt>
    ```

    The generated `ca.crt`{.literal} file is a self-signed CA certificate that you can use to sign other certificates for ten years. For a private CA, you can replace *`<example_CA>`{.literal}* with any string as the common name (CN).

3.  Set secure permissions on the private key of your CA, for example:

    ``` {.language-plaintext tabindex="-1"}
    # chown <root>:<root> <ca.key>
    # chmod 600 <ca.key>
    ```

**Next steps**

-   To use a self-signed CA certificate as a trust anchor on client systems, copy the CA certificate to the client and add it to the clients\' system-wide truststore as `root`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # trust anchor <ca.crt>
    ```

    See the [Using shared system certificates](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/using-shared-system-certificates) chapter for more information.

**Verification**

1.  Create a certificate signing request (CSR), and use your CA to sign the request. The CA must successfully create a certificate based on the CSR, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl x509 -req -in <client-cert.csr> -CA <ca.crt> -CAkey <ca.key> -CAcreateserial -days 365 -extfile <openssl.cnf> -extensions <client-cert> -out <client-cert.crt>
    Signature ok
    subject=C = US, O = Example Organization, CN = server.example.com
    Getting CA Private Key
    ```

    See [Section 2.6, "Using a private CA to issue certificates for CSRs with OpenSSL"](#using-a-private-ca-to-issue-certificates-for-csrs-with-openssl "2.6. Using a private CA to issue certificates for CSRs with OpenSSL") and the `ca(1)`{.literal}, `genpkey(1)`{.literal}, and `req(1)`{.literal} man pages on your system for more information.

2.  Display the basic information about your self-signed CA:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl x509 -in <ca.crt> -text -noout
    Certificate:
    …
            X509v3 extensions:
                …
                X509v3 Basic Constraints: critical
                    CA:TRUE
                X509v3 Key Usage: critical
                    Certificate Sign, CRL Sign
    …
    ```

3.  Verify the consistency of the private key:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl pkey -check -in <ca.key>
    Key is valid
    -----BEGIN PRIVATE KEY-----
    MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgcagSaTEBn74xZAwO
    18wRpXoCVC9vcPki7WlT+gnmCI+hRANCAARb9NxIvkaVjFhOoZbGp/HtIQxbM78E
    lwbDP0BI624xBJ8gK68ogSaq2x4SdezFdV1gNeKScDcU+Pj2pELldmdF
    -----END PRIVATE KEY-----
    ```

### [2.4. Creating a private key and a CSR for a TLS server certificate by using OpenSSL](#creating-a-private-key-and-a-csr-for-a-tls-server-certificate-using-openssl) {#creating-a-private-key-and-a-csr-for-a-tls-server-certificate-by-using-openssl .title}

You can use TLS-encrypted communication channels only if you have a valid TLS certificate from a certificate authority (CA). To get the certificate, create a private key and a certificate signing request (CSR) for your server first.

**Procedure**

1.  Generate a private key on your server system, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl genpkey -algorithm ec -pkeyopt ec_paramgen_curve:P-256 -out <server_private.key>
    ```

2.  Optional: Use a text editor to prepare a configuration file that simplifies creating your CSR, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ vi <example_server.cnf>
    [server-cert]
    keyUsage = critical, digitalSignature, keyEncipherment, keyAgreement
    extendedKeyUsage = serverAuth
    subjectAltName = @alt_name

    [req]
    distinguished_name = dn
    prompt = no

    [dn]
    C = <US>
    O = <Example Organization>
    CN = <server.example.com>

    [alt_name]
    DNS.1 = <example.com>
    DNS.2 = <server.example.com>
    IP.1 = <192.168.0.1>
    IP.2 = <::1>
    IP.3 = <127.0.0.1>
    ```

    The `extendedKeyUsage = serverAuth`{.literal} option limits the use of a certificate.

3.  Create a CSR using the private key you created previously:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl req -key <server_private.key> -config <example_server.cnf> -new -out <server_cert.csr>
    ```

    If you omit the `-config`{.literal} option, the `req`{.literal} utility prompts you for additional information, for example:

    ``` {.language-plaintext tabindex="-1"}
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [XX]: <US>
    State or Province Name (full name) []: <Washington>
    Locality Name (eg, city) [Default City]: <Seattle>
    Organization Name (eg, company) [Default Company Ltd]: <Example Organization>
    Organizational Unit Name (eg, section) []:
    Common Name (eg, your name or your server's hostname) []: <server.example.com>
    Email Address []: <server@example.com>
    ```

**Next steps**

-   Submit the CSR to a CA of your choice for signing. Alternatively, for an internal use scenario within a trusted network, use your private CA for signing. See [Using a private CA to issue certificates for CSRs with OpenSSL](#using-a-private-ca-to-issue-certificates-for-csrs-with-openssl "2.6. Using a private CA to issue certificates for CSRs with OpenSSL") for more information.

**Verification**

1.  After you get the requested certificate from the CA, check that the human-readable parts of the certificate match your requirements, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl x509 -text -noout -in <server_cert.crt>
    Certificate:
    …
            Issuer: CN = Example CA
            Validity
                Not Before: Feb  2 20:27:29 2023 GMT
                Not After : Feb  2 20:27:29 2024 GMT
            Subject: C = US, O = Example Organization, CN = server.example.com
            Subject Public Key Info:
                Public Key Algorithm: id-ecPublicKey
                    Public-Key: (256 bit)
    …
            X509v3 extensions:
                X509v3 Key Usage: critical
                    Digital Signature, Key Encipherment, Key Agreement
                X509v3 Extended Key Usage:
                    TLS Web Server Authentication
                X509v3 Subject Alternative Name:
                    DNS:example.com, DNS:server.example.com, IP Address:192.168.0.1, IP
    …
    ```

### [2.5. Creating a private key and a CSR for a TLS client certificate by using OpenSSL](#creating-a-private-key-and-a-csr-for-a-tls-client-certificate-using-openssl) {#creating-a-private-key-and-a-csr-for-a-tls-client-certificate-by-using-openssl .title}

You can use TLS-encrypted communication channels only if you have a valid TLS certificate from a certificate authority (CA). To get the certificate, create a private key and a certificate signing request (CSR) for your client first.

**Procedure**

1.  Generate a private key on your client system, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl genpkey -algorithm ec -pkeyopt ec_paramgen_curve:P-256 -out <client-private.key>
    ```

2.  Optional: Use a text editor to prepare a configuration file that simplifies creating your CSR, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ vi <example_client.cnf>
    [client-cert]
    keyUsage = critical, digitalSignature, keyEncipherment
    extendedKeyUsage = clientAuth
    subjectAltName = @alt_name

    [req]
    distinguished_name = dn
    prompt = no

    [dn]
    CN = <client.example.com>

    [clnt_alt_name]
    email= <client@example.com>
    ```

    The `extendedKeyUsage = clientAuth`{.literal} option limits the use of a certificate.

3.  Create a CSR using the private key you created previously:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl req -key <client-private.key> -config <example_client.cnf> -new -out <client-cert.csr>
    ```

    If you omit the `-config`{.literal} option, the `req`{.literal} utility prompts you for additional information, for example:

    ``` {.language-plaintext tabindex="-1"}
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    …
    Common Name (eg, your name or your server's hostname) []: <client.example.com>
    Email Address []: <client@example.com>
    ```

**Next steps**

-   Submit the CSR to a CA of your choice for signing. Alternatively, for an internal use scenario within a trusted network, use your private CA for signing. See the [Using a private CA to issue certificates for CSRs with OpenSSL](#using-a-private-ca-to-issue-certificates-for-csrs-with-openssl "2.6. Using a private CA to issue certificates for CSRs with OpenSSL") section for more information.

**Verification**

1.  Check that the human-readable parts of the certificate match your requirements, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl x509 -text -noout -in <client-cert.crt>
    Certificate:
    …
                X509v3 Extended Key Usage:
                    TLS Web Client Authentication
                X509v3 Subject Alternative Name:
                    email:client@example.com
    …
    ```

### [2.6. Using a private CA to issue certificates for CSRs with OpenSSL](#using-a-private-ca-to-issue-certificates-for-csrs-with-openssl) {#using-a-private-ca-to-issue-certificates-for-csrs-with-openssl .title}

To establish a TLS-encrypted data exchange channel, systems must get valid certificates from a certificate authority (CA). If you have a private CA, you can create the requested certificates by signing certificate signing requests (CSRs).

**Prerequisites**

-   You have already configured a private CA. See the [Creating a private CA by using OpenSSL](#creating-a-private-ca-using-openssl "2.3. Creating a private CA by using OpenSSL") section for more information.
-   You have a file containing a CSR. You can find an example of creating the CSR in the [Section 2.4, "Creating a private key and a CSR for a TLS server certificate by using OpenSSL"](#creating-a-private-key-and-a-csr-for-a-tls-server-certificate-using-openssl "2.4. Creating a private key and a CSR for a TLS server certificate by using OpenSSL") section.

**Procedure**

1.  Optional: Use a text editor to prepare an OpenSSL configuration file for adding extensions to certificates, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ vim <openssl.cnf>
    [server-cert]
    extendedKeyUsage = serverAuth

    [client-cert]
    extendedKeyUsage = clientAuth
    ```

    The previous example illustrates only the principle. The `openssl`{.literal} utility does not add all extensions to the certificate automatically. You must add the extensions you require either to the CNF file or append them to parameters of the `openssl`{.literal} command.

2.  Use the `x509`{.literal} utility to create a certificate based on a CSR, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl x509 -req -in <server_cert.csr> -CA <ca.crt> -CAkey <ca.key> -days 365 -extfile <openssl.cnf> -extensions <server_cert> -out <server_cert.crt>
    Signature ok
    subject=C = US, O = Example Organization, CN = server.example.com
    Getting CA Private Key
    ```

    To increase security, delete the serial-number file before you create another certificate from a CSR. This way, you ensure that the serial number is always random. If you omit the `CAserial`{.literal} option for specifying a custom file name, the serial-number file name is the same as the file name of the certificate, but its extension is replaced with the `.srl`{.literal} extension (`server-cert.srl`{.literal} in the previous example).

**Verification**

1.  Verify the certificate contents and fields:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl x509 -in <server_cert.crt> -text -noout
    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number: ...
            Issuer: C = US, O = Example CA, CN = Example CA
            Validity
                Not Before: May 21 10:30:00 2026 GMT
                Not After : May 21 10:30:00 2027 GMT
            Subject: C = US, O = Example Organization, CN = server.example.com
            ...
    ```

2.  Verify that the certificate is signed by the correct CA:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl verify -CAfile <ca.crt> <server_cert.crt>
    <server_cert.crt>: OK
    ```

3.  Check the certificate expiration date:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl x509 -in <server_cert.crt> -noout -dates
    notBefore=May 21 10:30:00 2026 GMT
    notAfter=May 21 10:30:00 2027 GMT
    ```

### [2.7. Creating a private CA by using GnuTLS](#creating-a-private-ca-using-gnutls) {#creating-a-private-ca-by-using-gnutls .title}

Private certificate authorities (CA) are useful when your scenario requires verifying entities within your internal network.

For example, use a private CA when you create a VPN gateway with authentication based on certificates signed by a CA under your control. You can also use a private CA when you do not want to pay a commercial CA. To sign certificates in such use cases, the private CA uses a self-signed certificate.

**Prerequisites**

-   You have `root`{.literal} privileges or permissions to enter administrative commands with `sudo`{.literal}. Commands that require such privileges are marked with `#`{.literal}.

-   You have already installed GnuTLS on your system. If you did not, you can use this command:

    ``` {.language-plaintext tabindex="-1"}
    $ dnf install gnutls-utils
    ```

**Procedure**

1.  Generate a private key for your CA. For example, the following command creates a 256-bit ECDSA (Elliptic Curve Digital Signature Algorithm) key:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --generate-privkey --sec-param High --key-type=ecdsa --outfile <ca.key>
    ```

    The time for the key-generation process depends on the hardware and entropy of the host, the selected algorithm, and the length of the key.

2.  Create a template file for a certificate.

    a.  Create a file with a text editor, for example:

        ``` {.language-plaintext tabindex="-1"}
        $ vi <ca.cfg>
        ```

    b.  Edit the file to include the necessary certification details:

        ``` {.language-plaintext tabindex="-1"}
        organization = "Example Inc."
        state = "Example"
        country = EX
        cn = "Example CA"
        serial = 007
        expiration_days = 365
        ca
        cert_signing_key
        crl_signing_key
        ```

3.  Create a certificate signed using the private key generated in step 1:

    The generated *\<ca.crt\>* file is a self-signed CA certificate that you can use to sign other certificates for one year. *\<ca.crt\>* file is the public key (certificate). The loaded file *\<ca.key\>* is the private key. You should keep this file in safe location.

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --generate-self-signed --load-privkey <ca.key> --template <ca.cfg> --outfile <ca.crt>
    ```

4.  Set secure permissions on the private key of your CA, for example:

    ``` {.language-plaintext tabindex="-1"}
    # chown <root>:<root> <ca.key>
    # chmod 600 <ca.key>
    ```

**Next steps**

-   To use a self-signed CA certificate as a trust anchor on client systems, copy the CA certificate to the client and add it to the clients\' system-wide truststore as `root`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # trust anchor <ca.crt>
    ```

    See the [Using shared system certificates](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/using-shared-system-certificates) chapter for more information.

**Verification**

1.  Display the basic information about your self-signed CA:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --certificate-info --infile <ca.crt>
    Certificate:
    …
            X509v3 extensions:
                …
                X509v3 Basic Constraints: critical
                    CA:TRUE
                X509v3 Key Usage: critical
                    Certificate Sign, CRL Sign
    ```

2.  Create a certificate signing request (CSR), and use your CA to sign the request. The CA must successfully create a certificate based on the CSR, for example:

    a.  Generate a private key for your CA:

        ``` {.language-plaintext tabindex="-1"}
        $ certtool --generate-privkey --outfile <example_server.key>
        ```

    b.  Open a new configuration file in a text editor, for example:

        ``` {.language-plaintext tabindex="-1"}
        $ vi <example_server.cfg>
        ```

    c.  Edit the file to include the necessary certification details:

        ``` {.language-plaintext tabindex="-1"}
        signing_key
        encryption_key
        key_agreement

        tls_www_server

        country = "US"
        organization = "Example Organization"
        cn = "server.example.com"

        dns_name = "example.com"
        dns_name = "server.example.com"
        ip_address = "192.168.0.1"
        ip_address = "::1"
        ip_address = "127.0.0.1"
        ```

    d.  Generate a request with the previously created private key:

        ``` {.language-plaintext tabindex="-1"}
        $ certtool --generate-request --load-privkey <example_server.key> --template <example_server.cfg> --outfile <example_server.crq>
        ```

    e.  Generate the certificate and sign it with the private key of the CA:

        ``` {.language-plaintext tabindex="-1"}
        $ certtool --generate-certificate --load-request <example_server.crq> --load-ca-certificate <ca.crt> --load-ca-privkey <ca.key> --outfile <example_server.crt>
        ```

### [2.8. Creating a private key and a CSR for a TLS server certificate by using GnuTLS](#creating-a-private-key-and-a-csr-for-a-tls-server-certificate-using-gnutls) {#creating-a-private-key-and-a-csr-for-a-tls-server-certificate-by-using-gnutls .title}

You can use TLS-encrypted communication channels only if you have a valid TLS certificate from a certificate authority (CA). To get the certificate, create a private key and a certificate signing request (CSR) for your server first.

**Procedure**

1.  Generate a private key on your server system, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --generate-privkey --sec-param High --outfile <example_server.key>
    ```

2.  Optional: Use a text editor to prepare a configuration file that simplifies creating your CSR, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ vim <example_server.cnf>
    signing_key
    encryption_key
    key_agreement

    tls_www_server

    country = "US"
    organization = "Example Organization"
    cn = "server.example.com"

    dns_name = "example.com"
    dns_name = "server.example.com"
    ip_address = "192.168.0.1"
    ip_address = "::1"
    ip_address = "127.0.0.1"
    ```

3.  Create a CSR by using the private key you created previously:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --generate-request --template <example_server.cfg> --load-privkey <example_server.key> --outfile <example_server.crq>
    ```

    If you omit the `--template`{.literal} option, the `certool`{.literal} utility prompts you for additional information, for example:

    ``` {.language-plaintext tabindex="-1"}
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Generating a PKCS #10 certificate request...
    Country name (2 chars): <US>
    State or province name: <Washington>
    Locality name: <Seattle>
    Organization name: <Example Organization>
    Organizational unit name:
    Common name: <server.example.com>
    ```

**Next steps**

-   Submit the CSR to a CA of your choice for signing. Alternatively, for an internal use scenario within a trusted network, use your private CA for signing. See the [Using a private CA to issue certificates for CSRs with GnuTLS](#using-a-private-ca-to-issue-certificates-for-csrs-with-gnutls "2.10. Using a private CA to issue certificates for CSRs with GnuTLS") for more information.

**Verification**

1.  After you get the requested certificate from the CA, check that the human-readable parts of the certificate match your requirements, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --certificate-info --infile <example_server.crt>
    Certificate:
    …
            Issuer: CN = Example CA
            Validity
                Not Before: Feb  2 20:27:29 2023 GMT
                Not After : Feb  2 20:27:29 2024 GMT
            Subject: C = US, O = Example Organization, CN = server.example.com
            Subject Public Key Info:
                Public Key Algorithm: id-ecPublicKey
                    Public-Key: (256 bit)
    …
            X509v3 extensions:
                X509v3 Key Usage: critical
                    Digital Signature, Key Encipherment, Key Agreement
                X509v3 Extended Key Usage:
                    TLS Web Server Authentication
                X509v3 Subject Alternative Name:
                    DNS:example.com, DNS:server.example.com, IP Address:192.168.0.1, IP
    …
    ```

### [2.9. Creating a private key and a CSR for a TLS client certificate by using GnuTLS](#creating-a-private-key-and-a-csr-for-a-tls-client-certificate-using-gnutls) {#creating-a-private-key-and-a-csr-for-a-tls-client-certificate-by-using-gnutls .title}

You can use TLS-encrypted communication channels only if you have a valid TLS certificate from a certificate authority (CA). To get the certificate, create a private key and a certificate signing request (CSR) for your client first.

**Procedure**

1.  Generate a private key on your client system, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --generate-privkey --sec-param High --outfile <example_client.key>
    ```

2.  Optional: Use a text editor to prepare a configuration file that simplifies creating your CSR, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ vim <example_client.cnf>
    signing_key
    encryption_key

    tls_www_client

    cn = "client.example.com"
    email = "client@example.com"
    ```

3.  Create a CSR using the private key you created previously:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --generate-request --template <example_client.cfg> --load-privkey <example_client.key> --outfile <example_client.crq>
    ```

    If you omit the `--template`{.literal} option, the `certtool`{.literal} utility prompts you for additional information, for example:

    ``` {.language-plaintext tabindex="-1"}
    Generating a PKCS #10 certificate request...
    Country name (2 chars): <US>
    State or province name: <Washington>
    Locality name: <Seattle>
    Organization name: <Example Organization>
    Organizational unit name:
    Common name: <server.example.com>
    ```

**Next steps**

-   Submit the CSR to a CA of your choice for signing. Alternatively, for an internal use scenario within a trusted network, use your private CA for signing. See [Section 2.10, "Using a private CA to issue certificates for CSRs with GnuTLS"](#using-a-private-ca-to-issue-certificates-for-csrs-with-gnutls "2.10. Using a private CA to issue certificates for CSRs with GnuTLS") for more information.

**Verification**

1.  Check that the human-readable parts of the certificate match your requirements, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --certificate-info --infile <example_client.crt>
    Certificate:
    …
                X509v3 Extended Key Usage:
                    TLS Web Client Authentication
                X509v3 Subject Alternative Name:
                    email:client@example.com
    …
    ```

### [2.10. Using a private CA to issue certificates for CSRs with GnuTLS](#using-a-private-ca-to-issue-certificates-for-csrs-with-gnutls) {#using-a-private-ca-to-issue-certificates-for-csrs-with-gnutls .title}

To enable systems to establish a TLS-encrypted communication channel, a certificate authority (CA) must provide valid certificates to them. If you have a private CA, you can create the requested certificates by signing certificate signing requests (CSRs).

**Prerequisites**

-   You have already configured a private CA. See [Section 2.7, "Creating a private CA by using GnuTLS"](#creating-a-private-ca-using-gnutls "2.7. Creating a private CA by using GnuTLS") for more information.
-   You have a file containing a CSR. You can find an example of creating the CSR in [Section 2.8, "Creating a private key and a CSR for a TLS server certificate by using GnuTLS"](#creating-a-private-key-and-a-csr-for-a-tls-server-certificate-using-gnutls "2.8. Creating a private key and a CSR for a TLS server certificate by using GnuTLS") .

**Procedure**

1.  Optional: Use a text editor to prepare a GnuTLS configuration file for adding extensions to certificates, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ vi <server_extensions.cfg>
    honor_crq_extensions
    ocsp_uri = "http://ocsp.example.com"
    ```

2.  Use the `certtool`{.literal} utility to create a certificate based on a CSR, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --generate-certificate --load-request <example_server.crq> --load-ca-privkey <ca.key> --load-ca-certificate <ca.crt> --template <server_extensions.cfg> --outfile <example_server.crt>
    ```

**Verification**

1.  Verify the certificate contents and fields:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --certificate-info --infile <example_server.crt>
    X.509 Certificate Information:
            Version: 3
            Serial Number (hex): 00
            Issuer: CN=Example CA
            Validity:
                    Not Before: Tue May 21 10:30:00 UTC 2026
                    Not After: Wed May 21 10:30:00 UTC 2027
            Subject: CN=server.example.com
            ...
    ```

2.  Verify that the certificate is signed by the correct CA:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --verify --load-ca-certificate <ca.crt> --infile <example_server.crt>
    Certificate[0]: CN=server.example.com
            Issued by: CN=Example CA
            Verification output: Verified.
    ```

3.  Check the certificate expiration date:

    ``` {.language-plaintext tabindex="-1"}
    $ certtool --certificate-info --infile <example_server.crt> | grep -A2 Validity
            Validity:
                    Not Before: Tue May 21 10:30:00 UTC 2026
                    Not After: Wed May 21 10:30:00 UTC 2027
    ```

## [Chapter 3. Using shared system certificates](#using-shared-system-certificates) {#chapter-3.-using-shared-system-certificates .title}

Use the centralized system truststore in RHEL for managing TLS certificates. Using a shared trust location simplifies certificate management and verification across the system.

### [3.1. The system-wide truststore](#the-system-wide-truststore) {#the-system-wide-truststore .title}

RHEL contains a centralized system for managing TLS certificates. NSS, GnuTLS, OpenSSL, and Java use this shared certificate storage to retrieve system certificate anchors and denylist information.

By default, the truststore contains the Mozilla CA list, which includes both positive and negative trust. You can update the core Mozilla CA list by using the centralized system.

The system-wide truststore is located in the `/etc/pki/ca-trust/`{.literal} and `/usr/share/pki/ca-trust-source/`{.literal} directories. The trust settings in `/usr/share/pki/ca-trust-source/`{.literal} have lower priority than settings in `/etc/pki/ca-trust/`{.literal}.

The system treats certificate files based on the subdirectory to which you install them:

-   Trust anchors belong to

    -   `/usr/share/pki/ca-trust-source/anchors/`{.literal} or
    -   `/etc/pki/ca-trust/source/anchors/`{.literal}.

-   Distrusted certificates are stored in

    -   `/usr/share/pki/ca-trust-source/blocklist/`{.literal} or
    -   `/etc/pki/ca-trust/source/blocklist/`{.literal}.

-   Certificates in the extended BEGIN TRUSTED file (OpenSSL trust certificate) format are located in

    -   `/usr/share/pki/ca-trust-source/`{.literal} or
    -   `/etc/pki/ca-trust/source/`{.literal}.

To add a new certificate to the truststore:

-   For trusted certificates, copy the certificate to `/etc/pki/ca-trust/source/anchors/`{.literal}.
-   For distrusted certificates, copy the certificate to `/etc/pki/ca-trust/source/blocklist/`{.literal}.
-   Enter the `update-ca-trust`{.literal} command, or use the `trust anchor`{.literal} subcommand.

See the `update-ca-trust(8)`{.literal} and `trust(1)`{.literal} man pages on your system for more information.

Note

In a hierarchical cryptographic system, a trust anchor is an authoritative entity that other parties consider trustworthy. In the X.509 architecture, a root certificate is a trust anchor from which a chain of trust is derived. To enable chain validation, the trusting party must have access to the trust anchor.

### [3.2. Adding new certificates to the system-wide truststore](#adding-new-certificates-to-the-system-wide-truststore) {#adding-new-certificates-to-the-system-wide-truststore .title}

You can add new certificates to the system-wide truststore. All cryptographic applications running on the system recognize them as trusted.

Note

Even though the Mozilla Firefox browser can use an added certificate without executing `update-ca-trust`{.literal}, enter the `update-ca-trust`{.literal} command after every CA change.

Browsers, such as Mozilla Firefox and Chromium, cache files. You might have to clear your browser's cache or restart your browser to load the current system certificate configuration.

**Prerequisites**

-   The `ca-certificates`{.literal} package is present on the system.

**Procedure**

1.  Copy your certificate file in the PEM or DER format to `/usr/share/pki/ca-trust-source/anchors/`{.literal} or `/etc/pki/ca-trust/source/anchors/`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # cp <~/certificate-trust-examples/Cert-trust-test-ca.pem> /usr/share/pki/ca-trust-source/anchors/
    ```

2.  Update the system-wide truststore configuration:

    ``` {.language-plaintext tabindex="-1"}
    # update-ca-trust extract
    ```

### [3.3. Trusted system certificates management with the trust command](#trusted-system-certificates-management-with-the-trust-command) {#trusted-system-certificates-management-with-the-trust-command .title}

You can manage certificates within the shared system-wide truststore by using the trust command.

You can add or remove certificates from the system-wide truststore by using:

-   Basic file operations with the corresponding files and the `update-ca-trust`{.literal} command. See the [Adding new certificates to the system-wide truststore](#adding-new-certificates-to-the-system-wide-truststore "3.2. Adding new certificates to the system-wide truststore") section for details.
-   The `trust`{.literal} command.

The `trust`{.literal} command manages certificates in the shared system-wide truststore. You can use its subcommands to list, extract, add, remove, or change trust anchors.

-   To see the built-in help for the `trust`{.literal} command, enter it without any arguments or with the `--help`{.literal .option} directive. Also, all subcommands of the `trust`{.literal .command} commands provide a detailed built-in help, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ trust list --help
    usage: trust list --filter=<what>
    …
    ```

-   To list all system trust anchors and certificates, use the `trust list`{.literal .command} command, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ trust list
    …
    pkcs11:id=%DD%04%09%07%A2%F5%7A%7D%52%53%12%92%95%EE%38%80%25%0D%A6%59;type=cert
        type: certificate
        label: SSL.com Root Certification Authority RSA
        trust: anchor
        category: authority
    …
    ```

-   To store a trust anchor into the system-wide truststore, use the `trust anchor`{.literal} subcommand. Specify a path to a certificate. Replace *\<path.to/certificate.crt\>* with the path to your certificate:

    ``` {.language-plaintext tabindex="-1"}
    # trust anchor <path.to/certificate.crt>
    ```

-   To remove a certificate, use either a path to a certificate or the ID of a certificate:

    ``` {.language-plaintext tabindex="-1"}
    # trust anchor --remove <path.to/certificate.crt>
    # trust anchor --remove "pkcs11:id=<%AA%BB%CC%DD%EE>;type=cert"
    ```

See the `trust(1)`{.literal} man page on your system for more information.

## [Chapter 4. Planning and implementing TLS](#planning-and-implementing-tls) {#chapter-4.-planning-and-implementing-tls .title}

When you harden TLS, you must balance security and client compatibility. Stricter settings limit client support. Relaxed settings support more clients but reduce security.

TLS (Transport Layer Security) secures network traffic. You can improve security by setting:

-   Key-exchange methods
-   Authentication methods
-   Encryption algorithms

More client support means lower security. Strict settings mean better security but less compatibility.

Use the strictest settings. Relax them only when you need more compatibility.

### [4.1. SSL and TLS protocols](#ssl-and-tls-protocols) {#ssl-and-tls-protocols .title}

Review the history and usage recommendations for SSL and TLS protocols to understand which versions are secure and which to avoid.

Netscape Corporation developed the Secure Sockets Layer (SSL) protocol for secure Internet communication. The Internet Engineering Task Force (IETF) adopted it and renamed it Transport Layer Security (TLS).

TLS sits between an application protocol layer and a reliable transport layer such as TCP/IP. You can layer TLS underneath different protocols such as HTTP, FTP, and SMTP.

+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Protocol version | Usage recommendation                                                                                                                                                                                                          |
+:=================+:==============================================================================================================================================================================================================================+
| SSL v2           | Do not use. This version has serious security vulnerabilities. RHEL 7 removed it from the core cryptographic libraries.                                                                                                       |
+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SSL v3           | Do not use. This version has serious security vulnerabilities. RHEL 8 removed it from the core cryptographic libraries.                                                                                                       |
+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TLS 1.0          | Not recommended. This version has known issues that cannot be fixed. It does not support modern cipher suites. RHEL 10 disables it in all cryptographic policies.                                                             |
+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TLS 1.1          | Use only for interoperability. This version does not support modern cipher suites. RHEL 10 disables it in all cryptographic policies.                                                                                         |
+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TLS 1.2          | Uses AEAD cipher suites. All system-wide cryptographic policies enable this version. Some optional parts have vulnerabilities. Supports outdated algorithms.                                                                  |
+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TLS 1.3          | Recommended version. Removes known problematic options. Provides additional privacy by encrypting more of the handshake. Faster due to more efficient algorithms. All system-wide cryptographic policies enable this version. |
+------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

**Additional resources**

-   [IETF: The Transport Layer Security (TLS) Protocol Version 1.3](https://tools.ietf.org/html/rfc8446)

### [4.2. Security considerations for TLS in RHEL 10](#security-considerations-for-tls-in-rhel-10) {#security-considerations-for-tls-in-rhel-10 .title}

Review key security aspects when configuring TLS in RHEL. You can harden your cryptographic settings by selecting protocols, cipher suites, and key lengths.

RHEL 10 libraries provide secure default settings for most deployments. TLS implementations use secure algorithms when possible. They do not prevent connections from or to legacy clients or servers.

Apply hardened settings in strict security environments. Use hardened settings when legacy clients or servers lack secure algorithm support. Apply them when such clients are not expected or allowed to connect.

RHEL 10 configures TLS by using the system-wide cryptographic policies mechanism. TLS versions earlier than 1.2 are no longer supported. The `DEFAULT`{.literal}, `FUTURE`{.literal}, and `LEGACY`{.literal} cryptographic policies allow only TLS 1.2 and 1.3.

The most straightforward way to harden your TLS configuration is switching the system-wide cryptographic policy level to `FUTURE`{.literal} by using the `update-crypto-policies --set FUTURE`{.literal} command.

Warning

Algorithms disabled for the `LEGACY`{.literal} cryptographic policy do not conform to Red Hat's vision of RHEL 10 security. Their security properties are not reliable. Consider moving away from using these algorithms instead of re-enabling them.

If you re-enable them for interoperability with old hardware, treat them as insecure. Apply extra protection measures such as isolating their network interactions to separate network segments. Do not use them across public networks.

If you do not follow RHEL system-wide cryptographic policies, use the following recommendations. These also apply when you create custom cryptographic policies for your setup. The recommendations cover protocols, cipher suites, and key lengths:

#### [4.2.1. Protocols](#protocols) {#protocols .title}

The latest TLS version provides the best security. TLS 1.2 is the minimum version even when using the `LEGACY`{.literal} cryptographic policy.

You can re-enable older protocol versions by opting out of cryptographic policies or providing a custom policy. The resulting configuration is not supported.

RHEL 10 supports TLS version 1.3. Not all features of this protocol are fully supported by RHEL 10 components. For example, Apache web server does not yet fully support the 0-RTT (Zero Round Trip Time) feature.

Warning

RHEL 9.2 and later systems running in FIPS mode enforce the Extended Primary Secret (EMS) extension (RFC 7627). The FIPS 140-3 standard requires EMS for any TLS 1.2 connection. Legacy clients that do not support EMS or TLS 1.3 cannot connect to RHEL 9 and 10 servers in FIPS mode. RHEL 9 and 10 clients in FIPS mode cannot connect to servers that support only TLS 1.2 without EMS.

#### [4.2.2. Cipher suites](#cipher_suites) {#cipher-suites .title}

Prefer modern, secure cipher suites to old, insecure ones. Always disable eNULL and aNULL cipher suites. These offer no encryption or authentication.

Disable cipher suites based on RC4 or HMAC-MD5. These have serious shortcomings. Also disable export cipher suites. These have been intentionally weakened and are easy to break.

Cipher suites that offer less than 128 bits of security have a short useful life. Do not use them.

Algorithms that use 128 bits of security or more remain unbreakable for at least several years. Use these algorithms. Note that 3DES ciphers advertise 168 bits but actually offer 112 bits of security.

Always prefer cipher suites that support (perfect) forward secrecy (PFS). PFS ensures the confidentiality of encrypted data even when the server key is compromised.

This rules out the fast RSA key exchange. Use ECDHE or DHE instead. ECDHE is faster and the preferred choice.

Prefer AEAD ciphers such as AES-GCM over CBC-mode ciphers. AEAD ciphers are not vulnerable to padding oracle attacks.

AES-GCM is faster than AES in CBC mode in many cases. This is especially true when the hardware has cryptographic accelerators for AES.

ECDHE key exchange with ECDSA certificates is faster than pure RSA key exchange. You can install two pairs of certificates and keys on a server to support legacy clients. Use ECDSA keys for new clients and RSA keys for legacy ones.

#### [4.2.3. Public key length](#public_key_length) {#public-key-length .title}

When using RSA keys, prefer key lengths of at least 3072 bits signed by at least SHA-256. This is sufficiently large for true 128 bits of security.

Warning

Your system security is only as strong as the weakest link in the chain. A strong cipher alone does not guarantee good security.

The keys and certificates are equally important. The hash functions and keys used by the Certification Authority (CA) to sign your keys are also important.

**Additional resources**

-   [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies)
-   [TLS Extension \"Extended Master Secret\" enforced with Red Hat Enterprise Linux 9.2 (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7018256)

### [4.3. TLS configuration hardening in applications](#hardening-tls-configuration-in-applications) {#tls-configuration-hardening-in-applications .title}

You can override system-wide cryptographic policies with custom TLS configuration settings to harden specific applications.

RHEL system-wide cryptographic policies ensure security compliance for applications that use cryptographic libraries. They prevent the use of known insecure protocols, ciphers, or algorithms.

Always ensure that your server application enforces *server-side cipher order*. This determines the cipher suite by the order you configure. For more information, see the `crypto-policies(7)`{.literal}, `config(5)`{.literal}, and `ciphers(1)`{.literal} man pages.

#### [4.3.1. TLS configuration of an Apache HTTP server](#configuring-the-apache-http-server) {#tls-configuration-of-an-apache-http-server .title}

The `Apache HTTP Server`{.literal} is compatible with both OpenSSL and NSS libraries for handling TLS requirements. RHEL 10 includes packages for the `mod_ssl`{.literal} functionality.

The `mod_ssl`{.literal} package creates the `/etc/httpd/conf.d/ssl.conf`{.literal} configuration file. You can use this file to modify the server's TLS-related settings.

The `httpd-manual`{.literal} package provides complete documentation for the `Apache HTTP Server`{.literal}, including TLS configuration. The `/usr/share/httpd/manual/mod/mod_ssl.html`{.literal} file describes directives available in `/etc/httpd/conf.d/ssl.conf`{.literal}. The `/usr/share/httpd/manual/ssl/ssl_howto.html`{.literal} file describes examples of various settings.

When modifying the `/etc/httpd/conf.d/ssl.conf`{.literal} configuration file, consider these three directives:

`SSLProtocol`{.literal}
:   Use this directive to specify the version of TLS or SSL you want to allow.

`SSLCipherSuite`{.literal}
:   Use this directive to specify your preferred cipher suite or disable the ones you want to disallow.

`SSLHonorCipherOrder`{.literal}
:   Uncomment and set this directive to `on`{.literal} to ensure that the connecting clients adhere to the order of ciphers you specified.

To use only the TLS 1.2 and 1.3 protocols, add the following line to the configuration file:

``` {.language-plaintext tabindex="-1"}
SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
```

#### [4.3.2. TLS configuration of an Nginx HTTP and proxy server](#configuring-the-nginx-http-and-proxy-server) {#tls-configuration-of-an-nginx-http-and-proxy-server .title}

To enable TLS 1.3 support in `Nginx`{.literal}, add the `TLSv1.3`{.literal} value to the `ssl_protocols`{.literal} option in the `server`{.literal} section of `/etc/nginx/nginx.conf`{.literal}:

``` {.language-plaintext tabindex="-1"}
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    …
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers
    …
}
```

#### [4.3.3. TLS configuration of a Dovecot mail server](#configuring-the-dovecot-mail-server) {#tls-configuration-of-a-dovecot-mail-server .title}

To configure the `Dovecot`{.literal} mail server to use TLS, modify the `/etc/dovecot/conf.d/10-ssl.conf`{.literal} configuration file. The `/usr/share/doc/dovecot/wiki/SSL.DovecotConfiguration.txt`{.literal} file explains basic configuration directives. The standard `Dovecot`{.literal} installation installs this file.

When modifying `/etc/dovecot/conf.d/10-ssl.conf`{.literal}, consider these three directives:

`ssl_protocols`{.literal}
:   Use this directive to specify the version of TLS or SSL you want to allow or disable.

`ssl_cipher_list`{.literal}
:   Use this directive to specify your preferred cipher suites or disable the ones you want to disallow.

`ssl_prefer_server_ciphers`{.literal}
:   Uncomment and set this directive to `yes`{.literal} to ensure that the connecting clients adhere to the order of ciphers you specified.

For example, the following line in `/etc/dovecot/conf.d/10-ssl.conf`{.literal} allows only TLS 1.1 and later:

``` {.language-plaintext tabindex="-1"}
ssl_protocols = !SSLv2 !SSLv3 !TLSv1
```

**Additional resources**

-   [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies)
-   [Deploying web servers and reverse proxies](https://docs.redhat.com/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/index)
-   [Configuring TLS encryption on an Apache HTTP Server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/setting-up-the-apache-http-web-server#configuring-tls-encryption-on-an-apache-http-server)
-   [Adding TLS encryption to an Nginx web server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/setting-up-and-configuring-nginx#adding-tls-encryption-to-an-nginx-web-server)
-   [Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)](https://tools.ietf.org/html/rfc7525)
-   [Mozilla SSL Configuration Generator](https://mozilla.github.io/server-side-tls/ssl-config-generator/)
-   [SSL Server Test](https://www.ssllabs.com/ssltest/)

## [Chapter 5. Securing system DNS traffic with encrypted DNS (eDNS)](#securing-system-dns-traffic-with-encrypted-dns) {#chapter-5.-securing-system-dns-traffic-with-encrypted-dns-edns .title}

You can enable encrypted DNS (eDNS) to secure DNS communication that uses DNS-over-TLS (DoT) protocol. Encrypted DNS encrypts all DNS traffic end-to-end, with no fallback to insecure protocols. It aligns with the principles of zero trust architecture (ZTA).

The current implementation of eDNS in RHEL uses only the DoT protocol. You can use two primary methods to install RHEL with eDNS enabled:

-   Perform an interactive installation from local media.
-   Build a custom bootable ISO to ensure eDNS is configured with an `enforce`{.literal} policy during and after installation.
-   Convert an existing RHEL installation to use eDNS.

### [5.1. Overview of components for eDNS in RHEL](#overview-of-components-for-edns) {#overview-of-components-for-edns-in-rhel .title}

The core components interact in the eDNS setup to enable proper configuration and security.

The following components make up the eDNS setup in RHEL:

NetworkManager
:   NetworkManager enables eDNS and enforces the use of encrypted DNS protocols based on the configured policy. It uses `dnsconfd`{.literal} as its DNS resolver.

`dnsconfd`{.literal}
:   `dnsconfd`{.literal} is a local DNS cache configuration daemon. It simplifies the setup of DNS caching, split DNS, and DNS over TLS (DoT).

`unbound`{.literal}
:   `unbound`{.literal} is a validating, recursive, and caching DNS resolver. In the eDNS setup, it serves as the runtime cache service for `dnsconfd`{.literal}. `unbound`{.literal} uses TLS for upstream DNS queries to encrypt DNS traffic to external DoT servers. `unbound`{.literal} also manages caches to store DNS responses, reducing repeated external queries and improving performance.

#### [5.1.1. eDNS resolution process and core interactions](#edns_resolution_process_and_core_interactions) {#edns-resolution-process-and-core-interactions .title}

1.  An application requests to resolve a hostname.
2.  The system reads the `/etc/resolv.conf`{.literal} file and sends the query to the local `unbound`{.literal} service.
3.  `unbound`{.literal} first checks its internal caches for a valid, cached response.
4.  If not found in the cache, `unbound`{.literal} encrypts the DNS query by using TLS and sends it to the configured upstream DoT enabled DNS server.
5.  The upstream DoT server processes the query and sends an encrypted DNS response back to `unbound`{.literal}.
6.  `unbound`{.literal} decrypts, validates, and caches the response.
7.  Finally, `unbound`{.literal} sends the resolved DNS response back to the application.

### [5.2. Installing RHEL with eDNS enabled from a local installation media](#installing-rhel-with-edns-enabled-from-a-local-installation-media) {#installing-rhel-with-edns-enabled-from-a-local-installation-media .title}

Install RHEL with encrypted DNS (eDNS) enabled directly from local media using an enforce policy. This helps ensure that all DNS queries remain private and secure during and after the installation process.

If you require a custom CA certificate bundle, you must install it by using the `%certificate`{.literal} section in the Kickstart file.

During the installation, you must provide both the RHEL installation content and the Kickstart file from local media. You cannot download the Kickstart file from a remote HTTP server because the installation program requires to use DNS to resolve the server's hostname. If your environment is configured to support a fallback to unencrypted DNS, you can perform a standard RHEL installation and configure eDNS afterwards.

**Prerequisites**

-   Commands that start with the `#`{.literal} command prompt require administrative privileges provided by `sudo`{.literal} or root user access. For information on how to configure `sudo`{.literal} access, see [Enabling unprivileged users to run certain commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access#enabling-unprivileged-users-to-run-certain-commands).
-   You have the RHEL installation media available locally.
-   If you require a custom CA bundle, have your Kickstart file with a `%certificate`{.literal} section available locally.

**Procedure**

1.  Optional: Create a Kickstart file with a `%certificate`{.literal} section. Ensure the certificate is saved in a file named `tls-ca-bundle.pem`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    %certificate --dir /etc/pki/dns/extracted/pem/ --filename tls-ca-bundle.pem
    -----BEGIN CERTIFICATE-----
    <Base64-encoded_certificate_content>
    -----END CERTIFICATE-----
    %end
    ```

2.  Prepare your bootable installation media. For instructions, see [Creating a bootable installation medium for RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/creating-a-bootable-installation-medium-for-rhel). If you use a custom CA bundle, include your Kickstart file on the media.

3.  [Boot the installation media](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/booting-the-installation-media-).

4.  From the boot menu window, select the required option and press the `e`{.literal} key to edit the boot parameters.

5.  Add the eDNS kernel arguments:

    ``` {.language-plaintext tabindex="-1"}
    linux ($root)/vmlinuz-6.12.0-0.el10_0.x86_64 root=/dev/mapper/rhel-root ro crashkernel=2G-64G:256M,64G-:512M resume=/dev/mapper/rhel-swap rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet emergency ip=dhcp rd.net.dns=dns+tls://<server_ip>#<dns_server_hostname> rd.net.dns-resolve-mode=exclusive rd.net.dns-backend=dnsconfd inst.ks=hd:/dev/sdb1/mykickstart.ks
    ```

6.  When you finish editing, press `Ctrl+X`{.literal} to start the installation using the specified options.

**Verification**

-   Verify your eDNS configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ dnsconfd status
    ```

    Expected output:

    ``` {.language-plaintext tabindex="-1"}
    Running cache service:
    unbound
    Resolving mode: exclusive
    Config present in service:
    {
        ".": [
            "dns+tls://198.51.100.143#dot.dns.example.com"
        ]
    }
    State of Dnsconfd:
    RUNNING
    Info about servers: [
        {
            "address": "198.51.100.143",
            "port": 853,
            "name": "dot.dns.example.com",
            "routing_domains": [
                "."
            ],
            "search_domains": [],
            "interface": null,
            "protocol": "dns+tls",
            "dnssec": true,
            "networks": [],
            "firewall_zone": null
        }
    ]
    ```

-   Verify that DNS server is responsive by using `nslookup`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ nslookup <domain_name>
    ```

    Replace the *`<domain_name>`{.literal}* with the domain that you want to query.

**Troubleshooting**

-   Enable detailed logging in `unbound`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # unbound-control verbosity 5
    ```

-   Review logs for the relevant service:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -xe -u <service_name>
    ```

    Replace *`<service_name>`{.literal}* with `NetworkManager`{.literal}, `dnsconfd`{.literal}, or `unbound`{.literal}.

**Additional resources**

-   [Creating Kickstart files](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/creating-kickstart-files)
-   [Kickstart certificates section](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/kickstart-script-file-format-reference#kickstart-certificates-section)
-   [Creating a bootable installation medium for RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/creating-a-bootable-installation-medium-for-rhel)
-   [Configuring kernel command-line parameters](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kernel-command-line-parameters)

### [5.3. Installing RHEL with eDNS enabled using a custom bootable ISO](#installing-rhel-with-edns-enabled-using-a-custom-bootable-iso) {#installing-rhel-with-edns-enabled-using-a-custom-bootable-iso .title}

Create a custom bootable ISO to install RHEL with encrypted DNS (eDNS) enabled using a strict enforce policy. This method helps ensure that all DNS traffic is private and secure during and after the installation.

If you require a custom CA certificate bundle, you must install it by using the `%certificate`{.literal} section in the Kickstart file. You then reference this Kickstart file in a script to build a new ISO, which includes kernel arguments to enforce a strict DoT policy. If your environment is configured to support a fallback to unencrypted DNS, you can perform a standard RHEL installation and configure eDNS afterwards.

**Prerequisites**

-   Commands that start with the `#`{.literal} command prompt require administrative privileges provided by `sudo`{.literal} or root user access. For information on how to configure `sudo`{.literal} access, see [Enabling unprivileged users to run certain commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access#enabling-unprivileged-users-to-run-certain-commands).
-   You have downloaded the minimal installation Boot ISO image from the Product Downloads page.
-   You have a Kickstart file ready with a `%certificate`{.literal} section if you need a custom CA bundle.
-   The `lorax`{.literal} package is installed.

**Procedure**

1.  Optional: Create a Kickstart file with a `%certificate`{.literal} section. Ensure the certificate is saved in a file named `tls-ca-bundle.pem`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    %certificate --dir /etc/pki/dns/extracted/pem/ --filename tls-ca-bundle.pem
    -----BEGIN CERTIFICATE-----
    <Base64-encoded_certificate_content>
    -----END CERTIFICATE-----
    %end
    ```

2.  Add the Kickstart file and kernel arguments into the ISO:

    The following script example demonstrates how to create a custom bootable ISO with eDNS enabled. You must create a script file to automate this process.

    ``` {.language-plaintext tabindex="-1"}
    #!/bin/bash

    set -ex

    KERNELARGS=""

    # Enable network
    KERNELARGS+="ip=dhcp "

    # Set DoT DNS server
    KERNELARGS+="rd.net.dns=dns+tls://_<server_ip>_#_<dns_server_hostname>_ "

    # Set to 'exclusive' to disable fallback to unencrypted DNS. Other values: 'backup', 'prefer'.
    KERNELARGS+="rd.net.dns-resolve-mode=exclusive "

    # Set the dnsconfd plugin for NetworkManager
    KERNELARGS+="rd.net.dns-backend=dnsconfd "

    # Remove any existing ISO to prevent conflicts with the new build
    rm -f _<output_iso_filename>_

    # Create a new bootable ISO with the Kickstart config file and kernel arguments
    mkksiso --ks _<kickstart_file>_ --cmdline "$KERNELARGS" _<input_iso_filename>_ _<output_iso_filename>_
    ```

3.  Run the script.

    ``` {.language-plaintext tabindex="-1"}
    sh <script_filename>
    ```

4.  Install RHEL using the customized ISO file.

**Verification**

-   Verify your eDNS configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ dnsconfd status
    ```

    Expected output:

    ``` {.language-plaintext tabindex="-1"}
    Running cache service:
    unbound
    Resolving mode: exclusive
    Config present in service:
    {
        ".": [
            "dns+tls://198.51.100.143#dot.dns.example.com"
        ]
    }
    State of Dnsconfd:
    RUNNING
    Info about servers: [
        {
            "address": "198.51.100.143",
            "port": 853,
            "name": "dot.dns.example.com",
            "routing_domains": [
                "."
            ],
            "search_domains": [],
            "interface": null,
            "protocol": "dns+tls",
            "dnssec": true,
            "networks": [],
            "firewall_zone": null
        }
    ]
    ```

-   Verify that DNS server is responsive by using `nslookup`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ nslookup <domain_name>
    ```

    Replace the *`<domain_name>`{.literal}* with the domain that you want to query.

**Troubleshooting**

-   Enable detailed logging in `unbound`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # unbound-control verbosity 5
    ```

-   Review logs for the relevant service:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -xe -u <service_name>
    ```

    Replace *`<service_name>`{.literal}* with `NetworkManager`{.literal}, `dnsconfd`{.literal}, or `unbound`{.literal}.

**Additional resources**

-   [Creating Kickstart files](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/creating-kickstart-files)
-   [Kickstart certificates section](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/kickstart-script-file-format-reference#kickstart-certificates-section)
-   [Creating a bootable installation medium for RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/creating-a-bootable-installation-medium-for-rhel)

### [5.4. Enabling eDNS on an existing RHEL installation](#enabling-edns-on-an-existing-rhel-installation) {#enabling-edns-on-an-existing-rhel-installation .title}

You can enable encrypted DNS (eDNS) on an existing RHEL installation to handle all DNS traffic by using DNS-over-TLS.

**Prerequisites**

-   Commands that start with the `#`{.literal} command prompt require administrative privileges provided by `sudo`{.literal} or root user access. For information on how to configure `sudo`{.literal} access, see [Enabling unprivileged users to run certain commands](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access#enabling-unprivileged-users-to-run-certain-commands).

-   Have an existing RHEL installation.

-   The following packages are installed on your system:

    -   `dnsconfd`{.literal}
    -   `dnsconfd-dracut`{.literal}
    -   `grubby`{.literal}

-   If on an IBM Z system, the `zipl`{.literal} utility is installed.

**Procedure**

1.  Configure NetworkManager in the `/etc/NetworkManager/conf.d/global-dot.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [main]
    dns=dnsconfd

    [global-dns]
    resolve-mode=exclusive

    [global-dns-domain-*]
    servers=dns+tls://<server_ip_1><dns_server_hostname_1>,dns+tls://<server_ip_2><dns_server_hostname_2>
    ```

    For more details on global DNS options, see the `GLOBAL-DNS SECTION`{.literal} in `NetworkManager.conf(5)`{.literal} man page on your system.

2.  Optional: To use a custom CA bundle for validating upstream DoT servers, copy the PEM-formatted file to the `/etc/pki/dns/extracted/pem/tls-ca-bundle.pem`{.literal} file.

    Note

    After adding or removing certificates in `/etc/pki/dns/extracted/pem`{.literal}, restart the `dnsconfd`{.literal} service to apply the changes.

3.  Enable the `dnsconfd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now dnsconfd
    ```

4.  Reload NetworkManager:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload NetworkManager
    ```

5.  Regenerate `initramfs`{.literal} for all installed kernels to include `dnsconfd`{.literal} and its configuration:

    ``` {.language-plaintext tabindex="-1"}
    # for kernel in `rpm -q kernel --qf '%{VERSION}-%{RELEASE}.%{ARCH}\n'`; do
        dracut -f --kver="$kernel"
    done
    ```

6.  Set kernel arguments to the current and newly installed kernel version:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --args="rd.net.dns=dns+tls://<server_ip>#<dns_server_hostname> rd.net.dns-resolve-mode=exclusive rd.net.dns-backend=dnsconfd" --update-kernel=ALL
    ```

    -   If on IBM Z, update the boot menu:

        ``` {.language-plaintext tabindex="-1"}
        # zipl
        ```

**Verification**

-   Verify your eDNS configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ dnsconfd status
    ```

    Expected output:

    ``` {.language-plaintext tabindex="-1"}
    Running cache service:
    unbound
    Resolving mode: exclusive
    Config present in service:
    {
        ".": [
            "dns+tls://198.51.100.143#dot.dns.example.com"
        ]
    }
    State of Dnsconfd:
    RUNNING
    Info about servers: [
        {
            "address": "198.51.100.143",
            "port": 853,
            "name": "dot.dns.example.com",
            "routing_domains": [
                "."
            ],
            "search_domains": [],
            "interface": null,
            "protocol": "dns+tls",
            "dnssec": true,
            "networks": [],
            "firewall_zone": null
        }
    ]
    ```

-   Verify that the DNS server is responsive by using `nslookup`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ nslookup <domain_name>
    ```

    Replace the *`<domain_name>`{.literal}* with the domain that you want to query.

**Troubleshooting**

-   Enable detailed logging in `unbound`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # unbound-control verbosity 5
    ```

-   Review logs for the relevant service:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -xe -u <service_name>
    ```

    Replace *`<service_name>`{.literal}* with `NetworkManager`{.literal}, `dnsconfd`{.literal}, or `unbound`{.literal}.

**Additional resources**

-   [Changing kernel command-line parameters for all boot entries](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kernel-command-line-parameters#changing-kernel-command-line-parameters-for-all-boot-entries)

### [5.5. Kernel parameters for DNS configuration](#kernel-parameters-for-dns-configuration) {#kernel-parameters-for-dns-configuration .title}

You can use kernel arguments to enable DNS over TLS (DoT) at boot time and set DNS resolution behavior for your system.

`rd.net.dns-resolve-mode`{.literal}

:   Defines how DNS servers from global configuration are used during resolution. The following modes are relevant for both kernel arguments and `NetworkManager.conf`{.literal} global configuration:

    `exclusive`{.literal}
    :   Uses only the DNS servers specified by kernel arguments or in `NetworkManager.conf`{.literal}. Forbids fallback to DNS servers retrieved from connections. This mode is relevant only for `dnsconfd`{.literal} plugin.

    `prefer`{.literal}
    :   Forbids using DNS servers from connections for general queries unless the queries are subdomains of domains set by connection.

    `backup`{.literal}
    :   Merges and uses DNS servers from both the global configuration and network connections for the same purposes.

`rd.net.dns-servers`{.literal}

:   Configures the list of DNS servers to use. To define multiple DNS servers, set `rd.net.dns`{.literal} multiple times:

    ``` {.language-plaintext tabindex="-1"}
    rd.net.dns=dns+tls://<server_ip_1>#<dns_server_hostname_1> rd.net.dns=dns+tls://<server_ip_2>#<dns_server_hostname_2>
    ```

    For example:

    ``` {.language-plaintext tabindex="-1"}
    rd.net.dns=dns+tls://198.51.100.143#dot.dns.example.com rd.net.dns=dns+tls://203.0.113.1#dot.dns.example.net
    ```

`rd.net.dns-backend`{.literal}
:   Specifies the back-end DNS resolver. When set to `dnsconfd`{.literal}, the system uses `dnsconfd`{.literal} as a local DNS cache configuration daemon.

### [5.6. Additional resources](#securing-system-dns-traffic-with-encrypted-dns_56-additional-resources) {#additional-resources-2 .title}

-   [Securing DNS with DoT in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/securing-dns-with-dot-in-idm)

## [Chapter 6. Setting up an IPsec VPN](#setting-up-an-ipsec-vpn) {#chapter-6.-setting-up-an-ipsec-vpn .title}

Configure and manage a secure Virtual Private Network (VPN) by using the Libreswan implementation of the IPsec protocol suite. Libreswan creates encrypted tunnels for secure data transmission over the internet.

IPsec tunnels ensure the confidentiality and integrity of data in transit. Common use cases include connecting branch offices to headquarters or providing remote users with secure access to a corporate network.

RHEL provides different options to configure Libreswan:

-   Manually edit the Libreswan configuration files for granular control over advanced options.
-   Use the `vpn`{.literal} RHEL system role to automate the process of creating Libreswan VPN configurations.
-   Use Nmstate to configure a Libreswan connection through a declarative API.

Libreswan does not use terms such as \"client\" and \"server\". Instead, IPsec refers to endpoints as \"left\" and \"right\".

With this design, you can often use the same configuration on both hosts. Libreswan dynamically sets the role. By convention, you can use `left`{.literal} for the local host and `right`{.literal} for the remote host.

Note

Libreswan is the only supported VPN technology in RHEL.

IPsec relies on standardized protocols, such as Internet Key Exchange (IKE), to ensure that different systems can communicate effectively. However, in practice, minor differences in how vendors implement these standards can lead to compatibility problems. If you encounter such interoperability issues when connecting Libreswan to a third-party IPsec peer, contact Red Hat Support.

### [6.1. Components in an IPsec VPN](#components-in-an-ipsec-vpn) {#components-in-an-ipsec-vpn .title}

Before setting up an IPsec VPN, it is important to understand its main components: Internet Key Exchange (IKE) for authentication and negotiation, and IPsec for data encryption and transport.

IKE is the protocol for authentication and negotiation between two endpoints. It negotiates connection rules, including encryption algorithms. Libreswan implements IKE in the `pluto`{.literal} daemon.

IPsec encrypts and transports data. It follows the policy from the IKE negotiation. The Linux kernel implements the IPsec protocol suite.

### [6.2. Libreswan authentication methods](#libreswan-authentication-methods) {#libreswan-authentication-methods .title}

Select the appropriate authentication method to establish a secure VPN connection based on your security needs and network environment.

Libreswan supports the following authentication methods:

Pre-Shared key
:   The Pre-Shared Key (PSK) method uses the same secret on both endpoints. Each endpoint authenticates the other endpoint. PSKs are simple and broadly compatible. They are suitable for small-scale deployments. However, managing PSKs is risky if you reuse the key or do not rotate it frequently. For security, PSKs must have more than 64 random characters. On hosts in FIPS mode, PSKs must meet FIPS strength requirements.

Raw RSA key
:   This method uses an RSA public and private key pair on each peer for mutual identification. Raw RSA keys provide stronger security than PSKs and are ideal for environments where a full certificate infrastructure is not required.

X.509 certificates
:   This method uses X.509 certificates from a trusted Certificate Authority (CA). Each peer proves its identity with its certificate and private key. The other peer verifies the certificate against the trusted CA. This method provides the highest level of security and scalability for large enterprises. However, it is more complex. You must deploy and maintain a public key infrastructure (PKI).

NULL authentication
:   This method provides only encryption with no authentication between peers. Because it does not verify the identity of the remote endpoint, NULL authentication is insecure and offers no protection against man-in-the-middle attacks.

Protection against quantum computers
:   PPKs are not a standalone authentication method. Libreswan offers them to protect modern IKEv2 connections from attacks by quantum computers. This feature is necessary because the older IKEv1 protocol and standard IKEv2 are not quantum-resistant on their own. A PPK adds another layer of security on top of the primary authentication method. PPK security depends on using a cryptographically strong key. Distribute this key securely through an external communication channel.

### [6.3. Manually configuring an IPsec host-to-host VPN with raw RSA key authentication](#manually-configuring-an-ipsec-host-to-host-vpn-with-raw-rsa-key-authentication) {#manually-configuring-an-ipsec-host-to-host-vpn-with-raw-rsa-key-authentication .title}

A host-to-host VPN establishes a direct, secure, and encrypted connection between two devices, allowing applications to communicate safely over an insecure network, such as the internet.

For authentication, RSA keys are more secure than pre-shared keys (PSKs) because their asymmetric encryption eliminates the risk of a shared secret. Using RSA keys also simplifies deployment by avoiding the need for a certificate authority (CA), and provides strong peer-to-peer authentication.

Perform the steps on both hosts.

**Procedure**

1.  If Libreswan is not yet installed, perform the following steps:

    a.  Install the `libreswan`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install libreswan
        ```

    b.  Initialize the Network Security Services (NSS) database:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec initnss
        ```

        The command creates the database in the `/var/lib/ipsec/nss/`{.literal} directory.

    c.  Enable and start the `ipsec`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now ipsec
        ```

    d.  Open the IPsec ports and protocols in the firewall:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service="ipsec"
        # firewall-cmd --reload
        ```

2.  Create an RSA key pair:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec newhostkey
    ```

    The `ipsec`{.literal} utility stores the key pair in the NSS database.

3.  Designate your peers. In an IPsec tunnel, you must designate one host as *left* and the other as *right*. This is an arbitrary choice. A common practice is to call your local host *left* and the remote host *right*.

4.  Display the Certificate Key Attribute ID (CKAID) on both the left and right peer:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec showhostkey --list
    < 1> RSA keyid: <key_id> ckaid: <ckaid>
    ```

    You require the CKAIDs of both peers in the next steps.

5.  Display the public keys:

    a.  On the left peer, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec showhostkey --left --ckaid <ckaid_of_left_peer>
            # rsakey AwEAAdKCx
            leftrsasigkey=0sAwEAAdKCxpc9db48cehzQiQD...
        ```

    b.  On the right peer, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec showhostkey --right --ckaid <ckaid_of_right_peer>
            # rsakey AwEAAcNWC
            rightrsasigkey=0sAwEAAcNWCzZO+PR1j8WbO8X...
        ```

    The commands display the public keys with the corresponding parameters that you must use in the configuration file.

6.  Create a `.conf`{.literal} file for the connection in the `/etc/ipsec.d/`{.literal} directory. For example, create the `/etc/ipsec.d/host-to-host.conf`{.literal} file with the following settings:

    ``` {.language-bash tabindex="-1"}
    conn <connection_name>
        # General setup and authentication type
        auto=start
        authby=rsasig

        # Peer A
        left=<ip_address_or_fqdn_of_left_peer>
        leftid=@peer_a
        leftrsasigkey=<public_key_of_left_peer>

        # Peer B
        right=<ip_address_or_fqdn_of_right_peer>
        rightid=@peer_b
        rightrsasigkey=<public_key_of_right_peer>
    ```

    Note

    You can use the same configuration file on both hosts, and Libreswan identifies whether it is operating on the left or right host by using internal information. However, it is important that all values in `left*`{.literal} parameters belong to one peer and the values in `right*`{.literal} parameters belong to the other.

    The settings specified in the example include the following:

    `conn `{.literal}*`<connection_name>`{.literal}*
    :   Defines the connection name. The name is arbitrary, and Libreswan uses it to identify the connection. You must indent parameters in this connection by at least one space or tab.

    `auto=`{.literal}*`<type>`{.literal}*
    :   Controls how the connection is initiated. If you set the value to `start`{.literal}, Libreswan activates the connection automatically when the service starts.

    `authby=rsasig`{.literal}
    :   Enables RSA signature authentication for this connection.

    `left=`{.literal}*`<ip_address_or_fqdn_of_left_peer>`{.literal}* and `right=`{.literal}*`<ip_address_or_fqdn_of_right_peer>`{.literal}*
    :   Defines the IP address or DNS name of the peers.

    `leftid=`{.literal}*`<id>`{.literal}* and `rightid=`{.literal}*`<id>`{.literal}*
    :   Defines how each peer is identified during the Internet Key Exchange (IKE) negotiation process. This can be a fully-qualified domain name (FQDN), an IP address, or a literal string. In the latter case, precede the string with an `@`{.literal} sign.

    `leftrsasigkey=`{.literal}*`<public_key>`{.literal}* and `rightrsasigkey=`{.literal}*`<public_key>`{.literal}*
    :   Specifies the public key of the peers. Use the values displayed by the `ipsec showhostkey`{.literal} command in a previous step.

7.  Restart the `ipsec`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart ipsec
    ```

    If you use `auto=start`{.literal} in the configuration file, the connection is automatically activated. With other methods, additional steps are required to activate the connection. For details, see the `ipsec.conf(5)`{.literal} man page on your system.

**Verification**

-   Display the IPsec status:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec status
    ```

    If the connection is successfully established, the output contains lines as follows:

    -   Phase 1 of an Internet Key Exchange version 2 (IKEv2) negotiation has been successfully completed:

        ``` {.language-plaintext tabindex="-1"}
        #1: "<connection_name>":500 ESTABLISHED_IKE_SA (established IKE SA); REKEY in 28523s; REPLACE in 28793s; newest; idle;
        ```

        The Security Association (SA) is now ready to negotiate the actual data encryption tunnels, known as child SAs or Phase 2 SAs.

    -   A child SA has been established:

        ``` {.language-plaintext tabindex="-1"}
        #2: "<connection_name>":500 ESTABLISHED_CHILD_SA (established Child SA); REKEY in 28523s; REPLACE in 28793s; newest; eroute owner; IKE SA #1; idle;
        ```

        This is the actual tunnel that your data traffic flows through.

**Troubleshooting**

-   If the connection fails to establish, check the IPsec logs on both peers:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u ipsec -n 50
    ```

-   If the firewall blocks IPsec traffic, verify that the IPsec service is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-services | grep ipsec
    ```

    The firewall must allow ESP protocol (IP protocol 50) and UDP ports 500 and 4500.

-   If authentication fails due to key mismatch, verify that the public keys in the configuration file match the output from `ipsec showhostkey`{.literal} on each peer. The `leftrsasigkey`{.literal} value on one peer must match the `rightrsasigkey`{.literal} value on the other peer.

-   If the NSS database has permission issues, verify the database files have correct ownership and SELinux contexts:

    ``` {.language-plaintext tabindex="-1"}
    # ls -lZ /var/lib/ipsec/nss/
    -rw-r--r--. root root system_u:object_r:ipsec_key_file_t:s0 cert9.db
    -rw-r--r--. root root system_u:object_r:ipsec_key_file_t:s0 key4.db
    ```

**Next steps**

-   If you use this host in a network with DHCP or Stateless Address Autoconfiguration (SLAAC), the connection can be vulnerable to being redirected. For details and mitigation steps, see [Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel](#assigning-a-vpn-connection-to-a-dedicated-routing-table-to-prevent-the-connection-from-bypassing-the-tunnel_ipsec "6.11. Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel").

### [6.4. Manually configuring an IPsec site-to-site VPN with raw RSA key authentication](#manually-configuring-an-ipsec-site-to-site-vpn-with-raw-rsa-key-authentication) {#manually-configuring-an-ipsec-site-to-site-vpn-with-raw-rsa-key-authentication .title}

A site-to-site VPN establishes a secure, encrypted tunnel between two distinct networks, linking them across an insecure public network such as the internet.

For example, a site-to-site VPN enables devices in a branch office to access resources at a corporate headquarters as if they were all part of the same local network.

For authenticating the gateway devices, RSA keys are more secure than pre-shared keys (PSKs) because their asymmetric encryption eliminates the risk of a shared secret. Using RSA keys also simplifies deployment by avoiding the need for a certificate authority (CA), and provides strong peer-to-peer authentication.

Perform the steps on both gateway devices.

**Prerequisites**

-   Routes in both networks ensure that the traffic to the remote networks is sent through the local VPN gateway devices.

**Procedure**

1.  If Libreswan is not yet installed, perform the following steps:

    a.  Install the `libreswan`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install libreswan
        ```

    b.  Initialize the Network Security Services (NSS) database:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec initnss
        ```

        The command creates the database in the `/var/lib/ipsec/nss/`{.literal} directory.

    c.  Enable and start the `ipsec`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now ipsec
        ```

    d.  Open the IPsec ports and protocols in the firewall:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service="ipsec"
        # firewall-cmd --reload
        ```

2.  Create an RSA key pair:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec newhostkey
    ```

    The `ipsec`{.literal} utility stores the key pair in the NSS database.

3.  Designate your peers. In an IPsec tunnel, you must designate one host as *left* and the other as *right*. This is an arbitrary choice. A common practice is to call your local host *left* and the remote host *right*.

4.  Display the Certificate Key Attribute ID (CKAID) on both the left and right peer:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec showhostkey --list
    < 1> RSA keyid: <key_id> ckaid: <ckaid>
    ```

    You require the CKAIDs of both peers in the next steps.

5.  Display the public keys:

    a.  On the left peer, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec showhostkey --left --ckaid <ckaid_of_left_peer>
            # rsakey AwEAAdKCx
            leftrsasigkey=0sAwEAAdKCxpc9db48cehzQiQD...
        ```

    b.  On the right peer, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec showhostkey --right --ckaid <ckaid_of_right_peer>
            # rsakey AwEAAcNWC
            rightrsasigkey=0sAwEAAcNWCzZO+PR1j8WbO8X...
        ```

    The commands display the public keys with the corresponding parameters that you must use in the configuration file.

6.  Create a `.conf`{.literal} file for the connection in the `/etc/ipsec.d/`{.literal} directory. For example, create the `/etc/ipsec.d/site-to-site.conf`{.literal} file with the following settings:

    ``` {.language-bash tabindex="-1"}
    conn <connection_name>
        # General setup and authentication type
        auto=start
        authby=rsasig

        # Site A
        left=<ip_address_or_fqdn_of_left_peer>
        leftid=@site_a
        leftrsasigkey=<public_key_of_left_peer>
        leftsubnet=192.0.2.0/24

        # Site B
        right=<ip_address_or_fqdn_of_right_peer>
        rightid=@site_b
        rightrsasigkey=<public_key_of_right_peer>
        rightsubnet={198.51.100.0/24, 203.0.113.0/24}
    ```

    Note

    You can use the same configuration file on both gateway devices, and Libreswan identifies whether it is operating on the left or right host by using internal information. However, it is important that all values in `left*`{.literal} parameters belong to one peer and the values in `right*`{.literal} parameters belong to the other.

    The settings specified in the example include the following:

    `conn `{.literal}*`<connection_name>`{.literal}*
    :   Defines the connection name. The name is arbitrary, and Libreswan uses it to identify the connection. You must indent parameters in this connection by at least one space or tab.

    `auto=`{.literal}*`<type>`{.literal}*
    :   Controls how the connection is initiated. If you set the value to `start`{.literal}, Libreswan activates the connection automatically when the service starts.

    `authby=rsasig`{.literal}
    :   Enables RSA signature authentication for this connection.

    `left=`{.literal}*`<ip_address_or_fqdn_of_left_peer>`{.literal}* and `right=`{.literal}*`<ip_address_or_fqdn_of_right_peer>`{.literal}*
    :   Defines the IP address or DNS name of the peers.

    `leftid=`{.literal}*`<id>`{.literal}* and `rightid=`{.literal}*`<id>`{.literal}*
    :   Defines how each peer is identified during the Internet Key Exchange (IKE) negotiation process. This can be a fully-qualified domain name (FQDN), an IP address, or a literal string. In the latter case, precede the string with an `@`{.literal} sign.

    `leftrsasigkey=`{.literal}*`<public_key>`{.literal}* and `rightrsasigkey=`{.literal}*`<public_key>`{.literal}*
    :   Specifies the public key of the peers. Use the values displayed by the `ipsec showhostkey`{.literal} command in a previous step.

    `leftsubnet=`{.literal}*`<subnet>`{.literal}* and `rightsubnet=`{.literal}*`<subnet>`{.literal}*
    :   Defines subnets in classless inter-domain routing (CIDR) format that are connected through the tunnel. If you want to tunnel multiple subnets on one side, specify them in curly brackets and separate them with a comma.

7.  Enable packet forwarding:

    ``` {.language-plaintext tabindex="-1"}
    # echo "net.ipv4.ip_forward=1" > /etc/sysctl.d/95-IPv4-forwarding.conf
    # sysctl -p /etc/sysctl.d/95-IPv4-forwarding.conf
    ```

8.  Restart the `ipsec`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart ipsec
    ```

    If you use `auto=start`{.literal} in the configuration file, the connection is automatically activated. With other methods, additional steps are required to activate the connection. For details, see the `ipsec.conf(5)`{.literal} man page on your system.

**Verification**

1.  Display the IPsec status:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec status
    ```

    If the connection is successfully established, the output contains lines as follows:

    -   Phase 1 of an Internet Key Exchange version 2 (IKEv2) negotiation has been successfully completed:

        ``` {.language-plaintext tabindex="-1"}
        #2: "<connection_name>":500 ESTABLISHED_IKE_SA (established IKE SA); REKEY in 28523s; REPLACE in 28793s; newest; idle;
        ```

        The Security Association (SA) is now ready to negotiate the actual data encryption tunnels, known as child SAs or Phase 2 SAs.

    -   A child SA has been established:

        ``` {.language-plaintext tabindex="-1"}
        #3: "<connection_name>":500 ESTABLISHED_CHILD_SA (established Child SA); REKEY in 28523s; REPLACE in 28793s; newest; eroute owner; IKE SA #2; idle;
        ```

        This is the actual tunnel that your data traffic flows through.

2.  From a client in the local subnet, ping a client in the remote subnet.

**Troubleshooting**

-   If the connection fails to establish, check the IPsec logs on both peers:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u ipsec -n 50
    ```

-   If the firewall blocks IPsec traffic, verify that the IPsec service is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-services | grep ipsec
    ```

    The firewall must allow ESP protocol (IP protocol 50) and UDP ports 500 and 4500.

-   If authentication fails due to key mismatch, verify that the public keys in the configuration file match the output from `ipsec showhostkey`{.literal} on each peer. The `leftrsasigkey`{.literal} value on one peer must match the `rightrsasigkey`{.literal} value on the other peer.

-   If the connection establishes but traffic does not flow, verify that packet forwarding is enabled on both gateways:

    ``` {.language-plaintext tabindex="-1"}
    # sysctl net.ipv4.ip_forward
    net.ipv4.ip_forward = 1
    ```

-   If Phase 1 (IKE SA) succeeds but Phase 2 (Child SA) fails, verify that the subnet definitions in `leftsubnet`{.literal} and `rightsubnet`{.literal} match the actual network configuration on both peers.

**Next steps**

-   If you use this host in a network with DHCP or Stateless Address Autoconfiguration (SLAAC), the connection can be vulnerable to being redirected. For details and mitigation steps, see [Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel](#assigning-a-vpn-connection-to-a-dedicated-routing-table-to-prevent-the-connection-from-bypassing-the-tunnel_ipsec "6.11. Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel").

### [6.5. Manually configuring an IPsec host-to-site VPN with certificate-based authentication](#manually-configuring-an-ipsec-host-to-site-vpn-with-certificate-based-authentication) {#manually-configuring-an-ipsec-host-to-site-vpn-with-certificate-based-authentication .title}

A host-to-site VPN creates a secure, encrypted connection between a remote computer and a private network. This links them across a public network such as the internet.

Remote employees use host-to-site VPNs to access their company's internal network. They can access resources from their computer as if they were in the office.

For authentication, use digital certificates managed by a Certificate Authority (CA). This provides a secure and scalable solution. Each host and the gateway presents a certificate signed by a trusted CA. This method provides strong authentication and simplifies user management. You can grant or revoke access centrally at the CA. Libreswan checks each certificate against a certificate revocation list (CRL). If a certificate is on the list, Libreswan denies access.

#### [6.5.1. Setting up an IPsec gateway manually](#setting-up-an-ipsec-gateway-manually) {#setting-up-an-ipsec-gateway-manually .title}

You must configure the Libreswan IPsec gateway properly to enable secure remote access. Libreswan reads the server certificate, private key, and CA certificate from a Network Security Services (NSS) database.

The following example permits authenticated clients to access the internal 192.0.2.0/24 subnet and dynamically assigns an IP address from a virtual IP pool to each client. To maintain security, the gateway verifies that client certificates are issued by the same trusted CA and automatically uses a certificate revocation list (CRL) to ensure access is denied for any revoked certificates.

**Prerequisites**

-   The Public Key Cryptography Standards #12 (PKCS #12) file `~/file.p12`{.literal} exists on the gateway with the following contents:

    -   The private key of the server
    -   The server certificate
    -   The CA certificate
    -   If required, intermediate certificates

    For details about creating a private key and certificate signing request (CSR), as well as about requesting a certificate from a CA, see your CA's documentation.

-   The server certificate contains the following fields:

    -   Extended Key Usage (EKU) is set to `TLS Web Server Authentication`{.literal}.
    -   Common Name (CN) or Subject Alternative Name (SAN) is set to the fully-qualified domain name (FQDN) of the gateway.
    -   X509v3 CRL distribution points contain URLs to Certificate Revocation Lists (CRLs).

-   A return route for VPN client traffic is configured on the internal network, pointing to the VPN gateway.

**Procedure**

1.  If Libreswan is not yet installed:

    a.  Install the `libreswan`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install libreswan
        ```

    b.  Initialize the Network Security Services (NSS) database:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec initnss
        ```

        The command creates the database in the `/var/lib/ipsec/nss/`{.literal} directory.

    c.  Enable and start the `ipsec`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now ipsec
        ```

    d.  Open the IPsec ports and protocols in the firewall:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service="ipsec"
        # firewall-cmd --reload
        ```

2.  Import the PKCS #12 file into the NSS database:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec import ~/file.p12
    Enter password for PKCS12 file: <password>
    pk12util: PKCS12 IMPORT SUCCESSFUL
    correcting trust bits for Example-CA
    ```

3.  Display the nicknames of the server and CA certificates:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -L -d /var/lib/ipsec/nss/
    Certificate Nickname     Trust Attributes
                             SSL,S/MIME,JAR/XPI

    vpn-gateway              u,u,u
    Example-CA               CT,,
    ...
    ```

    You need this information for the configuration file.

4.  Create a `.conf`{.literal} file for the connection in the `/etc/ipsec.d/`{.literal} directory. For example, create the `/etc/ipsec.d/host-to-site.conf`{.literal} file with the following settings:

    a.  Add a `config setup`{.literal} section to enable CRL checks:

        ``` {.language-bash tabindex="-1"}
        config setup
            crl-strict=yes
            crlcheckinterval=1h
        ```

        The settings specified in the example include the following:

        `crl-strict=yes`{.literal}
        :   Enables CRL checks. Authenticating clients are rejected if no CRL is available in the NSS database.

        `crlcheckinterval=1h`{.literal}
        :   Re-fetches the CRL from the URL specified in the server's certificate after the specified period.

    b.  Add a section for the gateway:

        ``` {.language-bash tabindex="-1"}
        conn <connection_name>
            # General setup and authentication type
            auto=start
            ikev2=insist
            authby=rsasig

            # VPN gateway settings
            left=%defaultroute
            leftid=%fromcert
            leftcert="<server_certificate_nickname>"
            leftrsasigkey=%cert
            leftsendcert=always
            leftsubnet=192.0.2.0/24
            rekey=no
            mobike=yes
            narrowing=yes

            # Client-related settings
            right=%any
            rightid=%fromcert
            rightrsasigkey=%cert
            rightaddresspool=198.51.100.129-198.51.100.254
            rightmodecfgclient=yes
            modecfgclient=yes
            modecfgdns=192.0.2.5
            modecfgdomains="example.com"

            # Dead Peer Detection
            dpddelay=30
            dpdtimeout=120
            dpdaction=clear
        ```

        The settings specified in the example include the following:

        `ikev2=insist`{.literal}
        :   Defines the modern IKEv2 protocol as the only allowed protocol without fallback to IKEv1.

        `left=%defaultroute`{.literal}
        :   Dynamically sets the IP address of the default route interface when the `ipsec`{.literal} service starts. Alternatively, you can set the `left`{.literal} parameter to the IP address or the FQDN of the host.

        `leftid=%fromcert`{.literal} and `rightid=%fromcert`{.literal}
        :   Configures Libreswan to retrieve the identity from the distinguished name (DN) field of the certificate.

        `leftcert="`{.literal}*`<server_certificate_nickname>`{.literal}*`"`{.literal}
        :   Sets the nickname of the server's certificate used in the NSS database.

        `leftrsasigkey=%cert`{.literal} and `rightrsasigkey=%cert`{.literal}
        :   Configures Libreswan to use the RSA public key embedded in the certificate.

        `leftsendcert=always`{.literal}
        :   Instructs the gateway to always send the certificate, so that clients can validate it against the CA certificate.

        `leftsubnet=`{.literal}*`<subnets>`{.literal}*
        :   Specifies the subnets connected to the gateway that clients can access through the tunnel.

        `mobike=yes`{.literal}
        :   Enables clients to roam among networks.

        `rightaddresspool=`{.literal}*`<ip_range>`{.literal}*
        :   Specifies from which range the gateway can assign IP addresses to the clients.

        `modecfgclient=yes`{.literal}
        :   Enables clients to receive the DNS server IP set in the `modecfgdns`{.literal} parameter and the DNS search domain set in `modecfgdomains`{.literal}.

    For details about all parameters used in the example, see the `ipsec.conf(5)`{.literal} man page on your system.

5.  Enable packet forwarding:

    ``` {.language-plaintext tabindex="-1"}
    # echo "net.ipv4.ip_forward=1" > /etc/sysctl.d/95-IPv4-forwarding.conf
    # sysctl -p /etc/sysctl.d/95-IPv4-forwarding.conf
    ```

6.  Restart the `ipsec`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart ipsec
    ```

    If you use `auto=start`{.literal} in the configuration file, the connection is automatically activated. With other methods, additional steps are required to activate the connection. For details, see the `ipsec.conf(5)`{.literal} man page on your system.

**Verification**

1.  [Configure a client and connect to the VPN gateway](#configuring-a-client-to-connect-to-an-ipsec-vpn-gateway-by-using-gnome-settings "6.5.2. Configuring a client to connect to an IPsec VPN gateway by using GNOME Settings").

2.  Check if the service loaded the CRL and added the entries to the NSS database:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec listcrls

    List of CRLs:

    issuer: CN=Example-CA
    revoked certs: 1
    updates: this Tue Jul 15 10:22:36 2025
             next Sun Jan 11 10:22:36 2026

    List of CRL fetch requests:

    Jul 15 15:13:56 2025, trials: 1
           issuer:  'CN=Example-CA'
           distPts: 'https://ca.example.com/crl.pem'
    ```

**Troubleshooting**

-   If clients cannot connect to the gateway, check the IPsec logs:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u ipsec -n 50
    ```

-   If the firewall blocks IPsec traffic, verify that the IPsec service is enabled in `firewalld`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-services
    ipsec
    ```

    If the service is not listed, add it:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service="ipsec"
    # firewall-cmd --reload
    ```

-   If certificate validation fails, verify that the CA certificate is imported and trusted in the NSS database:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -L -d /var/lib/ipsec/nss/
    Certificate Nickname     Trust Attributes
                             SSL,S/MIME,JAR/XPI

    Example-CA               CT,,
    ```

    The CA certificate trust attributes must include `C`{.literal} for certificate authority trust.

-   If CRL download fails, check network connectivity to the CRL distribution point URL specified in the server certificate, and verify that the URL is accessible from the gateway.

-   If the NSS database has permission issues, verify the database files are owned by root with correct SELinux contexts:

    ``` {.language-plaintext tabindex="-1"}
    # ls -lZ /var/lib/ipsec/nss/
    -rw-r--r--. root root system_u:object_r:ipsec_key_file_t:s0 cert9.db
    -rw-r--r--. root root system_u:object_r:ipsec_key_file_t:s0 key4.db
    -rw-r--r--. root root system_u:object_r:ipsec_key_file_t:s0 pkcs11.txt
    ```

**Next steps**

-   Configure firewall rules to ensure that clients can only communicate with required resources. For details about firewalls, see [Configuring firewalls and packet filters](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/index).

#### [6.5.2. Configuring a client to connect to an IPsec VPN gateway by using GNOME Settings](#configuring-a-client-to-connect-to-an-ipsec-vpn-gateway-by-using-gnome-settings) {#configuring-a-client-to-connect-to-an-ipsec-vpn-gateway-by-using-gnome-settings .title}

To access resources on a remote private network, users must first configure an IPsec VPN connection. The GNOME Settings application provides a graphical solution to create an IPsec VPN connection profile in NetworkManager and to establish the tunnel.

**Prerequisites**

-   [You configured the IPsec VPN gateway](#setting-up-an-ipsec-gateway-manually "6.5.1. Setting up an IPsec gateway manually").

-   The `NetworkManager-libreswan-gnome`{.literal} package is installed.

-   The PKCS #12 file `~/file.p12`{.literal} exists on the client with the following contents:

    -   The private key of the user
    -   The user certificate
    -   The CA certificate
    -   If required, intermediate certificates

    For details about creating a private key and certificate signing request (CSR), as well as about requesting a certificate from a CA, see your CA's documentation.

-   The Extended Key Usage (EKU) in the certificate is set to `TLS Web Client Authentication`{.literal}.

**Procedure**

1.  Initialize the Network Security Services (NSS) database:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec initnss
    ```

    The command creates the database in the `/var/lib/ipsec/nss/`{.literal} directory.

2.  Import the PKCS #12 file into the NSS database:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec import ~/file.p12
    Enter password for PKCS12 file: <password>
    pk12util: PKCS12 IMPORT SUCCESSFUL
    correcting trust bits for Example-CA
    ```

3.  Display the nicknames of the user and CA certificates:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -L -d /var/lib/ipsec/nss/
    Certificate Nickname     Trust Attributes
                             SSL,S/MIME,JAR/XPI

    user                     u,u,u
    Example-CA               CT,,
    ...
    ```

    You require this information in the configuration file.

4.  Press the Super key, type **Settings**, and press Enter to open the GNOME **Settings** application.

5.  Click the + button next to the **VPN** entry.

6.  Select **IPsec based VPN** from the list.

7.  On the **Identity** tab, fill the fields as follows:

    +----------------------+---------------------------------------------------+------------------------------------------------+
    | Field name           | Value                                             | Corresponding `ipsec.conf`{.literal} parameter |
    +:=====================+:==================================================+:===============================================+
    | **Name**             | *`<networkmanager_profile_name>`{.literal}*       | N/A                                            |
    +----------------------+---------------------------------------------------+------------------------------------------------+
    | **Gateway**          | *`<ip_address_or_fqdn_of_the_gateway>`{.literal}* | `right`{.literal}                              |
    +----------------------+---------------------------------------------------+------------------------------------------------+
    | **Type**             | `IKEv2 (certificate)`{.literal}                   | `authby`{.literal}                             |
    +----------------------+---------------------------------------------------+------------------------------------------------+
    | **Group name**       | `%fromcert`{.literal}                             | `leftid`{.literal}                             |
    +----------------------+---------------------------------------------------+------------------------------------------------+
    | **Certificate name** | *`<user_certificate_nickname>`{.literal}*         | `leftcert`{.literal}                           |
    +----------------------+---------------------------------------------------+------------------------------------------------+
    | **Remote ID**        | `%fromcert`{.literal}                             | `rightid`{.literal}                            |
    +----------------------+---------------------------------------------------+------------------------------------------------+

    : Table 6.1. Identity tab settings

    Show more

8.  Click **Advanced**.

9.  In the **Advanced properties** window, fill the fields of the **Connectivity** tab as follows:

    +----------------------+-----------------------------------+------------------------------------------------+
    | Field name           | Value                             | Corresponding `ipsec.conf`{.literal} parameter |
    +:=====================+:==================================+:===============================================+
    | **Remote Network**   | `192.0.2.0/24`{.literal}          | `rightsubnet`{.literal}                        |
    +----------------------+-----------------------------------+------------------------------------------------+
    | **Narrowing**        | Selected                          | `narrowing`{.literal}                          |
    +----------------------+-----------------------------------+------------------------------------------------+
    | **Enable MOBIKE**    | `yes`{.literal}                   | `mobike`{.literal}                             |
    +----------------------+-----------------------------------+------------------------------------------------+
    | **Delay**            | `30`{.literal}                    | `dpddelay`{.literal}                           |
    +----------------------+-----------------------------------+------------------------------------------------+
    | **Timeout**          | `120`{.literal}                   | `dpdtimeout`{.literal}                         |
    +----------------------+-----------------------------------+------------------------------------------------+
    | **Action**           | `Clear`{.literal}                 | `dpdaction`{.literal}                          |
    +----------------------+-----------------------------------+------------------------------------------------+

    : Table 6.2. Connectivity tab settings

    Show more

10. Click Apply to return to the connection settings.

11. Click Apply to save the connection.

12. In the **Network** tab of the **Settings** application, toggle the switch next to the VPN profile to activate the connection.

**Verification**

-   Establish a connection to a host in the remote network or ping it.

**Next steps**

-   If you use this host in a network with DHCP or Stateless Address Autoconfiguration (SLAAC), the connection can be vulnerable to being redirected. For details and mitigation steps, see [Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel](#assigning-a-vpn-connection-to-a-dedicated-routing-table-to-prevent-the-connection-from-bypassing-the-tunnel_ipsec "6.11. Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel").

### [6.6. Manually configuring an IPsec mesh VPN with certificate-based authentication](#manually-configuring-an-ipsec-mesh-vpn-with-certificate-based-authentication) {#manually-configuring-an-ipsec-mesh-vpn-with-certificate-based-authentication .title}

An IPsec mesh creates a fully interconnected network where every server can communicate securely and directly with every other server. This is ideal for distributed database clusters or high-availability environments that span multiple data centers or cloud providers.

Establishing a direct, encrypted tunnel between each pair of servers ensures secure communication without a central bottleneck. For authentication, using digital certificates managed by a Certificate Authority (CA) offers a secure and scalable solution. Each host in the mesh presents a certificate signed by a trusted CA. This method provides strong, verifiable authentication and simplifies user management. Access can be granted or revoked centrally at the CA, and Libreswan enforces this by checking each certificate against a certificate revocation list (CRL), denying access if a certificate appears on the list.

**Prerequisites**

-   A Public Key Cryptography Standards #12 (PKCS #12) file exists on each peer in the mesh with the following contents:

    -   The private key of the server
    -   The server certificate
    -   The CA certificate
    -   If required, intermediate certificates

    For details about creating a private key and certificate signing request (CSR), as well as about requesting a certificate from a CA, see your CA's documentation.

-   The server certificate contains the following fields:

    -   Extended Key Usage (EKU) is set to `TLS Web Server Authentication`{.literal}.
    -   Common Name (CN) or Subject Alternative Name (SAN) is set to the fully-qualified domain name (FQDN) of the host.
    -   X509v3 CRL distribution points contain URLs to Certificate Revocation Lists (CRLs).

**Procedure**

1.  If Libreswan is not yet installed, perform the following steps:

    a.  Install the `libreswan`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install libreswan
        ```

    b.  Initialize the Network Security Services (NSS) database:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec initnss
        ```

        The command creates the database in the `/var/lib/ipsec/nss/`{.literal} directory.

    c.  Enable and start the `ipsec`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now ipsec
        ```

    d.  Open the IPsec ports and protocols in the firewall:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service="ipsec"
        # firewall-cmd --reload
        ```

2.  Import the PKCS #12 file into the NSS database:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec import <file>.p12
    Enter password for PKCS12 file: <password>
    pk12util: PKCS12 IMPORT SUCCESSFUL
    correcting trust bits for Example-CA
    ```

3.  Display the nicknames of the server and CA certificates:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -L -d /var/lib/ipsec/nss/
    Certificate Nickname     Trust Attributes
                             SSL,S/MIME,JAR/XPI

    server1                  u,u,u
    Example-CA               CT,,
    ...
    ```

    You need this information for the configuration file.

4.  Create a `.conf`{.literal} file for the connection in the `/etc/ipsec.d/`{.literal} directory. For example, create the `/etc/ipsec.d/mesh.conf`{.literal} file with the following settings:

    a.  Add a `config setup`{.literal} section to enable CRL checks:

        ``` {.language-bash tabindex="-1"}
        config setup
            crl-strict=yes
            crlcheckinterval=1h
        ```

        The settings specified in the example include the following:

        `crl-strict=yes`{.literal}
        :   Enables CRL checks. Authenticating peers are rejected if no CRL is available in the NSS database.

        `crlcheckinterval=1h`{.literal}
        :   Re-fetches the CRL from the URL specified in the server's certificate after the specified period.

    b.  Add a section that enforces traffic among members in the mesh:

        ``` {.language-bash tabindex="-1"}
        conn <connection_name>
            # General setup and authentication type
            auto=ondemand
            authby=rsasig

            # Local settings settings
            left=%defaultroute
            leftid=%fromcert
            leftcert="<server_certificate_nickname>"
            leftrsasigkey=%cert
            leftsendcert=always
            failureshunt=drop
            type=transport

            # Settings related to other peers in the mesh
            right=%opportunisticgroup
            rightid=%fromcert
        ```

        The settings specified in the example include the following:

        `left=%defaultroute`{.literal}
        :   Dynamically sets the IP address of the default route interface when the `ipsec`{.literal} service starts. Alternatively, you can set the `left`{.literal} parameter to the IP address or the FQDN of the host.

        `leftid=%fromcert`{.literal} and `rightid=%fromcert`{.literal}
        :   Configures Libreswan to retrieve the identity from the distinguished name (DN) field of the certificate.

        `leftcert="`{.literal}*`<server_certificate_nickname>`{.literal}*`"`{.literal}
        :   Sets the nickname of the server's certificate used in the NSS database.

        `leftrsasigkey=%cert`{.literal}
        :   Configures Libreswan to use the RSA public key embedded in the certificate.

        `leftsendcert=always`{.literal}
        :   Instructs the peer to always send the certificate, so that peers can validate it against the CA certificate.

        `failureshunt=drop`{.literal}
        :   Enforces encryption and drops traffic if IPsec negotiation fails. This is critical for a secure mesh.

        `right=%opportunisticgroup`{.literal}
        :   Specifies that the connection should apply to a dynamic group of remote peers defined in a policy file. This enables Libreswan to instantiate IPsec tunnels opportunistically for each listed IP or subnet in that group.

    For details about all parameters used in the example, see the `ipsec.conf(5)`{.literal} man page on your system.

5.  Create the `/etc/ipsec.d/policies/server-mesh`{.literal} policy file that specifies the peers or subnets in classless inter-domain routing (CIDR) format:

    ``` {.language-bash tabindex="-1"}
    192.0.2.0/24
    198.51.100.0/24
    ```

    With these settings, the `ipsec`{.literal} service encrypts traffic between hosts in these subnets. If a host is not configured as a member of the IPsec mesh, communication between this host and the mesh members fails.

6.  Restart the `ipsec`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart ipsec
    ```

7.  Repeat the procedure on every host in the subnets you specified in the policy file.

**Verification**

1.  Send traffic to a host in the mesh to establish the tunnel. For example, ping the host:

    ``` {.language-plaintext tabindex="-1"}
    # ping -c3 <peer_in_mesh>
    ```

2.  Display the IPsec status:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec status
    ```

    If the connection is successfully established, the output contains lines as follows for the peer:

    -   Phase 1 of an Internet Key Exchange version 2 (IKEv2) negotiation has been successfully completed:

        ``` {.language-plaintext tabindex="-1"}
        #1: "<connection_name>#192.0.2.0/24"[1] ...192.0.2.2:500 ESTABLISHED_IKE_SA (established IKE SA); REKEY in 12822s; REPLACE in 13875s; newest; idle;
        ```

        The Security Association (SA) is now ready to negotiate the actual data encryption tunnels, known as child SAs or Phase 2 SAs.

    -   A child SA has been established:

        ``` {.language-plaintext tabindex="-1"}
        #2: "<connection_name>#192.0.2.0/24"[1] ...192.0.2.2:500 ESTABLISHED_CHILD_SA (established Child SA); REKEY in 13071s; REPLACE in 13875s; newest; eroute owner; IKE SA #1; idle;
        ```

        This is the actual tunnel that your data traffic flows through.

3.  Check if the service loaded the CRL and added the entries to the NSS database:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec listcrls

    List of CRLs:

    issuer: CN=Example-CA
    revoked certs: 1
    updates: this Tue Jul 15 10:22:36 2025
             next Sun Jan 11 10:22:36 2026

    List of CRL fetch requests:

    Jul 15 15:13:56 2025, trials: 1
           issuer:  'CN=Example-CA'
           distPts: 'https://ca.example.com/crl.pem'
    ```

**Troubleshooting**

-   If the connection fails to establish, check the IPsec logs:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u ipsec -n 50
    ```

-   If the firewall blocks IPsec traffic, verify that the IPsec service is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-services | grep ipsec
    ```

    The firewall must allow ESP protocol (IP protocol 50) and UDP ports 500 and 4500.

-   If certificate validation fails, verify that the CA certificate is imported and trusted in the NSS database:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -L -d /var/lib/ipsec/nss/
    Certificate Nickname     Trust Attributes
                             SSL,S/MIME,JAR/XPI

    Example-CA               CT,,
    ```

    The CA certificate trust attributes must include `C`{.literal} for certificate authority trust.

-   If CRL download fails, check network connectivity to the CRL distribution point URL specified in the server certificate, and verify that the URL is accessible from all mesh members.

-   If traffic between mesh members is not encrypted despite the configuration, verify that the IP addresses or subnets in the `/etc/ipsec.d/policies/server-mesh`{.literal} file match the actual network addresses of the mesh members.

-   If the NSS database has permission issues, verify the database files are owned by root with correct SELinux contexts:

    ``` {.language-plaintext tabindex="-1"}
    # ls -lZ /var/lib/ipsec/nss/
    -rw-r--r--. root root system_u:object_r:ipsec_key_file_t:s0 cert9.db
    -rw-r--r--. root root system_u:object_r:ipsec_key_file_t:s0 key4.db
    ```

**Next steps**

-   If you use this host in a network with DHCP or Stateless Address Autoconfiguration (SLAAC), the connection can be vulnerable to being redirected. For details and mitigation steps, see [Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel](#assigning-a-vpn-connection-to-a-dedicated-routing-table-to-prevent-the-connection-from-bypassing-the-tunnel_ipsec "6.11. Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel").

### [6.7. Protecting the IPsec NSS database with a password](#protecting-the-ipsec-nss-database-with-a-password) {#protecting-the-ipsec-nss-database-with-a-password .title}

By default, only the root user can access the IPsec Network Security Services (NSS) database in the `/var/lib/ipsec/nss/`{.literal} directory. You can additionally protect the database with a password. This is required if you run RHEL in Federal Information Processing Standard (FIPS) mode.

**Prerequisites**

-   The `/var/lib/ipsec/nss/`{.literal} directory contains the NSS database.

**Procedure**

1.  Enable password protection for the Libreswan NSS database:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -W -d /var/lib/ipsec/nss/
    ```

2.  Enter the current password:

    ``` {.language-plaintext tabindex="-1"}
    Enter Password or Pin for "NSS Certificate DB": <password>
    ```

    If the database is currently not protected by a password, press Enter.

3.  Enter the new password:

    ``` {.language-plaintext tabindex="-1"}
    Enter new password: <new_password>
    Re-enter password: <new_password>
    ```

4.  To unlock the database, the `ipsec`{.literal} service requires the `/etc/ipsec.d/nsspassword`{.literal} file. Create the file with the following content:

    -   If the host does not run in FIPS mode:

        ``` {.language-plaintext tabindex="-1"}
        NSS Certificate DB:<password>
        ```

    -   If the host runs in FIPS mode:

        ``` {.language-plaintext tabindex="-1"}
        NSS FIPS 140-2 Certificate DB:<password>
        ```

5.  Set secure permissions on the `/etc/ipsec.d/nsspassword`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 600 /etc/ipsec.d/nsspassword
    # chown root:root /etc/ipsec.d/nsspassword
    ```

6.  Restart the `ipsec`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart ipsec
    ```

**Verification**

1.  Verify that the `ipsec`{.literal} service is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl is-active ipsec
    ```

    If the command returns `active`{.literal}, the service successfully uses the password file to unlock the NSS database.

2.  Perform an action on the NSS database that requires the password. For example, display the private keys:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -K -d /var/lib/ipsec/nss/
    certutil: Checking token "NSS Certificate DB" in slot "NSS User Private Key and Certificate Services"
    Enter Password or Pin for "NSS Certificate DB":
    ```

    Verify that the command prompts for the password.

### [6.8. Using IPsec on a system with FIPS mode enabled](#using-ipsec-on-a-system-with-fips-mode-enabled) {#using-ipsec-on-a-system-with-fips-mode-enabled .title}

RHEL in Federal Information Processing Standard (FIPS) mode uses only validated crypto modules. FIPS mode disables legacy protocols and ciphers. Federal compliance often requires FIPS mode. It also improves system security.

The Libreswan IPsec tool in RHEL is fully FIPS-compliant. When FIPS mode is on, Libreswan uses the certified crypto modules. You do not need to configure anything. This works whether you install Libreswan on a new FIPS system or enable FIPS on an existing Libreswan VPN.

If FIPS mode is enabled, you can confirm that Libreswan is running in FIPS mode:

``` {.language-plaintext tabindex="-1"}
# ipsec whack --fipsstatus
FIPS mode enabled
```

To list the allowed algorithms and ciphers in Libreswan in FIPS mode, enter:

``` {.language-plaintext tabindex="-1"}
# ipsec pluto --selftest 2>&1
...
FIPS Encryption algorithms:
  AES_CCM_16  {256,192,*128} IKEv1:  ESP  IKEv2:  ESP  FIPS   aes_ccm, aes_ccm_c
  AES_CCM_12  {256,192,*128} IKEv1:  ESP  IKEv2:  ESP  FIPS   aes_ccm_b
  AES_CCM_8   {256,192,*128} IKEv1:  ESP  IKEv2:  ESP  FIPS   aes_ccm_a
...
```

### [6.9. Configuring TCP fallback for an IPsec VPN connection](#configuring-tcp-fallback-for-an-ipsec-vpn-connection) {#configuring-tcp-fallback-for-an-ipsec-vpn-connection .title}

Standard IPsec VPNs can fail on restrictive networks that block the UDP and Encapsulating Security Payload (ESP) protocols. To ensure connectivity in such environments, Libreswan can encapsulate all VPN traffic within a TCP connection.

Important

Encapsulating VPN packets within TCP can reduce throughput and increase latency. For this reason, use TCP encapsulation only as a fallback option or if UDP-based connections are consistently blocked in your environment.

**Prerequisites**

-   The IPsec connection is configured.

**Procedure**

1.  Edit the `/etc/ipsec.conf`{.literal} file, and make the following changes in the `config setup`{.literal} section:

    a.  Configure Libreswan to listen on a TCP port:

        ``` {.language-bash tabindex="-1"}
        listen-tcp=yes
        ```

    b.  By default, Libreswan listens on port 4500. If you want to use a different port, enter:

        ``` {.language-bash tabindex="-1"}
        tcp-remoteport=<port_number>
        ```

    c.  Decide whether to use TCP as a fallback option if UDP is not available or permanently:

        -   As a fallback option, enter:

            ``` {.language-bash tabindex="-1"}
            enable-tcp=fallback
            retransmit-timeout=5s
            ```

            By default, Libreswan waits 60 seconds after a failed attempt to connect by using UDP before retrying the connection over TCP. Lowering the `retransmit-timeout`{.literal} value shortens the delay, enabling the fallback protocol to initiate more quickly.

        -   As a permanent replacement for UDP, enter:

            ``` {.language-bash tabindex="-1"}
            enable-tcp=yes
            ```

2.  Restart the `ipsec`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart ipsec
    ```

3.  If you configured a TCP port other than the default 4500, open the port in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=<tcp_port>/tcp
    # firewall-cmd --reload
    ```

4.  Repeat the procedure on the peers that use this gateway.

### [6.10. Enabling legacy ciphers and algorithms in Libreswan](#enabling-legacy-ciphers-and-algorithms-in-libreswan) {#enabling-legacy-ciphers-and-algorithms-in-libreswan .title}

Enable legacy ciphers and algorithms in Libreswan for backward compatibility with other IPsec peers. This overrides the RHEL system-wide cryptographic policies which, by default, enforce strong encryption ciphers and algorithms for IPsec and Internet Key Exchange (IKE).

The RHEL system-wide cryptographic policies create a special connection called `%default`{.literal}. This connection sets the default values for the `keyexchange`{.literal}, `esp`{.literal}, and `ike`{.literal} parameters.

**Prerequisites**

-   Libreswan is installed.

**Procedure**

1.  To override the defaults set by the RHEL system-wide cryptographic policies, add the `keyexchange`{.literal}, `esp`{.literal}, and `ike`{.literal} parameters to your connection configuration and set them to the values you require. For example:

    ``` {.language-bash tabindex="-1"}
    conn <connection_name>
        keyexchange=ikev1
        ike=aes-sha2,aes-sha1;modp2048
        esp=aes-sha2,aes-sha1
        ...
    ```

2.  Restart the `ipsec`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart ipsec
    ```

### [6.11. Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel](#assigning-a-vpn-connection-to-a-dedicated-routing-table-to-prevent-the-connection-from-bypassing-the-tunnel_ipsec) {#assigning-a-vpn-connection-to-a-dedicated-routing-table-to-prevent-the-connection-from-bypassing-the-tunnel .title}

To protect your VPN connection from traffic redirection attacks, assign it to a dedicated routing table. This prevents malicious network servers from bypassing the secure tunnel and compromising data integrity.

Both a DHCP server and Stateless Address Autoconfiguration (SLAAC) can add routes to a client's routing table. For example, a malicious DHCP server can use this feature to force a host with VPN connection to redirect traffic through a physical interface instead of the VPN tunnel. This vulnerability is also known as TunnelVision and described in the [CVE-2024-3661](https://access.redhat.com/security/cve/cve-2024-3661) vulnerability article.

To mitigate this vulnerability, you can assign the VPN connection to a dedicated routing table. This prevents the DHCP configuration or SLAAC from manipulating routing decisions for network packets intended for the VPN tunnel.

Follow the steps if at least one of the conditions applies to your environment:

-   At least one network interface uses DHCP or SLAAC.
-   Your network does not use mechanisms, such as DHCP snooping, that prevent a rogue DHCP server.

Important

Routing the entire traffic through the VPN prevents the host from accessing local network resources.

**Procedure**

1.  Decide which routing table you want to use. The following steps use table 75. By default, RHEL does not use the tables 1-254, and you can use any of them.

2.  Configure the VPN connection profile to place the VPN routes in a dedicated routing table:

    ``` {.language-plaintext tabindex="-1"}
    # nmcli connection modify <vpn_connection_profile> ipv4.route-table 75 ipv6.route-table 75
    ```

3.  Set a low priority value for the table you used in the previous command:

    ``` {.language-plaintext tabindex="-1"}
    # nmcli connection modify <vpn_connection_profile> ipv4.routing-rules "priority 32345 from all table 75" ipv6.routing-rules "priority 32345 from all table 75"
    ```

    The priority value can be any value between 1 and 32766. The lower the value, the higher the priority.

4.  Reconnect the VPN connection:

    ``` {.language-plaintext tabindex="-1"}
    # nmcli connection down <vpn_connection_profile>
    # nmcli connection up <vpn_connection_profile>
    ```

**Verification**

1.  Display the IPv4 routes in table 75:

    ``` {.language-plaintext tabindex="-1"}
    # ip route show table 75
    ...
    192.0.2.0/24 via 192.0.2.254 dev vpn_device proto static metric 50
    default dev vpn_device proto static scope link metric 50
    ```

    The output confirms that both the route to the remote network and the default gateway are assigned to routing table 75 and, therefore, all traffic is routed through the tunnel. If you set `ipv4.never-default true`{.literal} in the VPN connection profile, a default route is not created and, therefore, not visible in this output.

2.  Display the IPv6 routes in table 75:

    ``` {.language-plaintext tabindex="-1"}
    # ip -6 route show table 75
    ...
    2001:db8:1::/64 dev vpn_device proto kernel metric 50 pref medium
    default dev vpn_device proto static metric 50 pref medium
    ```

    The output confirms that both the route to the remote network and the default gateway are assigned to routing table 75 and, therefore, all traffic is routed through the tunnel. If you set `ipv6.never-default true`{.literal} in the VPN connection profile, a default route is not created and, therefore, not visible in this output.

**Additional resources**

-   [CVE-2024-3661](https://access.redhat.com/security/cve/cve-2024-3661)

### [6.12. Configuring IPsec VPN connections by using RHEL system roles](#configuring-ipsec-vpn-connections-by-using-rhel-system-roles) {#configuring-ipsec-vpn-connections-by-using-rhel-system-roles .title}

Configure IPsec VPN connections to establish encrypted tunnels over untrusted networks and ensure the integrity of data in transit. By using the RHEL system roles, you can automate the setup for use cases, such as connecting branch offices to headquarters.

Note

The `vpn`{.literal} RHEL system role can only create VPN configurations that use pre-shared keys (PSKs) or certificates to authenticate peers to each other.

#### [6.12.1. Configuring an IPsec host-to-host VPN with PSK authentication by using the vpn RHEL system role](#configuring-an-ipsec-host-to-host-vpn-with-psk-authentication-by-using-the-vpn-rhel-system-role) {#configuring-an-ipsec-host-to-host-vpn-with-psk-authentication-by-using-the-vpn-rhel-system-role .title}

A host-to-host VPN establishes an encrypted connection between two devices, allowing applications to communicate safely over an insecure network. By using the `vpn`{.literal} RHEL system role, you can automate the process of creating IPsec host-to-host connections.

For authentication, a pre-shared key (PSK) is a straightforward method that uses a single, shared secret known only to the two peers. This approach is simple to configure and ideal for basic setups where ease of deployment is a priority. However, you must keep the key strictly confidential. An attacker with access to the key can compromise the connection.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configuring VPN
      hosts: managed-node-01.example.com, managed-node-02.example.com
      tasks:
        - name: IPsec VPN with PSK authentication
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.vpn
          vars:
            vpn_connections:
              - hosts:
                  managed-node-01.example.com:
                  managed-node-02.example.com:
                auth_method: psk
                auto: start
            vpn_manage_firewall: true
            vpn_manage_selinux: true
    ```

    The settings specified in the example playbook include the following:

    `hosts: `{.literal}*`<list>`{.literal}*

    :   Defines a YAML dictionary with the peers between which you want to configure a VPN. If an entry is not an Ansible managed node, you must specify its fully-qualified domain name (FQDN) or IP address in the `hostname`{.literal} parameter, for example:

        ``` {.language-yaml tabindex="-1"}
                  ...
                  - hosts:
                      ...
                      external-host.example.com:
                        hostname: 192.0.2.1
        ```

        The role configures the VPN connection on each managed node. The connections are named *`<peer_A>`{.literal}*`-to-`{.literal}*`<peer_B>`{.literal}*, for example, `managed-node-01.example.com-to-managed-node-02.example.com`{.literal}. Note that the role cannot configure Libreswan on external (unmanaged) nodes. You must manually create the configuration on these peers.

    `auth_method: psk`{.literal}
    :   Enables PSK authentication between the peers. The role uses `openssl`{.literal} on the control node to create the PSK.

    `auto: `{.literal}*`<startup_method>`{.literal}*
    :   Specifies the startup method of the connection. Valid values are `add`{.literal}, `ondemand`{.literal}, `start`{.literal}, and `ignore`{.literal}. For details, see the `ipsec.conf(5)`{.literal} man page on a system with Libreswan installed. The default value of this variable is null, which means no automatic startup operation.

    `vpn_manage_firewall: true`{.literal}
    :   Defines that the role opens the required ports in the `firewalld`{.literal} service on the managed nodes.

    `vpn_manage_selinux: true`{.literal}
    :   Defines that the role sets the required SELinux port type on the IPsec ports.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.vpn/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Confirm that the connections are successfully started, for example:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m shell -a 'ipsec trafficstatus | grep "managed-node-01.example.com-to-managed-node-02.example.com"'
    ...
    006 #3: "managed-node-01.example.com-to-managed-node-02.example.com", type=ESP, add_time=1741857153, inBytes=38622, outBytes=324626, maxBytes=2^63B, id='@managed-node-02.example.com'
    ```

    Note that this command only succeeds if the VPN connection is active. If you set the `auto`{.literal} variable in the playbook to a value other than `start`{.literal}, you might need to manually activate the connection on the managed nodes first.

**Troubleshooting**

-   If the playbook fails with syntax errors, validate the YAML structure:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

-   If managed nodes are unreachable, verify SSH connectivity and authentication:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m ping
    ```

-   If the playbook completes but the VPN connection does not establish, check the IPsec logs on the managed nodes:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m shell -a 'journalctl -u ipsec -n 50'
    ```

-   For detailed output during playbook execution, run with verbose mode:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook -vvv ~/playbook.yml
    ```

-   If the firewall blocks connections despite `vpn_manage_firewall: true`{.literal}, verify that `firewalld`{.literal} is running on the managed nodes and that the IPsec service was added to the active zone.

#### [6.12.2. Configuring an IPsec host-to-host VPN with PSK authentication and separate data and control planes by using the vpn RHEL system role](#configuring-an-ipsec-host-to-host-vpn-with-psk-authentication-and-separate-data-and-control-planes-by-using-the-vpn-rhel-system-role) {#configuring-an-ipsec-host-to-host-vpn-with-psk-authentication-and-separate-data-and-control-planes-by-using-the-vpn-rhel-system-role .title}

Use the `vpn`{.literal} RHEL system role to automate the process of creating an IPsec host-to-host VPN. To enhance security by minimizing the risk of control messages being intercepted or disrupted, configure separate connections for both the data traffic and the control traffic.

A host-to-host VPN establishes a direct, secure, and encrypted connection between two devices, allowing applications to communicate safely over an insecure network, such as the internet.

For authentication, a pre-shared key (PSK) is a straightforward method that uses a single, shared secret known only to the two peers. This approach is simple to configure and ideal for basic setups where ease of deployment is a priority. However, you must keep the key strictly confidential. An attacker with access to the key can compromise the connection.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configuring VPN
      hosts: managed-node-01.example.com, managed-node-02.example.com
      tasks:
        - name: IPsec VPN with PSK authentication
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.vpn
          vars:
            vpn_connections:
              - name: control_plane_vpn
                hosts:
                  managed-node-01.example.com:
                    hostname: 203.0.113.1  # IP address for the control plane
                  managed-node-02.example.com:
                    hostname: 198.51.100.2 # IP address for the control plane
                auth_method: psk
                auto: start
              - name: data_plane_vpn
                hosts:
                  managed-node-01.example.com:
                    hostname: 10.0.0.1   # IP address for the data plane
                  managed-node-02.example.com:
                    hostname: 172.16.0.2 # IP address for the data plane
                auth_method: psk
                auto: start
            vpn_manage_firewall: true
            vpn_manage_selinux: true
    ```

    The settings specified in the example playbook include the following:

    `hosts: `{.literal}*`<list>`{.literal}*

    :   Defines a YAML dictionary with the hosts between which you want to configure a VPN. The connections are named *`<name>`{.literal}*`-`{.literal}*`<IP_address_A>`{.literal}*`-to-`{.literal}*`<IP_address_B>`{.literal}*, for example `control_plane_vpn-203.0.113.1-to-198.51.100.2`{.literal}.

        The role configures the VPN connection on each managed node. Note that the role cannot configure Libreswan on external (unmanaged) nodes. You must manually create the configuration on these hosts.

    `auth_method: psk`{.literal}
    :   Enables PSK authentication between the hosts. The role uses `openssl`{.literal} on the control node to create the pre-shared key.

    `auto: `{.literal}*`<startup_method>`{.literal}*
    :   Specifies the startup method of the connection. Valid values are `add`{.literal}, `ondemand`{.literal}, `start`{.literal}, and `ignore`{.literal}. For details, see the `ipsec.conf(5)`{.literal} man page on a system with Libreswan installed. The default value of this variable is null, which means no automatic startup operation.

    `vpn_manage_firewall: true`{.literal}
    :   Defines that the role opens the required ports in the `firewalld`{.literal} service on the managed nodes.

    `vpn_manage_selinux: true`{.literal}
    :   Defines that the role sets the required SELinux port type on the IPsec ports.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.vpn/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Confirm that the connections are successfully started, for example:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m shell -a 'ipsec trafficstatus | grep "control_plane_vpn-203.0.113.1-to-198.51.100.2"'
    ...
    006 #3: "control_plane_vpn-203.0.113.1-to-198.51.100.2", type=ESP, add_time=1741860073, inBytes=0, outBytes=0, maxBytes=2^63B, id='198.51.100.2'
    ```

    Note that this command only succeeds if the VPN connection is active. If you set the `auto`{.literal} variable in the playbook to a value other than `start`{.literal}, you might need to manually activate the connection on the managed nodes first.

#### [6.12.3. Configuring an IPsec site-to-site VPN with PSK authentication by using the vpn RHEL system role](#configuring-an-ipsec-site-to-site-vpn-with-psk-authentication-by-using-the-vpn-rhel-system-role) {#configuring-an-ipsec-site-to-site-vpn-with-psk-authentication-by-using-the-vpn-rhel-system-role .title}

A site-to-site VPN establishes an encrypted tunnel between two distinct networks, linking them across an insecure public network. By using the `vpn`{.literal} RHEL system role, you can automate the process of creating IPsec site-to-site VPN connections.

A site-to-site VPN enables devices in a branch office to access resources at a corporate headquarters as if they were all part of the same local network.

For authentication, a pre-shared key (PSK) is a straightforward method that uses a single, shared secret known only to the two peers. This approach is simple to configure and ideal for basic setups where ease of deployment is a priority. However, you must keep the key strictly confidential. An attacker with access to the key can compromise the connection.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configuring VPN
      hosts: managed-node-01.example.com, managed-node-02.example.com
      tasks:
        - name: IPsec VPN with PSK authentication
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.vpn
          vars:
            vpn_connections:
              - hosts:
                  managed-node-01.example.com:
                    subnets:
                      - 192.0.2.0/24
                  managed-node-02.example.com:
                    subnets:
                      - 198.51.100.0/24
                      - 203.0.113.0/24
                auth_method: psk
                auto: start
            vpn_manage_firewall: true
            vpn_manage_selinux: true
    ```

    The settings specified in the example playbook include the following:

    `hosts: `{.literal}*`<list>`{.literal}*

    :   Defines a YAML dictionary with the gateways between which you want to configure a VPN. If an entry is not an Ansible-managed node, you must specify its fully-qualified domain name (FQDN) or IP address in the `hostname`{.literal} parameter, for example:

        ``` {.language-yaml tabindex="-1"}
                  ...
                  - hosts:
                      ...
                      external-host.example.com:
                        hostname: 192.0.2.1
        ```

        The role configures the VPN connection on each managed node. The connections are named *`<gateway_A>`{.literal}*`-to-`{.literal}*`<gateway_B>`{.literal}*, for example, `managed-node-01.example.com-to-managed-node-02.example.com`{.literal}. Note that the role cannot configure Libreswan on external (unmanaged) nodes. You must manually create the configuration on these peers.

    `subnets: `{.literal}*`<yaml_list_of_subnets>`{.literal}*
    :   Defines subnets in classless inter-domain routing (CIDR) format that are connected through the tunnel.

    `auth_method: psk`{.literal}
    :   Enables PSK authentication between the peers. The role uses `openssl`{.literal} on the control node to create the PSK.

    `auto: `{.literal}*`<startup_method>`{.literal}*
    :   Specifies the startup method of the connection. Valid values are `add`{.literal}, `ondemand`{.literal}, `start`{.literal}, and `ignore`{.literal}. For details, see the `ipsec.conf(5)`{.literal} man page on a system with Libreswan installed. The default value of this variable is null, which means no automatic startup operation.

    `vpn_manage_firewall: true`{.literal}
    :   Defines that the role opens the required ports in the `firewalld`{.literal} service on the managed nodes.

    `vpn_manage_selinux: true`{.literal}
    :   Defines that the role sets the required SELinux port type on the IPsec ports.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.vpn/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

**Verification**

-   Confirm that the connections are successfully started, for example:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m shell -a 'ipsec trafficstatus | grep "managed-node-01.example.com-to-managed-node-02.example.com"'
    ...
    006 #3: "managed-node-01.example.com-to-managed-node-02.example.com", type=ESP, add_time=1741857153, inBytes=38622, outBytes=324626, maxBytes=2^63B, id='@managed-node-02.example.com'
    ```

    Note that this command only succeeds if the VPN connection is active. If you set the `auto`{.literal} variable in the playbook to a value other than `start`{.literal}, you might need to manually activate the connection on the managed nodes first.

**Troubleshooting**

-   If the playbook fails with syntax errors, validate the YAML structure:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

-   If managed nodes are unreachable, verify SSH connectivity and authentication:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m ping
    ```

-   If the playbook completes but the VPN connection does not establish, check the IPsec logs on the managed nodes:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m shell -a 'journalctl -u ipsec -n 50'
    ```

-   For detailed output during playbook execution, run with verbose mode:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook -vvv ~/playbook.yml
    ```

-   If the firewall blocks connections despite `vpn_manage_firewall: true`{.literal}, verify that `firewalld`{.literal} is running on the managed nodes and that the IPsec service was added to the active zone.

#### [6.12.4. Configuring an IPsec mesh VPN with certificate-based authentication by using the vpn RHEL system role](#configuring-an-ipsec-mesh-vpn-with-certificate-based-authentication-by-using-the-vpn-rhel-system-role) {#configuring-an-ipsec-mesh-vpn-with-certificate-based-authentication-by-using-the-vpn-rhel-system-role .title}

An IPsec mesh creates a fully interconnected network where every server can communicate securely and directly with every other server. By using the `vpn`{.literal} RHEL system role, you can automate configuring a VPN mesh with certificate-based authentication among managed nodes.

An IPsec mesh is ideal for distributed database clusters or high-availability environments that span multiple data centers or cloud providers. Establishing a direct, encrypted tunnel between each pair of servers ensures secure communication without a central bottleneck.

For authentication, using digital certificates managed by a Certificate Authority (CA) offers a highly secure and scalable solution. Each host in the mesh presents a certificate signed by a trusted CA. This method provides strong, verifiable authentication and simplifies user management. Access can be granted or revoked centrally at the CA, and Libreswan enforces this by checking each certificate against a certificate revocation list (CRL), denying access if a certificate is displayed on the list.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).

-   You are logged in to the control node as a user who can run playbooks on the managed nodes.

-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

-   You prepared a PKCS #12 file for each managed node:

    -   Each file contains:

        -   The private key of the server
        -   The server certificate
        -   The CA certificate
        -   If required, intermediate certificates

    -   The files are named *`<managed_node_name_as_in_the_inventory>`{.literal}*`.p12`{.literal}.

    -   The files are stored in the same directory as the playbook.

    -   The server certificate contains the following fields:

        -   Extended Key Usage (EKU) is set to `TLS Web Server Authentication`{.literal}.
        -   Common Name (CN) or Subject Alternative Name (SAN) is set to the fully-qualified domain name (FQDN) of the host.
        -   X509v3 CRL distribution points contain URLs to Certificate Revocation Lists (CRLs).

**Procedure**

1.  Edit the `~/inventory`{.literal} file, and append the `cert_name`{.literal} variable:

    ``` {.language-plaintext tabindex="-1"}
    managed-node-01.example.com cert_name=managed-node-01.example.com
    managed-node-02.example.com cert_name=managed-node-02.example.com
    managed-node-03.example.com cert_name=managed-node-03.example.com
    ```

    Set the `cert_name`{.literal} variable to the value of the common name (CN) field used in the certificate for each host. Typically, the CN field is set to the fully-qualified domain name (FQDN).

2.  Store your sensitive variables in an encrypted file:

    a.  Create the vault:

        ``` {.language-plaintext tabindex="-1"}
        $ ansible-vault create ~/vault.yml
        New Vault password: <vault_password>
        Confirm New Vault password: <vault_password>
        ```

    b.  After the `ansible-vault create`{.literal} command opens an editor, enter the sensitive data in the *`<key>`{.literal}*`: `{.literal}*`<value>`{.literal}* format:

        ``` {.language-plaintext tabindex="-1"}
        pkcs12_pwd: <password>
        ```

    c.  Save the changes, and close the editor. Ansible encrypts the data in the vault.

3.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    - name: Configuring VPN
      hosts: managed-node-01.example.com, managed-node-02.example.com, managed-node-03.example.com
      vars_files:
        - ~/vault.yml
      tasks:
        - name: Install LibreSwan
          ansible.builtin.package:
            name: libreswan
            state: present

        - name: Identify the path to IPsec NSS database
          ansible.builtin.set_fact:
            nss_db_dir: "{{ '/etc/ipsec.d/' if
              ansible_distribution in ['CentOS', 'RedHat']
              and ansible_distribution_major_version is version('8', '=')
              else '/var/lib/ipsec/nss/' }}"

        - name: Locate IPsec NSS database files
          ansible.builtin.find:
            paths: "{{ nss_db_dir }}"
            patterns: "*.db"
          register: db_files

        - name: Initialize IPsec NSS database if not initialized
          ansible.builtin.command:
            cmd: ipsec initnss
          when: db_files.matched == 0

        - name: Copy PKCS #12 file to the managed node
          ansible.builtin.copy:
            src: "~/{{ inventory_hostname }}.p12"
            dest: "/etc/ipsec.d/{{ inventory_hostname }}.p12"
            mode: 0600

        - name: Import PKCS #12 file in IPsec NSS database
          ansible.builtin.shell:
            cmd: 'pk12util -d {{ nss_db_dir }} -i /etc/ipsec.d/{{ inventory_hostname }}.p12 -W "{{ pkcs12_pwd }}"'

        - name: Remove PKCS #12 file
          ansible.builtin.file:
            path: "/etc/ipsec.d/{{ inventory_hostname }}.p12"
            state: absent

        - name: Opportunistic mesh IPsec VPN with certificate-based authentication
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.vpn
          vars:
            vpn_connections:
              - opportunistic: true
                auth_method: cert
                policies:
                  - policy: private
                    cidr: default
                  - policy: private
                    cidr: 192.0.2.0/24
                  - policy: clear
                    cidr: 192.0.2.1/32
            vpn_manage_firewall: true
            vpn_manage_selinux: true
    ```

    The settings specified in the example playbook include the following:

    `opportunistic: true`{.literal}
    :   Enables an opportunistic mesh among multiple hosts. The `policies`{.literal} variable defines for which subnets and hosts traffic must or can be encrypted and which of them continue using plain text connections.

    `auth_method: cert`{.literal}
    :   Enables certificate-based authentication. This requires that you specify the nickname of each managed node's certificate in the inventory.

    `policies: `{.literal}*`<list_of_policies>`{.literal}*

    :   Defines the Libreswan policies in YAML list format.

        The default policy is `private-or-clear`{.literal}. To change it to `private`{.literal}, the playbook contains an according policy for the default `cidr`{.literal} entry.

        To prevent a loss of the SSH connection during the execution of the playbook if the Ansible control node is in the same IP subnet as the managed nodes, add a `clear`{.literal} policy for the control node's IP address. For example, if you want the mesh to be configured for the `192.0.2.0/24`{.literal} subnet and the control node uses the IP address `192.0.2.1`{.literal}, you require a `clear`{.literal} policy for `192.0.2.1/32`{.literal} as shown in the playbook.

        For details about policies, see the `ipsec.conf(5)`{.literal} man page on a system with Libreswan installed.

    `vpn_manage_firewall: true`{.literal}
    :   Defines that the role opens the required ports in the `firewalld`{.literal} service on the managed nodes.

    `vpn_manage_selinux: true`{.literal}
    :   Defines that the role sets the required SELinux port type on the IPsec ports.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.vpn/README.md`{.literal} file on the control node.

4.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --ask-vault-pass --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

5.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --ask-vault-pass ~/playbook.yml
    ```

**Verification**

1.  On a node in the mesh, ping another node to activate the connection:

    ``` {.language-plaintext tabindex="-1"}
    [root@managed-node-01]# ping managed-node-02.example.com
    ```

2.  Confirm that the connection is active:

    ``` {.language-plaintext tabindex="-1"}
    [root@managed-node-01]# ipsec trafficstatus
    006 #2: "private#192.0.2.0/24"[1] ...192.0.2.2, type=ESP, add_time=1741938929, inBytes=372408, outBytes=545728, maxBytes=2^63B, id='CN=managed-node-02.example.com'
    ```

**Troubleshooting**

-   If the playbook fails with syntax errors, validate the YAML structure:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --ask-vault-pass --syntax-check ~/playbook.yml
    ```

-   If managed nodes are unreachable, verify SSH connectivity and authentication:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m ping
    ```

-   If the PKCS #12 import fails, verify that the password in the vault matches the PKCS #12 file password and that the certificate files are named correctly according to the inventory hostnames.

-   If the mesh connection does not establish, check the IPsec logs on the managed nodes:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m shell -a 'journalctl -u ipsec -n 50'
    ```

-   If certificate validation fails, verify that the `cert_name`{.literal} values in the inventory file match the Common Name (CN) fields in the certificates.

-   For detailed output during playbook execution, run with verbose mode:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --ask-vault-pass -vvv ~/playbook.yml
    ```

### [6.13. Configuring IPsec VPN connections by using nmstatectl](#configuring-ipsec-vpn-connections-by-using-nmstatectl) {#configuring-ipsec-vpn-connections-by-using-nmstatectl .title}

Configure IPsec VPN connections to establish encrypted tunnels over untrusted networks and ensure the integrity of data in transit. By using Nmstate, you can create IPsec VPN connections by using a declarative API.

You can use the `nmstatectl`{.literal} utility to configure Libreswan IPsec VPN connections through the Nmstate API. The `nmstatectl`{.literal} utility is a command-line tool to manage host networking through the declarative Nmstate API. Instead of running multiple imperative commands to configure an interface, you define the expected state in a YAML file. Nmstate then takes this definition and applies it to the system. A key advantage of this approach is an atomic result. Nmstate ensures that the resulting configuration precisely matches your YAML definition. If any part of the configuration fails to apply, it automatically rolls back all changes and prevents the system from entering an incorrect or broken network state.

Note

Due to the design of the `NetworkManager-libreswan`{.literal} plugin, you can use `nmstatectl`{.literal} only on one peer and must manually configure Libreswan on the other peer.

#### [6.13.1. Configuring an IPsec host-to-host VPN with raw RSA key authentication by using nmstatectl](#configuring-an-ipsec-host-to-host-vpn-with-raw-rsa-key-authentication-by-using-nmstatectl) {#configuring-an-ipsec-host-to-host-vpn-with-raw-rsa-key-authentication-by-using-nmstatectl .title}

You can use the declarative Nmstate API to configure a host-to-host VPN between two devices to communicate safely over an insecure network. Nmstate ensures that the result matches the configuration file or rolls back the changes.

For authentication, RSA keys are more secure than pre-shared keys (PSKs) because their asymmetric encryption eliminates the risk of a shared secret. Using RSA keys also simplifies deployment by avoiding the need for a certificate authority (CA), and provides strong peer-to-peer authentication.

Note

In general, the choice of which host is named *left* and *right* is arbitrary. However, NetworkManager always uses the term *left* for the local host and *right* for the remote host.

**Prerequisites**

-   The remote peer runs Libreswan IPsec and is prepared for a [host-to-host](#manually-configuring-an-ipsec-host-to-host-vpn-with-raw-rsa-key-authentication "6.3. Manually configuring an IPsec host-to-host VPN with raw RSA key authentication") connection.

    Due to the design of the `NetworkManager-libreswan`{.literal} plugin, Nmstate cannot communicate with other peers that also use this plugin for the same connection.

**Procedure**

1.  If Libreswan is not yet installed, perform the following steps:

    a.  Install the required packages:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install nmstate libreswan NetworkManager-libreswan
        ```

    b.  Restart the NetworkManager service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart NetworkManager
        ```

    c.  Initialize the Network Security Services (NSS) database:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec initnss
        ```

        The command creates the database in the `/var/lib/ipsec/nss/`{.literal} directory.

    d.  Open the IPsec ports and protocols in the firewall:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service="ipsec"
        # firewall-cmd --reload
        ```

2.  Create an RSA key pair:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec newhostkey
    ```

    The `ipsec`{.literal} utility stores the key pair in the NSS database.

3.  Display the Certificate Key Attribute ID (CKAID) on both the left and right peers:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec showhostkey --list
    < 1> RSA keyid: <key_id> ckaid: <ckaid>
    ```

    You require the CKAIDs of both peers in the next steps.

4.  Display the public keys:

    a.  On the left peer, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec showhostkey --left --ckaid <ckaid_of_left_peer>
                # rsakey AwEAAdKCx
                leftrsasigkey=0sAwEAAdKCxpc9db48cehzQiQD...
        ```

    b.  On the right peer, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec showhostkey --right --ckaid <ckaid_of_right_peer>
                # rsakey AwEAAcNWC
                rightrsasigkey=0sAwEAAcNWCzZO+PR1j8WbO8X...
        ```

    The commands display the public keys with the corresponding parameters that you must use in the configuration file.

5.  Create a YAML file, for example `~/ipsec-host-to-host-rsa-auth.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    interfaces:
    - name: '<connection_name>'
      type: ipsec
      libreswan:
        ikev2: insist

        left: <ip_address_or_fqdn_of_left_peer>
        leftid: peer_b
        leftrsasigkey: <public_key_of_left_peer>
        leftmodecfgclient: false

        right: <ip_address_or_fqdn_of_right_peer>
        rightid: peer_a
        rightrsasigkey: <public_key_of_right_peer>
        rightsubnet: <ip_address_of_right_peer>/32
    ```

    The settings specified in the example include the following:

    `ikev2: insist`{.literal}
    :   Defines the modern IKEv2 protocol as the only allowed protocol without fallback to IKEv1. This setting is mandatory in a host-to-host configuration with Nmstate.

    `left=`{.literal}*`<ip_address_or_fqdn_of_left_peer>`{.literal}* and `right=`{.literal}*`<ip_address_or_fqdn_of_right_peer>`{.literal}*
    :   Defines the IP address or DNS name of the peers.

    `leftid=`{.literal}*`<id>`{.literal}* and `rightid=`{.literal}*`<id>`{.literal}*
    :   Defines how each peer is identified during the Internet Key Exchange (IKE) negotiation process. This can be an IP address or a literal string. Note that NetworkManager interprets all values other than IP addresses as a literal string and internally adds a leading `@`{.literal} sign. This requires that the Libreswan peer also uses literal strings as IDs or authentication fails.

    `leftrsasigkey=`{.literal}*`<public_key>`{.literal}* and `rightrsasigkey=`{.literal}*`<public_key>`{.literal}*
    :   Specifies the public key of the peers. Use the values displayed by the `ipsec showhostkey`{.literal} command in a previous step.

    `leftmodecfgclient: false`{.literal}
    :   Disables dynamic configuration on this host. This setting is mandatory in a host-to-host configuration with Nmstate.

    `rightsubnet: `{.literal}*`<ip_address_of_right_peer>`{.literal}*`/32`{.literal}
    :   Defines that the host can only access this peer. This setting is mandatory in a host-to-host configuration with Nmstate.

6.  Apply the settings to the system:

    ``` {.language-plaintext tabindex="-1"}
    # nmstatectl apply ~/ipsec-host-to-host-rsa-auth.yml
    ```

**Verification**

-   Display the IPsec status:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec status
    ```

    If the connection is successfully established, the output contains lines as follows:

    -   Phase 1 of an Internet Key Exchange version 2 (IKEv2) negotiation has been successfully completed:

        ``` {.language-plaintext tabindex="-1"}
        000 #1: "<connection_name>":500 STATE_V2_ESTABLISHED_IKE_SA (established IKE SA); REKEY in 27935s; REPLACE in 28610s; newest; idle;
        ```

        The Security Association (SA) is now ready to negotiate the actual data encryption tunnels, known as child SAs or Phase 2 SAs.

    -   A child SA has been established:

        ``` {.language-plaintext tabindex="-1"}
        000 #2: "<connection_name>":500 STATE_V2_ESTABLISHED_CHILD_SA (established Child SA); REKEY in 27671s; REPLACE in 28610s; IKE SA #1; idle;
        ```

        This is the actual tunnel that your data traffic flows through.

**Troubleshooting**

-   To display the actual configuration NetworkManager passes to Libreswan, enter:

    ``` {.language-plaintext tabindex="-1"}
    # nmcli connection export <connection_name>
    ```

    The output can help to identify deviating settings, such as IDs and keys, when you compare them with the Libreswan configuration on the remote host.

**Next steps**

-   If you use this host in a network with DHCP or Stateless Address Autoconfiguration (SLAAC), the connection can be vulnerable to being redirected. For details and mitigation steps, see [Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel](#assigning-a-vpn-connection-to-a-dedicated-routing-table-to-prevent-the-connection-from-bypassing-the-tunnel_ipsec "6.11. Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel").

#### [6.13.2. Configuring an IPsec site-to-site VPN with raw RSA key authentication by using nmstatectl](#configuring-an-ipsec-site-to-site-vpn-with-raw-rsa-key-authentication-by-using-nmstatectl) {#configuring-an-ipsec-site-to-site-vpn-with-raw-rsa-key-authentication-by-using-nmstatectl .title}

You can use the declarative Nmstate API to configure a site-to-site VPN between two distinct networks, linking them across an insecure network. Nmstate ensures that the result matches the configuration file or rolls back the changes.

For authenticating the gateway devices, RSA keys are more secure than pre-shared keys (PSKs) because their asymmetric encryption eliminates the risk of a shared secret. Using RSA keys also simplifies deployment by avoiding the need for a certificate authority (CA), and provides strong peer-to-peer authentication.

Note

In general, the choice which host is named *left* and *right* is arbitrary. However, NetworkManager always uses the term *left* for the local host and *right* for the remote host.

**Prerequisites**

-   The remote gateway runs Libreswan IPsec and is prepared for a [site-to-site](#manually-configuring-an-ipsec-site-to-site-vpn-with-raw-rsa-key-authentication "6.4. Manually configuring an IPsec site-to-site VPN with raw RSA key authentication") connection.

    Due to the design of the `NetworkManager-libreswan`{.literal} plugin, Nmstate cannot communicate with other peers that also use this plugin for the same connection.

**Procedure**

1.  If Libreswan is not yet installed, perform the following steps:

    a.  Install the required packages:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install nmstate libreswan NetworkManager-libreswan
        ```

    b.  Restart the NetworkManager service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart NetworkManager
        ```

    c.  Initialize the Network Security Services (NSS) database:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec initnss
        ```

        The command creates the database in the `/var/lib/ipsec/nss/`{.literal} directory.

    d.  Open the IPsec ports and protocols in the firewall:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service="ipsec"
        # firewall-cmd --reload
        ```

2.  Create an RSA key pair:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec newhostkey
    ```

    The `ipsec`{.literal} utility stores the key pair in the NSS database.

3.  Display the Certificate Key Attribute ID (CKAID) on both the left and right peer:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec showhostkey --list
    < 1> RSA keyid: <key_id> ckaid: <ckaid>
    ```

    You require the CKAIDs of both peers in the following steps.

4.  Display the public keys:

    a.  On the left peer, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec showhostkey --left --ckaid <ckaid_of_left_peer>
                # rsakey AwEAAdKCx
                leftrsasigkey=0sAwEAAdKCxpc9db48cehzQiQD...
        ```

    b.  On the right peer, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec showhostkey --right --ckaid <ckaid_of_right_peer>
                # rsakey AwEAAcNWC
                rightrsasigkey=0sAwEAAcNWCzZO+PR1j8WbO8X...
        ```

    The commands display the public keys with the corresponding parameters that you must use in the configuration file.

5.  Create a YAML file, for example `~/ipsec-site-to-site-rsa-auth.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    interfaces:
    - name: '<connection_name>'
      type: ipsec
      libreswan:
        ikev2: insist

        left: <ip_address_or_fqdn_of_left_peer>
        leftid: peer_b
        leftrsasigkey: <public_key_of_left_peer>
        leftmodecfgclient: false
        leftsubnet: 198.51.100.0/24

        right: <ip_address_or_fqdn_of_right_peer>
        rightid: peer_a
        rightrsasigkey: <public_key_of_right_peer>
        rightsubnet: 192.0.2.0/24
    ```

    The settings specified in the example include the following:

    `ikev2: insist`{.literal}
    :   Defines the modern IKEv2 protocol as the only allowed protocol without fallback to IKEv1. This setting is mandatory in a site-to-site configuration with Nmstate.

    `left=`{.literal}*`<ip_address_or_fqdn_of_left_peer>`{.literal}* and `right=`{.literal}*`<ip_address_or_fqdn_of_right_peer>`{.literal}*
    :   Defines the IP address or DNS name of the peers.

    `leftid=`{.literal}*`<id>`{.literal}* and `rightid=`{.literal}*`<id>`{.literal}*
    :   Defines how each peer is identified during the Internet Key Exchange (IKE) negotiation process. This can be an IP address or a literal string. Note that NetworkManager interprets all values other than IP addresses as a literal string and internally adds a leading `@`{.literal} sign. This requires that the Libreswan peer also uses literal strings as IDs or authentication fails.

    `leftrsasigkey=`{.literal}*`<public_key>`{.literal}* and `rightrsasigkey=`{.literal}*`<public_key>`{.literal}*
    :   Specifies the public key of the peers. Use the values displayed by the `ipsec showhostkey`{.literal} command in a previous step.

    `leftmodecfgclient: false`{.literal}
    :   Disables dynamic configuration on this host. This setting is mandatory in a site-to-site configuration with Nmstate.

    `leftsubnet=`{.literal}*`<subnet>`{.literal}* and `rightsubnet=`{.literal}*`<subnet>`{.literal}*
    :   Defines subnets in classless inter-domain routing (CIDR) format that are connected through the tunnel.

6.  Enable packet forwarding:

    ``` {.language-plaintext tabindex="-1"}
    # echo "net.ipv4.ip_forward=1" > /etc/sysctl.d/95-IPv4-forwarding.conf
    # sysctl -p /etc/sysctl.d/95-IPv4-forwarding.conf
    ```

7.  Apply the settings to the system:

    ``` {.language-plaintext tabindex="-1"}
    # nmstatectl apply ~/ipsec-site-to-site-rsa-auth.yml
    ```

**Verification**

1.  Display the IPsec status:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec status
    ```

    If the connection is successfully established, the output contains lines as follows:

    -   Phase 1 of an Internet Key Exchange version 2 (IKEv2) negotiation has been successfully completed:

        ``` {.language-plaintext tabindex="-1"}
        000 #1: "<connection_name>":500 STATE_V2_ESTABLISHED_IKE_SA (established IKE SA); REKEY in 27935s; REPLACE in 28610s; newest; idle;
        ```

        The Security Association (SA) is now ready to negotiate the actual data encryption tunnels, known as child SAs or Phase 2 SAs.

    -   A child SA has been established:

        ``` {.language-plaintext tabindex="-1"}
        000 #2: "<connection_name>":500 STATE_V2_ESTABLISHED_CHILD_SA (established Child SA); REKEY in 27671s; REPLACE in 28610s; IKE SA #1; idle;
        ```

        This is the actual tunnel that your data traffic flows through.

2.  From a client in the local subnet, ping a client in the remote subnet.

**Troubleshooting**

-   To display the actual configuration NetworkManager passes to Libreswan, enter:

    ``` {.language-plaintext tabindex="-1"}
    # nmcli connection export <connection_name>
    ```

    The output can help to identify deviating settings, such as IDs and keys, when you compare them with the Libreswan configuration on the remote host.

**Next steps**

-   If you use this host in a network with DHCP or Stateless Address Autoconfiguration (SLAAC), the connection can be vulnerable to being redirected. For details and mitigation steps, see [Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel](#assigning-a-vpn-connection-to-a-dedicated-routing-table-to-prevent-the-connection-from-bypassing-the-tunnel_ipsec "6.11. Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel").

#### [6.13.3. Configuring a client to connect to an IPsec VPN gateway by using nmstatectl](#configuring-a-client-to-connect-to-an-ipsec-vpn-gateway-by-using-nmstatectl) {#configuring-a-client-to-connect-to-an-ipsec-vpn-gateway-by-using-nmstatectl .title}

To access resources on a remote private network, users must first configure an IPsec VPN connection. By using Nmstate, you can create the connection with an existing Libreswan IPsec gateway by using a declarative API.

Note

In general, the choice of which host is named *left* and *right* is arbitrary. However, NetworkManager always uses the term *left* for the local host and *right* for the remote host.

**Prerequisites**

-   The remote gateway runs Libreswan IPsec and is prepared for a [host-to-site](#setting-up-an-ipsec-gateway-manually "6.5.1. Setting up an IPsec gateway manually") connection with certificate-based authentication.

    Due to the design of the `NetworkManager-libreswan`{.literal} plugin, Nmstate cannot communicate with other peers that also use this plugin for the same connection.

-   The PKCS#12 file `~/file.p12`{.literal} exists on the client with the following contents:

    -   The private key of the user
    -   The user certificate
    -   The CA certificate
    -   If required, intermediate certificates

    For details about creating a private key and certificate signing request (CSR), as well as about requesting a certificate from a CA, see your CA's documentation.

-   The Extended Key Usage (EKU) in the certificate is set to `TLS Web Client Authentication`{.literal}.

**Procedure**

1.  If Libreswan is not yet installed:

    a.  Install the required packages:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install nmstate libreswan NetworkManager-libreswan
        ```

    b.  Restart the NetworkManager service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart NetworkManager
        ```

    c.  Initialize the Network Security Services (NSS) database:

        ``` {.language-plaintext tabindex="-1"}
        # ipsec initnss
        ```

        The command creates the database in the `/var/lib/ipsec/nss/`{.literal} directory.

    d.  Open the IPsec ports and protocols in the firewall:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-service="ipsec"
        # firewall-cmd --reload
        ```

2.  Import the PKCS #12 file into the NSS database:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec import ~/file.p12
    Enter password for PKCS12 file: <password>
    pk12util: PKCS12 IMPORT SUCCESSFUL
    correcting trust bits for Example-CA
    ```

3.  Display the nicknames of the user and CA certificates:

    ``` {.language-plaintext tabindex="-1"}
    # certutil -L -d /var/lib/ipsec/nss/
    Certificate Nickname     Trust Attributes
                             SSL,S/MIME,JAR/XPI

    user                     u,u,u
    Example-CA               CT,,
    ...
    ```

    You require this information in the Nmstate YAML file.

4.  Create a YAML file, for example, `~/ipsec-host-to-site-cert-auth.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    interfaces:
    - name: '<connection_name>'
      type: ipsec
      libreswan:
        ikev2: insist

        left: <ip_address_or_fqdn_of_left_peer>
        leftid: '%fromcert'
        leftcert: <user_certificate_nickname>

        right: <ip_address_or_fqdn_of_right_peer>
        rightid: '%fromcert'
        rightsubnet: 192.0.2.0/24
    ```

    The settings specified in the example include the following:

    `ikev2: insist`{.literal}
    :   Defines the modern IKEv2 protocol as the only allowed protocol without fallback to IKEv1. This setting is mandatory in a host-to-site configuration with Nmstate.

    `left=`{.literal}*`<ip_address_or_fqdn_of_left_peer>`{.literal}* and `right=`{.literal}*`<ip_address_or_fqdn_of_right_peer>`{.literal}*
    :   Defines the IP address or DNS name of the peers.

    `leftid=%fromcert`{.literal} and `rightid=%fromcert`{.literal}
    :   Configures Libreswan to retrieve the identity from the distinguished name (DN) field of the certificate.

    `leftcert="`{.literal}*`<server_certificate_nickname>`{.literal}*`"`{.literal}
    :   Sets the nickname of the server's certificate used in the NSS database.

    `rightsubnet: `{.literal}*`<subnet>`{.literal}*
    :   Defines the subnet in classless inter-domain routing (CIDR) format that is connected to the gateway.

5.  Apply the settings to the system:

    ``` {.language-plaintext tabindex="-1"}
    # nmstatectl apply ~/ipsec-host-to-site-cert-auth.yml
    ```

**Verification**

-   Establish a connection to a host in the remote network or ping it.

**Troubleshooting**

-   To display the actual configuration NetworkManager passes to Libreswan, enter:

    ``` {.language-plaintext tabindex="-1"}
    # nmcli connection export <connection_name>
    ```

    The output can help to identify deviating settings, such as IDs and keys, when you compare them with the Libreswan configuration on the remote host.

**Next steps**

-   If you use this host in a network with DHCP or Stateless Address Autoconfiguration (SLAAC), the connection can be vulnerable to being redirected. For details and mitigation steps, see [Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel](#assigning-a-vpn-connection-to-a-dedicated-routing-table-to-prevent-the-connection-from-bypassing-the-tunnel_ipsec "6.11. Assigning a VPN connection to a dedicated routing table to prevent the connection from bypassing the tunnel").

### [6.14. Troubleshooting IPsec configurations](#troubleshooting-ipsec-configurations) {#troubleshooting-ipsec-configurations .title}

Diagnosing IPsec configuration failures can be challenging, because issues can be caused by mismatched settings, firewall rules, and kernel-level errors. The following information provides a systematic approach to resolving common problems with IPsec VPN connections.

#### [6.14.1. Basic connection issues](#basic-connection-issues) {#basic-connection-issues .title}

Problems with VPN connections often occur due to mismatched configurations between the endpoints.

To confirm that an IPsec connection is established, enter:

``` {.language-plaintext tabindex="-1"}
# ipsec trafficstatus
006 #8: "vpn.example.com"[1] 192.0.2.1, type=ESP, add_time=1595296930, inBytes=5999, outBytes=3231, id='@vpn.example.com', lease=198.51.100.1/32
```

For a successful connection, the command shows an entry with the connection's name and details. If the output is empty, the tunnel is not established.

#### [6.14.2. Firewall-related problems](#firewall-related-problems) {#firewall-related-problems .title}

Diagnose IPsec connection failures caused by firewall-related problems.

If a firewall on an endpoint or an intermediate route drops Internet Key Exchange version 2 (IKEv2) packets, the `ipsec up`{.literal} command times out and shows repeated *retransmission* messages:

``` {.language-plaintext tabindex="-1"}
181 "vpn.example.com"[1] 192.0.2.2 #15: initiating IKEv2 IKE SA
181 "vpn.example.com"[1] 192.0.2.2 #15: STATE_PARENT_I1: sent v2I1, expected v2R1
010 "vpn.example.com"[1] 192.0.2.2 #15: STATE_PARENT_I1: retransmission; will wait 0.5 seconds for response
010 "vpn.example.com"[1] 192.0.2.2 #15: STATE_PARENT_I1: retransmission; will wait 1 seconds for response
010 "vpn.example.com"[1] 192.0.2.2 #15: STATE_PARENT_I1: retransmission; will wait 2 seconds for response
...
```

You can use the `tcpdump`{.literal} utility to capture traffic and verify if IKE or IPsec packets are dropped by a firewall, for example:

``` {.language-plaintext tabindex="-1"}
# tcpdump -i <interface> -n -n esp or udp port 500 or udp port 4500 or tcp port 4500
```

Note that `tcpdump`{.literal} is of limited use for diagnosing other types of IPsec problems because the IKE protocol is encrypted.

#### [6.14.3. Mismatched Configurations](#mismatched-configurations) {#mismatched-configurations .title}

VPN connections fail if the endpoints are not configured with matching Internet Key Exchange (IKE) versions, algorithms, IP address ranges, or pre-shared keys (PSK). If you identify a mismatch, you must align the settings on both endpoints to resolve the issue.

Remote Peer Not Running IKE/IPsec

:   If the connection was refused, an ICMP error is displayed:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec up vpn.example.com
    ...
    000 "vpn.example.com"[1] 192.0.2.2 #16: ERROR: asynchronous network error report on wlp2s0 (192.0.2.2:500), complainant 198.51.100.1: Connection refused [errno 111, origin ICMP type 3 code 3 (not authenticated)]
    ```

Mismatched IKE Algorithms

:   The connection fails with a `NO_PROPOSAL_CHOSEN`{.literal} notification during the initial setup:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec up vpn.example.com
    ...
    003 "vpn.example.com"[1] 193.110.157.148 #3: dropping unexpected IKE_SA_INIT message containing NO_PROPOSAL_CHOSEN notification; message payloads: N; missing payloads: SA,KE,Ni
    ```

Mismatched IPsec Algorithms

:   The connection fails with a `NO_PROPOSAL_CHOSEN`{.literal} error after the initial exchange:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec up vpn.example.com
    ...
    182 "vpn.example.com"[1] 193.110.157.148 #5: STATE_PARENT_I2: sent v2I2, expected v2R2 {auth=IKEv2 cipher=AES_GCM_16_256 integ=n/a prf=HMAC_SHA2_256 group=MODP2048}
    002 "vpn.example.com"[1] 193.110.157.148 #6: IKE_AUTH response contained the error notification NO_PROPOSAL_CHOSEN
    ```

Mismatched IP Address Ranges (IKEv2)

:   The remote peer responds with a `TS_UNACCEPTABLE`{.literal} error:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec up vpn.example.com
    ...
    1v2 "vpn.example.com" #1: STATE_PARENT_I2: sent v2I2, expected v2R2 {auth=IKEv2 cipher=AES_GCM_16_256 integ=n/a prf=HMAC_SHA2_512 group=MODP2048}
    002 "vpn.example.com" #2: IKE_AUTH response contained the error notification TS_UNACCEPTABLE
    ```

Mismatched IP Address Ranges (IKEv1)

:   The connection times out during quick mode, with a message indicating the peer did not accept the proposal:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec up vpn.example.com
    ...
    031 "vpn.example.com" #2: STATE_QUICK_I1: 60 second timeout exceeded after 0 retransmits.  No acceptable response to our first Quick Mode message: perhaps peer likes no proposal
    ```

Mismatched PSK (IKEv2)

:   The peer rejects the connection with an `AUTHENTICATION_FAILED`{.literal} error:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec up vpn.example.com
    ...
    003 "vpn.example.com" #1: received Hash Payload does not match computed value
    223 "vpn.example.com" #1: sending notification INVALID_HASH_INFORMATION to 192.0.2.23:500
    ```

Mismatched PSK (IKEv1)

:   The hash payload does not match, making the IKE message unreadable and resulting in an `INVALID_HASH_INFORMATION`{.literal} error:

    ``` {.language-plaintext tabindex="-1"}
    # ipsec up vpn.example.com
    ...
    002 "vpn.example.com" #1: IKE SA authentication request rejected by peer: AUTHENTICATION_FAILED
    ```

#### [6.14.4. MTU issues](#mtu-issues) {#mtu-issues .title}

Diagnose intermittent IPsec connection failures caused by Maximum Transmission Unit (MTU) issues. Encryption increases packet size, leading to fragmentation and lost data when packets exceed the network's MTU, often seen with larger data transfers.

A common symptom is that small packets, for example pings, work correctly, but larger packets, such as an SSH session, freeze after the login. To fix the problem, lower the MTU for the tunnel by adding the `mtu=1400`{.literal} option to the configuration file.

#### [6.14.5. NAT conflicts](#nat-conflicts) {#nat-conflicts .title}

Resolve NAT conflicts that occur when an IPsec host also acts as a NAT router. Incorrect NAT application can translate source IP addresses before encryption, causing packets to be sent unencrypted over the network.

For example, if the source IP address of the packet is translated by a masquerade rule before IPsec encryption is applied, the packet's source no longer matches the IPsec policy, and Libreswan sends it unencrypted over the network.

To solve this problem, add a firewall rule that excludes traffic between the IPsec subnets from NAT. Insert this rule at the beginning of the `POSTROUTING`{.literal} chain to ensure it is processed before the general NAT rule.

**Example 6.1. Solution by using the `nftables`{.literal} framework**

The following example uses `nftables`{.literal} to configure a basic NAT environment that excludes traffic between the 192.0.2.0/24 and 198.51.100.0/24 subnets from address translation:

``` {.language-plaintext tabindex="-1"}
# nft add table ip nat
# nft add chain ip nat postrouting { type nat hook postrouting priority 100 \; }
# nft add rule ip nat postrouting ip saddr 192.0.2.0/24 ip daddr 198.51.100.0/24 return
```

#### [6.14.6. Kernel-level IPsec issues](#kernel-level-ipsec-issues) {#kernel-level-ipsec-issues .title}

Troubleshoot kernel-level IPsec issues when a VPN tunnel appears established but no traffic flows. In this case, inspect the kernel's IPsec state to check if the tunnel policies and cryptographic keys were correctly installed.

This process involves checking two components:

-   The Security Policy Database (SPD): The rule that instructs the kernel what traffic to encrypt.
-   The Security Association Database (SAD): The keys that instruct the kernel how to encrypt that traffic.

First, check if the correct policy exists in the SPD:

``` {.language-plaintext tabindex="-1"}
# ip xfrm policy
src 192.0.2.1/32 dst 10.0.0.0/8
    dir out priority 666 ptype main
    tmpl src 198.51.100.13 dst 203.0.113.22
        proto esp reqid 16417 mode tunnel
```

The output contains the policies matching your `leftsubnet`{.literal} and `rightsubnet`{.literal} parameters with both in and out directions. If you do not see a policy for your traffic, Libreswan failed to create the kernel rule, and traffic is not encrypted.

If the policy exists, check if it has a corresponding set of keys in the SAD:

``` {.language-plaintext tabindex="-1"}
# ip xfrm state
src 203.0.113.22 dst 198.51.100.13
    proto esp spi 0xa78b3fdb reqid 16417 mode tunnel
    auth-trunc hmac(sha1) 0x3763cd3b... 96
    enc cbc(aes) 0xd9dba399...
```

Warning

This command displays private cryptographic keys. Do not share this output, because attackers can use it to decrypt your VPN traffic.

If a policy exists but you see no corresponding state with the same `reqid`{.literal}, it typically means the Internet Key Exchange (IKE) negotiation failed. The two VPN endpoints could not agree on a set of keys.

For more detailed diagnostics, use the `-s`{.literal} option with either of the commands. This option adds traffic counters, which can help you identify if the kernel processes packets by a specific rule.

#### [6.14.7. Kernel IPsec subsystem bugs](#kernel-ipsec-subsystem-bugs) {#kernel-ipsec-subsystem-bugs .title}

A defect in the kernel's IPsec subsystem can cause it to lose sync with the IKE daemon. This can lead to discrepancies between negotiated security associations and actual IPsec policy enforcement, disrupting secure network communication.

To check for kernel-level errors, display the transform (XFRM) statistics:

``` {.language-plaintext tabindex="-1"}
# cat /proc/net/xfrm_stat
```

If any of the counters in the output, such as `XfrmInError`{.literal}, show a nonzero value, it indicates a problem with the kernel subsystem. In this case, open a [support case](https://access.redhat.com/support), and attach the output of the command along with the corresponding IKE logs.

#### [6.14.8. Displaying Libreswan logs](#displaying-libreswan-logs) {#displaying-libreswan-logs .title}

Display Libreswan logs to diagnose and troubleshoot IPsec service events and issues. Access the journal for the `ipsec`{.literal} service to gain insights into connection status and potential problems.

To display the journal, enter:

``` {.language-plaintext tabindex="-1"}
# journalctl -xeu ipsec
```

If the default logging level does not provide enough details, enable comprehensive debug logging by adding the following settings to the `config setup`{.literal} section in the `/etc/ipsec.conf`{.literal} file:

``` {.language-bash tabindex="-1"}
plutodebug=all
logfile=/var/log/pluto.log
```

Because debug logging can produce many entries, redirecting the messages to a dedicated log file can prevent the `journald`{.literal} and `systemd`{.literal} services from rate-limiting the messages.

## [Chapter 7. Using MACsec to encrypt layer-2 traffic in the same physical network](#using-macsec-to-encrypt-layer-2-traffic-in-the-same-physical-network) {#chapter-7.-using-macsec-to-encrypt-layer-2-traffic-in-the-same-physical-network .title}

Configure MACsec to encrypt Layer 2 traffic within the same physical network. This helps secure point-to-point communication between directly connected devices, such as hosts or switches.

### [7.1. How MACsec increases security](#how-macsec-increases-security) {#how-macsec-increases-security .title}

Use Media Access Control security (MACsec) to encrypt and authenticate LAN traffic at layer 2. This removes the need to encrypt individual services at layer 7.

MACsec secures point-to-point communication between devices. For example, you can configure MACsec on the two hosts connecting your branch and central offices over a Metro-Ethernet connection to increase security.

MACsec is a layer-2 protocol that encrypts and authenticates all LAN traffic. It uses a pre-shared key to establish connections. To change this key, you must update the NetworkManager configuration on all hosts that use MACsec.

MACsec secures different traffic types over the Ethernet links, including:

-   Dynamic host configuration protocol (DHCP)
-   address resolution protocol (ARP)
-   IPv4 and IPv6 traffic
-   Any traffic over IP such as TCP or UDP

A MACsec connection uses an Ethernet device, such as a network card, Virtual Local Area Network (VLAN), or tunnel device, as a parent. You can either set an IP configuration only on the MACsec device to communicate with other hosts only by using the encrypted connection, or you can also set an IP configuration on the parent device. In this case, you can use the parent device to communicate with other hosts by using an unencrypted connection and the MACsec device for encrypted connections.

MACsec does not require any special hardware. You can use any switch, except if you want to encrypt traffic only between a host and a switch. In this scenario, the switch must also support MACsec.

You can configure MACsec for two common scenarios:

-   Host-to-host
-   Host-to-switch and switch-to-other-hosts

Important

You can use MACsec only between hosts that are in the same physical or virtual LAN.

MACsec provides these benefits:

-   Reduces the workload of managing certificates for each endpoint on each host by encrypting at layer 2 instead of individual services at layer 7.
-   Provides point-to-point security between directly connected network devices such as routers and switches.
-   No changes needed for applications and higher-layer protocols.

**Additional resources**

-   [MACsec: a different solution to encrypt network traffic](https://developers.redhat.com/blog/2016/10/14/macsec-a-different-solution-to-encrypt-network-traffic)

### [7.2. Configuring a MACsec connection by using nmcli](#configuring-a-macsec-connection-by-using-nmcli) {#configuring-a-macsec-connection-by-using-nmcli .title}

You can use the `nmcli`{.literal} utility to configure Ethernet interfaces to use MACsec. For example, you can create a MACsec connection between two hosts that are connected over Ethernet.

**Procedure**

1.  On the first host, create the connectivity association key (CAK) and connectivity-association key name (CKN) for the pre-shared key:

    a.  Create a 16-byte hexadecimal CAK:

        ``` {.language-plaintext tabindex="-1"}
        # dd if=/dev/urandom count=16 bs=1 2> /dev/null | hexdump -e '1/2 "%04x"'
        50b71a8ef0bd5751ea76de6d6c98c03a
        ```

    b.  Create a 32-byte hexadecimal CKN:

        ``` {.language-plaintext tabindex="-1"}
        # dd if=/dev/urandom count=32 bs=1 2> /dev/null | hexdump -e '1/2 "%04x"'
        f2b4297d39da7330910a74abc0449feb45b5c0b9fc23df1430e1898fcf1c4550
        ```

2.  On both hosts, create the MACsec connection using the CAK and CKN from step 1. The values must be the same on every host in the MACsec-protected network:

    ``` {.language-plaintext tabindex="-1"}
    # nmcli connection add type macsec con-name macsec0 ifname macsec0 connection.autoconnect yes macsec.parent enp1s0 macsec.mode psk macsec.mka-cak 50b71a8ef0bd5751ea76de6d6c98c03a macsec.mka-ckn f2b4297d39da7330910a74abc0449feb45b5c0b9fc23df1430e1898fcf1c4550
    ```

3.  Configure the IP settings on the MACsec connection.

    a.  Configure the `IPv4`{.literal} settings. For example, to set a static `IPv4`{.literal} address, network mask, default gateway, and DNS server to the `macsec0`{.literal} connection, enter:

        ``` {.language-plaintext tabindex="-1"}
        # nmcli connection modify macsec0 ipv4.method manual ipv4.addresses '192.0.2.1/24' ipv4.gateway '192.0.2.254' ipv4.dns '192.0.2.253'
        ```

    b.  Configure the `IPv6`{.literal} settings. For example, to set a static `IPv6`{.literal} address, network mask, default gateway, and DNS server to the `macsec0`{.literal} connection, enter:

        ``` {.language-plaintext tabindex="-1"}
        # nmcli connection modify macsec0 ipv6.method manual ipv6.addresses '2001:db8:1::1/32' ipv6.gateway '2001:db8:1::fffe' ipv6.dns '2001:db8:1::fffd'
        ```

4.  Activate the connection:

    ``` {.language-plaintext tabindex="-1"}
    # nmcli connection up macsec0
    ```

**Verification**

1.  Verify that the traffic on the parent interface is encrypted. The output shows encrypted MACsec frames:

    ``` {.language-plaintext tabindex="-1"}
    # tcpdump -nn -i enp1s0
    ```

2.  Optional: Display the unencrypted traffic on the MACsec interface:

    ``` {.language-plaintext tabindex="-1"}
    # tcpdump -nn -i macsec0
    ```

3.  Display MACsec statistics:

    ``` {.language-plaintext tabindex="-1"}
    # ip macsec show
    ```

4.  Display individual counters for each type of protection: integrity-only (encrypt off) and encryption (encrypt on)

    ``` {.language-plaintext tabindex="-1"}
    # ip -s macsec show
    ```

**Additional resources**

-   [MACsec: a different solution to encrypt network traffic](https://developers.redhat.com/blog/2016/10/14/macsec-a-different-solution-to-encrypt-network-traffic)

### [7.3. Configuring a MACsec connection by using nmstatectl](#configuring-a-macsec-connection-by-using-nmstatectl) {#configuring-a-macsec-connection-by-using-nmstatectl .title}

You can use the declarative Nmstate API to configure Ethernet interfaces to use MACsec. Nmstate ensures that the result matches the configuration file or rolls back the changes.

**Prerequisites**

-   A physical or virtual Ethernet Network Interface Controller (NIC) exists in the server configuration.
-   The `nmstate`{.literal} package is installed.

**Procedure**

1.  On the first host, create the connectivity association key (CAK) and connectivity-association key name (CKN) for the pre-shared key:

    a.  Create a 16-byte hexadecimal CAK:

        ``` {.language-plaintext tabindex="-1"}
        # dd if=/dev/urandom count=16 bs=1 2> /dev/null | hexdump -e '1/2 "%04x"'
        50b71a8ef0bd5751ea76de6d6c98c03a
        ```

    b.  Create a 32-byte hexadecimal CKN:

        ``` {.language-plaintext tabindex="-1"}
        # dd if=/dev/urandom count=32 bs=1 2> /dev/null | hexdump -e '1/2 "%04x"'
        f2b4297d39da7330910a74abc0449feb45b5c0b9fc23df1430e1898fcf1c4550
        ```

2.  On both hosts that you want to connect over a MACsec connection, complete the following steps:

    a.  Create a YAML file, for example `create-macsec-connection.yml`{.literal}, with the following settings:

        ``` {.language-plaintext tabindex="-1"}
        ---
        routes:
          config:
          - destination: 0.0.0.0/0
            next-hop-interface: macsec0
            next-hop-address: 192.0.2.2
            table-id: 254
          - destination: 192.0.2.2/32
            next-hop-interface: macsec0
            next-hop-address: 0.0.0.0
            table-id: 254
        dns-resolver:
          config:
            search:
            - example.com
            server:
            - 192.0.2.200
            - 2001:db8:1::ffbb
        interfaces:
        - name: macsec0
          type: macsec
          state: up
          ipv4:
            enabled: true
            address:
            - ip: 192.0.2.1
              prefix-length: 32
          ipv6:
            enabled: true
            address:
            - ip: 2001:db8:1::1
              prefix-length: 64
          macsec:
            encrypt: true
            base-iface: enp0s1
            mka-cak: 50b71a8ef0bd5751ea76de6d6c98c03a
            mka-ckn: f2b4297d39da7330910a74abc0449feb45b5c0b9fc23df1430e1898fcf1c4550
            port: 0
            validation: strict
            send-sci: true
        ```

        Use the CAK and CKN generated in step 1 in the `mka-cak`{.literal} and `mka-ckn`{.literal} parameters. The values must be the same on every host in the MACsec-protected network.

3.  Apply the settings to the system:

    ``` {.language-plaintext tabindex="-1"}
    # nmstatectl apply create-macsec-connection.yml
    ```

**Verification**

1.  Verify the MACsec interface is active and configured correctly:

    ``` {.language-plaintext tabindex="-1"}
    # nmstatectl show macsec0
    ```

    The output displays the MACsec interface configuration including the encryption status.

2.  Verify that the traffic on the parent interface is encrypted. The output shows encrypted MACsec frames:

    ``` {.language-plaintext tabindex="-1"}
    # tcpdump -nn -i enp0s1
    ```

3.  Optional: Display the unencrypted traffic:

    ``` {.language-plaintext tabindex="-1"}
    # tcpdump -nn -i macsec0
    ```

4.  Display MACsec statistics:

    ``` {.language-plaintext tabindex="-1"}
    # ip macsec show
    ```

5.  Display individual counters for each type of protection: integrity-only (encrypt off) and encryption (encrypt on)

    ``` {.language-plaintext tabindex="-1"}
    # ip -s macsec show
    ```

**Additional resources**

-   [MACsec: a different solution to encrypt network traffic](https://developers.redhat.com/blog/2016/10/14/macsec-a-different-solution-to-encrypt-network-traffic)

## [Chapter 8. Securing network services](#securing-network-services) {#chapter-8.-securing-network-services .title}

Harden and monitor network services to protect your system against various risks. Turning off unused services helps limit exposure.

Red Hat Enterprise Linux supports many different types of network servers. Their network services can expose the system to various kinds of attacks. These include denial-of-service (DoS), distributed denial-of-service (DDoS), script vulnerability, and buffer overflow attacks.

To increase system security against attacks, it is crucial to monitor the active network services you use. For example, when a network service runs on a machine, its daemon listens for connections on network ports. This can reduce security. To limit network exposure to attacks, turn off all unused services, ports, and networking capabilities.

### [8.1. Securing the rpcbind service](#securing-the-rpcbind-service) {#securing-the-rpcbind-service .title}

You can secure `rpcbind`{.literal} by restricting access to all networks and defining specific exceptions by using firewall rules on the server.

The `rpcbind`{.literal} service is a dynamic port-assignment daemon for remote procedure calls (RPC) services such as Network Information Service (NIS) and Network File System (NFS). Because it has weak authentication mechanisms and can assign a wide range of ports for the services it controls, secure `rpcbind`{.literal}.

Note

-   The `rpcbind`{.literal} service is required on `NFSv3`{.literal} servers.
-   The `rpcbind`{.literal} service is not required on `NFSv4`{.literal}.

**Prerequisites**

-   The `rpcbind`{.literal} package is installed.
-   The `firewalld`{.literal} package is installed and the service is running.

**Procedure**

1.  Add firewall rules, for example:

    -   Limit TCP connection and accept packages only from the `192.168.0.0/24`{.literal} host on port `111`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --add-rich-rule='rule family="ipv4" port port="111" protocol="tcp" source address="192.168.0.0/24" invert="True" drop'
        ```

    -   Limit TCP connection and accept packages only from local host on port `111`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --add-rich-rule='rule family="ipv4" port port="111" protocol="tcp" source address="127.0.0.1" accept'
        ```

    -   Limit UDP connection and accept packages only from the `192.168.0.0/24`{.literal} host on port `111`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="111" protocol="udp" source address="192.168.0.0/24" invert="True" drop'
        ```

        To make the firewall settings permanent, use the `--permanent`{.literal} option when adding firewall rules.

2.  Reload the firewall to apply the new rules:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

**Verification**

-   List the firewall rules:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-rich-rule
    rule family="ipv4" port port="111" protocol="tcp" source address="192.168.0.0/24" invert="True" drop
    rule family="ipv4" port port="111" protocol="tcp" source address="127.0.0.1" accept
    rule family="ipv4" port port="111" protocol="udp" source address="192.168.0.0/24" invert="True" drop
    ```

**Troubleshooting**

-   If NFS clients cannot connect after applying the firewall rules, verify that the client IP addresses are within the allowed subnet:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-all
    ```

    Check that the rich rules allow the client's source address.

-   If clients from the allowed subnet still cannot connect, verify that the `rpcbind`{.literal} service is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status rpcbind
    ```

-   If firewall changes are not taking effect, verify that the rules were made permanent:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --list-rich-rules
    ```

    If the rules are missing, re-add them with the `--permanent`{.literal} option and reload the firewall.

-   If you added rules without `--permanent`{.literal} and then reloaded, the rules are lost. Use `--runtime-to-permanent`{.literal} to save current runtime rules:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --runtime-to-permanent
    ```

**Additional resources**

-   [Configuring an NFSv4-only server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/deploying-an-nfs-server#configuring-an-nfsv4-only-server)
-   [Using and configuring firewalld](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/using-and-configuring-firewalld)

### [8.2. Securing the rpc.mountd service](#securing-the-rpc-mountd-service) {#securing-the-rpc.mountd-service .title}

The `rpc.mountd`{.literal} daemon implements the server side of the NFS mount protocol. The NFS mount protocol is used by NFS version 3 (RFC 1813).

You can secure the `rpc.mountd`{.literal} service by adding firewall rules. Restrict access to all networks and define specific exceptions.

**Prerequisites**

-   The `rpc.mountd`{.literal} package is installed.
-   The `firewalld`{.literal} package is installed and the service is running.

**Procedure**

1.  Add firewall rules with the `--permanent`{.literal} option to make them persistent across reboots.

    Examples:

    -   Drop `mountd`{.literal} connections from the `192.168.0.0/24`{.literal} network:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-rich-rule 'rule family="ipv4" service name="mountd" source address="192.168.0.0/24" invert="True" drop'
        ```

    -   Accept `mountd`{.literal} connections from the local host:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-rich-rule 'rule family="ipv4" source address="127.0.0.1" service name="mountd" accept'
        ```

2.  Reload the firewall to apply the new rules:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

**Verification**

-   List the firewall rules:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-rich-rule
    rule family="ipv4" service name="mountd" source address="192.168.0.0/24" invert="True" drop
    rule family="ipv4" source address="127.0.0.1" service name="mountd" accept
    ```

**Troubleshooting**

-   If NFS clients cannot mount file systems after applying the firewall rules, verify that the client IP addresses are within the allowed subnet:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-all
    ```

    Check that the rich rules allow the client's source address.

-   If clients from the allowed subnet still cannot mount, verify that the `rpc.mountd`{.literal} service is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status nfs-mountd
    ```

-   If firewall changes are not taking effect, verify that the rules are applied with the `--permanent`{.literal} option and the firewall is reloaded.

-   To debug firewall blocking, temporarily enable logging for dropped packets:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --set-log-denied=all
    # journalctl -f -u firewalld
    ```

    Attempt the NFS mount from the client and check the logs for dropped packets. Disable logging after troubleshooting:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --set-log-denied=off
    ```

**Additional resources**

-   [Using and configuring firewalld](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/using-and-configuring-firewalld)

### [8.3. Securing the NFS service](#securing-the-nfs-service) {#securing-the-nfs-service .title}

Secure Network File System (NFS) by using Kerberos authentication and encryption for file system operations. Proper security configuration helps protect remote hosts mounting file systems over a network.

When using NFSv4 with Network Address Translation (NAT) or a firewall, you can turn off the delegations by modifying the `/etc/default/nfs`{.literal} file. Delegation is a technique by which the server delegates the management of a file to a client. In contrast, NFSv3 do not use Kerberos for locking and mounting files.

The NFS service sends the traffic using TCP in all versions of NFS. The service supports Kerberos user and group authentication, as part of the `RPCSEC_GSS`{.literal} kernel module.

NFS allows remote hosts to mount file systems over a network and interact with those file systems as if they are mounted locally. You can merge the resources on centralized servers and additionally customize NFS mount options in the `/etc/nfsmount.conf`{.literal} file when sharing the file systems.

#### [8.3.1. Export options for securing an NFS server](#export-options-for-securing-an-nfs-server) {#export-options-for-securing-an-nfs-server .title}

Use export options in the `/etc/exports`{.literal} file to define which hosts can access exported file systems and the permissions they hold. This helps control access and limits security risks.

Configure which file systems to export and which hosts can access them in the `/etc/exports`{.literal} file.

You can use the following export options on the `/etc/exports`{.literal} file:

`ro`{.literal}
:   Exports the NFS volume as read-only.

`rw`{.literal}
:   Controls permission for read and write requests on the NFS volume. Use this option cautiously, as granting write access increases the risk of attacks. If your scenario requires mounting the directories with the `rw`{.literal} option, make sure they are not writable for all users to reduce possible risks.

`root_squash`{.literal}
:   Maps requests from `uid`{.literal}/`gid`{.literal} 0 to the anonymous `uid`{.literal}/`gid`{.literal}. This does not apply to any other UIDs or GIDs that might be equally sensitive, such as the `bin`{.literal} user or the `staff`{.literal} group.

`no_root_squash`{.literal}
:   Turns off root squashing. By default, NFS shares change the `root`{.literal} user to the `nobody`{.literal} user, which is an unprivileged user account. This changes the owner of all the `root`{.literal}-created files to `nobody`{.literal}, which prevents the uploading of programs with the `setuid`{.literal} bit set. When using the `no_root_squash`{.literal} option, remote root users can change any file on the shared file system and leave applications infected by trojans for other users.

`secure`{.literal}
:   Restricts exports to reserved ports. By default, the server allows client communication only through reserved ports. However, it is easy for anyone to become a `root`{.literal} user on a client on many networks, so it is rarely safe for the server to assume that communication through a reserved port is privileged. Therefore, restricting to reserved ports is of limited value; it is better to rely on Kerberos, firewalls, and limiting exports to particular clients.

See the `exports(5)`{.literal} and `nfs(5)`{.literal} man pages on your system for more information.

You can check the shared directories on your system by entering the `showmount -e `{.literal}*`<hostname>`{.literal}* command.

Warning

Extra spaces in the syntax of the `/etc/exports`{.literal} file can lead to significant changes in the configuration.

In the following example, the `/tmp/nfs/`{.literal} directory is shared with the `bob.example.com`{.literal} host and has read and write permissions:

``` {.language-plaintext tabindex="-1"}
/tmp/nfs/     bob.example.com(rw)
```

The following example is the same as the previous one, but shares the same directory to the `bob.example.com`{.literal} host with read-only permissions and shares it to the *world* with read and write permissions due to a single space character after the hostname:

``` {.language-plaintext tabindex="-1"}
/tmp/nfs/     bob.example.com (rw)
```

Additionally, consider the following best practices when exporting an NFS server:

-   Exporting home directories is a risk because some applications store passwords in plain text or in a weakly encrypted format. You can reduce the risk by reviewing and improving the application code.
-   Some users do not set passwords on SSH keys, which again leads to risks with home directories. You can reduce these risks by enforcing the use of passwords or using Kerberos.
-   Restrict the NFS exports only to required clients. Use the `showmount -e`{.literal} command on the NFS server to review what the server is exporting. Do not export anything that is not specifically required.
-   Do not allow unnecessary users to log in to a server to reduce the risk of attacks. You can periodically check who and what can access the server.

Warning

Export an entire file system because exporting a subdirectory of a file system is not secure. An attacker might access the unexported part of a partially-exported file system.

**Additional resources**

-   [Using Ansible to automount NFS shares for IdM users](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-ansible-to-automount-nfs-shares-for-idm-users)

#### [8.3.2. Mount options for securing an NFS client](#mount-options-for-securing-an-nfs-client) {#mount-options-for-securing-an-nfs-client .title}

You can apply mount options when configuring an NFS client to help enforce stronger security. These settings ensure that the client/server communication uses required security protocols such as Kerberos.

The following options to the `mount`{.literal} command might increase the security of NFS-based clients:

`nosuid`{.literal}
:   Use the `nosuid`{.literal} option to disable the `set-user-identifier`{.literal} or `set-group-identifier`{.literal} bits. This prevents remote users from gaining higher privileges by running a `setuid`{.literal} program, and you can use this option in opposition to `setuid`{.literal} option.

`noexec`{.literal}
:   Use the `noexec`{.literal} option to disable all executable files on the client. Use this to prevent users from accidentally executing files placed in the shared file system.

`nodev`{.literal}
:   Use the `nodev`{.literal} option to prevent the client's processing of device files as a hardware device.

`resvport`{.literal}
:   Use the `resvport`{.literal} option to restrict communication to a reserved port, and you can use a privileged source port to communicate with the server. The reserved ports are reserved for privileged users and processes such as the `root`{.literal} user.

`sec`{.literal}
:   Use the `sec`{.literal} option on the NFS server to choose the RPCGSS security method for accessing files on the mount point. Valid security methods are `none`{.literal}, `sys`{.literal}, `krb5`{.literal}, `krb5i`{.literal}, and `krb5p`{.literal}.

Important

The MIT Kerberos libraries provided by the `krb5-libs`{.literal} package do not support the Data Encryption Standard (DES) algorithm in new deployments. DES is deprecated and disabled by default in Kerberos libraries because of security and compatibility reasons. Use newer and more secure algorithms instead of DES, unless your environment requires DES for compatibility reasons.

**Additional resources**

-   [Frequently-used NFS mount options](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/mounting-nfs-shares#frequently-used-nfs-mount-options)

#### [8.3.3. Securing NFS with firewall](#securing-nfs-with-firewall) {#securing-nfs-with-firewall .title}

To secure the firewall on an NFS server, keep only the required ports open. Do not use the NFS connection port numbers for any other service.

**Prerequisites**

-   The `nfs-utils`{.literal} package is installed.
-   The `firewalld`{.literal} package is installed and running.

**Procedure**

1.  Configure static ports for NFS services to simplify firewall rules. The `rpcbind`{.literal} service assigns NFS ports dynamically by default. Specify static ports in the `/etc/nfs.conf`{.literal} file:

    For NFSv3, configure these services:

    a.  Set TCP and UDP port for `mountd`{.literal} (`rpc.mountd`{.literal}) in the `[mountd]`{.literal} section in `port=`{.literal}*`<value>`{.literal}* format.
    b.  Set TCP and UDP port for `statd`{.literal} (`rpc.statd`{.literal}) in the `[statd]`{.literal} section in `port=`{.literal}*`<value>`{.literal}* format.
    c.  Set TCP port for the lock manager in the `[lockd]`{.literal} section in `port=`{.literal}*`<value>`{.literal}* format. Alternatively, use the `nlm_tcpport`{.literal} option in the `/etc/modprobe.d/lockd.conf`{.literal} file.
    d.  Set UDP port for the lock manager in the `[lockd]`{.literal} section in `udp-port=`{.literal}*`<value>`{.literal}* format. Alternatively, use the `nlm_udpport`{.literal} option in the `/etc/modprobe.d/lockd.conf`{.literal} file.

    For NFSv4, only port `2049`{.literal} is required.

2.  Open the required ports in the firewall:

    For NFSv4:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=2049/tcp
    ```

    For NFSv3, also open the ports you configured in step 1:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=2049/tcp
    # firewall-cmd --permanent --add-port=<mountd_port>/tcp
    # firewall-cmd --permanent --add-port=<mountd_port>/udp
    # firewall-cmd --permanent --add-port=<statd_port>/tcp
    # firewall-cmd --permanent --add-port=<statd_port>/udp
    # firewall-cmd --permanent --add-port=<lockd_tcp_port>/tcp
    # firewall-cmd --permanent --add-port=<lockd_udp_port>/udp
    ```

3.  Reload the firewall to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

**Verification**

1.  List the active ports and RPC programs on the NFS server:

    ``` {.language-plaintext tabindex="-1"}
    $ rpcinfo -p
    ```

2.  Verify the firewall rules:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-ports
    ```

### [8.4. Securing the FTP service](#securing-the-ftp-service) {#securing-the-ftp-service .title}

You can use the File Transfer Protocol (FTP) to transfer files over a network. Because all FTP transactions with the server, including user authentication, are unencrypted, make sure it is configured securely.

Red Hat Enterprise Linux provides two FTP servers:

Red Hat Content Accelerator (`tux`{.literal})
:   A kernel-space web server with FTP capabilities.

Very Secure FTP Daemon (`vsftpd`{.literal})
:   A standalone, security-oriented implementation of the FTP service.

The following security guidelines are for setting up the `vsftpd`{.literal} FTP service.

#### [8.4.1. Securing the FTP greeting banner](#securing-the-ftp-greeting-banner) {#securing-the-ftp-greeting-banner .title}

When a user connects to the FTP service, the server displays a greeting banner that, by default, includes version information. Attackers might use this information to identify vulnerabilities in the system. You can hide this information by changing the default banner.

You can define a custom banner by editing the `/etc/banners/ftp.msg`{.literal} file to either directly include a single-line message, or to refer to a separate file, which can contain a multi-line message.

**Procedure**

-   To define a single line message, add the following option to the `/etc/vsftpd/vsftpd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    ftpd_banner=Hello, all activity on ftp.example.com is logged.
    ```

-   To define a message in a separate file:

    -   Create a `.msg`{.literal} file which contains the banner message, for example `/etc/banners/`{.literal}*`ftp`{.literal}*`.msg`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        ######### Hello, all activity on ftp.example.com is logged. #########
        ```

        To simplify the management of multiple banners, place all banners into the `/etc/banners/`{.literal} directory.

    -   Add the path to the banner file to the `banner_file`{.literal} option in the `/etc/vsftpd/vsftpd.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        banner_file=/etc/banners/ftp.msg
        ```

**Verification**

-   Display the modified banner:

    ``` {.language-plaintext tabindex="-1"}
    $ ftp localhost
    Trying ::1…
    Connected to localhost (::1).
    Hello, all activity on ftp.example.com is logged.
    ```

#### [8.4.2. Configuring write-only anonymous uploads in FTP](#preventing-anonymous-access-and-uploads-in-ftp) {#configuring-write-only-anonymous-uploads-in-ftp .title}

Configure anonymous FTP access to allow uploads. Prevent read access to increase security.

By default, the `vsftpd`{.literal} package creates the `/var/ftp/`{.literal} directory tree. Anonymous users have read-only permissions. Configure a write-only directory where anonymous users can upload files. They cannot read or modify existing content.

**Procedure**

1.  Create a write-only directory in the `/var/ftp/pub/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /var/ftp/pub/upload
    # chmod 730 /var/ftp/pub/upload
    # ls -ld /var/ftp/pub/upload
    drwx-wx---. 2 root ftp 4096 Nov 14 22:57 /var/ftp/pub/upload
    ```

2.  Add the following lines to the `/etc/vsftpd/vsftpd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    anon_upload_enable=YES
    anonymous_enable=YES
    ```

3.  Optional: Enable SELinux boolean attributes `allow_ftpd_anon_write`{.literal} and `allow_ftpd_full_access`{.literal} if your system has SELinux enabled and enforcing.

    Warning

    Configuring directories for anonymous read and write access increases risk. The server might become a repository for stolen software.

#### [8.4.3. Security tips for FTP user accounts](#securing-user-accounts-for-ftp) {#security-tips-for-ftp-user-accounts .title}

FTP transmits usernames and passwords unencrypted over insecure networks for authentication. You can improve the security of FTP by denying system users access to the server from their user accounts.

Perform as many of the following configuration steps as applicable for your configuration:

-   Disable all user accounts in the `vsftpd`{.literal} server, by adding the following line to the `/etc/vsftpd/vsftpd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    local_enable=NO
    ```

-   Disable FTP access for specific accounts or specific groups of accounts, such as the `root`{.literal} user and users with `sudo`{.literal} privileges, by adding the usernames to the `/etc/pam.d/vsftpd`{.literal} PAM configuration file.

-   Disable user accounts, by adding the usernames to the `/etc/vsftpd/ftpusers`{.literal} file.

### [8.5. Securing HTTP servers](#securing-http-servers) {#securing-http-servers .title}

Harden your HTTP servers, such as Apache and Nginx, to mitigate security risks. This involves configuring security options in the main configuration files and checking that scripts run correctly.

#### [8.5.1. Security enhancements in httpd.conf](#security-enhancements-in-httpd-conf) {#security-enhancements-in-httpd.conf .title}

You can enhance the security of the Apache HTTP server by configuring security options in the `/etc/httpd/conf/httpd.conf`{.literal} file.

In the `/etc/httpd/conf/httpd.conf`{.literal} file, you can configure the following options:

`FollowSymLinks`{.literal}
:   This directive is enabled by default and follows symbolic links in the directory.

`Indexes`{.literal}
:   This directive is enabled by default. Disable this directive to prevent visitors from browsing files on the server.

`UserDir`{.literal}
:   This directive is disabled by default because it can confirm the presence of a user account on the system. To activate user directory browsing for all user directories other than `/root/`{.literal}, use the `UserDir enabled`{.literal} and `UserDir disabled`{.literal} root directives. To add users to the list of disabled accounts, add a space-delimited list of users on the `UserDir disabled`{.literal} line.

`ServerTokens`{.literal}

:   This directive controls the server response header field which is sent back to clients. You can use the following parameters to customize the information:

    `ServerTokens Full`{.literal}

    :   Provides all available information such as web server version number, server operating system details, installed Apache modules, for example:

        ``` {.language-plaintext tabindex="-1"}
        Apache/2.4.37 (Red Hat Enterprise Linux) MyMod/1.2
        ```

    `ServerTokens Full-Release`{.literal}

    :   Provides all available information with release versions, for example:

        ``` {.language-plaintext tabindex="-1"}
        Apache/2.4.37 (Red Hat Enterprise Linux) (Release 41.module+el8.5.0+11772+c8e0c271)
        ```

    `ServerTokens Prod / ServerTokens ProductOnly`{.literal}

    :   Provides the web server name, for example:

        ``` {.language-plaintext tabindex="-1"}
        Apache
        ```

    `ServerTokens Major`{.literal}

    :   Provides the web server major release version, for example:

        ``` {.language-plaintext tabindex="-1"}
        Apache/2
        ```

    `ServerTokens Minor`{.literal}

    :   Provides the web server minor release version, for example:

        ``` {.language-plaintext tabindex="-1"}
        Apache/2.4
        ```

    `ServerTokens Min`{.literal} / `ServerTokens Minimal`{.literal}

    :   Provides the web server minimal release version, for example:

        ``` {.language-plaintext tabindex="-1"}
        Apache/2.4.37
        ```

    `ServerTokens OS`{.literal}

    :   Provides the web server release version and operating system, for example:

        ``` {.language-plaintext tabindex="-1"}
        Apache/2.4.37 (Red Hat Enterprise Linux)
        ```

        Use the `ServerTokens Prod`{.literal} option to reduce the risk of attackers gaining any valuable information about your system.

Important

Do not remove the `IncludesNoExec`{.literal} directive. By default, the Server Side Includes (SSI) module cannot run commands. Changing this can allow an attacker to enter commands on the system.

##### [8.5.1.1. Securing CGI and script directories](#securing_cgi_and_script_directories) {#securing-cgi-and-script-directories .title}

Ensure that only the `root`{.literal} user has write permissions to directories containing scripts or Common Gateway Interfaces (CGI):

``` {.language-plaintext tabindex="-1"}
# chown root <directory_name>
# chmod 755 <directory_name>
```

Always verify that all scripts work correctly before putting them into production.

##### [8.5.1.2. Removing httpd modules](#removing_httpd_modules) {#removing-httpd-modules .title}

You can remove the `httpd`{.literal} modules to limit the functionality of the HTTP server. To do so, edit configuration files in the `/etc/httpd/conf.modules.d/`{.literal} or `/etc/httpd/conf.d/`{.literal} directory. For example, to remove the proxy module:

``` {.language-plaintext tabindex="-1"}
echo '# All proxy modules disabled' > /etc/httpd/conf.modules.d/00-proxy.conf
```

**Additional resources**

-   [Configuring the Apache HTTP web server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/setting-up-the-apache-http-web-server)
-   [Customizing the SELinux policy for the Apache HTTP server in a non-standard configuration](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/configuring-selinux-for-applications-and-services-with-non-standard-configurations#customizing-the-selinux-policy-for-the-apache-http-server-in-a-non-standard-configuration)

#### [8.5.2. Nginx server configuration hardening](#securing-the-nginx-server-configuration) {#nginx-server-configuration-hardening .title}

Harden your Nginx HTTP and proxy server configuration by adjusting security options. This helps protect your system against common web application vulnerabilities.

Configure the following security options to protect against common web application vulnerabilities:

-   To disable version strings, modify the `server_tokens`{.literal} configuration option:

    ``` {.language-plaintext tabindex="-1"}
    server_tokens off;
    ```

    This option stops displaying additional details such as server version number. This configuration displays only the server name in all requests served by Nginx, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ curl -sI http://localhost | grep Server
    Server: nginx
    ```

-   Add security headers in your server or location blocks within `/etc/nginx/nginx.conf`{.literal} or `/etc/nginx/conf.d/*.conf`{.literal} files:

    -   For example, the `X-Frame-Options`{.literal} header option denies any page outside of your domain to frame any content served by Nginx, mitigating clickjacking attacks:

        ``` {.language-plaintext tabindex="-1"}
        add_header X-Frame-Options "SAMEORIGIN";
        ```

    -   For example, the `x-content-type`{.literal} header prevents MIME-type sniffing in certain older browsers:

        ``` {.language-plaintext tabindex="-1"}
        add_header X-Content-Type-Options nosniff;
        ```

    -   For example, the `X-XSS-Protection`{.literal} header enables Cross-Site Scripting (XSS) filtering, which prevents browsers from rendering potentially malicious content included in a response by Nginx:

        ``` {.language-plaintext tabindex="-1"}
        add_header X-XSS-Protection "1; mode=block";
        ```

-   You can limit the services exposed to the public and limit what they do and accept from the visitors, for example:

    ``` {.language-plaintext tabindex="-1"}
    limit_except GET {
        allow 192.168.1.0/32;
        deny  all;
    }
    ```

    The snippet will limit access to all methods except `GET`{.literal} and `HEAD`{.literal}.

-   You can disable HTTP methods, for example:

    ``` {.language-plaintext tabindex="-1"}
    # Allow GET, PUT, POST; return "405 Method Not Allowed" for all others.
    if ( $request_method !~ ^(GET|PUT|POST)$ ) {
        return 405;
    }
    ```

-   Configure TLS to protect data served by your Nginx web server. Serve content over HTTPS only. You can generate a secure configuration profile for enabling TLS in your Nginx server using the Mozilla SSL Configuration Generator. The generated configuration ensures that known vulnerable protocols, ciphers, and hashing algorithms are disabled. Use the SSL Server Test to verify that your configuration meets modern security requirements.

**Additional resources**

-   [Planning and implementing TLS](#planning-and-implementing-tls "Chapter 4. Planning and implementing TLS")
-   [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)
-   [SSL Server Test](https://www.ssllabs.com/ssltest/)

### [8.6. Securing PostgreSQL by limiting access to authenticated local users](#securing-postgresql-by-limiting-access-to-authenticated-local-users) {#securing-postgresql-by-limiting-access-to-authenticated-local-users .title}

Secure your PostgreSQL database by configuring client authentication. Limit access to authenticated local users only. This reduces unauthorized access and attack risks.

PostgreSQL is an object-relational database management system (DBMS). The `postgresql-server`{.literal} package provides PostgreSQL in Red Hat Enterprise Linux.

The `pg_hba.conf`{.literal} configuration file specifies client authentication settings. This file is stored in the database cluster's data directory. Configure PostgreSQL for host-based authentication using this procedure.

**Procedure**

1.  Install PostgreSQL:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install postgresql-server
    ```

2.  Initialize a database storage area using one of the following options:

    a.  Use the `initdb`{.literal} utility:

        ``` {.language-plaintext tabindex="-1"}
        $ initdb -D /home/postgresql/db1/
        ```

        This directory contains all database data. It also contains the client authentication configuration file.

    b.  Use the `postgresql-setup`{.literal} script:

        ``` {.language-plaintext tabindex="-1"}
        $ postgresql-setup --initdb
        ```

        By default, the script uses the `/var/lib/pgsql/data/`{.literal} directory. This script helps with basic database cluster administration.

3.  Configure local authentication in the `pg_hba.conf`{.literal} file. By default, the file contains:

    ``` {.language-plaintext tabindex="-1"}
    local   all             all                                     trust
    ```

    This `trust`{.literal} authentication allows any local user to access any database. To require authentication, change `trust`{.literal} to another method. Use `peer`{.literal} to authenticate based on system username. Use `md5`{.literal} for password authentication:

    ``` {.language-plaintext tabindex="-1"}
    local   all             all                                     peer
    ```

    You can disable local socket connections entirely. Remove the `local`{.literal} line entry if you use layered applications that create database users without corresponding local users.

4.  Restart the database to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart postgresql
    ```

    This command updates the database. It also verifies the syntax of the configuration file.

**Verification**

1.  Verify the authentication setting in the configuration file:

    ``` {.language-plaintext tabindex="-1"}
    $ grep "^local" /var/lib/pgsql/data/pg_hba.conf
    local   all             all                                     peer
    ```

2.  Test the authentication by attempting to connect as a local user with a matching database user:

    ``` {.language-plaintext tabindex="-1"}
    $ psql -U postgres -d postgres
    psql (16.4)
    Type "help" for help.

    postgres=#
    ```

    The connection succeeds because the local system user matches the database user.

3.  Test that unauthorized users cannot connect by attempting to connect as a non-existent database user:

    ``` {.language-plaintext tabindex="-1"}
    $ psql -U nonexistent -d postgres
    psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  Peer authentication failed for user "nonexistent"
    ```

    The connection is rejected because peer authentication requires a matching system user.

### [8.7. Securing the Memcached service](#securing-the-memcached-service) {#securing-the-memcached-service .title}

Secure the Memcached caching service against denial-of-service (DoS) attacks and unauthorized access. Configure it to accept only local traffic. Enable user authentication. This prevents DDoS amplification. Only authorized clients can access stored data.

Memcached is an open source, high-performance, distributed memory object caching system. It improves the performance of dynamic web applications by lowering database load.

Memcached is an in-memory key-value store for small data chunks such as strings and objects. It stores results from database calls, API calls, or page rendering. Memcached assigns memory from underutilized areas to applications that need more memory.

In 2018, DDoS amplification vulnerabilities were discovered in Memcached servers exposed to the public internet. These attacks exploited Memcached communication when using the UDP protocol for transport. The attack was effective due to the high amplification ratio. A request of a few hundred bytes could generate a response of a few megabytes or hundreds of megabytes.

Do not expose the `memcached`{.literal} service to the public internet in most situations. Public exposure causes security problems. Remote attackers can leak or modify information stored in Memcached.

#### [8.7.1. Memcached hardening against DDoS attacks](#hardening-memcached-against-ddos) {#memcached-hardening-against-ddos-attacks .title}

Harden Memcached against distributed denial-of-service (DDoS) attacks to prevent attackers from overwhelming the service.

Perform these steps as applicable to your configuration:

-   Limit access to your local network. Configure your firewall to block external traffic. Remove the default port `11211`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --remove-port=11211/udp
    # firewall-cmd --runtime-to-permanent
    ```

-   Limit Memcached to local connections only. Edit the `OPTIONS`{.literal} value in `/etc/sysconfig/memcached`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    OPTIONS="-l 127.0.0.1,::1"
    ```

-   Enable Simple Authentication and Security Layer (SASL) authentication:

    1.  Create `/etc/sasl2/memcached.conf`{.literal} and set the SASL database path:

        ``` {.language-plaintext tabindex="-1"}
        sasldb_path: /path.to/memcached.sasldb
        ```

    2.  Add an account in the SASL database:

        ``` {.language-plaintext tabindex="-1"}
        # saslpasswd2 -a memcached -c cacheuser -f /path.to/memcached.sasldb
        ```

    3.  Set permissions for the `memcached`{.literal} user and group:

        ``` {.language-plaintext tabindex="-1"}
        # chown memcached:memcached /path.to/memcached.sasldb
        ```

    4.  Enable SASL support. Add `-S`{.literal} to `OPTIONS`{.literal} in `/etc/sysconfig/memcached`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        OPTIONS="-S"
        ```

    5.  Restart Memcached:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart memcached
        ```

    6.  Add the SASL username and password to your application's Memcached client configuration.

-   Encrypt communication between Memcached clients and servers with TLS:

    1.  Enable TLS encryption. Add `-Z`{.literal} to `OPTIONS`{.literal} in `/etc/sysconfig/memcached`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        OPTIONS="-Z"
        ```

    2.  Add the certificate chain file path. Append `-o ssl_chain_cert=/path/to/cert.pem`{.literal} to `OPTIONS`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        OPTIONS="-Z -o ssl_chain_cert=/path/to/cert.pem"
        ```

    3.  Add the private key file path. Append `-o ssl_key=/path/to/key.pem`{.literal} to `OPTIONS`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        OPTIONS="-Z -o ssl_chain_cert=/path/to/cert.pem -o ssl_key=/path/to/key.pem"
        ```

### [8.8. Securing the Postfix service](#securing-the-postfix-service) {#securing-the-postfix-service .title}

Secure the Postfix mail transfer agent by configuring it to use encryption and applying settings that mitigate risks from various attacks. This involves configuring SMTP Authentication (AUTH) using SASL and setting limits to reduce vulnerability to denial-of-service (DoS) attacks.

Postfix is a mail transfer agent (MTA) that uses the Simple Mail Transfer Protocol (SMTP) to deliver electronic messages between other MTAs and to email clients or delivery agents. Although MTAs can encrypt traffic between one another, they might not do so by default.

#### [8.8.1. Reducing Postfix network-related security risks](#reducing-postfix-network-related-security-risks) {#reducing-postfix-network-related-security-risks .title}

Reduce Postfix security risks related to the network by adjusting configuration options to restrict access.

To reduce the risk of attackers invading your system through the network, perform as many of the following tasks as possible:

-   Do not share the `/var/spool/postfix/`{.literal} mail spool directory on a Network File System (NFS) volume. NFSv2 and NFSv3 do not maintain control over user and group IDs, allowing users with the same UID to receive and read each other's mail. NFSv4 using Kerberos does not have this limitation because the `SECRPC_GSS`{.literal} kernel module does not use UID-based authentication. However, avoid placing the mail spool directory on NFS volumes to reduce security risks.
-   Require mail users to access Postfix using an email program only. Do not allow shell accounts on the mail server. Set all user shells in the `/etc/passwd`{.literal} file to `/sbin/nologin`{.literal}, with the possible exception of the `root`{.literal} user. This prevents users from directly accessing the mail server and reduces the attack surface.
-   To protect Postfix from a network attack, it is configured to only listen to the local loopback address by default. You can verify this by viewing the `inet_interfaces = localhost`{.literal} line in the `/etc/postfix/main.cf`{.literal} file. This ensures that Postfix only accepts mail messages, such as `cron`{.literal} job reports, from the local system and not from the network. This is the default setting and protects Postfix from a network attack. To remove the localhost restriction and allow Postfix to listen on all interfaces, set the `inet_interfaces`{.literal} parameter to `all`{.literal} in `/etc/postfix/main.cf`{.literal}.

#### [8.8.2. Postfix configuration options for limiting DoS attacks](#postfix-configuration-options-for-limiting-dos-attacks) {#postfix-configuration-options-for-limiting-dos-attacks .title}

You can limit denial-of-service (DoS) attacks by configuring certain Postfix options. This involves setting strict rate and message-size limits to protect the server from being flooded with traffic.

An attacker can flood the server with traffic or send information that triggers a crash, causing a denial-of-service (DoS) attack. You can configure your system to reduce the risk of such attacks by setting limits in the `/etc/postfix/main.cf`{.literal} file. You can change the value of the existing directives, or you can add new directives with custom values in the *`<directive>`{.literal}*` = `{.literal}*`<value>`{.literal}* format.

Use the following list of directives for limiting DoS attacks:

`smtpd_client_connection_rate_limit`{.literal}
:   Limits the maximum number of connection attempts any client can make to this service per time unit. The default value is `0`{.literal}, which means a client can make as many connections per time unit as Postfix can accept. By default, the directive excludes clients in trusted networks.

`anvil_rate_time_unit`{.literal}
:   Defines a time unit to calculate the rate limit. The default value is `60`{.literal} seconds.

`smtpd_client_event_limit_exceptions`{.literal}
:   Excludes clients from the connection and rate limit commands. By default, the directive excludes clients in trusted networks.

`smtpd_client_message_rate_limit`{.literal}
:   Defines the maximum number of message deliveries from client to request per time unit (regardless of whether or not Postfix actually accepts those messages).

`default_process_limit`{.literal}
:   Defines the default maximum number of Postfix child processes that provide a given service. You can ignore this rule for specific services in the `master.cf`{.literal} file. By default, the value is `100`{.literal}.

`queue_minfree`{.literal}
:   Defines the minimum amount of free space required to receive mail in the queue file system. The directive is currently used by the Postfix SMTP server to decide if it accepts any mail at all. By default, the Postfix SMTP server rejects `MAIL FROM`{.literal} commands when the amount of free space is less than 1.5 times the `message_size_limit`{.literal}. To specify a higher minimum free space limit, specify a `queue_minfree`{.literal} value that is at least 1.5 times the `message_size_limit`{.literal}. By default, the `queue_minfree`{.literal} value is `0`{.literal}.

`header_size_limit`{.literal}
:   Defines the maximum amount of memory in bytes for storing a message header. If a header is large, it discards the excess header. By default, the value is `102400`{.literal} bytes.

`message_size_limit`{.literal}
:   Defines the maximum size of a message, including the envelope information, in bytes. By default, the value is `10240000`{.literal} bytes.

#### [8.8.3. Configuring Postfix to use SASL](#configuring-postfix-to-use-sasl) {#configuring-postfix-to-use-sasl .title}

You can configure the Postfix mail transfer agent to use Simple Authentication and Security Layer (SASL). This strengthens authentication when sending and receiving electronic messages.

Postfix supports SASL-based SMTP Authentication (AUTH). SMTP AUTH is an extension of the Simple Mail Transfer Protocol. Currently, the Postfix SMTP server supports the SASL implementations in the following ways:

Dovecot SASL
:   The Postfix SMTP server can communicate with the Dovecot SASL implementation by using either a UNIX-domain socket or a TCP socket. Use this method if Postfix and Dovecot applications are running on separate machines.

Cyrus SASL
:   When enabled, SMTP clients must authenticate with the SMTP server by using an authentication method supported and accepted by both the server and the client.

**Prerequisites**

-   The `dovecot`{.literal} package is installed on the system

**Procedure**

1.  Configure Dovecot:

    a.  Include the following lines in the `/etc/dovecot/conf.d/10-master.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        service auth {
          unix_listener /var/spool/postfix/private/auth {
            mode = 0660
            user = postfix
            group = postfix
          }
        }
        ```

        The previous example uses UNIX-domain sockets for communication between Postfix and Dovecot. The example also assumes default Postfix SMTP server settings, which include the mail queue located in the `/var/spool/postfix/`{.literal} directory, and the application running under the `postfix`{.literal} user and group.

    b.  Optional: Configure Dovecot to listen for Postfix authentication requests through TCP:

        ``` {.language-bash tabindex="-1"}
        service auth {
          inet_listener {
              port = <port_number>
          }
        }
        ```

    c.  Specify the method that the email client uses to authenticate with Dovecot by editing the `auth_mechanisms`{.literal} parameter in `/etc/dovecot/conf.d/10-auth.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        auth_mechanisms = plain login
        ```

        The `auth_mechanisms`{.literal} parameter supports different plain text and non-plain text authentication methods.

2.  Configure Postfix by modifying the `/etc/postfix/main.cf`{.literal} file:

    a.  Enable SMTP Authentication on the Postfix SMTP server:

        ``` {.language-plaintext tabindex="-1"}
        smtpd_sasl_auth_enable = yes
        ```

    b.  Enable the use of Dovecot SASL implementation for SMTP Authentication:

        ``` {.language-plaintext tabindex="-1"}
        smtpd_sasl_type = dovecot
        ```

    c.  Provide the authentication path relative to the Postfix queue directory. Note that the use of a relative path ensures that the configuration works regardless of whether the Postfix server runs in `chroot`{.literal} or not:

        ``` {.language-plaintext tabindex="-1"}
        smtpd_sasl_path = private/auth
        ```

        This step uses UNIX-domain sockets for communication between Postfix and Dovecot.

        To configure Postfix to look for Dovecot on a different machine in case you use TCP sockets for communication, use configuration values similar to the following:

        ``` {.language-bash tabindex="-1"}
        smtpd_sasl_path = inet: <IP_address> : <port_number>
        ```

        In the previous example, replace the *`<IP_address>`{.literal}* with the IP address of the Dovecot machine and *`<port_number>`{.literal}* with the port number specified in Dovecot's `/etc/dovecot/conf.d/10-master.conf`{.literal} file.

    d.  Specify SASL mechanisms that the Postfix SMTP server makes available to clients. Note that you can specify different mechanisms for encrypted and unencrypted sessions.

        ``` {.language-plaintext tabindex="-1"}
        smtpd_sasl_security_options = noanonymous, noplaintext
        smtpd_sasl_tls_security_options = noanonymous
        ```

        The previous directives specify that during unencrypted sessions, no anonymous authentication is allowed, and no mechanisms that transmit unencrypted user names or passwords are allowed. For encrypted sessions that use TLS, only non-anonymous authentication mechanisms are allowed.

**Additional resources**

-   [Postfix SMTP server policy - SASL mechanism properties](http://www.postfix.org/SASL_README.html#smtpd_sasl_security_options)
-   [Postfix and Dovecot SASL](https://doc.dovecot.org/configuration_manual/howto/postfix_and_dovecot_sasl/)
-   [Configuring SASL authentication in the Postfix SMTP server](http://www.postfix.org/SASL_README.html#server_sasl)

## [Legal Notice](#idm140168172028816) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
