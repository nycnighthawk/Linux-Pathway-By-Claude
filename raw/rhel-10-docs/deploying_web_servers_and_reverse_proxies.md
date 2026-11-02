---
{"title": "Deploying web servers and reverse proxies", "guide": "deploying_web_servers_and_reverse_proxies", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/deploying_web_servers_and_reverse_proxies/index", "retrieved": "2026-11-02", "license": "CC-BY-SA-3.0"}
---

# Deploying web servers and reverse proxies {#deploying-web-servers-and-reverse-proxies .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Configuring web servers and reverse proxies {#configuring-web-servers-and-reverse-proxies .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139883211375200)

**Abstract**

Configure and run the Apache HTTP web server, the NGINX web server, or the Squid caching proxy server. Configure TLS encryption. Configure Kerberos authentication for the Apache HTTP web server. Configure NGINX as a reverse proxy for the HTTP traffic or as an HTTP load balancer. Configure Squid as a caching proxy without authentication, with LDAP authentication, or with Kerberos authentication.

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

## [Chapter 1. Configuring the Apache HTTP web server](#setting-up-the-apache-http-web-server) {#chapter-1.-configuring-the-apache-http-web-server .title}

Deploy Apache HTTP Server to host websites and web applications. Configure virtual hosts, manage services, and distribute static or dynamic content efficiently to clients.

### [1.1. Introduction to the Apache HTTP web server](#introduction-to-the-apache-http-web-server) {#introduction-to-the-apache-http-web-server .title}

To host websites and web applications, you can use the Apache HTTP web server. A **web server** is a network service that distributes contents, including web pages and other document types, to clients over the internet.

Web servers are also known as HTTP servers because they use the HTTP protocol. The Apache HTTP Server, also known as `httpd`{.literal}, is an open source web server developed by the Apache Software Foundation. If you are upgrading from a previous release of Red Hat Enterprise Linux, you must update the `httpd`{.literal} service configuration.

### [1.2. The Apache configuration files](#the-apache-configuration-files) {#the-apache-configuration-files .title}

You can configure the Apache HTTP web server to set server parameters and virtual hosts. The `httpd`{.literal} service, by default, reads the configuration files after start.

+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Path                                   | Description                                                                                                                                                                                                      |
+:=======================================+:=================================================================================================================================================================================================================+
| `/etc/httpd/conf/httpd.conf`{.literal} | The main configuration file.                                                                                                                                                                                     |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/httpd/conf.d/`{.literal}         | The main configuration directory provides an auxiliary directory for configuration files.                                                                                                                        |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/httpd/conf.modules.d/`{.literal} | The auxiliary directory for configuration files which load installed dynamic modules packaged in Red Hat Enterprise Linux. In the default configuration, processing of these configuration files is on priority. |
+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.1. The httpd service configuration files

Show more

Although the main configuration file is suitable for most situations, you can also use other configuration options.

For any changes to take effect, restart the web server first. Create a backup of the configuration file before editing it to revert any changes.

To check the configuration for possible errors, enter:

``` {.language-bash tabindex="-1"}
# apachectl configtest
Syntax OK
```

For details, see the `apachectl(8)`{.literal} man page on your system.

### [1.3. Managing the httpd service](#managing-the-httpd-service) {#managing-the-httpd-service .title}

You can start, stop, and restart the `httpd`{.literal} service to manage the Apache HTTP web server.

**Prerequisites**

-   You have installed the Apache HTTP Server.

**Procedure**

-   To start the `httpd`{.literal} service, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start httpd
    ```

-   To stop the `httpd`{.literal} service, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop httpd
    ```

-   To restart the `httpd`{.literal} service, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart httpd
    ```

### [1.4. Configuring a single-instance Apache HTTP server](#setting-up-a-single-instance-apache-http-server) {#configuring-a-single-instance-apache-http-server .title}

To distribute static contents through your web server, configure the Apache HTTP Server to distribute these contents.

By default, the Apache HTTP Server provides the same content for all domains associated with the server. To provide different content for different domains, configure name-based virtual hosts. For details, see [Configuring Apache name-based virtual hosts](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/setting-up-the-apache-http-web-server#configuring-apache-name-based-virtual-hosts).

**Prerequisites**

-   You have created firewall rules to enable basic web service connectivity before configuring the Transport Layer Security (TLS) protocol.

**Procedure**

1.  Install the `httpd`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install httpd
    ```

2.  If you use `firewalld`{.literal}, open the TCP port `80`{.literal} in the local firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=80/tcp
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

3.  Enable and start the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now httpd
    ```

4.  Optional: Add HTML files to the `/var/www/html/`{.literal} directory.

    Note

    When adding content to `/var/www/html/`{.literal}, files and directories must be readable by the user under which `httpd`{.literal} runs by default. The content owner can be either the `root`{.literal} user and `root`{.literal} user group, or another user or group of the administrator's choice. If the content owner is the `root`{.literal} user and `root`{.literal} user group, the files must be readable by other users. All the files and directories must have the `httpd_sys_content_t`{.literal} SELinux context, which is applicable by default to all content within the `/var/www`{.literal} directory.

5.  Connect to a web browser at `http://`{.literal}*`server_IP_or_host_name`{.literal}*`/`{.literal}.

    If the `/var/www/html/`{.literal} directory is empty or does not contain an `index.html`{.literal} or `index.htm`{.literal} file, Apache displays the `Red Hat Enterprise Linux Test Page`{.literal}. If `/var/www/html/`{.literal} contains HTML files with a different name, you can load them by entering the URL to that file, such as `http://`{.literal}*`server_IP_or_host_name`{.literal}*`/`{.literal}*`example.html`{.literal}*.

    For details, see the `httpd.service(8)`{.literal} man page on your system.

### [1.5. Configuring Apache name-based virtual hosts](#configuring-apache-name-based-virtual-hosts) {#configuring-apache-name-based-virtual-hosts .title}

To host multiple websites of different domains on a single Apache HTTP Server, you can configure name-based virtual hosts. With name-based virtual hosts, the Apache HTTP Server can distribute different websites to different domains that resolve to the server IP address.

You can configure a name-based virtual host for both the `example.com`{.literal} and `example.net`{.literal} domains with separate document root directories. Both virtual hosts serve static HTML content.

**Prerequisites**

-   Clients and the web server resolve the `example.com`{.literal} and `example.net`{.literal} domain to the IP address of the web server.

    Note that you must manually add the `example.com`{.literal} and `example.net`{.literal} domain entries to your DNS server.

**Procedure**

1.  Install the `httpd`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install httpd
    ```

2.  Edit the `/etc/httpd/conf/httpd.conf`{.literal} file:

    a.  Append the following virtual host configuration for the `example.com`{.literal} domain:

        ``` {.language-plaintext tabindex="-1"}
        <VirtualHost *:80>
            DocumentRoot "/var/www/example.com/"
            ServerName example.com
            CustomLog /var/log/httpd/example.com_access.log combined
            ErrorLog /var/log/httpd/example.com_error.log
        </VirtualHost>
        ```

        These settings configure the following:

        -   All settings in the `<VirtualHost *:80>`{.literal} directive are specific for this virtual host.

        -   `DocumentRoot`{.literal} sets the path to the web content of the virtual host.

        -   `ServerName`{.literal} sets the domains for which this virtual host serves content.

            To set multiple domains, add the `ServerAlias`{.literal} parameter to the configuration and specify the additional domains separated with a space in this parameter.

        -   `CustomLog`{.literal} sets the path to the access log of the virtual host.

        -   `ErrorLog`{.literal} sets the path to the error log of the virtual host.

            Note

            The Apache HTTP Server uses the first virtual host found in the configuration also for requests that do not match any domain set in the `ServerName`{.literal} and `ServerAlias`{.literal} parameters. This also includes requests sent to the IP address of the server.

3.  Append a similar virtual host configuration for the `example.net`{.literal} domain:

    ``` {.language-plaintext tabindex="-1"}
    <VirtualHost *:80>
        DocumentRoot "/var/www/example.net/"
        ServerName example.net
        CustomLog /var/log/httpd/example.net_access.log combined
        ErrorLog /var/log/httpd/example.net_error.log
    </VirtualHost>
    ```

4.  Create the document roots for both virtual hosts:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /var/www/example.com/
    # mkdir /var/www/example.net/
    ```

5.  Install the `policycoreutils-python-utils`{.literal} package to run the `restorecon`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install policycoreutils-python-utils
    ```

6.  If you set paths in the `DocumentRoot`{.literal} parameters that are not within `/var/www/`{.literal}, set the `httpd_sys_content_t`{.literal} context on both document roots:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t httpd_sys_content_t "/srv/example.com(/.*)?"
    # restorecon -Rv /srv/example.com/
    # semanage fcontext -a -t httpd_sys_content_t "/srv/example.net(/.\*)?"
    # restorecon -Rv /srv/example.net/
    ```

    These commands set the `httpd_sys_content_t`{.literal} context on the `/srv/example.com/`{.literal} and `/srv/example.net/`{.literal} directory.

7.  If you use `firewalld`{.literal}, open port `80`{.literal} in the local firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=80/tcp
    # firewall-cmd --reload
    ```

8.  Enable and start the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now httpd
    ```

**Verification**

1.  Create a different example file in each virtual host's document root:

    ``` {.language-plaintext tabindex="-1"}
    # echo "vHost example.com" > /var/www/example.com/index.html
    # echo "vHost example.net" > /var/www/example.net/index.html
    ```

2.  Use a browser and connect to `http://example.com`{.literal}. The web server shows the example file from the `example.com`{.literal} virtual host.

For details, see `httpd(8)`{.literal} and `httpd.conf(5)`{.literal} man pages on your system.

### [1.6. Configuring Kerberos authentication for the Apache HTTP web server](#configuring-kerberos-authentication-for-the-apache-http-web-server) {#configuring-kerberos-authentication-for-the-apache-http-web-server .title}

To use the `mod_auth_gssapi`{.literal} Apache module on Red Hat Enterprise Linux (RHEL), configure Kerberos authentication for the Apache HTTP web server. The Generic Security Services API (`GSSAPI`{.literal}) is an interface for applications that make requests to use Kerberos security libraries.

#### [1.6.1. Configuring gss-proxy in an IdM environment](#setting-up-gss-proxy-in-an-idm-environment) {#configuring-gss-proxy-in-an-idm-environment .title}

To enable secure and authenticated access to Kerberos-protected resources across various services and applications, you can set up the Generic Security Services Proxy (`GSS-Proxy`{.literal}) on the Apache HTTP web server

You can implement the `gssproxy`{.literal} service to enable privilege separation for the `httpd`{.literal} server. `gssproxy`{.literal} provides security optimization to this process. Note that the `mod_auth_gssapi`{.literal} module replaces the `mod_auth_kerb`{.literal} module, which is no longer available in the current version of Red Hat Enterprise Linux (RHEL).

**Prerequisites**

-   You have installed the `httpd`{.literal}, `mod_auth_gssapi`{.literal} and `gssproxy`{.literal} packages.
-   You have configured and started the `httpd`{.literal} service.

**Procedure**

1.  Enable access to the `keytab`{.literal} file of the `HTTP/<SERVER_NAME>@realm`{.literal} principal by creating the service principal:

    ``` {.language-plaintext tabindex="-1"}
    # ipa service-add HTTP/<SERVER_NAME>
    ```

2.  Retrieve the `keytab`{.literal} for the principal stored in the `/etc/gssproxy/http.keytab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-getkeytab -s $(awk '/^server =/ {print $3}' /etc/ipa/default.conf) -k /etc/gssproxy/http.keytab -p HTTP/$(hostname -f)
    ```

    This step sets permissions to 400, therefore only the `root`{.literal} user has access to the `keytab`{.literal} file. The `apache`{.literal} user does not.

3.  Create the `/etc/gssproxy/80-httpd.conf`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [service/HTTP]
      mechs = krb5
      cred_store = keytab:/etc/gssproxy/http.keytab
      cred_store = ccache:/var/lib/gssproxy/clients/krb5cc_%U
      euid = apache
    ```

4.  Restart and enable the `gssproxy`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart gssproxy.service
    # systemctl enable gssproxy.service
    ```

**Verification**

1.  Obtain a Kerberos ticket:

    ``` {.language-plaintext tabindex="-1"}
    # kinit
    ```

2.  Open the URL to the protected directory in a browser.

For details, see `gssproxy(8)`{.literal}, `gssproxy-mech(8)`{.literal}, `gssproxy.conf(5)`{.literal} man pages on your system.

#### [1.6.2. Configuring Kerberos authentication for a directory shared by the Apache HTTP web server](#configuring-kerberos-authentication-for-a-directory-shared-by-the-apache-http-web-server) {#configuring-kerberos-authentication-for-a-directory-shared-by-the-apache-http-web-server .title}

To ensure only authorized users can access or modify contents in the `/var/www/html/private/`{.literal} directory, you can configure Kerberos authentication for this directory.

**Prerequisites**

-   You have installed the `httpd`{.literal}, `mod_auth_gssapi`{.literal} and `gssproxy`{.literal} packages.
-   You have configured and started the `httpd`{.literal} service.
-   You have configured and started the `gssproxy`{.literal} service.

**Procedure**

1.  Configure the `mod_auth_gssapi`{.literal} module to protect the `/var/www/html/private/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    <Location /var/www/html/private>
      AuthType GSSAPI
      AuthName "GSSAPI Login"
      Require valid-user
    </Location>
    ```

2.  Create system unit configuration drop-in file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl edit httpd.service
    ```

3.  Add the following parameter to the system drop-in file:

    ``` {.language-plaintext tabindex="-1"}
    [Service]
    Environment=GSS_USE_PROXY=1
    ```

4.  Reload the `systemd`{.literal} configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

5.  Restart the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart httpd.service
    ```

**Verification**

1.  Obtain a Kerberos ticket:

    ``` {.language-plaintext tabindex="-1"}
    # kinit
    ```

2.  Open the URL to the protected directory in a browser.

**Additional resources**

-   [Using GSS-Proxy for Apache httpd operation (Red Hat Knowledgebase)](https://access.redhat.com/articles/5854761)

### [1.7. Configuring TLS encryption on an Apache HTTP server](#configuring-tls-encryption-on-an-apache-http-server) {#configuring-tls-encryption-on-an-apache-http-server .title}

By default, Apache distributes content to clients by using an unsecured HTTP connection. To secure web traffic, you can enable TLS encryption and configure often used encryption-related settings on an Apache HTTP Server.

#### [1.7.1. Adding TLS encryption to an Apache HTTP server](#adding-tls-encryption-to-an-apache-http-server) {#adding-tls-encryption-to-an-apache-http-server .title}

You can secure web traffic by installing `mod_ssl`{.literal}. Configure the virtual host to use the IdM-issued private key and certificate to enable encrypted HTTPS connections for the domain by using the sub-CA credentials.

**Prerequisites**

-   The Apache HTTP Server is installed and running.

-   The private key is stored in the `/etc/pki/tls/private/example.com.key`{.literal} file.

    For details about creating a private key and certificate signing request (CSR), and how to request a certificate from a certificate authority (CA), see documentation of your CA.

-   The TLS certificate is stored in the `/etc/pki/tls/certs/example.com.crt`{.literal} file. If you use a different path, follow the corresponding steps of the procedure.

-   The CA certificate is stored in the `/etc/pki/tls/certs/ca.crt`{.literal} file. If you use a different path, follow the corresponding steps of the procedure.

-   The clients and the web server resolve the hostname of the server to the IP address of the web server.

-   If the server runs Red Hat Enterprise Linux 10 (RHEL) and the Federal Information Processing Standards (FIPS) mode is enabled, clients must either support the `Extended Master Secret`{.literal} (EMS) extension or use Transport Layer Security (TLS) 1.3. TLS 1.2 connections without EMS fail. For details, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Install the `mod_ssl`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install mod_ssl
    ```

2.  Edit the `/etc/httpd/conf.d/ssl.conf`{.literal} file and add the following settings to the `<VirtualHost _default_:443>`{.literal} directive:

    a.  Set the server name:

        ``` {.language-plaintext tabindex="-1"}
        ServerName example.com
        ```

        The server name must match the entry set in the `Common Name`{.literal} field of the certificate.

    b.  Optional: If the certificate includes additional host names in the `Subject Alt Names`{.literal} (SAN) field, you can configure `mod_ssl`{.literal} to provide TLS encryption also for these host names. To configure this, add the `ServerAliases`{.literal} parameter with corresponding names:

        ``` {.language-plaintext tabindex="-1"}
        ServerAlias www.example.com server.example.com
        ```

    c.  Set the paths to the private key, the server certificate, and the CA certificate:

        ``` {.language-plaintext tabindex="-1"}
        SSLCertificateKeyFile "/etc/pki/tls/private/example.com.key"
        SSLCertificateFile "/etc/pki/tls/certs/example.com.crt"
        SSLCACertificateFile "/etc/pki/tls/certs/ca.crt"
        ```

3.  For security reasons, configure that only the `root`{.literal} user can access the private key file:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:root /etc/pki/tls/private/example.com.key
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 600 /etc/pki/tls/private/example.com.key
    ```

    Warning

    If unauthorized users access the private key, revoke the certificate, create a new private key, and request a new certificate. Otherwise, the TLS connection is no longer secure.

    -   Open a web browser and connect to `https://`{.literal}*`example.com`{.literal}*.

**Additional resources**

-   [Security considerations for TLS in RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/planning-and-implementing-tls#security-considerations-for-tls-in-rhel-10)

#### [1.7.2. Setting the supported TLS protocol versions on an Apache HTTP server](#setting-the-supported-tls-protocol-versions-on-an-apache-http-server) {#setting-the-supported-tls-protocol-versions-on-an-apache-http-server .title}

The Apache HTTP server on Red Hat Enterprise Linux (RHEL) has a system level cryptographic policy. This policy defines browser-compatible safe default values. For example, in Apache HTTP Server, the `DEFAULT`{.literal} policy defines that only the `TLSv1.2`{.literal} and `TLSv1.3`{.literal} protocol versions are enabled.

You can manually configure TLS protocol versions that the Apache HTTP Server supports. You need to enable only specific TLS protocol versions in your environment in these cases:

-   If your environment requires that clients can also use the weak `TLS1`{.literal} (TLSv1.0) or `TLS1.1`{.literal} protocol.
-   If you want to configure that Apache only supports the `TLSv1.2`{.literal} or `TLSv1.3`{.literal} protocol.

**Prerequisites**

-   You have enabled transport layer security (TLS) encryption on the server.
-   If the Red Hat Enterprise Linux (RHEL) server is running in Federal Information Processing Standards (FIPS) mode, FIPS permits only connections that comply with cryptographic standards. In this mode, clients must either use TLS 1.3 or, if using TLS 1.2, support the `Extended Master Secret`{.literal} (EMS) extension. FIPS does not permit TLS 1.2 connections without EMS support. For additional information, see [TLS extension \"Extended Master Secret\" enforced (Red Hat Knowledgebase solution)](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Edit the `/etc/httpd/conf/httpd.conf`{.literal} file and add the `<VirtualHost>`{.literal} directive for which you want to set the `TLSv1.3`{.literal} protocol version:

    ``` {.language-plaintext tabindex="-1"}
    SSLProtocol -All TLSv1.3
    ```

2.  Restart the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart httpd
    ```

**Verification**

1.  Verify support for `TLSv1.3`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # openssl s_client -connect example.com:443 -tls1_3
    ```

2.  Verify support for `TLSv1.2`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # openssl s_client -connect example.com:443 -tls1_2
    ```

    If the server does not support the protocol, the command returns an error:

    ``` {.language-plaintext tabindex="-1"}
    140111600609088:error:1409442E:SSL routines:ssl3_read_bytes:tlsv1 alert protocol version:ssl/record/rec_layer_s3.c:1543:SSL alert number 70
    ```

3.  Optional: Repeat the command for other TLS protocol versions.

#### [1.7.3. Setting the supported ciphers on an Apache HTTP server](#setting-the-supported-ciphers-on-an-apache-http-server) {#setting-the-supported-ciphers-on-an-apache-http-server .title}

By default, the Apache HTTP Server uses the system-wide cryptographic policy that defines safe default values, which are also compatible with recent browsers. For the list of ciphers the system-wide cryptographic policy allows, see the `/etc/crypto-policies/back-ends/openssl.config`{.literal} file.

You can manually configure ciphers that the Apache HTTP Server supports.

**Prerequisites**

-   You have enabled Transport Layer Security (TLS) encryption on the server.

**Procedure**

1.  Install the `nmap`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install nmap
    ```

2.  Edit the `/etc/httpd/conf/httpd.conf`{.literal} file and add the `SSLCipherSuite`{.literal} parameter to the `<VirtualHost>`{.literal} directive for which you want to set the TLS ciphers:

    ``` {.language-plaintext tabindex="-1"}
    SSLCipherSuite "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH:!SHA1:!SHA256"
    ```

    This example enables only the `EECDH+AESGCM`{.literal}, `EDH+AESGCM`{.literal}, `AES256+EECDH`{.literal}, and `AES256+EDH`{.literal} ciphers and disables all ciphers that use the `SHA1`{.literal} and `SHA256`{.literal} message authentication code (MAC).

3.  Restart the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart httpd
    ```

**Verification**

-   Display the supported ciphers:

    ``` {.language-plaintext tabindex="-1"}
    # nmap --script ssl-enum-ciphers -p 443 example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    PORT    STATE SERVICE
    443/tcp open  https
    | ssl-enum-ciphers:
    |   TLSv1.2:
    |     ciphers:
    |       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
    |       TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (dh 2048) - A
    |       TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (ecdh_x25519) - A
    ...
    ```

**Additional resources**

-   [Installing the Apache HTTP server manual](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/setting-up-the-apache-http-web-server#installing-the-apache-http-server-manual)
-   [Configuring applications to use cryptographic hardware through PKCS #11](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/configuring-applications-to-use-cryptographic-hardware-through-pkcs-11#using-hsms-protecting-private-keys-in-apache)

### [1.8. Configuring TLS client certificate authentication](#configuring-tls-client-certificate-authentication) {#configuring-tls-client-certificate-authentication .title}

To allow only authenticated users to access resources on the web server, configure client certificate authentication for the `/var/www/html/Example/`{.literal} directory.

If the Apache HTTP Server uses the Transport Layer Security (TLS) 1.3 protocol, some clients require additional configuration. For example, in Mozilla Firefox, set the `security.tls.enable_post_handshake_auth`{.literal} parameter in the `about:config`{.literal} menu to `true`{.literal}.

**Prerequisites**

-   You have enabled TLS encryption on the server.

**Procedure**

1.  Edit the `/etc/httpd/conf/httpd.conf`{.literal} file to configure client authentication:

    ``` {.language-plaintext tabindex="-1"}
    <Directory "/var/www/html/Example/">
      SSLVerifyClient require
    </Directory>
    ```

    The `SSLVerifyClient require`{.literal} setting configures the server to require a client certificate before the client can access the content in the `/var/www/html/Example/`{.literal} directory.

2.  Restart the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart httpd
    ```

**Verification**

1.  Access the `https://example.com/Example/`{.literal} URL without client authentication:

    ``` {.language-plaintext tabindex="-1"}
    $ curl \https://example.com/Example/
    ```

    ``` {.language-plaintext tabindex="-1"}
    curl: (56) OpenSSL SSL_read: error:1409445C:SSL routines:ssl3_read_bytes:tlsv13 alert certificate required, errno 0
    ```

    The error indicates that the web server requires a client certificate authentication.

2.  Access the same URL with client authentication by passing the client private key and certificate, and the CA certificate:

    ``` {.language-plaintext tabindex="-1"}
    $ curl --cacert ca.crt --key client.key --cert client.crt https://example.com/Example/
    ```

    If the request succeeds, the `curl`{.literal} utility displays the `index.html`{.literal} file stored in the `/var/www/html/Example/`{.literal} directory.

### [1.9. Installing the Apache HTTP server manual](#installing-the-apache-http-server-manual) {#installing-the-apache-http-server-manual .title}

To perform various configuration tasks, you can use the Apache HTTP Server manual. This manual includes detailed documentation of configuration parameters and directives, performance tuning, authentication settings, modules, content caching, security tips, and configuring TLS encryption.

**Prerequisites**

-   The Apache HTTP Server is installed and running.

**Procedure**

1.  Install the `httpd-manual`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install httpd-manual
    ```

2.  Optional: By default, all clients connecting to the Apache HTTP Server can display the manual. To restrict access to a specific IP range, such as the `192.0.2.0/24`{.literal} subnet, edit the `/etc/httpd/conf.d/manual.conf`{.literal} file and add the `Require ip 192.0.2.0/24`{.literal} setting to the `<Directory "/usr/share/httpd/manual">`{.literal} directive:

    ``` {.language-plaintext tabindex="-1"}
    <Directory "/usr/share/httpd/manual">
    ...
        Require ip 192.0.2.0/24
    ...
    </Directory>
    ```

3.  Restart the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart httpd
    ```

**Verification**

-   To display the Apache HTTP Server manual, connect to the `http://`{.literal}*`host_name_or_IP_address`{.literal}*`/manual/`{.literal} URL with a web browser.

### [1.10. Working with Apache modules](#working-with-apache-modules) {#working-with-apache-modules .title}

The `httpd`{.literal} service is a modular application, and you can extend it with several Dynamic Shared Objects (DSO). You can dynamically load or unload DSO modules at runtime as necessary. You can find these modules in the `/usr/lib64/httpd/modules/`{.literal} directory.

#### [1.10.1. Loading a dynamic shared object module](#loading-a-dso-module) {#loading-a-dynamic-shared-object-module .title}

To configure the functionality for the Apache HTTP Server, you can load Dynamic Shared Object (DSO) modules. Use the `LoadModule`{.literal} directive to load a particular DSO module. A separate package has modules with their own configuration file stored in the `/etc/httpd/conf.modules.d/`{.literal} directory.

**Prerequisites**

-   You have installed the `httpd`{.literal} package.

**Procedure**

1.  Search for the module name in the configuration files in the `/etc/httpd/conf.modules.d/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # grep mod_ssl.so /etc/httpd/conf.modules.d/*
    ```

2.  Uncomment the `LoadModule`{.literal} directive of the module in the configuration file where the module name is present:

    ``` {.language-plaintext tabindex="-1"}
    LoadModule ssl_module modules/mod_ssl.so
    ```

3.  If the module does not exist, create a configuration file, such as `/etc/httpd/conf.modules.d/30-example.conf`{.literal} with the following directive:

    ``` {.language-plaintext tabindex="-1"}
    LoadModule ssl_module modules/<custom_module>.so
    ```

    For example, a Red Hat Enterprise Linux (RHEL) package does not include the module.

4.  Restart the `httpd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart httpd
    ```

**Verification**

-   Verify that the module is loaded and enabled:

    ``` {.language-plaintext tabindex="-1"}
    # httpd -M | grep ssl
    ```

#### [1.10.2. Compiling a custom Apache module](#compiling-a-custom-apache-module) {#compiling-a-custom-apache-module .title}

You can create your own module and build it by using the `httpd-devel`{.literal} package. This package includes header files, include files, and the **`Apache Extension`{.literal}** (`apxs`{.literal}) utility, which is required to compile a module.

**Prerequisites**

-   You have the `httpd-devel`{.literal} package installed.

**Procedure**

-   Build a custom module:

    ``` {.language-plaintext tabindex="-1"}
    # apxs -i -a -c module_name.c
    ```

**Verification**

-   Load the module the same way as described in [Loading a DSO module](#loading-a-dso-module "1.10.1. Loading a dynamic shared object module").

## [Chapter 2. Configuring NGINX](#setting-up-and-configuring-nginx) {#chapter-2.-configuring-nginx .title}

NGINX is a high-performance and modular server that you can use as a web server, a reverse proxy, or an HTTP load balancer.

### [2.1. Installing and preparing NGINX](#installing-and-preparing-nginx) {#installing-and-preparing-nginx .title}

Red Hat uses Application Streams to provide different versions of NGINX. With Application Streams, you can select a stream and install NGINX, open the required ports in the firewall, enable and start the `nginx`{.literal} service.

By default, an NGINX server runs on port `80`{.literal} and provides content from the `/usr/share/nginx/html/`{.literal} directory.

**Prerequisites**

-   You have a [Red Hat subscription](https://access.redhat.com/).
-   The `firewalld`{.literal} service is enabled and running.

**Procedure**

1.  Install the `nginx`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install nginx
    ```

2.  Open the ports on which NGINX should run its service in the firewall. For example, to open the default ports for HTTP (port 80) and HTTPS (port 443) in `firewalld`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port={80/tcp,443/tcp}
    # firewall-cmd --reload
    ```

3.  Enable the `nginx`{.literal} service to start automatically when the system boots:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable nginx
    ```

4.  Optional: Start the `nginx`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start nginx
    ```

    If you do not want to use the default configuration, skip this step, and configure NGINX before you start the service.

**Verification**

1.  Verify the installation of the `nginx`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf list installed nginx
    ```

    ``` {.language-plaintext tabindex="-1"}
    Installed Packages
    nginx.x86_64    1:1.14.1-9.module+el8.0.0+4108+af250afe    @rhel-8-for-x86_64-appstream-rpms
    ```

2.  Verify the allowed ports through the firewall on which NGINX should run its service:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --list-ports
    ```

    ``` {.language-plaintext tabindex="-1"}
    80/tcp 443/tcp
    ```

3.  Verify the `nginx`{.literal} service is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl is-enabled nginx
    ```

    ``` {.language-plaintext tabindex="-1"}
    enabled
    ```

**Additional resources**

-   [Subscription Manager](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/index#basic-reg-rhel-cli-sub-man)

### [2.2. Configuring NGINX as a web server to distribute different content for different domains](#configuring-nginx-as-a-web-server-that-provides-different-content-for-different-domains) {#configuring-nginx-as-a-web-server-to-distribute-different-content-for-different-domains .title}

To optimize resource usage and management, you can configure the NGINX web server to distribute different content for different domains. By default, NGINX distributes the same content to clients for all domain names associated with the IP addresses of the server.

You can configure NGINX to serve different content for different domains. For example, configure the `example.com`{.literal} domain with content from the `/var/www/example.com/`{.literal} directory, and configure the `example.net`{.literal} domain with content from the `/var/www/example.net/`{.literal} directory. Configure all other requests to use content from the `/usr/share/nginx/html/`{.literal} directory.

**Prerequisites**

-   NGINX is installed.

-   Clients and the web server resolve the `example.com`{.literal} and `example.net`{.literal} domain to the IP address of the web server.

    Note that you must manually add these entries to your DNS server.

**Procedure**

1.  Edit the `/etc/nginx/nginx.conf`{.literal} file:

    a.  By default, the `/etc/nginx/nginx.conf`{.literal} file already has a default configuration. If you have deleted this part from the configuration, re-add the following `server`{.literal} block to the `http`{.literal} block in the `/etc/nginx/nginx.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        server {
            listen       80 default_server;
            listen       [::]:80 default_server;
            server_name  _;
            root         /usr/share/nginx/html;
        }
        ```

        -   The `listen`{.literal} directive defines which IP address and ports the service listens. In this case, NGINX listens on port `80`{.literal} on both all IPv4 and IPv6 addresses. The `default_server`{.literal} parameter indicates that NGINX uses this `server`{.literal} block as the default for requests matching the IP addresses and ports.
        -   The `server_name`{.literal} parameter defines the host names for which this `server`{.literal} block is responsible. Setting `server_name`{.literal} to `_`{.literal} configures NGINX to accept any hostname for this `server`{.literal} block.
        -   The `root`{.literal} directive sets the path to the web content for this `server`{.literal} block.

    b.  Append a similar `server`{.literal} block for the `example.com`{.literal} domain to the `http`{.literal} block:

        ``` {.language-plaintext tabindex="-1"}
        server {
            server_name  example.com;
            root         /var/www/example.com/;
            access_log   /var/log/nginx/example.com/access.log;
            error_log    /var/log/nginx/example.com/error.log;
        }
        ```

        -   The `access_log`{.literal} directive defines a separate access log file for this domain.
        -   The `error_log`{.literal} directive defines a separate error log file for this domain.

    c.  Append a similar `server`{.literal} block for the `example.net`{.literal} domain to the `http`{.literal} block:

        ``` {.language-plaintext tabindex="-1"}
        server {
            server_name  example.net;
            root         /var/www/example.net/;
            access_log   /var/log/nginx/example.net/access.log;
            error_log    /var/log/nginx/example.net/error.log;
        }
        ```

2.  Create the main directories for both domains:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /var/www/example.com/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /var/www/example.net/
    ```

3.  Set the `httpd_sys_content_t`{.literal} context on both main directories:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t httpd_sys_content_t "/var/www/example.com(/.\*)?"
    ```

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /var/www/example.com/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t httpd_sys_content_t "/var/www/example.net(/.\*)?"
    ```

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /var/www/example.net/
    ```

    These commands set the `httpd_sys_content_t`{.literal} context on the `/var/www/example.com/`{.literal} and `/var/www/example.net/`{.literal} directories.

    Note that you must install the `policycoreutils-python-utils`{.literal} package to run the `restorecon`{.literal} commands.

4.  Create the log directories for both domains:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /var/log/nginx/example.com/
    # mkdir /var/log/nginx/example.net/
    ```

5.  Restart the `nginx`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart nginx
    ```

**Verification**

1.  Create a different example file in each virtual host's document root:

    ``` {.language-plaintext tabindex="-1"}
    # echo "Content for example.com" > /var/www/example.com/index.html
    # echo "Content for example.net" > /var/www/example.net/index.html
    # echo "Catch All content" > /usr/share/nginx/html/index.html
    ```

2.  Use a browser and connect to `http://example.com`{.literal}. The web server shows the example content from the `/var/www/example.com/index.html`{.literal} file.

3.  Use a browser and connect to `http://example.net`{.literal}. The web server shows the example content from the `/var/www/example.net/index.html`{.literal} file.

4.  Use a browser and connect to `http://`{.literal}*`IP_address_of_the_server`{.literal}*. The web server shows the example content from the `/usr/share/nginx/html/index.html`{.literal} file.

### [2.3. Adding TLS encryption to an NGINX web server](#adding-tls-encryption-to-an-nginx-web-server) {#adding-tls-encryption-to-an-nginx-web-server .title}

To protect against eavesdropping and man-in-the-middle attacks, you can enable Transport Layer Security (TLS) protocol encryption on an NGINX web server.

**Prerequisites**

-   You have installed NGINX. For details, see [installing and preparing NGINX](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_web_servers_and_reverse_proxies/setting-up-and-configuring-nginx#installing-and-preparing-nginx).

-   The private key is stored in the `/etc/pki/tls/private/example.com.key`{.literal} file.

    For details about creating a private key and certificate signing request (CSR), and how to request a certificate from a certificate authority (CA), see documentation of your CA.

-   The TLS certificate is stored in the `/etc/pki/tls/certs/example.com.crt`{.literal} file. If you use a different path, adapt the corresponding steps of the procedure.

-   The CA certificate has been appended to the TLS certificate file of the server.

-   Clients and the web server resolve the hostname of the server to the IP address of the web server.

-   Port `443`{.literal} is open in the local firewall.

-   If the Red Hat Enterprise Linux (RHEL) server is running in Federal Information Processing Standards (FIPS) mode, FIPS permits only connections that comply with cryptographic standards. In this mode, clients must either use TLS 1.3 or, if using TLS 1.2, support the `Extended Master Secret`{.literal} (EMS) extension. FIPS does not permit TLS 1.2 connections without EMS support. For additional information, see [TLS extension \"Extended Master Secret\" enforced (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Edit the `/etc/nginx/nginx.conf`{.literal} file, and add the following `server`{.literal} block to the `http`{.literal} block in the configuration:

    ``` {.language-plaintext tabindex="-1"}
    server {
        listen              443 ssl;
        server_name         example.com;
        root                /usr/share/nginx/html;
        ssl_certificate     /etc/pki/tls/certs/example.com.crt;
        ssl_certificate_key /etc/pki/tls/private/example.com.key;
    }
    ```

2.  Optional: Starting from RHEL 9.3, you can use the `ssl_pass_phrase_dialog`{.literal} directive to configure an external program that NGINX calls at startup for each encrypted private key. Add one of the following lines to the `/etc/nginx/nginx.conf`{.literal} file:

    -   To call an external program for each encrypted private key file, enter:

        ``` {.language-plaintext tabindex="-1"}
        ssl_pass_phrase_dialog exec:<path_to_program>;
        ```

        NGINX calls this program with the following two arguments:

        -   The server name specified in the `server_name`{.literal} setting.
        -   One of the following algorithms: Rivest-Shamir-Adleman (RSA), Digital Signature Algorithm (DSA), Elliptic Curve (EC), Diffie-Hellman (DH), or `UNK`{.literal} if NGINX cannot recognize a cryptographic algorithm.

    -   If you want to manually enter a passphrase for each encrypted private key file, enter:

        ``` {.language-plaintext tabindex="-1"}
        ssl_pass_phrase_dialog builtin;
        ```

        This is the default behavior if `ssl_pass_phrase_dialog`{.literal} is not configured.

        Note that the `nginx`{.literal} service fails to start if you use this method but have at least one private key protected by a passphrase. In this case, use one of the other methods.

    -   If you want `systemd`{.literal} to prompt for the passphrase for each encrypted private key when you start the `nginx`{.literal} service by using the `systemctl`{.literal} utility, enter:

        ``` {.language-plaintext tabindex="-1"}
        ssl_pass_phrase_dialog exec:/usr/libexec/nginx-ssl-pass-dialog;
        ```

3.  For security reasons, configure that only the `root`{.literal} user can access the private key file:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:root /etc/pki/tls/private/example.com.key
    # chmod 600 /etc/pki/tls/private/example.com.key
    ```

    Warning

    If unauthorized users have access to the private key, revoke the certificate, create a new private key, and request a new certificate. Otherwise, the TLS connection is no longer secure.

4.  Restart the `nginx`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart nginx
    ```

**Verification**

-   Use a browser and connect to `https://example.com`{.literal}.

**Additional resources**

-   [Security considerations for TLS in RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/planning-and-implementing-tls#security-considerations-for-tls-in-rhel-10)

### [2.4. Configuring NGINX as a reverse proxy for the HTTP traffic](#configuring-nginx-as-a-reverse-proxy-for-the-http-traffic) {#configuring-nginx-as-a-reverse-proxy-for-the-http-traffic .title}

To forward requests to a specific subdirectory on a remote server, you can configure the NGINX web server to act as a reverse proxy for HTTP traffic.

When NGINX acts as a reverse proxy, the client loads the content from the host it accesses. However, NGINX loads the actual content from the remote server and forwards it to the client. You can configure NGINX to forward traffic from the `/example`{.literal} directory on the web server to the URL `https://example.com`{.literal}.

**Prerequisites**

-   NGINX is installed.
-   Optional: TLS encryption is enabled on the reverse proxy.

**Procedure**

1.  Edit the `/etc/nginx/nginx.conf`{.literal} file and add the following settings to the `server`{.literal} block that should provide the reverse proxy:

    ``` {.language-plaintext tabindex="-1"}
    location /example {
        proxy_pass https://example.com;
    }
    ```

    The `location`{.literal} block defines that NGINX passes all requests in the `/example`{.literal} directory to `https://example.com`{.literal}.

2.  Set the `httpd_can_network_connect`{.literal} Security-Enhanced Linux (SELinux) boolean parameter to `1`{.literal} to configure that SELinux allows NGINX to forward traffic:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool -P httpd_can_network_connect 1
    ```

3.  Restart the `nginx`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart nginx
    ```

**Verification**

-   Use a browser and connect to `http://`{.literal}*`host_name`{.literal}*`/example`{.literal} and the content of `https://example.com`{.literal} is shown.

### [2.5. Configuring NGINX as an HTTP load balancer](#configuring-nginx-as-an-http-load-balancer) {#configuring-nginx-as-an-http-load-balancer .title}

To configure the number of requests to different servers and define a fallback host, you can use the NGINX reverse proxy feature for load balancing.

Configuring NGINX as an HTTP load balancer directs traffic to multiple servers. The load balancer selects a server with the fewest active connections. If the primary servers are unavailable, NGINX automatically sends requests to the fallback host.

**Prerequisites**

-   You have installed NGINX.

**Procedure**

1.  Edit settings in the `/etc/nginx/nginx.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    http {
        upstream backend {
            least_conn;
            server server1.example.com;
            server server2.example.com;
            server server3.example.com backup;
        }

        server {
            location / {
                proxy_pass http://backend;
            }
        }
    }
    ```

    The `least_conn`{.literal} directive in the `backend`{.literal} named host group defines that NGINX sends requests to `server1.example.com`{.literal} or `server2.example.com`{.literal}. This directive selects the server with the least number of active connections. NGINX uses `server3.example.com`{.literal} only as a backup in case the other two hosts are unavailable.

    With the `proxy_pass`{.literal} directive set to `http://backend`{.literal}, NGINX acts as a reverse proxy and uses the `backend`{.literal} host group to distribute requests based on the settings of this group.

    Instead of the `least_conn`{.literal} load balancing method, you can specify:

    -   No method to use round robin and distribute requests evenly across servers.
    -   `ip_hash`{.literal}: Send requests from one client address to the same server. The request is based on a hash calculated from the first three octets of the IPv4 address or the entire IPv6 address of the client.
    -   `hash`{.literal}: Decide the server based on a user-defined key, which can be a string, a variable, or a combination of both. The `consistent`{.literal} parameter configures that NGINX distributes requests across all servers based on the user-defined hashed key value.
    -   `random`{.literal}: Send requests to a randomly selected server.

2.  Restart the `nginx`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart nginx
    ```

## [Chapter 3. Configuring the Squid caching proxy server](#configuring-the-squid-caching-proxy-server) {#chapter-3.-configuring-the-squid-caching-proxy-server .title}

To reduce bandwidth and quickly load web pages, use Squid. It is a caching proxy server that can act as a proxy for HTTP, HTTPS, and FTP protocols, and allows access authentication and restrictions. For details, see the configuration parameters at `/usr/share/doc/squid/squid.conf.documented`{.literal}.

### [3.1. Configuring Squid as a caching proxy without authentication](#setting-up-squid-as-a-caching-proxy-without-authentication) {#configuring-squid-as-a-caching-proxy-without-authentication .title}

To simplify access for users while improving bandwidth efficiency and response time by using the content caching, configure Squid as a caching proxy without authentication. You need to limit access to the proxy, based on IP ranges only.

**Prerequisites**

-   The `squid`{.literal} package includes the `/etc/squid/squid.conf`{.literal} file. If you edited this file before, remove and reinstall the package.

**Procedure**

1.  Install the `squid`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install squid
    ```

2.  Edit the `/etc/squid/squid.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/squid/squid.conf
    ```

    a.  Adapt the `localnet`{.literal} access control lists (ACL) to match the allowed IP ranges that can access the proxy:

        ``` {.language-plaintext tabindex="-1"}
        acl localnet src 192.0.2.0/24
        acl localnet 2001:db8:1::/64
        ```

        By default, the `/etc/squid/squid.conf`{.literal} file includes the `http_access allow localnet`{.literal} rule. This rule uses the proxy from all IP ranges specified in `localnet`{.literal} ACL. You must specify all `localnet`{.literal} ACL before the `http_access allow localnet`{.literal} rule.

        Important

        Remove all existing `acl localnet`{.literal} entries that do not match your environment.

    b.  To grant users to use the HTTPS protocol on other ports, add an ACL for each of these ports:

        ``` {.language-plaintext tabindex="-1"}
        acl SSL_ports port <port_number>
        ```

        The following ACL exists in the default configuration and defines `443`{.literal} as a port that uses the HTTPS protocol:

        ``` {.language-plaintext tabindex="-1"}
        acl SSL_ports port 443
        ```

    c.  Update the list of `acl Safe_ports`{.literal} rules to configure to which ports Squid can establish a connection:

        ``` {.language-plaintext tabindex="-1"}
        acl Safe_ports port 21
        acl Safe_ports port 80
        acl Safe_ports port 443
        ```

        Configure the clients to only access resources on ports `21`{.literal} file transfer protocol (FTP), `80`{.literal} (HTTP), and `443`{.literal} (HTTPS) over the proxy. Add the `acl Safe_ports`{.literal} statements to the configuration file. By default, the configuration file includes the `http_access deny !Safe_ports`{.literal} rule. This rule defines access denial to ports that are not defined in the `Safe_ports`{.literal} ACL.

    d.  Configure the cache type, the path to the cache directory, the cache size, and further cache type-specific settings in the `cache_dir`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        cache_dir ufs /var/spool/squid 10000 16 256
        ```

        With these settings:

        -   Squid uses the `ufs`{.literal} cache type.

        -   Squid stores its cache in the `/var/spool/squid/`{.literal} directory.

        -   The cache grows up to `10000`{.literal} MB.

        -   Squid creates `16`{.literal} level-1 sub-directories in the `/var/spool/squid/`{.literal} directory.

        -   Squid creates `256`{.literal} sub-directories in each level-1 directory.

            If you do not set a `cache_dir`{.literal} directive, Squid stores the cache in memory.

3.  If you set a different cache directory than `/var/spool/squid/`{.literal} in the `cache_dir`{.literal} parameter:

    a.  Create the cache directory:

        ``` {.language-plaintext tabindex="-1"}
        # mkdir -p <path_to_cache_directory>
        ```

    b.  Configure the permissions for the cache directory:

        ``` {.language-plaintext tabindex="-1"}
        # chown squid:squid <path_to_cache_directory>
        ```

    c.  If the `semanage`{.literal} utility is not available, install the `policycoreutils-python-utils`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install policycoreutils-python-utils
        ```

    d.  Set the `squid_cache_t`{.literal} context for the cache directory if Security-Enhanced Linux (SELinux) is in the `enforcing`{.literal} mode:

        ``` {.language-plaintext tabindex="-1"}
        # semanage fcontext -a -t squid_cache_t "<path_to_cache_directory>(/.)?"*
        ```

        ``` {.language-plaintext tabindex="-1"}
        # restorecon -Rv <path_to_cache_directory>
        ```

4.  Open the `3128`{.literal} port in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=3128/tcp
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

5.  Enable and start the `squid`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now squid
    ```

**Verification**

-   Download a web page by using the `curl`{.literal} utility to verify that the proxy works correctly:

    ``` {.language-plaintext tabindex="-1"}
    # curl -O -L "https://www.redhat.com/index.html" -x "proxy.example.com:3128"
    ```

    If `curl`{.literal} does not display any error and the `index.html`{.literal} file gets downloaded to the current directory, the proxy works.

### [3.2. Configuring Squid as a caching proxy with LDAP authentication](#setting-up-squid-as-a-caching-proxy-with-ldap-authentication) {#configuring-squid-as-a-caching-proxy-with-ldap-authentication .title}

To allow only authenticated users to use the proxy, configure Squid as a caching proxy with the Lightweight Directory Access Protocol (LDAP) authentication.

**Prerequisites**

-   You have installed the `squid`{.literal} package.
-   The `squid`{.literal} package includes the `/etc/squid/squid.conf`{.literal} file. If you edited this file before, remove and reinstall the package.
-   A service user, such as `uid=proxy_user,cn=users,cn=accounts,dc=example,dc=com`{.literal} exists in the LDAP directory. Squid uses this account only to search for the authenticating user. If the authenticating user exists, Squid binds this user to the directory to verify the authentication.

**Procedure**

1.  Edit the `/etc/squid/squid.conf`{.literal} file:

    a.  To configure the `basic_ldap_auth`{.literal} helper utility, add the following configuration entry to the top of `/etc/squid/squid.conf`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        auth_param basic program /usr/lib64/squid/basic_ldap_auth -b "cn=users,cn=accounts,dc=example,dc=com" -D "uid=proxy_user,cn=users,cn=accounts,dc=example,dc=com" -W /etc/squid/ldap_password -f "(&(objectClass=person)(uid=%s))" -ZZ -H ldap://ldap_server.example.com:389
        ```

        -   `-b `{.literal}*`base_DN`{.literal}* specifies the distinguished name (DN) of the LDAP search base from which Squid will start searching for users.

        -   `-D `{.literal}*`proxy_service_user_DN`{.literal}* sets the DN of the account Squid uses to search for the authenticating user in the directory.

        -   `-W `{.literal}*`path_to_password_file`{.literal}* sets the path to the file that has the password of the proxy service user. Using a password file prevents that the password is visible in the operating system's process list.

        -   `-f `{.literal}*`LDAP_filter`{.literal}* specifies the LDAP search filter. Squid replaces the `%s`{.literal} variable with the user name provided by the authenticating user.

            The `(&(objectClass=person)(uid=%s))`{.literal} filter in the example defines that the user name must match the value set in the `uid`{.literal} attribute and that the directory entry includes the `person`{.literal} object class.

        -   `-ZZ`{.literal} enforces a transport layer security (TLS) encrypted connection over the LDAP protocol using the `STARTTLS`{.literal} command. Omit the `-ZZ`{.literal} in the following situations:

            -   The LDAP server does not support encrypted connections.
            -   The port specified in the URL uses the Lightweight Directory Access Protocol Secure (LDAPS) protocol.

        -   The -H LDAP_URL parameter specifies the protocol, the hostname or IP address, and the port of the LDAP server in URL format.

    b.  Add the following Access Control List (ACL) and rule to configure that Squid allows only authenticated users to use the proxy:

        ``` {.language-plaintext tabindex="-1"}
        acl ldap-auth proxy_auth REQUIRED
        http_access allow ldap-auth
        ```

        Important

        Specify these settings before the `http_access deny`{.literal} all rule.

    c.  Remove the following rule to disable bypassing the proxy authentication from IP ranges specified in `localnet`{.literal} ACLs:

        ``` {.language-plaintext tabindex="-1"}
        http_access allow localnet
        ```

    d.  Add an ACL for each of these ports so that users can use the HTTPS protocol on other ports:

        ``` {.language-plaintext tabindex="-1"}
        acl SSL_ports port port_number
        ```

        For example, the following ACL exists in the default configuration and defines `443`{.literal} as a port that uses the HTTPS protocol:

        ``` {.language-plaintext tabindex="-1"}
        acl SSL_ports port 443
        ```

    e.  Update the list of `acl Safe_ports`{.literal} rules to configure to which ports Squid can establish a connection:

        ``` {.language-plaintext tabindex="-1"}
        acl Safe_ports port 21
        acl Safe_ports port 80
        acl Safe_ports port 443
        ```

        Configure the clients to only access resources on ports `21`{.literal} (FTP), `80`{.literal} (HTTP), and `443`{.literal} (HTTPS) over the proxy. Add the `acl Safe_ports`{.literal} statements to the configuration file. By default, the configuration file includes the `http_access deny !Safe_ports`{.literal} rule. This rule defines access denial to ports that are not defined in the `Safe_ports`{.literal} ACL.

    f.  Configure the cache type, the path to the cache directory, the cache size, and further cache type-specific settings in the `cache_dir`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        cache_dir ufs /var/spool/squid 10000 16 256
        ```

        With these settings:

        -   Squid uses the `ufs`{.literal} cache type.

        -   Squid stores its cache in the `/var/spool/squid/`{.literal} directory.

        -   The cache grows up to `10000`{.literal} MB.

        -   Squid creates `16`{.literal} level-1 sub-directories in the `/var/spool/squid/`{.literal} directory.

        -   Squid creates `256`{.literal} sub-directories in each level-1 directory.

            If you do not set a `cache_dir`{.literal} directive, Squid stores the cache in memory.

2.  If you set a different cache directory than `/var/spool/squid/`{.literal} in the `cache_dir`{.literal} parameter:

    a.  Create the cache directory:

        ``` {.language-plaintext tabindex="-1"}
        # mkdir -p path_to_cache_directory
        ```

    b.  Configure the permissions for the cache directory:

        ``` {.language-plaintext tabindex="-1"}
        # chown squid:squid path_to_cache_directory
        ```

    c.  If you run Security-Enhanced Linux (SELinux) in `enforcing`{.literal} mode, set the `squid_cache_t`{.literal} context for the cache directory:

        ``` {.language-plaintext tabindex="-1"}
        # semanage fcontext -a -t squid_cache_t "path_to_cache_directory(/.*)?"
        # restorecon -Rv path_to_cache_directory
        ```

        If the `semanage`{.literal} utility is not available on your system, install the `policycoreutils-python-utils`{.literal} package.

3.  Store the password of the LDAP service user in the `/etc/squid/ldap_password`{.literal} file, and set appropriate permissions for the file:

    ``` {.language-plaintext tabindex="-1"}
    # echo "password" > /etc/squid/ldap_password
    # chown root:squid /etc/squid/ldap_password
    # chmod 640 /etc/squid/ldap_password
    ```

4.  Open the `3128`{.literal} port in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=3128/tcp
    # firewall-cmd --reload
    ```

5.  Enable and start the `squid`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now squid
    ```

**Verification**

-   To verify that the proxy works correctly, download a web page:

    ``` {.language-plaintext tabindex="-1"}
    # curl -O -L "https://www.redhat.com/index.html" -x "user_name:password@proxy.example.com:3128"
    ```

    If curl does not display any error and the `index.html`{.literal} file was downloaded to the current directory, the proxy works.

**Troubleshooting**

1.  To verify that the helper utility works correctly:

    a.  Manually start the helper utility with the same settings you used in the `auth_param`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        # /usr/lib64/squid/basic_ldap_auth -b "cn=users,cn=accounts,dc=example,dc=com" -D "uid=proxy_user,cn=users,cn=accounts,dc=example,dc=com" -W /etc/squid/ldap_password -f "(&(objectClass=person)(uid=%s))" -ZZ -H ldap://ldap_server.example.com:389
        ```

    b.  Enter a valid user name and password, and press `Enter`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        user_name password
        ```

        If the helper utility returns `OK`{.literal}, authentication succeeded.

### [3.3. Configuring Squid as a caching proxy with Kerberos authentication](#setting-up-squid-as-a-caching-proxy-with-kerberos-authentication) {#configuring-squid-as-a-caching-proxy-with-kerberos-authentication .title}

To authenticate users to an Active Directory (AD) by using Kerberos, configure Squid as a caching proxy. Only authenticated users can use the proxy.

**Prerequisites**

-   The `squid`{.literal} package includes the `/etc/squid/squid.conf`{.literal} file. If you edited this file before, remove and reinstall the package.
-   The server on which you want to install Squid is a member of the AD domain.

**Procedure**

1.  Install the packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install squid krb5-workstation
    ```

2.  Authenticate as the AD domain administrator:

    ``` {.language-plaintext tabindex="-1"}
    # kinit administrator@AD.EXAMPLE.COM
    ```

3.  Create a keytab for Squid, store it in the `/etc/squid/HTTP.keytab`{.literal} file, and add the `HTTP`{.literal} service principal to the keytab:

    ``` {.language-plaintext tabindex="-1"}
    # export KRB5_KTNAME=FILE:/etc/squid/HTTP.keytab
    ```

    ``` {.language-plaintext tabindex="-1"}
    # net ads keytab CREATE -U administrator
    ```

    ``` {.language-plaintext tabindex="-1"}
    # net ads keytab ADD HTTP -U administrator
    ```

4.  Optional: If system is initially joined to the AD domain with realm (through `adcli`{.literal}), add `HTTP`{.literal} principal and create a keytab file for Squid:

    a.  Add the `HTTP`{.literal} service principal to the default keytab file `/etc/krb5.keytab`{.literal} and verify:

        ``` {.language-plaintext tabindex="-1"}
        # adcli update -vvv --domain=ad.example.com --computer-name=PROXY --add-service-principal="HTTP/proxy.ad.example.com" -C
        ```

        ``` {.language-plaintext tabindex="-1"}
        # klist -kte /etc/krb5.keytab | grep -i HTTP
        ```

    b.  Load the `/etc/krb5.keytab`{.literal} file, remove all service principals except `HTTP`{.literal}, and save the remaining principals into the `/etc/squid/HTTP.keytab`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # ktutil
        ```

        ``` {.language-plaintext tabindex="-1"}
        ktutil:  rkt /etc/krb5.keytab
        ktutil:  l -e
        slot | KVNO | Principal
        -----------------------------------------------------------------------------
        1 |    2 |            PROXY$@AD.EXAMPLE.COM (aes128-cts-hmac-sha1-96)
        2 |    2 |            PROXY$@AD.EXAMPLE.COM (aes256-cts-hmac-sha1-96)
        3 |    2 |         host/PROXY@AD.EXAMPLE.COM (aes128-cts-hmac-sha1-96)
        4 |    2 |         host/PROXY@AD.EXAMPLE.COM (aes256-cts-hmac-sha1-96)
        5 |    2 | host/proxy.ad.example.com@AD.EXAMPLE.COM (aes128-cts-hmac-sha1-96)
        6 |    2 | host/proxy.ad.example.com@AD.EXAMPLE.COM (aes256-cts-hmac-sha1-96)
        7 |    2 | HTTP/proxy.ad.example.com@AD.EXAMPLE.COM (aes128-cts-hmac-sha1-96)
        8 |    2 | HTTP/proxy.ad.example.com@AD.EXAMPLE.COM (aes256-cts-hmac-sha1-96)
        ```

        In the interactive terminal of `ktutil`{.literal}, you can use the different options, until you remove all unwanted principals from the keytab, for example:

        ``` {.language-plaintext tabindex="-1"}
        ktutil:  delent 1
        ```

        ``` {.language-plaintext tabindex="-1"}
        ktutil:  l -e
        ```

        ``` {.language-plaintext tabindex="-1"}
        slot | KVNO | Principal
        ----------------------------------------------------------------------------
        1 |   2 | HTTP/proxy.ad.example.com@AD.EXAMPLE.COM (aes128-cts-hmac-sha1-96)
        2 |   2 | HTTP/proxy.ad.example.com@AD.EXAMPLE.COM (aes256-cts-hmac-sha1-96)

        ktutil:  wkt /etc/squid/HTTP.keytab
        ktutil:  q
        ```

        Warning

        If System Security Services Daemon (SSSD) or Samba/winbind update the machine account password, the keys in `/etc/krb5.keytab`{.literal} might get updated. After the update, the key in `/etc/squid/HTTP.keytab`{.literal} stops working. You must repeat the `ktutil`{.literal} steps to copy the new keys into the keytab.

5.  Set the owner of the keytab file to the `squid`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # chown squid /etc/squid/HTTP.keytab
    ```

6.  Optional: Verify that the keytab file has the `HTTP`{.literal} service principal for the fully-qualified domain name (FQDN) of the proxy server:

    ``` {.language-plaintext tabindex="-1"}
    # klist -k /etc/squid/HTTP.keytab
    Keytab name: FILE:/etc/squid/HTTP.keytab
    KVNO   Principal
    ----   -------------------
    ...
       2 HTTP/proxy.ad.example.com@AD.EXAMPLE.COM
    ...
    ```

7.  Edit the `/etc/squid/squid.conf`{.literal} file:

    a.  To configure the `negotiate_kerberos_auth`{.literal} helper utility, add the following configuration entry to the top of `/etc/squid/squid.conf`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        auth_param negotiate program /usr/lib64/squid/negotiate_kerberos_auth -k /etc/squid/HTTP.keytab -s HTTP/proxy.ad.example.com@AD.EXAMPLE.COM
        ```

        The following describes the parameters passed to the `negotiate_kerberos_auth`{.literal} helper utility:

        -   `-k `{.literal}*`file`{.literal}* sets the path to the key tab file. Note that the squid user must have read permissions on this file.

        -   `-s HTTP/`{.literal}*`host_name`{.literal}*`@`{.literal}*`kerberos_realm`{.literal}* sets the Kerberos principal that Squid uses.

            Optionally, you can enable logging by passing one or both of the following parameters to the helper utility:

        -   `-i`{.literal} logs informational messages, such as the authenticating user.

        -   `-d`{.literal} enables debug logging.

            Squid logs the debugging information from the helper utility to the `/var/log/squid/cache.log`{.literal} file.

    b.  Add the following Access Control List (ACL) and rule to configure that Squid allows only authenticated users to use the proxy:

        ``` {.language-plaintext tabindex="-1"}
        acl kerb-auth proxy_auth REQUIRED
        http_access allow kerb-auth
        ```

        Important

        Specify these settings before the `http_access deny all`{.literal} rule.

    c.  Remove the following rule to disable bypassing the proxy authentication from IP ranges specified in `localnet`{.literal} ACL:

        ``` {.language-plaintext tabindex="-1"}
        http_access allow localnet
        ```

    d.  If users should be able to use the HTTPS protocol also on other ports, add an ACL for each of these port:

        ``` {.language-plaintext tabindex="-1"}
        acl SSL_ports port port_number
        ```

        For example, the following ACL exists in the default configuration and defines `443`{.literal} as a port that uses the HTTPS protocol:

        ``` {.language-plaintext tabindex="-1"}
        acl SSL_ports port 443
        ```

    e.  Update the list of `acl Safe_ports`{.literal} rules to configure to which ports Squid can establish a connection:

        ``` {.language-plaintext tabindex="-1"}
        acl Safe_ports port 21
        acl Safe_ports port 80
        acl Safe_ports port 443
        ```

        Configure the clients to only access resources on ports `21`{.literal} (FTP), `80`{.literal} (HTTP), and `443`{.literal} (HTTPS) over the proxy. Add the `acl Safe_ports`{.literal} statements to the configuration file. By default, the configuration file includes the `http_access deny !Safe_ports`{.literal} rule. This rule defines access denial to ports that are not defined in the `Safe_ports`{.literal} ACL.

    f.  Configure the cache type, the path to the cache directory, the cache size, and further cache type-specific settings in the `cache_dir`{.literal} parameter:

        ``` {.language-plaintext tabindex="-1"}
        cache_dir ufs /var/spool/squid 10000 16 256
        ```

        With these settings:

        -   Squid uses the `ufs`{.literal} cache type.

        -   Squid stores its cache in the `/var/spool/squid/`{.literal} directory.

        -   The cache grows up to `10000`{.literal} MB.

        -   Squid creates `16`{.literal} level-1 sub-directories in the `/var/spool/squid/`{.literal} directory.

        -   Squid creates `256`{.literal} sub-directories in each level-1 directory.

            If you do not set a `cache_dir`{.literal} directive, Squid stores the cache in memory.

8.  If you set a different cache directory than `/var/spool/squid/`{.literal} in the `cache_dir`{.literal} parameter:

    a.  Create the cache directory:

        ``` {.language-plaintext tabindex="-1"}
        # mkdir -p path_to_cache_directory
        ```

    b.  Configure the permissions for the cache directory:

        ``` {.language-plaintext tabindex="-1"}
        # chown squid:squid path_to_cache_directory
        ```

    c.  If you run Security-Enhanced Linux (SELinux) in `enforcing`{.literal} mode, set the `squid_cache_t`{.literal} context for the cache directory:

        ``` {.language-plaintext tabindex="-1"}
        # semanage fcontext -a -t squid_cache_t "path_to_cache_directory(/.*)?"
        ```

        ``` {.language-plaintext tabindex="-1"}
        # restorecon -Rv path_to_cache_directory
        ```

        If the `semanage`{.literal} utility is not available on your system, install the `policycoreutils-python-utils`{.literal} package.

9.  Open the `3128`{.literal} port in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=3128/tcp
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

10. Enable and start the `squid`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now squid
    ```

**Verification**

-   To verify that the proxy works correctly, download a web page using the `curl`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # curl -O -L "https://www.redhat.com/index.html" --proxy-negotiate -u : -x "proxy.ad.example.com:3128"
    ```

    If `curl`{.literal} does not display any error and the `index.html`{.literal} file exists in the current directory, the proxy works.

**Troubleshooting steps**

1.  Obtain a Kerberos ticket for the AD account:

    ``` {.language-plaintext tabindex="-1"}
    # kinit user@AD.EXAMPLE.COM
    ```

2.  Optional: Display the ticket:

    ``` {.language-plaintext tabindex="-1"}
    # klist
    ```

3.  Use the `negotiate_kerberos_auth_test`{.literal} utility to test the authentication:

    ``` {.language-plaintext tabindex="-1"}
    # /usr/lib64/squid/negotiate_kerberos_auth_test proxy.ad.example.com
    ```

    If the helper utility returns a token, the authentication succeeded:

    ``` {.language-plaintext tabindex="-1"}
    Token: YIIFtAYGKwYBBQUCoIIFqDC...
    ```

### [3.4. Configuring a domain deny list in Squid](#configuring-a-domain-deny-list-in-squid) {#configuring-a-domain-deny-list-in-squid .title}

To block access to specific domains, configure a domain deny list in Squid. It is useful to block domains that are either malicious or spam.

**Prerequisites**

-   You have configured Squid as a caching proxy, and users can use the proxy.

**Procedure**

1.  Edit following settings in the `/etc/squid/squid.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    acl domain_deny_list dstdomain "/etc/squid/domain_deny_list.txt"
    http_access deny all domain_deny_list
    ```

    Important

    Add these entries before the first `http_access allow`{.literal} statement that allows access to users or clients.

2.  Create the `/etc/squid/domain_deny_list.txt`{.literal} file and add the domains you want to block. For example, to block access to `example.com`{.literal} including subdomains and to block `example.net`{.literal} only, add:

    ``` {.language-plaintext tabindex="-1"}
    .example.com
    example.net
    ```

    Important

    If you referred to the `/etc/squid/domain_deny_list.txt`{.literal} file in the squid configuration, this file must not be empty. If the file is empty, Squid fails to start.

3.  Restart the `squid`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart squid
    ```

### [3.5. Configuring the Squid service to listen on a specific port or IP address](#configuring-the-squid-service-to-listen-on-a-specific-port-or-ip-address) {#configuring-the-squid-service-to-listen-on-a-specific-port-or-ip-address .title}

To configure the Squid service to listen on a specific port or IP address, edit the `/etc/squid/squid.conf`{.literal} file. By default, the Squid proxy service listens on the `3128`{.literal} port on all network interfaces.

**Prerequisites**

-   You have installed the `squid`{.literal} package.

**Procedure**

1.  Edit the `/etc/squid/squid.conf`{.literal} file:

    -   To set the port on which the Squid service listens, set the port number in the `http_port`{.literal} parameter. For example, to set the port to `8080`{.literal}, enter:

        ``` {.language-plaintext tabindex="-1"}
        http_port 8080
        ```

    -   To configure on which IP address the Squid service listens, set the IP address and port number in the `http_port`{.literal} parameter. For example, to configure that Squid listens only on the `192.0.2.1`{.literal} IP address on port `3128`{.literal}, enter:

        ``` {.language-plaintext tabindex="-1"}
        http_port 192.0.2.1:3128
        ```

    -   Add multiple `http_port`{.literal} parameters to the configuration file to configure that Squid listens on multiple ports and IP addresses:

        ``` {.language-plaintext tabindex="-1"}
        http_port 192.0.2.1:3128
        ```

        ``` {.language-plaintext tabindex="-1"}
        http_port 192.0.2.1:8080
        ```

2.  If you configured that Squid uses a different port than the default `3128`{.literal}:

    a.  Open the port in the firewall:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --permanent --add-port=port_number/tcp
        ```

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --reload
        ```

    b.  Install the `policycoreutils-python-utils`{.literal} package to use the `semanage`{.literal} utility:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install policycoreutils-python-utils
        ```

    c.  If you run Security-Enhanced Linux (SELinux) in enforcing mode, assign the port to the `squid_port_t`{.literal} port type definition:

        ``` {.language-plaintext tabindex="-1"}
        # semanage port -a -t squid_port_t -p tcp <port_number>
        ```

3.  Restart the `squid`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart squid
    ```

## [Legal Notice](#idm139883211375200) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
