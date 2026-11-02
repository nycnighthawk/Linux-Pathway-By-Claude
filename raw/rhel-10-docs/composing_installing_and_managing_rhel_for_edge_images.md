---
{"title": "Composing, installing, and managing RHEL for Edge images", "guide": "composing_installing_and_managing_rhel_for_edge_images", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/composing_installing_and_managing_rhel_for_edge_images/index", "retrieved": "2026-11-02", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Composing, installing, and managing RHEL for Edge images {#composing-installing-and-managing-rhel-for-edge-images .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Creating, deploying, and managing Edge systems with RHEL 10 {#creating-deploying-and-managing-edge-systems-with-rhel-10 .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140016714671696)

**Abstract**

You can use image mode for RHEL to build operating system images suitable for your edge deployments. Then, you can remotely install, and securely manage and scale deployments of the images on Edge servers.

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

## [Chapter 1. Introducing RHEL for Edge images](#introducing-rhel-for-edge-images) {#chapter-1.-introducing-rhel-for-edge-images .title}

A RHEL for Edge image uses an `rpm-ostree`{.literal} image. It includes system packages that you need to remotely install RHEL on remote edge servers.

The system packages include:

-   `Base OS`{.literal} package
-   Podman is the container engine
-   Additional RPM Package Manager (RPM) content

In contrast with standard RHEL, RHEL for Edge is an immutable operating system. The root directory is `read-only`{.literal}, and the system provides the following features:

-   Packages are isolated from the root directory.
-   Each operating system version is a separate deployment. You can roll back to a previous deployment of the system at any time.
-   Offers efficient updates over the network.
-   Supports multiple operating system branches and repositories.
-   Contains a hybrid `rpm-ostree`{.literal} package system.

You can deploy a RHEL for Edge image on Bare Metal, Appliance, and edge servers.

As a result, a RHEL for Edge image provides the following benefits:

Atomic upgrades
:   Updates are staged in an isolated background environment, which ensures that the active system remains unchanged. You have full visibility into the update's readiness, but no changes take effect until a reboot triggers the switch to the new version.

Custom health checks and intelligent rollbacks
:   You can create custom health checks. If a health check fails, the operating system automatically rolls back to the previous stable state.

Container-focused workflow
:   Applications run in isolated containers, separated from the host operating system. This enables you to update or swap individual workloads in the background without impacting the rest of the system's availability.

Optimized Over-the-Air updates
:   Efficient Over-the-Air (OTA) delta updates keep your systems up-to-date, even with intermittent connectivity.

### [1.1. Difference between RHEL RPM images and RHEL for Edge images](#difference-between-rhel-rpm-images-and-rhel-for-edge-images) {#difference-between-rhel-rpm-images-and-rhel-for-edge-images .title}

You can create RHEL system images in the traditional package-based RPM format or as RHEL for Edge (`rpm-ostree`{.literal}) images. Using traditional package-based RPMs is optimal to deploy RHEL on traditional data centers.

With RHEL for Edge images, you can deploy RHEL on servers other than traditional data centers. These edge servers process large amounts of data close to the source where the data is generated.

The RHEL for Edge (`rpm-ostree`{.literal}) image is not a package manager. It only supports complete bootable file system trees rather than individual files. It does not track the origin of specific files within the image, such as how these files were generated or anything related to their origin.

The `rpm-ostree`{.literal} images use the package manager as a separate mechanism to install applications in the `/var`{.literal} directory. This keeps the core operating system unchanged and also maintains the state of the `/var`{.literal} and `/etc`{.literal} directories. The atomic updates enable rollbacks and background staging of updates.

The following table compares RHEL RPM and RHEL for Edge images:

+:------------------------------------+:---------------------------------------------------------------------------------+:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Key attributes                      | RHEL RPM image                                                                   | RHEL for Edge image                                                                                                                                                                      |
+-------------------------------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `OS assembly`{.literal}             | Assemble packages locally to form an image.                                      | Assemble packages in an OSTree, which you can install on a system.                                                                                                                       |
+-------------------------------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `OS updates`{.literal}              | Use `dnf update`{.literal} to apply available updates from enabled repositories. | Use `rpm-ostree upgrade`{.literal} to stage updates if any new commit is available in the OSTree remote at `/etc/ostree/remotes.d/`{.literal}. The update takes effect on system reboot. |
+-------------------------------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Repository`{.literal}              | The package contains DNF repositories.                                           | The package contains an OSTree remote repository.                                                                                                                                        |
+-------------------------------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `User access permissions`{.literal} | Read and write access.                                                           | Read-only access for `/usr`{.literal}.                                                                                                                                                   |
+-------------------------------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Data persistence`{.literal}        | Mount the image to any non-`tmpfs`{.literal} mount point                         | `/etc`{.literal} & `/var`{.literal} are read and write enabled and include persisting data.                                                                                              |
+-------------------------------------+----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.1. Difference between RHEL RPM images and RHEL for Edge images

Show more

### [1.2. Additional resources](#introducing-rhel-for-edge-images_12-additional-resources) {#additional-resources .title}

-   [Interactively installing RHEL from installation media](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_from_installation_media/index)

## [Chapter 2. Automatically provisioning and onboarding RHEL for Edge devices with FDO client and server](#automatically-provisioning-and-onboarding-rhel-for-edge-devices-with-fdo-client-and-server) {#chapter-2.-automatically-provisioning-and-onboarding-rhel-for-edge-devices-with-fdo-client-and-server .title}

You can use the `go-fdo-client`{.literal} and `go-fdo-server`{.literal} RPMs to deploy a Go-based implementation of the FIDO Device Onboarding (FDO) client and server. This FIDO Device Onboarding protocol version enables secure, automated, zero-touch provisioning of edge devices.

Important

These Go-based implementations are not compatible with the original FDO RPMs and container images that remain in Technology Preview. Do not use the go-fdo-\* packages alongside the fdo-\* packages or containers.

### [2.1. The FDO trust model process overview](#the-fdo-trust-model-process-overview) {#the-fdo-trust-model-process-overview .title}

You can automatically and securely integrate new devices into your Internet of Things (IoT) infrastructure by using FIDO Device Onboarding (FDO). FDO verifies device authenticity, protects the configuration process, and synchronizes each device with your existing infrastructure upon installation.

FDO provides the following capabilities:

-   Provides a zero-touch procedure for onboarding a new device to the owner's management platform at scale.
-   Cryptographically verifies the device's authenticity and ownership before the exchange of sensitive information.
-   Provisions devices across untrusted networks by using a securely encrypted communications channel.
-   Applies ownership credentials and configuration during device onboarding rather than at device manufacture (late binding).

FDO is a two-phase process:

1.  Device initialization: The device manufacturer performs the first phase. During this phase, the manufacturer configures the device to perform onboarding after purchase. On completion of this phase:

    -   The device stores a set of credentials to prove its identity.
    -   The manufacturer creates an ownership voucher, which is a digital document that proves the ownership chain of the device.
    -   The device receives a globally unique identifier (GUID).

2.  Transfer of ownership: The second phase occurs after the device is purchased. During this phase, the device is onboarded to the new owner's infrastructure.

### [2.2. Components of the FDO system](#components-of-the-fdo-system) {#components-of-the-fdo-system .title}

FIDO Device Onboarding (FDO) onboarding employs a device-side client application and three specialized FDO servers: Manufacturing, Rendezvous, and Owner.

Device client

:   This application is installed on the device and performs the following operations:

    -   During device manufacture, the client application initializes the device's FDO state with the help of the Manufacturing server.
    -   When the final owner installs the device, the client application performs the onboarding process in concert with the Rendezvous and Owner FDO servers.

Manufacturing server
:   Deployed at the device manufacturer's site, this server is responsible for the FDO Device Initialization protocol, which prepares the device for the FDO onboarding process and creates the Ownership Voucher. The device client initiates device initialization. Once device initialization completes, the Manufacturing server has no further involvement with the onboarding process.

Rendezvous server
:   To enable late binding of device ownership, which is required when the device's ownership is unknown during manufacturing, the device requires a discovery service at the start of onboarding to securely identify its owner. The Rendezvous server provides this discovery service. The device client contacts the Rendezvous server at the start of the onboarding process to retrieve the network addresses for the Owner server.

Owner server
:   The device owner's organization deploys the Owner server. It is responsible for integrating the new device into the owner's IoT infrastructure. When the device is installed and first booted at the owner's facility, the device client connects to the Owner server and initiates the final phase of onboarding. The FDO onboarding process completes once the Owner server finishes provisioning the device for use.

### [2.3. The FDO workflow](#the-fdo-workflow) {#the-fdo-workflow .title}

The FIDO Device Onboard (FDO) workflow transfers device ownership and operational configuration from the manufacturer to the target owner environment through two primary stages.

-   **Overview of the FDO Lifecycle**

FDO enables zero-touch onboarding by establishing cryptographically verified trust between the device, the manufacturer, and the owner. The onboarding lifecycle transitions the device from initial manufacturing to full operational status without requiring manual field configuration.

-   **Stage 1: Device Initialization (DI Protocol)**

During manufacturing or factory preparation, the device establishes its foundational identity and cryptographic credentials.

Credential Generation
:   The device client contacts the manufacturer server to generate and store secure credentials directly on the device.

Identity Assignment
:   The manufacturer server assigns a globally unique identifier (GUID) to the device.

Ownership Voucher Creation

:   The manufacturer server generates an ownership voucher containing the network address of the rendezvous server (or the Owner server in rendezvous-bypass scenarios). Upon completion, the device is ready for shipment and onboarding.

    -   **Stage 2: On-Site Onboarding (TO0, TO1, and TO2 Protocols)**

Onsite onboarding connects the device to its final owner through a three-part Transfer Ownership (TO) protocol sequence.

Owner Registration (TO0)
:   The server administrator uploads the ownership voucher to the Owner server. The Owner server extracts the rendezvous server address, contacts the rendezvous server to prove ownership, and registers its own network address for device discovery.

Rendezvous Routing (TO1)
:   Upon first boot, the device client retrieves the rendezvous server address from its credentials and connects to it. The rendezvous server locates the device's ownership voucher and redirects the client to the Owner server's network address.

Device Setup and Provisioning (TO2)
:   The device client connects to the Owner server. Both entities authenticate each other using the ownership voucher and device credentials to establish an encrypted channel. The Owner server delivers `ServiceInfo`{.literal} key-value pairs, which the device uses to execute its final configuration and reach an operational state.

### [2.4. Cryptographic credentials for FDO](#fdo-server-installation-and-configuration) {#cryptographic-credentials-for-fdo .title}

To use the FIDO Device Onboarding (FDO) process, you must provide cryptographic credentials, such as certificates and private keys, to meet its security guarantees. The party deploying FDO must provide these certificates; the FDO packages do not provide them.

The FDO protocol operation requires the following certificates and private keys:

Manufacturer certificate and key
:   Issued by the manufacturer. The manufacturer server uses it only during device initialization and does not share it.

Owner certificate and key
:   Issued by the owner organization. The Owner server requires the private key, and the public certificate is provided to the manufacturer server to use when extending the ownership voucher.

Device CA certificate and key
:   Issued by the manufacturer to certify that the device is legitimate. The manufacturer server uses the certificate and private key during device initialization, and the certificate is provided to the Owner server for verifying the device's identity.

TLS certificates
:   All FDO servers support network access by using HTTP. You can configure servers to enable HTTPS for security purposes. If you enable HTTPS, you must provide additional certificates for server authentication. These certificates are separate from the certificates required by FDO. For more information, see the server configuration documentation.

Database support
:   All FDO servers require a database to persist state across restarts. You can configure the FDO servers to use either SQLite or PostgreSQL as the database implementation. For more information about FDO server database configuration, see the server configuration documentation.

### [2.5. Generating test certificates for single-host evaluation](#generating-test-certificates-for-single-host-evaluation) {#generating-test-certificates-for-single-host-evaluation .title}

Generate self-signed test certificates by using the go-fdo-server utility script. This utility is intended for development and testing environments where the Manufacturer, Rendezvous, and Owner servers all reside on the same physical or virtual host.

Warning

These certificates are suitable for testing and demonstration purposes only. They use a shared directory structure that is not suitable for production or distributed environments.

**Prerequisites**

-   RHEL 10 Linux system in image mode (`bootc`{.literal})
-   `go-fdo-server`{.literal} RPMs installed locally: The certificate generation script is a component of the server package
-   Network connectivity between the device and FDO servers

**Procedure**

-   Generate all the required keys and certificate files:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo /usr/libexec/go-fdo-server/generate-go-fdo-server-certs.sh
    ```

    This script writes the generated keys and certificate files into the `/etc/pki/go-fdo-server/`{.literal} directory and sets the appropriate permissions in the following files:

-   `manufacturer-example.key`{.literal}:: The manufacturer private key file.

-   `manufacturer-example.crt`{.literal}:: The manufacturer public certificate file.

-   `owner-example.key`{.literal}: The owner private key file.

-   `owner-example.crt`{.literal}: The owner public certificate file.

-   `device-ca-example.key`{.literal}: The device CA private key file.

-   `device-ca-example.crt`{.literal}: The device CA public certificate file.

**Next steps**

-   Add the required keys and certificate files to the server configurations.

### [2.6. Installing the FDO Manufacturing server](#installing-the-fdo-manufacturing-server) {#installing-the-fdo-manufacturing-server .title}

Install the `go-fdo-server-manufacturer`{.literal} RPM package to deploy the Manufacturing server. This service is responsible for performing device initialization and issuing the initial Device Credential.

**Prerequisites**

-   A registered RHEL 10 system
-   Subscriptions or repositories enabled that include the FDO server packages

**Procedure**

1.  Install the Manufacturing server package:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install go-fdo-server-manufacturer
    ```

2.  Verify that the Manufacturing server's systemd unit file and the default configuration directories were created:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl list-unit-files | grep go-fdo-server-manufacturer
    ```

    ``` {.language-plaintext tabindex="-1"}
    go-fdo-server-manufacturer.service disabled disabled
    ```

3.  Configure certificates by moving the test certificates generated in the previous section to the manufacturer's configuration path.

4.  After configuration, enable and start the service:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl enable --now go-fdo-server-manufacturer
    ```

### [2.7. Configuring the FDO Manufacturing server](#configuring-the-fdo-manufacturing-server) {#configuring-the-fdo-manufacturing-server .title}

Configure the FIDO Device Onboard (FDO) Manufacturing server by modifying the YAML-formatted initialization file and setting the required file permissions. This process ensures the server has the necessary operational parameters and security controls to generate and sign device credentials.

**Prerequisites**

-   You have installed the FDO Manufacturing server RPM packages.
-   You have obtained the required certificates and keys from your issuing organization.
-   You have administrative (`sudo`{.literal}) access to the server.

**Procedure**

1.  Install the required credentials by moving all certificates and keys provided by your organization into the `/etc/pki/go-fdo-server/`{.literal} directory.

2.  Secure the certificate and key files. Restricted permissions are required to protect the integrity of the credentials. Set the ownership and permissions for the private keys so they are accessible only by the `go-fdo-server-manufacturer`{.literal} user:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo chown go-fdo-server-manufacturer:go-fdo-server /etc/pki/go-fdo-server/device-ca.key /etc/pki/go-fdo-server/manufacturer.key
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ sudo chmod 600 /etc/pki/go-fdo-server/device-ca.key /etc/pki/go-fdo-server/manufacturer.key
    ```

3.  Modify the `/etc/go-fdo-server/manufacturing.yaml`{.literal} configuration file to define your operational parameters.

    Note

    Access to this file is restricted to the `go-fdo-server`{.literal} group by default.

4.  Define the server parameters. Ensure the following items are correctly mapped in your YAML file:

    Database (`db`{.literal})
    :   The path to the server's database.

    Networking (`http`{.literal})
    :   The server's HTTP endpoint IP and port.

    Manufacturer Key
    :   The path to the manufacturer's private key.

    Device CA
    :   The paths to the Device CA certificate and private key.

    Owner Certificate

    :   The path to the Owner server's public certificate.

        **Example `manufacturing.yaml`{.literal} configuration**

        ``` {.language-plaintext tabindex="-1"}
        log:
          level: info
        db:
          type: sqlite
          dsn: file:/var/lib/go-fdo-server-manufacturer/db.sqlite
        http:
          ip: 0.0.0.0
          port: "8038"
        manufacturing:
          key: /etc/pki/go-fdo-server/manufacturer.key
          device_ca:
            cert: /etc/pki/go-fdo-server/device-ca.crt
            key: /etc/pki/go-fdo-server/device-ca.key
        owner:
          cert: /etc/pki/go-fdo-server/owner.crt
        ```

### [2.8. Running the FDO Manufacturing server](#running-the-fdo-manufacturing-server) {#running-the-fdo-manufacturing-server .title}

The FIDO Device Onboarding (FDO) Manufacturing server provides an HTTP interface for administrative tasks and device communication. Network accessibility is mandatory to process initialization requests, manage device credentials, and facilitate the Device Initialization (DI) protocol.

**Prerequisites**

-   The `go-fdo-server-manufacturer`{.literal} RPM package is installed.
-   Test certificates are generated and stored in the `/etc/pki/go-fdo-server/`{.literal} directory.
-   The server configuration file is updated with valid paths and port settings.
-   You have root privileges.

**Procedure**

1.  Open the Manufacturer server's default port in the firewalld service:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo firewall-cmd --add-port=8038/tcp --permanent
    ```

    Note

    If you customized the `http.port`{.literal} parameter in your configuration file, use that port number instead of the default.

    If you change the default port, you must relabel the new port in SELinux to enable the `go-fdo-server`{.literal} service to bind to it. Failure to do so might cause the service to fail to start or be blocked by security policies.

    To enable traffic on a custom port, such as port 8040, run the following command to install the `policycoreutils-python-utils`{.literal} package to use the `semanage`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo semanage port -a -t fdo_port_t -p tcp 8040
    ```

2.  Reload the firewall to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo firewall-cmd --reload
    ```

3.  Enable and start the manufacturer server by using the `systemd`{.literal} system and service manager:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl enable --now go-fdo-server-manufacturer.service
    ```

    This ensures the server starts automatically upon system reboot.

4.  Verify the manufacturer server status:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl status go-fdo-server-manufacturer.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    ● go-fdo-server-manufacturer.service - Go FDO manufacturer server
         Loaded: loaded (/usr/lib/systemd/system/go-fdo-server-manufacturer.service; enabled; preset: disabled)
         Active: active (running) since Fri 2026-03-20 16:15:47 EDT; 38s ago
    ...
    ```

5.  Optional: Verify that the server's network endpoint is functioning and accessible by probing the serve's `/health`{.literal} API endpoint:

    ``` {.language-plaintext tabindex="-1"}
    $ curl http://<ip-address>:8038/health
    ```

    ``` {.language-plaintext tabindex="-1"}
    {"message":"the service is up and running","status":"OK","version":"1.0.0"}
    ```

    To validate that your `firewalld`{.literal} configuration is correct, perform this check from a different computer on the network. Local requests typically bypass firewall filtering rules.

### [2.9. Configuration reference for HTTPS and database](#configuration-reference-for-https-and-database) {#configuration-reference-for-https-and-database .title}

Check the HTTPS and database parameters required to secure network traffic and ensure reliable data persistence. Use these settings to harden your environment and maintain a stable connection between the application and your data layer.

#### [2.9.1. HTTPS requirements](#https_requirements) {#https-requirements .title}

To enable HTTPS, you must provide paths for both the certificate and the private key. Providing only one will result in a connection error.

`http.cert`{.literal}
:   Path to the server certificate.

`http.key`{.literal}
:   Path to the certificate's private key.

#### [2.9.2. Database connection (db.dsn)](#database_connection_db_dsn) {#database-connection-db.dsn .title}

The syntax for the Data Source Name (`db.dsn`{.literal}) depends entirely on the `db.type`{.literal} you select:

+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Database type (`db.type`{.literal}) | Connection string syntax (`db.dsn`{.literal})                                                                                                                                                                                   |
+:====================================+:================================================================================================================================================================================================================================+
| SQLite                              | `file:_<database_file>_.db`{.literal}                                                                                                                                                                                           |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PostgreSQL                          | `host=`{.literal}*`<hostname>`{.literal}*` port=`{.literal}*`<port_number>`{.literal}*` user=`{.literal}*`<username>`{.literal}*` password=`{.literal}*`<password>`{.literal}*` dbname=`{.literal}*`<database_name>`{.literal}* |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

### [2.10. Installing the FDO Rendezvous server](#installing-the-fdo-rendezvous-server) {#installing-the-fdo-rendezvous-server .title}

Install the `go-fdo-server-rendezvous`{.literal} RPM package to deploy the Rendezvous server. This server acts as the directory that redirects devices to their assigned Owner server during onboarding.

**Prerequisites**

-   You have a registered `bootc`{.literal} Red Hat Enterprise Linux (RHEL) 10 system.
-   You have `sudo`{.literal} privileges.
-   You have access to the repositories containing the FDO server packages.

**Procedure**

1.  Install the Rendezvous server package:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install go-fdo-server-rendezvous
    ```

    The package installs several files, creates the `go-fdo-server`{.literal} group and `go-fdo-server-rendezvous`{.literal} user, and installs a `systemd`{.literal} service for running the Rendezvous server.

### [2.11. Running the FDO Rendezvous server](#running-the-fdo-rendezvous-server) {#running-the-fdo-rendezvous-server .title}

The Rendezvous server acts as the central directory during the onboarding process. Its HTTP endpoint must be accessible by the device, the Owner server, and for administrative management.

**Prerequisites**

-   You have installed the `go-fdo-server-rendezvous`{.literal} RPM locally.
-   You have configured the `rendezvous-server.conf.d`{.literal} file, specifically the `http.port`{.literal} (default is 8041).
-   You have administrative access.

**Procedure**

1.  Open the server's HTTP port in the firewalld service:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo firewall-cmd --add-port=8041/tcp --permanent
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ sudo firewall-cmd --reload
    ```

2.  Enable and start the Rendezvous server by using the `systemd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl enable --now go-fdo-server-rendezvous.service
    ```

3.  Verify the server status:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl status go-fdo-server-rendezvous.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    ● go-fdo-server-rendezvous.service - Go FDO Rendezvous server
         Loaded: loaded (/usr/lib/systemd/system/go-fdo-server-rendezvous.service; enabled; preset: disabled)
         Active: active (running) since Fri 2026-03-20 17:21:34 EDT; 16h ago
    ```

4.  Optional: Verify that the server's network endpoint is functioning and accessible:

    ``` {.language-plaintext tabindex="-1"}
    $ curl http://192.168.124.132:8041/health
    ```

    **Example output**

    ``` {.language-plaintext tabindex="-1"}
    {"message":"the service is up and running","status":"OK","version":"1.0.0"}
    ```

    To validate that your `firewalld`{.literal} configuration is correct, perform this check from a different computer on the network. Local requests typically bypass firewall filtering rules.

    +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Parameter             | Description                                                                                                                                                                              |
    +:======================+:=========================================================================================================================================================================================+
    | `log.level`{.literal} | The logging level. Allowed values: `debug`{.literal}, `info`{.literal} (default), `warn`{.literal}, and `error`{.literal}.                                                               |
    +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `db.type`{.literal}   | The database type. Allowed values: `sqlite`{.literal} and `postgres`{.literal}.                                                                                                          |
    +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `db.dsn`{.literal}    | The database connection string (for example, `file:database.db`{.literal} for SQLite, or `host=localhost port=5432 user=postgres password=secret dbname=mydb`{.literal} for PostgreSQL). |
    +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `http.ip`{.literal}   | The HTTP server IP address or hostname.                                                                                                                                                  |
    +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `http.port`{.literal} | The HTTP server port (string).                                                                                                                                                           |
    +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `http.cert`{.literal} | Optional: The path to the certificate file to use for server authentication.                                                                                                             |
    +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `http.key`{.literal}  | Optional: The path to the private key file of the cert certificate.                                                                                                                      |
    +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Show more

### [2.12. Advanced Rendezvous configuration (TO0)](#advanced-rendezvous-configuration-to0) {#advanced-rendezvous-configuration-to0 .title}

For most deployments, the default Rendezvous settings are sufficient. To manage server load and device check-in frequency, tune the Transfer of Ownership Protocol 0 (TO0) wait intervals.

The following table describes the TO0 wait interval parameters.

+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter                           | Description                                                                                                                                                                                                   |
+:====================================+:==============================================================================================================================================================================================================+
| `rendezvous.to0_min_wait`{.literal} | Optional: The minimum wait time, in seconds, that a device must wait between TO0 requests. If a device attempts to check in more frequently than this value, the request fails. Default: 0 (no minimum wait). |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rendezvous.to0_max_wait`{.literal} | Optional: The maximum wait time, in seconds, allowed for a TO0 entry. This defines the upper boundary for the device's check-in interval. Default: 3600 (1 hour).                                             |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

### [2.13. Installing the FDO Owner server](#installing-the-fdo-owner-server) {#installing-the-fdo-owner-server .title}

Install the `go-fdo-server-owner`{.literal} RPM package to deploy the Owner server for performing device onboarding.

**Procedure**

1.  Install the `go-fdo-server-owner`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install go-fdo-server-owner
    ```

    The package installs several files, creates the `go-fdo-server`{.literal} group and `go-fdo-server-owner`{.literal} user, and installs a `systemd`{.literal} service for running the Owner server.

2.  Verify that the Owner server's `systemd`{.literal} unit file is available:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl list-unit-files | grep go-fdo-server-owner
    ```

    ``` {.language-plaintext tabindex="-1"}
    go-fdo-server-owner.service disabled
    ```

### [2.14. Configuring the FDO Owner server](#configuring-the-fdo-owner-server) {#configuring-the-fdo-owner-server .title}

To configure the FDO Owner server, modify the YAML-formatted configuration file and ensure that the server has access to the necessary certificates and keys. The server reads this file during initialization to establish database connections, network endpoints, and security credentials.

**Prerequisites**

-   You have installed the `go-fdo-server-owner`{.literal} RPM package.
-   You have obtained the required FDO certificates and keys from your issuing organization.
-   You have installed the certificates and keys into the `/etc/pki/go-fdo-server`{.literal} directory.

**Procedure**

1.  Open the `/etc/go-fdo-server/owner.yaml`{.literal} configuration file in a text editor.

2.  Provide values for the following mandatory configuration items:

    -   Database configuration: The connection details for the server's database.
    -   HTTP endpoint address: The address where the server listens for requests.
    -   Device CA certificate path: The path to the Device CA certificate file.
    -   Owner server public certificate path: The path to the Owner server's public certificate file.
    -   Owner server private key path: The path to the Owner server's private key file.

3.  Optional: Add a list of FDO ServiceInfo Modules (FSIM) to the configuration if you require specific device provisioning during onboarding.

4.  Save the changes and close the file.

5.  Set the ownership on the `owner.key`{.literal} file to the `go-fdo-server-owner`{.literal} user and the `go-fdo-server`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo chown go-fdo-server-owner:go-fdo-server /etc/pki/go-fdo-server/owner.key
    ```

6.  Set the permissions on the `owner.key`{.literal} file to restrict access:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo chmod 600 /etc/pki/go-fdo-server/owner.key
    ```

### [2.15. FDO ServiceInfo Modules (FSIMs)](#fdo-serviceinfo-modules-fsims) {#fdo-serviceinfo-modules-fsims .title}

FDO ServiceInfo Modules (FSIMs) enable automated device provisioning during the TO2 protocol exchange. FSIMs deliver credentials, configurations, and scripts to change devices from a factory-default state to a fully operational, managed asset within the owner's infrastructure.

With FIDO Device Onboard (FDO), you can perform administrative operations from the Owner server by using FDO ServiceInfo Modules (FSIMs). For example, you can use FSIMs to download files to the device, upload files from the device, and run commands on the device.

The following FSIMs are available to the Owner server:

-   `fdo.download`{.literal}: Download files to the device's file system.
-   `fdo.upload`{.literal}: Upload files from the device's file system.
-   `fdo.wget`{.literal}: Download files from an HTTP server to the device's file system.
-   `fdo.command`{.literal}: Run commands on the device.

The `go-fdo-client`{.literal} must have the necessary privileges to perform these functions on behalf of the Owner server. For example, when downloading files to the device's file system, the device client must have permission to create and write the file to the destination directory.

FSIMs run during onboarding after the device client and Owner server establish mutual trust, and the secure communications channel is active. This ensures that FSIM operations can perform privileged actions on the device securely.

To use FSIMs, you must specify them in the Owner server's configuration file. The configuration file supports an ordered list of FSIM configuration entries. The server performs FSIMs in the listed order during onboarding.

The `fdo.download`{.literal} FSIM
:   The `fdo.download`{.literal} FSIM downloads a file from the Owner server's file system to the device's file system. The Owner server downloads the file over the secure communications channel, guaranteeing that sensitive content is protected.

The `fdo.upload`{.literal} FSIM
:   The `fdo.upload`{.literal} FSIM uploads a file from the device's file system to the Owner server's file system. The device uploads the file over the secure communications channel, guaranteeing that sensitive content is protected. The Owner server saves the file to a directory that is unique to the device.

The `fdo.wget`{.literal} FSIM
:   The `fdo.wget`{.literal} FSIM downloads a file to the device's file system. The source of the file is an HTTP server. The `fdo.wget`{.literal} FSIM has much faster download performance than `fdo.download`{.literal}, making it a better choice for downloading large files, such as container images.

The `fdo.wget`{.literal} FSIM does not download the file over the secure FDO communications channel. The device connects directly to the target HTTP server. The FDO protocol does not guarantee the security of the HTTP connection. If the file contains sensitive information, you must either encrypt it before downloading or transfer it by using a properly authenticated HTTPS connection.

The `fdo.command`{.literal} FSIM
:   The Owner server uses the `fdo.command`{.literal} FSIM to run programs on the device. The device client run these programs, which must be present on the device before you issue the `fdo.command`{.literal}. The `fdo.command`{.literal} FSIM supports passing arguments to the program and redirecting `stdout`{.literal} and `stderr`{.literal} back to the Owner server's logs. The `fdo.command`{.literal} FSIM supports adding shell scripts directly into the configuration file.

### [2.16. Configuring FDO ServiceInfo Modules (FSIMs) for device provisioning](#configuring-fdo-serviceinfo-modules-fsims-for-device-provisioning) {#configuring-fdo-serviceinfo-modules-fsims-for-device-provisioning .title}

You can use FIDO Device Onboard (FDO) ServiceInfo Modules (FSIMs) to automate tasks on a device during the onboarding process, such as downloading files, running commands, or fetching large payloads. To use FSIMs, you must add an `fsim`{.literal} section to your Owner server configuration file.

**Prerequisites**

-   You have administrative access to the Owner server.
-   The FDO Owner server is installed and the base configuration in `/etc/go-fdo-server/owner.yaml`{.literal} is complete.
-   Any local scripts or files intended for download through the `fdo.download`{.literal} module are stored in a directory accessible to the `go-fdo-server`{.literal} user, such as `/var/lib/go-fdo-server-owner/scripts/`{.literal}.

**Procedure**

1.  Open your Owner server configuration file (for example, `/etc/go-fdo-server/owner.yaml`{.literal}) in a text editor.

2.  Define the `fsim`{.literal} section and add the required modules. The following example configures a script download, a command execution, and a large file download by using `fdo.wget`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    log:
      level: "info"

    db:
      type: "sqlite"
      dsn: "file:/var/lib/go-fdo-server-owner/db.sqlite"

    http:
      ip: "0.0.0.0"
      port: "8043"

    device_ca:
      cert: "/etc/pki/go-fdo-server/device-ca.crt"

    owner:
      cert: "/etc/pki/go-fdo-server/owner.crt"
      key: "/etc/pki/go-fdo-server/owner.key"

    fsim:
      - module: "fdo.download"
        files:
          - src: "/var/lib/go-fdo-server-owner/scripts/setup-env.sh"
            dst: "/usr/local/bin/setup-env.sh"
            permissions: "0755"

      - module: "fdo.command"
        commands:
          - command: ["/usr/local/bin/setup-env.sh", "--init"]
            description: "Initializing environment"

      - module: "fdo.wget"
        files:
          - src: "http://distribution.example.com/images/worker-payload.tar.gz"
            dst: "/var/tmp/worker-payload.tar.gz"
            may_fail: true
    ```

3.  Save the file and restart the Owner server service to apply the configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl restart fdo-owner-server
    ```

### [2.17. Running the FDO Owner server](#running-the-fdo-owner-server) {#running-the-fdo-owner-server .title}

For administrative management and device communication during the TO2 protocol, make the FDO Owner server HTTP endpoint accessible. Proper network routing is required to facilitate secure ownership transfer and run ServiceInfo provisioning modules.

**Prerequisite**

-   Network accessibility.

**Procedure**

1.  Ensure that the system firewall does not block the server's HTTP endpoint by opening the server's network port:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo firewall-cmd --add-port=8043/tcp --permanent
    ```

2.  Restart the `firewalld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl restart firewalld
    ```

3.  Enable and start the Owner server by using the `systemd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl enable --now go-fdo-server-owner.service
    ```

4.  Verify that the server is active:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl status go-fdo-server-owner.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    ● go-fdo-server-owner.service - Go FDO owner server
         Loaded: loaded (/usr/lib/systemd/system/go-fdo-server-owner.service; enabled; preset: disabled)
         Active: active (running) since Sun 2026-03-22 16:35:04 EDT; 18s ago
    ...
    ```

**Verification**

-   Optional: Verify that the server's network endpoint is functioning and accessible:

    ``` {.language-plaintext tabindex="-1"}
    $ curl http://192.168.124.132:8043/health
    ```

    ``` {.language-plaintext tabindex="-1"}
    {"message":"the service is up and running","status":"OK","version":"1.0.0"}
    ```

### [2.18. Installing and configuring the FIDO Device Onboard (FDO) client on RHEL 10](#installing-and-configuring-the-fido-device-onboard-fdo-client-on-rhel-10) {#installing-and-configuring-the-fido-device-onboard-fdo-client-on-rhel-10 .title}

In RHEL 10 image mode, the operating system is immutable. To deploy the FDO client, define the package installation in the `Containerfile`{.literal} used to build the bootable container image. This ensures that the client is baked into the file system at build time.

Important

FDO is supported only on a Red Hat Enterprise Linux (RHEL) 10 system in image mode (`bootc`{.literal}).

**Prerequisites**

-   You have a `Containerfile`{.literal}.
-   You have a RHEL 10 Linux system in image mode (`bootc`{.literal}).
-   FDO servers (Manufacturer, Rendezvous, and Owner) are deployed and accessible.
-   You have network connectivity between the device and FDO servers.

**Procedure**

1.  Install the packages by using a `Containerfile`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    FROM registry.redhat.io/rhel10/rhel-bootc:10.2
    #Install the go-fdo-client package using your distribution's package manager:
    RUN dnf install -y go-fdo-client && dnf clean all
    ```

    Note

    If you plan to use a Trusted Platform Module (TPM) for credential storage, you must also install `tpm2-tools`{.literal} in the `Containerfile`{.literal}. For more information, see *\<Using_a_TPM\>*.

2.  Build the container image:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/example/fdo-client-bootc:latest -f Containerfile .
    ```

3.  Push the container image to the registry:

    ``` {.language-plaintext tabindex="-1"}
    $ podman push quay.io/example/fdo-client-bootc:latest
    ```

4.  Reference the container image in your Kickstart file by using the `ostreecontainer`{.literal} directive to deploy it on the target device.

### [2.19. Configuring the FDO client](#configuring-the-fdo-client) {#configuring-the-fdo-client .title}

To customize the behavior of the FIDO Device Onboard (FDO) client to suit your environment, manage how it interacts with the manufacturing and onboarding servers.

Configuring the behavior of the FDO client ensures that the device can securely authenticate and receive its intended credentials and software packages during the onboarding process.

**Prerequisites**

-   You installed the `go-fdo-client`{.literal} package on the target device.
-   You have access to a command line with sufficient permissions to run the client.
-   Optional: You have a predefined configuration file in the YAML or TOML format.

**Procedure**

1.  Identify the required configuration parameters. To view a comprehensive list of all available flags and options for a specific subcommand, pass the `--help`{.literal} flag:

    ``` {.language-plaintext tabindex="-1"}
    $ go-fdo-client <command> --help
    ```

2.  Create or edit a configuration file. You can use either the YAML (`.yaml`{.literal}, `.yml`{.literal}) or TOML (`.toml`{.literal}) format. Ensure that any file paths defined within the configuration are either absolute or relative to your current working directory.

3.  Run the client by using a configuration file. Use the `--config`{.literal} flag to point the client to your specific settings:

    ``` {.language-plaintext tabindex="-1"}
    $ go-fdo-client <command> --config /etc/fdo/config.yaml
    ```

    Note

    The file format is automatically detected by the extension provided in the `--config`{.literal} path.

4.  Optional: Override settings by using CLI flags. The client resolves configuration values based on a specific hierarchy. If a value is defined in multiple places, the client applies them in the following order of precedence (from highest to lowest):

    -   Positional arguments: Such as the server URL for `device-init`{.literal}.
    -   CLI flags: `--key`{.literal} or `--kex`{.literal}.
    -   Configuration file values: Settings defined in your YAML or TOML file.
    -   Default values: Built-in application defaults.

### [2.20. Using a TPM to store the device credentials](#using-a-tpm-to-store-the-device-credentials) {#using-a-tpm-to-store-the-device-credentials .title}

The FIDO Device Onboard (FDO) client can store the device credential in a Trusted Platform Module (TPM) instead of a file. This provides hardware-backed protection for credential secrets.

**Prerequisites**

-   You have a TPM 2.0 device such as `/dev/tpmrm0`{.literal}.
-   You installed the `tpm2-tools`{.literal} package in the `bootc`{.literal} container image.
-   You have root privileges.

**Procedure**

1.  Initialize the device by using the TPM:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo go-fdo-client device-init http://manufacturer.example.com:8038 --key ec256 --tpm /dev/tpmrm0
    ```

2.  Run the onboarding command by using the TPM:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo go-fdo-client onboard --key ec256 --kex ECDH256 \ --tpm /dev/tpmrm0
    ```

### [2.21. Verifying the FDO device credential](#verifying-the-fdo-device-credential) {#verifying-the-fdo-device-credential .title}

Verify the FDO device credential to ensure that the initialization process is successful and that the device is ready for secure onboarding.

**Prerequisites**

-   You successfully initialized the device.
-   You installed the `fdo-client`{.literal} or `go-fdo-client`{.literal} package.
-   You have root privileges.

**Procedure**

1.  Verify the credential by using the command appropriate for your storage method:

    -   For file-based storage:

        If the credential was stored in the boot directory during initialization, use the `--blob`{.literal} flag to point to the file path.

        ``` {.language-plaintext tabindex="-1"}
        $ sudo go-fdo-client print --blob /boot/device_credential
        ```

    -   For Trusted Platform Module (TPM)-based storage:

        If the device uses a Hardware Security Module (HSM) or TPM for enhanced security, use the `--tpm`{.literal} flag and specify the TPM resource manager path.

        ``` {.language-plaintext tabindex="-1"}
        $ sudo go-fdo-client print --tpm /dev/tpmrm0
        ```

**Verification**

1.  Verify the following command output parameters to ensure the device is prepared for deployment:

    -   The device's public key information
    -   Rendezvous server information
    -   Ownership header status

2.  Ensure the output does not return an error, which indicates a corrupted or missing credential.

### [2.22. Clearing FDO device credentials](#clearing-fdo-device-credentials) {#clearing-fdo-device-credentials .title}

To decommission a device, repurpose it for a new environment, or troubleshoot failed onboarding attempts, clear the FDO device credentials.

By removing the FDO device credentials, you reset the device's identity, ensuring that sensitive ownership metadata is cleared and the device is ready to be re-initialized from a clean state.

**Prerequisites**

-   You have root privileges.
-   Optional: For TPM-based clearing, you installed the `tpm2-tools`{.literal} package.
-   All active onboarding processes are stopped.

**Procedure**

-   Clear the credential by using the method appropriate for your storage type:

    -   For a file-based credential:

        Delete the credential blob from the `/boot`{.literal} directory or the specific location defined during initialization.

        ``` {.language-plaintext tabindex="-1"}
        $ sudo rm /boot/device_credential
        ```

    -   For a TPM-backed credential:

        If the credential is stored in the Trusted Platform Module (TPM) non-volatile (NV) memory, release the specific index, which is typically 0x01D10001 for FDO.

        ``` {.language-plaintext tabindex="-1"}
        $ sudo tpm2_nvundefine 0x01D10001
        ```

**Verification**

-   Run the `print`{.literal} command. The command fails and returns a `file not found`{.literal} or `NV index not defined`{.literal} error, which confirms that the credential is cleared.

### [2.23. FDO troubleshooting reference](#troubleshooting-device-initialization-and-onboarding) {#fdo-troubleshooting-reference .title}

This reference identifies common issues and provides solutions for FIDO Device Onboard (FDO) initialization and onboarding. Use these resolutions and diagnostic commands to resolve configuration issues and ensure a successful ownership transfer.

+----------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Error / Issue                                      | Common Cause                                                                                | Resolution                                                                                                                                        |
+:===================================================+:============================================================================================+:==================================================================================================================================================+
| `TO1 failed`{.literal}                             | The Rendezvous (RV) server has no record of the device.                                     | 1.  Verify the transfer of the ownership voucher to the Owner server.                                                                             |
|                                                    |                                                                                             | 2.  Confirm the Owner server registered the device with the RV server.                                                                            |
|                                                    |                                                                                             | 3.  Verify the Owner server targets the correct RV address.                                                                                       |
|                                                    |                                                                                             | 4.  Match the voucher GUID with the device GUID by using the `go-fdo-client print`{.literal} command.                                             |
+----------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| `no rendezvous information found…​`{.literal}       | Missing RV metadata in the device credential.                                               | 1.  Use the `go-fdo-client print`{.literal} command to verify RV information in the credential.                                                   |
|                                                    |                                                                                             | 2.  Configure the Manufacturer server with the correct RV data.                                                                                   |
|                                                    |                                                                                             | 3.  Re-initialize the device.                                                                                                                     |
+----------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| `TLS Errors`{.literal}                             | Self-signed certificates or untrusted Certificate Authority (CA) chains.                    | Use the `--insecure-tls`{.literal} flag for the `device-init`{.literal} or `onboard`{.literal} commands. Use this flag only in test environments. |
+----------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| `Failed to read credential from TPM`{.literal}     | Missing or invalid credential in the Trusted Platform Module (TPM) non-volatile (NV) index. | Run the `device-init --tpm`{.literal} command to provision the credential first.                                                                  |
+----------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| `Permission denied on /dev/tpmrm0`{.literal}       | Insufficient user privileges for TPM access.                                                | Run the command with `sudo`{.literal}.                                                                                                            |
+----------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| `TPM NV index corrupted or inaccessible`{.literal} | Inconsistent TPM state.                                                                     | 1.  Clear the index by using the `tpm2_nvundefine 0x01D10001`{.literal} command.                                                                  |
|                                                    |                                                                                             | 2.  Re-run `device-init`{.literal}.                                                                                                               |
+----------------------------------------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

#### [2.23.1. Diagnostic commands:](#diagnostic_commands) {#diagnostic-commands .title}

To further investigate persistent issues, use the following commands to gather metadata or verbose logs.

**Print device GUID and metadata:**

For file-based credentials:

``` {.language-plaintext tabindex="-1"}
$ sudo go-fdo-client print --blob /boot/device_credential
```

For TPM-based credentials:

``` {.language-plaintext tabindex="-1"}
$ sudo go-fdo-client print --tpm /dev/tpmrm0
```

**Enable verbose debugging:**

Add the `--debug`{.literal} flag to your command to inspect the HTTP request and response payloads between the client and servers:

``` {.language-plaintext tabindex="-1"}
$ sudo go-fdo-client onboard --blob /boot/device_credential --key ec256 --kex ECDH256 --debug
```

Note

Most TO1 failures result from timing issues or a mismatch between the Manufacturer's programmed Rendezvous info and the location where the Owner server uploaded the voucher. Always verify that the \"Rendezvous Server Info\" in your `manufacturing.yaml`{.literal} file matches the live RV server address.

## [Chapter 3. Automatically provisioning and onboarding RHEL for Edge devices with FDO](#automatically-provisioning-and-onboarding-rhel-for-edge-devices-with-fdo) {#chapter-3.-automatically-provisioning-and-onboarding-rhel-for-edge-devices-with-fdo .title}

Use image mode for RHEL to build operating system images optimized for edge deployments. These images support the FIDO Device Onboarding (FDO) process, which automates device provisioning and securely integrates your edge devices with your network infrastructure.

The FIDO Device Onboarding (FDO) process automatically provisions and onboards your Edge devices, and exchanges data with other devices and systems connected to the networks.

Important

Red Hat provides the `FDO`{.literal} process as a Technology Preview feature. Because this feature is in development, ensure you deploy and test it only on secure networks. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

### [3.1. The FIDO Device Onboarding (FDO) process overview](#the-fido-device-onboarding-fdo-process) {#the-fido-device-onboarding-fdo-process-overview .title}

Securely automate new device onboarding into your IoT architecture by using FIDO Device Onboarding (FDO). By using FDO, you can verify device authenticity, deploy configurations, and ensure every device is trusted and synchronized with your infrastructure upon installation.

The FDO protocol provides the following benefits and capabilities:

-   Automates the secure onboarding of devices at scale without requiring technical personnel at the edge location.
-   Performs device initialization at the manufacturing stage and late device binding for its actual use.
-   Solves the trust and chain of ownership by cryptographically identifying the system identity before enrolling and passing configurations.
-   Applies device credentials directly to the ISO image during the device's first boot, instead of embedding a Kickstart configuration.
-   Enables you to share sensitive data over a secure FDO channel.
-   Allows the management platform to securely connect to the device to apply patches, updates, and rollbacks.

The FDO protocol is based on the following servers:

Manufacturing server

:   1.  Generates the device credentials.
    2.  Creates an ownership voucher that is used to set the ownership of the device later in the process.
    3.  Binds the device to a specific management platform.

Owner management system

:   1.  Receives the ownership voucher from the manufacturing server and becomes the owner of the associated device.
    2.  Creates a secure channel between the device and the owner onboarding server after device authentication.
    3.  Uses the secure channel to send the required information, such as files and scripts for the onboarding automation, to the device.

Service-info API server
:   Based on the Service-info API server's configuration and the modules available on the client, it performs the final steps of onboarding on target client devices. These steps include copying SSH keys and files, running commands, creating users, and encrypting disks.

Rendezvous server

:   1.  Receives the ownership voucher from the owner management system and maps the device Universal Unique Identifier (UUID) to the owner server IP. The rendezvous server then matches the device UUID with a target platform and informs the device which owner onboarding server endpoint to use.
    2.  Acts as the contact point for the device during the first boot, directing the device to the owner so they can establish a secure channel.

Device client

:   Installed on the device, the device client performs the following actions:

    -   Queries the multiple servers where the onboarding automation will be executed.
    -   Uses an Internet Protocol (IP) network to communicate with the servers.

During **device initialization**, the device contacts the manufacturing server to get the FDO credentials, which are a set of certificates and keys installed on the operating system alongside the rendezvous server endpoint (URL). It also gets the ownership voucher, which is maintained separately to allow for owner assignment changes:

1.  The device contacts the manufacturing server.
2.  The manufacturing server generates an ownership voucher and the device credentials.
3.  The ownership voucher transfers to the owner onboarding server.

During **on-site onboarding**, the device gets the rendezvous server endpoint (URL) from its device credentials and contacts the rendezvous server endpoint to start the onboarding process. This redirects the device to the owner management system, which consists of the owner onboarding server and the Service-info API server:

4.  The owner onboarding server transfers the ownership voucher to the rendezvous server, which maps the ownership voucher to the owner.
5.  The device client reads the device credentials and connects to the network.
6.  After connecting to the network, the device client contacts the rendezvous server.
7.  The rendezvous server sends the owner endpoint URL to the device client and registers the device.
8.  The device client connects to the owner onboarding server shared by the rendezvous server.
9.  The device proves its identity by signing a statement with a device key.
10. The owner onboarding server proves its identity by signing a statement with the last key of the ownership voucher.
11. The owner onboarding server transfers the device information to the Service-info API server.
12. The Service-info API server sends the configuration to the device.
13. The device is onboarded.

### [3.2. FDO automatic onboarding technologies](#fdo-automatic-onboarding-technologies) {#fdo-automatic-onboarding-technologies .title}

The FDO automatic onboarding relies on the interaction between a set of technologies to enable secure and automated onboarding.

+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Technology                        | Definition                                                                                        |
+:==================================+:==================================================================================================+
| UEFI                              | Unified Extensible Firmware Interface.                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| RHEL                              | Red Hat® Enterprise Linux® operating system                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| `rpm-ostree`{.literal}            | Background image-based upgrades.                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Greenboot                         | `Healthcheck`{.literal} framework for systemd on `rpm-ostree`{.literal}.                          |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| image mode for RHEL               | The new deployment method that uses containers to build a system for operating system artifacts.  |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Container                         | A Linux® container is a set of 1 or more processes that are isolated from the rest of the system. |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Coreos-installer                  | Assists installation of RHEL images and boots UEFI-based systems.                                 |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| FIDO FDO                          | Specification protocol to provision configuration and onboarding devices.                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------+

: Table 3.1. OSTree and rpm-ostree terminology

Show more

### [3.3. Automatically provisioning and onboarding RHEL for Edge devices with FDO](#automatically-provisioning-and-onboarding-rhel-for-edge-devices) {#automatically-provisioning-and-onboarding-rhel-for-edge-devices-with-fdo .title}

Build and automatically onboard RHEL for Edge systems by using `podman build`{.literal}. By booting the resulting image, you can trigger an automated provisioning that installs RHEL for Edge onto local storage or virtualized environments.

**Prerequisites**

-   You have installed and registered a RHEL system.
-   You have an FDO infrastructure, that is, **Manufacturing Server**, **Rendezvous server**, and **Owner Server**, already deployed.

**Procedure**

1.  Create a `Containerfile`{.literal} to include the FDO client and kernel arguments. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ cat Containerfile
    FROM registry.redhat.io/rhel10/rhel-bootc:10
    #fdo
    RUN dnf install -y fdo-init fdo-client && \
    systemctl enable fdo-client-linuxapp.service

    RUN mkdir -p /usr/lib/bootc/kargs.d && \ cat <<`EOF` >> /usr/lib/bootc/kargs.d/console.toml kargs = ["inst.device=/dev/sda"] EOF
    ```

2.  Build the *\<image\>* container image by using the `Containerfile`{.literal} in the current directory:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/<namespace>/<image>:<tag> .
    ```

3.  Install the resulting image on the target device and power it on.

    After powering on, the system performs the following steps automatically:

    -   The FDO client reaches out to the **Manufacturing Server** to exchange initial credentials.
    -   The device contacts the **Rendezvous Server** to verify its voucher and locate its intended owner.
    -   The device establishes mutual trust with the **Owner Server**. The `service-info`{.literal} API then pushes the final configuration, such as SSH keys, user accounts, and encrypted filesystems, to the device.

### [3.4. Generating keys and certificates](#generating-key-and-certificates) {#generating-keys-and-certificates .title}

Installing FIDO Device Onboarding (FDO) services automatically generates keys and certificates for the manufacturing server. You can manually re-create these credentials if needed. Services start with default settings after installation.

Important

Red Hat provides the `fdo-admin-tool`{.literal} tool as a Technology Preview feature. Because this feature is in development, ensure you deploy and test it only on secure networks. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. See [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview) on the Red Hat Customer Portal for information about the support scope for Technology Preview features.

**Prerequisites**

-   You installed the `fdo-admin-cli`{.literal} RPM package.

**Procedure**

1.  Generate the keys and certificates in the `/etc/fdo`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ for i in "diun" "manufacturer" "device-ca" "owner"; do fdo-admin-tool generate-key-and-cert $i; done
    $ ls keys
    device_ca_cert.pem device_ca_key.der diun_cert.pem diun_key.der manufacturer_cert.pem manufacturer_key.der owner_cert.pem owner_key.der
    ```

2.  Check the key and certificates that were created in the `/etc/fdo/keys`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ tree keys
    ```

    You can see the following output:

    ``` {.language-plaintext tabindex="-1"}
    - device_ca_cert.pem
    - device_ca_key.der
    - diun_cert.pem
    - diun_key.dre
    - manufacturer_cert.pem
    - manufacturer_key.der
    - owner_cert.pem
    - owner_key.pem
    ```

    See the `fdo-admin-tool generate-key-and-cert --help`{.literal} command output for more details.

### [3.5. Installing and configuring the manufacturing server](#installing-and-running-the-manufacturing-server) {#installing-and-configuring-the-manufacturing-server .title}

Deploy the FDO manufacturing server for automatic onboarding by installing the `fdo-manufacturing-server`{.literal} RPM. It generates device metadata, GUIDs, and rendezvous information, and creates the credentials and owner vouchers required to connect devices to the rendezvous server.

Important

Red Hat provides the `fdo-manufacturing-server`{.literal} tool as a Technology Preview feature. Because this feature is in development, ensure you deploy and test it only on secure networks. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. See [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview) on the Red Hat Customer Portal for information about the support scope for Technology Preview features.

To install the `manufacturing server`{.literal} RPM package, complete the following steps:

**Procedure**

1.  Install the `fdo-admin-cli`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install -y fdo-admin-cli
    ```

2.  Check if the `fdo-manufacturing-server`{.literal} RPM package is installed:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm -qa | grep fdo-manufacturing-server --refresh
    ```

3.  Check if the files were correctly installed:

    ``` {.language-plaintext tabindex="-1"}
    $ ls /usr/share/doc/fdo
    ```

    You can see the following output:

    ``` {.language-plaintext tabindex="-1"}
    Output:
    manufacturing-server.yml
    owner-onboarding-server.yml
    rendezvous-info.yml
    rendezvous-server.yml
    serviceinfo-api-server.yml
    ```

4.  Optional: Check the content of each file:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /usr/share/doc/fdo/manufacturing-server.yml
    ```

5.  Configure the Manufacturing server. You must provide the following information:

    -   The Manufacturing server URL

    -   The IP address or DNS name for the Rendezvous server

    -   The path to the keys and certificates that you generated.

        You can find an example of a Manufacturing server configuration file in the `/usr/share/doc/fdo/manufacturing-server.yml`{.literal} directory. The following is a `manufacturing server.yml`{.literal} example that is created and saved in the `/etc/fdo`{.literal} directory. It contains paths to the directories, certificates, keys that you created, the Rendezvous server IP address, and the default port.

        ``` {.language-plaintext tabindex="-1"}
        session_store_driver:
          Directory:
            path: /etc/fdo/stores/manufacturing_sessions/
        ownership_voucher_store_driver:
          Directory:
            path: /etc/fdo/stores/owner_vouchers
        public_key_store_driver:
          Directory:
            path: /etc/fdo/stores/manufacturer_keys
        bind: "0.0.0.0:8080"
        protocols:
          plain_di: false
          diun:
            mfg_string_type: SerialNumber
            key_type: SECP384R1
            allowed_key_storage_types:
              - Tpm
              - FileSystem
            key_path: /etc/fdo/keys/diun_key.der
            cert_path: /etc/fdo/keys/diun_cert.pem
        rendezvous_info:
          - deviceport: 8082
            ip_address: 192.168.122.99
            ownerport: 8082
            protocol: http
        manufacturing:
          manufacturer_cert_path: /etc/fdo/keys/manufacturer_cert.pem
          device_cert_ca_private_key: /etc/fdo/keys/device_ca_key.der
          device_cert_ca_chain: /etc/fdo/keys/device_ca_cert.pem
          owner_cert_path: /etc/fdo/keys/owner_cert.pem
          manufacturer_private_key: /etc/fdo/keys/manufacturer_key.der
        ```

6.  Start the Manufacturing server.

    a.  Check if the systemd unit files are in the server:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl list-unit-files | grep fdo | grep manufacturing
        fdo-manufacturing-server.service disabled disabled
        ```

    b.  Enable and start the manufacturing server.

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now fdo-manufacturing-server.service
        ```

    c.  Open the default ports in your firewall:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --add-port=8080/tcp --permanent
        # systemctl restart firewalld
        ```

    d.  Ensure that the service is listening on the `8080`{.literal} port:

        ``` {.language-plaintext tabindex="-1"}
        # ss -ltn
        ```

7.  Install RHEL for Edge onto your system by using the RHEL for Edge Simplified Installer image.

**Additional resources**

-   [manufacturing-server.yml](https://github.com/fedora-iot/fido-device-onboard-rs/blob/main/examples/config/manufacturing-server.yml)
-   [FDO automatic onboarding terminology](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_installing_and_managing_rhel_for_edge_images/automatically-provisioning-and-onboarding-rhel-for-edge-devices-with-fdo#fdo-automatic-onboarding-technologies)

### [3.6. Installing, configuring, and running the Rendezvous server](#installing-configuring-and-running-the-rendezvous-server) {#installing-configuring-and-running-the-rendezvous-server .title}

You can enable systems to receive the manufacturing server voucher during the first boot by installing the `fdo-rendezvous-server`{.literal} package. The rendezvous server matches the device UUID to the target platform or cloud and directs the device to the correct owner server endpoint.

**Prerequisites**

-   You created a `manufacturer_cert.pem`{.literal} certificate.
-   You copied the `manufacturer_cert.pem`{.literal} certificate to the `/etc/fdo/keys`{.literal} directory in the Rendezvous server.

**Procedure**

1.  Install the `fdo-rendezvous-server`{.literal} RPM packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install -y fdo-rendezvous-server
    ```

2.  Create the `rendezvous-server.yml`{.literal} configuration file, including the path to the manufacturer certificate. You can find an example in `/usr/share/doc/fdo/rendezvous-server.yml`{.literal}. The following example shows a configuration file that is saved in `/etc/fdo/rendezvous-server.yml`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    storage_driver:
      Directory:
        path: /etc/fdo/stores/rendezvous_registered
    session_store_driver:
      Directory:
        path: /etc/fdo/stores/rendezvous_sessions
    trusted_manufacturer_keys_path: /etc/fdo/keys/manufacturer_cert.pem
    max_wait_seconds: ~
    bind: "0.0.0.0:8082"
    ```

3.  Check the Rendezvous server service status:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl list-unit-files | grep fdo | grep rende
    fdo-rendezvous-server.service disabled disabled
    ```

    a.  If the service is stopped and disabled, enable and start it:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now fdo-rendezvous-server.service
        ```

4.  Check that the server is listening on the default configured port 8082:

    ``` {.language-plaintext tabindex="-1"}
    # ss -ltn
    ```

5.  Open the port if you have a firewall configured on this server:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port=8082/tcp --permanent
    # systemctl restart firewalld
    ```

### [3.7. Installing, configuring, and running the Owner server](#installing-configuring-and-running-the-owner-server) {#installing-configuring-and-running-the-owner-server .title}

Enable systems to receive the manufacturing server voucher during the first boot by installing the `fdo-owner-cli`{.literal} and `fdo-owner-onboarding-server`{.literal} packages. The rendezvous server matches the device UUID to the target platform or cloud and directs the device to the correct owner server endpoint.

**Prerequisites**

-   The device where the server will be deployed has a Trusted Platform Module (TPM) device to encrypt the disk. If not, you will get an error when booting the RHEL for Edge device.
-   You created the `device_ca_cert.pem`{.literal}, `owner_key.der`{.literal}, and `owner_cert.pem`{.literal} with keys and certificates, and copied them into the `/etc/fdo/keys`{.literal} directory.

**Procedure**

1.  Install the required RPMs in this server:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install -y fdo-owner-cli fdo-owner-onboarding-server
    ```

2.  Prepare the `owner-onboarding-server.yml`{.literal} configuration file and save it to the `/etc/fdo/`{.literal} directory. Include the path to the certificates you already copied and information about where to publish the Owner server service in this file.

    The following is an example available in `/usr/share/doc/fdo/owner-onboarding-server.yml`{.literal}. You can find references to the Service Info API, such as the URL or the authentication token.

    ``` {.language-plaintext tabindex="-1"}
    ---
    ownership_voucher_store_driver:
      Directory:
        path: /etc/fdo/stores/owner_vouchers
    session_store_driver:
      Directory:
        path: /etc/fdo/stores/owner_onboarding_sessions
    trusted_device_keys_path: /etc/fdo/keys/device_ca_cert.pem
    owner_private_key_path: /etc/fdo/keys/owner_key.der
    owner_public_key_path: /etc/fdo/keys/owner_cert.pem
    bind: "0.0.0.0:8081"
    service_info_api_url: "http://localhost:8083/device_info"
    service_info_api_authentication:
      BearerToken:
        token: Kpt5P/5flBkaiNSvDYS3cEdBQXJn2Zv9n1D50431/lo=
    owner_addresses:
      - transport: http
        addresses:
          - ip_address: 192.168.122.149
    ```

3.  Create and configure the Service Info API.

    a.  Add the automated information for onboarding, such as user creation, files to be copied or created, commands to be executed, disk to be encrypted, and so on. Use the Service Info API configuration file example in `/usr/share/doc/fdo/serviceinfo-api-server.yml`{.literal} as a template to create the configuration file under `/etc/fdo/`{.literal}.

        ``` {.language-plaintext tabindex="-1"}
        ---
        service_info:
          initial_user:
            username: admin
            sshkeys:
            - "ssh-rsa AAAA...."
          files:
          - path: /root/resolv.conf
            source_path: /etc/resolv.conf
          commands:
          - command: touch
            args:
            - /root/test
            return_stdout: true
            return_stderr: true
          diskencryption_clevis:
          - disk_label: /dev/vda4
            binding:
              pin: tpm2
              config: "{}"
            reencrypt: true
          additional_serviceinfo: ~
        bind: "0.0.0.0:8083"
        device_specific_store_driver:
          Directory:
            path: /etc/fdo/stores/serviceinfo_api_devices
        service_info_auth_token: Kpt5P/5flBkaiNSvDYS3cEdBQXJn2Zv9n1D50431/lo=
        admin_auth_token: zJNoErq7aa0RusJ1w0tkTjdITdMCWYkndzVv7F0V42Q=
        ```

4.  Check the status of the systemd units:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl list-unit-files | grep fdo
    fdo-owner-onboarding-server.service        disabled        disabled
    fdo-serviceinfo-api-server.service         disabled        disabled
    ```

    a.  If the service is stopped and disabled, enable and start it:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now fdo-owner-onboarding-server.service
        # systemctl enable --now fdo-serviceinfo-api-server.service
        ```

        Note

        You must restart the `systemd`{.literal} services every time you change the configuration files.

5.  Check that the server is listening on the default configured port 8083:

    ``` {.language-plaintext tabindex="-1"}
    # ss -ltn
    ```

6.  Open the port if you have a firewall configured on this server:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --add-port=8081/tcp --permanent
    # firewall-cmd --add-port=8083/tcp --permanent
    # systemctl restart firewalld
    ```

### [3.8. Automating RHEL for Edge device onboarding with FDO](#automatically-onboarding-a-rhel-for-edge-device-by-using-fdo-authentication) {#automating-rhel-for-edge-device-onboarding-with-fdo .title}

Configure the FIDO Device Onboarding (FDO) authentication process to automatically onboard and provision a RHEL for Edge device during installation.

**Prerequisites**

-   You built a customized image by using `podman build`{.literal}.
-   Your device is assembled.
-   You installed the `fdo-manufacturing-server`{.literal} RPM package. See [Installing and configuring the manufacturing server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_installing_and_managing_rhel_for_edge_images/automatically-provisioning-and-onboarding-rhel-for-edge-devices-with-fdo#installing-and-running-the-manufacturing-server).

**Procedure**

1.  Start the installation process by booting the RHEL for Edge image on your device. For example, you can install it from a CD-ROM or from a USB flash drive.

2.  Verify through the command line that the device has reached the manufacturing service to perform the initial device credential exchange and has produced an ownership voucher.

    You can find the ownership voucher at the storage location configured by the *`ownership_voucher_store_driver`{.literal}*`:`{.literal} parameter in the *`manufacturing-sever.yml`{.literal}* file.

    The directory should have an *`ownership_voucher`{.literal}* file with a name in the GUID format, which indicates that the correct device credentials were added to the device.

    The onboarding server uses the device credential to authenticate the hardware. Once authenticated, the server pushes the required configuration and SSH keys to the device. After receiving these assets, the device completes the operating system installation automatically.

    Finally, the system automatically reboots and encrypts the device with a strong key stored in the Trusted Platform Module (TPM).

**Verification**

After the device reboots, log in with the credentials you created during the FDO process.

-   Log in to the device by providing the username and password you created in the Service Info API.

### [3.9. Deploying an image mode for RHEL systems by using FDO](#deploying-an-image-mode-for-rhel-systems-by-using-fdo) {#deploying-an-image-mode-for-rhel-systems-by-using-fdo .title}

You can automate the deployment of image mode for RHEL systems by using FIDO Device Onboarding (FDO) to deliver secure configuration. Embed a Kickstart file within your ISO build to configure the specifics of the installation, such as user accounts, custom partitioning, and SSH keys.

If you use an ISO with a bootc container base image, `bootc-image-builder`{.literal} automatically installs `ostreecontainer`{.literal}, the command to install the container image. You can still configure anything, except the `ostreecontainer`{.literal} command.

**Prerequisites**

-   You have Podman installed on your host machine.
-   You have root access to run the `bootc-image-builder`{.literal} tool and run the containers in `--privileged`{.literal} mode.
-   You have FDO server infrastructure deployed.

**Procedure**

1.  Create a Containerfile, for example:

    ``` {.language-plaintext tabindex="-1"}
    FROM registry.redhat.io/rhel10/rhel-bootc:latest
    RUN dnf install -y fdo-init fdo-client
    RUN systemctl enable fdo-client-linuxapp.service
    ```

2.  Create your Kickstart file. The following Kickstart file is an example of a fully unattended Kickstart file configuration that contains user creation and partition instructions.

    ``` {.language-plaintext tabindex="-1"}
    [customizations.installer.kickstart]
    contents = """
    text --non-interactive
    zerombr
    clearpart --all --initlabel --disklabel=gpt
    autopart --noswap --type=lvm
    user --name=test --groups=wheel --plaintext --password=test
    sshkey --username=test "ssh-ed25519 AAA..."
    network --bootproto=dhcp --device=link --activate --onboot=on
    poweroff

    %post
    export MANUFACTURING_SERVER_URL="http://192.168……"
    export DIUN_PUB_KEY_INSECURE="true"
    /usr/libexec/fdo/fdo-manufacturing-client
    %end

    """
    ```

    In the export *\<MANUFACTURING_SERVER_URL\>* field, replace the manufacturing server URL with your own manufacturing server URL.

3.  Save the Kickstart configuration in the `.toml`{.literal} format to inject the Kickstart content. For example, `config.toml`{.literal}.

4.  Create the following folder:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir $(pwd)/output"
    ```

5.  Run `bootc-image-builder`{.literal}, and include the Kickstart file configuration that you want to add to the ISO build. The `bootc-image-builder`{.literal} automatically adds the `ostreecontainer`{.literal} command that installs the container image.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
        --rm \
        -it \
        --privileged \
        --pull=newer \
        --security-opt label=type:unconfined_t \
        -v /var/lib/containers/storage:/var/lib/containers/storage \
        -v $(pwd)/config.toml:/config.toml \
        -v $(pwd)/output:/output \
        registry.redhat.io/rhel10/bootc-image-builder:latest \
        --type iso \
        --config /config.toml \
      quay.io/<namespace>/<image>:<tag>
    ```

    You can find the resulting `.iso`{.literal} image in the output folder.

**Additional resources**

-   [Automatically provisioning and onboarding RHEL for Edge devices with FDO](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_installing_and_managing_rhel_for_edge_images/automatically-provisioning-and-onboarding-rhel-for-edge-devices-with-fdo)

**Additional resources**

-   [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview)

## [Legal Notice](#idm140016714671696) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
