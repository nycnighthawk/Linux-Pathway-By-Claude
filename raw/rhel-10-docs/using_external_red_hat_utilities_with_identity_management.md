---
{"title": "Using external Red Hat utilities with Identity Management", "guide": "using_external_red_hat_utilities_with_identity_management", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_external_red_hat_utilities_with_identity_management/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Using external Red Hat utilities with Identity Management {#using-external-red-hat-utilities-with-identity-management .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Integrating services and Red Hat products in IdM {#integrating-services-and-red-hat-products-in-idm .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140339881612368)

**Abstract**

Administrators can integrate services and Red Hat products in a Red Hat Enterprise Linux Identity Management (IdM) domain. This includes services, such as Samba, Ansible, and automount, and also products, such as OpenShift Container Platform, OpenStack, and Satellite. IdM users can then access these services and products.

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

## [Chapter 1. IdM integration with Red Hat products](#idm-integration-with-red-hat-products) {#chapter-1.-idm-integration-with-red-hat-products .title}

Find documentation for other Red Hat products that integrate with IdM. You can configure these products to grant your IdM users access to their services.

-   [Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform)
-   [OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform)
-   [Red Hat OpenStack Platform](https://docs.redhat.com/en/documentation/red_hat_openstack_platform)
-   [Red Hat Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite)
-   [Red Hat Single Sign-On](https://docs.redhat.com/en/documentation/red_hat_single_sign-on)
-   [Red Hat Virtualization](https://docs.redhat.com/en/documentation/red_hat_virtualization)

## [Chapter 2. Using external identity providers to authenticate to IdM](#using-external-identity-providers-to-authenticate-to-idm) {#chapter-2.-using-external-identity-providers-to-authenticate-to-idm .title}

You can associate users with external identity providers (IdP) that support the OAuth 2 device authorization flow.

When these users authenticate with the SSSD they receive RHEL Identity Management (IdM) single sign-on capabilities with Kerberos tickets after performing authentication and authorization at the external IdP.

Notable features include:

-   Adding, modifying, and deleting references to external IdPs with `ipa idp-*`{.literal} commands.

-   Enabling IdP authentication for users with the `ipa user-mod --user-auth-type=idp`{.literal} command.

    What is supported

    :   

-   Logging in remotely via SSH with the `keyboard-interactive`{.literal} authentication method enabled, which allows calling Pluggable Authentication Module (PAM) libraries.

-   Logging in locally with the console through the `logind`{.literal} service.

-   Retrieving a Kerberos ticket-granting ticket (TGT) with the `kinit`{.literal} utility.

    What is currently not supported

    :   

-   Logging in to the IdM WebUI directly. To log in to the IdM WebUI, you must first acquire a Kerberos ticket.

-   Logging in to Cockpit WebUI directly. To log in to the Cockpit WebUI, you must first acquire a Kerberos ticket.

### [2.1. The benefits of connecting IdM to an external IdP](#the-benefits-of-connecting-idm-to-an-external-idp) {#the-benefits-of-connecting-idm-to-an-external-idp .title}

You can delegate Kerberos ticket issuance to an external identity provider (IdP) so that users from external sources, such as cloud services, can access RHEL systems in your Identity Management (IdM) environment.

You can use this feature to expand IdM's capabilities and allow users stored in external identity providers (IdPs) to access Linux systems managed by IdM.

### [2.2. How IdM incorporates logins via external IdPs](#how-idm-incorporates-logins-via-external-idps) {#how-idm-incorporates-logins-via-external-idps .title}

SSSD 2.7.0 contains the `sssd-idp`{.literal} package, which implements the `idp`{.literal} Kerberos pre-authentication method. This authentication method follows the OAuth 2.0 Device Authorization Grant flow to delegate authorization decisions to external IdPs:

1.  An IdM client user initiates OAuth 2.0 Device Authorization Grant flow, for example, by attempting to retrieve a Kerberos TGT with the `kinit`{.literal} utility at the command line.

2.  A special code and website link are sent from the Authorization Server to the IdM KDC backend.

3.  The IdM client displays the link and the code to the user. In this example, the IdM client outputs the link and code on the command line.

4.  The user opens the website link in a browser, which can be on another host, a mobile phone, and so on:

    a.  The user enters the special code.
    b.  If necessary, the user logs in to the OAuth 2.0-based IdP.
    c.  The user is prompted to authorize the client to access information.

5.  The user confirms access at the original device prompt. In this example, the user hits the Enter key at the command line.

6.  The IdM KDC backend polls the OAuth 2.0 Authorization Server for access to user information.

**Additional resources**

-   [Authentication against external identity providers](https://freeipa.readthedocs.io/en/latest/workshop/12-external-idp-support.html)
-   [RFC 8628: OAuth 2.0 Device Authorization Grant](https://www.rfc-editor.org/rfc/rfc8628)

### [2.3. Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider) {#creating-a-reference-to-an-external-identity-provider .title}

You can create IdP references in IdM to connect external identity providers (IdPs) to your Identity Management (IdM) environment. You can create a reference called **my-keycloak-idp** to an IdP based on the Keycloak template. For more reference templates, see [Example references to different external IdPs in IdM](#example-references-to-different-external-idps-in-idm "2.4. Example references to different external IdPs in IdM").

**Prerequisites**

-   You have registered IdM as an OAuth application to your external IdP, and obtained a client ID.
-   You can authenticate as the IdM admin account.

**Procedure**

1.  Authenticate as the IdM admin on an IdM server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit admin
    ```

2.  Create a reference called `my-keycloak-idp`{.literal} to an IdP based on the Keycloak template, where the `--base-url`{.literal} option specifies the URL to the Keycloak server in the format `server-name.$DOMAIN:$PORT/prefix`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idp-add my-keycloak-idp \
                     --provider keycloak --organization main \
                     --base-url keycloak.idm.example.com:8443/auth \
                     --client-id id13778
    ------------------------------------------------
    Added Identity Provider reference "my-keycloak-idp"
    ------------------------------------------------
      Identity Provider reference name: my-keycloak-idp
      Authorization URI: https://keycloak.idm.example.com:8443/auth/realms/main/protocol/openid-connect/auth
      Device authorization URI: https://keycloak.idm.example.com:8443/auth/realms/main/protocol/openid-connect/auth/device
      Token URI: https://keycloak.idm.example.com:8443/auth/realms/main/protocol/openid-connect/token
      User info URI: https://keycloak.idm.example.com:8443/auth/realms/main/protocol/openid-connect/userinfo
      Client identifier: ipa_oidc_client
      Scope: openid email
      External IdP user identifier attribute: email
    ```

**Verification**

-   Verify that the output of the `ipa idp-show`{.literal} command shows the IdP reference you have created.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa idp-show my-keycloak-idp
    ```

**Additional resources**

-   [Example references to different external IdPs in IdM](#example-references-to-different-external-idps-in-idm "2.4. Example references to different external IdPs in IdM")
-   [Options for the ipa idp-\* commands to manage external identity providers in IdM](#options-for-the-ipa-idp-commands-to-manage-external-identity-providers-in-idm "2.5. Options for the ipa idp-* commands to manage external identity providers in IdM")
-   [The \--provider option in the ipa idp-\* commands](#the-provider-option-in-the-ipa-idp-commands "2.10. The --provider option in the ipa idp-* commands")

### [2.4. Example references to different external IdPs in IdM](#example-references-to-different-external-idps-in-idm) {#example-references-to-different-external-idps-in-idm .title}

The following table lists examples of the `ipa idp-add`{.literal} command for creating references to different IdPs in IdM.

+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Identity provider                               | Important options                | Command example                                                                                                                                                                                                                               |
+:================================================+:=================================+:==============================================================================================================================================================================================================================================+
| Microsoft Identity Platform, Microsoft Entra ID | `--provider microsoft`{.literal} | `# ipa idp-add my-entra-id-idp \ --provider microsoft \ --organization main \ --client-id <entra_client_id>`{.literallayout}                                                                                                                  |
|                                                 |                                  |                                                                                                                                                                                                                                               |
|                                                 | `--organization`{.literal}       |                                                                                                                                                                                                                                               |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Google                                          | `--provider google`{.literal}    | `# ipa idp-add my-google-idp \ --provider google \ --client-id <google_client_id>`{.literallayout}                                                                                                                                            |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GitHub                                          | `--provider github`{.literal}    | `# ipa idp-add my-github-idp \ --provider github \ --client-id <github_client_id>`{.literallayout}                                                                                                                                            |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Keycloak, Red Hat Single Sign-On                | `--provider keycloak`{.literal}  | `# ipa idp-add my-keycloak-idp \ --provider keycloak \ --organization main \ --base-url keycloak.idm.example.com:8443/auth \ --client-id <keycloak_client_id>`{.literallayout}                                                                |
|                                                 |                                  |                                                                                                                                                                                                                                               |
|                                                 | `--organization`{.literal}       | Note                                                                                                                                                                                                                                          |
|                                                 |                                  |                                                                                                                                                                                                                                               |
|                                                 | `--base-url`{.literal}           | The Quarkus version of Keycloak 17 and later have removed the `/auth/`{.literal} portion of the URI. If you use the non-Quarkus distribution of Keycloak in your deployment, include `/auth/`{.literal} in the `--base-url`{.literal} option. |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Okta                                            | `--provider okta`{.literal}      | `# ipa idp-add my-okta-idp \ --provider okta --base-url dev-12345.okta.com \ --client-id <okta_client_id>`{.literallayout}                                                                                                                    |
+-------------------------------------------------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

**Additional resources**

-   [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "2.3. Creating a reference to an external identity provider")
-   [Options for the ipa idp-\* commands to manage external identity providers in IdM](#options-for-the-ipa-idp-commands-to-manage-external-identity-providers-in-idm "2.5. Options for the ipa idp-* commands to manage external identity providers in IdM")
-   [The \--provider option in the ipa idp-\* commands](#the-provider-option-in-the-ipa-idp-commands "2.10. The --provider option in the ipa idp-* commands")
-   [Configure IdM to use Google as external IdP (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7073951)
-   [Configure IdM to use Microsoft Entra ID as external IdP (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7073948)
-   [Configure IdM to use GitHub as external IdP (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7072954)

### [2.5. Options for the ipa idp-\* commands to manage external identity providers in IdM](#options-for-the-ipa-idp-commands-to-manage-external-identity-providers-in-idm) {#options-for-the-ipa-idp--commands-to-manage-external-identity-providers-in-idm .title}

The following examples show how to configure references to external IdPs based on the different IdP templates. Use the following options to specify your settings:

`--provider`{.literal}
:   the predefined template for one of the known identity providers

`--client-id`{.literal}
:   the OAuth 2.0 client identifier issued by the IdP during application registration. As the application registration procedure is specific to each IdP, refer to their documentation for details. If the external IdP is Red Hat Single Sign-On (SSO), see [Creating an OpenID Connect Client](https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html-single/server_administration_guide/index#proc-creating-oidc-client_server_administration_guide).

`--base-url`{.literal}
:   base URL for IdP templates, required by Keycloak and Okta

`--organization`{.literal}
:   Domain or Organization ID from the IdP, required by Microsoft Entra ID

`--secret`{.literal}
:   *(optional)* Use this option if you have configured your external IdP to require a secret from confidential OAuth 2.0 clients. If you use this option when creating an IdP reference, you are prompted for the secret interactively. Protect the client secret as a password.

**Additional resources**

-   [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "2.3. Creating a reference to an external identity provider")
-   [Example references to different external IdPs in IdM](#example-references-to-different-external-idps-in-idm "2.4. Example references to different external IdPs in IdM")
-   [The \--provider option in the ipa idp-\* commands](#the-provider-option-in-the-ipa-idp-commands "2.10. The --provider option in the ipa idp-* commands")

### [2.6. Managing references to external IdPs](#managing-references-to-external-idps) {#managing-references-to-external-idps .title}

After you create a reference to an external identity provider (IdP), you can find, show, modify, and delete that reference. This example shows you how to manage a reference to an external IdP named `keycloak-server1`{.literal}.

**Prerequisites**

-   You can authenticate as the IdM admin account.
-   You have created a reference to an external IdP in IdM. See [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "2.3. Creating a reference to an external identity provider").

**Procedure**

1.  Authenticate as the IdM admin on an IdM server.

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# kinit admin
    ```

2.  Manage the IdP reference.

    -   To find an IdP reference whose entry includes the string `keycloak`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idp-find keycloak
        ```

    -   To display an IdP reference named `my-keycloak-idp`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idp-show my-keycloak-idp
        ```

    -   To modify an IdP reference, use the `ipa idp-mod`{.literal} command. For example, to change the secret for an IdP reference named `my-keycloak-idp`{.literal}, specify the `--secret`{.literal} option to be prompted for the secret:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idp-mod my-keycloak-idp --secret
        ```

    -   To delete an IdP reference named `my-keycloak-idp`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        [root@server ~]# ipa idp-del my-keycloak-idp
        ```

### [2.7. Enabling an IdM user to authenticate via an external IdP](#enabling-an-idm-user-to-authenticate-via-an-external-idp) {#enabling-an-idm-user-to-authenticate-via-an-external-idp .title}

To enable an IdM user to authenticate via an external identity provider (IdP), associate the external IdP reference you have previously created with the user account. This example associates the external IdP reference `keycloak-server1`{.literal} with the user `idm-user-with-external-idp`{.literal}.

**Prerequisites**

-   You have created a reference to an external IdP in IdM. See [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "2.3. Creating a reference to an external identity provider").

**Procedure**

-   Modify the IdM user entry to associate an IdP reference with the user account:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa user-mod idm-user-with-external-idp \
                   --idp my-keycloak-idp \
                   --idp-user-id idm-user-with-external-idp@idm.example.com \
                   --user-auth-type=idp
    ---------------------------------
    Modified user "idm-user-with-external-idp"
    ---------------------------------
      User login: idm-user-with-external-idp
      First name: Test
      Last name: User1
      Home directory: /home/idm-user-with-external-idp
      Login shell: /bin/sh
      Principal name: idm-user-with-external-idp@idm.example.com
      Principal alias: idm-user-with-external-idp@idm.example.com
      Email address: idm-user-with-external-idp@idm.example.com
      UID: 35000003
      GID: 35000003
      User authentication types: idp
      External IdP configuration: keycloak
      External IdP user identifier: idm-user-with-external-idp@idm.example.com
      Account disabled: False
      Password: False
      Member of groups: ipausers
      Kerberos keys available: False
    ```

**Verification**

-   Verify that the output of the `ipa user-show`{.literal} command for that user displays references to the IdP:

    ``` {.language-plaintext tabindex="-1"}
    [root@server ~]# ipa user-show idm-user-with-external-idp
      User login: idm-user-with-external-idp
      First name: Test
      Last name: User1
      Home directory: /home/idm-user-with-external-idp
      Login shell: /bin/sh
      Principal name: idm-user-with-external-idp@idm.example.com
      Principal alias: idm-user-with-external-idp@idm.example.com
      Email address: idm-user-with-external-idp@idm.example.com
      ID: 35000003
      GID: 35000003
      User authentication types: idp
      External IdP configuration: keycloak
      External IdP user identifier: idm-user-with-external-idp@idm.example.com
      Account disabled: False
      Password: False
      Member of groups: ipausers
      Kerberos keys available: False
    ```

### [2.8. Retrieving an IdM ticket-granting ticket as an external IdP user](#retrieving-an-idm-ticket-granting-ticket-as-an-external-idp-user) {#retrieving-an-idm-ticket-granting-ticket-as-an-external-idp-user .title}

If you have delegated authentication for an Identity Management (IdM) user to an external identity provider (IdP), the IdM user can request a Kerberos ticket-granting ticket (TGT) by authenticating to the external IdP.

Complete this procedure to:

1.  Retrieve and store an anonymous Kerberos ticket locally.
2.  Request the TGT for the **idm-user-with-external-idp** user by using `kinit`{.literal} with the `-T`{.literal} option to enable Flexible Authentication via Secure Tunneling (FAST) channel to provide a secure connection between the Kerberos client and Kerberos Distribution Center (KDC).

**Prerequisites**

-   You have created a reference to an external IdP in IdM. See [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "2.3. Creating a reference to an external identity provider").
-   You have associated an external IdP reference with the user account. See [Enabling an IdM user to authenticate via an external IdP](#enabling-an-idm-user-to-authenticate-via-an-external-idp "2.7. Enabling an IdM user to authenticate via an external IdP").
-   The user that you are initially logged in as has write permissions on a directory in the local filesystem.

**Procedure**

1.  Use Anonymous PKINIT to obtain a Kerberos ticket and store it in a file named `./fast.ccache`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ kinit -n -c ./fast.ccache
    ```

2.  Optional: View the retrieved ticket:

    ``` {.language-plaintext tabindex="-1"}
    $ klist -c fast.ccache
    Ticket cache: FILE:fast.ccache
    Default principal: WELLKNOWN/ANONYMOUS@WELLKNOWN:ANONYMOUS

    Valid starting       Expires              Service principal
    03/03/2024 13:36:37  03/04/2024 13:14:28  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    ```

3.  Begin authenticating as the IdM user, using the `-T`{.literal} option to enable the FAST communication channel.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# kinit -T ./fast.ccache idm-user-with-external-idp
    Authenticate at https://oauth2.idp.com:8443/auth/realms/master/device?user_code=YHMQ-XKTL and press ENTER.:
    ```

4.  In a browser, authenticate as the user at the website provided in the command output.

5.  At the command line, press the Enter key to finish the authentication process.

**Verification**

-   Display your Kerberos ticket information and confirm that the line `config: pa_type`{.literal} shows `152`{.literal} for pre-authentication with an external IdP.

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# klist -C
    Ticket cache: KCM:0:58420
    Default principal: idm-user-with-external-idp@IDM.EXAMPLE.COM

    Valid starting     Expires            Service principal
    05/09/22 07:48:23  05/10/22 07:03:07  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: fast_avail(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = yes
    08/17/2022 20:22:45  08/18/2022 20:22:43  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: pa_type(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = 152
    ```

    The `pa_type = 152`{.literal} indicates external IdP authentication.

### [2.9. Logging in to an IdM client via SSH as an external IdP user](#logging-in-to-an-idm-client-via-ssh-as-an-external-idp-user) {#logging-in-to-an-idm-client-via-ssh-as-an-external-idp-user .title}

To log in to an IdM client by using SSH as an external identity provider (IdP) user, begin the login process on the command line. When prompted, authenticate at the website associated with the IdP, and finish the process at the Identity Management (IdM) client.

**Prerequisites**

-   You have created a reference to an external IdP in IdM. See [Creating a reference to an external identity provider](#creating-a-reference-to-an-external-identity-provider "2.3. Creating a reference to an external identity provider").
-   You have associated an external IdP reference with the user account. See [Enabling an IdM user to authenticate via an external IdP](#enabling-an-idm-user-to-authenticate-via-an-external-idp "2.7. Enabling an IdM user to authenticate via an external IdP").

**Procedure**

1.  Attempt to log in to the IdM client via SSH.

    ``` {.language-plaintext tabindex="-1"}
    [user@client ~]$ ssh idm-user-with-external-idp@client.idm.example.com
    (idm-user-with-external-idp@client.idm.example.com) Authenticate at https://oauth2.idp.com:8443/auth/realms/main/device?user_code=XYFL-ROYR and press ENTER.
    ```

2.  In a browser, authenticate as the user at the website provided in the command output.

3.  At the command line, press the Enter key to finish the authentication process.

**Verification**

-   Display your Kerberos ticket information and confirm that the line `config: pa_type`{.literal} shows `152`{.literal} for pre-authentication with an external IdP.

    ``` {.language-plaintext tabindex="-1"}
    [idm-user-with-external-idp@client ~]$ klist -C
    Ticket cache: KCM:0:58420
    Default principal: idm-user-with-external-idp@IDM.EXAMPLE.COM

    Valid starting     Expires            Service principal
    05/09/22 07:48:23  05/10/22 07:03:07  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: fast_avail(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = yes
    08/17/2022 20:22:45  08/18/2022 20:22:43  krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM
    config: pa_type(krbtgt/IDM.EXAMPLE.COM@IDM.EXAMPLE.COM) = 152
    ```

### [2.10. The \--provider option in the ipa idp-\* commands](#the-provider-option-in-the-ipa-idp-commands) {#the---provider-option-in-the-ipa-idp--commands .title}

The following identity providers (IdPs) support OAuth 2.0 device authorization grant flow:

-   Microsoft Identity Platform, Microsoft Entra ID
-   Google
-   GitHub
-   Keycloak, including Red Hat Single Sign-On (SSO)
-   Okta

When using the `ipa idp-add`{.literal} command to create a reference to one of these external IdPs, you can specify the IdP type with the `--provider`{.literal} option, which expands into additional options as described below:

`--provider=microsoft`{.literal}

:   Microsoft Entra ID IdPs allow parametrization based on the Microsoft Entra ID tenant ID, which you can specify with the `--organization`{.literal} option to the `ipa idp-add`{.literal} command. If you need support for the live.com IdP, specify the option `--organization common`{.literal}.

    Choosing `--provider=microsoft`{.literal} expands to use the following options. The value of the `--organization`{.literal} option replaces the string `${ipaidporg}`{.literal} in the table.

    +--------------------------------+-----------------------------------------------------------------------------------+
    | Option                         | Value                                                                             |
    +:===============================+:==================================================================================+
    | `--auth-uri=URI`{.literal}     | `https://login.microsoftonline.com/${ipaidporg}/oauth2/v2.0/authorize`{.literal}  |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://login.microsoftonline.com/${ipaidporg}/oauth2/v2.0/devicecode`{.literal} |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://login.microsoftonline.com/${ipaidporg}/oauth2/v2.0/token`{.literal}      |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://graph.microsoft.com/oidc/userinfo`{.literal}                             |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--keys-uri=URI`{.literal}     | `https://login.microsoftonline.com/common/discovery/v2.0/keys`{.literal}          |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `openid email`{.literal}                                                          |
    +--------------------------------+-----------------------------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `email`{.literal}                                                                 |
    +--------------------------------+-----------------------------------------------------------------------------------+

    Show more

`--provider=google`{.literal}

:   Choosing `--provider=google`{.literal} expands to use the following options:

    +--------------------------------+--------------------------------------------------------------+
    | Option                         | Value                                                        |
    +:===============================+:=============================================================+
    | `--auth-uri=URI`{.literal}     | `https://accounts.google.com/o/oauth2/auth`{.literal}        |
    +--------------------------------+--------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://oauth2.googleapis.com/device/code`{.literal}        |
    +--------------------------------+--------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://oauth2.googleapis.com/token`{.literal}              |
    +--------------------------------+--------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://openidconnect.googleapis.com/v1/userinfo`{.literal} |
    +--------------------------------+--------------------------------------------------------------+
    | `--keys-uri=URI`{.literal}     | `https://www.googleapis.com/oauth2/v3/certs`{.literal}       |
    +--------------------------------+--------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `openid email`{.literal}                                     |
    +--------------------------------+--------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `email`{.literal}                                            |
    +--------------------------------+--------------------------------------------------------------+

    Show more

`--provider=github`{.literal}

:   Choosing `--provider=github`{.literal} expands to use the following options:

    +--------------------------------+--------------------------------------------------------------+
    | Option                         | Value                                                        |
    +:===============================+:=============================================================+
    | `--auth-uri=URI`{.literal}     | `https://github.com/login/oauth/authorize`{.literal}         |
    +--------------------------------+--------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://github.com/login/device/code`{.literal}             |
    +--------------------------------+--------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://github.com/login/oauth/access_token`{.literal}      |
    +--------------------------------+--------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://openidconnect.googleapis.com/v1/userinfo`{.literal} |
    +--------------------------------+--------------------------------------------------------------+
    | `--keys-uri=URI`{.literal}     | `https://api.github.com/user`{.literal}                      |
    +--------------------------------+--------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `user`{.literal}                                             |
    +--------------------------------+--------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `login`{.literal}                                            |
    +--------------------------------+--------------------------------------------------------------+

    Show more

`--provider=keycloak`{.literal}

:   With Keycloak, you can define multiple realms or organizations. Since it is often a part of a custom deployment, both base URL and realm ID are required, and you can specify them with the `--base-url`{.literal} and `--organization`{.literal} options to the `ipa idp-add`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# ipa idp-add MySSO --provider keycloak \
        --org main --base-url keycloak.domain.com:8443/auth \
        --client-id <your-client-id>
    ```

    Choosing `--provider=keycloak`{.literal} expands to use the following options. The value you specify in the `--base-url`{.literal} option replaces the string `${ipaidpbaseurl}`{.literal} in the table, and the value you specify for the `` --organization `option replaces the string `${ipaidporg} ``{.literal}.

    +--------------------------------+----------------------------------------------------------------------------------------------+
    | Option                         | Value                                                                                        |
    +:===============================+:=============================================================================================+
    | `--auth-uri=URI`{.literal}     | `https://${ipaidpbaseurl}/realms/${ipaidporg}/protocol/openid-connect/auth`{.literal}        |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://${ipaidpbaseurl}/realms/${ipaidporg}/protocol/openid-connect/auth/device`{.literal} |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://${ipaidpbaseurl}/realms/${ipaidporg}/protocol/openid-connect/token`{.literal}       |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://${ipaidpbaseurl}/realms/${ipaidporg}/protocol/openid-connect/userinfo`{.literal}    |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `openid email`{.literal}                                                                     |
    +--------------------------------+----------------------------------------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `email`{.literal}                                                                            |
    +--------------------------------+----------------------------------------------------------------------------------------------+

    Show more

`--provider=okta`{.literal}

:   After registering a new organization in Okta, a new base URL is associated with it. You can specify this base URL with the `--base-url`{.literal} option to the `ipa idp-add`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    [root@client ~]# ipa idp-add MyOkta --provider okta --base-url dev-12345.okta.com --client-id <your-client-id>
    ```

    Choosing `--provider=okta`{.literal} expands to use the following options. The value you specify for the `--base-url`{.literal} option replaces the string `${ipaidpbaseurl}`{.literal} in the table.

    +--------------------------------+-----------------------------------------------------------------+
    | Option                         | Value                                                           |
    +:===============================+:================================================================+
    | `--auth-uri=URI`{.literal}     | `https://${ipaidpbaseurl}/oauth2/v1/authorize`{.literal}        |
    +--------------------------------+-----------------------------------------------------------------+
    | `--dev-auth-uri=URI`{.literal} | `https://${ipaidpbaseurl}/oauth2/v1/device/authorize`{.literal} |
    +--------------------------------+-----------------------------------------------------------------+
    | `--token-uri=URI`{.literal}    | `https://${ipaidpbaseurl}/oauth2/v1/token`{.literal}            |
    +--------------------------------+-----------------------------------------------------------------+
    | `--userinfo-uri=URI`{.literal} | `https://${ipaidpbaseurl}/oauth2/v1/userinfo`{.literal}         |
    +--------------------------------+-----------------------------------------------------------------+
    | `--scope=STR`{.literal}        | `openid email`{.literal}                                        |
    +--------------------------------+-----------------------------------------------------------------+
    | `--idp-user-id=STR`{.literal}  | `email`{.literal}                                               |
    +--------------------------------+-----------------------------------------------------------------+

    Show more

**Additional resources**

-   [Pre-populated IdP templates](https://freeipa.readthedocs.io/en/latest/designs/external-idp/idp-api.html#pre-populated-idp-templates)

### [2.11. Additional resources](#using-external-identity-providers-to-authenticate-to-idm_211-additional-resources) {#additional-resources .title}

-   [Using Ansible to delegate authentication for IdM users to external identity providers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-ansible-to-delegate-authentication-for-idm-users-to-external-identity-providers)

## [Chapter 3. Setting up Samba on an IdM domain member](#setting-up-samba-on-an-idm-domain-member) {#chapter-3.-setting-up-samba-on-an-idm-domain-member .title}

You can configure Samba on a host that is joined to a Red Hat Identity Management (IdM) domain. Users from IdM and also, if available, from trusted Active Directory (AD) domains, can access shares and printer services provided by Samba.

Important

Using Samba on an IdM domain member is an unsupported Technology Preview feature and contains certain limitations. For example, IdM trust controllers do not support the Active Directory Global Catalog service. They also do not support resolving IdM groups by using the Distributed Computing Environment / Remote Procedure Calls (DCE/RPC) protocols. As a consequence, AD users can only access Samba shares and printers hosted on IdM clients when logged in to other IdM clients. AD users logged into a Windows machine cannot access Samba shares hosted on an IdM domain member.

Customers deploying Samba on IdM domain members are encouraged to provide feedback to Red Hat.

If users from AD domains access shares and printer services by Samba, ensure Advanced Encryption Standard (AES) is enabled in AD.

### [3.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   The host is joined as a client to the IdM domain.
-   Both the IdM servers and the client must run on RHEL 10.

### [3.2. Preparing the IdM domain for installing Samba on domain members](#preparing-the-idm-domain-for-installing-samba-on-domain-members) {#preparing-the-idm-domain-for-installing-samba-on-domain-members .title}

Before you can configure Samba on an IdM client, you must prepare the IdM domain by using the `ipa-adtrust-install`{.literal} utility on an IdM server.

Any system where you run the `ipa-adtrust-install`{.literal} command automatically becomes an AD trust controller. However, you must run `ipa-adtrust-install`{.literal} only once on an IdM server.

**Prerequisites**

-   IdM server is installed.
-   You have root privileges to install packages and restart IdM services.

**Procedure**

1.  Install the required packages:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# dnf install ipa-server-trust-ad samba-client
    ```

2.  Authenticate as the IdM administrative user:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# kinit admin
    ```

3.  Run the `ipa-adtrust-install`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# ipa-adtrust-install
    ```

    The DNS service records are created automatically if IdM was installed with an integrated DNS server.

    If you installed IdM without an integrated DNS server, `ipa-adtrust-install`{.literal} prints a list of service records that you must manually add to DNS before you can continue.

4.  The script prompts you that the `/etc/samba/smb.conf`{.literal} already exists and will be rewritten:

    ``` {.language-plaintext tabindex="-1"}
    WARNING: The smb.conf already exists. Running ipa-adtrust-install will break your existing Samba configuration.

    Do you wish to continue? [no]: yes
    ```

5.  The script prompts you to configure the `slapi-nis`{.literal} plug-in, a compatibility plug-in that allows older Linux clients to work with trusted users:

    ``` {.language-plaintext tabindex="-1"}
    Do you want to enable support for trusted domains in Schema Compatibility plugin?
    This will allow clients older than SSSD 1.9 and non-Linux clients to work with trusted users.

    Enable trusted domains support in slapi-nis? [no]: yes
    ```

6.  You are prompted to run the SID generation task to create a SID for any existing users:

    ``` {.language-plaintext tabindex="-1"}
    Do you want to run the ipa-sidgen task? [no]: yes
    ```

    This is a resource-intensive task, so if you have a high number of users, you can run this at another time.

7.  Optional: By default, the Dynamic RPC port range is defined as `49152-65535`{.literal} for Windows Server 2008 and later. If you need to define a different Dynamic RPC port range for your environment, configure Samba to use different ports and open those ports in your firewall settings. The following example sets the port range to `55000-65000`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# net conf setparm global 'rpc server dynamic port range' 55000-65000
    [root@ipaserver ~]# firewall-cmd --add-port=55000-65000/tcp
    [root@ipaserver ~]# firewall-cmd --runtime-to-permanent
    ```

8.  Restart the `ipa`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# ipactl restart
    ```

9.  Use the `smbclient`{.literal} utility to verify that Samba responds to Kerberos authentication from the IdM side:

    ``` {.language-plaintext tabindex="-1"}
    [root@ipaserver ~]# smbclient -L ipaserver.idm.example.com -U user_name --use-kerberos=required
    ```

    ``` {.language-plaintext tabindex="-1"}
    lp_load_ex: changing to config backend registry
        Sharename       Type      Comment
        ---------       ----      -------
        IPC$            IPC       IPC Service (Samba 4.15.2)
    ...
    ```

### [3.3. Installing and configuring a Samba server on an IdM client](#installing-and-configuring-a-samba-server-on-an-idm-client) {#installing-and-configuring-a-samba-server-on-an-idm-client .title}

You can install and configure Samba on an IdM client to securely share files with integrated authentication. This leverages IdM domain accounts for access. Ensure proper prerequisites and configuration to enable seamless resource sharing across your network.

**Prerequisites**

-   Both the IdM servers and the client must run on RHEL 10 or later.
-   The IdM domain is prepared as described in [Preparing the IdM domain for installing Samba on domain members](#preparing-the-idm-domain-for-installing-samba-on-domain-members "3.2. Preparing the IdM domain for installing Samba on domain members").
-   If IdM has a trust configured with AD, enable the AES encryption type for Kerberos. For example, use a group policy object (GPO) to enable the AES encryption type. For details, see [Enabling AES encryption in Active Directory using a GPO](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/ensuring-support-for-common-encryption-types-in-ad-and-rhel#enabling-the-aes-encryption-type-in-active-directory-using-a-gpo).

**Procedure**

1.  Install the `ipa-client-samba`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# dnf install ipa-client-samba
    ```

2.  Use the `ipa-client-samba`{.literal} utility to prepare the client and create an initial Samba configuration:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# ipa-client-samba
    ```

    ``` {.language-plaintext tabindex="-1"}
    Searching for IPA server...
    IPA server: DNS discovery
    Chosen IPA master: idm_server.idm.example.com
    SMB principal to be created: cifs/idm_client.idm.example.com@IDM.EXAMPLE.COM
    NetBIOS name to be used: IDM_CLIENT
    Discovered domains to use:

     Domain name: idm.example.com
    NetBIOS name: IDM
             SID: S-1-5-21-525930803-952335037-206501584
        ID range: 212000000 - 212199999

     Domain name: ad.example.com
    NetBIOS name: AD
             SID: None
        ID range: 1918400000 - 1918599999

    Continue to configure the system with these values? [no]: yes
    Samba domain member is configured. Please check configuration at /etc/samba/smb.conf and start smb and winbind services
    ```

3.  By default, `ipa-client-samba`{.literal} automatically adds the `[homes]`{.literal} section to the `/etc/samba/smb.conf`{.literal} file. This section dynamically shares the home directory of a user when the user connects. If users do not have home directories on this server, or you do not want to share them, remove these from `/etc/samba/smb.conf`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [homes]
        read only = no
    ```

4.  Share directories and printers. For details, see:

    -   [Setting up a Samba file share that uses POSIX ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-samba-file-share-that-uses-posix-acls)
    -   [Setting up a share that uses Windows ACLs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-a-share-that-uses-windows-acls)
    -   [Setting up Samba as a print server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/using-samba-as-a-server#setting-up-samba-as-a-print-server)

5.  Open the ports required for a Samba client in the local firewall:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# firewall-cmd --permanent --add-service=samba-client
    ```

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# firewall-cmd --reload
    ```

6.  Enable and start the `smb`{.literal} and `winbind`{.literal} services:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# systemctl enable --now smb winbind
    ```

    Note

    Do not start the `nmbd`{.literal} service. When using Samba with Active Directory, NetBIOS is not required for interoperability --- DNS handles name resolution in AD environments.

**Verification**

-   Run the following verification step on a different IdM domain member that has the `samba-client`{.literal} package installed:

    -   List the shares on the Samba server using Kerberos authentication:

        ``` {.language-plaintext tabindex="-1"}
        $ smbclient -L idm_client.idm.example.com -U user_name --use-kerberos=required
        ```

        ``` {.language-plaintext tabindex="-1"}
        lp_load_ex: changing to config backend registry

            Sharename       Type      Comment
            ---------       ----      -------
            example         Disk
            IPC$            IPC       IPC Service (Samba 4.15.2)
        ...
        ```

        For more information, see the `ipa-client-samba(1)`{.literal} man page on your system.

### [3.4. Manually adding an ID mapping configuration if IdM trusts a new domain](#manually-adding-an-id-mapping-configuration-if-idm-trusts-a-new-domain) {#manually-adding-an-id-mapping-configuration-if-idm-trusts-a-new-domain .title}

Samba requires an ID mapping configuration for each domain that accesses resources. On an existing Samba server running on an IdM client, manually add the configuration. Do this after adding a new trust to an AD domain.

**Prerequisites**

-   You configured Samba on an IdM client. Afterward, a new trust was added to IdM.
-   The Data Encryption Standard (DES) and RC4 encryption types for Kerberos must be disabled in the trusted AD domain. For security reasons, RHEL 10 does not support these weak encryption types.

**Procedure**

1.  Authenticate by using the host's keytab:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# kinit -k
    ```

2.  Use the `ipa idrange-find`{.literal} command to display both the base ID and the ID range size of the new domain. For example, the following command displays the values for the `ad.example.com`{.literal} domain:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# ipa idrange-find --name="AD.EXAMPLE.COM_id_range" --raw
    ```

    ``` {.language-plaintext tabindex="-1"}
    ---------------
    1 range matched
    ---------------
      cn: AD.EXAMPLE.COM_id_range
      ipabaseid: 1918400000
      ipaidrangesize: 200000
      ipabaserid: 0
      ipanttrusteddomainsid: S-1-5-21-968346183-862388825-1738313271
      iparangetype: ipa-ad-trust
    ----------------------------
    Number of entries returned 1
    ----------------------------
    ```

    You need the values from the `ipabaseid`{.literal} and `ipaidrangesize`{.literal} attributes in the next steps.

3.  To calculate the highest usable ID, use the following formula:

    ``` {.language-plaintext tabindex="-1"}
    maximum_range = ipabaseid + ipaidrangesize - 1
    ```

    With the values from the previous step, the highest usable ID for the `ad.example.com`{.literal} domain is `1918599999`{.literal} (1918400000 + 200000 - 1).

4.  Edit the `/etc/samba/smb.conf`{.literal} file, and add the ID mapping configuration for the domain to the `[global]`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    idmap config AD : range = 1918400000 - 1918599999
    idmap config AD : backend = sss
    ```

    Specify the value from `ipabaseid`{.literal} attribute as the lowest and the computed value from the previous step as the highest value.

5.  Restart the `smb`{.literal} and `winbind`{.literal} services:

    ``` {.language-plaintext tabindex="-1"}
    [root@idm_client]# systemctl restart smb winbind
    ```

**Verification**

-   List the shares on the Samba server using Kerberos authentication:

    ``` {.language-plaintext tabindex="-1"}
    $ smbclient -L idm_client.idm.example.com -U user_name --use-kerberos=required
    ```

    ``` {.language-plaintext tabindex="-1"}
    lp_load_ex: changing to config backend registry

        Sharename       Type      Comment
        ---------       ----      -------
        example         Disk
        IPC$            IPC       IPC Service (Samba 4.15.2)
    ...
    ```

### [3.5. Additional resources](#setting-up-samba-on-an-idm-domain-member_35-additional-resources) {#additional-resources-1 .title}

-   [Installing an Identity Management client](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-client)
-   [Enabling the AES encryption type in Active Directory using a GPO](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_trust_between_idm_and_ad/ensuring-support-for-common-encryption-types-in-ad-and-rhel#enabling-the-aes-encryption-type-in-active-directory-using-a-gpo)

## [Chapter 4. Migrating from NIS to Identity Management](#migrating-from-nis-to-identity-management) {#chapter-4.-migrating-from-nis-to-identity-management .title}

Migrate user, group, host, netgroup, and automount map entries from a Network Information Service (NIS) server to Identity Management (IdM) so that all user management operations happen on the IdM server.

Migrating also transfers authentication and authorization data from NIS and gives you access to more secure protocols such as Kerberos.

### [4.1. Migrating user entries from NIS to IdM](#nis-import-users) {#migrating-user-entries-from-nis-to-idm .title}

The NIS `passwd`{.literal} map contains information about users, such as names, UIDs, primary group, GECOS, shell, and home directory. Use this data to migrate NIS user accounts to Identity Management (IdM).

**Prerequisites**

-   You have root access on NIS server.
-   The NIS server is enrolled into IdM.
-   You have [ID ranges](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules/adjusting-id-ranges-manually) that can store UIDs of imported users.

**Procedure**

1.  Install the `yp-tools`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# dnf install yp-tools -y
    ```

2.  On the NIS server create the `/root/nis-users.sh`{.literal} script with the following content:

    ``` {.language-bash tabindex="-1"}
    #!/bin/sh
    # $1 is the NIS domain, $2 is the primary NIS server
    ypcat -d $1 -h $2 passwd > /dev/shm/nis-map.passwd 2>&1

    IFS=$'\n'
    for line in $(cat /dev/shm/nis-map.passwd) ; do
        IFS=' '
        username=$(echo $line | cut -f1 -d:)
        # Not collecting encrypted password because we need cleartext password
        # to create kerberos key
        uid=$(echo $line | cut -f3 -d:)
        gid=$(echo $line | cut -f4 -d:)
        gecos=$(echo $line | cut -f5 -d:)
        homedir=$(echo $line | cut -f6 -d:)
        shell=$(echo $line | cut -f7 -d:)

        # Now create this entry
        echo passw0rd1 | ipa user-add $username --first=NIS --last=USER \
             --password --gidnumber=$gid --uid=$uid --gecos="$gecos" --homedir=$homedir \
             --shell=$shell
        ipa user-show $username
    done
    ```

3.  Authenticate as the IdM `admin`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# kinit admin
    ```

4.  Run the script. For example:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# sh /root/nis-users.sh nisdomain nis-server.example.com
    ```

    Important

    This script uses hard-coded values for first name, last name, and sets the password to `passw0rd1`{.literal}. The user must change the temporary password at the next login.

### [4.2. Migrating user group from NIS to IdM](#nis-import-groups) {#migrating-user-group-from-nis-to-idm .title}

The NIS `group`{.literal} map contains information about groups, such as group names, GIDs, or group members. Use this data to migrate NIS groups to Identity Management (IdM).

**Prerequisites**

-   You have root access on NIS server.
-   The NIS server is enrolled into IdM.

**Procedure**

1.  Install the `yp-tools`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# dnf install yp-tools -y
    ```

2.  Create the `/root/nis-groups.sh`{.literal} script with the following content on the NIS server:

    ``` {.language-bash tabindex="-1"}
    #!/bin/sh
    # $1 is the NIS domain, $2 is the primary NIS server
    ypcat -d $1 -h $2 group > /dev/shm/nis-map.group 2>&1

    IFS=$'\n'
    for line in $(cat /dev/shm/nis-map.group); do
        IFS=' '
        groupname=$(echo $line | cut -f1 -d:)
        # Not collecting encrypted password because we need cleartext password
        # to create kerberos key
        gid=$(echo $line | cut -f3 -d:)
        members=$(echo $line | cut -f4 -d:)

        # Now create this entry
        ipa group-add $groupname --desc=NIS_GROUP_$groupname --gid=$gid
        if [ -n "$members" ]; then
            useropts=$(eval echo --users={$members})
            ipa group-add-member $groupname $useropts
        fi
        ipa group-show $groupname
    done
    ```

    Note

    Make sure your usernames do not contain any special characters to ensure successful migration of the user group.

3.  Authenticate as the IdM `admin`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# kinit admin
    ```

4.  Run the script. For example:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# sh /root/nis-groups.sh nisdomain nis-server.example.com
    ```

### [4.3. Migrating host entries from NIS to IdM](#nis-import-hosts) {#migrating-host-entries-from-nis-to-idm .title}

The NIS `hosts`{.literal} map contains information about hosts, such as host names and IP addresses. Use this data to migrate NIS host entries to Identity Management (IdM):

**Prerequisites**

-   You have root access on NIS server.
-   The NIS server is enrolled into IdM.

**Procedure**

1.  Install the `yp-tools`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# dnf install yp-tools -y
    ```

2.  Create the `/root/nis-hosts.sh`{.literal} script with the following content on the NIS server:

    ``` {.language-bash tabindex="-1"}
    #!/bin/sh
    # $1 is the NIS domain, $2 is the primary NIS server
    ypcat -d $1 -h $2 hosts | egrep -v "localhost|127.0.0.1" > /dev/shm/nis-map.hosts 2>&1

    IFS=$'\n'
    for line in $(cat /dev/shm/nis-map.hosts); do
        IFS=' '
        ipaddress=$(echo $line | awk '{print $1}')
        hostname=$(echo $line | awk '{print $2}')
        primary=$(ipa env xmlrpc_uri | tr -d '[:space:]' | cut -f3 -d: | cut -f3 -d/)
        domain=$(ipa env domain | tr -d '[:space:]' | cut -f2 -d:)
        if [ $(echo $hostname | grep "\." |wc -l) -eq 0 ] ; then
            hostname=$(echo $hostname.$domain)
        fi
        zone=$(echo $hostname | cut -f2- -d.)
        if [ $(ipa dnszone-show $zone 2>/dev/null | wc -l) -eq 0 ] ; then
            ipa dnszone-add --name-server=$primary --admin-email=root.$primary
        fi
        ptrzone=$(echo $ipaddress | awk -F. '{print $3 "." $2 "." $1 ".in-addr.arpa."}')
        if [ $(ipa dnszone-show $ptrzone 2>/dev/null | wc -l) -eq 0 ] ; then
            ipa dnszone-add  $ptrzone --name-server=$primary --admin-email=root.$primary
        fi
        # Now create this entry
        ipa host-add $hostname --ip-address=$ipaddress
        ipa host-show $hostname
    done
    ```

3.  Authenticate as the IdM `admin`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# kinit admin
    ```

4.  Run the script. For example:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# sh /root/nis-hosts.sh nisdomain nis-server.example.com
    ```

    Note

    This script does not migrate special host configurations, such as aliases.

### [4.4. Migrating netgroup entries from NIS to IdM](#nis-import-netgroups) {#migrating-netgroup-entries-from-nis-to-idm .title}

The NIS `netgroup`{.literal} map contains information about netgroups. Use this data to migrate NIS netgroups to Identity Management (IdM).

**Prerequisites**

-   You have root access on NIS server.
-   The NIS server is enrolled into IdM.

**Procedure**

1.  Install the `yp-tools`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# dnf install yp-tools -y
    ```

2.  Create the `/root/nis-netgroups.sh`{.literal} script with the following content on the NIS server:

    ``` {.language-bash tabindex="-1"}
    #!/bin/sh
    # $1 is the NIS domain, $2 is the primary NIS server
    ypcat -k -d $1 -h $2 netgroup > /dev/shm/nis-map.netgroup 2>&1

    IFS=$'\n'
    for line in $(cat /dev/shm/nis-map.netgroup); do
        IFS=' '
        netgroupname=$(echo $line | awk '{print $1}')
        triples=$(echo $line | sed "s/^$netgroupname //")
        echo "ipa netgroup-add $netgroupname --desc=NIS_NG_$netgroupname"
        if [ $(echo $line | grep "(," | wc -l) -gt 0 ]; then
            echo "ipa netgroup-mod $netgroupname --hostcat=all"
        fi
        if [ $(echo $line | grep ",," | wc -l) -gt 0 ]; then
            echo "ipa netgroup-mod $netgroupname --usercat=all"
        fi

        for triple in $triples; do
            triple=$(echo $triple | sed -e 's/-//g' -e 's/(//' -e 's/)//')
            if [ $(echo $triple | grep ",.*," | wc -l) -gt 0 ]; then
                hostname=$(echo $triple | cut -f1 -d,)
                username=$(echo $triple | cut -f2 -d,)
                domain=$(echo $triple | cut -f3 -d,)
                hosts=""; users=""; doms="";
                [ -n "$hostname" ] && hosts="--hosts=$hostname"
                [ -n "$username" ] && users="--users=$username"
                [ -n "$domain"   ] && doms="--nisdomain=$domain"
                echo "ipa netgroup-add-member $netgroup $hosts $users $doms"
            else
                netgroup=$triple
                echo "ipa netgroup-add $netgroup --desc=<NIS_NG>_$netgroup"
            fi
        done
    done
    ```

3.  Authenticate as the IdM `admin`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# kinit admin
    ```

4.  Run the script. For example:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# sh /root/nis-netgroups.sh nisdomain nis-server.example.com
    ```

### [4.5. Migrating automount maps from NIS to IdM](#nis-import-automount) {#migrating-automount-maps-from-nis-to-idm .title}

Automount maps are a series of nested and interrelated entries that define the location (the parent entry), the associated keys, and maps. To migrate NIS automount maps to Identity Management (IdM):

**Prerequisites**

-   You have root access on NIS server.
-   The NIS server is enrolled into IdM.

**Procedure**

1.  Install the `yp-tools`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# dnf install yp-tools -y
    ```

2.  Create the `/root/nis-automounts.sh`{.literal} script with the following content on the NIS server:

    ``` {.language-bash tabindex="-1"}
    #!/bin/sh
    # $1 is for the automount entry in ipa

    ipa automountlocation-add $1

    # $2 is the NIS domain, $3 is the primary NIS server, $4 is the map name

    ypcat -k -d $2 -h $3 $4 > /dev/shm/nis-map.$4 2>&1

    ipa automountmap-add $1 $4

    IFS=$'\n'
    for line in $(cat /dev/shm/nis-map.$4); do
        IFS=" "
        key=$(echo "$line" | awk '{print $1}')
        info=$(echo "$line" | sed -e "s^$key[ \t]*")
        ipa automountkey-add nis $4 --key="$key" --info="$info"
    done
    ```

3.  Authenticate as the IdM `admin`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# kinit admin
    ```

4.  Run the script. For example:

    ``` {.language-plaintext tabindex="-1"}
    [root@nis-server ~]# sh /root/nis-automounts.sh location nisdomain nis-server.example.com map_name
    ```

## [Chapter 5. Using Ansible to automount NFS shares for IdM users](#using-ansible-to-automount-nfs-shares-for-idm-users) {#chapter-5.-using-ansible-to-automount-nfs-shares-for-idm-users .title}

To ensure that IdM users can automatically access NFS shares when logging into IdM clients, configure automount maps and locations by using Ansible.

Automount manages directories across multiple systems. It automatically mounts a directory whenever access is requested for the directory. This works well within an Identity Management (IdM) domain so that you can share directories on clients within the domain easily.

### [5.1. Autofs and automount in IdM](#autofs-and-automount-in-idm) {#autofs-and-automount-in-idm .title}

The `autofs`{.literal} service automatically mounts directories when they are accessed and unmounts them after a period of inactivity, which saves system resources compared to static mounting.

The `autofs`{.literal} service directs the `automount`{.literal} daemon to perform the actual mounting and unmounting of directories.

Automount maps

:   On a system that utilizes `autofs`{.literal}, the `automount`{.literal} configuration is stored in several different files. The primary `automount`{.literal} configuration file is `/etc/auto.master`{.literal}, which contains the master mapping of `automount`{.literal} mount points, and their associated resources, on a system. This mapping is known as *automount maps*.

    The `/etc/auto.master`{.literal} configuration file contains the *master map*. It can contain references to other maps. These maps can either be direct or indirect. Direct maps use absolute path names for their mount points, while indirect maps use relative path names.

Automount configuration in IdM

:   While `automount`{.literal} typically retrieves its map data from the local `/etc/auto.master`{.literal} and associated files, it can also retrieve map data from other sources. One common source is an LDAP server. In the context of Identity Management (IdM), this is a 389 Directory Server.

    If a system that uses `autofs`{.literal} is a client in an IdM domain, the `automount`{.literal} configuration is not stored in local configuration files. Instead, the `autofs`{.literal} configuration, such as maps, locations, and keys, is stored as LDAP entries in the IdM directory. For example, for the `idm.example.com`{.literal} IdM domain, the default *master map* is stored as follows:

    ``` {.language-plaintext tabindex="-1"}
    dn:
    automountmapname=auto.master,cn=default,cn=automount,dc=idm,dc=example,dc=com
    objectClass: automountMap
    objectClass: top
    automountMapName: auto.master
    ```

**Additional resources**

-   [Mounting file systems on demand](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/mounting-file-systems-on-demand)

### [5.2. Setting up an NFS server with Kerberos in an Identity Management domain](#setting-up-an-nfs-server-with-kerberos-in-a-rhel-identity-management-domain) {#setting-up-an-nfs-server-with-kerberos-in-an-identity-management-domain .title}

If you use Red Hat Enterprise Linux Identity Management (IdM), you can join your NFS server to the IdM domain. This enables you to centrally manage users and groups and to use Kerberos for authentication, integrity protection, and traffic encryption.

**Prerequisites**

-   The NFS server is [enrolled](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-client) in a Red Hat Enterprise Linux Identity Management (IdM) domain.
-   The NFS server is running and configured.

**Procedure**

1.  Obtain a kerberos ticket as an IdM administrator:

    ``` {.language-plaintext tabindex="-1"}
    # kinit admin
    ```

2.  Create a `nfs/<FQDN>`{.literal} service principal:

    ``` {.language-plaintext tabindex="-1"}
    # ipa service-add nfs/nfs_server.idm.example.com
    ```

3.  Retrieve the `nfs`{.literal} service principal from IdM, and store it in the `/etc/krb5.keytab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-getkeytab -s idm_server.idm.example.com -p nfs/nfs_server.idm.example.com -k /etc/krb5.keytab
    ```

4.  Optional: Display the principals in the `/etc/krb5.keytab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # klist -k /etc/krb5.keytab
    ```

    ``` {.language-plaintext tabindex="-1"}
    Keytab name: FILE:/etc/krb5.keytab
    KVNO Principal
    ---- --------------------------------------------------------------------------
       1 nfs/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       1 nfs/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       1 nfs/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       1 nfs/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       7 host/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       7 host/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       7 host/nfs_server.idm.example.com@IDM.EXAMPLE.COM
       7 host/nfs_server.idm.example.com@IDM.EXAMPLE.COM
    ```

    By default, the IdM client adds the host principal to the `/etc/krb5.keytab`{.literal} file when you join the host to IdM. If the host principal is missing, use the **`ipa-getkeytab -s`{.literal}**` `{.literal}*`idm_server.idm.example.com`{.literal}*` `{.literal}**`-p`{.literal}**` `{.literal}*`host/nfs_server.idm.example.com`{.literal}*` `{.literal}**`-k /etc/krb5.keytab`{.literal}** command to add it.

5.  Use the `ipa-client-automount`{.literal} utility to configure mapping of IdM IDs.

    a.  If the client is not in the IdM DNS domain, use the `--domain`{.literal} option to specify the primary DNS domain of the IdM deployment. Alternatively, use the `--server`{.literal} option to specify the IdM server to connect to:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-client-automount --domain idm.example.com
        ```

        The `--domain`{.literal} option triggers DNS discovery to determine the IdM servers to use.

    b.  If the client is already in the IdM DNS domain, run the command without the `--domain`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-client-automount
        ```

        ``` {.language-plaintext tabindex="-1"}
        Searching for IPA server...
        IPA server: DNS discovery
        Location: default
        Continue to configure the system with these values? [no]: yes
        Configured /etc/idmapd.conf
        Restarting sssd, waiting for it to become available.
        Started autofs
        ```

6.  Update your `/etc/exports`{.literal} file, and add the Kerberos security method to the client options. For example:

    ``` {.language-plaintext tabindex="-1"}
    /nfs/projects/       192.0.2.0/24(rw,sec=krb5i)
    ```

    If you want that your clients can select from multiple security methods, specify them separated by colons:

    ``` {.language-plaintext tabindex="-1"}
    /nfs/projects/       192.0.2.0/24(rw,sec=krb5:krb5i:krb5p)
    ```

7.  Reload the exported file systems:

    ``` {.language-plaintext tabindex="-1"}
    # exportfs -r
    ```

### [5.3. Configuring automount locations, maps, and keys in IdM by using Ansible](#configuring-automount-locations-maps-and-keys-in-idm-by-using-ansible) {#configuring-automount-locations-maps-and-keys-in-idm-by-using-ansible .title}

As an Identity Management (IdM) system administrator, you can configure automount locations and maps in IdM so that users in a location can access shares exported by a Network File System (NFS) server by navigating to mount points on their hosts.

The exported NFS directory and the mount points are specified in the automount maps. In LDAP terms, a location is a container for map entries.

The following procedure describes how to use Ansible to configure the example **raleigh** automount location with the following details:

-   **nfs-server.idm.example.com** is the fully-qualified domain name (FQDN) of a Network File System (NFS) server and an IdM client .
-   A map that mounts the **nfs-server.idm.example.com:/exports/project** share on the **/devel/project** mount point on the IdM client as a read-write directory.

**Prerequisites**

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  On your Ansible control node, navigate to your **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Copy the `automount-location-present.yml`{.literal} Ansible playbook file located in the `/usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automount/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp /usr/share/ansible/collections/ansible_collections/freeipa/ansible_freeipa/playbooks/automount/automount-location-present.yml automount-location-map-and-key-present.yml
    ```

3.  Open the `automount-location-map-and-key-present.yml`{.literal} file for editing.

4.  Adapt the file by setting the following variables in the `freeipa.ansible_freeipa.ipaautomountlocation`{.literal} task section:

    -   Indicate that the value of the `ipaadmin_password`{.literal} variable is defined in the **secret.yml** Ansible vault file.

    -   Set the `name`{.literal} variable to **raleigh**.

    -   Ensure that the `state`{.literal} variable is set to `present`{.literal}.

        This is the modified Ansible playbook file for the current example:

    ``` {.language-plaintext tabindex="-1"}
    ---
    - name: Automount location present example
      hosts: ipaserver
      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
      - name: Ensure automount location is present
        freeipa.ansible_freeipa.ipaautomountlocation:
          ipaadmin_password: "{{ ipaadmin_password }}"
          name: raleigh
          state: present
    ```

5.  Continue editing the `automount-location-map-and-key-present.yml`{.literal} file:

    a.  In the `tasks`{.literal} section, add a task to ensure the presence of an automount map:

        ``` {.language-plaintext tabindex="-1"}
        [...]
          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
        [...]
          - name: ensure map named auto.devel in location raleigh is created
            freeipa.ansible_freeipa.ipaautomountmap:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: auto.devel
              location: raleigh
              state: present
        ```

    b.  Add another task to add the mount point and NFS server information to the map:

        ``` {.language-plaintext tabindex="-1"}
        [...]
          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
        [...]
          - name: ensure automount key /devel/project is present
            freeipa.ansible_freeipa.ipaautomountkey:
              ipaadmin_password: "{{ ipaadmin_password }}"
              location: raleigh
              mapname: auto.devel
              key: /devel/project
              info: nfs-server.idm.example.com:/exports/project
              state: present
        ```

    c.  Add another task to ensure **auto.devel** is connected to **auto.master**:

        ``` {.language-plaintext tabindex="-1"}
        [...]
          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
        [...]
        - name: Ensure auto.devel is connected in auto.master:
          freeipa.ansible_freeipa.ipaautomountkey:
            ipaadmin_password: "{{ ipaadmin_password }}"
            location: raleigh
            mapname: auto.map
            key: /devel
            info: auto.devel
            state: present
        ```

6.  Save the file.

7.  Run the Ansible playbook and specify the playbook and inventory files:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory automount-location-map-and-key-present.yml
    ```

### [5.4. Using Ansible to add IdM users to a group that owns NFS shares](#using-ansible-to-add-idm-users-to-a-group-that-owns-nfs-shares) {#using-ansible-to-add-idm-users-to-a-group-that-owns-nfs-shares .title}

As an Identity Management (IdM) system administrator, you can use Ansible to create a group of users that is able to access NFS shares, and add IdM users to this group.

This example describes how to use an Ansible playbook to ensure that the **idm_user** account belongs to the **developers** group, so that **idm_user** can access the **/exports/project** NFS share.

**Prerequisites**

-   You have `root`{.literal} access to the **nfs-server.idm.example.com** NFS server, which is an IdM client located in the **raleigh** automount location.

-   On the control node:

    -   You are using Ansible version 2.15 or later.
    -   You have installed the [`ansible-freeipa`{.literal}](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/installing-an-identity-management-server-using-an-ansible-playbook#installing-the-ansible-freeipa-package) package.
    -   The example assumes that in the **\~/*MyPlaybooks*/** directory, you have created an [Ansible inventory file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/preparing-your-environment-for-managing-idm-using-ansible-playbooks) with the fully-qualified domain name (FQDN) of the IdM server.
    -   The example assumes that the **secret.yml** Ansible vault stores your `ipaadmin_password`{.literal} and that you have access to a file that stores the password protecting the **secret.yml** file.

-   The target node, that is the node on which the `freeipa.ansible_freeipa`{.literal} module is executed, is part of the IdM domain as an IdM client, server or replica.

**Procedure**

1.  On your Ansible control node, navigate to the **\~/*MyPlaybooks*/** directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Open the `automount-location-map-and-key-present.yml`{.literal} file for editing.

3.  In the `tasks`{.literal} section, add a task to ensure that the IdM **developers** group exists and **idm_user** is added to this group:

    ``` {.language-plaintext tabindex="-1"}
    [...]
      vars_files:
      - /home/user_name/MyPlaybooks/secret.yml
      tasks:
    [...]
      - ipagroup:
         ipaadmin_password: "{{ ipaadmin_password }}"
          name: developers
          user:
          - idm_user
          state: present
    ```

4.  Save the file.

5.  Run the Ansible playbook and specify the playbook and inventory files:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory automount-location-map-and-key-present.yml
    ```

6.  On the NFS server, change the group ownership of the **/exports/project** directory to **developers** so that every IdM user in the group can access the directory:

    ``` {.language-plaintext tabindex="-1"}
    # chgrp developers /exports/project
    ```

### [5.5. Configuring automount on an IdM client](#configuring-automount-on-an-idm-client) {#configuring-automount-on-an-idm-client .title}

As an Identity Management (IdM) system administrator, you can configure automount services on an IdM client so that Network File System (NFS) shares for the client's location are automatically accessible to IdM users when they log in.

This procedure configures an IdM client to use automount services available in the **raleigh** location.

**Prerequisites**

-   You have `root`{.literal} access to the IdM client.
-   You are logged in as IdM administrator.
-   The automount location exists. The example location is **raleigh**.

**Procedure**

1.  On the IdM client, enter the `ipa-client-automount`{.literal} command and specify the location. Use the `-U`{.literal} option to run the script unattended.

    a.  If the client is not in the IdM DNS domain, either use the `--domain`{.literal} option to specify the primary DNS domain of the IdM deployment or the `--server`{.literal} option to specify the IdM server to connect to:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-client-automount --domain idm.example.com --location raleigh -U
        ```

        With the `--domain`{.literal} option, DNS discovery will attempt to determine the IdM server(s) to use.

    b.  If the client is already in the IdM DNS domain, run the command without the `--domain`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        # ipa-client-automount --location raleigh -U
        ```

2.  Stop the autofs service, clear the SSSD cache, and start the autofs service to load the new configuration settings:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop autofs ; sss_cache -E ; systemctl start autofs
    ```

### [5.6. Verifying that an IdM user can access NFS shares on an IdM client](#verifying-that-an-idm-user-can-access-nfs-shares-on-an-idm-client_ansible-automount) {#verifying-that-an-idm-user-can-access-nfs-shares-on-an-idm-client .title}

As an Identity Management (IdM) system administrator, you can test if an IdM user that is a member of a specific group can access NFS shares when logged in to a specific IdM client.

In the example, the following scenario is tested:

-   An IdM user named **idm_user** belonging to the **developers** group can read and write the contents of the files in the **/devel/project** directory automounted on **idm-client.idm.example.com**, an IdM client located in the **raleigh** automount location.

**Prerequisites**

-   You have [configured an NFS server with Kerberos on an IdM host](#setting-up-an-nfs-server-with-kerberos-in-a-rhel-identity-management-domain "5.2. Setting up an NFS server with Kerberos in an Identity Management domain").
-   You have [configured automount locations, maps, and mount points in IdM](#configuring-automount-locations-maps-and-keys-in-idm-by-using-ansible "5.3. Configuring automount locations, maps, and keys in IdM by using Ansible") in which you configured how IdM users can access the NFS share.
-   You have [used Ansible to add IdM users to the developers group that owns the NFS shares](#using-ansible-to-add-idm-users-to-a-group-that-owns-nfs-shares "5.4. Using Ansible to add IdM users to a group that owns NFS shares").
-   You have [configured automount on the IdM client](#configuring-automount-on-an-idm-client "5.5. Configuring automount on an IdM client").

**Procedure**

1.  Verify that the IdM user can access the `read-write`{.literal} directory:

    a.  Connect to the IdM client as the IdM user:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh idm_user@idm-client.idm.example.com
        Password:
        ```

    b.  Obtain the ticket-granting ticket (TGT) for the IdM user:

        ``` {.language-plaintext tabindex="-1"}
        $ kinit idm_user
        ```

    c.  Optional: View the group membership of the IdM user:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa user-show idm_user
          User login: idm_user
          [...]
          Member of groups: developers, ipausers
        ```

    d.  Navigate to the **/devel/project** directory:

        ``` {.language-plaintext tabindex="-1"}
        $ cd /devel/project
        ```

    e.  List the directory contents:

        ``` {.language-plaintext tabindex="-1"}
        $ ls
        rw_file
        ```

    f.  Add a line to the file in the directory to test the `write`{.literal} permission:

        ``` {.language-plaintext tabindex="-1"}
        $ echo "idm_user can write into the file" > rw_file
        ```

    g.  Optional: View the updated contents of the file:

        ``` {.language-plaintext tabindex="-1"}
        $ cat rw_file
        this is a read-write file
        idm_user can write into the file
        ```

    The output confirms that **idm_user** can write into the file.

## [Legal Notice](#idm140339881612368) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
