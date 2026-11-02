---
{"title": "Configuring and using database servers", "guide": "configuring_and_using_database_servers", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_using_database_servers/index", "retrieved": "2026-11-02", "license": "CC-BY-SA-3.0"}
---

# Configuring and using database servers {#configuring-and-using-database-servers .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Installing, configuring, backing up and migrating data on database servers {#installing-configuring-backing-up-and-migrating-data-on-database-servers .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140662000774848)

**Abstract**

Install the MariaDB, MySQL, or PostgreSQL database server on Red Hat Enterprise Linux 10. Configure the chosen database server, back up your data, and migrate your data to a later version of the database server.

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

## [Chapter 1. Using MariaDB](#using-mariadb) {#chapter-1.-using-mariadb .title}

MariaDB Server is a high-performance, open source relational database management system (RDBMS). Built on the MySQL technology, it offers a powerful SQL interface for data access and includes advanced features, such as support for multiple storage engines.

You can install, configure, back up, migrate, and replicate MariaDB databases on RHEL by using MariaDB Galera Cluster.

### [1.1. Installing MariaDB](#installing-mariadb) {#installing-mariadb .title}

RHEL 10 provides MariaDB 10.11 as the initial version of the Application Stream, which you can install as an RPM package. In minor releases, RHEL 10 provides additional MariaDB versions as application streams with a shorter life cycle.

In RHEL 10, the MariaDB server is available in the following versions, each provided by a separate stream:

-   MariaDB 10.11
-   MariaDB 11.8 - available since RHEL 10.2

Important

By design, you can install only one version (stream) of the same application stream and, because of conflicting RPM packages, you cannot install MariaDB and MySQL on the same host. As an alternative, you can run the database server services in a container. See [Using containers to run multiple MariaDB and MySQL instances on a single host](#using-containers-to-run-multiple-mariadb-and-mysql-instances-on-a-single-host_mariadb "1.2. Using containers to run multiple MariaDB and MySQL instances on a single host").

**Procedure**

1.  Install MariaDB server packages:

    -   For MariaDB 10.11, enter:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install mariadb-server
        ```

    -   For MariaDB 11.8, enter:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install mariadb11.8-server
        ```

2.  Enable and start the `mariadb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now mariadb.service
    ```

### [1.2. Using containers to run multiple MariaDB and MySQL instances on a single host](#using-containers-to-run-multiple-mariadb-and-mysql-instances-on-a-single-host_mariadb) {#using-containers-to-run-multiple-mariadb-and-mysql-instances-on-a-single-host .title}

If you install MariaDB or MySQL from packages, you can only run one of these services and only a single version of it on the same host. As an alternative, you can run the services in a container.

You can configure the following scenarios:

-   You want to run multiple instances of MariaDB or MySQL on the same host.
-   You want to run both MariaDB and MySQL on the same host.

Important

The container names and host ports of the database servers must differ.

**Prerequisites**

-   The `podman`{.literal} package is installed.

**Procedure**

1.  Authenticate to the `registry.redhat.io`{.literal} registry by using your Red Hat Customer Portal account:

    ``` {.language-plaintext tabindex="-1"}
    # podman login registry.redhat.io
    ```

    Skip this step if you are already logged in to the container registry.

2.  Start the containers you want to use:

    -   MariaDB 10.11:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run -d --name <container_name_1> -e MARIADB_ROOT_PASSWORD=<password> -p <host_port_1>:3306 rhel10/mariadb-1011
        ```

        For more information about the usage of this container image, see the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/rhel10/mariadb-1011/677d10b3607921b4d74fb9f5).

    -   MariaDB 11.8:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run -d --name <container_name_2> -e MARIADB_ROOT_PASSWORD=<password> -p <host_port_2>:3306 rhel10/mariadb-118
        ```

        For more information about the usage of this container image, see the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/en/software/containers/rhel9/mariadb-118/69845dc2e1b6f8096d7384c4).

    -   MySQL 8.4:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run -d --name <container_name_3> -e MYSQL_ROOT_PASSWORD=<password> -p <host_port_3>:3306 rhel10/mysql-84
        ```

        For more information about the usage of this container image, see the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/rhel10/mysql-84/677d145d607921b4d74fcc6d).

3.  To ensure that clients can access the database server on the network, open the host ports in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port={<host_port_1>/tcp,<host_port_2>/tcp,...}
    # firewall-cmd --reload
    ```

**Verification**

1.  Connect to the database server and log in as root:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h localhost -P <host_port> --protocol tcp
    ```

2.  Optional: Display information about the running containers:

    ``` {.language-plaintext tabindex="-1"}
    $ podman ps
    ```

**Additional resources**

-   [Building, running, and managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/index)
-   [Browse containers in the Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/search)

### [1.3. Configuring network access to MariaDB](#configuring-network-access-to-mariadb) {#configuring-network-access-to-mariadb .title}

You must configure MariaDB to listen on network interfaces and open firewall ports to allow remote client access to the database server.

**Procedure**

1.  Edit the `[mysqld]`{.literal} section of the `/etc/my.cnf.d/mariadb-server.cnf`{.literal} file. You can set the following configuration directives:

    -   `bind-address`{.literal} - is the address on which the server listens. Possible options are:

        -   a host name
        -   an IPv4 address
        -   an IPv6 address

    -   `skip-networking`{.literal} - controls whether the server listens for TCP/IP connections. Possible values are:

        -   0 - to listen for all clients
        -   1 - to listen for local clients only

    -   `port`{.literal} - the port on which **MariaDB** listens for TCP/IP connections.

2.  To ensure that clients can access the database server on the network, open the port in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=mysql
    # firewall-cmd --reload
    ```

3.  Restart the `mariadb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart mariadb.service
    ```

### [1.4. Setting up TLS encryption on a MariaDB server](#setting-up-tls-encryption-on-a-mariadb-server) {#setting-up-tls-encryption-on-a-mariadb-server .title}

By default, MariaDB uses unencrypted connections. For secure connections, enable TLS support on the MariaDB server and configure your clients to establish encrypted connections.

#### [1.4.1. Placing the CA certificate, server certificate, and private key on the MariaDB server](#placing-the-ca-certificate-server-certificate-and-private-key-on-the-mariadb-server) {#placing-the-ca-certificate-server-certificate-and-private-key-on-the-mariadb-server .title}

Before you can enable TLS encryption in the MariaDB server, store the certificate authority (CA) certificate, the server certificate, and the private key on the MariaDB server.

**Prerequisites**

-   The following files in Privacy Enhanced Mail (PEM) format have been copied to the server:

    -   The private key of the server: `server.example.com.key.pem`{.literal}
    -   The server certificate: `server.example.com.crt.pem`{.literal}
    -   The Certificate Authority (CA) certificate: `ca.crt.pem`{.literal}

    For details about creating a private key and certificate signing request (CSR), as well as about requesting a certificate from a CA, see your CA's documentation.

**Procedure**

1.  Store the CA and server certificates in the `/etc/pki/tls/certs/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mv <path>/server.example.com.crt.pem /etc/pki/tls/certs/
    # mv <path>/ca.crt.pem /etc/pki/tls/certs/
    ```

2.  Set permissions on the CA and server certificate that enable the MariaDB server to read the files:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 644 /etc/pki/tls/certs/server.example.com.crt.pem /etc/pki/tls/certs/ca.crt.pem
    ```

    Because certificates are part of the communication before the server establishes a secure connection, any client can retrieve them without authentication. Therefore, you do not need to set strict permissions on the CA and server certificate files.

3.  Store the server's private key in the `/etc/pki/tls/private/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mv <path>/server.example.com.key.pem /etc/pki/tls/private/
    ```

4.  Set secure permissions on the server's private key:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 640 /etc/pki/tls/private/server.example.com.key.pem
    # chgrp mysql /etc/pki/tls/private/server.example.com.key.pem
    ```

    If unauthorized users have access to the private key, connections to the MariaDB server are no longer secure.

5.  Restore the SELinux context:

    ``` {.language-plaintext tabindex="-1"}
    #  restorecon -Rv /etc/pki/tls/
    ```

#### [1.4.2. Configuring TLS encryption on a MariaDB server](#configuring-tls-encryption-on-a-mariadb-server) {#configuring-tls-encryption-on-a-mariadb-server .title}

By default, MariaDB uses unencrypted connections. For more secure connections, you can enable Transport Layer Security (TLS) support on the MariaDB server and configure your clients to establish encrypted connections.

**Prerequisites**

-   You installed the MariaDB server.

-   The `mariadb`{.literal} service is running.

-   The following files in Privacy Enhanced Mail (PEM) format exist on the server and are readable by the `mysql`{.literal} user:

    -   The private key of the server: `/etc/pki/tls/private/server.example.com.key.pem`{.literal}
    -   The server certificate: `/etc/pki/tls/certs/server.example.com.crt.pem`{.literal}
    -   The Certificate Authority (CA) certificate `/etc/pki/tls/certs/ca.crt.pem`{.literal}

-   The subject distinguished name (DN) or the subject alternative name (SAN) field in the server certificate matches the server's host name.

-   If the FIPS mode is active, clients must either support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced on RHEL 9.2 and later](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  Create the `/etc/my.cnf.d/mariadb-server-tls.cnf`{.literal} file:

    a.  Add the following content to configure the paths to the private key, server and CA certificate:

        ``` {.language-plaintext tabindex="-1"}
        [mariadb]
        ssl_key = /etc/pki/tls/private/server.example.com.key.pem
        ssl_cert = /etc/pki/tls/certs/server.example.com.crt.pem
        ssl_ca = /etc/pki/tls/certs/ca.crt.pem
        ```

    b.  If you have a Certificate Revocation List (CRL), configure the MariaDB server to use it:

        ``` {.language-plaintext tabindex="-1"}
        ssl_crl = /etc/pki/tls/certs/example.crl.pem
        ```

    c.  Optional: Reject connection attempts without encryption. To enable this feature, append:

        ``` {.language-plaintext tabindex="-1"}
        require_secure_transport = on
        ```

    d.  Optional: Set the TLS versions the server should support. For example, to support TLS 1.2 and TLS 1.3, append:

        ``` {.language-plaintext tabindex="-1"}
        tls_version = TLSv1.2,TLSv1.3
        ```

        By default, the server supports TLS 1.1, TLS 1.2, and TLS 1.3.

2.  Restart the `mariadb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart mariadb
    ```

**Verification**

To simplify troubleshooting, perform the following steps on the **MariaDB** server before you configure the local client to use TLS encryption:

1.  Verify that MariaDB now has TLS encryption enabled:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e "SHOW GLOBAL VARIABLES LIKE 'have_ssl';"
    +---------------+-----------------+
    | Variable_name | Value           |
    +---------------+-----------------+
    | have_ssl      | YES             |
    +---------------+-----------------+
    ```

    If the `have_ssl`{.literal} variable is set to `yes`{.literal}, TLS encryption is enabled.

2.  If you configured the **MariaDB** service to only support specific TLS versions, display the `tls_version`{.literal} variable:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e "SHOW GLOBAL VARIABLES LIKE 'tls_version';"
    +---------------+-----------------+
    | Variable_name | Value           |
    +---------------+-----------------+
    | tls_version   | TLSv1.2,TLSv1.3 |
    +---------------+-----------------+
    ```

**Additional resources**

-   [Placing the CA certificate, server certificate, and private key on the MariaDB server](#placing-the-ca-certificate-server-certificate-and-private-key-on-the-mariadb-server "1.4.1. Placing the CA certificate, server certificate, and private key on the MariaDB server")

#### [1.4.3. Requiring TLS encrypted connections for specific user accounts on a MariaDB server](#requiring-tls-encrypted-connections-for-specific-user-accounts-on-a-mariadb-server) {#requiring-tls-encrypted-connections-for-specific-user-accounts-on-a-mariadb-server .title}

You can configure specific MariaDB user accounts to require TLS-encrypted connections to protect sensitive data transmission.

If you cannot configure on the server that it requires a secure transport for all connections for all connections (`require_secure_transport = on`{.literal}), configure individual user accounts to require TLS encryption.

**Prerequisites**

-   The **MariaDB** server has TLS support enabled.
-   The user you configure to require secure transport exists.

**Procedure**

1.  Connect as an administrative user to the **MariaDB** server:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h server.example.com
    ```

    If your administrative user has no permissions to access the server remotely, perform the command on the **MariaDB** server and connect to `localhost`{.literal}.

2.  Use the `REQUIRE SSL`{.literal} clause to enforce that a user must connect by using a TLS-encrypted connection:

    ``` {.language-plaintext tabindex="-1"}
    MariaDB [(none)]> ALTER USER 'example'@'%' REQUIRE SSL;
    ```

**Verification**

1.  Connect to the server as the `example`{.literal} user by using TLS encryption:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u example -p -h server.example.com --ssl
    ...
    MariaDB [(none)]>
    ```

    If the command returns no error and you have access to the interactive **MariaDB** console, the connection with TLS succeeds.

2.  Attempt to connect as the `example`{.literal} user with TLS disabled:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u example -p -h server.example.com --skip-ssl
    ERROR 1045 (28000): Access denied for user 'example'@'server.example.com' (using password: YES)
    ```

    The server rejected the login attempt because this user requires TLS but the option `--skip-ssl`{.literal} disables it.

### [1.5. Configuring the MariaDB client to use TLS encryption by default](#configuring-the-mariadb-client-to-use-tls-encryption-by-default) {#configuring-the-mariadb-client-to-use-tls-encryption-by-default .title}

On RHEL, globally configure that the MariaDB client uses TLS encryption and verifies that the Common Name (CN) in the server certificate matches the hostname the user connects to. This prevents man-in-the-middle attacks.

**Prerequisites**

-   The MariaDB server has TLS support enabled.
-   If the certificate authority (CA) that issued the server's certificate is not trusted by RHEL, the CA certificate has been copied to the client.
-   If the FIPS mode is enabled, this client supports the Extended Master Secret (EMS) extension or uses TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced on RHEL 9.2 and later](https://access.redhat.com/solutions/7018256).

**Procedure**

1.  If RHEL does not trust the CA that issued the server's certificate:

    a.  Copy the CA certificate to the `/etc/pki/ca-trust/source/anchors/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        # cp <path>/ca.crt.pem /etc/pki/ca-trust/source/anchors/
        ```

    b.  Set permissions that enable all users to read the CA certificate file:

        ``` {.language-plaintext tabindex="-1"}
        # chmod 644 /etc/pki/ca-trust/source/anchors/ca.crt.pem
        ```

    c.  Rebuild the CA trust database:

        ``` {.language-plaintext tabindex="-1"}
        # update-ca-trust
        ```

2.  Create the `/etc/my.cnf.d/mariadb-client-tls.cnf`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [client-mariadb]
    ssl
    ssl-verify-server-cert
    ```

    These settings define that the MariaDB client uses TLS encryption (`ssl`{.literal}) and that the client compares the hostname with the CN in the server certificate (`ssl-verify-server-cert`{.literal}).

**Verification**

-   Connect to the server by using the hostname, and display the server status:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h server.example.com -e status
    ...
    SSL:        Cipher in use is TLS_AES_256_GCM_SHA384
    ```

    If the `SSL`{.literal} entry contains `Cipher in use is…​`{.literal}, the client encrypted the connection.

    Note that the user you use in this command has permissions to authenticate remotely.

    If the hostname you connect to does not match the hostname in the TLS certificate of the server, the `ssl-verify-server-cert`{.literal} parameter causes the connection to fail. For example, if you connect to `localhost`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h localhost -e status
    ERROR 2026 (HY000): SSL connection error: Validation of SSL server certificate failed
    ```

### [1.6. Backing up and restoring MariaDB data with logical dumps](#backing-up-and-restoring-mariadb-data-with-logical-dumps) {#backing-up-and-restoring-mariadb-data-with-logical-dumps .title}

A logical backup of MariaDB data consists of the SQL statements necessary to restore the data. The advantage of logical backup over physical backup is that you can restore the logical back up on other hardware configurations and MariaDB versions.

#### [1.6.1. Performing a logical backup by using mariadb-dump](#performing-a-logical-backup-by-using-mariadb-dump) {#performing-a-logical-backup-by-using-mariadb-dump .title}

You can use the `mariadb-dump`{.literal} utility to back up databases while the MariaDB server is running and store the exported data in an SQL file. Store the backup in a safe location to be able to recover it in data loss scenarios.

Frequent scenarios with `mariadb-dump`{.literal} include:

-   Backing up a single database
-   Backing up multiple databases
-   Backing up all databases

The `mariadb-dump`{.literal} utility stores its output in a single file. If you want to back up multiple databases and require one file per database, back up each database individually.

Note

The `mariadb-dump`{.literal} utility can back up only databases. This also includes server settings stored in the `mysql`{.literal} database. However, the utility does not back up configuration files, such as `/etc/my.cnf`{.literal}.

**Prerequisites**

-   The `mariadb`{.literal} service is running.
-   You have credentials with permissions to back up a database, for example, the `root`{.literal} account.

**Procedure**

-   Create a consistent and comprehensive logical backup of MariaDB databases:

    ``` {.language-plaintext tabindex="-1"}
    # mariadb-dump -u <username> -p --routines --events --triggers --single-transaction --result-file=backup.sql --databases <database_1> <database_2>
    ```

    where:

    `-u `{.literal}*`<username>`{.literal}*
    :   Sets the username the utility uses to connect to the database server.

    `-p`{.literal}
    :   Prompts for the password.

    `--routines`{.literal}
    :   Includes stored procedures and functions in the backup.

    `--events`{.literal}
    :   Includes scheduled events in the backup.

    `--triggers`{.literal}
    :   Includes triggers in the backup.

    `--single-transaction`{.literal}

    :   Initiates a consistent snapshot of databases with a transactional storage engine, such as InnoDB. By using a single transaction, all read operations reflect the database state at the moment the dump begins.

        If you still use a non-transactional storage engine, such as MyISAM, use the `--lock-tables`{.literal} option instead of `--single-transaction`{.literal} to ensure a consistent backup.

    `--result-file=`{.literal}*`<output_file>`{.literal}*
    :   Defines in which file `mariadb-dump`{.literal} stores the output.

    `--databases `{.literal}*`<list_of_databases>`{.literal}*

    :   Defines the databases to back up. Alternatively, to back up all databases at once, use the `--all-databases`{.literal} option.

        Important

        A backup of a database contains only the data from that database. It does not include MariaDB user accounts or other server settings. MariaDB stores this essential security and system information in a separate `mysql`{.literal} system database. Therefore, you must back up `mysql`{.literal} as well if you need to preserve these settings.

**Verification**

-   Restore the backup in a sandbox environment and ensure that the data is correct.

#### [1.6.2. Restoring MariaDB data from a dump in SQL format](#restoring-mariadb-data-from-a-dump-in-sql-format) {#restoring-mariadb-data-from-a-dump-in-sql-format .title}

If you backed up one or multiple databases to an SQL file, you can use this file to re-create the database structure and its data.

**Prerequisites**

-   The `mariadb`{.literal} service is running.
-   You have credentials with permissions to restore data, for example, the `root`{.literal} account.

**Procedure**

1.  If the database you want to restore already exists and your SQL file does not contain `DROP TABLE IF EXISTS`{.literal} statements, manually remove the tables or the entire database:

    -   To remove a table, enter:

        ``` {.language-plaintext tabindex="-1"}
        # mariadb -u root -p -e "DROP TABLE <database>.<table>;"
        ```

        Repeat this command for every table that the SQL file re-creates.

    -   To remove a database, enter:

        ``` {.language-plaintext tabindex="-1"}
        # mariadb -u root -p -e "DROP DATABASE <database>;"
        ```

        Repeat this command for every database that the SQL file re-creates.

2.  Import the SQL file:

    ``` {.language-plaintext tabindex="-1"}
    # mariadb -u root -p < backup.sql"
    ```

**Verification**

-   Connect to a MariaDB database and query data, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mariadb -u root -p <database> -e "*SELECT * FROM <table>;"
    ```

### [1.7. Backing up and restoring MariaDB data with physical copies](#backing-up-and-restoring-mariadb-data-with-physical-copies) {#backing-up-and-restoring-mariadb-data-with-physical-copies .title}

A physical backup of MariaDB data contains files and directories that store the content. This method is typically faster and smaller in size.

#### [1.7.1. Performing a physical online backup by using mariabackup](#performing-a-physical-online-backup-by-using-mariabackup) {#performing-a-physical-online-backup-by-using-mariabackup .title}

You can create physical online backups of your MariaDB server by using the `mariabackup`{.literal} utility to backup InnoDB, Aria, and MyISAM tables while the server is running. The utility supports full backup capability for MariaDB server, which includes encrypted and compressed data.

**Prerequisites**

-   The `mariadb-backup`{.literal} package is installed on the system:
-   You must provide `mariabackup`{.literal} with credentials for the user that runs the backup. You can provide the credentials either on the command line or by a configuration file.
-   Users of `mariabackup`{.literal} must have the `RELOAD`{.literal}, `LOCK TABLES`{.literal}, and `REPLICATION CLIENT`{.literal} privileges.

**Procedure**

-   Use one of the following options to create a backup:

    -   To create a backup while providing credentials on the command line, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ mariabackup --backup --target-dir <backup_directory> --user <backup_user> --password <backup_passwd>
        ```

        The `target-dir`{.literal} option defines the directory where mariabackup stores the backup files. If you want to perform a full backup, the target directory must be empty or not exist.

        The `user`{.literal} and `password`{.literal} options allow you to configure the user name and the password.

    -   To create a backup with credentials set in a configuration file:

        i.  Create a configuration file in the `/etc/my.cnf.d/`{.literal} directory, for example, `/etc/my.cnf.d/mariabackup.cnf`{.literal}.

        ii. Add the following content to the file:

            ``` {.language-plaintext tabindex="-1"}
            [mysqld]
            user=<backup_username>
            password=<password>
            ```

        iii. Perform the backup:

             ``` {.language-plaintext tabindex="-1"}
             $ mariabackup --backup --target-dir <backup_directory>
             ```

**Additional resources**

-   [Full Backup and Restore with mariabackup](https://mariadb.com/kb/en/library/full-backup-and-restore-with-mariadb-backup/)

#### [1.7.2. Restoring data by using mariabackup](#restoring-data-using-the-mariabackup-utility) {#restoring-data-by-using-mariabackup .title}

If you have a MariaDB backup created by the `mariabackup`{.literal} utility, you can use the same utility to restore the data.

**Prerequisites**

-   The `mariadb`{.literal} service is stopped.
-   The data directory is empty.
-   Users of `mariabackup`{.literal} must have the `RELOAD`{.literal}, `LOCK TABLES`{.literal}, and `REPLICATION CLIENT`{.literal} privileges.

**Procedure**

1.  Use one of the following options to restore the data:

    -   To restore data from the backup in the `/var/mariadb/backup/`{.literal} directory and keep the original backup files, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ mariabackup --copy-back --target-dir=/var/mariadb/backup/
        ```

    -   To restore data from the backup in the `/var/mariadb/backup/`{.literal} directory and remove the original backup files, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ mariabackup --move-back --target-dir=/var/mariadb/backup/
        ```

2.  Fix the file permissions. For example, to recursively change ownership of the files to the `mysql`{.literal} user and group, enter:

    ``` {.language-plaintext tabindex="-1"}
    # chown -R mysql:mysql /var/lib/mysql/
    ```

    When restoring a database, `mariabackup`{.literal} preserves the file and directory privileges of the backup. However, `mariabackup`{.literal} writes the files to disk as the user and group restoring the database. Therefore, after restoring a backup, you must adjust the owner of the data directory to match the user and group for the MariaDB server.

3.  Start the `mariadb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start mariadb.service
    ```

**Additional resources**

-   [Full Backup and Restore with mariabackup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup)

#### [1.7.3. Performing a file system backup on a MariaDB server](#performing-a-file-system-backup-on-a-mariadb-server) {#performing-a-file-system-backup-on-a-mariadb-server .title}

A file system level backup is a fast way to back up a complete MariaDB instance. This method requires a shutdown of the `mariadb`{.literal} service for data consistency.

Important

A file system-level backup is specific to an architecture and MariaDB version. You cannot restore data backed up by this method on a different architecture or MariaDB version.

**Procedure**

1.  Stop the `mariadb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop mariadb.service
    ```

2.  Create a backup directory, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /root/mariadb-backup/{data,config}/
    ```

3.  Back up the data directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /var/lib/mysql/ /root/mariadb-backup/data/
    ```

4.  Back up the configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /etc/my.cnf /etc/my.cnf.d/ /root/mariadb-backup/config/
    ```

5.  Start the `mariadb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start mariadb.service
    ```

#### [1.7.4. Restoring a file system backup on a MariaDB server](#restoring-a-file-system-backup-on-a-mariadb-server) {#restoring-a-file-system-backup-on-a-mariadb-server .title}

If your MariaDB instance has been corrupted, and you previously performed a file system backup that includes the data directory and the configuration files, restore the instance from this backup.

**Prerequisites**

-   [You performed a file system backup on a MariaDB server](#performing-a-file-system-backup-on-a-mariadb-server "1.7.3. Performing a file system backup on a MariaDB server").

-   The target server must meet the following conditions of the backup source:

    -   The MariaDB version must be identical or higher.
    -   The system architecture must be identical.

**Procedure**

1.  Stop the `mariadb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop mariadb.service
    ```

2.  Remove the current `/var/lib/mysql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # rm -rf /var/lib/mysql/
    ```

3.  Restore the data directory from your backup:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /root/mariadb-backup/data/mysql/ /var/lib/
    ```

4.  Ensure the correct ownership of the `/var/lib/mysql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # chown -R mysql:mysql /var/lib/mysql/
    ```

5.  Restore the SELinux context of the `/var/lib/mysql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /var/lib/mysql/
    ```

6.  Remove the current configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # rm -rf /etc/my.cnf /etc/my.cnf.d/
    ```

7.  Restore the configuration files from your backup:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /root/mariadb-backup/config/my.cnf /root/mariadb-backup/config/my.cnf.d/ /etc/
    ```

8.  Ensure the correct ownership of the configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # chown -R root:root /etc/my.cnf /etc/my.cnf.d/
    ```

9.  Restore the SELinux context of the configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /etc/my.cnf /etc/my.cnf.d/
    ```

10. Start the `mariadb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start mariadb.service
    ```

**Verification**

-   Connect to a MariaDB database and query data, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mariadb -u root -p <database> -e "*SELECT * FROM <table>;"
    ```

### [1.8. Replicating MariaDB with Galera](#replicating-mariadb-with-galera) {#replicating-mariadb-with-galera .title}

You can replicate a MariaDB database using the Galera solution to create a synchronous multi-source cluster for high availability and data consistency.

Warning

Replication itself is not a sufficient backup solution. Replication protects source servers against hardware failures, but it does not ensure protection against data loss.

#### [1.8.1. MariaDB Galera Cluster synchronous replication](#mariadb-galera-cluster-synchronous-replication) {#mariadb-galera-cluster-synchronous-replication .title}

MariaDB Galera Cluster provides synchronous multi-source replication that allows all nodes to be writable and ensures data consistency across the cluster.

The write set replication API (**wsrep API**) defines the interface between Galera replication and a MariaDB database.

The main features of MariaDB Galera Cluster are:

-   Synchronous replication
-   Active-active multi-source topology
-   Read and write to any cluster node
-   Automatic membership control, failed nodes drop from the cluster
-   Automatic node joining
-   Parallel replication on row level
-   Direct client connections: users can log in to the cluster nodes, and work with the nodes directly while the replication runs

Synchronous replication means that a server replicates a transaction at commit time by broadcasting the write set associated with the transaction to every node in the cluster. The client (user application) connects directly to the Database Management System (DBMS), and experiences behavior that is similar to native MariaDB.

Synchronous replication guarantees that a change that happened on one node in the cluster happens on other nodes in the cluster at the same time.

Therefore, synchronous replication has the following advantages over asynchronous replication:

-   No delay in propagation of the changes between particular cluster nodes
-   All cluster nodes are always consistent
-   The latest changes are not lost if one of the cluster nodes crashes
-   Transactions on all cluster nodes are executed in parallel
-   Causality across the whole cluster

**Additional resources**

-   [What is Galera replication](https://mariadb.com/docs/galera-cluster/readme/about-galera-replication)
-   [What is MariaDB Galera Cluster](https://mariadb.com/docs/galera-cluster/readme/mariadb-galera-cluster-guide)
-   [Getting started with MariaDB Galera Cluster](https://mariadb.com/docs/galera-cluster/galera-management/getting-started-with-mariadb-galera-cluster)

#### [1.8.2. Components to build MariaDB Galera Cluster](#components-to-build-mariadb-galera-cluster) {#components-to-build-mariadb-galera-cluster .title}

Before deploying a functional, synchronously replicated MariaDB Galera Cluster, install and understand the MariaDB Server, Galera Replication library, and supporting Galera packages.

To build **MariaDB Galera Cluster**, you must install the following packages on your system:

-   `mariadb-server-galera`{.literal} - contains support files and scripts for **MariaDB Galera Cluster**.

-   `mariadb-server`{.literal} - is patched by **MariaDB** upstream to include the write set replication API (**wsrep API**). This API provides the interface between **Galera** replication and **MariaDB**.

-   `galera`{.literal} - is patched by **MariaDB** upstream to add full support for **MariaDB**. The `galera`{.literal} package contains the following:

    -   **Galera Replication Library** provides the whole replication functionality.
    -   The **Galera Arbitrator** utility serves as a cluster member that participates in voting in split-brain scenarios. However, **Galera Arbitrator** cannot participate in the actual replication.
    -   **Galera Systemd service** and **Galera wrapper script** deploy the Galera Arbitrator utility. RHEL 10 provides the upstream version of these files, located at `/usr/lib/systemd/system/garbd.service`{.literal} and `/usr/sbin/garb-systemd`{.literal}.

**Additional resources**

-   [Galera Replication Library](https://mariadb.com/docs/galera-cluster/readme/about-galera-replication#generic-replication-library)
-   [Galera Arbitrator](https://galeracluster.com/library/documentation/arbitrator.html)

#### [1.8.3. Deploying MariaDB Galera Cluster](#deploying-mariadb-galera-cluster) {#deploying-mariadb-galera-cluster .title}

You can deploy MariaDB Galera Cluster by installing the required packages, configuring cluster settings, and bootstrapping the first node to create a new cluster.

**Prerequisites**

-   All of the nodes in the cluster have [TLS configured](#setting-up-tls-encryption-on-a-mariadb-server "1.4. Setting up TLS encryption on a MariaDB server").

-   All certificates on all nodes must have the `Extended Key Usage`{.literal} field set to:

    ``` {.language-plaintext tabindex="-1"}
    TLS Web Server Authentication, TLS Web Client Authentication
    ```

**Procedure**

1.  Install the MariaDB Galera Cluster packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install mariadb-server-galera
    ```

    As a result, this command installs the following packages with their dependencies:

    -   `mariadb-server-galera`{.literal}

    -   `mariadb-server`{.literal}

    -   `galera`{.literal}

        For more information about these packages required to build MariaDB Galera Cluster, see [Components to build MariaDB Cluster](#components-to-build-mariadb-galera-cluster "1.8.2. Components to build MariaDB Galera Cluster").

2.  Update the MariaDB server replication configuration before you add the system to a cluster for the first time. The `/etc/my.cnf.d/galera.cnf`{.literal} file contains the default configuration. Before deploying MariaDB Galera Cluster, set the `wsrep_cluster_address`{.literal} option in the `/etc/my.cnf.d/galera.cnf`{.literal} file on all nodes to start with the following string:

    ``` {.language-plaintext tabindex="-1"}
    gcomm://
    ```

    -   For the initial node, it is possible to set `wsrep_cluster_address`{.literal} as an empty list:

        ``` {.language-plaintext tabindex="-1"}
        wsrep_cluster_address="gcomm://"
        ```

        The default Galera configuration is distributed in this file. Set this option before you add the node to a cluster for the first time.

3.  On each additional node, set `wsrep_cluster_address`{.literal} in the `/etc/my.cnf.d/galera.cnf`{.literal} file to include the address of a node that is already in the running cluster. For example:

    ``` {.language-plaintext tabindex="-1"}
    wsrep_cluster_address="gcomm://192.0.2.10"
    ```

    For more information about how to set the Galera Cluster address, see [Galera Cluster Address](https://mariadb.com/docs/galera-cluster/galera-management/galera-cluster-address).

4.  Enable the `wsrep`{.literal} API on every node by setting the `wsrep_on=1`{.literal} option in the `/etc/my.cnf.d/galera.cnf`{.literal} configuration file.

5.  Add the `wsrep_provider_options`{.literal} variable to the Galera configuration file with the TLS keys and certificates. For example:

    ``` {.language-plaintext tabindex="-1"}
    wsrep_provider_options="socket.ssl_cert=/etc/pki/tls/certs/source.crt;socket.ssl_key=/etc/pki/tls/private/source.key;socket.ssl_ca=/etc/pki/tls/certs/ca.crt"
    ```

6.  Bootstrap a first node of a new cluster by running the following wrapper on that node:

    ``` {.language-plaintext tabindex="-1"}
    # galera_new_cluster
    ```

    This wrapper ensures that the MariaDB server daemon (`mariadbd`{.literal}) runs with the `--wsrep-new-cluster`{.literal} option. This option provides the information that there is no existing cluster to connect to. Therefore, the node creates a new UUID to identify the new cluster.

    Note

    The `mariadb`{.literal} service supports a systemd method for interacting with multiple MariaDB server processes. Therefore, in cases with multiple running MariaDB servers, you can bootstrap a specific instance by specifying the instance name as a suffix:

    ``` {.language-plaintext tabindex="-1"}
    # galera_new_cluster mariadb@node1
    ```

7.  Connect other nodes to the cluster by running the following command on each of the nodes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start mariadb
    ```

    As a result, the node connects to the cluster, and synchronizes itself with the state of the cluster.

**Verification**

-   See [MariaDB Galera cluster status variables](#mariadb-galera-cluster-status-variables "1.8.4. MariaDB Galera cluster status variables").

**Additional resources**

-   [Getting started with MariaDB Galera Cluster](https://mariadb.com/kb/en/library/getting-started-with-mariadb-galera-cluster/)

#### [1.8.4. MariaDB Galera cluster status variables](#mariadb-galera-cluster-status-variables) {#mariadb-galera-cluster-status-variables .title}

It is important to monitor and ensure the health, performance, and synchronization of a MariaDB Galera cluster. For that, you can query status variables on each node to monitor the node and the cluster.

To check the status of a MariaDB Galera cluster, you can use the following queries:

-   Display the number of nodes in the cluster:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e 'show status like "wsrep_cluster_size";'
    +--------------------+-------+
    | Variable_name      | Value |
    +--------------------+-------+
    | wsrep_cluster_size | 4     |
    +--------------------+-------+
    ```

-   Display the node's cluster component status:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e 'show status like "wsrep_cluster_status";'
    +----------------------+---------+
    | Variable_name        | Value   |
    +----------------------+---------+
    | wsrep_cluster_status | Primary |
    +----------------------+---------+
    ```

    The value of the `wsrep_cluster_status`{.literal} variable indicates the status of the cluster component the current node belongs to. Possible values are:

    -   `Primary`{.literal}: The cluster is functioning normally. A quorum is present. In a healthy cluster, all nodes report `Primary`{.literal}.
    -   `Non-primary`{.literal}: The node has lost the connection to the primary component of the cluster and is no longer part of the active cluster. However, the node still can serve read queries but cannot process write operations.
    -   `Disconnected`{.literal}: The node is not connected to any cluster component. Consequently, it cannot accept queries and is not replicating any data.

-   Display the node's status:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e 'show status like "wsrep_local_state_comment";'
    +---------------------------+--------+
    | Variable_name             | Value  |
    +---------------------------+--------+
    | wsrep_local_state_comment | Synced |
    +---------------------------+--------+
    ```

    The following are frequent values of the `wsrep_local_state_comment`{.literal} variable:

    -   `Synced`{.literal}: The node is fully synchronized within the cluster and actively participating in replication.
    -   `Desynced`{.literal}: The node is still part of the cluster but it is primarily busy with the state transfer.
    -   `Joining`{.literal}: The node is in the process of joining a cluster.
    -   `Joined`{.literal}: The node has successfully joined a cluster. It can receive and apply write sets from the cluster.
    -   `Donor`{.literal}: The node currently provides a State Snapshot Transfer (SST) to a joining node. When a new node joins and requires a full state transfer, the cluster selects an existing node to send the necessary data.

-   Check whether the node accepts write sets from the cluster:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e 'show status like "wsrep_ready";'
    +---------------+-------+
    | Variable_name | Value |
    +---------------+-------+
    | wsrep_ready   | ON    |
    +---------------+-------+
    ```

    When the `wsrep_ready`{.literal} variable is `ON`{.literal}, the node has successfully initialized its components and connects to a cluster. Additionally, the node is synchronized or has reached a state where it can serve queries.

-   Check whether the node has network connectivity with other hosts:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e 'show status like "wsrep_connected";'
    +-----------------+-------+
    | Variable_name   | Value |
    +-----------------+-------+
    | wsrep_connected | ON    |
    +-----------------+-------+
    ```

    The `ON`{.literal} value means that node has connectivity to at least one member in the cluster.

-   Display the average size of the local received queue for write sets since the last `FLUSH STATUS`{.literal} command or since the server started:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e 'show status like "wsrep_local_recv_queue_avg";'
    +----------------------------+-------+
    | Variable_name              | Value |
    +----------------------------+-------+
    | wsrep_local_recv_queue_avg | 0.012 |
    +----------------------------+-------+
    ```

    A value near 0 is the ideal state and indicates that the node continues applying write sets as the node receives them. A persistently high or growing value can be an indicator of performance bottlenecks, such as slow disk I/O.

-   Display the flow control status:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e 'show status like "wsrep_flow_control_paused";'
    +---------------------------+-------+
    | Variable_name             | Value |
    +---------------------------+-------+
    | wsrep_flow_control_paused | 0     |
    +---------------------------+-------+
    ```

    This variable represents the fraction of time a node is paused and unable to process incoming transactions because its receive queue is too full, triggering flow control. A value close to 0 indicates the node continues with the replication workload efficiently. A value approaching 1.0 means that the node frequently or constantly encounters difficulty in applying write sets and can be a bottleneck for the cluster.

    If the node is frequently pausing, you can adjust the `wsrep_slave_threads`{.literal} parameter in the `/etc/my.cnf.d/galera.cnf`{.literal} file.

-   Display the average distance between the lowest and highest sequence numbers the node can apply in parallel:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e 'show status like "wsrep_cert_deps_distance";'
    +--------------------------+-------+
    | Variable_name            | Value |
    +--------------------------+-------+
    | wsrep_cert_deps_distance | 1     |
    +--------------------------+-------+
    ```

    A higher value indicates a greater degree of parallelism. It is the optimal value you can use in the `wsrep_slave_threads`{.literal} parameter in the `/etc/my.cnf.d/galera.cnf`{.literal} file.

#### [1.8.5. Adding a new node to MariaDB Galera Cluster](#adding-a-new-node-to-mariadb-galera-cluster) {#adding-a-new-node-to-mariadb-galera-cluster .title}

You can add a new node to your MariaDB Galera Cluster or reconnect an existing one by configuring the cluster address in the node's configuration file.

**Procedure**

-   On the particular node, provide an address to one or more existing cluster members in the `wsrep_cluster_address`{.literal} option within the `[mariadb]`{.literal} section of the `/etc/my.cnf.d/galera.cnf`{.literal} configuration file :

    ``` {.language-plaintext tabindex="-1"}
    [mariadb]
    wsrep_cluster_address="gcomm://192.168.0.1"
    ```

    When a new node connects to one of the existing cluster nodes, it is able to see all nodes in the cluster.

    However, preferably list all nodes of the cluster in `wsrep_cluster_address`{.literal}.

    As a result, any node can join a cluster by connecting to any other cluster node, even if one or more cluster nodes are down. When all members agree on the membership, the cluster's state is changed. If the new node's state differs from the cluster's, it requests an Incremental State Transfer (IST) or State Snapshot Transfer (SST) to ensure consistency.

**Additional resources**

-   [Getting started with MariaDB Galera Cluster](https://mariadb.com/kb/en/library/getting-started-with-mariadb-galera-cluster/)
-   [Introduction to State Snapshot Transfers](https://mariadb.com/docs/galera-cluster/galera-management/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts)
-   [Securing Communications in Galera Cluster](https://mariadb.com/kb/en/securing-communications-in-galera-cluster/)

#### [1.8.6. MariaDB Galera Cluster restart behavior](#mariadb-galera-cluster-restart-behavior) {#mariadb-galera-cluster-restart-behavior .title}

If you shut down all nodes at the same time, you stop the cluster, and the running cluster no longer exists. However, the cluster's data still exist. To restart the cluster, bootstrap a first node.

Warning

If the cluster is not bootstrapped, starting `mariadb`{.literal} on the first node with `systemctl start mariadb`{.literal} does not bootstrap the cluster. The node instead tries to connect to a node listed in `wsrep_cluster_address`{.literal} in `/etc/my.cnf.d/galera.cnf`{.literal}. If no nodes are currently running, the restart fails.

**Additional resources**

-   [Getting started with MariaDB Galera Cluster](https://mariadb.com/kb/en/library/getting-started-with-mariadb-galera-cluster/)

### [1.9. Migrating a MariaDB instance from a previous RHEL version to MariaDB 10.11 on RHEL 10](#migrating-a-mariadb-instance-from-a-previous-rhel-version-to-mariadb-10-11-on-rhel-10) {#migrating-a-mariadb-instance-from-a-previous-rhel-version-to-mariadb-10.11-on-rhel-10 .title}

RHEL 10 provides MariaDB 10.11. If you run a MariaDB instance on a previous RHEL version, you can configure RHEL 10 on a new host and migrate the instance to it.

**Prerequisites**

-   You configure RHEL 10 on a new host.
-   You performed a file system backup of the MariaDB instance on the RHEL 8 or RHEL 9 host.

**Procedure**

1.  Install the `mariadb-server`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install mariadb-server
    ```

2.  Stop the service if it is already running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop mariadb.service
    ```

3.  Copy the content of the `/var/lib/mysql/`{.literal} directory from the previous host to the same location on the RHEL 10 host.

4.  Copy the configuration files from the previous host to the `/etc/my.cnf.d/`{.literal} directory.

5.  Ensure that the files include only options valid for MariaDB 10.11. For details, see the [upstream documentation](https://mariadb.com/kb/en/changes-improvements-in-mariadb-1011/).

6.  Restore the SELinux context:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -rv /var/lib/mysql/
    # restorecon -rv /etc/my.cnf.d/
    ```

7.  Ensure the correct ownership of `/var/lib/mysql/`{.literal} and its subdirectories:

    ``` {.language-plaintext tabindex="-1"}
    # chown -R mysql:mysql /var/lib/mysql/
    ```

8.  Enable and start the `mariadb`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now mariadb.service
    ```

    When the service starts, MariaDB automatically checks, repairs, and updates internal tables.

**Verification**

-   Establish a connection to the MariaDB server:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h <hostname>
    ```

### [1.10. Upgrading from a RHEL 10 version of MariaDB 10.11 to MariaDB 11.8](#upgrading-from-a-rhel-10-version-of-mariadb-10-11-to-mariadb-11-8) {#upgrading-from-a-rhel-10-version-of-mariadb-10.11-to-mariadb-11.8 .title}

You can upgrade your MariaDB database from version 10.11 to 11.8 on RHEL 10 to access new features and improvements.

For notable enhancements and changes, see the [release note](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/10.2_release_notes/new-features-and-enhancements#Jira-RHEL-115468) in the RHEL 10.2 Release Notes document.

Important

Certain risks and known problems relate to an in-place upgrade. For example, some queries might not work or run in a different order than before the upgrade. For more information about these risks and problems, and for general information about an in-place upgrade, see [MariaDB 11.8 Release Notes](https://mariadb.com/docs/release-notes/community-server/11.8).

**Prerequisites**

-   You created a backup of your MariaDB databases and configuration files.

**Procedure**

1.  Stop the MariaDB server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop mariadb.service
    ```

2.  Switch to MariaDB 11.8:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install --allowerasing mariadb11.8-server
    ```

    Important

    Review the proposed `dnf`{.literal} transaction carefully before proceeding. Ensure that its equivalent in the new version replaces each package from the previous version. The `--allowerasing`{.literal} option can lead to unintended package removal if the installation list is incomplete, potentially removing more software than it installs.

3.  Adjust the configuration so that the option files located in the `/etc/my.cnf.d/`{.literal} directory include only options valid for MariaDB 11.8. For details, see the upstream documentation for [MariaDB 11.4](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-10-11-to-mariadb-11-4#incompatible-changes-between-10.11-and-11.4) and [MariaDB 11.8](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-11-4-to-mariadb-11-8#incompatible-changes-between-11.4-and-11.8).

4.  Start the MariaDB server.

    -   If upgrading the primary node in a Galera cluster, enter:

        ``` {.language-plaintext tabindex="-1"}
        # galera_new_cluster
        ```

        The `mariadb`{.literal} service starts automatically.

    -   If upgrading a database running standalone or a replica in a Galera cluster, enter:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl start mariadb.service
        ```

5.  Run the `mariadb-upgrade`{.literal} utility to check and repair internal tables.

    -   If upgrading a Galera cluster node:

        ``` {.language-plaintext tabindex="-1"}
        # mariadb-upgrade --skip-write-binlog
        ```

    -   If upgrading a database running standalone:

        ``` {.language-plaintext tabindex="-1"}
        # mariadb-upgrade
        ```

## [Chapter 2. Using MySQL](#using-mysql) {#chapter-2.-using-mysql .title}

MySQL server is a high-performance, open source relational database management system (RDBMS). It offers an SQL interface for data access and includes advanced features, such as support for multiple storage engines.

You can install, configure, back up, migrate, and replicate MySQL databases on RHEL by using MySQL replication.

### [2.1. Installing MySQL](#installing-mysql) {#installing-mysql .title}

RHEL 10 provides MySQL 8.4 as the initial version of the Application Stream, which can install as an RPM package. In minor releases of RHEL 10, Red Hat provides additional MySQL versions as application streams with a shorter life cycle.

Note

By design, you can install only one version (stream) of the same application stream and, because of conflicting RPM packages, you cannot install MariaDB and MySQL on the same host. As an alternative, you can run the database server services in a container. See [Using containers to run multiple MariaDB and MySQL instances on a single host](#using-containers-to-run-multiple-mariadb-and-mysql-instances-on-a-single-host_mysql "2.2. Using containers to run multiple MariaDB and MySQL instances on a single host").

**Procedure**

1.  Install MySQL server packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install mysql8.4-server
    ```

2.  Enable and start the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now mysqld.service
    ```

3.  Improve the security after the installation:

    ``` {.language-plaintext tabindex="-1"}
    $ mysql_secure_installation
    ```

    The command launches a fully interactive script, which prompts for each step in the process. The script enables you to improve security in the following ways:

    -   Setting a password for root accounts
    -   Removing anonymous users
    -   Disallowing remote root logins (outside the local host)

### [2.2. Using containers to run multiple MariaDB and MySQL instances on a single host](#using-containers-to-run-multiple-mariadb-and-mysql-instances-on-a-single-host_mysql) {#using-containers-to-run-multiple-mariadb-and-mysql-instances-on-a-single-host-1 .title}

If you install MariaDB or MySQL from packages, you can only run one of these services and only a single version of it on the same host. As an alternative, you can run the services in a container.

You can configure the following scenarios:

-   You want to run multiple instances of MariaDB or MySQL on the same host.
-   You want to run both MariaDB and MySQL on the same host.

Important

The container names and host ports of the database servers must differ.

**Prerequisites**

-   The `podman`{.literal} package is installed.

**Procedure**

1.  Authenticate to the `registry.redhat.io`{.literal} registry by using your Red Hat Customer Portal account:

    ``` {.language-plaintext tabindex="-1"}
    # podman login registry.redhat.io
    ```

    Skip this step if you are already logged in to the container registry.

2.  Start the containers you want to use:

    -   MariaDB 10.11:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run -d --name <container_name_1> -e MARIADB_ROOT_PASSWORD=<password> -p <host_port_1>:3306 rhel10/mariadb-1011
        ```

        For more information about the usage of this container image, see the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/rhel10/mariadb-1011/677d10b3607921b4d74fb9f5).

    -   MariaDB 11.8:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run -d --name <container_name_2> -e MARIADB_ROOT_PASSWORD=<password> -p <host_port_2>:3306 rhel10/mariadb-118
        ```

        For more information about the usage of this container image, see the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/en/software/containers/rhel9/mariadb-118/69845dc2e1b6f8096d7384c4).

    -   MySQL 8.4:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run -d --name <container_name_3> -e MYSQL_ROOT_PASSWORD=<password> -p <host_port_3>:3306 rhel10/mysql-84
        ```

        For more information about the usage of this container image, see the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/rhel10/mysql-84/677d145d607921b4d74fcc6d).

3.  To ensure that clients can access the database server on the network, open the host ports in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port={<host_port_1>/tcp,<host_port_2>/tcp,...}
    # firewall-cmd --reload
    ```

**Verification**

1.  Connect to the database server and log in as root:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h localhost -P <host_port> --protocol tcp
    ```

2.  Optional: Display information about the running containers:

    ``` {.language-plaintext tabindex="-1"}
    $ podman ps
    ```

**Additional resources**

-   [Building, running, and managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/index)
-   [Browse containers in the Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/search)

### [2.3. Configuring network access to MySQL](#configuring-mysql) {#configuring-network-access-to-mysql .title}

You must configure MySQL to listen on network interfaces and open firewall ports to allow remote client access to the database server.

**Procedure**

1.  Edit the `mysqld`{.literal} section of the `/etc/my.cnf.d/mysql-server.cnf`{.literal} file. You can set the following configuration directives:

    -   `bind-address`{.literal} - is the address on which the server listens. Possible options are:

        -   a host name
        -   an IPv4 address
        -   an IPv6 address

    -   `skip-networking`{.literal} - controls whether the server listens for TCP/IP connections. Possible values are:

        -   0 - to listen for all clients
        -   1 - to listen for local clients only

    -   `port`{.literal} - the port on which MySQL listens for TCP/IP connections.

2.  To ensure that clients can access the database server on the network, open the port in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=mysql
    # firewall-cmd --reload
    ```

3.  Restart the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart mysqld.service
    ```

### [2.4. Setting up TLS encryption on a MySQL server](#setting-up-tls-encryption-on-a-mysql-server) {#setting-up-tls-encryption-on-a-mysql-server .title}

By default, MySQL uses unencrypted connections. For secure connections, enable TLS support on the MySQL server and configure your clients to establish encrypted connections.

#### [2.4.1. Placing the CA certificate, server certificate, and private key on the MySQL server](#placing-the-ca-certificate-server-certificate-and-private-key-on-the-mysql-server) {#placing-the-ca-certificate-server-certificate-and-private-key-on-the-mysql-server .title}

Before you can enable TLS encryption on the MySQL server, store the certificate authority (CA) certificate, the server certificate, and the private key on the MySQL server.

**Prerequisites**

-   The following files in Privacy Enhanced Mail (PEM) format have been copied to the server:

    -   The private key of the server: `server.example.com.key.pem`{.literal}
    -   The server certificate: `server.example.com.crt.pem`{.literal}
    -   The Certificate Authority (CA) certificate: `ca.crt.pem`{.literal}

    For details about creating a private key and certificate signing request (CSR), as well as about requesting a certificate from a CA, see your CA's documentation.

**Procedure**

1.  Store the CA and server certificates in the `/etc/pki/tls/certs/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mv <path>/server.example.com.crt.pem /etc/pki/tls/certs/
    # mv <path>/ca.crt.pem /etc/pki/tls/certs/
    ```

2.  Set permissions on the CA and server certificate that enable the MySQL server to read the files:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 644 /etc/pki/tls/certs/server.example.com.crt.pem /etc/pki/tls/certs/ca.crt.pem
    ```

    Because certificates are part of the communication before the client and server establish a secure connection, any client can retrieve them without authentication. Therefore, you do not need to set strict permissions on the CA and server certificate files.

3.  Store the server's private key in the `/etc/pki/tls/private/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mv <path>/server.example.com.key.pem /etc/pki/tls/private/
    ```

4.  Set secure permissions on the server's private key:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 640 /etc/pki/tls/private/server.example.com.key.pem
    # chgrp mysql /etc/pki/tls/private/server.example.com.key.pem
    ```

    If unauthorized users have access to the private key, connections to the MySQL server are no longer secure.

5.  Restore the SELinux context:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /etc/pki/tls/
    ```

#### [2.4.2. Configuring TLS encryption on a MySQL server](#configuring-tls-encryption-on-a-mysql-server) {#configuring-tls-encryption-on-a-mysql-server .title}

By default, MySQL uses unencrypted connections. For more secure connections, you can enable Transport Layer Security (TLS) support on the MySQL server and configure your clients to establish encrypted connections.

**Prerequisites**

-   You installed the MySQL server.

-   The `mysqld`{.literal} service is running.

-   The following files in Privacy Enhanced Mail (PEM) format exist on the server and are readable by the `mysql`{.literal} user:

    -   The private key of the server: `/etc/pki/tls/private/server.example.com.key.pem`{.literal}
    -   The server certificate: `/etc/pki/tls/certs/server.example.com.crt.pem`{.literal}
    -   The Certificate Authority (CA) certificate `/etc/pki/tls/certs/ca.crt.pem`{.literal}

-   The subject distinguished name (DN) or the subject alternative name (SAN) field in the server certificate matches the server's host name.

**Procedure**

1.  Create the `/etc/my.cnf.d/mysql-server-tls.cnf`{.literal} file:

    a.  Add the following content to configure the paths to the private key, server and CA certificate:

        ``` {.language-plaintext tabindex="-1"}
        [mysqld]
        ssl_key = /etc/pki/tls/private/server.example.com.key.pem
        ssl_cert = /etc/pki/tls/certs/server.example.com.crt.pem
        ssl_ca = /etc/pki/tls/certs/ca.crt.pem
        ```

    b.  If you have a Certificate Revocation List (CRL), configure the MySQL server to use it:

        ``` {.language-plaintext tabindex="-1"}
        ssl_crl = /etc/pki/tls/certs/example.crl.pem
        ```

    c.  Optional: Reject connection attempts without encryption. To enable this feature, append:

        ``` {.language-plaintext tabindex="-1"}
        require_secure_transport = on
        ```

    d.  Optional: Set the TLS versions the server should support. For example, to support only TLS 1.3, append:

        ``` {.language-plaintext tabindex="-1"}
        tls_version = TLSv1.3
        ```

        By default, the server supports TLS 1.2 and TLS 1.3.

2.  Restart the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart mysqld
    ```

**Verification**

To simplify troubleshooting, perform the following steps on the MySQL server before you configure the local client to use TLS encryption:

1.  Verify that MySQL now has TLS encryption enabled:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h <MySQL_server_hostname> -e "SHOW session status LIKE 'Ssl_cipher';"
    +---------------+------------------------+
    | Variable_name | Value                  |
    +---------------+------------------------+
    | Ssl_cipher    | TLS_AES_256_GCM_SHA384 |
    +---------------+------------------------+
    ```

2.  If you configured the MySQL server to only support specific TLS versions, display the `tls_version`{.literal} variable:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -e "SHOW GLOBAL VARIABLES LIKE 'tls_version';"
    +---------------+---------+
    | Variable_name | Value   |
    +---------------+---------+
    | tls_version   | TLSv1.3 |
    +---------------+---------+
    ```

3.  Verify that the server uses the correct CA certificate, server certificate, and private key files:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -e "SHOW GLOBAL VARIABLES WHERE Variable_name REGEXP '{caret}ssl_ca|{caret}ssl_cert|{caret}ssl_key';"
    +-----------------+-------------------------------------------------+
    | Variable_name   | Value                                           |
    +-----------------+-------------------------------------------------+
    | ssl_ca          | /etc/pki/tls/certs/ca.crt.pem                   |
    | ssl_capath      |                                                 |
    | ssl_cert        | /etc/pki/tls/certs/server.example.com.crt.pem   |
    | ssl_key         | /etc/pki/tls/private/server.example.com.key.pem |
    +-----------------+-------------------------------------------------+
    ```

**Additional resources**

-   [Placing the CA certificate, server certificate, and private key on the MySQL server](#placing-the-ca-certificate-server-certificate-and-private-key-on-the-mysql-server "2.4.1. Placing the CA certificate, server certificate, and private key on the MySQL server")

#### [2.4.3. Requiring TLS encrypted connections for specific user accounts on a MySQL server](#requiring-tls-encrypted-connections-for-specific-user-accounts-on-a-mysql-server) {#requiring-tls-encrypted-connections-for-specific-user-accounts-on-a-mysql-server .title}

You can configure specific MySQL user accounts to require TLS-encrypted connections to protect sensitive data transmission.

If you cannot configure on the server that a secure transport is required for all connections (`require_secure_transport = on`{.literal}), configure individual user accounts to require TLS encryption.

**Prerequisites**

-   The MySQL server has TLS support enabled.
-   The user you configure to require secure transport exists.
-   The CA certificate is stored on the client.

**Procedure**

1.  Connect as an administrative user to the MySQL server:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h server.example.com
    ```

    If your administrative user has no permissions to access the server remotely, perform the command on the MySQL server and connect to `localhost`{.literal}.

2.  Use the `REQUIRE SSL`{.literal} clause to enforce that a user must connect by using a TLS-encrypted connection:

    ``` {.language-plaintext tabindex="-1"}
    MySQL [(none)]> ALTER USER 'example'@'%' REQUIRE SSL;
    ```

**Verification**

1.  Connect to the server as the `example`{.literal} user by using TLS encryption:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u example -p -h server.example.com
    ...
    MySQL [(none)]>
    ```

    If the command does not return any error and you have access to the interactive MySQL console, the connection with TLS succeeds.

    By default, the client uses TLS encryption if the server provides it. You do not need to specify the `--ssl-ca=ca.crt.pem`{.literal} and `--ssl-mode=VERIFY_IDENTITY`{.literal} options. However, specifying these options improves security by verifying the server's identity.

2.  Attempt to connect as the `example`{.literal} user with TLS disabled:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u example -p -h server.example.com --ssl-mode=DISABLED
    ERROR 1045 (28000): Access denied for user 'example'@'server.example.com' (using password: YES)
    ```

    The server rejected the login attempt because this user requires TLS, but the `--ssl-mode=DISABLED`{.literal} option disables it.

### [2.5. Configuring the MySQL client to use TLS encryption by default](#configuring-the-mysql-client-to-use-tls-encryption-by-default) {#configuring-the-mysql-client-to-use-tls-encryption-by-default .title}

On RHEL, globally configure that the MySQL client uses TLS encryption and verifies that the Common Name (CN) in the server certificate matches the hostname the user connects to. This prevents man-in-the-middle attacks.

**Prerequisites**

-   The MySQL server has TLS support enabled.
-   The CA certificate is stored in the `/etc/pki/tls/certs/ca.crt.pem`{.literal} file on the client.

**Procedure**

-   Create the `/etc/my.cnf.d/mysql-client-tls.cnf`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [client]
    ssl-mode=VERIFY_IDENTITY
    ssl-ca=/etc/pki/tls/certs/ca.crt.pem
    ```

    These settings define that the MySQL client uses TLS encryption and that the client compares the hostname with the CN in the server certificate (`ssl-mode=VERIFY_IDENTITY`{.literal}). Additionally, the `ssl-ca`{.literal} setting specifies the path to the CA certificate.

**Verification**

-   Connect to the server using the hostname, and display the server status:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h server.example.com -e status
    ...
    SSL:        Cipher in use is TLS_AES_256_GCM_SHA384
    ```

    If the `SSL`{.literal} entry contains `Cipher in use is…​`{.literal}, the connection is encrypted.

    Note that the user you use in this command has permissions to authenticate remotely.

    If the hostname you connect to does not match the hostname in the TLS certificate of the server, the `ssl-mode=VERIFY_IDENTITY`{.literal} parameter causes the connection to fail. For example, if you connect to `localhost`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h localhost -e status
    ERROR 2026 (HY000): SSL connection error: error:0A000086:SSL routines::certificate verify failed
    ```

### [2.6. Backing up and restoring MySQL data with logical dumps](#backing-up-and-restoring-mysql-data-with-logical-dumps) {#backing-up-and-restoring-mysql-data-with-logical-dumps .title}

A logical backup of MySQL data consists of the SQL statements necessary to restore the data. The advantage of logical backup over physical backup is that the data can be restored on other hardware configurations and MySQL versions.

#### [2.6.1. Performing a logical backup by using mysqldump](#performing-a-logical-backup-by-using-mysqldump) {#performing-a-logical-backup-by-using-mysqldump .title}

The `mysqldump`{.literal} utility is a backup utility that can export one or more databases. The output of `mysqldump`{.literal} typically consists of SQL statements to re-create the server table structure, populate it with data, or both.

To perform the `mysqldump`{.literal} backup, you can use one of the following options:

-   Back up one or more selected databases
-   Back up all databases
-   Back up a subset of tables from one database

**Procedure**

-   To dump a single database, run:

    ``` {.language-plaintext tabindex="-1"}
    # mysqldump [options] --databases db_name > backup-file.sql
    ```

-   To dump multiple databases at once, run:

    ``` {.language-plaintext tabindex="-1"}
    # mysqldump [options] --databases db_name1 [db_name2 ...] > backup-file.sql
    ```

-   To dump all databases, run:

    ``` {.language-plaintext tabindex="-1"}
    # mysqldump [options] --all-databases > backup-file.sql
    ```

-   To load one or more dumped full databases back into a server, run:

    ``` {.language-plaintext tabindex="-1"}
    # mysql < backup-file.sql
    ```

-   To load a database to a remote MySQL server, run:

    ``` {.language-plaintext tabindex="-1"}
    # mysql --host=remote_host < backup-file.sql
    ```

-   To dump a subset of tables from one database, add a list of the chosen tables at the end of the `mysqldump`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # mysqldump [options] db_name [tbl_name ...​] > backup-file.sql
    ```

-   To load a subset of tables dumped from one database, run:

    ``` {.language-plaintext tabindex="-1"}
    # mysql db_name < backup-file.sql
    ```

    Note

    The *db_name* database must exist at this point.

-   To see a list of the options that `mysqldump`{.literal} supports, run:

    ``` {.language-plaintext tabindex="-1"}
    $ mysqldump --help
    ```

**Additional resources**

-   [Logical backup with mysqldump](https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html)

#### [2.6.2. Restoring MySQL data from a dump in SQL format](#restoring-mysql-data-from-a-dump-in-sql-format) {#restoring-mysql-data-from-a-dump-in-sql-format .title}

If you backed up one or multiple databases to an SQL file, you can use this file to re-create the database structure and its data.

**Prerequisites**

-   The `mysqld`{.literal} service is running.
-   You have credentials with permissions to restore data, for example, the `root`{.literal} account.

**Procedure**

1.  If the database you want to restore already exists and your SQL file does not contain `DROP TABLE IF EXISTS`{.literal} statements, manually remove the tables or the entire database:

    -   To remove a table, enter:

        ``` {.language-plaintext tabindex="-1"}
        # mysql -u root -p -e "DROP TABLE <database>.<table>;"
        ```

        Repeat this command for every table that the SQL file re-creates.

    -   To remove a database, enter:

        ``` {.language-plaintext tabindex="-1"}
        # mysql -u root -p -e "DROP DATABASE <database>;"
        ```

        Repeat this command for every database that the SQL file re-creates.

2.  Import the SQL file:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p < backup.sql"
    ```

**Verification**

-   Connect to a MySQL database and query data, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p <database> -e "*SELECT * FROM <table>;"
    ```

### [2.7. Backing up and restoring MySQL data with physical copies](#backing-up-and-restoring-mysql-data-with-physical-copies) {#backing-up-and-restoring-mysql-data-with-physical-copies .title}

A physical backup of MySQL data contains files and directories that store the content. This method is typically faster and smaller in size.

#### [2.7.1. Performing a file system backup on a MySQL server](#performing-a-file-system-backup-on-a-mysql-server) {#performing-a-file-system-backup-on-a-mysql-server .title}

A file system-level backup is a fast way to back up a complete MySQL instance. This method requires a shutdown of the `mysqld`{.literal} service for data consistency.

Important

A file system-level backup is specific to an architecture and MySQL version. You cannot restore data backed up by this method on a different architecture or MySQL version.

**Procedure**

1.  Stop the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop mysqld.service
    ```

2.  Create a backup directory, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /root/mysqld-backup/{data,config}/
    ```

3.  Back up the data directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /var/lib/mysql/ /root/mysqld-backup/data/
    ```

4.  Back up the configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /etc/my.cnf /etc/my.cnf.d/ /root/mysqld-backup/config/
    ```

5.  Start the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start mysqld.service
    ```

#### [2.7.2. Restoring a file system backup on a MySQL server](#restoring-a-file-system-backup-on-a-mysql-server) {#restoring-a-file-system-backup-on-a-mysql-server .title}

If corruption occurred in your MySQL instance, and you previously performed a file system backup that includes the data directory and the configuration files, restore the instance from this backup.

**Prerequisites**

-   [You performed a file system backup on a MySQL server](#performing-a-file-system-backup-on-a-mysql-server "2.7.1. Performing a file system backup on a MySQL server").

-   The target server must meet the following conditions of the backup source:

    -   The MySQL version must be identical or higher.
    -   The system architecture must be identical.

**Procedure**

1.  Stop the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop mysqld.service
    ```

2.  Remove the current `/var/lib/mysql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # rm -rf /var/lib/mysql/
    ```

3.  Restore the data directory from your backup:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /root/mysqld-backup/data/mysql/ /var/lib/
    ```

4.  Ensure the correct ownership of the `/var/lib/mysql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # chown -R mysql:mysql /var/lib/mysql/
    ```

5.  Restore the SELinux context of the `/var/lib/mysql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /var/lib/mysql/
    ```

6.  Remove the current configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # rm -rf /etc/my.cnf /etc/my.cnf.d/
    ```

7.  Restore the configuration files from your backup:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /root/mysqld-backup/config/my.cnf /root/mysqld-backup/config/my.cnf.d/ /etc/
    ```

8.  Ensure the correct ownership of the configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # chown -R root:root /etc/my.cnf /etc/my.cnf.d/
    ```

9.  Restore the SELinux context of the configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /etc/my.cnf /etc/my.cnf.d/
    ```

10. Start the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start mysqld.service
    ```

**Verification**

-   Connect to a MySQL database and query data, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p <database> -e "*SELECT * FROM <table>;"
    ```

### [2.8. Replicating MySQL with TLS encryption](#replicating-mysql-with-tls-encryption) {#replicating-mysql-with-tls-encryption .title}

You can configure MySQL replication with TLS encryption to create secure data replication between source and replica servers.

Warning

Replication itself is not a sufficient backup solution. Replication protects source servers against hardware failures, but it does not ensure protection against data loss.

#### [2.8.1. Configuring a MySQL source server](#configuring-a-mysql-source-server) {#configuring-a-mysql-source-server .title}

You can set configuration options required for a MySQL source server to properly run and replicate all changes made on the database server through the TLS protocol.

**Prerequisites**

-   The source server is installed.

-   The source server has [TLS configured](#setting-up-tls-encryption-on-a-mysql-server "2.4. Setting up TLS encryption on a MySQL server").

    Important

    The source and replica certificates must be signed by the same certificate authority.

**Procedure**

1.  Include the following options in the `/etc/my.cnf.d/mysql-server.cnf`{.literal} file under the `[mysqld]`{.literal} section:

    -   `bind-address=`{.literal}*`source_ip_adress`{.literal}*

        Replicas require this option to connect to the source.

    -   `server-id=`{.literal}*`id`{.literal}*

        The *id* must be unique.

    -   `log_bin=`{.literal}*`path_to_source_server_log`{.literal}*

        This option defines a path to the binary log file of the MySQL source server. For example: `log_bin=/var/log/mysql/mysql-bin.log`{.literal}.

    -   `gtid_mode=ON`{.literal}

        This option enables global transaction identifiers (GTIDs) on the server.

    -   `enforce-gtid-consistency=ON`{.literal}

        The server enforces GTID consistency by allowing execution of only statements that the server can safely log by using a GTID.

    -   *Optional:* `binlog_do_db=`{.literal}*`db_name`{.literal}*

        Use this option if you want to replicate only selected databases. To replicate more than one selected database, specify each of the databases separately:

        ``` {.language-plaintext tabindex="-1"}
        binlog_do_db=db_name1
        binlog_do_db=db_name2
        binlog_do_db=db_name3
        ```

    -   *Optional:* `binlog_ignore_db=`{.literal}*`db_name`{.literal}*

        Use this option to exclude a specific database from replication.

2.  Restart the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart mysqld.service
    ```

#### [2.8.2. Configuring a MySQL replica server](#configuring-a-mysql-replica-server) {#configuring-a-mysql-replica-server .title}

You can set configuration options required for a MySQL replica server to ensure a successful replication.

**Prerequisites**

-   The replica server is installed.

-   The replica server has [TLS configured](#setting-up-tls-encryption-on-a-mysql-server "2.4. Setting up TLS encryption on a MySQL server").

    Important

    The source and replica certificates must be signed by the same certificate authority.

**Procedure**

1.  Include the following options in the `/etc/my.cnf.d/mysql-server.cnf`{.literal} file under the `[mysqld]`{.literal} section:

    -   `server-id=`{.literal}*`id`{.literal}*

        The *id* must be unique.

    -   `relay-log=`{.literal}*`path_to_replica_server_log`{.literal}*

        The relay log is a set of log files created by the MySQL replica server during replication.

    -   `log_bin=`{.literal}*`path_to_replica_sever_log`{.literal}*

        This option defines a path to the binary log file of the MySQL replica server. For example: `log_bin=/var/log/mysql/mysql-bin.log`{.literal}.

    -   `gtid_mode=ON`{.literal}

        This option enables global transaction identifiers (GTIDs) on the server.

    -   `enforce-gtid-consistency=ON`{.literal}

        The server enforces GTID consistency by allowing execution of only statements that the server can safely log by using a GTID.

    -   `log-replica-updates=ON`{.literal}

        This option ensures that the replica binary log records updates received from the source server.

    -   `skip-replica-start=ON`{.literal}

        This option ensures that the replica server does not start the replication threads when the replica server starts.

    -   *Optional:* `binlog_do_db=`{.literal}*`db_name`{.literal}*

        Use this option if you want to replicate only certain databases. To replicate more than one database, specify each of the databases separately:

        ``` {.language-plaintext tabindex="-1"}
        binlog_do_db=db_name1
        binlog_do_db=db_name2
        binlog_do_db=db_name3
        ```

    -   *Optional:* `binlog_ignore_db=`{.literal}*`db_name`{.literal}*

        Use this option to exclude a specific database from replication.

2.  Restart the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart mysqld.service
    ```

#### [2.8.3. Creating a replication user on the MySQL source server](#creating-a-replication-user-on-the-mysql-source-server) {#creating-a-replication-user-on-the-mysql-source-server .title}

You must create a replication user with appropriate permissions on the MySQL source server to enable replica servers to connect and receive data changes.

**Prerequisites**

-   The source server is installed and configured as described in [Configuring a MySQL source server](#configuring-a-mysql-source-server "2.8.1. Configuring a MySQL source server").

**Procedure**

1.  Create a replication user:

    ``` {.language-plaintext tabindex="-1"}
    mysql> CREATE USER 'replication_user'@'replica_server_hostname' IDENTIFIED WITH mysql_native_password BY 'password';
    ```

2.  Grant the user replication permissions:

    ``` {.language-plaintext tabindex="-1"}
    mysql> GRANT REPLICATION SLAVE ON *.* TO 'replication_user'@'replica_server_hostname';*
    ```

3.  Reload the grant tables in the MySQL database:

    ``` {.language-plaintext tabindex="-1"}
    mysql> FLUSH PRIVILEGES;
    ```

4.  Set the source server to read-only state:

    ``` {.language-plaintext tabindex="-1"}
    mysql> SET @@GLOBAL.read_only = ON;
    ```

#### [2.8.4. Connecting the MySQL replica server to the source server](#connecting-the-mysql-replica-server-to-the-source-server) {#connecting-the-mysql-replica-server-to-the-source-server .title}

You must configure the replica server with source server credentials and start replication to establish a connection between the MySQL replica and source servers.

**Prerequisites**

-   The source server is installed and configured as described in [Configuring a MySQL source server](#configuring-a-mysql-source-server "2.8.1. Configuring a MySQL source server").
-   The replica server is installed and configured as described in [Configuring a MySQL replica server](#configuring-a-mysql-replica-server "2.8.2. Configuring a MySQL replica server").
-   You have created a replication user. See [Creating a replication user on the MySQL source server](#creating-a-replication-user-on-the-mysql-source-server "2.8.3. Creating a replication user on the MySQL source server").

**Procedure**

1.  Set the replica server to read-only state:

    ``` {.language-plaintext tabindex="-1"}
    mysql> SET @@GLOBAL.read_only = ON;
    ```

2.  Configure the replication source:

    ``` {.language-plaintext tabindex="-1"}
    mysql> CHANGE REPLICATION SOURCE TO
           SOURCE_HOST='source_hostname',
           SOURCE_USER='replication_user',
           SOURCE_PASSWORD='password',
           SOURCE_AUTO_POSITION=1,
           SOURCE_SSL=1,
           SOURCE_SSL_CA='path_to_ca_on_source',
           SOURCE_SSL_CAPATH='path_to_directory_with_certificates',
           SOURCE_SSL_CERT='path_to_source_certificate',
           SOURCE_SSL_KEY='path_to_source_key';
    ```

3.  Start the replica thread in the MySQL replica server:

    ``` {.language-plaintext tabindex="-1"}
    mysql> START REPLICA;
    ```

4.  Unset the read-only state on both the source and replica servers:

    ``` {.language-plaintext tabindex="-1"}
    mysql> SET @@GLOBAL.read_only = OFF;
    ```

5.  Optional: Inspect the status of the replica server for debugging purposes:

    ``` {.language-plaintext tabindex="-1"}
    mysql> SHOW REPLICA STATUS\G;
    ```

    Note

    If the replica server fails to start or connect, skip events after the binary log position shown by the `SHOW MASTER STATUS`{.literal} command. For example, skip the first event from the defined position:

    ``` {.language-plaintext tabindex="-1"}
    mysql> SET GLOBAL SQL_SLAVE_SKIP_COUNTER=1;
    ```

    Afterwards, try to start the replica server again.

6.  Optional: Stop the replica thread in the replica server:

    ``` {.language-plaintext tabindex="-1"}
    mysql> STOP REPLICA;
    ```

#### [2.8.5. Verifying replication on a MySQL server](#verifying-replication-on-a-mysql-server) {#verifying-replication-on-a-mysql-server .title}

You can verify that MySQL replication works correctly by creating test databases and checking replication status on source and replica servers.

**Procedure**

1.  Create an example database on the source server:

    ``` {.language-plaintext tabindex="-1"}
    mysql> CREATE DATABASE test_db_name;
    ```

2.  Verify that the *`test_db_name`{.literal}* database replicates on the replica server.

3.  Display status information about the binary log files of the MySQL server by executing the following command on either of the source or replica servers:

    ``` {.language-plaintext tabindex="-1"}
    mysql> SHOW MASTER STATUS;
    ```

    The `Executed_Gtid_Set`{.literal} column, which shows a set of GTIDs for transactions executed on the source, must not be empty.

    Note

    The `Executed_Gtid_Set`{.literal} row shows the same set of GTIDs when you use `SHOW REPLICA STATUS`{.literal} on the replica server.

**Additional resources**

-   [MySQL Replication documentation](https://dev.mysql.com/doc/refman/8.4/en/replication.html)
-   [Replication with Global Transaction Identifiers](https://dev.mysql.com/doc/refman/8.4/en/replication-gtids.html)

### [2.9. Migrating a MySQL instance from a previous RHEL version to MySQL 8.4 on RHEL 10](#migrating-a-mysql-instance-from-a-previous-rhel-version-to-mysql-8-4-on-rhel-10) {#migrating-a-mysql-instance-from-a-previous-rhel-version-to-mysql-8.4-on-rhel-10 .title}

RHEL 10 provides MySQL 8.4. If you run a MySQL instance on a previous RHEL version, you can configure RHEL 10 on a new host and migrate the instance to it.

**Prerequisites**

-   You configure RHEL 10 on a new host.
-   You performed a file system backup of the MySQL instance on the RHEL 8 or RHEL 9 host.

**Procedure**

1.  Install the `mysql8.4-server`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install mysql8.4-server
    ```

2.  Stop the service if it is already running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop mysqld.service
    ```

3.  Copy the content of the `/var/lib/mysql/`{.literal} directory from the previous host to the same location on the RHEL 10 host.

4.  Copy the configuration files from the previous host to the `/etc/my.cnf.d/`{.literal} directory.

5.  Ensure that the files include only options valid for MySQL 8.4. For details, see the [upstream documentation](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html).

6.  Restore the SELinux context:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -rv /var/lib/mysql/
    # restorecon -rv /etc/my.cnf.d/
    ```

7.  Ensure the correct ownership of `/var/lib/mysql/`{.literal} and its subdirectories:

    ``` {.language-plaintext tabindex="-1"}
    # chown -R mysql:mysql /var/lib/mysql/
    ```

8.  Enable and start the `mysqld`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now mysqld.service
    ```

    When the service starts, MySQL automatically checks, repairs, and updates internal tables.

**Verification**

-   Establish a connection to the MySQL server:

    ``` {.language-plaintext tabindex="-1"}
    # mysql -u root -p -h <hostname>
    ```

## [Chapter 3. Using PostgreSQL](#using-postgresql) {#chapter-3.-using-postgresql .title}

The PostgreSQL server is an open source robust and highly-extensible database server based on the SQL language. The PostgreSQL server provides an object-relational database system that can manage extensive datasets and a high number of concurrent users.

The PostgreSQL server includes features for ensuring data integrity, building fault-tolerant environments and applications. With the PostgreSQL server, you can extend a database with your own data types, custom functions, or code from different programming languages without the need to recompile the database.

Learn how to install and configure PostgreSQL on a RHEL system, how to back up PostgreSQL data, and how to migrate from an earlier PostgreSQL version.

### [3.1. Installing PostgreSQL](#installing-postgresql) {#installing-postgresql .title}

RHEL 10 provides PostgreSQL 16 as the initial version of the Application Stream, which you can install as an RPM package. In minor releases, RHEL 10 provides additional PostgreSQL versions as alternative versions with a shorter life cycle.

In RHEL 10, the PostgreSQL server is available in the following versions:

-   PostgreSQL 16
-   PostgreSQL 18 available since RHEL 10.2

Important

By design, you can install only one version (stream) of the same application stream and, because of conflicting RPM packages, you cannot install multiple PostgreSQL instances on the same host. As an alternative, you can run the database server services in a container. See [Using containers to run multiple PostgreSQL instances on a single host](#using-containers-to-run-multiple-postgresql-instances-on-a-single-host "3.2. Using containers to run multiple PostgreSQL instances on a single host").

**Procedure**

1.  Install the PostgreSQL server packages:

    -   For PostgreSQL 16, enter:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install postgresql-server
        ```

    -   For PostgreSQL 18, enter:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install postgresql18-server
        ```

    The `postgres`{.literal} superuser is created automatically.

2.  Initialize the database cluster:

    ``` {.language-plaintext tabindex="-1"}
    # postgresql-setup --initdb
    ```

    Store the data in the default `/var/lib/pgsql/data`{.literal} directory.

3.  Enable and start the `postgresql`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now postgresql.service
    ```

### [3.2. Using containers to run multiple PostgreSQL instances on a single host](#using-containers-to-run-multiple-postgresql-instances-on-a-single-host) {#using-containers-to-run-multiple-postgresql-instances-on-a-single-host .title}

If you install PostgreSQL from packages, you can run only a single version of it on the same host. To run multiple instances or different versions of PostgreSQL, you can run the service in a container.

**Prerequisites**

-   The `podman`{.literal} package is installed.

**Procedure**

1.  Authenticate to the `registry.redhat.io`{.literal} registry by using your Red Hat Customer Portal account:

    ``` {.language-plaintext tabindex="-1"}
    # podman login registry.redhat.io
    ```

    Skip this step if you are already logged in to the container registry.

2.  Start the containers you want to use.

    -   For PostgreSQL 16, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run -d --name <container_name> -e POSTGRESQL_USER=<user_name> -e POSTGRESQL_PASSWORD=<password> -p <host_port_1>:5432 rhel10/postgresql-16
        ```

        For more information about the usage of this container image, see the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/rhel10/postgresql-16/677d13af607921b4d74fca88).

    -   For PostgreSQL 18, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run -d --name <container_name> -e POSTGRESQL_USER=<user_name> -e POSTGRESQL_PASSWORD=<password> -p <host_port_2>:5432 rhel10/postgresql-18
        ```

        For more information about the usage of this container image, see the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/en/software/containers/rhel10/postgresql-18/6942a60aab9edd836017e3d0).

    Important

    The container names and host ports of the two database servers must differ.

3.  To ensure that clients can access the database server on the network, open the host ports in the firewall:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port={<host_port_1>/tcp,<host_port_2>/tcp,...}
    # firewall-cmd --reload
    ```

**Verification**

1.  Connect to the database server and log in as root:

    ``` {.language-plaintext tabindex="-1"}
    # psql -u postgres -p -h localhost -P <host_port> --protocol tcp
    ```

2.  Display information about running containers:

    ``` {.language-plaintext tabindex="-1"}
    $ podman ps
    ```

**Additional resources**

-   [Building, running, and managing containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/index)
-   [Browse containers in the Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/search)

### [3.3. Creating PostgreSQL users](#creating-postgresql-users) {#creating-postgresql-users .title}

You can create PostgreSQL users with specific permissions to manage database access and control user privileges for secure database administration.

PostgreSQL users are of the following types:

-   The `postgres`{.literal} Linux system user: Use it only to run the PostgreSQL server and client applications, such as `pg_dump`{.literal}. Do not use the `postgres`{.literal} system user for any interactive work on PostgreSQL administration, such as database creation and user management.

-   A database superuser: The default `postgres`{.literal} PostgreSQL superuser is not related to the `postgres`{.literal} system user. You can limit access of the `postgres`{.literal} superuser in the `/var/lib/pgsql/data/pg_hba.conf`{.literal} file, otherwise no other permission limitations exist. You can also create other database superusers.

-   A role with specific database access permissions:

    -   A database user: Has a permission to log in by default.
    -   A group of users: Enables managing permissions for the group as a whole.

Roles can own database objects (for example, tables and functions) and can assign object privileges to other roles by using SQL commands.

Standard database management privileges include `SELECT`{.literal}, `INSERT`{.literal}, `UPDATE`{.literal}, `DELETE`{.literal}, `TRUNCATE`{.literal}, `REFERENCES`{.literal}, `TRIGGER`{.literal}, `CREATE`{.literal}, `CONNECT`{.literal}, `TEMPORARY`{.literal}, `EXECUTE`{.literal}, and `USAGE`{.literal}.

Role attributes are special privileges, such as `LOGIN`{.literal}, `SUPERUSER`{.literal}, `CREATEDB`{.literal}, and `CREATEROLE`{.literal}.

Important

Perform most tasks as a role that is not a superuser. A common practice is to create a role that has the `CREATEDB`{.literal} and `CREATEROLE`{.literal} privileges and use this role for all routine management of databases and roles.

**Prerequisites**

-   The PostgreSQL server is installed.
-   The database cluster is initialized.
-   The `password_encryption`{.literal} parameter in the `/var/lib/pgsql/data/postgresql.conf`{.literal} file is set to `scram-sha-256`{.literal}.
-   Entries in the `/var/lib/pgsql/data/pg_hba.conf`{.literal} file use the `scram-sha-256`{.literal} hashing algorithm as authentication method.

**Procedure**

1.  Log in as the `postgres`{.literal} system user, or switch to this user:

    ``` {.language-plaintext tabindex="-1"}
    # su - postgres
    ```

2.  Start the PostgreSQL interactive shell prompt:

    ``` {.language-plaintext tabindex="-1"}
    $ psql
    psql (16.4)
    Type "help" for help.

    postgres=#
    ```

3.  Optional: Obtain information about the current database connection:

    ``` {.language-plaintext tabindex="-1"}
    postgres=# \conninfo
    You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
    ```

4.  Create a user named `mydbuser`{.literal}, set a password for it, and assign the `CREATEROLE`{.literal} and `CREATEDB`{.literal} permissions to the user:

    ``` {.language-plaintext tabindex="-1"}
    postgres=# CREATE USER mydbuser WITH PASSWORD '<password>' CREATEROLE CREATEDB;
    CREATE ROLE
    ```

    The `mydbuser`{.literal} user now can perform routine database management operations: create databases and manage user indexes.

5.  Log out of the interactive shell prompt by using the `\q`{.literal} meta command:

    ``` {.language-plaintext tabindex="-1"}
    postgres=# \q
    ```

**Verification**

1.  Log in to PostgreSQL as `mydbuser`{.literal}, specify the hostname, and connect to the default `postgres`{.literal} database, which was created during initialization:

    ``` {.language-plaintext tabindex="-1"}
    # psql -U mydbuser -h 127.0.0.1 -d postgres
    Password for user mydbuser:
    Type the password.
    psql (16.4)
    Type "help" for help.

    postgres=>
    ```

2.  Create a database:

    ``` {.language-plaintext tabindex="-1"}
    postgres=> CREATE DATABASE <db_name>;
    ```

3.  Log out of the session:

    ``` {.language-plaintext tabindex="-1"}
    postgres=# \q
    ```

4.  Connect to new database as `mydbuser`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # psql -U mydbuser -h 127.0.0.1 -d <db_name>
    Password for user mydbuser:
    psql (16.4)
    Type "help" for help.
    mydatabase=>
    ```

**Additional resources**

-   [PostgreSQL database roles](https://www.postgresql.org/docs/16/user-manag.html)
-   [PostgreSQL privileges](https://www.postgresql.org/docs/16/ddl-priv.html)

### [3.4. Configuring PostgreSQL](#configuring-postgresql) {#configuring-postgresql .title}

You can configure PostgreSQL by editing the configuration files in the database cluster directory to set database parameters, authentication, and client access. By default, PostgreSQL uses the `/var/lib/pgsql/data/`{.literal} directory.

The PostgreSQL configuration files include:

-   `/var/lib/pgsql/data/postgresql.conf`{.literal} - sets the database cluster parameters.
-   `/var/lib/pgsql/data/postgresql.auto.conf`{.literal} - holds basic PostgreSQL settings similarly to `postgresql.conf`{.literal}. However, this file is under the server's control. The `ALTER SYSTEM`{.literal} queries edit this file. You cannot edit it manually.
-   `/var/lib/pgsql/data/pg_ident.conf`{.literal} - maps user identities from external authentication mechanisms into the PostgreSQL user identities.
-   `/var/lib/pgsql/data/pg_hba.conf`{.literal} - configures client authentication for PostgreSQL databases.

**Procedure**

1.  Edit the `/var/lib/pgsql/data/postgresql.conf`{.literal} file and configure basic settings of the database cluster parameters, for example:

    ``` {.language-plaintext tabindex="-1"}
    log_connections = yes
    log_destination = 'syslog'
    search_path = '"$user", public'
    shared_buffers = 128MB
    password_encryption = scram-sha-256
    ```

2.  Edit the `/var/lib/pgsql/data/pg_hba.conf`{.literal} file and configure client authentication, for example:

    ``` {.language-plaintext tabindex="-1"}
    # TYPE    DATABASE       USER        ADDRESS              METHOD
    local     all            all                              trust
    host      postgres       all         192.168.93.0/24      ident
    host      all            all         .example.com         scram-sha-256
    ```

3.  Restart the `postgresql`{.literal} service so that the changes become effective:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart postgresql.service
    ```

### [3.5. Configuring TLS encryption on a PostgreSQL server](#configuring-tls-encryption-on-a-postgresql-server) {#configuring-tls-encryption-on-a-postgresql-server .title}

By default, PostgreSQL uses unencrypted connections. For more secure connections, you can enable Transport Layer Security (TLS) support on the PostgreSQL server and configure your clients to establish encrypted connections.

**Prerequisites**

-   You created a TLS private key and a certificate authority (CA) issued a server certificate for your PostgreSQL server.
-   The PostgreSQL server is installed.
-   The database cluster is initialized.
-   If FIPS mode is enabled, clients must either support the Extended Master Secret (EMS) extension or use TLS 1.3. TLS 1.2 connections without EMS fail. For more information, see the Red Hat Knowledgebase solution [TLS extension \"Extended Master Secret\" enforced on RHEL 9.2 and later](https://access.redhat.com/solutions/7018256).
-   You have root privileges, or you can temporarily obtain root privileges by using the `sudo`{.literal} command.

**Procedure**

1.  Store the private key and the server certificate in the `/var/lib/pgsql/data/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp server.{key,crt} /var/lib/pgsql/data/
    ```

2.  Set the ownership of the private key and certificate:

    ``` {.language-plaintext tabindex="-1"}
    # chown postgres:postgres /var/lib/pgsql/data/server.{key,crt}
    ```

3.  Set permissions on the server certificate that enable only the PostgreSQL server to read the file:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 0400 /var/lib/pgsql/data/server.key
    ```

    Because certificates are part of the communication before the server establishes a secure connection, any client can retrieve them without authentication. Therefore, you do not need to set strict permissions on the server certificate file.

4.  Edit the `/var/lib/pgsql/data/postgresql.conf`{.literal} file and make the following changes:

    a.  Set the password hashing algorithm to SCRAM-SHA-256:

        ``` {.language-plaintext tabindex="-1"}
        password_encryption = scram-sha-256
        ```

    b.  Enable TLS encryption:

        ``` {.language-plaintext tabindex="-1"}
        ssl = on
        ```

    c.  Configure TLS ciphers to follow the system-wide cryptographic profile:

        ``` {.language-plaintext tabindex="-1"}
        ssl_ciphers = 'PROFILE=SYSTEM'
        ```

5.  Edit the `/var/lib/pgsql/data/pg_hba.conf`{.literal} file and update the authentication entries to use TLS encryption and the `scram-sha-256`{.literal} hashing algorithm. For example, change `host`{.literal} entries to `hostssl`{.literal} to enable TLS encryption, and set the `scram-sha-256`{.literal} hashing algorithm in the last column:

    ``` {.language-plaintext tabindex="-1"}
    hostssl    all    all    192.0.2.0/24    scram-sha-256
    ```

6.  Restart the `postgresql`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart postgresql.service
    ```

**Verification**

-   Use the `postgres`{.literal} super user to connect to a PostgreSQL server and run the `\conninfo`{.literal} meta command:

    ``` {.language-plaintext tabindex="-1"}
    # psql "postgresql://postgres@localhost:5432" -c '\conninfo'
    Password for user postgres:
    You are connected to database "postgres" as user "postgres" on host "192.0.2.1" at port "5432".
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
    ```

### [3.6. Backing up and restoring PostgreSQL data with logical dumps](#backing-up-and-restoring-postgresql-data-with-logical-dumps) {#backing-up-and-restoring-postgresql-data-with-logical-dumps .title}

A logical backup of PostgreSQL data consists of the SQL statements necessary to restore the data. The advantage of logical backup over physical backup is that you can restore data from logical backup on other hardware configurations and PostgreSQL versions.

The SQL dump method generates a dump file containing SQL commands. Uploading the file to the database server recreates the database in its state at the time of the dump.

The following PostgreSQL client applications ensure SQL dumps:

-   `pg_dump`{.literal} dumps a single database without cluster-wide information about roles or tablespaces
-   `pg_dumpall`{.literal} dumps each database in a given cluster and preserves cluster-wide data, such as role and tablespace definitions.

By default, the `pg_dump`{.literal} and `pg_dumpall`{.literal} commands write their results into the standard output. To store the dump in a file, redirect the output to an SQL file. The resulting SQL file can be either in a text format or in other formats that allow for parallelism and for more detailed control of object restoration.

You can perform the SQL dump from any remote host that has access to the database.

#### [3.6.1. Advantages and disadvantages of an SQL dump](#advantages-and-disadvantages-of-an-sql-dump) {#advantages-and-disadvantages-of-an-sql-dump .title}

SQL dumps are text files containing a database's structure and data in the form of SQL statements.

Advantages:

-   An SQL dump is the only PostgreSQL backup method that is not server version-specific. You can reload the output of the `pg_dump`{.literal} utility into later versions of PostgreSQL, which is not possible for file system level backups or continuous archiving.
-   An SQL dump is the only method that works when transferring a database to a different machine architecture, such as going from a 32-bit to a 64-bit server.
-   An SQL dump provides internally consistent dumps. A dump represents a snapshot of the database at the time `pg_dump`{.literal} began running.
-   The `pg_dump`{.literal} utility does not block other operations on the database when it is running.

Disadvantage:

-   An SQL dump takes more time compared to a file system level backup.

#### [3.6.2. Backing up a single PostgreSQL database by using pg_dump](#backing-up-a-single-postgresql-database-by-using-pgdump) {#backing-up-a-single-postgresql-database-by-using-pg_dump .title}

You can create a backup of a single PostgreSQL database by using the `pg_dump`{.literal} utility to export the database structure and data to a file.

**Prerequisites**

-   You are logged in as the `postgres`{.literal} superuser or a user with database administrator privileges.

**Procedure**

-   Dump a database without cluster-wide information:

    ``` {.language-plaintext tabindex="-1"}
    $ pg_dump <db_name> > <dump_file>
    ```

    To specify which database server `pg_dump`{.literal} contacts, use the following command-line options:

    -   The `-h`{.literal} option to define the host.

        The default host is either the local host or what the `PGHOST`{.literal} environment variable specifies.

    -   The `-p`{.literal} option to define the port.

        The `PGPORT`{.literal} environment variable indicates the default port or the compiled-in default.

#### [3.6.3. Restoring a single PostgreSQL database by using pg_dump](#restoring-a-single-postgresql-database-by-using-pgdump) {#restoring-a-single-postgresql-database-by-using-pg_dump .title}

You can restore a PostgreSQL database from an SQL dump file by using the `pg_restore`{.literal} utility to re-create the database structure and data.

**Prerequisites**

-   You are logged in as the `postgres`{.literal} superuser or a user with database administrator privileges.

**Procedure**

1.  Create a new database:

    ``` {.language-plaintext tabindex="-1"}
    $ createdb <db_name>
    ```

2.  Verify that all users who own objects or have permissions on objects in the dumped database already exist. If such users do not exist, the restore fails to re-create the objects with the original ownership and permissions.

3.  Run the `psql`{.literal} utility to restore a text file dump created by the `pg_dump`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ psql <db_name> < <dump_file>
    ```

    where `<dump_file>`{.literal} is the output of the `pg_dump`{.literal} command. To restore a non-text file dump, use the `pg_restore`{.literal} utility instead:

    ``` {.language-plaintext tabindex="-1"}
    $ pg_restore <non-plain_text_file>
    ```

#### [3.6.4. Backing up all databases on a PostgreSQL server by using pg_dumpall](#backing-up-all-databases-on-a-postgresq-server-by-using-pgdumpall) {#backing-up-all-databases-on-a-postgresql-server-by-using-pg_dumpall .title}

You can create a backup of all databases on a PostgreSQL server by using the `pg_dumpall`{.literal} utility to export all databases and cluster-wide data to a single file.

**Prerequisites**

-   You are logged in as the `postgres`{.literal} superuser or a user with database administrator privileges.

**Procedure**

-   Dump all databases in the database cluster and preserve cluster-wide data:

    ``` {.language-plaintext tabindex="-1"}
    $ pg_dumpall > <dump_file>
    ```

    To specify which database server `pg_dumpall`{.literal} contacts, use the following command-line options:

    -   The `-h`{.literal} option to define the host.

        The default host is either the local host or what the `PGHOST`{.literal} environment variable specifies.

    -   The `-p`{.literal} option to define the port.

        The `PGPORT`{.literal} environment variable indicates the default port or the compiled-in default.

    -   The `-l`{.literal} option to define the default database.

        This option enables you to choose a default database different from the `postgres`{.literal} database created automatically during initialization.

#### [3.6.5. Restoring all databases on a PostgreSQL server by using pg_dumpall](#restoring-all-databases-on-a-postgresql-server-by-using-pgdumpall) {#restoring-all-databases-on-a-postgresql-server-by-using-pg_dumpall .title}

You can restore all databases on a PostgreSQL server from a `pg_dumpall`{.literal} file by using the `psql`{.literal} utility to re-create the entire database cluster.

**Prerequisites**

-   You are logged in as the `postgres`{.literal} superuser or a user with database administrator privileges.

**Procedure**

1.  Ensure that all users who own objects or were granted permissions on objects in the dumped databases already exist. If such users do not exist, the restore fails to re-create the objects with the original ownership and permissions.

2.  Run the `psql`{.literal} utility to restore a text file dump created by the `pg_dumpall`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ psql < <dump_file>
    ```

    where `<dump_file>`{.literal} is the output of the `pg_dumpall`{.literal} command.

#### [3.6.6. Handling SQL errors during restore](#handling-sql-errors-during-restore) {#handling-sql-errors-during-restore .title}

By default, the `psql`{.literal} utility continues to run if an SQL error occurs, causing the database to restore only partially. Alternatively, you can configure `psql`{.literal} to stop on errors to ensure data integrity.

**Prerequisites**

-   You are logged in as the `postgres`{.literal} superuser or a user with database administrator privileges.

**Procedure**

-   Make `psql`{.literal} exit with an exit status of 3 if an SQL error occurs by setting the `ON_ERROR_STOP`{.literal} variable:

    ``` {.language-plaintext tabindex="-1"}
    $ psql --set ON_ERROR_STOP=on <db_name> < <dump_file>
    ```

-   Specify that the whole dump is restored as a single transaction so that the restore is either fully completed or canceled.

    -   When restoring a text file dump by using the `psql`{.literal} utility:

        ``` {.language-plaintext tabindex="-1"}
        $ psql -1
        ```

    -   When restoring a non-text file dump by using the `pg_restore`{.literal} utility:

        ``` {.language-plaintext tabindex="-1"}
        $ pg_restore -e
        ```

    Note that when you use this approach, even a minor error can cancel a restore operation that has already run for many hours.

**Additional resources**

-   [PostgreSQL Documentation - SQL dump](https://www.postgresql.org/docs/16/backup-dump.html)

### [3.7. Backing up and restoring PostgreSQL data with physical copies](#backing-up-and-restoring-postgresql-data-with-physical-copies) {#backing-up-and-restoring-postgresql-data-with-physical-copies .title}

A physical backup of PostgreSQL data contains files and directories that store the content. This method is typically faster and smaller in size.

#### [3.7.1. Performing a file system backup on a PostgreSQL server](#performing-a-file-system-backup-on-a-postgresql-server) {#performing-a-file-system-backup-on-a-postgresql-server .title}

A file system-level backup is a fast way to back up a complete PostgreSQL instance. This method requires a shutdown of the `postgresql`{.literal} service for data consistency.

Important

A PostgreSQL file system-level backup is specific to an architecture and RHEL major version. You cannot restore data that you backed up by this method on a different architecture or RHEL major version.

**Procedure**

1.  Stop the `postgresql`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop postgresql.service
    ```

2.  Create a backup directory, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /root/postgresql-backup/
    ```

3.  Back up the `/var/lib/pgsql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /var/lib/pgsql/ /root/postgresql-backup/
    ```

    The `/var/lib/pgsql/`{.literal} contains all essential files of the PostgreSQL database server, including configuration files, data files, and logs.

4.  Start the `postgresql`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start postgresql.service
    ```

#### [3.7.2. Restoring a file system backup on a PostgreSQL server](#restoring-a-file-system-backup-on-a-postgresql-server) {#restoring-a-file-system-backup-on-a-postgresql-server .title}

If your PostgreSQL instance is corrupt and you previously performed a file system backup that includes the data directory, you can restore the instance from this backup.

**Prerequisites**

-   [You performed a file system backup on a PostgreSQL server](#performing-a-file-system-backup-on-a-postgresql-server "3.7.1. Performing a file system backup on a PostgreSQL server").

-   The target server must meet the following conditions of the backup source:

    -   The PostgreSQL version must be identical.
    -   The system architecture must be identical.

**Procedure**

1.  Stop the `postgresql`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop postgresql.service
    ```

2.  Remove the current `/var/lib/pgsql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # rm -rf /var/lib/pgsql/
    ```

3.  Restore the data directory from your backup:

    ``` {.language-plaintext tabindex="-1"}
    # cp -rp /root/postgresql-backup/pgsql/ /var/lib/
    ```

4.  Ensure the correct ownership of the `/var/lib/pgsql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # chown -R postgres:postgres /var/lib/pgsql/
    ```

5.  Restore the SELinux context of the `/var/lib/pgsql/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /var/lib/pgsql/
    ```

6.  Start the `postgresql`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start postgresql.service
    ```

**Verification**

1.  Log in as the `postgres`{.literal} user.

2.  Connect to a database:

    ``` {.language-plaintext tabindex="-1"}
    $ psql <database>
    ```

3.  Access data in the database:

    ``` {.language-plaintext tabindex="-1"}
    <database>=# SELECT * FROM <table>;
    ```

4.  Disconnect from the PostgreSQL service:

    ``` {.language-plaintext tabindex="-1"}
    <database>=# \q
    ```

### [3.8. Backing up and restoring PostgreSQL data with continuous archiving](#backing-up-and-restoring-postgresql-data-with-continuous-archiving) {#backing-up-and-restoring-postgresql-data-with-continuous-archiving .title}

You can use continuous archiving to create robust PostgreSQL backups by combining WAL files with base backups for point-in-time recovery and high availability.

PostgreSQL records every change to the database's data files to a write-ahead log (WAL) file that is available in the `pg_wal/`{.literal} subdirectory of the cluster's data directory. This log primarily serves crash recovery. After a crash, you can use log entries made since the last checkpoint to restore the database to a consistent state.

The continuous archiving method, or online backup, combines WAL files with a database cluster copy from a running-server base backup or file system-level backup.

To recover the system to its current state, restore the database cluster copy and replay the backed-up WAL files.

With the continuous archiving method, you must keep a continuous sequence of all archived WAL files that extends at minimum back to the start time of your last base backup. Therefore the ideal frequency of base backups depends on:

-   The storage volume available for archived WAL files.
-   The maximum possible duration of data recovery in situations when recovery is necessary. In cases with a long period since the last backup, the system replays more WAL segments, and the recovery therefore takes more time.

Note

You cannot use `pg_dump`{.literal} and `pg_dumpall`{.literal} SQL dumps as a part of a continuous archiving backup solution. SQL dumps produce logical backups and do not contain enough information for WAL replay.

#### [3.8.1. Advantages and disadvantages of continuous archiving](#advantages-and-disadvantages-of-continuous-archiving) {#advantages-and-disadvantages-of-continuous-archiving .title}

Continuous archiving is a feature that provides a robust strategy for data backup, high availability, and point-in-time recovery (PITR) by continuously saving the database's transaction log files.

Advantages:

-   With the continuous backup method, you can use a base backup that is not entirely consistent because the log replay corrects any internal inconsistency. Therefore you can perform a base backup on a running PostgreSQL server.
-   You do not need a file system snapshot; `tar`{.literal} or a similar archiving utility is sufficient.
-   You can achieve continuous backup by continuing to archive the WAL files because the sequence of WAL files for the log replay can be indefinitely long. This is particularly valuable for large databases.
-   Continuous backup supports point-in-time recovery. It is not necessary to replay the WAL entries to the end. You can stop the replay at any point and restore the database to its state at any time since the base backup was taken.
-   If WAL files remain continuously available on another machine that has the same base backup, you can restore the database on that machine. The restored copy can be nearly current at any point.

Disadvantages:

-   Continuous backup method supports only restoration of an entire database cluster, not a subset.
-   Continuous backup requires extensive archival storage.

#### [3.8.2. Setting up WAL archiving](#setting-up-wal-archiving) {#setting-up-wal-archiving .title}

You can enable write ahead log (WAL) archiving on your PostgreSQL server to capture and save WAL segment files for backup and point-in-time recovery purposes.

A PostgreSQL server generates a sequence of WAL records while it runs. The server physically divides this sequence into WAL segment files and assigns each file a numeric name that reflects its position in the WAL sequence. Without WAL archiving, the server reuses the segment files and renames them with higher segment numbers.

When archiving WAL data, the server captures and saves the contents of each segment file to a new location before reusing the file. You have multiple options where to save the content, such as an NFS-mounted directory on another machine, a tape drive, or a CD.

Note that WAL records do not include changes to configuration files.

**Procedure**

1.  In the `/var/lib/pgsql/data/postgresql.conf`{.literal} file:

    a.  Set the `wal_level`{.literal} configuration parameter to `replica`{.literal} or higher.

    b.  Set the `archive_mode`{.literal} parameter to `on`{.literal}.

    c.  Specify the shell command in the `archive_command`{.literal} configuration parameter. You can use the `cp`{.literal} command, another command, or a shell script.

        For example:

        ``` {.language-plaintext tabindex="-1"}
        archive_command = 'test ! -f /mnt/server/archivedir/%f && cp %p /mnt/server/archivedir/%f'
        ```

        where the `%p`{.literal} parameter specifies the relative path to the file to archive, and the `%f`{.literal} parameter specifies the file name.

    This command copies archivable WAL segments to the `/mnt/server/archivedir/`{.literal} directory. After replacing the `%p`{.literal} and `%f`{.literal} parameters, the resulting command looks as follows:

    \+

    ``` {.language-plaintext tabindex="-1"}
    test ! -f /mnt/server/archivedir/00000001000000A900000065 && cp pg_wal/00000001000000A900000065 /mnt/server/archivedir/00000001000000A900000065
    ```

    \+ A similar command is generated for each new file that is archived.

    \+

    Note

    The archive command runs only after a WAL segment is completed. A server that generates little WAL traffic can have a substantial delay between the completion of a transaction and its safe recording in archive storage. To limit how old unarchived data can be, you can:

    -   Set the `archive_timeout`{.literal} parameter to force the server to switch to a new WAL segment file with a given frequency.
    -   Use the `pg_switch_wal`{.literal} parameter to force a segment switch to ensure that a transaction is archived immediately after it finishes.

2.  Restart the `postgresql`{.literal} service to enable the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart postgresql.service
    ```

3.  Test your archive command and ensure it does not overwrite an existing file and that it returns a nonzero exit status if it fails.

4.  To protect your data, ensure that the segment files are archived into a directory that does not have group or world read access.

**Additional resources**

-   [PostgreSQL 16 Documentation](https://www.postgresql.org/docs/16/continuous-archiving.html#BACKUP-ARCHIVING-WAL)

#### [3.8.3. Making a base backup](#making-a-base-backup) {#making-a-base-backup .title}

You can create a PostgreSQL base backup by using the `pg_basebackup`{.literal} utility to capture a consistent snapshot of your database for backup and recovery purposes.

The base backup creates a history file in the WAL archive area, named after the first WAL segment required for the backup.

The backup history file is a small text file containing the starting and ending times, and WAL segments of the backup. If you used the label string to identify the associated dump file, you can use the backup history file to determine which dump file to restore.

Note

Consider keeping several backup sets to be certain that you can recover your data.

**Prerequisites**

-   You are logged in as the `postgres`{.literal} superuser, a user with database administrator privileges, or another user with at least `REPLICATION`{.literal} permissions.
-   You must keep all the WAL segment files generated during and after the base backup.

**Procedure**

1.  Use the `pg_basebackup`{.literal} utility to perform the base backup.

    -   To create a base backup as individual files (plain format):

        ``` {.language-plaintext tabindex="-1"}
        $ pg_basebackup -D <backup_directory> -Fp
        ```

        Replace *backup_directory* with your chosen backup location.

        If you use tablespaces and perform the base backup on the same host as the server, you must use the `--tablespace-mapping`{.literal} option. Otherwise the backup fails upon an attempt to write the backup to the same location.

    -   To create a base backup as a `tar`{.literal} archive (`tar`{.literal} and compressed format):

        ``` {.language-plaintext tabindex="-1"}
        $ pg_basebackup -D <backup_directory> -Ft -z
        ```

        Replace *backup_directory* with your chosen backup location.

        To restore such data, you must manually extract the files in the correct locations.

    To specify which database server **pg_basebackup** will contact, use the following command-line options:

    -   The `-h`{.literal} option to define the host.

        The default host is either the local host or a host specified by the `PGHOST`{.literal} environment variable.

    -   The `-p`{.literal} option to define the port.

        The default port is indicated by the `PGPORT`{.literal} environment variable or the compiled-in default.

2.  After the base backup process completes, safely archive the database cluster copy and WAL segment files used during the backup, as specified in the backup history file.

3.  Delete WAL segments numerically lower than the WAL segment files used in the base backup because these are older than the base backup and no longer needed for a restore.

**Additional resources**

-   [PostgreSQL Documentation - base backup](https://www.postgresql.org/docs/16/continuous-archiving.html#BACKUP-BASE-BACKUP)
-   [PostgreSQL Documentation - pg_basebackup utility](https://www.postgresql.org/docs/16/app-pgbasebackup.html)

#### [3.8.4. Restoring the database by using a continuous archive backup](#restoring-the-database-by-using-a-continuous-archive-backup) {#restoring-the-database-by-using-a-continuous-archive-backup .title}

You can restore a PostgreSQL database by restoring the base backup and applying archived WAL files for point-in-time recovery.

**Procedure**

1.  Stop the server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop postgresql.service
    ```

2.  Copy the necessary data to a temporary location.

    Preferably, copy the whole cluster data directory and any tablespaces. Note that this requires enough free space on your system to hold two copies of your existing database.

    If you do not have enough space, save the contents of the cluster's `pg_wal`{.literal} directory, which can contain logs that were not archived before the system went down.

3.  Remove all existing files and subdirectories under the cluster data directory and under the root directories of any tablespaces you are using.

4.  Restore the database files from your base backup.

    Ensure that:

    -   The files are restored with the correct ownership (the database system user, not `root`{.literal}).
    -   The files are restored with the correct permissions.
    -   The symbolic links in the `pg_tblspc/`{.literal} subdirectory are restored correctly.

5.  Remove any files present in the `pg_wal/`{.literal} subdirectory.

    These files resulted from the base backup and are therefore obsolete. If you did not archive `pg_wal/`{.literal}, re-create it with proper permissions.

6.  Copy any unarchived WAL segment files that you saved in step 2 into `pg_wal/`{.literal}.

7.  Create the `recovery.conf`{.literal} recovery command file in the cluster data directory and specify the shell command in the `restore_command`{.literal} configuration parameter. You can use the `cp`{.literal} command, another command, or a shell script. For example:

    ``` {.language-plaintext tabindex="-1"}
    restore_command = 'cp /mnt/server/archivedir/%f "%p"'
    ```

8.  Start the server:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start postgresql.service
    ```

    The server enters the recovery mode and proceeds to read through the archived WAL files that it needs.

    If an external error terminates the recovery process, you can restart the server to continue the recovery. When the recovery process completes, the server renames `recovery.conf`{.literal} to `recovery.done`{.literal}. This prevents the server from accidentally re-entering the recovery mode after it starts normal database operations.

9.  Check the contents of the database to verify that the database has recovered into the required state.

    If the database has not recovered into the required state, return to step 1. If the database has recovered into the required state, allow the users to connect by restoring the client authentication configuration in the `pg_hba.conf`{.literal} file.

**Additional resources**

-   [Continuous archiving method](https://www.postgresql.org/docs/16/continuous-archiving.html)

### [3.9. Directly transferring a PostgreSQL database from one server to another](#directly-transferring-a-postgresql-database-from-one-server-to-another) {#directly-transferring-a-postgresql-database-from-one-server-to-another .title}

You can use the `pg_dump`{.literal} and `psql`{.literal} utilities to back up a PostgreSQL database and directly restore it on another PostgreSQL server. With this method you can transfer a database in a single step without intermediate files.

**Prerequisites**

-   You are logged in as the `postgres`{.literal} user.

**Procedure**

-   Transfer a database from the source server to a destination server:

    ``` {.language-plaintext tabindex="-1"}
    $ pg_dump -h <source_server> <db_name> | psql -h <destination_server> <db_name>
    ```

    If the transfer succeeds, `psql`{.literal} prints a status keyword for each applied SQL statement, such as `SET`{.literal}, `CREATE TABLE`{.literal}, `ALTER TABLE`{.literal}, and `COPY`{.literal}. The `COPY`{.literal} line includes the number of transferred rows. For example:

    ``` {.language-plaintext tabindex="-1"}
    SET
    SET
    CREATE TABLE
    ALTER TABLE
    COPY 20
    ```

### [3.10. Migrating a PostgreSQL instance from a previous RHEL version to PostgreSQL on RHEL 10](#migrating-a-postgresql-instance-from-a-previous-rhel-version-to-postgresql-on-rhel-10) {#migrating-a-postgresql-instance-from-a-previous-rhel-version-to-postgresql-on-rhel-10 .title}

If you already run PostgreSQL on RHEL 9 and want to move the database software to a host that runs RHEL 10, you can migrate the databases.

The following migration methods are available:

-   Backup and restore upgrade: This method might require more time but works in most scenarios.
-   Fast upgrade by using the `pg_upgrade`{.literal} utility: This method is faster but works only if you migrate from PostgreSQL 13 to 16 and the hardware architecture stays the same.

Important

Always back up the `/var/lib/pgsql/data/`{.literal} directory on the source host before a PostgreSQL migration.

#### [3.10.1. Migrating to PostgreSQL on RHEL 10 by using the backup and restore method](#migrating-to-postgresql-on-rhel-10-by-using-the-backup-and-restore-method) {#migrating-to-postgresql-on-rhel-10-by-using-the-backup-and-restore-method .title}

Use the backup and restore method to migrate data from any RHEL 8 or RHEL 9 version of PostgreSQL to any equal or later version of PostgreSQL on RHEL 10.

**Prerequisites**

-   The existing database server runs on RHEL 8 or RHEL 9 and uses a PostgreSQL version installed from the RHEL repositories.
-   The locale settings on both hosts are the same. To verify this, compare the output of the `echo $LANG`{.literal} command on both hosts.

**Procedure**

1.  On the host with the existing PostgreSQL instance that you want to migrate:

    a.  Export all databases to the `/var/lib/pgsql/pgdump_file.sql`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # su - postgres -c "pg_dumpall > /var/lib/pgsql/pgdump_file.sql"
        ```

    b.  Check the exported file:

        ``` {.language-plaintext tabindex="-1"}
        # su - postgres -c 'less "/var/lib/pgsql/pgdump_file.sql"'
        ```

    c.  Copy the database dump that you created in an earlier step and the PostgreSQL configuration files to the RHEL 10 host, for example:

        ``` {.language-plaintext tabindex="-1"}
        # scp /var/lib/pgsql/pgdump_file.sql \
               /var/lib/pgsql/data/pg_hba.conf \
               /var/lib/pgsql/data/pg_ident.conf \
               /var/lib/pgsql/data/postgresql.conf \
               <user>@<rhel_10_host>:/tmp/
        ```

2.  On the RHEL 10 host:

    a.  Install the `postgresql-server`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install postgresql-server
        ```

    b.  Initialize the `/var/lib/pgsql/data/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        # postgresql-setup --initdb
        ```

    c.  Move the copied configuration files to the `/var/lib/pgsql/data/`{.literal} directory:

        ``` {.language-plaintext tabindex="-1"}
        # mv /tmp/pg_hba.conf \
             /tmp/pg_ident.conf \
             /tmp/postgresql.conf \
             /var/lib/pgsql/data/
        ```

    d.  Ensure a correct ownership of the content in the `/var/lib/pgsql/data/ directory`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # chown -R postgres:postgres /var/lib/pgsql/data/
        ```

    e.  Restore the SELinux context on `/var/lib/pgsql/data/`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # restorecon -Rv /var/lib/pgsql/data/
        ```

    f.  Enable and start the `postgresql`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now postgresql.service
        ```

    g.  Import the data as the `postgres`{.literal} user:

        ``` {.language-plaintext tabindex="-1"}
        # su - postgres -c 'psql -f /tmp/pgdump_file.sql postgres'
        ```

    h.  Verify your databases and ensure that your applications that use the PostgreSQL server work as expected.

#### [3.10.2. Migrating PostgreSQL 13 from a previous RHEL version to PostgreSQL 16 on RHEL 10 by using pg_upgrade](#migrating-postgresql-13-from-a-previous-rhel-version-to-postgresql-16-on-rhel-10-by-using-pg-upgrade) {#migrating-postgresql-13-from-a-previous-rhel-version-to-postgresql-16-on-rhel-10-by-using-pg_upgrade .title}

If you want to migrate a PostgreSQL 13 instance from a previous RHEL version to PostgreSQL 16 on RHEL 10, you can use the fast upgrade method. With this method, you copy the content of the `/var/lib/pgsql/data/`{.literal} directory to the RHEL 10 host and the `pg_upgrade`{.literal} utility converts the databases.

Important

The fast upgrade method works only if your existing PostgreSQL instance is version 13 and the hardware architecture is the same on the source and destination host. In other cases, use the [backup and restore method](#migrating-to-postgresql-on-rhel-10-by-using-the-backup-and-restore-method "3.10.1. Migrating to PostgreSQL on RHEL 10 by using the backup and restore method").

**Prerequisites**

-   The existing database server uses PostgreSQL 13.

-   The hardware architecture of the current and future server is the same.

-   The RHEL 10 host has enough free space on the disk that holds the `/var/lib/pgsql/`{.literal} directory.

    For example, migrating a 10 GiB PostgreSQL directory requires at least 20 GiB of free disk space on the RHEL 10 host.

-   The locale settings on both hosts are the same. To verify this, compare the output of the `echo $LANG`{.literal} command on both hosts.

**Procedure**

1.  On the host with the existing PostgreSQL instance that you want to migrate:

    a.  Stop the `postgresql`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl stop postgresql.service
        ```

    b.  Change into the `/var/lib/pgsql/`{.literal} directory, and back up the `data`{.literal} subdirectory:

        ``` {.language-plaintext tabindex="-1"}
        # cd /var/lib/pgsql/
        # tar -zcf ~/pgdata.bak.tar.gz data/
        ```

    c.  Copy the `~/pgdata.bak.tar.gz`{.literal} archive to the RHEL 10 host, for example:

        ``` {.language-plaintext tabindex="-1"}
        # scp ~/pgdata.bak.tar.gz <user>@<rhel_10_host>:/tmp/
        ```

2.  On the RHEL 10 host:

    a.  Install the required packages:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install postgresql-server postgresql-upgrade
        ```

        The `postgresql-upgrade`{.literal} package provides a PostgreSQL 13 server which is required during the migration.

    b.  If you use third party PostgreSQL server modules, build them against both the `postgresql-devel`{.literal} and `postgresql-upgrade-devel`{.literal} packages, and install them.

    c.  Ensure that the `postgresql`{.literal} service is stopped:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl stop postgresql.service
        ```

    d.  Change into the `/var/lib/pgsql/`{.literal} directory, and extract the backed up data directory from the previous host:

        ``` {.language-plaintext tabindex="-1"}
        # cd /var/lib/pgsql/
        # tar -zxf /tmp/pgdata.bak.tar.gz
        ```

    e.  Optional: Remove the `/tmp/pgdata.bak.tar.gz`{.literal} archive:

        ``` {.language-plaintext tabindex="-1"}
        # rm /tmp/pgdata.bak.tar.gz
        ```

    f.  Perform the upgrade process:

        ``` {.language-plaintext tabindex="-1"}
        # postgresql-setup --upgrade
        ```

        The `postgresql-setup`{.literal} shell script renames the `/var/lib/pgsql/data/`{.literal} directory to `/var/lib/pgsql/data-old/`{.literal} and uses the `pg_upgrade`{.literal} utility to migrate the databases to a re-created `/var/lib/pgsql/data/`{.literal} directory.

        Important

        The `pg_upgrade`{.literal} utility migrates only the databases and not the configuration files. After the migration, `/var/lib/pgsql/data/`{.literal} contains only the default `.conf`{.literal} files. If you, previously, had custom configuration files, copy them from the `/var/lib/pgsql/data-old/`{.literal} directory and ensure that they are compatible with the new PostgreSQL version.

    g.  Enable and start the `postgresql`{.literal} service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable --now postgresql.service
        ```

    h.  Clean up and analyze all databases:

        ``` {.language-plaintext tabindex="-1"}
        # su postgres -c 'vacuumdb --all --analyze-in-stages'
        ```

    i.  Verify your databases and ensure that your applications that use the PostgreSQL server work as expected.

    j.  Optional: Remove the `/var/lib/pgsql/data-old/`{.literal} directory which contains the databases and configuration file from before the migration.

        ``` {.language-plaintext tabindex="-1"}
        # rm -r /var/lib/pgsql/data-old/
        ```

    k.  Optional: Remove the `postgresql-upgrade`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf remove postgresql-upgrade
        ```

### [3.11. Upgrading from a RHEL 10 version of PostgreSQL 16 to PostgreSQL 18](#upgrading-from-a-rhel-10-version-of-postgresql-16-to-postgresql-18) {#upgrading-from-a-rhel-10-version-of-postgresql-16-to-postgresql-18 .title}

You can upgrade your PostgreSQL database server from version 16 to 18 on RHEL 10 to access new features and improvements.

For notable enhancements and changes, see the [release note](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/10.2_release_notes/new-features-and-enhancements#Jira-RHEL-116546) in the RHEL 10.2 Release Notes document.

**Prerequisites**

-   The existing database server uses PostgreSQL 16 on RHEL 10.

-   The host has enough free space on the disk that holds the `/var/lib/pgsql/`{.literal} directory.

    For example, if the size of the directory is 10 GiB, you need at least 10 GiB extra free disk space.

**Procedure**

1.  Display the current data page checksum status:

    ``` {.language-plaintext tabindex="-1"}
    # pg_controldata /var/lib/pgsql/data | grep "Data page checksum"
    ```

    ``` {.language-plaintext tabindex="-1"}
    Data page checksum version:           0
    ```

    If the command returns `0`{.literal}, data page checksums are disabled.

2.  Stop the `postgresql`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl stop postgresql
    ```

3.  If data page checksums are disabled, determine the strategy:

    -   If you want to enable data page checksums before the upgrade to improve data integrity:

        i.  Enable data page checksums::

            ``` {.language-plaintext tabindex="-1"}
            # pg_checksums --enable -D /var/lib/pgsql/data/
            ```

            Depending on the size of your databases, this operation can take a significant amount of time.

        ii. Verify the activation:

            ``` {.language-plaintext tabindex="-1"}
            # pg_controldata /var/lib/pgsql/data | grep "Data page checksum"
            ```

            ``` {.language-plaintext tabindex="-1"}
            Data page checksum version:           1
            ```

    -   If you want to keep the data page checksums disabled, set the `PGSETUP_INITDB_OPTIONS`{.literal} environment option to `--no-data-checksums`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # export PGSETUP_INITDB_OPTIONS="--no-data-checksums"
        ```

4.  Switch to PostgreSQL 18:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install --allowerasing postgresql18-server
    ```

    Important

    Review the proposed `dnf`{.literal} transaction carefully before proceeding. Ensure that each package from the previous version is being replaced by its equivalent in the new version. The `--allowerasing`{.literal} option can lead to unintended package removal if the installation list is incomplete, potentially removing more software than it installs.

5.  Install the `postgresql18-upgrade`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install postgresql18-upgrade
    ```

6.  Perform the upgrade process:

    ``` {.language-plaintext tabindex="-1"}
    # postgresql-setup --upgrade
    ```

    The `postgresql-setup`{.literal} shell script renames the `/var/lib/pgsql/data/`{.literal} directory to `/var/lib/pgsql/data-old/`{.literal} and uses the `pg_upgrade`{.literal} utility to migrate the databases to a re-created `/var/lib/pgsql/data/`{.literal} directory.

    Important

    The `pg_upgrade`{.literal} utility migrates only the databases and not the configuration files. After the migration, `/var/lib/pgsql/data/`{.literal} contains only the default `.conf`{.literal} files. If you, previously, had custom configuration files, copy them from the `/var/lib/pgsql/data-old/`{.literal} directory and ensure that they are compatible with the new PostgreSQL version.

7.  Start the `postgresql`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start postgresql
    ```

8.  Clean up and analyze all databases:

    ``` {.language-plaintext tabindex="-1"}
    # su postgres -c 'vacuumdb --all --analyze-in-stages'
    ```

9.  Verify your databases and ensure that your applications that use the PostgreSQL server work as expected.

10. Optional: Remove the `/var/lib/pgsql/data-old/`{.literal} directory, which contains the databases and configuration files from before the migration.

    ``` {.language-plaintext tabindex="-1"}
    # rm -r /var/lib/pgsql/data-old/
    ```

11. Optional: Remove the `postgresql18-upgrade`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf remove postgresql18-upgrade
    ```

## [Legal Notice](#idm140662000774848) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
