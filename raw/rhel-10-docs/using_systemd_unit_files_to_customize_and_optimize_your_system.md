---
{"title": "Using systemd unit files to customize and optimize your system", "guide": "using_systemd_unit_files_to_customize_and_optimize_your_system", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_systemd_unit_files_to_customize_and_optimize_your_system/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Using systemd unit files to customize and optimize your system {#using-systemd-unit-files-to-customize-and-optimize-your-system .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Optimize system performance and extend configuration with systemd {#optimize-system-performance-and-extend-configuration-with-systemd .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140461332442464)

**Abstract**

Modify the systemd unit files and extend the default configuration, examine the system boot performance and optimize systemd to shorten the boot time.

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

## [Chapter 1. Working with systemd unit files](#working-with-systemd-unit-files) {#chapter-1.-working-with-systemd-unit-files .title}

To perform tasks for managing your system resources, you need to configure the `systemd`{.literal} unit files. With unit files, you can create custom unit files, modify existing unit files, and work with instantiated units.

### [1.1. Introduction to unit files](#introduction-to-unit-files) {#introduction-to-unit-files .title}

To manage units and their resources, you can use unit files. Several `systemctl`{.literal} commands work with unit files in the background. A unit file is the `.service`{.literal} or `.target`{.literal} file on your hard drive. This unit file has configuration directives to describe the unit and define its properties.

The basic object that systemd manages is a `systemd`{.literal} unit, a representation of system resources and services. A `systemd`{.literal} unit consists of a name, type and a configuration file that defines and manages a particular task. You can use unit files to configure system behavior. Examples of various `systemd`{.literal} unit types are as follows:

-   **Service** : Controls and manages individual system services.
-   **Target** : Represents a group of units that define system states.
-   **Device** : Manages hardware devices and their availability.
-   **Mount** : Handles file system mounting.
-   **Timer** : Schedules tasks to run at specific intervals.

You can edit or create unit files manually. Three main directories contain unit files on the system:

-   `/usr/lib/systemd/system/`{.literal} - `systemd`{.literal} unit files distributed with installed RPM packages.
-   `/run/systemd/system/`{.literal} - `systemd`{.literal} unit files created at run time.
-   `/etc/systemd/system/`{.literal} - `systemd`{.literal} unit files created by using the `systemctl enable`{.literal} command and unit files added for extending a service.

The `/etc/systemd/system/`{.literal} directory is reserved for unit files created or customized by a system administrator.

Unit file naming convention is as follows:

``` {.language-plaintext tabindex="-1"}
<unit_name>.<type_extension>
```

In this example, *\<unit_name\>* stands for the name of the unit and *\<type_extension\>* identifies the unit type. For example, you can find `sshd.service`{.literal} and `sshd.socket`{.literal} units present on your system.

For additional configurations, you can use systemd drop-in files.

-   Create the `sshd.service.d/`{.literal} directory and edit the `custom.conf`{.literal} file.

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p /etc/systemd/system/sshd.service.d
    ```

-   Create a drop-in file:

    ``` {.language-plaintext tabindex="-1"}
    # touch /etc/systemd/system/sshd.service.d/custom.conf
    ```

-   Edit the service with the `custom.conf`{.literal} drop-in file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl edit sshd.service
    ```

    The `systemctl edit`{.literal} command opens the `sshd.service`{.literal} unit file in the default text editor.

-   You can add additional directives to the file. For example, to add a custom configuration option to `sshd.service`{.literal}, add the following line to the file:

    ``` {.language-plaintext tabindex="-1"}
    [Service]
    ExecStart=
    ExecStart=/usr/sbin/sshd -D -f /etc/ssh/sshd_config.custom
    ```

The system uses systemd to manage the `sshd.service`{.literal} dependencies through the directories `/etc/systemd/system/sshd.service.wants/`{.literal} and `/etc/systemd/system/sshd.service.requires/`{.literal}. These directories are for symlinks to other services that the SSH daemon needs or wants to start. While systemd does not create these directories directly, you can use the `systemctl enable `{.literal}*`<service>`{.literal}* command to automatically add the necessary links. `systemd`{.literal} creates the symbolic links automatically either during installation according to the `[Install]`{.literal} section options or at runtime based on the `[Unit]`{.literal} section options from the unit file.

With unit specifiers, you can set many unit file options. Unit specifiers are wildcard strings that the system dynamically replaces with unit parameters when it loads the unit file. This feature enables you to create unit files that serve as templates for generating instantiated units.

**Additional resources**

-   [Modifying existing unit files](#modifying-existing-unit-files "1.12. Modifying existing unit files")
-   [Working with instantiated units](#working-with-instantiated-units "1.17. Working with instantiated units")

### [1.2. Systemd unit files locations](#systemd-unit-files-locations) {#systemd-unit-files-locations .title}

You can find the unit configuration files in the mentioned directories.

+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Directory                            | Description                                                                                                                                                                                                        |
+:=====================================+:===================================================================================================================================================================================================================+
| `/usr/lib/systemd/system/`{.literal} | `systemd`{.literal} unit files distributed with installed RPM packages.                                                                                                                                            |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/run/systemd/system/`{.literal}     | `systemd`{.literal} unit files created at run time. This directory takes precedence over the directory with installed service unit files.                                                                          |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/systemd/system/`{.literal}     | `systemd`{.literal} unit files created by using the `systemctl enable`{.literal} command and unit files added for extending a service. This directory takes precedence over the directory with runtime unit files. |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.1. systemd unit files locations

Show more

The default configuration of `systemd`{.literal} is defined during the compilation and you can find the configuration in the `/etc/systemd/system.conf`{.literal} file. By editing this file, you can modify the default configuration by overriding values for `systemd`{.literal} units globally.

For example, to override the default value of the timeout limit 90 seconds, use the `DefaultTimeoutStartSec`{.literal} parameter to input the required value in seconds:

``` {.language-plaintext tabindex="-1"}
DefaultTimeoutStartSec=_required value_
```

### [1.3. Unit file structure](#unit-file-structure) {#unit-file-structure .title}

Unit files consist of three main sections that define unit behavior, type-specific directives, and installation information. Understanding this structure helps you to create and change systemd units effectively.

`[Unit]`{.literal} section
:   Contains generic options that do not depend on the type of the unit. These options provide a unit description, specify the unit's behavior, and set dependencies to other units.

\[\<unit_type\>\] section
:   Contains type-specific directives, which are grouped under a section named after the unit type. For example, service unit files contain the `[Service]`{.literal} section.

`[Install]`{.literal} section
:   Contains information about unit installation that the `systemctl enable`{.literal} and `systemctl disable`{.literal} commands use.

**Additional resources**

-   [Important \[Unit\] section options](#important-unit-section-options "1.4. Important [Unit] section options")
-   [Important \[Service\] section options](#important-service-section-options "1.5. Important [Service] section options")
-   [Important \[Install\] section options](#important-install-section-options "1.6. Important [Install] section options")

### [1.4. Important \[Unit\] section options](#important-unit-section-options) {#important-unit-section-options .title}

The \[Unit\] section has generic options that are not dependent on the type of the unit. These options have a unit description, specify the unit's behavior, and set dependencies to other units.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option [^\[a\]^](#ftn.idm140461329842000)                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                       |
+:==========================================================================================================================================================================================================================================================================================================================================================================================================================+:==================================================================================================================================================================================================================================================================================================================+
| `Description`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                   | A meaningful description of the unit. This text is displayed for example in the output of the `systemctl status`{.literal} command.                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Documentation`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                 | Provides a list of URIs referencing documentation for the unit.                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `After`{.literal}[^\[b\]^](#ftn.idm140461334462752)                                                                                                                                                                                                                                                                                                                                                                       | Defines the order in which units are started. The unit starts only after the units specified in `After`{.literal} are active. Unlike `Requires`{.literal}, `After`{.literal} does not explicitly activate the specified units. The `Before`{.literal} option has the opposite functionality to `After`{.literal}. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Requires`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                      | Configures dependencies on other units. The units listed in `Requires`{.literal} are activated together with the unit. If any of the required units fail to start, the unit is not activated.                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Wants`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                         | Configures weaker dependencies than `Requires`{.literal}. If any of the listed units does not start successfully, it has no impact on the unit activation. This is the suggested way to establish custom unit dependencies.                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Conflicts`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                     | Configures negative dependencies, an opposite to `Requires`{.literal}.                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [^\[a\]^](#idm140461329842000) For a complete list of options configurable in the \[Unit\] section, see the `systemd.unit(5)`{.literal} manual page.                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                   |
| [^\[b\]^](#idm140461334462752) In most cases, it is sufficient to set only the ordering dependencies with `After`{.literal} and `Before`{.literal} unit file options. If you also set a requirement dependency with `Wants`{.literal} (suggested) or `Requires`{.literal}, the ordering dependency still needs to be specified. That is because ordering and requirement dependencies work independently from each other. |                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.2. Important \[Unit\] section options

Show more

### [1.5. Important \[Service\] section options](#important-service-section-options) {#important-service-section-options .title}

To manage configuration parameters that define how the service operates and interacts with the system, use the `[Service]`{.literal} section. Each systemd service unit has a `[Service]`{.literal} section that includes directives for this unit type.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option [^\[a\]^](#ftn.idm140461330925088)                                                                                                                         | Description                                                                                                                                                                                                                                                                                  |
+:==================================================================================================================================================================+:=============================================================================================================================================================================================================================================================================================+
| `Type`{.literal}                                                                                                                                                  | Configures the unit process startup type that affects the functionality of `ExecStart`{.literal} and related options. One of:                                                                                                                                                                |
|                                                                                                                                                                   |                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                   | -   `simple`{.literal}: The default value. The process started with `ExecStart`{.literal} is the main process of the service.                                                                                                                                                                |
|                                                                                                                                                                   | -   `forking`{.literal} : The process started with `ExecStart`{.literal} spawns a child process that becomes the main process of the service. The parent process exits when the startup is complete.                                                                                         |
|                                                                                                                                                                   | -   `oneshot`{.literal} : This type is similar to `simple`{.literal}, but the process exits before starting consequent units.                                                                                                                                                                |
|                                                                                                                                                                   | -   `dbus`{.literal} : This type is similar to `simple`{.literal}, but consequent units start only after the main process gains a D-Bus name.                                                                                                                                                |
|                                                                                                                                                                   | -   `notify`{.literal} : This type is similar to `simple`{.literal}, but consequent units start only after the main process sends a notification message by using the `sd_notify()`{.literal} function.                                                                                      |
|                                                                                                                                                                   | -   `idle`{.literal} : Similar to `simple`{.literal}, the system delays the actual execution of the service binary until all jobs finish. This avoids mixing the status output with the standard output of services.                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ExecStart`{.literal}                                                                                                                                             | Specifies commands or scripts to run when the unit starts. `ExecStartPre`{.literal} and `ExecStartPost`{.literal} specify custom commands to run before and after `ExecStart`{.literal}. `Type=oneshot`{.literal} specifies multiple custom commands that the system then runs sequentially. |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ExecStop`{.literal}                                                                                                                                              | Specifies commands or scripts to run when the unit stops.                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ExecReload`{.literal}                                                                                                                                            | Specifies commands or scripts to run when the unit reloads.                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Restart`{.literal}                                                                                                                                               | Restarts the service after its process exits, with the exception of a clean stop by the `systemctl`{.literal} command.                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `RemainAfterExit`{.literal}                                                                                                                                       | Keeps the service active even when all its processes exit. Default is False. This option is especially useful if you configure `Type=oneshot`{.literal}.                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [^\[a\]^](#idm140461330925088) For a complete list of options configurable in the `[Service]`{.literal} section, see the `systemd.service(5)`{.literal} man page. |                                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.3. Important \[Service\] section options

Show more

### [1.6. Important \[Install\] section options](#important-install-section-options) {#important-install-section-options .title}

The \[Install\] section has information about unit installation used by `systemctl enable`{.literal} and `disable`{.literal} commands.

+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option [^\[a\]^](#ftn.idm140461329146704)                                                                                                               | Description                                                                                                                                                                                                               |
+:========================================================================================================================================================+:==========================================================================================================================================================================================================================+
| `Alias`{.literal}                                                                                                                                       | Provides a space-separated list of additional names for the unit. Most `systemctl`{.literal} commands, excluding `systemctl enable`{.literal}, can use aliases instead of the actual unit name.                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `RequiredBy`{.literal}                                                                                                                                  | A list of units that depend on the unit. When this unit is enabled, the units listed in `RequiredBy`{.literal} gain a `Require`{.literal} dependency on the unit.                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `WantedBy`{.literal}                                                                                                                                    | A list of units that weakly depend on the unit. When this unit is enabled, the units listed in `WantedBy`{.literal} gain a `Want`{.literal} dependency on the unit.                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Also`{.literal}                                                                                                                                        | Specifies a list of units to be installed or uninstalled along with the unit.                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `DefaultInstance`{.literal}                                                                                                                             | Limited to instantiated units, this option specifies the default instance for which the unit is enabled. See [Working with instantiated units](#working-with-instantiated-units "1.17. Working with instantiated units"). |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [^\[a\]^](#idm140461329146704) For a complete list of options configurable in the \[Install\] section, see the `systemd.unit(5)`{.literal} manual page. |                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.4. Important \[Install\] section options

Show more

### [1.7. Creating custom unit files](#creating-custom-unit-files) {#creating-custom-unit-files .title}

To modify properties of an existing unit or create a new unit from scratch, you need to create custom unit files.

You could run a custom daemon or create a second instance of some existing service. For details, see [creating a custom unit file by using the second instance of the sshd service](#creating-a-custom-unit-file-by-using-the-second-instance-of-the-sshd-service "1.8. Creating a custom unit file by using the second instance of the sshd service").

However, to modify or extend the properties of an existing unit, use the instructions from [Modifying existing unit files](#modifying-existing-unit-files "1.12. Modifying existing unit files").

**Prerequisites**

-   To create a custom service, prepare the executable file with the service. The file can contain a custom-created script, or an executable delivered by a software provider.
-   To manage custom services, prepare a PID file to hold a constant PID for the main process of the custom service. You can also include environment files to store shell variables for the service. Make sure the source script is executable (by executing the `chmod a+x`{.literal}) and is not interactive.
-   You have administrative privileges.

**Procedure**

1.  Create a unit file in the `/etc/systemd/system/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # touch /etc/systemd/system/<name>.service
    ```

2.  Apply the read-only permission to the unit file:

    ``` {.language-plaintext tabindex="-1"}
    # chmod 664 /etc/systemd/system/<name>.service
    ```

    Replace *\<name\>* with a name of the service you want to create.

3.  Open the created *`<name>`{.literal}*`.service`{.literal} file, and add the service configuration options. You can use various options depending on the type of service you need to create, see [unit file structure](#unit-file-structure "1.3. Unit file structure").

    The following is an example unit configuration for a network-related service:

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Description=<service_description>
    After=network.target

    [Service]
    ExecStart=<path_to_executable>
    Type=forking
    PIDFile=<path_to_pidfile>

    [Install]
    WantedBy=default.target
    ```

    -   *\<service_description\>* is an informative description that is displayed in journal log files and in the output of the `systemctl status`{.literal} command.
    -   The `After`{.literal} setting ensures that the service is started only after the network is running. Add a space-separated list of other relevant services or targets.
    -   *path_to_executable* stands for the path to the actual service executable.
    -   `Type=forking`{.literal} is used for daemons that make the fork system call. The main process of the service is created with the PID specified in *path_to_pidfile*. Find other startup types in [important \[Service\] section options](#important-service-section-options "1.5. Important [Service] section options").
    -   `WantedBy`{.literal} states the target or targets that the service should be started under. Think of these targets as a replacement of the older concept of runlevels.

4.  Notify `systemd`{.literal} that a new *`<name>`{.literal}*`.service`{.literal} file exists:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start <name>.service
    ```

    Important

    Always run the `systemctl daemon-reload`{.literal} command after creating new unit files or modifying existing unit files. Otherwise, `systemctl start`{.literal} or `systemctl enable`{.literal} might fail due to mismatched systemd and service unit file states on disk. Systems with a large number of units can take a long time to reload. This is because the state of each unit is serialized and subsequently deserialized during the reload.

### [1.8. Creating a custom unit file by using the second instance of the sshd service](#creating-a-custom-unit-file-by-using-the-second-instance-of-the-sshd-service) {#creating-a-custom-unit-file-by-using-the-second-instance-of-the-sshd-service .title}

To configure and run multiple instances of a service, you can create copies of the original service configuration files. Then, modify certain parameters to avoid conflicts with the primary instance of the service.

**Prerequisites**

-   You have administrative privileges.
-   You have installed the `sshd`{.literal} service.

**Procedure**

1.  Create a copy of the `sshd_config`{.literal} file that the second daemon will use:

    ``` {.language-plaintext tabindex="-1"}
    # cp /etc/ssh/sshd_config /etc/ssh/sshd-second_config
    ```

2.  Edit the `sshd-second_config`{.literal} file to assign a different port number and process identifier (PID) file to the second daemon:

    ``` {.language-plaintext tabindex="-1"}
    Port 22220
    PidFile /var/run/sshd-second.pid
    ```

    See the `sshd_config (5)`{.literal} man page for `Port`{.literal} and `PidFile`{.literal} options. Make sure the requested port is not in use by any other service. The PID file does not have to exist before running the service, it is generated automatically on service start.

3.  Create a copy of the `systemd`{.literal} unit file for the `sshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # cp /usr/lib/systemd/system/sshd.service /etc/systemd/system/sshd-second.service
    ```

4.  Edit the created `sshd-second.service`{.literal} file:

    a.  Modify the `Description`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        # vi /etc/systemd/system/sshd-second.service
        ```

        ``` {.language-plaintext tabindex="-1"}
        Description=OpenSSH server second instance daemon
        ```

    b.  Add `sshd.service`{.literal} to services specified in the `After`{.literal} option, so that the second instance starts only after the first one has already started:

        ``` {.language-plaintext tabindex="-1"}
        After=syslog.target network.target auditd.service sshd.service
        ```

    c.  Remove the `ExecStartPre=/usr/sbin/sshd-keygen`{.literal} line, the first instance of `sshd`{.literal} includes key generation.

    d.  Add the `-f /etc/ssh/sshd-second_config`{.literal} parameter to the `sshd`{.literal} command, so that the alternative configuration file is used:

        ``` {.language-plaintext tabindex="-1"}
        ExecStart=/usr/sbin/sshd -D -f /etc/ssh/sshd-second_config $OPTIONS
        ```

    e.  After the modifications, the `sshd-second.service`{.literal} unit file contains the following settings:

        ``` {.language-plaintext tabindex="-1"}
        [Unit]
        Description=OpenSSH server second instance daemon
        After=syslog.target network.target auditd.service sshd.service

        [Service]
        EnvironmentFile=/etc/sysconfig/sshd
        ExecStart=/usr/sbin/sshd -D -f /etc/ssh/sshd-second_config $OPTIONS
        ExecReload=/bin/kill -HUP $MAINPID
        KillMode=process
        Restart=on-failure
        RestartSec=42s

        [Install]
        WantedBy=multi-user.target
        ```

5.  If using SELinux, add the port for the second instance of `sshd`{.literal} to SSH ports:

    ``` {.language-plaintext tabindex="-1"}
    # semanage port -a -t ssh_port_t -p tcp 22220
    ```

    Otherwise, the second instance of `sshd`{.literal} will be rejected to bind to the port.

6.  Enable `sshd-second.service`{.literal} to start automatically on boot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now sshd-second.service
    ```

**Verification**

1.  Verify if the `sshd-second.service`{.literal} is running by using the `systemctl status`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status sshd-second.service
    ```

2.  Verify if the port is enabled by connecting to the second instance of `sshd`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -p 22220 user@server
    ```

    Make sure you configure the firewall to allow connections to the second instance of `sshd`{.literal}.

### [1.9. Finding the systemd service descriptions and dependencies](#finding-the-systemd-service-descriptions-and-dependencies) {#finding-the-systemd-service-descriptions-and-dependencies .title}

To discover the service descriptions and dependencies, you can use the `systemctl show `{.literal}*`<example_service_name>`{.literal}* command. You can also list the dependencies by using the `systemctl list-dependencies `{.literal}*`<example_service_name>`{.literal}* command.

To find the description of the service, you can use the line starting with **#description**. Use this description together with the service name in the `Description`{.literal} option in the `[Unit]`{.literal} section of the unit file. The header might contain similar data on the **#Short-Description** and **#Description** lines.

To find the dependencies of the service, you can use the Linux standard base (LSB) header. It might contain several directives that form dependencies between services.

``` {.language-plaintext tabindex="-1"}
# grep -i "Required-Start\|Required-Stop\|Default-Start\|Default-Stop" /etc/init.d/<example_service_name>
```

Most of them are translatable to systemd unit options, see the following table:

+---------------------------------------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LSB Option                                        | Equivalent Unit File                  | Description                                                                                                                                                                                                                                                                                                                                                         |
+:==================================================+:======================================+:====================================================================================================================================================================================================================================================================================================================================================================+
| `Required-Stop`{.literal},`Should-Stop`{.literal} | `Conflicts`{.literal}                 | Include negative dependencies.                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Provides`{.literal}                              | `-`{.literal}                         | Specifies the boot facility name of the service, that can be referenced in other init scripts (with the \"\$\" prefix). This is no longer needed as unit files refer to other units by their file names.                                                                                                                                                            |
+---------------------------------------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Required-Start`{.literal}                        | `After`{.literal}, `Before`{.literal} | Includes boot facility names of required services. This is translated as an ordering dependency, boot facility names are replaced with unit file names of corresponding services or targets they belong to. For example, in case of `myservice`{.literal}, the Required-Start dependency on **\$network** was translated to the After dependency on network.target. |
+---------------------------------------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Should-Start`{.literal}                          | `After`{.literal}, `Before`{.literal} | Includes weaker dependencies than Required-Start. Failed Should-Start dependencies do not affect the service startup.                                                                                                                                                                                                                                               |
+---------------------------------------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.5. Dependency options from the LSB header

Show more

### [1.10. Finding default targets of the service](#finding-default-targets-of-the-service) {#finding-default-targets-of-the-service .title}

You need to define the default systemd targets in which a service should start. In SysV init scripts, check for lines such as **#chkconfig** or **#Default-Start** in the service script or Linux Standard Base (LSB) header.

The runlevels correspond to default systemd targets. In systemd, runlevels 2, 3, and 5 map to multi-user.target and graphical.target. The runlevel 4 maps to a custom or user defined target. Specify these targets in the `WantedBy`{.literal} option in the `[Install]`{.literal} section of your unit file to control when the service starts by default. Because graphical.target depends on multi-user.target, you can also specify only graphical.target for services meant to run in a graphical environment. Also, examine **#Default-Stop** to identify targets to stop the service by default. The other two values specified on the **#chkconfig** line represent startup and shutdown priorities of the init script. These values are interpreted by systemd if it loads the init script, but there is no unit file equivalent.

### [1.11. Finding files used by the service](#finding-files-used-by-the-service) {#finding-files-used-by-the-service .title}

You need to review the init script or systemd unit file to find files used by a service. Look for references of configuration files, environment files, PID files, and executables in the init script or systemd unit file.

-   In traditional init scripts, check for lines that load function libraries, source configuration files, or specify environment and PID files. It is often mentioned as `#config`{.literal} and `#pidfile`{.literal} in the header.
-   In systemd unit files, check options such as `EnvironmentFile=`{.literal} for environment configurations and `PIDFile=`{.literal} for PID files. The `ExecStart=`{.literal}, `ExecStartPre=`{.literal}, and other related directives show executables or scripts the service calls.
-   Additionally, review paths and filenames mentioned in these scripts and directives to identify all files that the service uses during its operation.

The init script header does not include the path to the executable program and other dependent files required by the service. In previous versions of Red Hat Enterprise Linux, init scripts used a Bash case statement. This Bash statement defines the behavior of the service on default actions. It includes default actions such as **start**, **stop**, or **restart**, and custom-defined actions. The following excerpt from the `example_service`{.literal} init script shows the block of code executed at service start.

``` {.language-plaintext tabindex="-1"}
conf_check() {
    [ -x /usr/sbin/myservice ] || exit 5
    [ -d /etc/myservice ] || exit 6
    [ -d /var/spool/myservice ] || exit 5
}

make_aliasesdb() {
    if [ "$(/usr/sbin/postconf -h alias_database)" == "hash:/etc/aliases" ]
    then
        # /etc/aliases.db might be used by other MTA, make sure nothing
        # has touched it since our last newaliases call
        [ /etc/aliases -nt /etc/aliases.db ] ||
            [ "$ALIASESDB_STAMP" -nt /etc/aliases.db ] ||
            [ "$ALIASESDB_STAMP" -ot /etc/aliases.db ] || return
        /usr/bin/newaliases
        touch -r /etc/aliases.db "$ALIASESDB_STAMP"
    else
        /usr/bin/newaliases
    fi
}

start() {
    [ "$EUID" != "0" ] && exit 4
    # Check that networking is up.
    [ ${NETWORKING} = "no" ] && exit 1
    conf_check
    # Start daemons.
    echo -n $"Starting myservice: "
    make_aliasesdb >/dev/null 2>&1
    [ -x $CHROOT_UPDATE ] && $CHROOT_UPDATE
    /usr/sbin/myservice start 2>/dev/null 1>&2 && success || failure $"$prog start"
    RETVAL=$?
    [ $RETVAL -eq 0 ] && touch $lockfile
        echo
    return $RETVAL
}
```

The extensibility of the init script permits specifying two custom functions, `conf_check()`{.literal} and `make_aliasesdb()`{.literal} are called from the `start()`{.literal} function block. Several external files and directories are mentioned: the `/usr/sbin/myservice`{.literal} main executable program, the `/etc/myservice/`{.literal} and `/var/spool/myservice/`{.literal} configuration directories, and the `/usr/sbin/postconf/`{.literal} directory.

The `systemd`{.literal} unit file supports only the predefined actions, but enables executing custom executables with `ExecStart`{.literal}, `ExecStartPre`{.literal}, `ExecStartPost`{.literal}, `ExecStop`{.literal}, and `ExecReload`{.literal} options. The `/usr/sbin/myservice`{.literal} together with supporting scripts are executed on service start.

Converting complex init scripts requires understanding the purpose of every statement in the script. Some of the statements are specific to the operating system version, therefore you do not need to convert them. However, some adjustments required for the new environment, both in the unit file and in the executable program and supporting files.

### [1.12. Modifying existing unit files](#modifying-existing-unit-files) {#modifying-existing-unit-files .title}

To customize and optimize services without creating a new configuration from scratch, you can modify an existing unit file. If you want to modify existing unit files, proceed to the `/etc/systemd/system/`{.literal} directory.

Do not modify the unit files in the `/usr/lib/systemd/system/`{.literal} directory.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   Create a directory for supplementary configuration files at `/etc/systemd/system/`{.literal}*`<unit>`{.literal}*`.d/`{.literal}. You can extend the default configuration with additional functionality, while still referring to the original unit file. Changes to the default unit introduced with a package upgrade are therefore applied automatically. For details, see [extending the default unit configuration](#extending-the-default-unit-configuration "1.13. Extending the default unit configuration").

-   Create a copy of the original unit file from `/usr/lib/systemd/system/`{.literal} directory in the `/etc/systemd/system/`{.literal} directory and make changes there. The copy overrides the original file, therefore changes introduced with the package update are not applied. This method is useful for making significant unit changes that should persist regardless of package updates. For details, see [Overriding the default unit configuration](#overriding-the-default-unit-configuration "1.14. Overriding the default unit configuration").

    a.  To return to the default configuration of the unit, delete custom-created configuration files and the `/etc/systemd/system/`{.literal}*`<unit>`{.literal}*`.d/`{.literal} drop-in directory.

    b.  Apply changes to unit files:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl daemon-reload
        ```

        The `daemon-reload`{.literal} option reloads all unit files and recreates the entire dependency tree, which is needed to immediately apply any change to a unit file.

    c.  If the modified unit file belongs to a running service, restart the service:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart <name>.service
        ```

        Important

        To modify a service properties, such as dependencies or timeouts, that is handled by a SysV initscript, do not modify the initscript. Instead, create a `systemd`{.literal} drop-in configuration file for the service. For details, see [extending the default unit configuration](#extending-the-default-unit-configuration "1.13. Extending the default unit configuration") and [overriding the default unit configuration](#overriding-the-default-unit-configuration "1.14. Overriding the default unit configuration").

        To manage the service in the same way as a normal systemd service, create a new directory `/etc/systemd/system/network.service.d/`{.literal} and a systemd drop-in file `/etc/systemd/system/network.service.d/`{.literal}*`<example_config.conf>`{.literal}*. Then, put the modified values into the drop-in file.

        The `systemd`{.literal} service identifies the `network`{.literal} service as `network.service`{.literal}, so the created directory must be named as `network.service.d`{.literal}.

### [1.13. Extending the default unit configuration](#extending-the-default-unit-configuration) {#extending-the-default-unit-configuration .title}

To extend the default unit file with additional systemd configuration options, you can create a configuration directory in the `/etc/systemd/system/`{.literal} directory.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

1.  Create a configuration directory in `/etc/systemd/system/`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /etc/systemd/system/<name>.service.d/
    ```

    Replace *\<name\>* with the name of the service you want to extend. The syntax applies to all unit types.

2.  Create a configuration file with the `.conf`{.literal} suffix:

    ``` {.language-plaintext tabindex="-1"}
    # touch /etc/systemd/system/name.service.d/<config_name>.conf
    ```

    Replace *\<config_name\>* with the name of the configuration file. This file adheres to the normal unit file structure and you have to specify all directives in the appropriate sections. For details, see [Unit file structure](#unit-file-structure "1.3. Unit file structure").

    For example, to add a custom dependency, create a configuration file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Requires=<new_dependency>
    After=<new_dependency>
    ```

    The *\<new_dependency\>* stands for the unit to be marked as a dependency. Another example is a configuration file that restarts the service after its main process exited, with a delay of 30 seconds:

    ``` {.language-plaintext tabindex="-1"}
    [Service]
    Restart=always
    RestartSec=30
    ```

    Create small configuration files focused only on one task. Such files can be easily moved or linked to configuration directories of other services.

3.  Apply changes to the unit:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart <name>.service
    ```

4.  To automatically run a custom shell script when starting the Apache service, modify the `httpd.service`{.literal} unit.

    a.  Create a directory and a custom configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # mkdir /etc/systemd/system/httpd.service.d/
        ```

        ``` {.language-plaintext tabindex="-1"}
        # touch /etc/systemd/system/httpd.service.d/custom_script.conf
        ```

    b.  Specify the script you want to run after the main service process by inserting the following text to the `custom_script.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [Service]
        ExecStartPost=/usr/local/bin/custom.sh
        ```

    c.  Apply the unit changes::

        ``` {.language-plaintext tabindex="-1"}
        # systemctl daemon-reload
        ```

        ``` {.language-plaintext tabindex="-1"}
        # systemctl restart httpd.service
        ```

        Note

        The configuration files from the `/etc/systemd/system/`{.literal} configuration directories take precedence over unit files in `/usr/lib/systemd/system/`{.literal}. You need to specify an option, such as `Description`{.literal} or `ExecStart`{.literal}, only once in the configuration files. The value of this option overrides the default.

        In the output of the `systemd-delta`{.literal} command, units are described in [monitoring overridden units](#monitoring-overridden-units "1.16. Monitoring overridden units"). Such units are always marked as `[EXTENDED]`{.literal}, even though in some cases, certain options are actually overridden.

### [1.14. Overriding the default unit configuration](#overriding-the-default-unit-configuration) {#overriding-the-default-unit-configuration .title}

To make persistent changes to the unit file configuration when updating the package, override the default unit configuration.

When a package contains the default unit file configuration and the package is updated, the default configuration changes.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

1.  Copy the unit file to the `/etc/systemd/system/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # cp /usr/lib/systemd/system/<name>.service /etc/systemd/system/<name>.service
    ```

    Replace *\<name\>* with the name of the service you want to override.

2.  Open the copied file and make changes.

3.  Apply unit changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

4.  Restart the service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart <name>.service
    ```

### [1.15. Changing the timeout limit](#changing-the-timeout-limit) {#changing-the-timeout-limit .title}

To prevent a malfunctioning service from freezing the system, you can specify a timeout value per service. Otherwise, the default value for timeout is 90 seconds for normal services and 300 seconds for SysV-compatible services.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

1.  Edit the `httpd`{.literal} unit file:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl edit httpd
    ```

2.  Specify the `TimeoutStartSec`{.literal} value in the `[Service]`{.literal} section:

    ``` {.language-plaintext tabindex="-1"}
    ...
    [Service]
    ...
    PrivateTmp=true
    TimeoutStartSec=10

    [Install]
    WantedBy=multi-user.target
    ...
    ```

3.  Reload the `systemd`{.literal} daemon:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

**Verification**

-   Verify the new timeout value:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl show httpd -p TimeoutStartUSec
    ```

    Note

    To change the timeout limit globally, input the `DefaultTimeoutStartSec`{.literal} in the `/etc/systemd/system.conf`{.literal} file.

### [1.16. Monitoring overridden units](#monitoring-overridden-units) {#monitoring-overridden-units .title}

To monitor overridden or modified unit files, you can use the `systemd-delta`{.literal} command.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   Display an overview of overridden or modified unit files:

    ``` {.language-plaintext tabindex="-1"}
    # systemd-delta
    ```

    ``` {.language-plaintext tabindex="-1"}
    [EQUIVALENT] /etc/systemd/system/default.target → /usr/lib/systemd/system/default.target
    [OVERRIDDEN] /etc/systemd/system/autofs.service → /usr/lib/systemd/system/autofs.service

    --- /usr/lib/systemd/system/autofs.service      2014-10-16 21:30:39.000000000 -0400
    +++ /etc/systemd/system/autofs.service  2014-11-21 10:00:58.513568275 -0500
    @@ -8,7 +8,8 @@
     EnvironmentFile=-/etc/sysconfig/autofs
     ExecStart=/usr/sbin/automount $OPTIONS --pid-file /run/autofs.pid
     ExecReload=/usr/bin/kill -HUP $MAINPID
    -TimeoutSec=180
    +TimeoutSec=240
    +Restart=Always

     [Install]
     WantedBy=multi-user.target

    [MASKED]     /etc/systemd/system/cups.service → /usr/lib/systemd/system/cups.service
    [EXTENDED]   /usr/lib/systemd/system/sssd.service → /etc/systemd/system/sssd.service.d/journal.conf

    4 overridden configuration files found.
    ```

### [1.17. Working with instantiated units](#working-with-instantiated-units) {#working-with-instantiated-units .title}

You can simplify the management of multiple service instances by using a single systemd template configuration.

To manage multiple instances of a service, you can use a single template configuration. You can define a generic template, denoted by `@`{.literal}, for a unit and generate multiple unit instances with specific parameters at runtime. By using `Requires`{.literal} or `Wants`{.literal} options or the `systemctl start`{.literal} command, you can start instantiated units from another unit file.

``` {.language-plaintext tabindex="-1"}
<template_name>@<instance_name>.service
```

The *\<template_name\>* stands for the name of the template configuration file. Replace *\<instance_name\>* with the name for the unit instance. Several instances can point to the same template file with configuration options common for all instances of the unit. Template unit name has the form of:

``` {.language-plaintext tabindex="-1"}
<unit_name>@.service
```

For example, the following `Wants`{.literal} setting in a unit file:

``` {.language-plaintext tabindex="-1"}
Wants=getty@ttyA.service getty@ttyB.service
```

With this command, systemd searches for given service units. If no such units are found, the part between `@`{.literal} and the type suffix gets ignored. Systemd searches for the `getty@.service`{.literal} file, reads the configuration from it, and starts the services.

For example, the `getty@.service`{.literal} template has the following directives:

``` {.language-plaintext tabindex="-1"}
[Unit]
Description=Getty on %I
...
[Service]
ExecStart=-/sbin/agetty --noclear %I $TERM
...
```

When the `getty@ttyA.service`{.literal} and `getty@ttyB.service`{.literal} are instantiated from the `getty@.service`{.literal} template, `Description=Getty on %I`{.literal} is resolved as **Getty on ttyA** and **Getty on ttyB**.

### [1.18. Important unit specifiers](#important-unit-specifiers) {#important-unit-specifiers .title}

You can use the wildcard characters, called **unit specifiers**, in any unit configuration file. Unit specifiers substitute certain unit parameters and are interpreted at runtime.

+----------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Unit Specifier | Meaning           | Description                                                                                                                                                                                |
+:===============+:==================+:===========================================================================================================================================================================================+
| `%n`{.literal} | Full unit name    | Stands for the full unit name including the type suffix. `%N`{.literal} has the same meaning but also replaces the forbidden characters with ASCII codes.                                  |
+----------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%p`{.literal} | Prefix name       | Stands for a unit name with type suffix removed. For instantiated units %p stands for the part of the unit name before the \"@\" character.                                                |
+----------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%i`{.literal} | Instance name     | Is the part of the instantiated unit name between the \"@\" character and the type suffix. `%I`{.literal} has the same meaning but also replaces the forbidden characters for ASCII codes. |
+----------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%H`{.literal} | Hostname          | Stands for the hostname of the running system at the point in time the unit configuration is loaded.                                                                                       |
+----------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%t`{.literal} | Runtime directory | Represents the runtime directory, which is either `/run`{.literal} for the `root`{.literal} user, or the value of the XDG_RUNTIME_DIR variable for unprivileged users.                     |
+----------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.6. Important unit specifiers

Show more

For a complete list of unit specifiers, see the `systemd.unit(5)`{.literal} man page on your system.

**Additional resources**

-   [How to set limits for services in RHEL and systemd (Red Hat Knowledgebase)](https://access.redhat.com/solutions/1257953)
-   [How to write a service unit file which enforces that particular services have to be started (Red Hat Knowledgebase)](https://access.redhat.com/solutions/3120581)
-   [How to decide what dependencies a systemd service unit definition should have (Red Hat Knowledgebase)](https://access.redhat.com/solutions/3116611)

## [Chapter 2. Managing system services with systemctl](#managing-system-services-with-systemctl) {#chapter-2.-managing-system-services-with-systemctl .title}

To administer system level services, use the `systemctl`{.literal} utility. You can interact with systemd by enabling control of services and units. With `systemctl`{.literal}, you can manage states of system services, list available services, and display status of system services.

### [2.1. Listing system services](#listing-system-services) {#listing-system-services .title}

To optimize system performance, you can use the `systemctl`{.literal} command to list and review system services. System services handle background processes, manage hardware, and supports core system functionality.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   List all currently loaded service units:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl list-units --type service
    ```

    ``` {.language-plaintext tabindex="-1"}
    UNIT                             LOAD    ACTIVE   SUB     DESCRIPTION
    abrt-ccpp.service               loaded  active   exited   Install ABRT coredump hook
    abrt-oops.service               loaded  active   running  ABRT kernel log watcher
    abrtd.service                   loaded  active   running  Automated Bug Reporting Tool
    ...
    systemd-vconsole-setup.service  loaded  active   exited   Configure Virtual Console
    tog-pegasus.service             loaded  active   running  OpenPegasus CIM Server

    LOAD   = Reflects whether the unit definition was properly loaded.
    ACTIVE = The high-level unit activation state, or a generalization of SUB.
    SUB    = The low-level unit activation state, values depend on unit type.

    46 loaded units listed. Pass --all to see loaded but inactive units, too.
    To show all installed unit files use 'systemctl list-unit-files'
    ```

    By default, the `systemctl list-units`{.literal} command displays only active units. For each service unit file, the command provides an overview of the following parameters:

    `UNIT`{.literal} 
    :   The full name of the service unit

    `LOAD`{.literal} 
    :   The load state of the configuration file

    `ACTIVE`{.literal} or `SUB`{.literal} 
    :   The current high-level and low-level unit file activation state

    `DESCRIPTION`{.literal} 
    :   A short description of the unit's purpose and functionality

-   List all loaded units regardless of their state:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl list-units --type service --all
    ```

-   List the status, for example `enabled`{.literal} or `disabled`{.literal}, of all available service units:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl list-unit-files --type service
    ```

    ``` {.language-plaintext tabindex="-1"}
    UNIT FILE                               STATE
    abrt-ccpp.service                       enabled
    abrt-oops.service                       enabled
    abrtd.service                           enabled
    ...
    wpa_supplicant.service                  disabled
    ypbind.service                          disabled

    208 unit files listed.
    ```

    For each service unit, this command displays:

    -   `UNIT FILE`{.literal}: The full name of the service unit.
    -   `STATE`{.literal}: The information whether the service unit is enabled or disabled to start automatically during boot.

### [2.2. Displaying system service status](#displaying-system-service-status) {#displaying-system-service-status .title}

To inspect any service unit to get detailed information and verify the state of the service, use the `systemctl`{.literal} command. Status information includes whether the service unit is running, enabled to start during boot, or masked.

You can also view services that are scheduled to start after or before a particular service unit. See the following table for the available service unit information.

+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                | Description                                                                                                                                            |
+:=====================+:=======================================================================================================================================================+
| `Loaded`{.literal}   | Information whether the service unit has been loaded, the absolute path to the unit file, and a note whether the unit is enabled to start during boot. |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Active`{.literal}   | Information whether the service unit is running followed by a timestamp.                                                                               |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Main PID`{.literal} | The process ID and the name of the corresponding system service.                                                                                       |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Status`{.literal}   | Additional information about the corresponding system service.                                                                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Process`{.literal}  | Additional information about related processes.                                                                                                        |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| `CGroup`{.literal}   | Additional information about related control groups (`cgroups`{.literal}).                                                                             |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 2.1. Available service unit information

Show more

You can use the following commands to display system service status:

-   Display detailed information about a service unit that corresponds to a system service:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl status <name>.service
    ```

    Replace *\<name\>* with the name of the service unit you want to inspect, for example, `gdm`{.literal}.

    This command displays the following information:

    -   The name of the selected service unit followed by a short description
    -   The execution of the service unit, if the unit is executed by the `root`{.literal} user
    -   The most recent log entries
    -   Detailed information about the service unit

-   Verify that a particular service unit is running:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl is-active <name>.service
    ```

-   Decide whether a particular service unit is enabled to start during boot time:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl is-enabled <name>.service
    ```

    Both `systemctl is-active`{.literal} and `systemctl is-enabled`{.literal} commands return an exit status of `0`{.literal} if the specified service unit is running or enabled.

-   Check which services systemd scheduled to start before the specified service unit:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl list-dependencies --after <name>.service
    ```

    For example, to view the list of services ordered to start before `gdm`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl list-dependencies --after gdm.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    `gdm.service
    ├─dbus.socket
    ├─getty@tty1.service
    ├─livesys.service
    ├─plymouth-quit.service
    ├─system.slice
    ├─systemd-journald.socket
    ├─systemd-user-sessions.service
    └─basic.target
    ...
    ```

-   Check what services systemd orders to start after the specified service unit:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl list-dependencies --before <name>.service
    ```

    For example, to view the list of services systemd orders to start after `gdm`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl list-dependencies --before gdm.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    gdm.service
    ├─dracut-shutdown.service
    ├─graphical.target
    │ ├─systemd-readahead-done.service
    │ ├─systemd-readahead-done.timer
    │ └─systemd-update-utmp-runlevel.service
    └─shutdown.target
      ├─systemd-reboot.service
      └─final.target
        └─systemd-reboot.service
    ...
    ```

### [2.3. Starting and stopping a systemd unit](#starting-and-stopping-a-systemd-unit) {#starting-and-stopping-a-systemd-unit .title}

To start or stop a system service in the current session, you can use the `systemctl`{.literal} command.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   To start or stop a system service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl <action> <systemd_unit>
    ```

    Replace *\<action\>* with the action you want to perform such as `start`{.literal} or `stop`{.literal}. And replace *\<systemd_unit\>* with the service unit name such as `httpd`{.literal}.

    Note

    Starting a particular service might require starting one or more other services (**positive dependency**) or stopping one or more services (**negative dependency**). In systemd, positive and negative dependencies between services exist. When you try to start a new service, systemd resolves all dependencies automatically, without explicit notification to the user.

    If a service is already running and you start another service with a negative dependency, the first service stops automatically. For example, if you are running the `httpd`{.literal} service (Apache web server) and then try to start the NGINX service, systemd will automatically stop `httpd`{.literal} first. This is because both services are web servers that cannot run simultaneously on the same port (usually port 80 or 443).

### [2.4. Restarting and reloading a system service](#restarting-and-reload-a-system-service) {#restarting-and-reloading-a-system-service .title}

To restart or reload a system service in the current session, use the `systemctl`{.literal} command. You can stop and start a service, restart a running service, or reload a service without interrupting it.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   Restart a system service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart <name>.service
    ```

    Replace *`<name>`{.literal}* with the name of the service unit you want to restart (for example, `httpd`{.literal}).

-   Restart a service unit only if the corresponding service is already running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl try-restart <name>.service
    ```

-   Reload the configuration without interrupting service execution:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload <name>.service
    ```

    Certain services do not support reload operations. If you use `systemctl reload-or-restart`{.literal} or `systemctl reload-or-try-restart`{.literal}, systemd automatically restarts the service if a reload is not possible. Note that a restart of a service might interrupt connections to this service.

    For details, see `systemctl(1)`{.literal} man page on your system.

### [2.5. Enabling a system service to start at boot](#enabling-a-system-service-to-start-at-boot) {#enabling-a-system-service-to-start-at-boot .title}

To enable a service to start automatically at boot, use the `systemctl`{.literal} command. These changes apply at the next reboot.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   Check if the unit is masked:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status <systemd_unit>
    ```

-   If the unit is masked, unmask it first:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl unmask <systemd_unit>
    ```

-   Enable a service to start at boot time:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now <systemd_unit>
    ```

    Replace *`<systemd_unit>`{.literal}* with the name of the service unit you want to enable, for example, `httpd`{.literal}.

### [2.6. Disabling a system service to start at boot](#disabling-a-system-service-to-start-at-boot) {#disabling-a-system-service-to-start-at-boot .title}

To reduce boot time of your system, you need to either disable or mask the services that start automatically at boot time.

Disabling a service prevents it from starting at boot, but you can still start it manually. Masking a service prevents it from starting automatically or manually and makes it unusable until you unmask it.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   Disable a service to start at boot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl disable <name>.service
    ```

    Replace *`<name>`{.literal}* with the name of the service unit you want to disable (for example, `bluetooth`{.literal}). Optionally, pass the `--now`{.literal} command to also stop the service if it is currently running.

-   To prevent the unit from being accidentally started by an administrator or as a dependency of other units, mask the service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl mask <name>.service
    ```

    For details, see the `systemctl(1)`{.literal} man page on your system.

## [Chapter 3. Booting into a target system state](#booting-into-a-target-system-state) {#chapter-3.-booting-into-a-target-system-state .title}

To set a permanent boot environment or enter a recovery mode, use `systemd`{.literal} targets to have full control over your system functionality. The `systemd`{.literal} init system is a set of systemd unit types such as systemd.target, multi-user.target, shutdown.target.

### [3.1. Target unit files](#target-unit-files) {#target-unit-files .title}

To group various `systemd`{.literal} units through a chain of dependencies during a boot process, use targets in `systemd`{.literal}. Targets in `systemd`{.literal} are groups of related units to act as synchronization points when your system boots.

Target unit files end with the `.target`{.literal} file extension. It represents the `systemd`{.literal} targets. For example, the `multi-user.target`{.literal} unit starts other essential system services such as NetworkManager (`NetworkManager.service`{.literal}) or D-Bus (`dbus.service`{.literal}) and activates another target unit named `basic.target`{.literal}.

You can set the following `systemd`{.literal} targets as default or current targets.

+-------------------------------+---------------------------------------------------------------------+
| Target                        | Purpose                                                             |
+:==============================+:====================================================================+
| `rescue.target`{.literal}     | unit target that pulls in the base system and spawns a rescue shell |
+-------------------------------+---------------------------------------------------------------------+
| `multi-user.target`{.literal} | unit target for setting up a multi-user system                      |
+-------------------------------+---------------------------------------------------------------------+
| `graphical.target`{.literal}  | unit target for setting up a graphical login screen                 |
+-------------------------------+---------------------------------------------------------------------+
| `emergency.target`{.literal}  | unit target that starts an emergency shell on the main console      |
+-------------------------------+---------------------------------------------------------------------+

: Table 3.1. Common systemd targets

Show more

For more information, see `systemd.special(7)`{.literal} and `systemd.target(5)`{.literal} man pages on your system

### [3.2. Changing the default target for booting a system](#changing-the-default-target-to-boot-into) {#changing-the-default-target-for-booting-a-system .title}

To change the default target, modify the current `default.target`{.literal} symbolic link to point to the new target unit. When you set a new default target unit, the current target remains unchanged until the next reboot.

During the boot process, the system initializes the default `systemd`{.literal} target to which `default.target`{.literal} points. `Systemd`{.literal} then resolves this link and boots into the defined target. The selected default target unit is present in the `/etc/systemd/system/default.target`{.literal} file. Each target has a certain level of functionality and groups other units. Additionally, target units act as synchronization points during boot. The `systemd`{.literal} target types include graphical.target, multi-user target, and so on.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

1.  Display the current default target unit `systemd`{.literal} uses to start the system:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl get-default
    ```

    ``` {.language-plaintext tabindex="-1"}
    graphical.target
    ```

2.  List the currently loaded targets:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl list-units --type target
    ```

3.  Configure the system to use a different target unit by default:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl set-default <name>.target
    ```

    Replace *`<name>`{.literal}* with the name of the target unit you want to use by default.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl set-default multi-user.target
    ```

    ``` {.language-plaintext tabindex="-1"}
    Removed /etc/systemd/system/default.target
    Created symlink /etc/systemd/system/default.target -> /usr/lib/systemd/system/multi-user.target
    ```

4.  Optional: To immediately switch to the new default target unit:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl isolate default.target
    ```

**Verification**

1.  Verify the default target unit:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl get-default
    ```

    ``` {.language-plaintext tabindex="-1"}
    multi-user.target
    ```

2.  Reboot the system.

### [3.3. Temporarily changing the current target](#changing-the-current-target) {#temporarily-changing-the-current-target .title}

To troubleshoot or recover the system, you can temporarily change the current target without rebooting the system. To switch to a different target, use the `systemctl isolate`{.literal} command.

By selecting or changing `systemd`{.literal} targets, you define and control selective services and units starting during the boot process. You can also view the current default, switch targets, or access the emergency shell prompt as needed.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

1.  Display the list of targets you can select:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl list-units --type target
    ```

2.  Change to a different target unit in the current session:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl isolate <name>.target
    ```

    Replace *\<name\>* with the name of the target unit you want to use in the current session.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl isolate multi-user.target
    ```

    This command starts the **`multi-user`{.literal}** target unit and all dependent units. It also immediately stops all other units that are not part of the new target. As this is a temporary operation, the system will boot again into the default target when you reboot the host. You can only isolate targets that have the `AllowIsolate=yes`{.literal} option set in the unit files.

    For details, see the `systemctl(1)`{.literal} man page on your system.

### [3.4. Booting to rescue mode](#booting-to-rescue-mode) {#booting-to-rescue-mode .title}

To troubleshoot or repair the system, you can boot into the rescue mode to enter a single-user environment. This happens when the system fails to reach a later target and the existing booting process fails.

In rescue mode, the system mounts local file systems and starts required services. It does not activate network interfaces.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   Enter the rescue mode:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl rescue
    ```

    ``` {.language-plaintext tabindex="-1"}
    Broadcast message from root@localhost on pts/0 (Fri 2023-03-24 18:23:15 CEST):
    The system is going down to rescue mode NOW!
    ```

    This command is similar to `systemctl isolate rescue.target`{.literal} and also sends an informative message to all users currently logged in the system.

    Note

    To prevent `systemd`{.literal} from sending a message, enter:

    ``` {.language-plaintext tabindex="-1"}
    # *systemctl --no-wall rescue*
    ```

**Troubleshooting**

If you cannot boot the system in the rescue mode, boot in the emergency mode to enter in a minimal environment. In the emergency mode, the system mounts the root file system only for reading and initiates essential services. Additionally, the system neither mounts any other local filesystems nor activates network interfaces in the emergency mode.

### [3.5. Troubleshooting the boot process](#troubleshooting-the-boot-process) {#troubleshooting-the-boot-process .title}

To enter in the most minimal environment for troubleshooting the boot process, you can select a non-default target at boot time. Choose the emergency mode to enter in the most minimal environment. Changing the target at boot time affects only a single boot event.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

1.  Reboot the system, and interrupt the boot loader menu countdown by pressing any key except the `Enter`{.literal} key to initiate a normal boot.

2.  Select the kernel entry that you want to start.

3.  Press the `e`{.literal} key to edit the current entry.

4.  Navigate to the end of the line that starts with `linux`{.literal} and press Ctrl+E to jump to the end of this line.

5.  To select a different boot target, append the `systemd.unit=`{.literal} parameter to the end of the line that starts with `linux`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    linux ... systemd.unit=<name>.target
    ```

    Replace *`<name>`{.literal}* with the name of the target unit you want to use. For example, `systemd.unit=emergency.target`{.literal}

6.  Press Ctrl+X to boot with these settings.

## [Chapter 4. Shutting down, suspending, and hibernating the system](#shutting-down-suspending-and-hibernating-the-system) {#chapter-4.-shutting-down-suspending-and-hibernating-the-system .title}

To administer and manage data and settings on a system, use the `systemd`{.literal} power management options. Tasks include managing power consumption, performing system shutdowns to protect data, and restarting the system to apply changes or updates.

### [4.1. Scheduling a system shutdown](#scheduling-a-system-shutdown) {#scheduling-a-system-shutdown .title}

To perform maintenance tasks and apply updates to applications, you can schedule a delayed shutdown by using the `shutdown`{.literal} command. It is important to schedule a shutdown for system maintenance tasks to avoid data loss and unexpected system failures.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   Shut down the system and power off the machine at a certain time:

    ``` {.language-plaintext tabindex="-1"}
    # shutdown --poweroff hh:mm
    ```

    Replace *`hh:mm`{.literal}* with the time in the 24-hour format. To prevent new logins, the system creates the `/run/nologin`{.literal} file 5 minutes before the shutdown.

    When you specify time of the `shutdown`{.literal} command, you can notify users logged in to the system of the planned shutdown by specifying an optional *wall message*:

    ``` {.language-plaintext tabindex="-1"}
    # shutdown --poweroff 13:59 "Attention. The system will shut down at 13:59"
    ```

-   Shut down and halt the system after a delay, without powering off the machine:

    ``` {.language-plaintext tabindex="-1"}
    # shutdown --halt +m
    ```

    Where *`+m`{.literal}* is the delay time in minutes. You can use the `now`{.literal} keyword as an alias for `+0`{.literal}.

-   Cancel a pending shutdown:

    ``` {.language-plaintext tabindex="-1"}
    # shutdown -c
    ```

    For details, see `shutdown(8)`{.literal} man page on your system.

### [4.2. Shutting down the system using the systemctl command](#shutting-down-the-system-using-the-systemctl-command) {#shutting-down-the-system-using-the-systemctl-command .title}

You can safely shut down the system by using the `systemctl`{.literal} command to prevent data corruption during maintenance. You can choose to either power off the machine or halt the system without powering off.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   Shut down the system and power off the machine:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl poweroff
    ```

    -   Use the `--when`{.literal} option with the `systemctl poweroff`{.literal} command to specify time:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl poweroff --when="+15min"
        ```

-   Shut down and halt the system without powering off the machine:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl halt
    ```

    -   Use the `--when`{.literal} option with the `systemctl halt`{.literal} command to specify time:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl halt --when="+15min"
        ```

        Note

        By default, running these commands causes `systemd`{.literal} to send an informative message to all users that are currently logged into the system. To prevent `systemd`{.literal} from sending this message, run the selected command with the `--no-wall`{.literal} command line option.

### [4.3. Restarting the system](#restarting-the-system) {#restarting-the-system .title}

To apply pending changes and updates, you can restart the system by using the `systemctl`{.literal} command. When you restart the system, `systemd`{.literal} stops all running programs and services, the system shuts down, and then starts again immediately.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

-   Restart the system:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reboot
    ```

    Note

    By default, running this command causes `systemd`{.literal} to send an informative message to all users that are currently logged into the system.

    To prevent `systemd`{.literal} from sending this message, run this command with the `--no-wall`{.literal} option.

### [4.4. Optimizing power consumption by suspending and hibernating the system](#optimizing-power-consumption-by-suspending-and-hibernating-the-system) {#optimizing-power-consumption-by-suspending-and-hibernating-the-system .title}

To save the current system state and reduce power consumption, you can use the `systemctl`{.literal} command. With `systemctl`{.literal}, you can suspend, hibernate, hybrid sleep, or suspend-then-hibernate the system.

-   To suspend the system, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl suspend
    ```

    Suspending saves the system state in RAM and powers off most devices, except the RAM module. When you turn the machine back on, the system restores its state from RAM without rebooting. Restoring from suspend mode is significantly faster than from hibernation because this operation saves the state in RAM, not on disk. However, the suspended system state is vulnerable to power outages.

-   To hibernate the system, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl hibernate
    ```

    Hibernating saves the system state on the hard disk drive and powers off the machine. When you turn the machine back on, the system restores its state from the saved data without rebooting. Restoring from hibernation is significantly slower than from suspend mode because this operation saves state on disk, not in RAM. However, the machine does not have to keep electrical power to the RAM module.

-   To hibernate and suspend the system, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl hybrid-sleep
    ```

    Hybrid sleep combines hibernation and suspend. The system saves the current state to disk and enters a low-power state, allowing faster resume. In case of power loss during the sleep operation, the system recovers the state from the saved disk image, similar to hibernation.

-   To suspend and then hibernate the system, enter:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl suspend-then-hibernate
    ```

    This mode first suspends the system, saving the state to RAM in low-power mode. If the system remains suspended for a duration you define in `HibernateDelaySec`{.literal}, it then hibernates. Hibernation saves the state to the hard disk and powers off the system completely. This mode conserves battery power while enabling quick resume. It also protects your data during power failures.

### [4.5. Changing the behavior of the power button when GNOME is not running](#changing-the-behavior-of-the-power-button-when-pressing-the-button-and-gnome-is-not-running) {#changing-the-behavior-of-the-power-button-when-gnome-is-not-running .title}

To prevent the system from shutting down when you press the power button, modify settings for the non-graphical `systemd`{.literal} target. Select the option according to requirement.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

1.  Edit the `/etc/systemd/logind.conf`{.literal} configuration file to set the `HandlePowerKey`{.literal} variable.

2.  To reboot the system when you press the power button, set the `reboot`{.literal} value:

    ``` {.language-plaintext tabindex="-1"}
    HandlePowerKey=reboot
    ```

    Use one of the following options:

    -   `poweroff`{.literal}: Shut down the computer.
    -   `reboot`{.literal}: Reboot the system.
    -   `halt`{.literal}: Initiate a system halt.
    -   `kexec`{.literal}: Initiate a `kexec`{.literal} reboot.
    -   `suspend`{.literal}: Suspend the system.
    -   `hibernate`{.literal}: Initiate system hibernation.
    -   `ignore`{.literal}: Do nothing.

3.  Restart the `systemd-logind`{.literal} service to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload systemd-logind
    ```

### [4.6. Changing the behavior of the power button in GNOME](#changing-the-behavior-of-the-power-button-when-pressing-the-button-and-gnome-is-running) {#changing-the-behavior-of-the-power-button-in-gnome .title}

To prevent the system from suspending when you press the power button, modify settings for the GNOME login screen and user session. You can select one of the options: physically on a system or virtually from a remote console.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

1.  Create a local database for system-wide settings in the `/etc/dconf/db/local.d/01-power`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    [org/gnome/settings-daemon/plugins/power]
    power-button-action=<value>
    ```

    Replace `<value>`{.literal} with one of the following power button actions:

    -   `nothing`{.literal}: Does nothing.

    -   `suspend`{.literal}: Suspends the system.

    -   `hibernate`{.literal}: Hibernates the system.

    -   `interactive`{.literal}: Shows a pop-up query asking the user what to do.

        In the interactive mode, when you press the power button, the system automatically powers off after 60 seconds. You can select a different behavior from the pop-up query.

2.  Optional: To override existing settings and prevent other users from changing it, edit configuration in the `/etc/dconf/db/local.d/locks/01-power`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    /org/gnome/settings-daemon/plugins/power/power-button-action
    ```

3.  Update the system databases:

    ``` {.language-plaintext tabindex="-1"}
    # dconf update
    ```

4.  Log out and log in again for the system-wide settings to take effect.

**Verification**

-   Press the power button and check if the system performs the action you configured.

## [Chapter 5. Optimizing systemd to shorten the boot time](#optimizing-systemd-to-shorten-the-boot-time) {#chapter-5.-optimizing-systemd-to-shorten-the-boot-time .title}

You can optimize system performance by managing services associated with systemd. Review services that systemd starts during boot time and evaluate them according to your requirements. Disabling certain services that start at boot can shorten the boot time.

### [5.1. Examining system boot performance](#examining-system-boot-performance) {#examining-system-boot-performance .title}

You can tune the `systemd`{.literal} service by using the `systemd-analyze`{.literal} command to shorten boot time and examine boot performance.

**Procedure**

-   List all enabled services to determine `systemd`{.literal} to tune the boot time:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl list-unit-files --state=enabled
    ```

-   Analyze the information about the time that the last successful boot took:

    ``` {.language-plaintext tabindex="-1"}
    $ systemd-analyze
    ```

-   Analyze the unit initialization time of each `systemd`{.literal} unit:

    ``` {.language-plaintext tabindex="-1"}
    $ systemd-analyze blame
    ```

    The output lists the units in descending order according to the time they took to initialize during the last successful boot.

-   Identify critical units that took the longest time to initialize at the last successful boot:

    ``` {.language-plaintext tabindex="-1"}
    $ systemd-analyze critical-chain
    ```

**Verification**

-   The output with red color text indicates the units that can critically slow down the boot.

    For details, see `systemd(1)`{.literal}, `systemctl(1)`{.literal}, and `systemd-analyze (1)`{.literal} man pages on your system.

### [5.2. A guide to disable selective services](#a-guide-to-selecting-services-that-can-be-safely-disabled) {#a-guide-to-disable-selective-services .title}

To reduce boot time of your system, you need to selectively disable only the non-essential services that start automatically at boot time.

-   List enabled services:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl list-unit-files --state=enabled
    ```

-   Disable a service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl disable <service_name>
    ```

Some services are not critical yet required for normal functioning of Red Hat Enterprise Linux (RHEL). Except these services, you can disable other services that are enabled by default with a minimal installation of RHEL.

+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Service name                                            | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+:========================================================+:=======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `auditd.service`{.literal}                              | Disable `auditd.service`{.literal} only if you do not need audit messages from the kernel. Be aware that if you disable `auditd.service`{.literal}, the `/var/log/audit/audit.log`{.literal} file is not produced. As a result, you cannot retroactively review some commonly-reviewed actions or events, such as user logins, service starts or password changes. Also note that `auditd`{.literal} has two parts: a kernel part, and a service itself. By using the `systemctl disable auditd`{.literal} command, you only disable the service, but not the kernel part. To disable system auditing in its entirety, set `audit=0`{.literal} on kernel command line. |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `crond.service`{.literal}                               | Be aware that no items from `crontab`{.literal} will run if you disable crond.service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dbus-org.fedoraproject.FirewallD1.service`{.literal}   | A symlink to `firewalld.service`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dbus-org.freedesktop.NetworkManager.service`{.literal} | A symlink to `NetworkManager.service`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dbus-org.freedesktop.nm-dispatcher.service`{.literal}  | A symlink to `NetworkManager-dispatcher.service`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `firewalld.service`{.literal}                           | Disable `firewalld.service`{.literal} only if you do not need a firewall.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `import-state.service`{.literal}                        | Disable `import-state.service`{.literal} only if you do not need to boot from a network storage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `irqbalance.service`{.literal}                          | Disable `irqbalance.service`{.literal} only if you have just one CPU. Do not disable `irqbalance.service`{.literal} on systems with multiple CPUs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `kdump.service`{.literal}                               | Disable `kdump.service`{.literal} only if you do not need reports from kernel crashes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `loadmodules.service`{.literal}                         | This service is not started unless the `/etc/rc.modules`{.literal} or `/etc/sysconfig/modules`{.literal} directory exists, which means that it is not started on a minimal RHEL installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `lvm2-monitor.service`{.literal}                        | Disable `lvm2-monitor.service`{.literal} only if you do not use Logical Volume Manager (LVM).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `NetworkManager-dispatcher.service`{.literal}           | Disable `NetworkManager-dispatcher.service`{.literal} only if you do not need notifications on network configuration changes (for example in static networks).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `NetworkManager-wait-online.service`{.literal}          | Disable `NetworkManager-wait-online.service`{.literal} only if you do not need a working network connection immediately after boot. When this service is enabled, the system does not finish the boot process until the network connection is established. This setting prolongs the boot time significantly.                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `NetworkManager.service`{.literal}                      | Disable `NetworkManager.service`{.literal} only if you do not need connection to a network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `nis-domainname.service`{.literal}                      | Disable `nis-domainname.service`{.literal} only if you do not use Network Information Service (NIS).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rngd.service`{.literal}                                | Disable `rngd.service`{.literal} only if you do not need much entropy on your system, or you do not have any sort of hardware generator. Note that the service is necessary in environments that require many good entropy, such as systems used for generation of X.509 certificates (for example the FreeIPA server).                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rsyslog.service`{.literal}                             | Disable `rsyslog.service`{.literal} only if you do not need persistent logs, or you set `systemd-journald`{.literal} to persistent mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `selinux-autorelabel-mark.service`{.literal}            | Disable `selinux-autorelabel-mark.service`{.literal} only if you do not use SELinux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sshd.service`{.literal}                                | Disable `sshd.service`{.literal} only if you do not need remote logins by OpenSSH server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sssd.service`{.literal}                                | Disable `sssd.service`{.literal} only if there are no users who log in the system over the network (for example by using LDAP or Kerberos). Disable all `sssd-*`{.literal} units if you disable `sssd.service`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `syslog.service`{.literal}                              | An alias for `rsyslog.service`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `tuned.service`{.literal}                               | Disable `tuned.service`{.literal} only if you do not need to use performance tuning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `lvm2-lvmpolld.socket`{.literal}                        | Disable `lvm2-lvmpolld.socket`{.literal} only if you do not use Logical Volume Manager (LVM).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dnf-makecache.timer`{.literal}                         | Disable `dnf-makecache.timer`{.literal} only if you do not need your package metadata to be updated automatically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `unbound-anchor.timer`{.literal}                        | Disable `unbound-anchor.timer`{.literal} only if you do not need daily updates of the root trust anchor for DNS Security Extensions (DNSSEC). The Unbound resolver and resolver library for DNSSEC validation uses this root trust anchor.                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 5.1. Services enabled by default on a minimal installation of RHEL

Show more

To find details about a service, use one of the following commands:

``` {.language-plaintext tabindex="-1"}
$ systemctl cat <service_name>
```

``` {.language-plaintext tabindex="-1"}
$ systemctl help <service_name>
```

The `systemctl cat`{.literal} command displays the contents of a service's main unit file, typically located at `/usr/lib/systemd/system/`{.literal}*`<service>`{.literal}*, along with any override files. Overrides include custom unit files in `/etc/systemd/system/`{.literal}*`<service>`{.literal}* or drop-in configuration files in corresponding `unit.type.d`{.literal} directories. For details, see the `systemd.unit(5)`{.literal} man page or use `systemctl help `{.literal}*`<service>`{.literal}* to view the manual for a specific service.

## [Legal Notice](#idm140461332442464) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
