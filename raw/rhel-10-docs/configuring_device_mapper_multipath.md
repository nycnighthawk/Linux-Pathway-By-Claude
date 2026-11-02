---
{"title": "Configuring device mapper multipath", "guide": "configuring_device_mapper_multipath", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_device_mapper_multipath/index", "retrieved": "2026-11-02", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Configuring device mapper multipath {#configuring-device-mapper-multipath .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Configuring and managing the Device Mapper Multipath feature {#configuring-and-managing-the-device-mapper-multipath-feature .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139779445705600)

**Abstract**

With Device mapper multipathing (DM Multipath), you can configure multiple I/O paths between server nodes and storage arrays into a single device. These I/O paths are physical Storage Area Network (SAN) connections that can include separate cables, switches, and controllers.

Multipathing aggregates the I/O paths and creates a new device that consists of the aggregated paths.

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

## [Chapter 1. Overview of device mapper multipathing](#overview-of-device-mapper-multipathing) {#chapter-1.-overview-of-device-mapper-multipathing .title}

Device Mapper (DM) Multipath provides redundancy through failover in active/passive configurations and improved performance by spreading I/O across multiple paths.

DM Multipath provides:

Redundancy

:   DM Multipath supports failover in an active/passive setup, where only some of the available paths handle I/O at any given time. If any active path component, such as a cable, switch, or controller fails, DM Multipath automatically redirects I/O to an alternate path. For more information, see:

    -   `multipath(8)`{.literal} and `multipathd(8)`{.literal} man pages on your system
    -   `/etc/multipath.conf`{.literal} file

Note

The number of paths is dependent on the setup. Usually, DM Multipath setups have 2, 4, or 8 paths to the storage, but other numbers are also possible.

Improved Performance
:   DM Multipath also supports an active/active configuration in which I/O is distributed across all available paths by using rotational allocation. Depending on the setup, it can monitor the load on each path and adjust the distribution dynamically to balance I/O more efficiently.

### [1.1. Active/Passive multipath configuration with one RAID device](#activepassive-multipath-configuration-with-one-raid-device) {#activepassive-multipath-configuration-with-one-raid-device .title}

Active/passive configuration provides redundant I/O paths through dual Host Bus Adapters (HBAs) and Storage Area Network (SAN) switches. These paths connect to a single Redundant Array of Independent Disks (RAID) device, enabling automatic failover.

In this configuration, there are two HBAs on the server, two SAN switches, and two RAID controllers. Following are the possible failure in this configuration:

-   HBA failure
-   Fibre Channel cable failure
-   SAN switch failure
-   Array controller port failure

With DM Multipath configured, a failure at any of these points causes DM Multipath to switch to the alternate I/O path. The following image describes the configuration with two I/O paths from the server to a RAID device. One I/O path goes through `hba1`{.literal}, `SAN1`{.literal}, and `cntrlr1`{.literal}. A second I/O path goes through `hba2`{.literal}, `SAN2`{.literal}, and `cntrlr2`{.literal}.

**Figure 1.1. Active/Passive multipath configuration with one RAID device**

### [1.2. Active/Passive multipath configuration with two RAID devices](#activepassive-multipath-configuration-with-two-raid-devices) {#activepassive-multipath-configuration-with-two-raid-devices .title}

Active/passive configuration with dual RAID devices provides redundant paths to multiple storage arrays. This ensures failover protection across separate RAID systems with dedicated controllers.

In this configuration, there are two HBAs on the server, two SAN switches, and two RAID devices with two RAID controllers each. With DM Multipath configured, a failure at any point of the I/O path causes DM Multipath to switch to the alternate I/O path. The following image describes the configuration with two I/O paths to each RAID device. Here, there are two I/O paths to each RAID device.

**Figure 1.2. Active/Passive multipath configuration with two RAID device**

### [1.3. Active/Active multipath configuration with one RAID device](#activeactive-multipath-configuration-with-one-raid-device) {#activeactive-multipath-configuration-with-one-raid-device .title}

Active/active configuration enables simultaneous I/O across multiple paths to a Redundant Array of Independent Disks (RAID) device, distributing workload for improved performance while maintaining failover capability.

In this configuration, there are two of each of the following:

-   Host Bus Adapters (HBAs) on the server
-   Storage Area Network (SAN) switches
-   RAID controllers.

The following image describes the configuration with two I/O paths from the server to a storage device. Here, I/O can be spread among these two paths.

**Figure 1.3. Active/Active multipath configuration with one RAID device**

### [1.4. DM Multipath components](#dm-multipath-components) {#dm-multipath-components .title}

Device Mapper (DM) Multipath consists of kernel modules, utilities, and daemons that work together to manage multiple I/O paths, including the multipathd daemon and multipath command tools.

The following table describes the DM Multipath components.

+:---------------------------------------+:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Component                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dm_multipath`{.literal} kernel module | Reroutes I/O and supports failover for paths and path groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mpathconf`{.literal} utility          | Configures and enables device mapper multipathing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `multipath`{.literal} command          | Lists and configures the multipath devices. It is also executed by `udev`{.literal} whenever a block device is added, to determine if the device should be part of a multipath device or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `multipathd`{.literal} daemon          | Automatically creates and removes multipath devices and monitors paths; as paths fail and come back, it may update the multipath device. Allows interactive changes to multipath devices. Reload the service if there are any changes to the `/etc/multipath.conf`{.literal} file.                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `kpartx`{.literal} command             | Creates device mapper devices for the partitions on a device. This command is automatically executed by `udev`{.literal} when multipath devices are created to create partition devices on top of them. The `kpartx`{.literal} command is provided in its own package, but the `device-mapper-multipath`{.literal} package depends on it.                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mpathpersist`{.literal}               | Sets up `SCSI-3`{.literal} persistent reservations on multipath devices. This command works similarly to the way `sg_persist`{.literal} works for SCSI devices that are not multipathed. But it handles setting persistent reservations on all paths of a multipath device. It coordinates with `multipathd`{.literal} to ensure that the reservations are configured correctly on paths that are added later. To use this functionality, the `reservation_key`{.literal} attribute must be defined in the `/etc/multipath.conf`{.literal} file. Otherwise the `multipathd`{.literal} daemon will not check for persistent reservations for newly discovered paths or reinstated paths. |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.1. Components of DM Multipath

Show more

### [1.5. Displaying multipath topology](#displaying-multipath-topology) {#displaying-multipath-topology .title}

To effectively monitor paths, troubleshoot multipath issues, or check whether the multipath configurations are set correctly, you can display the multipath topology.

**Procedure**

1.  Display the multipath device topology:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -ll
    ```

    ``` {.language-plaintext tabindex="-1"}
    mpatha (3600d0230000000000e13954ed5f89300) dm-4 WINSYS,SF2372
    size=233G features='1 queue_if_no_path' hwhandler='0' wp=rw
    `-+- policy='service-time 0' prio=1 status=active
      `- 6:0:0:0 sdf 8:80 active ready running
    ```

    The output can be split into three parts. Each part displays information for the following group:

    -   Multipath device information:

        -   `mpatha (3600d0230000000000e13954ed5f89300)`{.literal}: alias (wwid if it's different from the alias)
        -   `dm-4`{.literal}: dm device name
        -   `WINSYS,SF2372`{.literal}: vendor, product
        -   `size=233G`{.literal}: size
        -   `features='1 queue_if_no_path'`{.literal}: features
        -   `hwhandler='0'`{.literal}: hardware handler
        -   `wp=rw`{.literal}: write permissions

    -   Path group information:

        -   `policy='service-time 0'`{.literal}: scheduling policy
        -   `prio=1`{.literal}: path group priority
        -   `status=active`{.literal}: path group status

    -   Path information:

        -   `6:0:0:0`{.literal}: host:channel:id:lun

        -   `sdf`{.literal}: devnode

        -   `8:80`{.literal}: major:minor numbers

        -   `active`{.literal}: dm status

        -   `ready`{.literal}: path status

        -   `running`{.literal}: online status

            For more information about the dm, path and online status, see [Path status](#path-status "1.6. Path status").

            Other multipath commands, which are used to list, create, or reload multipath devices, also display the device topology. However, some information might be unknown and shown as `undef`{.literal} in the output. This is normal behavior. Use the `multipath -ll`{.literal} command to view the correct state.

            Note

            In certain cases, such as creating a multipath device, the multipath topology displays a parameter, which represents if any action was taken. For example, the following command output shows the `create:`{.literal} parameter to represent that a multipath device was created:

            ``` {.language-plaintext tabindex="-1"}
            create: mpatha (3600d0230000000000e13954ed5f89300) undef WINSYS,SF2372
            size=233G features='1 queue_if_no_path' hwhandler='0' wp=undef
            `-+- policy='service-time 0' prio=1 status=undef
              `- 6:0:0:0 sdf 8:80 undef ready running
            ```

### [1.6. Path status](#path-status) {#path-status .title}

Path status indicates the current state of individual storage paths, ranging from ready and functional to faulty or delayed, helping determine multipath device health and behavior.

The path status is updated periodically by the `multipathd`{.literal} daemon based on the polling interval defined in the `/etc/multipath.conf`{.literal} file. In terms of the kernel, the `dm`{.literal} status is similar to the path status. The `dm`{.literal} state will retain its current status until the path checker has completed.

Path status

:   

    ready, ghost
    :   The path is up and ready for I/O.

    faulty, shaky
    :   The path is down.

    i/o pending
    :   The checker is actively checking this path, and the state will be updated shortly.

    i/o timeout
    :   The checker did not return `success`{.literal}/`failure`{.literal} before the timeout period. This is treated the same as `faulty`{.literal}.

    removed
    :   The path has been removed from the system, and will shortly be removed from the multipath device. This is treated the same as `faulty`{.literal}.

    wild
    :   `multipathd`{.literal} was unable to run the path checker, because of an internal error or configuration issue. This is treated the same as `faulty`{.literal}, except multipath will skip many actions on the path.

    unchecked
    :   The path checker has not run on this path, either because it has just been discovered, it does not have an assigned path checker, or the path checker encountered an error. This is treated the same as `wild`{.literal}.

    delayed
    :   The path checker returns that the path is up, but multipath is delaying the reinstatement of the path because the path has recently failed multiple times and multipath has been configured to delay paths in this case. This is treated the same as `faulty`{.literal}.

Dm status

:   

    Active
    :   Maps to the `ready`{.literal} and `ghost`{.literal} path status.

    Failed
    :   Maps to all other path status, except `i/o pending`{.literal} that does not have an equivalent `dm`{.literal} state.

Online status

:   

    Running
    :   The device is enabled.

    Offline
    :   The device has been disabled.

## [Chapter 2. Multipath devices](#multipath-devices) {#chapter-2.-multipath-devices .title}

DM Multipath creates a single multipath device over multiple I/O paths to the same storage, organizing them logically. Without it, each path is seen as a separate device, even if they connect the same server to the same storage controller.

### [2.1. Multipath device identifiers](#multipath-device-identifiers) {#multipath-device-identifiers .title}

Multipath devices use specific naming conventions that determine how they appear in the file system. They can be identified by their World Wide Identifier (WWID) or user-friendly names like `mpathN`{.literal}, depending on your configuration preferences.

When new devices are under the control of Device Mapper (DM) Multipath, these devices are created in the `/dev/mapper/`{.literal} and `/dev/`{.literal} directory.

Note

Any devices of the form `/dev/dm-X`{.literal} are for internal use only and should never be used by the administrator directly.

The following describes multipath device names:

-   When the `user_friendly_names`{.literal} configuration option is set to `no`{.literal}, the name of the multipath device is set to World Wide Identifier (WWID). By default, the name of a multipath device is set to its WWID. The device name would be `/dev/mapper/WWID`{.literal}. It is also created in the `/dev/`{.literal} directory, named as `/dev/dm-X`{.literal}.
-   Alternately, you can set the `user_friendly_names`{.literal} option to `yes`{.literal} in the `/etc/multipath.conf`{.literal} file. This sets the `alias`{.literal} in the `multipath`{.literal} section to a node-unique name of the form `mpathN`{.literal}. The device name would be `/dev/mapper/mpathN`{.literal} and `/dev/dm-X`{.literal}. But the device name is not guaranteed to be the same on all nodes using the multipath device. If you set the `alias`{.literal} option in the `/etc/multipath.conf`{.literal} file, the name is not automatically consistent across all nodes in the cluster.

Note

This should not cause any difficulties if you use LVM to create logical devices from the multipath device. To keep your multipath device names consistent in every node, disable the `user_friendly_names`{.literal} option.

For example, a node has two Host Bus Adapters (HBAs). They connect through an unzoned Fibre Channel (FC) switch to a dual-port storage controller. As a result, the node sees four devices. These devices are, `/dev/sda`{.literal}, `/dev/sdb`{.literal}, `/dev/sdc`{.literal}, and `/dev/sdd`{.literal}. DM Multipath creates a single device with a unique WWID that reroutes I/O to those four underlying devices per the multipath configuration.

In addition to the `user_friendly_names`{.literal} and `alias`{.literal} options, a multipath device also has other attributes. You can modify these attributes for a specific multipath device. To do this, create an entry for that device in the `multipaths`{.literal} section of the `/etc/multipath.conf`{.literal} file.

You can modify attributes for a specific multipath device by adding an entry in the multipaths section of /etc/multipath.conf.

For more information, see:

-   `multipath(8)`{.literal} and `multipath.conf(8)`{.literal} man pages on your system
-   `/etc/multipath.conf`{.literal} file

### [2.2. Multipath devices in logical volumes](#multipath-devices-in-logical-volumes) {#multipath-devices-in-logical-volumes .title}

Multipath devices integrate seamlessly with LVM. This allows you to create physical volumes, volume groups, and logical volumes by using multipath device names instead of individual disk paths.

After creating multipath devices, you can use the multipath device names as a physical device name. You can do this when creating an Logical volume manager (LVM) physical volume. For example, if `/dev/mapper/mpatha`{.literal} is the name of a multipath device, the `pvcreate /dev/mapper/mpatha`{.literal} command marks `/dev/mapper/mpatha`{.literal} as a physical volume.

You can use the resulting LVM physical device when you create an LVM volume group like any other LVM physical device.

To filter all the `sd`{.literal} devices in the `/etc/lvm/lvm.conf`{.literal} file, add the `filter = [ "r/block/", "r/disk/", "r/sd.`{.literal}**`/", "a/.`{.literal}**`/" ]`{.literal} filter in the `devices`{.literal} section of the file. For more information see the `lvm.conf`{.literal} man page on your system.

Note

If you attempt to create an LVM physical volume on a whole device with configured partitions, the `pvcreate`{.literal} command fails. The Anaconda and Kickstart installation programs create empty partition tables if you do not specify otherwise for every block device. If you want to use the whole device instead of creating a partition, remove the existing partitions from the device. You can remove existing partitions with the `kpartx -d`{.literal} device command and the `fdisk`{.literal} utility. If your system has block devices that are greater than 2Tb, use the `parted`{.literal} utility to remove partitions.

When you create an LVM logical volume that uses `active/passive`{.literal} multipath arrays as underlying physical devices, you can include filters. Add these filters in the `/etc/lvm/lvm.conf`{.literal} file to exclude the disks that underline the multipath devices. The kernel changes the active/passive state by automatically detecting the correct hardware handler to use. For active/passive paths that require intervention to change their state, multipath automatically uses this hardware handler to do so as necessary. If the kernel does not detect the correct hardware handler, configure it in the `multipath.conf`{.literal} file with the \"hardware_handler\" option. For `active/passive`{.literal} arrays that require a command to make the passive path active, LVM prints a warning message when this occurs.

Depending on your configuration, LVM may print any of the following messages:

-   LUN not ready:

    ``` {.language-plaintext tabindex="-1"}
    end_request: I/O error, dev sdc, sector 0
    sd 0:0:0:3: Device not ready: <6>: Current: sense key: Not Ready
        Add. Sense: Logical unit not ready, manual intervention required
    ```

-   Read failed:

    ``` {.language-plaintext tabindex="-1"}
    /dev/sde: read failed after 0 of 4096 at 0: Input/output error
    ```

The following are the reasons for the mentioned errors:

-   Multipath is not configured on storage devices that are providing active/passive paths to a machine.
-   Paths are accessed directly, instead of through the multipath device.

## [Chapter 3. Configuring DM Multipath](#configuring-dm-multipath) {#chapter-3.-configuring-dm-multipath .title}

Configure DM Multipath by using the `mpathconf`{.literal} utility, which creates or edits the `/etc/multipath.conf`{.literal} configuration file to establish basic failover and additional storage options.

This utility creates or edits the `/etc/multipath.conf`{.literal} multipath configuration file based on the following scenarios:

-   If the `/etc/multipath.conf`{.literal} file already exists, the `mpathconf`{.literal} utility will edit it.
-   If the `/etc/multipath.conf`{.literal} file does not exist, the `mpathconf`{.literal} utility will create the `/etc/multipath.conf`{.literal} file from scratch.

### [3.1. Checking for the device-mapper-multipath package](#checking-for-the-device-mapper-multipath-package) {#checking-for-the-device-mapper-multipath-package .title}

Verify that the device-mapper-multipath package is installed on your system to ensure all necessary components are available before configuring multipathing. This prevents potential failures caused by missing core software.

**Procedure**

1.  Check if your system includes the `device-mapper-multipath`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # rpm -q device-mapper-multipath
    ```

    ``` {.language-plaintext tabindex="-1"}
    device-mapper-multipath-current-package-version
    ```

    If your system does not include the package, it prints the following:

    ``` {.language-plaintext tabindex="-1"}
    package device-mapper-multipath is not installed
    ```

2.  If your system does not include the package, install it by running the following command:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install device-mapper-multipath
    ```

### [3.2. Setting up basic failover configuration with DM Multipath](#setting-up-basic-failover-configuration-with-dm-multipath) {#setting-up-basic-failover-configuration-with-dm-multipath .title}

Establishing a basic failover configuration for DM Multipath provides path redundancy and enhances storage reliability. It ensures that I/O operations continue through alternate paths if one fails, preventing downtime or data loss.

**Prerequisites**

-   Administrative access.

**Procedure**

1.  Enable and initialize the multipath configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # mpathconf --enable
    ```

2.  Optional: Edit the `/etc/multipath.conf`{.literal} file.

    Most default settings are already configured, including `path_grouping_policy`{.literal} which is set to `failover`{.literal}.

3.  Optional: The default naming format of multipath devices is set to `/dev/mapper/mpathn`{.literal} format. If you prefer a different naming format:

    a.  Configure DM Multipath to use the multipath device WWID as its name, instead of the mpath_n\_ user-friendly naming scheme:

        ``` {.language-plaintext tabindex="-1"}
        # mpathconf --enable --user_friendly_names n
        ```

    b.  Reload the configuration of the DM Multipath daemon:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl reload multipathd.service
        ```

4.  Start the DM Multipath daemon:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start multipathd.service
    ```

**Verification**

-   Confirm that the DM Multipath daemon is running without issues:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status multipathd.service
    ```

-   Verify the naming format of multipath devices:

    ``` {.language-plaintext tabindex="-1"}
    # ls /dev/mapper/
    ```

### [3.3. Ignoring local disks when generating multipath devices](#ignoring-local-disks-when-generating-multipath-devices) {#ignoring-local-disks-when-generating-multipath-devices .title}

To prevent DM Multipath from using local Small Computer System Interface (SCSI) disks, you can configure it to ignore these devices during multipath device generation. Setting `find_multipaths`{.literal} to `on`{.literal} simplifies this process; otherwise, manual exclusion is required in the configuration file.

**Procedure**

1.  Identify the internal disk by using known parameters such as the device's model, path, or vendor. Determine its WWID by using the following options:

    -   Display existing multipath devices:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -v2 -l
        ```

        ``` {.language-plaintext tabindex="-1"}
        mpatha (WDC_WD800JD-75MSA3_WD-WMAM9FU71040) dm-2 ATA,WDC WD800JD-75MS
        size=33 GB features="0" hwhandler="0" wp=rw
        `-+- policy='round-robin 0' prio=0 status=active
          |- 0:0:0:0 sda 8:0 active undef running
        ```

    -   Display additional multipath devices that DM Multipath could create:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -v2 -d
        ```

        ``` {.language-plaintext tabindex="-1"}
        : mpatha (WDC_WD800JD-75MSA3_WD-WMAM9FU71040) dm-2 ATA,WDC WD800JD-75MS
        size=33 GB features="0" hwhandler="0" wp=undef
        `-+- policy='round-robin 0' prio=1 status=undef
          |- 0:0:0:0 sda 8:0  undef ready running
        ```

    -   Display device information:

        ``` {.language-plaintext tabindex="-1"}
        # multipathd show paths raw format "%d %w" | grep sda
        ```

        ``` {.language-plaintext tabindex="-1"}
        sda WDC_WD800JD-75MSA3_WD-WMAM9FU71040
        ```

        In this example, `/dev/sda`{.literal} is the internal disk and its WWID is `WDC_WD800JD-75MSA3_WD-WMAM9FU71040`{.literal}.

2.  Edit the `blacklist`{.literal} section of the `/etc/multipath.conf`{.literal} file to ignore this device by using its WWID attribute:

    ``` {.language-plaintext tabindex="-1"}
    blacklist {
          wwid WDC_WD800JD-75MSA3_WD-WMAM9FU71040
    }
    ```

    Warning

    Although you can identify the device by using its `devnode`{.literal} parameter, such as sda, this is not safe. The `/dev/sda`{.literal} identifier is not guaranteed to refer to the same device on reboot.

3.  Check for any configuration errors in the `/etc/multipath.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -t > /dev/null
    ```

    To see the full report, do not discard the command output:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -t
    ```

4.  Remake the initramfs if the disk is included in `initramfs`{.literal}. For more information, see [Configuring multipathing in initramfs](#configuring-multipathing-in-initramfs "3.5. Configuring multipathing in initramfs").

5.  Reload the `/etc/multipath.conf`{.literal} file by reconfiguring the `multipathd`{.literal} daemon:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload multipathd
    ```

    Note

    Multipath devices on top of local disks cannot be removed when in use. To ignore such device, stop all users of the device. For example, by unmounting any filesystem on top of it and deactivating any logical volumes using it. If this is not possible, you can reboot the system to remove the multipath device.

**Verification**

1.  Verify that the internal disk is ignored and it is not displayed in the multipath output:

    -   List the multipathed devices:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -v2 -l
        ```

    -   List the additional devices that DM Multipath could create:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -v2 -d
        ```

### [3.4. Configuring additional storage with DM Multipath](#configuring-additional-storage-with-dm-multipath) {#configuring-additional-storage-with-dm-multipath .title}

By default, DM Multipath includes built-in configurations for the most common storage arrays, which support DM Multipath. If your storage array does not already have a configuration, you can add one by editing the `/etc/multipath.conf`{.literal} file.

Consider adding additional storage devices during the initial configuration to align the setup with your anticipated needs. DM Multipath supports adding devices later for scalability or upgrades, but this approach may require adjusting configurations to ensure compatibility.

**Procedure**

1.  View the default configuration value and supported devices:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show config
    ```

2.  Edit the `/etc/multipath.conf`{.literal} file to configure your multipath configuration. Following is an example for the DM Multipath configuration for HP OPEN-V Storage Device:

    ``` {.language-plaintext tabindex="-1"}
    # Set default configurations for all devices managed by DM Multipath
    ```

    ``` {.language-plaintext tabindex="-1"}
    defaults {
        # Enable user-friendly names for devices
        user_friendly_names yes
    }

    devices {
        # Define configuration for HP OPEN-V storage
        device {
            vendor "HP"
            pproduct "OPEN-V"
            no_path_retry 18
        }
    }
    ```

3.  Save your changes and close the editor.

4.  Update the multipath device list by scanning for new devices:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -r
    ```

**Verification**

-   Confirm that the multipath devices are recognized correctly:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -ll
    ```

### [3.5. Configuring multipathing in initramfs](#configuring-multipathing-in-initramfs) {#configuring-multipathing-in-initramfs .title}

Setting up multipathing in the `initramfs`{.literal} ensure multipath devices are available early in the boot process. This is essential for storage setups requiring redundancy and load balancing, helping maintain system integrity and avoid issues during startup.

**Prerequisites**

-   Configured DM multipath on your system.

**Procedure**

1.  Rebuild the `initramfs`{.literal} file system with the multipath configuration files:

    ``` {.language-plaintext tabindex="-1"}
    # dracut --force --add multipath
    ```

    Note

    When using multipath in the `initramfs`{.literal} and modifying its configuration files, remember to rebuild the `initramfs`{.literal} for the changes to take effect. If your root device employs multipath, the `dracut`{.literal} command will automatically include the multipath module in the `initramfs`{.literal}.

2.  Optional: If multipath in the `initramfs`{.literal} is no longer necessary:

    a.  Remove the multipath configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # rm /etc/dracut.conf.d/multipath.conf
        ```

    b.  Rebuild the `initramfs`{.literal} with the added multipath configuration:

        ``` {.language-plaintext tabindex="-1"}
        # dracut --force --omit multipath
        ```

**Verification**

-   Check if multipath-related files and configurations are present:

    ``` {.language-plaintext tabindex="-1"}
    # lsinitrd /path/to/initramfs.img -m | grep multipath
    ```

Note

While verification steps provided can give you an indication of success, you must perform a final test boot-up to ensure that the configuration works as expected.

-   After the reboot, confirm that the multipath devices are recognized correctly:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -ll
    ```

## [Chapter 4. Modifying the DM Multipath configuration file](#modifying-the-dm-multipath-configuration-file) {#chapter-4.-modifying-the-dm-multipath-configuration-file .title}

Override DM Multipath default configuration values by editing the `/etc/multipath.conf`{.literal} file to customize multipathing behavior and add support for unsupported storage arrays.

In the multipath configuration file, you need to specify only the sections that you need for your configuration, or that you need to change from the default values. If there are sections of the file that are not relevant to your environment or for which you do not need to override the default values, you can leave them commented out, as they are in the initial file.

In the configuration file, you can also use the regular expression.

Note

If you run multipath from the `initramfs`{.literal} file system and you make any changes to the multipath configuration files, you must rebuild the `initramfs`{.literal} file system for the changes to take effect.

### [4.1. Configuration file overview](#configuration-file-overview) {#configuration-file-overview .title}

The multipath configuration file contains distinct sections for blacklists, defaults, devices, multipaths, and overrides, evaluated in priority order to determine device behavior.

The multipath configuration file is divided into the following sections:

blacklist
:   Listing of specific devices that will not be considered for multipath.

blacklist_exceptions
:   Listing of multipath devices that would otherwise be ignored according to the parameters of the `blacklist`{.literal} section.

defaults
:   General default settings for Device Mapper (DM) Multipath.

multipaths
:   Settings for the characteristics of individual multipath devices. These values replace settings specified in the `overrides`{.literal}, `devices`{.literal}, and `defaults`{.literal} sections of the configuration file.

devices
:   Settings for the individual storage controllers. These values overwrite what is specified in the `defaults`{.literal} section of the configuration file. If you are using a storage array that is not supported by default, you may need to create a `devices`{.literal} subsection for your array.

overrides
:   Settings that are applied to all devices. These values overwrite what is specified in the `devices`{.literal} and `defaults`{.literal} sections of the configuration file.

When the system determines the attributes of a multipath device, it checks the settings of the separate sections from the `multipath.conf`{.literal} file in the following order:

1.  `multipaths`{.literal} section
2.  `overrides`{.literal} section
3.  `devices`{.literal} section
4.  `defaults`{.literal} section

The following are the ways to view the default configurations:

-   If you install your machine on a multipath device, the default multipath configuration applies automatically. The default configuration includes the following:

    -   For a complete list of the default configuration values, run either `multipath -t`{.literal} or `multipathd show config`{.literal} command.
    -   For a list of configuration options with descriptions, see the `multipath.conf`{.literal} man page on your system.

-   If you did not configure multipathing during installation, run the `mpathconf --enable`{.literal} command to get the default configuration.

### [4.2. Configuration file defaults](#configuration-file-defaults) {#configuration-file-defaults .title}

The `defaults`{.literal} section establishes global configuration parameters for DM Multipath behavior, including polling intervals, path grouping policies, and failover settings applied to all multipath devices.

The `/etc/multipath.conf`{.literal} configuration file contains a `defaults`{.literal} section. This section includes the default configuration of Device Mapper (DM) Multipath. The default values might differ based on your initial device settings.

The following table describes the optional attributes, set in the `defaults`{.literal} section of the `multipath.conf`{.literal} configuration file. If you do not set them, default values from the `overrides`{.literal}, or `devices`{.literal} sections apply.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+:======================================================================================================================================================================================+:==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `polling_interval`{.literal}                                                                                                                                                          | Specifies the interval between two path checks in seconds. For properly functioning paths, the interval between checks gradually increases to `max_polling_interval`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `5`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `max_polling_interval`{.literal}                                                                                                                                                      | Specifies the maximum length of the interval between two path checks in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `4 * polling_interval`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `find_multipaths`{.literal}                                                                                                                                                           | Defines the mode for setting up multipath devices. Available values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `off`{.literal}: If `find_multipaths`{.literal} is set to `off`{.literal}, `multipath`{.literal} applies rules as with the `strict`{.literal} value and the `multipathd`{.literal} daemon applies rules as with the `greedy`{.literal} value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `on`{.literal}: If there are at least two devices that are not on the `blacklist`{.literal} with the same World Wide Identifier (WWID), or if multipath created a multipath device with a device WWID before (even if that multipath device is no longer present), then the device is treated as a multipath device path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `greedy`{.literal}: Both `multipathd`{.literal} and `multipath`{.literal} treat every non-blacklisted device as a multipath device path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `smart`{.literal}: Multipath automatically considers that every non-blacklisted device is a multipath device path. If a second path, with the same WWID does not appear within the time set for `find_multipaths_timeout`{.literal}, multipath releases the device and enables it for use by the rest of the system. The `multipathd`{.literal} daemon applies rules as with the `on`{.literal} value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `strict`{.literal}: This value only treats a device as a multipath path, if you create a multipath device with the device WWID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `off`{.literal}. The default `multipath.conf`{.literal} file sets `find_multipaths`{.literal} to `on`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `find_multipaths_timeout`{.literal}                                                                                                                                                   | This represents the timeout in seconds, to wait for additional paths after detecting the first one, if `find_multipaths`{.literal} `smart`{.literal} is set. Possible values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | **Positive value**: If set with a positive value, the timeout applies for all non-blacklisted devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | **Negative value**: If set with a negative value, the timeout applies only to known devices that have an entry in the multipath hardware table, either in the built-in table, or in a `device`{.literal} section. Other unknown devices use a timeout of only 1 second to avoid booting delays.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `0`{.literal}: The system applies the built-in default for this attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value for known hardware is `-10`{.literal}. This means that known devices have a 10 second timeout. Unknown devices have a 1 second timeout. If the `find_multipaths`{.literal} attribute has a value other than `smart`{.literal}, this attribute has no effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `uxsock_timeout`{.literal}                                                                                                                                                            | Set the timeout of `multipathd`{.literal} interactive commands in milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | For systems with a large number of devices, `multipathd`{.literal} interactive commands might timeout and fail. If this happens, increase this timeout to resolve the issue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `4000`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reassign_maps`{.literal}                                                                                                                                                             | Enable reassigning of device-mapper maps. With this option, the `multipathd`{.literal} daemon remaps existing device-mapper maps to always point to the multipath device, not the underlying block devices. Possible values are `yes`{.literal} and `no`{.literal}. The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `verbosity`{.literal}                                                                                                                                                                 | The default verbosity value is `2`{.literal}. Higher values increase the verbosity level. Valid levels are between `0`{.literal} and `4`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `path_selector`{.literal}                                                                                                                                                             | Specifies the default algorithm to use in determining what path to use for the next I/O operation. Possible values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `round-robin 0`{.literal}: Loop through every path in the path group, sending the same number of I/O requests, determined by `rr_min_io`{.literal} or `rr_min_io_rq`{.literal}, to each.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `queue-length 0`{.literal}: Send the next group of I/O requests down the path with the least number of outstanding I/O requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `service-time 0`{.literal}: Send the next group of I/O requests down the path with the shortest estimated service time. This is determined by dividing the total size of the outstanding I/O to each path by the relative throughput.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `service-time 0`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `path_grouping_policy`{.literal}                                                                                                                                                      | Specifies the default path grouping policy to apply to unspecified multipaths. Possible values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `failover`{.literal}: 1 path per priority group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `multibus`{.literal}: All valid paths in 1 priority group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `group_by_serial`{.literal}: 1 priority group per detected serial number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `group_by_prio`{.literal}: 1 priority group per path priority value. Priorities are determined by the `prio`{.literal} attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `group_by_node_name`{.literal}: 1 priority group per target node name. The `/sys/class/fc_transport/target*/node_name`{.literal} directory includes target node names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `group_by_tpg`{.literal}: 1 priority group per target port group. All paths in the multipath device must have their priority function set to `alua`{.literal} or `sysfs`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `failover`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `uid_attrs`{.literal}                                                                                                                                                                 | Set this option to activate merging `uevents`{.literal} by WWID. This action might improve uevent processing efficiency. It is also an alternative method to configure the udev properties to use for determining unique path identifiers (WWIDs).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The value of this option is a space separated list of records like `type:ATTR`{.literal}, where `type`{.literal} is matched against the beginning of the device node name, and `ATTR`{.literal} is the name of the udev property to use for matching devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | If you configure this option and it matches the device node name of a device, it overrides any other configured methods for determining the WWID for this device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | You can enable `uevent`{.literal} merging by setting this value to `sd:ID_SERIAL dasd:ID_UID nvme:ID_WWN`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default is `unset`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `prio`{.literal}                                                                                                                                                                      | Specifies the default function to call to obtain a path priority value. For example, the Asymmetric Logical Unit Access (ALUA) bits in SPC-3 provide an exploitable `prio`{.literal} value. Possible values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `const`{.literal}: Set a priority of 1 to all paths.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `emc`{.literal}: Generate the path priority for EMC arrays.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `sysfs`{.literal}: Generate the path priority from `sysfs`{.literal}. This prioritizer accepts the optional `prio_arg`{.literal} value `exclusive_pref_bit`{.literal}. The `sysfs`{.literal} value uses the `sysfs`{.literal} attributes `access_state`{.literal} and `preferred_path`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `alua`{.literal}: Generate the path priority based on the Small Computer System Interface-3 (SCSI-3) ALUA settings. If you specify `prio alua`{.literal} and `prio_args`{.literal} `exclusive_pref_bit`{.literal} in your device configuration, multipath creates a path group that contains only the path with the `exclusive_pref_bit`{.literal} set, and assigns that path group the highest priority. Refer to the `multipath.conf(5)`{.literal} man page for more information about this type of cases.                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `ontap`{.literal}: Generate the path priority for NetApp arrays.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `rdac`{.literal}: Generate the path priority for LSI/Engenio RDAC controller.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `hp_sw`{.literal}: Generate the path priority for Compaq/HP controller in active/standby mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `hds`{.literal}: Generate the path priority for Hitachi HDS Modular storage arrays.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `random`{.literal}: Generate a random priority between 1 and 10.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `weightedpath`{.literal}: Generate the path priority based on the regular expression and the provided priority as an argument. Requires a `prio_args`{.literal} keyword.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `path_latency`{.literal}: Generate the path priority based on a latency algorithm. Requires a `prio_args`{.literal} keyword.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `ana`{.literal}: Generate the path priority based on the Non-Volatile Memory Express (NVMe) Asymmetric Namespace Access (ANA) settings. This priority routine is hardware dependent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `datacore`{.literal}: Generate the path priority for some DataCore storage arrays. Requires a `prio_args`{.literal} keyword. This priority routine is hardware dependent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `iet`{.literal}: Generate path priority for iSCSI targets based on IP their address. Requires a `prio_args`{.literal} keyword. This priority routine is available only with iSCSI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value depends on the `detect_prio`{.literal} setting. If `detect_prio`{.literal} is set to `yes`{.literal}, then the default priority algorithm is `sysfs`{.literal}. The only exception is for NetAPP E-Series, where the default is `alua`{.literal}. If `detect_prio`{.literal} is set to `no`{.literal}, the default priority algorithm is `const`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `prio_args`{.literal}                                                                                                                                                                 | Arguments to pass to the `prio`{.literal} function. This applies only to the following prioritizers:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `weighted`{.literal}: Needs a value of the form `<hbtl,devname,serial,wwn> <regex1> <prio1> <regex2> <prio2>`{.literal}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `hbtl`{.literal}: The Regex value can be of SCSI H:B:T:L format. For example: `1:0:.:. , *:0:0:`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `devname`{.literal}: The Regex value can be in device name format. For example: `sda`{.literal}, `sd.e`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `serial`{.literal}: The Regex value can be in serial number format. Look up `serial`{.literal} through `sysfs`{.literal}, or by running the command `multipathd show paths format "%z"`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `wwn`{.literal}: The Regex value can be in the form `host_wwnn:host_wwpn:target_wwnn:target_wwpn`{.literal}. These values can be looked up through `sysfs`{.literal} or by running the command `multipathd show paths format %N:%R:%n:%r"`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `path_latency`{.literal}: Requires a value in the form `io_num= <integer> base_num=<integer>`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `io_num`{.literal}: The number of read IOs, continuously sent to the current path. This value helps calculate the average path latency. Valid values include `Integer`{.literal}, `[2, 200]`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `base_num`{.literal}: The base number value of logarithmic scale. This value helps to partition different priority ranks. Valid values include `Integer`{.literal}, `[2, 10]`{.literal}. The maximum average latency value is `100s`{.literal} and the minimum average latency value is `1us`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `alua`{.literal}: If the `exclusive_pref_bit`{.literal} value is set, paths with the `preferred_path_bit`{.literal} set always create their own path group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `sysfs`{.literal}: If the `exclusive_pref_bit`{.literal} value is set, paths with the `preferred_path_bit`{.literal} set always create their own path group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `datacore`{.literal}: Requires a value of the form `timeout=<milliseconds> preferredsds=<name>`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `preferredsds`{.literal}: This value is mandatory and it represents the preferred SDS name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `timeout`{.literal}: This value is optional. Set the timeout for the inquiry in milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `iet`{.literal}: Requires a value of the form `preferredip=<ip_address>`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `preferredip`{.literal}: This value is mandatory. This is the preferred IP address, in dotted decimal notation, for iSCSI targets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `unset`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `features`{.literal}                                                                                                                                                                  | The default extra features of multipath devices, using the format: *\"number_of_features_plus_arguments feature1 ...​\"*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | Possible values for `features`{.literal} include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `queue_if_no_path`{.literal}: The same as setting `no_path_retry`{.literal} to `queue`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `pg_init_retries `{.literal}*`n`{.literal}*: Retry path group initialization up to *n* times before failing. The number must be between 1 and 50.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `pg_init_delay_msecs `{.literal}*`msecs`{.literal}*: Number of milliseconds before `pg_init`{.literal} retry initiates. The number must be between 0 and 60000.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `queue_mode `{.literal}*`mode`{.literal}*: Select the queueing mode per multipath device. The *mode* value options are `bio`{.literal}, `rq`{.literal} or `mq`{.literal}. These correspond to bio-based, request-based, and block-multiqueue request-based (`blk-mq`{.literal}), respectively.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | By default, the value is *unset*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `path_checker`{.literal}                                                                                                                                                              | Specifies the default method to determine the state of the paths. Possible values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `readsector0`{.literal}: Read the first sector of the device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `tur`{.literal}: Issue a `TEST UNIT READY`{.literal} command to the device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `emc_clariion`{.literal}: Query the EMC Clariion specific EVPD page 0xC0 to determine the path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `hp_sw`{.literal}: Check the path state for HP storage arrays with Active/Standby firmware.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `rdac`{.literal}: Check the path state for LSI/Engenio RDAC storage controller.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `directio`{.literal}: Read the first sector with direct I/O.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `cciss_tur`{.literal}: Check the path state for HP/COMPAQ Smart Array(CCISS) controllers. This is hardware dependent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `none`{.literal}: Does not check the device. Falls back to use values retrieved from `sysfs`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `tur`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `alias_prefix`{.literal}                                                                                                                                                              | This attribute represents the `user_friendly_names`{.literal} prefix.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `mpath`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `failback`{.literal}                                                                                                                                                                  | Manages path group failback. Possible values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `immediate`{.literal}: Specifies immediate failback to the highest priority path group that contains active paths.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `manual`{.literal}: Specifies that there is no immediate failback, but that failback can happen only with operator intervention.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `followover`{.literal}: Specifies that automatic failback can only be performed when the first path of a path group becomes active. This keeps a node from automatically failing back, when another node requested the failover.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | A numeric value greater than zero, specifies deferred failback, and is expressed in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `manual`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rr_min_io`{.literal}                                                                                                                                                                 | Specifies the number of I/O requests to route to a path before switching to the next path in the current path group. This setting is only for systems running kernels older than 2.6.31. Newer systems should use `rr_min_io_rq`{.literal}. The default value is `1000`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rr_min_io_rq`{.literal}                                                                                                                                                              | Specifies the number of I/O requests to route to a path, before switching to the next path in the current path group. Uses a request-based device-mapper-multipath. This setting can be used on systems running current kernels. On systems running kernels older than 2.6.31, use `rr_min_io`{.literal}. The default value is `1`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `no_path_retry`{.literal}                                                                                                                                                             | A numeric value for this attribute specifies the number of times that the path checker must fail for all paths in a multipath device, before disabling queuing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | A value of `fail`{.literal} indicates immediate failure, without queuing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | A value of `queue`{.literal} indicates that queuing should not stop until the path is fixed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `fail`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `user_friendly_names`{.literal}                                                                                                                                                       | Possible values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `yes`{.literal}: Specifies that the system can use the `/etc/multipath/bindings`{.literal} file to assign a persistent and unique alias to the multipath, in the form of `mpath<n>`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `no`{.literal}: The system uses the WWID as the alias for the multipath. Any device-specific alias you set in the `multipaths`{.literal} section of the configuration file, overrides this name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `queue_without_daemon`{.literal}                                                                                                                                                      | If set to `no`{.literal}, the `multipathd`{.literal} daemon disables queuing for all devices, when it is shut down. The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `flush_on_last_del`{.literal}                                                                                                                                                         | If set to `yes`{.literal}, the `multipathd`{.literal} daemon disables queuing when the last path to a device is deleted. The default value is no.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `max_fds`{.literal}                                                                                                                                                                   | Sets the maximum number of open file descriptors that can be opened by multipath and the `multipathd`{.literal} daemon. This is equivalent to the `ulimit -n`{.literal} command. The default value is `max`{.literal}, which sets this to the system limit from `/proc/sys/fs/nr_open`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `checker_timeout`{.literal}                                                                                                                                                           | The timeout to use for prioritizers and path checkers that issue SCSI commands with an explicit timeout, in seconds. The `sys/block/sd<x>/device/timeout`{.literal} directory contains the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fast_io_fail_tmo`{.literal}                                                                                                                                                          | The number of seconds the SCSI layer waits after a problem is detected on an FC remote port, before failing I/O to devices on that remote port. This value must be smaller than the value of `dev_loss_tmo`{.literal}. Setting this to `off`{.literal} disables the timeout. The default value is `5`{.literal}. The `fast_io_fail_tmo`{.literal} option overrides the values of the `recovery_tmo`{.literal} and `replacement_timeout`{.literal} options of the underlying path devices.                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dev_loss_tmo`{.literal}                                                                                                                                                              | The number of seconds the SCSI layer waits after a problem is detected on an FC remote port, before removing it from the system. Setting this to infinity will set this to 2147483647 seconds, or 68 years. The operating system determines the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `eh_deadline`{.literal}                                                                                                                                                               | Specifies the maximum number of seconds the SCSI layer spends performing error handling, when SCSI devices fail. After this timeout, the scsi layer performs a full Host Bus Adapter (HBA) reset. Setting this is necessary in cases where the `rport`{.literal} is never lost, so `fast_io_fail_tmo`{.literal} and `dev_loss_tmo`{.literal} never trigger, but `scsi`{.literal} commands still hang. When the SCSI error handler performs the HBA reset, this affects all target paths on that HBA. The `eh_deadline`{.literal} value should only be set in cases where all targets on the affected HBAs are multipathed.                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `unset`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `detect_prio`{.literal}                                                                                                                                                               | If set to `yes`{.literal}, multipath detects if the device is a SCSI device that supports Asymmetric Logical Unit Access (ALUA), or a NVMe device that supports Asymmetric Namespace Access (ANA). If the device supports ALUA, multipath automatically assigns it the `alua`{.literal} prioritizer. If the device supports ANA, multipath automatically assigns it the `ana`{.literal} prioritizer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | If set to `no`{.literal}, or if the device does not support ALUA or ANA, the `prio`{.literal} attribute sets the prioritizer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `yes`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `detect_pgpolicy`{.literal}                                                                                                                                                           | If `detect_pgpolicy`{.literal} is set to `yes`{.literal} and all paths of a multipath device are configured with either the `alua`{.literal} or `sysfs`{.literal} prioritizer, multipath automatically sets `path_grouping_policy`{.literal} to `group_by_prio`{.literal} or `group_by_tpg`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | If `detect_pgpolicy`{.literal} is set to `no`{.literal}, the path grouping policy is set to `failover`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `yes`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `detect_pgpolicy_use_tpg`{.literal}                                                                                                                                                   | Controls which path grouping policy is set when `detect_pgpolicy`{.literal} is set to `yes`{.literal} and an ALUA compatible device is detected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | If `detect_pgpolicy_use_tpg`{.literal} is set to `yes`{.literal}, then `detect_pgpolicy`{.literal} sets `path_grouping_policy`{.literal} to `group_by_tpg`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | If `detect_pgpolicy_use_tpg`{.literal} is set to `no`{.literal}, then `detect_pgpolicy`{.literal} sets `path_grouping_policy`{.literal} to `group_by_prio`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `uid_attribute`{.literal}                                                                                                                                                             | Specifies the `udev`{.literal} attribute to use for the device WWID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is device dependent: `ID_SERIAL`{.literal} for SCSI devices, `ID_UID`{.literal} for DASD devices, and `ID_WWN`{.literal} for NVMe devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `force_sync`{.literal}                                                                                                                                                                | If set to `yes`{.literal}, this parameter prevents path checkers from running in async mode. This means that only one checker runs at a time. This is useful in cases where many `multipathd`{.literal} checkers run in parallel, and can cause significant CPU pressure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `strict_timing`{.literal}                                                                                                                                                             | If set to `yes`{.literal}, the `multipathd`{.literal} daemon starts a new path checker loop after exactly one second, so that each path check occurs at the exactly set seconds for `polling_interval`{.literal}. On busy systems, path checks might take longer than one second. The missing ticks are accounted for in the next round. A warning prints if path checks take longer than the set seconds for `polling_interval`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `retrigger_tries`{.literal}, `retrigger_delay`{.literal}                                                                                                                              | Use the `retrigger_tries`{.literal} and `retrigger_delay`{.literal} parameters in conjunction to make `multipathd`{.literal} retrigger uevents. If `udev`{.literal} fails to completely process the original `uevents`{.literal}, this leaves multipath unable to use the device. The `retrigger_tries`{.literal} parameter sets the number of times that multipath tries to retrigger a `uevent`{.literal}, in case a device is not completely configured. The `retrigger_delay`{.literal} parameter sets the number of seconds between retries. Both of these options accept numbers greater than or equal to `0`{.literal}. Setting the `retrigger_tries`{.literal} parameter to `0`{.literal} disables retries. Setting the `retrigger_delay`{.literal} parameter to `0`{.literal} causes the `uevent`{.literal} to be reissued on the next loop of the path checker.                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value of `retrigger_tries`{.literal} is `3`{.literal}. The default value of `retrigger_delay`{.literal} is 10.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `missing_uev_wait_timeout`{.literal}                                                                                                                                                  | This attribute controls the number of seconds the `multipathd`{.literal} daemon waits to receive a change event from `udev`{.literal} for a newly created multipath device. After that it automatically enables device reloads. In most cases, `multipathd`{.literal} delays reloads on a device, until it receives a change `uevent`{.literal} from the initial table load.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `30`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `deferred_remove`{.literal}                                                                                                                                                           | If set to `yes`{.literal}, `multipathd`{.literal} performs a deferred remove, instead of a regular remove, when the last path device is deleted. This ensures that if a multipathed device is in use when a regular remove is performed and the remove fails, the device is automatically removed, when the last user closes the device. The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `san_path_err_threshold`{.literal}, `san_path_err_forget_rate`{.literal}, `san_path_err_recovery_time`{.literal}                                                                      | If you set all three of these attributes to integers greater than zero, they enable the `multipathd`{.literal} daemon to keep shaky paths from reinstating, by monitoring how frequently the path checker fails. If a path checker fails a path more than the value in the `san_path_err_threshold`{.literal} attribute, within `san_path_err_forget_rate`{.literal} checks, then the `multipathd`{.literal} daemon does not reinstate the path until the value of the `san_path_err_recovery_time`{.literal} attribute in seconds passes, without any path checker failures.                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | See the **Shaky paths detection** section of the `multipath.conf(5)`{.literal} for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `marginal_path_double_failed_time`{.literal}, `marginal_path_err_sample_time`{.literal}, `marginal_path_err_rate_threshold`{.literal}, `marginal_path_err_recheck_gap_time`{.literal} | If `marginal_path_double_failed_time`{.literal}, `marginal_path_err_rate_threshold`{.literal}, and `marginal_path_err_recheck_gap_time`{.literal} are set to integers greater than `0`{.literal} and `marginal_path_err_sample_time`{.literal} is set to an integer greater than `120`{.literal}, they enable the `multipathd`{.literal} daemon to keep shaky paths from reinstating, by testing the I/O failure rate of paths that repeatedly fail.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | If a path fails twice within the value set in the `marginal_path_double_failed_time`{.literal} attribute in seconds, the `multipathd`{.literal} daemon does not immediately reinstate it, when the path checker determines that it is back up. Instead, `multipathd`{.literal} issues a steady stream of read I/Os to the path for the value set in the `marginal_path_err_sample_time`{.literal} attribute in seconds. If there are more than the value set in the `marginal_path_err_rate_threshold`{.literal} attribute number of errors per thousand I/Os, `multipathd`{.literal} waits for `marginal_path_err_recheck_gap_time`{.literal} seconds, and then starts another cycle of testing the path with read I/Os. Otherwise, `multipathd`{.literal} reinstates the path.                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | See the **Shaky paths detection** section of the `multipath.conf(5)`{.literal} for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `marginal_pathgroups`{.literal}                                                                                                                                                       | Possible values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `on`{.literal}: When one of the marginal path detecting methods determines that a path is marginal, the system reinstates the path and places it in a separate pathgroup. This group comes into effect only after all the non-marginal path groups are tried first. This prevents the possibility of IO errors occurring while the system can still use some marginal paths. The path returns to a regular path group as soon as it passes monitoring for a configured time.                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `off`{.literal}: The `delay_*_checks`{.literal}, `marginal_path_*`{.literal}, and `san_path_err_*`{.literal} attributes keep the system from reinstating any **marginal**, or **shaky** paths, until they are monitored for a configured time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `fpin`{.literal}: The `multipathd`{.literal} daemon receives `fpin`{.literal} notifications, sets path states to `marginal`{.literal}, and regroups paths, as described for the `on`{.literal} value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The `marginal_path_*`{.literal} and `san_path_err_*`{.literal} attributes are implicitly set to `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | See the **Shaky paths detection** section of the `multipath.conf(5)`{.literal} for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `log_checker_err`{.literal}                                                                                                                                                           | If set to `once`{.literal}, `multipathd`{.literal} logs the first path checker error at verbosity level 2. The system logs any further errors at verbosity level 3, until the device is restored. If the `log_checker_err`{.literal} parameter is set to `always`{.literal}, `multipathd`{.literal} always logs the path checker error at verbosity level 2. The default value is `always`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `skip_kpartx`{.literal}                                                                                                                                                               | If set to `yes`{.literal}, `kpartx`{.literal} does not automatically create partitions on the device. This enables you to create a multipath device, without creating partitions, even if the device has a partition table. The default value of this option is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `max_sectors_kb`{.literal}                                                                                                                                                            | Using this option, you can set the `max_sectors_kb`{.literal} device queue parameter to the specified value on all underlying paths of a multipath device, before the first activation of a multipath device. Whenever the system creates a new multipath device, the device inherits the `max_sectors_kb`{.literal} value from the path devices. Manually raising this value for the multipath device, or lowering this value for the path devices, can cause multipath to create I/O operations larger than the path devices allow. Using the `max_sectors_kb`{.literal} parameter is an easy way to set these values, before the creation of a multipath device on top of the path devices, and prevent passing any invalid-sized I/O operations. If you do not set this parameter, the path devices driver sets it automatically, and the multipath device inherits it from the path devices. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ghost_delay`{.literal}                                                                                                                                                               | This attribute sets the number of seconds that multipath waits after creating a device with only ghost paths, before marking it ready for use in `systemd`{.literal}. This gives the active paths time to appear before the multipath runs the hardware handler to switch the ghost paths to active ones.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | Setting this to `0`{.literal} or `no`{.literal} makes multipath immediately mark a device with only ghost paths as ready.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `enable_foreign`{.literal}                                                                                                                                                            | This attribute enables or disables foreign libraries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The value is a regular expression. Foreign libraries are loaded if their name matches the expression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | By default, no foreign libraries are enabled. Use `nvme`{.literal} to enable NVMe native multipath support, or `".*"`{.literal} to enable all foreign libraries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `recheck_wwid`{.literal}                                                                                                                                                              | If set to `yes`{.literal}, when a failed path is restored, the `multipathd`{.literal} daemon rechecks the path WWID. If there is a change in the WWID, the path is removed from the current multipath device, and added again as a new path. The `multipathd`{.literal} daemon also checks the path WWID again if it is manually re-added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | This option only works for SCSI devices with configuration to use the default `uid_attribute`{.literal}, `ID_SERIAL`{.literal}, or `sysfs`{.literal}, for getting their WWID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `remove_retries`{.literal}                                                                                                                                                            | This option sets the number of times multipath retries removing a device that is in use. Between each attempt, multipath becomes inactive for 1 second. The default value is `0`{.literal}, which means that multipath does not retry the remove.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `detect_checker`{.literal}                                                                                                                                                            | If set to `yes`{.literal}, multipath checks if the device supports AsymmetricLogical Unit Access (ALUA) or Redundant Disk Array Controller (RDAC). If the device supports ALUA, multipath assigns it the `tur`{.literal} `path_checker`{.literal}. If the device supports RDAC, the `multipathd`{.literal} daemon assigns it the `rdac`{.literal} `path_checker`{.literal}. If the device does not support ALUA or RDAC, or the `detect_checker`{.literal} is set to `no`{.literal}, the `path_checker`{.literal} attribute sets the path checker.                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `yes`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `reservation_key`{.literal}                                                                                                                                                           | The `mpathpersist`{.literal} parameter uses this service action reservation key. It must be set for all multipath devices using persistent reservations, and it must be the same as the `RESERVATION KEY`{.literal} field of the `PERSISTENT RESERVE OUT`{.literal} parameter list, which contains an 8-byte value provided by the application client to the device server to identify the I_T nexus. If you use the `--param-aptpl`{.literal} option when registering the key with `mpathpersist`{.literal}, you must append `:aptpl`{.literal} to the end of the reservation key.                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | This parameter can also be set to `file`{.literal}, which causes `mpathpersist`{.literal} to automatically store the `RESERVATION KEY`{.literal} used to register the multipath device in the `prkeys`{.literal} file. The `multipathd`{.literal} daemon then uses this key to register additional paths as they appear. When you remove the registration, this automatically removes the `RESERVATION KEY`{.literal} from the `prkeys`{.literal} file. It is `unset`{.literal} by default. If persistent reservations are necessary, set this attribute to `file`{.literal}.                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `all_tg_pt`{.literal}                                                                                                                                                                 | If set to `yes`{.literal} when `mpathpersist`{.literal} registers keys, it treats a registered key from one host to one target port, as going from one host to all target ports. This must be set to `yes`{.literal} to successfully use `mpathpersist`{.literal} on arrays that automatically set and clear registration keys on all target ports from a host, instead of per target port per host. The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `auto_resize`{.literal}                                                                                                                                                               | Controls when the `multipathd`{.literal} command can automatically resize a multipath device. Possible values include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `never`{.literal}: `multipathd`{.literal} works without any change. This is the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `grow_only`{.literal}: `multipathd`{.literal} automatically resizes the multipath device when the device's paths have grown in size.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `grow_shrink`{.literal}: `multipathd`{.literal} automatically resizes the multipath device when the device's paths have either decreased or grown in size.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `purge_disconnected`{.literal}                                                                                                                                                        | If set to `yes`{.literal}, `multipathd`{.literal} automatically removes SCSI path devices that are in a disconnected state. This happens when a LUN is unmapped or no longer presented by a storage array, and helps clean up stale SCSI devices that would otherwise remain in the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | `purge_disconnected`{.literal} only works for SCSI path devices using the default `tur`{.literal} path checker.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                       | The default value is `no`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.1. Multipath configuration defaults

Show more

For more information, see the `multipath.conf(5)`{.literal} man page on your system.

### [4.3. Modifying multipath configuration file defaults](#modifying-multipath-configuration-file-defaults) {#modifying-multipath-configuration-file-defaults .title}

Customize global DM Multipath behavior by editing the defaults section of the `multipath.conf`{.literal} file. Set system-wide values like polling intervals, path selection algorithms, and timeouts to match the needs and performance goals of your storage environment.

**Procedure**

1.  View the `/etc/multipath.conf`{.literal} configuration file, which includes a template of configuration defaults:

    ``` {.language-plaintext tabindex="-1"}
    #defaults {
    #       polling_interval        10
    #       path_selector           "round-robin 0"
    #       path_grouping_policy    multibus
    #       uid_attribute           ID_SERIAL
    #       prio                    alua
    #       path_checker            readsector0
    #       rr_min_io               100
    #       max_fds                 8192
    #       rr_weight               priorities
    #       failback                immediate
    #       no_path_retry           fail
    #       user_friendly_names     yes
    #}
    ```

2.  Overwrite the default value for any of the configuration parameters. You can copy the relevant line from this template into the `defaults`{.literal} section and uncomment it.

    For example, to overwrite the `path_grouping_policy`{.literal} parameter to `multibus`{.literal} instead of the default value of `failover`{.literal}, copy the appropriate line from the template to the initial defaults section of the configuration file, and uncomment it, as follows:

    ``` {.language-plaintext tabindex="-1"}
    defaults {
            user_friendly_names     yes
            path_grouping_policy    multibus
    }
    ```

3.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

4.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

### [4.4. Configuration file multipaths section](#configuration-file-multipaths-section) {#configuration-file-multipaths-section .title}

The `multipaths`{.literal} section allows customization of specific multipath devices by WWID, overriding global settings with device-specific configurations like aliases and path policies.

Set attributes of individual multipath devices by using the `multipaths`{.literal} section of the `/etc/multipath.conf`{.literal} configuration file. Device Mapper (DM) Multipath uses these attributes to override all other configuration settings, including those from the `overrides`{.literal} section.

The `multipaths`{.literal} section recognizes only the `multipath`{.literal} subsection as an attribute. The following table shows the attributes that you can set in the `multipath`{.literal} subsection, for each specific multipath device. These attributes apply only to one specified multipath. If several `multipath`{.literal} subsections match a specific device World Wide Identifier (WWID), the contents of those subsections merge. The settings from latest entries have priority over any previous versions. For more information, see the `multipath.conf(5)`{.literal} man page on your system.

+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute            | Description                                                                                                                                                                                                                                                                                                              |
+:=====================+:=========================================================================================================================================================================================================================================================================================================================+
| `wwid`{.literal}     | Specifies the WWID of the multipath device, to which the multipath attributes apply. This parameter is mandatory for this section of the `multipath.conf`{.literal} file.                                                                                                                                                |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `alias`{.literal}    | Specifies the symbolic name for the multipath device, to which the multipath attributes apply. If you are using `user_friendly_names`{.literal}, do not set this value to `mpath <n>`{.literal}. This might cause conflicts with an automatically assigned user friendly name, and give you incorrect device node names. |
+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.2. Multipath subsection attributes

Show more

The following example shows multipath attributes specified in the configuration file for two specific multipath devices. The first device has a WWID of `3600508b4000156d70001200000b0000`{.literal} and a symbolic name of `yellow`{.literal}.

The second multipath device in the example has a WWID of `1DEC`{.literal}*`_`{.literal}*`321816758474`{.literal} and a symbolic name of `red`{.literal}.

**Example 4.1. Multipath attributes specification**

``` {.language-plaintext tabindex="-1"}
multipaths {
       multipath {
              wwid                  3600508b4000156d70001200000b0000
              alias                 yellow
              path_grouping_policy  multibus
              path_selector         "round-robin 0"
              failback              manual
              no_path_retry         5
       }
       multipath {
              wwid                  1DEC_321816758474
              alias                 red
        }
}
```

**Additional resources**

-   [Configuration file defaults](#configuration-file-defaults "4.2. Configuration file defaults")
-   [Configuration file overrides section](#configuration-file-overrides-section "4.6. Configuration file overrides section")

### [4.5. Configuration file devices section](#configuration-file-devices-section) {#configuration-file-devices-section .title}

The `devices`{.literal} section defines configuration settings for specific storage controller types, identified by vendor, product, and revision patterns to optimize multipath behavior per device.

Use the `devices`{.literal} section of the `multipath.conf`{.literal} configuration file to define settings for individual storage controller types. Values set in this section overwrite specified values in the `defaults`{.literal} section.

The system identifies the storage controller types by the `vendor`{.literal}, `product`{.literal}, and `revision`{.literal} keywords. These keywords are regular expressions and must match the `sysfs`{.literal} information about the specific device.

The `devices`{.literal} section recognizes only the `device`{.literal} subsection as an attribute. If there are multiple keyword matches for a device, the attributes of all matching entries apply to it. If an attribute is specified in several matching `device`{.literal} subsections, later versions of entries have priority over any previous entries. For more information, see the `multipath.conf(5)`{.literal} man page on your system

Important

Configuration attributes in the latest version of the `device`{.literal} subsections override attributes in any previous `devices`{.literal} subsections and from the `defaults`{.literal} section.

The following table shows the attributes that you can set in the `device`{.literal} subsection.

+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute                     | Description                                                                                                                                                                                                                                                                             |
+:==============================+:========================================================================================================================================================================================================================================================================================+
| `vendor`{.literal}            | Specifies the regular expression to match the device vendor name. This is a mandatory attribute.                                                                                                                                                                                        |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `product`{.literal}           | Specifies the regular expression to match the device product name. This is a mandatory attribute.                                                                                                                                                                                       |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `revision`{.literal}          | Specifies the regular expression to match the device product revision. If the revision attribute is missing, all device revisions match.                                                                                                                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `product_blacklist`{.literal} | Multipath uses this attribute to create a device `blacklist`{.literal} entry that has a `vendor`{.literal} attribute that matches the `vendor`{.literal} attribute of this device entry, and a `product`{.literal} attribute that matches this `product_blacklist`{.literal} attribute. |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `vpd_vendor`{.literal}        | Shows the vendor specific Vital Product Data (VPD) page information, using the VPD page abbreviation.                                                                                                                                                                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | The `multipathd`{.literal} daemon uses this information to gather device specific information. Currently only the `hp3par`{.literal} VPD page is supported.                                                                                                                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `hardware_handler`{.literal}  | Specifies the hardware handler to use for a particular device type. All possible values are hardware dependent and include:                                                                                                                                                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | `emc`{.literal}: Hardware handler for DGC class arrays, as CLARiiON CX/AX and EMC VNX and Unity families.                                                                                                                                                                               |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | `rdac`{.literal}: Hardware handler for LSI/Engenio/NetApp RDAC class, as NetApp SANtricity E/EF Series, and OEM arrays from IBM DELL SGI STK and SUN.                                                                                                                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | `hp_sw`{.literal}: Hardware handler for HP/COMPAQ/DEC HSG80 and MSA/HSV arrays with Active/Standby mode exclusively.                                                                                                                                                                    |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | `alua`{.literal}: Hardware handler for Small Computer System Interface-3 (SCSI-3) Asymmetric Logical Unit Access (ALUA) compatible arrays.                                                                                                                                              |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | `ana`{.literal}: Hardware handler for Non-Volatile Memory Express (NVMe) Asymmetric Namespace Access (ANA) compatible arrays.                                                                                                                                                           |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                               | The default value is `unset`{.literal}.                                                                                                                                                                                                                                                 |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.3. Devices section attributes

Show more

Important

​​Linux kernels, versions 4.3 and newer, automatically attach a device handler to known devices. This includes all devices supporting SCSI-3 ALUA). The kernel does not enable changing the handler later on. Setting the hardware_handler attribute for such devices on these kernels takes no effect.

**Additional resources**

-   [Configuration file defaults](#configuration-file-defaults "4.2. Configuration file defaults")

### [4.6. Configuration file overrides section](#configuration-file-overrides-section) {#configuration-file-overrides-section .title}

The `overrides`{.literal} section applies configuration changes to all devices, with optional protocol-specific subsections that take precedence over device and default settings.

The `overrides`{.literal} section recognizes the optional `protocol`{.literal} subsection, and can contain multiple `protocol`{.literal} subsections. The system matches path devices against the `protocol`{.literal} subsection with the mandatory `type`{.literal} attribute. Attributes in a matching `protocol`{.literal} subsection have priority over attributes in the rest of the `overrides`{.literal} section. If there are multiple matching `protocol`{.literal} subsections, later entries have higher priority. For more information, see the `multipath.conf(5)`{.literal} man page on your system.

The `protocol`{.literal} subsection recognizes the following mandatory attribute:

+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attribute            | Description                                                                                                                                                                                                                                                                                              |
+:=====================+:=========================================================================================================================================================================================================================================================================================================+
| `type`{.literal}     | Specifies the protocol string of the path device. Possible values include:                                                                                                                                                                                                                               |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      | `scsi:fcp`{.literal}, `scsi:spi`{.literal}, `scsi:ssa`{.literal}, `scsi:sbp`{.literal}, `scsi:srp`{.literal}, `scsi:iscsi`{.literal}, `scsi:sas`{.literal}, `scsi:adt`{.literal}, `scsi:ata`{.literal}, `scsi:unspec`{.literal}, `ccw`{.literal}, `cciss`{.literal}, `nvme`{.literal}, `undef`{.literal} |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                      | This attribute is not a regular expression. The path device protocol string must match exactly.                                                                                                                                                                                                          |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.4. Protocol subsection attribute

Show more

The attributes in the following list are optional for the `protocol`{.literal} subsection. If you do not set them, default values from the `overrides`{.literal}, `devices`{.literal} or `defaults`{.literal} sections apply.

-   `fast_io_fail_tmo`{.literal}
-   `dev_loss_tmo`{.literal}
-   `eh_deadline`{.literal}

**Additional resources**

-   [Configuration file defaults](#configuration-file-defaults "4.2. Configuration file defaults")

### [4.7. DM Multipath overrides of the device timeout](#dm-multipath-overrides-of-the-device-timeout) {#dm-multipath-overrides-of-the-device-timeout .title}

The `recovery_tmo`{.literal} `sysfs`{.literal} option controls the timeout for a particular Internet Small Computer Systems Interface (iSCSI) device.

The following options globally override the `recovery_tmo`{.literal} values:

-   The `replacement_timeout`{.literal} configuration option globally overrides the `recovery_tmo`{.literal} value for all iSCSI devices.

-   For all iSCSI devices that are managed by DM Multipath, the `fast_io_fail_tmo`{.literal} option in DM Multipath globally overrides the `recovery_tmo`{.literal} value.

    The `fast_io_fail_tmo`{.literal} option in DM Multipath also overrides the `fast_io_fail_tmo`{.literal} option in Fibre Channel devices.

The DM Multipath `fast_io_fail_tmo`{.literal} option takes precedence over `replacement_timeout`{.literal}. Every time the `multipathd`{.literal} service is reloaded, it resets `recovery_tmo`{.literal} to the value of the `fast_io_fail_tmo`{.literal} configuration option. Use the DM multipath `fast_io_fail_tmo`{.literal} configuration option to override `recovery_tmo`{.literal} in devices managed by DM Multipath.

### [4.8. Modifying multipath settings for specific devices](#modifying-multipath-settings-for-specific-devices) {#modifying-multipath-settings-for-specific-devices .title}

In the multipaths section of the `multipath.conf`{.literal} file, define settings for specific devices using the WWID. These settings override values in overrides, defaults, and devices, letting you fine-tune behavior per device. Multiple entries are allowed.

**Procedure**

1.  Modify the `multipaths`{.literal} section for specific multipath device. The following example shows multipath attributes specified in the configuration file for two specific multipath devices:

    -   The first device has a WWID of `3600508b4000156d70001200000b0000`{.literal} and a symbolic name of `yellow`{.literal}.
    -   The second multipath device in the example has a WWID of `1DEC_321816758474`{.literal} and a symbolic name of `red`{.literal}.

    In this example, the `rr_weight`{.literal} attribute is set to `priorities`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    multipaths {
           multipath {
                  wwid                  3600508b4000156d70001200000b0000
                  alias                 yellow
                  path_grouping_policy  multibus
                  path_selector         "round-robin 0"
                  failback              manual
                  rr_weight             priorities
                  no_path_retry         5
           }
           multipath {
                  wwid                  1DEC_321816758474
                  alias                 red
                  rr_weight             priorities
            }
    }
    ```

2.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

3.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

### [4.9. Modifying the multipath configuration for specific devices with protocol](#modifying-the-multipath-configuration-for-specific-devices-with-protocol) {#modifying-the-multipath-configuration-for-specific-devices-with-protocol .title}

You can Use the `protocol`{.literal} subsection in the overrides section of `/etc/multipath.conf`{.literal} to set path-specific options by transport type. These settings override values in overrides, devices, and defaults and apply only to matching type values.

**Prerequisites**

-   You have configured Device Mapper (DM) multipath in your system.
-   You have multipath devices where not all paths use the same transport protocol.

**Procedure**

1.  View the specific path protocol by running the following:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show paths format "%d %P"
    ```

    ``` {.language-plaintext tabindex="-1"}
    dev protocol
    sda scsi:ata
    sdb scsi:fcp
    sdc scsi:fcp
    ```

2.  Edit the `overrides`{.literal} section of the `/etc/multipath.conf`{.literal} file, by adding `protocol`{.literal} subsections for each multipath type.

    The `overrides`{.literal} section can include multiple `protocol`{.literal} subsections.

    Important

    The `protocol`{.literal} subsection must include a `type`{.literal} parameter. The configuration of all paths with a matching `type`{.literal} parameter is then updated with the rest of the parameters listed in the `protocol`{.literal} subsection.

    -   Settings for path devices, which use the `scsi:fcp`{.literal} protocol:

        ``` {.language-plaintext tabindex="-1"}
        overrides {
                dev_loss_tmo 60
                fast_io_fail_tmo 8
                protocol {
                        type "scsi:fcp"
                        dev_loss_tmo 70
                        fast_io_fail_tmo 10
                        eh_deadline 360
                }
        }
        ```

    -   Settings for path devices, which use the `scsi:iscsi`{.literal} protocol:

        ``` {.language-plaintext tabindex="-1"}
        overrides {
                dev_loss_tmo 60
                fast_io_fail_tmo 8
                protocol {
                        type "scsi:iscsi"
                        dev_loss_tmo 60
                        fast_io_fail_tmo 120
                }
        }
        ```

    -   Settings for path devices, which use all other protocols:

        ``` {.language-plaintext tabindex="-1"}
        overrides {
                dev_loss_tmo 60
                fast_io_fail_tmo 8
                protocol {
                        type "<type of protocol>"
                        dev_loss_tmo 60
                        fast_io_fail_tmo 8
                }
        }
        ```

### [4.10. Modifying multipath settings for storage controllers](#modifying-multipath-settings-for-storage-controllers) {#modifying-multipath-settings-for-storage-controllers .title}

Customize DM Multipath settings for specific storage vendors and models in the devices section of `multipath.conf`{.literal}. These attributes optimize performance and override defaults, unless replaced by values in multipaths or overrides for matching paths.

**Procedure**

1.  View the information about the default configuration value, including supported devices:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show config
    ```

    ``` {.language-plaintext tabindex="-1"}
    # multipath -t
    ```

    Many devices that support multipathing are included by default in a multipath configuration.

2.  Optional: If you need to modify the default configuration values, you can overwrite the default values by including an entry in the configuration file for the device that overwrites those values. You can copy the device configuration defaults for the device that the `multipathd show config`{.literal} command displays and override the values that you want to change.

3.  Add a device that is not configured automatically by default to the `devices`{.literal} section of the configuration file by setting the `vendor`{.literal} and `product`{.literal} parameters. Find these values by opening the `/sys/block/`{.literal}*`device_name`{.literal}*`/device/vendor`{.literal} and `/sys/block/`{.literal}*`device_name`{.literal}*`/device/model`{.literal} files where *device_name* is the device to be multipathed, as mentioned in the following example:

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/block/sda/device/vendor
    WINSYS
    ```

    ``` {.language-plaintext tabindex="-1"}
    # cat /sys/block/sda/device/model
    SF2372
    ```

4.  Optional: Specify the additional parameters depending on your specific device:

    `active/active`{.literal} device
    :   Usually there is no need to set additional parameters in this case. If required, you might set `path_grouping_policy`{.literal} to `multibus`{.literal}. Other parameters you may need to set are `no_path_retry`{.literal} and `rr_min_io`{.literal}.

    `active/passive`{.literal} device
    :   If it automatically switches paths with I/O to the passive path, you need to change the checker function to one that does not send I/O to the path to test if it is working, otherwise, your device will keep failing over. This means that you have set the `path_checker`{.literal} to `tur`{.literal}, which works for all SCSI devices that support the Test Unit Ready command, which most do.

    If the device needs a special command to switch paths, then configuring this device for multipath requires a hardware handler kernel module. The current available hardware handler is `emc`{.literal}. If this is not sufficient for your device, you might not be able to configure the device for multipath.

    The following example shows a `device`{.literal} entry in the multipath configuration file:

    ``` {.language-plaintext tabindex="-1"}
    #    }
    #   device {
    #       vendor          "COMPAQ  "
    #       product         "MSA1000         "
    #       path_grouping_policy    multibus
    #       path_checker        tur
    #       rr_weight       priorities
    #   }
    #}
    ```

5.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

6.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

### [4.11. Setting multipath values for all devices](#setting-multipath-values-for-all-devices) {#setting-multipath-values-for-all-devices .title}

Use the overrides section in `multipath.conf`{.literal} to apply global settings to all devices, ensuring consistent path management, timeouts, and other parameters. These values override defaults and devices, unless replaced in the multipaths section.

**Procedure**

1.  Override device specific settings. For example, you might want all devices to set `no_path_retry`{.literal} to `fail`{.literal}. Use the following command to turn off queueing, when all paths have failed. This overrides any device specific settings.

    ``` {.language-plaintext tabindex="-1"}
    overrides {
            no_path_retry fail
    }
    ```

2.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

3.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

## [Chapter 5. Preventing devices from multipathing](#preventing-devices-from-multipathing) {#chapter-5.-preventing-devices-from-multipathing .title}

You can configure DM Multipath to ignore selected devices when it configures multipath devices. DM Multipath does not group these ignored devices into a multipath device.

### [5.1. Conditions when DM Multipath creates a multipath device for a path](#conditions-when-dm-multipath-creates-a-multipath-device-for-a-path) {#conditions-when-dm-multipath-creates-a-multipath-device-for-a-path .title}

DM Multipath uses the `find_multipaths`{.literal} parameter and device discovery rules to automatically determine when to create multipath devices for detected storage paths.

DM Multipath has default rules to determine whether to create a multipath device for a path or ignore it. You can configure the behavior.

If `find_multipaths`{.literal} is set to `off`{.literal}, multipath always tries to create a multipath device for every non-disabled path. If the `find_multipaths`{.literal} configuration parameter is set to `on`{.literal}, then multipath creates a device, only if one of following conditions is met:

-   There are at least two paths with the same World-Wide Identification (WWID) that are not disabled.
-   You manually force the creation of the device by specifying a device with the `multipath`{.literal} command.
-   A path has the same WWID as a previously created multipath device, even if that device no longer exists. Whenever a multipath device is created, multipath remembers its WWID. It then automatically recreates the device when it detects a path with that WWID. This lets multipath automatically choose the correct paths to make into multipath devices, without having to disable multipathing on other devices.

If you created a multipath device without using `find_multipaths`{.literal} and later set it to `on`{.literal}, remove unwanted device WWIDs from `/etc/multipath/wwids`{.literal}. The following example shows a sample `/etc/multipath/wwids`{.literal} file. The WWIDs are enclosed by slashes (`/`{.literal}):

``` {.language-plaintext tabindex="-1"}
# Multipath wwids, Version : 1.0
# NOTE: This file is automatically maintained by multipath and multipathd.
# You should not need to edit this file in normal circumstances.
#
# Valid WWIDs:
/3600d0230000000000e13955cc3757802/
/3600d0230000000000e13955cc3757801/
/3600d0230000000000e13955cc3757800/
/3600d02300069c9ce09d41c31f29d4c00/
/SWINSYS  SF2372         0E13955CC3757802/
/3600d0230000000000e13955cc3757803/
```

In addition to `on`{.literal} and `off`{.literal}, you can also set `find_multipaths`{.literal} to the following values:

`strict`{.literal}
:   Multipath never accepts paths that have not previously been multipathed and are therefore not in the `/etc/multipath/wwids`{.literal} file.

`smart`{.literal}
:   Multipath always accepts non-disabled devices in `udev`{.literal} as soon as they appear. If `multipathd`{.literal} does not create the device within the timeout set in the `find_multipaths_timeout`{.literal} parameter, it releases its claim on the device.

The built-in default value of `find_multipaths`{.literal} is `off`{.literal}. The default `multipath.conf`{.literal} file created by `mpathconf`{.literal}, however, will set the value of `find_multipaths`{.literal} to `on`{.literal}.

When `find_multipaths`{.literal} is set to `on`{.literal}, disable multipathing only on devices with multiple paths that you do not want multipathed. Because of this, it will generally not be necessary to disable multipathing on devices.

If you add a multipath device to `blacklist`{.literal}, remove its WWID from the `/etc/multipath/wwids`{.literal} file by using the `-w`{.literal} option. This avoids issues with other programs. For example, to remove the device `/dev/sdb`{.literal} with WWID `3600d0230000000000e13954ed5f89300`{.literal} from the `/etc/multipath/wwids`{.literal} file, you can use either of the following methods.

-   Removing a multipath device by using the device name.

    ``` {.language-plaintext tabindex="-1"}
    # multipath -w /dev/sdb
    ```

    ``` {.language-plaintext tabindex="-1"}
    wwid '3600d0230000000000e13954ed5f89300' removed
    ```

-   Removing a multipath device by using the WWID of the device.

    ``` {.language-plaintext tabindex="-1"}
    # multipath -w 3600d0230000000000e13954ed5f89300
    ```

    ``` {.language-plaintext tabindex="-1"}
    wwid '3600d0230000000000e13954ed5f89300' removed
    ```

You can also use the `-W`{.literal} option to update the `/etc/multipath/wwids`{.literal} file. This would reset the `/etc/multipath/wwids`{.literal} file to only include the WWIDs of the current multipath devices. To reset the file, run the following:

``` {.language-plaintext tabindex="-1"}
# multipath -W
```

``` {.language-plaintext tabindex="-1"}
successfully reset wwids
```

### [5.2. Criteria for disabling multipathing on certain devices](#criteria-for-disabling-multipathing-on-certain-devices) {#criteria-for-disabling-multipathing-on-certain-devices .title}

Device exclusion from multipathing uses criteria such as, WWID, device name, type, property, or protocol, evaluated in priority order with exception lists taking precedence.

You can disable multipathing on devices by any of the following criteria:

-   WWID
-   device name
-   device type
-   property
-   protocol

Note

By default, a variety of device types are disabled, even after you comment out the initial `blacklist`{.literal} section of the configuration file.

For every device, DM Multipath evaluates these criteria in the following order:

1.  `property`{.literal}
2.  `devnode`{.literal}
3.  `device`{.literal}
4.  `protocol`{.literal}
5.  `wwid`{.literal}

If a device turns out to be disabled by any of the mentioned criteria, DM Multipath excludes it from handling by `multipathd`{.literal}, and does not evaluate the later criteria. For each criteria, the exception list takes precedence over the list of disabled devices, if a device matches both.

**Additional resources**

-   [Adding exceptions for devices with disabled multipathing](#adding-exceptions-for-devices-with-disabled-multipathing "5.8. Adding exceptions for devices with disabled multipathing")

### [5.3. Disabling multipathing by WWID](#disabling-multipathing-by-wwid) {#disabling-multipathing-by-wwid .title}

Exclude specific devices from multipath by disabling them by using their WWID in the `multipath.conf file`{.literal}. This is useful for local disks, single-path devices, or storage needing special handling outside the multipath framework.

**Procedure**

1.  Find WWID of a device:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show paths raw format "%d %w" | grep sdb
    ```

    ``` {.language-plaintext tabindex="-1"}
    sdb 3600508b4001080520001e00011700000
    ```

2.  Disable devices in the `/etc/multipath.conf`{.literal} configuration file by using the `wwid`{.literal} entry.

    The following example shows the lines in the DM Multipath configuration file that disable a device with a WWID of `3600508b4001080520001e00011700000`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    blacklist {
           wwid 3600508b4001080520001e00011700000
    }
    ```

3.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

4.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

### [5.4. Disabling multipathing by device name](#disabling-multipathing-by-device-name) {#disabling-multipathing-by-device-name .title}

Disable multipathing for specific devices by using their device names, such as `/dev/sda`{.literal} in the multipath.conf file. This prevents DM Multipath from grouping local disks, USB devices, or other storage into multipath devices, keeping them as individual block devices.

**Procedure**

1.  Display device information:

    ``` {.language-plaintext tabindex="-1"}
    # udevadm info --query=all -n /dev/mapper/sd* 
    ```

2.  Disable devices in the `/etc/multipath.conf`{.literal} configuration file by using the `devnode`{.literal} entry. The following example shows the lines in the DM Multipath configuration file that disable all SCSI devices, because it disables all `sd*`{.literal} devices as well:

    ``` {.language-plaintext tabindex="-1"}
    blacklist {
           devnode "^sd[a-z]"
    }
    ```

    You can use a `devnode`{.literal} entry to disable individual devices rather than all devices of a specific type. However, this is not recommended because unless it is statically mapped by `udev`{.literal} rules, there is no guarantee that a specific device will have the same name on reboot. For example, a device name could change from `/dev/sda`{.literal} to `/dev/sdb`{.literal} on reboot.

    By default, DM Multipath disables all devices that are not the following:

    -   Small Computer System Interface (SCSI)

    -   Non-Volatile Memory Express (NVMe)

    -   Direct Access Storage Device (DASD).

        To disable, it uses the following `devnode`{.literal} entry:

        ``` {.language-plaintext tabindex="-1"}
        blacklist {
               devnode "!^(sd[a-z]|dasd[a-z]|nvme[0-9])"
        }
        ```

        The devices that this entry disables do not generally support DM Multipath.

3.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

4.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

**Additional resources**

-   [Adding exceptions for devices with disabled multipathing](#adding-exceptions-for-devices-with-disabled-multipathing "5.8. Adding exceptions for devices with disabled multipathing")

### [5.5. Disabling multipathing by device type](#disabling-multipathing-by-device-type) {#disabling-multipathing-by-device-type .title}

Exclude entire categories of devices from multipath by specifying vendor and product info in the device section of `multipath.conf`{.literal}. This prevents DM Multipath from grouping devices of certain models or vendors, keeping them as individual block devices.

**Procedure**

1.  Display device type:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show paths raw format "%d %s" | grep sdb
    ```

    ``` {.language-plaintext tabindex="-1"}
    sdb HP,HSV210
    ```

2.  Disable devices in the `/etc/multipath.conf`{.literal} configuration file by using the `device`{.literal} section.

    The following example disables multipathing on all IBM DS4200 and HP devices:

    ``` {.language-plaintext tabindex="-1"}
    blacklist {
           device {
                   vendor  "IBM"
                   product "3S42"       #DS4200 Product 10
           }
           device {
                   vendor  "HP"
                   product ".*"
           }
    }
    ```

3.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

4.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

### [5.6. Disabling multipathing by udev property](#disabling-multipathing-by-udev-property) {#disabling-multipathing-by-udev-property .title}

Exclude devices from multipath by using their udev properties in the `multipath.conf`{.literal} file. This method allows flexible filtering based on system-detected attributes like hardware type or connection, giving precise control over which devices are excluded from multipathing.

**Procedure**

1.  Display the `udev`{.literal} variables for a device:

    ``` {.language-plaintext tabindex="-1"}
    # udevadm info --query=all -n /dev/sdb
    ```

2.  Disable devices in the `/etc/multipath.conf`{.literal} configuration file by using the `property`{.literal} parameter. This parameter is a regular expression string that matches against the `udev`{.literal} environment variable name for the devices.

    The following example disables multipathing on all devices with the `udev`{.literal} property `ID_ATA`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    blacklist {
            property "ID_ATA"
    }
    ```

3.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

4.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

### [5.7. Disabling multipathing by device protocol](#disabling-multipathing-by-device-protocol) {#disabling-multipathing-by-device-protocol .title}

Exclude devices from multipath based on their transport protocol by using the device protocol setting in `multipath.conf`{.literal}. This is useful for preventing multipathing on local or specific protocols better managed outside the multipath framework.

**Procedure**

1.  Optional: View the protocol that a path is using:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show paths raw format "%d %P" | grep sdb
    ```

    ``` {.language-plaintext tabindex="-1"}
    sdb scsi:fcp
    ```

2.  Disable devices in the `/etc/multipath.conf`{.literal} configuration file by using the `protocol`{.literal} parameter.

    The `protocol`{.literal} parameter takes a regular expression and blacklists all devices with matching protocol strings. For example, to disable multipathing on all nvme devices, use the following:

    ``` {.language-plaintext tabindex="-1"}
    blacklist {
            protocol "nvme"
    }
    ```

    DM Multipath recognizes the `protocol`{.literal} strings such as `scsi:fcp`{.literal}, `scsi:spi`{.literal}, `scsi:ssa`{.literal}, `scsi:sbp`{.literal}, `scsi:srp`{.literal}, `scsi:iscsi`{.literal}, `scsi:sas`{.literal}, `scsi:adt`{.literal}, `scsi:ata`{.literal}, `scsi:unspec`{.literal}, `ccw`{.literal}, `cciss`{.literal}, `nvme:pcie`{.literal}, `nvme:rdma`{.literal}, `nvme:fc`{.literal}, `nvme:tcp`{.literal}, `nvme:loop`{.literal}, `nvme:apple-nvme`{.literal}, `nvme:unspec`{.literal}, and `undef`{.literal}.

3.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

4.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

### [5.8. Adding exceptions for devices with disabled multipathing](#adding-exceptions-for-devices-with-disabled-multipathing) {#adding-exceptions-for-devices-with-disabled-multipathing .title}

Re-enable multipathing for specific devices by adding exceptions in `multipath.conf`{.literal}. This is useful when broad exclusion rules are in place but certain devices still require multipathing. This allows precise control over which devices are managed by DM Multipath.

**Prerequisites**

-   Multipathing is disabled on certain devices.

**Procedure**

1.  Enable multipathing on the devices by using the `blacklist_exceptions`{.literal} section of the `/etc/multipath.conf`{.literal} configuration file.

    When specifying devices in the `blacklist_exceptions`{.literal} section, you must use the same criteria as the `blacklist`{.literal} section. For example, a WWID exception does not apply to devices disabled by a `devnode`{.literal} entry, even if associated with that WWID. Similarly, `devnode`{.literal} exceptions apply only to `devnode`{.literal} entries, and `device`{.literal} exceptions apply only to device entries.

    Following is an example for adding exceptions for devices with disabled multipathing

    -   An exception by WWID

        If you have many devices and want to multipath only one with WWID `3600d0230000000000e13955cc3757803`{.literal}, you can disable all devices, then add an exception. Add the following lines to the `/etc/multipath.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        blacklist {
                wwid ".*"
        }

        blacklist_exceptions {
                wwid "3600d0230000000000e13955cc3757803"
        }
        ```

        Alternatively, you can use an exclamation mark (`!`{.literal}) to invert the `blacklist`{.literal} entry, which disables all devices except the specified WWID:

        ``` {.language-plaintext tabindex="-1"}
        blacklist {
                wwid "!3600d0230000000000e13955cc3757803"
        }
        ```

    -   An exception by udev property

        The `property`{.literal} parameter works differently than the other `blacklist_exception`{.literal} parameters. The value of the `property`{.literal} parameter must match the name of a variable in the `udev`{.literal} database. Otherwise, the device is disabled. Using this parameter, you can disable multipathing on certain SCSI devices, such as USB sticks and local hard drives.

        To enable multipathing only on SCSI devices that can reasonably be multipathed, set this parameter to `(SCSI_IDENT_|ID_WWN)`{.literal} as in the following example:

        ``` {.language-plaintext tabindex="-1"}
        blacklist_exceptions {
                property "(SCSI_IDENT_|ID_WWN)"
        }
        ```

2.  Validate the `/etc/multipath.conf`{.literal} file after modifying the multipath configuration file by running one of the following commands:

    -   To display any configuration errors, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t > /dev/null
        ```

    -   To display the new configuration with the changes added, run:

        ``` {.language-plaintext tabindex="-1"}
        # multipath -t
        ```

3.  Reload the `/etc/multipath.conf`{.literal} file and reconfigure the `multipathd`{.literal} daemon for changes to take effect:

    ``` {.language-plaintext tabindex="-1"}
    # service multipathd reload
    ```

## [Chapter 6. Managing multipathed volumes](#managing-multipathed-volumes) {#chapter-6.-managing-multipathed-volumes .title}

You can manage multipath volumes by using the `multipath`{.literal}, `dmsetup`{.literal}, and `multipathd`{.literal} commands, which are provided by Device Mapper (DM) Multipath to resize devices, move file systems, and administer the `multipathd`{.literal} daemon.

### [6.1. Resizing an online multipath device](#resizing-an-online-multipath-device) {#resizing-an-online-multipath-device .title}

Resize an online multipath device and its filesystem by using the `multipathd`{.literal} and `resize2fs`{.literal} commands. This allows you to expand storage capacity without downtime, ensuring applications remain available while scaling to meet growing data needs.

**Procedure**

1.  Resize your physical device.

2.  Find the paths to the logical unit number (LUN):

    ``` {.language-plaintext tabindex="-1"}
    # multipath -l
    ```

3.  Resize your paths. For Small Computer System Interface (SCSI) devices, writing a 1 to the `rescan`{.literal} file for the device causes the SCSI driver to rescan, as in the following command:

    ``` {.language-plaintext tabindex="-1"}
    # echo 1 > /sys/block/path_device/device/rescan
    ```

    Ensure that you run this command for each of the path devices. For example, if your path devices are `sda`{.literal}, `sdb`{.literal}, `sde`{.literal}, and `sdf`{.literal}, run the following commands:

    ``` {.language-plaintext tabindex="-1"}
    # echo 1 > /sys/block/sda/device/rescan
    ```

    ``` {.language-plaintext tabindex="-1"}
    # echo 1 > /sys/block/sdb/device/rescan
    ```

    ``` {.language-plaintext tabindex="-1"}
    # echo 1 > /sys/block/sde/device/rescan
    ```

    ``` {.language-plaintext tabindex="-1"}
    # echo 1 > /sys/block/sdf/device/rescan
    ```

4.  Resize your multipath device:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd resize map multipath_device
    ```

5.  Resize the file system, assuming no LVM or DOS partitions are used:

    ``` {.language-plaintext tabindex="-1"}
    # resize2fs /dev/mapper/mpatha
    ```

### [6.2. Moving a root file system from a single path device to a multipath device](#moving-a-root-file-system-from-a-single-path-device-to-a-multipath-device) {#moving-a-root-file-system-from-a-single-path-device-to-a-multipath-device .title}

Move the root filesystem from a single-path device to a multipath setup to ensure path redundancy for critical system data. This enhances reliability by allowing the system to boot and operate even if one storage path fails, improving overall availability.

**Prerequisites**

-   You have installed the `device-mapper-multipath`{.literal} package.

**Procedure**

1.  Create the `/etc/multipath.conf`{.literal} configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # mpathconf --enable
    ```

2.  Enable the `multipathd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable multipathd.service
    ```

3.  If `find_multipaths`{.literal} is not set to `on`{.literal}, edit the `blacklist`{.literal} and `blacklist_exceptions`{.literal} sections of `/etc/multipath.conf`{.literal}, as described in [Preventing devices from multipathing](#preventing-devices-from-multipathing "Chapter 5. Preventing devices from multipathing").

4.  Add the WWID of the device to the `/etc/multipath/wwids`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -a /dev/sdb
    ```

    ``` {.language-plaintext tabindex="-1"}
    wwid '3600d02300069c9ce09d41c4ac9c53200' added
    ```

    Replace */dev/sdb* with the root device name.

5.  Confirm that your configuration file is configured correctly:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -d 3600d02300069c9ce09d41c4ac9c53200
    ```

    ``` {.language-plaintext tabindex="-1"}
    : mpatha (3600d02300069c9ce09d41c4ac9c53200) undef 3PARdata,VV
    size=446M features='1 queue_if_no_path' hwhandler='1 alua' wp=undef
    `-+- policy='service-time 0' prio=50 status=undef
      `- 5:0:0:0 sdb 8:16 undef ready running
    ```

    Replace 3600d02300069c9ce09d41c4ac9c53200 with the WWID of your swap device.

6.  Rebuild the `initramfs`{.literal} file system with `multipath`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # dracut --force --add multipath
    ```

7.  Shut the machine down.

8.  Boot the machine.

9.  Make the other paths visible to the machine.

**Verification**

-   Check if the multipath device is created by running the following command:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -l | grep 3600d02300069c9ce09d41c4ac9c53200
    ```

    ``` {.language-plaintext tabindex="-1"}
    mpatha (3600d02300069c9ce09d41c4ac9c53200) dm-0 3PARdata,VV
    ```

### [6.3. Moving a swap file system from a single path device to a multipath device](#moving-a-swap-file-system-from-a-single-path-device-to-a-multipath-device) {#moving-a-swap-file-system-from-a-single-path-device-to-a-multipath-device .title}

Move swap file system from single-path to multipath storage to ensure redundancy and prevent performance issues. If swap uses Logical Volume Manager (LVM), no special steps are needed. However, non-LVM swap devices might require editing `/etc/fstab`{.literal} to use the correct multipath device name.

**Procedure**

1.  Create the `/etc/multipath.conf`{.literal} configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # mpathconf --enable
    ```

2.  Enable the `multipathd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable multipathd.service
    ```

3.  If the `find_multipaths`{.literal} configuration parameter is not set to `on`{.literal}, edit the `blacklist`{.literal} and `blacklist_exceptions`{.literal} sections of the `/etc/multipath.conf`{.literal} file, as described in [Preventing devices from multipathing](#preventing-devices-from-multipathing "Chapter 5. Preventing devices from multipathing").

4.  Add the WWID of the device to the `/etc/multipath/wwids`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -a /dev/sdb
    ```

    ``` {.language-plaintext tabindex="-1"}
    wwid '3600d02300069c9ce09d41c4ac9c53200' added
    ```

    Replace */dev/sdb* with the swap device name.

5.  Confirm that your configuration file is configured correctly:

    ``` {.language-plaintext tabindex="-1"}
    # multipath -d 3600d02300069c9ce09d41c4ac9c53200
    ```

    ``` {.language-plaintext tabindex="-1"}
    : mpatha (3600d02300069c9ce09d41c4ac9c53200) undef 3PARdata,VV
    size=446M features='1 queue_if_no_path' hwhandler='1 alua' wp=undef
    `-+- policy='service-time 0' prio=50 status=undef
      `- 5:0:0:0 sdb 8:16 undef ready running
    ```

    Replace 3600d02300069c9ce09d41c4ac9c53200 with the WWID of your swap device.

6.  Configure an alias for the swap device in the `/etc/multipath.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    multipaths {
        multipath {
            wwid WWID_of_swap_device
            alias swapdev
        }
    }
    ```

7.  Edit the `/etc/fstab`{.literal} file and replace the old device path to the root device with the multipath device.

    For example, if you had the following entry in the `/etc/fstab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    /dev/sdb2 swap                    swap    defaults        0 0
    ```

    Change the entry to the following:

    ``` {.language-plaintext tabindex="-1"}
    /dev/mapper/swapdev swap          swap    defaults        0 0
    ```

8.  Rebuild the initramfs file system with multipath:

    ``` {.language-plaintext tabindex="-1"}
    # dracut --force --add multipath
    ```

9.  Shut the machine down.

10. Boot the machine and make the other paths visible to the machine.

**Verification**

-   Verify if the swap device is on the multipath device:

    ``` {.language-plaintext tabindex="-1"}
    # swapon -s
    ```

    ``` {.language-plaintext tabindex="-1"}
    Filename                Type          Size Used    Priority
    /dev/dm-3               partition     4169724 0    -2
    ```

    The file name should match the multipath swap device.

    ``` {.language-plaintext tabindex="-1"}
    # readlink -f /dev/mapper/swapdev
    ```

    ``` {.language-plaintext tabindex="-1"}
    /dev/dm-3
    ```

### [6.4. Determining device mapper entries for multipath devices](#determining-device-mapper-entries-for-multipath-devices) {#determining-device-mapper-entries-for-multipath-devices .title}

Identify device mapper entries for configured multipath devices by using the `multipathd`{.literal} command. This helps link multipath device names to their underlying device mapper entries, aiding in monitoring, troubleshooting, and system administration tasks for accurate device identification.

**Procedure**

-   Display all device mapper devices:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show maps format "%n %d"
    ```

    ``` {.language-plaintext tabindex="-1"}
    name   sysfs
    mpathd dm-4
    mpathb dm-3
    mpatha dm-2
    mpathh dm-9
    ```

### [6.5. Administering the multipathd daemon](#administering-the-multipathd-daemon) {#administering-the-multipathd-daemon .title}

Manage and interact with the `multipathd`{.literal} daemon by using its commands. Administering `multipathd`{.literal} is essential for monitoring path status, viewing device info, and controlling multipath behavior in real-time without needing service restarts or system reboots.

**Procedure**

-   View the default format for the output of the `multipathd show maps`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show maps
    ```

    ``` {.language-plaintext tabindex="-1"}
    name sysfs uuid
    mpathc dm-0 360a98000324669436c2b45666c567942
    ```

-   Some `multipathd`{.literal} commands include a `format`{.literal} option followed by a wildcard. Display a list of available wildcards with the following command:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show wildcards
    ```

    ``` {.language-plaintext tabindex="-1"}
    multipath format wildcards:
    %n  name
    %w  uuid
    %d  sysfs
    ...
    ```

-   Display the multipath devices that `multipathd`{.literal} is monitoring. Use wildcards to specify the shown fields:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show maps format "%n %w %d %s"
    ```

    ``` {.language-plaintext tabindex="-1"}
    name   uuid                              sysfs vend/prod/rev
    mpathc 360a98000324669436c2b45666c567942 dm-0  NETAPP,LUN
    ```

-   Display the paths that `multipathd`{.literal} is monitoring. Use wildcards to specify the shown fields:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show paths format "%n %w %d %s"
    ```

    ``` {.language-plaintext tabindex="-1"}
    target WWNN        uuid                              dev vend/prod/rev
    0x50001fe1500d2250 3600508b4001080520001e00011700000 sdb HP,HSV210
    ```

-   Display data in a raw format:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd show maps raw format "%n %w %d %s"
    ```

    ``` {.language-plaintext tabindex="-1"}
    mpathc 360a98000324669436c2b45666c567942 dm-0 NETAPP,LUN
    ```

    In raw format, no headers are printed and the fields are not padded to align the columns with the headers. This output can be more easily used for scripting.

## [Chapter 7. Removing storage devices](#removing-storage-devices) {#chapter-7.-removing-storage-devices .title}

You can safely remove a storage device from a running system, which helps prevent system memory overload and data loss.

Do not remove a storage device on a system where:

-   Free memory is less than 5% of the total memory in more than 10 samples per 100.
-   Swapping is active (non-zero `si`{.literal} and `so`{.literal} columns in the `vmstat`{.literal} command output).

Before you remove a storage device, ensure that you have enough free system memory due to the increased system memory load during an I/O flush. Use the following commands to view the current memory load and free memory of the system:

\+

``` {.language-plaintext tabindex="-1"}
# vmstat 1 100
```

\+

``` {.language-plaintext tabindex="-1"}
# free
```

### [7.1. Safe removal of storage devices](#safe-removal-of-storage-devices) {#safe-removal-of-storage-devices .title}

Safely removing a storage device from a running system requires a top-to-bottom approach. Start from the top layer, which typically is an application or a file system, and work towards the bottom layer. The bottom layer is the physical device.

You can use storage devices in multiple ways, and they can have different virtual configurations on top of physical devices. For example, you can group multiple instances of a device into a multipath device. You can also include it in a Redundant Array of Independent Disks (RAID). You can also make the device part of a Logical Volume Manager (LVM) group. Additionally, devices can be accessed through a file system, or they can be accessed directly such as a \"raw\" device.

While using the top-to-bottom approach, you must ensure that:

-   the device that you want to remove is not in use
-   all pending I/O to the device is flushed
-   the operating system is not referencing the storage device

### [7.2. Removing block devices and associated metadata](#removing-block-devices-and-associated-metadata) {#removing-block-devices-and-associated-metadata .title}

To safely remove a block device from a running system and avoid memory overload or data loss, remove its metadata first. Address each layer, starting with the filesystem down to the disk---to ensure the system remains stable and in a consistent state.

**Prerequisites**

-   You have an existing block device stack containing the file system, the logical volume, and the volume group.

-   You ensured that no other applications or services are using the device that you want to remove.

-   You backed up the data from the device that you want to remove.

-   Optional: If you want to remove a multipath device, and you are unable to access its path devices, disable queueing of the multipath device. Run the following command:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd disablequeueing map multipath-device
    ```

    This enables the I/O of the device to fail, allowing the applications that are using the device to shut down.

Note

Removing devices with their metadata one layer at a time ensures no stale signatures remain on the disk.

Use specific commands depending on what type of devices you are removing:

-   For LVM, run `lvremove`{.literal}, `vgremove`{.literal}, and `pvremove`{.literal}.
-   For software Redundant Array of Independent Disks (RAID), run `mdadm`{.literal} to remove the array. For more information, see [Managing RAID](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_storage_devices/managing-raid).
-   For block devices encrypted by using Linux Unified Key Setup (LUKS), there are specific additional steps. The following procedure will not work for the block devices encrypted by using LUKS. For more information, see [Encrypting block devices by using LUKS](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_storage_devices/encrypting-block-devices-by-using-luks).

Warning

Rescanning the Small Computer System Interface (SCSI) bus or performing other actions that change the operating system state can cause delays. These delays may result from I/O timeouts, unexpected device removal, or data loss.

**Procedure**

1.  Unmount the file system:

    ``` {.language-plaintext tabindex="-1"}
    # umount /mnt/mount-point
    ```

2.  Remove the file system:

    ``` {.language-plaintext tabindex="-1"}
    # wipefs -a /dev/vg0/myvol
    ```

    If you have added an entry into the `/etc/fstab`{.literal} file to make a persistent association between the file system and a mount point, remove it. Edit `/etc/fstab`{.literal} at this point to remove that entry.

    Continue with the following steps, depending on the type of the device you want to remove:

3.  Remove the logical volume (LV) that contained the file system:

    ``` {.language-plaintext tabindex="-1"}
    # lvremove vg0/myvol
    ```

4.  If no other logical volumes remain in the volume group (VG), you can safely remove the VG that contained the device:

    ``` {.language-plaintext tabindex="-1"}
    # vgremove vg0
    ```

5.  Remove the physical volume (PV) metadata from the PV device(s):

    ``` {.language-plaintext tabindex="-1"}
    # pvremove /dev/sdc1
    ```

    ``` {.language-plaintext tabindex="-1"}
    # wipefs -a /dev/sdc1
    ```

6.  Remove the partitions that contained the PVs:

    ``` {.language-plaintext tabindex="-1"}
    # parted /dev/sdc rm 1
    ```

7.  Remove the partition table if you want to fully wipe the device:

    ``` {.language-plaintext tabindex="-1"}
    # wipefs -a /dev/sdc
    ```

8.  Run the following steps only if you want to physically remove the device:

    -   If you are removing a multipath device, run the following commands:

        a.  View all the paths to the device:

            ``` {.language-plaintext tabindex="-1"}
            # multipath -l
            ```

            The output of this command is required in a later step.

        b.  Flush the I/O and remove the multipath device:

            ``` {.language-plaintext tabindex="-1"}
            # multipath -f multipath-device
            ```

    -   Flush any outstanding I/O to all device paths if the device is not configured as multipath. Also flush if it is multipath and you previously passed I/O to individual paths:

        ``` {.language-plaintext tabindex="-1"}
        # blockdev --flushbufs device
        ```

        This is important for devices accessed directly where the `umount`{.literal} or `vgreduce`{.literal} commands do not flush the I/O.

    -   If you are removing a SCSI device, run the following commands:

        a.  Remove any reference to the path-based name of the device in applications, scripts, or utilities on the system. This includes *`/dev/sd`{.literal}*, *`/dev/disk/by-path`{.literal}*, or the `major:minor`{.literal} number. This ensures that different devices added in the future are not mistaken for the current device.

        b.  Remove each path to the device from the SCSI subsystem:

            ``` {.language-plaintext tabindex="-1"}
            # echo 1 > /sys/block/device-name/device/delete
            ```

            Here the *`device-name`{.literal}* is retrieved from the output of the `multipath -l`{.literal} command if the device was previously used as multipath.

9.  Remove the physical device from a running system. Note that the I/O to other devices does not stop when you remove this device.

**Verification**

-   Verify that the devices you intended to remove are not displaying on the output of `lsblk`{.literal} command. The following is an example output:

    ``` {.language-plaintext tabindex="-1"}
    # lsblk
    ```

    ``` {.language-plaintext tabindex="-1"}
    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    sda      8:0    0    5G  0 disk
    sr0     11:0    1 1024M  0 rom
    vda    252:0    0   10G  0 disk
    |-vda1 252:1    0    1M  0 part
    |-vda2 252:2    0  100M  0 part /boot/efi
    `-vda3 252:3    0  9.9G  0 part /
    ```

## [Chapter 8. Troubleshooting DM Multipath](#troubleshooting-dm-multipath) {#chapter-8.-troubleshooting-dm-multipath .title}

Troubleshoot multipath configuration issues by checking daemon status, \"queue_if_no_path\" feature problems, and the `multipathd`{.literal} interactive console for diagnostics.

The following issues may result in a slow or non-functioning multipath configuration:

The multipath daemon is not running
:   If you find you have trouble implementing a multipath configuration, ensure that the `multipathd`{.literal} daemon is running.

Issues with `queue_if_no_path`{.literal} feature
:   If a multipath device is configured with the \"1 queue_if_no_path\" option, any process issuing I/O will hang. It remains hung until one or more paths are restored.

### [8.1. Troubleshooting issues with queue_if_no_path feature](#troubleshooting-issues-with-queueifnopath-feature) {#troubleshooting-issues-with-queue_if_no_path-feature .title}

Resolve I/O hangs from `queue_if_no_path`{.literal} by setting `no_path_retry N`{.literal} in `/etc/multipath.conf`{.literal}, limiting retries when all paths fail. You can also disable queueing at runtime for specific Logical Unit Numbers (LUNs) to prevent applications from hanging during path outages.

**Procedure**

1.  Disable queueing:

    -   For a specific device:

        ``` {.language-plaintext tabindex="-1"}
        # multipathd disablequeueing map device
        ```

    -   For all devices:

        ``` {.language-plaintext tabindex="-1"}
        # multipathd disablequeueing maps
        ```

        After you disable queueing, it will remain disabled until you restart or reload `multipathd`{.literal}.

2.  Reset queueing to a previous value:

    -   For a specific device:

        ``` {.language-plaintext tabindex="-1"}
        # multipathd restorequeueing map device
        ```

    -   For all devices:

        ``` {.language-plaintext tabindex="-1"}
        # multipathd restorequeueing maps
        ```

### [8.2. Troubleshooting with the multipathd interactive console](#troubleshooting-with-the-multipathd-interactive-console) {#troubleshooting-with-the-multipathd-interactive-console .title}

Use the `multipathd -k`{.literal} interactive console to troubleshoot multipath issues in real time. This console provides access to status info, config details, and control commands. Type `help`{.literal} for commands and press Ctrl+D to exit without disrupting services.

**Procedure**

1.  Display the multipath configuration, including the default values, before exiting the console:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd -k
    ```

    ``` {.language-plaintext tabindex="-1"}
    multipathd> show config
    multipathd> Ctrl+D
    ```

2.  Ensure that multipath picked up all changes to the `multipath.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd -k
    ```

    ``` {.language-plaintext tabindex="-1"}
    multipathd> reconfigure
    multipathd> Ctrl+D
    ```

3.  Ensure that the path checker is working properly:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd -k
    ```

    ``` {.language-plaintext tabindex="-1"}
    multipathd> show paths
    multipathd> Ctrl+D
    ```

4.  You can also run a single `multipathd`{.literal} interactive command directly from the command line, without starting the interactive console. For example, to check that multipath picks up all changes to the `multipath.conf`{.literal} file, run the following command:

    ``` {.language-plaintext tabindex="-1"}
    # multipathd reconfigure
    ```

**Additional resources**

-   [Configuring DM Multipath](#configuring-dm-multipath "Chapter 3. Configuring DM Multipath")

## [Chapter 9. Configuring maximum time for storage error recovery with eh_deadline](#configuring-maximum-time-for-storage-error-recovery-with-ehdeadline) {#chapter-9.-configuring-maximum-time-for-storage-error-recovery-with-eh_deadline .title}

You can configure the maximum allowed time to recover failed SCSI devices. This configuration guarantees an I/O response time even when storage hardware becomes unresponsive due to a failure.

### [9.1. The eh_deadline parameter](#the-ehdeadline-parameter) {#the-eh_deadline-parameter .title}

The `eh_deadline`{.literal} parameter sets a maximum time limit for Small Computer System Interface (SCSI) error recovery operations, after which the system resets the entire host bus adapter to prevent indefinite hangs.

The SCSI error handling (EH) mechanism attempts to perform error recovery on failed SCSI devices. The SCSI host object `eh_deadline`{.literal} parameter enables you to configure the maximum amount of time for the recovery. After the configured time expires, SCSI EH stops and resets the entire Host Bus Adapter (HBA).

Using `eh_deadline`{.literal} can reduce the time:

-   to shut off a failed path,
-   to switch a path, or
-   to disable a RAID slice.

Warning

When `eh_deadline`{.literal} expires, SCSI EH resets the HBA, affecting all target paths on that HBA, not only the failing one. If some of the redundant paths are not available for other reasons, I/O errors might occur. Enable `eh_deadline`{.literal} only if you have multipath configured on all targets. Also, if your multipath devices are not fully redundant, you should verify that `no_path_retry`{.literal} is set large enough to allow paths to recover.

The value of the `eh_deadline`{.literal} parameter is specified in seconds. The default setting is `off`{.literal}, which disables the time limit and allows all of the error recovery to take place.

**Scenarios when eh_deadline is useful**

In most scenarios, you do not need to enable `eh_deadline`{.literal}. Using `eh_deadline`{.literal} can be useful in certain specific scenarios. For example, a link loss can occur between a Fibre Channel (FC) switch and a target port. In this case, the HBA does not receive Registered State Change Notifications (RSCNs). In such a case, I/O requests and error recovery commands all time out rather than encounter an error. Setting `eh_deadline`{.literal} in this environment puts an upper limit on the recovery time. That enables the failed I/O to be retried on another available path by DM Multipath.

Under the following conditions, the `eh_deadline`{.literal} parameter provides no additional benefit, because the I/O and error recovery commands fail immediately, which enables DM Multipath to retry:

-   If RSCNs are enabled
-   If the HBA does not register the link becoming unavailable

### [9.2. Setting the eh_deadline parameter](#setting-the-ehdeadline-parameter) {#setting-the-eh_deadline-parameter .title}

Configure the eh_deadline parameter to limit the maximum time allowed for Small Computer System Interface (SCSI) error recovery. This ensures predictable I/O response times and prevents indefinite hangs, allowing applications to handle unresponsive storage with defined timeout limits.

**Procedure**

-   You can configure `eh_deadline`{.literal} with either of the following methods:

    -   `defaults`{.literal} section of the `multpath.conf`{.literal} file

        From the defaults section of the `multpath.conf`{.literal} file, set the `eh_deadline`{.literal} parameter to the required number of seconds:

        ``` {.language-plaintext tabindex="-1"}
        # eh_deadline 300
        ```

        Note

        From RHEL 8.4, setting the `eh_deadline`{.literal} parameter by using the defaults section of the `multpath.conf`{.literal} file is the preferred method.

        To turn off the `eh_deadline`{.literal} parameter with this method, set `eh_deadline`{.literal} to `off`{.literal}.

    -   `sysfs`{.literal}

        Write the number of seconds into the `/sys/class/scsi_host/host<host-number>/eh_deadline`{.literal} files. For example, to set the `eh_deadline`{.literal} parameter through `sysfs`{.literal} on SCSI host 6:

        ``` {.language-plaintext tabindex="-1"}
        # echo 300 > /sys/class/scsi_host/host6/eh_deadline
        ```

        To turn off the `eh_deadline`{.literal} parameter with this method, use echo `off`{.literal}.

    -   Kernel parameter

        Set a default value for all SCSI Host Bus Adapters (HBAs) by using the `scsi_mod.eh_deadline`{.literal} kernel parameter.

        ``` {.language-plaintext tabindex="-1"}
        # echo 300 > /sys/module/scsi_mod/parameters/eh_deadline
        ```

        To turn off the `eh_deadline`{.literal} parameter with this method, use echo `-1`{.literal}.

**Additional resources**

-   [How to set eh_deadline and eh_timeout persistently, using a udev rule](https://access.redhat.com/solutions/3209481)

## [Legal Notice](#idm139779445705600) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
