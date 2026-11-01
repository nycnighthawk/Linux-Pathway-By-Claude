---
{"title": "Monitoring and managing system status and performance", "guide": "monitoring_and_managing_system_status_and_performance", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/monitoring_and_managing_system_status_and_performance/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Monitoring and managing system status and performance {#monitoring-and-managing-system-status-and-performance .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Optimizing system throughput, latency, and power consumption {#optimizing-system-throughput-latency-and-power-consumption .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140378399692928)

**Abstract**

Monitor, analyze, and improve the performance of your RHEL system by using tools such as TuneD for performance optimization, perf for monitoring hardware and software events, and Performance Co-Pilot (PCP) for system performance analysis. Review system activity, log and visualize performance data, and adjust key settings, for example, disk schedulers and power usage, by collecting performance metrics and configuring the system for your specific workload. Improve system efficiency by applying techniques for real-time CPU profiling, analyzing memory allocation, identifying performance bottlenecks, managing power consumption effectively, and detecting issues such as false sharing.

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

## [Chapter 1. Overview of performance monitoring options](#overview-of-performance-monitoring-options) {#chapter-1.-overview-of-performance-monitoring-options .title}

To monitor and optimize performance of your Red Hat Enterprise Linux system, you need to use specific tools.

-   Performance Co-Pilot (pcp) is a suite of tools for monitoring, visualizing, storing, and analyzing system-level performance measurements. It supports the monitoring and management of real-time data, as well as logging and retrieval of historical data.

-   RHEL provides several command-line tools to monitor a system outside runlevel 5. The following are the built-in command-line tools:

    -   The `procps-ng`{.literal} package provides following utilities:

        -   The `top`{.literal} utility gives a dynamic view of processes in a running system. It displays a variety of information, including a system summary and a list of tasks currently being managed by the Linux kernel.
        -   The `ps`{.literal} utility captures a snapshot of the selected group of active processes. By default, the examined group is limited to processes that are owned by the current user and associated with the command line where the `ps`{.literal} command is run.
        -   The virtual memory statistics (`vmstat`{.literal}) utility provides instant reports of processes, memory, paging, block input/output, interrupts, and CPU activity in the system.

    -   The `sysstat`{.literal} package provides the system activity reporter (`sar`{.literal}) utility, which collects and reports information about system activity for the current day.

-   `perf`{.literal} uses hardware performance counters and kernel trace-points to track the impact of other commands and applications on a system.

-   `bcc-tools`{.literal}, a set of performance analysis utilities, built on top of Berkeley Packet Filter (BPF) Compiler Collection (BCC). It provides over 100 Extended BPF (eBPF) scripts that monitor kernel activities. For more information about each of these tools, see the man page describing how to use it and what functions it performs.

-   The `kernel-tools`{.literal} package provides the `turbostat`{.literal} utility that reports on processor topology, frequency, idle power-state statistics, temperature, and power usage on the Intel 64 processors.

-   The `sysstat`{.literal} package provides the `iostat`{.literal} utility that monitors and reports on loading of system I/O device to help administrators make decisions about how to balance I/O load between physical disks.

-   The `irqbalance`{.literal} utility distributes hardware interrupts across processors to improve system performance.

-   The `numactl`{.literal} package provides the `numastat`{.literal} utility. By default, `numastat`{.literal} displays per-node Non-Uniform Memory Access (NUMA) hit and miss system statistics from the kernel memory allocator. High `numa_hit`{.literal} values and low `numa_miss`{.literal} values indicate optimal performance.

-   `numad`{.literal} is an automatic NUMA affinity management daemon. It monitors NUMA topology and resource usage within a system that dynamically improves NUMA resource allocation, management, and system performance.

-   `SystemTap`{.literal} is a programmable tracing/probing/debugging system for the kernel and userspace, and includes many brief scripts.

-   `valgrind`{.literal} runs uninstrumented userspace programs under supervision, to find memory errors, allocation statistics, concurrency violations.

-   The `intel-cmt-cat`{.literal} package provides the `pqos`{.literal} utility to monitor and control CPU cache and memory bandwidth on recent Intel processors.

**Additional resources**

-   [What exactly is the meaning of the value \"await\" reported by iostat? (Red Hat Knowledgebase article)](https://access.redhat.com/articles/524353)

## [Chapter 2. Optimizing system performance with TuneD](#optimizing-system-performance-with-tuned) {#chapter-2.-optimizing-system-performance-with-tuned .title}

TuneD is a system tuning service designed to optimize system performance and power consumption by using predefined or custom profiles. It includes predefined profiles suited for different workloads, such as high throughput, low latency, and power saving.

### [2.1. TuneD profiles distributed with RHEL](#tuned-profiles-distributed-with-rhel) {#tuned-profiles-distributed-with-rhel .title}

During installation, TuneD automatically selects the most suitable profile based on the system type. For example, the throughput-performance is selected for compute nodes, virtual-guest for virtual machines, and balanced for general systems. This ensures optimal performance for the environment.

Profiles are divided mainly into two categories:

-   power-saving profiles that reduce power consumption with minimal performance impact, and
-   performance-boosting profiles that optimize system resources for improved speed and responsiveness.

Following is the list of notable profiles distributed with RHEL to select based on the system load:

`balanced`{.literal}
:   It is the default power-saving profile and is intended to be a compromise between performance and power consumption. It uses auto-scaling and auto-tuning whenever possible.

`powersave`{.literal}

:   It is a profile for maximum power saving performance and can throttle the performance to minimize the actual power consumption. It enables USB autosuspend, Wi-Fi power saving, and Aggressive Link Power Management (ALPM) power savings for SATA host adapters. It also schedules multi-core power savings for systems with a low wakeup rate and activates the `ondemand`{.literal} governor. It enables AC97 audio power saving or, depending on your system, HDA-Intel power savings with a 10 seconds timeout. If your system contains a supported Radeon graphics card with enabled KMS, the profile configures it to automatic power saving. It changes the `energy_performance_preference`{.literal} attribute to the `powersave`{.literal} or `power energy`{.literal} setting. It also changes the `scaling_governor`{.literal} policy attribute to either the `ondemand`{.literal} or `powersave`{.literal} CPU governor.

    Note

    In some cases, the balanced profile is more efficient than powersave. For tasks such as video transcoding, running at full power completes the job faster. It also enables the system to enter an idle state and switch to efficient power-saving modes sooner. Throttling the machine reduces power during the task but extends its duration, potentially increasing overall energy use. Thus, the balanced profile is often a better choice.

`throughput-performance`{.literal}
:   A server profile optimized for high throughput that disables power savings mechanisms. It also enables `sysctl`{.literal} settings to improve the throughput performance of the disk and network IO.

`accelerator-performance`{.literal}
:   A profile that contains the same tuning as the `throughput-performance`{.literal} profile. Additionally, it locks the CPU to low C states so that the latency is less than 100us. This improves the performance of certain accelerators, such as GPUs.

`latency-performance`{.literal}
:   A server profile optimized for low latency and disables power savings mechanisms and enables `sysctl`{.literal} settings that improve latency. CPU governor is set to performance and the CPU is locked to the low C states (by PM QoS).

`network-latency`{.literal}
:   A profile for low latency network tuning. It is based on the `latency-performance`{.literal} profile. It additionally disables transparent huge pages and NUMA balancing, and tunes several other network-related sysctl parameters.

`hpc-compute`{.literal}
:   A profile optimized for high-performance computing. It is based on the `latency-performance`{.literal} profile.

`network-throughput`{.literal}
:   A profile for throughput network tuning. It is based on the `throughput-performance`{.literal} profile. It additionally increases kernel network buffers.

`virtual-guest`{.literal}
:   A profile designed for Red Hat Enterprise Linux virtual machines and VMWare guests based on the `throughput-performance`{.literal} profile. Among other tasks, it decreases virtual memory swappiness and increases disk readahead values. It does not disable disk barriers.

`virtual-host`{.literal}
:   A profile designed for virtual hosts based on the `throughput-performance`{.literal} profile. Among other tasks, it decreases virtual memory swappiness, increases disk readahead values, and enables a more aggressive value of dirty pages writeback.

`oracle`{.literal}
:   A profile optimized for Oracle database loads based on the `throughput-performance`{.literal} profile. It additionally disables transparent huge pages and modifies other performance-related kernel parameters. This profile is provided by the tuned-profiles-oracle package.

`desktop`{.literal}
:   A profile optimized for desktops, based on the `balanced`{.literal} profile. It additionally enables scheduler autogroups for better response of interactive applications.

`optimize-serial-console`{.literal}

:   A profile that tunes down I/O activity to the serial console by reducing the printk value. This should make the serial console more responsive. This profile is intended to be used as an overlay on other profiles. For example:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile throughput-performance optimize-serial-console
    ```

`mssql`{.literal}
:   A profile provided for Microsoft SQL Server. It is based on the `throughput-performance`{.literal} profile.

`intel-sst`{.literal}

:   A profile optimized for systems with user-defined **Intel Speed Select Technology** configurations. This profile is intended to be used as an overlay on other profiles. For example:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile cpu-partitioning intel-sst
    ```

`aws`{.literal}

:   A profile optimized for AWS EC2 instances. It is based on the `throughput-performance`{.literal} profile.

    For more information about these profiles, see the `tuned-profiles`{.literal} man page on your system.

### [2.2. Real-time TuneD profiles distributed with RHEL](#real-time-tuned-profiles-distributed-with-rhel) {#real-time-tuned-profiles-distributed-with-rhel .title}

RHEL ships some profiles specifically for systems running the real-time kernel. Without a special kernel build, they do not configure the system to be real-time. On RHEL, the profiles are available with additional repositories.

`realtime`{.literal}
:   Use on bare metal real-time systems. This is provided by the `tuned-profiles-realtime`{.literal} package, which is available from the RT or NFV repositories.

`realtime-virtual-host`{.literal}
:   Use in a virtualization host configured for real-time. This is provided by the `tuned-profiles-nfv-host`{.literal} package, which is available from the NFV repository.

`realtime-virtual-guest`{.literal}
:   Use in a virtualization guest configured for real-time. This is provided by the `tuned-profiles-nfv-guest`{.literal} package, which is available from the NFV repository.

### [2.3. Installing and enabling TuneD](#installing-and-enabling-tuned) {#installing-and-enabling-tuned .title}

As a system administrator, use `TuneD`{.literal} to optimize the performance profile for a variety of use cases. You must install and enable TuneD to start using it.

After you install TuneD, the `/usr/lib/tuned/profiles`{.literal} directory stores distribution-specific profiles. Each profile is stored in its own subdirectory. The profile includes the profile configuration file, named `tuned.conf`{.literal} and optionally other files, such as helper scripts. Also, to customize a profile, copy the profile directory into `/etc/tuned/profiles`{.literal}, which stores the files related to the custom profiles. In cases where profiles with the same name exist, the custom profile located in `/etc/tuned/profiles`{.literal} takes precedence.

**Prerequisites**

-   You have administrative privileges.

**Procedure**

1.  Install the TuneD package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tuned
    ```

2.  Enable and start the TuneD service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now tuned
    ```

3.  Optional: Install TuneD profiles for real-time systems:

    For the TuneD profiles for real-time systems enable the `rhel-10`{.literal} repository.

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable=rhel-10-for-x86_64-nfv-beta-rpms
    ```

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tuned-profiles-realtime tuned-profiles-nfv
    ```

**Verification**

-   Check the activation status of the profile:

    ``` {.language-plaintext tabindex="-1"}
    $ tuned-adm active
    ```

    ``` {.language-plaintext tabindex="-1"}
    Current active profile: throughput-performance
    ```

-   Check if the profile is active and applied:

    ``` {.language-plaintext tabindex="-1"}
    $ tuned-adm verify
    ```

    ``` {.language-plaintext tabindex="-1"}
    Verification succeeded, current system settings match the preset profile. See tuned log file ('/var/log/tuned/tuned.log') for details.
    ```

### [2.4. Managing TuneD profiles](#managing-tuned-profiles) {#managing-tuned-profiles .title}

You can manage TuneD profiles in Red Hat Enterprise Linux, including listing available profiles, setting a specific profile, and disabling TuneD when necessary. Proper management of profiles optimizes system performance for specific workloads, such as using the cpu-partitioning profile for low-latency applications.

**Prerequisites**

-   You have installed and enabled TuneD.
-   You have administrative privileges.

**Procedure**

1.  List all the available predefined TuneD profiles:

    ``` {.language-plaintext tabindex="-1"}
    $ tuned-adm list
    ```

2.  Optional: To let TuneD recommend the most suitable profile for your system, use the following command:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm recommend
    ```

    ``` {.language-plaintext tabindex="-1"}
    throughput-performance
    ```

3.  Activate the profile:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile selected-profile
    ```

    Alternatively, you can activate a combination of multiple profiles:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile selected-profile1 selected-profile2
    ```

4.  View the current active TuneD profile on your system:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm active
    ```

    ``` {.language-plaintext tabindex="-1"}
    Current active profile: selected-profile
    ```

5.  Disable all tunings temporarily:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm off
    ```

    ``` {.language-plaintext tabindex="-1"}
    The tunings are applied again after the TuneD service restarts.
    ```

6.  Optional: Stop and disable the TuneD service permanently:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl disable --now tuned
    ```

### [2.5. Profile inheritance and variables for profile customization](#profile-inheritance-and-variables-for-profile-customization) {#profile-inheritance-and-variables-for-profile-customization .title}

TuneD supports profile inheritance, variable usage, and built-in functions to create new or modify existing profiles efficiently.

The pre-installed and custom profiles are available in the following directories:

-   Pre-installed profiles: Located in `/usr/lib/tuned/profiles/`{.literal}

-   Custom profiles: Created in `/etc/tuned/profiles/`{.literal}

    Profile Inheritance

    :   TuneD profiles can inherit settings from other profiles by using the include option in the \[main\] section. Profile inheritance means Child profiles inherit parent settings, but can override or add parameters for custom requirements. For example, to create a profile based on the balanced profile that additionally sets ALPM to `min_power`{.literal} instead of `medium_power`{.literal}, use:

        ``` {.language-plaintext tabindex="-1"}
        [main]
        include=balanced

        [scsi_host]
        alpm=min_power
        ```

    Variables' usage while customizing profiles

    :   You can define variables while customizing profiles. Variables help to simplify configurations by reducing repetitive definitions. Define your own variables by creating the `[variables]`{.literal} section in a profile and by using:

        ``` {.language-plaintext tabindex="-1"}
        [variables]
        variable_name=value
        ```

        To expand the value of a variable in a profile, use:

        ``` {.language-plaintext tabindex="-1"}
        ${variable_name}
        ```

        Store the variables in different files and use these variables while customizing profiles by adding the filepath to the variable file. For example, add the following lines to the configuration file to consider variables from the separate file:

        ``` {.language-plaintext tabindex="-1"}
        tuned.conf:
        [variables]
        include=/etc/tuned/my-variables.conf

        [bootloader]
        cmdline=isolcpus=${isolated_cores}
        ```

        Where `isolated_cores=1,2`{.literal} is added in **my-variable.conf** file as follows:

    ``` {.language-plaintext tabindex="-1"}
    my-variable.conf:
    isolated_cores=1,2
    ```

### [2.6. Built-in functions for profile customization](#built-in-functions-for-profile-customization) {#built-in-functions-for-profile-customization .title}

You can use the built-in functions in TuneD profiles to dynamically expand at runtime when a profile is activated. Use built-in functions with TuneD variables to modify and process values dynamically within a profile.

You can extend TuneD with custom functions by creating and integrating custom Python functions as plugins.

Syntax to start a built-in function

:   ``` {.language-plaintext tabindex="-1"}
    ${f:function_name:argument_1:argument_2}
    ```

    To retrieve the directory path where the profile and the `tuned.conf`{.literal} file are located, use the `PROFILE_DIR`{.literal} variable. It uses the following syntax:

    ``` {.language-plaintext tabindex="-1"}
    ${i:PROFILE_DIR}
    ```

Example of isolating CPU cores by using a built-in function

:   ``` {.language-plaintext tabindex="-1"}
    [variables]
    non_isolated_cores=0,3-5

    [bootloader]
    cmdline=isolcpus=${f:cpulist_invert:${non_isolated_cores}}
    ```

    In this example, the `${non_isolated_cores}`{.literal} variable expands to `0,3-5`{.literal}. The `cpulist_invert`{.literal} function inverts the CPU list. On a system with 6 CPUs, `0,3-5`{.literal} inverts to `1,2`{.literal}, resulting in the kernel booting with the `isolcpus=1,2`{.literal} option.

    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Function name                     | Description                                                                                                                                                                                                                                                                                                                                                                                                      |
    +:==================================+:=================================================================================================================================================================================================================================================================================================================================================================================================================+
    | assertion                         | Compare two arguments. If they do not match, the function logs text from the first argument and cancels profile loading.                                                                                                                                                                                                                                                                                         |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | assertion_non_equal               | Compare two arguments. If they match, the function logs text from the first argument and cancels profile loading.                                                                                                                                                                                                                                                                                                |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | calc_isolated_cores               | Calculates and returns isolated cores. The argument specifies how many cores per socket to reserve for housekeeping. If not specified, one core per socket is reserved for housekeeping and the rest are isolated.                                                                                                                                                                                               |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | check_net_queue_count             | Checks whether the user has specified a queue count for net devices. If not, it returns the number of housekeeping CPUs.                                                                                                                                                                                                                                                                                         |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpuinfo_check                     | Checks regular expressions against /proc/cpuinfo. Accepts arguments in the form: REGEX1, STR1, REGEX2, STR2, ...​\[, STR_FALLBACK\]. If REGEX1 matches something in /proc/cpuinfo, it expands to STR1; if REGEX2 matches, it expands to STR2. It stops on the first match. If no regular expression matches, it expands to STR_FALLBACK or an empty string if no fallback is provided.                            |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpulist2devs                      | Converts a CPU list to device strings.                                                                                                                                                                                                                                                                                                                                                                           |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpulist2hex                       | Converts a CPU list to a hexadecimal CPU mask.                                                                                                                                                                                                                                                                                                                                                                   |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpulist2hex_invert                | Converts a CPU list to a hexadecimal CPU mask and inverts it.                                                                                                                                                                                                                                                                                                                                                    |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpulist_invert                    | Inverts a list of CPUs to make its complement. For example, on a system with 4 CPUs (0-3), the inversion of the list 0,2,3 is 1.                                                                                                                                                                                                                                                                                 |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpulist_online                    | Checks whether the CPUs from the list are online. Returns the list containing only online CPUs.                                                                                                                                                                                                                                                                                                                  |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpulist_pack                      | Packs a CPU list in the form of 1,2,3,5 to 1-3,5.                                                                                                                                                                                                                                                                                                                                                                |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpulist_present                   | Checks whether the CPUs from the list are present. Returns the list containing only present CPUs.                                                                                                                                                                                                                                                                                                                |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | cpulist_unpack                    | Unpacks a CPU list in the form of 1-3,4 to 1,2,3,4.                                                                                                                                                                                                                                                                                                                                                              |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | exec                              | Runs a process and returns its output.                                                                                                                                                                                                                                                                                                                                                                           |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | hex2cpulist                       | Converts a hexadecimal CPU mask to a CPU list.                                                                                                                                                                                                                                                                                                                                                                   |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | intel_recommended_pstate          | Checks the processor code name and returns the recommended `intel_pstate`{.literal} CPUFreq driver mode. \"Active\" is returned for newer generation processors not in the `PROCESSOR_NAME`{.literal} list.                                                                                                                                                                                                      |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | iscpu_check                       | Checks regular expressions against the output of `iscpu`{.literal}. Accepts arguments in the form: REGEX1, STR1, REGEX2, STR2, ...​\[, STR_FALLBACK\]. If REGEX1 matches something in the output, it expands to STR1; if REGEX2 matches, it expands to STR2. It stops on the first match. If no regular expression matches, it expands to `STR_FALLBACK`{.literal} or an empty string if no fallback is provided. |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | package2cpus                      | Provides a CPU device list for a package (socket).                                                                                                                                                                                                                                                                                                                                                               |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | package2uncores                   | Provides an uncore device list for a package (socket).                                                                                                                                                                                                                                                                                                                                                           |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | regex_search_ternary              | Ternary regular expression operator. Takes arguments in the form: STR1, REGEX, STR2, STR3. If REGEX matches STR1 (`re.search`{.literal} is used), STR2 is returned; otherwise, STR3 is returned.                                                                                                                                                                                                                 |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | log                               | Expands to the concatenation of arguments and logs the result, useful for debugging.                                                                                                                                                                                                                                                                                                                             |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | kb2s                              | Converts KB to disk sectors.                                                                                                                                                                                                                                                                                                                                                                                     |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | s2kb                              | Converts disk sectors to KB.                                                                                                                                                                                                                                                                                                                                                                                     |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | strip                             | Creates a string from all passed arguments and deletes both leading and trailing white spaces.                                                                                                                                                                                                                                                                                                                   |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | virt_check                        | Checks whether TuneD is running inside a virtual machine (VM) or on bare metal. Inside a VM, the function returns the first argument. On bare metal, the function returns the second argument, even in case of an error.                                                                                                                                                                                         |
    +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    : Table 2.1. Available built-in functions:

    Show more

### [2.7. TuneD plugins](#tuned-plug-ins) {#tuned-plugins .title}

TuneD profiles use plugins to monitor or optimize different devices on the system.

TuneD uses two types of plugins:

Monitoring plugins
:   Used for gathering system data such as, CPU load, disk I/O, and network traffic. The output of the monitoring plugins can be used by tuning plugins for dynamic tuning. Monitoring plugins are automatically instantiated whenever their metrics are needed by any of the enabled tuning plugins. The available monitoring plugins are:

`disk`{.literal}
:   Gets disk load (number of IO operations) per device and measurement interval.

`net`{.literal}
:   Gets network load (number of transferred packets) per network card and measurement interval.

`load`{.literal}
:   Gets CPU load per CPU and measurement interval.

Tuning plugins
:   Each tuning plugin tunes an individual subsystem and takes several parameters that are populated from the TuneD profiles. Each subsystem can have multiple devices, such as multiple CPUs or network cards, handled by individual instances of the tuning plugins. Specific settings for individual devices are also supported. The available tuning plugins are:

`acpi`{.literal}
:   Configures the ACPI driver. Use the `platform_profile`{.literal} option to set the ACPI platform profile `sysfs`{.literal} attribute. It is a generic `power/performance`{.literal} preference API for other drivers. Multiple profiles can be specified, separated by `|`{.literal}. The first available profile is selected.

`audio`{.literal}
:   Sets the autosuspend timeout for audio codecs to the value specified by the timeout option. Currently, the `snd_hda_intel`{.literal} and `snd_ac97_codec`{.literal} codecs are supported. The value 0 means that autosuspend is disabled. You can also enforce the controller reset by setting the Boolean option reset_controller to `true`{.literal}.

`bootloader`{.literal}
:   Adds options to the kernel command line. This plugin supports only the GRUB boot loader. Customized non-standard location of the GRUB configuration file can be specified by the `grub2_cfg_file`{.literal} option. The kernel options are added to the current GRUB configuration and its templates. The system needs to be rebooted for the kernel options to take effect.

`cpu`{.literal}
:   Manages CPU governor and power settings by setting the CPU governor to the value specified by the `governor`{.literal} option. It dynamically changes the Power Management Quality of Service (PM QoS) CPU Direct Memory Access (DMA) latency, according to the CPU load.

`disk`{.literal}
:   Manages disk settings such as `apm`{.literal}, `scheduler_quantum`{.literal}, `readahead`{.literal}, `readahead_multiply`{.literal}, `spindown`{.literal}.

`eeepc_she`{.literal}
:   Dynamically sets the front-side bus (FSB) speed according to the CPU load.

`irq`{.literal}
:   Handles individual interrupt requests (IRQ) as devices and multiple plugin instances can be defined, each addressing different devices or irqs. The device names used by the plugin are `irq<n>`{.literal}, where `<n>`{.literal} is the IRQ number. The special device `DEFAULT`{.literal} controls values written to `/proc/irq/default_smp_affinity`{.literal}, which applies to all non-active IRQs.

`irqbalance`{.literal}
:   Manages settings for `irqbalance`{.literal}. The plugin configures CPUs which should be skipped when rebalancing IRQs in `/etc/sysconfig/irqbalance`{.literal}. It then restarts irqbalance only if it was previously running.

`modules`{.literal}
:   Applies custom kernel modules options. It can set parameters to kernel modules and creates `/etc/modprobe.d/tuned.conf`{.literal} file. The syntax is *`module`{.literal}*`=`{.literal}*`option1=value1 option2=value2…​`{.literal}* where *`module`{.literal}* is the module name and *`optionx=valuex`{.literal}* are module options which might be present.

`mounts`{.literal}
:   Enables or disables barriers for mounted filesystems.

`net`{.literal}
:   Configures Wake-on-LAN and interface speed by using the same syntax as the ethtool utility. Also, dynamically changes the interface speed according to the interface utilization.

`rtentsk`{.literal}
:   Avoids inter-processor interruptions caused by enabling or disabling static keys. It has no options. When included, **TuneD** keeps an open socket with timestamping enabled, thus keeping the static key enabled.

`selinux`{.literal}
:   Tunes SELinux options. SELinux decisions, such as allowing or denying access, are cached. This cache is known as the Access Vector Cache (AVC). When using these cached decisions, SELinux policy rules need to be checked less, which increases performance. The `avc_cache_threshold`{.literal .option} option adjusts the maximum number of AVC entries.

`systemd`{.literal}
:   Tunes systemd options. The `cpu_affinity`{.literal} option sets CPU affinity in `/etc/systemd/system.conf`{.literal}. This configures the CPU affinity for the service manager and the default CPU affinity for all forked off processes. Add a comma-separated list of CPUs with optional CPU ranges specified by the minus sign (`-`{.literal}).

`scsi_host`{.literal}
:   Tunes SCSI host settings (for example, `ALPM`{.literal}).

`scheduler`{.literal}
:   Offers a variety of options for the tuning of scheduling priorities, CPU core isolation, and process, thread, and IRQ affinities.

`script`{.literal}
:   Runs external script or binary when loading or unloading a profile.

`service`{.literal}
:   Handles various sysvinit, sysv-rc, openrc, and systemd services specified by the plugin options. Supported service handling commands are start, stop, enable, and disable.

`sysctl`{.literal}
:   Modifies kernel parameters. Use this plugin only if you want to change system settings that are not covered by other plugins available in TuneD. The syntax is *name=value*, where *name* is the same as the name provided by the `sysctl`{.literal} utility.

`sysfs`{.literal}
:   Sets various `sysfs`{.literal} settings specified by the plugin options. The syntax is *name=value*, where *name* is the `sysfs`{.literal} path to use.

`usb`{.literal}
:   Adjusts USB autosuspend timeout. The value `0`{.literal} means that autosuspend is disabled.

`uncore`{.literal}
:   Limits the maximum and minimum uncore frequency. The options `max_freq_khz`{.literal .option}, `min_freq_khz`{.literal .option} correspond to `sysfs`{.literal} files exposed by Intel uncore frequency driver. Their values can be specified in kHz or as a percentage of their configurable range.

`video`{.literal}
:   Sets various powersave levels on video cards. Currently, only the `Radeon`{.literal} cards are supported. The `powersave`{.literal} level can be specified by using the `radeon_powersave`{.literal} option. Supported values are, default, auto, low, mid, high, dynpm, dpm-battery, dpm-balanced, and dpm-perfomance.

`vm`{.literal}
:   Enables or disables transparent huge pages. Valid values for the transparent_hugepages option are: `always, never, madvise`{.literal}.

**Additional resources**

-   [Optimizing CPU Scheduling with the TuneD Scheduler Plugin (Red Hat Knowledgebase)](https://access.redhat.com/articles/7112533)

### [2.8. Creating a new TuneD profile](#creating-a-new-tuned-profile) {#creating-a-new-tuned-profile .title}

You can create a new TuneD profile to customize your requirements for performance optimization.

**Prerequisites**

-   The TuneD service is running. See [Installing and enabling TuneD](#installing-and-enabling-tuned "2.3. Installing and enabling TuneD") for details.

**Procedure**

1.  In the `/etc/tuned/profiles`{.literal} directory, create a new directory named the same as the profile that you want to create:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /etc/tuned/profiles/my-profile
    ```

2.  In the new directory, create a file named `tuned.conf`{.literal}.

3.  Edit the file and add a `[main]`{.literal} section and plug in definitions in it, according to your requirements. For example, see the configuration of the `balanced`{.literal} profile:

    ``` {.language-plaintext tabindex="-1"}
    [main]
    summary=General non-specialized TuneD profile

    [cpu]
    governor=conservative
    energy_perf_bias=normal

    [audio]
    timeout=10

    [video]
    radeon_powersave=dpm-balanced, auto

    [scsi_host]
    alpm=medium_power
    ```

4.  Activate the profile.

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile my-profile
    ```

**Verification**

-   View the profile is active and applied:

    ``` {.language-plaintext tabindex="-1"}
    $ tuned-adm active
    ```

    ``` {.language-plaintext tabindex="-1"}
    Current active profile: my-profile
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ tuned-adm verify
    ```

    ``` {.language-plaintext tabindex="-1"}
    Verification succeeded, current system settings match the preset profile. See tuned log file ('/var/log/tuned/tuned.log') for details.
    ```

### [2.9. Modifying an existing TuneD profile](#modifying-an-existing-tuned-profile) {#modifying-an-existing-tuned-profile .title}

You can modify the parameters of an existing profile to suit your custom requirements. A modified child profile can be created based on an existing TuneD profile.

**Prerequisites**

-   The TuneD service is running. See [Installing and enabling TuneD](#installing-and-enabling-tuned "2.3. Installing and enabling TuneD") for details.

**Procedure**

1.  In the `/etc/tuned/profiles`{.literal} directory, create a new directory named the same as the profile that you want to create:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /etc/tuned/profiles/modified-profile
    ```

2.  In the new directory, create a file named `tuned.conf`{.literal}, and set the \[main\] section as follows:

    ``` {.language-plaintext tabindex="-1"}
    [main]
    include=parent-profile
    ```

    Replace *parent-profile* with the name of the profile you are modifying, for example: `throughput-performance`{.literal}

3.  Include your profile modifications. For example, to lower swappiness in the `throughput-performance`{.literal} profile, change the value of `vm.swappiness`{.literal} to `5`{.literal}, instead of the default `10`{.literal}, use:

    ``` {.language-plaintext tabindex="-1"}
    [main]
    include=throughput-performance

    [sysctl]
    vm.swappiness=5
    ```

4.  Activate the profile.

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile modified-profile
    ```

**Verification**

-   View the profile is active and applied:

    ``` {.language-plaintext tabindex="-1"}
    $ tuned-adm active
    ```

    ``` {.language-plaintext tabindex="-1"}
    Current active profile: modified-profile
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ tuned-adm verify
    ```

    ``` {.language-plaintext tabindex="-1"}
    Verification succeeded, current system settings match the preset profile. See tuned log file ('/var/log/tuned/tuned.log') for details.
    ```

### [2.10. Enabling TuneD no-daemon mode](#enabling-tuned-no-daemon-mode) {#enabling-tuned-no-daemon-mode .title}

You can run TuneD in no-daemon mode, which does not require any resident memory. In this mode, TuneD applies the settings and then exits. However, note that this mode disables certain features, including D-Bus and hot-plug support, and rollback functionality for settings.

**Prerequisites**

-   You have root privileges or appropriate permissions to modify the system configuration.

**Procedure**

1.  Edit the `/etc/tuned/tuned-main.conf`{.literal} file with the following changes:

    ``` {.language-plaintext tabindex="-1"}
    sudo vi /etc/tuned/tuned-main.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    daemon = 0
    ```

2.  Save and close the file.

3.  Restart the tuned service or reapply or switch profile:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart tuned
    ```

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile <tuned_profile>
    ```

4.  Verify the tuned status:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm active
    ```

    ``` {.language-plaintext tabindex="-1"}
    It seems that tuned daemon is not running, preset profile is not activated.
    Preset profile: <tuned_profile>
    ```

### [2.11. Additional resources](#optimizing-system-performance-with-tuned_211-additional-resources) {#additional-resources .title}

-   [TuneD documentation](https://tuned-project.org/docs/manual.html)

## [Chapter 3. Setting the disk scheduler](#setting-the-disk-scheduler) {#chapter-3.-setting-the-disk-scheduler .title}

The disk scheduler is responsible for ordering the I/O requests submitted to a storage device. You can configure the scheduler in several different ways:

-   Set the scheduler using TuneD.
-   Set the scheduler using `udev`{.literal}.
-   Temporarily change the scheduler on a running system.

Note

In Red Hat Enterprise Linux, block devices support only multi-queue scheduling. This enables the block layer performance to scale well with fast solid-state drives (SSDs) and multi-core systems.

### [3.1. Available disk schedulers](#available-disk-schedulers) {#available-disk-schedulers .title}

Choosing the appropriate disk scheduler significantly impacts system performance, responsiveness, and the efficiency of I/O operations. Evaluate each scheduler's characteristics to select the most suitable option for your specific workload and hardware.

The following multi-queue disk schedulers are supported in Red Hat Enterprise Linux:

`none`{.literal}
:   Implements a first-in first-out (FIFO) scheduling algorithm. It merges requests at the generic block layer through a simple last-hit cache.

`mq-deadline`{.literal}

:   Attempts to provide a guaranteed latency for requests from the point, at which requests reach the scheduler. The `mq-deadline`{.literal} scheduler sorts queued I/O requests into a read or write batch. Later, it schedules them in an increasing logical block addressing (LBA) order. By default, read batches take precedence over write batches, because applications get block on read I/O operations. After processing a batch, `mq-deadline`{.literal} checks for write starvation. It then schedules the next read or write batch accordingly.

    This scheduler is suitable for most use cases, but particularly those in which write operations are mostly asynchronous.

`bfq`{.literal}

:   Targets desktop systems and interactive tasks. The `bfq`{.literal} scheduler ensures that a single application is never using all of the bandwidth. In effect, the storage device is always as responsive as if it was idle. In its default configuration, `bfq`{.literal} focuses on delivering the lowest latency rather than achieving the maximum throughput.

    `bfq`{.literal} is based on `cfq`{.literal} code. The scheduler assigns a budget of sectors to each process instead of granting a fixed time slice of disk access. This scheduler is suitable when copying large files do not make the system unresponsive.

`kyber`{.literal}
:   The scheduler achieves a latency goal by calculating the latency of every request in the block I/O layer. You can configure the target latencies for read, in the case of cache-misses, and synchronous write requests. This scheduler is suitable for fast devices, for example NVMe, SSD, or other low latency devices.

Default disk scheduler
:   Block devices use the default disk scheduler unless you specify another scheduler.

Note

For non-volatile Memory Express (NVMe) block devices specifically, the default scheduler is none and Red Hat recommends not changing this.

The kernel selects a default disk scheduler based on the type of device. The automatically selected scheduler is typically the optimal setting. If you require a different scheduler, use `udev`{.literal} rules or the TuneD application to configure it. Match the selected devices and switch the scheduler only for those devices.

### [3.2. Different disk schedulers for different use cases](#different-disk-schedulers-for-different-use-cases) {#different-disk-schedulers-for-different-use-cases .title}

Use these disk schedulers as a starting point before performing analysis and tuning.

+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Use case                                                     | Disk scheduler                                                                                                       |
+:=============================================================+:=====================================================================================================================+
| Traditional HDD with a SCSI interface                        | Use `mq-deadline`{.literal} or `bfq`{.literal}.                                                                      |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| High-performance SSD or a CPU-bound system with fast storage | Use `none`{.literal}, especially when running enterprise applications. Alternatively, use `kyber`{.literal}.         |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Desktop or interactive tasks                                 | Use `bfq`{.literal}.                                                                                                 |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Virtual guest                                                | Use `mq-deadline`{.literal}. With a host bus adapter (HBA) driver that is multi-queue capable, use `none`{.literal}. |
+--------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

: Table 3.1. Disk scheduler recommendations by use case

Show more

### [3.3. Determining the active disk scheduler](#determining-the-active-disk-scheduler) {#determining-the-active-disk-scheduler .title}

You can view the disk scheduler that is currently active on a given block device.

**Procedure**

-   Read the content of the `/sys/block/device/queue/scheduler`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/block/device/queue/scheduler
    ```

    ``` {.language-plaintext tabindex="-1"}
    [mq-deadline] kyber bfq none
    ```

    In the file name, replace *device* with the block device name, for example `sdc`{.literal}. The active scheduler is listed in square brackets (`[ ]`{.literal}).

### [3.4. Setting the disk scheduler using TuneD](#setting-the-disk-scheduler-using-tuned) {#setting-the-disk-scheduler-using-tuned .title}

You can create and enable a TuneD profile that sets a given disk scheduler for selected block devices. The setting persists across system reboots.

When creating a TuneD profile to set a disk scheduler, replace:

-   *device* with the name of the block device, for example `sdf`{.literal} and
-   *selected-scheduler* with the disk scheduler that you want to set for the device, for example *bfq*.

**Prerequisites**

-   The TuneD service is installed and enabled. For details, see [Installing and enabling TuneD](#installing-and-enabling-tuned "2.3. Installing and enabling TuneD").

**Procedure**

1.  Optional: Select an existing TuneD profile on which your profile will be based. For a list of available profiles, see [TuneD profiles distributed with RHEL](#tuned-profiles-distributed-with-rhel "2.1. TuneD profiles distributed with RHEL").

2.  To see which profile is currently active, use:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm active
    ```

3.  Create a new directory to hold your TuneD profile:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /etc/tuned/profiles/<new_profile>
    ```

4.  Find the system unique identifier of the selected block device:

    ``` {.language-plaintext tabindex="-1"}
    # udevadm info --query=property --name=/dev/device | grep -E '(WWN|SERIAL)'
    ```

    ``` {.language-plaintext tabindex="-1"}
    ID_WWN=0x5002538d00000000_
    ID_SERIAL=Generic-_SD_MMC_20120501030900000-0:0
    ID_SERIAL_SHORT=20120501030900000
    ```

    Note

    This command returns all values identified as a World Wide Name (WWN) or serial number associated with the specified block device. Although using a WWN is preferred, it is not always available for every device. In such cases, you can use any value returned by the example command as the device system's unique ID.

5.  Create the `/etc/tuned/profiles/`{.literal}*`<new_profile>`{.literal}*`/tuned.conf`{.literal} configuration file. In the file, set the following options:

    a.  Optional: Include an existing profile:

        ``` {.language-plaintext tabindex="-1"}
        [main]
        include=<existing-profile>
        ```

    b.  Set the selected disk scheduler for the device that matches the WWN identifier:

        ``` {.language-plaintext tabindex="-1"}
        [disk]
        devices_udev_regex=IDNAME=device system unique id
        elevator=selected-scheduler
        ```

        Here:

        -   Replace *IDNAME* with the name of the identifier being used (for example, *ID_WWN*).

        -   Replace device system unique id with the value of the chosen identifier (for example, `0x5002538d00000000`{.literal}). To match multiple devices in the *devices_udev_regex* option, enclose the identifiers in parentheses and separate them with vertical bars:

            ``` {.language-plaintext tabindex="-1"}
            devices_udev_regex=(ID_WWN=0x5002538d00000000)|(ID_WWN=0x1234567800000000)
            ```

6.  Enable your profile:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile <new_profile>
    ```

**Verification**

1.  Verify that the TuneD profile is active and applied:

    ``` {.language-plaintext tabindex="-1"}
    $ tuned-adm active
    ```

    ``` {.language-plaintext tabindex="-1"}
    Current active profile: <profile>
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ tuned-adm verify
    ```

    ``` {.language-plaintext tabindex="-1"}
    Verification succeeded, current system settings match the preset profile.
    See TuneD log file ('/var/log/tuned/tuned.log') for details.
    ```

2.  Read the contents of the `/sys/block/device/queue/scheduler`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /sys/block/device/queue/scheduler
    ```

    ``` {.language-plaintext tabindex="-1"}
    [mq-deadline] kyber bfq none
    ```

    In the file name, replace *device* with the block device name, for example *sdc*. The active scheduler is listed in square brackets (`[]`{.literal}).

**Additional resources**

-   [Modifying an existing TuneD profile](#modifying-an-existing-tuned-profile "2.9. Modifying an existing TuneD profile")

### [3.5. Setting the disk scheduler using udev rules](#setting-the-disk-scheduler-using-udev-rules) {#setting-the-disk-scheduler-using-udev-rules .title}

You can set a given disk scheduler for specific block devices by using the `udev`{.literal} rules. The setting persists across system reboots.

When configuring `udev`{.literal} rules to set a disk scheduler, replace:

-   *device* with the name of the block device, for example `sdf`{.literal} and
-   *selected-scheduler* with the disk scheduler that you want to set for the device, for example `bfq`{.literal}.

**Procedure**

1.  Find the system unique identifier of the block device:

    ``` {.language-plaintext tabindex="-1"}
    # $ udevadm info --name=/dev/device | grep -E '(WWN|SERIAL)'
    ```

    ``` {.language-plaintext tabindex="-1"}
    E: ID_WWN=0x5002538d00000000
    E: ID_SERIAL=Generic-_SD_MMC_20120501030900000-0:0
    E: ID_SERIAL_SHORT=20120501030900000
    ```

    Note

    This command returns all values identified as a World Wide Name (WWN) or serial number associated with the specified block device. Although using a WWN is preferred, it is not always available for every device. In such cases, you can use any value returned by the example command as the device system's unique ID.

2.  To configure the `udev`{.literal} rule, create the `/etc/udev/rules.d/99-scheduler.rules`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    ACTION=="add|change", SUBSYSTEM=="block", ENV{IDNAME}=="device system unique id", ATTR{queue/scheduler}="selected-scheduler"
    ```

    Here:

    -   Replace *IDNAME* with the name of the identifier being used (for example, `ID_WWN`{.literal}).
    -   Replace device system unique id with the value of the chosen identifier (for example, `0x5002538d00000000`{.literal}).

3.  Reload `udev`{.literal} rules:

    ``` {.language-plaintext tabindex="-1"}
    # udevadm control --reload-rules
    ```

4.  Apply the scheduler configuration:

    ``` {.language-plaintext tabindex="-1"}
    # udevadm trigger --type=devices --action=change
    ```

**Verification**

-   Verify the active scheduler:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/block/device/queue/scheduler
    ```

### [3.6. Temporarily setting a scheduler for a specific disk](#temporarily-setting-a-scheduler-for-a-specific-disk) {#temporarily-setting-a-scheduler-for-a-specific-disk .title}

You can set a given disk scheduler for specific block devices. The setting does not persist across system reboots.

**Procedure**

-   Write the name of the selected scheduler to the `/sys/block/device/queue/scheduler`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # echo selected-scheduler > /sys/block/device/queue/scheduler
    ```

    In the file name, replace *device* with the block device name, for example sdc.

**Verification**

-   Verify that the scheduler is active on the device.

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/block/device/queue/scheduler
    ```

## [Chapter 4. Configuring Performance Co-Pilot](#configuring-performance-co-pilot) {#chapter-4.-configuring-performance-co-pilot .title}

Performance Co-Pilot (PCP) is a suite of tools, services, and libraries for managing and measuring system-level performance. You use Python, Perl, C++, and C interfaces to add performance metrics.

Analysis tools use Python, C++, and C client APIs directly. Web applications can access performance data through a JSON interface. To analyze data patterns,compare live results with archived data.

Features of PCP

:   -   Light-weight distributed architecture useful during the centralized analysis of complex systems.
    -   Ability to monitor and manage real-time data.
    -   Ability to log and retrieve historical data.

PCP has the following components

:   -   The Performance Metric Collector Daemon (pmcd) collects performance data from the installed Performance Metric Domain Agents (PMDA). PMDAs can be individually loaded or unloaded on the system and are controlled by the PMCD on the same host.
    -   Various client tools, such as `pminfo`{.literal} or `pmstat`{.literal}, can retrieve, display, archive, and process this data on the same host or over the network.
    -   The `pcp`{.literal} and `pcp-system-tools`{.literal} packages provide the command-line tools and core functionality.
    -   The `pcp-gui`{.literal} package provides the graphical application `pmchart`{.literal}.
    -   The `grafana-pcp`{.literal} package provides powerful web-based visualizations and alerting with Grafana.

### [4.1. PCP installation methods](#pcp-installation-methods) {#pcp-installation-methods .title}

You can install PCP in several ways. The methods differ in how much configuration you perform yourself, how many metrics the system records by default, and how many hosts to set up at a time. Choose the method that matches the scale of your deployment and the resources you want PCP to consume.

The `pcp-zeroconf`{.literal} package

:   Installs PCP and applies a working configuration in a single step. The system records a default set of metrics into archived files without further configuration. Use this method for a default configuration and for the quickest way to start collecting performance data on a host.

    `pcp-zeroconf`{.literal} collects more metrics than the pcp package and it sets the sampling interval of many metrics to 10 seconds. This results in about 100-200 MB of compressed `pmlogger`{.literal} archives stored, per day. Archive files older than 14 days are deleted.

The `pcp`{.literal} package
:   Installs the PCP tools and services but leaves the configuration to you. You enable the services and select the metric groups that `pmlogger`{.literal} records. Use this method when you want PCP tailored to a specific use case, because collecting fewer metrics uses less CPU and disk space than the default `pcp-zeroconf`{.literal} configuration.

The `metrics`{.literal} RHEL system role
:   Configures PCP remotely on multiple managed nodes by using Ansible. Use this method when you administer a group of hosts and want a consistent PCP configuration across them.

**Additional resources**

-   [Install PCP by using pcp-zeroconf](#installing-pcp-with-pcp-zeroconf "4.3. Install PCP by using pcp-zeroconf")
-   [Install and enable PCP manually](#installing-and-enabling-pcp "4.4. Install and enable PCP manually")
-   [Configure Performance Co-Pilot by using the metrics RHEL system role](#configuring-performance-co-pilot-by-using-the-metrics-rhel-system-role "4.7. Configuring Performance Co-Pilot by using the metrics RHEL system role")

### [4.2. PCP deployment architectures](#pcp-deployment-architectures) {#pcp-deployment-architectures .title}

PCP supports multiple deployment architectures, based on the scale of the PCP deployment, and offers many options to accomplish advanced configurations.

Available scaling deployment configuration variants, determined by sizing factors and configuration options, include the following:

Localhost
:   Each service runs locally on the monitored machine. Starting a service without any configuration changes results in a default standalone deployment on the localhost. This configuration does not support scaling beyond a single node. However, Valkey can also run in a highly available and scalable clustered mode, where data is shared across multiple hosts. You can also deploy a Valkey cluster in the cloud or use a managed Valkey cluster from a cloud provider.

Decentralized
:   The only difference between localhost and decentralized configuration is the centralized Valkey service. In this model, the host runs pmlogger service on each monitored host and retrieves metrics from a local pmcd instance. A local pmproxy service then exports the performance metrics to a central Valkey instance.

**Figure 4.1. Decentralized logging**

Centralized logging - `pmlogger`{.literal} farm
:   For resource-constrained hosts, use a `pmlogger`{.literal} farm. This deployment is also called centralized logging. A single logger host runs `pmlogger`{.literal} processes to collect metrics from multiple remote hosts. The centralized logger host runs the `pmproxy`{.literal} service, which discovers the resulting PCP archives and loads the metric data into a Valkey instance.

**Figure 4.2. Centralized logging - `pmlogger`{.literal} farm**

Federated - multiple `pmlogger`{.literal} farms
:   For large scale deployments, deploy multiple pmlogger farms in a federated fashion. For example, one pmlogger farm per rack or data center. Each pmlogger farm loads the metrics into a central Valkey instance.

**Figure 4.3. Federated - multiple `pmlogger`{.literal} farms**

Note

By default, the deployment configuration for Valkey is standalone, localhost. However, Valkey can optionally perform in a highly-available and highly scalable clustered fashion, where data is shared across multiple hosts. Another option is to deploy a Valkey cluster in the cloud, or to use a managed Valkey cluster from a cloud provider.

### [4.3. Install PCP by using pcp-zeroconf](#installing-pcp-with-pcp-zeroconf) {#install-pcp-by-using-pcp-zeroconf .title}

Install and configure PCP in a single step with the `pcp-zeroconf`{.literal} package. Once the `pcp-zeroconf`{.literal} package is installed, the system records the default set of metrics into archived files. This is the suggested method for a default configuration.

Because `pcp-zeroconf`{.literal} collects more metrics than the `pcp`{.literal} package and sets the sampling interval to 10 seconds instead of 60 seconds it produces larger pmlogger archives. To collect a smaller set of metrics, you can install the `pcp`{.literal} package and configure it manually instead.

Note

The `pcp-zeroconf`{.literal} package is designed specifically for standalone, localhost deployments. If you require another deployment architecture, such as a distributed or federated setup, you must configure PCP manually instead of using `pcp-zeroconf`{.literal}. While RHEL system roles can assist with distributed deployments in certain scenarios, they do not encompass all configuration options that PCP supports for distributed and federated architectures.

**Procedure**

-   Install the `pcp-zeroconf`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp-zeroconf
    ```

**Verification**

-   Ensure that the pmlogger service is active, and starts archiving the metrics:

    ``` {.language-plaintext tabindex="-1"}
    # pcp | grep pmlogger
    ```

    ``` {.language-plaintext tabindex="-1"}
    pmlogger: primary logger: /var/log/pcp/pmlogger/localhost.localdomain/20200401.00.12
    ```

**Additional resources**

-   [PCP installation methods](#pcp-installation-methods "4.1. PCP installation methods")
-   [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually")
-   [Monitoring performance with Performance Co-Pilot](#monitoring-performance-with-performance-co-pilot "Chapter 7. Monitoring performance with Performance Co-Pilot")

### [4.4. Install and enable PCP manually](#installing-and-enabling-pcp) {#install-and-enable-pcp-manually .title}

Install the `pcp`{.literal} package and enable the PCP monitoring services yourself when you want to select which metrics the system collects.

Unlike `pcp-zeroconf`{.literal}, the base `pcp`{.literal} RPM does not automatically pull in additional RPM packages to collect specific metric groups, such as `openmetrics`{.literal}, `opentelemetry`{.literal}, or `nfsclient`{.literal}. Collecting fewer metrics uses less CPU and disk space than the default `pcp-zeroconf`{.literal} configuration. To install and configure PCP in a single step instead, see [Install PCP by using pcp-zeroconf](#installing-pcp-with-pcp-zeroconf "4.3. Install PCP by using pcp-zeroconf").

**Procedure**

1.  Install the pcp package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp
    ```

2.  Enable and start the pmcd service on the host machine:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable pmcd
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pmcd
    ```

**Verification**

-   Verify if the PMCD process is running on the host:

    ``` {.language-plaintext tabindex="-1"}
    # pcp
    ```

    ``` {.language-plaintext tabindex="-1"}
    Performance Co-Pilot configuration on arm10.local:

     platform: Linux arm10.local 6.12.0-55.13.1.el10_0.aarch64 #1 SMP PREEMPT_DYNAMIC Mon May 19 07:29:57 UTC 2025 aarch64
     hardware: 4 cpus, 1 disk, 1 node, 3579MB RAM
     timezone: JST-9
     services: pmcd
         pmcd: Version 6.3.7-1, 12 agents, 6 clients
         pmda: root pmcd proc pmproxy xfs linux nfsclient mmv kvm jbd2
               dm openmetrics
    ```

**Additional resources**

-   [Deploy minimal configuration for archiving collected metrics](#deploying-a-minimal-pcp-setup "4.6. Deploying minimal configuration for archiving collected metrics")
-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")

### [4.5. PCP archive rotation, compression, and comparison](#pcp-archive-rotation-compression-and-comparison) {#pcp-archive-rotation-compression-and-comparison .title}

Performance Co-Pilot (PCP) stores collected metrics in archive files for historical performance analysis. To manage storage and simplify long-term retention, PCP rotates and compresses archives daily. Compare archived performance data from different periods to identify changes in system behavior.

PCP rotates local archives daily by using the `pmlogger_daily`{.literal} utility, which is typically started shortly after midnight by the `pmlogger_daily.timer`{.literal} systemd unit. During daily processing, PCP rotates active archives, optionally merges completed daily archives, and compresses older archive volumes to reduce disk space usage. The `pmlogcompress`{.literal} utility performs archive compression according to the settings in the `pmlogger`{.literal} control configuration.

When `pmlogger`{.literal} runs as a service, archive files are created with a base name in the `YYYYMMDD.HH.MM`{.literal} format, for example, `20260527.00.10`{.literal}. After daily processing, archive volumes can include additional suffixes such as .`bz2`{.literal} or `.xz`{.literal}, indicating that the files have been compressed.

In addition to archive maintenance, PCP provides tools for analyzing historical performance data. The `pmdiff`{.literal} utility compares average metric values between two archives and highlights metrics whose values differ significantly. This comparison is useful for identifying performance regressions, workload changes, or resource utilization differences between days. By default, `pmdiff`{.literal} reports metrics whose averages have at least doubled or halved relative to each other, although you can adjust this threshold when performing comparisons.

Together, archive rotation, compression, and comparison capabilities help maintain manageable archive storage while enabling efficient analysis of historical system performance data.

Factors affecting scaling in PCP logging

:   -   Remote system size

        You can use remote hardware such as CPUs, disks, and network interfaces, determines the volume of data collected by each `pmlogger`{.literal} instance.

    -   Logged metrics

        The number and types of logged metrics significantly affect storage requirements. In particular, the `per-process proc.*`{.literal} metrics require a large amount of disk space. For example, a standard `pcp-zeroconf`{.literal} logging at 10-second intervals uses 11 MB. Enabling `proc`{.literal} metrics increases this to 155 MB. Additionally, the number of CPUs, block devices, and network interfaces impacts storage capacity requirements.

    -   Logging interval

        The frequency of metric logging determines storage usage. The expected daily PCP archive file sizes for each `pmlogger`{.literal} instance are recorded in the `pmlogger.log`{.literal} file. PCP archives typically compress at 10:1. Use this ratio to estimate long-term disk space requirements for uncompressed data.

    -   Managing archive updates with `pmlogrewrite`{.literal}

        After PCP upgrades, `pmlogrewrite`{.literal} updates existing archives if changes are detected in the metric metadata between versions. The time required for this process scales linearly with the number of stored archives.

**Additional resources**

-   [System services and tools distributed with PCP](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/configuring-performance-co-pilot#system-services-and-tools-distributed-with-pcp)

### [4.6. Deploying minimal configuration for archiving collected metrics](#deploying-a-minimal-pcp-setup) {#deploying-minimal-configuration-for-archiving-collected-metrics .title}

You can configure PCP to archive performance metrics collected on the local system by using a minimal `pmlogger`{.literal} configuration. The system stores these archives under `/var/log/pcp/pmlogger/`{.literal}. You can analyze archives with PCP tools such as `pmlogsummary`{.literal} and `pmdiff`{.literal}.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").

**Procedure**

1.  Update the `pmlogger`{.literal} configuration by reprobing the default metric groups against the local `pmcd`{.literal} instance:

    ``` {.language-plaintext tabindex="-1"}
    # pmlogconf -r /var/lib/pcp/config/pmlogger/config.default
    ```

    `pmlogconf`{.literal} might prompt to enable or disable groups of related metrics. Accept the defaults for a minimal configuration, or enable only the groups you need.

2.  Start or restart the `pmlogger`{.literal} service to apply the updated configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart pmlogger.service
    ```

3.  Optional: If `pmlogger`{.literal} is not running yet, start it.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pmlogger.service
    ```

4.  Verify that `pmlogger`{.literal} is writing archives. List the archive directory for the local host:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -l /var/log/pcp/pmlogger/$(hostname)/
    ```

    Example output:

    ``` {.language-plaintext tabindex="-1"}
    -rw-r--r--. 1 pcp pcp 1899948 May 27 12:55 20260527.11.59.0
    -rw-r--r--. 1 pcp pcp    1640 May 27 12:54 20260527.11.59.index
    -rw-r--r--. 1 pcp pcp  339929 May 27 12:54 20260527.11.59.meta
    lrwxrwxrwx. 1 pcp pcp     375 May 27 11:59 Latest
    -rw-r--r--. 1 pcp pcp   27452 May 27 11:59 pmlogger.log
    ```

    The archive base name is the shared prefix of the `.index`{.literal}, `.meta`{.literal}, and volume files (for example, `20260527.11.59`{.literal}). Pass this path, without a file suffix, to PCP archive tools.

5.  Summarize metrics from the current archive to confirm that data is being recorded. Use the archive base name from the earlier step:

    ``` {.language-plaintext tabindex="-1"}
    $ pmlogsummary /var/log/pcp/pmlogger/$(hostname)/20260527.11.59 -a disk.dev.read disk.dev.write
    ```

    Example output:

    ``` {.language-plaintext tabindex="-1"}
    Log Label (Log Format Version 3)
    Performance metrics from host hostname.example.com
      commencing Tue May 27 11:59:00.000 2026
      ending     Tue May 27 12:55:00.000 2026
    disk.dev.read ["sda"] 125.4 124.8 0.0 0.0 3300 [] 0 [] 0 count / sec
    disk.dev.write ["sda"] 42.1 41.9 0.0 0.0 3300 [] 0 [] 0 count / sec
    ```

    If `pmlogsummary`{.literal} reports metrics with non-zero averages over the archive interval, `pmlogger`{.literal} is archiving performance data successfully.

### [4.7. Configuring Performance Co-Pilot by using the metrics RHEL system role](#configuring-performance-co-pilot-by-using-the-metrics-rhel-system-role) {#configuring-performance-co-pilot-by-using-the-metrics-rhel-system-role .title}

You can use Performance Co-Pilot (PCP) to monitor many metrics, such as CPU utilization and memory usage. For example, this can help to identify resource and performance bottlenecks. By using the `metrics`{.literal} RHEL system role, you can remotely configure PCP on multiple hosts to record metrics.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Monitoring performance metrics
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure Performance Co-Pilot
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.metrics
          vars:
            metrics_retention_days: 14
            metrics_manage_firewall: true
            metrics_manage_selinux: true
    ```

    The settings specified in the example playbook include the following:

    `metrics_retention_days: `{.literal}*`<number>`{.literal}*
    :   Sets the number of days after which the `pmlogger_daily`{.literal} systemd timer removes old PCP archives.

    `metrics_manage_firewall: `{.literal}*`<true|false>`{.literal}*
    :   Defines whether the role opens the required ports in the `firewalld`{.literal} service. If you want to remotely access PCP on the managed nodes, set this variable to `true`{.literal}.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.metrics/README.md`{.literal} file on the control node.

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

-   Query a metric, for example:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'pminfo -f kernel.all.load'
    ```

**Next step**

-   Optional: [Configure Grafana to monitor PCP hosts and visualize metrics](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/configuring-performance-monitoring-with-pcp-by-using-rhel-system-roles#setting-up-grafana-by-using-the-metrics-rhel-system-role-to-monitor-multiple-hosts-with-performance-co-pilot).

### [4.8. System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp) {#system-services-and-tools-distributed-with-pcp .title}

The basic package `pcp`{.literal} includes the system services and basic tools. You can install additional tools that are provided with the `pcp-system-tools`{.literal}, `pcp-gui`{.literal}, and `pcp-devel`{.literal} packages.

**Roles of system services distributed with PCP**

`pmcd`{.literal}
:   The Performance Metric Collector Daemon.

`pmie`{.literal}
:   The Performance Metrics Inference Engine.

`pmlogger`{.literal}
:   The performance metrics logger.

`pmproxy`{.literal}
:   The realtime and historical performance metrics proxy, time series query and REST API service.

**Tools distributed with base PCP package**

`pcp`{.literal}
:   Displays the current status of a Performance Co-Pilot installation.

`pcp-check`{.literal}
:   Activates, or deactivates core and optional components, such as `pmcd`{.literal}, `pmlogger`{.literal}, `pmproxy`{.literal}, and PMDAs.

`pcp-vmstat`{.literal}
:   Provides a high-level system performance overview every 5 seconds. Displays information about processes, memory, paging, block IO, traps, and CPU activity.

`pmconfig`{.literal}
:   Displays the values of configuration parameters.

`pmdiff`{.literal}
:   Compares average metric values across two archives within a time window to identify potential performance regressions.

`pmdumplog`{.literal}
:   Displays control, metadata, index, and state information from a Performance Co-Pilot archive file.

`pmfind`{.literal}
:   Finds PCP services on the network.

`pmie`{.literal}
:   An inference engine that periodically evaluates a set of arithmetic, logical, and rule expressions. The metrics are collected either from a live system, or from a Performance Co-Pilot archive file.

`pmieconf`{.literal}
:   Displays or sets configurable pmie variables.

`pmiectl`{.literal}
:   Manages non-primary instances of pmie.

`pminfo`{.literal}
:   Displays information about performance metrics. The metrics are collected either from a live system, or from a Performance Co-Pilot archive file.

`pmlc`{.literal}
:   Interactively configures active pmlogger instances.

`pmlogcheck`{.literal}
:   Identifies invalid data in a Performance Co-Pilot archive file.

`pmlogconf`{.literal}
:   Creates and modifies a pmlogger configuration file.

`pmlogctl`{.literal}
:   Manages non-primary instances of pmlogger.

`pmloglabel`{.literal}
:   Verifies, modifies, or repairs the label of a Performance Co-Pilot archive file.

`pmlogsummary`{.literal}
:   Calculates statistical information about performance metrics stored in a Performance Co-Pilot archive file.

`pmprobe`{.literal}
:   Determines the availability of performance metrics.

`pmsocks`{.literal}
:   Provides access to a Performance Co-Pilot hosted through a firewall.

`pmstat`{.literal}
:   Periodically displays a brief summary of system performance.

`pmstore`{.literal}
:   Modifies the values of performance metrics.

`pmseries`{.literal}
:   Fast, scalable time series querying, using the facilities of PCP and a distributed key-value data store such as [Valkey](https://valkey.io).

`pmtrace`{.literal}
:   Provides a command-line interface to the trace PMDA.

`pmval`{.literal}
:   An updating display of the current value of any performance metric.

**Tools distributed with the separately installed pcp-system-tools package**

`pcp-atop`{.literal}
:   Shows the system-level occupation of the most critical hardware resources from the performance point of view: CPU, memory, disk, and network.

`pcp-atopsar`{.literal}
:   Generates a system-level activity report over a variety of system resource utilization. The report is generated from a raw logfile previously recorded using pmlogger or the -w option of pcp-atop.

`pcp-dmcache`{.literal}
:   Displays information about configured Device Mapper Cache targets. Metrics include device IOPS, utilization, and read/write hit/miss rates for each cache device.

`pcp-dstat`{.literal}
:   Displays metrics of one system at a time. To display metrics of multiple systems, use \--host option.

`pcp-free`{.literal}
:   Reports on free and used memory in a system.

`pcp-htop`{.literal}
:   Lists all processes running on a system along with their command-line arguments. It is similar to the `top`{.literal} command, with vertical and horizontal scrolling and mouse interaction.

`pcp-ipcs`{.literal}
:   Displays information about the inter-process communication (IPC) facilities that the calling process has read access for.

`pcp-mpstat`{.literal}
:   Reports CPU and interrupt-related statistics.

`pcp-numastat`{.literal}
:   Displays NUMA allocation statistics from the kernel memory allocator.

`pcp-pidstat`{.literal}
:   Displays information about individual tasks or processes running on the system. This includes CPU percentage, memory and stack usage, scheduling, and priority. Reports live data for the local host by default.

`pcp-shping`{.literal}
:   Samples and reports on the shell-ping service metrics exported by the pmdashping Performance Metrics Domain Agent (PMDA).

`pcp-ss`{.literal}
:   Displays socket statistics collected by the pmdasockets PMDA.

`pcp-tapestat`{.literal}
:   Reports I/O statistics for tape devices.

`pcp-uptime`{.literal}
:   Displays the system uptime, currently logged on users, and system load averages for the past 1, 5, and 15 minutes.

`pcp-verify`{.literal}
:   Inspects various aspects of a Performance Co-Pilot collector's configuration and ensures it is optimized for specific operations.

`pcp-iostat`{.literal}
:   Reports I/O statistics for SCSI devices (by default) or device-mapper devices (with the -x device-mapper option).

`pmrep`{.literal}
:   Reports on selected, easily customizable, performance metrics values.

**Tools distributed with the separately installed pcp-gui package**

`pmchart`{.literal}
:   Plots performance metrics values available through the facilities of the PCP.

`pmdumptext`{.literal}
:   Outputs the values of performance metrics collected live or from a PCP archive.

**Tools distributed with the separately installed pcp-devel package**

`pmclient`{.literal}
:   Displays high-level system performance metrics by using the Performance Metrics Application Programming Interface (PMAPI).

`pmdbg`{.literal}
:   Displays available Performance Co-Pilot debug control flags and their values.

`pmerr`{.literal}
:   Displays available Performance Co-Pilot error codes and their corresponding error messages.

`pcp-xsos`{.literal}
:   Gives a fast summary report for a system by using a single sample taken from either a PCP archive or live metrics from the system.

**Other tools distributed as a separate packages**

`pcp-geolocate`{.literal}
:   Discovers collector system geographical labels.

`pcp2openmetrics`{.literal}
:   A customizable performance metrics exporter tool from PCP to [Open Metrics](https://openmetrics.io) format. You can select any live or archived PCP metric for exporting by using either command line arguments or a configuration file.

### [4.9. Additional resources](#configuring-performance-co-pilot_49-additional-resources) {#additional-resources-1 .title}

-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")
-   [Index of Performance Co-Pilot (PCP) articles, solutions, tutorials, and white papers from Red Hat Customer Portal](https://access.redhat.com/articles/1145953)

## [Chapter 5. Configuring pmda-openmetrics](#configuring-pmda-openmetrics) {#chapter-5.-configuring-pmda-openmetrics .title}

Performance Co-Pilot (PCP) is a system for monitoring and managing system performance. It includes several built-in agents called Performance Metric Domain Agents (PMDAs). These agents collect metrics from applications and services, such as PostgreSQL, Apache HTTPD, and KVM virtual machines.

### [5.1. Overview of pmda-openmetrics](#overview-of-pmda-openmetrics) {#overview-of-pmda-openmetrics .title}

You can run custom or less common applications for which no out-of-the-box PMDA exists in the Red Hat repositories. In such cases, the `pmda-openmetrics`{.literal} agent exposes performance metrics from arbitrary applications by converting OpenMetrics-style text files into PCP-compatible metrics.

OpenMetrics is a widely adopted format used by Prometheus and other monitoring tools, which makes integration easier. You can run `pmda-openmetrics`{.literal} to do the following tasks:

-   Monitor custom applications that are not covered by existing PMDAs.
-   Integrate existing OpenMetrics or `Prometheus-exported`{.literal} metrics into the PCP framework.
-   Create quick models or test metrics for diagnostic or demonstration purposes.

### [5.2. Installing and configuring pmda-openmetrics](#installing-and-configuring-pmda-openmetrics) {#installing-and-configuring-pmda-openmetrics .title}

You must install and configure `pmda-openmetrics`{.literal} before you start using it. The following example demonstrates how to expose a single numeric value from a text file as a PCP metric by using `pmda-openmetrics`{.literal}.

**Prerequisites**

-   PCP is installed and `pmcd`{.literal} is running. For more information, see [Install PCP by using pcp-zeroconf](#installing-pcp-with-pcp-zeroconf "4.3. Install PCP by using pcp-zeroconf").

**Procedure**

1.  Install the `pmda-openmetrics`{.literal} PMDA.

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install pcp-pmda-openmetrics
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cd /var/lib/pcp/pmdas/openmetrics/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ./Install
    ```

2.  Create a sample OpenMetrics file.

    ``` {.language-plaintext tabindex="-1"}
    # echo 'var1 {var2="var3"} 42' > /tmp/example.txt
    ```

    Replace *example*.txt with the file name that you want to use.

3.  Verify that the file is created correctly.

    ``` {.language-plaintext tabindex="-1"}
    # cat /tmp/example.txt
    ```

4.  Register the metric file path with the OpenMetrics agent.

    ``` {.language-plaintext tabindex="-1"}
    # echo "file:///tmp/example.txt" > /etc/pcp/openmetrics/example.url
    ```

5.  Verify that the configuration is created correctly.

    ``` {.language-plaintext tabindex="-1"}
    # cat /etc/pcp/openmetrics/example.url
    ```

6.  Configure `systemd-tmpfiles`{.literal} to create the necessary symlinks.

    ``` {.language-plaintext tabindex="-1"}
    # echo 'L+ /var/lib/pcp/pmdas/openmetrics/config.d/example.url - - - - ../../../../../../etc/pcp/openmetrics/example.url' \ > /usr/lib/tmpfiles.d/pcp-pmda-openmetrics-cust.conf
    ```

7.  Verify that the symlinks are configured correctly.

    ``` {.language-plaintext tabindex="-1"}
    # cat /usr/lib/tmpfiles.d/pcp-pmda-openmetrics-cust.conf
    ```

8.  Create the symlinks by applying the tmpfiles configuration.

    ``` {.language-plaintext tabindex="-1"}
    # systemd-tmpfiles --create --remove /usr/lib/tmpfiles.d/pcp-pmda-openmetrics-cust.conf
    ```

9.  Verify that the symlinks are created correctly.

    ``` {.language-plaintext tabindex="-1"}
    # ls -al /var/lib/pcp/pmdas/openmetrics/config.d/
    ```

10. Verify that the metric is correctly reported.

    ``` {.language-plaintext tabindex="-1"}
    # pminfo -f openmetrics.example.var1
    ```

    ``` {.language-plaintext tabindex="-1"}
    inst [0 or "0 var2:var3"] value 42
    ```

**Verification**

-   Run `pcp`{.literal} and confirm that `openmetrics`{.literal} is listed.
-   Run `systemd-analyze cat-config tmpfiles.d`{.literal} and confirm that *`example`{.literal}*`.url`{.literal} appears in the output.
-   Use `pminfo`{.literal} to confirm the presence and value of the metric.

## [Chapter 6. Logging performance data with pmlogger](#logging-performance-data-with-pmlogger) {#chapter-6.-logging-performance-data-with-pmlogger .title}

With the PCP tool you can log the performance metric values and replay them later. You can use this data to perform retrospective performance analysis. Using the pmlogger tool, you can:

-   Create the archived logs of selected metrics on the system
-   Specify which metrics are recorded on the system and how often

### [6.1. Modifying the pmlogger configuration file with pmlogconf](#modifying-the-pmlogger-configuration-file-with-pmlogconf) {#modifying-the-pmlogger-configuration-file-with-pmlogconf .title}

When the `pmlogger`{.literal} service is running, PCP logs a default set of metrics on the host. Use the `pmlogconf`{.literal} utility to check the default configuration. If the `pmlogger`{.literal} configuration file does not exist, `pmlogconf`{.literal} creates it with a default metric values.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").

**Procedure**

1.  Create or modify the `pmlogger`{.literal} configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # pmlogconf -r /var/lib/pcp/config/pmlogger/config.default
    ```

2.  Follow `pmlogconf`{.literal} prompts to enable or disable groups of related performance metrics and to control the logging interval for each enabled group. For example,

    ``` {.language-plaintext tabindex="-1"}
    # pmlogconf -r /var/lib/pcp/config/pmlogger/config.default
    ```

    ``` {.language-plaintext tabindex="-1"}
    Group: per logical block device activity
    Log this group? [y]
    Logging interval? [default]
    ```

**Additional resources**

-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")

### [6.2. Configuring pmlogger manually](#configuring-pmlogger-manually) {#configuring-pmlogger-manually .title}

You can manually edit the `pmlogger`{.literal} configuration file to create a tailored logging configuration with specific metrics and intervals. The default configuration file is `/var/lib/pcp/config/pmlogger/config.default`{.literal}, which specifies the metrics logged by the primary logging instance.

With manual `pmlogger`{.literal} configuration, you can:

-   Record metrics which are not listed in the automatic configuration.
-   Choose custom logging frequencies.
-   Add **PMDA** with the application metrics.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").

**Procedure**

-   Open and edit the `/var/lib/pcp/config/pmlogger/config.default`{.literal} file to add specific metrics:

    ``` {.language-plaintext tabindex="-1"}
    # It is safe to make additions from here on ...
    #
    log mandatory on every 5 seconds {
        xfs.write
        xfs.write_bytes
        xfs.read
        xfs.read_bytes
    }
    log mandatory on every 10 seconds {
        xfs.allocs
        xfs.block_map
        xfs.transactions
        xfs.log
    }
    [access]
    disallow * : all;
    allow localhost : enquire;
    ```

**Additional resources**

-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")

### [6.3. Enabling the pmlogger service](#enabling-the-pmlogger-service) {#enabling-the-pmlogger-service .title}

The `pmlogger`{.literal} service must be started and enabled to log the metric values on the local machine.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").

**Procedure**

-   Start and enable the `pmlogger`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pmlogger
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable pmlogger
    ```

**Verification**

-   Verify that the `pmlogger`{.literal} service is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # pcp
    ```

    ``` {.language-plaintext tabindex="-1"}
     platform: Linux arm10.local 6.12.0-55.13.1.el10_0.aarch64 #1 SMP PREEMPT_DYNAMIC Mon May 19 07:29:57 UTC 2025 aarch64
     hardware: 4 cpus, 1 disk, 1 node, 3579MB RAM
     timezone: JST-9
     services: pmcd
         pmcd: Version 6.3.7-1, 12 agents, 6 clients
         pmda: root pmcd proc pmproxy xfs linux nfsclient mmv kvm jbd2
               dm openmetrics
     pmlogger: primary logger: /var/log/pcp/pmlogger/arm10.local/20250529.15.49
         pmie: primary engine: /var/log/pcp/pmie/arm10.local/pmie.log
    ```

    For more information, see the `/var/lib/pcp/config/pmlogger/config.default`{.literal} file.

**Additional resources**

-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")

### [6.4. Configuring a client system for metrics collection](#configuring-a-client-system-for-metrics-collection) {#configuring-a-client-system-for-metrics-collection .title}

You can configure a client system to enable a central server to collect performance metrics from clients running PCP.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").

**Procedure**

1.  Install the `pcp-system-tools`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp-system-tools
    ```

2.  Configure an IP address for pmcd:

    ``` {.language-plaintext tabindex="-1"}
    # echo "-i 192.168.4.62" >>/etc/pcp/pmcd/pmcd.options
    ```

    Replace *192.168.4.62* with the IP address, the client should listen on. By default, `pmcd`{.literal} is listening on the localhost.

3.  Configure the firewall to add the public zone permanently:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --zone=public --add-port=44321/tcp
    ```

    ``` {.language-plaintext tabindex="-1"}
    success
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

    ``` {.language-plaintext tabindex="-1"}
    success
    ```

4.  Set an SELinux boolean:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool -P pcp_bind_all_unreserved_ports on
    ```

5.  Enable the `pmcd`{.literal} and `pmlogger`{.literal} services:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable pmcd pmlogger
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart pmcd pmlogger
    ```

**Verification**

-   Verify that the `pmcd`{.literal} is correctly listening on the configured IP address:

    ``` {.language-plaintext tabindex="-1"}
    # ss -tlp | grep 44321
    ```

    ``` {.language-plaintext tabindex="-1"}
    LISTEN   0   5     127.0.0.1:44321   0.0.0.0:*   users:(("pmcd",pid=151595,fd=6))
    LISTEN   0   5  192.168.4.62:44321   0.0.0.0:*   users:(("pmcd",pid=151595,fd=0))
    LISTEN   0   5         [::1]:44321      [::]:*   users:(("pmcd",pid=151595,fd=7))
    ```

**Additional resources**

-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")

### [6.5. Configuring a central server to collect data](#configuring-a-central-server-to-collect-data) {#configuring-a-central-server-to-collect-data .title}

You can create a central server to collect metrics from clients running PCP.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").
-   Client is configured for metrics collection. For more information, see [Configuring a client system for metrics collection](#configuring-a-client-system-for-metrics-collection "6.4. Configuring a client system for metrics collection").

**Procedure**

1.  Install the `pcp-system-tools`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp-system-tools
    ```

2.  Create the `/etc/pcp/pmlogger/control.d/remote`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    # DO NOT REMOVE OR EDIT THE FOLLOWING LINE
    $version=1.1
    192.168.4.13 n n PCP_ARCHIVE_DIR/rhel7u4a -r -T24h10m -c config.rhel7u4a
    192.168.4.14 n n PCP_ARCHIVE_DIR/rhel6u10a -r -T24h10m -c config.rhel6u10a
    192.168.4.62 n n PCP_ARCHIVE_DIR/rhel8u1a -r -T24h10m -c config.rhel8u1a
    ```

    Replace *192.168.4.13*, *192.168.4.14* and *192.168.4.62* with the client IP addresses.

3.  Enable the pmcd and pmlogger services:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable pmcd pmlogger
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart pmcd pmlogger
    ```

**Verification**

-   Verify that you can access the latest archive file from each directory:

    ``` {.language-plaintext tabindex="-1"}
    # for i in /var/log/pcp/pmlogger/rhel*/*.0; do pmdumplog -L $i; done
    ```

    ``` {.language-plaintext tabindex="-1"}
    Log Label (Log Format Version 2)
    Performance metrics from host rhel6u10a.local
      commencing Mon Nov 25 21:55:04.851 2019
      ending     Mon Nov 25 22:06:04.874 2019
    Archive timezone: JST-9
    PID for pmlogger: 24002
    Log Label (Log Format Version 2)
    Performance metrics from host rhel7u4a
      commencing Tue Nov 26 06:49:24.954 2019
      ending     Tue Nov 26 07:06:24.979 2019
    Archive timezone: CET-1
    PID for pmlogger: 10941
    [..]
    ```

    The archive files from the `/var/log/pcp/pmlogger/`{.literal} directory can be used for further analysis and graphing.

**Additional resources**

-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")

### [6.6. Systemd units and pmlogger](#systemd-units-and-pmlogger) {#systemd-units-and-pmlogger .title}

The `pmlogger`{.literal} deployments, whether local or a remote farm, include several associated systemd service and timer units. These units monitor `pmlogger`{.literal} instances, restart failed processes, and manage archives through tasks like file compression.

The checking and housekeeping services typically deployed by pmlogger are:

pmlogger_daily.service
:   Runs daily, soon after midnight by default, to aggregate, compress, and rotate one or more sets of PCP archives. Also culls archives older than the limit, 2 weeks by default. Triggered by the `pmlogger_daily.timer`{.literal} unit, which is required by the `pmlogger.service`{.literal} unit.

pmlogger_check
:   Performs half-hourly checks that `pmlogger`{.literal} instances are running. Restarts any missing instances and performs any required compression tasks. Triggered by the `pmlogger_check.timer`{.literal} unit, which is required by the `pmlogger.service`{.literal} unit.

pmlogger_farm_check
:   Checks the status of all configured `pmlogger`{.literal} instances. Restarts any missing instances. Migrates all non-primary instances to the `pmlogger_farm`{.literal} service. Triggered by the `pmlogger_farm_check.timer`{.literal}, which is required by the `pmlogger_farm.service`{.literal} unit that is itself required by the `pmlogger`{.literal}.service unit.

These services are managed through a series of positive dependencies, meaning that they are all enabled upon activating the primary pmlogger instance. Note that while `pmlogger_daily.service`{.literal} is disabled by default, `pmlogger_daily.timer`{.literal} being active through the dependency with `pmlogger.service`{.literal} will trigger `pmlogger_daily.service`{.literal} to run.

`pmlogger_daily`{.literal} is also integrated with `pmlogrewrite`{.literal} for automatically rewriting archives before merging. This helps to ensure metadata consistency amid changing production environments and PMDAs. For example, updating `pmcd`{.literal} during logging can change metric semantics, creating new archives incompatible with previously recorded data. For more information, see the `pmlogrewrite(1)`{.literal} man page on your system.

### [6.7. Managing systemd services triggered by pmlogger](#managing-systemd-services-triggered-by-pmlogger) {#managing-systemd-services-triggered-by-pmlogger .title}

You can create an automated custom archive management system for data collected by your `pmlogger`{.literal} instances by using the control files.

The primary `pmlogger`{.literal} instance must be running on the same host as the `pmcd`{.literal} it connects to. You do not need to configure a primary instance. If a central host collects data from several `pmlogger`{.literal} instances connected to `pmcd`{.literal} instances running on remote hosts, a primary instance might not be required.

**Procedure**

-   Do one of the following:

    -   For the primary pmlogger instance, use `/etc/pcp/pmlogger/control.d/local`{.literal}

    -   For the remote hosts, use `/etc/pcp/pmlogger/control.d/`{.literal}*`remote`{.literal}*

        Replace *remote* with the file name that you want to use.

        The file should contain one line for each host to be logged. The default format of the primary logger instance that is automatically created looks similar to:

        ``` {.language-plaintext tabindex="-1"}
        # === LOGGER CONTROL SPECIFICATIONS ===
        #
        #Host        P?  S?    directory         args
        # local primary logger
        LOCALHOSTNAME    y   n    PCP_ARCHIVE_DIR/LOCALHOSTNAME    -r -T24h10m -c config.default -v 100Mb
        ```

        Where the fields are:

        Host
        :   The name of the host to be logged.

        P?
        :   Stands for "Primary?\". This field indicates if the host is the primary logger instance, **y**, or not, **n**. Only one primary logger is permitted. It must run on the same host as its connected `pmcd`{.literal} instance.

        S?
        :   Stands for "Socks?\". This field indicates if this logger instance needs to use the `SOCKS`{.literal} protocol to connect to `pmcd`{.literal} through a firewall, **y**, or not, **n**.

        directory
        :   All archives associated with this line are created in this directory.

        args
        :   Arguments passed to `pmlogger`{.literal}. The default values for the `args`{.literal} field are:

        -r
        :   Report the archive sizes and growth rate.

        T24h10m
        :   Specifies when to end logging for each day. This is typically the time when `pmlogger_daily.service`{.literal} runs. The default value of `24h10m`{.literal} indicates that logging should end 24 hours and 10 minutes after it begins, at the latest.

        -c config.default
        :   Specifies which configuration file to use. This defines what metrics to record.

        -v 100Mb
        :   Specifies the size at which point one data volume is filled and another is created. After it switches to the new archive, the previously recorded one will be compressed by either `pmlogger_daily`{.literal} or `pmlogger_check`{.literal}.

### [6.8. Replaying the PCP log archives with pmrep](#replaying-the-pcp-log-archives-with-pmrep) {#replaying-the-pcp-log-archives-with-pmrep .title}

After recording the metric data, you can replay the PCP log archives. To export the logs to text files and import them into spreadsheets, use PCP utilities such as `pcp2csv`{.literal}, `pcp2xml`{.literal}, `pmrep`{.literal} or `pmlogsummary`{.literal}.

With the `pmrep`{.literal} tool, you can:

-   View the log files.
-   Parse the selected PCP log archive and export the values into an ASCII table.
-   Extract the entire archive log or only select metric values from the log by specifying individual metrics on the command line.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").

-   The `pmlogger`{.literal} service is enabled. For more information, see [Enabling the pmlogger service](#enabling-the-pmlogger-service "6.3. Enabling the pmlogger service").

-   Installed the `pcp-gui`{.literal} package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp-gui
    ```

**Procedure**

-   Display the data on the metric:

    ``` {.language-plaintext tabindex="-1"}
    $ pmrep --start @3:00am --archive 20211128 --interval 5seconds --samples 10 --output csv disk.dev.write
    ```

    ``` {.language-plaintext tabindex="-1"}
    Time,"disk.dev.write-sda","disk.dev.write-sdb"
    2021-11-28 03:00:00,,
    2021-11-28 03:00:05,4.000,5.200
    2021-11-28 03:00:10,1.600,7.600
    2021-11-28 03:00:15,0.800,7.100
    2021-11-28 03:00:20,16.600,8.400
    2021-11-28 03:00:25,21.400,7.200
    2021-11-28 03:00:30,21.200,6.800
    2021-11-28 03:00:35,21.000,27.600
    2021-11-28 03:00:40,12.400,33.800
    2021-11-28 03:00:45,9.800,20.600
    ```

    The example displays the data on the `disk.dev.write`{.literal} metric collected in an archive at a 5 second interval in `comma-separated-value`{.literal} format. Replace *20211128* in this example with a filename containing the `pmlogger`{.literal} archive you want to display data for.

**Additional resources**

-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")

## [Chapter 7. Monitoring performance with Performance Co-Pilot](#monitoring-performance-with-performance-co-pilot) {#chapter-7.-monitoring-performance-with-performance-co-pilot .title}

Performance Co-Pilot (PCP) is a suite of tools, services, and libraries for monitoring, visualizing, storing, and analyzing system-level performance measurements. As a system administrator, you can monitor the system's performance by using PCP in Red Hat Enterprise Linux.

### [7.1. Monitoring postfix with pmda-postfix](#monitoring-postfix-with-pmda-postfix) {#monitoring-postfix-with-pmda-postfix .title}

You can monitor performance metrics of the postfix mail server with `pmda-postfix`{.literal}. It helps to check how many emails are received per second.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").
-   The `pmlogger`{.literal} service is enabled. For more information, see [Enabling the pmlogger service](#enabling-the-pmlogger-service "6.3. Enabling the pmlogger service").

**Procedure**

1.  Install the following packages:

    a.  Install the `pcp-system-tools`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install pcp-system-tools
        ```

    b.  Install the `pmda-postfix`{.literal} package to monitor postfix:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install pcp-pmda-postfix postfix
        ```

    c.  Install the `logging`{.literal} daemon:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install rsyslog
        ```

    d.  Install the mail client for testing:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install mutt
        ```

2.  Enable the `postfix`{.literal} and `rsyslog`{.literal} services:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable postfix rsyslog
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart postfix rsyslog
    ```

3.  Enable the SELinux boolean, so that `pmda-postfix`{.literal} can access the required log files:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool -P pcp_read_generic_logs=on
    ```

4.  Install the PMDA:

    ``` {.language-plaintext tabindex="-1"}
    # cd /var/lib/pcp/pmdas/postfix/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ./Install
    ```

    ``` {.language-plaintext tabindex="-1"}
    Updating the Performance Metrics Name Space (PMNS) ...
    Terminate PMDA if already installed ...
    Updating the PMCD control file, and notifying PMCD ...
    Waiting for pmcd to terminate ...
    Starting pmcd ...
    Check postfix metrics have appeared ... 7 metrics and 58 values
    ```

**Verification**

-   Verify the `pmda-postfix`{.literal} operation:

    ``` {.language-plaintext tabindex="-1"}
    echo testmail | mutt root
    ```

-   Verify the available metrics:

    ``` {.language-plaintext tabindex="-1"}
    # pminfo postfix
    ```

    ``` {.language-plaintext tabindex="-1"}
    postfix.received
    postfix.sent
    postfix.queues.incoming
    postfix.queues.maildrop
    postfix.queues.hold
    postfix.queues.deferred
    postfix.queues.active
    ```

**Additional resources**

-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")

### [7.2. Visually tracing PCP log archives with the PCP Charts application](#visually-tracing-pcp-log-archives-with-the-pcp-charts-application) {#visually-tracing-pcp-log-archives-with-the-pcp-charts-application .title}

After recording metric data, replay the PCP log archives as graphs. The metrics are sourced from one or more live hosts. You can also use metric data from PCP log archives as a source of historical data.

In the PCP Charts application, you can customize the interface to display performance metric data by using line plots, bar graphs, or utilization graphs.

Using the PCP Charts application, you can:

-   Replay the data in the PCP Charts application and use graphs to visualize the retrospective data alongside live data of the system.
-   Plot performance metric values into graphs.
-   Display multiple charts simultaneously.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").

-   Logged performance data with the `pmlogger`{.literal}. For more information, see [Logging performance data with pmlogger](#logging-performance-data-with-pmlogger "Chapter 6. Logging performance data with pmlogger").

-   Installed the `pcp-gui`{.literal} package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp-gui
    ```

**Procedure**

1.  Launch the PCP Charts application from the command line:

    ``` {.language-plaintext tabindex="-1"}
    # pmchart
    ```

    The `pmtime`{.literal} server settings are located at the bottom. With **start** and **pause** buttons you can control:

    -   The interval in which PCP polls the metric data
    -   The date and time for the metrics of historical data

2.  Click **File** and then **New Chart** to select metric from both the local machine and remote machines by specifying their host name or address. Advanced configuration options include the ability to manually set the axis values for the chart, and to manually choose the color of the plots.

3.  Record the views created in the PCP Charts application:

    Following are the options to take images or record the views created in the PCP Charts application:

    -   Click **File** and then **Export** to save an image of the current view.
    -   Click **Record** and then **Start** to start a recording.
    -   Click **Record** and then **Stop** to stop the recording. After stopping the recording, the recorded metrics are archived to be viewed later.

4.  Optional: In the **PCP Charts** application, the main configuration file, known as the view, stores the metadata associated with one or more charts. This metadata describes all chart aspects, including the metrics used and the chart columns.

5.  Optional: Save the custom view configuration by clicking **File** and then **Save View**, and load the view configuration later.

    The following example of the PCP Charts application view configuration file describes a stacking chart graph showing the total number of bytes read and written to the given XFS file system `loop1`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pmchart
    ```

    ``` {.language-plaintext tabindex="-1"}
    version 1
    chart title "Filesystem Throughput /loop1" style stacking antialiasing off
        plot legend Read rate   metric xfs.read_bytes   instance  loop1
        plot legend Write rate  metric xfs.write_bytes  instance  loop1
    ```

**Additional resources**

-   [System services and tools distributed with PCP](#system-services-and-tools-distributed-with-pcp "4.8. System services and tools distributed with PCP")

### [7.3. Collecting data from SQL server by using PCP](#collecting-data-from-sql-server-by-using-pcp) {#collecting-data-from-sql-server-by-using-pcp .title}

To monitor and analyze database performance issues, use the SQL Server agent in Performance Co-Pilot (PCP). You can collect data for Microsoft SQL Server by using PCP on your system.

**Prerequisites**

-   You have installed Microsoft SQL Server for Red Hat Enterprise Linux and established a `trusted`{.literal} connection to an SQL server.
-   You have installed the Microsoft ODBC driver for SQL Server for Red Hat Enterprise Linux.

**Procedure**

1.  Install PCP:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp-zeroconf
    ```

2.  Install packages required for the `pyodbc`{.literal} driver:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install gcc-c++ python3-devel unixODBC-devel
    ```

    ``` {.language-plaintext tabindex="-1"}
    # dnf install python3-pyodbc
    ```

3.  Install the `mssql`{.literal} agent:

    a.  Install the Microsoft SQL Server domain agent for PCP:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install pcp-pmda-mssql
        ```

    b.  Edit the `/etc/pcp/mssql/mssql.conf`{.literal} file to configure the SQL server account's username and password for the mssql agent. Ensure that the account you configure has access rights to performance data.

        ``` {.language-plaintext tabindex="-1"}
        username: user_name
        password: user_password
        ```

        Replace *user_name* with the SQL Server account username and *user_password* with the SQL Server user password for this account.

4.  Install the agent:

    ``` {.language-plaintext tabindex="-1"}
    # cd /var/lib/pcp/pmdas/mssql
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ./Install
    ```

    ``` {.language-plaintext tabindex="-1"}
    Updating the Performance Metrics Name Space (PMNS) ...
    Terminate PMDA if already installed ...
    Updating the PMCD control file, and notifying PMCD ...
    Check mssql metrics have appeared ... 168 metrics and 598 values
    [...]
    ```

**Verification**

-   Using the `pcp`{.literal} command, verify if the SQL Server PMDA (`mssql`{.literal}) is loaded and running:

    ``` {.language-plaintext tabindex="-1"}
    $ pcp
    ```

    ``` {.language-plaintext tabindex="-1"}
    Performance Co-Pilot configuration on rhel.local:
    platform: Linux rhel.local 4.18.0-167.el8.x86_64 #1 SMP Sun Dec 15 01:24:23 UTC 2019 x86_64
     hardware: 2 cpus, 1 disk, 1 node, 2770MB RAM
     timezone: PDT+7
     services: pmcd pmproxy
         pmcd: Version 5.0.2-1, 12 agents, 4 clients
         pmda: root pmcd proc pmproxy xfs linux nfsclient mmv kvm mssql
               jbd2 dm
     pmlogger: primary logger: /var/log/pcp/pmlogger/rhel.local/20200326.16.31
        pmie: primary engine: /var/log/pcp/pmie/rhel.local/pmie.log
    ```

-   View the complete list of metrics that PCP can collect from the SQL Server:

    ``` {.language-plaintext tabindex="-1"}
    # pminfo mssql
    ```

-   After viewing the list of metrics, you can report the rate of transactions. For example, to report on the overall transaction count per second, over a five second time window:

    ``` {.language-plaintext tabindex="-1"}
    # pmval -t 1 -T 5 mssql.databases.transactions
    ```

-   View the graphical chart of these metrics on your system by using the pmchart command. For more information, see [Visually tracing PCP log archives with the PCP Charts application](#visually-tracing-pcp-log-archives-with-the-pcp-charts-application "7.2. Visually tracing PCP log archives with the PCP Charts application") and `pcp(1)`{.literal}, `pminfo(1)`{.literal}, `pmval(1)`{.literal}, `pmchart(1)`{.literal}, and `pmdamssql(1)`{.literal} man pages on your system.

**Additional resources**

-   [Performance Co-Pilot for Microsoft SQL Server with RHEL 8.2 Red Hat Developers Blog post](https://www.redhat.com/en/blog/performance-co-pilot-microsoft-sql-server-rhel-82)

## [Chapter 8. Set up PCP with Grafana](#setting-up-pcp-with-grafana) {#chapter-8.-set-up-pcp-with-grafana .title}

Configure Performance Co-Pilot (PCP), Grafana, and Valkey to create a graphical monitoring system with panels, alerts, and secure authentication. Install PCP before you begin.

### [8.1. Configuring a grafana-server](#configuring-a-grafana-server) {#configuring-a-grafana-server .title}

Grafana generates graphs accessible from a browser. The `grafana-server`{.literal} is a backend server for the Grafana dashboard. It listens by default on all interfaces and provides web services accessed through a web browser. The `grafana-pcp`{.literal} plugin interacts with the `pmproxy`{.literal} daemon in the back end.

**Prerequisites**

-   PCP is configured. For more information, see [Install PCP by using pcp-zeroconf](#installing-pcp-with-pcp-zeroconf "4.3. Install PCP by using pcp-zeroconf").

**Procedure**

1.  Install the following packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install grafana grafana-pcp
    ```

2.  Restart and enable `grafana-server`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart grafana-server
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable grafana-server
    ```

3.  Open the server's firewall for network traffic to the Grafana service.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=grafana
    ```

    ``` {.language-plaintext tabindex="-1"}
    success
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

    ``` {.language-plaintext tabindex="-1"}
    success
    ```

**Verification**

-   Ensure that the `grafana-server`{.literal} is listening and responding to requests:

    ``` {.language-plaintext tabindex="-1"}
    # ss -ntlp | grep 3000
    ```

    ``` {.language-plaintext tabindex="-1"}
    LISTEN  0  128  :3000 *:  users:(("grafana-server",pid=19522,fd=7))
    ```

-   Ensure that the grafana-pcp plugin is installed:

    ``` {.language-plaintext tabindex="-1"}
    # grafana-cli plugins ls | grep performancecopilot-pcp-app
    ```

    ``` {.language-plaintext tabindex="-1"}
    performancecopilot-pcp-app @ 5.2.2
    ```

### [8.2. Configuring valkey](#configuring-valkey) {#configuring-valkey .title}

Use the Valkey data source to view data archives, query time series with the pmseries language, and analyze data across multiple hosts.

**Prerequisites**

-   PCP is configured. For more information, see [Install PCP by using pcp-zeroconf](#installing-pcp-with-pcp-zeroconf "4.3. Install PCP by using pcp-zeroconf").
-   The `grafana-server`{.literal} is configured. For more information, see [Configuring a grafana-server](#configuring-a-grafana-server "8.1. Configuring a grafana-server").
-   Mail transfer agent, for example, `postfix`{.literal} is installed and configured.

**Procedure**

1.  Install the `valkey`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install valkey
    ```

2.  Start and enable the `pmproxy`{.literal} and `valkey`{.literal} services:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pmproxy valkey
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable pmproxy valkey
    ```

3.  Restart `grafana-server`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart grafana-server
    ```

**Verification**

-   Ensure that the `pmproxy`{.literal} and `valkey`{.literal} are working:

    ``` {.language-plaintext tabindex="-1"}
    # pmseries disk.dev.read
    ```

    ``` {.language-plaintext tabindex="-1"}
    2eb3e58d8f1e231361fb15cf1aa26fe534b4d9df
    ```

    This command does not return any data if the valkey package is not installed.

    For details, see the `pmseries(1)`{.literal} man page on your system.

### [8.3. Accessing the Grafana web UI](#accessing-the-grafana-web-ui) {#accessing-the-grafana-web-ui .title}

You can access the Grafana web interface. By using the Grafana web interface, you can add Valkey, PCP bpftrace, and PCP Vector data sources, create a dashboard, view an overview of any useful metrics, and create alerts in Valkey.

**Prerequisites**

-   PCP is configured. For more information, see [Install PCP by using pcp-zeroconf](#installing-pcp-with-pcp-zeroconf "4.3. Install PCP by using pcp-zeroconf").
-   The `grafana-server`{.literal} is configured. For more information, see [Configuring a grafana-server](#configuring-a-grafana-server "8.1. Configuring a grafana-server").

**Procedure**

1.  On the client system, open a browser and access the `grafana-server`{.literal} on port 3000 by using the *http://192.0.2.0:3000* link.

    Replace *192.0.2.0* with your machine IP when accessing Grafana web UI from a remote machine, or with *localhost* when accessing the web UI locally.

2.  For the first login, enter admin in both the **Email** or **username** and **Password** fields.

3.  Grafana prompts to set a **New password** to create a secured account. If you want to set it later, click **Skip**.

4.  From the more options icon (☰) on the top left, click **Administration** \> **Plugins**.

5.  In the **Plugins** tab, type performance co-pilot in the **Search by name or type** text box and then click the **Performance Co-Pilot (PCP)** plugin.

6.  In the **Plugins / Performance Co-Pilot** pane, click **Enable**.

7.  Click the **Grafana** icon. The **Grafana Home page** is displayed.

    **Figure 8.1. Home Dashboard**

    Note

    The top corner of the screen has a **Settings** icon, but it controls the general **Dashboard settings**.

8.  In the **Grafana Home** page, click Add your first data source to add Valkey, PCP bpftrace, and PCP Vector data sources.

    -   To add PCP valkey data source, view default dashboard, create a panel, and an alert rule, see [Creating panels and alerts in PCP valkey data source](#creating-panels-and-alerts-in-pcp-valkey-data-source "8.5. Creating panels and alerts in PCP Valkey data source").
    -   To add pcp bpftrace data source and view the default dashboard, see [Viewing the PCP bpftrace System Analysis dashboard](#viewing-the-pcp-bpftrace-system-analysis-dashboard "9.2. Viewing the PCP bpftrace System Analysis dashboard").
    -   To add pcp vector data source, view the default dashboard, and to view the vector checklist, see [Viewing the PCP Vector Checklist](#viewing-the-pcp-vector-checklist "9.4. Viewing the PCP Vector Checklist").

9.  Optional: From the menu, hover over the **admin** profile icon to change the **Preferences** including **Edit Profile**, **Change Password**, or to **Sign out**.

    For more information, see the `grafana-cli`{.literal} and `grafana-server`{.literal} man pages on your system.

### [8.4. Configuring secure connections for Valkey and PCP](#configuring-secure-connections-for-valkey-and-pcp) {#configuring-secure-connections-for-valkey-and-pcp .title}

You can establish secure connections between Performance Co-Pilot (PCP), Grafana, and Valkey. Establishing secure connections between these components helps prevent unauthorized parties from accessing or modifying the data being collected and monitored.

**Prerequisites**

-   PCP is installed. For more information, see [Install and enable PCP](#installing-and-enabling-pcp "4.4. Install and enable PCP manually").
-   The Grafana server is configured. For more information, see [Configuring a grafana-server](#configuring-a-grafana-server "8.1. Configuring a grafana-server").
-   Valkey is installed. For more information, see [Configuring Valkey](#configuring-valkey "8.2. Configuring valkey").
-   The private client key is stored in the `/etc/valkey/client.key`{.literal} file. If you use a different path, modify the path in the corresponding steps of the procedure. For details about creating a private key, creating a certificate signing request (CSR), and requesting a certificate from a certificate authority (CA), see your CA's documentation.
-   The TLS client certificate is stored in the `/etc/valkey/client.crt`{.literal} file. If you use a different path, modify the path in the corresponding steps of the procedure.
-   The TLS server key is stored in the `/etc/valkey/valkey.key`{.literal} file. If you use a different path, modify the path in the corresponding steps of the procedure.
-   The TLS server certificate is stored in the `/etc/valkey/valkey.crt`{.literal} file. If you use a different path, modify the path in the corresponding steps of the procedure.
-   The CA certificate is stored in the `/etc/valkey/ca.crt`{.literal} file. If you use a different path, modify the path in the corresponding steps of the procedure.
-   For the `pmproxy`{.literal} daemon, the private server key is stored in the `/etc/pcp/tls/server.key`{.literal} file. If you use a different path, modify the path in the corresponding steps of the procedure.

**Procedure**

1.  As a root user, open the `/etc/valkey/valkey.conf`{.literal} file and adjust the TLS/SSL options to reflect the following properties:

    ``` {.language-plaintext tabindex="-1"}
    port 0
    tls-port 6379
    tls-cert-file /etc/valkey/valkey.crt
    tls-key-file /etc/valkey/valkey.key
    tls-client-key-file /etc/valkey/client.key
    tls-client-cert-file /etc/valkey/client.crt
    tls-ca-cert-file /etc/valkey/ca.crt
    ```

2.  Ensure valkey can access the TLS certificates:

    ``` {.language-plaintext tabindex="-1"}
    # su valkey -s /bin/bash -c \
    ```

    ``` {.language-plaintext tabindex="-1"}
      'ls -1 /etc/valkey/ca.crt /etc/valkey/valkey.key /etc/valkey/valkey.crt'
    /etc/valkey/ca.crt
    /etc/valkey/valkey.crt
    /etc/valkey/valkey.key
    ```

3.  Restart the valkey server to apply the configuration changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart valkey
    ```

**Verification**

-   Confirm the TLS configuration works:

    ``` {.language-plaintext tabindex="-1"}
    # valkey-cli --tls --cert /etc/valkey/client.crt \
        --key /etc/valkey/client.key \
        --cacert /etc/valkey/ca.crt <<< "PING"
    ```

    ``` {.language-plaintext tabindex="-1"}
    PONG
    Unsuccessful TLS configuration might result in the following error message:
    Could not negotiate a TLS connection: Invalid CA Certificate File/Directory
    ```

### [8.5. Creating panels and alerts in PCP Valkey data source](#creating-panels-and-alerts-in-pcp-valkey-data-source) {#creating-panels-and-alerts-in-pcp-valkey-data-source .title}

After adding the PCP Valkey data source, you can view the dashboard with an overview of useful metrics. Add a query to visualize the load graph, and create alerts that help you view system issues after they occur.

**Prerequisites**

-   The Valkey is configured. For more information, see [Configuring Valkey](#configuring-valkey "8.2. Configuring valkey").
-   The `grafana-server`{.literal} is accessible. For more information, see [Accessing the Grafana web UI](#accessing-the-grafana-web-ui "8.3. Accessing the Grafana web UI").

**Procedure**

1.  Log into the Grafana web UI.

2.  In the **Grafana Home** page, click **Add your first data source**.

3.  In the **Add data source** pane, type valkey in the **Filter by name or type** text box and then **click Valkey**.

4.  In the **Data Sources / Valkey** pane, perform the following:

    a.  Add *http://localhost:44322* in the URL field and then click **Save & Test**.

    b.  Click **Dashboards** tab \> **Import** \> **Valkey: Host Overview** to see a dashboard with an overview of any useful metrics.

        **Figure 8.2. Valkey: Host overview**

5.  Add a new panel:

    a.  From the menu, hover over the **Create** icon \> **Dashboard** \> **Add new panel** icon to add a panel.

    b.  In the **Query** tab, select the **Valkey** from the query list instead of the selected **default** option and in the text field of **A**, enter metric, for example, `kernel.all.load`{.literal} to visualize the kernel load graph.

    c.  Optional: Add **Panel title** and **Description**, and update other options from the **Settings**.

    d.  Click **Save** to apply changes and save the dashboard. Add **Dashboard name**.

    e.  Click **Apply** to apply changes and go back to the dashboard.

        **Figure 8.3. Valkey query panel**

6.  Create an alert rule:

    a.  In the Valkey query panel, click **Alert** and then click **Create Alert**.

    b.  Edit the **Name**, **Evaluate query**, and **For** fields from the **Rule**, and specify the **Conditions** for your alert.

    c.  Click **Save** to apply changes and save the dashboard. Click Apply to apply changes and go back to the dashboard.

        **Figure 8.4. Creating alerts in the Valkey panel**

    d.  Optional: In the same panel, scroll down and click **Delete** icon to delete the created rule.

    e.  Optional: From the menu, click **Alerting** icon to view the created alert rules with different alert statuses, to edit the alert rule, or to pause the existing rule from the **Alert Rules** tab. To add a notification channel for the created alert rule to receive an alert notification from Grafana, see [Adding notification channels for alerts](#adding-notification-channels-for-alerts "8.6. Adding notification channels for alerts").

### [8.6. Adding notification channels for alerts](#adding-notification-channels-for-alerts) {#adding-notification-channels-for-alerts .title}

Add notification channels to receive an alert notification from Grafana when rule conditions are met and the system requires attention. You can receive these alerts after selecting any one type from the supported list of notifiers.

Grafana supports the following notification channel types: **DingDing, Discord, Email, Google Hangouts Chat, HipChat, Kafka REST Proxy, LINE, Microsoft Teams, OpsGenie, PagerDuty, Prometheus Alertmanager, Pushover, Sensu, Slack, Telegram, Threema Gateway, VictorOps**, and **webhook**.

**Prerequisites**

-   The `grafana-server`{.literal} is accessible. For more information, see [Accessing the Grafana web UI](#accessing-the-grafana-web-ui "8.3. Accessing the Grafana web UI").

-   An alert rule is created. For more information, see [Creating panels and alerts in PCP valkey data source](#creating-panels-and-alerts-in-pcp-valkey-data-source "8.5. Creating panels and alerts in PCP Valkey data source").

-   Configured SMTP and added a valid sender's email address in the `grafana/grafana.ini`{.literal} file, for example:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/grafana/grafana.ini
    ```

    ``` {.language-plaintext tabindex="-1"}
    [smtp]
    enabled = true
    from_address = abc@gmail.com
    ```

    Replace *abc@gmail.com* by a valid email address.

-   Restarted grafana-server after changing the configurations:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart grafana-server.service
    ```

**Procedure**

1.  From the menu, hover over the **Alerting** icon \> click **Notification channels** \> **Add channel**.

2.  In the Add notification channel details pane, perform the following:

    a.  Enter your name in the **Name** text box.
    b.  Select the communication **Type**, for example, **Email** and enter the email address. You can add multiple email addresses using the `;`{.literal} separator.
    c.  Optional: **Configure Optional Email** settings and **Notification** settings.

3.  Click **Save**.

4.  Select a notification channel in the alert rule:

    a.  From the menu, hover over the **Alerting** icon and then click **Alert rules**.
    b.  From the **Alert Rules** tab, click the created alert rule.
    c.  On the **Notifications** tab, select your notification channel name from the **Send to** option, and then add an alert message.

5.  Click **Apply**.

**Additional resources**

-   [Upstream Grafana documentation for alert notifications](https://grafana.com/docs/grafana/latest/alerting/notifications/)

### [8.7. Configuring authentication between PCP components](#configuring-authentication-between-pcp-components) {#configuring-authentication-between-pcp-components .title}

You can configure authentication by using the `scram-sha-256`{.literal} authentication mechanism. It is supported by PCP through the Simple Authentication Security Layer (SASL) framework.

**Procedure**

1.  Install the SASL framework for the `scram-sha-256`{.literal} authentication mechanism:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install cyrus-sasl-scram cyrus-sasl-lib
    ```

2.  Specify the supported authentication mechanism and the user database path in the `pmcd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/sasl2/pmcd.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    mech_list: scram-sha-256
    sasldb_path: /etc/pcp/passwd.db
    ```

3.  Create a new user:

    ``` {.language-plaintext tabindex="-1"}
    # useradd -r metrics
    ```

    Replace *metrics* by your user name.

4.  Add the created user in the user database:

    ``` {.language-plaintext tabindex="-1"}
    # saslpasswd2 -a pmcd metrics
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password:
    Again (for verification):
    ```

    To add the created user, it is required to enter the *metrics* account password.

5.  Set the permissions of the user database:

    ``` {.language-plaintext tabindex="-1"}
    # chown root:pcp /etc/pcp/passwd.db
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 640 /etc/pcp/passwd.db
    ```

6.  Restart the *pmcd* service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart pmcd
    ```

**Verification**

-   Verify the SASL configuration:

    ``` {.language-plaintext tabindex="-1"}
    # pminfo -f -h "pcp://127.0.0.1?username=metrics" disk.dev.read
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password:
    disk.dev.read
    inst [0 or "sda"] value 19540
    ```

**Additional resources**

-   [How can I configure authentication between PCP components, like PMDAs and pmcd in RHEL 8.2? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/5041891)

### [8.8. Additional resources](#setting-up-pcp-with-grafana_88-additional-resources) {#additional-resources-2 .title}

-   [PCP installation methods](#pcp-installation-methods "4.1. PCP installation methods")

## [Chapter 9. Advanced PCP monitoring and visualization](#advanced-pcp-monitoring-and-visualization) {#chapter-9.-advanced-pcp-monitoring-and-visualization .title}

Extend PCP monitoring capabilities with specialized tools like bpftrace and vector, and create advanced visualizations using heatmaps and geomaps in Grafana.

### [9.1. Installing PCP bpftrace](#installing-pcp-bpftrace) {#installing-pcp-bpftrace .title}

You can install the `PCP bpftrace`{.literal} agent to introspect a system and to gather metrics from the kernel and user-space tracepoints. The `bpftrace`{.literal} agent uses `bpftrace`{.literal} scripts to gather the metrics. The `bpftrace`{.literal} scripts use the enhanced Berkeley Packet Filter (eBPF).

**Prerequisites**

-   PCP is configured. For more information, see [Install PCP by using pcp-zeroconf](#installing-pcp-with-pcp-zeroconf "4.3. Install PCP by using pcp-zeroconf").
-   The `grafana-server`{.literal} is configured. For more information, see [Configuring a grafana-server](#configuring-a-grafana-server "8.1. Configuring a grafana-server").
-   The `scram-sha-256`{.literal} authentication mechanism is configured. For more information, see [Configuring authentication between PCP components](#configuring-authentication-between-pcp-components "8.7. Configuring authentication between PCP components").

**Procedure**

1.  Install the `pcp-pmda-bpftrace`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp-pmda-bpftrace
    ```

2.  Edit the bpftrace.conf file and add the user:

    ``` {.language-plaintext tabindex="-1"}
    # vi /var/lib/pcp/pmdas/bpftrace/bpftrace.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    [dynamic_scripts]
    enabled = true
    auth_enabled = true
    allowed_users = root,metrics
    ```

    Replace *metrics* by your user name from [Configuring authentication between PCP components](#configuring-authentication-between-pcp-components "8.7. Configuring authentication between PCP components").

3.  Install `bpftrace`{.literal} PMDA:

    ``` {.language-plaintext tabindex="-1"}
    # cd /var/lib/pcp/pmdas/bpftrace/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ./Install
    ```

    ``` {.language-plaintext tabindex="-1"}
    Updating the Performance Metrics Name Space (PMNS) ...
    Terminate PMDA if already installed ...
    Updating the PMCD control file, and notifying PMCD …
    Check bpftrace metrics have appeared ... 7 metrics and 6 values
    ```

    The `pmda-bpftrace`{.literal} is now installed, and can only be used after authenticating your user. For more information, see [Viewing the PCP bpftrace System Analysis dashboard](#viewing-the-pcp-bpftrace-system-analysis-dashboard "9.2. Viewing the PCP bpftrace System Analysis dashboard").

### [9.2. Viewing the PCP bpftrace System Analysis dashboard](#viewing-the-pcp-bpftrace-system-analysis-dashboard) {#viewing-the-pcp-bpftrace-system-analysis-dashboard .title}

The `PCP bpftrace`{.literal} data source accesses live data unavailable through standard `pmlogger`{.literal} instances or archives. In the `PCP bpftrace`{.literal} data source, view the dashboard with an overview of useful metrics.

**Prerequisites**

-   The PCP `bpftrace`{.literal} is installed. For more information, see [Installing PCP bpftrace](#installing-pcp-bpftrace "9.1. Installing PCP bpftrace").
-   The `grafana-server`{.literal} is configured. For more information, see [Configuring a grafana-server](#configuring-a-grafana-server "8.1. Configuring a grafana-server").

**Procedure**

1.  Log into the **Grafana web UI**.

2.  In the **Grafana Home** page, click **Add your first data source**.

3.  In the **Add data source** pane, type `bpftrace`{.literal} in the **Filter by name or type** text box and then click **PCP bpftrace**.

4.  In the **Data Sources / PCP bpftrace** pane, perform the following:

    a.  Add *http://localhost:44322* in the URL field.

    b.  Toggle the **Basic Auth** option and add the created user credentials in the **User** and **Password** field.

    c.  Click **Save & Test**.

        **Figure 9.1. Adding PCP bpftrace in the data source**

    d.  Click **Dashboards** tab \> **Import** \> **PCP bpftrace: System Analysis** to see a dashboard with an overview of any useful metrics.

        **Figure 9.2. PCP bpftrace: System Analysis**

### [9.3. Installing PCP Vector](#installing-pcp-vector) {#installing-pcp-vector .title}

You must install pcp vector before you start using it.

**Prerequisites**

-   PCP is configured. For more information, see [Install PCP by using pcp-zeroconf](#installing-pcp-with-pcp-zeroconf "4.3. Install PCP by using pcp-zeroconf").
-   The `grafana-server`{.literal} is configured. For more information, see [Configuring a grafana-server](#configuring-a-grafana-server "8.1. Configuring a grafana-server").

**Procedure**

-   Install the bcc PMDA:

    ``` {.language-plaintext tabindex="-1"}
    # cd /var/lib/pcp/pmdas/bcc
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ./Install
    ```

    ``` {.language-plaintext tabindex="-1"}
    [Wed Apr  1 00:27:48] pmdabcc(22341) Info: Initializing, currently in 'notready' state.
    [Wed Apr  1 00:27:48] pmdabcc(22341) Info: Enabled modules:
    [Wed Apr  1 00:27:48] pmdabcc(22341) Info: ['biolatency', 'sysfork',
    [...]
    Updating the Performance Metrics Name Space (PMNS) ...
    Terminate PMDA if already installed ...
    Updating the PMCD control file, and notifying PMCD …
    Check bcc metrics have appeared ... 1 warnings, 1 metrics and 0 values
    ```

### [9.4. Viewing the PCP Vector Checklist](#viewing-the-pcp-vector-checklist) {#viewing-the-pcp-vector-checklist .title}

The PCP Vector data source displays live metrics and uses the pcp metrics. It analyzes data for individual hosts. After adding the PCP Vector data source, view the dashboard with an overview of useful metrics. Also, view related troubleshooting or reference links in the checklist.

**Prerequisites**

-   The PCP Vector is installed. For more information, see [Installing PCP Vector](#installing-pcp-vector "9.3. Installing PCP Vector").
-   The `grafana-server`{.literal} is accessible. For more information, see [Accessing the Grafana web UI](#accessing-the-grafana-web-ui "8.3. Accessing the Grafana web UI").

**Procedure**

1.  Log into the **Grafana web UI**.

2.  In the **Grafana Home** page, click **Add your first data source**.

3.  In the **Add data source** pane, type vector in the **Filter by name or type** text box and then click **PCP Vector**.

4.  In the **Data Sources / PCP Vector** pane, perform the following:

    a.  Add *http://localhost:44322* in the **URL** field and then click **Save & Test**.

    b.  Click **Dashboards** tab \> **Import** \* **PCP Vector: Host Overview** to see a dashboard with an overview of any useful metrics.

        **Figure 9.3. PCP Vector: Host Overview**

5.  From the menu, hover over the **Performance Co-Pilot** plugin and then click **PCP Vector** Checklist.

    In the PCP checklist, click help or warning icon to view the related troubleshooting or reference links.

    **Figure 9.4. Performance Co-Pilot / PCP Vector Checklist**

### [9.5. Using heatmaps in Grafana](#using-heatmaps-in-grafana) {#using-heatmaps-in-grafana .title}

Use heatmaps in Grafana to view data as histograms, identify trends and patterns in your data, and see how they change over time. Each heatmap column is a histogram, with cell colors showing the density of observations.

**Prerequisites**

-   Valkey is configured. For more information see [Configuring Valkey](#configuring-valkey "8.2. Configuring valkey").
-   The `grafana-server`{.literal} is accessible. For more information, see [Accessing the Grafana web UI](#accessing-the-grafana-web-ui "8.3. Accessing the Grafana web UI").
-   The PCP valkey data source is configured. For more information see [Creating panels and alerts in PCP Valkey data source](#creating-panels-and-alerts-in-pcp-valkey-data-source "8.5. Creating panels and alerts in PCP Valkey data source").

**Procedure**

1.  Hover the cursor over the **Dashboards** tab and click **+ New dashboard**.

2.  In the **Add panel** menu, click **Add a new panel**.

3.  In the **Query** tab:

    a.  Select **Valkey** from the query list instead of the selected default option.
    b.  In the text field of **A**, enter a metric, for example, `kernel.all.load`{.literal} to visualize the kernel load graph.

4.  Click the visualization dropdown menu, which is set to **Time series** by default, and then click **Heatmap**.

5.  Optional: In the **Panel Options** dropdown menu, add a **Panel Title** and **Description**.

6.  In the **Heatmap** dropdown menu, under the **Calculate from data** setting, click **Yes**.

    **Figure 9.5. Heatmap**

7.  Optional: In the **Colors** dropdown menu, change the **Scheme** from the default **Orange** and select the number of steps (color shades).

8.  Optional: In the **Tooltip** dropdown menu, under the **Show histogram (Y Axis)** setting, click the toggle to display a cell's position within its specific histogram when hovering your cursor over a cell in the heatmap. For example:

### [9.6. Configuring pcp-geolocate for Grafana geomaps](#configuring-pcp-geolocate-for-grafana-geomaps) {#configuring-pcp-geolocate-for-grafana-geomaps .title}

Configuring the `pcp-geolocate`{.literal} service adds longitude and latitude labels to Performance Co-Pilot (PCP) metric values in Valkey. Enable this service so Grafana geomaps can place metrics from monitored systems on a world map.

**Prerequisites**

-   Valkey is configured.
-   The `grafana-server`{.literal} is accessible.

**Procedure**

1.  Install the `pcp-geolocate`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcp-geolocate
    ```

2.  Start and enable the `pcp-geolocate`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pcp-geolocate
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable pcp-geolocate
    ```

3.  Restart `pmproxy`{.literal}, `valkey`{.literal}, and `grafana-server`{.literal} to apply the changes:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart pmproxy valkey grafana-server
    ```

**Verification**

-   Verify that longitude and latitude labels are present in the Valkey database:

    ``` {.language-plaintext tabindex="-1"}
    # pmseries --labels
    ```

    The output is similar to the following example:

    ``` {.language-plaintext tabindex="-1"}
    {"agent":"linux","domainname":"example.com","groupid":1000,"hostname":"server.example.com","latitude":-25.28496,"longitude":152.87886,"machineid":"295b16e3b6074cc8bdbda8bf96f6930a","userid":1000}
    ```

    The output must include the `latitude`{.literal} and `longitude`{.literal} labels. Without these labels, the geomap panel cannot place metrics on the map.

    For details, see the `pmseries(1)`{.literal} man page on your system.

**Additional resources**

-   [Configuring Valkey](#configuring-valkey "8.2. Configuring valkey")
-   [Accessing the Grafana web UI](#accessing-the-grafana-web-ui "8.3. Accessing the Grafana web UI")

### [9.7. Visualizing PCP data with geomaps in Grafana](#visualizing-pcp-data-with-geomaps-in-grafana) {#visualizing-pcp-data-with-geomaps-in-grafana .title}

Visualizing Performance Co-Pilot (PCP) metrics in Grafana geomaps presents performance data from monitored systems on a world map. Use the PCP Valkey data source in Red Hat Enterprise Linux 10.1 and later to compare metrics across geographic locations and identify systems that need further investigation.

**Prerequisites**

-   The PCP Valkey data source is configured.
-   `pcp-geolocate`{.literal} is configured.

**Procedure**

1.  Log into the Grafana web UI.

2.  Create a geomap panel:

    a.  Hover the cursor over the **Dashboards** tab and click **+ New dashboard**.
    b.  In the **Add panel** menu, click **Add a new panel**.
    c.  In the **Query** tab, select **Valkey** from the query list instead of the selected **default** option.
    d.  Open the **Format** drop-down menu at the bottom of the query window and select **Geomap**.
    e.  In the text field of **A**, enter a PCP metric, for example, `kernel.all.pswitch`{.literal}.
    f.  Optional: In the **Panel options** section, add a **Panel title** and **Description**.
    g.  Optional: In the panel editor, open the **Thresholds** section and set a threshold value and color. For example, set the threshold to `1000`{.literal} and the color to `red`{.literal} so that locations with values above `1000`{.literal} appear as red markers on the map.
    h.  Optional: In the panel editor, open the **Value mappings** section and add a mapping for a value range. For example, map values from `0`{.literal} to `200`{.literal} to the message `Less than 200`{.literal}.
    i.  Click **Save** to apply changes and save the dashboard. Add a **Dashboard name**.
    j.  Click **Apply** to return to the dashboard.

**Verification**

-   On the dashboard, confirm that the geomap panel displays markers on the world map for monitored systems.
-   Hover over a marker to confirm that the panel shows the metric value for that location.

**Additional resources**

-   [Configuring pcp-geolocate for Grafana geomaps](#configuring-pcp-geolocate-for-grafana-geomaps "9.6. Configuring pcp-geolocate for Grafana geomaps")
-   [Creating panels and alerts in PCP Valkey data source](#creating-panels-and-alerts-in-pcp-valkey-data-source "8.5. Creating panels and alerts in PCP Valkey data source")
-   [Red Hat Developer article on visualizing PCP data with geomaps in Grafana](https://developers.redhat.com/articles/2025/12/11/visualize-performance-co-pilot-data-geomaps-grafana)

### [9.8. Managing SELinux booleans for Grafana](#managing-selinux-booleans-for-grafana) {#managing-selinux-booleans-for-grafana .title}

The `grafana-selinux`{.literal} subpackage includes several SELinux booleans that control Grafana's access to external services. These booleans are off by default. You can turn them `on`{.literal} or `off`{.literal} based on your system requirements.

**Prerequisites**

-   You have installed `grafana-selinux`{.literal} subpackage.
-   You have root privileges.

**Procedure**

1.  View all Grafana-related SELinux booleans:

    ``` {.language-plaintext tabindex="-1"}
    # semanage boolean -l | grep grafana
    ```

2.  Enable a SELinux boolean:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool [-P] <boolean_name> on
    ```

    -   Replace *\<boolean_name\>* with the name of the SELinux boolean you want to enable.
    -   Use the *-P* option to make the change persistent across system reboots.

3.  Optional: Turn off any SELinux option:

    ``` {.language-plaintext tabindex="-1"}
    # setsebool [-P] <boolean_name> off
    ```

### [9.9. Troubleshooting Grafana issues](#troubleshooting-grafana-issues) {#troubleshooting-grafana-issues .title}

At times, it is necessary to troubleshoot Grafana issues, such as Grafana not displaying data, a black dashboard, or similar issues.

**Procedure**

-   Verify that the `pmlogger`{.literal} service is up and running by using the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl status pmlogger
    ```

-   Verify if files were created or modified to the disk by using the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ ls /var/log/pcp/pmlogger/$(hostname)/ -rlt
    ```

    ``` {.language-plaintext tabindex="-1"}
    total 4024
    -rw-r--r--. 1 pcp pcp   45996 Oct 13  2019 20191013.20.07.meta.xz
    -rw-r--r--. 1 pcp pcp     412 Oct 13  2019 20191013.20.07.index
    -rw-r--r--. 1 pcp pcp   32188 Oct 13  2019 20191013.20.07.0.xz
    -rw-r--r--. 1 pcp pcp   44756 Oct 13  2019 20191013.20.30-00.meta.xz
    [..]
    ```

-   Verify that the `pmproxy`{.literal} service is running by using the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl status pmproxy
    ```

-   Verify that `pmproxy`{.literal} is running, time series support is enabled, and a connection to valkey is established by viewing the `/var/log/pcp/pmproxy/pmproxy.log`{.literal} file. Ensure that it contains the following text:

    ``` {.language-plaintext tabindex="-1"}
    pmproxy(1716) Info: valkey slots, command keys, schema version setup
    Here, 1716 is the PID of pmproxy, which will be different for every invocation of pmproxy.
    Verify if the valkey database contains any keys by executing the following command:
    $ valkey-cli dbsize
    (integer) 34837
    ```

-   Verify if any PCP metrics are in the valkey database and pmproxy is able to access them by using the following commands:

    ``` {.language-plaintext tabindex="-1"}
    $ pmseries disk.dev.read
    ```

    ``` {.language-plaintext tabindex="-1"}
    2eb3e58d8f1e231361fb15cf1aa26fe534b4d9df
    $ pmseries "disk.dev.read[count:10]"
    2eb3e58d8f1e231361fb15cf1aa26fe534b4d9df
        [Mon Jul 26 12:21:10.085468000 2021] 117971 70e83e88d4e1857a3a31605c6d1333755f2dd17c
        [Mon Jul 26 12:21:00.087401000 2021] 117758 70e83e88d4e1857a3a31605c6d1333755f2dd17c
        [Mon Jul 26 12:20:50.085738000 2021] 116688 70e83e88d4e1857a3a31605c6d1333755f2dd17c
    [...]
    $ valkey-cli --scan --pattern "*$(pmseries 'disk.dev.read')"
    pcp:metric.name:series:2eb3e58d8f1e231361fb15cf1aa26fe534b4d9df
    pcp:values:series:2eb3e58d8f1e231361fb15cf1aa26fe534b4d9df
    pcp:desc:series:2eb3e58d8f1e231361fb15cf1aa26fe534b4d9df
    pcp:labelvalue:series:2eb3e58d8f1e231361fb15cf1aa26fe534b4d9df
    pcp:instances:series:2eb3e58d8f1e231361fb15cf1aa26fe534b4d9df
    pcp:labelflags:series:2eb3e58d8f1e231361fb15cf1aa26fe534b4d9df
    ```

-   Verify if there are any errors in the Grafana logs by using the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -e -u grafana-server
    ```

    ``` {.language-plaintext tabindex="-1"}
    -- Logs begin at Mon 2021-07-26 11:55:10 IST, end at Mon 2021-07-26 12:30:15 IST. --
    Jul 26 11:55:17 localhost.localdomain systemd[1]: Starting Grafana instance...
    Jul 26 11:55:17 localhost.localdomain grafana-server[1171]: t=2021-07-26T11:55:17+0530 lvl=info msg="Starting Grafana" logger=server version=7.3.6 c>
    Jul 26 11:55:17 localhost.localdomain grafana-server[1171]: t=2021-07-26T11:55:17+0530 lvl=info msg="Config loaded from" logger=settings file=/usr/s>
    Jul 26 11:55:17 localhost.localdomain grafana-server[1171]: t=2021-07-26T11:55:17+0530 lvl=info msg="Config loaded from" logger=settings file=/etc/g>
    [...]
    ```

## [Chapter 10. Managing power consumption with PowerTOP](#managing-power-consumption-with-powertop) {#chapter-10.-managing-power-consumption-with-powertop .title}

Reducing the overall power consumption of computer systems helps to save cost. To optimize energy consumption, study system tasks and configure each component to match the performance requirements of that specific task.

Lowering the power consumption of a specific component or of the system as a whole leads to lower heat and performance. Proper power management results in:

-   Heat reduction for servers and computing centers.
-   Reduced secondary costs, including cooling, space, cables, generators, and uninterruptible power supplies (UPS).
-   Extended battery life for laptops.
-   Lower carbon dioxide output.
-   Meeting government regulations or legal requirements regarding Green IT, for example, Energy Star.
-   Meeting company guidelines for new systems.

### [10.1. Power management basics](#power-management-basics) {#power-management-basics .title}

Effective power management is built on the following principles:

An idle CPU should only wake up when needed
:   Since Red Hat Enterprise Linux 6, the kernel runs tickless. It replaced periodic timer interrupts with on-demand interrupts. Therefore, idle CPUs are allowed to remain idle until a new task is queued for processing. CPUs that have entered lower power states can remain in these states longer.

However, benefits from this feature can be offset if your system has applications that create unnecessary timer events. Polling events, such as checks for volume changes or mouse movement, are examples of such events.

Unused hardware and devices should be disabled completely
:   This is true for devices that have moving parts, for example, hard disks. In addition, some applications may leave an unused but enabled device \"open\". When this occurs, the kernel assumes that the device is in use. It prevents the device from going into a power saving state.

Low activity should translate to low wattage
:   Power efficiency often depends on modern hardware and proper BIOS or UEFI configuration, especially on non-x86 architectures. Install the latest firmware. Enable power management features in the BIOS or system settings to improve power efficiency.

Some features to look for include:

-   Collaborative Processor Performance Controls (CPPC) support for ARM64
-   PowerNV support for IBM Power Systems
-   Cool'n'Quiet
-   ACPI (C-state)
-   Smart

Red Hat Enterprise Linux automatically uses these features when supported and enabled in the BIOS.

Different forms of CPU states and their effects

:   Modern CPUs together with Advanced Configuration and Power Interface (ACPI) provide different power states. The three different states are:

    -   Sleep (C-states)

    -   Frequency and voltage (P-states)

    -   Heat output (T-states or thermal states)

        A CPU running on the lowest sleep state consumes the least amount of energy, but it also takes considerably more time to wake it up from that state when needed. In very rare cases this can lead to the CPU having to wake up immediately every time it just went to sleep. This permanently busy CPU loses power savings available from more efficient idle states.

A turned off machine uses the least amount of power
:   One of the best ways to save power is to turn off systems. For example, companies can develop a corporate culture focused on \"green IT\" awareness under a guideline to turn off machines during breaks or when going home. Consolidate several physical servers into one bigger server and virtualize them by using the virtualization technology. The virtualization technology is shipped with Red Hat Enterprise Linux.

**Additional resources**

-   [Audit and analysis overview](#audit-and-analysis-overview "10.2. Audit and analysis overview")
-   [Tools for auditing](#tools-for-auditing "10.3. Tools for auditing")

### [10.2. Audit and analysis overview](#audit-and-analysis-overview) {#audit-and-analysis-overview .title}

The detailed manual audit, analysis, and tuning of a single system is rare. The time and cost spent to do so typically outweighs the benefits gained from these last pieces of system tuning.

Tuning is valuable for large groups of identical systems where you can reuse the same settings. For example, consider the deployment of thousands of desktop systems, or an HPC cluster where the machines are nearly identical.

Another reason for auditing and analysis is to provide a basis for comparison. Use the results to identify regressions or changes in system behavior and to avoid power consumption issues when hardware, BIOS, or software updates occur regularly. Generally, a thorough audit and analysis gives a better idea of what is really happening on a particular system.

Auditing and analyzing a system with regard to power consumption is relatively hard, even with the most modern systems available. Most systems do not provide the necessary means to measure power use by using software. Exceptions exist though:

-   iLO management console of Hewlett Packard server systems has a power management module that you can access through the web.
-   IBM provides a similar solution in their BladeCenter power management module.
-   On some Dell systems, the IT Assistant offers power monitoring capabilities.

Other vendors are likely to offer similar capabilities for their server platforms. However, there is no single solution available that is supported by all vendors.

### [10.3. Tools for auditing](#tools-for-auditing) {#tools-for-auditing .title}

Red Hat Enterprise Linux offers tools for system auditing and analysis. Use these tools to verify existing findings or gain in-depth information about specific system components.

Many of these tools are used for performance tuning, including:

PowerTOP
:   PowerTOP identifies specific components of kernel and user-space applications that frequently wake up the CPU. Intel CPU's Intel Hardware P-State (HWP) adjusts CPU frequency and voltage to regulate the power efficiency and performance. You can use the `powertop`{.literal} command as root to start the PowerTOP tool and `powertop --calibrate`{.literal} to calibrate the power estimation engine.

`diskdevstat`{.literal} and `netdevstat`{.literal}

:   These SystemTap tools collect detailed information about the disk and network activity of all applications running on a system. Use these statistics to detect power-wasting applications performing many small rather than few large I/O operations. Use the `dnf install tuned-utils-systemtap kernel-debuginfo`{.literal} command to install the `diskdevstat`{.literal} and `netdevstat`{.literal} tools. To view detailed information about the disk and network activity, use:

    ``` {.language-plaintext tabindex="-1"}
    # diskdevstat
    ```

    ``` {.language-plaintext tabindex="-1"}
    PID   UID   DEV   WRITE_CNT   WRITE_MIN   WRITE_MAX   WRITE_AVG   READ_CNT   READ_MIN   READ_MAX   READ_AVG   COMMAND

    3575  1000  dm-2   59          0.000      0.365        0.006        5         0.000        0.000      0.000      mozStorage #5
    3575  1000  dm-2    7          0.000      0.000        0.000        0         0.000        0.000      0.000      localStorage DB
    [...]
    ```

    ``` {.language-plaintext tabindex="-1"}
    # netdevstat
    ```

    ``` {.language-plaintext tabindex="-1"}
    PID   UID   DEV       XMIT_CNT   XMIT_MIN   XMIT_MAX   XMIT_AVG   RECV_CNT   RECV_MIN   RECV_MAX   RECV_AVG   COMMAND
    3572  991  enp0s31f6    40       0.000      0.882       0.108        0         0.000       0.000       0.000     openvpn
    3575  1000 enp0s31f6    27       0.000      1.363       0.160        0         0.000       0.000       0.000     Socket Thread
    [...]
    ```

    With these commands, you can specify three parameters: `update_interval`{.literal}, `total_duration`{.literal}, and `display_histogram`{.literal}.

TuneD
:   It is a profile-based system tuning tool. It uses the `udev`{.literal} device manager to monitor connected devices and enables both static and dynamic tuning of system settings. Use the `tuned-adm recommend`{.literal} command to determine which profile Red Hat suggests as the most suitable for a particular product.

Virtual memory statistics (`vmstat`{.literal})

:   It is a tool provided by the `procps-ng`{.literal} package. It provides detailed information about processes, memory, paging, block I/O, traps, and CPU activity. Use the `vmstat`{.literal} command to view this information:

    ``` {.language-plaintext tabindex="-1"}
    $ vmstat
    ```

    ``` {.language-plaintext tabindex="-1"}
    procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
    r  b  swpd  free    buff   cache   si   so  bi   bo   in  cs  us  sy id  wa  st
    1  0   0   5805576 380856 4852848   0    0  119  73  814  640  2   2 96   0   0
    ```

    View the active and inactive memory by using the `vmstat -a`{.literal} command.

`iostat`{.literal}

:   Provided by the `sysstat`{.literal} package, this tool is similar to `vmstat`{.literal}, but only for monitoring I/O on block devices. It provides more verbose output and statistics. You can use the following command to monitor the system I/O:

    ``` {.language-plaintext tabindex="-1"}
    $ iostat
    ```

    ``` {.language-plaintext tabindex="-1"}
    avg-cpu:  %user   %nice %system %iowait  %steal   %idle
               2.05    0.46    1.55    0.26    0.00   95.67

    Device     tps     kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
    nvme0n1    53.54     899.48     616.99      3445229     2363196
    dm-0       42.84     753.72     238.71      2886921      914296
    dm-1        0.03       0.60       0.00         2292           0
    dm-2       24.15     143.12     379.80       548193     1454712
    ```

`blktrace`{.literal}

:   Provides detailed information about how time is spent in the I/O subsystem. Use the following command to view this information in human readable format:

    ``` {.language-plaintext tabindex="-1"}
    # blktrace -d /dev/dm-0 -o - | blkparse -i -
    ```

    ``` {.language-plaintext tabindex="-1"}
    253,0   1    1   0.000000000  17694  Q   W 76423384 + 8 [kworker/u16:1]
    253,0   2    1   0.001926913     0   C   W 76423384 + 8 [0]
    [...]
    ```

    -   The first column, `253,0`{.literal} is the device major and minor tuple.
    -   The second column displays sequence number of the event.
    -   The third column displays the CPU id for event occurrence.
    -   The fourth column of `timestamps`{.literal}.
    -   The fifth column of PID of the I/O-issuing process.
    -   The sixth column displays the event type. `Q`{.literal} for queued process, C for completed process.
    -   The seventh column, `W`{.literal} for write operation.
    -   The eighth column, `76423384`{.literal}, is the block number
    -   The ninth column `+ 8`{.literal} is the number of requested blocks as a number of bytes in I/O operation.
    -   The last field, `[kworker/u16:1]`{.literal}, is the process name. By default, the `blktrace`{.literal} command runs forever until the process is explicitly killed. Use the `-w`{.literal} option to specify the run-time duration.

`turbostat`{.literal}

:   It is provided by the `kernel-tools`{.literal} package. It reports on processor topology, frequency, idle power-state statistics, temperature, and power usage on x86-64 processors. Use the following command to view the summary:

    ``` {.language-plaintext tabindex="-1"}
    # turbostat
    ```

    ``` {.language-plaintext tabindex="-1"}
    CPUID(0): GenuineIntel 0x16 CPUID levels; 0x80000008 xlevels; family:model:stepping 0x6:8e:a (6:142:10)
    CPUID(1): SSE3 MONITOR SMX EIST TM2 TSC MSR ACPI-TM HT TM
    CPUID(6): APERF, TURBO, DTS, PTM, HWP, HWPnotify, HWPwindow, HWPepp, No-HWPpkg, EPB
    [...]
    ```

    By default, `turbostat`{.literal} prints a summary of counter results for the entire screen, followed by counter results every 5 seconds. Specify a different period between counter results with the `-i`{.literal} option. For example, use turbostat `-i 10`{.literal} to print results every `10`{.literal} seconds instead. `turbostat`{.literal} is also useful for identifying servers that are inefficient in terms of power usage or idle time. It also helps to identify the rate of system management interrupts (SMIs) occurring on the system. Verify the effects of power management tuning with `turbostat`{.literal}.

`cpupower`{.literal}

:   The `cpupower`{.literal} package contains a collection of tools to examine and tune power saving related features of processors. Use the `cpupower`{.literal} command with the `frequency-info`{.literal}, `frequency-set`{.literal}, `idle-info`{.literal}, `idle-set`{.literal}, `set`{.literal}, `info`{.literal}, and monitor options to display and set processor related values.

    For example, to view available `cpufreq`{.literal} governors, use:

    ``` {.language-plaintext tabindex="-1"}
    $ cpupower frequency-info --governors
    ```

    ``` {.language-plaintext tabindex="-1"}
    analyzing CPU 0:
      available cpufreq governors: performance powersave
    ```

GNOME Power Manager
:   It is a daemon that is installed as part of the GNOME desktop environment. GNOME Power Manager notifies you of changes in your system's power status, for example, a change from battery to AC power. It also reports battery status, and warns you when battery power is low.

`pmda-denki`{.literal}
:   `pmda-denki`{.literal} monitors power consumption. It's part of the Performance Co-Pilot suite, and helps to monitor consumption over time, and visualize it.

**Additional resources**

-   [Take control of your RHEL systems' power consumption with pmda-denki](https://www.redhat.com/en/blog/take-control-your-rhel-systems-power-consumption)
-   [Optimizing system performance with TuneD](#optimizing-system-performance-with-tuned "Chapter 2. Optimizing system performance with TuneD")
-   [Optimizing power consumption](#optimizing-power-consumption "10.11. Optimizing power consumption")

### [10.4. The purpose of PowerTOP](#the-purpose-of-powertop) {#the-purpose-of-powertop .title}

PowerTOP is a program that diagnoses issues related to power consumption and provides suggestions on how to extend battery lifetime. PowerTOP estimates total system power usage and consumption for individual processes, devices, and kernel handlers.

The tool can also identify specific components of kernel and user-space applications that frequently wake up the CPU. Red Hat Enterprise Linux uses version 2.x of PowerTOP.

### [10.5. Installing PowerTOP](#installing-powertop) {#installing-powertop .title}

You can install PowerTop and start using it to diagnose issues related to power consumption.

**Procedure**

-   Open the command line and enter:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install powertop
    ```

### [10.6. Starting PowerTOP](#starting-powertop) {#starting-powertop .title}

After you install it on your system, you can start using PowerTop to optimize system performance.

**Prerequisites**

-   You are running your laptop on battery power.

**Procedure**

-   To run PowerTOP, enter:

    ``` {.language-plaintext tabindex="-1"}
    # powertop
    ```

### [10.7. Calibrating PowerTOP](#calibrating-powertop) {#calibrating-powertop .title}

You can use the PowerTOP calibration process to improve the accuracy of power consumption measurements on your laptop.

**Procedure**

-   On a laptop, you can calibrate the power estimation engine by running the following command:

    ``` {.language-plaintext tabindex="-1"}
    # powertop --calibrate
    ```

    Let the calibration finish without interacting with the machine during the process. Calibration takes time because the process performs various tests, cycles through brightness levels and switches devices on and off. When the calibration process is completed, PowerTOP starts as normal. Let it run for approximately an hour to collect data.

    When enough data is collected, power estimation figures will be displayed in the first column of the output table.

### [10.8. Setting the measuring interval](#setting-the-measuring-interval) {#setting-the-measuring-interval .title}

By default, PowerTOP takes measurements in 20 seconds intervals. But, you can change this measuring frequency based on your requirements.

**Procedure**

-   To change the measuring frequency, run the `powertop`{.literal} command with the `--time`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # powertop --time=<time_in_seconds>
    ```

### [10.9. Controlling CPU frequency drivers and modes](#controlling-cpu-frequency-drivers-and-modes) {#controlling-cpu-frequency-drivers-and-modes .title}

While using the Intel P-State driver, PowerTOP only displays values in the `Frequency Stats`{.literal} tab if the driver is in passive mode. But, even in this case, the values can be incomplete.

The **Intel P-State** driver supports the following modes:

-   Active mode with Hardware P-States (HWP)
-   Active mode without HWP
-   Passive mode

Switching to the ACPI CPUfreq driver results in complete information being displayed by PowerTOP. However, it is recommended to keep your system on the default settings.

**Procedure**

1.  View what driver is loaded and in what mode:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_driver
    ```

    -   *intel_pstate* is returned if the **Intel P-State** driver is loaded and in active mode.
    -   *intel_cpufreq* is returned if the **Intel P-State** driver is loaded and in passive mode.
    -   *acpi-cpufreq* is returned if the **ACPI CPUfreq** driver is loaded.

2.  While using the **Intel P-State** driver:

    a.  Add the following argument to the kernel boot command line to force the driver to run in passive mode:

        ``` {.language-plaintext tabindex="-1"}
        intel_pstate=passive
        ```

    b.  To disable the **Intel P-State** driver and use the **ACPI CPUfreq** driver, add the following argument to the kernel boot command line:

        ``` {.language-plaintext tabindex="-1"}
        intel_pstate=disable
        ```

### [10.10. Generating an HTML output](#generating-an-html-output) {#generating-an-html-output .title}

You can also generate an HTML report apart from the powertop's output in the command line.

**Procedure**

-   Run the `powertop`{.literal} command with the `--html`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # powertop --html=<htmlfile.html>
    ```

    Replace the *\<htmlfile.html\>* parameter with the required name for the output file.

### [10.11. Optimizing power consumption](#optimizing-power-consumption) {#optimizing-power-consumption .title}

You can use either the `powertop`{.literal} service or the `powertop2tuned`{.literal} utility to optimize power consumption.

#### [10.11.1. Optimizing power consumption using the powertop service](#optimizing-power-consumption-using-the-powertop-service) {#optimizing-power-consumption-using-the-powertop-service .title}

You can use the `powertop`{.literal} service to automatically enable all PowerTOP's suggestions from the **Tunables** tab on the boot.

**Procedure**

-   Enable the `powertop`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable powertop
    ```

#### [10.11.2. The powertop2tuned utility](#the-powertop2tuned-utility) {#the-powertop2tuned-utility .title}

Use the `powertop2tuned`{.literal} utility to create custom **TuneD** profiles from PowerTOP suggestions. By default, `powertop2tuned`{.literal} creates profiles in the `/etc/tuned/profiles/`{.literal} directory, and bases the custom profile on the currently selected **TuneD** profile.

For safety reasons, all PowerTOP tunings are initially disabled in the new profile. You can enable the tunings by uncommenting them in the `/etc/tuned/profiles/profile_name/tuned.conf`{.literal} file.

Use the `--enable`{.literal} or `-e`{.literal} option to generate a new profile that enables most of the tunings suggested by PowerTOP. Certain potentially problematic tunings, such as the USB `autosuspend`{.literal}, are disabled by default and need to be uncommented manually.

#### [10.11.3. Optimizing power consumption using the powertop2tuned utility](#optimizing-power-consumption-using-the-powertop2tuned-utility) {#optimizing-power-consumption-using-the-powertop2tuned-utility .title}

You can use the `powertop2tuned`{.literal} utility to generate a custom TuneD profile that helps optimize your system's power consumption.

**Prerequisites**

-   The `powertop2tuned`{.literal} utility is installed on the system.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tuned-utils
    ```

**Procedure**

1.  Create a custom profile:

    ``` {.language-plaintext tabindex="-1"}
    # powertop2tuned <new_profile_name>
    ```

2.  Activate the new profile:

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile <new_profile_name>
    ```

#### [10.11.4. Comparing powertop2tuned and powertop.service usage](#comparing-powertop2tuned-and-powertop-service-usage) {#comparing-powertop2tuned-and-powertop.service-usage .title}

You can prefer optimizing power consumption with `powertop2tuned`{.literal} over `powertop.service`{.literal} for the following reasons:

-   The `powertop2tuned`{.literal} utility represents integration of PowerTOP into TuneD, which enables the benefit of both tools.
-   The `powertop2tuned`{.literal} utility provides fine-grained control of enabled tuning.
-   With `powertop2tuned`{.literal}, potentially dangerous tuning is not automatically enabled.
-   With `powertop2tuned`{.literal}, rollback is possible without reboot.

## [Chapter 11. Getting started with perf](#getting-started-with-perf) {#chapter-11.-getting-started-with-perf .title}

As a system administrator, you can use the `perf`{.literal} tool to collect and analyze performance data of your system. The `perf`{.literal} user-space tool interfaces with the kernel-based subsystem Performance Counters for Linux (PCL).

`perf`{.literal} uses the Performance Monitoring Unit (PMU) to measure, record, and monitor a variety of hardware and software events. `perf`{.literal} also supports `tracepoints`{.literal}, `kprobes`{.literal}, and `uprobes`{.literal}.

### [11.1. Installing perf](#installing-perf) {#installing-perf .title}

You must install the `perf`{.literal} user-space tool to start using the `perf`{.literal} tool.

**Procedure**

-   Install the perf tool:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install perf
    ```

### [11.2. Common perf commands](#common-perf-commands) {#common-perf-commands .title}

You can use the following commonly used `perf`{.literal} commands to collect and analyze performance data.

perf stat
:   Provides overall statistics for common performance events, including instructions run and clock cycles used. Options allow for selection of events other than the default measurement events.

perf record
:   Records performance data into a file, `perf.data`{.literal}, which can be later analyzed by using the `perf report`{.literal} command.

perf report
:   Reads and displays the performance data from the `perf.data`{.literal} file created by the `perf record`{.literal} command.

perf list
:   Lists the events available on a particular machine. These events vary based on performance monitoring hardware and software configuration of the system.

perf top
:   Performs a similar function to the top utility. It generates and displays a performance counter profile in real time.

perf trace
:   Performs a similar function to the `strace`{.literal} tool. It monitors the system calls used by a specified thread or process and all signals received by that application.

perf help
:   Displays a complete list of the `perf`{.literal} commands.

## [Chapter 12. Profiling CPU usage in real time with perf top](#profiling-cpu-usage-in-real-time-with-perf-top) {#chapter-12.-profiling-cpu-usage-in-real-time-with-perf-top .title}

You can use the `perf top`{.literal} command to measure CPU usage of different functions in real time.

### [12.1. The purpose of perf top](#the-purpose-of-perf-top) {#the-purpose-of-perf-top .title}

The `perf top`{.literal} command performs real-time system profiling and functions similarly to the `top`{.literal} utility. While `top`{.literal} monitors process CPU usage, `perf top`{.literal} displays CPU time by specific function.

In its default state, `perf top`{.literal} informs about functions being used across all CPUs in both the user-space and the kernel-space. To use `perf top`{.literal}, you need root access.

### [12.2. Profiling CPU usage with perf top](#profiling-cpu-usage-with-perf-top) {#profiling-cpu-usage-with-perf-top .title}

You can use `perf top`{.literal} to monitor real-time CPU usage and identify functions consuming the most processing time.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").
-   You have root access.

**Procedure**

-   Start the perf top monitoring interface:

    ``` {.language-plaintext tabindex="-1"}
    # perf top
    ```

    ``` {.language-plaintext tabindex="-1"}
    The monitoring interface looks similar to the following:
    Samples: 8K of event 'cycles', 2000 Hz, Event count (approx.): 4579432780 lost: 0/0 drop: 0/0
    Overhead  Shared Object       Symbol
       2.20%  [kernel]            [k] do_syscall_64
       2.17%  [kernel]            [k] module_get_kallsym
       1.49%  [kernel]            [k] copy_user_enhanced_fast_string
       1.37%  libpthread-2.29.so  [.] pthread_mutex_lock 1.31% [unknown] [.] 0000000000000000 1.07% [kernel] [k] psi_task_change 1.04% [kernel] [k] switch_mm_irqs_off 0.94% [kernel] [k] fget
       0.74%  [kernel]            [k] entry_SYSCALL_64
       0.69%  [kernel]            [k] syscall_return_via_sysret
       0.69%  libxul.so           [.] 0x000000000113f9b0
       0.67%  [kernel]            [k] kallsyms_expand_symbol.constprop.0
       0.65%  firefox             [.] moz_xmalloc
       0.65%  libpthread-2.29.so  [.] __pthread_mutex_unlock_usercnt
       0.60%  firefox             [.] free
       0.60%  libxul.so           [.] 0x000000000241d1cd
       0.60%  [kernel]            [k] do_sys_poll
       0.58%  [kernel]            [k] menu_select
       0.56%  [kernel]            [k] _raw_spin_lock_irqsave
       0.55%  perf                [.] 0x00000000002ae0f3
    ```

    In this example, the kernel function `do_syscall_64`{.literal} is using the most CPU time.

### [12.3. Perf output and symbol resolution](#understanding-perf-output-and-symbol-resolution) {#perf-output-and-symbol-resolution .title}

The `perf top`{.literal} monitoring interface provides a real-time view of CPU usage and function activity. Understanding its output helps identify performance bottlenecks and optimizes system behavior.

Key columns in perf top output
:   The interface displays several following columns:

Overhead
:   Shows the percentage of CPU time consumed by a given function. This helps pinpoint the most `resource-intensive`{.literal} operations.

Shared Object
:   Indicates the name of the program or library where the function resides.

Symbol

:   Displays the name of the function or symbol.

    -   Functions running in kernel space are marked with \[k\].
    -   Functions running in user space are marked with \[.\].

Causes of unresolved symbols in perf output

:   For kernel functions, `perf`{.literal} uses the information from the `/proc/kallsyms`{.literal} file to map the samples to their respective function names or symbols. For functions running in the user space, however, you might see raw function addresses because the binary is stripped.

    This information can be included by installing the corresponding debuginfo package or by compiling the application with debugging enabled, such as using the `-g`{.literal} option in `gcc`{.literal}. Once the necessary debug information is available, `perf`{.literal} can accurately map sampled addresses to human-readable function names during reporting.

    Note

    After making debug information available, it is not necessary to re-run the `perf record`{.literal} command. Running the `perf report`{.literal} command again will reflect the resolved symbols.

**Additional resources**

-   [Enabling debugging with debugging information](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/developing_c_and_cpp_applications_in_rhel_10/index#enabling-debugging-with-debugging-information)

### [12.4. Enabling debug and source repositories](#enabling-debug-and-source-repositories) {#enabling-debug-and-source-repositories .title}

To access essential debugging data for system components, enable debug and source repositories. RHEL disables these by default to save space. Enable them to install debuginfo packages required for performance measurement and deep system troubleshooting.

**Procedure**

-   Enable the source and debug information package channels:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable rhel-10-for-$(uname -m)-baseos-debug-rpms
    ```

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable rhel-10-for-$(uname -m)-baseos-source-rpms
    ```

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable rhel-10-for-$(uname -m)-appstream-debug-rpms
    ```

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable rhel-10-for-$(uname -m)-appstream-source-rpms
    ```

    The `$(uname -m)`{.literal} part is automatically replaced with a matching value for architecture of your system:

    +-----------------------------------+-----------------------------------+
    | Architecture name                 | Value                             |
    +:==================================+:==================================+
    | 64-bit Intel and AMD              | x86_64                            |
    +-----------------------------------+-----------------------------------+
    | 64-bit ARM                        | aarch64                           |
    +-----------------------------------+-----------------------------------+
    | IBM POWER                         | ppc64le                           |
    +-----------------------------------+-----------------------------------+
    | 64-bit IBM Z                      | s390x                             |
    +-----------------------------------+-----------------------------------+

    : Table 12.1. Architecture name mappings

    Show more

### [12.5. Getting debuginfo packages for an application or library by using GDB](#getting-debuginfo-packages-for-an-application-or-library-using-gdb) {#getting-debuginfo-packages-for-an-application-or-library-by-using-gdb .title}

When you debug an issue and the installed package lacks the required debugging information, the GNU Debugger detects the missing information. It then suggests commands to install the corresponding debug packages.

**Prerequisites**

-   The application or library you want to debug must be installed on the system.
-   GDB and the `debuginfo-install`{.literal} tool must be installed on the system. For details, see [Installing tools for debugging applications](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/developing_c_and_cpp_applications_in_rhel_10/index#installing-tools-for-debugging-applications).
-   Repositories providing `debuginfo`{.literal} and `debugsource`{.literal} packages must be configured and enabled on the system. For details, see [Enabling debug and source repositories](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/developing_c_and_cpp_applications_in_rhel_10/index#enabling-debug-and-source-repositories).

**Procedure**

1.  Start GDB attached to the application or library you want to debug. GDB automatically recognizes missing debugging information and suggests a command to run.

    ``` {.language-plaintext tabindex="-1"}
    $ gdb -q /bin/ls
    ```

    ``` {.language-plaintext tabindex="-1"}
    Reading symbols from /bin/ls...Reading symbols from .gnu_debugdata for /usr/bin/ls...(no debugging symbols found)...done.
    (no debugging symbols found)...done.
    Missing separate debuginfos, use: dnf debuginfo-install coreutils-9.5-6.el10.x86_64
    (gdb)
    ```

2.  To exit GDB, type q and confirm with Enter.

    ``` {.language-plaintext tabindex="-1"}
    (gdb) q
    ```

3.  Run the command suggested by GDB to install the required `debuginfo`{.literal} packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf debuginfo-install coreutils-9.5-6.el10.x86_64
    ```

    The dnf package management tool provides a summary of the changes, asks for confirmation and once you confirm, downloads and installs all the necessary files. In case GDB is not able to suggest the `debuginfo`{.literal} package, follow the procedure described in [Getting `debuginfo`{.literal} packages for an application or library manually](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/developing_c_and_cpp_applications_in_rhel_10/index#getting-debuginfo-packages-for-an-application-or-library-manually).

**Additional resources**

-   [How can I download or install debuginfo packages for RHEL systems? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/9907)

## [Chapter 13. Counting events during process execution with perf stat](#counting-events-during-process-execution-with-perf-stat) {#chapter-13.-counting-events-during-process-execution-with-perf-stat .title}

You can use the `perf stat`{.literal} command to count hardware and software events during process execution.

### [13.1. The purpose of perf stat](#the-purpose-of-perf-stat) {#the-purpose-of-perf-stat .title}

The `perf stat`{.literal} command generates counts for hardware and software performance events. If you do not specify any events, then `perf stat`{.literal} counts a set of common hardware and software events.

### [13.2. Counting events with perf stat](#counting-events-with-perf-stat) {#counting-events-with-perf-stat .title}

You can use `perf stat`{.literal} to count hardware and software event occurrences while a command is running and generate statistics of these counts. By default, `perf stat`{.literal} operates in per-thread mode.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed as described in [Installing perf](#installing-perf "11.1. Installing perf").
-   You have root access to count both user-space and kernel-space events.

**Procedure**

-   Count the events.

    -   Running the `perf stat`{.literal} command without root access will only count events occurring in the user space:

        ``` {.language-plaintext tabindex="-1"}
        $ perf stat ls
        ```

        ``` {.language-plaintext tabindex="-1"}
        Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos

         Performance counter stats for 'ls':

                      1.28 msec task-clock:u               #    0.165 CPUs utilized
                         0      context-switches:u         #    0.000 M/sec
                         0      cpu-migrations:u           #    0.000 K/sec
                       104      page-faults:u              #    0.081 M/sec
                 1,054,302      cycles:u                   #    0.823 GHz
                 1,136,989      instructions:u             #    1.08  insn per cycle
                   228,531      branches:u                 #  178.447 M/sec
                    11,331      branch-misses:u            #    4.96% of all branches

            0.007754312 seconds time elapsed
            0.000000000 seconds user
            0.007717000 seconds sys
        ```

        In the previous example, `perf stat`{.literal} runs without root access the event names are followed by `:u`{.literal}, indicating that these events were counted only in the user-space.

    -   To count both user-space and kernel-space events, enter:

        ``` {.language-plaintext tabindex="-1"}
        # perf stat ls
        ```

        ``` {.language-plaintext tabindex="-1"}
        Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
         Performance counter stats for 'ls':

                      3.09 msec task-clock                #    0.119 CPUs utilized
                        18      context-switches          #    0.006 M/sec
                         3      cpu-migrations            #    0.969 K/sec
                       108      page-faults               #    0.035 M/sec
                 6,576,004      cycles                    #    2.125 GHz
                 5,694,223      instructions              #    0.87  insn per cycle
                 1,092,372      branches                  #  352.960 M/sec
                    31,515      branch-misses             #    2.89% of all branches

        0.026020043 seconds time elapsed
        0.000000000 seconds user
        0.014061000 seconds sys
        ```

-   By default, `perf stat`{.literal} operates in per-thread mode. To change to CPU-wide event counting, pass the `-a`{.literal} option to `perf stat`{.literal}. To count CPU-wide events, you need root access:

    ``` {.language-plaintext tabindex="-1"}
    # perf stat -a ls
    ```

### [13.3. Interpretation of perf stat output](#interpretation-of-perf-stat-output) {#interpretation-of-perf-stat-output .title}

`perf stat`{.literal} executes a specified command and counts event occurrences during the command execution. It displays statistics of these counts in three columns:

-   The number of occurrences counted for a given event.
-   The name of the event that was counted.
-   When related metrics are available, a ratio or percentage is displayed after the hash sign (`#`{.literal}) in the right-most column. For example, in default mode, `perf stat`{.literal} counts cycles and instructions to calculate and display instructions per cycle in the right-most column. Branch misses as a percentage of total branches show similar behavior in default counts.

### [13.4. Attaching perf stat to a running process](#attaching-perf-stat-to-a-running-process) {#attaching-perf-stat-to-a-running-process .title}

You can attach `perf stat`{.literal} to a running process. This instructs `perf stat`{.literal} to count event occurrences only in the specified processes during the execution of a command.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed as described in [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Attach `perf stat`{.literal} to a running process:

    ``` {.language-plaintext tabindex="-1"}
    $ perf stat -p ID1,ID2 sleep seconds
    ```

    The previous example counts events in the processes with the IDs of `ID1`{.literal} and `ID2`{.literal} for a time period of `seconds`{.literal} seconds as dictated by using the `sleep`{.literal} command.

## [Chapter 14. Recording and analyzing performance profiles with perf](#recording-and-analyzing-performance-profiles-with-perf) {#chapter-14.-recording-and-analyzing-performance-profiles-with-perf .title}

Use the `perf`{.literal} tool to record performance data and analyze it at a later time.

### [14.1. The purpose of perf record](#the-purpose-of-perf-record) {#the-purpose-of-perf-record .title}

The `perf record`{.literal} command samples performance data and stores it in a `perf.data`{.literal} file. You can then read and visualize data with other perf commands. `perf.data`{.literal} is generated in the current directory. It can be accessed at a later time, possibly on a different machine.

You can profile the entire system by running `perf record -a`{.literal}. This records performance data until you press Ctrl+C or for the duration of a specific command. You can profile a single application/process by running `perf record ./your_app`{.literal} or by attaching to an already running one by using `perf record -p PID`{.literal}.

### [14.2. Recording a performance profile](#recording-a-performance-profile) {#recording-a-performance-profile .title}

You can use `perf record`{.literal} to sample and record performance data. The level of data captured depends on the access level. Without root access, `perf record`{.literal} collects data only in the user space. With root access, `perf record`{.literal} collects data in both the user and kernel space.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").
-   You have root access if you want to collect data for user and kernel space.

**Procedure**

-   Do one of the following:

    -   To sample and record the performance data for the user space:

        ``` {.language-plaintext tabindex="-1"}
        $ perf record command
        ```

    -   To sample and record the performance data for kernel space (use root or sudo access):

        ``` {.language-plaintext tabindex="-1"}
        # perf record command
        ```

        Replace *command* with the actual command you want to profile. If you do not specify a command, then `perf record`{.literal} samples data until you manually stop it by pressing Ctrl+C.

### [14.3. Recording a performance profile in per-CPU mode](#recording-a-performance-profile-in-per-cpu-mode) {#recording-a-performance-profile-in-per-cpu-mode .title}

Use `perf record`{.literal} in per-CPU mode to sample and record performance data across all threads on a monitored CPU. It captures data from both user space and kernel space simultaneously. By default, per-CPU mode monitors all online CPUs.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Sample and record the performance data:

    ``` {.language-plaintext tabindex="-1"}
    # perf record -a command
    ```

    Replace *command* with the command you want to sample data during. If you do not specify a command, then `perf record`{.literal} samples data until you manually stop it by pressing Ctrl+C.

### [14.4. Capturing call graph data with perf record](#capturing-call-graph-data-with-perf-record) {#capturing-call-graph-data-with-perf-record .title}

You can configure the `perf record`{.literal} tool so that it records which function calls other functions in the performance profile. This helps to identify a bottleneck if several processes are calling the same function.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Sample and record performance data with the `--call-graph`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    $ perf record --call-graph method command
    ```

    -   Replace *command* with the command you want to sample data during. If you do not specify a command, then `perf record`{.literal} samples data until you manually stop it by pressing Ctrl+C.

    -   Replace method with one of the following unwinding methods:

        fp
        :   Uses the frame pointer method. Depending on compiler optimization, such as with binaries built with the GCC option `--fomit-frame-pointer`{.literal}, this may not be able to unwind the stack.

        dwarf
        :   Uses DWARF Call Frame Information to unwind the stack.

        lbr
        :   Uses the last branch record hardware on Intel processors.

### [14.5. Analyzing perf.data with perf report](#analyzing-perf-data-with-perf-report) {#analyzing-perf.data-with-perf-report .title}

You can use `perf report`{.literal} to display and analyze data from the `perf.data`{.literal} file.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").
-   A `perf.data`{.literal} file is stored in the current directory.
-   You have the `root`{.literal} access, if the `perf.data`{.literal} file was created with root access.

**Procedure**

-   Display the contents of the perf.data file for further analysis:

    ``` {.language-plaintext tabindex="-1"}
    # perf report
    ```

    ``` {.language-plaintext tabindex="-1"}
    Samples: 2K of event 'cycles', Event count (approx.): 235462960
    Overhead  Command          Shared Object                     Symbol
       2.36%  kswapd0          [kernel.kallsyms]                 [k] page_vma_mapped_walk
       2.13%  sssd_kcm         libc-2.28.so                      [.] memset_avx2_erms 2.13% perf [kernel.kallsyms] [k] smp_call_function_single 1.53% gnome-shell libc-2.28.so [.] strcmp_avx2
       1.17%  gnome-shell      libglib-2.0.so.0.5600.4           [.] g_hash_table_lookup
       0.93%  Xorg             libc-2.28.so                      [.] memmove_avx_unaligned_erms 0.89% gnome-shell libgobject-2.0.so.0.5600.4 [.] g_object_unref 0.87% kswapd0 [kernel.kallsyms] [k] page_referenced_one 0.86% gnome-shell libc-2.28.so [.] memmove_avx_unaligned_erms
       0.83%  Xorg             [kernel.kallsyms]                 [k] alloc_vmap_area
       0.63%  gnome-shell      libglib-2.0.so.0.5600.4           [.] g_slice_alloc
       0.53%  gnome-shell      libgirepository-1.0.so.1.0.0      [.] g_base_info_unref
       0.53%  gnome-shell      ld-2.28.so                        [.] _dl_find_dso_for_object
       0.49%  kswapd0          [kernel.kallsyms]                 [k] vma_interval_tree_iter_next
    0.48%  gnome-shell      libpthread-2.28.so                [.] pthread_getspecific 0.47% gnome-shell libgirepository-1.0.so.1.0.0 [.] 0x0000000000013b1d 0.45% gnome-shell libglib-2.0.so.0.5600.4 [.] g_slice_free1 0.45% gnome-shell libgobject-2.0.so.0.5600.4 [.] g_type_check_instance_is_fundamentally_a 0.44% gnome-shell libc-2.28.so [.] malloc 0.41% swapper [kernel.kallsyms] [k] apic_timer_interrupt 0.40% gnome-shell ld-2.28.so [.] _dl_lookup_symbol_x 0.39% kswapd0 [kernel.kallsyms] [k] raw_callee_save___pv_queued_spin_unlock
    ```

    For more information, see the `perf-record(1)`{.literal} man page on your system.

### [14.6. Attaching perf record to a running process](#attaching-perf-record-to-a-running-process) {#attaching-perf-record-to-a-running-process .title}

You can attach `perf`{.literal} record to a running process. This instructs `perf`{.literal} record to only sample and record performance data in the specified processes.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Attach `perf record`{.literal} to a running process:

    ``` {.language-plaintext tabindex="-1"}
    $ perf record -p ID1,ID2 sleep seconds
    ```

    This command samples and records performance data of the processes with the process ID's `ID1`{.literal} and `ID2`{.literal} for a time period of *`seconds`{.literal}* seconds as dictated by using the sleep command. You can also configure `perf`{.literal} to record events in specific threads:

    ``` {.language-plaintext tabindex="-1"}
    $ perf record -t ID1,ID2 sleep seconds
    ```

    Note

    When using the `-t`{.literal} flag and stipulating thread ID's, `perf`{.literal} disables inheritance by default. You can enable inheritance by adding the `--inherit`{.literal} option.

### [14.7. Interpretation of perf report output](#interpretation-of-perf-report-output) {#interpretation-of-perf-report-output .title}

The table displayed by running the `perf report`{.literal} command sorts the data into the following several columns:

Overhead
:   Indicates what percentage of overall samples were collected in that particular function.

Command
:   Tells you which process the samples were collected from.

Shared Object
:   Displays the ELF image name where the samples come from (the name \[kernel.kallsyms\] is used when the samples come from the kernel).

Symbol
:   Displays the function name or symbol. In default mode, the functions are sorted in descending order with those with the highest overhead displayed first.

### [14.8. Generating a perf.data file readable on a different device](#generating-a-perf-data-file-readable-on-a-different-device) {#generating-a-perf.data-file-readable-on-a-different-device .title}

You can use the `perf`{.literal} tool to record performance data into a `perf.data`{.literal} file to be analyzed on a different device.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").
-   The kernel `debuginfo`{.literal} package is installed. For more information, see [Getting debuginfo packages for an application or library using GDB](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/developing_c_and_cpp_applications_in_rhel_10/index#getting-debuginfo-packages-for-an-application-or-library-using-gdb).

**Procedure**

1.  Capture performance data you are interested in investigating further:

    ``` {.language-plaintext tabindex="-1"}
    # perf record -a --call-graph fp sleep <seconds>
    ```

    This example generates a `perf.data`{.literal} over the entire system for a period of *seconds* seconds as dictated by the use of the sleep command. It would also capture call graph data using the frame pointer method.

2.  Generate an archive file containing debug symbols of the recorded data:

    ``` {.language-plaintext tabindex="-1"}
    # perf archive
    ```

**Verification**

-   Verify that the archive file has been generated in your current active directory:

    ``` {.language-plaintext tabindex="-1"}
    # ls perf.data*
    ```

    The output will display every file in your current directory that begins with `perf.data`{.literal}. The archive file will be named either: `perf.data.tar.gz`{.literal} or `perf.data.tar.bz2`{.literal}.

**Additional resources**

-   [Recording and analyzing performance profiles with perf](#recording-and-analyzing-performance-profiles-with-perf "Chapter 14. Recording and analyzing performance profiles with perf")
-   [Capturing call graph data with perf record](#capturing-call-graph-data-with-perf-record "14.4. Capturing call graph data with perf record")

### [14.9. Analyzing a perf.data file from a different device](#analyzing-a-perf-data-file-from-a-different-device) {#analyzing-a-perf.data-file-from-a-different-device .title}

You can use the `perf`{.literal} tool to analyze a `perf.data`{.literal} file that was generated on a different device.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").
-   You have `perf.data`{.literal} and associated archive files generated on a different device.

**Procedure**

1.  Copy both the `perf.data`{.literal} file and the archive file into your current active directory.

2.  Extract the archive file into `~/.debug`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir -p ~/.debug
    ```

    ``` {.language-plaintext tabindex="-1"}
    # tar xf perf.data.tar.bz2 -C ~/.debug
    ```

    Note

    The archive file might also be named `perf.data.tar.gz`{.literal}.

3.  Open the `perf.data`{.literal} file for further analysis:

    ``` {.language-plaintext tabindex="-1"}
    # perf report
    ```

**Additional resources**

-   [Enabling debugging with debugging information](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/developing_c_and_cpp_applications_in_rhel_10/index#enabling-debugging-with-debugging-information)
-   [Getting debuginfo packages for an application or library using GDB](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/developing_c_and_cpp_applications_in_rhel_10/index#getting-debuginfo-packages-for-an-application-or-library-using-gdb)
-   [How can I download or install debuginfo packages for RHEL systems? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/9907)

## [Chapter 15. Investigating busy CPUs with perf](#investigating-busy-cpus-with-perf) {#chapter-15.-investigating-busy-cpus-with-perf .title}

When investigating performance issues on a system, use `perf`{.literal} to identify and monitor the busiest CPUs. This helps you focus your efforts.

### [15.1. Displaying CPU events counted with perf stat](#displaying-cpu-events-counted-with-perf-stat) {#displaying-cpu-events-counted-with-perf-stat .title}

You can use `perf stat`{.literal} to display which CPU events were counted on by disabling CPU count aggregation. You must count events in the system-wide mode by using the `-a`{.literal} flag in order to use this functionality.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Count the events with CPU count aggregation disabled:

    ``` {.language-plaintext tabindex="-1"}
    # perf stat -a -A sleep seconds
    ```

    This command displays the count of a default set of common hardware and software events recorded for a time-period of *seconds* seconds, as dictated by using the sleep command, over each CPU in ascending order, starting with CPU0. As such, it may be useful to specify an event such as cycles:

    ``` {.language-plaintext tabindex="-1"}
    # perf stat -a -A -e cycles sleep seconds
    ```

### [15.2. Displaying CPU samples taken with perf report](#displaying-cpu-samples-taken-with-perf-report) {#displaying-cpu-samples-taken-with-perf-report .title}

The `perf record`{.literal} command samples performance data and stores it in a `perf.data`{.literal} file. You can read this file by using the `perf report`{.literal} command. The `perf record`{.literal} command also records the CPU on which each sample was taken. To view this information, configure the `perf report`{.literal} command accordingly.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").
-   There is a `perf.data`{.literal} file created with perf record in the current directory. If the `perf.data`{.literal} file was created with root access, you need to run perf report with root access too.

**Procedure**

-   Display the contents of the `perf.data`{.literal} file for further analysis while sorting by CPU:

    ``` {.language-plaintext tabindex="-1"}
    # perf report --sort cpu
    ```

    -   You can sort by CPU and command to display more detailed information about where CPU time is being spent:

        ``` {.language-plaintext tabindex="-1"}
        # perf report --sort cpu,comm
        ```

        This example will list commands from all monitored CPUs by total overhead in descending order of overhead usage and identify the CPU the command was run.

**Additional resources**

-   [Recording and analyzing performance profiles with perf](#recording-and-analyzing-performance-profiles-with-perf "Chapter 14. Recording and analyzing performance profiles with perf")

### [15.3. Displaying specific CPUs during profiling with perf top](#displaying-specific-cpus-during-profiling-with-perf-top) {#displaying-specific-cpus-during-profiling-with-perf-top .title}

You can configure `perf top`{.literal} to display specific CPUs and their relative usage while profiling your system in real time.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Start the perf top interface while sorting by CPU:

    ``` {.language-plaintext tabindex="-1"}
    # perf top --sort cpu
    ```

    This command lists CPUs and their respective overhead in descending order of overhead usage in real time. You can sort by CPU and command for more detailed information of where CPU time is being spent:

    ``` {.language-plaintext tabindex="-1"}
    # perf top --sort cpu,comm
    ```

    This command lists commands by total overhead in descending order of overhead usage and identifies the CPU the command was run on in real time.

### [15.4. Monitoring specific CPUs by using perf record and perf report](#monitoring-specific-cpus-by-using-perf-record-and-perf-report) {#monitoring-specific-cpus-by-using-perf-record-and-perf-report .title}

Use `perf`{.literal} to sample performance data from specific CPUs and analyze the results to identify CPU-specific bottlenecks.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

1.  Record performance data from specific CPUs:

    Use the `-C`{.literal} option with `perf record`{.literal} to target specific CPUs. The following examples demonstrate how to specify individual CPUs or a range.

    -   To sample data from selected CPUs (comma-separated):

        ``` {.language-plaintext tabindex="-1"}
        # perf record -C 0,1 sleep <seconds>
        ```

        This command samples and records performance data from CPUs `0`{.literal} and `1`{.literal} for the specified number of seconds.

    -   To sample data from a range of CPUs:

        ``` {.language-plaintext tabindex="-1"}
        # perf record -C 0-2 sleep <seconds>
        ```

        This command samples and records performance data from CPUs `0`{.literal}, `1`{.literal}, and `2`{.literal} over the specified duration.

2.  Analyze the recorded performance data:

    Use the `perf report`{.literal} command to read and analyze the `perf.data`{.literal} file.

    ``` {.language-plaintext tabindex="-1"}
    # perf report
    ```

    This command displays the contents of the `perf.data`{.literal} file.

    Note

    If you want to see which CPU each sample was recorded on, see Displaying which CPU samples were taken on with perf report.

## [Chapter 16. Creating uprobes with perf](#creating-uprobes-with-perf) {#chapter-16.-creating-uprobes-with-perf .title}

`Uprobes`{.literal} (user-space probes) provide dynamic instrumentation for user-space applications at runtime. They require no source code changes or recompilation.

There are two primary use cases where `uprobes`{.literal} are useful:

Debugging and performance analysis
:   `Uprobes`{.literal} function similarly to watchpoints. You can insert them at specific locations in your application to count how often those code paths are run. Additionally, they can capture rich context such as call stacks or variable values. Use them to identify performance bottlenecks or track bugs.

Event-based data collection
:   `Uprobes`{.literal} act as switching events for mechanisms such as circular buffers. They can control when data is recorded or flushed based on execution triggers in user space.

`Uprobes`{.literal} integrate seamlessly with `perf`{.literal}, which can both consume existing `uprobes`{.literal} and create new ones. This flexibility enables powerful, non-intrusive observability and profiling of user-space behavior alongside kernel-space instrumentation (by using `kprobes`{.literal}).

### [16.1. Creating uprobes at the function level with perf](#creating-uprobes-at-the-function-level-with-perf) {#creating-uprobes-at-the-function-level-with-perf .title}

Use the `perf`{.literal} tool to create dynamic tracepoints at arbitrary points in a process or application. Use these tracepoints with `perf stat`{.literal} or `perf record`{.literal} to analyze process and application behavior.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Create the uprobe in the process or application you are interested in monitoring at a location of interest within the process or application:

    ``` {.language-plaintext tabindex="-1"}
    # perf probe -x /path/to/executable -a function
    ```

    ``` {.language-plaintext tabindex="-1"}
    Added new event:
      probe_executable:function   (on function in /path/to/executable)

    You can now use it in all perf tools, such as:
        perf record -e probe_executable:function -aR sleep 1
    ```

**Additional resources**

-   [Recording and analyzing performance profiles with perf](#recording-and-analyzing-performance-profiles-with-perf "Chapter 14. Recording and analyzing performance profiles with perf")
-   [Counting events during process execution with perf stat](#counting-events-during-process-execution-with-perf-stat "Chapter 13. Counting events during process execution with perf stat")

### [16.2. Creating uprobes on lines within a function with perf](#creating-uprobes-on-lines-within-a-function-with-perf) {#creating-uprobes-on-lines-within-a-function-with-perf .title}

You can use the tracepoints conjunction with other `perf`{.literal} tools such as `perf stat`{.literal} and `perf record`{.literal} to better understand the process or application behavior.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

-   You have received the debugging symbols for your executable:

    ``` {.language-plaintext tabindex="-1"}
    # objdump -t ./your_executable | head
    ```

    Note

    To do this, install the `debuginfo`{.literal} package of the executable. If the executable is a locally developed application, compile the application with debugging information by using the `-g`{.literal} option in GCC.

**Procedure**

1.  View the function lines where you can place a `uprobe`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ perf probe -x ./your_executable -L main
    ```

    ``` {.language-plaintext tabindex="-1"}
    <main@/home/user/my_executable:0>
                  0  int main(int argc, const char *argv) 1 { int err; const char *cmd; char sbuf[STRERR_BUFSIZE]; / libsubcmd init */
                  7         exec_cmd_init("perf", PREFIX, PERF_EXEC_PATH, EXEC_PATH_ENVIRONMENT);
    8         pager_init(PERF_PAGER_ENVIRONMENT);
    ```

2.  Create the `uprobe`{.literal} for the function line that you want to monitor:

    ``` {.language-plaintext tabindex="-1"}
    # perf probe -x ./my_executable main:8
    ```

    ``` {.language-plaintext tabindex="-1"}
    Added new event:
              probe_my_executable:main_L8   (on main:8 in /home/user/my_executable)

    you can now use it in all perf tools, such as:

    Perf record -e probe_my_executable:main_L8 -aR sleep 1
    ```

### [16.3. Perf script output of data recorded over uprobes](#perf-script-output-of-data-recorded-over-uprobes) {#perf-script-output-of-data-recorded-over-uprobes .title}

A common method to analyze data collected with `uprobes`{.literal} is to run the perf script command. It which reads the `perf.data`{.literal} file and displays a detailed trace of the recorded workload.

In the perf script example output

:   -   A `uprobe`{.literal} is added to the function `isprime()`{.literal} in a program called `my_prog`{.literal}

    -   `a`{.literal} is a function argument added to the `uprobe`{.literal}. Alternatively, `a`{.literal} could be an arbitrary variable visible in the code scope of where you add your `uprobe`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # perf script
        ```

        ``` {.language-plaintext tabindex="-1"}
            my_prog  1367 [007] 10802159.906593: probe_my_prog:isprime: (400551) a=2
            my_prog  1367 [007] 10802159.906623: probe_my_prog:isprime: (400551) a=3
            my_prog  1367 [007] 10802159.906625: probe_my_prog:isprime: (400551) a=4
            my_prog  1367 [007] 10802159.906627: probe_my_prog:isprime: (400551) a=5
            my_prog  1367 [007] 10802159.906629: probe_my_prog:isprime: (400551) a=6
            my_prog  1367 [007] 10802159.906631: probe_my_prog:isprime: (400551) a=7
            my_prog  1367 [007] 10802159.906633: probe_my_prog:isprime: (400551) a=13
            my_prog  1367 [007] 10802159.906635: probe_my_prog:isprime: (400551) a=17
            my_prog  1367 [007] 10802159.906637: probe_my_prog:isprime: (400551) a=19
        ```

## [Chapter 17. Profiling memory accesses with perf mem](#profiling-memory-accesses-with-perf-mem) {#chapter-17.-profiling-memory-accesses-with-perf-mem .title}

You can use the `perf mem`{.literal} command to sample memory accesses on your system. The `mem`{.literal} subcommand of the `perf`{.literal} tool enables the sampling of memory accesses (loads and stores).

The `perf mem`{.literal} command tracks memory latency, access types, and cache hits. Recording data symbols also identifies memory locations for these events.

### [17.1. Sampling memory access with perf mem](#sampling-memory-access-with-perf-mem) {#sampling-memory-access-with-perf-mem .title}

You can use the `perf mem`{.literal} command to sample memory accesses on your system. The command takes the same options as `perf record`{.literal} and `perf report`{.literal} as well as some options exclusive to the `mem`{.literal} sub-command. The recorded data is stored in a `perf.data`{.literal} file in the current directory for later analysis.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

1.  Sample the memory accesses:

    ``` {.language-plaintext tabindex="-1"}
    # perf mem record -a sleep <seconds>
    ```

    This command samples memory accesses across all CPUs for a period of *`<seconds>`{.literal}* seconds as dictated by the `sleep`{.literal} command. You can replace the `sleep`{.literal} command for any command during which you want to sample memory access data. By default, `perf mem`{.literal} samples both memory loads and stores. You can select only one memory operation by using the `-t`{.literal} option and specifying either `load`{.literal} or `store`{.literal} between `perf mem`{.literal} and `record`{.literal}. For loads, information over the memory hierarchy level, TLB memory accesses, bus snoops, and memory locks is captured.

2.  Open the `perf.data`{.literal} file for analysis:

    ``` {.language-plaintext tabindex="-1"}
    # perf mem report
    ```

    If you have used the example commands, the output is:

    ``` {.language-plaintext tabindex="-1"}
    Available samples
    35k cpu/mem-loads,ldlat=30/P
    54k cpu/mem-stores/P
    ```

    The `cpu/mem-loads,ldlat=30/P`{.literal} line denotes data collected over memory loads and the `cpu/mem-stores/P`{.literal} line denotes data collected over memory stores. Highlight the category of interest and press Enter to view the data:

    ``` {.language-plaintext tabindex="-1"}
    Samples: 35K of event 'cpu/mem-loads,ldlat=30/P', Event count (approx.): 4067062
    Overhead       Samples  Local Weight  Memory access             Symbol                                                                 Shared Object                 Data Symbol                                                     Data Object                            Snoop         TLB access              Locked
       0.07%            29  98            L1 or L1 hit              [.] 0x000000000000a255                                                 libspeexdsp.so.1.5.0          [.] 0x00007f697a3cd0f0                                          anon                                   None          L1 or L2 hit            No
       0.06%            26  97            L1 or L1 hit              [.] 0x000000000000a255                                                 libspeexdsp.so.1.5.0          [.] 0x00007f697a3cd0f0                                          anon                                   None          L1 or L2 hit            No
       0.06%            25  96            L1 or L1 hit              [.] 0x000000000000a255                                                 libspeexdsp.so.1.5.0          [.] 0x00007f697a3cd0f0                                          anon                                   None          L1 or L2 hit            No
       0.06%             1  2325          Uncached or N/A hit       [k] pci_azx_readl                                                      [kernel.kallsyms]             [k] 0xffffb092c06e9084                                          [kernel.kallsyms]                      None          L1 or L2 hit            No
       0.06%             1  2247          Uncached or N/A hit       [k] pci_azx_readl                                                      [kernel.kallsyms]             [k] 0xffffb092c06e8164                                          [kernel.kallsyms]                      None          L1 or L2 hit            No
       0.05%             1  2166          L1 or L1 hit              [.] 0x00000000038140d6                                                 libxul.so                     [.] 0x00007ffd7b84b4a8                                          [stack]                                None          L1 or L2 hit            No
       0.05%             1  2117          Uncached or N/A hit       [k] check_for_unclaimed_mmio                                           [kernel.kallsyms]             [k] 0xffffb092c1842300                                          [kernel.kallsyms]                      None          L1 or L2 hit            No
       0.05%            22  95            L1 or L1 hit              [.] 0x000000000000a255                                                 libspeexdsp.so.1.5.0          [.] 0x00007f697a3cd0f0                                          anon                                   None          L1 or L2 hit            No
       0.05%             1  1898          L1 or L1 hit              [.] 0x0000000002a30e07                                                 libxul.so                     [.] 0x00007f610422e0e0                                          anon                                   None          L1 or L2 hit            No
       0.05%             1  1878          Uncached or N/A hit       [k] pci_azx_readl                                                      [kernel.kallsyms]             [k] 0xffffb092c06e8164                                          [kernel.kallsyms]                      None          L2 miss                 No
       0.04%            18  94            L1 or L1 hit              [.] 0x000000000000a255                                                 libspeexdsp.so.1.5.0          [.] 0x00007f697a3cd0f0                                          anon                                   None          L1 or L2 hit            No
       0.04%             1  1593          Local RAM or RAM hit      [.] 0x00000000026f907d                                                 libxul.so                     [.] 0x00007f3336d50a80                                          anon                                   Hit           L2 miss                 No
       0.03%             1  1399          L1 or L1 hit              [.] 0x00000000037cb5f1                                                 libxul.so                     [.] 0x00007fbe81ef5d78                                          libxul.so                              None          L1 or L2 hit            No
       0.03%             1  1229          LFB or LFB hit            [.] 0x0000000002962aad                                                 libxul.so                     [.] 0x00007fb6f1be2b28                                          anon                                   None          L2 miss                 No
       0.03%             1  1202          LFB or LFB hit            [.] __pthread_mutex_lock                                               libpthread-2.29.so            [.] 0x00007fb75583ef20                                          anon                                   None          L1 or L2 hit            No
       0.03%             1  1193          Uncached or N/A hit       [k] pci_azx_readl                                                      [kernel.kallsyms]             [k] 0xffffb092c06e9164                                          [kernel.kallsyms]                      None          L2 miss                 No
    0.03%             1  1191          L1 or L1 hit              [k] azx_get_delay_from_lpib                                            [kernel.kallsyms]             [k] 0xffffb092ca7efcf0                                          [kernel.kallsyms]                      None          L1 or L2 hit            No
    ```

3.  Optional: Sort your results to investigate different aspects of interest when displaying the data. For example, to sort data over memory loads by type of memory accesses occurring during the sampling period in descending order of overhead they account for:

    ``` {.language-plaintext tabindex="-1"}
    # perf mem -t load report --sort=mem
    ```

    For example, the output can be:

    ``` {.language-plaintext tabindex="-1"}
    Samples: 35K of event 'cpu/mem-loads,ldlat=30/P', Event count (approx.): 40670
    Overhead       Samples  Memory access
      31.53%          9725  LFB or LFB hit
      29.70%         12201  L1 or L1 hit
      23.03%          9725  L3 or L3 hit
      12.91%          2316  Local RAM or RAM hit
       2.37%           743  L2 or L2 hit
       0.34%             9  Uncached or N/A hit
       0.10%            69  I/O or N/A hit
       0.02%           825  L3 miss
    ```

### [17.2. Interpretation of perf mem report output](#interpretation-of-perf-mem-report-output) {#interpretation-of-perf-mem-report-output .title}

When you run the `perf mem report`{.literal} command without any modifiers sorts the data into several columns:

Overhead
:   Indicates percentage of overall samples collected in that particular function.

Samples
:   Displays the number of samples accounted for by that row.

Local Weight
:   Displays the access latency in processor core cycles.

Memory Access
:   Displays the type of memory access that occurred.

Symbol
:   Displays the function name or symbol.

Shared Object
:   Displays the ELF image name where the samples come from (the name `[kernel.kallsyms]`{.literal} is used when the samples come from the kernel).

Data Symbol

:   Displays the address of the memory location that row was targeting.

    Important

    The `Data Symbol`{.literal} column might display a raw address due to dynamic allocation of memory or stack memory being accessed.

Snoop
:   Displays bus transactions.

TLB Access
:   Displays TLB memory accesses.

Locked
:   Indicates if a function was or was not memory locked. In default mode, the functions are sorted in descending order with those with the highest overhead displayed first.

## [Chapter 18. Detecting false sharing](#detecting-false-sharing) {#chapter-18.-detecting-false-sharing .title}

False sharing occurs when a processor core on a Symmetric Multi Processing (SMP) system modifies different data items located on the same cache line. These processors access other data items that are not being shared between the processors.

Modified cache lines force other processors to invalidate and update their copies, even if they do not need the modified data.

You can use the `perf c2c`{.literal} command to detect false sharing.

### [18.1. The purpose of perf c2c](#the-purpose-of-perf-c2c) {#the-purpose-of-perf-c2c .title}

The `c2c`{.literal} subcommand of the `perf`{.literal} tool enables Shared Data Cache-to-Cache (C2C) analysis. You can use the `perf c2c`{.literal} command to inspect cache-line contention to detect both true and false sharing.

Cache-line contention occurs when a processor core modifies data on a cache line shared by other processors. All other processors using this cache-line then must invalidate their copy and request an updated one. This can lead to degraded performance.

The `perf c2c`{.literal} command provides the following information:

-   Cache lines where contention has been detected
-   Processes reading and writing the data
-   Instructions causing the contention
-   The Non-Uniform Memory Access (NUMA) nodes involved in the contention

### [18.2. Detecting cache-line contention with perf c2c](#detecting-cache-line-contention-with-perf-c2c) {#detecting-cache-line-contention-with-perf-c2c .title}

You can use the `perf c2c`{.literal} command to detect cache-line contention in a system. The `perf c2c`{.literal} command supports the same options as `perf record`{.literal} as well as some options exclusive to the `c2c`{.literal} subcommand. The recorded data is stored in a `perf.data`{.literal} file in the current directory for later analysis.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Use `perf c2c`{.literal} to detect cache-line contention:

    ``` {.language-plaintext tabindex="-1"}
    # perf c2c record -a sleep <seconds>
    ```

    This command samples and records cache-line contention data across all CPU's for a period of *`<seconds>`{.literal}* as dictated by the `sleep`{.literal} command. You can replace the `sleep`{.literal} command with any command you want to collect cache-line contention data over.

### [18.3. Visualizing a perf.data file recorded with perf c2c record](#visualizing-a-perf-data-file-recorded-with-perf-c2c-record) {#visualizing-a-perf.data-file-recorded-with-perf-c2c-record .title}

You can visualize the `perf.data`{.literal} file that is recorded with the `perf c2c`{.literal} command.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").
-   A `perf.data`{.literal} file recorded by using the `perf c2c`{.literal} command is available in the current directory. For more information, see [Detecting cache-line contention with perf c2c](#detecting-cache-line-contention-with-perf-c2c "18.2. Detecting cache-line contention with perf c2c").

**Procedure**

1.  Open the `perf.data`{.literal} file for analysis:

    ``` {.language-plaintext tabindex="-1"}
    # perf c2c report --stdio
    ```

    This command visualizes the `perf.data`{.literal} file into several graphs within the command line:

    ``` {.language-plaintext tabindex="-1"}
    =================================================
               Trace Event Information
    =================================================
     Total records                     :     329219
     Locked Load/Store Operations      :      14654
     Load Operations                   :      69679
     Loads - uncacheable               :          0
     Loads - IO                        :          0
     Loads - Miss                      :       3972
     Loads - no mapping                :          0
     Load Fill Buffer Hit              :      11958
     Load L1D hit                      :      17235
     Load L2D hit                      :         21
     Load LLC hit                      :      14219
     Load Local HITM                   :       3402
     Load Remote HITM                  :      12757
     Load Remote HIT                   :       5295
     Load Local DRAM                   :        976
     Load Remote DRAM                  :       3246
     Load MESI State Exclusive         :       4222
     Load MESI State Shared            :          0
     Load LLC Misses                   :      22274
     LLC Misses to Local DRAM          :        4.4%
     LLC Misses to Remote DRAM         :       14.6%
     LLC Misses to Remote cache (HIT)  :       23.8%
     LLC Misses to Remote cache (HITM) :       57.3%
     Store Operations                  :     259539
     Store - uncacheable               :          0
     Store - no mapping                :         11
     Store L1D Hit                     :     256696
     Store L1D Miss                    :       2832
     No Page Map Rejects               :       2376
     Unable to parse data source       :          1

    =================================================
       Global Shared Cache Line Event Information
    =================================================
     Total Shared Cache Lines          :         55
     Load HITs on shared lines         :      55454
     Fill Buffer Hits on shared lines  :      10635
     L1D hits on shared lines          :      16415
     L2D hits on shared lines          :          0
     LLC hits on shared lines          :       8501
     Locked Access on shared lines     :      14351
     Store HITs on shared lines        :     109953
     Store L1D hits on shared lines    :     109449
     Total Merged records              :     126112

    =================================================
                     c2c details
    =================================================
     Events                            : cpu/mem-loads,ldlat=30/P
                                            : cpu/mem-stores/P
     Cachelines sort on                : Remote HITMs
     Cacheline data grouping          : offset,pid,iaddr

    =================================================
           Shared Data Cache Line Table
    =================================================
    #
    #                              Total      Rmt  ----- LLC Load Hitm -----  ---- Store Reference ----  --- Load Dram ----      LLC    Total  ----- Core Load Hit -----  -- LLC Load Hit --
    # Index           Cacheline  records     Hitm    Total      Lcl      Rmt    Total    L1Hit   L1Miss       Lcl       Rmt  Ld Miss    Loads       FB       L1       L2       Llc       Rmt
    # .....  ..................  .......  .......  .......  .......  .......  .......  .......  .......  ........  ........  .......  .......  .......  .......  .......  ........  ........
    #
          0            0x602180   149904   77.09%    12103     2269     9834   109504   109036      468       727      2657    13747    40400     5355    16154        0      2875       529
          1            0x602100    12128   22.20%     3951     1119     2832        0        0        0        65       200     3749    12128     5096      108        0      2056       652
          2  0xffff883ffb6a7e80      260    0.09%       15        3       12      161      161        0         1         1       15       99       25       50        0         6         1
          3  0xffffffff81aec000      157    0.07%        9        0        9        1        0        1         0         7       20      156       50       59        0        27         4
          4  0xffffffff81e3f540      179    0.06%        9        1        8      117       97       20         0        10       25       62       11        1        0        24         7

    =================================================
          Shared Cache Line Distribution Pareto
    =================================================
    #
    #        ----- HITM -----  -- Store Refs --        Data address                               ---------- cycles ----------       cpu                                     Shared
    #   Num      Rmt      Lcl   L1 Hit  L1 Miss              Offset      Pid        Code address  rmt hitm  lcl hitm      load       cnt               Symbol                Object                  Source:Line  Node{cpu list}
    # .....  .......  .......  .......  .......  ..................  .......  ..................  ........  ........  ........  ........  ...................  ....................  ...........................  ....
    #
      -------------------------------------------------------------
          0     9834     2269   109036      468            0x602180
      -------------------------------------------------------------
              65.51%   55.88%   75.20%    0.00%                 0x0    14604            0x400b4f     27161     26039     26017         9  [.] read_write_func  no_false_sharing.exe  false_sharing_example.c:144   0{0-1,4}  1{24-25,120}  2{48,54}  3{169}
           0.41%    0.35%    0.00%    0.00%                 0x0    14604            0x400b56     18088     12601     26671         9  [.] read_write_func  no_false_sharing.exe  false_sharing_example.c:145   0{0-1,4}  1{24-25,120}  2{48,54}  3{169}
           0.00%    0.00%   24.80%  100.00%                 0x0    14604            0x400b61         0         0         0         9  [.] read_write_func  no_false_sharing.exe  false_sharing_example.c:145   0{0-1,4}  1{24-25,120}  2{48,54}  3{169}
           7.50%    9.92%    0.00%    0.00%                0x20    14604            0x400ba7      2470      1729      1897         2  [.] read_write_func  no_false_sharing.exe  false_sharing_example.c:154   1{122}  2{144}
          17.61%   20.89%    0.00%    0.00%                0x28    14604            0x400bc1      2294      1575      1649         2  [.] read_write_func  no_false_sharing.exe  false_sharing_example.c:158   2{53}  3{170}
           8.97%   12.96%    0.00%    0.00%                0x30    14604            0x400bdb      2325      1897      1828         2  [.] read_write_func  no_false_sharing.exe  false_sharing_example.c:162   0{96}  3{171}

      -------------------------------------------------------------
          1     2832     1119        0        0            0x602100
      -------------------------------------------------------------
          29.13%   36.19%    0.00%    0.00%                0x20    14604            0x400bb3      1964      1230      1788         2  [.] read_write_func  no_false_sharing.exe  false_sharing_example.c:155   1{122}  2{144}
          43.68%   34.41%    0.00%    0.00%                0x28    14604            0x400bcd      2274      1566      1793         2  [.] read_write_func  no_false_sharing.exe  false_sharing_example.c:159   2{53}  3{170}
    27.19%   29.40%    0.00%    0.00%                0x30    14604            0x400be7      2045      1247      2011         2  [.] read_write_func  no_false_sharing.exe  false_sharing_example.c:163   0{96}  3{171}
    ```

### [18.4. Interpretation of perf c2c report output](#interpretation-of-perf-c2c-report-output) {#interpretation-of-perf-c2c-report-output .title}

The visualization displayed by running the `perf c2c report --stdio`{.literal} command sorts the data into several tables:

Trace Events Information
:   Provides a high level summary of all the load and store samples collected by `perf c2c record`{.literal}.

Global Shared Cache Line Event Information
:   Provides statistics over shared cache lines.

`c2c`{.literal} Details
:   Provides information about what events were sampled and how the `perf c2c report`{.literal} data is organized.

Shared Data Cache Line Table
:   Summarizes the hottest cache lines showing false sharing. Sorts by descending remote Hitm counts per cache line.

Shared Cache Line Distribution Pareto

:   Provides a variety of information about each cache line experiencing contention:

    -   The cache lines are numbered in the **NUM** column, starting at `0`{.literal}.
    -   The virtual address of each cache line is contained in the **Data address Offset** column. It is then followed by the offset into the cache line where different accesses occurred.
    -   The **Pid** column contains the process ID.
    -   The **Code Address** column contains the instruction pointer code address.
    -   The columns under the **cycles** label show average load latencies.
    -   The **cpu cnt** column displays how many different CPUs samples came from. This is the number of different CPUs waiting for the data indexed at that given location.
    -   The **Symbol** column displays the function name or symbol.
    -   The **Shared Object** column displays the ELF image name where the samples come from (\[kernel.kallsyms\] is used when the samples come from the kernel).
    -   The **Source:Line** column displays the source file and line number.
    -   The **Node{cpu list}** column displays which specific CPUs samples came from for each node.

### [18.5. Detecting false sharing with perf c2c](#detecting-false-sharing-with-perf-c2c) {#detecting-false-sharing-with-perf-c2c .title}

You can detect false sharing with the `perf c2c`{.literal} command.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").
-   A `perf.data`{.literal} file recorded by using the `perf c2c`{.literal} command is available in the current directory. For more information, see [Detecting cache-line contention with perf c2c](#detecting-cache-line-contention-with-perf-c2c "18.2. Detecting cache-line contention with perf c2c").

**Procedure**

1.  Open the `perf.data`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # perf c2c report --stdio
    ```

    This opens the `perf.data`{.literal} file in the command line.

2.  In the **Trace Event Information** table, locate the row containing the values for LLC Misses to Remote Cache (HITM):

    The percentage in the value column of the **LLC Misses to Remote Cache (HITM)** row represents the percentage of LLC misses that were occurring across NUMA nodes in modified cache-lines and is a key indicator that false sharing has occurred.

    ``` {.language-plaintext tabindex="-1"}
    =================================================
                Trace Event Information
    =================================================
      Total records                     :     329219
      Locked Load/Store Operations      :      14654
      Load Operations                   :      69679
      Loads - uncacheable               :          0
      Loads - IO                        :          0
      Loads - Miss                      :       3972
      Loads - no mapping                :          0
      Load Fill Buffer Hit              :      11958
      Load L1D hit                      :      17235
      Load L2D hit                      :         21
      Load LLC hit                      :      14219
      Load Local HITM                   :       3402
      Load Remote HITM                  :      12757
      Load Remote HIT                   :       5295
      Load Local DRAM                   :        976
      Load Remote DRAM                  :       3246
      Load MESI State Exclusive         :       4222
      Load MESI State Shared            :          0
      Load LLC Misses                   :      22274
      LLC Misses to Local DRAM          :        4.4%
      LLC Misses to Remote DRAM         :       14.6%
      LLC Misses to Remote cache (HIT)  :       23.8%
      LLC Misses to Remote cache (HITM) : 57.3%
      Store Operations                  :     259539
      Store - uncacheable               :          0
      Store - no mapping                :         11
      Store L1D Hit                     :     256696
      Store L1D Miss                    :       2832
      No Page Map Rejects               :       2376
      Unable to parse data source       :          1
    ```

3.  Inspect the **Rmt** column of the **LLC Load Hitm** field of the **Shared Data Cache Line Table**:

    ``` {.language-plaintext tabindex="-1"}
    =================================================
                 Shared Data Cache Line Table
    =================================================
      #
      #                              Total      Rmt  ----- LLC Load Hitm -----  ---- Store Reference ----  --- Load Dram ----      LLC    Total  ----- Core Load Hit -----  -- LLC Load Hit --
      # Index           Cacheline  records     Hitm    Total      Lcl      Rmt    Total    L1Hit   L1Miss       Lcl       Rmt  Ld Miss    Loads       FB       L1       L2       Llc       Rmt
      # .....  ..................  .......  .......  .......  .......  .......  .......  .......  .......  ........  ........  .......  .......  .......  .......  .......  ........  ........
      #
            0            0x602180   149904   77.09%    12103     2269     9834   109504   109036      468       727      2657    13747    40400     5355    16154        0      2875       529
            1            0x602100    12128   22.20%     3951     1119     2832        0        0        0        65       200     3749    12128     5096      108        0      2056       652
            2  0xffff883ffb6a7e80      260    0.09%       15        3       12      161      161        0         1         1       15       99       25       50        0         6         1
            3  0xffffffff81aec000      157    0.07%        9        0        9        1        0        1         0         7       20      156       50       59        0        27         4
            4  0xffffffff81e3f540      179    0.06%        9        1        8      117       97       20         0        10       25       62       11        1        0        24         7
    ```

    The table is sorted in descending order by the amount of remote **Hitm** detected per cache line. A high number in the **Rmt** column of the **LLC Load Hitm** section indicates false sharing. Further inspection of the cache line where it occurred is required to debug the false sharing activity.

## [Chapter 19. Getting started with flamegraphs](#getting-started-with-flamegraphs) {#chapter-19.-getting-started-with-flamegraphs .title}

As a system administrator, use `flamegraphs`{.literal} to visualize system performance data recorded with the `perf`{.literal} tool. As a software developer, use `flamegraphs`{.literal} to visualize application performance data recorded with the `perf`{.literal} tool.

Sampling stack traces is a common technique for profiling CPU performance with the `perf`{.literal} tool. With visualizations, you can quickly identify hot code-paths because stack trace profiling results from `perf`{.literal} can be verbose and labor-intensive to analyze.

### [19.1. Installing flamegraphs](#installing-flamegraphs) {#installing-flamegraphs .title}

You must install the required packages to start using `flamegraphs`{.literal}.

**Procedure**

-   Install the flamegraphs package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install js-d3-flame-graph
    ```

### [19.2. Creating flamegraphs over the entire system](#creating-flamegraphs-over-the-entire-system) {#creating-flamegraphs-over-the-entire-system .title}

You can visualize performance data recorded over an entire system by using `flamegraphs`{.literal}.

**Prerequisites**

-   `flamegraphs`{.literal} are installed as described in [Installing flamegraphs](#installing-flamegraphs "19.1. Installing flamegraphs").
-   The `perf`{.literal} tool is installed as described in [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Record the data and create the visualization.

    ``` {.language-plaintext tabindex="-1"}
    # perf script flamegraph -a -F 99 sleep 60
    ```

    This command samples and records performance data over the entire system for 60 seconds, as stipulated by use of the `sleep`{.literal} command, and then constructs the visualization which is stored in the current active directory as `flamegraph.html`{.literal}. The command samples call-graph data by default and takes the same arguments as the `perf`{.literal} tool, in this particular case:

    -a
    :   Stipulates to record data over the entire system.

    -F
    :   To set the sampling frequency per second.

**Verification**

-   For analysis, view the generated visualization:

    ``` {.language-plaintext tabindex="-1"}
    # xdg-open flamegraph.html
    ```

    This command opens the visualization in the default browser:

### [19.3. Creating flamegraphs over specific processes](#creating-flamegraphs-over-specific-processes) {#creating-flamegraphs-over-specific-processes .title}

You can use `flamegraphs`{.literal} to visualize performance data recorded over specific running processes.

**Prerequisites**

-   `flamegraphs`{.literal} are installed as described in [Installing flamegraphs](#installing-flamegraphs "19.1. Installing flamegraphs").
-   The `perf`{.literal} tool is installed as described in [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

-   Record the data and create the visualization.

    ``` {.language-plaintext tabindex="-1"}
    # perf script flamegraph -a -F 99 -p ID1,ID2 sleep 60
    ```

    This command samples and records performance data of the processes with the process ID's `ID1`{.literal} and `ID2`{.literal} for `60`{.literal} seconds, as stipulated by use of the `sleep`{.literal} command, and then constructs the visualization which will be stored in the current active directory as `flamegraph.html`{.literal}. The command samples call-graph data by default and takes the same arguments as the `perf`{.literal} tool, in this particular case:

    -a
    :   Stipulates to record data over the entire system.

    -F
    :   To set the sampling frequency per second.

    -p
    :   To stipulate specific process ID's to sample and record data over.

**Verification**

-   For analysis, view the generated visualization:

    ``` {.language-plaintext tabindex="-1"}
    # xdg-open flamegraph.html
    ```

    This command opens the visualization in the default browser:

### [19.4. Analyzing stack traces and function hotspots in flamegraphs](#interpreting-flamegraphs) {#analyzing-stack-traces-and-function-hotspots-in-flamegraphs .title}

Each box in the `flamegraph`{.literal} represents a different function in the stack. The `y-axis`{.literal} shows the stack depth. The top box in each stack represents the function that was on-CPU and the remaining boxes represent ancestry. The `x-axis`{.literal} displays the population of the sampled call-graph data.

In a flame graph, the `x-axis`{.literal} sorts functions by sample count, not time. Children appear in descending order of their total samples. Box width represents frequency on-CPU. Wider boxes indicate functions or ancestors captured in more samples.

**Procedure**

-   To reveal the names of functions which may have not been displayed previously and further investigate the data, click the box within the flamegraph to zoom into the stack at that given location:

-   To return to the default view of the flamegraph, click **Reset Zoom**.

    Important

    Boxes representing user-space functions may be labeled as `Unknown`{.literal} in flamegraphs because the binary of the function is stripped. Install the `debuginfo`{.literal} package or compile your local application with debugging information enabled. Use the `-g`{.literal} option in GCC, to display the function names or symbols in such a situation.

**Additional resources**

-   [Enabling debugging with debugging information](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/developing_c_and_cpp_applications_in_rhel_10/index#enabling-debugging-with-debugging-information)

## [Chapter 20. Monitoring processes for performance bottlenecks by using perf circular buffers](#monitoring-processes-for-performance-bottlenecks-by-using-perf-circular-buffers) {#chapter-20.-monitoring-processes-for-performance-bottlenecks-by-using-perf-circular-buffers .title}

You can create circular buffers that take event-specific snapshots of data with the `perf`{.literal} tool. Use them to monitor performance bottlenecks in specific processes or parts of applications running on your system.

In such cases, `perf`{.literal} only writes data to a `perf.data`{.literal} file for later analysis if a specified event is detected.

### [20.1. Circular buffers and event-specific snapshots with perf](#circular-buffers-and-event-specific-snapshots-with-perf) {#circular-buffers-and-event-specific-snapshots-with-perf .title}

Recording hours of perf data before a specific event may cause excessive overhead or prove impractical for analysis. In such cases, use `perf record`{.literal} to create custom circular buffers that take snapshots after specific events.

The `--overwrite`{.literal} option makes `perf record`{.literal} store all data in an overwritable circular buffer. When the buffer gets full, `perf record`{.literal} automatically overwrites the oldest records which, therefore, never get written to a `perf.data`{.literal} file.

Using the `--overwrite`{.literal} and `--switch-output-event`{.literal} options together configures a circular buffer. It records and dumps data continuously until it detects the `--switch-output-event`{.literal} trigger event. The trigger signals `perf record`{.literal} to write data from the circular buffer to the `perf.data`{.literal} file after an event. This collects specific data while reducing overhead by only writing relevant information to the `perf.data`{.literal} file.

### [20.2. Collecting specific data to monitor for performance bottlenecks by using perf circular buffers](#collecting-specific-data-to-monitor-for-performance-bottlenecks-using-perf-circular-buffers) {#collecting-specific-data-to-monitor-for-performance-bottlenecks-by-using-perf-circular-buffers .title}

With the `perf`{.literal} tool, you can create circular buffers. These are triggered by events you specify to only collect data you are interested in. To create circular buffers that collect event-specific data, use the `--overwrite`{.literal} and `--switch-output-event`{.literal} options for `perf`{.literal}.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

-   You have placed a `uprobe`{.literal} in the process or application you are interested in monitoring at a location of interest within the process or application:

    ``` {.language-plaintext tabindex="-1"}
    # perf probe -x </path/to/executable> -a function
    ```

    ``` {.language-plaintext tabindex="-1"}
    Added new event:
      probe_executable:function   (on function in /path/to/executable)

    You can now use it in all perf tools, such as:

        perf record -e probe_executable:function -aR sleep 1
    ```

**Procedure**

-   Create the circular buffer with the `uprobe`{.literal} as the trigger event:

    ``` {.language-plaintext tabindex="-1"}
    # perf record --overwrite -e cycles --switch-output-event probe_executable:function ./executable
    ```

    ``` {.language-plaintext tabindex="-1"}
    [ perf record: dump data: Woken up 1 times ]
    [ perf record: Dump perf.data.2021021012231959 ]
    [ perf record: dump data: Woken up 1 times ]
    [ perf record: Dump perf.data.2021021012232008 ]
    [ perf record: dump data: Woken up 1 times ]
    [ perf record: Dump perf.data.2021021012232082 ]
    [ perf record: Captured and wrote 5.621 MB perf.data.<timestamp> ]
    ```

    This command initiates the executable and collects cpu cycles, specified after the `-e`{.literal} option, until `perf`{.literal} detects the `uprobe`{.literal}, the trigger event specified after the `--switch-output-event`{.literal} option. At that point, `perf`{.literal} snapshots circular buffer data and stores it in a unique `perf.data`{.literal} file identified by timestamp. This example produced a total of 2 snapshots, the last `perf.data`{.literal} file was forced by pressing Ctrl+C.

## [Chapter 21. Managing tracepoints by using perf collector without restarting perf](#managing-tracepoints-by-using-perf-collector-without-restarting-perf) {#chapter-21.-managing-tracepoints-by-using-perf-collector-without-restarting-perf .title}

Use the control pipe interface to manage different tracepoints in a running `perf`{.literal} collector. You can dynamically adjust what data you are collecting without having to stop or restart `perf`{.literal}. This prevents performance data loss that occurs when you stop or restart recording processes.

### [21.1. Adding tracepoints to a running perf collector without stopping or restarting perf](#adding-tracepoints-to-a-running-perf-collector-without-stopping-or-restarting-perf) {#adding-tracepoints-to-a-running-perf-collector-without-stopping-or-restarting-perf .title}

You can add tracepoints to a running `perf`{.literal} collector by using the control pipe interface. `perf`{.literal} adjusts the data being recorded without having to stop `perf`{.literal}, therefore preventing the loss of performance data.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").

**Procedure**

1.  Configure the control pipe interface:

    ``` {.language-plaintext tabindex="-1"}
    # mkfifo control ack perf.pipe
    ```

2.  Run `perf record`{.literal} with the control file configuration and events you are interested in enabling:

    ``` {.language-plaintext tabindex="-1"}
    # perf record --control=fifo:control,ack -D -1 --no-buffering -e 'sched:*' -o - > perf.pipe
    ```

    In this example, declaring `'sched:*'`{.literal} after the `-e`{.literal} option starts `perf record`{.literal} with scheduler events.

3.  In a second command line, start the read side of the control pipe:

    ``` {.language-plaintext tabindex="-1"}
    # cat perf.pipe | perf --no-pager script -i -
    ```

4.  Starting the read side of the control pipe triggers the following message in the first command line:

    ``` {.language-plaintext tabindex="-1"}
    Events disabled
    ```

5.  In a third command line, enable a tracepoint by using the control file:

    ``` {.language-plaintext tabindex="-1"}
    # echo 'enable sched:sched_process_fork' > control
    ```

    This command triggers `perf`{.literal} to scan the current event list in the control file for the declared event. If the event is present, the tracepoint is enabled and the following message appears in the first command line:

    ``` {.language-plaintext tabindex="-1"}
    event sched:sched_process_fork enabled
    ```

6.  Once the tracepoint is enabled, the second command line displays the output from perf detecting the tracepoint:

    ``` {.language-plaintext tabindex="-1"}
    bash 33349 [034] 149587.674295: sched:sched_process_fork: comm=bash pid=33349 child_comm=bash child_pid=34056
    ```

### [21.2. Removing tracepoints from a running perf collector without stopping or restarting perf](#removing-tracepoints-from-a-running-perf-collector-without-stopping-or-restarting-perf) {#removing-tracepoints-from-a-running-perf-collector-without-stopping-or-restarting-perf .title}

You can remove tracepoints from a running `perf`{.literal} collector by using the control pipe interface. It helps to reduce the scope of data you are collecting without having to stop `perf`{.literal} and losing performance data.

**Prerequisites**

-   You have the `perf`{.literal} user space tool installed. For more information, see [Installing perf](#installing-perf "11.1. Installing perf").
-   You have added tracepoints to a running `perf`{.literal} collector by using the control pipe interface. For more information, see [Adding tracepoints to a running perf collector without stopping or restarting perf](#adding-tracepoints-to-a-running-perf-collector-without-stopping-or-restarting-perf "21.1. Adding tracepoints to a running perf collector without stopping or restarting perf").

**Procedure**

-   Remove the tracepoint:

    ``` {.language-plaintext tabindex="-1"}
    # echo 'disable sched:sched_process_fork' > control
    ```

    This example assumes you have previously loaded scheduler events into the control file and enabled the tracepoint `sched:sched_process_fork`{.literal}.

    This command triggers `perf`{.literal} to scan the current event list in the control file for the declared event. If found, the tracepoint is disabled and the following message appears in the command line used to configure the control pipe:

    ``` {.language-plaintext tabindex="-1"}
    # event sched:sched_process_fork disabled
    ```

## [Chapter 22. Optimizing the system performance in the web console](#optimizing-the-system-performance-using-the-web-console) {#chapter-22.-optimizing-the-system-performance-in-the-web-console .title}

You can set a performance profile in the RHEL web console to optimize the performance of the system for a selected task.

### [22.1. Performance tuning options in the web console](#performance-tuning-options-in-the-web-console) {#performance-tuning-options-in-the-web-console .title}

Red Hat Enterprise Linux provides several performance profiles that optimize the system for:

-   Systems using the desktop
-   Throughput performance
-   Latency performance
-   Network performance
-   Low-power consumption
-   Virtual machines

The TuneD service optimizes system options to match the selected profile. In the web console, you can set your system's performance profile.

**Additional resources**

-   [Optimizing system performance with TuneD](#optimizing-system-performance-with-tuned "Chapter 2. Optimizing system performance with TuneD")

### [22.2. Setting a performance profile in the web console](#setting-a-performance-profile-in-the-web-console) {#setting-a-performance-profile-in-the-web-console .title}

Depending on the task you want to perform, use the web console to optimize system performance by setting a suitable profile.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click **Overview**.

3.  In the **Configuration** section, click the current performance profile.

4.  In the **Change performance profile** dialog box, set the required profile.

5.  Click **Change profile**.

### [22.3. Monitoring performance on the local system by using the web console](#monitoring-performance-on-the-local-system-by-using-the-web-console) {#monitoring-performance-on-the-local-system-by-using-the-web-console .title}

The RHEL web console uses the Utilization Saturation and Errors (USE) Method for troubleshooting. The performance metrics page provides a chronological historical view with newest data first. In the **Metrics and history** page, you can view events, errors, and utilization and saturation graphs.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   The `cockpit-pcp`{.literal} package is installed.

-   The Performance Co-Pilot (PCP) services `pmlogger.service`{.literal} and `pmproxy.service`{.literal} are enabled and running.

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click **Overview**.

3.  In the **Usage** section, click **View metrics and history**.

    The **Metrics and history** section opens and displays: **the current system configuration and usage** the performance metrics in a graphical form over a user-specified time interval

### [22.4. Monitoring performance on several systems by using the web console and Grafana](#monitoring-performance-on-several-systems-by-using-the-web-console-and-grafana) {#monitoring-performance-on-several-systems-by-using-the-web-console-and-grafana .title}

Grafana aggregates data from multiple systems to visualize their Performance Co-Pilot (PCP) metrics graphically. You can configure performance metrics monitoring and export for several systems in the web console interface.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   You have installed the `cockpit-pcp`{.literal} package.

-   The Performance Co-Pilot (PCP) services `pmlogger.service`{.literal} and `pmproxy.service`{.literal} are enabled and running.

-   You have configured the **Grafana** dashboard. For more information, see [Configuring a grafana-server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/index#configuring-a-grafana-server).

-   You have installed the `valkey`{.literal} package.

    Alternatively, you can install the package from the web console interface later in the procedure.

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  In the **Overview** page, click **View metrics and history** in the **Usage** table.

3.  Click the **Metrics settings** button.

4.  Move the **Export to network** slider to the active position.

    If you do not have the `valkey`{.literal} package installed, the web console prompts you to install it.

5.  To open the `pmproxy`{.literal} service, select a zone from a drop-down list and click the **Add pmproxy** button.

6.  Click **Save**.

**Verification**

1.  Click **Networking**.

2.  In the **Firewall** table, click the **Edit rules and zones** button.

3.  Search for `pmproxy`{.literal} in your selected zone.

    Important

    Repeat this procedure on all systems you want to monitor for performance.

**Additional resources**

-   [Configuring a graphical representation of PCP metrics](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/index#configuring-a-graphical-representation-of-pcp-metrics)

## [Chapter 23. Analyzing system performance with BPF Compiler Collection](#analyzing-system-performance-with-bpf-compiler-collection) {#chapter-23.-analyzing-system-performance-with-bpf-compiler-collection .title}

The BPF Compiler Collection (BCC) analyzes system performance by using Berkeley Packet Filter (BPF) functions to run custom kernel programs. BCC accesses system events for performance monitoring, tracing, and debugging of BPF programs, providing tools and libraries for extracting system insights.

### [23.1. Installing the bcc-tools package](#installing-the-bcc-tools-package) {#installing-the-bcc-tools-package .title}

You can install the `bcc-tools`{.literal} package to get the BPF Compiler Collection (BCC) library and related tools.

**Procedure**

-   Install bcc-tools.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install bcc-tools
    ```

    The BCC tools are installed in the `/usr/share/bcc/tools/`{.literal} directory.

**Verification**

-   Inspect the installed tools.

    ``` {.language-plaintext tabindex="-1"}
    # ls -l /usr/share/bcc/tools/
    ```

    A list of tools installed appears. The `doc`{.literal} directory in the listing provides documentation for each tool.

### [23.2. Examining the system processes with execsnoop](#examining-the-system-processes-with-execsnoop) {#examining-the-system-processes-with-execsnoop .title}

The `execsnoop`{.literal} tool from the BCC suite captures and displays new process execution events in real time. It is useful for observing which commands or binaries are being executed on a system, helping with debugging, auditing, and security monitoring.

**Procedure**

1.  Run the `execsnoop`{.literal} program in one command line:

    ``` {.language-plaintext tabindex="-1"}
    # /usr/share/bcc/tools/execsnoop
    ```

2.  To create a short-lived process of the `ls`{.literal} command, in another command line, enter:

    ``` {.language-plaintext tabindex="-1"}
    $ ls /usr/share/bcc/tools/doc/
    ```

    The command line running `execsnoop`{.literal} shows the following output:

    ``` {.language-plaintext tabindex="-1"}
    PCOMM    PID    PPID   RET ARGS
    ls      8382   8287     0 /usr/bin/ls --color=auto /usr/share/bcc/tools/doc/
    ```

    The `execsnoop`{.literal} program prints a line of output for each new process that consumes system resources. It even detects processes of programs that run very shortly, such as `ls`{.literal}, and most monitoring tools would not register them. The `execsnoop`{.literal} output displays the following fields:

    PCOMM
    :   The parent process name. (`ls`{.literal})

    PID
    :   The process ID. (8382)

    PPID
    :   The parent process ID. (8287)

    RET
    :   The return value of the exec() system call (0), which loads program code into new processes.

    ARGS

    :   The location of the started program with arguments.

        For more information, see the `/usr/share/bcc/tools/doc/execsnoop_example.txt`{.literal} file and the `exec(3)`{.literal} man page on your system.

### [23.3. Tracking files opened by a command with opensnoop](#tracking-files-opened-by-a-command-with-opensnoop) {#tracking-files-opened-by-a-command-with-opensnoop .title}

Use the `opensnoop`{.literal} tool from BPF Compiler Collection (BCC) to monitor and log file access by a specific command in real time. This is useful for debugging, auditing, or understanding the runtime behavior of an application.

**Procedure**

1.  In one command line, run the `opensnoop`{.literal} program to print the output for files opened only by the process of the `uname`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # /usr/share/bcc/tools/opensnoop -n uname
    ```

2.  In another command line, enter the command to open certain files:

    ``` {.language-plaintext tabindex="-1"}
    $ uname
    ```

    ``` {.language-plaintext tabindex="-1"}
    The command line running opensnoop shows the output similar to the following:
    PID    COMM     FD ERR PATH
    8596   uname    3  0   /etc/ld.so.cache
    8596   uname    3  0   /lib64/libc.so.6
    8596   uname    3  0   /usr/lib/locale/locale-archive
    ...
    ```

    The `opensnoop`{.literal} program watches the `open()`{.literal} system call across the whole system, and prints a line of output for each file that `uname`{.literal} tries to open along the way. The `opensnoop`{.literal} output displays the following fields:

    PID
    :   The process ID. (8596)

    COMM
    :   The process name. (`uname`{.literal})

    FD
    :   The file descriptor - a value that open() returns to refer to the open file. (3)

    ERR
    :   Any errors.

    PATH

    :   The location of files that `open()`{.literal} tries to open.

        If a command tries to read a non-existent file, the FD column returns `-1`{.literal}. Also, the ERR column prints a value corresponding to the relevant error. Use `opensnoop`{.literal} to identify an application that does not behave properly. For more information, see the `/usr/share/bcc/tools/doc/opensnoop_example.txt`{.literal} file and `open(2)`{.literal} man page on your system.

### [23.4. Monitoring the top processes performing I/O operations on the disk with biotop](#monitoring-the-top-processes-performing-i-o-operations-on-the-disk-with-biotop) {#monitoring-the-top-processes-performing-io-operations-on-the-disk-with-biotop .title}

The `biotop`{.literal} tool provides a real-time view of processes generating the most disk I/O activity. It identifies high-disk-usage applications, serving as a tool for performance monitoring and troubleshooting.

**Procedure**

1.  Run the `biotop`{.literal} program in one command line with 30 as an argument to produce 30 second summary:

    ``` {.language-plaintext tabindex="-1"}
    # /usr/share/bcc/tools/biotop 30
    ```

    When you do not provide any argument, the output screen refreshes every 1 second by default.

2.  In another command line, enter command to read the content from the local hard disk device and write the output to the `/dev/zero`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # dd if=/dev/vda of=/dev/zero
    ```

    This step generates certain I/O traffic to illustrate `biotop`{.literal}. The command line running `biotop`{.literal} shows an output similar to the following:

    ``` {.language-plaintext tabindex="-1"}
    PID    COMM             D MAJ MIN DISK       I/O  Kbytes     AVGms
    9568   dd               R 252 0   vda      16294 14440636.0  3.69
    48     kswapd0          W 252 0   vda       1763 120696.0    1.65
    7571   gnome-shell      R 252 0   vda        834 83612.0     0.33
    1891   gnome-shell      R 252 0   vda       1379 19792.0     0.15
    7515   Xorg             R 252 0   vda        280  9940.0     0.28
    7579   llvmpipe-1       R 252 0   vda        228  6928.0     0.19
    9515   gnome-control-c  R 252 0   vda         62  6444.0     0.43
    8112   gnome-terminal-  R 252 0   vda         67  2572.0     1.54
    7807   gnome-software   R 252 0   vda         31  2336.0     0.73
    9578   awk              R 252 0   vda         17  2228.0     0.66
    7578   llvmpipe-0       R 252 0   vda        156  2204.0     0.07
    9581   pgrep            R 252 0   vda         58  1748.0     0.42
    7531   InputThread      R 252 0   vda         30  1200.0     0.48
    7504   gdbus            R 252 0   vda          3  1164.0     0.30
    1983   llvmpipe-1       R 252 0   vda         39   724.0     0.08
    1982   llvmpipe-0       R 252 0   vda         36   652.0     0.06
    ...
    ```

    The `biotop`{.literal} output displays the following fields:

    PID
    :   The process ID. (9568)

    COMM
    :   The process name. (`dd`{.literal})

    DISK
    :   The disk performs the read operations. (vda)

    I/O
    :   The number of read operations performed. (16294)

    Kbytes
    :   The amount of Kbytes reached by the read operations. (14,440,636)

    AVGms

    :   The average I/O time of read operations. (3.69)

        For more information, see the `/usr/share/bcc/tools/doc/biotop_example.txt`{.literal} file and the `dd(1)`{.literal} man page on your system.

### [23.5. Exposing unexpectedly slow file system operations with xfsslower](#exposing-unexpectedly-slow-file-system-operations-with-xfsslower) {#exposing-unexpectedly-slow-file-system-operations-with-xfsslower .title}

The `xfsslower`{.literal} measures the time spent by the XFS file system in performing read, write, open or sync `(fsync)`{.literal} operations. The argument `1`{.literal} ensures that the program shows only the operations that are slower than 1 ms.

**Procedure**

1.  Run the `xfsslower`{.literal} program in one command line:

    ``` {.language-plaintext tabindex="-1"}
    # /usr/share/bcc/tools/xfsslower 1
    ```

    When you do not provide any arguments, `xfsslower`{.literal} displays operations slower than 10 ms by default.

2.  Use `vim`{.literal} in another command line to create a text file to start interaction with the XFS file system:

    ``` {.language-plaintext tabindex="-1"}
    $ vim text
    ```

    ``` {.language-plaintext tabindex="-1"}
    The command line running xfsslower shows something similar upon saving the file from the previous step:
    TIME     COMM           PID    T BYTES   OFF_KB   LAT(ms) FILENAME
    13:07:14 b'bash'        4754   R 256     0           7.11 b'vim'
    13:07:14 b'vim'         4754   R 832     0           4.03 b'libgpm.so.2.1.0'
    13:07:14 b'vim'         4754   R 32      20          1.04 b'libgpm.so.2.1.0'
    13:07:14 b'vim'         4754   R 1982    0           2.30 b'vimrc'
    13:07:14 b'vim'         4754   R 1393    0           2.52 b'getscriptPlugin.vim'
    13:07:45 b'vim'         4754   S 0       0           6.71 b'text'
    13:07:45 b'pool'        2588   R 16      0           5.58 b'text’
    ...
    ```

    Each line represents an operation in the file system, which took more time than a certain threshold. `xfsslower`{.literal} detects possible file system problems, which can take the form of unexpectedly slow operations. The `xfsslower`{.literal} output displays the following fields:

    COMM
    :   The process name. (`b’bash'`{.literal})

    T

    :   The operation type. (`R`{.literal})

        -   **R**ead
        -   **W**rite
        -   **O**pen
        -   **S**ync

    OFF_KB
    :   The file offset in KB. (0)

    FILENAME

    :   The file that is read, written, or synced.

        For more information, see the `/usr/share/bcc/tools/doc/xfsslower_example.txt`{.literal} file and the `fsync(2)`{.literal} man page on your system.

## [Chapter 24. Configuring an operating system to optimize CPU utilization](#configuring-an-operating-system-to-optimize-cpu-utilization) {#chapter-24.-configuring-an-operating-system-to-optimize-cpu-utilization .title}

You can configure the operating system to optimize CPU utilization across their workloads.

### [24.1. Tools for monitoring and diagnosing processor issues](#tools-for-monitoring-and-diagnosing-processor-issues) {#tools-for-monitoring-and-diagnosing-processor-issues .title}

The following are the tools available in Red Hat Enterprise Linux to monitor and diagnose processor-related performance issues:

-   `numactl`{.literal} utility provides a number of options to manage processor and memory affinity. The `numactl`{.literal} package includes the `libnuma`{.literal} library, which offers a simple programming interface to the NUMA policy supported by the kernel, and can be used for more fine-grained tuning than the `numactl`{.literal} application.

-   `numad`{.literal} is an automatic NUMA affinity management daemon. It monitors NUMA topology and resource usage within a system to dynamically improve NUMA resource allocation and management.

-   `numastat`{.literal} tool displays per-NUMA node memory statistics for the operating system and its processes and shows administrators whether the process memory is spread throughout a system or is centralized on specific nodes. This tool is provided by the `numactl`{.literal} package.

-   `pqos`{.literal} utility is available in the `intel-cmt-cat`{.literal} package. It monitors CPU cache and memory bandwidth on recent Intel processors. It monitors the following types of information:

    -   The instructions per cycle (IPC)
    -   The count of last level cache MISSES
    -   The size in kilobytes that the program running in a given CPU occupies in the LLC
    -   The bandwidth to local memory (MBL)
    -   The bandwidth to remote memory (MBR)

-   `/proc/interrupts`{.literal} file displays the following types of information:

    -   Interrupt request (IRQ) number
    -   The number of similar interrupt requests handled by each processor in the system
    -   The type of interrupt sent
    -   A comma-separated list of devices that respond to the listed interrupt request

-   `taskset`{.literal} tool is provided by the `util-linux`{.literal} package. It enables administrators to retrieve and set the processor affinity of a running process, or launch a process with a specified processor affinity.

-   `turbostat`{.literal} tool prints counter results at specified intervals to help administrators identify unexpected behavior in servers, such as excessive power usage, failure to enter deep sleep states, or system management interrupts (SMIs) being created unnecessarily.

-   `x86_energy_perf_policy`{.literal} tool enables administrators to define the relative importance of performance and energy efficiency. Influence supported processors to balance performance and energy efficiency by using these specific hardware features.

### [24.2. Types of system topology](#types-of-system-topology) {#types-of-system-topology .title}

In modern computing, the idea of a single CPU is a misleading one, as most modern systems have multiple processors. The topology of the system is the way these processors are connected to each other and to other system resources.

This can affect system and application performance and the tuning considerations for a system.

The following are the two primary types of topology used in modern computing:

Symmetric Multi-Processor (SMP) topology
:   SMP topology enables all processors to access memory in the same amount of time. Serialized memory access in SMP systems creates scaling constraints that are no longer acceptable. Therefore, practically all modern server systems are NUMA machines.

Non-Uniform Memory Access (NUMA) topology

:   NUMA topology was developed more recently than SMP topology. In a NUMA system, multiple processors are physically grouped on a socket. Each socket has a dedicated area of memory, and the processors on that socket have local access to this memory. Together, the socket, its memory, and the associated processors form what is referred to as a node. Processors on the same node have high-speed access to the node's memory bank, and slower access to memory banks on other nodes.

    As a result, there is a performance penalty when accessing non-local memory. Thus, performance sensitive applications on a system with NUMA topology should access local memory. They should also avoid accessing remote memory wherever possible to ensure optimal performance.

    Multi-threaded applications that are sensitive to performance may benefit from being configured to run on a specific NUMA node rather than a specific processor. Whether this is suitable depends on your system and the requirements of your application.

    -   If multiple application threads access the same cached data, then configuring those threads to run on the same processor may be suitable.
    -   If multiple threads that access and cache different data run on the same processor, each thread may evict cached data accessed by a previous thread. This means that each thread \'misses\' the cache and wastes execution time fetching data from memory and replacing it in the cache. Use the `perf`{.literal} tool to check for an excessive number of cache misses.

### [24.3. Displaying system topologies](#displaying-system-topologies) {#displaying-system-topologies .title}

You can understand the topology of a system by using a number of commands.

**Procedure**

-   To display an overview of your system topology:

    ``` {.language-plaintext tabindex="-1"}
    $ numactl --hardware
    ```

    ``` {.language-plaintext tabindex="-1"}
    available: 4 nodes (0-3)
    node 0 cpus: 0 4 8 12 16 20 24 28 32 36
    node 0 size: 65415 MB
    node 0 free: 43971 MB
    [...]
    ```

-   To gather the information about the CPU architecture, such as the number of CPUs, threads, cores, sockets, and NUMA nodes:

    ``` {.language-plaintext tabindex="-1"}
    $ lscpu
    ```

    ``` {.language-plaintext tabindex="-1"}
    Architecture:          x86_64
    CPU op-mode(s):        32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                40
    On-line CPU(s) list:   0-39
    Thread(s) per core:    1
    Core(s) per socket:    10
    Socket(s):             4
    NUMA node(s):          4
    Vendor ID:             GenuineIntel
    CPU family:            6
    Model:                 47
    Model name:            Intel(R) Xeon(R) CPU E7- 4870  @ 2.40GHz
    Stepping:              2
    CPU MHz:               2394.204
    BogoMIPS:              4787.85
    Virtualization:        VT-x
    L1d cache:             32K
    L1i cache:             32K
    L2 cache:              256K
    L3 cache:              30720K
    NUMA node0 CPU(s):     0,4,8,12,16,20,24,28,32,36
    NUMA node1 CPU(s):     2,6,10,14,18,22,26,30,34,38
    NUMA node2 CPU(s):     1,5,9,13,17,21,25,29,33,37
    NUMA node3 CPU(s):     3,7,11,15,19,23,27,31,35,39
    ```

-   To view a graphical representation of your system:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install hwloc-gui
    ```

    ``` {.language-plaintext tabindex="-1"}
    # lstopo
    ```

-   To view the detailed textual output:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install hwloc
    ```

    ``` {.language-plaintext tabindex="-1"}
    # lstopo-no-graphics
    ```

    ``` {.language-plaintext tabindex="-1"}
    Machine (15GB)
      Package L#0 + L3 L#0 (8192KB)
        L2 L#0 (256KB) + L1d L#0 (32KB) + L1i L#0 (32KB) + Core L#0
            PU L#0 (P#0)
            PU L#1 (P#4)
           HostBridge L#0
        PCI 8086:5917
            GPU L#0 "renderD128"
            GPU L#1 "controlD64"
            GPU L#2 "card0"
        PCIBridge
            PCI 8086:24fd
              Net L#3 "wlp61s0"
        PCIBridge
            PCI 8086:f1a6
        PCI 8086:15d7
    Net L#4 "enp0s31f6"
    ```

### [24.4. Configuring kernel tick time](#configuring-kernel-tick-time) {#configuring-kernel-tick-time .title}

By default, RHEL uses a tickless kernel that does not interrupt idle CPUs, reducing power usage and enabling deep sleep states on newer processors. RHEL also provides a dynamic tickless option for latency-sensitive workloads, such as high-performance and real-time computing.

By default, the dynamic tickless option is disabled. You can use the cpu-partitioning TuneD profile to enable the dynamic tickless option for cores specified as `isolated_cores`{.literal}.

**Procedure**

1.  To enable dynamic tickless behavior in certain cores, specify those cores on the kernel command line with the `nohz_full`{.literal} parameter. For example, on a 16 core system, enable the `nohz_full=1-15`{.literal} kernel option:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=ALL --args="nohz_full=1-15"
    ```

    This enables dynamic tickless behavior on cores 1 through 15, moving all timekeeping to the only unspecified core (core 0).

2.  When the system boots, manually move the `rcu`{.literal} threads to the non-latency-sensitive core, in this case core 0:

    ``` {.language-plaintext tabindex="-1"}
    # for i in pgrep rcu[^c] ; do taskset -pc 0 $i ; done
    ```

3.  Optional: Use the `isolcpus`{.literal} parameter on the kernel command line to isolate certain cores from user-space tasks.

4.  Optional: Set the CPU affinity for the kernel's write-back `bdi-flush`{.literal} threads to the housekeeping core:

    ``` {.language-plaintext tabindex="-1"}
    echo 1 > /sys/bus/workqueue/devices/writeback/cpumask
    ```

**Verification**

-   Once the system is rebooted, verify if `dynticks`{.literal} are enabled:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -xe | grep dynticks
    ```

    ``` {.language-plaintext tabindex="-1"}
    Mar 15 18:34:54 rhel-server kernel: NO_HZ: Full dynticks CPUs: 1-15.
    ```

-   Verify that the dynamic tickless configuration is working correctly:

    ``` {.language-plaintext tabindex="-1"}
    # perf stat -C 1 -e irq_vectors:local_timer_entry taskset -c 1 sleep 3
    ```

    This command measures ticks on CPU 1 while telling CPU 1 to sleep for 3 seconds. The default kernel timer configuration shows around 3100 ticks on a regular CPU:

    ``` {.language-plaintext tabindex="-1"}
    # perf stat -C 0 -e irq_vectors:local_timer_entry taskset -c 0 sleep 3
    ```

    ``` {.language-plaintext tabindex="-1"}
     Performance counter stats for 'CPU(s) 0':

                 3,107      irq_vectors:local_timer_entry

      3.001342790 seconds time elapsed
    ```

    With the dynamic tickless kernel configured, you should see around 4 ticks instead:

    ``` {.language-plaintext tabindex="-1"}
    # perf stat -C 1 -e irq_vectors:local_timer_entry taskset -c 1 sleep 3
    ```

    ``` {.language-plaintext tabindex="-1"}
     Performance counter stats for 'CPU(s) 1':

                     4      irq_vectors:local_timer_entry

           3.001544078 seconds time elapsed
    ```

**Additional resources**

-   [All about nohz_full kernel parameter Red Hat Knowledgebase article (Red Hat Knowledgebase)](https://access.redhat.com/solutions/2273531)
-   [How to verify the list of \"isolated\" and \"nohz_full\" CPU information from sysfs? Red Hat Knowledgebase article (Red Hat Knowledgebase)](https://access.redhat.com/solutions/3875421)

### [24.5. Overview of an interrupt request](#overview-of-an-interrupt-request) {#overview-of-an-interrupt-request .title}

An interrupt request (IRQ) is a signal for immediate attention sent from a piece of hardware to a processor. Each device in a system is assigned one or more IRQ numbers, which allow it to send unique interrupts.

When enabled interrupts, processors receiving an interrupt request pause execution of the current application thread to address the interrupt request.

Because an interrupt halts normal operation, high interrupt rates can severely degrade system performance. Reduce interrupt overhead by configuring interrupt affinity or by batching lower-priority interrupts using coalescing.

Interrupt requests have an associated affinity property, `smp_affinity`{.literal}, which defines the processors that handle the interrupt request. To improve application performance and enable the specified interrupt and application threads to share cache lines, make the following improvements:

-   Assign interrupt affinity.
-   Process affinity to either the same processor or processors on the same core.

Modifying `smp_affinity`{.literal} on supported systems enables hardware-level interrupt steering. The hardware routes interrupts to specific processors without kernel intervention.

### [24.6. Balancing interrupts manually](#balancing-interrupts-manually) {#balancing-interrupts-manually .title}

If the BIOS exports Non-Uniform Memory Access (NUMA) topology, `irqbalance`{.literal} serves interrupt requests on the node local to the requesting hardware.

**Procedure**

1.  Check which devices correspond to the interrupt requests that you want to configure.

2.  Find the hardware specification for your platform. Check if the chipset on your system supports distributing interrupts.

    -   If the chipset supports distribution, you can configure interrupt delivery as described in the following steps. Additionally, check which algorithm your chipset uses to balance interrupts. Some BIOSes have options to configure interrupt delivery.
    -   If the chipset does not support distribution, your chipset always routes all interrupts to a single, static CPU. You cannot configure which CPU is used.

3.  Check which Advanced Programmable Interrupt Controller (APIC) mode is in use on your system:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl --dmesg | grep APIC
    ```

    -   If your system uses a mode other than flat, you can see a line similar to **Setting APIC routing to physical flat**.

    -   If you can see no such message, your system uses `flat`{.literal} mode.

    -   If your system uses `x2apic`{.literal} mode, you can disable it by adding the `nox2apic`{.literal} option to the kernel command line in the bootloader configuration.

        Only non-physical flat mode (flat) supports distributing interrupts to multiple CPUs. This mode is available only for systems with 8 CPUs or less.

4.  Calculate the `smp_affinity`{.literal} mask. For more information about how to calculate the `smp_affinity`{.literal} mask, see [Setting the `smp_affinity`{.literal} mask](#setting-the-smp-affinity-mask "24.7. Setting the smp_affinity mask").

### [24.7. Setting the smp_affinity mask](#setting-the-smp-affinity-mask) {#setting-the-smp_affinity-mask .title}

The `smp_affinity`{.literal} value is stored as a hexadecimal bit mask representing all processors in the system. Each bit configures a different CPU. The least significant bit is CPU 0. The default value of the mask is `f`{.literal}. It means that an interrupt request can be handled on any processor in the system.

Setting `smp_affinity`{.literal} value to `1`{.literal} means that only processor `0`{.literal} can handle the interrupt.

**Procedure**

1.  In binary, use the value `1`{.literal} for CPUs that handle the interrupts. For example, to set CPU `0`{.literal} and CPU `7`{.literal} to handle interrupts, use `0000000010000001`{.literal} as the binary code:

    |        |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
    |:-------|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
    | CPU    | 15  | 14  | 13  | 12  | 11  | 10  | 9   | 8   | 7   | 6   | 5   | 4   | 3   | 2   | 1   | 0   |
    | Binary | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 1   |

    : Table 24.1. Binary Bits for CPUs

    Show more

2.  Convert the binary code to hexadecimal:

    For example, to convert the binary code using Python:

    ``` {.language-plaintext tabindex="-1"}
    >>> hex(int('0000000010000001', 2))

    '0x81'
    ```

    On systems with more than 32 processors, you must delimit the `smp_affinity`{.literal} values for discrete 32 bit groups. For example, if you want only the first 32 processors of a 64 processor system to service an interrupt request, use `0xffffffff,00000000`{.literal}.

3.  The interrupt affinity value for a particular interrupt request is stored in the associated `/proc/irq/irq_number/smp_affinity`{.literal} file. Set the `smp_affinity`{.literal} mask in this file:

    ``` {.language-plaintext tabindex="-1"}
    # echo mask > /proc/irq/irq_number/smp_affinity
    ```

## [Chapter 25. Reviewing a system by using the tuna interface](#reviewing-a-system-by-using-the-tuna-interface) {#chapter-25.-reviewing-a-system-by-using-the-tuna-interface .title}

The `tuna`{.literal} tool reduces complexity of performing tuning tasks. You can use `tuna`{.literal} to adjust scheduler tunables parameters, tune thread priority, IRQ handlers, and isolate CPU cores and sockets. By using `tuna`{.literal}, you can perform the following operations:

-   List the CPUs on a system.
-   List the interrupt requests (IRQs), currently running on a system.
-   Change policy and priority information about threads.
-   Display the current policies and priorities of a system.

### [25.1. Installing the tuna tool](#installing-the-tuna-tool) {#installing-the-tuna-tool .title}

The `tuna`{.literal} tool is designed to be used on a running system. The application-specific measurement tools can start analyzing system performance immediately after making the changes.

**Procedure**

-   Install the `tuna`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install tuna
    ```

**Verification**

-   Display the available tuna `CLI`{.literal} options:

    ``` {.language-plaintext tabindex="-1"}
    # tuna -h
    ```

    For more information, see the `tuna(8)`{.literal} man page on your system.

### [25.2. Viewing the system status by using the tuna tool](#viewing-the-system-status-by-using-the-tuna-tool) {#viewing-the-system-status-by-using-the-tuna-tool .title}

You can use the `tuna`{.literal} command-line interface (CLI) tool to view the system status.

**Prerequisites**

-   The `tuna`{.literal} tool is installed. For details, see [Installing the tuna tool](#installing-the-tuna-tool "25.1. Installing the tuna tool").

**Procedure**

1.  View the current policies and priorities:

    ``` {.language-plaintext tabindex="-1"}
    # tuna show_threads
    ```

    ``` {.language-plaintext tabindex="-1"}
    pid   SCHED_ rtpri affinity             cmd
    1      OTHER     0      0,1            init
    2       FIFO    99        0     migration/0
    3      OTHER     0        0     ksoftirqd/0
    4       FIFO    99        0      watchdog/0
    ```

2.  Alternatively, view a specific thread corresponding to a PID or matching a command name:

    ``` {.language-plaintext tabindex="-1"}
    # tuna show_threads -t pid_or_cmd_list
    ```

    The *pid_or_cmd_list* argument is a list of comma-separated PIDs or command-name patterns.

3.  Depending on the scenario, perform one of the following actions:

    -   To tune CPUs by using the tuna CLI, complete the steps in [Tuning CPUs by using the tuna tool](#tuning-cpus-by-using-the-tuna-tool "25.3. Tuning CPUs by using the tuna tool").
    -   To tune the IRQs by using the tuna tool, complete the steps in [Tuning IRQs by using the tuna tool](#tuning-irqs-by-using-the-tuna-tool "25.4. Tuning IRQs by using the tuna tool").

4.  Save the changed configuration:

    ``` {.language-plaintext tabindex="-1"}
    # tuna save filename
    ```

    This command saves only currently running kernel threads. Processes that are not running are not saved.

### [25.3. Tuning CPUs by using the tuna tool](#tuning-cpus-by-using-the-tuna-tool) {#tuning-cpus-by-using-the-tuna-tool .title}

Use the `tuna`{.literal} tool to manage individual CPUs by changing their availability and task affinity. You can **isolate CPUs** to remove them from thread affinity masks, **include CPUs** to make them available for tasks, or **restore CPUs** to their previous configuration.

**Prerequisites**

-   The `tuna`{.literal} tool is installed. For more information, see [Installing the tuna tool](#installing-the-tuna-tool "25.1. Installing the tuna tool").

**Procedure**

1.  List all currently running processes:

    ``` {.language-plaintext tabindex="-1"}
    # ps ax | awk 'BEGIN { ORS="," }{ print $1 }'
    ```

    ``` {.language-plaintext tabindex="-1"}
    PID,1,2,3,4,5,6,8,10,11,12,13,14,15,16,17,19
    ```

2.  Display the thread list in the `tuna`{.literal} interface:

    ``` {.language-plaintext tabindex="-1"}
    # tuna show_threads -t 'thread_list from above cmd'
    ```

3.  Depending on your scenario, use this command to manage CPU affinity of processes with one of the following actions:

    ``` {.language-plaintext tabindex="-1"}
    # tuna [command] --cpus cpu_list
    ```

    -   The *cpu_list* argument is a list of comma-separated CPU numbers, for example, `--cpus 0,2`{.literal}.
    -   To add a specific CPU to the current *cpu_list*, use, for example, `--cpus +0`{.literal}.

4.  Depending on your scenario, perform one of the following actions:

    a.  To isolate a CPU, enter:

        ``` {.language-plaintext tabindex="-1"}
        # tuna isolate --cpus cpu_list
        ```

    b.  To include a CPU, enter:

        ``` {.language-plaintext tabindex="-1"}
        # tuna include --cpus cpu_list
        ```

5.  To use a system with four or more processors, make all `ssh`{.literal} threads run on CPU `0`{.literal} and `1`{.literal} and all `http`{.literal} threads on CPU `2`{.literal} and `3`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # tuna move --cpus 0,1 -t ssh*
    ```

    ``` {.language-plaintext tabindex="-1"}
    # tuna move --cpus 2,3 -t http\*
    ```

**Verification**

-   Verify the applied changes by displaying the current configuration:

    ``` {.language-plaintext tabindex="-1"}
    # tuna show_threads -t ssh*
    ```

    ``` {.language-plaintext tabindex="-1"}
    pid   SCHED_  rtpri  affinity   voluntary   nonvoluntary   cmd
    855   OTHER   0      0,1        23           15            sshd
    ```

    ``` {.language-plaintext tabindex="-1"}
    # tuna show_threads -t http\*
    ```

    ``` {.language-plaintext tabindex="-1"}
    pid   SCHED_  rtpri  affinity   voluntary   nonvoluntary   cmd
    855   OTHER   0       2,3        23           15           http
    ```

    For more information, see the `/proc/cpuinfo`{.literal} file and the `tuna(8)`{.literal} man page on your system.

### [25.4. Tuning IRQs by using the tuna tool](#tuning-irqs-by-using-the-tuna-tool) {#tuning-irqs-by-using-the-tuna-tool .title}

The `/proc/interrupts`{.literal} file records interrupt counts per IRQ including the interrupt type and the device name.

**Prerequisites**

-   The `tuna`{.literal} tool is installed. For more information, see [Installing the tuna tool](#installing-the-tuna-tool "25.1. Installing the tuna tool").

**Procedure**

1.  View the current IRQs and their affinity:

    ``` {.language-plaintext tabindex="-1"}
    # tuna show_irqs
    ```

    ``` {.language-plaintext tabindex="-1"}
    # users            affinity
    0 timer                   0
    1 i8042                   0
    7 parport0                0
    ```

2.  Specify the list of IRQs to be affected by a command:

    ``` {.language-plaintext tabindex="-1"}
    # tuna <command> --irqs irq_list --cpus cpu_list
    ```

    -   The *irq_list* argument is a list of comma-separated IRQ numbers or user-name patterns.
    -   Replace *`<command>`{.literal}* with, for example, `--spread`{.literal}.

3.  Move an interrupt to a specified CPU:

    ``` {.language-plaintext tabindex="-1"}
    # tuna show_irqs --irqs <128>
    ```

    ``` {.language-plaintext tabindex="-1"}
    users            affinity
    128 iwlwifi           0,1,2,3
    ```

    ``` {.language-plaintext tabindex="-1"}
    # tuna move --irqs 128 --cpus 3
    ```

    -   Replace *128* with the *irq_list* argument and `3`{.literal} with the *cpu_list* argument.
    -   The *cpu_list* argument is a list of comma-separated CPU numbers, for example, `--cpus 0,2`{.literal}. For more information, see [Tuning CPUs by using the tuna tool](#tuning-cpus-by-using-the-tuna-tool "25.3. Tuning CPUs by using the tuna tool").

**Verification**

-   Compare the state of the selected IRQs before and after moving any interrupt to a specified CPU:

    ``` {.language-plaintext tabindex="-1"}
    # tuna show_irqs --irqs 128
    ```

    ``` {.language-plaintext tabindex="-1"}
         users            affinity
     128 iwlwifi                 3
    ```

    For more information, see the `/proc/interrupts`{.literal} file and the `tuna(8)`{.literal} man page on your system.

## [Chapter 26. Configuring an operating system to optimize memory access](#configuring-an-operating-system-to-optimize-memory-access) {#chapter-26.-configuring-an-operating-system-to-optimize-memory-access .title}

You can configure the operating system to optimize memory access across workloads with the tools that are included in RHEL.

### [26.1. Tools for monitoring and diagnosing system memory issues](#tools-for-monitoring-and-diagnosing-system-memory-issues) {#tools-for-monitoring-and-diagnosing-system-memory-issues .title}

The following tools are available in Red Hat Enterprise Linux for monitoring system performance and diagnosing performance issues related to system memory:

-   The `vmstat`{.literal} tool, included in the `procps-ng`{.literal} package, displays reports of a system's processes, memory, paging, block I/O, traps, disks, and CPU activity. It generates an instant report displaying the average of these events from the time the machine was last turned on, or since the previous report.

-   The `valgrind`{.literal} framework provides instrumentation to user-space binaries. This framework includes several tools, which you can use to profile and analyze program performance, such as:

    -   The `memcheck`{.literal} tool is the default tool in `valgrind`{.literal}. It detects and reports several memory errors that can be difficult to detect and diagnose, such as:

        -   Invalid Memory Access

        -   Use of undefined or uninitialized values

        -   Incorrectly freed heap memory

        -   Pointer overlap (Buffer overlap)

        -   Memory leaks

            Note

            `Memcheck`{.literal} can only report these errors, it cannot prevent them from occurring. However, `memcheck`{.literal} logs an error message immediately before the error occurs.

    -   The `cachegrind`{.literal} tool simulates how an application interacts with a system's cache hierarchy and branch predictor. It gathers statistics for the duration of application's execution and displays a summary to the console.

    -   The `massif`{.literal} tool measures the heap space used by a specified application. It measures both useful space and any additional space allocated for bookkeeping and alignment purposes.

        For more information, see the `/usr/share/doc/valgrind-version/valgrind_manual.pdf`{.literal} file and `vmstat(8)`{.literal} and `valgrind(1)`{.literal} man pages on your system.

### [26.2. Overview of system memory](#overview-of-system-memory) {#overview-of-system-memory .title}

The Linux Kernel is designed to maximize the utilization of resources in system memory (RAM). Due to these design characteristics, Kernel operations use most system memory for the workload, while leaving a small portion free.

This free memory is reserved for: special system allocations and other low or high priority system services. The rest of the system memory is dedicated to the workload itself, and divided into the following two categories:

File memory

:   Pages added in this category represent parts of files in permanent storage. These pages, from the page cache, can be mapped or unmapped in address spaces of an application. Applications can map files into their address space by using the `mmap`{.literal} system calls or operate on files by using the buffered I/O read or write system calls.

    Buffered I/O system calls, as well as applications that map pages directly, can re-use unmapped pages. As a result, the kernel caches these pages to avoid repeated, slow I/O operations, particularly during periods of low memory usage.

Anonymous memory
:   These pages are used by dynamic processes or have no related files in permanent storage. These pages back up the in-memory control structures of each task, such as the application stack and heap.

### [26.3. Virtual memory parameters](#virtual-memory-parameters) {#virtual-memory-parameters .title}

The virtual memory parameters are listed in the `/proc/sys/vm`{.literal} directory.

The following are the available virtual memory parameters:

`vm.dirty_ratio`{.literal}
:   A percentage value. When this percentage of total system memory is modified, the system begins writing the modifications to the disk. The default value is 20 percent.

`vm.dirty_background_ratio`{.literal}
:   A percentage value. When this percentage of total system memory is modified, the system begins writing the modifications to the disk in the background. The default value is 10 percent.

`vm.overcommit_memory`{.literal}
:   Defines the conditions that determine whether a large memory request is accepted or denied. The default value is 0. The kernel grants memory requests based on total available RAM and swap, rejecting only large allocations. Otherwise, virtual memory allocations are granted, and can allow memory overcommitment.

Setting the `overcommit_memory`{.literal} parameter's value

:   -   When set to 1, the kernel performs no memory overcommit handling. This increases the possibility of memory overload, but improves performance for memory-intensive tasks.
    -   When set to 2, the kernel denies allocations exceeding the total swap plus the RAM percentage defined in `overcommit_ratio`{.literal}. This setting reduces the risk of overcommitting memory. Use this only for systems with the swap partition larger than physical memory.

`vm.overcommit_ratio`{.literal}
:   Specifies the percentage of physical RAM considered when `overcommit_memory`{.literal} is set to 2. The default value is 50.

`vm.max_map_count`{.literal}
:   Defines the maximum number of memory map areas that a process can use. The default value is 65530. Increase this value if your application needs more memory map areas.

`vm.min_free_kbytes`{.literal}
:   Sets the size of the reserved free pages pool. It is also responsible for setting the `min_page`{.literal}, `low_page`{.literal}, and `high_page`{.literal} thresholds. These thresholds govern the behavior of the page reclaim algorithms in the Linux kernel. It also specifies to keep the minimum number of free kilobytes across the system. This calculates a specific value for each low memory zone. Each zone is assigned a number of reserved free pages in proportion to its size.

Setting the `vm.min_free_kbytes`{.literal} parameter's value

:   -   Increasing the parameter value effectively reduces the application working set usable memory. Therefore, you can use it for only kernel-driven workloads, where driver buffers need to be allocated in atomic contexts.

    -   Decreasing the parameter value might render the kernel unable to service system requests if memory becomes heavily contended in the system.

        Warning

        Extreme values can be detrimental to the system's performance. Setting the `vm.min_free_kbytes`{.literal} to an extremely low value prevents the system from reclaiming memory effectively. This can result in system crashes and failure to service interrupts or other kernel services. However, setting `vm.min_free_kbytes`{.literal} too high considerably increases system reclaim activity, causing allocation latency due to a false direct reclaim state. This might cause the system to immediately enter an out-of-memory state. The `vm.min_free_kbytes`{.literal} parameter also sets a page reclaim watermark, called `min_pages`{.literal}. This watermark is used as a factor when determining the two other memory watermarks, `low_pages`{.literal}, and `high_pages`{.literal}, that govern page reclaim algorithms.

    -   `/proc/PID/oom_adj`{.literal} In the event, when a system runs out of memory and the `panic_on_oom`{.literal} parameter is set to 0, the `oom_killer`{.literal} function kills processes, starting with the process that has the highest `oom_score`{.literal}, until the system recovers. The `oom_adj`{.literal} parameter determines the `oom_score`{.literal} of a process. This parameter is set per process identifier. A value of **-17** disables the `oom_killer`{.literal} for that process. Other valid values range from **-16** to **15**.

        Note

        Processes created by an adjusted process inherit the `oom_score`{.literal} of that process.

`vm.swappiness`{.literal}
:   The swappiness value, ranging from 0 to 200, controls whether the system prioritizes reclaiming memory from anonymous pages or the page cache.

Setting the swappiness parameter's value

:   -   Higher values prefer file-mapped driven workloads while swapping out the less actively accessed processes' anonymous mapped memory of RAM. File servers and streaming applications use this to keep data in memory, reducing I/O latency.

    -   Low values prefer anonymous-mapped driven workloads while reclaiming the page cache (file mapped memory). This setting is useful for applications that do not depend heavily on file system information and use dynamically allocated private memory. Examples include mathematical and number-crunching applications and some hardware virtualization supervisors such as **QEMU**. The default value of the `vm.swappiness`{.literal} parameter is 60.

        Warning

        Setting the `vm.swappiness`{.literal} to 0 aggressively avoids swapping out anonymous memory to a disk. This increases the likelihood that the `oom_killer`{.literal} function kills processes during memory or I/O-intensive workloads.

### [26.4. File system parameters](#file-system-parameters) {#file-system-parameters .title}

The file system parameters are listed in the `/proc/sys/fs`{.literal} directory. The following are the available file system parameters:

`aio-max-nr`{.literal}
:   Defines the maximum number of events allowed in all active asynchronous input/output contexts. The default value is 65536, and modifying this value does not pre-allocate or resize any kernel data structures.

`file-max`{.literal}

:   Determines the maximum number of file handles for the entire system. On Red Hat Enterprise Linux 10, the default value is `9223372036854775807`{.literal}.

    Note

    The default value is set by `systemd`{.literal} and corresponds to the configurable maximum.

### [26.5. Kernel parameters](#kernel-parameters) {#kernel-parameters .title}

The default values for the kernel parameters are located in the `/proc/sys/kernel/`{.literal} directory. These are set default values provided by the kernel or values specified by a user by using sysctl. The following kernel parameters configure limits for the msg\* and shm\* System V IPC (`sysvipc`{.literal}) system calls:

`msgmax`{.literal}
:   Defines the maximum allowed size in bytes of any single message in a message queue. This value must not exceed the size of the queue (`msgmnb`{.literal}). Use the `sysctl kernel.msgmax`{.literal} command to determine the current `msgmax`{.literal} value on your system.

`msgmnb`{.literal}
:   Defines the maximum size in bytes of a single message queue. Use the `sysctl msgmnb`{.literal} command to determine the current `msgmnb`{.literal} value on your system.

`msgmni`{.literal}
:   Defines the maximum number of message queue identifiers, and therefore the maximum number of queues. Use the `sysctl kernel.msgmni`{.literal} command to determine the current `msgmni`{.literal} value on your system.

`shmall`{.literal}
:   Defines the total amount of shared memory pages that can be used on the system at one time. For example, a page is 4096 bytes on the AMD64 and Intel 64 architecture. Use the `sysctl kernel.shmall`{.literal} command to determine the current `shmall`{.literal} value on your system.

`shmmax`{.literal}
:   Defines the maximum size in bytes of a single shared memory segment allowed by the kernel. Shared memory segments up to 1Gb are now supported in the kernel. Use the `sysctl kernel.shmmax`{.literal} command to determine the current `shmmax`{.literal} value on your system.

`shmmni`{.literal}
:   Defines the system-wide maximum number of shared memory segments. The default value is 4096 on all systems.

### [26.6. Setting memory-related kernel parameters](#setting-memory-related-kernel-parameters) {#setting-memory-related-kernel-parameters .title}

Setting a parameter temporarily is useful for determining the effect the parameter has on a system. You can later set the parameter persistently when you are sure that the parameter value has the expected effect.

**Procedure**

-   To temporarily set the memory-related kernel parameters, edit the respective files in the `/proc`{.literal} file system or the `sysctl`{.literal} tool. For example, to temporarily set the `vm.overcommit_memory`{.literal} parameter to *`1`{.literal}*:

    ``` {.language-plaintext tabindex="-1"}
    # echo 1 > /proc/sys/vm/overcommit_memory
    ```

    ``` {.language-plaintext tabindex="-1"}
    # sysctl -w vm.overcommit_memory=1
    ```

-   To persistently set the memory-related kernel parameter, edit the `/etc/sysctl.conf`{.literal} file and reload the settings. For example, to persistently set the `vm.overcommit_memory`{.literal} parameter to *`1`{.literal}*:

    -   Add the following content in the `/etc/sysctl.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        vm.overcommit_memory=1
        ```

    -   Reload the sysctl settings from the `/etc/sysctl.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # sysctl -p
        ```

**Additional resources**

-   [Tuning Red Hat Enterprise Linux for IBM DB2 (Red Hat Knowledgebase)](https://access.redhat.com/solutions/3530941)

## [Chapter 27. Getting started with SystemTap](#getting-started-with-systemtap) {#chapter-27.-getting-started-with-systemtap .title}

As a system administrator, use SystemTap to identify underlying causes of a bug or performance problem on a running Red Hat Enterprise Linux (RHEL) system. As an application developer, you can use SystemTap to closely monitor and analyze your application's behavior within the RHEL environment.

### [27.1. The purpose of SystemTap](#the-purpose-of-systemtap) {#the-purpose-of-systemtap .title}

SystemTap monitors operating system and kernel activities in fine detail through tracing and probing. SystemTap provides information similar to the output of tools such as `netstat`{.literal}, `ps`{.literal}, `top`{.literal}, and `iostat`{.literal}. However, SystemTap provides more filtering and analysis options for collected information.

In SystemTap scripts, specify the information that SystemTap gathers.

SystemTap tracks kernel activity, supplementing Linux monitoring tools with two primary attributes:

Flexibility
:   Develop SystemTap scripts to monitor kernel functions, system calls, and other kernel-space events. This makes SystemTap not just a tool, but a system for developing your own kernel-specific forensic and monitoring tools.

Ease-of-Use
:   With SystemTap, you can monitor kernel activity without having to recompile the kernel or reboot the system.

### [27.2. Installing SystemTap](#installing-systemtap) {#installing-systemtap .title}

To begin using SystemTap, install the required packages. To use SystemTap with multiple kernels, install the matching kernel packages for each version.

**Prerequisites**

-   You have enabled debug repositories as described in [Enabling debug and source repositories](#enabling-debug-and-source-repositories "12.4. Enabling debug and source repositories").

**Procedure**

1.  Install the required SystemTap packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install systemtap
    ```

2.  Install the required kernel packages:

    -   Using `stap-prep`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # stap-prep
        ```

    -   If `stap-prep`{.literal} does not work, install the required kernel packages manually:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install kernel-debuginfo-$(uname -r) kernel-debuginfo-common-$(uname -m)-$(uname -r) kernel-devel-$(uname -r)
        ```

        `$(uname -m)`{.literal} is automatically replaced with the hardware platform of your system and `$(uname -r)`{.literal} is automatically replaced with the version of your running kernel.

**Verification**

-   If the kernel to be probed with SystemTap is currently in use, test if your installation was successful:

    ``` {.language-plaintext tabindex="-1"}
    # stap -v -e 'probe kernel.function("vfs_read") {printf("read performed\n"); exit()}'
    ```

    For a successful SystemTap deployment, you see an output similar to the following:

    ``` {.language-plaintext tabindex="-1"}
    Pass 1: parsed user script and 45 library script(s) in 340usr/0sys/358real ms.
    Pass 2: analyzed script: 1 probe(s), 1 function(s), 0 embed(s), 0 global(s) in 290usr/260sys/568real ms.
    Pass 3: translated to C into "/tmp/stapiArgLX/stap_e5886fa50499994e6a87aacdc43cd392_399.c" in 490usr/430sys/938real ms.
    Pass 4: compiled C into "stap_e5886fa50499994e6a87aacdc43cd392_399.ko" in 3310usr/430sys/3714real ms.
    Pass 5: starting run.
    read performed
    Pass 5: run completed in 10usr/40sys/73real ms.
    ```

    where:

-   `Pass 5: starting run`{.literal} indicates that SystemTap successfully created the instrumentation to probe the kernel and runs the instrumentation.

-   `read performed`{.literal} indicates that SystemTap detected the specified event, in this example, a VFS read.

-   `Pass 5: run completed in `{.literal}*`<time>`{.literal}*` ms`{.literal} indicates that SystemTap ran a valid handler. It displayed text and closed with no errors.

### [27.3. Privileges to run SystemTap](#privileges-to-run-systemtap) {#privileges-to-run-systemtap .title}

Running SystemTap scripts requires elevated system privileges, but in some instances non-privileged users might need to run SystemTap instrumentation on their machine.

To allow users to build and run the SystemTap scripts without root access, add users to both of these user groups:

stapdev
:   Members of this group can use `stap`{.literal} to run SystemTap scripts, or `staprun`{.literal} to run SystemTap instrumentation modules. Running `stap`{.literal} involves compiling SystemTap scripts into kernel modules and loading them into the kernel. This requires elevated privileges to the system, which are granted to `stapdev`{.literal} members. These privileges also grant effective root access to `stapdev`{.literal} members. Grant `stapdev`{.literal} group membership only to users who can be trusted with root access.

stapusr
:   Members of this group can only use `staprun`{.literal} to run SystemTap instrumentation modules. In addition, these users can run those modules only from the `/lib/modules/`{.literal}*`<kernel_version>`{.literal}*`/systemtap/`{.literal} directory. This directory must be owned and writable only by the root user.

### [27.4. Running SystemTap scripts](#running-systemtap-scripts) {#running-systemtap-scripts .title}

You can run SystemTap scripts from standard input or from a file. Find sample scripts that are distributed with the installation of SystemTap in [Sample SystemTap scripts](#sample-systemtap-scripts "27.5. Sample SystemTap scripts") or in the `/usr/share/systemtap/examples`{.literal} directory.

**Prerequisites**

-   SystemTap and the required kernel packages are installed as described in [Installing Systemtap](#installing-systemtap "27.2. Installing SystemTap").

-   To run SystemTap scripts as a normal user, add the user to the SystemTap groups:

    ``` {.language-plaintext tabindex="-1"}
    # usermod --append --groups
    stapdev,stapusr <user_name>
    ```

**Procedure**

-   Run the SystemTap script:

    -   From standard input:

        ``` {.language-plaintext tabindex="-1"}
        # stap -e "probe timer.s(1) {exit()}"
        ```

    -   From a file:

        ``` {.language-plaintext tabindex="-1"}
        # stap <file_name>.stp
        ```

### [27.5. Sample SystemTap scripts](#sample-systemtap-scripts) {#sample-systemtap-scripts .title}

You can find sample scripts that are distributed with the installation of SystemTap in the `/usr/share/systemtap/examples`{.literal} directory.

Use the `stap`{.literal} command to run different SystemTap scripts:

Tracing function calls

:   You can use the `para-callgraph.stp`{.literal} SystemTap script to trace function calls and function returns.

    ``` {.language-plaintext tabindex="-1"}
    # stap para-callgraph.stp <argument1 argument2>
    ```

    The script takes two command-line arguments:

    -   The name of the function(s) whose entry/exit you are tracing.

    -   An optional trigger function, which enables or disables tracing on a per-thread basis.

        Tracing in each thread continues as long as the trigger function has not exited.

Monitoring polling applications

:   You can use the `timeout.stp`{.literal} SystemTap script to identify and monitor which applications are polling. Knowing this, you can track unnecessary or excessive polling. It can help you to pinpoint areas for improvement in terms of CPU usage and power savings.

    ``` {.language-plaintext tabindex="-1"}
    # stap timeout.stp
    ```

    This script tracks how many times each application uses `poll`{.literal}, `select`{.literal}, `epoll`{.literal}, `itimer`{.literal}, `futex`{.literal}, `nanosleep`{.literal}, and `Signal`{.literal} system calls over time.

Tracking system call volume per process

:   You can use the `syscalls_by_proc.stp`{.literal} SystemTap script to see what processes are performing the highest volume of system calls. It displays the top 20 processes by default.

    ``` {.language-plaintext tabindex="-1"}
    # stap syscalls_by_proc.stp
    ```

Tracing functions called in network socket code

:   You can use the `socket-trace.stp`{.literal} SystemTap script to trace functions called from the kernel's `net/socket.c`{.literal} file. This helps you to identify how each process interacts with the network at the kernel level in fine detail.

    ``` {.language-plaintext tabindex="-1"}
    # stap socket-trace.stp
    ```

Tracking I/O time for each file read or write

:   Use the `iotime.stp`{.literal} SystemTap script to monitor time taken for each process to read from or write to any file. This helps you to determine what files are slow to load on a system.

    ``` {.language-plaintext tabindex="-1"}
    # stap iotime.stp
    ```

Tracking IRQ's and other processes stealing cycles from a task

:   Use the `cycle_thief.stp`{.literal} SystemTap script to track the time a task is running and the amount of time it is not running. This helps you to identify which processes are stealing cycles from a task.

    ``` {.language-plaintext tabindex="-1"}
    # stap cycle_thief.stp -x pid
    ```

    For more information, see the `/usr/share/systemtap/examples`{.literal} directory.

    Note

    You can find more examples and information about SystemTap scripts in the `/usr/share/systemtap/examples/index.html`{.literal} file. Open it in a web browser to see a list of all the available scripts and their descriptions.

### [27.6. SystemTap cross-instrumentation](#systemtap-cross-instrumentation) {#systemtap-cross-instrumentation .title}

Cross-instrumentation builds SystemTap modules on one host for use on others without the full software suite. When you run a SystemTap script, a kernel module is built out of that script. SystemTap then loads the module into the kernel.

Normally, SystemTap scripts can run only on systems where SystemTap is deployed. To run SystemTap on ten systems, SystemTap needs to be deployed on all those systems. In some cases, this might be neither feasible nor practical. For example, corporate policies may prohibit compilers or debug data, preventing a standard SystemTap deployment on all target systems.

To work around this, use cross-instrumentation. Cross-instrumentation is the process of generating SystemTap instrumentation modules from a SystemTap script on one system to be used on another system. This process offers the following benefits:

-   The kernel information packages for various machines can be installed on a single host machine. Kernel packaging bugs may prevent the installation. In such cases, the `kernel-debuginfo`{.literal} and `kernel-devel`{.literal} packages for the host system and target system must match. If a bug occurs, report the bug to Red Hat JIRA.

-   Each target machine needs only one package to be installed to use the generated SystemTap instrumentation module: `systemtap-runtime`{.literal}. Instrumentation modules require the host and target systems to share identical architectures and distributions.

    Terminology

    :   

-   *instrumentation module*

    Build the SystemTap module on the host, then load it onto the target system's kernel.

-   *host system*

    The system on which the instrumentation modules (from SystemTap scripts) are compiled, to be loaded on target systems.

-   *target system*

    The system in which the instrumentation module is being built (from SystemTap scripts).

-   *target kernel*

    The kernel of the target system. This is the kernel that loads and runs the instrumentation module.

**Additional resources**

-   [Red Hat JIRA for reporting the bug](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/providing-feedback-on-red-hat-documentation)

### [27.7. Initializing cross-instrumentation of SystemTap](#initializing-cross-instrumentation-of-systemtap) {#initializing-cross-instrumentation-of-systemtap .title}

Initialize SystemTap cross-instrumentation to build modules on one system and deploy them to systems lacking the full suite.

**Prerequisites**

-   SystemTap is installed on the host system as described in [Installing Systemtap](#installing-systemtap "27.2. Installing SystemTap").

-   The `systemtap-runtime`{.literal} package is installed on each target system:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install systemtap-runtime
    ```

-   Both the host and the target systems are the same architecture.

-   Both the host and the target systems are running the same major version of Red Hat Enterprise Linux (such as Red Hat Enterprise Linux 10).

    Important

    Kernel packaging bugs might prevent multiple `kernel-debuginfo`{.literal} and `kernel-devel`{.literal} packages from being installed on one system. In such cases, the minor version for the host and the target systems must match. If a bug occurs, report the bug at [Red Hat JIRA](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/providing-feedback-on-red-hat-documentation).

**Procedure**

1.  Determine the kernel running on each target system:

    ``` {.language-plaintext tabindex="-1"}
    $ uname -r
    ```

2.  Repeat this step for each *target* system.

3.  On the host system, install the target kernel and related packages for each target system by the method described in [Installing Systemtap](#installing-systemtap "27.2. Installing SystemTap").

4.  Build an instrumentation module on the host system, copy this module to and run this module on the target system either:

    a.  If an SSH connection can be made to the target system from the host system, use remote implementation:

        ``` {.language-plaintext tabindex="-1"}
        # stap --remote <target_system> script
        ```

        You must ensure an SSH connection can be made to the target system from the host system for this to be successful.

    b.  Manually:

        i.  Build the instrumentation module on the host system:

            ``` {.language-plaintext tabindex="-1"}
            # stap -r <kernel_version> script -m <module_name> -p 4
            ```

            Here, *`<kernel_version>`{.literal}* is the version of the target kernel determined in step 1, `script`{.literal} is the script to be converted into an instrumentation module, and *`<module_name>`{.literal}* specifies the name of the instrumentation module. The `-p4`{.literal} option tells SystemTap to not load and run the compiled module.

        ii. Once the instrumentation module is compiled, copy it to the target system and load it by using the following command:

            ``` {.language-plaintext tabindex="-1"}
            # staprun <module_name>.ko
            ```

## [Chapter 28. Tuning scheduling policy](#tuning-scheduling-policy) {#chapter-28.-tuning-scheduling-policy .title}

In Red Hat Enterprise Linux (RHEL), thread is the smallest unit of process execution. The system scheduler chooses which processor runs a thread and for how long, prioritizing overall system utilization. Consequently, thread scheduling might not optimized for specific application performance policy.

For example, if an application on a NUMA system is running on Node A when a processor on Node B becomes available. To keep the processor on Node B busy, the scheduler moves one of the application's threads to Node B. However, the application thread still requires access to memory on Node A. Accessing this memory takes longer. The thread now runs on Node B, making Node A memory remote rather than local. Running on Node B might take longer than waiting for Node A. Local memory access often outweighs the benefit of migration.

### [28.1. Categories of scheduling policies](#categories-of-scheduling-policies) {#categories-of-scheduling-policies .title}

Performance-sensitive applications often benefit when designers or administrators control where threads run. The Linux scheduler implements multiple scheduling policies that determine where and how long a thread runs.

The following are the two major scheduling policy categories:

Normal policies
:   Normal threads are used for tasks of normal priority.

Realtime policies
:   Real-time policies are used for time-sensitive tasks that must be completed without interruptions. Real-time threads are not subject to time slicing. This means the thread runs until they block, exit, voluntarily yield, or are preempted by a higher priority thread.

The lowest priority realtime thread is scheduled before any thread with a normal policy. For more information, see the `sched(7)`{.literal}, `sched_setaffinity(2)`{.literal}, `sched_getaffinity(2)`{.literal}, `sched_setscheduler(2)`{.literal}, and `sched_getscheduler(2)`{.literal} man pages on your system.

**Additional resources**

-   [Static priority scheduling with SCHED_FIFO](#static-priority-scheduling-with-sched-fifo "28.2. Static priority scheduling with SCHED_FIFO")
-   [Round robin priority scheduling with SCHED_RR](#round-robin-priority-scheduling-with-sched-rr "28.3. Round robin priority scheduling with SCHED_RR")

### [28.2. Static priority scheduling with SCHED_FIFO](#static-priority-scheduling-with-sched-fifo) {#static-priority-scheduling-with-sched_fifo .title}

The `SCHED_FIFO`{.literal}, also called static priority scheduling, is a real-time policy that defines a fixed priority for each thread. This policy enables administrators to improve event response time and reduce latency. Avoid using this policy for an extended period of time for time-sensitive tasks.

The scheduler runs the highest-priority `SCHED_FIFO`{.literal} thread from the list of ready threads. The `SCHED_FIFO`{.literal} priority levels range from integer `1`{.literal} to `99`{.literal}, where `99`{.literal} is the highest. Start with a lower number and increase priority only when you identify latency issues.

Warning

Because real-time threads are not subject to time slicing, avoid setting a priority of 99. This keeps your process at the same priority level as migration and watchdog threads. If your thread goes into a computational loop and these threads are blocked, they cannot run. Systems with a single processor will eventually hang in this situation.

Administrators can limit `SCHED_FIFO`{.literal} bandwidth to prevent realtime application programmers from initiating realtime tasks that monopolize the processor. The following are some of the parameters used in this policy:

`/proc/sys/kernel/sched_rt_period_us`{.literal}
:   This parameter defines the time period, in microseconds, that is considered to be one hundred percent of the processor bandwidth. The default value is **1000000 μs** or **1 second**.

`/proc/sys/kernel/sched_rt_runtime_us`{.literal}
:   This parameter defines the time period, in microseconds, that is devoted to running real-time threads. The default value is **950000 μs** or **0.95 seconds**.

### [28.3. Round robin priority scheduling with SCHED_RR](#round-robin-priority-scheduling-with-sched-rr) {#round-robin-priority-scheduling-with-sched_rr .title}

The `SCHED_RR`{.literal} is a round-robin variant of the `SCHED_FIFO`{.literal}. This policy is useful when multiple threads need to run at the same priority level. Like `SCHED_FIFO`{.literal}, `SCHED_RR`{.literal} is a realtime policy that defines a fixed priority for each thread.

The scheduler scans the list of all `SCHED_RR`{.literal} threads in order of priority. It then schedules the highest priority thread that is ready to run. However, unlike `SCHED_FIFO`{.literal}, threads that have the same priority are scheduled in a round-robin style within a certain time slice. You can set the value of this time slice in milliseconds with the `sched_rr_timeslice_ms`{.literal} kernel parameter in the `/proc/sys/kernel/sched_rr_timeslice_ms`{.literal} file. The lowest value is **1 millisecond**.

### [28.4. Normal scheduling with SCHED_OTHER](#normal-scheduling-with-sched-other) {#normal-scheduling-with-sched_other .title}

To enable fair processor access to all threads scheduled with this policy, `SCHED_OTHER`{.literal} uses the Completely Fair Scheduler (CFS). The `SCHED_OTHER`{.literal} is the default scheduling policy.

`SCHED_OTHER`{.literal} is useful when there are a large number of threads or data throughput is a priority. It enables more efficient scheduling of threads over time. The scheduler creates a dynamic priority list based on each thread's niceness value. Administrators can change the niceness value of a process, but cannot change the scheduler's dynamic priority list directly.

### [28.5. Setting scheduler policies](#setting-scheduler-policies) {#setting-scheduler-policies .title}

You can check and adjust scheduler policies and priorities by using the `chrt`{.literal} command line tool. It can start new processes with the expected properties or change the properties of a running process. It can also be used for setting the policy at runtime.

**Procedure**

1.  View the process ID (PID) of the active processes:

    ``` {.language-plaintext tabindex="-1"}
    # ps
    ```

2.  Use the `--pid`{.literal} or `-p`{.literal} option with the `ps`{.literal} command to view the details of the particular PID.

3.  Check the scheduling policy, PID, and priority of a particular process:

    ``` {.language-plaintext tabindex="-1"}
    # chrt -p 468
    ```

    ``` {.language-plaintext tabindex="-1"}
    pid 468's current scheduling policy: SCHED_FIFO
    pid 468's current scheduling priority: 85
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chrt -p 476
    ```

    ``` {.language-plaintext tabindex="-1"}
    pid 476's current scheduling policy: SCHED_OTHER
    pid 476's current scheduling priority: 0
    ```

4.  Set the scheduling policy of a process, for example:

    a.  To set the process with PID **1000** to `SCHED_FIFO`{.literal}, with a priority of **50**:

        ``` {.language-plaintext tabindex="-1"}
        # chrt -f -p 50 1000
        ```

    b.  To set the process with PID **1000** to `SCHED_OTHER`{.literal}, with a priority of **0**:

        ``` {.language-plaintext tabindex="-1"}
        # chrt -o -p 0 1000
        ```

    c.  To set the process with PID **1000** to `SCHED_RR`{.literal}, with a priority of **10**:

        ``` {.language-plaintext tabindex="-1"}
        # chrt -r -p 10 1000
        ```

    d.  To start a new application with a particular policy and priority, specify the name of the application:

        ``` {.language-plaintext tabindex="-1"}
        # chrt -f 36 /bin/my-app
        ```

**Additional resources**

-   [Policy Options for the chrt command](#policy-options-for-the-chrt-command "28.6. Policy options for the chrt command")
-   [Changing the priority of services during the boot process](#changing-the-priority-of-services-during-the-boot-process "28.7. Changing the priority of services during the boot process")

### [28.6. Policy options for the chrt command](#policy-options-for-the-chrt-command) {#policy-options-for-the-chrt-command .title}

You can view and set the scheduling policy of processes by using the `chrt`{.literal} command. The following table describes the appropriate policy options, which can be used to set the scheduling policy of a process.

+----------------+---------------------+------------------------------------------+
| Short option   | Long option         | Description                              |
+:===============+:====================+:=========================================+
| `-f`{.literal} | `--fifo`{.literal}  | Set schedule to `SCHED_FIFO`{.literal}   |
+----------------+---------------------+------------------------------------------+
| `-o`{.literal} | `--other`{.literal} | Set schedule to `SCHED_OTHER`{.literal}  |
+----------------+---------------------+------------------------------------------+
| `-r`{.literal} | `--rr`{.literal}    | Set schedule to `SCHED_RR`{.literal}     |
+----------------+---------------------+------------------------------------------+

: Table 28.1. Policy options for chrt command

Show more

### [28.7. Changing the priority of services during the boot process](#changing-the-priority-of-services-during-the-boot-process) {#changing-the-priority-of-services-during-the-boot-process .title}

You can configure real-time priorities for services started during boot by using the `systemd`{.literal} service. Unit configuration directives change service priority during boot.

You can change boot process priority by using different directives in the service section.

-   `CPUSchedulingPolicy=`{.literal}: Sets the CPU scheduling policy for running processes. It is used to set other, fifo, and rr policies.
-   `CPUSchedulingPriority=`{.literal}: Sets the CPU scheduling priority for running processes. The available priority range depends on the selected CPU scheduling policy. For real-time scheduling policies, an integer between 1 (lowest priority) and 99 (highest priority) can be used.

You can change the priority of a service during the boot process and by using the `mcelog`{.literal} service.

**Prerequisites**

-   You have installed and enabled `tuned`{.literal}. For more information, see [Installing and enabling TuneD](#installing-and-enabling-tuned "2.3. Installing and enabling TuneD").

**Procedure**

1.  View the scheduling priorities of running threads:

    ``` {.language-plaintext tabindex="-1"}
    # tuna --show_threads
    ```

    ``` {.language-plaintext tabindex="-1"}
        thread       ctxt_switches
        pid SCHED_ rtpri affinity voluntary nonvoluntary             cmd
      1      OTHER     0     0xff      3181          292         systemd
      2      OTHER     0     0xff       254            0        kthreadd
      3      OTHER     0     0xff         2            0          rcu_gp
      4      OTHER     0     0xff         2            0      rcu_par_gp
      6      OTHER     0        0         9            0 kworker/0:0H-kblockd
      7      OTHER     0     0xff      1301            1 kworker/u16:0-events_unbound
      8      OTHER     0     0xff         2            0    mm_percpu_wq
      9      OTHER     0        0       266            0     ksoftirqd/0
    [...]
    ```

2.  Create a supplementary `mcelog`{.literal} service configuration directory file and insert the policy name and priority in this file:

    ``` {.language-plaintext tabindex="-1"}
    # cat << EOF > /etc/systemd/system/mcelog.service.d/priority.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    [Service]
    CPUSchedulingPolicy=fifo
    CPUSchedulingPriority=20
    EOF
    ```

3.  Reload the `systemd`{.literal} scripts configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

4.  Restart the `mcelog`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart mcelog
    ```

**Verification**

-   Display the `mcelog`{.literal} priority set by `systemd`{.literal} issue:

    ``` {.language-plaintext tabindex="-1"}
    # tuna -t mcelog -P
    ```

    ``` {.language-plaintext tabindex="-1"}
    thread       ctxt_switches
    pid SCHED_ rtpri affinity voluntary nonvoluntary             cmd
    826     FIFO    20  0,1,2,3        13            0          mcelog
    ```

**Additional resources**

-   [Description of the priority range](#priority-map "28.8. Priority map")

### [28.8. Priority map](#priority-map) {#priority-map .title}

Priorities are defined in groups, with some groups dedicated to certain kernel functions. For real-time scheduling policies, an integer between `1`{.literal} (lowest priority) and `99`{.literal} (highest priority) is used.

The following table describes the priority range, which can be used when setting the scheduling policy of a process.

+----------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Priority             | Threads                     | Description                                                                                                                                                     |
+:=====================+:============================+:================================================================================================================================================================+
| 1                    | Low priority kernel threads | This priority is usually reserved for the tasks that need to be just prior to `SCHED_OTHER`{.literal}.                                                          |
+----------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2 - 49               | Available for use           | The range used for typical application priorities.                                                                                                              |
+----------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 50                   | Default hard-IRQ value      |                                                                                                                                                                 |
+----------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 51 - 98              | High priority threads       | Use this range for threads that run periodically and must have quick response times. Do not use this range for CPU-bound threads as you will starve interrupts. |
+----------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 99                   | Watchdogs and migration     | System threads that must run at the highest priority.                                                                                                           |
+----------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 28.2. Description of the priority range

Show more

### [28.9. TuneD cpu-partitioning profile](#tuned-cpu-partitioning-profile) {#tuned-cpu-partitioning-profile .title}

For tuning Red Hat Enterprise Linux for latency-sensitive workloads, use the `cpu-partitioning`{.literal} TuneD profile. In RHEL 9 and later, you can perform low-latency tuning more efficiently by using the cpu-partitioning TuneD profile.

This profile is easily customizable according to the requirements for individual low-latency applications. The following figure is an example to demonstrate how to use the cpu-partitioning profile. This example uses the CPU and node layout.

Configure the cpu-partitioning profile in the `/etc/tuned/cpu-partitioning-variables.conf`{.literal} file by using the following configuration options:

Isolated CPUs with load balancing

:   In the `cpu-partitioning`{.literal} figure, the blocks numbered from 4 to 23, are the default isolated CPUs. The kernel scheduler's process load balancing is enabled on these CPUs. It is designed for low-latency processes with multiple threads that need the kernel scheduler load balancing. Configure the cpu-partitioning profile in the `/etc/tuned/cpu-partitioning-variables.conf`{.literal} file by using the `isolated_cores=cpu-list`{.literal} option. This option lists CPUs to isolate that will use the kernel scheduler load balancing.

    The list of isolated CPUs is comma-separated or specify a range using a dash, such as 3-5. This option is mandatory. Any CPU missing from this list is automatically considered a housekeeping CPU.

Isolated CPUs without load balancing

:   In the cpu-partitioning figure, CPUs 2 and 3 are isolated and exclude kernel scheduler load balancing.

    You can configure the `cpu-partitioning`{.literal} profile in the `/etc/tuned/cpu-partitioning-variables.conf`{.literal} file by using the `no_balance_cores=cpu-list`{.literal} option, which lists CPUs to isolate that will not use the kernel scheduler load balancing.

    Specifying the `no_balance_cores`{.literal} option is optional, however any CPUs in this list must be a subset of the CPUs listed in the `isolated_cores`{.literal} list. Application threads using these CPUs need to be pinned individually to each CPU.

Housekeeping CPUs
:   Any CPU not isolated in the `cpu-partitioning-variables.conf`{.literal} file is automatically considered a housekeeping CPU. On the housekeeping CPUs, all services, daemons, user processes, movable kernel threads, interrupt handlers, and kernel timers are permitted to run.

### [28.10. Using the TuneD cpu-partitioning profile for low-latency tuning](#using-the-tuned-cpu-partitioning-profile-for-low-latency-tuning) {#using-the-tuned-cpu-partitioning-profile-for-low-latency-tuning .title}

You can tune a system for low-latency by using the TuneD's cpu-partitioning profile.

An application configured with this profile uses:

-   One dedicated reader thread that reads data from the network will be pinned to CPU 2.
-   A large number of threads that process this network data will be pinned to CPUs 4-23.
-   A dedicated writer thread that writes the processed data to the network is pinned to CPU 3.

**Prerequisites**

-   You have installed the `cpu-partitioning`{.literal} TuneD profile by using the `dnf install tuned-profiles-cpu-partitioning`{.literal} command as root.

**Procedure**

1.  Edit the `/etc/tuned/cpu-partitioning-variables.conf`{.literal} file with the following changes:

    a.  Comment the `isolated_cores=${f:calc_isolated_cores:1}`{.literal} line:

        ``` {.language-plaintext tabindex="-1"}
        # isolated_cores=${f:calc_isolated_cores:1}
        ```

    b.  Add the following information for isolated CPUS:

        ``` {.language-plaintext tabindex="-1"}
        # All isolated CPUs:
        isolated_cores=2-23
        # Isolated CPUs without the kernel’s scheduler load balancing:
        no_balance_cores=2,3
        ```

    c.  Set the cpu-partitioning TuneD profile:

        ``` {.language-plaintext tabindex="-1"}
        # tuned-adm profile cpu-partitioning
        ```

2.  Reboot the system.

    After rebooting, the system is tuned for low-latency, according to the isolation in the cpu-partitioning figure. The application can use taskset to pin the reader and writer threads to CPUs 2 and 3, and the remaining application threads on CPUs 4-23.

**Verification**

-   Verify that the isolated CPUs are not reflected in the Cpus_allowed_list field:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/self/status | grep Cpu
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cpus_allowed:    003
    Cpus_allowed_list:  0-1
    ```

-   To see affinity of all processes, enter:

    ``` {.language-plaintext tabindex="-1"}
    # ps -ae -o pid= | xargs -n 1 taskset -cp
    ```

    ``` {.language-plaintext tabindex="-1"}
    pid 1's current affinity list: 0,1
    pid 2's current affinity list: 0,1
    pid 3's current affinity list: 0,1
    pid 4's current affinity list: 0-5
    pid 5's current affinity list: 0,1
    pid 6's current affinity list: 0,1
    pid 7's current affinity list: 0,1
    pid 9's current affinity list: 0
    ...
    ```

    Note

    TuneD cannot change the affinity of some processes, mostly kernel processes. In this example, processes with PID 4 and 9 remain unchanged.

### [28.11. Customizing the cpu-partitioning TuneD profile](#customizing-the-cpu-partitioning-tuned-profile) {#customizing-the-cpu-partitioning-tuned-profile .title}

You can extend the TuneD profile to make additional tuning changes. For example, the `cpu-partitioning`{.literal} profile sets the CPUs to use `cstate=1`{.literal}. To use the `cpu-partitioning`{.literal} profile but to additionally change the CPU `cstate`{.literal} from `cstate1`{.literal} to `cstate0`{.literal}, follow this procedure.

**Procedure**

1.  Create the `/etc/tuned/profiles/my_profile`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /etc/tuned/profiles/my_profile
    ```

2.  Create a `tuned.conf`{.literal} file in this directory, and add the following content:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/tuned/profiles/my_profile/tuned.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    [main]
    summary=Customized tuning on top of cpu-partitioning
    include=cpu-partitioning
    [cpu]
    force_latency=cstate.id:0|1
    ```

3.  Use the new profile.

    ``` {.language-plaintext tabindex="-1"}
    # tuned-adm profile my_profile
    ```

    Note

    In the shared example, a reboot is not required. However, if the changes in the *my_profile* profile require a reboot to take effect, then reboot your machine.

## [Chapter 29. Profiling memory allocation with numastat](#profiling-memory-allocation-with-numastat) {#chapter-29.-profiling-memory-allocation-with-numastat .title}

The `numastat`{.literal} tool provides detailed statistics on memory allocations within a system, presenting data for each NUMA node individually. This information is valuable for analyzing system memory performance and evaluating the efficacy of various memory policies.

### [29.1. Default numastat statistics](#default-numastat-statistics) {#default-numastat-statistics .title}

By default, the `numastat`{.literal} tool displays statistics over these categories of data for each NUMA node:

`numa_hit`{.literal}
:   The number of pages that were successfully allocated to this node.

`numa_miss`{.literal}

:   The number of pages that were allocated on this node because of low memory on the intended node. Each `numa_miss`{.literal} event has a corresponding `numa_foreign`{.literal} event on another node.

    Note

    High `numa_hit`{.literal} values and low `numa_miss`{.literal} values (relative to each other) indicate optimal performance.

`numa_foreign`{.literal}
:   The number of pages initially intended for this node that were allocated to another node instead. Each `numa_foreign`{.literal} event has a corresponding `numa_miss`{.literal} event on another node.

`interleave_hit`{.literal}
:   The number of interleave policy pages successfully allocated to this node.

`local_node`{.literal}
:   The number of pages successfully allocated on this node by a process on this node.

`other_node`{.literal}
:   The number of pages allocated on this node by a process on another node.

### [29.2. Viewing memory allocation with numastat](#viewing-memory-allocation-with-numastat) {#viewing-memory-allocation-with-numastat .title}

You can view the memory allocation of the system by using the `numastat`{.literal} tool.

**Prerequisites**

-   You have installed the `numactl`{.literal} package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install numactl
    ```

**Procedure**

-   View the memory allocation of your system:

    ``` {.language-plaintext tabindex="-1"}
    $ numastat
    ```

    ``` {.language-plaintext tabindex="-1"}
                                 node0         node1
    numa_hit                  76557759      92126519
    numa_miss                 30772308      30827638
    numa_foreign              30827638      30772308
    interleave_hit              106507        103832
    local_node                76502227      92086995
    other_node                30827840      30867162
    ```

## [Legal Notice](#idm140378399692928) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
