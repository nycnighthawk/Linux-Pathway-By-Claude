---
{"title": "Managing smart card authentication", "guide": "managing_smart_card_authentication", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_smart_card_authentication/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Managing smart card authentication {#managing-smart-card-authentication .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Configuring and using smart card authentication {#configuring-and-using-smart-card-authentication .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139860719719280)

**Abstract**

With Identity Management (IdM), you can store credentials in the form of a private key and a certificate on a smart card. You can then use this smart card instead of passwords to authenticate to services. Administrators can configure mapping rules to reduce the administrative overhead.

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

## [Chapter 1. Understanding smart card authentication](#understanding-smart-card-authentication) {#chapter-1.-understanding-smart-card-authentication .title}

Smart card authentication replaces passwords with physical tokens containing private keys. Users insert the card and enter a PIN to achieve two-factor security. Administrators use specific tools to manage card content and configure Identity Management servers and clients to support these workflows.

### [1.1. What is a smart card](#what-is-a-smart-card) {#what-is-a-smart-card .title}

A smart card acts as a secure portable token containing a microprocessor for cryptographic operations. It stores user credentials, such as private keys and certificates, enabling authentication by using specialized hardware readers and software interfaces.

You place the smart card into a reader or a USB socket and supply the PIN code for the smart card instead of providing your password.

### [1.2. What is smart card authentication](#what-is-smart-card-authentication) {#what-is-smart-card-authentication .title}

Smart card authentication verifies identity using cryptographic keys stored on a physical card rather than a password. This two-factor authentication method requires both possession of the card and knowledge of its PIN, significantly reducing the risk of impersonation.

Public-key based authentication and certificate based authentication are two widely used alternatives to password based authentication. Your identity is confirmed by using public and private keys instead of your password. A certificate is an electronic document used to identify an individual, a server, a company, or other entity and to associate that identity with a public key. Like a driver's license or passport, a certificate provides generally recognized proof of a person's identity. Public-key cryptography uses certificates to address the problem of impersonation.

In the case of smart card authentication, your user credentials, that is your public and private keys and certificate, are stored on a smart card and can only be used after the smart card is inserted into the reader and a PIN is provided. As you need to possess a physical device, the smart card, and know its PIN, smart card authentication is considered as a type of two factor authentication.

#### [1.2.1. Examples of smart card authentication in IdM](#examples_of_smart_card_authentication_in_idm) {#examples-of-smart-card-authentication-in-idm .title}

You can implement smart card authentication to secure system entry points. Common scenarios include enforcing card-based login for local users and configuring automatic screen locking when a user removes their card from the reader.

**Logging in to your system with a smart card**

You can use a smart card to authenticate to a RHEL system as a local user. If your system is configured to enforce smart card login, you are prompted to insert your smart card and enter its PIN and, if that fails, you cannot log in to your system. Alternatively, you can configure your system to authenticate using either smart card authentication or your user name and password. In this case, if you do not have your smart card inserted, you are prompted for your user name and password.

**Logging in to GDM with lock on removal**

You can activate the lock on removal function if you have configured smart card authentication on your RHEL system. If you are logged in to the GNOME Display Manager (GDM) and you remove your smart card, screen lock is enabled and you must reinsert your smart card and authenticate with the PIN to unlock the screen. You cannot use your user name and password to authenticate.

Note

If you are logged in to GDM and you remove your smart card, screen lock is enabled and you must reinsert your smart card and authenticate with the PIN to unlock the screen.

### [1.3. Supported smart cards](#supported-smart-cards) {#supported-smart-cards .title}

Red Hat Enterprise Linux supports specific smart card standards including Coolkey, CAC, PIV, and PKCS #15. Compatibility depends on the card type and configuration, with options available for various government and enterprise security requirements.

In Red Hat Enterprise Linux, the following types of smart cards are supported:

-   Cards with Coolkey applet:

    -   Gemalto TOP IM FIPS CY2 64K token (SCP01)
    -   Giesecke & Devrient (G&D) SmartCafe Expert 7.0 (SCP03)
    -   SafeNet Assured Technologies SC-650 (SCP01)

-   CAC and PIV smart cards.

-   Selected PKCS #15 cards are also supported. While several cards in this family are supported, there are many different configurations and options for these cards. For fully details on what cards are compatible with RHEL, contact your customer representative.

-   Additionally, other cards may be supported at Red Hat's discretion. For details on other cards supported, contact your customer representative.

#### [1.3.1. Supported smart card readers](#supported_smart_card_readers) {#supported-smart-card-readers .title}

The system supports smart card readers compatible with the CCID standard by using the `pcsc-lite`{.literal} project. While most CCID-compliant USB devices work automatically, Red Hat specifically tests and verifies select readers to ensure reliability.

Red Hat periodically updates the USB identifiers from the upstream project into our `pcsc-lite-ccid`{.literal} driver. Furthermore, additional readers may be supported at Red Hat's discretion. The following list of smart card readers are tested and verified by Red Hat:

-   SCR331/SCR3310
-   Omnikey 3121 (must be part number R31210399 for the SC650 card)

**Additional resources**

-   [Supported CCID readers/ICCD tokens](https://ccid.apdu.fr/ccid/supported.html)
-   [Personal Identity Verification of Federal Employees and Contractors (PIV)](https://csrc.nist.gov/Projects/piv/piv-standards-and-supporting-documentation)
-   [Smart card support in RHEL](https://access.redhat.com/articles/4253861)

### [1.4. Supported hardware security modules](#supported-hardware-security-modules) {#supported-hardware-security-modules .title}

Using hardware security modules (HSMs) provides dedicated cryptographic processing for Identity Management servers. The system supports specific firmware and client software versions for devices like nCipher nShield and Thales Luna to ensure secure key management.

+-------------------------------------+------------------------------+--------------------+------------------------------------+
| HSM                                 | Firmware                     | Appliance Software | Client Software                    |
+:====================================+:=============================+:===================+:===================================+
| nCipher nShield Connect XC (High)   | nShield_HSM_Firmware-12.72.1 | 12.71.0            | SecWorld_Lin64-12.71.0             |
+-------------------------------------+------------------------------+--------------------+------------------------------------+
| Thales TCT Luna Network HSM Luna-T7 | lunafw_update-7.11.1-4       | 7.11.0-25          | 610-500244-001_LunaClient-7.11.1-5 |
+-------------------------------------+------------------------------+--------------------+------------------------------------+

Show more

### [1.5. Smart card authentication options in RHEL](#smart-card-authentication-options-in-rhel_understanding-smart-card-authentication) {#smart-card-authentication-options-in-rhel .title}

The `authselect`{.literal} command configures system-wide authentication behaviors. You can enforce exclusive smart card usage, enabling hybrid password options, or trigger automatic session locking upon card removal to meet specific security policies.

You can configure how you want smart card authentication to work in a particular Identity Management (IdM) client by using the `authselect`{.literal} command, `authselect enable-feature `{.literal}*`<smartcard_option>`{.literal}*. The following smart card options are available:

-   `with-smartcard`{.literal}: Users can authenticate with the user name and password or with their smart card.

-   `with-smartcard-required`{.literal}: Users can authenticate with their smart cards, and password authentication is disabled. You cannot access the system without your smart card. Once you have authenticated with your smart card, you can stay logged in even if your smart card is removed from its reader.

    Note

    The `with-smartcard-required`{.literal} option only enforces exclusive smart card authentication for login services, such as `login`{.literal}, `gdm`{.literal}, `xdm`{.literal}, `xscreensaver`{.literal}, and `gnome-screensaver`{.literal}. For other services, such as `su`{.literal} or `sudo`{.literal} for switching users, smart card authentication is not enforced and if your smart card is not inserted, you are prompted for a password.

-   `with-smartcard-lock-on-removal`{.literal}: Users can authenticate with their smart card. However, if you remove your smart card from its reader, you are automatically locked out of the system. You cannot use password authentication.

    Note

    The `with-smartcard-lock-on-removal`{.literal} option only works on systems with the GNOME desktop environment. If you are using a system that is `tty`{.literal} or console based and you remove your smart card from its reader, you are not automatically locked out of the system.

**Additional resources**

-   [Configuring smart cards using authselect](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-smart-card-authentication-using-authselect)

### [1.6. Tools for managing smart cards and their contents](#tools-for-managing-smart-cards-and-their-contents) {#tools-for-managing-smart-cards-and-their-contents .title}

Utilize a suite of command-line tools to interact with smart card hardware and data. Utilities like `opensc-tool`{.literal}, `p11tool`{.literal}, and `certutil`{.literal} enable listing devices, managing cryptographic objects, and troubleshooting certificate issues.

You can use these tools to perform the following actions:

-   List available smart card readers connected to a system.
-   List available smart cards and view their contents.
-   Manipulate the smart card content, that is the keys and certificates.

There are many tools that provide similar functionality but some work at different layers of your system. Smart cards are managed on multiple layers by multiple components. On the lower level, the operating system communicates with the smart card reader using the PC/SC protocol, and this communication is handled by the `pcsc-lite`{.literal} daemon. The daemon forwards the commands received to the smart card reader typically over USB, which is handled by low-level CCID driver. The PC/SC low level communication is rarely seen on the application level. The main method in RHEL for applications to access smart cards is by using a higher level application programming interface (API), the OASIS PKCS#11 API, which abstracts the card communication to specific commands that operate on cryptographic objects, for example, private keys. Smart card vendors provide a shared module, such as an `.so`{.literal} file, which follows the PKCS#11 API and serves as a driver for the smart card.

You can use the following tools to manage your smart cards and their contents:

-   OpenSC tools: work with the drivers implemented in `opensc`{.literal}.

    -   `opensc-tool`{.literal}: perform smart card operations.
    -   `pkcs15-tool`{.literal}: manage the PKCS#15 data structures on smart cards, such as listing and reading PINs, keys, and certificates stored on the token.
    -   `pkcs11-tool`{.literal}: manage the PKCS#11 data objects on smart cards, such as listing and reading PINs, keys, and certificates stored on the token.

-   GnuTLS utils: an API for applications to enable secure communication over the network transport layer, as well as interfaces to access X.509, PKCS#12, OpenPGP, and other structures.

    -   `p11tool`{.literal}: perform operations on PKCS#11 smart cards and security modules.
    -   `certtool`{.literal}: parse and generate X.509 certificates, requests, and private keys.

-   Network Security Services (NSS) Tools: a set of libraries designed to support the cross-platform development of security-enabled client and server applications. Applications built with NSS can support SSL v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3 certificates, and other security standards.

    -   `modutil`{.literal}: manage PKCS#11 module information with the security module database.
    -   `certutil`{.literal}: manage keys and certificates in both NSS databases and other NSS tokens.

**Additional resources**

-   [Troubleshooting authentication with smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/troubleshooting-authentication-with-smart-cards)

### [1.7. Certificates and smart card authentication](#certificates-and-smart-card-authentication) {#certificates-and-smart-card-authentication .title}

Authentication relies on valid certificates generated by Identity Management (IdM), Active Directory (AD), or external authorities. You must configure the domain to trust the issuing authority and map these certificates to specific user accounts.

If you use Identity Management or Active Directory to manage identity stores, authentication, policies, and authorization policies in your domain, the certificates used for authentication are generated by IdM or AD, respectively. You can also use certificates provided by an external certificate authority and in this case you must configure Active Directory or IdM to accept certificates from the external provider. If the user is not part of a domain, you can use a certificate generated by a local certificate authority.

**Additional resources**

-   [Configuring Identity Management for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication)
-   [Configuring certificates issued by ADCS for smart card authentication in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm)
-   [Certificates eligible for smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-smart-card-authentication-using-authselect#certificates-eligible-for-smart-cards)

### [1.8. Required steps for smart card authentication in IdM](#required-steps-for-smart-card-authentication-in-idm) {#required-steps-for-smart-card-authentication-in-idm .title}

Deploying smart card authentication involves configuring both server and client components. You must configure the IdM infrastructure, map certificates to user entries, and provision the physical cards with the correct cryptographic keys.

You must ensure the following steps have been followed before you can authenticate with a smart card in Identity Management (IdM):

-   Configure your IdM server for smart card authentication.
-   Configure your IdM client for smart card authentication.
-   Add the certificate to the user entry in IdM.
-   Store your keys and certificates on the smart card.

**Additional resources**

-   [Configuring the IdM server for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-server-for-smart-card-authentication)
-   [Configuring the IdM client for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-client-for-smart-card-authentication)
-   [Adding a certificate to a user entry in the IdM Web UI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/configuring-identity-management-for-smart-card-authentication#adding-a-certificate-to-a-user-entry-in-the-idm-web-ui)
-   [Storing a certificate on a smart card](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#preparing-your-smart-card-and-uploading-your-certificates-and-keys-to-your-smart-card)

### [1.9. Required steps for smart card authentication with certificates issued by Active Directory](#required-steps-for-smart-card-authentication-with-certificates-issued-by-active-directory) {#required-steps-for-smart-card-authentication-with-certificates-issued-by-active-directory .title}

Integrating Active Directory (AD) certificates requires establishing trust and mapping rules within Identity Management (IdM). You must import AD certificate authorities, convert user credentials for card storage, and configure SSSD to handle the cross-domain authentication flow.

You must ensure the following steps have been followed before you can authenticate with a smart card with certificates issued by Active Directory (AD):

-   Copy the CA and user certificates from Active Directory to the IdM server and client.
-   Configure the IdM server and clients for smart card authentication using ADCS certificates.
-   Convert the PFX (PKCS#12) file to be able to store the certificate and private key on the smart card.
-   Configure timeouts in the sssd.conf file.
-   Create certificate mapping rules for smart card authentication.

**Additional resources**

-   [Copying certificates from Active Directory using SFTP](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm#copying-certificates-from-active-directory-using-sftp)
-   [Configuring the IdM server and clients for smart card authentication using ADCS certificates](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm#configuring-the-idm-server-and-clients-for-smart-card-authentication-using-adcs-certificates)
-   [Converting the PFX file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm#converting-the-pfx-file)
-   [Configuring timeouts in sssd.conf](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm#configuring-timeouts-in-sssd-conf)
-   [Creating certificate mapping rules for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm#creating-certificate-mapping-rules-for-smart-card-authentication)

## [Chapter 2. Configuring Identity Management for smart card authentication](#configuring-identity-management-for-smart-card-authentication) {#chapter-2.-configuring-identity-management-for-smart-card-authentication .title}

Identity Management (IdM) supports smart card authentication by using certificates issued internally or by external authorities. Configure the `rootca.pem`{.literal} file to establish trust for external certificate authorities, enabling secure access across the domain.

Note

Currently, IdM does not support importing multiple CAs that share the same Subject Distinguished Name (DN) but are cryptographically different.

### [2.1. Configuring the IdM server for smart card authentication](#configuring-the-idm-server-for-smart-card-authentication) {#configuring-the-idm-server-for-smart-card-authentication .title}

The `ipa-advise`{.literal} utility generates a configuration script to enable smart card authentication on the server. This script automates the configuration of the Apache HTTP Server, Key Distribution Center (KDC) Public Key Cryptography for Initial Authentication in Kerberos (PKINIT), and the IdM Web UI for certificate handling.

Learn how to enable smart card authentication for users whose certificates have been issued by the certificate authority (CA) of the \<EXAMPLE.ORG\> domain that your Identity Management (IdM) CA trusts.

**Prerequisites**

-   You have root access to the IdM server.

-   You have the root CA certificate and all the intermediate CA certificates:

    -   The certificate of the root CA that has either issued the certificate for the \<EXAMPLE.ORG\> CA directly, or by using one or more of its sub-CAs. You can download the certificate chain from a web page whose certificate has been issued by the authority.
    -   The IdM CA certificate. You can obtain the CA certificate from the `/etc/ipa/ca.crt`{.literal} file on the IdM server on which an IdM CA instance is running.
    -   The certificates of all of the intermediate CAs; that is, intermediate between the \<EXAMPLE.ORG\> CA and the IdM CA.

**Procedure**

1.  Create a directory in which you will do the configuration:

    ``` {.language-plaintext tabindex="-1"}
    [root@server]# mkdir ~/SmartCard/
    ```

2.  Navigate to the directory:

    ``` {.language-plaintext tabindex="-1"}
    [root@server]# cd ~/SmartCard/
    ```

3.  Obtain the relevant CA certificates stored in files in PEM format. If your CA certificate is stored in a file of a different format, such as DER, convert it to PEM format. The IdM Certificate Authority certificate is in PEM format and is located in the `/etc/ipa/ca.crt`{.literal} file.

    Convert a DER file to a PEM file:

    ``` {.language-plaintext tabindex="-1"}
    # openssl x509 -in <filename>.der -inform DER -out <filename>.pem -outform PEM
    ```

4.  For convenience, copy the certificates to the directory in which you want to do the configuration:

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# cp /tmp/rootca.pem ~/SmartCard/
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# cp /tmp/subca.pem ~/SmartCard/
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# cp /tmp/issuingca.pem ~/SmartCard/
    ```

5.  Optional: If you use certificates of external certificate authorities, use the `openssl x509`{.literal} utility to view the contents of the files in the `PEM`{.literal} format to check that the `Issuer`{.literal} and `Subject`{.literal} values are correct:

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# openssl x509 -noout -text -in rootca.pem | more
    ```

6.  Generate a configuration script with the in-built `ipa-advise`{.literal} utility, using the administrator's privileges:

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# ipa-advise config-server-for-smart-card-auth > config-server-for-smart-card-auth.sh
    ```

    The `config-server-for-smart-card-auth.sh`{.literal} script performs the following actions:

    -   It configures the IdM Apache HTTP Server.
    -   It enables Public Key Cryptography for Initial Authentication in Kerberos (PKINIT) on the Key Distribution Center (KDC).
    -   It configures the IdM Web UI to accept smart card authorization requests.

7.  Run the script, adding the PEM files containing the root CA and sub CA certificates as arguments:

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# chmod +x config-server-for-smart-card-auth.sh
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# ./config-server-for-smart-card-auth.sh rootca.pem subca.pem issuingca.pem
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache:KEYRING:persistent:0:0
    Default principal: \admin@IDM.EXAMPLE.COM
    [...]
    Systemwide CA database updated.
    The ipa-certupdate command was successful
    ```

    Note

    Ensure that you add the root CA's certificate as an argument before any sub CA certificates and that the CA or sub CA certificates have not expired.

8.  Optional: If the certificate authority that issued the user certificate does not provide any Online Certificate Status Protocol (OCSP) responder, you may need to disable OCSP check for authentication to the IdM Web UI:

    a.  Set the `SSLOCSPEnable`{.literal} parameter to `off`{.literal} in the `/etc/httpd/conf.d/ssl.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        SSLOCSPEnable off
        ```

    b.  Restart the Apache daemon (httpd) for the changes to take effect immediately:

        ``` {.language-plaintext tabindex="-1"}
        [root@server SmartCard]# systemctl restart httpd
        ```

    Warning

    Do not disable the OCSP check if you only use user certificates issued by the IdM CA. OCSP responders are part of IdM.

    For instructions on how to keep the OCSP check enabled, and yet prevent a user certificate from being rejected by the IdM server if it does not contain the information about the location at which the CA that issued the user certificate listens for OCSP service requests, see the `SSLOCSPDefaultResponder`{.literal} directive in [Apache mod_ssl configuration options](http://httpd.apache.org/docs/trunk/en/mod/mod_ssl.html).

    The server is now configured for smart card authentication.

    Note

    To enable smart card authentication in the whole topology, run the procedure on each IdM server.

**Additional resources**

-   [Configuring a browser to enable certificate authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/configuring-authentication-with-a-certificate-stored-on-the-desktop-of-an-idm-client#configuring-a-browser-to-enable-certificate-authentication)

### [2.2. Using Ansible to configure the IdM server for smart card authentication](#using-ansible-to-configure-the-idm-server-for-smart-card-authentication) {#using-ansible-to-configure-the-idm-server-for-smart-card-authentication .title}

Ansible automates the server configuration by using the `ipasmartcard_server`{.literal} role. This playbook configures Apache and the KDC using the root and intermediate CA certificates specified in the inventory file.

You can use Ansible to enable smart card authentication for users whose certificates have been issued by the certificate authority (CA) of the \<EXAMPLE.ORG\> domain that your Identity Management (IdM) CA trusts. To do that, you must obtain the following certificates so that you can use them when running an Ansible playbook with the `ipasmartcard_server`{.literal} `ansible-freeipa`{.literal} role script:

-   The certificate of the root CA that has either issued the certificate for the \<EXAMPLE.ORG\> CA directly, or by using one or more of its sub-CAs. You can download the certificate chain from a web page whose certificate has been issued by the authority. For details, see Step 4 in [Configuring a browser to enable certificate authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/configuring-authentication-with-a-certificate-stored-on-the-desktop-of-an-idm-client#configuring-a-browser-to-enable-certificate-authentication).
-   The IdM CA certificate. You can obtain the CA certificate from the `/etc/ipa/ca.crt`{.literal} file on any IdM CA server.
-   The certificates of all of the CAs that are intermediate between the \<EXAMPLE.ORG\> CA and the IdM CA.

**Prerequisites**

-   You have `root`{.literal} access to the IdM server.

-   You know the IdM `admin`{.literal} password.

-   You have the root CA certificate, the IdM CA certificate, and all the intermediate CA certificates.

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  If your CA certificates are stored in files of a different format, such as `DER`{.literal}, convert them to `PEM`{.literal} format:

    ``` {.language-plaintext tabindex="-1"}
    # openssl x509 -in <filename>.der -inform DER -out <filename>.pem -outform PEM
    ```

    The IdM Certificate Authority certificate is in `PEM`{.literal} format and is located in the `/etc/ipa/ca.crt`{.literal} file.

2.  Optional: Use the `openssl x509`{.literal} utility to view the contents of the files in the `PEM`{.literal} format to check that the `Issuer`{.literal} and `Subject`{.literal} values are correct:

    ``` {.language-plaintext tabindex="-1"}
    # openssl x509 -noout -text -in root-ca.pem | more
    ```

3.  Navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

4.  Create a subdirectory dedicated to the CA certificates:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir SmartCard/
    ```

5.  For convenience, copy all the required certificates to the **\~/MyPlaybooks/SmartCard/** directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp /tmp/root-ca.pem ~/MyPlaybooks/SmartCard/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cp /tmp/intermediate-ca.pem ~/MyPlaybooks/SmartCard/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cp /etc/ipa/ca.crt ~/MyPlaybooks/SmartCard/ipa-ca.crt
    ```

6.  In your Ansible inventory file, specify the following:

    -   The IdM servers that you want to configure for smart card authentication.

    -   The IdM administrator password.

    -   The paths to the certificates of the CAs in the following order:

        -   The root CA certificate file
        -   The intermediate CA certificates files
        -   The IdM CA certificate file

    The file can look as follows:

    ``` {.language-plaintext tabindex="-1"}
    [ipaserver]
    ipaserver.idm.example.com

    [ipareplicas]
    ipareplica1.idm.example.com
    ipareplica2.idm.example.com

    [ipacluster:children]
    ipaserver
    ipareplicas

    [ipacluster:vars]
    ipaadmin_password= "{{ ipaadmin_password }}"
    ipasmartcard_server_ca_certs=/home/<user_name>/MyPlaybooks/SmartCard/root-ca.pem,/home/<user_name>/MyPlaybooks/SmartCard/intermediate-ca.pem,/home/<user_name>/MyPlaybooks/SmartCard/ipa-ca.crt
    ```

7.  Create an `install-smartcard-server.yml`{.literal} playbook with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to set up smart card authentication for an IdM server
      hosts: ipaserver
      become: true

      roles:
      - role: ipasmartcard_server
        state: present
    ```

8.  Save the file.

    For example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/`{.literal} directory on the control node.

9.  Run the Ansible playbook. Specify the playbook file, the file storing the password protecting the **secret.yml** file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory install-smartcard-server.yml
    ```

    The `ipasmartcard_server`{.literal} Ansible role performs the following actions:

    -   It configures the IdM Apache HTTP Server.
    -   It enables Public Key Cryptography for Initial Authentication in Kerberos (PKINIT) on the Key Distribution Center (KDC).
    -   It configures the IdM Web UI to accept smart card authorization requests.

10. Optional: If the certificate authority that issued the user certificate does not provide any Online Certificate Status Protocol (OCSP) responder, you may need to disable OCSP check for authentication to the IdM Web UI:

    a.  Connect to the IdM server as `root`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        ssh root@ipaserver.idm.example.com
        ```

    b.  Set the `SSLOCSPEnable`{.literal} parameter to `off`{.literal} in the `/etc/httpd/conf.d/ssl.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        SSLOCSPEnable off
        ```

    c.  Restart the Apache daemon (httpd) for the changes to take effect immediately:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart httpd
        ```

    Warning

    Do not disable the OCSP check if you only use user certificates issued by the IdM CA. OCSP responders are part of IdM.

    For instructions on how to keep the OCSP check enabled, and yet prevent a user certificate from being rejected by the IdM server if it does not contain the information about the location at which the CA that issued the user certificate listens for OCSP service requests, see the `SSLOCSPDefaultResponder`{.literal} directive in [Apache mod_ssl configuration options](http://httpd.apache.org/docs/trunk/en/mod/mod_ssl.html).

    The server listed in the inventory file is now configured for smart card authentication.

    Note

    To enable smart card authentication in the whole topology, set the `hosts`{.literal} variable in the Ansible playbook to `ipacluster`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to set up smartcard for IPA server and replicas
      hosts: ipacluster
    [...]
    ```

### [2.3. Configuring the IdM client for smart card authentication](#configuring-the-idm-client-for-smart-card-authentication) {#configuring-the-idm-client-for-smart-card-authentication .title}

IdM clients require specific configurations to support smart card logins for SSH, GDM, and console sessions. You can generate a configuration script on the server and run it on target clients to configure SSSD and system truststores.

You can configure IdM clients for smart card authentication. The procedure needs to be run on each IdM system, a client or a server, to which you want to connect while using a smart card for authentication. For example, to enable an `ssh`{.literal} connection from host A to host B, the script needs to be run on host B.

As an administrator, run this procedure to enable smart card authentication using

-   The `ssh`{.literal} protocol

    For details see [Configuring SSH access using smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-smart-card-authentication-with-local-certificates#configuring-ssh-access-using-smart-card-authentication).

-   The console login

-   The GNOME Display Manager (GDM)

-   The `su`{.literal} command

This procedure is not required for authenticating to the IdM Web UI. Authenticating to the IdM Web UI involves two hosts, neither of which needs to be an IdM client:

-   The machine on which the browser is running. The machine can be outside of the IdM domain.
-   The IdM server on which `httpd`{.literal} is running.

The following procedure assumes that you are configuring smart card authentication on an IdM client, not an IdM server. For this reason you need two computers: an IdM server to generate the configuration script, and the IdM client on which to run the script.

**Prerequisites**

-   Your IdM server has been configured for smart card authentication, as described in [Configuring the IdM server for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-server-for-smart-card-authentication).
-   You have root access to the IdM server and the IdM client.
-   You have the root CA certificate and all the intermediate CA certificates.
-   You installed the IdM client with the `--mkhomedir`{.literal} option to ensure remote users can log in successfully. If you do not create a home directory, the default login location is the root of the directory structure, `/`{.literal}.

**Procedure**

1.  On an IdM server, generate a configuration script with `ipa-advise`{.literal} using the administrator's privileges:

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# ipa-advise config-client-for-smart-card-auth > config-client-for-smart-card-auth.sh
    ```

    The `config-client-for-smart-card-auth.sh`{.literal} script performs the following actions:

    -   It configures the smart card daemon.
    -   It sets the system-wide truststore.
    -   It configures the System Security Services Daemon (SSSD) to allow users to authenticate with either their user name and password or with their smart card. For more details on SSSD profile options for smart card authentication, see [Smart card authentication options in RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/understanding-smart-card-authentication#smart-card-authentication-options-in-rhel).

2.  From the IdM server, copy the script to a directory of your choice on the IdM client machine:

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# scp config-client-for-smart-card-auth.sh root@client.idm.example.com:/root/SmartCard/
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password:
    config-client-for-smart-card-auth.sh        100%   2419       3.5MB/s   00:00
    ```

3.  From the IdM server, copy the CA certificate files in PEM format for convenience to the same directory on the IdM client machine as used in the previous step:

    ``` {.language-plaintext tabindex="-1"}
    [root@server SmartCard]# scp {rootca.pem,subca.pem,issuingca.pem} root@client.idm.example.com:/root/SmartCard/
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password:
    rootca.pem                          100%   1237     9.6KB/s   00:00
    subca.pem                           100%   2514    19.6KB/s   00:00
    issuingca.pem                       100%   2514    19.6KB/s   00:00
    ```

4.  On the client machine, run the script, adding the PEM files containing the CA certificates as arguments:

    ``` {.language-plaintext tabindex="-1"}
    [root@client SmartCard]# kinit admin
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@client SmartCard]# chmod +x config-client-for-smart-card-auth.sh
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@client SmartCard]# ./config-client-for-smart-card-auth.sh rootca.pem subca.pem issuingca.pem
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache:KEYRING:persistent:0:0
    Default principal: \admin@IDM.EXAMPLE.COM
    [...]
    Systemwide CA database updated.
    The ipa-certupdate command was successful
    ```

    Note

    Ensure that you add the root CA's certificate as an argument before any sub CA certificates and that the CA or sub CA certificates have not expired.

    The client is now configured for smart card authentication.

### [2.4. Using Ansible to configure IdM clients for smart card authentication](#using-ansible-to-configure-idm-clients-for-smart-card-authentication) {#using-ansible-to-configure-idm-clients-for-smart-card-authentication .title}

The `ipasmartcard_client`{.literal} Ansible role automates the configuration of multiple clients simultaneously. This playbook configures the smart card daemon, system truststores, and SSSD profiles to permit certificate-based authentication across the entire infrastructure.

Enable smart card authentication for IdM users that use any of the following to access IdM:

-   The `ssh`{.literal} protocol

    For details see [Configuring SSH access using smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication).

-   The console login

-   The GNOME Display Manager (GDM)

-   The `su`{.literal} command

Note

This procedure is not required for authenticating to the IdM Web UI. Authenticating to the IdM Web UI involves two hosts, neither of which needs to be an IdM client:

-   The machine on which the browser is running. The machine can be outside of the IdM domain.
-   The IdM server on which `httpd`{.literal} is running.

**Prerequisites**

-   Your IdM server has been configured for smart card authentication, as described in [Using Ansible to configure the IdM server for smart card authentication](#using-ansible-to-configure-the-idm-server-for-smart-card-authentication "2.2. Using Ansible to configure the IdM server for smart card authentication").

-   You have root access to the IdM server and the IdM client.

-   You have the root CA certificate, the IdM CA certificate, and all the intermediate CA certificates.

-   You have configured your Ansible control node to meet the following requirements:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  If your CA certificates are stored in files of a different format, such as `DER`{.literal}, convert them to `PEM`{.literal} format:

    ``` {.language-plaintext tabindex="-1"}
    # openssl x509 -in <filename>.der -inform DER -out <filename>.pem -outform PEM
    ```

    The IdM CA certificate is in `PEM`{.literal} format and is located in the `/etc/ipa/ca.crt`{.literal} file.

2.  Optional: Use the `openssl x509`{.literal} utility to view the contents of the files in the `PEM`{.literal} format to check that the `Issuer`{.literal} and `Subject`{.literal} values are correct:

    ``` {.language-plaintext tabindex="-1"}
    # openssl x509 -noout -text -in root-ca.pem | more
    ```

3.  On your Ansible control node, navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

4.  Create a subdirectory dedicated to the CA certificates:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir SmartCard/
    ```

5.  For convenience, copy all the required certificates to the **\~/MyPlaybooks/SmartCard/** directory, for example:

    ``` {.language-plaintext tabindex="-1"}
    # cp /tmp/root-ca.pem ~/MyPlaybooks/SmartCard/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cp /tmp/intermediate-ca.pem ~/MyPlaybooks/SmartCard/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cp /etc/ipa/ca.crt ~/MyPlaybooks/SmartCard/ipa-ca.crt
    ```

6.  In your Ansible inventory file, specify the following:

    -   The IdM clients that you want to configure for smart card authentication.

    -   The IdM administrator password.

    -   The paths to the certificates of the CAs in the following order:

        -   The root CA certificate file
        -   The intermediate CA certificates files
        -   The IdM CA certificate file

    The file can look as follows:

    ``` {.language-plaintext tabindex="-1"}
    [ipaclients]
    ipaclient1.example.com
    ipaclient2.example.com

    [ipaclients:vars]
    ipaadmin_password=SomeADMINpassword
    ipasmartcard_client_ca_certs=/home/<user_name>/MyPlaybooks/SmartCard/root-ca.pem,/home/<user_name>/MyPlaybooks/SmartCard/intermediate-ca.pem,/home/<user_name>/MyPlaybooks/SmartCard/ipa-ca.crt
    ```

7.  Create an `install-smartcard-clients.yml`{.literal} playbook with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Playbook to set up smart card authentication for an IdM client
      hosts: ipaclients
      become: true

      roles:
      - role: ipasmartcard_client
        state: present
    ```

8.  Save the file.

    For example playbooks in the FreeIPA Ansible collection, see the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/`{.literal} directory on the control node.

9.  Run the Ansible playbook. Specify the playbook and inventory files:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory install-smartcard-clients.yml
    ```

    The `ipasmartcard_client`{.literal} Ansible role performs the following actions:

    -   It configures the smart card daemon.

    -   It sets the system-wide truststore.

    -   It configures the System Security Services Daemon (SSSD) to allow users to authenticate with either their user name and password or their smart card. For more details on SSSD profile options for smart card authentication, see [Smart card authentication options in RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/understanding-smart-card-authentication#smart-card-authentication-options-in-rhel).

        The clients listed in the **ipaclients** section of the inventory file are now configured for smart card authentication.

    Note

    If you have installed the IdM clients with the `--mkhomedir`{.literal} option, remote users will be able to log in to their home directories. Otherwise, the default login location is the root of the directory structure, `/`{.literal}.

### [2.5. Adding a certificate to a user entry in the IdM Web UI](#adding-a-certificate-to-a-user-entry-in-the-idm-web-ui) {#adding-a-certificate-to-a-user-entry-in-the-idm-web-ui .title}

You can upload external certificates directly to user profiles by using the IdM Web UI. This action associates the specific credentials on a physical smart card with the corresponding Identity Management user account.

Instead of uploading the whole certificate, it is also possible to upload certificate mapping data to a user entry in IdM. User entries containing either full certificates or certificate mapping data can be used in conjunction with corresponding certificate mapping rules to facilitate the configuration of smart card authentication for system administrators. For details, see [Certificate mapping rules for configuring authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/certificate-mapping-rules-for-configuring-authentication).

Note

If the user's certificate has been issued by the IdM Certificate Authority, the certificate is already stored in the user entry, and you do not need to follow this procedure.

**Prerequisites**

-   You have the certificate that you want to add to the user entry at your disposal.

**Procedure**

1.  Log into the IdM Web UI as an administrator if you want to add a certificate to another user. For adding a certificate to your own profile, you do not need the administrator's credentials.

2.  Navigate to `Users`{.literal} → `Active users`{.literal} → `sc_user`{.literal}.

3.  Find the `Certificate`{.literal} option and click `Add`{.literal}.

4.  On the command line, display the certificate in the `PEM`{.literal} format using the `cat`{.literal} utility or a text editor:

    ``` {.language-plaintext tabindex="-1"}
    [user@client SmartCard]$ cat testuser.crt
    ```

5.  Copy and paste the certificate from the CLI into the window that has opened in the Web UI.

6.  Click `Add`{.literal}.

    The `sc_user`{.literal} entry now contains an external certificate.

### [2.6. Adding a certificate to a user entry in the IdM CLI](#adding-a-certificate-to-a-user-entry-in-the-idm-cli) {#adding-a-certificate-to-a-user-entry-in-the-idm-cli .title}

The command-line interface enables you to map external certificates to user entries. You must format the certificate string to remove headers and footers before executing the `ipa user-add-cert`{.literal} command.

Instead of uploading the whole certificate, it is also possible to upload certificate mapping data to a user entry in IdM. User entries containing either full certificates or certificate mapping data can be used in conjunction with corresponding certificate mapping rules to facilitate the configuration of smart card authentication for system administrators. For details, see [Certificate mapping rules for configuring authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/certificate-mapping-rules-for-configuring-authentication).

Note

If the user's certificate has been issued by the IdM Certificate Authority, the certificate is already stored in the user entry, and you do not need to follow this procedure.

**Prerequisites**

-   You have the certificate that you want to add to the user entry at your disposal.

**Procedure**

1.  Log into the IdM CLI as an administrator if you want to add a certificate to another user:

    ``` {.language-plaintext tabindex="-1"}
    [user@client SmartCard]$ kinit admin
    ```

    For adding a certificate to your own profile, you do not need the administrator's credentials.

    ``` {.language-plaintext tabindex="-1"}
    [user@client SmartCard]$ kinit <smartcard_user>
    ```

2.  Create an environment variable containing the certificate with the header and footer removed and concatenated into a single line, which is the format expected by the `ipa user-add-cert`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [user@client SmartCard]$ export CERT=`openssl x509 -outform der -in testuser.crt | base64 -w0 -`
    ```

    Note that certificate in the `testuser.crt`{.literal} file must be in the `PEM`{.literal} format.

3.  Add the certificate to the profile of *\<smartcard_user\>* using the `ipa user-add-cert`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [user@client SmartCard]$ ipa user-add-cert <smartcard_user> --certificate=$CERT
    ```

    The *`<smartcard_user>`{.literal}* entry now contains an external certificate.

### [2.7. Installing tools for managing and using smart cards](#installing-tools-for-managing-and-using-smart-cards) {#installing-tools-for-managing-and-using-smart-cards .title}

Configuring smart cards requires specific middleware and management utilities, such as OpenSC and GnuTLS packages. Enable the `pcscd`{.literal} service to facilitate communication between the system and the card reader.

**Prerequisites**

-   You have `root`{.literal} permissions.

**Procedure**

1.  Install the `opensc`{.literal} and `gnutls-utils`{.literal} packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install opensc gnutls-utils
    ```

2.  Start the `pcscd`{.literal} service.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pcscd
    ```

**Verification**

-   Verify that the `pcscd`{.literal} service is up and running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status pcscd
    ```

### [2.8. Preparing your smart card and uploading your certificates and keys to your smart card](#preparing-your-smart-card-and-uploading-your-certificates-and-keys-to-your-smart-card) {#preparing-your-smart-card-and-uploading-your-certificates-and-keys-to-your-smart-card .title}

The `pkcs15-init`{.literal} tool initializes blank smart cards and manages their cryptographic contents. Use this utility to erase cards, define PINs, create storage slots, and upload the necessary private keys and certificates.

The `pkcs15-init`{.literal} tool may not work with all smart cards. You must use the tools that work with the smart card you are using.

**Prerequisites**

-   The `opensc`{.literal} package, which includes the `pkcs15-init`{.literal} tool, is installed.

    For more details, see [Installing tools for managing and using smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#installing-tools-for-managing-and-using-smart-cards).

-   The card is inserted in the reader and connected to the computer.

-   You have a private key, a public key, and a certificate to store on the smart card. In this procedure, `testuser.key`{.literal}, `testuserpublic.key`{.literal}, and `testuser.crt`{.literal} are the names used for the private key, public key, and the certificate.

-   You have your current smart card user PIN and Security Officer PIN (SO-PIN).

**Procedure**

1.  Erase your smart card and authenticate yourself with your PIN:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --erase-card --use-default-transport-keys
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    PIN [Security Officer PIN] required.
    Please enter PIN [Security Officer PIN]:
    ```

    The card has been erased.

2.  Initialize your smart card, set your user PIN and PUK, and your Security Officer PIN and PUK:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --create-pkcs15 --use-default-transport-keys \
        --pin 963214 --puk 321478 --so-pin 65498714 --so-puk 784123
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

    The `pcks15-init`{.literal} tool creates a new slot on the smart card.

3.  Set a label and the authentication ID for the slot:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --store-pin --label testuser \
        --auth-id 01 --so-pin 65498714 --pin 963214 --puk 321478
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

    The label is set to a human-readable value, in this case, `testuser`{.literal}. The `auth-id`{.literal} must be two hexadecimal values, in this case it is set to `01`{.literal}.

4.  Store and label the private key in the new slot on the smart card:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --store-private-key testuser.key --label testuser_key \
        --auth-id 01 --id 01 --pin 963214
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

    Note

    The value you specify for `--id`{.literal} must be the same when storing your private key and storing your certificate in the next step. Specifying your own value for `--id`{.literal} is recommended as otherwise a more complicated value is calculated by the tool.

5.  Store and label the certificate in the new slot on the smart card:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --store-certificate testuser.crt --label testuser_crt \
        --auth-id 01 --id 01 --format pem --pin 963214
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

6.  Optional: Store and label the public key in the new slot on the smart card:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --store-public-key testuserpublic.key \
        --label testuserpublic_key --auth-id 01 --id 01 --pin 963214
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

    Note

    If the public key corresponds to a private key or certificate, specify the same ID as the ID of the private key or certificate.

7.  Optional: Certain smart cards require you to finalize the card by locking the settings:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init -F
    ```

    At this stage, your smart card contains the certificate, private key, and public key in the newly created slot. You have also created your user PIN and PUK and the Security Officer PIN and PUK.

### [2.9. Logging in to IdM with smart cards](#logging-in-to-idm-with-smart-cards) {#logging-in-to-idm-with-smart-cards .title}

Users access the IdM Web UI securely by selecting the certificate authentication option. The browser prompts for the smart card PIN to unlock the device and validate the user's identity against the server.

**Prerequisites**

-   The web browser is configured for using smart card authentication.
-   The IdM server is configured for smart card authentication.
-   The certificate installed on your smart card is either issued by the IdM server or has been added to the user entry in IdM.
-   You know the PIN required to unlock the smart card.
-   The smart card has been inserted into the reader.

**Procedure**

1.  Open the IdM Web UI in the browser.

2.  Click **Log In Using Certificate**.

3.  If the **Password Required** dialog box opens, add the PIN to unlock the smart card and click the **OK** button.

    The **User Identification Request** dialog box opens.

    If the smart card contains more than one certificate, select the certificate you want to use for authentication in the drop down list below **Choose a certificate to present as identification**.

4.  Click the **OK** button.

    Now you are successfully logged in to the IdM Web UI.

### [2.10. Logging in to GDM using smart card authentication on an IdM client](#logging-in-to-gdm-using-smart-card-authentication-on-an-idm-client) {#logging-in-to-gdm-using-smart-card-authentication-on-an-idm-client .title}

The GNOME Display Manager (GDM) supports direct login by using smart card hardware. Users insert their card and enter the PIN to authenticate, automatically obtaining a Kerberos Ticket Granting Ticket (TGT) for the session.

**Prerequisites**

-   The system has been configured for smart card authentication. For details, see [Configuring the IdM client for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-client-for-smart-card-authentication).

-   The smart card contains your certificate and private key.

-   The user account is a member of the IdM domain.

-   The certificate on the smart card maps to the user entry by using one of the following:

    -   Assigning the certificate to a particular user entry. For details, see, [Adding a certificate to a user entry in the IdM Web UI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#adding-a-certificate-to-a-user-entry-in-the-idm-web-ui) or [Adding a certificate to a user entry in the IdM CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#adding-a-certificate-to-a-user-entry-in-the-idm-cli).
    -   The certificate mapping data being applied to the account. For details, see [Certificate mapping rules for configuring authentication on smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/certificate-mapping-rules-for-configuring-authentication).

**Procedure**

1.  Insert the smart card in the reader.

2.  Enter the smart card PIN.

3.  Click **Sign In**.

    You are successfully logged in to the RHEL system and you have a TGT provided by the IdM server.

**Verification**

-   In the **Terminal** window, enter `klist`{.literal} and check the result:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KEYRING:persistent:1358900015:krb_cache_TObtNMd
    Default principal: example.user@REDHAT.COM

    Valid starting       Expires              Service principal
    04/20/2020 13:58:24  04/20/2020 23:58:24  krbtgt/EXAMPLE.COM@EXAMPLE.COM
        renew until 04/27/2020 08:58:15
    ```

### [2.11. Using smart card authentication with the su command](#using-smart-card-authentication-with-the-su-command) {#using-smart-card-authentication-with-the-su-command .title}

The `su`{.literal} command supports smart card validation for switching user contexts. When you configure it, the system prompts the user for the smart card PIN instead of a password to authorize the privilege escalation.

**Prerequisites**

-   Your IdM server and client have been configured for smart card authentication.

    -   See [Configuring the IdM server for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-server-for-smart-card-authentication)
    -   See [Configuring the IdM client for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-client-for-smart-card-authentication)

-   The card is inserted in the reader and connected to the computer.

**Procedure**

-   In a terminal window, change to a different user with the `su`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ su - <user_name>
    ```

    ``` {.language-plaintext tabindex="-1"}
    PIN for smart_card
    ```

    If the configuration is correct, you are prompted to enter the smart card PIN.

## [Chapter 3. Configuring certificates issued by ADCS for smart card authentication in IdM](#configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm) {#chapter-3.-configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm .title}

You can leverage Active Directory (AD) Certificate Services (ADCS) to issue credentials for IdM smart card users. This configuration integrates AD-issued certificates within an IdM environment, utilizing a cross-forest trust to authenticate users across both domains.

### [3.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   Identity Management (IdM) and Active Directory (AD) trust is installed
-   Active Directory Certificate Services (ADCS) is installed and certificates for users are generated

### [3.2. Windows Server settings required for trust configuration and certificate usage](#windows-server-settings-required-for-trust-configuration-and-certificate-usage) {#windows-server-settings-required-for-trust-configuration-and-certificate-usage .title}

Configuring the Windows Server involves preparing the Certificate Authority to issue compatible credentials. You must set key lengths to at least 2048 bits and enable private key export to generate valid PKCS #12 (.PFX) files.

You must configure the following on the Windows Server:

-   Active Directory Certificate Services (ADCS) is installed
-   Certificate Authority is created
-   Optional: If you are using Certificate Authority Web Enrollment, the Internet Information Services (IIS) must be configured

The exported certificate must fulfill the following criteria:

-   Key must have `2048`{.literal} bits or more

-   Include a private key

-   You will need a certificate in the following format: Personal Information Exchange --- `PKCS #12(.PFX)`{.literal}

    -   Enable certificate privacy

### [3.3. Copying certificates from Active Directory using sftp](#copying-certificates-from-active-directory-using-sftp) {#copying-certificates-from-active-directory-using-sftp .title}

To enable cross-platform trust, you must transfer specific certificate files from the Windows Server to the Linux environment. You must securely copying the root CA certificate to the IdM server and the user's private key file to the client.

To be able to use smart card authentication, you need to copy the following certificate files:

-   A root CA certificate in the `CER`{.literal} format: `adcs-winserver-ca.cer`{.literal} on your IdM server.
-   A user certificate with a private key in the `PFX`{.literal} format: `aduser1.pfx`{.literal} on an IdM client.

Note

This procedure expects SSH access is allowed. If SSH is unavailable the user must copy the file from the AD Server to the IdM server and client.

**Procedure**

1.  Connect from **the IdM server** and copy the `adcs-winserver-ca.cer`{.literal} root certificate to the IdM server:

    ``` {.language-plaintext tabindex="-1"}
    root@idmserver ~]# sftp Administrator@winserver.ad.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Administrator@winserver.ad.example.com's password:
    Connected to Administrator@winserver.ad.example.com.
    sftp> cd <path_to_certificates>
    sftp> ls
    adcs-winserver-ca.cer    aduser1.pfx
    sftp>
    sftp> get adcs-winserver-ca.cer
    Fetching <path_to_certificates>/adcs-winserver-ca.cer to adcs-winserver-ca.cer
    <path_to_certificates>/adcs-winserver-ca.cer                 100%  1254    15KB/s 00:00
    sftp quit
    ```

2.  Connect from **the IdM client** and copy the `aduser1.pfx`{.literal} user certificate to the client:

    ``` {.language-plaintext tabindex="-1"}
    [root@client1 ~]# sftp Administrator@winserver.ad.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Administrator@winserver.ad.example.com's password:
    Connected to Administrator@winserver.ad.example.com.
    sftp> cd /<path_to_certificates>
    sftp> get aduser1.pfx
    Fetching <path_to_certificates>/aduser1.pfx to aduser1.pfx
    <path_to_certificates>/aduser1.pfx                 100%  1254    15KB/s 00:00
    sftp quit
    ```

    Now the CA certificate is stored in the IdM server and the user certificates is stored on the client machine.

### [3.4. Configuring the IdM server and clients for smart card authentication using ADCS certificates](#configuring-the-idm-server-and-clients-for-smart-card-authentication-using-adcs-certificates) {#configuring-the-idm-server-and-clients-for-smart-card-authentication-using-adcs-certificates .title}

The `ipa-advise`{.literal} utility automates the configuration of Identity Management (IdM) components for ADCS integration. Generate server and client scripts to install necessary packages, configure Kerberos PKINIT, and place CA certificates in the correct system directories.

Configure your server and clients for smart card authentication by choosing one of the options:

-   On an IdM server: Prepare the `ipa-advise`{.literal} script to configure your IdM server for smart card authentication.
-   On an IdM server: Prepare the `ipa-advise`{.literal} script to configure your IdM client for smart card authentication.
-   On an IdM server: Apply the `ipa-advise`{.literal} server script on the IdM server using the AD certificate.
-   Move the client script to the IdM client machine.
-   On an IdM client: Apply the `ipa-advise`{.literal} client script on the IdM client using the AD certificate.

**Prerequisites**

-   The certificate has been copied to the IdM server.
-   Obtain the Kerberos ticket.
-   Log in as a user with administration rights.

**Procedure**

1.  On the IdM server, use the `ipa-advise`{.literal} script for configuring a client:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmserver ~]# ipa-advise config-client-for-smart-card-auth > sc_client.sh
    ```

2.  On the IdM server, use the `ipa-advise`{.literal} script for configuring a server:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmserver ~]# ipa-advise config-server-for-smart-card-auth > sc_server.sh
    ```

3.  On the IdM server, run the script:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmserver ~]# sh -x sc_server.sh adcs-winserver-ca.cer
    ```

    -   It configures the IdM Apache HTTP Server.
    -   It enables Public Key Cryptography for Initial Authentication in Kerberos (PKINIT) on the Key Distribution Center (KDC).
    -   It configures the IdM Web UI to accept smart card authorization requests.

4.  Copy the `sc_client.sh`{.literal} script to the client system:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmserver ~]# scp sc_client.sh root@client1.idm.example.com:/root
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password:
    sc_client.sh                  100%  2857   1.6MB/s   00:00
    ```

5.  Copy the Windows certificate to the client system:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmserver ~]# scp adcs-winserver-ca.cer root@client1.idm.example.com:/root
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password:
    adcs-winserver-ca.cer                 100%  1254   952.0KB/s   00:00
    ```

6.  On the client system, run the client script:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient1 ~]# sh -x sc_client.sh adcs-winserver-ca.cer
    ```

    The CA certificate is now installed in the correct format on the IdM server and client systems. The next step is to copy the user certificates onto the smart card itself.

### [3.5. Converting the PFX file](#converting-the-pfx-file) {#converting-the-pfx-file .title}

Smart card tools require certificates and keys in specific formats. You must convert the PKCS #12 (.PFX) file exported from Active Directory into separate PEM-formatted private key and certificate files using OpenSSL.

**Prerequisites**

-   The PFX file is copied into the IdM client machine.

**Procedure**

1.  On the IdM client, convert the file into the PEM format:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient1 ~]# openssl pkcs12 -in aduser1.pfx -out aduser1_cert_only.pem -clcerts -nodes
    ```

    ``` {.language-plaintext tabindex="-1"}
    Enter Import Password:
    ```

2.  Extract the key into the separate file:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient1 ~]# openssl pkcs12 -in adduser1.pfx -nocerts -out adduser1.pem > aduser1.key
    ```

3.  Extract the public certificate into the separate file:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient1 ~]# openssl pkcs12 -in adduser1.pfx -clcerts -nokeys -out aduser1_cert_only.pem > aduser1.crt
    ```

    At this point, you can store the `aduser1.key`{.literal} and `aduser1.crt`{.literal} into the smart card.

### [3.6. Installing tools for managing and using smart cards with ADCS certificates on them](#installing-tools-for-managing-and-using-smart-cards-with-adcs-certificates-on-them) {#installing-tools-for-managing-and-using-smart-cards-with-adcs-certificates-on-them .title}

Managing smart card content requires specific software utilities, such as the `opensc`{.literal} and `gnutls-utils`{.literal} packages. You must start the `pcscd`{.literal} service to enable communication between the system and the smart card reader.

**Prerequisites**

-   You have `root`{.literal} permissions.

**Procedure**

1.  Install the `opensc`{.literal} and `gnutls-utils`{.literal} packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install opensc gnutls-utils
    ```

2.  Start the `pcscd`{.literal} service.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pcscd
    ```

**Verification**

-   Verify that the `pcscd`{.literal} service is up and running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status pcscd
    ```

### [3.7. Preparing your smart card and uploading your ADCS certificates and keys to your smart card](#preparing-your-smart-card-and-uploading-your-adcs-certificates-and-keys-to-your-smart-card) {#preparing-your-smart-card-and-uploading-your-adcs-certificates-and-keys-to-your-smart-card .title}

With the `pkcs15-init`{.literal} tool, you can initialize smart cards and provision them with ADCS credentials. Initialization involves erasing the card, setting PINs, and uploading the converted private key and certificate files to a new storage slot.

The `pkcs15-init`{.literal} tool may not work with all smart cards. You must use the tools that work with the smart card you are using.

**Prerequisites**

-   The `opensc`{.literal} package, which includes the `pkcs15-init`{.literal} tool, is installed.

    For more details, see [Installing tools for managing and using smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#installing-tools-for-managing-and-using-smart-cards).

-   The card is inserted in the reader and connected to the computer.

-   You have a private key, a public key, and a certificate to store on the smart card. In this procedure, `testuser.key`{.literal}, `testuserpublic.key`{.literal}, and `testuser.crt`{.literal} are the names used for the private key, public key, and the certificate.

-   You have your current smart card user PIN and Security Officer PIN (SO-PIN).

**Procedure**

1.  Erase your smart card and authenticate yourself with your PIN:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --erase-card --use-default-transport-keys
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    PIN [Security Officer PIN] required.
    Please enter PIN [Security Officer PIN]:
    ```

    The card has been erased.

2.  Initialize your smart card, set your user PIN and PUK, and your Security Officer PIN and PUK:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --create-pkcs15 --use-default-transport-keys \
        --pin 963214 --puk 321478 --so-pin 65498714 --so-puk 784123
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

    The `pcks15-init`{.literal} tool creates a new slot on the smart card.

3.  Set a label and the authentication ID for the slot:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --store-pin --label testuser \
        --auth-id 01 --so-pin 65498714 --pin 963214 --puk 321478
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

    The label is set to a human-readable value, in this case, `testuser`{.literal}. The `auth-id`{.literal} must be two hexadecimal values, in this case it is set to `01`{.literal}.

4.  Store and label the private key in the new slot on the smart card:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --store-private-key testuser.key --label testuser_key \
        --auth-id 01 --id 01 --pin 963214
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

    Note

    The value you specify for `--id`{.literal} must be the same when storing your private key and storing your certificate in the next step. Specifying your own value for `--id`{.literal} is recommended as otherwise a more complicated value is calculated by the tool.

5.  Store and label the certificate in the new slot on the smart card:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --store-certificate testuser.crt --label testuser_crt \
        --auth-id 01 --id 01 --format pem --pin 963214
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

6.  Optional: Store and label the public key in the new slot on the smart card:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init --store-public-key testuserpublic.key \
        --label testuserpublic_key --auth-id 01 --id 01 --pin 963214
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using reader with a card: Reader name
    ```

    Note

    If the public key corresponds to a private key or certificate, specify the same ID as the ID of the private key or certificate.

7.  Optional: Certain smart cards require you to finalize the card by locking the settings:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs15-init -F
    ```

    At this stage, your smart card contains the certificate, private key, and public key in the newly created slot. You have also created your user PIN and PUK and the Security Officer PIN and PUK.

### [3.8. Configuring timeouts in sssd.conf](#configuring-timeouts-in-sssd-conf) {#configuring-timeouts-in-sssd.conf .title}

Smart card operations can exceed default SSSD timeout values due to hardware latency or virtualization. You can extend the `p11_child_timeout`{.literal} and `krb5_auth_timeout`{.literal} parameters in `sssd.conf`{.literal} to prevent premature authentication failures.

Authentication with a smart card certificate might take longer than the default timeouts used by SSSD. Time out expiration can be caused by:

-   A slow reader
-   Forwarding from a physical device into a virtual environment
-   Too many certificates stored on the smart card
-   Slow response from the OCSP (Online Certificate Status Protocol) responder if OCSP is used to verify the certificates

**Prerequisites**

-   You must be logged in as root.

**Procedure**

1.  Open the `sssd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [root@idmclient1 ~]# vim /etc/sssd/sssd.conf
    ```

2.  Change the value of `p11_child_timeout`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [pam]
    p11_child_timeout = 60
    ```

3.  Change the value of `krb5_auth_timeout`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [domain/IDM.EXAMPLE.COM]
    krb5_auth_timeout = 60
    ```

4.  Save the settings.

    Now, the interaction with the smart card is allowed to run for 1 minute (60 seconds) before authentication fails with a timeout.

### [3.9. Creating certificate mapping rules for smart card authentication](#creating-certificate-mapping-rules-for-smart-card-authentication) {#creating-certificate-mapping-rules-for-smart-card-authentication .title}

Certificate mapping rules link a single smart card certificate to multiple user accounts across Active Directory (AD) and IdM. Administrators configure these rules on the Identity Management (IdM) server to enable seamless authentication in both domains using the same physical token.

If you want to use one certificate for a user who has accounts in AD and in IdM, you can create a certificate mapping rule on the IdM server.

After creating such a rule, the user is able to authenticate with their smart card in both domains.

**Additional resources**

-   [Certificate mapping rules for configuring authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/certificate-mapping-rules-for-configuring-authentication)

## [Chapter 4. Certificate mapping rules for configuring authentication](#certificate-mapping-rules-for-configuring-authentication) {#chapter-4.-certificate-mapping-rules-for-configuring-authentication .title}

You might need to configure certificate mapping rules in the following scenarios:

-   Certificates have been issued by the Certificate System of the Active Directory (AD) with which the IdM domain is in a trust relationship.
-   Certificates have been issued by an external certificate authority.
-   The IdM environment is large with many users using smart cards. In this case, adding full certificates can be complicated. The subject and issuer are predictable in most scenarios and therefore easier to add ahead of time than the full certificate.

As a system administrator, you can create a certificate mapping rule and add certificate mapping data to a user entry even before a certificate is issued to a particular user. Once the certificate is issued, the user can log in using the certificate even though the full certificate has not yet been uploaded to the user entry.

In addition, as certificates are renewed at regular intervals, certificate mapping rules reduce administrative overhead. When a user's certificate is renewed, the administrator does not have to update the user entry. For example, if the mapping is based on the `Subject`{.literal} and `Issuer`{.literal} values, and if the new certificate has the same subject and issuer as the old one, the mapping still applies. If, in contrast, the full certificate was used, then the administrator would have to upload the new certificate to the user entry to replace the old one.

To configure certificate mapping:

1.  An administrator has to load the certificate mapping data or the full certificate into a user account.
2.  An administrator has to create a certificate mapping rule to allow successful logging into IdM for a user whose account contains a certificate mapping data entry that matches the information on the certificate.

Once the certificate mapping rules have been created, when the end-user presents the certificate, stored either on the filesystem or a smart card, authentication is successful.

Note

-   The Key Distribution Center (KDC) has a cache for certificate mapping rules. The cache is populated on the first `certauth`{.literal} request and it has a hard-coded timeout of 300 seconds. KDC will not see any changes to certificate mapping rules unless it is restarted or the cache expires.
-   Your certificate mapping rules can depend on the use case for which you are using the certificate. For example, if you are using SSH with certificates, you must have the full certificate to extract the public key from the certificate.

**Additional resources**

-   [Configuring authentication with a certificate stored on the desktop of an IdM client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/configuring-authentication-with-a-certificate-stored-on-the-desktop-of-an-idm-client)
-   [Logging in to IdM with smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#logging-in-to-idm-with-smart-cards)

## [Chapter 5. Configuring smart card authentication with the web console for centrally managed users](#configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users) {#chapter-5.-configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users .title}

Configure smart card authentication for centrally managed users in the RHEL web console. This security measure helps to provide physical access control for administrative and regular users.

You can configure smart card authentication in the RHEL web console for users who are centrally managed by:

-   Identity Management
-   Active Directory which is connected in the cross-forest trust with Identity Management

### [5.1. Prerequisites](#prerequisites_2) {#prerequisites-1 .title}

-   The system for which you want to use the smart card authentication must be a member of an Active Directory or Identity Management domain.
-   The certificate used for the smart card authentication must be associated with a particular user in Identity Management or Active Directory.

### [5.2. Smart-card authentication for centrally managed users](#smart-card-authentication-for-centrally-managed-users) {#smart-card-authentication-for-centrally-managed-users .title}

Use smart-card authentication to provide strong authentication for centrally managed users. This method links the user account to a physical credential, enhancing security for systems within the Identity Management domain.

A smart card is a physical device, which can provide personal authentication by using certificates stored on the card. Personal authentication means that you can use smart cards in the same way as user passwords.

You can store user credentials on the smart card in the form of a private key and a certificate. Special software and hardware is used to access them. You insert the smart card into a reader or a USB socket and supply the PIN code for the smart card instead of providing your password.

Identity Management (IdM) supports smart-card authentication with user certificates issued by the Active Directory Certificate Service (ADCS) certificate authority.

**Additional resources**

-   [Configuring certificates issued by ADCS for smart card authentication in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm)
-   [Smart-card support in RHEL 8 and later (Red Hat Knowledgebase)](https://access.redhat.com/articles/4253861)

### [5.3. Enabling smart-card authentication for the web console](#enabling-smart-card-authentication-for-the-web-console) {#enabling-smart-card-authentication-for-the-web-console .title}

To allow centrally managed users to securely log in by using their smart card credentials and the IdM domain policy, enable smart card authentication for the RHEL web console.

To use smart-card authentication in the web console, enable this authentication method in the `cockpit.conf`{.literal} file. Additionally, you can disable password authentication in the same file.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click **Terminal**.

3.  In the `/etc/cockpit/cockpit.conf`{.literal}, set the `ClientCertAuthentication`{.literal} to `yes`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [WebService]
    ClientCertAuthentication = yes
    ```

4.  Optional: Disable password-based authentication in `cockpit.conf`{.literal} with:

    ``` {.language-plaintext tabindex="-1"}
    [Basic]
    action = none
    ```

    This configuration disables password authentication and you must always use the smart card.

5.  Restart the web console to ensure that the `cockpit.service`{.literal} accepts the change:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart cockpit
    ```

**Verification**

-   Open the web console login page. The web console prompts you to insert your smart card or use a smart card for authentication.

### [5.4. Logging in to the web console with smart cards](#logging-in-to-the-web-console-with-smart-cards) {#logging-in-to-the-web-console-with-smart-cards .title}

You can log in to the RHEL web console with your smart card credentials. This uses the configured smart card policy for secure access by centrally managed users.

**Prerequisites**

-   A valid certificate stored in your smart card that is associated to a user account created in an Active Directory or Identity Management domain.

-   PIN to unlock the smart card.

-   The smart card has been put into the reader.

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.

    The browser asks you to add the PIN protecting the certificate stored on the smart card.

2.  In the **Password Required** dialog box, enter PIN and click **OK**.

3.  In the **User Identification Request** dialog box, select the certificate stored in the smart card.

4.  Select **Remember this decision**.

    The system does not open this window next time.

    Note

    This step does not apply to Google Chrome users.

5.  Click **OK**.

**Verification**

-   The web console displays the **Overview** page, confirming that the smart card authentication was successful.

### [5.5. Enabling passwordless sudo authentication for smart-card users](#enabling-passwordless-sudo-authentication-for-smart-card-users) {#enabling-passwordless-sudo-authentication-for-smart-card-users .title}

You can enable passwordless `sudo`{.literal} authentication for smart-card users to allow them to perform administrative tasks without entering a password, improving operational efficiency and security.

Alternatively, if you use RHEL Identity Management, you can declare the initial web console certificate as trusted for authentication with `sudo`{.literal}, SSH, or other services. The web console automatically creates an S4U2Proxy Kerberos ticket in the user session for this purpose.

In the following example, the web console session runs on `host.example.com`{.literal} and is trusted to access its own host with `sudo`{.literal}. Additionally, the example steps add a second trusted host - `remote.example.com`{.literal}.

**Prerequisites**

-   Identity Management is installed.
-   Active Directory is connected in the cross-forest trust with Identity Management.
-   Your smart card is configured to log in to the web console. See [Configuring smart-card authentication with the web console for centrally managed users](#configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users "Chapter 5. Configuring smart card authentication with the web console for centrally managed users") for more information.

**Procedure**

1.  Configure constraint delegation rules to list which hosts the ticket can access.

    -   Create the following example delegation:

        -   Enter the following commands to add a list of target machines a particular rule can access:

            ``` {.language-plaintext tabindex="-1"}
            # ipa servicedelegationtarget-add cockpit-target
            ```

            ``` {.language-plaintext tabindex="-1"}
            # ipa servicedelegationtarget-add-member cockpit-target \ --principals=host/host.example.com@EXAMPLE.COM \ --principals=host/remote.example.com@EXAMPLE.COM
            ```

        -   To enable the web console sessions (HTTP/principal) to access that host list, use the following commands:

            ``` {.language-plaintext tabindex="-1"}
            # ipa servicedelegationrule-add cockpit-delegation
            ```

            ``` {.language-plaintext tabindex="-1"}
            # ipa servicedelegationrule-add-member cockpit-delegation \ --principals=HTTP/host.example.com@EXAMPLE.COM
            ```

            ``` {.language-plaintext tabindex="-1"}
            # ipa servicedelegationrule-add-target cockpit-delegation \ --servicedelegationtargets=cockpit-target
            ```

2.  Enable GSS authentication in the corresponding services:

    a.  For `sudo`{.literal}, enable the `pam_sss_gss`{.literal} module in the `/etc/sssd/sssd.conf`{.literal} file:

        i.  As `root`{.literal}, add an entry for your domain to the `/etc/sssd/sssd.conf`{.literal} configuration file.

            ``` {.language-plaintext tabindex="-1"}
            [domain/example.com]
            pam_gssapi_services = sudo, sudo-i
            ```

        ii. Enable the module in the `/etc/pam.d/sudo`{.literal} file on the first line.

            ``` {.language-plaintext tabindex="-1"}
            auth sufficient pam_sss_gss.so
            ```

    b.  For SSH, update the `GSSAPIAuthentication`{.literal} option in the `/etc/ssh/sshd_config`{.literal} file to `yes`{.literal}.

        Warning

        The delegated S4U ticket is not forwarded to remote SSH hosts when connecting to them from the web console. Authenticating to `sudo`{.literal} on a remote host with your ticket will not work.

**Verification**

1.  Log in to the web console using a smart card.
2.  Click the **Limited access** button.
3.  Authenticate using your smart card.
4.  Alternatively: Try to connect to a different host with SSH.

### [5.6. Limiting user sessions and memory to prevent a DoS attack](#limiting-user-sessions-and-memory-to-prevent-a-dos-attack) {#limiting-user-sessions-and-memory-to-prevent-a-dos-attack .title}

To mitigate the risk of denial-of-service (DoS) attacks on the `cockpit-ws`{.literal} web server, limit user sessions and memory consumption of the web console service by changing its systemd configuration.

Certificate authentication isolates instances of the `cockpit-ws`{.literal} web server to prevent user impersonation. However, it introduces a surface for a DoS attack. A remote attacker could create multiple certificates and send multiple HTTPS requests to `cockpit-ws`{.literal}, each using a different one.

To prevent such DoS attacks, the collective resources of these web server instances are limited. By default, limits are set to 200 threads, with 75% as a soft limit and 90% as a hard limit on memory usage.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  On the command line, open the `system-cockpithttps.slice`{.literal} configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl edit system-cockpithttps.slice
    ```

2.  Limit the `TasksMax`{.literal} to *100* and `CPUQuota`{.literal} to *30%*:

    ``` {.language-plaintext tabindex="-1"}
    [Slice]
    # change existing value
    TasksMax=100
    # add new restriction
    CPUQuota=30%
    ```

3.  To apply the changes, restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop cockpit
    ```

**Verification**

-   Verify that the new resource limits are applied:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl show system-cockpithttps.slice --property=TasksMax,CPUQuota
    ```

### [5.7. Additional resources](#configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users_57-additional-resources) {#additional-resources .title}

-   [Joining a RHEL system to an IdM domain by using the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/configuring-sso-authentication-for-the-rhel-web-console-in-the-idm-domain)
-   [Adding a certificate to a user entry in the IdM Web UI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#adding-a-certificate-to-a-user-entry-in-the-idm-web-ui)
-   [Adding a certificate to a user entry in the IdM CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#adding-a-certificate-to-a-user-entry-in-the-idm-cli)

## [Chapter 6. Configuring smart card authentication with local certificates](#configuring-smart-card-authentication-with-local-certificates) {#chapter-6.-configuring-smart-card-authentication-with-local-certificates .title}

You can configure smart card authentication on standalone hosts without a domain connection. This setup involves generating local certificates, storing them on the smart card, and configuring system services such as SSH to validate credentials against a local authority.

To configure smart card authentication with local certificates:

-   The host is not connected to a domain.
-   You want to authenticate with a smart card on this host.
-   You want to configure SSH access using smart card authentication.
-   You want to configure the smart card with `authselect`{.literal}.

Use the following configuration to accomplish this scenario:

-   Obtain a user certificate for the user who wants to authenticate with a smart card. The certificate should be generated by a trustworthy Certification Authority used in the domain.

    If you cannot get the certificate, you can generate a user certificate signed by a local certificate authority for testing purposes,

-   Store the certificate and private key in a smart card.

-   Configure the smart card authentication for SSH access.

Important

If a host can be part of the domain, add the host to the domain and use certificates generated by Active Directory or Identity Management Certification Authority.

The `authselect`{.literal} tool configures user authentication on Linux hosts and you can use it to configure smart card authentication parameters.

### [6.1. Prerequisites](#prerequisites_3) {#prerequisites-2 .title}

-   Supported Smart Card or USB devices.

### [6.2. Creating local certificates](#creating-local-certificates) {#creating-local-certificates .title}

Testing smart card authentication requires a valid certificate chain. Administrators can generate a local self-signed Certificate Authority (CA) and use it to sign user certificate requests, creating a functional credential set for development environments.

Follow this procedure to perform the following tasks:

-   Generate the OpenSSL certificate authority
-   Create a certificate signing request

Warning

The following steps are intended for testing purposes only. Certificates generated by a local self-signed Certificate Authority are not as secure as using AD, IdM, or RHCS Certification Authority. You should use a certificate generated by your enterprise Certification Authority even if the host is not part of the domain.

**Procedure**

1.  Create a directory where you can generate the certificate, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /tmp/ca
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cd /tmp/ca
    ```

2.  Set up the certificate (copy this text to your command line in the `ca`{.literal} directory):

    ``` {.language-plaintext tabindex="-1"}
    # cat > ca.cnf <<EOF
    ```

    ``` {.language-plaintext tabindex="-1"}
    [ ca ]
    default_ca = CA_default

    [ CA_default ]
    dir              = .
    database         = \$dir/index.txt
    new_certs_dir    = \$dir/newcerts

    certificate      = \$dir/rootCA.crt
    serial           = \$dir/serial
    private_key      = \$dir/rootCA.key
    RANDFILE         = \$dir/rand

    default_days     = 365
    default_crl_days = 30
    default_md       = sha256

    policy           = policy_any
    email_in_dn      = no

    name_opt         = ca_default
    cert_opt         = ca_default
    copy_extensions  = copy

    [ usr_cert ]
    authorityKeyIdentifier = keyid, issuer

    [ v3_ca ]
    subjectKeyIdentifier   = hash
    authorityKeyIdentifier = keyid:always,issuer:always
    basicConstraints       = CA:true
    keyUsage               = critical, digitalSignature, cRLSign, keyCertSign

    [ policy_any ]
    organizationName       = supplied
    organizationalUnitName = supplied
    commonName             = supplied
    emailAddress           = optional

    [ req ]
    distinguished_name = req_distinguished_name
    prompt             = no

    [ req_distinguished_name ]
    O  = Example
    OU = Example Test
    CN = Example Test CA
    EOF
    ```

3.  Create the following directories:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir certs crl newcerts
    ```

4.  Create the following files:

    ``` {.language-plaintext tabindex="-1"}
    # touch index.txt crlnumber index.txt.attr
    ```

5.  Write the number 01 in the serial file:

    ``` {.language-plaintext tabindex="-1"}
    # echo 01 > serial
    ```

    This command writes a number 01 in the serial file. It is a serial number of the certificate. With each new certificate released by this CA the number increases by one.

6.  Create an OpenSSL root CA key:

    ``` {.language-plaintext tabindex="-1"}
    # openssl genrsa -out rootCA.key 2048
    ```

7.  Create a self-signed root Certification Authority certificate:

    ``` {.language-plaintext tabindex="-1"}
    # openssl req -batch -config ca.cnf \ -x509 -new -nodes -key rootCA.key -sha256 -days 10000 \ -set_serial 0 -extensions v3_ca -out rootCA.crt
    ```

8.  Create the key for your username:

    ``` {.language-plaintext tabindex="-1"}
    # openssl genrsa -out example.user.key 2048
    ```

    This key is generated in the local system which is not secure, therefore, remove the key from the system when the key is stored in the card.

    You can create a key directly in the smart card as well. For doing this, follow instructions created by the manufacturer of your smart card.

9.  Create the certificate signing request configuration file (copy this text to your command line in the ca directory):

    ``` {.language-plaintext tabindex="-1"}
    # cat > req.cnf <<EOF
    ```

    ``` {.language-plaintext tabindex="-1"}
    [ req ]
    distinguished_name = req_distinguished_name
    prompt = no

    [ req_distinguished_name ]
    O = Example
    OU = Example Test
    CN = testuser

    [ req_exts ]
    basicConstraints = CA:FALSE
    nsCertType = client, email
    nsComment = "testuser"
    subjectKeyIdentifier = hash
    keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
    extendedKeyUsage = clientAuth, emailProtection, msSmartcardLogin
    subjectAltName = otherName:msUPN;UTF8:testuser@EXAMPLE.COM, email:testuser@example.com
    EOF
    ```

10. Create a certificate signing request for your example.user certificate:

    ``` {.language-plaintext tabindex="-1"}
    # openssl req -new -nodes -key example.user.key \ -reqexts req_exts -config req.cnf -out example.user.csr
    ```

11. Configure the new certificate. Expiration period is set to 1 year:

    ``` {.language-plaintext tabindex="-1"}
    # openssl ca -config ca.cnf -batch -notext \ -keyfile rootCA.key -in example.user.csr -days 365 \ -extensions usr_cert -out example.user.crt
    ```

    At this point, the certification authority and certificates are successfully generated and prepared for import into a smart card.

### [6.3. Copying certificates to the SSSD directory](#copying-certificates-to-the-sssd-directory) {#copying-certificates-to-the-sssd-directory .title}

SSSD requires access to the trusted Certificate Authority to validate user credentials. Administrators must copy the generated root CA certificate to the `/etc/sssd/pki`{.literal} directory, allowing the system to verify the authenticity of smart card logins.

GNOME Display Manager (GDM) requires SSSD. If you use GDM, you need to copy the PEM certificate to the `/etc/sssd/pki`{.literal} directory.

**Prerequisites**

-   The local CA authority and certificates have been generated

**Procedure**

1.  Ensure that you have SSSD installed on the system.

    ``` {.language-plaintext tabindex="-1"}
    # rpm -q sssd
    ```

    ``` {.language-plaintext tabindex="-1"}
    sssd-2.0.0.43.el8_0.3.x86_64
    ```

2.  Create a `/etc/sssd/pki`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # file /etc/sssd/pki
    ```

    ``` {.language-plaintext tabindex="-1"}
    /etc/sssd/pki/: directory
    ```

3.  Copy the `rootCA.crt`{.literal} as a PEM file in the `/etc/sssd/pki/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp /tmp/ca/rootCA.crt /etc/sssd/pki/sssd_auth_ca_db.pem
    ```

    Now you have successfully generated the certificate authority and certificates, and you have saved them in the `/etc/sssd/pki`{.literal} directory.

    Note

    If you want to share the Certificate Authority certificates with another application, you can change the location in sssd.conf:

    -   SSSD PAM responder: `pam_cert_db_path`{.literal} in the `[pam]`{.literal} section
    -   SSSD ssh responder: `ca_db`{.literal} in the `[ssh]`{.literal} section

    For details, see man page for `sssd.conf`{.literal}.

    Red Hat recommends keeping the default path and using a dedicated Certificate Authority certificate file for SSSD to make sure that only Certificate Authorities trusted for authentication are listed here.

### [6.4. Configuring SSH access using smart card authentication](#configuring-ssh-access-using-smart-card-authentication) {#configuring-ssh-access-using-smart-card-authentication .title}

SSH supports smart card authentication by retrieving public keys directly from the token. You can extract the key by using `opensc`{.literal} libraries and add it to the user's `authorized_keys`{.literal} file to enable PIN-based login.

SSH connections require authentication. You can use a password or a certificate. Follow this procedure to enable authentication using a certificate stored on a smart card.

For details about configuring smart cards with `authselect`{.literal}, see [Configuring smart cards using authselect](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-smart-card-authentication-using-authselect).

**Prerequisites**

-   The smart card contains your certificate and private key.

-   The card is inserted in the reader and connected to the computer.

-   The `pcscd`{.literal} service is running on your local machine.

    For details, see [Installing tools for managing and using smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#installing-tools-for-managing-and-using-smart-cards).

**Procedure**

1.  Create a new directory for SSH keys in the home directory of the user who uses smart card authentication:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /home/<example_user>/.ssh
    ```

2.  Run the `ssh-keygen -D`{.literal} command with the `opensc`{.literal} library to retrieve the existing public key paired with the private key on the smart card, and add it to the `authorized_keys`{.literal} list of the user's SSH keys directory to enable SSH access with smart card authentication.

    ``` {.language-plaintext tabindex="-1"}
    # ssh-keygen -D /usr/lib64/pkcs11/opensc-pkcs11.so >> ~<example_user>/.ssh/authorized_keys
    ```

3.  SSH requires access right configuration for the `/.ssh`{.literal} directory and the `authorized_keys`{.literal} file. To set or change the access rights, enter:

    ``` {.language-plaintext tabindex="-1"}
    # chown -R <example_user:example_user> ~<example_user>/.ssh/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 700 ~<example_user>/.ssh/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 600 ~<example_user>/.ssh/authorized_keys
    ```

**Verification**

1.  Display the keys:

    ``` {.language-plaintext tabindex="-1"}
    # cat ~<example_user>/.ssh/authorized_keys
    ```

    The terminal displays the keys.

2.  Verify the SSH access with the following command:

    ``` {.language-plaintext tabindex="-1"}
    # ssh -I /usr/lib64/opensc-pkcs11.so -l <example_user> localhost hostname
    ```

If the configuration is successful, you are prompted to enter the smart card PIN.

The configuration works now locally. Now you can copy the public key and distribute it to `authorized_keys`{.literal} files located on all servers on which you want to use SSH.

### [6.5. Creating certificate mapping rules when using smart cards](#creating-certificate-mapping-rules-when-using-smart-cards) {#creating-certificate-mapping-rules-when-using-smart-cards .title}

Certificate mapping rules link specific certificate attributes, such as Subject or Issuer, to local system accounts. You can define these rules in SSSD configuration files to authorize users based on the credentials stored on their physical tokens.

You need to create certificate mapping rules in order to log in using the certificate stored on a smart card.

**Prerequisites**

-   The smart card contains your certificate and private key.
-   The card is inserted in the reader and connected to the computer.
-   The `pcscd`{.literal} service is running on your local machine.

**Procedure**

1.  Create a certificate mapping configuration file, such as `/etc/sssd/conf.d/sssd_certmap.conf`{.literal}.

2.  Add certificate mapping rules to the `sssd_certmap.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [certmap/shadowutils/otheruser]
    matchrule = <SUBJECT>.CN=certificate_user.<ISSUER>^CN=Example Test CA,OU=Example Test,O=EXAMPLE$
    ```

    Note that you must define each certificate mapping rule in separate sections. Define each section as follows:

    ``` {.language-plaintext tabindex="-1"}
    [certmap/<DOMAIN_NAME>/<RULE_NAME>]
    ```

    If SSSD is configured to use the proxy provider to allow smart card authentication for local users instead of AD, IPA, or LDAP, the *\<RULE_NAME\>* can simply be the username of the user with the card matching the data provided in the `matchrule`{.literal}.

**Verification**

Note that to verify SSH access with a smart card, SSH access must be configured. For more information, see [Configuring SSH access using smart card authentication](#configuring-ssh-access-using-smart-card-authentication "6.4. Configuring SSH access using smart card authentication").

-   You can verify the SSH access with the following command:

    ``` {.language-plaintext tabindex="-1"}
    # ssh -I /usr/lib64/opensc-pkcs11.so -l otheruser localhost hostname
    ```

    If the configuration is successful, you are prompted to enter the smart card PIN.

### [6.6. Additional resources](#configuring-smart-card-authentication-with-local-certificates_66-additional-resources) {#additional-resources-1 .title}

-   [Configuring Identity Management for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication)
-   [What is authselect used for](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect#what-is-authselect-used-for)
-   [Smart card support in RHEL](https://access.redhat.com/articles/4253861)

## [Chapter 7. Configuring smart card authentication using authselect](#configuring-smart-card-authentication-using-authselect) {#chapter-7.-configuring-smart-card-authentication-using-authselect .title}

Configure smart cards authentication by using the `authselect`{.literal} tool to increase workstation security and simplify the user login process. This utility manages system-wide authentication profiles, allowing options ranging from hybrid password access to strict card-only enforcement and automated screen locking.

You can configure your smart card to achieve one of the following goals:

-   Enable both password and smart card authentication
-   Disable password and enable smart card authentication
-   Enable lock on removal

### [7.1. Certificates eligible for smart cards](#certificates-eligible-for-smart-cards) {#certificates-eligible-for-smart-cards .title}

Smart card configuration relies on valid cryptographic credentials. Before you can configure a smart card with `authselect`{.literal}, you must import a certificate into your card. You can provision cards using certificates issued by the following providers:

-   Active Directory (AD)
-   Identity Management (IdM)
-   Red Hat Certificate System (RHCS)
-   Third-party Certification Authority (CA)
-   Local Certification Authority. You can use a certificate generated by the Local Certification Authority if the user is not part of a domain or for testing purposes.

**Additional resources**

-   [Managing Smart Cards with the Enterprise Security Client](https://docs.redhat.com/en/documentation/red_hat_certificate_system/10/html/managing_smart_cards_with_the_enterprise_security_client/index)
-   [Requesting a new user certificate and exporting it to the client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/configuring-authentication-with-a-certificate-stored-on-the-desktop-of-an-idm-client#requesting-a-new-user-certificate-and-exporting-it-to-the-client)

### [7.2. Configuring smart card authentication with authselect](#configuring-smart-card-authentication-with-authselect) {#configuring-smart-card-authentication-with-authselect .title}

Configure smart card authentication on your system using the `authselect`{.literal} tool. You can enable hybrid password and smart card access to provide a backup login method, enforce strict card-only authentication, or configure automatic screen locking when the card is removed.

The `authselect`{.literal} command includes the following options for smart card configuration:

-   `with-smartcard`{.literal} --- enables smart card authentication in addition to password authentication
-   `with-smartcard-required`{.literal} --- enables smart card authentication and disables password authentication
-   `with-smartcard-lock-on-removal`{.literal} --- enforces automatic screen lock when the smart card is removed

**Prerequisites**

-   The smart card contains your certificate and private key.
-   The card is inserted into the reader and connected to the computer.

**Procedure**

1.  Choose one of the following configuration options based on your security requirements to enable smart card authentication:

    a.  Enable both smart card and password authentication:

        ``` {.language-plaintext tabindex="-1"}
        # authselect select sssd with-smartcard --force
        ```

        This configuration permits users to authenticate using either a smart card or a password, this ensures access continuity if the smart card is unavailable.

    b.  Enforce smart card authentication only:

        ``` {.language-plaintext tabindex="-1"}
        # authselect select sssd with-smartcard with-smartcard-required --force
        ```

        Important

        After running this command, users can no longer authenticate using their passwords. Ensure smart card authentication is functional before you apply this change, or the users might be locked out of their systems.

    c.  Enforce smart card authentication with automatic lock on removal:

        ``` {.language-plaintext tabindex="-1"}
        # authselect select sssd with-smartcard with-smartcard-required with-smartcard-lock-on-removal --force
        ```

        This configuration links the active session to the physical presence of the smart card. Removal of the token triggers an immediate screen lock that requires card re-insertion for access.

2.  Configure SSSD to enable smart card authentication by adding the following line to the `[pam]`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    [pam]
    pam_cert_auth = True
    ```

3.  Restart the SSSD service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

    Note

    Enabling `pam_cert_auth = True`{.literal} involves accessing and reading from the smart card, which might take multiple seconds.

### [7.3. Smart card authentication options in RHEL](#smart-card-authentication-options-in-rhel_configuring-smart-card-authentication-using-authselect) {#smart-card-authentication-options-in-rhel-1 .title}

The `authselect`{.literal} command configures system-wide authentication behaviors. You can enforce exclusive smart card usage, enabling hybrid password options, or trigger automatic session locking upon card removal to meet specific security policies.

You can configure how you want smart card authentication to work in a particular Identity Management (IdM) client by using the `authselect`{.literal} command, `authselect enable-feature `{.literal}*`<smartcard_option>`{.literal}*. The following smart card options are available:

-   `with-smartcard`{.literal}: Users can authenticate with the user name and password or with their smart card.

-   `with-smartcard-required`{.literal}: Users can authenticate with their smart cards, and password authentication is disabled. You cannot access the system without your smart card. Once you have authenticated with your smart card, you can stay logged in even if your smart card is removed from its reader.

    Note

    The `with-smartcard-required`{.literal} option only enforces exclusive smart card authentication for login services, such as `login`{.literal}, `gdm`{.literal}, `xdm`{.literal}, `xscreensaver`{.literal}, and `gnome-screensaver`{.literal}. For other services, such as `su`{.literal} or `sudo`{.literal} for switching users, smart card authentication is not enforced and if your smart card is not inserted, you are prompted for a password.

-   `with-smartcard-lock-on-removal`{.literal}: Users can authenticate with their smart card. However, if you remove your smart card from its reader, you are automatically locked out of the system. You cannot use password authentication.

    Note

    The `with-smartcard-lock-on-removal`{.literal} option only works on systems with the GNOME desktop environment. If you are using a system that is `tty`{.literal} or console based and you remove your smart card from its reader, you are not automatically locked out of the system.

**Additional resources**

-   [Configuring smart cards using authselect](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-smart-card-authentication-using-authselect)

### [7.4. Additional resources](#configuring-smart-card-authentication-using-authselect_74-additional-resources) {#additional-resources-2 .title}

-   [Configuring user authentication using authselect](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/configuring-user-authentication-using-authselect)
-   [Smart card support in RHEL](https://access.redhat.com/articles/4253861)

## [Chapter 8. Enabling authentication mechanism selection in GDM using SSSD](#authentication-mechanism-selection-in-gdm) {#chapter-8.-enabling-authentication-mechanism-selection-in-gdm-using-sssd .title}

Strengthen organizational security by enabling passwordless GDM authentication for managed users. Replace traditional password-based authentication with external identity providers (EIdP), passkey devices, or smart cards and switch between these methods on the GNOME Display Manager login screen.

Important

Passwordless GDM is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

### [8.1. Passwordless authentication for centrally managed users in GDM](#passwordless-authentication-for-centrally-managed-users-in-gdm) {#passwordless-authentication-for-centrally-managed-users-in-gdm .title}

Passwordless GDM authentication is a technology preview feature that provides several methods for logging in through the GNOME Display Manager (GDM) without a traditional password.

Depending on the system configuration, you can use the following authentication methods:

External identity providers (EIdP)
:   You can use providers such as Keycloak, Google, Microsoft, or GitHub for a unified login experience.

Passkey devices
:   You can use passwordless authentication using FIDO2-compatible devices like YubiKey.

Smart cards
:   You can use physical smart cards.

When the administrator configures multiple authentication methods for users, users can switch between these methods on the GDM login screen.

#### [8.1.1. Current limitations](#current_limitations) {#current-limitations .title}

When using these authentication methods, users might encounter the following behaviors:

EIdP priority over passkey
:   If an administrator configures both an EIdP and a passkey for a user, the IdM server, specifically the KDC, announces only the EIdP. Consequently, the GDM login screen displays only the EIdP option and does not show the passkey.

PIN prompts for passkey devices
:   GDM always prompts the user for a PIN when using a passkey, even if the passkey does not require one. In these cases, a touch is enough to authenticate. The PIN prompt ensures the user is ready to touch the device before the short authentication window expires. Additionally, the interface does not display the number of remaining PIN attempts.

Passkey availability in non-IdM environments
:   If the system is not enrolled in an IdM domain, SELinux security policies might prevent the passkey service from starting. In these environments, the passkey authentication method does not function and the option does not appear on the GDM login screen.

Smart card detection
:   The login option for smart cards only appears in the GDM menu when the user inserts a smart card that contains a valid certificate for their specific account into the reader.

**Additional resources**

-   [Supported smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/understanding-smart-card-authentication#supported-smart-cards)

### [8.2. Enabling authentication mechanism selection in GDM using SSSD](#enabling-authentication-mechanism-selection-in-gdm-using-sssd) {#enabling-authentication-mechanism-selection-in-gdm-using-sssd .title}

Enable credential switching in GNOME Display Manager (GDM) using System Security Services Daemon (SSSD) and authselect. Centrally managed users can then choose between passwordless login options, such as smart cards, passkeys, or external identity providers (EIdP), directly at the login screen.

Before enabling these options in GDM, you must first configure the individual authentication methods and the Identity Management (IdM) server. After these credentials and server-side settings are functional, you can configure the system services to display these options at the login screen.

**Prerequisites**

-   The system is a member of an Identity Management (IdM) domain.
-   You have fulfilled the prerequisites for the specific passwordless authentication methods you want to use, such as configuring the IdM server and enrolling user credentials.
-   You have `root`{.literal} privileges on the system.
-   Have SSSD installed.

**Procedure**

1.  (Optional): View the information about your `authselect`{.literal} profile:

    ``` {.language-plaintext tabindex="-1"}
    $ authselect current
    ```

2.  Depending on your current `authselect`{.literal} profile, do one of the following:

    a.  Select the `sssd`{.literal} profile and enable the switchable authentication feature:

        ``` {.language-plaintext tabindex="-1"}
        # authselect select sssd with-switchable-auth
        ```

    b.  If you are already using the `sssd`{.literal} profile, enable the switchable authentication feature:

        ``` {.language-plaintext tabindex="-1"}
        # authselect enable-feature with-switchable-auth
        ```

        Note

        This command configures the `/etc/pam.d/switchable-auth`{.literal} PAM service file to enable the GDM login screen to display the corresponding passwordless mechanisms that you have previously configured for the user account.

3.  Configure the SSSD PAM responder to authorize the switchable authentication service. Open the `/etc/sssd/sssd.conf`{.literal} file and add the `pam_json_services`{.literal} option to the `[pam]`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    ...
    [pam]
    pam_json_services = gdm-switchable-auth
    ```

4.  Restart the SSSD service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd
    ```

**Verification**

-   As an administrator, verify the `/etc/sssd/sssd.conf`{.literal} file to confirm the configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /etc/sssd/sssd.conf
    ```

    The output must include the `pam_json_services`{.literal} key set to `gdm-switchable-auth`{.literal} within the `[pam]`{.literal} section.

-   As a user, you can read the `/etc/dconf/db/distro.d/20-authselect`{.literal} file to confirm the configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /etc/dconf/db/distro.d/20-authselect
    ```

    The `[org/gnome/login-screen]`{.literal} section in the output must include the `enable-switchable-authentication`{.literal} key set to `true`{.literal}.

**Additional resources**

-   [Configuring Identity Management for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-server-for-smart-card-authentication)
-   [Configuring smart card authentication using authselect](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-smart-card-authentication-using-authselect)
-   [Enabling passkey authentication in IdM environment](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/enabling-passkey-authentication-in-idm-environment)
-   [Using external identity providers to authenticate to IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/using-external-identity-providers-to-authenticate-to-idm)

## [Chapter 9. Authenticating to sudo remotely using smart cards](#authenticating-to-sudo-remotely-using-smart-cards) {#chapter-9.-authenticating-to-sudo-remotely-using-smart-cards .title}

You can leverage local smart cards to authenticate remote sudo commands by using SSH agent forwarding. This configuration eliminates password prompts on the remote host by securely utilizing the credentials stored on the physically connected token.

You can authenticate to `sudo`{.literal} remotely using smart cards. After the `ssh-agent`{.literal} service is running locally and can forward the `ssh-agent`{.literal} socket to a remote machine, you can use the SSH authentication protocol in the `sudo`{.literal} PAM module to authenticate users remotely.

After logging in locally using a smart card, you can log in by using SSH to the remote machine and run the `sudo`{.literal} command without being prompted for a password by using SSH forwarding of the smart card authentication.

For the purposes of this example, a client is connecting to the IPA server by using SSH and running the `sudo`{.literal} command on the IPA server with credentials stored on a smart card.

### [9.1. Creating sudo rules in IdM](#creating-sudo-rules-in-idm) {#creating-sudo-rules-in-idm .title}

Administrators define specific IdM policies to authorize `sudo`{.literal} access on remote hosts. Create specific rules to bind restricted commands, such as `/usr/bin/less`{.literal}, to the target user and host for granular privilege control.

Create `sudo`{.literal} rules in IdM to give *`<idm_user>`{.literal}* permission to run `sudo`{.literal} on the remote host. For the purposes of this example, the `less`{.literal} and `whoami`{.literal} commands are added as `sudo`{.literal} commands to test the procedure.

**Prerequisites**

-   The IdM user has been created. For the purpose of this example, the user is *`<idm_user>`{.literal}*.
-   You have the hostname of the system where you are running `sudo`{.literal} remotely. For the purpose of this example, the host is `server.ipa.test`{.literal}.

**Procedure**

1.  Create a `sudo`{.literal} rule named *\<sudorule_name\>* to allow a user to run commands. Replace *\<sudorule_name\>* with the actual name of the sudo rule you want to create.

    ``` {.language-plaintext tabindex="-1"}
    # ipa sudorule-add <sudorule_name>
    ```

2.  Add `less`{.literal} and `whoami`{.literal} as `sudo`{.literal} commands:

    ``` {.language-plaintext tabindex="-1"}
    # ipa sudocmd-add /usr/bin/less
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ipa sudocmd-add /usr/bin/whoami
    ```

3.  Add the `less`{.literal} and `whoami`{.literal} commands to the *\<sudorule_name\>*:

    ``` {.language-plaintext tabindex="-1"}
    # ipa sudorule-add-allow-command <sudorule_name> --sudocmds /usr/bin/less
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ipa sudorule-add-allow-command <sudorule_name> --sudocmds /usr/bin/whoami
    ```

4.  Add the *`<idm_user>`{.literal}* user to the *\<sudorule_name\>*:

    ``` {.language-plaintext tabindex="-1"}
    # ipa sudorule-add-user <sudorule_name> --users <idm_user>
    ```

5.  Add the host on which you are running `sudo`{.literal} to the *\<sudorule_name\>*:

    ``` {.language-plaintext tabindex="-1"}
    # ipa sudorule-add-host <sudorule_name> --hosts server.ipa.test
    ```

### [9.2. Connecting to sudo remotely using a smart card](#connecting-to-sudo-remotely-using-a-smart-card) {#connecting-to-sudo-remotely-using-a-smart-card .title}

Initiating the connection requires loading the smart card into the local SSH agent and enabling agent forwarding. This configuration enables the remote system to verify the user's identity against the local smart card during privilege escalation attempts.

**Prerequisites**

-   You have created `sudo`{.literal} rules in IdM.
-   You have configured IdM to support passkey authentication using FIDO2 Yubikeys or PKINIT authentication using smart cards.
-   You have configured the `pam_sss_gss`{.literal} module for `sudo`{.literal} authentication on the remote system where you are going to run `sudo`{.literal}.

**Procedure**

1.  Start the SSH agent (if not already running).

    ``` {.language-plaintext tabindex="-1"}
    # eval `ssh-agent`
    ```

2.  Add your smart card to the SSH agent. Enter your PIN when prompted:

    ``` {.language-plaintext tabindex="-1"}
    # ssh-add -s /usr/lib64/opensc-pkcs11.so
    ```

3.  Connect to the system where you need to run `sudo`{.literal} remotely by using SSH with ssh-agent forwarding enabled. Use the `-A`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # ssh -A ipauser1@server.ipa.test
    ```

**Verification**

-   Run the `whoami`{.literal} command with `sudo`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # sudo /usr/bin/whoami
    ```

You are not prompted for a PIN or password when the smart card is inserted.

Note

If the SSH agent is configured to use other sources, such as the GNOME Keyring, and you run the `sudo`{.literal} command after removing the smart card, you might not be prompted for a PIN or password, as one of the other sources might provide access to a valid private key. To check the public keys of all identities known by the SSH agent, run the `ssh-add -L`{.literal} command.

**Additional resources**

-   [Using secure communications between two systems with OpenSSH](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/using-secure-communications-between-two-systems-with-openssh)
-   [Enabling passkey authentication in IdM environment](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/enabling-passkey-authentication-in-idm-environment)
-   [Granting sudo access to an IdM user on an IdM client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/granting-sudo-access-to-an-idm-user-on-an-idm-client#enabling-gssapi-authentication-and-enforcing-kerberos-authentication-indicators-for-sudo-on-an-idm-client)

## [Chapter 10. Authenticating as an Active Directory user using PKINIT with a smart card](#authenticating-as-an-active-directory-user-using-pkinit-with-a-smart-card) {#chapter-10.-authenticating-as-an-active-directory-user-using-pkinit-with-a-smart-card .title}

Active Directory (AD) users can use a smart card to authenticate to a desktop client system joined to IdM and obtain a Kerberos ticket-granting ticket (TGT) for single sign-on (SSO) authentication from the client. This process is intended for AD user accounts that require smart card authentication, which prevents them from using password-based logins.

Important

You cannot use these instructions to access IdM resources for which their Kerberos service has `pkinit`{.literal} authentication indicator requirement. This is because the process obtains a TGT from the Active Directory Kerberos Distribution Center (AD KDC), not the IdM KDC. As a result, the TGT does not contain the necessary authentication indicator, and the IdM service will deny your access.

To enable PKINIT authentication for IdM users to access IdM services see [Managing Kerberos ticket policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/managing-kerberos-ticket-policies).

**Prerequisites**

-   The IdM server is configured for smart card authentication. For more information, see [Configuring the IdM server for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-server-for-smart-card-authentication) or [Using Ansible to configure the IdM server for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#using-ansible-to-configure-the-idm-server-for-smart-card-authentication).
-   The client is configured for smart card authentication. For more information, see [Configuring the IdM client for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#configuring-the-idm-client-for-smart-card-authentication) or [Using Ansible to configure IdM clients for smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#using-ansible-to-configure-idm-clients-for-smart-card-authentication).
-   The `krb5-pkinit`{.literal} package is installed.
-   The AD server is configured to trust the certificate authority (CA) that issued the smart card certificate. Import the CA certificates into the NTAuth store (see [Microsoft support](https://learn.microsoft.com/en-US/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/import-third-party-ca-to-enterprise-ntauth-store)) and add the CA as a trusted CA. See Active Directory documentation for details.

**Procedure**

1.  Configure the Kerberos client to trust the CA that issued the smart card certificate:

    a.  On the IdM client, open the `/etc/krb5.conf`{.literal} file.

    b.  Add the following lines to the file:

        ``` {.language-plaintext tabindex="-1"}
        [realms]
          AD.DOMAIN.COM = {
            pkinit_eku_checking = kpServerAuth
            pkinit_kdc_hostname = adserver.ad.domain.com
          }
        ```

2.  If the user certificates do not contain a certificate revocation list (CRL) distribution point extension, configure AD to ignore revocation errors:

    a.  Save the following REG-formatted content in a plain text file and import it to the Windows registry:

        ``` {.language-plaintext tabindex="-1"}
        Windows Registry Editor Version 5.00

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Kdc]
        "UseCachedCRLOnlyAndIgnoreRevocationUnknownErrors"=dword:00000001

        [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\LSA\Kerberos\Parameters]
        "UseCachedCRLOnlyAndIgnoreRevocationUnknownErrors"=dword:00000001
        ```

        Alternatively, you can set the values manually by using the `regedit.exe`{.literal} application.

    b.  Reboot the Windows system to apply the changes.

3.  Authenticate by using the `kinit`{.literal} utility on an Identity Management client. Specify the Active Directory user with the user name and domain name:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit -X X509_user_identity='PKCS11:opensc-pkcs11.so' ad_user@AD.DOMAIN.COM
    ```

    The `-X`{.literal} option specifies the `opensc-pkcs11.so module`{.literal} as the pre-authentication attribute.

**Additional resources**

-   [MIT Kerberos Documentation](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html)

## [Chapter 11. Troubleshooting authentication with smart cards](#troubleshooting-authentication-with-smart-cards) {#chapter-11.-troubleshooting-authentication-with-smart-cards .title}

You can diagnose smart card failures by systematically validating hardware recognition, service status, and certificate validity to resolve common configuration issues to restore secure access.

### [11.1. Testing smart card access on the system](#testing-smart-card-access-on-the-system) {#testing-smart-card-access-on-the-system .title}

Verifying hardware connectivity is the first step in troubleshooting. Use system utilities such as `lsusb`{.literal} and `pkcs11-tool`{.literal} to confirm the reader is active and that the operating system can read the smart card's contents.

**Prerequisites**

-   You have installed and configured your IdM Server and client for use with smart cards.
-   You have installed the `certutil`{.literal} tool from the `nss-tools`{.literal} package.
-   You have the PIN or password for your smart card.

**Procedure**

1.  Using the `lsusb`{.literal} command, verify that the smart card reader is visible to the operating system:

    ``` {.language-plaintext tabindex="-1"}
    $ lsusb
    ```

    ``` {.language-plaintext tabindex="-1"}
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 003: ID 072f:b100 Advanced Card Systems, Ltd ACR39U
    Bus 001 Device 002: ID 0627:0001 Adomax Technology Co., Ltd
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    ```

    For more information about the smart cards and readers tested and supported in RHEL, see [Smart Card support in RHEL 10](https://access.redhat.com/articles/4253861).

2.  Ensure that the `pcscd`{.literal} service and socket are enabled and running:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl status pcscd.service pcscd.socket
    ```

    ``` {.language-plaintext tabindex="-1"}
    ● pcscd.service - PC/SC Smart Card Daemon
          Loaded: loaded (/usr/lib/systemd/system/pcscd.service; indirect;
    vendor preset: disabled)
          Active: active (running) since Fri 2021-09-24 11:05:04 CEST; 2
    weeks 6 days ago
    TriggeredBy: ● pcscd.socket
            Docs: man:pcscd(8)
        Main PID: 3772184 (pcscd)
           Tasks: 12 (limit: 38201)
          Memory: 8.2M
             CPU: 1min 8.067s
          CGroup: /system.slice/pcscd.service
                  └─3772184 /usr/sbin/pcscd --foreground --auto-exit

    ● pcscd.socket - PC/SC Smart Card Daemon Activation Socket
          Loaded: loaded (/usr/lib/systemd/system/pcscd.socket; enabled;
    vendor preset: enabled)
          Active: active (running) since Fri 2021-09-24 11:05:04 CEST; 2
    weeks 6 days ago
        Triggers: ● pcscd.service
          Listen: /run/pcscd/pcscd.comm (Stream)
          CGroup: /system.slice/pcscd.socket
    ```

3.  Using the `p11-kit list-modules`{.literal} command, display information about the configured smart card and the tokens present on the smart card:

    ``` {.language-plaintext tabindex="-1"}
    $ p11-kit list-modules
    ```

    ``` {.language-plaintext tabindex="-1"}
    p11-kit-trust: p11-kit-trust.so
    [...]
    opensc: opensc-pkcs11.so
        library-description: OpenSC smartcard framework
        library-manufacturer: OpenSC Project
        library-version: 0.20
        token: MyEID (sctest)
            manufacturer: Aventra Ltd.
            model: PKCS#15
            serial-number: 8185043840990797
            firmware-version: 40.1
            flags:
                   rng
                   login-required
                   user-pin-initialized
                   token-initialized
    ```

4.  Verify you can access the contents of your smart card:

    ``` {.language-plaintext tabindex="-1"}
    $ pkcs11-tool --list-objects --login
    ```

    ``` {.language-plaintext tabindex="-1"}
    Using slot 0 with a present token (0x0)
    Logging in to "MyEID (sctest)".
    Please enter User PIN:
    Private Key Object; RSA
      label:      Certificate
      ID:         01
      Usage:      sign
      Access:     sensitive
    Public Key Object; RSA 2048 bits
      label:      Public Key
      ID:         01
      Usage:      verify
      Access:     none
    Certificate Object; type = X.509 cert
      label:      Certificate
      subject:    DN: O=IDM.EXAMPLE.COM, CN=idmuser1
      ID:         01
    ```

5.  Display the contents of the certificate on your smart card using the `certutil`{.literal} command:

    a.  Run the following command to determine the correct name of your certificate:

        ``` {.language-plaintext tabindex="-1"}
        $ certutil -d /etc/pki/nssdb -L -h all
        ```

        ``` {.language-plaintext tabindex="-1"}
        Certificate Nickname                                         Trust Attributes
                                                                     SSL,S/MIME,JAR/XPI

        Enter Password or Pin for "MyEID (sctest)":
        Smart Card CA 0f5019a8-7e65-46a1-afe5-8e17c256ae00           CT,C,C
        MyEID (sctest):Certificate                                   u,u,u
        ```

    b.  Display the contents of the certificate on your smart card:

        Note

        Ensure the name of the certificate is an exact match for the output displayed in the previous step, in this example `MyEID (sctest):Certificate`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        $ certutil -d /etc/pki/nssdb -L -n "MyEID (sctest):Certificate"
        ```

        ``` {.language-plaintext tabindex="-1"}
        Enter Password or Pin for "MyEID (sctest)":
        Certificate:
            Data:
                Version: 3 (0x2)
                Serial Number: 15 (0xf)
                Signature Algorithm: PKCS #1 SHA-256 With RSA Encryption
                Issuer: "CN=Certificate Authority,O=IDM.EXAMPLE.COM"
                Validity:
                    Not Before: Thu Sep 30 14:01:41 2021
                    Not After : Sun Oct 01 14:01:41 2023
                Subject: "CN=idmuser1,O=IDM.EXAMPLE.COM"
                Subject Public Key Info:
                    Public Key Algorithm: PKCS #1 RSA Encryption
                    RSA Public Key:
                        Modulus:
                            [...]
                        Exponent: 65537 (0x10001)
                Signed Extensions:
                    Name: Certificate Authority Key Identifier
                    Key ID:
                        e2:27:56:0d:2f:f5:f2:72:ce:de:37:20:44:8f:18:7f:
                        2f:56:f9:1a

                    Name: Authority Information Access
                    Method: PKIX Online Certificate Status Protocol
                    Location:
                        URI: "http://ipa-ca.idm.example.com/ca/ocsp"

                    Name: Certificate Key Usage
                    Critical: True
                    Usages: Digital Signature
                            Non-Repudiation
                            Key Encipherment
                            Data Encipherment

                    Name: Extended Key Usage
                        TLS Web Server Authentication Certificate
                        TLS Web Client Authentication Certificate

                    Name: CRL Distribution Points
                    Distribution point:
                        URI: "http://ipa-ca.idm.example.com/ipa/crl/MasterCRL.bin"
                        CRL issuer:
                            Directory Name: "CN=Certificate Authority,O=ipaca"

                    Name: Certificate Subject Key ID
                    Data:
                        43:23:9f:c1:cf:b1:9f:51:18:be:05:b5:44:dc:e6:ab:
                        be:07:1f:36

            Signature Algorithm: PKCS #1 SHA-256 With RSA Encryption
            Signature:
                [...]
            Fingerprint (SHA-256):
                6A:F9:64:F7:F2:A2:B5:04:88:27:6E:B8:53:3E:44:3E:F5:75:85:91:34:ED:48:A8:0D:F0:31:5D:7B:C9:E0:EC
            Fingerprint (SHA1):
                B4:9A:59:9F:1C:A8:5D:0E:C1:A2:41:EC:FD:43:E0:80:5F:63:DF:29

            Mozilla-CA-Policy: false (attribute missing)
            Certificate Trust Flags:
                SSL Flags:
                    User
                Email Flags:
                    User
                Object Signing Flags:
                    User
        ```

### [11.2. Troubleshooting smart card authentication with SSSD](#troubleshooting-smart-card-authentication-with-sssd) {#troubleshooting-smart-card-authentication-with-sssd .title}

SSSD manages the authentication flow between the smart card and the identity provider. Administrators analyze SSSD logs and use `sssctl`{.literal} to diagnose failures in the `pam`{.literal} or `krb5`{.literal} child processes when login attempts fail.

**Prerequisites**

-   You have installed and configured your IdM Server and client for use with smart cards.
-   You have installed the `sssd-tools`{.literal} package.
-   You are able to detect your smart card reader and display the contents of your smart card. See [Testing smart card access on the system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/troubleshooting-authentication-with-smart-cards#testing-smart-card-access-on-the-system).

**Procedure**

1.  Verify you can authenticate with your smart card using `su`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ su - idmuser1 -c ‘su - idmuser1 -c whoami'
    ```

    ``` {.language-plaintext tabindex="-1"}
    PIN for MyEID (sctest):
    idmuser1
    ```

    If you are not prompted for the smart card PIN, and either a password prompt or an authorization error are returned, check the SSSD logs. See [Troubleshooting authentication with SSSD in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_authentication_and_authorization_in_rhel/index#troubleshooting-authentication-with-sssd-in-idm_configuring-authentication-and-authorization-in-rhel) for information about logging in SSSD. The following is an example of an authentication failure:

    ``` {.language-plaintext tabindex="-1"}
    $ su - idmuser1 -c ‘su - idmuser1 -c whoami'
    ```

    ``` {.language-plaintext tabindex="-1"}
    PIN for MyEID (sctest):
    su: Authentication failure
    ```

    If the SSSD logs indicate an issue from the `krb5_child`{.literal}, similar to the following, you may have an issue with your CA certificates. To troubleshoot issues with certificates, see [Verifying that IdM Kerberos KDC can use Pkinit and that the CA certificates are correctly located](#verifying-that-idm-kerberos-kdc-can-use-pkinit-and-that-the-ca-certificates-are-correctly-located "11.3. Verifying that IdM Kerberos KDC can use PKINIT and that the CA certificates are correctly located").

    ``` {.language-plaintext tabindex="-1"}
    [Pre-authentication failed: Failed to verify own certificate (depth 0): unable to get local issuer certificate: could not load the shared library]
    ```

    If the SSSD logs indicate a timeout either from `p11_child`{.literal} or `krb5_child`{.literal}, you may need to increase the SSSD timeouts and try authenticating again with your smart card. See [Increasing SSSD timeouts](#increasing-sssd-timeouts "11.4. Increasing SSSD timeouts") for details on how to increase the timeouts.

2.  Verify your GDM smart card authentication configuration is correct. A success message for PAM authentication should be returned as shown below:

    ``` {.language-plaintext tabindex="-1"}
    # sssctl user-checks -s gdm-smartcard "idmuser1" -a auth
    ```

    ``` {.language-plaintext tabindex="-1"}
    user: idmuser1
    action: auth
    service: gdm-smartcard

    SSSD nss user lookup result:
     - user name: idmuser1
     - user id: 603200210
     - group id: 603200210
     - gecos: idm user1
     - home directory: /home/idmuser1
     - shell: /bin/sh

    SSSD InfoPipe user lookup result:
     - name: idmuser1
     - uidNumber: 603200210
     - gidNumber: 603200210
     - gecos: idm user1
     - homeDirectory: /home/idmuser1
     - loginShell: /bin/sh

    testing pam_authenticate

    PIN for MyEID (sctest)
    pam_authenticate for user [idmuser1]: Success

    PAM Environment:
     - PKCS11_LOGIN_TOKEN_NAME=MyEID (sctest)
     - KRB5CCNAME=KCM:
    ```

    If an authentication error, similar to the following, is returned, check the SSSD logs to try and determine what is causing the issue. See [Troubleshooting authentication with SSSD in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_authentication_and_authorization_in_rhel/troubleshooting-authentication-with-sssd-in-idm) for information about logging in SSSD.

    ``` {.language-plaintext tabindex="-1"}
    pam_authenticate for user [idmuser1]: Authentication failure

    PAM Environment:
     - no env -
    ```

    If PAM authentication continues to fail, clear your cache and run the command again.

    ``` {.language-plaintext tabindex="-1"}
    # sssctl cache-remove
    ```

    ``` {.language-plaintext tabindex="-1"}
    SSSD must not be running. Stop SSSD now? (yes/no) [yes] yes
    Creating backup of local data…
    Removing cache files…
    SSSD needs to be running. Start SSSD now? (yes/no) [yes] yes
    ```

### [11.3. Verifying that IdM Kerberos KDC can use PKINIT and that the CA certificates are correctly located](#verifying-that-idm-kerberos-kdc-can-use-pkinit-and-that-the-ca-certificates-are-correctly-located) {#verifying-that-idm-kerberos-kdc-can-use-pkinit-and-that-the-ca-certificates-are-correctly-located .title}

Successful PKINIT authentication relies on a valid certificate chain. You can use `kinit`{.literal} and `openssl`{.literal} to verify that the client trusts the Certificate Authority and that the smart card certificate is valid for Kerberos ticket retrieval.

**Prerequisites**

-   You have installed and configured your IdM Server and client for use with smart cards.
-   You are able to detect your smart card reader and display the contents of your smart card. See [Testing smart card access on the system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/troubleshooting-authentication-with-smart-cards#testing-smart-card-access-on-the-system).

**Procedure**

1.  Run the `kinit`{.literal} utility to authenticate as the `idmuser1`{.literal} with the certificate stored on your smart card:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit -X X509_user_identity=PKCS11: idmuser1
    ```

    ``` {.language-plaintext tabindex="-1"}
    MyEID (sctest)                   PIN:
    ```

2.  Enter your smart card PIN. If you are not prompted for your PIN, check that you can detect your smart card reader and display the contents of your smart card. See link:https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/troubleshooting-authentication-with-smart-cards#testing-smart-card-access-on-the-system

3.  If your PIN is accepted and you are then prompted for your password, you might be missing your CA signing certificate.

    a.  Verify the CA chain is listed in the default certificate bundle file using `openssl`{.literal} commands:

        ``` {.language-plaintext tabindex="-1"}
        $ openssl crl2pkcs7 -nocrl -certfile /var/lib/ipa-client/pki/ca-bundle.pem | openssl pkcs7 -print_certs -noout
        ```

        ``` {.language-plaintext tabindex="-1"}
        subject=O = IDM.EXAMPLE.COM, CN = Certificate Authority

        issuer=O = IDM.EXAMPLE.COM, CN = Certificate Authority
        ```

    b.  Verify the validity of your certificates:

        i.  Find the user authentication certificate ID for `idmuser1`{.literal}:

            ``` {.language-plaintext tabindex="-1"}
            $ pkcs11-tool --list-objects --login
            ```

            ``` {.language-plaintext tabindex="-1"}
            [...]
            Certificate Object; type = X.509 cert
              label:      Certificate
              subject:    DN: O=IDM.EXAMPLE.COM, CN=idmuser1
             ID: 01
            ```

        ii. Read the user certificate information from the smart card in DER format:

            ``` {.language-plaintext tabindex="-1"}
            $ pkcs11-tool --read-object --id 01 --type cert --output-file cert.der
            ```

            ``` {.language-plaintext tabindex="-1"}
            Using slot 0 with a present token (0x0)
            ```

        iii. Convert the DER certificate to PEM format:

             ``` {.language-plaintext tabindex="-1"}
             $ openssl x509 -in cert.der -inform DER -out cert.pem -outform PEM
             ```

        iv. Verify the certificate has valid issuer signatures up to the CA:

            ``` {.language-plaintext tabindex="-1"}
            $ openssl verify -CAfile /var/lib/ipa-client/pki/ca-bundle.pem <path>/cert.pem
            cert.pem: OK
            ```

4.  If your smart card contains several certificates, `kinit`{.literal} might fail to choose the correct certificate for authentication. In this case, you need to specify the certificate ID as an argument to the `kinit`{.literal} command using the `certid=<ID>`{.literal} option.

    a.  Check how many certificates are stored on the smart card and get the certificate ID for the one you are using:

        ``` {.language-plaintext tabindex="-1"}
        $ pkcs11-tool --list-objects --type cert --login
        ```

        ``` {.language-plaintext tabindex="-1"}
        Using slot 0 with a present token (0x0)
        Logging in to "MyEID (sctest)".
        Please enter User PIN:
        Certificate Object; type = X.509 cert
          label:      Certificate
          subject:    DN: O=IDM.EXAMPLE.COM, CN=idmuser1
          ID:         01
        Certificate Object; type = X.509 cert
          label:      Second certificate
          subject:    DN: O=IDM.EXAMPLE.COM, CN=ipauser1
          ID:         02
        ```

    b.  Run `kinit`{.literal} with certificate ID 01:

        ``` {.language-plaintext tabindex="-1"}
        $ kinit -X kinit -X X509_user_identity=PKCS11:certid=01 idmuser1
        ```

        ``` {.language-plaintext tabindex="-1"}
        MyEID (sctest)                   PIN:
        ```

5.  Run `klist`{.literal} to view the contents of the Kerberos credentials cache:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    ```

    ``` {.language-plaintext tabindex="-1"}
    Ticket cache: KCM:0:11485
    Default principal: idmuser1@EXAMPLE.COM

    Valid starting       Expires              Service principal
    10/04/2021 10:50:04  10/05/2021 10:49:55  krbtgt/EXAMPLE.COM@EXAMPLE.COM
    ```

6.  Destroy your active Kerberos tickets once you have finished:

    ``` {.language-plaintext tabindex="-1"}
    $ kdestroy -A
    ```

### [11.4. Increasing SSSD timeouts](#increasing-sssd-timeouts) {#increasing-sssd-timeouts .title}

Hardware latency or complex certificate chains can cause SSSD operations to time out. Administrators extend the `krb5_auth_timeout`{.literal} and `p11_child_timeout`{.literal} settings in `sssd.conf`{.literal} to enable sufficient time for smart card processing.

``` {.language-plaintext tabindex="-1"}
krb5_child: Timeout for child [9607] reached.....consider increasing value of krb5_auth_timeout.
```

If there is a timeout entry in the log file, try increasing the SSSD timeouts as outlined in this procedure.

**Prerequisites**

-   You have configured your IdM Server and client for smart card authentication.

**Procedure**

1.  Open the `sssd.conf`{.literal} file on the IdM client:

    ``` {.language-plaintext tabindex="-1"}
    # vim /etc/sssd/sssd.conf
    ```

2.  In your domain section, for example `[domain/idm.example.com]`{.literal}, add the following option:

    ``` {.language-plaintext tabindex="-1"}
    krb5_auth_timeout = 60
    ```

3.  In the `[pam]`{.literal} section, add the following:

    ``` {.language-plaintext tabindex="-1"}
    p11_child_timeout = 60
    ```

4.  Clear the SSSD cache:

    ``` {.language-plaintext tabindex="-1"}
    # sssctl cache-remove
    ```

    ``` {.language-plaintext tabindex="-1"}
    SSSD must not be running. Stop SSSD now? (yes/no) [yes] yes
    Creating backup of local data…
    Removing cache files…
    SSSD needs to be running. Start SSSD now? (yes/no) [yes] yes
    ```

    Once you have increased the timeouts, try authenticating again using your smart card. See [Testing smart card authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/troubleshooting-authentication-with-smart-cards#testing-smart-card-access-on-the-system) for more details.

## [Legal Notice](#idm139860719719280) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
