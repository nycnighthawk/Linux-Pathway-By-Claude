---
{"title": "Managing systems in the RHEL web console", "guide": "managing_systems_in_the_rhel_web_console", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_systems_in_the_rhel_web_console/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Managing systems in the RHEL web console {#managing-systems-in-the-rhel-web-console .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Server management with a graphical web-based interface {#server-management-with-a-graphical-web-based-interface .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139679037504752)

**Abstract**

The RHEL web console is a web-based graphical interface based on the upstream Cockpit project. Use it to perform system administration tasks, such as inspecting and controlling systemd services, managing storage, configuring networks, analyzing network issues, and inspecting logs.

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

## [Chapter 1. Getting started with the RHEL web console](#getting-started-with-the-rhel-web-console) {#chapter-1.-getting-started-with-the-rhel-web-console .title}

Install, configure, and monitor systems by using the RHEL web console. This graphical interface simplifies common administration tasks, such as managing logs, storage, and remote hosts.

### [1.1. What is the RHEL web console](#what-is-the-rhel-web-console) {#what-is-the-rhel-web-console .title}

The RHEL web console is a web-based graphical interface for managing and monitoring your local system and Linux servers in your network environment.

In the RHEL web console, you can perform a wide range of administration tasks, including:

-   Managing services
-   Managing user accounts
-   Managing and monitoring system services
-   Configuring network interfaces and firewall
-   Reviewing system logs
-   Managing virtual machines
-   Creating diagnostic reports
-   Setting kernel dump configuration
-   Configuring SELinux
-   Updating software
-   Managing system subscriptions

The web console uses the same system tools as the command line. If you change a setting on the command line, the web console updates instantly. You can switch between the web interface and the command line at any time.

You can also monitor the logs and performance of systems in the network environment in a graphical form. In addition, you can change the settings directly in the web console or on the command line.

### [1.2. Installing and enabling the web console](#installing-and-enabling-the-web-console) {#installing-and-enabling-the-web-console .title}

To access the RHEL web console, enable the `cockpit.socket`{.literal} service first. RHEL 10 includes the web console installed by default in many installation variants. If this is not the case on your system, install the `cockpit`{.literal} package before enabling the `cockpit.socket`{.literal} service.

**Procedure**

1.  If the web console is not installed by default on your installation variant, manually install the `cockpit`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install cockpit
    ```

2.  Enable and start the `cockpit.socket`{.literal} service, which runs a web server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now cockpit.socket
    ```

3.  If you are using a custom firewall profile, add the `cockpit`{.literal} service to `firewalld`{.literal} to open port 9090 in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-service=cockpit --permanent
    # firewall-cmd --reload
    ```

**Verification**

-   To verify the previous installation and configuration, [open the web console](#logging-in-to-the-web-console "1.3. Logging in to the web console").

### [1.3. Logging in to the web console](#logging-in-to-the-web-console) {#logging-in-to-the-web-console .title}

When the `cockpit.socket`{.literal} service is running and the corresponding firewall port is open, you can log in to the web console in your browser for the first time.

**Prerequisites**

-   Use one of the following browsers to open the web console:

    -   Mozilla Firefox 52 and later
    -   Google Chrome 57 and later
    -   Microsoft Edge 16 and later

-   System user account credentials

    The RHEL web console uses a specific pluggable authentication modules (PAM) stack at `/etc/pam.d/cockpit`{.literal}. The default configuration allows logging in with the user name and password of any local account on the system.

-   Port 9090 is open in your firewall.

**Procedure**

1.  In your web browser, enter the following address to access the web console:

    ``` {.language-plaintext tabindex="-1"}
    https://localhost:9090
    ```

    Note

    This provides a web-console login on your local machine. If you want to log in to the web console of a remote system, see the [Connecting to the web console from a remote machine](#connecting-to-the-web-console-from-a-remote-machine "1.6. Connecting to the web console from a remote machine") section.

    If you use a self-signed certificate, the browser displays a warning. Check the certificate, and accept the security exception to proceed with the login.

    The console loads a certificate from the `/etc/cockpit/ws-certs.d`{.literal} directory and uses the last file with a `.cert`{.literal} extension in alphabetical order. To avoid having to grant security exceptions, install a certificate signed by a certificate authority (CA).

2.  In the login screen, enter your system user name and password.

3.  Click **Log In**.

**Verification**

-   After successful authentication, the web console displays the **Overview** page.

### [1.4. Administrative access in the web console](#administrative-access-in-the-web-console) {#administrative-access-in-the-web-console .title}

You can gain administrative access in the RHEL web console to perform privileged tasks, such as managing services, users, and networking, which require elevated permissions.

After you log in for the first time with a regular user account, the web console starts with limited access. When you have limited access, you can view the settings, but you cannot perform actions that require administrative privileges, such as installing packages.

To perform administrative tasks, click **Limited access** in the top panel of the web console page. You must have `sudo`{.literal} access to the system and provide your user password to gain administrative access. From that point, the web console provides administrative access and preserves this setting across user sessions.

To switch back to limited access, click **Administrative access** in the top panel of the web console page.

Important

The RHEL web console disallows root account logins by default for security reasons. Instead of logging in as root, use administrative access. If your scenario requires logging in as root, see the *Connecting to the web console from a remote machine as a root user* section.

**Additional resources**

-   [Managing sudo access](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access)
-   [Connecting to the web console from a remote machine as a root user](#connecting-to-the-web-console-from-a-remote-machine-as-a-root-user "1.7. Connecting to the web console from a remote machine as a root user")

### [1.5. Disabling basic authentication in the web console](#disabling-basic-authentication-in-the-web-console) {#disabling-basic-authentication-in-the-web-console .title}

Disable basic authentication for the RHEL web console to enforce stronger authentication methods, such as Kerberos. You can configure this setting in the `cockpit.conf`{.literal} file to override default security behavior.

Use the `none`{.literal} action to disable an authentication scheme and only allow authentication through GSSAPI and forms.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

-   You have `root`{.literal} privileges or permissions to enter administrative commands with `sudo`{.literal}.

**Procedure**

1.  Open or create the `cockpit.conf`{.literal} file in the `/etc/cockpit/`{.literal} directory in a text editor of your preference, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi cockpit.conf
    ```

2.  Add the following text:

    ``` {.language-plaintext tabindex="-1"}
    [basic]
    action = none
    ```

3.  Save the file.

4.  Restart the web console for changes to take effect.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl try-restart cockpit
    ```

**Verification**

-   Attempt to log in to the web console by using basic authentication. The web console denies access and prompts you for alternative authentication.

### [1.6. Connecting to the web console from a remote machine](#connecting-to-the-web-console-from-a-remote-machine) {#connecting-to-the-web-console-from-a-remote-machine .title}

You can connect to your web console interface from any client operating system and also from mobile phones or tablets.

**Prerequisites**

-   A device with a supported internet browser, such as:

    -   Mozilla Firefox 52 and later
    -   Google Chrome 57 and later
    -   Microsoft Edge 16 and later

-   The RHEL 10 system you want to access with an installed and accessible web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

**Procedure**

1.  Open your web browser.

2.  Type the remote server's address in one of the following formats:

    a.  With the server's hostname:

        ``` {.language-plaintext tabindex="-1"}
        https://<server.hostname.example.com>:<port-number>
        ```

        For example:

        ``` {.language-plaintext tabindex="-1"}
        https://example.com:9090
        ```

    b.  With the server's IP address:

        ``` {.language-plaintext tabindex="-1"}
        https://<server.IP_address>:<port-number>
        ```

        For example:

        ``` {.language-plaintext tabindex="-1"}
        https://192.0.2.2:9090
        ```

3.  After the login interface opens, log in with your RHEL system credentials.

**Verification**

-   After a successful login, the web console displays the **Overview** page of the remote system.

### [1.7. Connecting to the web console from a remote machine as a root user](#connecting-to-the-web-console-from-a-remote-machine-as-a-root-user) {#connecting-to-the-web-console-from-a-remote-machine-as-a-root-user .title}

You can connect to the RHEL web console as the `root`{.literal} user to gain full administrative control of a remote host. Be sure to use SSH keys instead of a password for this privileged connection.

On new installations of RHEL 9.2 or later, the RHEL web console disallows root account logins by default for security reasons. You can allow the `root`{.literal} login in the `/etc/cockpit/disallowed-users`{.literal} file.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

**Procedure**

1.  Open the `disallowed-users`{.literal} file in the `/etc/cockpit/`{.literal} directory in a text editor of your preference, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/cockpit/disallowed-users
    ```

2.  Edit the file and remove the line for the `root`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    # List of users which are not allowed to login to Cockpit root
     
    ```

3.  Save the changes and quit the editor.

**Verification**

-   Log in to the web console as a `root`{.literal} user.

    For details, see [Logging in to the web console](#logging-in-to-the-web-console "1.3. Logging in to the web console").

### [1.8. Logging in to the web console using a one-time password](#logging-in-to-the-web-console-using-a-one-time-password) {#logging-in-to-the-web-console-using-a-one-time-password .title}

Log in to the RHEL web console by using a one-time password (OTP) to enhance security. You can use this two-factor authentication method in an IdM domain with enabled OTP.

Important

It is possible to log in using a one-time password only if your system is part of an Identity Management (IdM) domain with enabled OTP configuration.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

-   An Identity Management server with enabled OTP configuration.

-   A configured hardware or software device generating OTP tokens.

**Procedure**

1.  Open the RHEL web console in your browser:

    -   Locally: `https://localhost:9090`{.literal}

    -   Remotely with the server hostname: `https://example.com:9090`{.literal}

    -   Remotely with the server IP address: `https://EXAMPLE.SERVER.IP.ADDR:9090`{.literal}

        If you use a self-signed certificate, the browser issues a warning. Check the certificate and accept the security exception to proceed with the login.

        The console loads a certificate from the `/etc/cockpit/ws-certs.d`{.literal} directory and uses the last file with a `.cert`{.literal} extension in alphabetical order. To avoid having to grant security exceptions, install a certificate signed by a certificate authority (CA).

2.  The Login window opens. In the Login window, enter your system user name and password.

3.  Generate a one-time password on your device.

4.  Enter the one-time password into a new field that displays in the web console interface after you confirm your password.

5.  Click **Log in**.

**Verification**

-   After a successful login, the web console displays the **Overview** page.

### [1.9. Adding a banner to the login page](#adding-a-banner-to-the-login-page) {#adding-a-banner-to-the-login-page .title}

You can add a custom banner to the RHEL web console login page. This helps to display important security warnings or legal notices to users before they log in to the system.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

-   You have `root`{.literal} privileges or permissions to enter administrative commands with `sudo`{.literal}.

**Procedure**

1.  Open the `/etc/issue.cockpit`{.literal} file in a text editor of your preference:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/issue.cockpit
    ```

2.  Add the content you want to display as the banner to the file, for example:

    ``` {.language-plaintext tabindex="-1"}
    This is an example banner for the RHEL web console login page.
    ```

    You cannot include any macros in the file, but you can use line breaks and ASCII art.

3.  Save the file.

4.  Open the `cockpit.conf`{.literal} file in the `/etc/cockpit/`{.literal} directory in a text editor of your preference, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/cockpit/cockpit.conf
    ```

5.  Add the following text to the file:

    ``` {.language-plaintext tabindex="-1"}
    [Session]
    Banner=/etc/issue.cockpit
    ```

6.  Save the file.

7.  Restart the web console for changes to take effect.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl try-restart cockpit
    ```

**Verification**

-   Open the web console login screen again to verify that the banner is now visible:

### [1.10. Configuring automatic idle lock in the web console](#configuring-automatic-idle-lock-in-the-web-console) {#configuring-automatic-idle-lock-in-the-web-console .title}

You can enable the automatic idle lock and set the idle timeout for your system through the web console interface. This ensures your screen automatically locks after a period of inactivity, protecting the system from unauthorized access.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

-   You have `root`{.literal} privileges or permissions to enter administrative commands with `sudo`{.literal}.

**Procedure**

1.  Open the `cockpit.conf`{.literal} file in the `/etc/cockpit/`{.literal} directory in a text editor of your preference, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/cockpit/cockpit.conf
    ```

2.  Add the following text to the file:

    ``` {.language-plaintext tabindex="-1"}
    [Session]
    IdleTimeout=<X>
    ```

    Substitute *\<X\>* with a number for a time period of your choice in minutes.

3.  Save the file.

4.  Restart the web console for changes to take effect.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl try-restart cockpit
    ```

**Verification**

-   Check if the session logs you out after a set period of time.

### [1.11. Changing the web console listening port](#changing-the-web-console-listening-port) {#changing-the-web-console-listening-port .title}

By default, the RHEL web console communicates through TCP port 9090. You can change the port number by overriding the default socket settings. This adjustment is often necessary to meet specific security or network policies.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

-   You have `root`{.literal} privileges or permissions to enter administrative commands with `sudo`{.literal}.

-   The `firewalld`{.literal} service is running.

**Procedure**

1.  Pick an unoccupied port, for example, *\<4488/tcp\>*, and instruct SELinux to allow the `cockpit`{.literal} service to bind to that port:

    ``` {.language-plaintext tabindex="-1"}
    # semanage port -a -t websm_port_t -p tcp <4488>
    ```

    Note that a port can be used only by one service at a time, and thus an attempt to use an already occupied port implies the `ValueError: Port already defined`{.literal} error message.

2.  Open the new port and close the former one in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --service cockpit --permanent --add-port=<4488>/tcp
    # firewall-cmd --service cockpit --permanent --remove-port=9090/tcp
    ```

3.  Create an override file for the `cockpit.socket`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl edit cockpit.socket
    ```

4.  The editor opens an empty `override.conf`{.literal} file in the `/etc/systemd/system/cockpit.socket.d/`{.literal} directory. Change the default port to the previously picked number by adding the following lines:

    ``` {.language-plaintext tabindex="-1"}
    [Socket]
    ListenStream=
    ListenStream=<4488>
    ```

    The first `ListenStream=`{.literal} directive with an empty value resets the list and disables the default port 9090 from the original unit. You can declare multiple `ListenStream`{.literal} directives in a single socket unit.

    Important

    Insert the previous code snippet between the lines starting with `# Anything between here`{.literal} and `# Lines below this`{.literal}. Otherwise, the system discards your changes.

5.  Save the changes, and exit the editor.

6.  Reload the changed configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

7.  Check that your configuration is working:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl show cockpit.socket -p Listen
    Listen=[::]:4488 (Stream)
    ```

8.  Restart `cockpit.socket`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart cockpit.socket
    ```

**Verification**

-   Open your web browser, and access the web console on the updated port, for example:

    ``` {.language-plaintext tabindex="-1"}
    https://machine1.example.com:4488
    ```

## [Chapter 2. Installing and configuring web console by using RHEL system roles](#installing-and-configuring-web-console-by-using-rhel-system-roles) {#chapter-2.-installing-and-configuring-web-console-by-using-rhel-system-roles .title}

With the `cockpit`{.literal} RHEL system role, you can automatically deploy and enable the web console on multiple RHEL systems.

### [2.1. Installing the web console by using the cockpit RHEL system role](#installing-the-web-console-by-using-the-cockpit-rhel-system-role) {#installing-the-web-console-by-using-the-cockpit-rhel-system-role .title}

You can use the `cockpit`{.literal} system role to automate installing and enabling the RHEL web console on multiple systems.

Use the `cockpit`{.literal} system role to:

-   Install the RHEL web console.
-   Allow the `firewalld`{.literal} and `selinux`{.literal} system roles to configure the system for opening new ports.
-   Set the web console to use a certificate from the `ipa`{.literal} trusted certificate authority instead of using a self-signed certificate.

Note

You do not have to call the `firewall`{.literal} or `certificate`{.literal} system roles in the playbook to manage the firewall or create the certificate. The `cockpit`{.literal} system role calls them automatically as needed.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage the RHEL web console
      hosts: managed-node-01.example.com
      tasks:
        - name: Install RHEL web console
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.cockpit
          vars:
            cockpit_packages: default
            cockpit_port: 9090
            cockpit_manage_selinux: true
            cockpit_manage_firewall: true
            cockpit_certificates:
              - name: /etc/cockpit/ws-certs.d/01-certificate
                dns: ['localhost', 'www.example.com']
                ca: ipa
    ```

    The settings specified in the example playbook include the following:

    `cockpit_manage_selinux: true`{.literal}
    :   Allow using the `selinux`{.literal} system role to configure SELinux for setting the correct port permissions on the `websm_port_t`{.literal} SELinux type.

    `cockpit_manage_firewall: true`{.literal}
    :   Allow the `cockpit`{.literal} system role to use the `firewalld`{.literal} system role for adding ports.

    `cockpit_certificates: <YAML_dictionary>`{.literal}

    :   By default, the RHEL web console uses a self-signed certificate. Alternatively, you can add the `cockpit_certificates`{.literal} variable to the playbook and configure the role to request certificates from an IdM certificate authority (CA) or to use an existing certificate and private key that is available on the managed node.

        For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.cockpit/README.md`{.literal} file on the control node.

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

-   Open a web browser and access `https://managed-node-01.example.com:9090`{.literal}. The web console login page is displayed.

**Additional resources**

-   [Requesting certificates from a CA and creating self-signed certificates by using RHEL system roles](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/requesting-certificates-from-a-ca-and-creating-self-signed-certificates-by-using-rhel-system-roles)

## [Chapter 3. Installing web console add-ons and creating custom pages](#installing-web-console-add-ons-and-creating-custom-pages) {#chapter-3.-installing-web-console-add-ons-and-creating-custom-pages .title}

You can add additional **available** applications to the web console or create custom pages to extend its functionality for your use case.

### [3.1. Add-on applications for the RHEL web console](#add-ons-for-the-rhel-web-console) {#add-on-applications-for-the-rhel-web-console .title}

Install optional add-on applications for the RHEL web console by using either the **Applications page** in the console or the command line. These add-ons provide tools for specific management tasks.

You can install add-on applications by using one of the following methods:

1.  In the web console, click **Applications** and use the Install button in the list of available and already-installed applications.

2.  On the command line, use the `dnf install`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install <add-on>
    ```

    In the previous command, replace *\<add-on\>* by a package name from the list of available add-on applications for the RHEL web console.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Feature name                                                                                                                                                                                                                                                                                                                                                                                                                                           | Package name                                                      | Usage                                                                                                                                                                                                                                                                                                                                                                                                   |
+:=======================================================================================================================================================================================================================================================================================================================================================================================================================================================+:==================================================================+:========================================================================================================================================================================================================================================================================================================================================================================================================+
| File manager                                                                                                                                                                                                                                                                                                                                                                                                                                           | `cockpit-files`{.literal}                                         | Managing files and directories in the standard web console interface                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HA cluster management                                                                                                                                                                                                                                                                                                                                                                                                                                  | `cockpit-ha-cluster`{.literal} [^\[a\]^](#ftn.idm139679037014000) | The `pcsd`{.literal} Web UI for configuring Red Hat High Availability clusters                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Image builder                                                                                                                                                                                                                                                                                                                                                                                                                                          | `cockpit-image-builder`{.literal}                                 | Building customized operating system images                                                                                                                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Machines                                                                                                                                                                                                                                                                                                                                                                                                                                               | `cockpit-machines`{.literal}                                      | Managing `libvirt`{.literal} virtual machines                                                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PackageKit                                                                                                                                                                                                                                                                                                                                                                                                                                             | `cockpit-packagekit`{.literal}                                    | Software updates and application installation (usually installed by default)                                                                                                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PCP                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `cockpit-pcp`{.literal}                                           | Persistent and more fine-grained performance data (installed on-demand from the UI)                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Podman                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `cockpit-podman`{.literal}                                        | [Managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/managing-containers-by-using-the-rhel-web-console) and [managing container images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/managing-container-images-by-using-the-rhel-web-console) |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Session recording                                                                                                                                                                                                                                                                                                                                                                                                                                      | `cockpit-session-recording`{.literal}                             | Recording and managing user sessions                                                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Storage                                                                                                                                                                                                                                                                                                                                                                                                                                                | `cockpit-storaged`{.literal}                                      | Managing storage through `udisks`{.literal}                                                                                                                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [^\[a\]^](#idm139679037014000) Additional steps such as enabling the `pcsd`{.literal} service might be required. See the [Installing cluster software](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/creating-high-availability-cluster#installing-cluster-software) section in the Configuring and managing high availability clusters document for more information. |                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

### [3.2. Creating new pages in the web console](#creating-new-pages-in-the-web-console) {#creating-new-pages-in-the-web-console .title}

You can create custom pages in the RHEL web console by adding a package directory containing HTML and JavaScript files to integrate customized functions and interfaces into the web console.

For detailed information, see [Creating Plugins for the Cockpit User Interface](https://cockpit-project.org/blog/creating-plugins-for-the-cockpit-user-interface.html) and the [Cockpit Packages](https://cockpit-project.org/guide/latest/packages.html) section in the [Cockpit Project Developer Guide](https://cockpit-project.org/guide/latest/development.html).

### [3.3. Overriding the manifest settings in the web console](#overriding-the-manifest-settings-in-the-web-console) {#overriding-the-manifest-settings-in-the-web-console .title}

You can modify the RHEL web console menu structure for all users or a specific user by overriding the default manifest settings. Create an override to adjust the visibility or order of menu items.

In the `cockpit`{.literal} project, a package name is a directory name. A package contains the `manifest.json`{.literal} file along with other files. Default settings are present in the `manifest.json`{.literal} file. You can override the default `cockpit`{.literal} menu settings by creating a *`<package_name>`{.literal}*`.override.json`{.literal} file at a specific location for the specified user.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

**Procedure**

1.  Override manifest settings in the *`<systemd>`{.literal}*`.override.json`{.literal} file in a text editor of your choice, for example:

    a.  To edit for all users, enter:

        ``` {.language-plaintext tabindex="-1"}
        # vi /etc/cockpit/<systemd>.override.json
        ```

    b.  To edit for a single user, enter:

        ``` {.language-plaintext tabindex="-1"}
        # vi ~/.config/cockpit/<systemd>.override.json
        ```

2.  Edit the required file with the following details:

    ``` {.language-plaintext tabindex="-1"}
    {
      "menu": {
      "services": null,
      "logs": {
          "order": -1
      }
     }
    }
    ```

    -   The `null`{.literal} value hides the **services** tab
    -   The `-1`{.literal} value moves the **logs** tab to the first place.

3.  Restart the `cockpit`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart cockpit.service
    ```

**Verification**

-   Log in to the web console and verify that the menu reflects your overrides. For the example configuration, the **Logs** tab is displayed first and the **Services** tab is hidden.

**Additional resources**

-   [Manifest overrides](https://cockpit-project.org/guide/latest/packages.html#package-manifest-override)

## [Chapter 4. Managing subscriptions in the web console](#managing-subscriptions-in-the-web-console) {#chapter-4.-managing-subscriptions-in-the-web-console .title}

You can manage your Red Hat product subscriptions in the Red Hat Enterprise Linux 10 web console. This functionality provides a graphical interface for viewing, registering, and managing system subscriptions.

### [4.1. Prerequisites](#prerequisites) {#prerequisites .title}

-   Your Red Hat Customer Portal login or a subscription activation key.

### [4.2. Subscription management in the web console](#subscription-management-in-the-web-console) {#subscription-management-in-the-web-console .title}

You can use the RHEL web console as a graphical interface for Red Hat Subscription Manager on your local system. This simplifies the process of registering, managing, and viewing attached subscriptions.

The Subscription Manager connects to the Red Hat Customer Portal and verifies available:

-   Active subscriptions
-   Expired subscriptions
-   Renewed subscriptions

If you want to renew the subscription or get a different one on the Red Hat Customer Portal, you do not have to update the Subscription Manager data manually.

The Subscription Manager synchronizes data with the Red Hat Customer Portal automatically.

**Additional resources**

-   [Red Hat Customer Portal](https://access.redhat.com)

### [4.3. Registering subscriptions with credentials in the web console](#registering-subscriptions-with-credentials-in-the-web-console) {#registering-subscriptions-with-credentials-in-the-web-console .title}

You can register your RHEL system and attach subscriptions by using your Red Hat Customer Portal credentials directly in the web console.

**Prerequisites**

-   A valid user account on the [Red Hat Customer Portal](https://access.redhat.com).

    See the [Create a Red Hat Login](https://www.redhat.com/wapps/ugc/register.html) page.

-   An active subscription for your RHEL system.

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  In the **Health** filed in the **Overview** page, click the **Not registered** warning, or click **Subscriptions** in the main menu to move to page with your subscription information.

3.  In the **Overview** field, click Register.

4.  In the **Register system** dialog box, select **Account** to register by using your account credentials.

5.  Enter your username.

6.  Enter your password.

7.  Optional: Enter your organization's name or ID.

    If your account belongs to more than one organization on the Red Hat Customer Portal, you must add the organization name or organization ID. To get the org ID, go to your Red Hat contact point.

    -   If you do not want to connect your system to Red Hat Lightspeed, clear the **Insights** checkbox.

8.  Click Register.

**Verification**

-   Navigate to the **Overview** page and check that the **Health** field displays **Registered**.

### [4.4. Registering subscriptions with activation keys in the web console](#registering-subscriptions-with-activation-keys-in-the-web-console) {#registering-subscriptions-with-activation-keys-in-the-web-console .title}

You can register a newly installed Red Hat Enterprise Linux with an activation key in the RHEL web console.

**Prerequisites**

-   An activation key of your Red Hat product subscription.

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  In the **Health** field on the **Overview** page, click the **Not registered** warning, or click **Subscriptions** in the main menu to move to the page with your subscription information.

    .

3.  In the **Overview** filed, click Register.

4.  In the **Register system** dialog box, select **Activation key** to register using an activation key.

5.  Enter your key or keys.

6.  Enter your organization's name or ID.

    To get the organization ID, go to your Red Hat contact point.

    -   If you do not want to connect your system to Red Hat Lightspeed, clear the **Insights** checkbox.

7.  Click Register.

**Verification**

-   Navigate to the **Overview** page and check that the **Health** field displays **Registered**.

## [Chapter 5. Managing remote systems in the web console](#managing-remote-systems-in-the-web-console) {#chapter-5.-managing-remote-systems-in-the-web-console .title}

You can connect to remote systems and manage them in the Red Hat Enterprise Linux web console to monitor and administer systems across your network from a single interface.

For security reasons, use the following network configuration of remote systems managed by the web console:

-   Configure one system as a bastion host. The bastion host is a system with an opened HTTPS port.
-   All other systems communicate through SSH.

With the web interface running on the bastion host, you can reach all other systems through the SSH protocol.

### [5.1. Connecting to a remote host using SSH from the web console login page](#connecting-to-a-remote-host-using-ssh-from-the-web-console-login-page) {#connecting-to-a-remote-host-using-ssh-from-the-web-console-login-page .title}

You can connect to a remote system by using the SSH protocol directly from the login page of the RHEL web console. After you log in remotely, connection traffic is encrypted, and you can manage the remote system in the graphical interface of the web console.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

-   The `cockpit-system`{.literal} package is installed on the remote system.

-   The `sshd`{.literal} service runs on the remote system, and the corresponding port is allowed in the firewall.

**Procedure**

1.  Open the web console login page.

2.  Specify the username on the remote host in the **User name** field.

3.  Click **Other options** to reveal the **Connect to** text field.

4.  Specify the remote host you want to connect to using SSH in the **Connect to** text field. If you do not specify any port, the web console attempts to connect to port 22 on the specified remote host.

5.  Click **Log in**.

**Verification**

-   Verify that the web console displays the **Overview** page of the remote host.

### [5.2. Adding remote hosts to the web console](#adding-remote-hosts-to-the-web-console) {#adding-remote-hosts-to-the-web-console .title}

When logged in to the RHEL web console, you can switch between the local system and multiple remote hosts through the host switcher. You can connect to and manage a remote system after you add its credentials.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

**Procedure**

1.  On the command line, open or create the `cockpit.conf`{.literal} file in the `/etc/cockpit/`{.literal} directory in a text editor of your preference.

2.  Add the following text:

    ``` {.language-plaintext tabindex="-1"}
    [WebService]
    AllowMultiHost=yes
    ```

    Warning

    The host switcher is deprecated and disabled by default. Also, due to technical limitations, this feature is not secure. Do not enable the host switcher if you want to connect to untrusted hosts because all connected systems can make arbitrary changes to the rest of the connected systems. As a secure alternative, use the web console login page with the limit of one host per browser session, or use the Cockpit Client Flatpak.

3.  Save the file.

4.  Restart the web console to ensure the changes take effect.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl try-restart cockpit
    ```

5.  In the RHEL web console, click *`<username>`{.literal}*`@`{.literal}*`<hostname>`{.literal}* in the top left corner of the **Overview** page.

6.  In the drop-down menu, click Add new host.

7.  In the **Add new host** dialog box, specify the host you want to add.

8.  Optional: Add the username for the account you want to connect to.

    You can use any user account of the remote system. However, if you use the credentials of a user account without administration privileges, you cannot perform administration tasks.

    If you use the same credentials as on your local system, the web console authenticates remote systems automatically every time you log in.

    Important

    The web console does not save passwords used to log in to remote systems.

9.  Optional: Click the **Color** field to change the color of the system.

10. Click Add.

**Verification**

-   The new host is listed in the *`<username>`{.literal}*`@`{.literal}*`<hostname>`{.literal}* drop-down menu.

### [5.3. Enabling SSH login for a new host](#enabling-ssh-login-for-a-new-host) {#enabling-ssh-login-for-a-new-host .title}

You can enable secure SSH login for a new remote host that uses key-based authentication in the RHEL web console.

If you already have an SSH key on your system, the web console uses the existing one; otherwise, it can create a key.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](#installing-and-enabling-the-web-console "1.2. Installing and enabling the web console").

-   You considered security risks and enabled the host switcher.

    See [Adding remote hosts to the web console](#adding-remote-hosts-to-the-web-console "5.2. Adding remote hosts to the web console") for more information.

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  In the RHEL web console, click *`<username>`{.literal}*`@`{.literal}*`<hostname>`{.literal}* in the top left corner of the **Overview** page.

3.  In the drop-down menu, click Add new host.

4.  In the **Add new host** dialog box, specify the host you want to add. If you connect to the host for the first time, you must click Trust and add new host in the following dialog box.

5.  The password dialog box differs depending on the existence of an SSH key file on the host:

    a.  If you already have the SSH key for the host, select the **Authorize SSH key** option.
    b.  If you do not have the SSH key, select the **Create a new SSH key and authorize it** option. The web console creates the key.

6.  Add and confirm a password for the SSH key.

7.  Click Log in.

**Verification**

1.  Log out.
2.  Log back in.
3.  Click Log in in the **Not connected to host** screen.
4.  Select **SSH key** as your authentication option.
5.  Enter your key password.
6.  Click Log in.

**Additional resources**

-   [Using secure communications between two systems with OpenSSH](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/securing_networks/using-secure-communications-between-two-systems-with-openssh)

### [5.4. Configuring smart-card authentication for SSH logins in the web console](#configuring-smart-card-authentication-for-ssh-logins-in-the-web-console) {#configuring-smart-card-authentication-for-ssh-logins-in-the-web-console .title}

After logging in to a user account on the RHEL web console, you can connect to remote machines by using the SSH protocol. You can use the constrained delegation feature to use SSH without being asked to authenticate again.

In this example, the web console session runs on `myhost.idm.example.com`{.literal}. Configure the console to access `remote.idm.example.com`{.literal} by using SSH on behalf of the authenticated user.

**Prerequisites**

-   You have obtained an IdM `admin`{.literal} ticket-granting ticket (TGT) on `myhost.idm.example.com`{.literal}.
-   You have `root`{.literal} access to `remote.idm.example.com`{.literal}.
-   The host that runs the web console is a member of an IdM domain.

**Procedure**

1.  In the **Terminal** page, verify that the web console has created a Service for User to Proxy (S4U2proxy) Kerberos ticket in the user session:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    …
    Valid starting     Expires            Service principal
    05/20/25 09:19:06 05/21/25 09:19:06 HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
    …
    ```

2.  Create a list of the target hosts that the delegation rule can access:

    a.  Create a service delegation target:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationtarget-add cockpit-target
        ```

    b.  Add the target host to the delegation target:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationtarget-add-member cockpit-target \
          --principals=host/remote.idm.example.com@IDM.EXAMPLE.COM
        ```

3.  Allow `cockpit`{.literal} sessions to access the target host list by creating a service delegation rule and adding the HTTP service Kerberos principal to it:

    a.  Create a service delegation rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationrule-add cockpit-delegation
        ```

    b.  Add the web console client to the delegation rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationrule-add-member cockpit-delegation \
          --principals=HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
        ```

    c.  Add the delegation target to the delegation rule:

        ``` {.language-plaintext tabindex="-1"}
        $ ipa servicedelegationrule-add-target cockpit-delegation \
          --servicedelegationtargets=cockpit-target
        ```

4.  Enable Kerberos authentication on the `remote.idm.example.com`{.literal} host:

    a.  Connect through SSH to `remote.idm.example.com`{.literal} as `root`{.literal}.
    b.  Add the `GSSAPIAuthentication yes`{.literal} line to the `/etc/ssh/sshd_config`{.literal} file.

5.  Restart the `sshd`{.literal} service on `remote.idm.example.com`{.literal} so that the changes take effect immediately:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl try-restart sshd.service
    ```

**Verification**

-   In the web console, navigate to the **Terminal** page and connect to the remote host by using SSH. If the constrained delegation is configured correctly, no additional authentication is required:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh remote.idm.example.com
    ```

**Additional resources**

-   [Logging in to the web console with smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users#logging-in-to-the-web-console-with-smart-cards)
-   [Constrained delegation in Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-constrained-delegation-in-idm#constrained-delegation-in-identity-management)

### [5.5. Using Ansible to configure smart-card authentication for SSH logins in the web console](#using-ansible-to-configure-smart-card-authentication-for-SSH-logins-in-the-web-console) {#using-ansible-to-configure-smart-card-authentication-for-ssh-logins-in-the-web-console .title}

After logging in to the web console, you can connect to remote machines by using the SSH protocol. You can use the `servicedelegation*`{.literal} Ansible modules to configure the web console for the constrained delegation feature to allow SSH connections without additional authentication.

In this example, the web console session runs on `myhost.idm.example.com`{.literal}. You configure it to access `remote.idm.example.com`{.literal} by using SSH on behalf of the authenticated user.

**Prerequisites**

-   You have obtained an IdM `admin`{.literal} ticket-granting ticket (TGT) on `myhost.idm.example.com`{.literal}.

-   You have `root`{.literal} access to `remote.idm.example.com`{.literal}.

-   The host that runs the web console is a member of an IdM domain.

-   You have configured your Ansible control node to meet the following requirements:

    -   You have installed the `ansible-freeipa`{.literal} package.

    -   The example assumes you have created an Ansible inventory file with the fully-qualified domain name (FQDN) of the IdM server in the `~/`{.literal}*`MyPlaybooks`{.literal}*`/`{.literal} directory.

    -   The example assumes that the `secret.yml`{.literal} Ansible vault stores the admin password in the `ipaadmin_password`{.literal} variable.

        See the `/usr/share/doc/ansible-freeipa/playbooks/servicedelegationtarget`{.literal} and `/usr/share/doc/ansible-freeipa/playbooks/servicedelegationrule`{.literal} directories for example playbooks and the `README-servicedelegationrule.md`{.literal} and `README-servicedelegationtarget.md`{.literal} files in the `/usr/share/doc/ansible-freeipa/`{.literal} directory for more information.

-   The target node, that is the node on which the `ansible-freeipa`{.literal} module runs, is part of the IdM domain as an IdM client, server, or replica.

**Procedure**

1.  Navigate to your `~/`{.literal}*`MyPlaybooks`{.literal}*`/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cd ~/MyPlaybooks/
    ```

2.  Store your sensitive variables in an encrypted file:

    a.  Create the vault:

        ``` {.language-plaintext tabindex="-1"}
        $ ansible-vault create secret.yml
        New Vault password: <vault_password>
        Confirm New Vault password: <vault_password>
        ```

    b.  After the `ansible-vault create`{.literal} command opens an editor, enter the sensitive data in the *`<key>`{.literal}*`: `{.literal}*`<value>`{.literal}* format:

        ``` {.language-plaintext tabindex="-1"}
        ipaadmin_password: <admin_password>
        ```

    c.  Save the changes, and close the editor. Ansible encrypts the data in the vault.

3.  In the **Terminal** page, verify that the web console has created a Service for User to Proxy (S4U2proxy) Kerberos ticket in the user session:

    ``` {.language-plaintext tabindex="-1"}
    $ klist
    …
    Valid starting     Expires            Service principal
    05/20/25 09:19:06 05/21/25 09:19:06 HTTP/myhost.idm.example.com@IDM.EXAMPLE.COM
    …
    ```

4.  Create a `web-console-smart-card-ssh.yml`{.literal} playbook with the following content:

    a.  Create a task that ensures the presence of a delegation target:

        ``` {.language-yaml tabindex="-1"}
        ---
        - name: Playbook to create a constrained delegation target
          hosts: ipaserver

          vars_files:
          - /home/user_name/MyPlaybooks/secret.yml
          tasks:
          - name: Ensure servicedelegationtarget web-console-delegation-target is present
            ipaservicedelegationtarget:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-target
        ```

    b.  Add a task that adds the target host to the delegation target:

        ``` {.language-yaml tabindex="-1"}
          - name: Ensure servicedelegationtarget web-console-delegation-target member principal host/remote.idm.example.com@IDM.EXAMPLE.COM is present
            ipaservicedelegationtarget:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-target
              principal: host/remote.idm.example.com@IDM.EXAMPLE.COM
              action: member
        ```

    c.  Add a task that ensures the presence of a delegation rule:

        ``` {.language-yaml tabindex="-1"}
          - name: Ensure servicedelegationrule delegation-rule is present
            ipaservicedelegationrule:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-rule
        ```

    d.  Add a task that ensures that the Kerberos principal of the web console client service is a member of the constrained delegation rule:

        ``` {.language-yaml tabindex="-1"}
          - name: Ensure the Kerberos principal of the web console client service is added to the servicedelegationrule web-console-delegation-rule
            ipaservicedelegationrule:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-rule
              principal: HTTP/myhost.idm.example.com
              action: member
        ```

    e.  Add a task that ensures that the constrained delegation rule is associated with the web-console-delegation-target delegation target:

        ``` {.language-yaml tabindex="-1"}
          - name: Ensure a constrained delegation rule is associated with a specific delegation target
            ipaservicedelegationrule:
              ipaadmin_password: "{{ ipaadmin_password }}"
              name: web-console-delegation-rule
              target: web-console-delegation-target
              action: member
        ```

    f.  Add a task that enable Kerberos authentication on `remote.idm.example.com`{.literal}:

        ``` {.language-yaml tabindex="-1"}
          - name: Enable Kerberos authentication
            hosts: remote.idm.example.com
            vars:
              sshd_config:
                GSSAPIAuthentication: true
            roles:
              - role: rhel-system-roles.sshd
        ```

5.  Save the file.

6.  Run the Ansible Playbook. Specify the playbook file, the file storing the password protecting the `secret.yml`{.literal} file, and the inventory file:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --vault-password-file=password_file -v -i inventory web-console-smart-card-ssh.yml
    ```

**Verification**

-   In the web console, navigate to the **Terminal** page and connect to the remote host by using SSH. If the constrained delegation is configured correctly, no additional authentication is required:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh remote.idm.example.com
    ```

**Additional resources**

-   [Logging in to the web console with smart cards](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users#logging-in-to-the-web-console-with-smart-cards)
-   [Constrained delegation in Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_ansible_to_install_and_manage_identity_management_in_rhel/using-constrained-delegation-in-idm#constrained-delegation-in-identity-management)

## [Chapter 6. Configuring SSO authentication for the RHEL web console in the IdM domain](#configuring-sso-authentication-for-the-rhel-web-console-in-the-idm-domain) {#chapter-6.-configuring-sso-authentication-for-the-rhel-web-console-in-the-idm-domain .title}

Configure Single Sign-On (SSO) authentication for the RHEL web console by using Identity Management (IdM). With SSO enabled, IdM users with a Kerberos ticket can access the web console without re-entering credentials.

You can use Single Sign-on (SSO) authentication provided by Identity Management (IdM) in the RHEL web console to have the following advantages:

-   IdM domain administrators can use the web console to manage local systems.
-   Users with a Kerberos ticket in the IdM domain do not have to provide login credentials to access the web console.
-   All hosts known to the IdM domain are accessible through SSH from the local instance of the web console.
-   Certificate configuration is not necessary. The console's web server automatically switches to a certificate issued by the IdM certificate authority and accepted by browsers.

Configuring SSO for logging into the web console requires:

1.  You must add systems to the IdM domain by using the web console.
2.  If you want to use Kerberos for authentication, you must obtain a Kerberos ticket on your systems.
3.  Allow administrators on the IdM server to use any command on any host.

### [6.1. Joining a RHEL system to an IdM domain using the web console](#joining-a-rhel-system-to-an-idm-domain-using-the-web-console) {#joining-a-rhel-system-to-an-idm-domain-using-the-web-console .title}

You can join a RHEL system to an IdM domain directly in the RHEL web console to integrate the system into the centralized identity management environment and allow IdM users to log in.

**Prerequisites**

-   The IdM domain is running and reachable from the client you want to join.

-   You have the IdM domain administrator credentials.

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.
2.  In the **Configuration** field of the **Overview** tab click **Join Domain**.
3.  In the **Join a Domain** dialog box, enter the hostname of the IdM server in the **Domain Address** field.
4.  In the **Domain administrator name** field, enter the username of the IdM administration account.
5.  In the **Domain administrator password**, add a password.
6.  Click Join.

**Verification**

1.  If the RHEL 10 web console does not display an error, the system joined to the IdM domain and you can see the domain name in the **System** screen.

2.  To verify that the user is a member of the domain, click the **Terminal** page and type the `id`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ id
    ```

    ``` {.language-plaintext tabindex="-1"}
    euid=548800004(example_user) gid=548800004(example_user) groups=548800004(example_user) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
    ```

**Additional resources**

-   [Planning Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/planning_identity_management)
-   [Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management)
-   [Managing IdM users, groups, hosts, and access control rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_idm_users_groups_hosts_and_access_control_rules)

### [6.2. Logging in to the web console using Kerberos authentication](#logging-in-to-the-web-console-using-kerberos-authentication) {#logging-in-to-the-web-console-using-kerberos-authentication .title}

You can log in to the RHEL web console by using Kerberos authentication. If you already have a valid Kerberos ticket from your IdM domain, you can access the console without re-entering your password.

Important

With SSO, you usually do not have any administrative privileges in the web console. This only works if you configure passwordless `sudo`{.literal}. The web console does not prompt for a `sudo`{.literal} password interactively.

**Prerequisites**

-   IdM domain running and reachable in your company environment.

    For details, see [Joining a RHEL system to an IdM domain by using the web console](#joining-a-rhel-system-to-an-idm-domain-using-the-web-console "6.1. Joining a RHEL system to an IdM domain using the web console").

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   If the system does not use a Kerberos ticket managed by the SSSD client, request the ticket with the `kinit`{.literal} utility manually.

**Procedure**

-   Log in to the RHEL web console by entering the following URL in your web browser:

    ``` {.language-plaintext tabindex="-1"}
    https://<dns_name>:9090
    ```

**Verification**

-   After a successful login, the web console displays the **Overview** page without prompting for a password.

## [Chapter 7. Configuring smart card authentication with the web console for centrally managed users](#configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users) {#chapter-7.-configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users .title}

Configure smart card authentication for centrally managed users in the RHEL web console. This security measure helps to provide physical access control for administrative and regular users.

You can configure smart card authentication in the RHEL web console for users who are centrally managed by:

-   Identity Management
-   Active Directory which is connected in the cross-forest trust with Identity Management

### [7.1. Prerequisites](#prerequisites_2) {#prerequisites-1 .title}

-   The system for which you want to use the smart card authentication must be a member of an Active Directory or Identity Management domain.
-   The certificate used for the smart card authentication must be associated with a particular user in Identity Management or Active Directory.

### [7.2. Smart-card authentication for centrally managed users](#smart-card-authentication-for-centrally-managed-users) {#smart-card-authentication-for-centrally-managed-users .title}

Use smart-card authentication to provide strong authentication for centrally managed users. This method links the user account to a physical credential, enhancing security for systems within the Identity Management domain.

A smart card is a physical device, which can provide personal authentication by using certificates stored on the card. Personal authentication means that you can use smart cards in the same way as user passwords.

You can store user credentials on the smart card in the form of a private key and a certificate. Special software and hardware is used to access them. You insert the smart card into a reader or a USB socket and supply the PIN code for the smart card instead of providing your password.

Identity Management (IdM) supports smart-card authentication with user certificates issued by the Active Directory Certificate Service (ADCS) certificate authority.

**Additional resources**

-   [Configuring certificates issued by ADCS for smart card authentication in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/configuring-certificates-issued-by-adcs-for-smart-card-authentication-in-idm)
-   [Smart-card support in RHEL 8 and later (Red Hat Knowledgebase)](https://access.redhat.com/articles/4253861)

### [7.3. Enabling smart-card authentication for the web console](#enabling-smart-card-authentication-for-the-web-console) {#enabling-smart-card-authentication-for-the-web-console .title}

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

### [7.4. Logging in to the web console with smart cards](#logging-in-to-the-web-console-with-smart-cards) {#logging-in-to-the-web-console-with-smart-cards .title}

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

### [7.5. Enabling passwordless sudo authentication for smart-card users](#enabling-passwordless-sudo-authentication-for-smart-card-users) {#enabling-passwordless-sudo-authentication-for-smart-card-users .title}

You can enable passwordless `sudo`{.literal} authentication for smart-card users to allow them to perform administrative tasks without entering a password, improving operational efficiency and security.

Alternatively, if you use RHEL Identity Management, you can declare the initial web console certificate as trusted for authentication with `sudo`{.literal}, SSH, or other services. The web console automatically creates an S4U2Proxy Kerberos ticket in the user session for this purpose.

In the following example, the web console session runs on `host.example.com`{.literal} and is trusted to access its own host with `sudo`{.literal}. Additionally, the example steps add a second trusted host - `remote.example.com`{.literal}.

**Prerequisites**

-   Identity Management is installed.
-   Active Directory is connected in the cross-forest trust with Identity Management.
-   Your smart card is configured to log in to the web console. See [Configuring smart-card authentication with the web console for centrally managed users](#configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users "Chapter 7. Configuring smart card authentication with the web console for centrally managed users") for more information.

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

### [7.6. Limiting user sessions and memory to prevent a DoS attack](#limiting-user-sessions-and-memory-to-prevent-a-dos-attack) {#limiting-user-sessions-and-memory-to-prevent-a-dos-attack .title}

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

### [7.7. Additional resources](#configuring-smart-card-authentication-with-the-web-console-for-centrally-managed-users_77-additional-resources) {#additional-resources .title}

-   [Joining a RHEL system to an IdM domain by using the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/configuring-sso-authentication-for-the-rhel-web-console-in-the-idm-domain)
-   [Adding a certificate to a user entry in the IdM Web UI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#adding-a-certificate-to-a-user-entry-in-the-idm-web-ui)
-   [Adding a certificate to a user entry in the IdM CLI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_smart_card_authentication/configuring-identity-management-for-smart-card-authentication#adding-a-certificate-to-a-user-entry-in-the-idm-cli)

## [Chapter 8. Satellite host management and monitoring in the web console](#satellite-host-management-and-monitoring-in-the-web-console) {#chapter-8.-satellite-host-management-and-monitoring-in-the-web-console .title}

After enabling RHEL web console integration on a Red Hat Satellite Server, you can manage many hosts at scale in the web console.

Red Hat Satellite is a system management solution for deploying, configuring, and maintaining your systems across physical, virtual, and cloud environments. Satellite provides provisioning, remote management and monitoring of multiple Red Hat Enterprise Linux deployments with a centralized tool.

By default, RHEL web console integration is disabled in Red Hat Satellite. To access RHEL web console features for your hosts from within Red Hat Satellite, you must first enable RHEL web console integration on a Red Hat Satellite Server.

To enable the RHEL web console on your Satellite Server, enter the following command as `root`{.literal}:

``` {.language-plaintext tabindex="-1"}
# satellite-installer --enable-foreman-plugin-remote-execution-cockpit --reset-foreman-plugin-remote-execution-cockpit-ensure
```

**Additional resources**

-   [Host management and monitoring by using the RHEL web console in the Managing hosts in Red Hat Satellite guide](https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html/managing_hosts/host-management-and-monitoring-by-using-cockpit)

## [Legal Notice](#idm139679037504752) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
