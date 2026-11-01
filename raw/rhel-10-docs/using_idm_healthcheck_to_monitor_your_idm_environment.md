---
{"title": "Using IdM Healthcheck to monitor your IdM environment", "guide": "using_idm_healthcheck_to_monitor_your_idm_environment", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_idm_healthcheck_to_monitor_your_idm_environment/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Using IdM Healthcheck to monitor your IdM environment {#using-idm-healthcheck-to-monitor-your-idm-environment .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Performing status and health checks {#performing-status-and-health-checks .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140553447967296)

**Abstract**

The `ipa-healthcheck`{.literal} utility helps administrators to detect problems in a Red Hat Identity Management (IdM) environment. This includes status checks of IdM services, configuration file permissions, replication statuses, and issues with certificates.

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

## [Chapter 1. Installing and running the IdM Healthcheck tool](#installing-and-running-the-idm-healthcheck-tool) {#chapter-1.-installing-and-running-the-idm-healthcheck-tool .title}

Install and run the IdM Healthcheck tool to help find issues that can impact the performance of your IdM environment.

### [1.1. Healthcheck in IdM](#healthcheck-in-idm) {#healthcheck-in-idm .title}

The `Healthcheck`{.literal} command line tool in Identity Management (IdM) helps find issues that can impact the performance of your IdM environment. Using Healthcheck, you can identify an issue in advance so that you can correct it before it becomes critical.

Note

You can use Healthcheck without obtaining a Kerberos ticket.

**Modules are independent**

Healthcheck consists of independent modules which check for:

-   Replication issues
-   Certificate validity
-   Certificate authority infrastructure issues
-   IdM and Active Directory trust issues
-   Correct file permissions and ownership settings

**Output formats and destination**

You can set the following types of output for Healthcheck to generate by using the `output-type`{.literal} option:

-   `json`{.literal}: Machine-readable output in JSON format (default)
-   `human`{.literal}: Human-readable output

You can specify a file to store the output by using the `--output-file`{.literal} option.

**Results**

Each Healthcheck module returns one of the following results:

SUCCESS
:   The system is configured as expected.

WARNING
:   It is advisable to monitor or evaluate the configuration.

ERROR
:   The system is not configured as expected.

CRITICAL
:   The configuration is not as expected, with a significant potential to impact the functioning of your IdM deployment.

### [1.2. Installing IdM Healthcheck](#installing-idm-healthcheck) {#installing-idm-healthcheck .title}

You can install the IdM Healthcheck tool to help find issues that can impact the performance of your IdM environment.

**Prerequisites**

-   You are logged in as `root`{.literal}.

**Procedure**

-   Install the `ipa-healthcheck`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install ipa-healthcheck
    ```

**Verification**

-   Perform a basic Healthcheck test:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck
    ```

    ``` {.language-plaintext tabindex="-1"}
    []
    ```

    The empty square brackets `[]`{.literal} indicate a fully-functioning IdM installation.

### [1.3. Running IdM Healthcheck manually](#running-idm-healthcheck-manually) {#running-idm-healthcheck-manually .title}

You can run Healthcheck tests either manually on the CLI or automatically by using a timer. You can manually run IdM Healthcheck tests from the command line to diagnose and monitor the health of your environment.

**Prerequisites**

-   The Healthcheck tool is installed. See [Installing IdM Healthcheck](#installing-idm-healthcheck "1.2. Installing IdM Healthcheck").

**Procedure**

1.  Optional: To display a list of all available Healthcheck tests, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --list-sources
    ```

2.  To run the Healthcheck utility, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck
    ```

### [1.4. Running IdM Healthcheck on a schedule](#running-idm-healthcheck-on-a-schedule) {#running-idm-healthcheck-on-a-schedule .title}

You can configure IdM Healthcheck to run on a schedule. This includes configuring the `systemd`{.literal} timer to run the Healthcheck tool periodically and generate the logs and the `crond`{.literal} service to ensure log rotation.

The default log name is `healthcheck.log`{.literal} and the rotated logs use the `healthcheck.log-YYYYMMDD`{.literal} format.

Note

The Healthcheck timer tool is not a real-time tool. It is only meant to be run a few times an hour. If you require real-time monitoring of, for example, services or disk space, use a different tool.

**Prerequisites**

-   You have `root`{.literal} privileges.

**Procedure**

1.  Enable a `systemd`{.literal} timer:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable ipa-healthcheck.timer
    ```

    ``` {.language-plaintext tabindex="-1"}
    Created symlink /etc/systemd/system/multi-user.target.wants/ipa-healthcheck.timer -> /usr/lib/systemd/system/ipa-healthcheck.timer.
    ```

2.  Start the `systemd`{.literal} timer:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start ipa-healthcheck.timer
    ```

3.  Open the `/etc/logrotate.d/ipahealthcheck`{.literal} file to configure the number of logs you want to be saved:

    ``` {.language-plaintext tabindex="-1"}
    [...]
        rotate 30
    }
    ```

    By default, logs are stored for 30 days before they are overwritten by newer logs.

4.  In the same file, configure the path to the file storing the logs.

    ``` {.language-plaintext tabindex="-1"}
    /var/log/ipa/healthcheck/healthcheck.log {
    [...]
    ```

    By default, logs are saved in the `/var/log/ipa/healthcheck/`{.literal} directory.

5.  Save the file.

6.  Ensure that the `crond`{.literal} service is enabled and running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable crond
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start crond
    ```

7.  To start generating logs, start the IdM healthcheck service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start ipa-healthcheck
    ```

**Verification**

1.  Navigate to the `/var/log/ipa/healthcheck/`{.literal} directory.
2.  View the contents of the log file to check if it was created correctly.

### [1.5. Log rotation](#log-rotation) {#log-rotation .title}

Log rotation creates a new log file every day and the files are organized by date. The date is included in the filename.

By using log rotation, you can configure the maximum number of log files to store. If this number is exceeded, the newest file replaces the oldest one. For example, if the maximum rotation number is thirty, the thirty-first log file replaces the first, that is the oldest one.

Log rotation reduces voluminous log files and organizes them. This helps you analyze the logs.

### [1.6. IdM Healthcheck configuration modifications](#idm-healthcheck-configuration-modifications) {#idm-healthcheck-configuration-modifications .title}

You can change Identity Management (IdM) Healthcheck settings by adding the desired command line options to the `/etc/ipahealthcheck/ipahealthcheck.conf`{.literal} file. This can be useful when, for example, you configured log rotation previously and now want to ensure the logs are in a format suitable for automatic analysis, but do not want to create a new timer.

After you change the settings, all Healthcheck logs will use them, even when you run Healthcheck manually.

Note

When running Healthcheck manually, the settings in the configuration file take precedence over the options specified in the command line. For example, if `output_type`{.literal} is set to `human`{.literal} in the configuration file, specifying `json`{.literal} on the command line has no effect. Any command line options you use that are not specified in the configuration file are applied normally.

**Additional resources**

-   [Running IdM Healthcheck on a schedule](#running-idm-healthcheck-on-a-schedule "1.4. Running IdM Healthcheck on a schedule")

### [1.7. Configuring Healthcheck to change the output logs format](#configuring-healthcheck-to-change-the-output-logs-format) {#configuring-healthcheck-to-change-the-output-logs-format .title}

You can configure Healthcheck with a timer already configured. In this example, you re-configure Healthcheck to start producing logs in a human-readable format and to also include successful results instead of only errors.

**Prerequisites**

-   You have `root`{.literal} privileges.
-   You have previously configured Healthcheck to run on a schedule.

**Procedure**

1.  Open the `/etc/ipahealthcheck/ipahealthcheck.conf`{.literal} file in a text editor.
2.  Add options `output_type=human`{.literal} and `all=True`{.literal} to the `[default]`{.literal} section.
3.  Save and close the file.

**Verification**

1.  Run Healthcheck manually:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck
    ```

2.  Go to `/var/log/ipa/healthcheck/`{.literal} and check that the logs are in the correct format.

**Additional resources**

-   [Running IdM Healthcheck on a schedule](#running-idm-healthcheck-on-a-schedule "1.4. Running IdM Healthcheck on a schedule")

## [Chapter 2. Checking services by using IdM Healthcheck](#checking-services-by-using-idm-healthcheck) {#chapter-2.-checking-services-by-using-idm-healthcheck .title}

You can monitor services used by the Identity Management (IdM) server by using the Healthcheck tool.

### [2.1. The IdM services Healthcheck test](#the-idm-services-healthcheck-test) {#the-idm-services-healthcheck-test .title}

The Healthcheck tool includes a test to check if the Identity Management (IdM) services are running correctly. Start with this Healthcheck test as IdM services that are not running correctly can cause failures in other Healthcheck tests.

The services test is context-specific based on what features are configured. For example, `named`{.literal} is only checked if the integrated IdM DNS service is configured on the IdM server. Others, for example `smb`{.literal} or `winbind`{.literal}, are only checked if an IdM-AD trust is enabled.

The list of IdM services that the test evaluates can look as follows:

-   certmonger
-   dirsrv
-   gssproxy
-   httpd
-   ipa_custodia
-   ipa_otpd
-   kadmin
-   krb5kdc
-   named
-   ods_enforcerd
-   ipa_dnskeysyncd
-   pki_tomcatd
-   sssd
-   chronyd
-   smb
-   winbind

You can view this list by running the `ipa-healthcheck --list-sources`{.literal} command and identifying the `ipahealthcheck.meta.services`{.literal} section in the output.

### [2.2. Screening IdM services by using Healthcheck](#screening-idm-services-by-using-healthcheck) {#screening-idm-services-by-using-healthcheck .title}

You can run a standalone manual test of services running on the Identity Management (IdM) server by using the Healthcheck tool.

**Procedure**

-   To run the services test, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source=ipahealthcheck.meta.services
    ```

    -   The `--source=ipahealthcheck.meta.services`{.literal} option ensures that IdM Healthcheck only performs the services test.
    -   The `--failures-only`{.literal} option is enabled by default and it ensures that IdM Healthcheck only reports warnings, errors and critical issues.

    A successful test displays empty brackets:

    ``` {.language-plaintext tabindex="-1"}
    [ ]
    ```

    If one of the services fails, the result can looks similarly to this example:

    ``` {.language-plaintext tabindex="-1"}
    {
      "source": "ipahealthcheck.meta.services",
      "check": "httpd",
      "result": "ERROR",
      "kw": {
        "status": false,
        "msg": "httpd: not running"
      }
    }
    ```

    Note

    Run this test on all IdM servers when trying to discover issues.

**Additional resources**

-   [Healthcheck in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_idm_healthcheck_to_monitor_your_idm_environment/index#installing-and-running-the-ipa-healthcheck-tool_using-idm-healthcheck-to-monitor-your-idm-environment)

## [Chapter 3. Checking disk space by using IdM Healthcheck](#checking-disk-space-by-using-idm-healthcheck) {#chapter-3.-checking-disk-space-by-using-idm-healthcheck .title}

You can monitor the free disk space on an Identity Management (IdM) server by using the Healthcheck tool.

### [3.1. Disk space healthcheck test](#disk-space-healthcheck-test) {#disk-space-healthcheck-test .title}

The Healthcheck tool includes the `FileSystemSpaceCheck`{.literal} test for checking available disk space.

The test checks the following:

-   The minimum raw free bytes needed.
-   The percentage --- the minimum free disk space is hardcoded to 20%.

The test checks the following paths:

+-----------------------------------+-----------------------------------+
| Paths checked by the test         | Minimal disk space in MB          |
+:==================================+:==================================+
| `/var/lib/dirsrv/`{.literal}      | 1024                              |
+-----------------------------------+-----------------------------------+
| `/var/lib/ipa/backup/`{.literal}  | 512                               |
+-----------------------------------+-----------------------------------+
| `/var/log/`{.literal}             | 1024                              |
+-----------------------------------+-----------------------------------+
| `var/log/audit/`{.literal}        | 512                               |
+-----------------------------------+-----------------------------------+
| `/var/tmp/`{.literal}             | 512                               |
+-----------------------------------+-----------------------------------+
| `/tmp/`{.literal}                 | 512                               |
+-----------------------------------+-----------------------------------+

: Table 3.1. Tested paths

Show more

Insufficient free disk space can cause issues with the following:

-   Logging
-   Execution
-   Backups

You can find the `FileSystemSpaceCheck`{.literal} test by running the `ipa-healthcheck --list-sources`{.literal} command and identifying the `ipahealthcheck.system.filesystemspace`{.literal} section in the output.

### [3.2. Screening disk space by using the Healthcheck tool](#screening-disk-space-by-using-the-healthcheck-tool) {#screening-disk-space-by-using-the-healthcheck-tool .title}

You can run a standalone manual test to check available disk space on an Identity Management (IdM) server by using the Healthcheck tool.

**Procedure**

-   To run the disk space test, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source=ipahealthcheck.system.filesystemspace
    ```

    The `--source=ipahealthcheck.meta.services`{.literal} option ensures that IdM Healthcheck only performs the disk space test.

    A successful test displays empty brackets:

    ``` {.language-plaintext tabindex="-1"}
    []
    ```

    As an example, a failed test can display:

    ``` {.language-plaintext tabindex="-1"}
    {
      "source": "ipahealthcheck.system.filesystemspace",
      "check": "FileSystemSpaceCheck",
      "result": "ERROR",
      "kw": {
        "msg": "/var/lib/dirsrv: free space under threshold: 0 MiB < 1024 MiB",
        "store": "/var/lib/dirsrv",
        "free_space": 0,
        "threshold": 1024
      }
    }
    ```

    This failed test informs you that no space is available in the `/var/lib/dirsrv`{.literal} directory.

    Note

    Run this test on all IdM servers when trying to discover issues.

**Additional resources**

-   [Healthcheck in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_idm_healthcheck_to_monitor_your_idm_environment/index)

## [Chapter 4. Verifying permissions of IdM configuration files by using Healthcheck](#verifying-permissions-of-idm-configuration-files-by-using-healthcheck) {#chapter-4.-verifying-permissions-of-idm-configuration-files-by-using-healthcheck .title}

You can test the ownership and permissions of configuration files on an Identity Management (IdM) server by using the Healthcheck tool.

### [4.1. File permissions Healthcheck tests](#file-permissions-healthcheck-tests) {#file-permissions-healthcheck-tests .title}

The Healthcheck tool tests the ownership and permissions of files installed or configured by Identity Management (IdM).

If you change the ownership or permissions of these files, the tests return a warning in the `result`{.literal} section. While this does not necessarily mean that the configuration does not work, it means that the file differs from the default configuration.

You can find the file permissions tests under the `ipahealthcheck.ipa.files`{.literal} source of the output of the `ipa-healthcheck --list-sources`{.literal} command.

IPAFileNSSDBCheck
:   This test checks the 389-ds NSS database and the Certificate Authority (CA) database, if relevant. The 389-ds database is located in `/etc/dirsrv/slapd-<dashed-REALM>`{.literal} and the CA database is located in `/etc/pki/pki-tomcat/alias/`{.literal}.

IPAFileCheck

:   This test checks the following files:

    -   `/var/lib/ipa/ra-agent.{key|pem}`{.literal}

    -   `/var/lib/ipa/certs/httpd.pem`{.literal}

    -   `/var/lib/ipa/private/httpd.key`{.literal}

    -   `/etc/httpd/alias/ipasession.key`{.literal}

    -   `/etc/dirsrv/ds.keytab`{.literal}

    -   `/etc/ipa/ca.crt`{.literal}

    -   `/etc/ipa/custodia/server.keys`{.literal}

    -   `/etc/resolv.conf`{.literal}

    -   `/etc/hosts`{.literal}

        If PKINIT is enabled, it also tests:

    -   `/var/lib/ipa/certs/kdc.pem`{.literal}

    -   `/var/lib/ipa/private/kdc.key`{.literal}

        If DNS is configured, it also tests:

    -   `/etc/named.keytab`{.literal}

    -   `/etc/ipa/dnssec/ipa-dnskeysyncd.keytab`{.literal}

TomcatFileCheck

:   This test checks certain `tomcat`{.literal}-specific files:

    -   `/etc/pki/pki-tomcat/password.conf`{.literal}
    -   `/var/lib/pki/pki-tomcat/conf/ca/CS.cfg`{.literal}
    -   `/etc/pki/pki-tomcat/server.xml`{.literal}

### [4.2. Screening configuration files by using Healthcheck](#screening-configuration-files-by-using-healthcheck) {#screening-configuration-files-by-using-healthcheck .title}

You can run a standalone manual test to check the ownership and permissions of configuration files on an Identity Management (IdM) server by using the Healthcheck tool.

**Procedure**

-   To run Healthcheck tests on IdM configuration file ownership and permissions, while displaying only warnings, errors and critical issues, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source=ipahealthcheck.ipa.files
    ```

    A successful test displays empty brackets:

    ``` {.language-plaintext tabindex="-1"}
    []
    ```

    Failed tests display results similar to the following `WARNING`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    {
      "source": "ipahealthcheck.ipa.files",
      "check": "IPAFileNSSDBCheck",
      "result": "WARNING",
      "kw": {
        "key": "_etc_dirsrv_slapd-EXAMPLE-TEST_pkcs11.txt_mode",
        "path": "/etc/dirsrv/slapd-EXAMPLE-TEST/pkcs11.txt",
        "type": "mode",
        "expected": "0640",
        "got": "0666",
        "msg": "Permissions of /etc/dirsrv/slapd-EXAMPLE-TEST/pkcs11.txt are 0666 and should be 0640"
      }
    }
    ```

    Note

    Run these tests on all IdM servers when trying to find issues.

**Additional resources**

-   [Healthcheck in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_idm_healthcheck_to_monitor_your_idm_environment/index#installing-and-running-the-ipa-healthcheck-tool_using-idm-healthcheck-to-monitor-your-idm-environment)

## [Chapter 5. Checking DNS records by using IdM Healthcheck](#checking-dns-records-by-using-idm-healthcheck) {#chapter-5.-checking-dns-records-by-using-idm-healthcheck .title}

You can identify issues with DNS records in Identity Management (IdM) by using the Healthcheck tool.

### [5.1. DNS records healthcheck test](#dns-records-healthcheck-test) {#dns-records-healthcheck-test .title}

The Healthcheck tool includes the `IPADNSSystemRecordsCheck`{.literal} test for checking that the expected DNS records required for autodiscovery are resolvable.

Specifically, the test checks the DNS records obtained by the `ipa dns-update-system-records --dry-run`{.literal} command by using the first resolver specified in the `/etc/resolv.conf`{.literal} file on the IdM server to which you are logged in.

You can find the `IPADNSSystemRecordsCheck`{.literal} test under the `ipahealthcheck.ipa.idns`{.literal} source of the output of the `ipa-healthcheck --list-sources`{.literal} command.

### [5.2. Screening IdM DNS records by using the Healthcheck tool](#screening-idm-dns-records-by-using-the-healthcheck-tool) {#screening-idm-dns-records-by-using-the-healthcheck-tool .title}

You can run a standalone manual test to check DNS records on an Identity Management (IdM) server by using the Healthcheck tool.

The Healthcheck tool includes many tests. Results can be narrowed down by including only the DNS records tests by adding the `--source ipahealthcheck.ipa.idns`{.literal} option.

**Prerequisites**

-   You have `root`{.literal} privileges.

**Procedure**

-   To run the DNS records test, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source ipahealthcheck.ipa.idns
    ```

    -   The `--source ipahealthcheck.ipa.idns`{.literal} option ensures that IdM Healthcheck only performs the DNS records test.

        If the record is resolvable, the test returns `SUCCESS`{.literal} as a result:

        ``` {.language-plaintext tabindex="-1"}
        {
            "source": "ipahealthcheck.ipa.idns",
            "check": "IPADNSSystemRecordsCheck",
            "result": "SUCCESS",
            "uuid": "eb7a3b68-f6b2-4631-af01-798cac0eb018",
            "when": "20200415143339Z",
            "duration": "0.210471",
            "kw": {
              "key": "_ldap._tcp.idm.example.com.:server1.idm.example.com."
            }
        }
        ```

        The test returns a `WARNING`{.literal} when, for example, the number of records does not match the expected number:

    ``` {.language-plaintext tabindex="-1"}
    {
        "source": "ipahealthcheck.ipa.idns",
        "check": "IPADNSSystemRecordsCheck",
        "result": "WARNING",
        "uuid": "972b7782-1616-48e0-bd5c-49a80c257895",
        "when": "20200409100614Z",
        "duration": "0.203049",
        "kw": {
          "msg": "Got {count} ipa-ca A records, expected {expected}",
          "count": 2,
          "expected": 1
        }
    }
    ```

**Additional resources**

-   [Healthcheck in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_idm_healthcheck_to_monitor_your_idm_environment/index#installing-and-running-the-ipa-healthcheck-tool_using-idm-healthcheck-to-monitor-your-idm-environment)

### [5.3. Additional resources](#checking-dns-records-by-using-idm-healthcheck_53-additional-resources) {#additional-resources .title}

-   [Healthcheck in IdM](#healthcheck-in-idm "1.1. Healthcheck in IdM")

## [Chapter 6. Verifying the optimal number of KDC worker processes by using IdM Healthcheck](#verifying-the-optimal-number-of-kdc-worker-processes-by-using-idm-healthcheck) {#chapter-6.-verifying-the-optimal-number-of-kdc-worker-processes-by-using-idm-healthcheck .title}

You can use the Healthcheck tool in Identity Management (IdM) to verify that the Kerberos Key Distribution Center (KDC) is configured to use the optimal number of `krb5kdc`{.literal} worker processes, which should be equal to the number of CPU cores on the host.

You can find the test for the correct number of KDC worker processes under the `ipahealthcheck.ipa.kdc`{.literal} source. As the Healthcheck tool includes many tests, you can narrow down the results by including only the KDC worker tests by adding the `--source ipahealthcheck.ipa.kdc`{.literal} option.

**Prerequisites**

-   The KDC worker process Healthcheck tool is only available on RHEL 8.7 or newer.
-   You must perform Healthcheck tests as the `root`{.literal} user.

**Procedure**

-   To run the check for KDC worker processes, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source ipahealthcheck.ipa.kdc
    ```

    If the number of KDC worker processes matches the number of CPU cores, the test returns `SUCCESS`{.literal} as a result:

    ``` {.language-plaintext tabindex="-1"}
    {
        "source": "ipahealthcheck.ipa.kdc",
        "check": "KDCWorkersCheck",
        "result": "SUCCESS",
        "uuid": "68f6e20a-0aa9-427d-8fdc-fbb8196d56cd",
        "when": "20230105162211Z",
        "duration": "0.000157",
        "kw": {
        "key": "workers"
        }
    }
    ```

    The test returns a `WARNING`{.literal} if the number of worker processes does not match the number of CPU cores. In the following example, a host with 2 cores is configured to have only one KDC worker process:

    ``` {.language-plaintext tabindex="-1"}
    {
        "source": "ipahealthcheck.ipa.kdc",
        "check": "KDCWorkersCheck",
        "result": "WARNING",
        "uuid": "972b7782-1616-48e0-bd5c-49a80c257895",
        "when": "20230105122236Z",
        "duration": "0.203049",
        "kw": {
          "key": ‘workers',
          "cpus": 2,
          "workers": 1,
          "expected": "The number of CPUs {cpus} does not match the number of workers {workers} in {sysconfig}"
        }
    }
    ```

    The test also outputs a `WARNING`{.literal} if there are no configured workers. In the following example, the `KRB5KDC_ARGS`{.literal} variable is missing from the `/etc/sysconfig/krb5kdc`{.literal} configuration file:

    ``` {.language-plaintext tabindex="-1"}
      {
        "source": "ipahealthcheck.ipa.kdc",
        "check": "KDCWorkersCheck",
        "result": "WARNING",
        "uuid": "5d63ea86-67b9-4638-a41e-b71f4
    56efed7",
        "when": "20230105162526Z",
        "duration": "0.000135",
        "kw": {
          "key": "workers",
          "sysconfig": "/etc/sysconfig/krb5kdc",
          "msg": "KRB5KDC_ARGS is not set in {sysconfig}"
        }
      }
    ```

## [Chapter 7. Checking IdM replication by using Healthcheck](#checking-idm-replication-by-using-healthcheck) {#chapter-7.-checking-idm-replication-by-using-healthcheck .title}

Run Healthcheck tests on your IdM replication topology to identify configuration issues early, preventing data inconsistencies and service disruptions that could affect user authentication and access to domain resources.

You can test Identity Management (IdM) replication by using the Healthcheck tool.

### [7.1. The IdM replication and topology Healthcheck tests](#the-idm-replication-and-topology-healthcheck-tests) {#the-idm-replication-and-topology-healthcheck-tests .title}

Use built-in Healthcheck tests to verify your IdM replication topology meets connectivity and agreement requirements, preventing isolated servers and replication conflicts that could compromise data integrity.

The Identity Management (IdM) Healthcheck tool includes tests of the IdM topology configuration. The tests search for replication conflict issues.

You can find the `IPATopologyDomainCheck`{.literal} and `ReplicationConflictCheck`{.literal} tests under the `ipahealthcheck.ipa.topology`{.literal} and `ipahealthcheck.ds.replication`{.literal} sources of the output of the `ipa-healthcheck --list-sources`{.literal} command.

IPATopologyDomainCheck

:   Tests the following configuration:

    -   No IdM server is disconnected from the topology.
    -   The IdM servers do not have more than the recommended number of replication agreements.

    If the test succeeds, the test returns the configured domains. Otherwise, specific connection errors are reported.

    Note

    The test runs the `ipa topologysuffix-verify`{.literal} command for the `domain`{.literal} suffix. It also runs the command for the `ca`{.literal} suffix if the IdM Certificate Authority server role is configured on this server.

ReplicationConflictCheck
:   Searches for entries in LDAP matching `(&(!(objectclass=nstombstone))(nsds5ReplConflict=*))`{.literal}.

### [7.2. Screening replication by using Healthcheck](#screening-replication-by-using-healthcheck) {#screening-replication-by-using-healthcheck .title}

Run focused assessments to identify replication problems before they cause production outages.

You can run a standalone manual test to check the replication and topology configuration of your Identity Management (IdM) server by using the Healthcheck tool.

**Prerequisites**

-   You have `root`{.literal} privileges.

**Procedure**

-   To run the replication test, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source=ipahealthcheck.ds.replication --source=ipahealthcheck.ipa.topology
    ```

    The `--source=ipahealthcheck.ds.replication`{.literal} and `--source=ipahealthcheck.ipa.topology`{.literal} options ensure that IdM Healthcheck only performs the replication conflict and topology tests.

    Four different results are possible:

    -   `SUCCESS`{.literal} --- the test passed successfully.

        ``` {.language-plaintext tabindex="-1"}
        {
          "source": "ipahealthcheck.ipa.topology",
          "check": "IPATopologyDomainCheck",
          "result": "SUCCESS",
          "kw": {
            "suffix": "domain"
          }
        }
        ```

    -   `WARNING`{.literal} --- the test passed but there might be a problem.

    -   `ERROR`{.literal} --- the test failed.

        ``` {.language-plaintext tabindex="-1"}
        {
          "source": "ipahealthcheck.ipa.topology",
          "check": "IPATopologyDomainCheck",
          "result": "ERROR",
          "uuid": d6ce3332-92da-423d-9818-e79f49ed321f
          "when": 20191007115449Z
          "duration": 0.005943
          "kw": {
            "msg": "topologysuffix-verify domain failed, server2 is not connected (server2_139664377356472 in MainThread)"
          }
        }
        ```

    -   `CRITICAL`{.literal} --- the test failed and it affects the IdM server functionality.

    Note

    Run these tests on all IdM servers when trying to check for issues.

**Additional resources**

-   [Solving common replication problems](https://docs.redhat.com/en/documentation/red_hat_directory_server/13/html/configuring_and_managing_replication/solving-common-replication-problems)

### [7.3. Additional resources](#checking-idm-replication-by-using-healthcheck_73-additional-resources) {#additional-resources-1 .title}

-   [Healthcheck in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_idm_healthcheck_to_monitor_your_idm_environment/installing-and-running-the-idm-healthcheck-tool#healthcheck-in-idm)

## [Chapter 8. Verifying your IdM and AD trust configuration by using IdM Healthcheck](#verifying-your-idm-and-ad-trust-configuration-by-using-idm-healthcheck) {#chapter-8.-verifying-your-idm-and-ad-trust-configuration-by-using-idm-healthcheck .title}

You can identify issues with a trust between Identity Management (IdM) and Active Directory (AD) by using the Healthcheck tool.

### [8.1. IdM and AD trust Healthcheck tests](#idm-and-ad-trust-healthcheck-tests) {#idm-and-ad-trust-healthcheck-tests .title}

The Healthcheck tool includes several tests for testing the status of the trust between Identity Management (IdM) and Active Directory (AD).

To see all trust tests, run `ipa-healthcheck`{.literal} with the `--list-sources`{.literal} option:

``` {.language-plaintext tabindex="-1"}
# ipa-healthcheck --list-sources
```

You can find all trust-related tests under the `ipahealthcheck.ipa.trust`{.literal} source:

IPATrustAgentCheck
:   This test checks the SSSD configuration if the current host is configured as a trust agent. For each domain in `/etc/sssd/sssd.conf`{.literal} where `id_provider=ipa`{.literal} ensure that `ipa_server_mode`{.literal} is `True`{.literal}.

IPATrustDomainsCheck
:   This test checks if the trust domains match SSSD domains by comparing the list of domains in `sssctl domain-list`{.literal} with the list of domains from `ipa trust-find`{.literal} excluding the IdM domain.

IPATrustCatalogCheck

:   This test resolves an AD user, `Administrator@REALM`{.literal}. This populates the AD Global catalog and AD Domain Controller values in `sssctl domain-status`{.literal} output.

    For each trust domain look up the user with the ID of the SID + 500, that is the administrator ID, and then check the output of `sssctl domain-status <domain> --active-server`{.literal} to ensure that the domain is active.

IPAsidgenpluginCheck
:   This test verifies that the `sidgen`{.literal} plugin is enabled in the IdM 389-ds instance. The test also verifies that the `IPA SIDGEN`{.literal} and `ipa-sidgen-task`{.literal} plugins in `cn=plugins,cn=config`{.literal} include the `nsslapd-pluginEnabled`{.literal} option.

IPATrustAgentMemberCheck
:   This test verifies that the current host is a member of `cn=adtrust agents,cn=sysaccounts,cn=etc,SUFFIX`{.literal}.

IPATrustControllerPrincipalCheck
:   This test verifies that the current host is a member of `cn=adtrust agents,cn=sysaccounts,cn=etc,SUFFIX`{.literal}.

IPATrustControllerServiceCheck
:   This test verifies that the current host starts the ADTRUST service in ipactl.

IPATrustControllerConfCheck
:   This test verifies that `ldapi`{.literal} is enabled for the passdb backend in the output of `net conf`{.literal} list.

IPATrustControllerGroupSIDCheck
:   This test verifies that the `admins`{.literal} group's SID ends with 512, which is the Domain Admins\' RID.

IPATrustPackageCheck
:   This test verifies that the `trust-ad`{.literal} package is installed if the trust controller and AD trust are not enabled.

### [8.2. Screening the trust with the Healthcheck tool](#screening-the-trust-with-the-healthcheck-tool) {#screening-the-trust-with-the-healthcheck-tool .title}

You can run a standalone manual test of an Identity Management (IdM) and Active Directory (AD) trust health check by using the Healthcheck tool.

**Procedure**

-   To run the trust test, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source=ipahealthcheck.ipa.trust
    ```

    The `--source=ipahealthcheck.ipa.trust`{.literal} option ensures that IdM Healthcheck only performs the trust tests.

    A successful test displays empty brackets:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source=ipahealthcheck.ipa.trust
    ```

    ``` {.language-plaintext tabindex="-1"}
    []
    ```

    Note

    Run these tests on all IdM servers when trying to find an issue.

**Additional resources**

-   [Healthcheck in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_idm_healthcheck_to_monitor_your_idm_environment/installing-and-running-the-idm-healthcheck-tool#healthcheck-in-idm)

## [Chapter 9. Verifying system certificates by using IdM Healthcheck](#verifying-system-certificates-by-using-idm-healthcheck) {#chapter-9.-verifying-system-certificates-by-using-idm-healthcheck .title}

You can identify issues with system certificates on an Identity Management (IdM) server by using the Healthcheck tool.

### [9.1. System certificates Healthcheck tests](#system-certificates-healthcheck-tests) {#system-certificates-healthcheck-tests .title}

The Healthcheck tool includes several tests for verifying system, or Dogtag, certificates.

You can find all certificate-related tests under the `ipahealthcheck.dogtag.ca`{.literal} source in the output of the `ipa-healthcheck --list-sources`{.literal} command.

DogtagCertsConfigCheck

:   This test compares the CA (Certificate Authority) certificates in its NSS database to the same values stored in `CS.cfg`{.literal}. If they do not match, the CA fails to start.

    Specifically, it checks:

    -   `auditSigningCert cert-pki-ca`{.literal} against `ca.audit_signing.cert`{.literal}
    -   `ocspSigningCert cert-pki-ca`{.literal} against `ca.ocsp_signing.cert`{.literal}
    -   `caSigningCert cert-pki-ca`{.literal} against `ca.signing.cert`{.literal}
    -   `subsystemCert cert-pki-ca`{.literal} against `ca.subsystem.cert`{.literal}
    -   `Server-Cert cert-pki-ca`{.literal} against `ca.sslserver.cert`{.literal}

    If Key Recovery Authority (KRA) is installed, it also checks:

    -   `transportCert cert-pki-kra`{.literal} against `ca.connector.KRA.transportCert`{.literal}

DogtagCertsConnectivityCheck

:   This test verifies connectivity. This test is equivalent to the `ipa cert-show 1`{.literal} command which checks the following:

    -   The PKI proxy configuration in Apache
    -   IdM being able to find a CA
    -   The RA agent client certificate
    -   The correctness of CA replies to requests

    The test verifies that the `ipa cert-show`{.literal} command can be executed and that an expected response is returned from the IdM CA - either the certificate itself or a `not found`{.literal} response.

### [9.2. Screening system certificates by using Healthcheck](#screening-system-certificates-by-using-healthcheck) {#screening-system-certificates-by-using-healthcheck .title}

You can run a standalone manual test to check system certificates on an Identity Management (IdM) server by using the Healthcheck tool.

**Procedure**

-   To run the system certificates test, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source=ipahealthcheck.dogtag.ca
    ```

    The `--source=ipahealthcheck.dogtag.ca`{.literal} option ensures that Healthcheck only performs the certificate tests.

    An example of a successful test:

    ``` {.language-plaintext tabindex="-1"}
    {
      "source: ipahealthcheck.dogtag.ca",
      "check: DogtagCertsConfigCheck",
      "result: SUCCESS",
      "uuid: 9b366200-9ec8-4bd9-bb5e-9a280c803a9c",
      "when: 20191008135826Z",
      "duration: 0.252280",
      "kw:" {
        "key": "Server-Cert cert-pki-ca",
        "configfile":  "/var/lib/pki/pki-tomcat/conf/ca/CS.cfg"
        }
    }
    ```

    An example of a failed test:

    ``` {.language-plaintext tabindex="-1"}
    {
      "source: ipahealthcheck.dogtag.ca",
      "check: DogtagCertsConfigCheck",
      "result: CRITICAL",
      "uuid: 59d66200-1447-4b3b-be01-89810c803a98",
      "when: 20191008135912Z",
      "duration: 0.002022",
      "kw:" {
        "exception": "NSDB /etc/pki/pki-tomcat/alias not initialized",
        }
    }
    ```

    Note

    Run the certificate tests on all IdM servers when trying to find an issue.

**Additional resources**

-   [Healthcheck in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_idm_healthcheck_to_monitor_your_idm_environment/installing-and-running-the-idm-healthcheck-tool#healthcheck-in-idm)

## [Chapter 10. Verifying certificates by using IdM Healthcheck](#verifying-certificates-by-using-idm-healthcheck) {#chapter-10.-verifying-certificates-by-using-idm-healthcheck .title}

You can identify issues with certificates maintained by the `certmonger`{.literal} utility on an Identity Management (IdM) server by using the Healthcheck tool.

### [10.1. IdM certificates Healthcheck tests](#idm-certificates-healthcheck-tests) {#idm-certificates-healthcheck-tests .title}

The Healthcheck tool includes several tests for verifying the status of certificates maintained by `certmonger`{.literal} in Identity Management (IdM).

This suite of tests checks certificate expiration, validation, trust, and other configuration. Healthcheck can report multiple errors for the same underlying issue.

You can find these certificate tests under the `ipahealthcheck.ipa.certs`{.literal} source in the output of the `ipa-healthcheck --list-sources`{.literal} command.

IPACertmongerExpirationCheck

:   This test checks expirations in `certmonger`{.literal}.

    If an error is reported, the certificate has expired.

    If a warning appears, the certificate expires soon. By default, a warning appears if the test is run 28 days or fewer before certificate expiration.

    You can configure the number of days in the `/etc/ipahealthcheck/ipahealthcheck.conf`{.literal} file. After opening the file, change the `cert_expiration_days`{.literal} option located in the `default`{.literal} section.

    Note

    `Certmonger`{.literal} loads and maintains its own view of the certificate expiration. This check does not validate the on-disk certificate.

IPACertfileExpirationCheck

:   This test checks if the certificate file or NSS database have correct access rights configured. This test also checks expiration. Therefore, carefully read the `msg`{.literal} attribute in the error or warning output. The message specifies the problem.

    Note

    This test checks the on-disk certificate. If a certificate is missing or unreadable, Healthcheck returns an error.

IPACertNSSTrust
:   This test analyzes the trust for certificates stored in the NSS databases. For the expected tracked certificates in the NSS databases, Healthcheck compares the trust to an expected value and raises an error on a non-match.

IPANSSChainValidation
:   This test validates the certificate chain of the NSS certificates. The test executes the `certutil -V -u V -e -d [dbdir] -n`{.literal} command.

IPAOpenSSLChainValidation

:   This test validates the certificate chain of the OpenSSL certificates. Specifically, Healthcheck executes the following OpenSSL command:

    ``` {.language-plaintext tabindex="-1"}
    openssl verify -verbose -show_chain -CAfile /etc/ipa/ca.crt [cert file]
    ```

IPARAAgent
:   This test compares the certificate on disk with the equivalent record in LDAP in `uid=ipara,ou=People,o=ipaca`{.literal}.

IPACertRevocation
:   This test verifies that certificates that are maintained by `certmonger`{.literal} have not been revoked.

IPACertmongerCA

:   This test verifies the `certmonger`{.literal} Certificate Authority (CA) configuration. IdM cannot issue certificates without a CA.

    `Certmonger`{.literal} maintains a set of CA helpers. A CA named `IPA`{.literal} issues certificates for hosts or services through IdM, authenticating as a host or user principal.

    There are also `dogtag-ipa-ca-renew-agent`{.literal} and `dogtag-ipa-ca-renew-agent-reuse`{.literal} that renew the CA subsystem certificates.

**Additional resources**

-   [Obtaining an IdM certificate for a service using certmonger](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_certificates_in_idm/obtaining-an-idm-certificate-for-a-service-using-certmonger-assembly)

### [10.2. Screening certificates by using the Healthcheck tool](#screening-certificates-by-using-the-healthcheck-tool) {#screening-certificates-by-using-the-healthcheck-tool .title}

You can run a standalone manual test to check certificates on an Identity Management (IdM) server by using the Healthcheck tool.

**Prerequisites**

-   You have `root`{.literal} privileges.

**Procedure**

-   To run the certificates test, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-healthcheck --source=ipahealthcheck.ipa.certs
    ```

    -   The `--source=ipahealthcheck.ipa.certs`{.literal} option ensures that IdM Healthcheck only performs the `certmonger`{.literal} certificate tests.

        A successful test displays empty brackets:

        ``` {.language-plaintext tabindex="-1"}
        []
        ```

        Failed test shows you the following output:

        ``` {.language-plaintext tabindex="-1"}
        {
          "source": "ipahealthcheck.ipa.certs",
          "check": "IPACertfileExpirationCheck",
          "result": "ERROR",
          "kw": {
            "key": 1234,
            "dbdir": "/path/to/nssdb",
            "error": [error],
            "msg": "Unable to open NSS database '/path/to/nssdb': [error]"
          }
        }
        ```

        This `IPACertfileExpirationCheck`{.literal} test failed on opening the NSS database.

    Note

    Run this suite of Healthcheck tests on all IdM servers when trying to check for issues.

**Additional resources**

-   [Healthcheck in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_idm_healthcheck_to_monitor_your_idm_environment/installing-and-running-the-idm-healthcheck-tool#healthcheck-in-idm)

## [Legal Notice](#idm140553447967296) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
