---
{"title": "Configuring and using a CUPS printing server", "guide": "configuring_and_using_a_cups_printing_server", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_using_a_cups_printing_server/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Configuring and using a CUPS printing server {#configuring-and-using-a-cups-printing-server .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Configure your system to operate as a CUPS server and manage printers, print queues and your printing environment {#configure-your-system-to-operate-as-a-cups-server-and-manage-printers-print-queues-and-your-printing-environment .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140480843827696)

**Abstract**

The Common Unix Printing System (CUPS) manages printing on {ProductName}. Users configure printers in CUPS on their host to print. Additionally, you can share printers in CUPS to use the host as a print server.

CUPS supports printing to:

-   AirPrint™ and IPP Everywhere™ printers

-   Network and local USB printers with printer applications

-   Network and local USB printers with legacy PostScript Printer Description (PPD)-based drivers

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

## [Chapter 1. Installing and configuring CUPS](#installing-and-configuring-cups) {#chapter-1.-installing-and-configuring-cups .title}

You can use CUPS to print from a local host. You can also use this host to share printers in the network and act as a print server.

**Procedure**

1.  Install the `cups`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install cups
    ```

2.  If you configure CUPS as a print server, edit the `/etc/cups/cupsd.conf`{.literal} file, and make the following changes:

    a.  If you want to remotely configure CUPS or use this host as a print server, configure on which IP addresses and ports the service listens:

        ``` {.language-bash tabindex="-1"}
        Listen 192.0.2.1:631
        Listen [2001:db8:1::1]:631
        ```

        By default, CUPS listens only on `localhost`{.literal} interfaces (`127.0.0.1`{.literal} and `::1`{.literal}). Specify IPv6 addresses in square brackets.

        Important

        Do not configure CUPS to listen on interfaces that allow access from untrustworthy networks, such as the internet.

    b.  Configure which IP ranges can access the service by allowing the IP ranges in the `<Location />`{.literal} directive:

        ``` {.language-bash tabindex="-1"}
        <Location />
          Allow from 192.0.2.0/24
          Allow from [2001:db8:1::1]/32
          Order allow,deny
        </Location>
        ```

    c.  In the `<Location /admin>`{.literal} directive, configure which IP addresses and ranges can access the CUPS administration services:

        ``` {.language-bash tabindex="-1"}
        <Location /admin>
          Allow from 192.0.2.15/32
          Allow from [2001:db8:1::22]/128
          Order allow,deny
        </Location>
        ```

        With these settings, only the hosts with the IP addresses `192.0.2.15`{.literal} and `2001:db8:1::22`{.literal} can access the administration services.

    d.  Optional: Configure IP addresses and ranges allowed to access the configuration and log files in the web interface:

        ``` {.language-bash tabindex="-1"}
        <Location /admin/conf>
          Allow from 192.0.2.15/32
          Allow from [2001:db8:1::22]/128
          ...
        </Location>

        <Location /admin/log>
          Allow from 192.0.2.15/32
          Allow from [2001:db8:1::22]/128
          ...
        </Location>
        ```

3.  If you run the `firewalld`{.literal} service and want to configure remote access to CUPS, open the CUPS port in `firewalld`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=631/tcp
    # firewall-cmd --reload
    ```

    If you run CUPS on a host with multiple interfaces, consider limiting the access to the required networks.

4.  Enable and start the `cups`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now cups
    ```

**Verification**

-   Use a browser, and access `http://`{.literal}*`<hostname>`{.literal}*`:631`{.literal}. If you can connect to the web interface, CUPS works.

    Note that certain features, such as the `Administration`{.literal} tab, require authentication and an HTTPS connection. By default, CUPS uses a self-signed certificate for HTTPS access and, consequently, the connection is not secure when you authenticate.

## [Chapter 2. Configuring TLS encryption on a CUPS server](#configuring-tls-encryption-on-a-cups-server) {#chapter-2.-configuring-tls-encryption-on-a-cups-server .title}

CUPS supports TLS-encrypted connections and, by default, the service enforces encrypted connections for all requests that require authentication. TLS-encrypted connections ensure safe communication with the CUPS server.

If the user does not configure certificates, CUPS creates a private key and a self-signed certificate. This is only sufficient if you access CUPS from the local host itself. For a secure connection over the network, use a server certificate signed by a certificate authority (CA).

Warning

Without encryption or with a self-signed certificates, a man-in-the-middle (MITM) attack can disclose sensitive data, for example:

-   Credentials of administrators when configuring CUPS by using the web interface
-   Confidential data when sending print jobs over the network

**Prerequisites**

-   [CUPS is configured](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").

-   [You created a private key](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/creating-and-managing-tls-keys-and-certificates), and a CA issued a server certificate for it.

-   If an intermediate certificate is required to validate the server certificate, append the intermediate certificate to the server certificate.

-   The private key is not protected by a password because CUPS provides no option to enter the password when the service reads the key.

-   The Canonical Name (`CN`{.literal}) or Subject Alternative Name (SAN) field in the certificate matches one of the following:

    -   The fully-qualified domain name (FQDN) of the CUPS server
    -   An alias that the DNS resolves to the server's IP address

-   The private key and server certificate files use the Privacy Enhanced Mail (PEM) format.

-   Clients trust the CA certificate.

-   If the FIPS mode is enabled, clients must either support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Edit the `/etc/cups/cups-files.conf`{.literal} file, and add the following setting to disable the automatic creation of self-signed certificates:

    ``` {.language-plaintext tabindex="-1"}
    CreateSelfSignedCerts no
    ```

2.  Remove the self-signed certificate and private key:

    ``` {.language-plaintext tabindex="-1"}
    # rm /etc/cups/ssl/<hostname>.crt /etc/cups/ssl/<hostname>.key
    ```

3.  Optional: Display the FQDN of the server:

    ``` {.language-plaintext tabindex="-1"}
    # hostname -f
    ```

    ``` {.language-plaintext tabindex="-1"}
    server.example.com
    ```

4.  Store the private key and server certificate in the `/etc/cups/ssl/`{.literal} directory, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mv /root/server.key /etc/cups/ssl/server.example.com.key
    # mv /root/server.crt /etc/cups/ssl/server.example.com.crt
    ```

    Important

    CUPS requires that you name the private key *`<fqdn>`{.literal}*`.key`{.literal} and the server certificate file *`<fqdn>`{.literal}*`.crt`{.literal}. If you use an alias, you must name the files *`<alias>`{.literal}*`.key`{.literal} and *`<alias>.crt`{.literal}*.

5.  Set secure permissions on the private key that enable only the `root`{.literal} user to read this file:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:root /etc/cups/ssl/server.example.com.key
    # chmod 600 /etc/cups/ssl/server.example.com.key
    ```

    Because certificates are part of the communication between a client and the server before they establish a secure connection, any client can retrieve the certificates without authentication. Therefore, you do not need to set strict permissions on the server certificate file.

6.  Restore the SELinux context:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /etc/cups/ssl/
    ```

7.  Optional: Display the `CN`{.literal} and SAN fields of the certificate:

    ``` {.language-plaintext tabindex="-1"}
    # openssl x509 -text -in /etc/cups/ssl/server.example.com.crt
    ```

    ``` {.language-plaintext tabindex="-1"}
    Certificate:
      Data:
        ...
        Subject: CN = server.example.com
        ...
        X509v3 extensions:
          ...
          X509v3 Subject Alternative Name:
            DNS:server.example.com
      ...
    ```

8.  If the `CN`{.literal} or SAN fields in the server certificate contains an alias that is different from the server's FQDN, add the `ServerAlias`{.literal} parameter to the `/etc/cups/cupsd.conf`{.literal} file:

    ``` {.language-bash tabindex="-1"}
    ServerAlias alternative_name.example.com
    ```

    In this case, use the alternative name instead of the FQDN in the rest of the procedure.

9.  By default, CUPS enforces encrypted connections only if a task requires authentication, for example when performing administrative tasks on the `/admin`{.literal} page in the web interface.

    To enforce encryption for the entire CUPS server, add `Encryption Required`{.literal} to all `<Location>`{.literal} directives in the `/etc/cups/cupsd.conf`{.literal} file, for example:

    ``` {.language-bash tabindex="-1"}
    <Location />
      ...
      Encryption Required
    </Location>
    ```

10. Restart CUPS:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart cups
    ```

**Verification**

1.  Use a browser, and access `https://`{.literal}*`<hostname>`{.literal}*`:631/admin/`{.literal}. This requires that your browser trusts the CA certificate. If the connection succeeds, you configured TLS encryption in CUPS correctly.
2.  If you configured that encryption is required for the entire server, access `http://`{.literal}*`<hostname>`{.literal}*`:631/`{.literal}. CUPS returns an `Upgrade Required`{.literal} error in this case.

**Troubleshooting**

-   Display the `systemd`{.literal} journal entries of the `cups`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u cups
    ```

    If the journal contains an `Unable to encrypt connection: Error while reading file`{.literal} error after a failed connection to the web interface by using HTTPS, verify the private key. Also, verify the name of the server certificate file.

**Additional resources**

-   [How to configure CUPS to use a CA-signed TLS certificate in RHEL (Red Hat Knowledgebase)](https://access.redhat.com/solutions/5097251)

## [Chapter 3. Granting administration permissions to manage a CUPS server in the web interface](#granting-administration-permissions-to-manage-a-cups-server-in-the-web-interface) {#chapter-3.-granting-administration-permissions-to-manage-a-cups-server-in-the-web-interface .title}

To avoid CUPS administrators gaining unexpected permissions in other services, use a dedicated group for CUPS administrators.

By default, the CUPS web interface allows members of the `sys`{.literal}, `root`{.literal}, and `wheel`{.literal} groups to perform administration tasks. However, certain other services use these groups as well. For example, members of the `wheel`{.literal} groups can, by default, run commands with `root`{.literal} permissions by using `sudo`{.literal}. Using a separate group for CUPS administrators ensures that these users have only access to the CUPS interface.

**Prerequisites**

-   [CUPS is configured](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").
-   The IP address of the client you want to use has permissions to access the administration area in the web interface.

**Procedure**

1.  Create a group for CUPS administrators:

    ``` {.language-plaintext tabindex="-1"}
    # groupadd cups-admins
    ```

2.  Add the users who should manage the service in the web interface to the `cups-admins`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    # usermod -a -G cups-admins <username>
    ```

3.  Update the value of the `SystemGroup`{.literal} parameter in the `/etc/cups/cups-files.conf`{.literal} file, and append the `cups-admin`{.literal} group:

    ``` {.language-bash tabindex="-1"}
    SystemGroup sys root wheel cups-admins
    ```

    If only the `cups-admin`{.literal} group should have administrative access, remove the other group names from the parameter.

4.  Restart CUPS:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart cups
    ```

**Verification**

1.  Use a browser, and access `https://`{.literal}*`<hostname_or_ip_address>`{.literal}*`:631/admin/`{.literal}.

    Note

    You can access the administration area in the web UI only if you use the HTTPS protocol.

2.  Start performing an administrative task. For example, click `Add printer`{.literal}.

3.  The web interface prompts for a username and password. To proceed, authenticate by using credentials of a user who is a member of the `cups-admins`{.literal} group.

    If authentication succeeds, this user can perform administrative tasks.

## [Chapter 4. Packages with printer drivers](#packages-with-printer-drivers) {#chapter-4.-packages-with-printer-drivers .title}

Red Hat Enterprise Linux (RHEL) provides different packages with printer drivers for CUPS. After installing the required package, you can display the list of drivers in the CUPS web interface or by using the `lpinfo -m`{.literal} command.

The following is a general overview of these packages and for which vendors they contain drivers:

+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Package name                | Drivers for printers                                                                                                                   |
+:============================+:=======================================================================================================================================+
| `cups`{.literal}            | Zebra, Dymo                                                                                                                            |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| `c2esp`{.literal}           | Kodak                                                                                                                                  |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| `foomatic`{.literal}        | Brother, Canon, Epson, Gestetner, HP, Infotec, Kyocera, Lanier, Lexmark, NRG, Ricoh, Samsung, Savin, Sharp, Toshiba, Xerox, and others |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| `gutenprint-cups`{.literal} | Brother, Canon, Epson, Fujitsu, HP, Infotec, Kyocera, Lanier, NRG, Oki, Minolta, Ricoh, Samsung, Savin, Xerox, and others              |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| `hplip`{.literal}           | HP                                                                                                                                     |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| `pnm2ppa`{.literal}         | HP                                                                                                                                     |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| `splix`{.literal}           | Samsung, Xerox, and others                                                                                                             |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.1. Driver package list

Show more

Note that some packages can contain drivers for the same printer vendor or model but with different functionality.

## [Chapter 5. Determining whether a printer supports driverless printing](#determining-whether-a-printer-supports-driverless-printing) {#chapter-5.-determining-whether-a-printer-supports-driverless-printing .title}

CUPS supports driverless printing, which means that you can print without providing any hardware-specific software for the printer model.

To support driverless printing, the printer must inform the client about its capabilities and use one of the following standards:

-   AirPrint™
-   IPP Everywhere™
-   Mopria®
-   Wi-Fi Direct Print Services

You can use the `ipptool`{.literal} utility to discover whether a printer supports driverless printing.

**Prerequisites**

-   The printer or remote print server supports the Internet Printing Protocol (IPP).
-   The host can connect to the IPP port of the printer or remote print server. The default IPP port is 631.

**Procedure**

-   Query the `ipp-versions-supported`{.literal} and `document-format-supported`{.literal} attributes, and ensure that the `get-printer-attributes`{.literal} test passes:

    -   For a remote printer, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipptool -tv ipp://<ip_address_or_hostname>:631/ipp/print get-printer-attributes.test | grep -E "ipp-versions-supported|document-format-supported|get-printer-attributes"
        ```

        ``` {.language-plaintext tabindex="-1"}
        Get printer attributes using get-printer-attributes      [PASS]
            ipp-versions-supported (1setOf keyword) = ...
            document-format-supported (1setOf mimeMediaType) = ...
        ```

    -   For a queue on a remote print server, enter:

        ``` {.language-plaintext tabindex="-1"}
        # ipptool -tv ipp://<ip_address_or_hostname>:631/printers/<queue_name> get-printer-attributes.test | grep -E "ipp-versions-supported|document-format-supported|get-printer-attributes"
        ```

        ``` {.language-plaintext tabindex="-1"}
        Get printer attributes using get-printer-attributes      [PASS]
            ipp-versions-supported (1setOf keyword) = ...
            document-format-supported (1setOf mimeMediaType) = ...
        ```

    To ensure that driverless printing works, verify in the output:

    -   The `get-printer-attributes`{.literal} test returns `PASS`{.literal}.

    -   The IPP version that the printer supports is 2.0 or higher.

    -   The list of formats contains one of the following:

        -   `application/pdf`{.literal}
        -   `image/urf`{.literal}
        -   `image/pwg-raster`{.literal}

    -   For color printers, the output contains one of the mentioned formats and, additionally, `image/jpeg`{.literal}.

## [Chapter 6. Driverless USB printing](#driverless-usb-printing-and-scanning) {#chapter-6.-driverless-usb-printing .title}

Driverless printing has variants for USB-connected devices, covered by the IPP over USB standard. Install the `ipp-usb`{.literal} package for it to work. This package registers the device with Avahi on the local host and makes the USB device look like a network device.

### [6.1. Installing and checking printer capabilities](#installing-and-checking-printer-capabilities) {#installing-and-checking-printer-capabilities .title}

To install a device for driverless printing, identify the device on your network and use a print server to configure a print queue.

After configuring the print queue, you can verify the printer capabilities by accessing its settings within the print queue or by using the `ipptool`{.literal} utility. For detailed steps on verifying driverless printing support, see [Determining whether a printer supports driverless printing](#determining-whether-a-printer-supports-driverless-printing "Chapter 5. Determining whether a printer supports driverless printing").

**Prerequisites**

-   You updated the device firmware.
-   You stopped and disabled the `cups-browsed`{.literal} service if it is not used for installing printers from remote print servers. Note that in this case, the `BrowsePoll`{.literal} server is used in the `/etc/cups/cups-browsed.conf`{.literal} file.

**Procedure**

1.  Install the `ipp-usb`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install ipp-usb
    ```

    Note

    The `ipp-usb`{.literal} package is installed by default with CUPS.

2.  Check if device has printing functionality:

    a.  Verify that the device is recognized by `ipp-usb`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # sudo ipp-usb check
        ```

    b.  Check if the device is identified by CUPS among existing destinations. The service name created by `ipp-usb`{.literal} has the suffix `_USB`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        $ lpstat -e
        ```

        ``` {.language-plaintext tabindex="-1"}
        Canon_MF440_Series_USB
        ```

        The service name created by `ipp-usb`{.literal} has the `_USB`{.literal} suffix. For example, here `Canon_MF440_Series_USB`{.literal} represents IPP-over-USB device called Canon I-Sensys MF433.

        Important

        If the Canon_MF440_Series_USB is displayed in the output of the `lpstat -e`{.literal} command, but not in your application, report the issue to the application.

    c.  Check device capabilities:

        ``` {.language-plaintext tabindex="-1"}
        # ipptool -tv ipp://localhost:60000/ipp/print get-printer-attributes.test
        # lpoptions -p Canon_MF440_Series_USB -l
        ```

        The `ipptool`{.literal} command returns all IPP attributes which the device supports. If your printing option is in IPP response, but not in `lpoptions`{.literal}, then it is a CUPS issue because the common PPD options are generated from some of the attributes. The `lpoptions`{.literal} utility returns available PPD options.

### [6.2. Migrating existing classic print queues](#migrating-existing-classic-print-queues) {#migrating-existing-classic-print-queues .title}

The `ipp-usb`{.literal} package is incompatible with classic printing drivers for `IPP-over-USB`{.literal} devices. Therefore, you must decide which method you want to use: driverless or classic drivers.

**Procedure**

-   Use one of the following options:

    -   Use driverless to support the USB device.

        To migrate the existing configuration with classic drivers to driverless support for a USB device, remove any existing printers installed for the device in the past.

        i.  To search for printer name, run:

            ``` {.language-plaintext tabindex="-1"}
            # lpstat -a
            ```

        ii. Remove the printer:

            ``` {.language-plaintext tabindex="-1"}
            # lpadmin -x <printer_name>
            ```

    -   Use a classic driver to support the device.

        Choosing a classic driver requires rejecting the printer model in the `ipp-usb`{.literal} configuration.

        i.  Search for device model name:

            ``` {.language-plaintext tabindex="-1"}
            # sudo ipp-usb check
            ```

            ``` {.language-plaintext tabindex="-1"}
            Configuration files: OK
            IPP over USB devices:
             Num  Device              Vndr:Prod  Model
               1. Bus 001 Device 005  04a9:2823  "Canon MF440 Series"
            ```

        ii. Create a quirk for `ipp-usb`{.literal} and use the name in the new quirk file in the `/etc/ipp-usb/quirks`{.literal} directory. Note that the `.conf`{.literal} suffix is required.

            ``` {.language-plaintext tabindex="-1"}
            # cat /etc/ipp-usb/quirks/canon.conf
            ```

            ``` {.language-plaintext tabindex="-1"}
            [Canon MF440 Series]
            blacklist = true
            ```

        iii. Restart the `ipp-usb`{.literal} service:

             ``` {.language-plaintext tabindex="-1"}
             # systemctl restart ipp-usb
             ```

             This quirk denies device's support in `ipp-usb`{.literal}, and classic drivers will work. The printer generated by `ipp-usb`{.literal} is removed from the list of existing printers.

             Note

             You can opt-out from driverless USB support by removing the `ipp-usb`{.literal} package and excluding it from DNF operations.

## [Chapter 7. Setting up a legacy printer](#setting-up-a-legacy-printer) {#chapter-7.-setting-up-a-legacy-printer .title}

Legacy printers are printers that do not support driverless printing standards, such as IPP Everywhere or AirPrint, and still require traditional drivers to function. To use a legacy printer with CUPS, you must configure it through a printer application.

A printer application is a service that acts as an intermediary between a legacy printer and CUPS. It communicates with the printer by using its driver and presents the printer to CUPS as a driverless IPP network printer. RHEL includes the following Printer Application Framework (PAPPL)-based printer applications and their default TCP ports:

-   LPrint: 8000
-   Legacy Printer Application: 8001

To configure a legacy printer, follow this workflow:

1.  Install and start a PAPPL-based printer application.
2.  Add the legacy printer to the printer application.
3.  Add the printer from the printer application to CUPS as a permanent queue.

Important

Installing printers with classic drivers directly in CUPS is deprecated. Use a printer application instead.

### [7.1. Configuring a PAPPL-based printer application](#setting-up-pappl-based-printer-application) {#configuring-a-pappl-based-printer-application .title}

To easily and effectively support various printing requirements and prepare the host for installing legacy printers, you can configure a PAPPL-based printer application.

**Prerequisites**

-   You have `root`{.literal} permissions on the host.

**Procedure**

1.  Install a PAPPL-based printer application package, for example, `lprint`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install <printer_application_name>
    ```

2.  Optional: Enable the port `8000`{.literal} in firewalld to access the printer application web interface from a remote host:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=8000/tcp
    # firewall-cmd --reload
    ```

    Note

    You can check the port in the `/etc/lprint.conf`{.literal} configuration file.

3.  Enable and start the service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now <printer_application_name>
    ```

### [7.2. Installing a legacy printer in PAPPL-based printer application by using web interface](#installing-a-legacy-printer-in-pappl-based-printer-application-by-using-web-console) {#installing-a-legacy-printer-in-pappl-based-printer-application-by-using-web-interface .title}

Add legacy printers to a PAPPL-based application to bridge the gap between older hardware and modern driverless environments. This process converts legacy protocols into IPP services, ensuring non-driverless devices remain functional and discoverable on your network.

**Prerequisites**

-   The printer application is installed and running.

**Procedure**

1.  In your browser, navigate to the printer application web interface at `https://`{.literal}*`<hostname>`{.literal}*`:8000`{.literal}. On the home page, click `Add Printer`{.literal}.

2.  Choose `printer name`{.literal}, `device`{.literal}, `hostname/IP address`{.literal} in case of network printers, select the driver name from the offered list, and click `Add Printer`{.literal}. You can also use the auto-detect option to search for the driver.

    Using the auto-detection option for the driver might result in finding an incompatible driver for your device, if the device model is too different from available drivers. Check the assigned driver before printing and change the driver manually to prevent any printing issues.

**Verification**

-   To test the functionality, click `Print Test Page`{.literal}.

    The used driver is on the second line in the `block Status`{.literal}.

### [7.3. Installing a legacy printer in PAPPL-based printer application by using the command line interface](#installing-a-legacy-printer-in-pappl-based-printer-application-by-using-the-command-line-interface) {#installing-a-legacy-printer-in-pappl-based-printer-application-by-using-the-command-line-interface .title}

Add legacy printers to a PAPPL-based application to bridge the gap between older hardware and modern driverless environments. This process converts legacy protocols into IPP services, ensuring non-driverless devices remain functional and discoverable on your network.

**Prerequisites**

-   The printer application is installed and running.

**Procedure**

1.  Search the available drivers in PAPPL based printer application:

    ``` {.language-plaintext tabindex="-1"}
    # lprint drivers
    ```

    ``` {.language-plaintext tabindex="-1"}
    zpl_2inch-203dpi-dt "Zebra ZPL 2-inch/203dpi/Direct-Thermal
    ```

2.  Install the printer. For example, to install a network printer with a specified driver, enter:

    ``` {.language-plaintext tabindex="-1"}
    # lprint add -d <printer_name> -v socket://<hostname> -m zpl_2inch-203dpi-dt
    ```

**Verification**

-   Check that the printer appears in the list of printers:

    ``` {.language-plaintext tabindex="-1"}
    # lprint printers
    ```

    ``` {.language-plaintext tabindex="-1"}
    <printer_name> - printer - ipp://localhost/ipp/print/<printer_name>
    ```

### [7.4. Adding a printer from a printer application to CUPS as a permanent queue](#adding-a-printer-from-a-printer-application-to-cups-as-a-permanent-queue) {#adding-a-printer-from-a-printer-application-to-cups-as-a-permanent-queue .title}

After you install a legacy printer in a printer application, the application makes it available as an IPP network printer. You can then add this printer to CUPS as a permanent queue so that users can print to it.

**Prerequisites**

-   CUPS is configured with a TLS certificate.
-   You have permission in CUPS to manage printers.
-   The legacy printer is installed in a printer application.

**Procedure**

1.  Check if the printer from the printer application is available:

    ``` {.language-plaintext tabindex="-1"}
    # lpstat -e
    ```

    ``` {.language-plaintext tabindex="-1"}
    <printer_name_in_printer_application>
    ```

2.  Search for the port that the printer application is using:

    ``` {.language-plaintext tabindex="-1"}
    # grep 'server-port=' /etc/lprint.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    server-port=8000
    ```

3.  Install the permanent queue by using the port number `8000`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # lpadmin -p <printer_name_in_CUPS> -v ipps://localhost:8000/ipp/print/<printer_name_in_printer_application> -m everywhere -E
    ```

**Verification**

-   To check if CUPS queue is installed:

    ``` {.language-plaintext tabindex="-1"}
    # lpstat -a
    ```

    ``` {.language-plaintext tabindex="-1"}
    <printer_name_in_CUPS>  accepting requests since Wed 07 May 2025 02:31:04 AM EDT
    ```

## [Chapter 8. Adding a printer to CUPS by using the web interface](#adding-a-printer-to-cups-by-using-the-web-interface) {#chapter-8.-adding-a-printer-to-cups-by-using-the-web-interface .title}

Before users can print through CUPS, you must add printers. You can use both network printers and printers that are directly attached to the CUPS host, for example over USB.

You can add printers by using the CUPS driverless feature or by using a PostScript Printer Description (PPD) file.

Note

CUPS prefers driverless printing, and using drivers is deprecated.

Red Hat Enterprise Linux (RHEL) does not provide the name service switch multicast DNS plugin (`nss-mdns`{.literal}), which resolves requests by querying an mDNS responder. Consequently, automatic discovery and installation for local driverless printers by using mDNS is not available in RHEL. To work around this limitation, install single printers manually or use `cups-browsed`{.literal} to automatically install a high amount of print queues that are available on a remote print server.

**Prerequisites**

-   [CUPS is configured](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").
-   [You have permissions in CUPS to manage printers](#granting-administration-permissions-to-manage-a-cups-server-in-the-web-interface "Chapter 3. Granting administration permissions to manage a CUPS server in the web interface").
-   If you use CUPS as a print server, [you configured TLS encryption](#configuring-tls-encryption-on-a-cups-server "Chapter 2. Configuring TLS encryption on a CUPS server") to securely transmit data over the network.
-   [The printer supports driverless printing](#determining-whether-a-printer-supports-driverless-printing "Chapter 5. Determining whether a printer supports driverless printing"), if you want to use this feature.

**Procedure**

1.  Use a browser, and access `https://`{.literal}*`<hostname>`{.literal}*`:631/admin/`{.literal}.

    You must connect to the web interface by using the HTTPS protocol. Otherwise, CUPS prevents you from authenticating in a later step for security reasons.

2.  Click Add printer.

3.  If you are not already authenticated, CUPS prompts for credentials of an administrative user. Enter the username and password of an authorized user.

4.  If you decide to not use driverless printing and the system automatically detects the printer you want to add, select it, and click Continue.

5.  If the printer was not detected:

    a.  Select the protocol that the printer supports.

        If your printer supports driverless printing and you want to use this feature, select the `ipp`{.literal} or `ipps`{.literal} protocol.

    b.  Click Continue.

    c.  Enter the URL to the printer or to the queue on a remote print server.

    d.  Click Continue.

6.  Enter a name and, optionally, a description and location. If you use CUPS as a print server, and other clients should be able to print through CUPS on this printer, select also **Share this printer**.

7.  Select the printer manufacturer in the **Make** list. If the printer manufacturer is not on the list, select **Generic** or upload a PPD file for the printer.

8.  Click Continue.

9.  Select the printer model:

    -   If the printer supports driverless printing, select **IPP Everywhere**. Note that, if you previously installed printer-specific drivers locally, it is possible that the list also contains entries such as ***\<printer_name\>* - IPP Everywhere**.
    -   If the printer does not support driverless printing, select the model or upload the PPD file for the printer.

10. Click Add Printer

11. The settings and tabs on the **Set printer options** page depend on the driver and the features the printer supports. Use this page to set default options, such as for the paper size.

12. Click Set default options.

**Verification**

1.  Open the **Printers** tab in the web interface.
2.  Click the printer's name.
3.  In the **Maintenance** list, select **Print test page**.

**Troubleshooting**

-   If you use driverless printing, and printing does not work, use the `lpadmin`{.literal} utility to add the printer on the command line. For details, see [Adding a printer to CUPS by using the `lpadmin`{.literal} utility](#adding-a-printer-to-cups-by-using-the-lpadmin-utility "Chapter 9. Adding a printer to CUPS by using the lpadmin utility").

## [Chapter 9. Adding a printer to CUPS by using the lpadmin utility](#adding-a-printer-to-cups-by-using-the-lpadmin-utility) {#chapter-9.-adding-a-printer-to-cups-by-using-the-lpadmin-utility .title}

Before users can print through CUPS, you must add printers. You can use both network printers and printers that are directly attached to the CUPS host, for example over USB.

You can add printers by using the CUPS driverless feature or by using a PostScript Printer Description (PPD) file.

Note

CUPS prefers driverless printing, and using drivers is deprecated.

Red Hat Enterprise Linux (RHEL) does not provide the name service switch multicast DNS plugin (`nss-mdns`{.literal}), which resolves requests by querying an mDNS responder. Consequently, automatic discovery and installation for local driverless printers by using mDNS is not available in RHEL. To work around this limitation, install single printers manually or use `cups-browsed`{.literal} to automatically install a high amount of print queues that are available on a remote print server.

**Prerequisites**

-   [CUPS is configured](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").
-   [The printer supports driverless printing](#determining-whether-a-printer-supports-driverless-printing "Chapter 5. Determining whether a printer supports driverless printing"), if you want to use this feature.
-   The printer accepts data on port 631 (IPP), 9100 (socket), or 515 (LPD). The port depends on the method you use to connect to the printer.

**Procedure**

-   Add the printer to CUPS:

    -   To add a printer with driverless support, enter:

        ``` {.language-plaintext tabindex="-1"}
        # lpadmin -p Demo-printer -E -v ipp://192.0.2.200/ipp/print -m everywhere
        ```

        If the `-m everywhere`{.literal} option does not work for your printer, try `-m driverless:`{.literal}*`<uri>`{.literal}*, for example: `-m driverless:`{.literal}*`ipp://192.0.2.200/ipp/print`{.literal}*.

    -   To add a queue from a remote print server with driverless support, enter:

        ``` {.language-plaintext tabindex="-1"}
        # lpadmin -p Demo-printer -E -v ipp://192.0.2.201/printers/example-queue -m everywhere
        ```

        If the `-m everywhere`{.literal} option does not work for your printer, try `-m driverless:`{.literal}*`<uri>`{.literal}*, for example: `-m driverless:`{.literal}*`ipp://192.0.2.200/printers/example-queue`{.literal}*.

    -   To add a printer with a driver in file, enter:

        ``` {.language-plaintext tabindex="-1"}
        # lpadmin -p Demo-printer -E -v socket://192.0.2.200/ -P /root/example.ppd
        ```

    -   To add a queue from a remote print server with a driver in a file, enter:

        ``` {.language-plaintext tabindex="-1"}
        # lpadmin -p Demo-printer -E -v ipp://192.0.2.201/printers/example-queue -P /root/example.ppd
        ```

    -   To add a printer with a driver in the local driver database:

        i.  List the drivers in the database:

            ``` {.language-plaintext tabindex="-1"}
            # lpinfo -m
            ```

            ``` {.language-plaintext tabindex="-1"}
            drv:///sample.drv/generpcl.ppd Generic PCL Laser Printer
            ```

        ii. Add the printer with the URI to the driver in the database:

            ``` {.language-plaintext tabindex="-1"}
            # lpadmin -p Demo-printer -E -v socket://192.0.2.200/ -m drv:///sample.drv/generpcl.ppd
            ```

    These commands use the following options:

    -   `-p `{.literal}*`<printer_name>`{.literal}*: Sets the name of the printer in CUPS.
    -   `-E`{.literal}: Enables the printer and CUPS accepts jobs for it. Note that you must specify this option after `-p`{.literal}. See the option's description in the man page on your system for further details.
    -   `-v `{.literal}*`<uri>`{.literal}*: Sets the URI to the printer or remote print server queue.
    -   `-m `{.literal}*`<driver_uri>`{.literal}*: Sets the PPD file based on the provided driver URI obtained from the local driver database.
    -   `-P `{.literal}*`<PPD_file>`{.literal}*: Sets the path to the PPD file.

**Verification**

1.  Display the available printers:

    ``` {.language-plaintext tabindex="-1"}
    # lpstat -p
    ```

    ``` {.language-plaintext tabindex="-1"}
    printer Demo-printer is idle. enabled since Fri 23 Jun 2023 09:36:40 AM CEST
    ```

2.  Print a test page:

    ``` {.language-plaintext tabindex="-1"}
    # lp -d Demo-printer /usr/share/cups/data/default-testpage.pdf
    ```

## [Chapter 10. Performing maintenance and administration tasks on CUPS printers by using the web interface](#performing-maintenance-and-administration-tasks-on-cups-printers-by-using-the-web-interface) {#chapter-10.-performing-maintenance-and-administration-tasks-on-cups-printers-by-using-the-web-interface .title}

The CUPS web interface provides a graphical option to perform administration tasks on printers.

Printer administrators sometimes need to perform different tasks on a print server. For example:

-   Maintenance tasks, such as temporary pausing a printer while a technician repairs a printer
-   Administrative tasks, such as changing a printer's default settings

You can perform these tasks by using the CUPS web interface.

**Prerequisites**

-   [CUPS is configured](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").
-   [You have permissions in CUPS to manage printers](#granting-administration-permissions-to-manage-a-cups-server-in-the-web-interface "Chapter 3. Granting administration permissions to manage a CUPS server in the web interface").
-   If you use CUPS as a print server, [you configured TLS encryption](#configuring-tls-encryption-on-a-cups-server "Chapter 2. Configuring TLS encryption on a CUPS server") to not send credentials in plain text over the network.
-   [The printer already exists in CUPS](#adding-a-printer-to-cups-by-using-the-web-interface "Chapter 8. Adding a printer to CUPS by using the web interface").

**Procedure**

1.  Use a browser, and access `https://`{.literal}*`<hostname>`{.literal}*`:631/printers/`{.literal}.

    You must connect to the web interface by using the HTTPS protocol. Otherwise, CUPS prevents you from authenticating in a later step for security reasons.

2.  Click the name of the printer that you want to configure.

3.  Depending on whether you want to perform a maintenance or administration task, select the required action from the list.

4.  If you are not already authenticated, CUPS prompts for credentials of an administrative user. Enter the username and password of an authorized user.

5.  Perform the task.

## [Chapter 11. Using Samba to print to a Windows print server with Kerberos authentication](#using-samba-to-print-to-a-windows-print-server-with-kerberos-authentication) {#chapter-11.-using-samba-to-print-to-a-windows-print-server-with-kerberos-authentication .title}

With the `samba-krb5-printing`{.literal} wrapper, Active Directory (AD) users logged in to Red Hat Enterprise Linux can authenticate to Active Directory (AD) by using Kerberos. They can then print to a local CUPS print server that forwards the print job to a Windows print server.

Using the `samba-krb5-printing`{.literal} wrapper eliminates the need for the CUPS administrator on RHEL to store a fixed user name and password in the configuration. CUPS authenticates to AD with the Kerberos ticket of the user that sends the print job.

Note

Red Hat supports only submitting print jobs to CUPS from your local system, and not to re-share a printer on a Samba print server.

**Prerequisites**

-   The printer that you want to add to the local CUPS instance is shared on an AD print server.
-   You joined the RHEL host as a member of the AD.
-   CUPS is installed on RHEL, and the `cups`{.literal} service is running.
-   The PostScript Printer Description (PPD) file for the printer is stored in the `/usr/share/cups/model/`{.literal} directory.

**Procedure**

1.  Install the `samba-krb5-printing`{.literal}, `samba-client`{.literal}, and `krb5-workstation`{.literal} packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install samba-krb5-printing samba-client krb5-workstation
    ```

2.  Optional: Authenticate as a domain administrator, and then display the printers that the Windows print server shares:

    ``` {.language-plaintext tabindex="-1"}
    # smbclient -L <windows_print_server> -U administrator@<AD_KERBEROS_REALM> --use-kerberos=required
    ```

    ``` {.language-plaintext tabindex="-1"}
     Sharename       Type      Comment
        ---------       ----      -------
        Example         Printer   Example
    ```

3.  Optional: Display the list of CUPS models to identify the PPD name of your printer:

    ``` {.language-plaintext tabindex="-1"}
    lpinfo -m
    ```

    ``` {.language-plaintext tabindex="-1"}
    samsung.ppd Samsung M267x 287x Series PXL
    ```

    You require the name of the PPD file when you add the printer in the next step.

4.  Add the printer to CUPS:

    ``` {.language-plaintext tabindex="-1"}
    # lpadmin -p "<printer_name>" -v smb://<windows_print_server>/<printer_share_name> -m samsung.ppd -o auth-info-required=negotiate -E
    ```

    The command uses the following options:

    -   `-p `{.literal}*`<printer_name>`{.literal}* sets the name of the printer in CUPS.
    -   `-v `{.literal}*`<URI_to_Windows_printer>`{.literal}* sets the URI to the Windows printer. Use the following format: `smb://`{.literal}*`<host_name>`{.literal}*`/`{.literal}*`<printer_share_name>`{.literal}*.
    -   `-m `{.literal}*`<PPD_file>`{.literal}* sets the PPD file the printer uses.
    -   `-o auth-info-required=negotiate`{.literal} configures CUPS to use Kerberos authentication when it forwards print jobs to the remote server.
    -   `-E`{.literal} enables the printer and CUPS accepts jobs for the printer.

**Verification**

1.  Log in to the RHEL host as an AD domain user.

2.  Authenticate as an AD domain user:

    ``` {.language-plaintext tabindex="-1"}
    # kinit <domain_user_name>@<AD_KERBEROS_REALM>
    ```

3.  Print a file to the printer you added to the local CUPS print server:

    ``` {.language-plaintext tabindex="-1"}
    # lp -d <printer_name> <file>
    ```

## [Chapter 12. Using cups-browsed to locally integrate printers from a remote print server](#using-cups-browsed-to-locally-integrate-printers-from-a-remote-print-server) {#chapter-12.-using-cups-browsed-to-locally-integrate-printers-from-a-remote-print-server .title}

The `cups-browsed`{.literal} service uses DNS service discovery (DNS-SD) and CUPS browsing to make all or a filtered subset of shared remote printers automatically available in a local CUPS service. Use this feature on workstations to make only printers from a trusted print server available.

You can configure `cups-browsed`{.literal} to filter browsed printers by certain criteria to reduce the number of listed printers when a print server shares a large number of printers.

Note

If the print dialog in an application uses other mechanisms than, for example DNS-SD, to list remote printers, `cups-browsed`{.literal} has no influence. The `cups-browsed`{.literal} service also does not prevent users from manually accessing non-listed printers.

**Prerequisites**

-   [The CUPS service is configured on the local host](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").

-   A remote CUPS print server exists, and the following conditions apply to this server:

    -   The server listens on an interface that is accessible from the client.
    -   The `Allow from`{.literal} parameter in the server's `<Location />`{.literal} directive in the `/etc/cups/cups.conf`{.literal} file allows access from the client's IP address.
    -   The server shares printers.
    -   Firewall rules allow access from the client to the CUPS port on the server.

**Procedure**

1.  Edit the `/etc/cups/cups-browsed.conf`{.literal} file, and make the following changes:

    a.  Add `BrowsePoll`{.literal} parameters for each remote CUPS server you want to poll:

        ``` {.language-bash tabindex="-1"}
        BrowsePoll remote_cups_server.example.com
        BrowsePoll 192.0.2.100:1631
        ```

        Append `:_<port>_`{.literal} to the hostname or IP address if the remote CUPS server listens on a port different from 631.

    b.  Optional: Configure a filter to limit the printers that the local CUPS service shows. For example, to filter for queues whose name contain `sales_`{.literal}, add:

        ``` {.language-bash tabindex="-1"}
        BrowseFilter name sales_
        ```

        You can filter by different field names, negate the filter, and match the exact values. For further details, see the parameter description and examples in the `cups-browsed.conf(5)`{.literal} man page on your system.

    c.  Optional: Change the polling interval and timeout to limit the number of browsing cycles:

        ``` {.language-bash tabindex="-1"}
        BrowseInterval 1200
        BrowseTimeout 6000
        ```

        Increase both `BrowseInterval`{.literal} and `BrowseTimeout`{.literal} in the same ratio to avoid situations in which printers disappear from the browsing list. This means, multiply the value of `BrowseInterval`{.literal} by 5 or a higher integer, and use this result value for `BrowseTimeout`{.literal}.

        By default, `cups-browsed`{.literal} polls remote servers every 60 seconds and the timeout is 300 seconds. However, on print servers with many queues, these default values can cost many resources.

2.  Enable and start the `cups-browsed`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now cups-browsed
    ```

**Verification**

-   List the available printers:

    ``` {.language-plaintext tabindex="-1"}
    # lpstat -v
    ```

    ``` {.language-plaintext tabindex="-1"}
    device for Demo-printer: implicitclass://Demo-printer/
    ```

    If the output for a printer contains `implicitclass`{.literal}, the `cups-browsed`{.literal} service manages the printer in CUPS.

## [Chapter 13. Accessing the CUPS logs in the systemd journal](#accessing-the-cups-logs-in-the-systemd-journal) {#chapter-13.-accessing-the-cups-logs-in-the-systemd-journal .title}

By default, CUPS stores log messages in the `systemd`{.literal} journal. This includes error messages, access log entries, and page log entries.

**Prerequisites**

-   [CUPS is installed](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").

**Procedure**

-   Display the log entries:

    -   To display all log entries, enter:

        ``` {.language-plaintext tabindex="-1"}
        # journalctl -u cups
        ```

    -   To display the log entries for a specific print job, enter:

        ``` {.language-plaintext tabindex="-1"}
        # journalctl -u cups JID=<print_job_id>
        ```

    -   To display log entries within a specific time frame, enter:

        ``` {.language-plaintext tabindex="-1"}
        # journalctl -u cups --since=<YYYY-MM-DD> --until=<YYYY-MM-DD>
        ```

        Replace `YYYY`{.literal} with the year, `MM`{.literal} with the month, and `DD`{.literal} with the day.

## [Chapter 14. Configuring CUPS to store logs in files instead of the systemd journal](#configuring-cups-to-store-logs-in-files-instead-of-the-systemd-journal) {#chapter-14.-configuring-cups-to-store-logs-in-files-instead-of-the-systemd-journal .title}

By default, CUPS stores log messages in the `systemd`{.literal} journal. Alternatively, you can configure CUPS to store log messages in files.

**Prerequisites**

-   [CUPS is installed](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").

**Procedure**

1.  Edit the `/etc/cups/cups-files.conf`{.literal} file, and set the `AccessLog`{.literal}, `ErrorLog`{.literal}, and `PageLog`{.literal} parameters to the paths where you want to store these log files:

    ``` {.language-bash tabindex="-1"}
    AccessLog /var/log/cups/access_log
    ErrorLog /var/log/cups/error_log
    PageLog /var/log/cups/page_log
    ```

2.  If you configure CUPS to store the logs in a directory other than `/var/log/cups/`{.literal}, set the `cupsd_log_t`{.literal} SELinux context on this directory, for example:

    ``` {.language-plaintext tabindex="-1"}
    # semanage fcontext -a -t cupsd_log_t "/var/log/printing(/.*)?"
    # restorecon -Rv /var/log/printing/
    ```

3.  Restart the `cups`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart cups
    ```

**Verification**

1.  Display the log files:

    ``` {.language-plaintext tabindex="-1"}
    # cat /var/log/cups/access_log
    # cat /var/log/cups/error_log
    # cat /var/log/cups/page_log
    ```

2.  If you configured CUPS to store the logs in a directory other than `/var/log/cups/`{.literal}, verify that the SELinux context on the log directory is `cupsd_log_t`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # ls -ldZ /var/log/printing/
    ```

    ``` {.language-plaintext tabindex="-1"}
    drwxr-xr-x. 2 lp sys unconfined_u:object_r:cupsd_log_t:s0 6 Jun 20 15:55 /var/log/printing/
    ```

## [Chapter 15. Configuring a high-availability CUPS print server environment](#setting-up-a-high-availability-cups-print-server-environment) {#chapter-15.-configuring-a-high-availability-cups-print-server-environment .title}

If your clients require access to printers without interruption, you can configure CUPS on multiple hosts and use the print queue browsing feature to provide high availability. Print clients then automatically configure print queues shared by the different print servers.

If a client sends a print job to its local print queue, CUPS routes it to a print server, which processes and sends the job to the printer.

**Procedure**

1.  Configure CUPS on two or more servers:

    a.  [Install and configure CUPS](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").

    b.  [Enable TLS encryption](#configuring-tls-encryption-on-a-cups-server "Chapter 2. Configuring TLS encryption on a CUPS server").

    c.  Add print queues to all CUPS instances by using the [`lpadmin`{.literal} utility](#adding-a-printer-to-cups-by-using-the-lpadmin-utility "Chapter 9. Adding a printer to CUPS by using the lpadmin utility") or the [web interface](#adding-a-printer-to-cups-by-using-the-web-interface "Chapter 8. Adding a printer to CUPS by using the web interface"). If you use the web interface, ensure that you select the **Share this printer** option while you add the printer. The `lpadmin`{.literal} utility enables this setting by default.

        Important

        For the high-availability scenario, each queue on one print server requires a queue with exactly the same queue name on the other servers. You can display the queue names on each server by using the `lpstat -e`{.literal} command.

        Optional: You can configure the queues on each server to refer to different printers.

2.  On print clients:

    a.  Edit the `/etc/cups/cups-browsed.conf`{.literal} file, and add `BrowsePoll`{.literal} directives for each CUPS print server:

        ``` {.language-bash tabindex="-1"}
        BrowsePoll print_server_1.example.com:631
        BrowsePoll print_server_2.example.com:631
        ```

    b.  Enable and start both the `cups`{.literal} and `cups-browsed`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now cups cups-browsed
        ```

**Verification**

-   Display the available printers on a client:

    ``` {.language-plaintext tabindex="-1"}
    # lpstat -t
    ```

    ``` {.language-plaintext tabindex="-1"}
    device for Demo-printer: implicitclass://Demo-printer/
    Demo-printer accepting requests since Fri 22 Nov 2024 11:54:59 AM CET
    printer Demo-printer is idle.  enabled since Fri 22 Nov 2024 11:54:59 AM CET
    ...
    ```

    The example output shows that the **Demo-printer** queue uses the `implicitclass`{.literal} back end. As a result, `cups-browsed`{.literal} routes print jobs for this queue to the hosts specified in the `BrowsePoll`{.literal} directives on this client.

**Additional resources**

-   [High-availability printing in Red Hat Enterprise Linux (Red Hat Knowledgebase)](https://access.redhat.com/solutions/20501)

## [Chapter 16. Accessing the CUPS documentation](#accessing-the-cups-documentation) {#chapter-16.-accessing-the-cups-documentation .title}

CUPS provides browser-based access to the service's documentation that is installed on the CUPS server.

The browser-accessible CUPS documentation includes:

-   Administration documentation, such as for command-line printer administration and accounting
-   Man pages
-   Programming documentation, such as the administration API
-   References
-   Specifications

**Prerequisites**

-   [CUPS is installed and running](#installing-and-configuring-cups "Chapter 1. Installing and configuring CUPS").
-   The IP address of the client you want to use has permissions to access the web interface.

**Procedure**

1.  Use a browser, and access `http://`{.literal}*`<hostname_or_ip_address>`{.literal}*`:631/help/`{.literal}.
2.  Expand the entries in `Online Help Documents`{.literal}, and select the documentation you want to read.

## [Legal Notice](#idm140480843827696) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
