---
{"title": "Deploying mail servers", "guide": "deploying_mail_servers", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/deploying_mail_servers/index", "retrieved": "2026-11-02", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Deploying mail servers {#deploying-mail-servers .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Configuring and maintaining mail server services {#configuring-and-maintaining-mail-server-services .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140592705019120)

**Abstract**

On Red Hat Enterprise Linux, you can provide reliable and secure mail services for your customers and internal users by using the mail transport agent Postfix as SMTP service and the mail delivery agent Dovecot as IMAP and POP3 services. Both services integrate with each other and they support central backends, such as LDAP directories to store account data and to authenticate users.

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

## [Chapter 1. Configuring and maintaining a Dovecot IMAP and POP3 server](#configuring-and-maintaining-a-dovecot-imap-and-pop3-server) {#chapter-1.-configuring-and-maintaining-a-dovecot-imap-and-pop3-server .title}

Dovecot is a high-performance mail delivery agent (MDA) with a focus on security. You can use internet message access protocol (IMAP) or post office protocol version 3 (POP3)-compatible email clients to connect to a Dovecot server and read or download emails.

Key features of Dovecot:

-   The design and implementation focuses on security
-   Two-way replication support for high availability to improve the performance in large environments
-   Supports the high-performance `dbox`{.literal} mailbox format, but also `mbox`{.literal} and `Maildir`{.literal} for compatibility reasons
-   Self-healing features, such as fixing broken index files
-   Compliance with the IMAP standards
-   Workaround support to bypass bugs in IMAP and POP3 clients

### [1.1. Configuring a Dovecot server with PAM authentication](#setting-up-a-dovecot-server-with-pam-authentication) {#configuring-a-dovecot-server-with-pam-authentication .title}

Dovecot supports the Name Service Switch (NSS) interface as a user database and the Pluggable Authentication Modules (PAM) framework as an authentication back end. With this configuration, Dovecot can provide services to users who are available locally on the server through NSS.

Use PAM authentication if accounts:

-   Are defined locally in the `/etc/passwd`{.literal} file
-   Are stored in a remote database but they are available locally through the System Security Services Daemon (SSSD) or other NSS plugins.

#### [1.1.1. Installing Dovecot](#installing-dovecot_dovecot-pam) {#installing-dovecot .title}

You can install Dovecot to configure the system as an IMAP or POP3 server.

The `dovecot`{.literal} package provides the following components:

-   The `dovecot`{.literal} service and the utilities to maintain it
-   Services that Dovecot starts on demand, such as for authentication
-   Plugins, such as server-side mail filtering
-   Configuration files in the `/etc/dovecot/`{.literal} directory
-   Documentation in the `/usr/share/doc/dovecot/`{.literal} directory

**Procedure**

-   Install the `dovecot`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install dovecot
    ```

    Note

    If Dovecot is already installed and you require clean configuration files, rename or remove the `/etc/dovecot/`{.literal} directory. Afterwards, reinstall the package. Without removing the configuration files, the `dnf reinstall dovecot`{.literal} command does not reset the configuration files in `/etc/dovecot/`{.literal}.

**Next step**

-   [Configuring TLS encryption on a Dovecot server](#configuring-tls-encryption-on-a-dovecot-server_dovecot-pam "1.1.2. Configuring TLS encryption on a Dovecot server").

#### [1.1.2. Configuring TLS encryption on a Dovecot server](#configuring-tls-encryption-on-a-dovecot-server_dovecot-pam) {#configuring-tls-encryption-on-a-dovecot-server .title}

By default, Dovecot enables TLS to securely transmit credentials and data. To configure TLS, set the paths to the certificate and private key files. Increase security by generating and using Diffie-Hellman parameters for perfect forward secrecy (PFS).

**Prerequisites**

-   Dovecot is installed.

-   The following files have been copied to the listed locations on the server:

    -   The server certificate: `/etc/pki/dovecot/certs/server.example.com.crt`{.literal}
    -   The private key: `/etc/pki/dovecot/private/server.example.com.key`{.literal}
    -   The Certificate Authority (CA) certificate: `/etc/pki/dovecot/certs/ca.crt`{.literal}

-   The hostname in the `Subject DN`{.literal} field of the server certificate matches the server's fully-qualified domain name (FQDN).

-   If the Federal information processing standards (FIPS) mode is enabled, clients must either support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Set secure permissions on the private key file:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:root /etc/pki/dovecot/private/server.example.com.key
    # chmod 600 /etc/pki/dovecot/private/server.example.com.key
    ```

2.  Generate a file with Diffie-Hellman parameters:

    ``` {.language-plaintext tabindex="-1"}
    # openssl dhparam -out /etc/dovecot/dh.pem 4096
    ```

    Depending on the hardware and entropy on the server, generating Diffie-Hellman parameters with 4096 bits can take several minutes.

3.  Set the paths to the certificate and private key files in the `/etc/dovecot/conf.d/10-ssl.conf`{.literal} file:

    a.  Update the `ssl_cert`{.literal} and `ssl_key`{.literal} parameters, and set them to use the paths of the server's certificate and private key:

        ``` {.language-plaintext tabindex="-1"}
        ssl_cert = </etc/pki/dovecot/certs/server.example.com.crt
        ssl_key = </etc/pki/dovecot/private/server.example.com.key
        ```

    b.  Uncomment the `ssl_ca`{.literal} parameter, and set it to use the path to the CA certificate:

        ``` {.language-plaintext tabindex="-1"}
        ssl_ca = </etc/pki/dovecot/certs/ca.crt
        ```

    c.  Uncomment the `ssl_dh`{.literal} parameter, and set it to use the path to the Diffie-Hellman parameters file:

        ``` {.language-plaintext tabindex="-1"}
        ssl_dh = </etc/dovecot/dh.pem
        ```

    Important

    To ensure that Dovecot reads the value of a parameter from a file, the path must start with a leading `<`{.literal} character.

**Next step**

-   [Preparing Dovecot to use virtual users](#preparing-dovecot-to-use-virtual-users_dovecot-pam "1.1.3. Preparing Dovecot to use virtual users")

#### [1.1.3. Preparing Dovecot to use virtual users](#preparing-dovecot-to-use-virtual-users_dovecot-pam) {#preparing-dovecot-to-use-virtual-users .title}

By default, Dovecot performs many actions on the file system as the user who uses the service. However, configuring the Dovecot back end to use one local user to perform these actions has several benefits.

Using one local user for Dovecot file system actions provides the following benefits:

-   Dovecot performs file system actions as a specific local user instead of using the user's ID (UID).
-   Users do not need to be available locally on the server.
-   You can store all mailboxes and user-specific files in one root directory.
-   Users do not require a UID and group ID (GID), which reduces administration efforts.
-   Users who have access to the file system on the server cannot compromise their mailboxes or indexes because they cannot access these files.
-   Configuring replication is easier.

**Prerequisites**

-   Dovecot is installed.

**Procedure**

1.  Create the `vmail`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # useradd --home-dir /var/mail/ --shell /usr/sbin/nologin vmail
    ```

    Dovecot will later use this user to manage the mailboxes. For security reasons, do not use the `dovecot`{.literal} or `dovenull`{.literal} system users for this purpose.

2.  If you use a different path than `/var/mail/`{.literal}, set the `mail_spool_t`{.literal} SELinux context on it, for example:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t mail_spool_t "<path>(/.)?"*
    # restorecon -Rv <path>
    ```

3.  Grant write permissions on `/var/mail/`{.literal} only to the `vmail`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # chown vmail:vmail /var/mail/
    # chmod 700 /var/mail/
    ```

4.  Uncomment the `mail_location`{.literal} parameter in the `/etc/dovecot/conf.d/10-mail.conf`{.literal} file, and set it to the mailbox format and location:

    ``` {.language-plaintext tabindex="-1"}
    mail_location = sdbox:/var/mail/%n/
    ```

    With this setting:

    -   Dovecot uses the high-performance `dbox`{.literal} mailbox format in `single`{.literal} mode. In this mode, the service stores each mail in a separate file, similar to the `maildir`{.literal} format.
    -   Dovecot resolves the `%n`{.literal} variable in the path to the username. This is required to ensure that each user has a separate directory for its mailbox.

**Next steps**

-   [Using PAM as the Dovecot authentication back end](#using-pam-as-the-dovecot-authentication-backend "1.1.4. Using PAM as the Dovecot authentication back end").

#### [1.1.4. Using PAM as the Dovecot authentication back end](#using-pam-as-the-dovecot-authentication-backend) {#using-pam-as-the-dovecot-authentication-back-end .title}

By default, Dovecot uses the Name Service Switch (NSS) interface as the user database and the Pluggable Authentication Modules (PAM) framework as the authentication back end. Customize settings to adapt Dovecot to your environment and to simplify administration by using the virtual users feature.

**Prerequisites**

-   Dovecot is installed.
-   The virtual users feature is configured.

**Procedure**

1.  Update the `first_valid_uid`{.literal} parameter in the `/etc/dovecot/conf.d/10-mail.conf`{.literal} file to define the lowest user ID (UID) that can authenticate to Dovecot:

    ``` {.language-plaintext tabindex="-1"}
    first_valid_uid = 1000
    ```

    By default, users with a UID greater than or equal to `1000`{.literal} can authenticate. If required, you can also set the `last_valid_uid`{.literal} parameter to define the highest UID that Dovecot allows to log in.

2.  In the `/etc/dovecot/conf.d/auth-system.conf.ext`{.literal} file, add the `override_fields`{.literal} parameter to the `userdb`{.literal} section as follows:

    ``` {.language-bash tabindex="-1"}
    userdb {
      driver = passwd
      override_fields = uid=vmail gid=vmail home=/var/mail/%n/
    }
    ```

    Due to the fixed values, Dovecot does not query these settings from the `/etc/passwd`{.literal} file. As a result, the home directory defined in `/etc/passwd`{.literal} does not need to exist.

**Next step**

-   [Complete the Dovecot configuration](#completing-the-dovecot-configuration_dovecot-pam "1.1.5. Completing the Dovecot configuration").

#### [1.1.5. Completing the Dovecot configuration](#completing-the-dovecot-configuration_dovecot-pam) {#completing-the-dovecot-configuration .title}

Once you have installed and configured Dovecot, open the required ports in the `firewalld`{.literal} service, and enable and start the service. Afterwards, you can test the server.

**Prerequisites**

-   The following has been configured in Dovecot:

    -   TLS encryption
    -   An authentication back end

-   Clients trust the Certificate Authority (CA) certificate.

**Procedure**

1.  If you want to provide only an IMAP or POP3 service to users, uncomment the `protocols`{.literal} parameter in the `/etc/dovecot/dovecot.conf`{.literal} file, and set it to the required protocols. For example, if you do not require POP3, set:

    ``` {.language-bash tabindex="-1"}
    protocols = imap lmtp
    ```

    By default, the `imap`{.literal}, `pop3`{.literal}, and `lmtp`{.literal} protocols are enabled.

2.  Open the ports in the local firewall. For example, to open the ports for the IMAPS, IMAP, POP3S, and POP3 protocols, enter:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=imaps --add-service=imap --add-service=pop3s --add-service=pop3
    # firewall-cmd --reload
    ```

3.  Enable and start the `dovecot`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now dovecot
    ```

**Verification**

1.  Use a mail client, such as Mozilla Thunderbird, to connect to Dovecot and read emails. The settings for the mail client depend on the protocol you want to use:

    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | Protocol                                                                                                                                                               | Port      | Connection security  | Authentication method                                              |
    +:=======================================================================================================================================================================+:==========+:=====================+:===================================================================+
    | IMAP                                                                                                                                                                   | 143       | STARTTLS             | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-pam) |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | IMAPS                                                                                                                                                                  | 993       | SSL/TLS              | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-pam) |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | POP3                                                                                                                                                                   | 110       | STARTTLS             | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-pam) |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | POP3S                                                                                                                                                                  | 995       | SSL/TLS              | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-pam) |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | [^\[a\]^](#fn-dovecot-con-settings-normal-pw_dovecot-pam) The client transmits data encrypted through the TLS connection. Consequently, credentials are not disclosed. |           |                      |                                                                    |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+

    : Table 1.1. Connection settings to the Dovecot server

    Show more

    Note that this table does not list settings for unencrypted connections because, by default, Dovecot does not accept plain text authentication on connections without TLS.

2.  Display configuration settings with non-default values:

    ``` {.language-plaintext tabindex="-1"}
    # doveconf -n
    ```

### [1.2. Configuring a Dovecot server with LDAP authentication](#setting-up-a-dovecot-server-with-ldap-authentication) {#configuring-a-dovecot-server-with-ldap-authentication .title}

If your infrastructure uses an lightweight directory access protocol (LDAP) server to store accounts, you can authenticate Dovecot users against it. In this case, you manage accounts centrally in the directory and users do not require local access to the file system on the Dovecot server.

Centrally managed accounts are also a benefit if you plan to deploy multiple Dovecot servers with replication to make your mailboxes highly available.

#### [1.2.1. Installing Dovecot](#installing-dovecot_dovecot-ldap) {#installing-dovecot-1 .title}

You can install Dovecot to configure the system as an IMAP or POP3 server.

The `dovecot`{.literal} package provides the following components:

-   The `dovecot`{.literal} service and the utilities to maintain it
-   Services that Dovecot starts on demand, such as for authentication
-   Plugins, such as server-side mail filtering
-   Configuration files in the `/etc/dovecot/`{.literal} directory
-   Documentation in the `/usr/share/doc/dovecot/`{.literal} directory

**Procedure**

-   Install the `dovecot`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install dovecot
    ```

    Note

    If Dovecot is already installed and you require clean configuration files, rename or remove the `/etc/dovecot/`{.literal} directory. Afterwards, reinstall the package. Without removing the configuration files, the `dnf reinstall dovecot`{.literal} command does not reset the configuration files in `/etc/dovecot/`{.literal}.

**Next step**

-   [Configuring TLS encryption on a Dovecot server](#configuring-tls-encryption-on-a-dovecot-server_dovecot-ldap "1.2.2. Configuring TLS encryption on a Dovecot server").

#### [1.2.2. Configuring TLS encryption on a Dovecot server](#configuring-tls-encryption-on-a-dovecot-server_dovecot-ldap) {#configuring-tls-encryption-on-a-dovecot-server-1 .title}

By default, Dovecot enables TLS to securely transmit credentials and data. To configure TLS, set the paths to the certificate and private key files. Increase security by generating and using Diffie-Hellman parameters for perfect forward secrecy (PFS).

**Prerequisites**

-   Dovecot is installed.

-   The following files have been copied to the listed locations on the server:

    -   The server certificate: `/etc/pki/dovecot/certs/server.example.com.crt`{.literal}
    -   The private key: `/etc/pki/dovecot/private/server.example.com.key`{.literal}
    -   The Certificate Authority (CA) certificate: `/etc/pki/dovecot/certs/ca.crt`{.literal}

-   The hostname in the `Subject DN`{.literal} field of the server certificate matches the server's fully-qualified domain name (FQDN).

-   If the Federal information processing standards (FIPS) mode is enabled, clients must either support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Set secure permissions on the private key file:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:root /etc/pki/dovecot/private/server.example.com.key
    # chmod 600 /etc/pki/dovecot/private/server.example.com.key
    ```

2.  Generate a file with Diffie-Hellman parameters:

    ``` {.language-plaintext tabindex="-1"}
    # openssl dhparam -out /etc/dovecot/dh.pem 4096
    ```

    Depending on the hardware and entropy on the server, generating Diffie-Hellman parameters with 4096 bits can take several minutes.

3.  Set the paths to the certificate and private key files in the `/etc/dovecot/conf.d/10-ssl.conf`{.literal} file:

    a.  Update the `ssl_cert`{.literal} and `ssl_key`{.literal} parameters, and set them to use the paths of the server's certificate and private key:

        ``` {.language-plaintext tabindex="-1"}
        ssl_cert = </etc/pki/dovecot/certs/server.example.com.crt
        ssl_key = </etc/pki/dovecot/private/server.example.com.key
        ```

    b.  Uncomment the `ssl_ca`{.literal} parameter, and set it to use the path to the CA certificate:

        ``` {.language-plaintext tabindex="-1"}
        ssl_ca = </etc/pki/dovecot/certs/ca.crt
        ```

    c.  Uncomment the `ssl_dh`{.literal} parameter, and set it to use the path to the Diffie-Hellman parameters file:

        ``` {.language-plaintext tabindex="-1"}
        ssl_dh = </etc/dovecot/dh.pem
        ```

    Important

    To ensure that Dovecot reads the value of a parameter from a file, the path must start with a leading `<`{.literal} character.

**Next step**

-   [Preparing Dovecot to use virtual users](#preparing-dovecot-to-use-virtual-users_dovecot-ldap "1.2.3. Preparing Dovecot to use virtual users")

#### [1.2.3. Preparing Dovecot to use virtual users](#preparing-dovecot-to-use-virtual-users_dovecot-ldap) {#preparing-dovecot-to-use-virtual-users-1 .title}

By default, Dovecot performs many actions on the file system as the user who uses the service. However, configuring the Dovecot back end to use one local user to perform these actions has several benefits.

Using one local user for Dovecot file system actions provides the following benefits:

-   Dovecot performs file system actions as a specific local user instead of using the user's ID (UID).
-   Users do not need to be available locally on the server.
-   You can store all mailboxes and user-specific files in one root directory.
-   Users do not require a UID and group ID (GID), which reduces administration efforts.
-   Users who have access to the file system on the server cannot compromise their mailboxes or indexes because they cannot access these files.
-   Configuring replication is easier.

**Prerequisites**

-   Dovecot is installed.

**Procedure**

1.  Create the `vmail`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # useradd --home-dir /var/mail/ --shell /usr/sbin/nologin vmail
    ```

    Dovecot will later use this user to manage the mailboxes. For security reasons, do not use the `dovecot`{.literal} or `dovenull`{.literal} system users for this purpose.

2.  If you use a different path than `/var/mail/`{.literal}, set the `mail_spool_t`{.literal} SELinux context on it, for example:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t mail_spool_t "<path>(/.)?"*
    # restorecon -Rv <path>
    ```

3.  Grant write permissions on `/var/mail/`{.literal} only to the `vmail`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # chown vmail:vmail /var/mail/
    # chmod 700 /var/mail/
    ```

4.  Uncomment the `mail_location`{.literal} parameter in the `/etc/dovecot/conf.d/10-mail.conf`{.literal} file, and set it to the mailbox format and location:

    ``` {.language-plaintext tabindex="-1"}
    mail_location = sdbox:/var/mail/%n/
    ```

    With this setting:

    -   Dovecot uses the high-performance `dbox`{.literal} mailbox format in `single`{.literal} mode. In this mode, the service stores each mail in a separate file, similar to the `maildir`{.literal} format.
    -   Dovecot resolves the `%n`{.literal} variable in the path to the username. This is required to ensure that each user has a separate directory for its mailbox.

**Next steps**

-   [Using LDAP as the Dovecot authentication back end](#using-ldap-as-the-dovecot-authentication-backend "1.2.4. Using LDAP as the Dovecot authentication back end").

#### [1.2.4. Using LDAP as the Dovecot authentication back end](#using-ldap-as-the-dovecot-authentication-backend) {#using-ldap-as-the-dovecot-authentication-back-end .title}

Users in an LDAP directory can usually authenticate themselves to the directory service. Dovecot can use this to authenticate users when they log in to the IMAP and POP3 services.

Using an LDAP directory for Dovecot authentication provides the following benefits:

-   Administrators can manage users centrally in the directory.
-   The LDAP accounts do not require any special attributes. They only need to be able to authenticate to the LDAP server. Consequently, this method is independent from the password storage scheme used on the LDAP server.
-   Users do not need to be available locally on the server through the Name Service Switch (NSS) interface and the Pluggable Authentication Modules (PAM) framework.

**Prerequisites**

-   Dovecot is installed.
-   The virtual users feature is configured.
-   Connections to the LDAP server support TLS encryption.
-   RHEL on the Dovecot server trusts the Certificate Authority (CA) certificate of the LDAP server.
-   If users are stored in different trees in the LDAP directory, a dedicated LDAP account for Dovecot exists to search the directory. This account requires permissions to search for Distinguished Names (DNs) of other users.
-   If the FIPS mode is enabled, this Dovecot server supports the Extended Master Secret (EMS) extension or uses TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Configure the authentication back ends in the `/etc/dovecot/conf.d/10-auth.conf`{.literal} file:

    a.  Comment out `include`{.literal} statements for `auth-*.conf.ext`{.literal} authentication back-end configuration files that you do not require, for example:

        ``` {.language-plaintext tabindex="-1"}
        #!include auth-system.conf.ext
        ```

    b.  Enable LDAP authentication by uncommenting the following line:

        ``` {.language-plaintext tabindex="-1"}
        !include auth-ldap.conf.ext
        ```

2.  Edit the `/etc/dovecot/conf.d/auth-ldap.conf.ext`{.literal} file, and add the `override_fields`{.literal} parameter as follows to the `userdb`{.literal} section:

    ``` {.language-bash tabindex="-1"}
    userdb {
      driver = ldap
      args = /etc/dovecot/dovecot-ldap.conf.ext
      override_fields = uid=vmail gid=vmail home=/var/mail/%n/
    }
    ```

    Due to the fixed values, Dovecot does not query these settings from the LDAP server. Consequently, these attributes also do not have to be present.

3.  Create the `/etc/dovecot/dovecot-ldap.conf.ext`{.literal} file with the following settings:

    a.  Depending on the LDAP structure, configure one of the following:

        -   If users are stored in different trees in the LDAP directory, configure dynamic DN lookups:

            ``` {.language-bash tabindex="-1"}
            dn = cn=dovecot_LDAP,dc=example,dc=com
            dnpass = <password>
            pass_filter = (&(objectClass=posixAccount)(uid=%n))
            ```

            Dovecot uses the specified DN, password, and filter to search the DN of the authenticating user in the directory. In this search, Dovecot replaces `%n`{.literal} in the filter with the username. Note that the LDAP search must return only one result.

        -   If all users are stored under a specific entry, configure a DN template:

            ``` {.language-plaintext tabindex="-1"}
            auth_bind_userdn = cn=%n,ou=People,dc=example,dc=com
            ```

    b.  Enable authentication binds to the LDAP server to verify Dovecot users:

        ``` {.language-plaintext tabindex="-1"}
        auth_bind = yes
        ```

    c.  Set the URL to the LDAP server:

        ``` {.language-plaintext tabindex="-1"}
        uris = ldaps://LDAP-srv.example.com
        ```

        For security reasons, only use encrypted connections by using LDAPS or the `STARTTLS`{.literal} command over the LDAP protocol. For the latter, additionally add `tls = yes`{.literal} to the settings.

        For a working certificate validation, the hostname of the LDAP server must match the hostname used in its TLS certificate.

    d.  Enable the verification of the LDAP server's TLS certificate:

        ``` {.language-plaintext tabindex="-1"}
        tls_require_cert = hard
        ```

    e.  Set the base DN to the DN where to start searching for users:

        ``` {.language-plaintext tabindex="-1"}
        base = ou=People,dc=example,dc=com
        ```

    f.  Set the search scope:

        ``` {.language-plaintext tabindex="-1"}
        scope = onelevel
        ```

        Dovecot searches with the `onelevel`{.literal} scope only in the specified base DN and with the `subtree`{.literal} scope also in subtrees.

4.  Set secure permissions on the `/etc/dovecot/dovecot-ldap.conf.ext`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:root /etc/dovecot/dovecot-ldap.conf.ext
    # chmod 600 /etc/dovecot/dovecot-ldap.conf.ext
    ```

**Next step**

-   [Complete the Dovecot configuration](#completing-the-dovecot-configuration_dovecot-ldap "1.2.5. Completing the Dovecot configuration").

#### [1.2.5. Completing the Dovecot configuration](#completing-the-dovecot-configuration_dovecot-ldap) {#completing-the-dovecot-configuration-1 .title}

Once you have installed and configured Dovecot, open the required ports in the `firewalld`{.literal} service, and enable and start the service. Afterwards, you can test the server.

**Prerequisites**

-   The following has been configured in Dovecot:

    -   TLS encryption
    -   An authentication back end

-   Clients trust the Certificate Authority (CA) certificate.

**Procedure**

1.  If you want to provide only an IMAP or POP3 service to users, uncomment the `protocols`{.literal} parameter in the `/etc/dovecot/dovecot.conf`{.literal} file, and set it to the required protocols. For example, if you do not require POP3, set:

    ``` {.language-bash tabindex="-1"}
    protocols = imap lmtp
    ```

    By default, the `imap`{.literal}, `pop3`{.literal}, and `lmtp`{.literal} protocols are enabled.

2.  Open the ports in the local firewall. For example, to open the ports for the IMAPS, IMAP, POP3S, and POP3 protocols, enter:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=imaps --add-service=imap --add-service=pop3s --add-service=pop3
    # firewall-cmd --reload
    ```

3.  Enable and start the `dovecot`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now dovecot
    ```

**Verification**

1.  Use a mail client, such as Mozilla Thunderbird, to connect to Dovecot and read emails. The settings for the mail client depend on the protocol you want to use:

    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+---------------------------------------------------------------------+
    | Protocol                                                                                                                                                                | Port      | Connection security  | Authentication method                                               |
    +:========================================================================================================================================================================+:==========+:=====================+:====================================================================+
    | IMAP                                                                                                                                                                    | 143       | STARTTLS             | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-ldap) |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+---------------------------------------------------------------------+
    | IMAPS                                                                                                                                                                   | 993       | SSL/TLS              | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-ldap) |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+---------------------------------------------------------------------+
    | POP3                                                                                                                                                                    | 110       | STARTTLS             | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-ldap) |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+---------------------------------------------------------------------+
    | POP3S                                                                                                                                                                   | 995       | SSL/TLS              | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-ldap) |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+---------------------------------------------------------------------+
    | [^\[a\]^](#fn-dovecot-con-settings-normal-pw_dovecot-ldap) The client transmits data encrypted through the TLS connection. Consequently, credentials are not disclosed. |           |                      |                                                                     |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+---------------------------------------------------------------------+

    : Table 1.2. Connection settings to the Dovecot server

    Show more

    Note that this table does not list settings for unencrypted connections because, by default, Dovecot does not accept plain text authentication on connections without TLS.

2.  Display configuration settings with non-default values:

    ``` {.language-plaintext tabindex="-1"}
    # doveconf -n
    ```

### [1.3. Configuring a Dovecot server with MariaDB SQL authentication](#setting-up-a-dovecot-server-with-mariadb-sql-authentication) {#configuring-a-dovecot-server-with-mariadb-sql-authentication .title}

If you store users and passwords in a MariaDB SQL server, you can configure Dovecot to use it as the user database and authentication back end. With this configuration, you manage accounts centrally in a database, and users have no local access to the file system on the Dovecot server.

Centrally managed accounts are also a benefit if you plan to deploy multiple Dovecot servers with replication to make your mailboxes highly available.

#### [1.3.1. Installing Dovecot](#installing-dovecot_dovecot-sql) {#installing-dovecot-2 .title}

You can install Dovecot to configure the system as an IMAP or POP3 server.

The `dovecot`{.literal} package provides the following components:

-   The `dovecot`{.literal} service and the utilities to maintain it
-   Services that Dovecot starts on demand, such as for authentication
-   Plugins, such as server-side mail filtering
-   Configuration files in the `/etc/dovecot/`{.literal} directory
-   Documentation in the `/usr/share/doc/dovecot/`{.literal} directory

**Procedure**

-   Install the `dovecot`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install dovecot
    ```

    Note

    If Dovecot is already installed and you require clean configuration files, rename or remove the `/etc/dovecot/`{.literal} directory. Afterwards, reinstall the package. Without removing the configuration files, the `dnf reinstall dovecot`{.literal} command does not reset the configuration files in `/etc/dovecot/`{.literal}.

**Next step**

-   [Configuring TLS encryption on a Dovecot server](#configuring-tls-encryption-on-a-dovecot-server_dovecot-sql "1.3.2. Configuring TLS encryption on a Dovecot server").

#### [1.3.2. Configuring TLS encryption on a Dovecot server](#configuring-tls-encryption-on-a-dovecot-server_dovecot-sql) {#configuring-tls-encryption-on-a-dovecot-server-2 .title}

By default, Dovecot enables TLS to securely transmit credentials and data. To configure TLS, set the paths to the certificate and private key files. Increase security by generating and using Diffie-Hellman parameters for perfect forward secrecy (PFS).

**Prerequisites**

-   Dovecot is installed.

-   The following files have been copied to the listed locations on the server:

    -   The server certificate: `/etc/pki/dovecot/certs/server.example.com.crt`{.literal}
    -   The private key: `/etc/pki/dovecot/private/server.example.com.key`{.literal}
    -   The Certificate Authority (CA) certificate: `/etc/pki/dovecot/certs/ca.crt`{.literal}

-   The hostname in the `Subject DN`{.literal} field of the server certificate matches the server's fully-qualified domain name (FQDN).

-   If the Federal information processing standards (FIPS) mode is enabled, clients must either support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Set secure permissions on the private key file:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:root /etc/pki/dovecot/private/server.example.com.key
    # chmod 600 /etc/pki/dovecot/private/server.example.com.key
    ```

2.  Generate a file with Diffie-Hellman parameters:

    ``` {.language-plaintext tabindex="-1"}
    # openssl dhparam -out /etc/dovecot/dh.pem 4096
    ```

    Depending on the hardware and entropy on the server, generating Diffie-Hellman parameters with 4096 bits can take several minutes.

3.  Set the paths to the certificate and private key files in the `/etc/dovecot/conf.d/10-ssl.conf`{.literal} file:

    a.  Update the `ssl_cert`{.literal} and `ssl_key`{.literal} parameters, and set them to use the paths of the server's certificate and private key:

        ``` {.language-plaintext tabindex="-1"}
        ssl_cert = </etc/pki/dovecot/certs/server.example.com.crt
        ssl_key = </etc/pki/dovecot/private/server.example.com.key
        ```

    b.  Uncomment the `ssl_ca`{.literal} parameter, and set it to use the path to the CA certificate:

        ``` {.language-plaintext tabindex="-1"}
        ssl_ca = </etc/pki/dovecot/certs/ca.crt
        ```

    c.  Uncomment the `ssl_dh`{.literal} parameter, and set it to use the path to the Diffie-Hellman parameters file:

        ``` {.language-plaintext tabindex="-1"}
        ssl_dh = </etc/dovecot/dh.pem
        ```

    Important

    To ensure that Dovecot reads the value of a parameter from a file, the path must start with a leading `<`{.literal} character.

**Next step**

-   [Preparing Dovecot to use virtual users](#preparing-dovecot-to-use-virtual-users_dovecot-sql "1.3.3. Preparing Dovecot to use virtual users")

#### [1.3.3. Preparing Dovecot to use virtual users](#preparing-dovecot-to-use-virtual-users_dovecot-sql) {#preparing-dovecot-to-use-virtual-users-2 .title}

By default, Dovecot performs many actions on the file system as the user who uses the service. However, configuring the Dovecot back end to use one local user to perform these actions has several benefits.

Using one local user for Dovecot file system actions provides the following benefits:

-   Dovecot performs file system actions as a specific local user instead of using the user's ID (UID).
-   Users do not need to be available locally on the server.
-   You can store all mailboxes and user-specific files in one root directory.
-   Users do not require a UID and group ID (GID), which reduces administration efforts.
-   Users who have access to the file system on the server cannot compromise their mailboxes or indexes because they cannot access these files.
-   Configuring replication is easier.

**Prerequisites**

-   Dovecot is installed.

**Procedure**

1.  Create the `vmail`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # useradd --home-dir /var/mail/ --shell /usr/sbin/nologin vmail
    ```

    Dovecot will later use this user to manage the mailboxes. For security reasons, do not use the `dovecot`{.literal} or `dovenull`{.literal} system users for this purpose.

2.  If you use a different path than `/var/mail/`{.literal}, set the `mail_spool_t`{.literal} SELinux context on it, for example:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t mail_spool_t "<path>(/.)?"*
    # restorecon -Rv <path>
    ```

3.  Grant write permissions on `/var/mail/`{.literal} only to the `vmail`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # chown vmail:vmail /var/mail/
    # chmod 700 /var/mail/
    ```

4.  Uncomment the `mail_location`{.literal} parameter in the `/etc/dovecot/conf.d/10-mail.conf`{.literal} file, and set it to the mailbox format and location:

    ``` {.language-plaintext tabindex="-1"}
    mail_location = sdbox:/var/mail/%n/
    ```

    With this setting:

    -   Dovecot uses the high-performance `dbox`{.literal} mailbox format in `single`{.literal} mode. In this mode, the service stores each mail in a separate file, similar to the `maildir`{.literal} format.
    -   Dovecot resolves the `%n`{.literal} variable in the path to the username. This is required to ensure that each user has a separate directory for its mailbox.

**Next steps**

-   [Using a MariaDB SQL database as the Dovecot authentication back end](#using-a-mariadb-sql-database-as-the-dovecot-authentication-backend "1.3.4. Using a MariaDB SQL database as the Dovecot authentication back end")

#### [1.3.4. Using a MariaDB SQL database as the Dovecot authentication back end](#using-a-mariadb-sql-database-as-the-dovecot-authentication-backend) {#using-a-mariadb-sql-database-as-the-dovecot-authentication-back-end .title}

Dovecot can read accounts and passwords from a MariaDB database and use it to authenticate users when they log in to the IMAP or POP3 service.

Using a MariaDB database for Dovecot authentication provides the following benefits:

-   Administrators can manage users centrally in a database.
-   Users have no local access to the server.

**Prerequisites**

-   Dovecot is installed.
-   The virtual users feature is configured.
-   Connections to the MariaDB server support TLS encryption.
-   The `dovecotDB`{.literal} database exists in MariaDB, and the `users`{.literal} table contains at least a `username`{.literal} and `password`{.literal} column.
-   The `password`{.literal} column contains passwords encrypted with a scheme that Dovecot supports.
-   The passwords either use the same scheme or have a `{`{.literal}*`pw-storage-scheme`{.literal}*`}`{.literal} prefix.
-   The `dovecot`{.literal} MariaDB user has read permission on the `users`{.literal} table in the `dovecotDB`{.literal} database.
-   The certificate of the Certificate Authority (CA) that issued the MariaDB server's TLS certificate is stored on the Dovecot server in the `/etc/pki/tls/certs/ca.crt`{.literal} file.
-   If the FIPS mode is enabled, this Dovecot server supports the Extended Master Secret (EMS) extension or uses TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Install the `dovecot-mysql`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install dovecot-mysql
    ```

2.  Configure the authentication back ends in the `/etc/dovecot/conf.d/10-auth.conf`{.literal} file:

    a.  Comment out `include`{.literal} statements for `auth-*.conf.ext`{.literal} authentication back-end configuration files that you do not require, for example:

        ``` {.language-plaintext tabindex="-1"}
        #!include auth-system.conf.ext
        ```

    b.  Enable SQL authentication by uncommenting the following line:

        ``` {.language-plaintext tabindex="-1"}
        !include auth-sql.conf.ext
        ```

3.  Edit the `/etc/dovecot/conf.d/auth-sql.conf.ext`{.literal} file, and add the `override_fields`{.literal} parameter to the `userdb`{.literal} section as follows:

    ``` {.language-bash tabindex="-1"}
    userdb {
      driver = sql
      args = /etc/dovecot/dovecot-sql.conf.ext
      override_fields = uid=vmail gid=vmail home=/var/mail/%n/
    }
    ```

    Due to the fixed values, Dovecot does not query these settings from the SQL server.

4.  Create the `/etc/dovecot/dovecot-sql.conf.ext`{.literal} file with the following settings:

    ``` {.language-bash tabindex="-1"}
    driver = mysql**
    connect = host=mariadb_srv.example.com dbname=dovecotDB user=dovecot password=<dovecotPW> ssl_ca=/etc/pki/tls/certs/ca.crt
    default_pass_scheme = SHA512-CRYPT
    user_query = SELECT username FROM users WHERE username='%u';
    password_query = SELECT username AS user, password FROM users WHERE username='%u';
    iterate_query = SELECT username FROM users;
    ```

    To use TLS encryption to the database server, set the `ssl_ca`{.literal} option to the path of the certificate of the CA that issued the MariaDB server certificate. For a working certificate validation, the hostname of the MariaDB server must match the hostname used in its TLS certificate.

    If the password values in the database contain a `{`{.literal}*`<pw-storage-scheme>`{.literal}*`}`{.literal} prefix, you can omit the `default_pass_scheme`{.literal} setting.

    The queries in the file must be set as follows:

    -   For the `user_query`{.literal} parameter, the query must return the username of the Dovecot user. The query must also return only one result.
    -   For the `password_query`{.literal} parameter, the query must return the username and the password, and Dovecot must use these values in the `user`{.literal} and `password`{.literal} variables. Therefore, if the database uses different column names, use the `AS`{.literal} SQL command to rename a column in the result.
    -   For the `iterate_query`{.literal} parameter, the query must return a list of all users.

5.  Set secure permissions on the `/etc/dovecot/dovecot-sql.conf.ext`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:root /etc/dovecot/dovecot-sql.conf.ext
    # chmod 600 /etc/dovecot/dovecot-sql.conf.ext
    ```

**Next step**

-   [Complete the Dovecot configuration](#completing-the-dovecot-configuration_dovecot-sql "1.3.5. Completing the Dovecot configuration").

#### [1.3.5. Completing the Dovecot configuration](#completing-the-dovecot-configuration_dovecot-sql) {#completing-the-dovecot-configuration-2 .title}

Once you have installed and configured Dovecot, open the required ports in the `firewalld`{.literal} service, and enable and start the service. Afterwards, you can test the server.

**Prerequisites**

-   The following has been configured in Dovecot:

    -   TLS encryption
    -   An authentication back end

-   Clients trust the Certificate Authority (CA) certificate.

**Procedure**

1.  If you want to provide only an IMAP or POP3 service to users, uncomment the `protocols`{.literal} parameter in the `/etc/dovecot/dovecot.conf`{.literal} file, and set it to the required protocols. For example, if you do not require POP3, set:

    ``` {.language-bash tabindex="-1"}
    protocols = imap lmtp
    ```

    By default, the `imap`{.literal}, `pop3`{.literal}, and `lmtp`{.literal} protocols are enabled.

2.  Open the ports in the local firewall. For example, to open the ports for the IMAPS, IMAP, POP3S, and POP3 protocols, enter:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=imaps --add-service=imap --add-service=pop3s --add-service=pop3
    # firewall-cmd --reload
    ```

3.  Enable and start the `dovecot`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now dovecot
    ```

**Verification**

1.  Use a mail client, such as Mozilla Thunderbird, to connect to Dovecot and read emails. The settings for the mail client depend on the protocol you want to use:

    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | Protocol                                                                                                                                                               | Port      | Connection security  | Authentication method                                              |
    +:=======================================================================================================================================================================+:==========+:=====================+:===================================================================+
    | IMAP                                                                                                                                                                   | 143       | STARTTLS             | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-sql) |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | IMAPS                                                                                                                                                                  | 993       | SSL/TLS              | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-sql) |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | POP3                                                                                                                                                                   | 110       | STARTTLS             | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-sql) |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | POP3S                                                                                                                                                                  | 995       | SSL/TLS              | PLAIN[^\[a\]^](#ftn.fn-dovecot-con-settings-normal-pw_dovecot-sql) |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+
    | [^\[a\]^](#fn-dovecot-con-settings-normal-pw_dovecot-sql) The client transmits data encrypted through the TLS connection. Consequently, credentials are not disclosed. |           |                      |                                                                    |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+----------------------+--------------------------------------------------------------------+

    : Table 1.3. Connection settings to the Dovecot server

    Show more

    Note that this table does not list settings for unencrypted connections because, by default, Dovecot does not accept plain text authentication on connections without TLS.

2.  Display configuration settings with non-default values:

    ``` {.language-plaintext tabindex="-1"}
    # doveconf -n
    ```

### [1.4. Configuring replication between two Dovecot servers](#configuring-replication-between-two-dovecot-servers) {#configuring-replication-between-two-dovecot-servers .title}

With two-way replication, you can make your Dovecot server highly available, and IMAP and POP3 clients can access a mailbox on both servers. Dovecot keeps track of changes in the index logs of each mailbox and solves conflicts in a safe way.

Perform the two-way replication procedure on both replication partners.

Note

Replication works only between server pairs. Consequently, in a large cluster, you need multiple independent back-end pairs.

**Prerequisites**

-   Both servers use the same authentication back end. Preferably, use LDAP or SQL to maintain accounts centrally.
-   The Dovecot user database configuration supports user listing. Use the `doveadm user '*'`{.literal} command to verify this.
-   Dovecot accesses mailboxes on the file system as the `vmail`{.literal} user instead of the user's ID (UID).

**Procedure**

1.  Create the `/etc/dovecot/conf.d/10-replication.conf`{.literal} file and perform the following steps in it:

    a.  Enable the `notify`{.literal} and `replication`{.literal} plugins:

        ``` {.language-plaintext tabindex="-1"}
        mail_plugins = $mail_plugins notify replication
        ```

    b.  Add a `service replicator`{.literal} section:

        ``` {.language-plaintext tabindex="-1"}
        service replicator {
          process_min_avail = 1

          unix_listener replicator-doveadm {
            mode = 0600
            user = vmail
          }
        }
        ```

        With these settings, Dovecot starts at least one replicator process when the `dovecot`{.literal} service starts. Additionally, this section defines the settings on the `replicator-doveadm`{.literal} socket.

    c.  Add a `service aggregator`{.literal} section to configure the `replication-notify-fifo`{.literal} pipe and `replication-notify`{.literal} socket:

        ``` {.language-plaintext tabindex="-1"}
        service aggregator {
          fifo_listener replication-notify-fifo {
            user = vmail
          }
          unix_listener replication-notify {
            user = vmail
          }
        }
        ```

    d.  Add a `service doveadm`{.literal} section to define the port of the replication service:

        ``` {.language-plaintext tabindex="-1"}
        service doveadm {
          inet_listener {
            port = 12345
          }
        }
        ```

    e.  Set the password of the `doveadm`{.literal} replication service:

        ``` {.language-bash tabindex="-1"}
        doveadm_password = <replication_password>
        ```

        The password must be the same on both servers.

    f.  Configure the replication partner:

        ``` {.language-plaintext tabindex="-1"}
        plugin {
          mail_replica = tcp:server2.example.com:12345
        }
        ```

    g.  Optional: Define the maximum number of parallel `dsync`{.literal} processes:

        ``` {.language-plaintext tabindex="-1"}
        replication_max_conns = 20
        ```

        The default value of `replication_max_conns`{.literal} is `10`{.literal}.

2.  Set secure permissions on the `/etc/dovecot/conf.d/10-replication.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:root /etc/dovecot/conf.d/10-replication.conf
    # chmod 600 /etc/dovecot/conf.d/10-replication.conf
    ```

3.  Enable the `nis_enabled`{.literal} SELinux Boolean to allow Dovecot to open the `doveadm`{.literal} replication port:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool -P nis_enabled on
    ```

4.  Configure `firewalld`{.literal} rules to allow only the replication partner to access the replication port, for example:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --zone=public --add-rich-rule="rule family="ipv4" source address="192.0.2.1/32" port protocol="tcp" port="12345" accept"
    # firewall-cmd --permanent --zone=public --add-rich-rule="rule family="ipv6" source address="2001:db8:2::1/128" port protocol="tcp" port="12345" accept"
    # firewall-cmd --reload
    ```

    The subnet masks `/32`{.literal} for the IPv4 and `/128`{.literal} for the IPv6 address limit the access to the specified addresses.

5.  Perform this procedure also on the other replication partner.

6.  Reload Dovecot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload dovecot
    ```

**Verification**

1.  Perform an action in a mailbox on one server and then verify if Dovecot has replicated the change to the other server.

2.  Display the replicator status:

    ``` {.language-plaintext tabindex="-1"}
    # doveadm replicator status
    Queued 'sync' requests        0
    Queued 'high' requests        0
    Queued 'low' requests         0
    Queued 'failed' requests      0
    Queued 'full resync' requests 30
    Waiting 'failed' requests     0
    Total number of known users   75
    ```

3.  Display the replicator status of a specific user:

    ``` {.language-plaintext tabindex="-1"}
    # doveadm replicator status <user_name>
    username        priority  fast sync  full sync  success sync  failed
    <user_name>     none      02:05:28   04:19:07   02:05:28      -
    ```

### [1.5. Automatically subscribing users to IMAP mailboxes](#automatically-subscribing-users-to-imap-mailboxes) {#automatically-subscribing-users-to-imap-mailboxes .title}

Typically, IMAP server administrators want Dovecot to automatically create certain mailboxes, such as `Sent`{.literal} and `Trash`{.literal}, and subscribe the users to them. You can set this in the configuration files.

You can define *special-use mailboxes*. IMAP clients often support defining mailboxes for special purposes, such as for sent emails. To avoid requiring the user to manually select and set the correct mailboxes, IMAP servers can send a `special-use`{.literal} attribute in the IMAP `LIST`{.literal} command. Clients can then use this attribute to identify and set, for example, the mailbox for sent emails.

**Prerequisites**

-   Dovecot is configured.

**Procedure**

1.  Update the `inbox`{.literal} namespace section in the `/etc/dovecot/conf.d/15-mailboxes.conf`{.literal} file:

    a.  Add the `auto = subscribe`{.literal} setting to each special-use mailbox that should be available to users, for example:

        ``` {.language-bash tabindex="-1"}
        namespace inbox {
          ...
          mailbox Drafts {
            special_use = \Drafts
            auto = subscribe
          }

          mailbox Junk {
            special_use = \Junk
            auto = subscribe
          }

          mailbox Trash {
            special_use = \Trash
            auto = subscribe
          }

          mailbox Sent {
            special_use = \Sent
            auto = subscribe
          }
          ...
        }
        ```

        If your mail clients support more special-use mailboxes, you can add similar entries. The `special_use`{.literal} parameter defines the value that Dovecot sends in the `special-use`{.literal} attribute to the clients.

        For further details, see the `/usr/share/doc/dovecot/wiki/MailboxSettings.txt`{.literal} file.

    b.  Optional: If you want to define other mailboxes that have no special purpose, add `mailbox`{.literal} sections for them in the user's inbox, for example:

        ``` {.language-bash tabindex="-1"}
        namespace inbox {
          ...
          mailbox "Important Emails" {
            auto = <value>
          }
          ...
        }
        ```

        You can set the `auto`{.literal} parameter to one of the following values:

        -   `subscribe`{.literal}: Automatically creates the mailbox and subscribes the user to it.
        -   `create`{.literal}: Automatically creates the mailbox without subscribing the user to it.
        -   `no`{.literal} (default): Dovecot neither creates the mailbox nor does it subscribe the user to it.

2.  Reload Dovecot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload dovecot
    ```

**Verification**

-   Use an IMAP client and access your mailbox.

    Mailboxes with the setting `auto = subscribe`{.literal} are automatically visible. If the client supports special-use mailboxes and the defined purposes, the client automatically uses them.

### [1.6. Configuring an LMTP socket and LMTPS listener](#configuring-an-lmtp-socket-and-lmtps-listener) {#configuring-an-lmtp-socket-and-lmtps-listener .title}

Configure a simple mail transfer protocol (SMTP) server, such as Postfix, to use the Local Mail Transfer Protocol (LMTP) to deliver emails to Dovecot.

To configure LMTP delivery to Dovecot:

-   If the SMTP server runs on the same host as Dovecot, use an LMTP socket.

-   If the SMTP server runs on a different host, use an LMTP service.

    By default, the LMTP protocol is not encrypted. However, if you configured TLS encryption, Dovecot uses the same settings automatically for the LMTP service. SMTP servers can then connect to it by using the LMTPS protocol or the `STARTTLS`{.literal} command over LMTP.

**Prerequisites**

-   Dovecot is installed.
-   If you want to configure an LMTP service, TLS encryption is configured in Dovecot.

**Procedure**

1.  Verify that the LMTP protocol is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # doveconf -a | grep -E "^protocols"
    protocols = imap pop3 lmtp
    ```

    The protocol is enabled, if the output contains `lmtp`{.literal}.

2.  If the `lmtp`{.literal} protocol is disabled, edit the `/etc/dovecot/dovecot.conf`{.literal} file, and append `lmtp`{.literal} to the values in the `protocols`{.literal} parameter:

    ``` {.language-bash tabindex="-1"}
    protocols = ... lmtp
    ```

3.  Depending on whether you need an LMTP socket or service, make the following changes in the `service lmtp`{.literal} section in the `/etc/dovecot/conf.d/10-master.conf`{.literal} file:

    -   LMTP socket: By default, Dovecot automatically creates the `/var/run/dovecot/lmtp`{.literal} socket.

        Optional: Customize the ownership and permissions:

        ``` {.language-bash tabindex="-1"}
        service lmtp {
          ...
          unix_listener lmtp {
            mode = 0600
            user = postfix
            group = postfix
          }
          ...
        }
        ```

    -   LMTP service: Add an `inet_listener`{.literal} sub-section:

        ``` {.language-bash tabindex="-1"}
        service lmtp {
          ...
          inet_listener lmtp {
            port = 24
          }
          ...
        }
        ```

4.  Configure `firewalld`{.literal} rules to allow only the SMTP server to access the LMTP port, for example:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --zone=public --add-rich-rule="rule family="ipv4" source address="<smtp_server_ip_address>/32" port protocol="tcp" port="24" accept"
    # firewall-cmd --permanent --zone=public --add-rich-rule="rule family="ipv6" source address="<smtp_server_ip_address>/128" port protocol="tcp" port="24" accept"
    # firewall-cmd --reload
    ```

    The subnet masks `/32`{.literal} for the IPv4 and `/128`{.literal} for the IPv6 address limit the access to the specified addresses.

5.  Reload Dovecot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload dovecot
    ```

**Verification**

1.  If you configured the LMTP socket, verify that Dovecot has created the socket and that the permissions are correct:

    ``` {.language-plaintext tabindex="-1"}
    # ls -l /var/run/dovecot/lmtp
    srw-------. 1 postfix postfix 0 Nov 22 17:17 /var/run/dovecot/lmtp
    ```

2.  Configure the SMTP server to submit emails to Dovecot using the LMTP socket or service.

    When you use the LMTP service, ensure that the SMTP server uses the LMTPS protocol or sends the `STARTTLS`{.literal} command to use an encrypted connection.

### [1.7. Disabling the IMAP or POP3 service in Dovecot](#disabling-the-imap-or-pop3-service-in-dovecot) {#disabling-the-imap-or-pop3-service-in-dovecot .title}

By default, Dovecot provides IMAP and POP3 services. If you require only one of them, you can disable the other to reduce the attack surface.

**Prerequisites**

-   Dovecot is installed.

**Procedure**

1.  Uncomment the `protocols`{.literal} parameter in the `/etc/dovecot/dovecot.conf`{.literal} file, and set it to use the required protocols. For example, if you do not require POP3, set:

    ``` {.language-plaintext tabindex="-1"}
    protocols = imap lmtp
    ```

    By default, the `imap`{.literal}, `pop3`{.literal}, and `lmtp`{.literal} protocols are enabled.

2.  Reload Dovecot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload dovecot
    ```

3.  Close the ports that are no longer required in the local firewall. For example, to close the ports for the POP3S and POP3 protocols, enter:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --remove-service=pop3s --remove-service=pop3
    # firewall-cmd --reload
    ```

**Verification**

-   Display all ports in `LISTEN`{.literal} mode opened by the `dovecot`{.literal} process:

    ``` {.language-plaintext tabindex="-1"}
    # ss -tulp | grep dovecot
    tcp  LISTEN 0  100  0.0.0.0:993  0.0.0.0:*  users:(("dovecot",pid=1405,fd=44))
    tcp  LISTEN 0  100  0.0.0.0:143  0.0.0.0:*  users:(("dovecot",pid=1405,fd=42))
    tcp  LISTEN 0  100     [::]:993     [::]:*  users:(("dovecot",pid=1405,fd=45))
    tcp  LISTEN 0  100     [::]:143     [::]:*  users:(("dovecot",pid=1405,fd=43))
    ```

    In this example, Dovecot listens only on the TCP ports `993`{.literal} (IMAPS) and `143`{.literal} (IMAP).

    Note that Dovecot only opens a port for the LMTP protocol if you configure the service to listen on a port instead of using a socket.

### [1.8. Enabling server-side email filtering with Sieve on a Dovecot IMAP server](#enabling-server-side-email-filtering-with-sieve-on-a-dovecot-imap-server) {#enabling-server-side-email-filtering-with-sieve-on-a-dovecot-imap-server .title}

You can upload Sieve scripts to a server by using the ManageSieve protocol. Sieve scripts define rules and actions for incoming emails. For example, users can forward emails from a specific sender, and administrators can move spam-filtered emails to a separate IMAP folder.

The `ManageSieve`{.literal} plugin adds support for Sieve scripts and the ManageSieve protocol to a Dovecot IMAP server.

Warning

Use only clients that support using the ManageSieve protocol over TLS connections. Disabling TLS for this protocol causes clients to send credentials in plain text over the network.

**Prerequisites**

-   Dovecot is configured and provides IMAP mailboxes.
-   TLS encryption is configured in Dovecot.
-   The mail clients support the ManageSieve protocol over TLS connections.

**Procedure**

1.  Install the `dovecot-pigeonhole`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install dovecot-pigeonhole
    ```

2.  Uncomment the following line in `/etc/dovecot/conf.d/20-managesieve.conf`{.literal} to enable the `sieve`{.literal} protocol:

    ``` {.language-plaintext tabindex="-1"}
    protocols = $protocols sieve
    ```

    This setting activates Sieve in addition to the other protocols that are already enabled.

3.  Open the ManageSieve port in `firewalld`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=managesieve
    # firewall-cmd --reload
    ```

4.  Reload Dovecot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload dovecot
    ```

**Verification**

1.  Use a client and upload a Sieve script. Use the following connection settings:

    -   Port: 4190
    -   Connection security: SSL/TLS
    -   Authentication method: PLAIN

2.  Send an email to the user who has the Sieve script uploaded. If the email matches the rules in the script, verify that the server performs the defined actions.

### [1.9. How Dovecot processes configuration files](#how-dovecot-processes-configuration-files) {#how-dovecot-processes-configuration-files .title}

The `dovecot`{.literal} package provides the main configuration file `/etc/dovecot/dovecot.conf`{.literal} and multiple configuration files in the `/etc/dovecot/conf.d/`{.literal} directory. Dovecot combines the files to build the configuration when you start the service.

The main benefit of multiple config files is to group settings and increase readability. If you prefer a single configuration file, you can instead maintain all settings in `/etc/dovecot/dovecot.conf`{.literal} and remove all `include`{.literal} and `include_try`{.literal} statements from that file.

For further details, see the `/usr/share/doc/dovecot/wiki/ConfigFile.txt`{.literal} and `/usr/share/doc/dovecot/wiki/Variables.txt`{.literal} files.

## [Chapter 2. Deploying and configuring a Postfix SMTP server](#deploying-and-configuring-a-postfix-smtp-server) {#chapter-2.-deploying-and-configuring-a-postfix-smtp-server .title}

You can configure your email infrastructure by using the Postfix mail transport agent (MTA) to transport email messages between hosts by using the SMTP protocol. Postfix is a server-side application for routing and delivering mail.

Use Postfix to:

-   Configure a local mail server
-   Create a null-client mail relay
-   Use a Postfix server as a destination for multiple domains
-   Choose an LDAP directory instead of files for lookups

The `postfix`{.literal} package provides multiple configuration files in the `/etc/postfix/`{.literal} directory.

To configure your email infrastructure, use the following configuration files:

-   `main.cf`{.literal}: contains the global configuration of Postfix.
-   `master.cf`{.literal}: specifies Postfix interaction with various processes to accomplish mail delivery.
-   `access`{.literal}: specifies access rules, for example hosts that are allowed to connect to Postfix.
-   `transport`{.literal}: maps email addresses to relay hosts.
-   `aliases`{.literal}: contains a configurable list required by the mail protocol that describes user ID aliases. Note that you can find this file in the `/etc/`{.literal} directory.

The key features of Postfix:

-   Security features to protect against common email-related threats
-   Customization options, including support for virtual domains and aliases

### [2.1. Installing and configuring a Postfix SMTP server](#installing-and-configuring-a-postfix-smtp-server) {#installing-and-configuring-a-postfix-smtp-server .title}

You can configure your Postfix SMTP server to receive, store, and deliver email messages. If you do not select the mail server package during the system installation, Postfix will not be available by default.

**Prerequisites**

-   [The system is registered](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/registering-your-rhel-system).

**Procedure**

1.  Remove the Sendmail utility:

    ``` {.language-plaintext tabindex="-1"}
    # dnf remove sendmail
    ```

2.  Install Postfix:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install postfix
    ```

3.  To configure Postfix, edit the `/etc/postfix/main.cf`{.literal} file and make the following changes:

    a.  By default, Postfix receives emails only on the `loopback`{.literal} interface. To configure Postfix to listen on specific interfaces, update the `inet_interfaces`{.literal} parameter to the IP addresses of these interfaces:

        ``` {.language-plaintext tabindex="-1"}
        inet_interfaces = 127.0.0.1/32, [::1]/128, 192.0.2.1, [2001:db8:1::1]
        ```

        To configure Postfix to listen on all interfaces, set:

        ``` {.language-plaintext tabindex="-1"}
        inet_interfaces = all
        ```

    b.  If you want Postfix to use a different hostname than the fully-qualified domain name (FQDN) that is returned by the `gethostname()`{.literal} function, add the `myhostname`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        myhostname = smtp.example.com
        ```

        For example, Postfix adds this hostname to the header of emails it processes.

    c.  If the domain name differs from the one in the `myhostname`{.literal} parameter, add the `mydomain`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        mydomain = example.com
        ```

    d.  Add the `myorigin`{.literal} parameter and set it to the value of `mydomain`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        myorigin = $mydomain
        ```

        With this setting, Postfix uses the domain name as origin for locally posted mails instead of the hostname.

    e.  Add the `mynetworks`{.literal} parameter, and define the IP ranges of trusted networks that are allowed to send mails:

        ``` {.language-plaintext tabindex="-1"}
        mynetworks = 127.0.0.1/32, [::1]/128, 192.0.2.1/24, [2001:db8:1::1]/64
        ```

        If clients from non-trustworthy networks, such as the internet, should be able to send mails through this server, you must configure relay restrictions in a later step.

4.  Verify if the Postfix configuration in the `main.cf`{.literal} file is correct:

    ``` {.language-plaintext tabindex="-1"}
    # postfix check
    ```

5.  Enable the `postfix`{.literal} service to start at boot and start it:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now postfix
    ```

6.  Allow the SMTP traffic through firewall and reload the firewall rules:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service smtp
    # firewall-cmd --reload
    ```

**Verification**

1.  Verify that the `postfix`{.literal} service is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status postfix
    ```

    -   Optional: Restart the `postfix`{.literal} service, if the output is stopped, waiting, or the service is not running:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart postfix
        ```

    -   Optional: Reload the `postfix`{.literal} service after changing any options in the configuration files in the `/etc/postfix/`{.literal} directory to apply those changes:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl reload postfix
        ```

2.  Verify the email communication between local users on your system:

    ``` {.language-plaintext tabindex="-1"}
    # echo "This is a test message" | mail -s <subject> <user@mydomain.com>
    ```

3.  Verify that your mail server does not relay emails from external IP ranges to foreign domains:

    a.  Log in to a client which is not within the subnets that you defined in `mynetworks`{.literal}.

    b.  Configure the client to use your mail server.

    c.  Try to send an email to an email address that is not under the domain you specified in `mydomain`{.literal} on your mail server. For example, try to send an email to `non-existing-user@redhat.com`{.literal}.

    d.  Check the `/var/log/maillog`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        554 Relay access denied - the server is not going to relay.
        250 OK or similar - the server is going to relay.
        ```

**Troubleshooting**

-   In case of errors, check the `/var/log/maillog`{.literal} file.

**Additional resources**

-   [Using and configuring firewalld](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/using-and-configuring-firewalld)

### [2.2. Customizing TLS settings of a Postfix server](#customizing-tls-settings-of-a-postfix-server) {#customizing-tls-settings-of-a-postfix-server .title}

With Transport Layer Security (TLS), you can encrypt email traffic to increase security. For example, you can customize TLS settings and use a certificate from a trusted certificate authority (CA) instead of the self-signed certificate.

By default, the Postfix TLS configuration enables the TLS protocol. It uses self-signed certificates for inbound SMTP and opportunistic TLS for outbound SMTP.

**Prerequisites**

-   You have the `postfix`{.literal} package installed on your server.

-   You have a certificate signed by a trusted certificate authority (CA) and a private key.

-   You have copied the following files to the Postfix server:

    -   The server certificate: `/etc/pki/tls/certs/postfix.pem`{.literal}
    -   The private key: `/etc/pki/tls/private/postfix.key`{.literal}

-   If the FIPS mode is enabled, clients must either support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Set the path to the certificate and private key files on the server where Postfix is running by adding the following lines to the `/etc/postfix/main.cf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    smtpd_tls_cert_file = /etc/pki/tls/certs/postfix.pem
    smtpd_tls_key_file = /etc/pki/tls/private/postfix.key
    ```

2.  Restrict the incoming SMTP connections to authenticated users only by editing the `/etc/postfix/main.cf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    smtpd_tls_auth_only = yes
    ```

3.  Reload the `postfix`{.literal} service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload postfix
    ```

**Verification**

-   Configure your client to use TLS encryption and send an email.

    Note

    To get additional information about Postfix client TLS activity, increase the log level from `0`{.literal} to `1`{.literal} by changing the following line in the `/etc/postfix/main.cf`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    smtp_tls_loglevel = 1
    ```

### [2.3. Configuring Postfix to forward all emails to a mail relay](#configuring-postfix-to-forward-all-emails-to-a-mail-relay) {#configuring-postfix-to-forward-all-emails-to-a-mail-relay .title}

If you want to forward all email to a mail relay, you can configure Postfix server as a null client. In this configuration Postfix only forwards mail to a different mail server and is not capable of receiving mail.

**Prerequisites**

-   You have the `postfix`{.literal} package installed on your server.
-   You have the IP address or hostname of the relay host to which you want to forward emails.

**Procedure**

1.  To prevent Postfix from accepting any local email delivery and making it a null client, edit the `/etc/postfix/main.cf`{.literal} file and make the following changes:

    a.  Configure Postfix to forward all email by setting the `mydestination`{.literal} parameter equal to an empty value:

        ``` {.language-plaintext tabindex="-1"}
        mydestination =
        ```

        In this configuration the Postfix server is not a destination for any email and acts as a null client.

    b.  Specify the mail relay server that receives the email from your null client:

        ``` {.language-plaintext tabindex="-1"}
        relayhost = [<ip_address_or_hostname>]
        ```

        The relay host is responsible for the mail delivery. Enclose *`<ip_address_or_hostname>`{.literal}* in square brackets.

    c.  Configure the Postfix mail server to listen only on the loopback interface for emails to deliver:

        ``` {.language-plaintext tabindex="-1"}
        inet_interfaces = loopback-only
        ```

    d.  If you want Postfix to rewrite the sender domain of all outgoing emails to the company domain of your relay mail server, set:

        ``` {.language-plaintext tabindex="-1"}
        myorigin = relay.example.com
        ```

    e.  To disable the local mail delivery, add the following directive at the end of the configuration file:

        ``` {.language-plaintext tabindex="-1"}
        local_transport = error: local delivery disabled
        ```

    f.  Add the `mynetworks`{.literal} parameter so that Postfix forwards email from the local system originating from the 127.0.0.0/8 IPv4 network and the \[::1\]/128 IPv6 network to the mail relay server:

        ``` {.language-plaintext tabindex="-1"}
        mynetworks = 127.0.0.0/8, [::1]/128
        ```

2.  Verify if the Postfix configuration in the `main.cf`{.literal} file is correct:

    ``` {.language-plaintext tabindex="-1"}
    # postfix check
    ```

3.  Restart the `postfix`{.literal} service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart postfix
    ```

**Verification**

-   Verify that the email communication is forwarded to the mail relay:

    ``` {.language-plaintext tabindex="-1"}
    # echo "This is a test message" | mail -s <subject> <user@example.com>
    ```

**Troubleshooting**

-   In case of errors, check the `/var/log/maillog`{.literal} file.

### [2.4. Configuring Postfix as a destination for multiple domains](#configuring-postfix-as-a-destination-for-multiple-domains) {#configuring-postfix-as-a-destination-for-multiple-domains .title}

You can configure Postfix as a mail server that can receive emails for multiple domains. In this configuration, Postfix acts as the final destination for emails sent to addresses within the specified domains.

A multi-domain Postfix configuration supports the following scenarios:

-   Create multiple email addresses that forward to the same destination.
-   Route incoming email for multiple domains to the same Postfix server.

**Prerequisites**

-   You have configured a Postfix server.

**Procedure**

1.  In the `/etc/postfix/virtual`{.literal} virtual alias file, specify the email addresses for each domain. Add each email address on a new line:

    ``` {.language-plaintext tabindex="-1"}
    <info@example.com>   <user22@example.net>
    <sales@example.com>  <user11@example.org>
    ```

    In this example, Postfix redirects all emails sent to info@example.com to user22@example.net and email sent to sales@example.com to user11@example.org.

2.  Create a hash file for the virtual alias map:

    ``` {.language-plaintext tabindex="-1"}
    # postmap /etc/postfix/virtual
    ```

    This command creates the `/etc/postfix/virtual.db`{.literal} file. Note that you must always re-run this command after you update the `/etc/postfix/virtual`{.literal} file.

3.  In the Postfix `/etc/postfix/main.cf`{.literal} configuration file, add the `virtual_alias_maps`{.literal} parameter and point it to the hash file:

    ``` {.language-plaintext tabindex="-1"}
    virtual_alias_maps = hash:/etc/postfix/virtual
    ```

4.  Reload the `postfix`{.literal} service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload postfix
    ```

**Verification**

-   Test the configuration by sending an email to one of the virtual email addresses.

**Troubleshooting**

-   In case of errors, check the `/var/log/maillog`{.literal} file.

### [2.5. Using an LDAP directory as a lookup table](#using-an-ldap-directory-as-a-lookup-table) {#using-an-ldap-directory-as-a-lookup-table .title}

If you use a Lightweight Directory Access Protocol (LDAP) server to store accounts, domains or aliases, you can configure Postfix to use the LDAP server as a lookup table. Using LDAP instead of files for lookups enables you to have a central database.

**Prerequisites**

-   You have the `postfix`{.literal} package installed on your server.
-   You have an LDAP server with the required schema and user credentials.
-   You have the `postfix-ldap`{.literal} plugin installed on the server running Postfix.

**Procedure**

1.  Configure the LDAP lookup parameters by creating a `/etc/postfix/ldap-aliases.cf`{.literal} file with the following content:

    a.  Specify the hostname of the LDAP server:

        ``` {.language-plaintext tabindex="-1"}
        server_host = ldap.example.com
        ```

    b.  Specify the base domain name for the LDAP search:

        ``` {.language-plaintext tabindex="-1"}
        search_base = dc=example,dc=com
        ```

    c.  Optional: Customize the LDAP search filter and attributes based on your requirements. The filter for searching the directory defaults to `query_filter = mailacceptinggeneralid=%s`{.literal}.

2.  Enable the LDAP source as a lookup table in the `/etc/postfix/main.cf`{.literal} configuration file by adding the following content:

    ``` {.language-plaintext tabindex="-1"}
    virtual_alias_maps = ldap:/etc/postfix/ldap-aliases.cf
    ```

    For further details, see the `/usr/share/doc/postfix/README_FILES/LDAP_README`{.literal} and `/usr/share/doc/postfix/README_FILES/DATABASE_README`{.literal} files.

3.  Verify the LDAP configuration by running the `postmap`{.literal} command, which checks for any syntax errors or connectivity issues:

    ``` {.language-plaintext tabindex="-1"}
    # postmap -q @example.com ldap:/etc/postfix/ldap-aliases.cf
    ```

4.  Reload the `postfix`{.literal} service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload postfix
    ```

**Verification**

-   Send a test email to verify that the LDAP lookup works correctly. Check the mail logs in `/var/log/maillog`{.literal} for any errors.

### [2.6. Configuring Postfix as an outgoing mail server to relay for authenticated users](#configuring-postfix-as-an-outgoing-mail-server-to-relay-for-authenticated-users) {#configuring-postfix-as-an-outgoing-mail-server-to-relay-for-authenticated-users .title}

You can configure Postfix to securely relay mail for authenticated users. In this scenario, you allow users to authenticate themselves and use their email address to send mail through your SMTP server by configuring Postfix as an outgoing mail server.

**Prerequisites**

-   You have configured a Postfix server.

**Procedure**

1.  To configure Postfix as an outgoing mail server, edit the `/etc/postfix/main.cf`{.literal} file and add the following:

    a.  Enable SMTP authentication:

        ``` {.language-plaintext tabindex="-1"}
        smtpd_sasl_auth_enable = yes
        broken_sasl_auth_clients = yes
        ```

    b.  Disable access without TLS:

        ``` {.language-plaintext tabindex="-1"}
        smtpd_tls_auth_only = yes
        ```

    c.  Allow mail relaying only for authenticated users:

        ``` {.language-plaintext tabindex="-1"}
        smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination
        ```

    d.  Optional: Restrict users to use their own email address only as a sender:

        ``` {.language-plaintext tabindex="-1"}
        smtpd_sender_restrictions = reject_sender_login_mismatch
        ```

2.  Reload the `postfix`{.literal} service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload postfix
    ```

**Verification**

-   Authenticate in your SMTP client that supports transport layer security (TLS) and simple authentication and security layer (SASL). Send a test email to verify that the SMTP authentication works correctly.

### [2.7. Delivering email from Postfix to Dovecot running on the same host](#delivering-email-from-postfix-to-dovecot-running-on-the-same-host) {#delivering-email-from-postfix-to-dovecot-running-on-the-same-host .title}

You can configure Postfix to deliver incoming mail to Dovecot on the same host by using LMTP over a UNIX socket. This socket enables direct communication between Postfix and Dovecot on the local machine.

**Prerequisites**

-   You have configured a Postfix server.
-   You have configured a Dovecot server, see [Configuring and maintaining a Dovecot IMAP and POP3 server](#configuring-and-maintaining-a-dovecot-imap-and-pop3-server "Chapter 1. Configuring and maintaining a Dovecot IMAP and POP3 server").
-   You have configured the LMTP socket on your Dovecot server, see [Configuring an LMTP socket and LMTPS listener](#configuring-an-lmtp-socket-and-lmtps-listener "1.6. Configuring an LMTP socket and LMTPS listener").

**Procedure**

1.  Configure Postfix to use the LMTP protocol and the UNIX domain socket for delivering mail to Dovecot in the `/etc/postfix/main.cf`{.literal} file:

    -   If you want to use virtual mailboxes, add the following content:

        ``` {.language-plaintext tabindex="-1"}
        virtual_transport = lmtp:unix:/var/run/dovecot/lmtp
        ```

    -   If you want to use non-virtual mailboxes, add the following content:

        ``` {.language-plaintext tabindex="-1"}
        mailbox_transport = lmtp:unix:/var/run/dovecot/lmtp
        ```

2.  Reload `postfix`{.literal} to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload postfix
    ```

**Verification**

-   Send a test email to verify that the LMTP socket works correctly. Check the mail logs in `/var/log/maillog`{.literal} for any errors.

### [2.8. Delivering email from Postfix to Dovecot running on a different host](#delivering-email-from-postfix-to-dovecot-running-on-a-different-host) {#delivering-email-from-postfix-to-dovecot-running-on-a-different-host .title}

You can establish a secure connection between Postfix mail server and the Dovecot delivery agent over the network. To do so, configure the LMTP service to use a network socket for delivering mail between mail servers.

By default, the LMTP service does not encrypt the LMTP protocol. However, if you configure TLS encryption, Dovecot automatically uses the same settings for the LMTP service. SMTP servers can then connect by using the `STARTTLS`{.literal} command over LMTP.

**Prerequisites**

-   You have configured a Postfix server.
-   You have configured a Dovecot server, see [Configuring and maintaining a Dovecot IMAP and POP3 server](#configuring-and-maintaining-a-dovecot-imap-and-pop3-server "Chapter 1. Configuring and maintaining a Dovecot IMAP and POP3 server").
-   You have configured the LMTP socket on your Dovecot server, see [Configuring an LMTP socket and LMTPS listener](#configuring-an-lmtp-socket-and-lmtps-listener "1.6. Configuring an LMTP socket and LMTPS listener").

**Procedure**

1.  Configure Postfix to use the LMTP protocol and the INET domain socket for delivering mail to Dovecot in the `/etc/postfix/main.cf`{.literal} file by adding the following content:

    ``` {.language-bash tabindex="-1"}
    mailbox_transport = lmtp:inet:<dovecot_host>:<port>
    ```

    Replace *`<dovecot_host>`{.literal}* with the IP address or hostname of the Dovecot server and `<port>`{.literal} with the port number of the LMTP service.

2.  Reload the `postfix`{.literal} service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload postfix
    ```

**Verification**

-   Send a test email to an address hosted by the remote Dovecot server and check the Dovecot logs to ensure that the mail was successfully delivered.

### [2.9. Securing the Postfix service](#securing-the-postfix-service) {#securing-the-postfix-service .title}

Secure the Postfix mail transfer agent by configuring it to use encryption and applying settings that mitigate risks from various attacks. This involves configuring SMTP Authentication (AUTH) using SASL and setting limits to reduce vulnerability to denial-of-service (DoS) attacks.

Postfix is a mail transfer agent (MTA) that uses the Simple Mail Transfer Protocol (SMTP) to deliver electronic messages between other MTAs and to email clients or delivery agents. Although MTAs can encrypt traffic between one another, they might not do so by default.

#### [2.9.1. Reducing Postfix network-related security risks](#reducing-postfix-network-related-security-risks) {#reducing-postfix-network-related-security-risks .title}

Reduce Postfix security risks related to the network by adjusting configuration options to restrict access.

To reduce the risk of attackers invading your system through the network, perform as many of the following tasks as possible:

-   Do not share the `/var/spool/postfix/`{.literal} mail spool directory on a Network File System (NFS) volume. NFSv2 and NFSv3 do not maintain control over user and group IDs, allowing users with the same UID to receive and read each other's mail. NFSv4 using Kerberos does not have this limitation because the `SECRPC_GSS`{.literal} kernel module does not use UID-based authentication. However, avoid placing the mail spool directory on NFS volumes to reduce security risks.
-   Require mail users to access Postfix using an email program only. Do not allow shell accounts on the mail server. Set all user shells in the `/etc/passwd`{.literal} file to `/sbin/nologin`{.literal}, with the possible exception of the `root`{.literal} user. This prevents users from directly accessing the mail server and reduces the attack surface.
-   To protect Postfix from a network attack, it is configured to only listen to the local loopback address by default. You can verify this by viewing the `inet_interfaces = localhost`{.literal} line in the `/etc/postfix/main.cf`{.literal} file. This ensures that Postfix only accepts mail messages, such as `cron`{.literal} job reports, from the local system and not from the network. This is the default setting and protects Postfix from a network attack. To remove the localhost restriction and allow Postfix to listen on all interfaces, set the `inet_interfaces`{.literal} parameter to `all`{.literal} in `/etc/postfix/main.cf`{.literal}.

#### [2.9.2. Postfix configuration options for limiting DoS attacks](#postfix-configuration-options-for-limiting-dos-attacks) {#postfix-configuration-options-for-limiting-dos-attacks .title}

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

#### [2.9.3. Configuring Postfix to use SASL](#configuring-postfix-to-use-sasl) {#configuring-postfix-to-use-sasl .title}

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

## [Legal Notice](#idm140592705019120) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
