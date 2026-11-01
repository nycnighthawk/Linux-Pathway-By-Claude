---
{"title": "Managing file systems", "guide": "managing_file_systems", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/managing_file_systems/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Managing file systems {#managing-file-systems .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Creating, modifying, and administering file systems {#creating-modifying-and-administering-file-systems .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm139944793744784)

**Abstract**

Red Hat Enterprise Linux supports a variety of file systems. Each type of file system solves different problems and their usage is application specific. Use the information about the key differences and considerations to select and deploy the appropriate file system based on your specific application requirements.

The supported file systems include local on-disk file systems XFS and ext4, and network and client-and-server file systems NFS and SMB. You can perform several operations with a file system such as creating, mounting, backing up, restoring, checking and repairing, as well as limiting the storage space by using quotas.

------------------------------------------------------------------------

## [Chapter 1. Overview of available file systems](#overview-of-available-file-systems) {#chapter-1.-overview-of-available-file-systems .title}

Choosing the file system that is appropriate for your application is an important decision due to the large number of options available and the choices to consider.

The following sections describe the file systems that Red Hat Enterprise Linux 10 includes by default, and recommendations on the most suitable file system for your application.

### [1.1. Types of file systems](#types-of-file-systems) {#types-of-file-systems .title}

Red Hat Enterprise Linux 10 supports a variety of file systems (FS). Different types of file systems solve different kinds of problems, and their usage is application specific.

At the most general level, available file systems can be grouped into the following major types:

+---------------------------------+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type                            | File system                | Attributes and use cases                                                                                                                                                                                                                                                                                                                                            |
+:================================+:===========================+:====================================================================================================================================================================================================================================================================================================================================================================+
| Disk or local FS                | XFS                        | XFS is the default file system in RHEL. Deploy XFS as your local file system unless there are specific reasons to do otherwise. For example, compatibility or corner cases around performance.                                                                                                                                                                      |
+---------------------------------+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                 | ext4                       | ext4 has the benefit of familiarity in Linux, having evolved from the older ext2 and ext3 file systems. In many cases, it rivals XFS on performance. Support limits for ext4 file system and file sizes are lower than those on XFS.                                                                                                                                |
+---------------------------------+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Network or client-and-server FS | Network File System (NFS)  | Use NFS to share files between multiple systems on the same network.                                                                                                                                                                                                                                                                                                |
+---------------------------------+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                 | Server Message Block (SMB) | Use SMB for file sharing with Microsoft Windows systems.                                                                                                                                                                                                                                                                                                            |
+---------------------------------+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume-managing FS              | Stratis                    | Stratis is a volume manager built on a combination of XFS and Logical Volume Manager (LVM). The purpose of Stratis is to emulate capabilities offered by volume-managing file systems like Btrfs and ZFS. It is possible to build this stack manually, but Stratis reduces configuration complexity, implements best practices, and consolidates error information. |
+---------------------------------+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.1. Types of file systems and their use cases

Show more

### [1.2. Local file systems](#local-file-systems) {#local-file-systems .title}

Local file systems run on one server with directly attached storage. They are used for internal Serial Advanced Technology Attachment (SATA) or Serial Attached SCSI (SAS) disks, hardware RAID, and non-shared SAN devices.

All local file systems follow Portable Operating System Interface (POSIX) standards and provide support for a well-defined set of system calls. Examples include read(), write(), and seek().

Available local file systems

:   -   XFS
    -   ext4

### [1.3. The XFS file system](#the-xfs-file-system_overview-of-available-file-systems) {#the-xfs-file-system .title}

XFS is a scalable, high-performance, 64-bit journaling file system. It supports very large files and file systems and is default in RHEL 10. Originally developed by SGI in the 1990s, it has long been used on large servers and storage arrays.

The features of XFS include:

Reliability

:   -   Metadata journaling ensures file system integrity after a system crash. It keeps a record of file system operations. These records can be replayed when the system restarts and the file system is remounted.
    -   Extensive run-time metadata consistency checking
    -   Scalable and fast repair utilities
    -   Quota journaling. This avoids the need for lengthy quota consistency checks after a crash.

Scalability and performance

:   -   Supported file system size up to 1024 TiB
    -   Ability to support a large number of concurrent operations
    -   B-tree indexing for scalability of free space management
    -   Sophisticated metadata read-ahead algorithms
    -   Optimizations for streaming video workloads

Allocation schemes

:   -   Extent-based allocation
    -   Stripe-aware allocation policies
    -   Delayed allocation
    -   Space pre-allocation
    -   Dynamically allocated inodes

Other features

:   -   Reflink-based file copies
    -   Tightly integrated backup and restore utilities
    -   Online defragmentation
    -   Online file system growing
    -   Comprehensive diagnostics capabilities
    -   Extended attributes (`xattr`{.literal}). With this, the system can associate several additional name/value pairs per file.
    -   Project or directory quotas for quota restrictions over a directory tree.
    -   Subsecond timestamps

Performance characteristics

:   XFS has high performance on large systems with enterprise workloads. A large system is one with a relatively high number of CPUs, multiple HBAs, and connections to external disk arrays. XFS also performs well on smaller systems that have a multi-threaded, parallel I/O workload.

    XFS performs comparably well on smaller systems, but is more focused on scalability and large data sets.

### [1.4. The ext4 file system](#the-ext4-file-system) {#the-ext4-file-system .title}

The ext4 file system is the fourth generation of the ext file system family. The ext4 driver can read and write to ext2 and ext3 file systems. However, the ext4 file system format is not compatible with ext2 and ext3 drivers.

ext4 adds several new and improved features, such as:

-   Supported file system size up to 50 TiB
-   Extent-based metadata
-   Delayed allocation
-   Journal checksumming
-   Large storage support

The extent-based metadata and the delayed allocation features help to track utilized space in a file system. These features improve file system performance and reduce the space consumed by metadata. The file system postpones selecting the permanent location for newly written user data because of delayed allocation.

The location is chosen only when the data is flushed to disk. This causes higher performance since it can allow for larger, more contiguous allocations. The file system can make decisions with much better information.

File system repair time by using the `fsck`{.literal} utility in ext4 is much faster than in ext2 and ext3. Some file system repairs have demonstrated up to a six-fold increase in performance.

### [1.5. Comparison of XFS and ext4](#comparison-of-xfs-and-ext4) {#comparison-of-xfs-and-ext4 .title}

XFS is the default file system in RHEL. This section compares the usage and features of XFS and ext4.

Metadata error behavior
:   In ext4, you can configure the behavior when the file system encounters metadata errors. The default behavior is to continue the operation. When XFS encounters an unrecoverable metadata error, it shuts down the file system and returns the `EFSCORRUPTED`{.literal} error. XFS also supports configurable error handling.

Quotas

:   In ext4, you can enable quotas when creating the file system or later on an existing file system. You can then configure the quota enforcement by using a mount option.

    XFS quotas are not a remountable option. You must activate quotas on the initial mount.

    Running the `quotacheck`{.literal} command on an XFS file system has no effect. The first time you turn on quota accounting, XFS checks quotas automatically.

File system resize
:   XFS has no utility to reduce the size of a file system. You can only increase the size of an XFS file system. In comparison, ext4 supports both extending and reducing the size of a file system. However, shrinking is only an offline operation.

Inode numbers

:   The ext4 file system does not support more than 2^32^ inodes.

    XFS supports dynamic inode allocation. The amount of space inodes can consume on an XFS filesystem is calculated as a percentage of the total filesystem space. To prevent the system from running out of inodes, an administrator can tune this percentage after the filesystem has been created. To prevent the system from running out of inodes, an administrator can tune this percentage after the file system has been created. This is possible when there is free space available on the file system.

    Certain applications cannot properly handle inode numbers larger than 2^32^ on an XFS file system. These applications might cause the failure of 32-bit stat calls with the `EOVERFLOW`{.literal} return value. Inode number exceed 2^32^ under the following conditions:

    -   The file system is larger than 1 TiB with 256-byte inodes.
    -   The file system is larger than 2 TiB with 512-byte inodes.

    If your application fails with large inode numbers, mount the XFS file system with the `-o inode32`{.literal} option to enforce inode numbers below 2^32^. Using `inode32`{.literal} does not affect inodes that are already allocated with 64-bit numbers.

    Important

    Do *not* use the `inode32`{.literal} option unless a specific environment requires it. The `inode32`{.literal} option changes allocation behavior. As a consequence, the `ENOSPC`{.literal} error might occur if no space is available to allocate inodes in the lower disk blocks.

**Additional resources**

-   [Configurable error handling in XFS](#configurable-error-handling-in-xfs "14.1. Configurable error handling in XFS")

### [1.6. Choosing a local file system](#choosing-a-local-file-system) {#choosing-a-local-file-system .title}

To choose a file system that meets your application requirements, you must understand the target system on which you deploy the file system. In general, use XFS unless you have a specific use case for ext4.

XFS
:   For large-scale deployments, use XFS, particularly when handling large files (hundreds of megabytes) and high I/O concurrency. XFS performs optimally in environments with high bandwidth (greater than 200MB/s) and more than 1000 Input/Output Operations Per Second (IOPS). However, it consumes more CPU resources for metadata operations compared to ext4 and does not support file system shrinking.

ext4
:   For smaller systems or environments with limited I/O bandwidth, ext4 might be a better fit. It performs better in single-threaded, lower I/O workloads and environments with lower throughput requirements. ext4 also supports offline shrinking, which can be beneficial if resizing the file system is a requirement.

Benchmark your application's performance on your target server and storage system to ensure the selected file system meets your performance and scalability requirements.

+------------------------------------------+---------------------------+
| Scenario                                 | Recommended file system   |
+:=========================================+:==========================+
| No special use case                      | XFS                       |
+------------------------------------------+---------------------------+
| Large server                             | XFS                       |
+------------------------------------------+---------------------------+
| Large storage devices                    | XFS                       |
+------------------------------------------+---------------------------+
| Large files                              | XFS                       |
+------------------------------------------+---------------------------+
| Multi-threaded I/O                       | XFS                       |
+------------------------------------------+---------------------------+
| Single-threaded I/O                      | XFS, ext4                 |
+------------------------------------------+---------------------------+
| Limited I/O capability (under 1000 IOPS) | XFS, ext4                 |
+------------------------------------------+---------------------------+
| Limited bandwidth (under 200MB/s)        | XFS, ext4                 |
+------------------------------------------+---------------------------+
| CPU-bound workload                       | XFS, ext4                 |
+------------------------------------------+---------------------------+
| Support for offline shrinking            | XFS, ext4                 |
+------------------------------------------+---------------------------+

: Table 1.2. Summary of suitable use cases for file systems

Show more

### [1.7. Network file systems](#network-file-systems) {#network-file-systems .title}

Network file systems, also referred to as client/server file systems, provide client systems with access to files that are stored on a shared server. This makes it possible for multiple users on multiple systems to share files and storage resources.

Such file systems are built from one or more servers that export a set of file systems to one or more clients. The client nodes do not have access to the underlying block storage. Instead, they interact with the storage by using a protocol that allows for better access control.

Available network file systems

:   -   The most common client/server file system for RHEL customers is the Network File Systems (NFS). RHEL provides both an NFS server component to export a local file system over the network and an NFS client to import these file systems.
    -   RHEL also includes a Common Internet File System (CIFS) client. This supports the popular Microsoft Server Message Block (SMB) file servers for Windows interoperability. The userspace Samba server provides Windows clients with a Microsoft SMB service from a RHEL server.

### [1.8. Shared storage file systems](#shared-storage-file-systems) {#shared-storage-file-systems .title}

Shared storage file systems, sometimes known as cluster file systems, give each server in the cluster direct access to a shared block device. They use a local storage area network (SAN).

Comparison with network file systems
:   Like client/server file systems, shared storage file systems work on a set of servers that are all members of a cluster. Unlike NFS, however, no single server provides access to data or metadata to other members. Each member of the cluster has direct access to the same storage device (the *shared storage*). All cluster member nodes access the same set of files.

Concurrency

:   Cache coherency is key in a clustered file system to ensure data consistency and integrity. There must be a single version of all files in a cluster visible to all nodes within a cluster. The file system must prevent cluster members from updating the same storage block simultaneously and causing data corruption. In order to do that, shared storage file systems use a cluster-wide locking mechanism. This controls access to the storage as a method to prevent conflicts.

    For example, before creating a new file or writing to a file opened on multiple servers, the file system component must obtain the correct lock.

    The requirement of cluster file systems is to provide a highly available service like an Apache web server. Any member of the cluster can see a fully coherent view of the data stored in their shared disk file system. All updates are arbitrated correctly by the locking mechanisms.

Performance characteristics

:   Shared disk file systems do not always perform as well as local file systems running on the same system. This is due to the computational cost of the locking overhead. Shared disk file systems perform well with certain workloads where each node writes almost exclusively to its own set of files. These files are not shared with other nodes.

    Alternatively, a set of files may be shared across nodes in an almost exclusively read-only manner. This results in a minimum of cross-node cache invalidation and can maximize performance.

    Configuring a shared disk file system is complex. Tuning an application to perform well on a shared disk file system can be challenging.

### [1.9. Choosing between network and shared storage file systems](#choosing-between-network-and-shared-storage-file-systems) {#choosing-between-network-and-shared-storage-file-systems .title}

Choose between network and shared storage file systems based on availability, performance, and maintenance needs. Network file systems suit most situations, while shared storage file systems best serve high-availability, minimal-downtime requirements.

When choosing between network and shared storage file systems, consider the following points:

-   NFS-based network file systems are an extremely common and popular choice for environments that provide NFS servers.
-   Network file systems can be deployed by using very high-performance networking technologies like Infiniband or 10 Gigabit Ethernet. This means that you should not turn to shared storage file systems just to get raw bandwidth to your storage. If the speed of access is of prime importance, then use NFS to export a local file system like XFS.
-   Shared storage file systems are not easy to set up or to maintain. Deploy them only when you cannot provide your required availability with either local or network file systems.
-   A shared storage file system in a clustered environment helps reduce downtime. It eliminates unmounting and mounting steps during typical fail-over scenarios involving high-availability service relocation.

Use network file systems unless you have a specific use case for shared storage file systems. Use shared storage file systems primarily for deployments requiring high-availability services with minimum downtime and stringent service-level requirements.

### [1.10. Volume-managing file systems](#volume-managing-file-systems) {#volume-managing-file-systems .title}

Volume-managing file systems integrate the entire storage stack for the purposes of simplicity and improvements within the storage layers.

Available volume-managing file systems

:   -   Red Hat Enterprise Linux 10 provides the Stratis volume manager. Stratis uses XFS for the file system layer and integrates it with Logical Volume Manager (LVM), Device Mapper, and other components.

    Stratis was first released in Red Hat Enterprise Linux 8.0. It is conceived to fill the gap created when Red Hat deprecated Btrfs. Stratis 1.0 is an intuitive, command line-based volume manager. It can perform significant storage management operations while hiding the complexity from the user:

    -   Volume management
    -   Pool creation
    -   Thin storage pools
    -   Snapshots
    -   Automated read cache

    Stratis offers powerful features, but currently lacks certain capabilities of other offerings that it might be compared to, such as Btrfs or ZFS. Most notably, it does not support checksums that can automatically fix errors.

## [Chapter 2. Managing local storage by using RHEL system roles](#managing-local-storage-by-using-rhel-system-roles) {#chapter-2.-managing-local-storage-by-using-rhel-system-roles .title}

To manage Logical Volume Manager (LVM) and local file systems (FS) by using Ansible, you can use the `storage`{.literal} role.

By using the `storage`{.literal} role, you can automate the administration of file systems on disks and logical volumes on multiple machines.

### [2.1. Creating an XFS file system on a block device by using the storage RHEL system role](#creating-an-xfs-file-system-on-a-block-device-by-using-the-storage-rhel-system-role) {#creating-an-xfs-file-system-on-a-block-device-by-using-the-storage-rhel-system-role .title}

You can use the `storage`{.literal} RHEL system role to automate the creation of an XFS file system on block devices.

Note

The `storage`{.literal} role can create a file system only on an unpartitioned, whole disk or a logical volume (LV). It cannot create the file system on a partition.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        - name: Create an XFS file system on a block device
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_volumes:
              - name: barefs
                type: disk
                disks:
                  - sdb
                fs_type: xfs
    ```

    The settings specified in the example playbook include the following:

    `name: barefs`{.literal}
    :   The volume name (*`barefs`{.literal}* in the example) is currently arbitrary. The `storage`{.literal} role identifies the volume by the disk device listed under the `disks`{.literal} attribute.

    `fs_type: `{.literal}*`<file_system>`{.literal}*
    :   You can omit the `fs_type`{.literal} parameter if you want to use the default file system XFS.

    `disks: `{.literal}*`<list_of_disks_and_volumes>`{.literal}*
    :   A YAML list of disk and LV names.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

### [2.2. Persistently mounting a file system by using the storage RHEL system role](#persistently-mounting-a-file-system-by-using-the-storage-rhel-system-role) {#persistently-mounting-a-file-system-by-using-the-storage-rhel-system-role .title}

You can use the `storage`{.literal} RHEL system role to persistently mount file systems to ensure they remain available across system reboots and are automatically mounted on startup. If the file system on the device you specified in the playbook does not exist, the role creates it.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        - name: Persistently mount a file system
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_safe_mode: false

            storage_volumes:
              - name: barefs
                type: disk
                disks:
                  - sdb
                fs_type: xfs
                mount_point: /mnt/data
                mount_user: somebody
                mount_group: somegroup
                mount_mode: "0755"
    ```

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

### [2.3. Creating or resizing a logical volume by using the storage RHEL system role](#creating-or-resizing-a-logical-volume-by-using-the-storage-rhel-system-role) {#creating-or-resizing-a-logical-volume-by-using-the-storage-rhel-system-role .title}

You can use the `storage`{.literal} RHEL system role to create and resize Logical Volume Manager (LVM) logical volumes. The role automatically creates volume groups if they do not exist.

Use the `storage`{.literal} role to perform the following tasks:

-   To create an LVM logical volume in a volume group consisting of many disks
-   To resize an existing file system on LVM
-   To express an LVM volume size in percentage of the pool's total size

If the volume group does not exist, the role creates it. If a logical volume exists in the volume group, it is resized if the size does not match what is specified in the playbook.

If you are reducing a logical volume, to prevent data loss you must ensure that the file system on that logical volume is not using the space in the logical volume that is being reduced.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        - name: Create logical volume
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_safe_mode: false

            storage_pools:
              - name: myvg
                disks:
                  - sda
                  - sdb
                  - sdc
                volumes:
                  - name: mylv
                    size: 2G
                    fs_type: ext4
                    mount_point: /mnt/data
    ```

    The settings specified in the example playbook include the following:

    `size: `{.literal}*`<size>`{.literal}*
    :   You must specify the size by using units (for example, GiB) or percentage (for example, 60%).

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

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

-   Verify that specified volume has been created or resized to the requested size:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'lvs myvg'
    ```

### [2.4. Enabling online block discard by using the storage RHEL system role](#enabling-online-block-discard-by-using-the-storage-rhel-system-role) {#enabling-online-block-discard-by-using-the-storage-rhel-system-role .title}

You can mount an XFS file system with the online block discard option to automatically discard unused blocks.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        - name: Enable online block discard
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_volumes:
              - name: barefs
                type: disk
                disks:
                  - /dev/sdb
                fs_type: xfs
                mount_point: /mnt/data
                mount_options: discard
    ```

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

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

-   Verify that online block discard option is enabled:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'findmnt /mnt/data'
    ```

### [2.5. Creating and mounting a file system by using the storage RHEL system role](#creating-and-mounting-a-file-system-by-using-the-storage-rhel-system-role) {#creating-and-mounting-a-file-system-by-using-the-storage-rhel-system-role .title}

You can use the `storage`{.literal} RHEL system role to create and mount file systems that persist across reboots. The role automatically adds entries to `/etc/fstab`{.literal} to ensure persistent mounting.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        -name: Create and mount a file system
        ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
        vars:
          storage_safe_mode: false

          storage_volumes:
            - name: barefs
              type: disk
              disks:
                - sdb
              fs_type: ext4
              fs_label: label-name
              mount_point: /mnt/data
    ```

    The settings specified in the example playbook include the following:

    `disks: `{.literal}*`<list_of_devices>`{.literal}*
    :   A YAML list of device names that the role uses when it creates the volume.

    `fs_type: `{.literal}*`<file_system>`{.literal}*
    :   Specifies the file system the role sets on the volume. You can select `xfs`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `swap`{.literal}, or `unformatted`{.literal}.

    `label-name: `{.literal}*`<file_system_label>`{.literal}*
    :   Optional: sets the label of the file system.

    `mount_point: `{.literal}*`<directory>`{.literal}*
    :   Optional: if the volume is intended for automatic mounting, set the `mount_point`{.literal} variable to the directory to which the volume mounts.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

### [2.6. Configuring a RAID volume by using the storage RHEL system role](#configuring-a-raid-volume-by-using-the-storage-rhel-system-role) {#configuring-a-raid-volume-by-using-the-storage-rhel-system-role .title}

With the `storage`{.literal} system role, you can configure a RAID volume on RHEL by using Red Hat Ansible Automation Platform and Ansible-Core. Create an Ansible Playbook with the parameters to configure a RAID volume to suit your requirements.

Warning

Device names might change in certain circumstances, for example, when you add a new disk to a system. Therefore, to prevent data loss, use persistent naming attributes in the playbook. For more information about persistent naming attributes, see [Persistent naming attributes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_storage_devices/persistent-naming-attributes).

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        - name: Create a RAID on sdd, sde, sdf, and sdg
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_safe_mode: false
            storage_volumes:
              - name: data
                type: raid
                disks: [sdd, sde, sdf, sdg]
                raid_level: raid0
                raid_chunk_size: 32 KiB
                mount_point: /mnt/data
                state: present
    ```

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

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

-   Verify that the array was correctly created:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'mdadm --detail /dev/md/data'
    ```

### [2.7. Configuring an LVM volume group on RAID by using the storage RHEL system role](#configuring-an-lvm-volume-group-on-raid-by-using-the-storage-rhel-system-role) {#configuring-an-lvm-volume-group-on-raid-by-using-the-storage-rhel-system-role .title}

You can use the `storage`{.literal} RHEL system role to configure LVM volume groups on RAID arrays.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure LVM pool with RAID
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_safe_mode: false
            storage_pools:
              - name: my_pool
                type: lvm
                disks: [sdh, sdi]
                raid_level: raid1
                volumes:
                  - name: my_volume
                    size: "1 GiB"
                    mount_point: "/mnt/app/shared"
                    fs_type: xfs
                    state: present
    ```

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

    Note

    Setting `raid_level`{.literal} at the `storage_pool`{.literal} level creates an MD RAID array first, and then builds an LVM volume group on top of it.

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

-   Verify that your pool is on RAID:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'lsblk'
    ```

**Additional resources**

-   [Managing RAID](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_storage_devices/managing-raid)

### [2.8. Configuring a stripe size for RAID LVM volumes by using the storage RHEL system role](#configuring-a-stripe-size-for-raid-lvm-volumes-by-using-the-storage-rhel-system-role) {#configuring-a-stripe-size-for-raid-lvm-volumes-by-using-the-storage-rhel-system-role .title}

You can use the `storage`{.literal} RHEL system role to configure stripe sizes for RAID LVM volumes.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        - name: Configure stripe size for RAID LVM volumes
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_safe_mode: false
            storage_pools:
              - name: my_pool
                type: lvm
                disks: [sdh, sdi]
                volumes:
                  - name: my_volume
                    size: "1 GiB"
                    mount_point: "/mnt/app/shared"
                    fs_type: xfs
                    raid_level: raid0
                    raid_stripe_size: "256 KiB"
                    state: present
    ```

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

    Note

    Setting `raid_level`{.literal} at the `volumes`{.literal} level creates LVM RAID logical volumes.

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

-   Verify that stripe size is set to the required size:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'lvs -o+stripesize /dev/my_pool/my_volume'
    ```

**Additional resources**

-   [Managing RAID](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_storage_devices/managing-raid)

### [2.9. Configuring an LVM-VDO volume by using the storage RHEL system role](#configuring-an-lvm-vdo-volume-by-using-the-storage-rhel-system-role) {#configuring-an-lvm-vdo-volume-by-using-the-storage-rhel-system-role .title}

You can use the `storage`{.literal} RHEL system role to create a VDO volume on LVM (LVM-VDO) with enabled compression and deduplication.

Note

Because of the `storage`{.literal} system role use of LVM-VDO, only one volume can be created per pool.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        - name: Create LVM-VDO volume under volume group 'myvg'
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_pools:
              - name: myvg
                disks:
                  - /dev/sdb
                volumes:
                  - name: mylv1
                    compression: true
                    deduplication: true
                    vdo_pool_size: 10 GiB
                    size: 30 GiB
                    mount_point: /mnt/app/shared
    ```

    The settings specified in the example playbook include the following:

    `vdo_pool_size: `{.literal}*`<size>`{.literal}*
    :   The actual size that the volume takes on the device. You can specify the size in human-readable format, such as 10 GiB. If you do not specify a unit, it defaults to bytes.

    `size: `{.literal}*`<size>`{.literal}*
    :   The virtual size of VDO volume.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

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

-   View the current status of compression and deduplication:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m command -a 'lvs -o+vdo_compression,vdo_compression_state,vdo_deduplication,vdo_index_state'
    ```

    ``` {.language-plaintext tabindex="-1"}
      LV       VG      Attr       LSize   Pool   Origin Data%  Meta%  Move Log Cpy%Sync Convert VDOCompression VDOCompressionState VDODeduplication VDOIndexState
      mylv1   myvg   vwi-a-v---   3.00t vpool0                                                         enabled              online          enabled        online
    ```

### [2.10. Creating a LUKS2 encrypted volume by using the storage RHEL system role](#creating-a-luks2-encrypted-volume-by-using-the-storage-rhel-system-role) {#creating-a-luks2-encrypted-volume-by-using-the-storage-rhel-system-role .title}

You can use the `storage`{.literal} role to create and configure a volume encrypted with LUKS by running an Ansible Playbook.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.

**Procedure**

1.  Store your sensitive variables in an encrypted file:

    a.  Create the vault:

        ``` {.language-plaintext tabindex="-1"}
        $ ansible-vault create ~/vault.yml
        ```

        ``` {.language-plaintext tabindex="-1"}
        New Vault password: <vault_password>
        Confirm New Vault password: <vault_password>
        ```

    b.  After the `ansible-vault create`{.literal} command opens an editor, enter the sensitive data in the *`<key>`{.literal}*`: `{.literal}*`<value>`{.literal}* format:

        ``` {.language-plaintext tabindex="-1"}
        luks_password: <password>
        ```

    c.  Save the changes, and close the editor. Ansible encrypts the data in the vault.

2.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      vars_files:
        - ~/vault.yml
      tasks:
        - name: Create and configure a volume encrypted with LUKS
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_volumes:
              - name: barefs
                type: disk
                disks:
                  - sdb
                fs_type: xfs
                fs_label: <label>
                mount_point: /mnt/data
                encryption: true
                encryption_password: "{{ luks_password }}"
                encryption_cipher: <cipher>
                encryption_key_size: <key_size>
                encryption_luks_version: luks2
    ```

    The settings specified in the example playbook include the following:

    `encryption_cipher: `{.literal}*`<cipher>`{.literal}*
    :   Specifies the LUKS cipher. Possible values are: `twofish-xts-plain64`{.literal}, `serpent-xts-plain64`{.literal}, and `aes-xts-plain64`{.literal} (default).

    `encryption_key_size: `{.literal}*`<key_size>`{.literal}*
    :   Specifies the LUKS key size. The default is `512`{.literal} bit.

    `encryption_luks_version: luks2`{.literal}
    :   Specifies the LUKS version. The default is `luks2`{.literal}.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

3.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --ask-vault-pass --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

4.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --ask-vault-pass ~/playbook.yml
    ```

**Verification**

-   Verify the created LUKS encrypted volume:

    ``` {.language-plaintext tabindex="-1"}
    # ansible managed-node-01.example.com -m command -a 'cryptsetup luksDump /dev/sdb'
    ```

    ``` {.language-plaintext tabindex="-1"}
    LUKS header information
    Version: 2
    Epoch: 3
    Metadata area: 16384 [bytes]
    Keyslots area: 16744448 [bytes]
    UUID: bdf6463f-6b3f-4e55-a0a6-1a66f0152a46
    Label: (no label)
    Subsystem: (no subsystem)
    Flags: (no flags)

    Data segments:
    0: crypt
    offset: 16777216 [bytes]
    length: (whole device)
    cipher: aes-cbc-essiv:sha256
    sector: 512 [bytes]

    Keyslots:
    0: luks2
    Key: 256 bits
    Priority: normal
    Cipher: aes-cbc-essiv:sha256
    Cipher key: 256 bits
    ```

**Additional resources**

-   [Encrypting block devices by using LUKS](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_storage_devices/encrypting-block-devices-by-using-luks)
-   [Ansible vault](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/ansible-vault)

### [2.11. Creating shared LVM devices by using the storage RHEL system role](#creating-shared-lvm-devices-using-the-storage-rhel-system-role) {#creating-shared-lvm-devices-by-using-the-storage-rhel-system-role .title}

You can use the `storage`{.literal} RHEL system role to create shared LVM devices if you want your multiple systems to access the same storage at the same time.

Shared LVM devices provide the following notable benefits:

-   Resource sharing
-   Flexibility in managing storage resources
-   Simplification of storage management tasks

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   `lvmlockd`{.literal} is configured on the managed node. For more information, see [Configuring LVM to share SAN disks among multiple machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_logical_volumes/configuring-lvm-on-shared-storage#configuring-lvm-on-san-multiple).
-   You have a working cluster environment with shared storage and the storage RHEL system role enabled on each node.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      become: true
      tasks:
        - name: Create shared LVM device
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_pools:
              - name: vg1
                disks: /dev/vdb
                type: lvm
                shared: true
                state: present
                volumes:
                  - name: lv1
                    size: 4g
                    mount_point: /opt/test1
                    fs_type: gfs2
            storage_safe_mode: false
            storage_use_partitions: true
    ```

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook ~/playbook.yml
    ```

### [2.12. Resizing physical volumes by using the storage RHEL system role](#resizing-physical-volumes-by-using-the-storage-rhel-system-role) {#resizing-physical-volumes-by-using-the-storage-rhel-system-role .title}

With the `storage`{.literal} system role, you can resize Logical Volume Manager (LVM) physical volumes after resizing the underlying storage or disks from outside of the host. For example, you increased the size of a virtual disk and want to use the extra space in an existing LVM.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   The size of the underlying block storage has been changed.

**Procedure**

1.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      tasks:
        - name: Resize LVM PV size
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_pools:
               - name: myvg
                 disks: ["sdf"]
                 type: lvm
                 grow_to_fill: true
    ```

    The settings specified in the example playbook include the following:

    `grow_to_fill`{.literal}

    :   `true`{.literal} The role automatically expands the storage volume to use any new capacity on the disk.

        `false`{.literal} The role leaves the storage volume at its current size, even if the underlying disk has grown.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

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

1.  Verify the `grow_to_fill`{.literal} setting works as expected. Prepare a test PV and VG:

    ``` {.language-plaintext tabindex="-1"}
    # pvcreate /dev/sdf
    ```

    ``` {.language-plaintext tabindex="-1"}
    # vgcreate myvg /dev/sdf
    ```

2.  Check and record the initial physical volume size:

    ``` {.language-plaintext tabindex="-1"}
    # pvs
    ```

3.  Edit the playbook to set `grow_to_fill: false`{.literal} and run the playbook.

4.  Check the volume size and verify that it remained unchanged.

5.  Edit the playbook to set `grow_to_fill: true`{.literal} and re-run the playbook.

6.  Check the volume size and verify that it has expanded.

### [2.13. Additional resources](#managing-local-storage-by-using-rhel-system-roles_213-additional-resources) {#additional-resources .title}

-   [Introduction to RHEL system roles](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/introduction-to-rhel-system-roles)

## [Chapter 3. Managing partitions by using the web console](#managing-partitions-using-the-web-console) {#chapter-3.-managing-partitions-by-using-the-web-console .title}

Manage disk partitions by using the web console to view formatted partitions, create new partitions, and delete existing partitions.

### [3.1. Displaying partitions formatted with file systems in the web console](#displaying-partitions-formatted-with-file-systems-in-the-web-console) {#displaying-partitions-formatted-with-file-systems-in-the-web-console .title}

The **Storage** section in the web console displays all available file systems in the **Filesystems** table. In addition to the list of partitions formatted with file systems, you can also use the page for creating a new storage.

**Prerequisites**

-   The `cockpit-storaged`{.literal} package is installed on your system.

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click the **Storage** tab.

    In the **Storage** table, you can see all available partitions formatted with file systems, their IDs, types, locations, sizes, and how much space is available on each partition.

    You can also use the drop-down menu in the upper-right corner to create new local or networked storage.

### [3.2. Creating partitions in the web console](#creating-partitions-in-the-web-console) {#creating-partitions-in-the-web-console .title}

Use the RHEL web console to create disk partitions with custom file systems, mount points, and optional encryption. You can initialize a partition table on an unformatted disk and create partitions with XFS or ext4 file systems.

**Prerequisites**

-   The `cockpit-storaged`{.literal} package is installed on your system.

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   An unformatted volume connected to the system is visible in the **Storage** table of the **Storage** tab.

**Procedure**

1.  Log in to the RHEL 10 web console and click the **Storage** tab.

2.  In the **Storage** table, click the device which you want to partition to open the page and options for that device.

3.  On the device page, click the menu button, ⋮, and select **Create partition table**.

4.  In the **Initialize disk** dialog box, select the following:

    a.  **Partitioning**:

        -   Compatible with all systems and devices (MBR)
        -   Compatible with modern system and hard disks \> 2TB (GPT)
        -   No partitioning

    b.  **Overwrite**:

        -   Select the **Overwrite existing data with zeros** checkbox if you want the RHEL web console to rewrite the whole disk with zeros. This option is slower because the program has to go through the whole disk, but it is more secure. Use this option if the disk includes any data and you need to overwrite it.

            If you do not select the **Overwrite existing data with zeros** checkbox, the RHEL web console rewrites only the disk header. This increases the speed of formatting.

5.  Click Initialize.

6.  Click the menu button, ⋮, next to the partition table you created. It is named **Free space** by default.

7.  Click Create partition.

8.  In the **Create partition** dialog box, enter a **Name** for the file system.

9.  Add a **Mount point**.

10. In the **Type** drop-down menu, select a file system:

    -   **XFS** file system supports large logical volumes, switching physical drives online without outage, and growing an existing file system. Leave this file system selected if you do not have a different strong preference.

    -   **ext4** file system supports:

        -   Logical volumes
        -   Switching physical drives online without outage
        -   Growing a file system
        -   Shrinking a file system

    Additional option is to enable encryption of partition done by LUKS (Linux Unified Key Setup). You can encrypt the volume with a passphrase.

11. Enter the **Size** of the volume you want to create.

12. Select the **Overwrite existing data with zeros** checkbox if you want the RHEL web console to rewrite the whole disk with zeros. This option is slower because the program has to go through the whole disk, but it is more secure. Use this option if the disk includes any data and you need to overwrite it.

    If you do not select the **Overwrite existing data with zeros** checkbox, the RHEL web console rewrites only the disk header. This increases the speed of formatting.

13. If you want to encrypt the volume, select the type of encryption in the **Encryption** drop-down menu.

    If you do not want to encrypt the volume, select **No encryption**.

14. In the **At boot** drop-down menu, select when you want to mount the volume.

15. In **Mount options** section:

    a.  Select the **Mount read only** checkbox if you want to mount the volume as a read-only logical volume.
    b.  Select the **Custom mount options** checkbox and add the mount options if you want to change the default mount option.

16. Create the partition:

    -   If you want to create and mount the partition, click the Create and mount button.

    -   If you want to only create the partition, click the Create only button.

        Formatting can take several minutes depending on the volume size and which formatting options are selected.

**Verification**

-   To verify that the partition has been successfully added, switch to the **Storage** tab and check the **Storage** table and verify whether the new partition is listed.

### [3.3. Deleting partitions in the web console](#deleting-partitions-in-the-web-console) {#deleting-partitions-in-the-web-console .title}

You can remove partitions in the web console interface.

**Prerequisites**

-   The `cockpit-storaged`{.literal} package is installed on your system.

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click the **Storage** tab.

3.  Click the device from which you want to delete a partition.

4.  On the device page and in the **GPT partitions** section, click the menu button, ⋮ next to the partition you want to delete.

5.  From the drop-down menu, select Delete.

    The RHEL web console terminates all processes that are currently using the partition and unmount the partition before deleting it.

**Verification**

-   To verify that the partition has been successfully removed, switch to the **Storage** tab and check the **Storage** table.

## [Chapter 4. Mounting NFS shares](#mounting-nfs-shares) {#chapter-4.-mounting-nfs-shares .title}

As a system administrator, you can mount remote NFS shares on your system to access shared data.

### [4.1. Services required on an NFS client](#services-required-on-an-nfs-client) {#services-required-on-an-nfs-client .title}

Principal services used by Network File System (NFS) clients include kernel modules and user-space processes that provide access to NFS file shares. These services also include details on their functions and configuration.

Install the `nfs-utils`{.literal} package to enable NFS client functionality. Principal services used by the NFS client include the following:

+--------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Service name                         | NFS version | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+:=====================================+:============+:=====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `nfsidmap`{.literal}                 | 4           | A program that services upcalls from the NFSv4 client mapping between NFSv4 names (strings in the form of *`<user@domain>`{.literal}*) and local user and group IDs. It provides similar functionality that `rpc.idmapd`{.literal} provides on behalf of the NFSv4 server. The difference is that while `rpc.idmapd`{.literal} is a daemon, `nfsidmap`{.literal} is invoked on-demand by using the kernel request-key mechanism. `nfsidmap`{.literal} uses two configuration files: `/etc/idmapd.conf`{.literal} and `/etc/request-key.d/id_resolver.conf`{.literal}. In most cases the defaults are sufficient and it is unnecessary to modify either of these configuration files. |
+--------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc.statd`{.literal}                | 3           | A daemon that implements the Network Status Monitor protocol. The two main functions of `rpc.statd`{.literal}:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                      |             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                      |             | -   Listen for requests from the local `lockd`{.literal} process (the kernel daemon that implements the Network Lock Manager protocol) to monitor network peers (in the case of an NFS client, `rpc.statd`{.literal} is monitoring the NFS server).                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                      |             | -   Listen for reboot notifications from remote peers (NFS servers that have rebooted) which it then forwards to `lockd`{.literal} so it can reclaim any locks it had from those servers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                      |             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                      |             | Use the `[statd]`{.literal} section in the `/etc/nfs.conf`{.literal} file to configure `rpc.statd`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc-statd.service`{.literal}        | 3           | A `systemd`{.literal} unit file that starts the `rpc.statd`{.literal} daemon. Note that it is not necessary to enable or start the service manually, because the `mount.nfs`{.literal} program automatically starts `rpc-statd.service`{.literal} (by using the `/usr/sbin/start-statd`{.literal} shell script) the first time it mounts a remote file system by using NFSv3. However, if configuring the NFSv3 client to run behind a firewall, it is typically necessary to restart the `rpc-statd.service`{.literal}.                                                                                                                                                             |
+--------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sm-notify`{.literal}                | 3           | A helper program that sends reboot notifications to remote peers that were monitored by `rpc.statd`{.literal} whenever the local system reboots. In the case of an NFS client, `sm-notify`{.literal} is sending reboot notifications to NFS servers so that those servers can drop any locks that were held by the client.                                                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc-statd-notify.service`{.literal} | 3           | A `systemd`{.literal} unit that triggers `sm-notify`{.literal}. It runs automatically at system boot, so it is not necessary to manually enable or start the service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+--------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc.gssd`{.literal}                 | 3, 4        | A daemon that acts on behalf of the kernel to establish a Generic Security Services (GSS) context with a remote peer (typically initiated from the NFS client to the NFS server, but also initiated from the NFS server to the NFS client in the case of NFSv4 callbacks). This process is necessary for securing NFS by using Kerberos V5. The `rpc.gssd`{.literal} program is configured by using the `[gssd]`{.literal} section in the `/etc/nfs.conf`{.literal} file.                                                                                                                                                                                                            |
+--------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `rpc-gssd.service`{.literal}         | 3, 4        | A `systemd`{.literal} unit file that starts the `rpc.gssd`{.literal} daemon. It is not necessary to manually enable or start this service, because the service automatically starts on system boot if the `/etc/krb5.keytab`{.literal} file is present on the system.                                                                                                                                                                                                                                                                                                                                                                                                                |
+--------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.1. Services required on an NFS client

Show more

### [4.2. Preparing an NFSv3 client to run behind a firewall](#preparing-an-nfsv3-client-to-run-behind-a-firewall) {#preparing-an-nfsv3-client-to-run-behind-a-firewall .title}

An NFS server notifies clients about file locks and the server status. To establish a connection back to the client, you must open the relevant ports in the firewall on the client.

**Procedure**

1.  By default, NFSv3 RPC services use random ports. To enable a firewall configuration, configure fixed port numbers in the `/etc/nfs.conf`{.literal} file:

    a.  In the `[lockd]`{.literal} section, set a fixed port number for the `nlockmgr`{.literal} RPC service, for example:

        ``` {.language-plaintext tabindex="-1"}
        port=5555
        ```

        With this setting, the service automatically uses this port number for both the UDP and TCP protocol.

    b.  In the `[statd]`{.literal} section, set a fixed port number for the `rpc.statd`{.literal} service, for example:

        ``` {.language-plaintext tabindex="-1"}
        port=6666
        ```

        With this setting, the service automatically uses this port number for both the UDP and TCP protocol.

2.  Open the relevant ports in `firewalld`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=rpc-bind
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port={5555/tcp,5555/udp,6666/tcp,6666/udp}
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

3.  Restart the `rpc-statd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart rpc-statd nfs-server
    ```

### [4.3. Preparing an NFSv4 client to run behind a firewall](#preparing-an-nfsv4-0-client-to-run-behind-a-firewall) {#preparing-an-nfsv4-client-to-run-behind-a-firewall .title}

An NFS server notifies clients about file locks and the server status. To establish a connection back to the client, you must open the relevant ports in the firewall on the client.

Note

NFS v4.1 and later uses the pre-existing client port for callbacks, so the callback port cannot be set separately. For more information, see the [How do I set the NFS4 client callback port to a specific port?](https://access.redhat.com/solutions/2616771) solution.

**Prerequisites**

-   The server uses the NFS 4 protocol.

**Procedure**

-   Open the relevant ports in `firewalld`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-port=<callback_port>/tcp
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

### [4.4. Manually mounting an NFS share](#manually-mounting-an-nfs-share) {#manually-mounting-an-nfs-share .title}

If you do not require that a NFS share is automatically mounted at boot time, you can manually mount it.

Warning

You can experience conflicts in your NFSv4 `clientid`{.literal} and their sudden expiration if your NFS clients have the same short hostname. To avoid any possible sudden expiration of your NFSv4 `clientid`{.literal}, you must use either unique hostnames for NFS clients or configure identifier on each container, depending on what system you are using. For more information, see the Red Hat Knowledgebase solution [NFSv4 clientid was expired suddenly due to use same hostname on several NFS clients](https://access.redhat.com/solutions/6395261).

**Procedure**

-   Use the following command to mount an NFS share on a client:

    ``` {.language-plaintext tabindex="-1"}
    # mount <nfs_server_ip_or_hostname>:/<exported_share> <mount point>
    ```

    For example, to mount the `/nfs/projects`{.literal} share from the `server.example.com`{.literal} NFS server to `/mnt`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    # mount server.example.com:/nfs/projects/ /mnt/
    ```

**Verification**

-   As a user who has permissions to access the NFS share, display the content of the mounted share:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -l /mnt/
    ```

### [4.5. Mounting an NFS share automatically when the system boots](#mounting-an-nfs-share-automatically-when-the-system-boots) {#mounting-an-nfs-share-automatically-when-the-system-boots .title}

Automatic mounting of an NFS share during system boot ensures that critical services reliant on centralized data, such as `/home`{.literal} directories hosted on the NFS server, have seamless and uninterrupted access from the moment the system starts up.

**Procedure**

1.  Edit the `/etc/fstab`{.literal} file and add a line for the share that you want to mount:

    ``` {.language-plaintext tabindex="-1"}
    <nfs_server_ip_or_hostname>:/<exported_share>     <mount point>    nfs    default   0 0
    ```

    For example, to mount the `/nfs/projects`{.literal} share from the `server.example.com`{.literal} NFS server to `/home`{.literal}, enter:

    ``` {.language-plaintext tabindex="-1"}
    server.example.com:/nfs/projects     /home        nfs    defaults        0 0
    ```

2.  Mount the share:

    ``` {.language-plaintext tabindex="-1"}
    # mount /home
    ```

**Verification**

-   As a user who has permissions to access the NFS share, display the content of the mounted share:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -l /home/
    ```

### [4.6. Connecting NFS mounts in the web console](#connecting-nfs-mounts-in-the-web-console) {#connecting-nfs-mounts-in-the-web-console .title}

Mount remote NFS directories by using the web console by specifying server address, remote path, and local mount point with configurable mount options.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   The `cockpit-storaged`{.literal} package is installed on your system.

-   NFS server name or the IP address.

-   Path to the directory on the remote server.

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click **Storage**.

3.  In the **Storage** table, click the menu button.

4.  From the drop-down menu, select **New NFS mount**.

5.  In the **New NFS Mount** dialog box, enter the server or IP address of the remote server.

6.  In the **Path on Server** field, enter the path to the directory that you want to mount.

7.  In the **Local Mount Point** field, enter the path to the directory on your local system where you want to mount the NFS.

8.  In the **Mount options** checkbox list, select how you want to mount the NFS. You can select multiple options depending on your requirements.

    -   Check the **Mount at boot** box if you want the directory to be reachable even after you restart the local system.
    -   Check the **Mount read only** box if you do not want to change the content of the NFS.
    -   Check the **Custom mount options** box and add the mount options if you want to change the default mount option.

9.  Click Add.

**Verification**

-   Open the mounted directory and verify that the content is accessible.

### [4.7. Customizing NFS mount options in the web console](#customizing-nfs-mount-options-in-the-web-console) {#customizing-nfs-mount-options-in-the-web-console .title}

Edit an existing NFS mount and add custom mount options. Custom mount options can help you to troubleshoot the connection or change parameters of the NFS mount. Examples include changing timeout limits or configuring authentication.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   The `cockpit-storaged`{.literal} package is installed on your system.

-   An NFS mount is added to your system.

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click **Storage**.

3.  In the **Storage** table, click the NFS mount you want to adjust.

4.  If the remote directory is mounted, click **Unmount**.

    You must unmount the directory during the custom mount options configuration. Otherwise, the web console does not save the configuration and this causes an error.

5.  Click **Edit**.

6.  In the **NFS Mount** dialog box, select **Custom mount option**.

7.  Enter mount options separated by a comma. For example:

    -   **`nfsvers=4`{.literal}**: The NFS protocol version number
    -   **`soft`{.literal}**: The type of recovery after an NFS request times out
    -   **`sec=krb5`{.literal}**: The files on the NFS server can be secured by Kerberos authentication. Both the NFS client and server have to support Kerberos authentication.

    For a complete list of the NFS mount options, enter `man nfs`{.literal} in the command line.

8.  Click **Apply**.

9.  Click **Mount**.

**Verification**

-   Open the mounted directory and verify that the content is accessible.

### [4.8. Setting up an NFS client with Kerberos in an IdM domain](#setting-up-an-nfs-client-with-kerberos-in-an-idM-domain) {#setting-up-an-nfs-client-with-kerberos-in-an-idm-domain .title}

If the Network File System (NFS) server uses Kerberos and is enrolled in a RHEL Identity Management (IdM) domain, your client must also be a domain member to mount the shares. This enables centralized management of users and groups, and supports Kerberos-based authentication, integrity protection, and traffic encryption.

**Prerequisites**

-   The NFS client is [enrolled](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/installing_identity_management/installing-an-idm-client) in a Red Hat Enterprise Linux Identity Management (IdM) domain.
-   The exported NFS share uses Kerberos.
-   `rpc.gssd`{.literal} services that provide gss security context establishment. For more information, see `rpc.gssd`{.literal}(8) man page on your system.

**Procedure**

1.  Obtain a kerberos ticket as an IdM administrator:

    ``` {.language-plaintext tabindex="-1"}
    # kinit admin
    ```

2.  Retrieve the host principal, and store it in the `/etc/krb5.keytab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # ipa-getkeytab -s idm_server.idm.example.com -p host/nfs_client.idm.example.com -k /etc/krb5.keytab
    ```

    IdM automatically created the `host`{.literal} principal when you joined the host to the IdM domain.

3.  Optional: Display the principals in the `/etc/krb5.keytab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # klist -k /etc/krb5.keytab
    ```

    ``` {.language-plaintext tabindex="-1"}
    Keytab name: FILE:/etc/krb5.keytab
    KVNO Principal
    ---- --------------------------------------------------------------------------
       6 host/nfs_client.idm.example.com@IDM.EXAMPLE.COM
       6 host/nfs_client.idm.example.com@IDM.EXAMPLE.COM
       6 host/nfs_client.idm.example.com@IDM.EXAMPLE.COM
       6 host/nfs_client.idm.example.com@IDM.EXAMPLE.COM
    ```

4.  Use the `ipa-client-automount`{.literal} utility to configure mapping of IdM IDs:

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

5.  Mount an exported NFS share, for example:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o sec=krb5i server.idm.example.com:/nfs/projects/ /mnt/
    ```

    The `-o sec`{.literal} option specifies the Kerberos security method.

**Verification**

1.  Log in as an IdM user who has permissions to write on the mounted share.

2.  Obtain a Kerberos ticket:

    ``` {.language-plaintext tabindex="-1"}
    $ kinit
    ```

3.  Create a file on the share, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ touch /mnt/test.txt
    ```

4.  List the directory to verify that the file was created:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -l /mnt/test.txt
    ```

    ``` {.language-plaintext tabindex="-1"}
    -rw-r--r--. 1 admin users 0 Feb 15 11:54 /mnt/test.txt
    ```

**Additional resources**

-   [The AUTH_GSS authentication method](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/deploying-an-nfs-server#the-auth-gss-authentication-method)

### [4.9. Configuring GNOME to store user settings on home directories hosted on an NFS share](#configuring-gnome-to-store-user-settings-on-home-directories-hosted-on-an-nfs-share) {#configuring-gnome-to-store-user-settings-on-home-directories-hosted-on-an-nfs-share .title}

If you use GNOME on a system with home directories hosted on an NFS server, you must change the `keyfile`{.literal} back end of the `dconf`{.literal} database. Otherwise, `dconf`{.literal} might not work correctly. This change affects all users because it changes how `dconf`{.literal} manages settings stored in home directories.

**Procedure**

1.  Add the following line to the beginning of the `/etc/dconf/profile/user`{.literal} file. If the file does not exist, create it.

    ``` {.language-plaintext tabindex="-1"}
    service-db:keyfile/user
    ```

    With this setting, `dconf`{.literal} polls the `keyfile`{.literal} back end to determine whether updates have been made, so settings might not be updated immediately.

2.  The changes take effect when the users logs out and in.

### [4.10. Configuring an NFS server with TLS support](#configuring-an-nfs-server-with-tls-support) {#configuring-an-nfs-server-with-tls-support .title}

Without the `RPCSEC_GSS`{.literal} protocol, Network File System (NFS) traffic is unencrypted by default. Starting with Red Hat Enterprise Linux 10, it is possible to configure NFS with Transport Layer Security (TLS). This allows NFS traffic to be encrypted by default.

**Prerequisites**

-   You have configured an NFSv4 server. For instructions, see [Configuring an NFSv4-only server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/deploying-an-nfs-server#configuring-an-nfsv4-only-server).
-   You have a Certificate Authority (CA) certificate.
-   You have installed the `ktls-utils`{.literal} package.

**Procedure**

1.  Create a private key and a certificate signing request (CSR):

    ``` {.language-plaintext tabindex="-1"}
    # openssl req -new -newkey rsa:4096 -noenc \
    -keyout /etc/pki/tls/private/server.example.com.key \
    -out /etc/pki/tls/private/server.example.com.csr \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=server.example.com" \
    -addext "subjectAltName=DNS:server.example.com,IP:192.0.2.1"
    ```

    Important

    Common Name (CN) and Domain Name System (DNS) must match the hostname. IP must match IP of the host.

2.  Send the `/etc/pki/tls/private/server.example.com.csr`{.literal} file to a CA and request a server certificate. Store the received CA certificate and the server certificate on the host.

3.  Import the CA certificate to the system's truststore:

    ``` {.language-plaintext tabindex="-1"}
    # cp ca.crt /etc/pki/ca-trust/source/anchors
    ```

    ``` {.language-plaintext tabindex="-1"}
    # update-ca-trust
    ```

4.  Move the server certificate to the `/etc/pki/tls/certs/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mv server.example.com.crt /etc/pki/tls/certs/
    ```

5.  Ensure the SELinux context is correct on the private key and certificates:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /etc/pki/tls/certs/
    ```

6.  Add the server certificate and private key to the `[authenticate.server]`{.literal} section in the `/etc/tlshd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    x509.certificate= /etc/pki/tls/certs/server.example.com.crt
    x509.private_key= /etc/pki/tls/private/server.example.com.key
    ```

    Leave the `x509.truststore`{.literal} parameter unset.

7.  Enable and start the `tlshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now tlshd.service
    ```

**Next steps**

-   [Configuring an NFS client with TLS support](#configuring-an-nfs-client-with-tls-support "4.11. Configuring an NFS client with TLS support")
-   [Configuring an NFS client with mutual TLS support](#configuring-an-nfs-client-with-mutual-tls-support "4.12. Configuring an NFS client with mutual TLS support")

### [4.11. Configuring an NFS client with TLS support](#configuring-an-nfs-client-with-tls-support) {#configuring-an-nfs-client-with-tls-support .title}

If the server supports NFS with TLS, configure the client and mount using `xprtsec=tls`{.literal}. Import the CA certificate, enable the TLS daemon, and mount the share with encryption. TLS helps protect data in transit between client and server.

**Prerequisites**

-   You have configured the NFS server with TLS encryption. For details, see [Configuring an NFS server with TLS support](#configuring-an-nfs-server-with-tls-support "4.10. Configuring an NFS server with TLS support").
-   You have installed the `ktls-utils`{.literal} package.

**Procedure**

1.  Import the Certificate Authority (CA) certificate to the system's truststore:

    ``` {.language-plaintext tabindex="-1"}
    # cp ca.crt /etc/pki/ca-trust/source/anchors
    ```

    ``` {.language-plaintext tabindex="-1"}
    # update-ca-trust
    ```

2.  Enable and start the `tlshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now tlshd.service
    ```

3.  Mount an NFS share by using TLS encryption:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o xprtsec=tls server.example.com:/nfs/projects/ /mnt/
    ```

**Verification**

-   Verify that the client successfully mounted NFS share with TLS support:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u tlshd
    ```

    ``` {.language-plaintext tabindex="-1"}
    …
    Apr 01 08:37:56 client.example.com tlshd[10688]: Handshake with server.example.com (192.0.2.1) was successful
    ```

### [4.12. Configuring an NFS client with mutual TLS support](#configuring-an-nfs-client-with-mutual-tls-support) {#configuring-an-nfs-client-with-mutual-tls-support .title}

If the server supports NFS with TLS encryption, configure both the server and client. TLS provides mutual authentication between systems. Configuration includes certificates, TLS daemon setup, and encrypted NFS mounts.

**Prerequisites**

-   You have configured the NFS server with TLS encryption. For details, see [Configuring an NFS server with TLS support](#configuring-an-nfs-server-with-tls-support "4.10. Configuring an NFS server with TLS support").
-   You have installed the `ktls-utils`{.literal} package.

**Procedure**

1.  Create a private key and a certificate signing request (CSR):

    ``` {.language-plaintext tabindex="-1"}
    # openssl req -new -newkey rsa:4096 -noenc \
    -keyout /etc/pki/tls/private/client.example.com.key \
    -out /etc/pki/tls/private/client.example.com.csr \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=client.example.com" \
    -addext "subjectAltName=DNS:client.example.com,IP:192.0.2.2"
    ```

    Important

    Common Name (CN) and Domain Name System (DNS) must match the hostname. IP must match IP of the host.

2.  Send the `/etc/pki/tls/private/client.example.com.csr`{.literal} file to a Certificate Authority (CA) and request a client certificate. Store the received CA certificate and the client certificate on the host.

3.  Import the CA certificate to the system's truststore:

    ``` {.language-plaintext tabindex="-1"}
    # cp ca.crt /etc/pki/ca-trust/source/anchors
    ```

    ``` {.language-plaintext tabindex="-1"}
    # update-ca-trust
    ```

4.  Move the client certificate to the `/etc/pki/tls/certs/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mv client.example.com.crt /etc/pki/tls/certs/
    ```

5.  Ensure the SELinux context is correct on the private key and certificates:

    ``` {.language-plaintext tabindex="-1"}
    # restorecon -Rv /etc/pki/tls/certs/
    ```

6.  Add the client certificate and private key to the `[authenticate.client]`{.literal} section in the `/etc/tlshd.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    x509.certificate= /etc/pki/tls/certs/client.example.com.crt
    x509.private_key= /etc/pki/tls/private/client.example.com.key
    ```

    Leave the `x509.truststore`{.literal} parameter unset.

7.  Enable and start the `tlshd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now tlshd.service
    ```

8.  Mount an NFS share by using TLS encryption:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o xprtsec=mtls server.example.com:/nfs/projects/ /mnt/
    ```

**Verification**

-   Verify that the client successfully mounted NFS share with TLS support:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u tlshd
    ```

    ``` {.language-plaintext tabindex="-1"}
    …
    Apr 01 08:37:56 client.example.com tlshd[10688]: Handshake with server.example.com (192.0.2.1) was successful
    ```

### [4.13. Frequently used NFS mount options](#frequently-used-nfs-mount-options) {#frequently-used-nfs-mount-options .title}

Common NFS mount options configure performance, security, and compatibility when mounting NFS shares by using command line, `fstab`{.literal}, or `autofs`{.literal}.

The following are the commonly-used options when mounting NFS shares. You can use these options with `mount`{.literal} commands, in `/etc/fstab`{.literal} settings, and the `autofs`{.literal} automapper.

`lookupcache=`{.literal}*`mode`{.literal}*
:   Specifies how the kernel should manage its cache of directory entries for a given mount point. Valid arguments for mode are `all`{.literal}, `none`{.literal}, or `positive`{.literal}.

`nfsvers=`{.literal}*`version`{.literal}*

:   Specifies which version of the NFS protocol to use, where version is `3`{.literal}, `4`{.literal}, `4.0`{.literal}, `4.1`{.literal}, or `4.2`{.literal}. This is useful for hosts that run multiple NFS servers, or to disable retrying a mount with lower versions. If no version is specified, the client tries version `4.2`{.literal} first. It then negotiates down until it finds a version supported by the server.

    The option `vers`{.literal} is identical to `nfsvers`{.literal}, and is included in this release for compatibility reasons.

`noacl`{.literal}
:   Turns off all ACL processing. This can be needed when interfacing with old Red Hat Enterprise Linux versions that are not compatible with the recent ACL technology.

`nolock`{.literal}
:   Disables file locking. This setting can be required when you connect to very old NFS servers.

`noexec`{.literal}
:   Prevents execution of binaries on mounted file systems. This is useful if the system is mounting a non-Linux file system containing incompatible binaries.

`nosuid`{.literal}
:   Disables the `set-user-identifier`{.literal} and `set-group-identifier`{.literal} bits. This prevents remote users from gaining higher privileges by running a `setuid`{.literal} program.

`retrans=`{.literal}*`num`{.literal}*
:   The number of times the NFS client retries a request before it attempts further recovery action. If the `retrans`{.literal} option is not specified, the NFS client tries each UDP request three times and each TCP request twice.

`timeo=`{.literal}*`num`{.literal}*
:   The time in tenths of a second the NFS client waits for a response before it retries an NFS request. For NFS over TCP, the default `timeo`{.literal} value is 600 (60 seconds). The NFS client performs linear backoff. After each retransmission the timeout is increased by `timeo`{.literal} up to the maximum of 600 seconds.

`port=`{.literal}*`num`{.literal}*
:   Specifies the numeric value of the NFS server port. For NFSv3, if num is `0`{.literal} (the default value), or not specified, then mount queries the `rpcbind`{.literal} service on the remote host for the port number to use. For NFSv4, if num is `0`{.literal}, then mount queries the `rpcbind`{.literal} service. However, if it is not specified, the standard NFS port number of TCP 2049 is used instead and the remote `rpcbind`{.literal} is not checked anymore.

`rsize=`{.literal}*`num`{.literal}* and `wsize=`{.literal}*`num`{.literal}*

:   These options set the maximum number of bytes to be transferred in a single NFS read or write operation.

    There is no fixed default value for `rsize`{.literal} and `wsize`{.literal}. By default, NFS uses the largest possible value that both the server and the client support. In Red Hat Enterprise Linux 10, the client and server maximum is 1,048,576 bytes. For more information, see the Red Hat Knowledgebase solution [What are the default and maximum values for rsize and wsize with NFS mounts?](https://access.redhat.com/solutions/753853).

`sec=`{.literal}*`options`{.literal}*

:   Security options to use for accessing files on the mounted export. The options value is a colon-separated list of one or more security options.

    By default, the client attempts to find a security option that both the client and the server support. If the server does not support any of the selected options, the mount operation fails.

    Available options:

    -   `sec=sys`{.literal} uses local UNIX UIDs and GIDs. These use `AUTH_SYS`{.literal} to authenticate NFS operations.
    -   `sec=krb5`{.literal} uses Kerberos V5 instead of local UNIX UIDs and GIDs to authenticate users.
    -   `sec=krb5i`{.literal} uses Kerberos V5 for user authentication and performs integrity checking of NFS operations by using secure checksums to prevent data tampering.
    -   `sec=krb5p`{.literal} uses Kerberos V5 for user authentication, integrity checking, and encrypts NFS traffic to prevent traffic sniffing. This is the most secure setting, but it also involves the most performance overhead.

For more information, see the `mount(8)`{.literal} and `nfs(5)`{.literal} man pages on your system.

### [4.14. Enabling client-side caching of NFS content](#enabling-client-side-caching-of-nfs-content) {#enabling-client-side-caching-of-nfs-content .title}

FS-Cache is a persistent local cache on the client. File systems can use it to take data retrieved from over the network and cache it on the local disk. This helps to minimize network traffic.

#### [4.14.1. How NFS caching works](#how-nfs-caching-works) {#how-nfs-caching-works .title}

Network File System (NFS) caching leverages FS-Cache to improve network file system performance, reduce server load, and enable efficient local data retrieval through cache back ends and transparent integration.

The following diagram is a high-level illustration of how FS-Cache works:

FS-Cache is designed to be as transparent as possible to the users and administrators of a system. With FS-Cache a file system on a server can interact directly with a client's local cache without creating an over-mounted file system. With NFS, a mount option instructs the client to mount the NFS share with FS-cache enabled. The mount point causes automatic upload for the kernel module `cachefiles`{.literal}. The `cachefilesd`{.literal} daemon communicates with the kernel modules to implement the cache.

FS-Cache does not alter the basic operation of a file system that works over the network. It merely provides that file system with a persistent place in which it can cache data. For example, a client can still mount an NFS share whether or not FS-Cache is enabled. In addition, cached NFS can handle files that do not fit into the cache (whether individually or collectively). As files can be partially cached and do not have to be read completely up front. FS-Cache also hides all input/output (I/O) errors that occur in the cache from the client file system driver.

To provide caching services, FS-Cache needs a cache back end, the `cachefiles`{.literal} service. FS-Cache requires a mounted block-based file system, that supports block mapping (`bmap`{.literal}) and extended attributes as its cache back end:

-   XFS
-   ext3
-   ext4

FS-Cache cannot arbitrarily cache any file system, whether through the network or otherwise: the shared file system's driver must be altered to allow interaction with FS-Cache, data storage or retrieval, and metadata configuration and validation. FS-Cache needs *indexing keys* and *coherency data* from the cached file system to support persistence: indexing keys to match file system objects to cache objects, and coherency data to determine whether the cache objects are still valid.

Using FS-Cache is a compromise between various factors. If FS-Cache is being used to cache NFS traffic, it may slow the client down, but can massively reduce the network and server loading by satisfying read requests locally without consuming network bandwidth.

#### [4.14.2. Installing and configuring the cachefilesd service](#installing-and-configuring-the-cachefilesd-service) {#installing-and-configuring-the-cachefilesd-service .title}

Red Hat Enterprise Linux provides only the `cachefiles`{.literal} caching back end. The `cachefilesd`{.literal} service initiates and manages `cachefiles`{.literal}. The `/etc/cachefilesd.conf`{.literal} file controls how `cachefiles`{.literal} provides caching services.

**Prerequisites**

-   The file system mounted under the `/var/cache/fscache/`{.literal} directory is `ext3`{.literal}, `ext4`{.literal}, or `xfs`{.literal}.
-   The file system mounted under `/var/cache/fscache/`{.literal} uses extended attributes, which is the default if you created the file system on RHEL 8 or later.

**Procedure**

1.  Install the `cachefilesd`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install cachefilesd
    ```

2.  Enable and start the `cachefilesd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now cachefilesd
    ```

**Verification**

1.  Mount an NFS share with the `fsc`{.literal} option to use the cache:

    a.  To mount a share temporarily, enter:

        ``` {.language-plaintext tabindex="-1"}
        # mount -o fsc server.example.com:/nfs/projects/ /mnt/
        ```

    b.  To mount a share permanently, add the `fsc`{.literal} option to the entry in the `/etc/fstab`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        <nfs_server_ip_or_hostname>:/<exported_share>     <mount point>    nfs fsc 0 0
        ```

2.  Display the FS-cache statistics:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/fs/fscache/stats
    ```

    For more information, see the:

    -   `/usr/share/doc/cachefilesd/README`{.literal} file
    -   `/usr/share/doc/kernel-doc-<kernel_version>/Documentation/filesystems/caching/fscache.rst`{.literal} provided by the `kernel-doc`{.literal} package

#### [4.14.3. Sharing NFS cache](#sharing-nfs-cache) {#sharing-nfs-cache .title}

NFS mounts share or isolate cache based on mount options, security, and protocol details. Factors like superblock uniqueness and configuration parameters determine whether caches are accessible across different mounts.

Because the cache is persistent, blocks of data in the cache are indexed on a sequence of four keys:

-   Level 1: Server details
-   Level 2: Some mount options; security type; FSID; a uniquifier string
-   Level 3: File Handle
-   Level 4: Page number in file

To avoid coherency management problems between superblocks, all NFS superblocks that require to cache the data have unique level 2 keys. Normally, two NFS mounts with the same source volume and options share a superblock, and therefore share the caching, even if they mount different directories within that volume.

**Example 4.1. NFS cache sharing:**

The following two mounts likely share the superblock as they have the same mount options, especially if because they come from the same partition on the NFS server:

``` {.language-plaintext tabindex="-1"}
# mount -o fsc home0:/nfs/projects /projects
```

``` {.language-plaintext tabindex="-1"}
# mount -o fsc home0:/nfs/home /home/
```

If the mount options are different, they do not share the superblock:

``` {.language-plaintext tabindex="-1"}
# mount -o fsc,rsize=8192 home0:/nfs/projects /projects
```

``` {.language-plaintext tabindex="-1"}
# mount -o fsc,rsize=65536 home0:/nfs/home /home/
```

Note

The user cannot share caches between superblocks that have different communications or protocol parameters. For example, it is not possible to share caches between NFSv4.0 and NFSv3 or between NFSv4.1 and NFSv4.2 because they force different superblocks. Also setting parameters, such as the read size (`rsize`{.literal}), prevents cache sharing because, again, it forces a different superblock.

#### [4.14.4. NFS cache limitations](#nfs-cache-limitations) {#nfs-cache-limitations .title}

NFS caching increases performance but can introduce consistency challenges.

There are some cache limitations with NFS:

-   Opening a file from a shared file system for direct I/O automatically bypasses the cache. This is because this type of access must be direct to the server.
-   Opening a file from a shared file system for either direct I/O or writing flushes the cached copy of the file. FS-Cache does not cache the file again until it is no longer opened for direct I/O or writing.
-   Furthermore, this release of FS-Cache only caches regular NFS files. FS-Cache does not cache directories, symlinks, device files, FIFOs, and sockets.

#### [4.14.5. How cache culling works](#how-cache-culling-works) {#how-cache-culling-works .title}

Cache culling is the process of removing less-recently accessed cache objects to ensure sufficient free space is maintained on local disks.

The `cachefilesd`{.literal} service caches remote data on local disk, which may consume available space. To manage this, cache culling periodically discards older, less-used objects from the cache to maintain free space.

The `cachefilesd`{.literal} service works by caching remote data from shared file systems to free space on the local disk. This could potentially consume all available free space, which could cause problems if the disk also contains the root partition. To control this, `cachefilesd`{.literal} tries to maintain a certain amount of free space by discarding old objects, such as less-recently accessed objects, from the cache. This behavior is known as cache culling.

Cache culling is done on the basis of the percentage of blocks and the percentage of files available in the underlying file system. There are settings in `/etc/cachefilesd.conf`{.literal} which control six limits:

brun *N%* (percentage of blocks), frun *N%* (percentage of files)
:   If the amount of free space and the number of available files in the cache rises above both these limits, then culling is turned off.

bcull *N%* (percentage of blocks), fcull *N%* (percentage of files)
:   If the amount of available space or the number of files in the cache falls below either of these limits, then culling is started.

bstop *N%* (percentage of blocks), fstop *N%* (percentage of files)
:   If the amount of available space or the number of available files in the cache falls below either of these limits, then no further allocation of disk space or files is permitted until culling has raised things above these limits again.

The default value of `N`{.literal} for each setting is as follows:

-   `brun/frun`{.literal}: 10%
-   `bcull/fcull`{.literal}: 7%
-   `bstop/fstop`{.literal}: 3%

When configuring these settings, the following must hold true:

-   0 ≤ `bstop`{.literal} \< `bcull`{.literal} \< `brun`{.literal} \< 100
-   0 ≤ `fstop`{.literal} \< `fcull`{.literal} \< `frun`{.literal} \< 100

These are the percentages of available space and available files and do not appear as 100 minus the percentage displayed by the `df`{.literal} program.

Important

Culling depends on both b*xxx* and f*xxx* pairs simultaneously; the user cannot treat them separately.

## [Chapter 5. Mounting an SMB Share](#mounting-an-smb-share) {#chapter-5.-mounting-an-smb-share .title}

The Server Message Block (SMB) protocol implements an application-layer network protocol used to access resources on a server, such as file shares and shared printers.

Note

In the context of SMB, you can find mentions about the Common Internet File System (CIFS) protocol, which is a dialect of SMB. Both the SMB and CIFS protocol are supported, and the kernel module and utilities involved in mounting SMB and CIFS shares both use the name `cifs`{.literal}.

The `cifs-utils`{.literal} package provides utilities to:

-   Mount SMB and CIFS shares
-   Manage NT LAN Manager (NTLM) credentials in the kernel's keyring
-   Set and display Access Control Lists (ACL) in a security descriptor on SMB and CIFS shares
-   Display session ID, encryption/decrytion keys, SMB-specific file and quota information from a mounted SMB share

### [5.1. Supported SMB protocol versions](#supported-smb-protocol-versions) {#supported-smb-protocol-versions .title}

The Linux `cifs.ko`{.literal} kernel module supports certain Server Message Block (SMB) protocol versions. There are some security considerations and feature differences among SMB1, SMB2, SMB3, and newer versions for optimal network file sharing.

The `cifs.ko`{.literal} kernel module supports the following SMB protocol versions:

-   SMB 1

    Warning

    The SMB1 protocol is deprecated due to known security issues, and is only **safe to use on a private network**. The main reason that SMB1 is still provided as a supported option is that currently it is the only SMB protocol version that supports UNIX extensions. If you do not need to use UNIX extensions on SMB, use SMB2 or later.

-   SMB 2.0

-   SMB 2.1

-   SMB 3.0

-   SMB 3.1.1

Note

Depending on the protocol version, not all SMB features are implemented.

### [5.2. UNIX extensions support](#unix-extensions-support) {#unix-extensions-support .title}

Samba uses the `CAP_UNIX`{.literal} capability bit in the SMB protocol to provide the UNIX extensions feature. These extensions are also supported by the `cifs.ko`{.literal} kernel module. However, both Samba and the kernel module support UNIX extensions only in the SMB 1 protocol.

**Prerequisites**

-   The `cifs-utils`{.literal} package is installed.

**Procedure**

1.  Set the `server min protocol`{.literal} parameter in the `[global]`{.literal} section in the `/etc/samba/smb.conf`{.literal} file to `NT1`{.literal}.

2.  Mount the share by using the SMB 1 protocol by providing the `-o vers=1.0`{.literal} option to the mount command. For example:

    ``` {.language-plaintext tabindex="-1"}
    # mount -t cifs -o vers=1.0,username=<user_name> //<server_name>/<share_name> /mnt/
    ```

    By default, the kernel module uses SMB 2 or the highest later protocol version supported by the server. Passing the `-o vers=1.0`{.literal} option to the `mount`{.literal} command forces that the kernel module uses the SMB 1 protocol that is required for using UNIX extensions.

**Verification**

-   Display the options of the mounted share:

    ``` {.language-plaintext tabindex="-1"}
    # mount
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    //<server_name>/<share_name> on /mnt type cifs (...,unix,...)
    ```

    If the `unix`{.literal} entry is displayed in the list of mount options, UNIX extensions are enabled.

### [5.3. Manually mounting an SMB share](#manually-mounting-an-smb-share) {#manually-mounting-an-smb-share .title}

You can access files on a remote SMB server temporarily by mounting the share manually with the `mount`{.literal} utility.

Note

Manually mounted shares are not mounted automatically again when you reboot the system. To configure that Red Hat Enterprise Linux automatically mounts the share when the system boots, see [Mounting an SMB share automatically when the system boots](#mounting-an-smb-share-automatically-when-the-system-boots "5.4. Mounting an SMB share automatically when the system boots").

**Prerequisites**

-   The `cifs-utils`{.literal} package is installed.

**Procedure**

-   Use the `mount`{.literal} utility with the `-t cifs`{.literal} parameter to mount an SMB share:

    ``` {.language-plaintext tabindex="-1"}
    # mount -t cifs -o username=<user_name> //<server_name>/<share_name> /mnt/
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for <user_name>@//<server_name>/<share_name>:  password
    ```

    In the `-o`{.literal} parameter, you can specify options that are used to mount the share. For details, see the `OPTIONS`{.literal} section in the `mount.cifs(8)`{.literal} man page and [Frequently used SMB mount options](#frequently-used-smb-mount-options "5.7. Frequently used SMB mount options"). Following is an example for mounting a share by using an encrypted SMB 3.0 connection.

    To mount the `\\server\example\`{.literal} share as the *`DOMAIN`{.literal}*`\Administrator`{.literal} user over an encrypted SMB 3.0 connection into the `/mnt/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mount -t cifs -o username=DOMAIN\Administrator,seal,vers=3.0 //server/example /mnt/
    ```

    ``` {.language-plaintext tabindex="-1"}
    Password for DOMAIN\Administrator@//server_name/share_name:  password
    ```

**Verification**

-   List the content of the mounted share:

    ``` {.language-plaintext tabindex="-1"}
    # ls -l /mnt/
    ```

    ``` {.language-plaintext tabindex="-1"}
    total 4
    drwxr-xr-x.  2 root root 8748 Dec  4 16:27 test.txt
    drwxr-xr-x. 17 root root 4096 Dec  4 07:43 Demo-Directory
    ```

### [5.4. Mounting an SMB share automatically when the system boots](#mounting-an-smb-share-automatically-when-the-system-boots) {#mounting-an-smb-share-automatically-when-the-system-boots .title}

If access to a mounted SMB share is permanently required on a server, mount the share automatically at boot time.

**Prerequisites**

-   The `cifs-utils`{.literal} package is installed.

**Procedure**

1.  Add an entry for the share to the `/etc/fstab`{.literal} file. For example:

    ``` {.language-plaintext tabindex="-1"}
    //<server_name>/<share_name>  /mnt  cifs  credentials=/root/smb.cred  0 0
    ```

    Important

    To enable the system to mount a share automatically, you must store the user name, password, and domain name in a credentials file. For details, see [Creating a credentials file to authenticate to an smb share](#creating-a-credentials-file-to-authenticate-to-an-smb-share "5.5. Creating a credentials file to authenticate to an SMB share").

    In the fourth field of the row in the `/etc/fstab`{.literal}, specify mount options, such as the path to the credentials file. For details, see the `OPTIONS`{.literal} section in the `mount.cifs(8)`{.literal} man page and [Frequently used SMB mount options](#frequently-used-smb-mount-options "5.7. Frequently used SMB mount options").

**Verification**

-   Mount the share by specifying the mount point:

    ``` {.language-plaintext tabindex="-1"}
    # mount /mnt/
    ```

### [5.5. Creating a credentials file to authenticate to an SMB share](#creating-a-credentials-file-to-authenticate-to-an-smb-share) {#creating-a-credentials-file-to-authenticate-to-an-smb-share .title}

In certain situations, such as when mounting a share automatically at boot time, a share should be mounted without entering the user name and password. To implement this, create a credentials file.

**Prerequisites**

-   The `cifs-utils`{.literal} package is installed.

**Procedure**

1.  Create a file, such as `/root/smb.cred`{.literal}, and specify the user name, password, and domain name in that file:

    ``` {.language-plaintext tabindex="-1"}
    username=user_name
    password=password
    domain=domain_name
    ```

2.  Set the permissions to only allow the owner to access the file:

    ``` {.language-plaintext tabindex="-1"}
    # chown user_name /root/smb.cred
    ```

    ``` {.language-plaintext tabindex="-1"}
    # chmod 600 /root/smb.cred
    ```

    You can now pass the `credentials=`{.literal}*`file_name`{.literal}* mount option to the `mount`{.literal} utility or use it in the `/etc/fstab`{.literal} file to mount the share without being prompted for the user name and password.

### [5.6. Performing a multi-user SMB mount](#performing-a-multi-user-smb-mount) {#performing-a-multi-user-smb-mount .title}

The credentials used to mount a share define default access permissions. For example, if you mount a share by using the *`DOMAIN`{.literal}*`\example`{.literal} user, all actions on that share run as that user, no matter which local user performs them.

In certain situations, the administrator wants to mount a share automatically when the system boots, but users should perform actions on the share's content by using their own credentials. You can configure this scenario by using the `multiuser`{.literal} mount option.

Important

To use the `multiuser`{.literal} mount option, you must additionally set the `sec`{.literal} mount option to a security type that supports providing credentials in a non-interactive way, such as `krb5`{.literal} or the `ntlmssp`{.literal} option with a credentials file.

The `root`{.literal} user mounts the share by using the `multiuser`{.literal} option and an account that has minimal access to the contents of the share. Regular users can then provide their user name and password to the current session's kernel keyring by using the `cifscreds`{.literal} utility. If the user accesses the content of the mounted share, the kernel uses the credentials from the kernel keyring instead of the one initially used to mount the share.

Using this feature consists of the following steps:

-   Ensure the `cifs-utils`{.literal} package is installed.
-   Mount a share with the `multiuser`{.literal} option.
-   Optionally, verify if the share was successfully mounted with the `multiuser`{.literal} option.
-   Access the share as a user.

#### [5.6.1. Mounting a share with the multiuser option](#mounting-a-share-with-the-multiuser-option) {#mounting-a-share-with-the-multiuser-option .title}

Before users can access the share with their own credentials, mount the share as the `root`{.literal} user by using an account with limited permissions.

**Procedure**

1.  Create the entry for the share in the `/etc/fstab`{.literal} file. For example:

    ``` {.language-plaintext tabindex="-1"}
    //server_name/share_name  /mnt  cifs  multiuser,sec=ntlmssp,credentials=/root/smb.cred  0 0
    ```

2.  Mount the share:

    ``` {.language-plaintext tabindex="-1"}
    # mount /mnt/
    ```

    If you do not want to mount the share automatically when the system boots, mount it manually by passing `-o multiuser,sec=security_type`{.literal} to the `mount`{.literal} command. For details about mounting an SMB share manually, see [Manually mounting an SMB share](#manually-mounting-an-smb-share "5.3. Manually mounting an SMB share").

#### [5.6.2. Verifying if an SMB share is mounted with the multiuser option](#verifying-if-an-smb-share-is-mounted-with-the-multiuser-option) {#verifying-if-an-smb-share-is-mounted-with-the-multiuser-option .title}

To verify if a share is mounted with the `multiuser`{.literal} option, display the mount options.

**Procedure**

-   Display the mount options:

    ``` {.language-plaintext tabindex="-1"}
    # mount
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    //server_name/share_name on /mnt type cifs (sec=ntlmssp,multiuser,...)
    ```

    If the `multiuser`{.literal} entry is displayed in the list of mount options, the feature is enabled.

#### [5.6.3. Accessing a share as a user](#accessing-a-share-as-a-user) {#accessing-a-share-as-a-user .title}

If an SMB share is mounted with the `multiuser`{.literal} option, users can provide their credentials for the server to the kernel's keyring:

``` {.language-plaintext tabindex="-1"}
# cifscreds add -u SMB_user_name server_name
```

``` {.language-plaintext tabindex="-1"}
Password: password
```

When the user performs operations in the directory that contains the mounted SMB share, the server applies the file system permissions for this user. It does not apply the permissions of the user who initially mounted the share.

Note

Multiple users can perform operations by using their own credentials on the mounted share at the same time.

**Additional resources**

-   [Accessing a share as a user](#accessing-a-share-as-a-user "5.6.3. Accessing a share as a user")
-   [Mount a share with the `multiuser`{.literal} option](#mounting-a-share-with-the-multiuser-option "5.6.1. Mounting a share with the multiuser option")
-   [Optionally, verify if the share was successfully mounted with the `multiuser`{.literal} option](#verifying-if-an-smb-share-is-mounted-with-the-multiuser-option "5.6.2. Verifying if an SMB share is mounted with the multiuser option")
-   [Access the share as a user](#accessing-a-share-as-a-user "5.6.3. Accessing a share as a user")

### [5.7. Frequently used SMB mount options](#frequently-used-smb-mount-options) {#frequently-used-smb-mount-options .title}

Explore frequently used SMB mount options, including configuration details for credential handling, permissions, encryption, security modes, and protocol versions, to optimize secure and efficient SMB share connections in Linux environments.

When you mount an SMB share, the mount options determine:

-   How the connection will be established with the server. For example, which SMB protocol version is used when connecting to the server.
-   How the share will be mounted into the local file system. For example, if the system overrides the remote file and directory permissions to provide access to multiple local users to the content on the server.

To set multiple options in the fourth field of the `/etc/fstab`{.literal} file or in the `-o`{.literal} parameter of a mount command, separate them with commas.

The following list gives frequently used mount options:

+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                      | Description                                                                                                                                                                                                                                |
+:============================+:===========================================================================================================================================================================================================================================+
| credentials=*file_name*     | Sets the path to the credentials file.                                                                                                                                                                                                     |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dir_mode=*mode*             | Sets the directory mode if the server does not support CIFS UNIX extensions.                                                                                                                                                               |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| file_mode=*mode*            | Sets the file mode if the server does not support CIFS UNIX extensions.                                                                                                                                                                    |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| password=*password*         | Sets the password used to authenticate to the SMB server. Alternatively, specify a credentials file by using the `credentials`{.literal} option.                                                                                           |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| seal                        | Enables encryption support for connections by using SMB 3.0 or a later protocol version. Therefore, use `seal`{.literal} together with the `vers`{.literal} mount option set to `3.0`{.literal} or later.                                  |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sec=*security_mode*         | Sets the security mode, such as `ntlmsspi`{.literal}, to enable NTLMv2 password hashing and enabled packet signing. For a list of supported values, see the option's description in the `mount.cifs(8)`{.literal} man page on your system. |
|                             |                                                                                                                                                                                                                                            |
|                             | If the server does not support the `ntlmv2`{.literal} security mode, use `sec=ntlmssp`{.literal}, which is the default.                                                                                                                    |
|                             |                                                                                                                                                                                                                                            |
|                             | For security reasons, do not use the insecure `ntlm`{.literal} security mode.                                                                                                                                                              |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| username=*user_name*        | Sets the user name used to authenticate to the SMB server. Alternatively, specify a credentials file by using the `credentials`{.literal} option.                                                                                          |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vers=*SMB_protocol_version* | Sets the SMB protocol version used for the communication with the server.                                                                                                                                                                  |
+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Show more

For a complete list, see the `OPTIONS`{.literal} section in the `mount.cifs(8)`{.literal} man page on your system.

**Additional resources**

-   [Mounting a share with the multiuser option](#mounting-a-share-with-the-multiuser-option "5.6.1. Mounting a share with the multiuser option")
-   [Creating a credentials file to authenticate to an smb share](#creating-a-credentials-file-to-authenticate-to-an-smb-share "5.5. Creating a credentials file to authenticate to an SMB share")
-   [Manually mounting an SMB share](#manually-mounting-an-smb-share "5.3. Manually mounting an SMB share")

## [Chapter 6. Overview of persistent naming attributes](#overview-of-persistent-naming-attributes) {#chapter-6.-overview-of-persistent-naming-attributes .title}

As a system administrator, you need to refer to storage volumes by using persistent naming attributes to build storage setups that are reliable over multiple system boots.

### [6.1. Disadvantages of non-persistent naming attributes](#disadvantages-of-non-persistent-naming-attributes) {#disadvantages-of-non-persistent-naming-attributes .title}

Red Hat Enterprise Linux provides a number of ways to identify storage devices. It is important to use the correct option to identify each device. This helps avoid inadvertently accessing the wrong device.

It is particularly important when installing to or reformatting drives.

Traditionally, non-persistent names in the form of `/dev/sd`{.literal}*`(major number)`{.literal}**`(minor number)`{.literal}* are used on Linux to refer to storage devices. The major and minor number range and associated `sd`{.literal} names are allocated for each device when it is detected. This means that the association between the major and minor number range and the associated `sd`{.literal} names can change. This can happen if the order of device detection changes.

Such a change in the ordering might occur in the following situations:

-   The parallelization of the system boot process detects storage devices in a different order with each system boot.
-   A disk fails to power up or respond to the Small Computer System Interface (SCSI) controller. This results in it not being detected by the normal device probe. The disk is not accessible to the system. As a result, subsequent devices will have their major and minor number ranges shifted down. This also affects the associated `sd`{.literal} names. For example, a disk normally referred to as `sdb`{.literal} might not be detected. In that case, a disk normally referred to as `sdc`{.literal} would appear as `sdb`{.literal} instead.
-   A SCSI controller (host bus adapter, or HBA) fails to initialize, causing all disks connected to that HBA to not be detected. Any disks connected to subsequently probed HBAs are assigned different major and minor number ranges, and different associated `sd`{.literal} names.
-   The order of driver initialization changes if different types of HBAs are present in the system. This causes the disks connected to those HBAs to be detected in a different order. This might also occur if HBAs are moved to different PCI slots on the system.
-   Disks connected through Fibre Channel, Internet Small Computer System Interface (iSCSI), or Fibre Channel over Ethernet (FCoE) adapters might be inaccessible when probed. For example, this can happen due to a storage array or intervening switch being powered off. This might occur when a system reboots after a power failure and the storage array takes longer to come online than the system. Some Fibre Channel drivers support a mechanism to specify a persistent SCSI target ID to World Wide Port Name (WWPN) mapping. However, this does not reserve the major and minor number ranges or the associated `sd`{.literal} names. It only provides consistent SCSI target ID numbers.

These reasons make it undesirable to use the major and minor number range or associated `sd`{.literal} names when referring to devices. This is especially true in files such as `/etc/fstab`{.literal}. There is the possibility that the wrong device will be mounted and data corruption might result.

Occasionally, it is still necessary to refer to `sd`{.literal} names, even when another mechanism is used. This can occur when errors are reported by a device. The Linux kernel uses `sd`{.literal} names in kernel messages about the device. It also uses SCSI host, channel, target, and Logical Unit Number (LUN) tuples.

### [6.2. File system and device identifiers](#file-system-and-device-identifiers) {#file-system-and-device-identifiers .title}

File system identifiers are tied to the file system itself, while device identifiers are linked to the physical block device. Understanding the difference is important for proper storage management.

**File system identifiers**

File system identifiers are tied to a particular file system created on a block device. The identifier is also stored as part of the file system. If you copy the file system to a different device, it still carries the same file system identifier.

However, if you rewrite the device, such as by formatting it with the `mkfs`{.literal} utility, the device loses the attribute.

File system identifiers include:

-   Unique identifier (UUID)
-   Label

**Device identifiers**

Device identifiers are tied to a block device: for example, a disk or a partition. If you rewrite the device, such as by formatting it with the `mkfs`{.literal} utility, the device keeps the attribute. This is because it is not stored in the file system.

Device identifiers include:

-   World Wide Identifier (WWID)
-   Partition UUID
-   Serial number

**Recommendations**

-   Some file systems, such as logical volumes, span multiple devices. Access these file systems by using file system identifiers rather than device identifiers.

### [6.3. Device names managed by the udev mechanism in /dev/disk/](#device-names-managed-by-the-udev-mechanism-in-devdisk) {#device-names-managed-by-the-udev-mechanism-in-devdisk .title}

The `udev`{.literal} mechanism in Linux handles all device types, not only storage devices. It provides persistent naming attributes in `/dev/disk/`{.literal}. In Red Hat Enterprise Linux, `udev`{.literal} rules for storage devices create symbolic links in this directory.

You can refer to storage devices by:

-   Their content
-   A unique identifier
-   Their serial number.

Although `udev`{.literal} naming attributes are persistent, in that they do not change on their own across system reboots, some are also configurable.

#### [6.3.1. File system identifiers](#file-system-identifiers) {#file-system-identifiers .title}

**The UUID attribute in /dev/disk/by-uuid/**

Entries in this directory provide a symbolic name that refers to the storage device by a **unique identifier** (UUID) in the content (that is, the data) stored on the device. For example:

``` {.language-plaintext tabindex="-1"}
/dev/disk/by-uuid/3e6be9de-8139-11d1-9106-a43f08d823a6
```

You can use the UUID to refer to the device in the `/etc/fstab`{.literal} file by using the following syntax:

``` {.language-plaintext tabindex="-1"}
UUID=3e6be9de-8139-11d1-9106-a43f08d823a6
```

You can configure the UUID attribute when creating a file system, and you can also change it later on.

**The Label attribute in /dev/disk/by-label/**

Entries in this directory provide a symbolic name that refers to the storage device by a **label** in the content (that is, the data) stored on the device. For example:

``` {.language-plaintext tabindex="-1"}
/dev/disk/by-label/Boot
```

You can use the label to refer to the device in the `/etc/fstab`{.literal} file by using the following syntax:

``` {.language-plaintext tabindex="-1"}
LABEL=Boot
```

You can configure the Label attribute when creating a file system, and you can also change it later on.

#### [6.3.2. Device identifiers](#device-identifiers) {#device-identifiers .title}

**The WWID attribute in /dev/disk/by-id/**

The World Wide Identifier (WWID) is a persistent, **system-independent identifier** required by the Small Computer System Interface (SCSI) standard for all devices. The WWID identifier is guaranteed to be unique for every storage device, and independent of the path that is used to access the device. The identifier is a property of the device but is not stored in the content (that is, the data) on the devices.

This identifier can be obtained by issuing a SCSI Inquiry to retrieve the Device Identification Vital Product Data (page `0x83`{.literal}) or Unit Serial Number (page `0x80`{.literal}).

Red Hat Enterprise Linux automatically maintains the proper mapping from the WWID-based device name to a current `/dev/sd`{.literal} name on that system. Applications can use the `/dev/disk/by-id/`{.literal} name to reference the data on the disk, even if the path to the device changes, and even when accessing the device from different systems.

Note

If your are using an NVMe device, you might run into a disk by-id naming change for some vendors, if the serial number of your device has leading whitespace.

**Example of WWID mappings:**

+---------------------------------------------------------------------------------+-----------------------+--------------------------------------------------+
| WWID symlink                                                                    | Non-persistent device | Note                                             |
+:================================================================================+:======================+:=================================================+
| `/dev/disk/by-id/scsi-3600508b400105e210000900000490000`{.literal}              | `/dev/sda`{.literal}  | A device with a page `0x83`{.literal} identifier |
+---------------------------------------------------------------------------------+-----------------------+--------------------------------------------------+
| `/dev/disk/by-id/scsi-SSEAGATE_ST373453LW_3HW1RHM6`{.literal}                   | `/dev/sdb`{.literal}  | A device with a page `0x80`{.literal} identifier |
+---------------------------------------------------------------------------------+-----------------------+--------------------------------------------------+
| `/dev/disk/by-id/ata-SAMSUNG_MZNLN256HMHQ-000L7_S2WDNX0J336519-part3`{.literal} | `/dev/sdc3`{.literal} | A disk partition                                 |
+---------------------------------------------------------------------------------+-----------------------+--------------------------------------------------+

Show more

In addition to these persistent names provided by the system, you can also use `udev`{.literal} rules to implement persistent names of your own, mapped to the WWID of the storage.

**The Partition UUID attribute in /dev/disk/by-partuuid**

The Partition UUID (PARTUUID) attribute identifies partitions as defined by the GUID Partition Table (GPT) partition table.

**Example of Partition UUID mappings:**

+-----------------------------------------------+---------------------------+
| PARTUUID symlink                              | Non-persistent device     |
+:==============================================+:==========================+
| `/dev/disk/by-partuuid/4cd1448a-01`{.literal} | `/dev/sda1`{.literal}     |
+-----------------------------------------------+---------------------------+
| `/dev/disk/by-partuuid/4cd1448a-02`{.literal} | `/dev/sda2`{.literal}     |
+-----------------------------------------------+---------------------------+
| `/dev/disk/by-partuuid/4cd1448a-03`{.literal} | `/dev/sda3`{.literal}     |
+-----------------------------------------------+---------------------------+

Show more

**The Path attribute in /dev/disk/by-path/**

This attribute provides a symbolic name that refers to the storage device by the **hardware path** used to access the device.

The Path attribute fails if any part of the hardware path (for example, the PCI ID, target port, or LUN number) changes. The Path attribute is therefore unreliable. However, the Path attribute may be useful in one of the following scenarios:

-   You need to identify a disk that you are planning to replace later.
-   You plan to install a storage service on a disk in a specific location.

### [6.4. The World Wide Identifier with DM Multipath](#the-world-wide-identifier-with-dm-multipath) {#the-world-wide-identifier-with-dm-multipath .title}

You can configure Device Mapper (DM) Multipath to map between the World Wide Identifier (WWID) and non-persistent device names.

If there are multiple paths from a system to a device, DM Multipath uses the WWID to detect this. DM Multipath then presents a single \"pseudo-device\" in the `/dev/mapper/wwid`{.literal} directory, such as `/dev/mapper/3600508b400105df70000e00000ac0000`{.literal}.

The command `multipath -l`{.literal} shows the mapping to the non-persistent identifiers:

-   *`Host`{.literal}*`:`{.literal}*`Channel`{.literal}*`:`{.literal}*`Target`{.literal}*`:`{.literal}*`LUN`{.literal}*
-   `/dev/sd`{.literal} name
-   *`major`{.literal}*`:`{.literal}*`minor`{.literal}* number

**Example 6.1. WWID mappings in a multipath configuration**

An example output of the `multipath -l`{.literal} command:

``` {.language-plaintext tabindex="-1"}
3600508b400105df70000e00000ac0000 dm-2 vendor,product
[size=20G][features=1 queue_if_no_path][hwhandler=0][rw]
\_ round-robin 0 [prio=0][active]
 \_ 5:0:1:1 sdc 8:32  [active][undef]
 \_ 6:0:1:1 sdg 8:96  [active][undef]
\_ round-robin 0 [prio=0][enabled]
 \_ 5:0:0:1 sdb 8:16  [active][undef]
 \_ 6:0:0:1 sdf 8:80  [active][undef]
```

DM Multipath automatically maintains the proper mapping of each WWID-based device name to its corresponding `/dev/sd`{.literal} name on the system. These names are persistent across path changes, and they are consistent when accessing the device from different systems.

When the `user_friendly_names`{.literal} feature of DM Multipath is used, the WWID is mapped to a name of the form `/dev/mapper/mpath`{.literal}*`N`{.literal}*. By default, this mapping is maintained in the file `/etc/multipath/bindings`{.literal}. These `mpath`{.literal}*`N`{.literal}* names are persistent as long as that file is maintained.

Important

If you use `user_friendly_names`{.literal}, then additional steps are required to obtain consistent names in a cluster.

### [6.5. Limitations of the udev device naming convention](#limitations-of-the-udev-device-naming-convention) {#limitations-of-the-udev-device-naming-convention .title}

The udev device naming convention has some challenges and constraints. These include event timing, device accessibility, latency, naming stability, and potential conflicts with external processes in dynamic storage environments.

The following are some limitations of the `udev`{.literal} naming convention:

-   It is possible that the device might not be accessible when the query is performed. This is because the `udev`{.literal} mechanism might rely on querying the storage device when processing `udev`{.literal} rules for a `udev`{.literal} event. This is more likely with Fibre Channel, Internet Small Computer System Interface (iSCSI), or Fibre Channel over Ethernet (FCoE) storage devices. This occurs when the device is not located in the server chassis.
-   The kernel might send `udev`{.literal} events at any time, causing the rules to be processed. This might remove `/dev/disk/by-*/`{.literal} links if the device is not accessible.
-   There might be a delay between when the `udev`{.literal} event is generated and when it is processed. This occurs when many devices are detected and the user-space `udevd`{.literal} service takes time to process the rules for each one. This might cause a delay between when the kernel detects the device and when the `/dev/disk/by-*/`{.literal} names are available.
-   External programs such as blkid invoked by the rules might open the device briefly. This makes the device temporarily inaccessible for other uses.
-   The device names managed by the `udev`{.literal} mechanism in `/dev/disk/`{.literal} may change between major releases, requiring you to update the links.

### [6.6. Listing persistent naming attributes](#listing-persistent-naming-attributes) {#listing-persistent-naming-attributes .title}

You can find out the persistent naming attributes of non-persistent storage devices.

**Procedure**

-   To list the Universally Unique Identifier (UUID) and Label attributes, use the `lsblk`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ lsblk --fs storage-device
    ```

    For example, view the UUID label of a file system:

    ``` {.language-plaintext tabindex="-1"}
    $ lsblk --fs /dev/sda1
    ```

    ``` {.language-plaintext tabindex="-1"}
    NAME FSTYPE LABEL UUID                                 MOUNTPOINT
    sda1 xfs    Boot  afa5d5e3-9050-48c3-acc1-bb30095f3dc4 /boot
    ```

-   To list the PARTUUID attribute, use the `lsblk`{.literal} utility with the `--output +PARTUUID`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    $ lsblk --output +PARTUUID
    ```

    For example, view the PARTUUID attribute of a partition:

    ``` {.language-plaintext tabindex="-1"}
    $ lsblk --output +PARTUUID /dev/sda1
    ```

    ``` {.language-plaintext tabindex="-1"}
    NAME MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT PARTUUID
    sda1   8:1    0  512M  0 part /boot      4cd1448a-01
    ```

-   To list the World Wide Identifier (WWID) attribute, examine the targets of symbolic links in the `/dev/disk/by-id/`{.literal} directory.

    For example, view the WWID of all storage devices on the system:

    ``` {.language-plaintext tabindex="-1"}
    $ file /dev/disk/by-id/*
    ```

    ``` {.language-plaintext tabindex="-1"}
    /dev/disk/by-id/ata-QEMU_HARDDISK_QM00001
    symbolic link to ../../sda
    /dev/disk/by-id/ata-QEMU_HARDDISK_QM00001-part1
    symbolic link to ../../sda1
    /dev/disk/by-id/ata-QEMU_HARDDISK_QM00001-part2
    symbolic link to ../../sda2
    /dev/disk/by-id/dm-name-rhel_rhel8-root
    symbolic link to ../../dm-0
    /dev/disk/by-id/dm-name-rhel_rhel8-swap
    symbolic link to ../../dm-1
    /dev/disk/by-id/dm-uuid-LVM-QIWtEHtXGobe5bewlIUDivKOz5ofkgFhP0RMFsNyySVihqEl2cWWbR7MjXJolD6g
    symbolic link to ../../dm-1
    /dev/disk/by-id/dm-uuid-LVM-QIWtEHtXGobe5bewlIUDivKOz5ofkgFhXqH2M45hD2H9nAf2qfWSrlRLhzfMyOKd
    symbolic link to ../../dm-0
    /dev/disk/by-id/lvm-pv-uuid-atlr2Y-vuMo-ueoH-CpMG-4JuH-AhEF-wu4QQm
    symbolic link to ../../sda2
    ```

### [6.7. Modifying persistent naming attributes](#modifying-persistent-naming-attributes) {#modifying-persistent-naming-attributes .title}

You can change the UUID or Label persistent naming attribute of a file system.

Note

Changing `udev`{.literal} attributes happens in the background and might take a long time. The `udevadm settle`{.literal} command waits until the change is fully registered, which ensures that your next command is able to use the new attribute correctly.

In the following commands:

-   Replace *new-uuid* with the UUID you want to set; for example, `1cdfbc07-1c90-4984-b5ec-f61943f5ea50`{.literal}. You can generate a UUID by using the `uuidgen`{.literal} command.
-   Replace *new-label* with a label; for example, `backup_data`{.literal}.

**Prerequisites**

-   If you are modifying the attributes of an XFS file system, unmount it first.

**Procedure**

-   To change the UUID or Label attributes of an **XFS** file system, use the `xfs_admin`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # xfs_admin -U new-uuid -L new-label storage-device
    ```

    ``` {.language-plaintext tabindex="-1"}
    # udevadm settle
    ```

-   To change the UUID or Label attributes of an **ext4**, **ext3**, or **ext2** file system, use the `tune2fs`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # tune2fs -U new-uuid -L new-label storage-device
    ```

    ``` {.language-plaintext tabindex="-1"}
    # udevadm settle
    ```

-   To change the UUID or Label attributes of a swap volume, use the `swaplabel`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # swaplabel --uuid new-uuid --label new-label swap-device
    ```

    ``` {.language-plaintext tabindex="-1"}
    # udevadm settle
    ```

## [Chapter 7. Partition operations with parted](#partition-operations-with-parted) {#chapter-7.-partition-operations-with-parted .title}

`parted`{.literal} is a program to manipulate disk partitions. It supports multiple partition table formats, including MS-DOS and GPT. It is useful for creating space for new operating systems, reorganizing disk usage, and copying data to new hard disks.

### [7.1. Viewing the partition table with parted](#viewing-the-partition-table-with-parted) {#viewing-the-partition-table-with-parted .title}

Display the partition table of a block device to see the partition layout and details about individual partitions. You can view the partition table on a block device by using the `parted`{.literal} utility. For more information, see the `parted(8)`{.literal} man page on your system.

**Procedure**

1.  Start the `parted`{.literal} utility. For example, the following output lists the device `/dev/sda`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # parted /dev/sda
    ```

2.  View the partition table:

    ``` {.language-plaintext tabindex="-1"}
    (parted) print
    ```

    ``` {.language-plaintext tabindex="-1"}
    Model: ATA SAMSUNG MZNLN256 (scsi)
    Disk /dev/sda: 256GB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos
    Disk Flags:

    Number  Start   End     Size    Type      File system  Flags
     1      1049kB  269MB   268MB   primary   xfs          boot
     2      269MB   34.6GB  34.4GB  primary
     3      34.6GB  45.4GB  10.7GB  primary
     4      45.4GB  256GB   211GB   extended
     5      45.4GB  256GB   211GB   logical
    ```

3.  Optional: Switch to the device you want to examine next:

    ``` {.language-plaintext tabindex="-1"}
    (parted) select block-device
    ```

    For a detailed description of the print command output, see the following:

    `Model: ATA SAMSUNG MZNLN256 (scsi)`{.literal}
    :   The disk type, manufacturer, model number, and interface.

    `Disk /dev/sda: 256GB`{.literal}
    :   The file path to the block device and the storage capacity.

    `Partition Table: msdos`{.literal}
    :   The disk label type.

    `Number`{.literal}
    :   The partition number. For example, the partition with minor number 1 corresponds to `/dev/sda1`{.literal}.

    `Start`{.literal} and `End`{.literal}
    :   The location on the device where the partition starts and ends.

    `Type`{.literal}
    :   Valid types are metadata, free, primary, extended, or logical.

    `File system`{.literal}
    :   The file system type. If the `File system`{.literal} field of a device shows no value, this means that its file system type is unknown. The `parted`{.literal} utility cannot recognize the file system on encrypted devices.

    `Flags`{.literal}
    :   Lists the flags set for the partition. The most commonly used flags are `boot`{.literal}, `root`{.literal}, `swap`{.literal}, `hidden`{.literal}, `raid`{.literal}, `lvm`{.literal}, or `lba`{.literal}. For a complete list of flags, see `parted(8)`{.literal} man page on your system.

### [7.2. Creating a partition table on a disk with parted](#creating-a-partition-table-on-a-disk-with-parted) {#creating-a-partition-table-on-a-disk-with-parted .title}

Create a partition table on a disk to define the layout for organizing storage space into separate, manageable sections. You can create multiple partitions for different purposes and operating systems by using this step.

Warning

Formatting a block device with a partition table deletes all data stored on the device.

**Procedure**

1.  Start the interactive `parted`{.literal} shell:

    ``` {.language-plaintext tabindex="-1"}
    # parted block-device
    ```

2.  Determine if there already is a partition table on the device:

    ``` {.language-plaintext tabindex="-1"}
    (parted) print
    ```

    If the device already contains partitions, they are deleted in the following steps.

3.  Create the new partition table:

    ``` {.language-plaintext tabindex="-1"}
    (parted) mklabel table-type
    ```

    -   Replace *table-type* with the intended partition table type:

        -   `msdos`{.literal} for Master Boot Record (MBR)

        -   `gpt`{.literal} for GUID Partition Table (GPT)

            For example to create a GPT table on the disk, use:

            ``` {.language-plaintext tabindex="-1"}
            (parted) mklabel gpt
            ```

            The changes start applying after you enter this command.

4.  View the partition table to confirm that it is created:

    ``` {.language-plaintext tabindex="-1"}
    (parted) print
    ```

5.  Exit the `parted`{.literal} shell:

    ``` {.language-plaintext tabindex="-1"}
    (parted) quit
    ```

### [7.3. Creating a partition with parted](#creating-a-partition-with-parted) {#creating-a-partition-with-parted .title}

Create new disk partitions to organize storage space efficiently and separate different types of data. You can configure dedicated areas for system files, user data, and swap space.

**Prerequisites**

-   A partition table on the disk.
-   If the partition you want to create is larger than 2 TiB, format the disk with the **GUID Partition Table (GPT)**.

Note

The required partitions are `swap`{.literal}, `/boot/`{.literal}, and `/ (root)`{.literal}.

**Procedure**

1.  Start the `parted`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # parted block-device
    ```

2.  View the current partition table to determine if there is enough free space:

    ``` {.language-plaintext tabindex="-1"}
    (parted) print
    ```

    -   Resize the partition in case there is not enough free space.

    -   From the partition table, determine:

        -   The start and end points of the new partition.
        -   On MBR, what partition type it should be.

3.  Create the new partition:

    For MS-DOS:

    ``` {.language-plaintext tabindex="-1"}
    (parted) mkpart part-type fs-type start end
    ```

    For GPT:

    ``` {.language-plaintext tabindex="-1"}
    (parted) mkpart part-name fs-type start end
    ```

    -   Replace *part-type* with `primary`{.literal}, `logical`{.literal}, or `extended`{.literal}. This applies only to the MBR partition table.

    -   Replace *name* with an arbitrary partition name. This is required for GPT partition tables.

    -   Replace *fs-type* with `xfs`{.literal}, `ext2`{.literal}, `ext3`{.literal}, `ext4`{.literal}, `fat16`{.literal}, `fat32`{.literal}, `hfs`{.literal}, `hfs+`{.literal}, `linux-swap`{.literal}, `ntfs`{.literal}, or `reiserfs`{.literal}. The *fs-type* parameter is optional. Note that the `parted`{.literal} utility does not create the file system on the partition.

    -   Replace *start* and *end* with the sizes that determine the starting and ending points of the partition, counting from the beginning of the disk. You can use size suffixes, such as `512MiB`{.literal}, `20GiB`{.literal}, or `1.5TiB`{.literal}. The default size is in megabytes.

        For example, to create a primary partition from 1024 MiB until 2048 MiB on an MBR table, use:

        ``` {.language-plaintext tabindex="-1"}
        (parted) mkpart primary 1024MiB 2048MiB
        ```

        The changes start applying after you enter the command.

4.  View the partition table to confirm that the created partition is in the partition table with the correct partition type, file system type, and size:

    ``` {.language-plaintext tabindex="-1"}
    (parted) print
    ```

5.  Exit the `parted`{.literal} shell:

    ``` {.language-plaintext tabindex="-1"}
    (parted) quit
    ```

6.  Verify that the kernel recognizes the new partition:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/partitions
    ```

### [7.4. Removing a partition with parted](#removing-a-partition-with-parted) {#removing-a-partition-with-parted .title}

Remove unnecessary disk partitions to reclaim storage space for other purposes. You can reorganize disk layout, eliminate unused partitions, and optimize storage utilization on your system with this operation.

**Procedure**

1.  Start the interactive `parted`{.literal} shell:

    ``` {.language-plaintext tabindex="-1"}
    # parted block-device
    ```

    -   Replace *block-device* with the path to the device where you want to remove a partition: for example, `/dev/sda`{.literal}.

2.  View the current partition table to determine the minor number of the partition to remove:

    ``` {.language-plaintext tabindex="-1"}
    (parted) print
    ```

3.  Remove the partition:

    ``` {.language-plaintext tabindex="-1"}
    (parted) rm partition-number
    ```

    -   Replace *partition-number* with the partition number you want to remove.

    The changes start applying as soon as you enter this command.

4.  Verify that you have removed the partition from the partition table:

    ``` {.language-plaintext tabindex="-1"}
    (parted) print
    ```

5.  Exit the `parted`{.literal} shell:

    ``` {.language-plaintext tabindex="-1"}
    (parted) quit
    ```

6.  Verify that the kernel registers that the partition is removed:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/partitions
    ```

7.  Remove the partition from the `/etc/fstab`{.literal} file, if it is present. Find the line that declares the removed partition, and remove it from the file.

8.  Regenerate mount units so that your system registers the new `/etc/fstab`{.literal} configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

    Important

    To remove a partition mentioned in `/proc/cmdline`{.literal} or that is part of a Logical Volume Manager (LVM), see [Configuring and managing logical volumes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_logical_volumes/index), and the `dracut(8)`{.literal} and `grubby (8)`{.literal} man pages on your system.

### [7.5. Resizing a partition with parted](#resizing-a-partition-with-parted) {#resizing-a-partition-with-parted .title}

Using the `parted`{.literal} utility, extend a partition to use unused disk space, or shrink a partition to use its capacity for different purposes. For more information, see the `parted(8)`{.literal} man page on your system.

**Prerequisites**

-   Back up the data before shrinking a partition.
-   If the partition you want to create is larger than 2 TiB, format the disk with the **GUID Partition Table (GPT)**.
-   If you want to shrink the partition, first shrink the file system so that it is not larger than the resized partition.

Note

XFS does not support shrinking.

**Procedure**

1.  Start the `parted`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # parted block-device
    ```

2.  View the current partition table:

    ``` {.language-plaintext tabindex="-1"}
    (parted) print
    ```

    From the partition table, determine:

    -   The minor number of the partition.

    -   The location of the existing partition and its new ending point after resizing.

        Important

        When resizing a partition, ensure there is enough unallocated space between the end of the partition being resized and either the beginning of the next partition, or the end of the disk if it is the last partition. If there is not sufficient space, `parted`{.literal} will return an error. However, it is best to verify the available space before attempting to resize to avoid partition overlap.

3.  Resize the partition:

    ``` {.language-plaintext tabindex="-1"}
    (parted) resizepart 1 2GiB
    ```

    -   Replace *1* with the minor number of the partition that you are resizing.
    -   Replace *2* with the size that determines the new ending point of the resized partition, counting from the beginning of the disk. You can use size suffixes, such as `512MiB`{.literal}, `20GiB`{.literal}, or `1.5TiB`{.literal}. The default size is in megabytes.

4.  View the partition table to confirm that the resized partition is in the partition table with the correct size:

    ``` {.language-plaintext tabindex="-1"}
    (parted) print
    ```

5.  Exit the `parted`{.literal} shell:

    ``` {.language-plaintext tabindex="-1"}
    (parted) quit
    ```

6.  Verify that the kernel registers the new partition:

    ``` {.language-plaintext tabindex="-1"}
    # cat /proc/partitions
    ```

7.  Optional: If you extended the partition, extend the file system on it as well.

## [Chapter 8. Strategies for repartitioning a disk](#strategies-for-repartitioning-a-disk) {#chapter-8.-strategies-for-repartitioning-a-disk .title}

Most RHEL systems manage storage space by using LVM. You can also use `parted`{.literal}, `fdisk`{.literal}, or other graphical tools for disk partitioning. Repartitioning may use unpartitioned free space, an unused partition or free space reclaimed from an active partition.

Note

The following examples provide a general overview of partitioning techniques. They are simplified for clarity and do not reflect the exact partition layout during a typical Red Hat Enterprise Linux installation.

### [8.1. Using unpartitioned free space](#using-unpartitioned-free-space) {#using-unpartitioned-free-space .title}

Partitions that are already defined and do not span the entire hard disk, leave unallocated space. This space is not part of any defined partition.

An unused hard disk also falls into this category. The only difference is that *all* the space is not part of any defined partition.

On a new disk, you can create the necessary partitions from the unused space. Most preinstalled operating systems are configured to take up all available space on a disk drive.

### [8.2. Using space from an unused partition](#using-space-from-an-unused-partition) {#using-space-from-an-unused-partition .title}

To use the space allocated to the unused partition, delete the partition and then create the appropriate Linux partition instead. Alternatively, during the installation process, delete the unused partition and manually create new partitions.

### [8.3. Using free space from an active partition](#using-free-space-from-an-active-partition) {#using-free-space-from-an-active-partition .title}

Managing this process can be hard if the required free space is on an active partition that's already in use. Most computers with preinstalled software have a single large partition that holds both the operating system and user data.

Warning

If you attempt to resize or modify an active partition that contains an operating system (OS), there is a risk of losing the data or making the OS unbootable. As a result, in some cases, you might need to reinstall the OS. Check whether your system includes a recovery or installation media before proceeding.

To optimise the use of available free space, you can use the methods of destructive or non-destructive repartitioning.

#### [8.3.1. Destructive repartitioning](#destructive-repartitioning) {#destructive-repartitioning .title}

Destructive repartitioning destroys the partition on your hard drive and creates new partitions in its place. Backup any needed data from the original partition as this method deletes the entire contents.

After creating a new partition from your existing operating system, you can:

-   Reinstall software.
-   Restore your data.

Warning

This method deletes all data previously stored in the original partition.

#### [8.3.2. Non-destructive repartitioning](#non-destructive-repartitioning) {#non-destructive-repartitioning .title}

Non-destructive repartitioning resizes partitions, without any data loss. This method is reliable, however it takes longer processing time on large drives.

The following is a list of methods, which can help initiate non-destructive repartitioning.

-   Reorganize existing data

The storage location of some data cannot be changed which can prevent the resizing of a partition to the required size. This ultimately requires a destructive repartition process. Reorganizing data within an existing partition can help you resize the partitions as needed. This creates space for additional partitions or maximizes the available free space.

To avoid any possible data loss, create a backup before continuing with the data migration process.

-   Resize the existing partition

By resizing an already existing partition, you can free up unused space. Depending on your resizing software, the results may vary. In the majority of cases, you can create a new unformatted partition of the same type, as the original partition.

The steps you take after resizing can depend on the software you use. In the following example, the best practice is to delete the new DOS (Disk Operating System) partition. Instead, create a Linux partition. Verify what is most suitable for your disk before initiating the resizing process.

Note

Resizing and creating partitions may vary depending on the tool you are using, for example `parted`{.literal}, GParted. Refer to the documentation of the tool for specific instructions.

-   Optional: Create new partitions

Some resizing software is available for Linux based systems. In such cases, there is no need to delete the newly created partition after resizing. Creating a new partition afterwards depends on the software you use.

## [Chapter 9. Getting started with XFS](#getting-started-with-xfs) {#chapter-9.-getting-started-with-xfs .title}

This is an overview of how to create and maintain XFS file systems.

### [9.1. The XFS file system](#the-xfs-file-system_getting-started-with-xfs) {#the-xfs-file-system-1 .title}

XFS is a scalable, high-performance, 64-bit journaling file system. It supports very large files and file systems and is default in RHEL 10. Originally developed by SGI in the 1990s, it has long been used on large servers and storage arrays.

The features of XFS include:

Reliability

:   -   Metadata journaling ensures file system integrity after a system crash. It keeps a record of file system operations. These records can be replayed when the system restarts and the file system is remounted.
    -   Extensive run-time metadata consistency checking
    -   Scalable and fast repair utilities
    -   Quota journaling. This avoids the need for lengthy quota consistency checks after a crash.

Scalability and performance

:   -   Supported file system size up to 1024 TiB
    -   Ability to support a large number of concurrent operations
    -   B-tree indexing for scalability of free space management
    -   Sophisticated metadata read-ahead algorithms
    -   Optimizations for streaming video workloads

Allocation schemes

:   -   Extent-based allocation
    -   Stripe-aware allocation policies
    -   Delayed allocation
    -   Space pre-allocation
    -   Dynamically allocated inodes

Other features

:   -   Reflink-based file copies
    -   Tightly integrated backup and restore utilities
    -   Online defragmentation
    -   Online file system growing
    -   Comprehensive diagnostics capabilities
    -   Extended attributes (`xattr`{.literal}). With this, the system can associate several additional name/value pairs per file.
    -   Project or directory quotas for quota restrictions over a directory tree.
    -   Subsecond timestamps

Performance characteristics

:   XFS has high performance on large systems with enterprise workloads. A large system is one with a relatively high number of CPUs, multiple HBAs, and connections to external disk arrays. XFS also performs well on smaller systems that have a multi-threaded, parallel I/O workload.

    XFS performs comparably well on smaller systems, but is more focused on scalability and large data sets.

### [9.2. Comparison of tools used with ext4 and XFS](#comparison-of-tools-used-with-ext4-and-xfs_getting-started-with-xfs) {#comparison-of-tools-used-with-ext4-and-xfs .title}

Different tools and commands accomplish common file system tasks on ext4 and XFS, including creation, checking, resizing, and backup operations.

This section compares which tools to use to accomplish common tasks on the ext4 and XFS file systems.

+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Task                           | ext4                                  | XFS                                                    |
+:===============================+:======================================+:=======================================================+
| Create a file system           | `mkfs.ext4`{.literal}                 | `mkfs.xfs`{.literal}                                   |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| File system check              | `e2fsck`{.literal}                    | `xfs_repair`{.literal}                                 |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Resize a file system           | `resize2fs`{.literal}                 | `xfs_growfs`{.literal}                                 |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Save an image of a file system | `e2image`{.literal}                   | `xfs_metadump`{.literal} and `xfs_mdrestore`{.literal} |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Label or tune a file system    | `tune2fs`{.literal}                   | `xfs_admin`{.literal}                                  |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Back up a file system          | `tar`{.literal} and `rsync`{.literal} | `xfsdump`{.literal} and `xfsrestore`{.literal}         |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Quota management               | `quota`{.literal}                     | `xfs_quota`{.literal}                                  |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| File mapping                   | `filefrag`{.literal}                  | `filefrag`{.literal}                                   |
+--------------------------------+---------------------------------------+--------------------------------------------------------+

Show more

Note

If you want a complete client-server solution for backups over network, you can use `bacula`{.literal} backup utility that is available in RHEL 9. For more information about Bacula, see [Bacula backup solution](https://www.bacula.org/documentation/documentation/).

## [Chapter 10. Creating an XFS file system](#creating-an-xfs-file-system) {#chapter-10.-creating-an-xfs-file-system .title}

As a system administrator, you can create an XFS file system on a block device to enable it to store files and directories.

### [10.1. Creating an XFS file system with mkfs.xfs](#creating-an-xfs-file-system-with-mkfs-xfs) {#creating-an-xfs-file-system-with-mkfs.xfs .title}

Create an XFS file system to take advantage of high performance, scalability, and advanced features for large-scale storage environments. XFS is particularly effective for applications requiring large files and high throughput.

**Procedure**

1.  To create the file system:

    -   If the device is a regular partition, an LVM volume, an MD volume, a disk, or a similar device, use the following command:

        ``` {.language-plaintext tabindex="-1"}
        # mkfs.xfs block-device
        ```

        Note

        The minimum XFS file system size is 300 MB. `mkfs.xfs`{.literal} does not support creating smaller file systems to prevent performance and redundancy issues.

        -   Replace *block-device* with the path to the block device. For example, `/dev/sdb1`{.literal}, `/dev/disk/by-uuid/05e99ec8-def1-4a5e-8a9d-5945339ceb2a`{.literal}, or `/dev/my-volgroup/my-lv`{.literal}.
        -   In general, the default options are optimal for common use.
        -   When using `mkfs.xfs`{.literal} on a block device containing an existing file system, add the `-f`{.literal} option to overwrite that file system.

    -   To create the file system on a hardware RAID device, check if the system correctly detects the stripe geometry of the device:

        -   If the stripe geometry information is correct, no additional options are needed. Create the file system:

            ``` {.language-plaintext tabindex="-1"}
            # mkfs.xfs block-device
            ```

        -   If the information is incorrect, specify stripe geometry manually with the `su`{.literal} and `sw`{.literal} parameters of the `-d`{.literal} option. The `su`{.literal} parameter specifies the RAID chunk size, and the `sw`{.literal} parameter specifies the number of data disks in the RAID device.

            For example:

            ``` {.language-plaintext tabindex="-1"}
            # mkfs.xfs -d su=64k,sw=4 /dev/sda3
            ```

2.  Use the following command to wait for the system to register the new device node:

    ``` {.language-plaintext tabindex="-1"}
    # udevadm settle
    ```

    For more information, see the `mkfs.xfs(8)`{.literal} man page on your system.

## [Chapter 11. Backing up an XFS file system](#backing-up-an-xfs-file-system) {#chapter-11.-backing-up-an-xfs-file-system .title}

As a system administrator, you can use the `xfsdump`{.literal} to back up an XFS file system into a file or on a tape. This provides a command-line backup mechanism that supports incremental backups and does not require unmounting the file system.

### [11.1. Features of XFS backup](#features-of-xfs-backup) {#features-of-xfs-backup .title}

This section describes key concepts and features of backing up an XFS file system with the `xfsdump`{.literal} utility.

You can use the `xfsdump`{.literal} utility to:

-   Perform backups to regular file images.

    Only one backup can be written to a regular file.

-   Perform backups to tape drives.

    You can also write multiple backups to the same tape by using the `xfsdump`{.literal} utility. A backup can span multiple tapes.

    To back up multiple file systems to a single tape device, write the backup to a tape that already contains an XFS backup. This appends the new backup to the previous one. By default, `xfsdump`{.literal} never overwrites existing backups.

-   Create incremental backups.

    The `xfsdump`{.literal} utility uses dump levels to determine a base backup to which other backups are relative. Numbers from 0 to 9 refer to increasing dump levels. An incremental backup only backs up files that have changed since the last dump of a lower level:

    -   To perform a full backup, perform a level 0 dump on the file system.
    -   A level 1 dump is the first incremental backup after a full backup. The next incremental backup would be level 2, which only backs up files that have changed since the last level 1 dump; and so on, to a maximum of level 9.

-   Exclude files from a backup by using size, subtree, or inode flags to filter them.

For more information, see the `xfsdump(8)`{.literal} man page on your system.

### [11.2. Backing up an XFS file system with xfsdump](#backing-up-an-xfs-file-system-with-xfsdump) {#backing-up-an-xfs-file-system-with-xfsdump .title}

You can use the `xfsdump`{.literal} utility to back up the content of an XFS file system into a file or a tape.

**Prerequisites**

-   An XFS file system that you can back up.
-   Another file system or a tape drive where you can store the backup.

**Procedure**

-   Use the following command to back up an XFS file system:

    ``` {.language-plaintext tabindex="-1"}
    # xfsdump -l level [-L label] \ -f backup-destination path-to-xfs-filesystem
    ```

    -   Replace *level* with the dump level of your backup. Use `0`{.literal} to perform a full backup or `1`{.literal} to `9`{.literal} to perform consequent incremental backups.

    -   Replace *backup-destination* with the path where you want to store your backup. The destination can be a regular file, a tape drive, or a remote tape device. For example, `/backup-files/Data.xfsdump`{.literal} for a file or `/dev/st0`{.literal} for a tape drive.

    -   Replace *path-to-xfs-filesystem* with the mount point of the XFS file system you want to back up. For example, `/mnt/data/`{.literal}. The file system must be mounted.

    -   When backing up multiple file systems and saving them on a single tape device, add a session label to each backup by using `-L `{.literal}*`label`{.literal}*. This makes backups easier to identify when restoring. Replace *label* with any name for your backup: for example, `backup_data`{.literal}.

        For example, to back up the content of XFS file systems mounted on the `/boot/`{.literal} and `/data/`{.literal} directories as files in `/backup-files/`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # xfsdump -l 0 -f /backup-files/boot.xfsdump /boot
        ```

        ``` {.language-plaintext tabindex="-1"}
        # xfsdump -l 0 -f /backup-files/data.xfsdump /data
        ```

-   To back up multiple file systems on a single tape device, add a session label by using the `-L `{.literal}*`label`{.literal}* option:

    ``` {.language-plaintext tabindex="-1"}
    # xfsdump -l 0 -L "backup_boot" -f /dev/st0 /boot
    ```

    ``` {.language-plaintext tabindex="-1"}
    # xfsdump -l 0 -L "backup_data" -f /dev/st0 /data
    ```

    For more information, see the `xfsdump(8)`{.literal} man page on your system.

## [Chapter 12. Restoring an XFS file system from backup](#restoring-an-xfs-file-system-from-backup) {#chapter-12.-restoring-an-xfs-file-system-from-backup .title}

As a system administrator, you can use the `xfsrestore`{.literal} utility to restore XFS backup created with the `xfsdump`{.literal} utility and stored in a file or on a tape.

### [12.1. Features of restoring XFS from backup](#features-of-restoring-xfs-from-backup) {#features-of-restoring-xfs-from-backup .title}

You can restore XFS file systems from backups by using `xfsrestore`{.literal}. Discover available restore modes, session identification, and methods for selectively recovering files, helping ensure data integrity and flexible recovery solutions.

The `xfsrestore`{.literal} utility restores file systems from backups produced by `xfsdump`{.literal}. The `xfsrestore`{.literal} utility has two modes:

-   With the **simple** mode you can restore an entire file system from a level 0 dump. This is the default mode.
-   With the **cumulative** mode you can restore the file system from an incremental backup: that is, level 1 to level 9.

A unique *session ID* or *session label* identifies each backup. Restoring a backup from a tape containing multiple backups requires its corresponding session ID or label.

To extract, add, or delete specific files from a backup, enter the `xfsrestore`{.literal} interactive mode. The interactive mode provides a set of commands to manipulate the backup files.

For more information, see the `xfsrestore(8)`{.literal} man page on your system.

### [12.2. Restoring an XFS file system from backup with xfsrestore](#restoring-an-xfs-file-system-from-backup-with-xfsrestore) {#restoring-an-xfs-file-system-from-backup-with-xfsrestore .title}

Restore XFS file system content from file or tape backups by using `xfsrestore`{.literal}, including full and incremental backups with optional interactive mode.

**Prerequisites**

-   A file or tape backup of XFS file systems, as described in [Backing up an XFS file system](#backing-up-an-xfs-file-system "Chapter 11. Backing up an XFS file system").
-   A storage device where you can restore the backup.

**Procedure**

-   The command to restore the backup varies depending on whether you are restoring from a full backup or an incremental one, or are restoring multiple backups from a single tape device:

    ``` {.language-plaintext tabindex="-1"}
    # xfsrestore [-r] [-S session-id] [-L session-label] [-i] -f backup-location restoration-path
    ```

    -   Replace *backup-location* with the location of the backup. This can be a regular file, a tape drive, or a remote tape device. For example, `/backup-files/Data.xfsdump`{.literal} for a file or `/dev/st0`{.literal} for a tape drive.

    -   Replace *restoration-path* with the path to the directory where you want to restore the file system. For example, `/mnt/data/`{.literal}.

    -   To restore a file system from an incremental (level 1 to level 9) backup, add the `-r`{.literal} option.

    -   To restore a backup from a tape device that contains multiple backups, specify the backup by using the `-S`{.literal} or `-L`{.literal} options.

        You can choose a backup by its session ID by using the `-S`{.literal} option. You can choose by the session label, by using the `-L`{.literal} option. To obtain the session ID and session labels, use the `xfsrestore -I`{.literal} command.

        Replace *session-id* with the session ID of the backup. For example, `b74a3586-e52e-4a4a-8775-c3334fa8ea2c`{.literal}. Replace *session-label* with the session label of the backup. For example, `my_backup_session_label`{.literal}.

    -   To use `xfsrestore`{.literal} interactively, use the `-i`{.literal} option.

        The interactive dialog begins after `xfsrestore`{.literal} finishes reading the specified device. Available commands in the interactive `xfsrestore`{.literal} shell include `cd`{.literal}, `ls`{.literal}, `add`{.literal}, `delete`{.literal}, and `extract`{.literal}; for a complete list of commands, use the `help`{.literal} command. Following is an example for restoring multiple XFS file systems:

        -   To restore the XFS backup files and save their content into directories under `/mnt/`{.literal}:

            ``` {.language-plaintext tabindex="-1"}
            # xfsrestore -f /backup-files/boot.xfsdump /mnt/boot/
            ```

            ``` {.language-plaintext tabindex="-1"}
            # xfsrestore -f /backup-files/data.xfsdump /mnt/data/
            ```

        -   To restore from a tape device containing multiple backups, specify each backup by its session label or session ID:

            ``` {.language-plaintext tabindex="-1"}
            # xfsrestore -L "backup_boot" -f /dev/st0 /mnt/boot/
            ```

            ``` {.language-plaintext tabindex="-1"}
            # xfsrestore -S "45e9af35-efd2-4244-87bc-4762e476cbab" \ -f /dev/st0 /mnt/data/
            ```

### [12.3. Informational messages when restoring an XFS backup from a tape](#informational-messages-when-restoring-an-xfs-backup-from-a-tape) {#informational-messages-when-restoring-an-xfs-backup-from-a-tape .title}

When restoring a backup from a tape with backups from multiple file systems, the `xfsrestore`{.literal} utility might issue messages. The messages inform you whether a match of the requested backup has been found when `xfsrestore`{.literal} examines each backup on the tape in sequential order.

For example:

``` {.language-plaintext tabindex="-1"}
xfsrestore: preparing drive
xfsrestore: examining media file 0
xfsrestore: inventory session uuid (8590224e-3c93-469c-a311-fc8f23029b2a) does not match the media header's session uuid (7eda9f86-f1e9-4dfd-b1d4-c50467912408)
xfsrestore: examining media file 1
xfsrestore: inventory session uuid (8590224e-3c93-469c-a311-fc8f23029b2a) does not match the media header's session uuid (7eda9f86-f1e9-4dfd-b1d4-c50467912408)
[...]
```

The informational messages keep appearing until the matching backup is found.

## [Chapter 13. Increasing the size of an XFS file system](#increasing-the-size-of-an-xfs-file-system) {#chapter-13.-increasing-the-size-of-an-xfs-file-system .title}

As a system administrator, you can increase the size of an XFS file system to make a complete use of a larger storage capacity. However, it is not currently possible to decrease the size of XFS file systems.

Important

Increasing a filesystem from a very small size to a significantly larger size creates a high number of allocations groups, potentially leading to performance issues. As a best practice, limit the size increase to a maximum of 10 times the original size.

### [13.1. Increasing the size of an XFS file system with xfs_growfs](#increasing-the-size-of-an-xfs-file-system-with-xfsgrowfs) {#increasing-the-size-of-an-xfs-file-system-with-xfs_growfs .title}

Expand an XFS file system by using `xfs_growfs`{.literal} while the file system remains mounted. You can do this to a specific size or maximum device capacity.

**Prerequisites**

-   Ensure that the underlying block device is of an appropriate size to hold the resized file system later. Use the appropriate resizing methods for the affected block device.
-   Mount the XFS file system.

**Procedure**

-   While the XFS file system is mounted, use the `xfs_growfs`{.literal} utility to increase its size:

    ``` {.language-plaintext tabindex="-1"}
    # xfs_growfs file-system -D new-size
    ```

    -   Replace *file-system* with the mount point of the XFS file system.

    -   With the `-D`{.literal} option, replace *new-size* with the required new size of the file system specified in the number of file system blocks.

        To find out the block size in kB of a given XFS file system, use the `xfs_info`{.literal} utility:

        ``` {.language-plaintext tabindex="-1"}
        # xfs_info block-device
        ```

        ``` {.language-plaintext tabindex="-1"}
        ...
        data     =              bsize=4096
        ...
        ```

    -   Without the `-D`{.literal} option, `xfs_growfs`{.literal} grows the file system to the maximum size supported by the underlying device.

        For more information, see the `xfs_growfs(8)`{.literal} man page on your system.

## [Chapter 14. Configuring XFS error behavior](#configuring-xfs-error-behavior) {#chapter-14.-configuring-xfs-error-behavior .title}

You can configure how an XFS file system behaves when it encounters I/O errors. Error handling controls whether operations are retried, continued, or the system shuts down. This helps prevent data corruption and allows adaptation to workload and storage reliability requirements.

### [14.1. Configurable error handling in XFS](#configurable-error-handling-in-xfs) {#configurable-error-handling-in-xfs .title}

You can configure XFS file system error handling by setting retry limits and timeouts for I/O errors. Control how XFS responds to device errors, no-space conditions, and device loss, enhancing reliability and flexibility during operation and unmounting.

The XFS file system responds in one of the following ways when an error occurs during an I/O operation:

-   XFS repeatedly retries the I/O operation until the operation succeeds or XFS reaches a set limit.

    The limit is based either on a maximum number of retries or a maximum time for retries.

-   XFS considers the error permanent and stops the operation on the file system.

You can configure how XFS reacts to the following error conditions:

`EIO`{.literal}
:   Error when reading or writing

`ENOSPC`{.literal}
:   No space left on the device

`ENODEV`{.literal}
:   Device cannot be found

You can set the maximum number of retries and the maximum time in seconds until XFS considers an error permanent. XFS stops retrying the operation when it reaches either of the limits.

You can also configure XFS so that when unmounting a file system, XFS immediately cancels the retries regardless of any other configuration. This configuration enables the unmount operation to succeed despite persistent errors.

**Default behavior**

The default behavior for each XFS error condition depends on the error context. Some XFS errors such as `ENODEV`{.literal} are considered to be fatal and unrecoverable, regardless of the retry count. Their default retry limit is 0.

### [14.2. Configuration files for specific and undefined XFS error conditions](#configuration-files-for-specific-and-undefined-xfs-error-conditions) {#configuration-files-for-specific-and-undefined-xfs-error-conditions .title}

Configure XFS error handling through files that set retry limits and timeouts for specific error conditions as well as defaults for undefined errors, ensuring robust and controlled filesystem behavior.

The following directories store configuration files that control XFS error behavior for different error conditions:

`/sys/fs/xfs/`{.literal}*`device`{.literal}*`/error/metadata/EIO/`{.literal}
:   For the `EIO`{.literal} error condition

`/sys/fs/xfs/`{.literal}*`device`{.literal}*`/error/metadata/ENODEV/`{.literal}
:   For the `ENODEV`{.literal} error condition

`/sys/fs/xfs/`{.literal}*`device`{.literal}*`/error/metadata/ENOSPC/`{.literal}
:   For the `ENOSPC`{.literal} error condition

`/sys/fs/xfs/`{.literal}*`device`{.literal}*`/error/default/`{.literal}
:   Common configuration for all other, undefined error conditions

Each directory contains the following configuration files for configuring retry limits:

`max_retries`{.literal}
:   Controls the maximum number of times that XFS retries the operation.

`retry_timeout_seconds`{.literal}
:   Specifies the time limit in seconds after which XFS stops retrying the operation.

### [14.3. Setting XFS behavior for specific conditions](#setting-xfs-behavior-for-specific-conditions) {#setting-xfs-behavior-for-specific-conditions .title}

Configure XFS metadata error handling by setting maximum retry attempts and timeout limits for specific error conditions by using `sysfs`{.literal} parameters.

**Procedure**

-   Set the maximum number of retries, the retry time limit, or both:

    -   To set the maximum number of retries, write the required number to the `max_retries`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # echo value > /sys/fs/xfs/device/error/metadata/condition/max_retries
        ```

    -   To set the time limit, write the required number of seconds to the `retry_timeout_seconds`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # echo value > /sys/fs/xfs/device/error/metadata/condition/retry_timeout_second
        ```

    *value* is a number between -1 and the maximum possible value of the C signed integer type. This is 2147483647 on 64-bit Linux.

    In both limits, the value `-1`{.literal} is used for continuous retries and `0`{.literal} to stop immediately.

    *device* is the name of the device, as found in the `/dev/`{.literal} directory; for example, `sda`{.literal}.

### [14.4. Setting XFS behavior for undefined conditions](#setting-xfs-behavior-for-undefined-conditions) {#setting-xfs-behavior-for-undefined-conditions .title}

Configure default XFS metadata error handling by setting retry attempts and timeout limits for undefined error conditions. You can do this by using `sysfs`{.literal} parameters.

**Procedure**

-   Set the maximum number of retries, the retry time limit, or both:

    -   To set the maximum number of retries, write the required number to the `max_retries`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # echo value > /sys/fs/xfs/device/error/metadata/default/max_retries
        ```

    -   To set the time limit, write the required number of seconds to the `retry_timeout_seconds`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        # echo value > /sys/fs/xfs/device/error/metadata/default/retry_timeout_seconds
        ```

    *value* is a number between -1 and the maximum possible value of the C signed integer type. This is 2147483647 on 64-bit Linux.

    In both limits, the value `-1`{.literal} is used for continuous retries and `0`{.literal} to stop immediately.

    *device* is the name of the device, as found in the `/dev/`{.literal} directory; for example, `sda`{.literal}.

### [14.5. Setting the XFS unmount behavior](#setting-the-xfs-unmount-behavior) {#setting-the-xfs-unmount-behavior .title}

Configure how XFS reacts to errors during unmount. `fail_at_unmount`{.literal} overrides other error settings and unmounts without retrying I/O operations. The unmount succeeds even when persistent errors occur.

Warning

You cannot change the `fail_at_unmount`{.literal} value after the unmount process starts, because the unmount process removes the configuration files from the `sysfs`{.literal} interface for the respective file system. You must configure the unmount behavior before the file system starts unmounting.

**Procedure**

-   Enable or disable the `fail_at_unmount`{.literal} option:

    -   To cancel retrying all operations when the file system unmounts, enable the option:

        ``` {.language-plaintext tabindex="-1"}
        # echo 1 > /sys/fs/xfs/device/error/fail_at_unmount
        ```

    -   To respect the `max_retries`{.literal} and `retry_timeout_seconds`{.literal} retry limits when the file system unmounts, disable the option:

        ``` {.language-plaintext tabindex="-1"}
        # echo 0 > /sys/fs/xfs/device/error/fail_at_unmount
        ```

    *device* is the name of the device, as found in the `/dev/`{.literal} directory; for example, `sda`{.literal}.

## [Chapter 15. Performance analysis of XFS with PCP](#performance-analysis-of-xfs-with-pcp) {#chapter-15.-performance-analysis-of-xfs-with-pcp .title}

The XFS PMDA ships as part of the `pcp`{.literal} package and is enabled by default during the installation. It is used to gather performance metric data of XFS file systems in Performance Co-Pilot (PCP). You can use PCP to analyze the XFS file system's performance.

### [15.1. Installing XFS PMDA manually](#installing-xfs-pmda-manually) {#installing-xfs-pmda-manually .title}

Manually install the XFS Performance Metrics Domain Agent (PMDA). Yoo can do so by running the Install script when the agent is not listed in `pcp`{.literal} configuration output.

**Prerequisites**

-   Performance Co-Pilot (PCP) is installed. For more information, see [Installing and enabling PCP](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/configuring-performance-co-pilot#installing-and-enabling-pcp).

**Procedure**

1.  Navigate to the xfs directory:

    ``` {.language-plaintext tabindex="-1"}
    # cd /var/lib/pcp/pmdas/xfs/
    ```

2.  Install the XFS PMDA manually:

    ``` {.language-plaintext tabindex="-1"}
    xfs]# ./Install
    Updating the Performance Metrics Name Space (PMNS) ...
    Terminate PMDA if already installed ...
    Updating the PMCD control file, and notifying PMCD ...
    Check xfs metrics have appeared ... 387 metrics and 387 values
    ```

**Verification**

-   Verify that the `pmcd`{.literal} process is running on the host and the XFS PMDA is listed as enabled in the configuration:

    ``` {.language-plaintext tabindex="-1"}
    # pcp
    ```

    ``` {.language-plaintext tabindex="-1"}
    Performance Co-Pilot configuration on workstation:

    platform: Linux workstation 4.18.0-80.el8.x86_64 #1 SMP Wed Mar 13 12:02:46 UTC 2019 x86_64
    hardware: 12 cpus, 2 disks, 1 node, 36023MB RAM
    timezone: CEST-2
    services: pmcd
    pmcd: Version 4.3.0-1, 8 agents
    pmda: root pmcd proc xfs linux mmv kvm jbd2
    ```

    For more information, see the `pmcd(1)`{.literal} man page on your system.

**Additional resources**

-   [System services and tools distributed with PCP](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/configuring-performance-co-pilot#system-services-and-tools-distributed-with-pcp)

### [15.2. Examining XFS performance metrics with pminfo](#examining-xfs-performance-metrics-with-pminfo) {#examining-xfs-performance-metrics-with-pminfo .title}

PCP supports reporting of certain XFS metrics per mounted XFS file system through the XFS PMDA. This makes it easier to pinpoint specific mounted file system issues and evaluate performance. The `pminfo`{.literal} command provides per-device XFS metrics for each mounted XFS file system.

**Prerequisites**

-   PCP is installed. For more information, see [Installing and enabling PCP](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/configuring-performance-co-pilot#installing-and-enabling-pcp).

**Procedure**

-   Display the list of all available metrics provided by the XFS PMDA:

    ``` {.language-plaintext tabindex="-1"}
    # pminfo xfs
    ```

-   Display information for the individual metrics. The following examples examine specific XFS `read`{.literal} and `write`{.literal} metrics by using the `pminfo`{.literal} tool:

    -   Display a short description of the `xfs.write_bytes`{.literal} metric:

        ``` {.language-plaintext tabindex="-1"}
        # pminfo --oneline xfs.write_bytes
        ```

        ``` {.language-plaintext tabindex="-1"}
        xfs.write_bytes [number of bytes written in XFS file system write operations]
        ```

    -   Display a long description of the `xfs.read_bytes`{.literal} metric:

        ``` {.language-plaintext tabindex="-1"}
        # pminfo --helptext xfs.read_bytes
        ```

        ``` {.language-plaintext tabindex="-1"}
        xfs.read_bytes
        Help:
        This is the number of bytes read from read(2) system calls to files in
        XFS file systems. It can be used in conjunction with the read_calls
        count to calculate the average size of the read operations to file in
        XFS file systems.
        ```

    -   Obtain the current performance value of the `xfs.read_bytes`{.literal} metric:

        ``` {.language-plaintext tabindex="-1"}
        # pminfo --fetch xfs.read_bytes
        ```

        ``` {.language-plaintext tabindex="-1"}
        xfs.read_bytes
            value 4891346238
        ```

    -   Obtain per-device XFS metrics with `pminfo`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # pminfo --fetch --oneline xfs.perdev.read xfs.perdev.write
        ```

        ``` {.language-plaintext tabindex="-1"}
        xfs.perdev.read [number of XFS file system read operations]
        inst [0 or "loop1"] value 0
        inst [0 or "loop2"] value 0

        xfs.perdev.write [number of XFS file system write operations]
        inst [0 or "loop1"] value 86
        inst [0 or "loop2"] value 0
        ```

        For more information, see the `pminfo(1)`{.literal} man page on your system.

### [15.3. Resetting XFS performance metrics with pmstore](#resetting-xfs-performance-metrics-with-pmstore) {#resetting-xfs-performance-metrics-with-pmstore .title}

With PCP, you can modify the values of certain metrics, especially if the metric acts as a control variable, such as the `xfs.control.reset`{.literal} metric. To modify a metric value, use the `pmstore`{.literal} tool.

**Prerequisites**

-   PCP is installed. For more information, see [Installing and enabling PCP](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/configuring-performance-co-pilot#installing-and-enabling-pcp).

**Procedure**

1.  Display the value of a metric:

    ``` {.language-plaintext tabindex="-1"}
    $ pminfo -f xfs.write
    ```

    ``` {.language-plaintext tabindex="-1"}
    xfs.write
        value 325262
    ```

2.  Reset all the XFS metrics:

    ``` {.language-plaintext tabindex="-1"}
    # pmstore xfs.control.reset 1
    ```

    ``` {.language-plaintext tabindex="-1"}
    xfs.control.reset old value=0 new value=1
    ```

**Verification**

-   View the information after resetting the metric:

    ``` {.language-plaintext tabindex="-1"}
    $ pminfo --fetch xfs.write
    ```

    ``` {.language-plaintext tabindex="-1"}
    xfs.write
        value 0
    ```

    For more information, see the `pmstore(1)`{.literal} and `pminfo(1)`{.literal} man pages on your system.

**Additional resources**

-   [System services and tools distributed with PCP](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/monitoring_and_managing_system_status_and_performance/configuring-performance-co-pilot#system-services-and-tools-distributed-with-pcp)

### [15.4. PCP metric groups for XFS](#pcp-metric-groups-for-xfs) {#pcp-metric-groups-for-xfs .title}

Performance Co-Pilot offers comprehensive metric groups for monitoring XFS file system operations across all devices, including allocation, transactions, and buffer activities.

The following table describes the available PCP metric groups for XFS.

+:----------------------------------+:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Metric Group                      | Metrics provided                                                                                                                                                                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.*`{.literal}                 | General XFS metrics including the read and write operation counts, read and write byte counts. Along with counters for the number of times inodes are flushed, clustered and number of failure to cluster.                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.allocs.*`{.literal}          | Range of metrics regarding the allocation of objects in the file system, these include number of extent and block creations/frees. Allocation tree lookup and compares along with extend record creation and deletion from the btree.      |
|                                   |                                                                                                                                                                                                                                            |
| `xfs.alloc_btree.*`{.literal}     |                                                                                                                                                                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.block_map.*`{.literal}       | Metrics include the number of block map read/write and block deletions, extent list operations for insertion, deletions and lookups. Also operations counters for compares, lookups, insertions and deletion operations from the blockmap. |
|                                   |                                                                                                                                                                                                                                            |
| `xfs.bmap_btree.*`{.literal}      |                                                                                                                                                                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.dir_ops.*`{.literal}         | Counters for directory operations on XFS file systems for creation, entry deletions, count of \"getdent\" operations.                                                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.transactions.*`{.literal}    | Counters for the number of meta-data transactions, these include the count for the number of synchronous and asynchronous transactions along with the number of empty transactions.                                                        |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.inode_ops.*`{.literal}       | Counters for the number of times that the operating system looked for an XFS inode in the inode cache with different outcomes. These count cache hits, cache misses, and so on.                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.log.*`{.literal}             | Counters for the number of log buffer writes over XFS file systems includes the number of blocks written to disk. Metrics also for the number of log flushes and pinning.                                                                  |
|                                   |                                                                                                                                                                                                                                            |
| `xfs.log_tail.*`{.literal}        |                                                                                                                                                                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.xstrat.*`{.literal}          | Counts for the number of bytes of file data flushed out by the XFS flush daemon along with counters for number of buffers flushed to contiguous and non-contiguous space on disk.                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.attr.*`{.literal}            | Counts for the number of attribute get, set, remove and list operations over all XFS file systems.                                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.quota.*`{.literal}           | Metrics for quota operation over XFS file systems, these include counters for number of quota reclaims, quota cache misses, cache hits and quota data reclaims.                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.buffer.*`{.literal}          | Range of metrics regarding XFS buffer objects. Counters include the number of requested buffer calls, successful buffer locks, waited buffer locks, miss_locks, miss_retries and buffer hits when looking up pages.                        |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.btree.*`{.literal}           | Metrics regarding the operations of the XFS btree.                                                                                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.control.reset`{.literal}     | Configuration metrics which are used to reset the metric counters for the XFS stats. Control metrics are toggled by means of the pmstore tool.                                                                                             |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 15.1. Metric groups for XFS

Show more

### [15.5. Per-device PCP metric groups for XFS](#per-device-pcp-metric-groups-for-xfs) {#per-device-pcp-metric-groups-for-xfs .title}

Performance Co-Pilot provides metric groups for monitoring individual XFS devices, covering operations from allocation to transaction management.

The following table describes the available per-device PCP metric group for XFS.

+:--------------------------------------+:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Metric Group                          | Metrics provided                                                                                                                                                                                                                           |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.*`{.literal}              | General XFS metrics including the read and write operation counts, read and write byte counts. Along with counters for the number of times inodes are flushed, clustered and number of failure to cluster.                                 |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.allocs.*`{.literal}       | Range of metrics regarding the allocation of objects in the file system, these include number of extent and block creations/frees. Allocation tree lookup and compares along with extend record creation and deletion from the btree.      |
|                                       |                                                                                                                                                                                                                                            |
| `xfs.perdev.alloc_btree.*`{.literal}  |                                                                                                                                                                                                                                            |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.block_map.*`{.literal}    | Metrics include the number of block map read/write and block deletions, extent list operations for insertion, deletions and lookups. Also operations counters for compares, lookups, insertions and deletion operations from the blockmap. |
|                                       |                                                                                                                                                                                                                                            |
| `xfs.perdev.bmap_btree.*`{.literal}   |                                                                                                                                                                                                                                            |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.dir_ops.*`{.literal}      | Counters for directory operations of XFS file systems for creation, entry deletions, count of \"getdent\" operations.                                                                                                                      |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.transactions.*`{.literal} | Counters for the number of meta-data transactions, these include the count for the number of synchronous and asynchronous transactions along with the number of empty transactions.                                                        |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.inode_ops.*`{.literal}    | Counters for the number of times that the operating system looked for an XFS inode in the inode cache with different outcomes. These count cache hits, cache misses, and so on.                                                            |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.log.*`{.literal}          | Counters for the number of log buffer writes over XFS file systems includes the number of blocks written to disk. Metrics also for the number of log flushes and pinning.                                                                  |
|                                       |                                                                                                                                                                                                                                            |
| `xfs.perdev.log_tail.*`{.literal}     |                                                                                                                                                                                                                                            |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.xstrat.*`{.literal}       | Counts for the number of bytes of file data flushed out by the XFS flush daemon along with counters for number of buffers flushed to contiguous and non-contiguous space on disk.                                                          |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.attr.*`{.literal}         | Counts for the number of attribute get, set, remove and list operations over all XFS file systems.                                                                                                                                         |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.quota.*`{.literal}        | Metrics for quota operation over XFS file systems, these include counters for number of quota reclaims, quota cache misses, cache hits and quota data reclaims.                                                                            |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.buffer.*`{.literal}       | Range of metrics regarding XFS buffer objects. Counters include the number of requested buffer calls, successful buffer locks, waited buffer locks, miss_locks, miss_retries and buffer hits when looking up pages.                        |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `xfs.perdev.btree.*`{.literal}        | Metrics regarding the operations of the XFS btree.                                                                                                                                                                                         |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 15.2. Per-device PCP metric groups for XFS

Show more

## [Chapter 16. Checking and repairing a file system](#checking-and-repairing-a-file-system_) {#chapter-16.-checking-and-repairing-a-file-system .title}

RHEL offers file system administration tools known as `fsck`{.literal} (file system check) to check and repair file systems. System administration tools might run automatically during boot if issues are detected, but they can also be run manually when needed.

Important

File system checkers guarantee only metadata consistency across the file system. They have no awareness of the actual data contained within the file system and are not data recovery tools.

### [16.1. Scenarios that require a file system check](#scenarios-that-require-a-file-system-check) {#scenarios-that-require-a-file-system-check .title}

Identify situations when a file system check is necessary, such as corruption, boot failures, or system errors. You can take appropriate actions and considerations for diagnosing and repairing file system issues. You can do this by using standard check utilities.

The relevant `fsck`{.literal} tools can be used to check your system if any of the following occurs:

-   System fails to boot
-   Files on a specific disk become corrupt
-   The file system shuts down or changes to read-only due to inconsistencies
-   A file on the file system is inaccessible

File system inconsistencies can occur for various reasons, including but not limited to hardware errors, storage administration errors, and software bugs.

Important

File system check tools cannot repair hardware problems. A file system must be fully readable and writable if repair is to operate successfully. If a file system was corrupted due to a hardware error, the file system must first be moved to a good disk, for example with the `dd(8)`{.literal} utility.

For journaling file systems, all that is normally required at boot time is to replay the journal if required and this is usually a very short operation.

However, if a file system inconsistency or corruption occurs, even for journaling file systems, then the file system checker must be used to repair the file system.

Important

It is possible to disable file system check at boot by setting the sixth field in `/etc/fstab`{.literal} to `0`{.literal}. However, do not do so unless you are having issues with `fsck`{.literal} at boot time, for example with extremely large or remote file systems.

For more information, see the `fstab(5)`{.literal}, `fsck(8)`{.literal}, and `dd(8)`{.literal} man pages on your system.

### [16.2. Potential side effects of running fsck](#potential-side-effects-of-running-fsck) {#potential-side-effects-of-running-fsck .title}

Generally, running the file system check and repair tool can be expected to automatically repair at least some of the inconsistencies it finds. In some cases, the following issues can arise:

-   Severely damaged inodes or directories may be discarded if they cannot be repaired.
-   Significant changes to the file system may occur.

To ensure that unexpected or undesirable changes are not permanently made, ensure you follow any precautionary steps outlined in the procedure.

### [16.3. Error-handling mechanisms in XFS](#error-handling-mechanisms-in-xfs) {#error-handling-mechanisms-in-xfs .title}

This section describes how XFS handles various kinds of errors in the file system.

**Unclean unmounts**

Journalling maintains a transactional record of metadata changes that happen on the file system.

In the event of a system crash, power failure, or other unclean unmount, XFS uses the journal (also called log) to recover the file system. The kernel performs journal recovery when mounting the XFS file system.

**Corruption**

In this context, *corruption* means errors on the file system caused by, for example:

-   Hardware faults
-   Bugs in storage firmware, device drivers, the software stack, or the file system itself
-   Problems that cause parts of the file system to be overwritten by something outside of the file system

When XFS detects corruption in the file system or the file-system metadata, it may shut down the file system and report the incident in the system log. Note that if the corruption occurred on the file system hosting the `/var`{.literal} directory, these logs are unavailable after a reboot.

The following is an example of system log entry reporting an XFS corruption:

``` {.language-plaintext tabindex="-1"}
# dmesg --notime | tail -15
```

``` {.language-plaintext tabindex="-1"}
XFS (loop0): Mounting V5 Filesystem
XFS (loop0): Metadata CRC error detected at xfs_agi_read_verify+0xcb/0xf0 [xfs], xfs_agi block 0x2
XFS (loop0): Unmount and run xfs_repair
XFS (loop0): First 128 bytes of corrupted metadata buffer:
00000000027b3b56: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
000000005f9abc7a: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
000000005b0aef35: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00000000da9d2ded: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
000000001e265b07: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
000000006a40df69: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
000000000b272907: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00000000e484aac5: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
XFS (loop0): metadata I/O error in "xfs_trans_read_buf_map" at daddr 0x2 len 1 error 74
XFS (loop0): xfs_imap_lookup: xfs_ialloc_read_agi() returned error -117, agno 0
XFS (loop0): Failed to read root inode 0x80, error 11
```

User-space utilities usually report the *Input/output error* message when trying to access a corrupted XFS file system. Mounting an XFS file system with a corrupted log results in a failed mount and the following error message:

``` {.language-plaintext tabindex="-1"}
mount: /mount-point: mount(2) system call failed: Structure needs cleaning.
```

You must manually use the `xfs_repair`{.literal} utility to repair the corruption. For more information see the `xfs_repair(8)`{.literal} man page on your system.

### [16.4. Checking an XFS file system with xfs_repair](#checking-an-xfs-file-system-with-xfsrepair) {#checking-an-xfs-file-system-with-xfs_repair .title}

Perform a read-only check of an XFS file system using `xfs_repair`{.literal}. Unlike other tools, `xfs_repair`{.literal} does not run at boot even after unclean unmounts. Instead, XFS replays the log at mount time; `xfs_repair`{.literal} cannot fix a dirty log without remounting.

Note

An `fsck.xfs`{.literal} binary is present in the `xfsprogs`{.literal} package only to satisfy `initscripts`{.literal} that look for an `fsck.file`{.literal} system binary at boot time. `fsck.xfs`{.literal} immediately exits with an exit code of 0.

**Procedure**

1.  Replay the log by mounting and unmounting the file system:

    ``` {.language-plaintext tabindex="-1"}
    # mount file-system
    ```

    ``` {.language-plaintext tabindex="-1"}
    # umount file-system
    ```

    Note

    If the mount fails with a structure needs cleaning error, the log is corrupted and cannot be replayed. The dry run should discover and report more on-disk corruption as a result.

2.  Use the `xfs_repair`{.literal} utility to perform a dry run to check the file system. Any errors are printed and an indication of the actions that would be taken, without modifying the file system.

    ``` {.language-plaintext tabindex="-1"}
    # xfs_repair -n block-device
    ```

3.  Mount the file system:

    ``` {.language-plaintext tabindex="-1"}
    # mount file-system
    ```

    For more information see the `xfs_repair(8)`{.literal} and `xfs_metadump(8)`{.literal} man pages on your system.

### [16.5. Repairing an XFS file system with xfs_repair](#repairing-an-xfs-file-system-with-xfsrepair) {#repairing-an-xfs-file-system-with-xfs_repair .title}

Repair a corrupted XFS file system by using `xfs_repair`{.literal} on an unmounted file system, with optional log zeroing for severe corruption.

**Procedure**

1.  Create a metadata image prior to repair for diagnostic or testing purposes by using the `xfs_metadump`{.literal} utility. A pre-repair file system metadata image can be useful for supporting investigations if the corruption is due to a software bug. Patterns of corruption present in the pre-repair image can aid in root-cause analysis.

    -   Use the `xfs_metadump`{.literal} debugging tool to copy the metadata from an XFS file system to a file. The resulting `metadump`{.literal} file can be compressed by using standard compression utilities to reduce the file size if large `metadump`{.literal} files need to be sent to support.

        ``` {.language-plaintext tabindex="-1"}
        # xfs_metadump block-device metadump-file
        ```

2.  Replay the log by remounting the file system:

    ``` {.language-plaintext tabindex="-1"}
    # mount file-system
    ```

    ``` {.language-plaintext tabindex="-1"}
    # umount file-system
    ```

3.  Use the `xfs_repair`{.literal} utility to repair the unmounted file system:

    -   If the mount succeeded, no additional options are required:

        ``` {.language-plaintext tabindex="-1"}
        # xfs_repair block-device
        ```

    -   If the mount failed with the *Structure needs cleaning* error, the log is corrupted and cannot be replayed. Use the `-L`{.literal} option (*force log zeroing*) to clear the log:

        Warning

        This command causes all metadata updates in progress at the time of the crash to be lost, which might cause significant file system damage and data loss. This should be used only as a last resort if the log cannot be replayed.

        ``` {.language-plaintext tabindex="-1"}
        # xfs_repair -L block-device
        ```

4.  Mount the file system:

    ``` {.language-plaintext tabindex="-1"}
    # mount file-system
    ```

    For more information, see the `xfs_repair(8)`{.literal} man page on your system.

### [16.6. Error handling mechanisms in ext2, ext3, and ext4](#error-handling-mechanisms-in-ext2-ext3-and-ext4) {#error-handling-mechanisms-in-ext2-ext3-and-ext4 .title}

The ext2, ext3, and ext4 file systems use e2fsck for checks and repairs. The fsck.ext2, fsck.ext3, and fsck.ext4 binaries are hardlinks to e2fsck and run automatically at boot. Their behavior varies by file system type and its state.

A full file system check and repair is invoked for ext2, which is not a metadata journaling file system, and for ext4 file systems without a journal.

For ext3 and ext4 file systems with metadata journaling, the journal is replayed in userspace and the utility exits. This is the default action because journal replay ensures a consistent file system after a crash.

If these file systems encounter metadata inconsistencies while mounted, they record this fact in the file system superblock. If `e2fsck`{.literal} finds that a file system is marked with such an error, `e2fsck`{.literal} performs a full check after replaying the journal (if present).

For more information, see the `fsck(8)`{.literal} and `e2fsck(8)`{.literal} man pages on your system.

### [16.7. Checking an ext2, ext3, or ext4 file system with e2fsck](#checking-an-ext2-ext3-or-ext4-file-system-with-e2fsck) {#checking-an-ext2-ext3-or-ext4-file-system-with-e2fsck .title}

Check ext2, ext3, or ext4 file systems by using `e2fsck -n`{.literal} for a dry run that reports errors without modifications.

**Procedure**

1.  Replay the log by remounting the file system:

    ``` {.language-plaintext tabindex="-1"}
    # mount file-system
    ```

    ``` {.language-plaintext tabindex="-1"}
    # umount file-system
    ```

2.  Perform a dry run to check the file system.

    ``` {.language-plaintext tabindex="-1"}
    # e2fsck -n block-device
    ```

    Note

    Any errors are printed and an indication of the actions that would be taken, without modifying the file system. Later phases of consistency checking may print extra errors as it discovers inconsistencies which would have been fixed in early phases if it were running in repair mode.

    For more information, see the `e2image(8)`{.literal} and `e2fsck(8)`{.literal} man pages on your system.

### [16.8. Repairing an ext2, ext3, or ext4 file system with e2fsck](#repairing-an-ext2-ext3-or-ext4-file-system-with-e2fsck) {#repairing-an-ext2-ext3-or-ext4-file-system-with-e2fsck .title}

Repair corrupted ext2, ext3, or ext4 file systems by using `e2fsck -p`{.literal} for automatic repair. You can do this with optional metadata image creation for diagnostics.

**Procedure**

1.  Save a file system image for support investigations. A pre-repair file system metadata image can be useful for support investigations if the corruption is due to a software bug. Patterns of corruption present in the pre-repair image can aid in root-cause analysis.

    Note

    Severely damaged file systems may cause problems with metadata image creation.

    -   If you are creating the image for testing purposes, use the `-r`{.literal} option to create a sparse file of the same size as the file system itself. `e2fsck`{.literal} can then operate directly on the resulting file.

        ``` {.language-plaintext tabindex="-1"}
        # e2image -r block-device image-file
        ```

    -   If you are creating the image to be archived or provided for diagnostic, use the `-Q`{.literal} option, which creates a more compact file format suitable for transfer.

        ``` {.language-plaintext tabindex="-1"}
        # e2image -Q block-device image-file
        ```

2.  Replay the log by remounting the file system:

    ``` {.language-plaintext tabindex="-1"}
    # mount file-system
    ```

    ``` {.language-plaintext tabindex="-1"}
    # umount file-system
    ```

3.  Automatically repair the file system. If user intervention is required, `e2fsck`{.literal} indicates the unfixed problem in its output and reflects this status in the exit code.

    ``` {.language-plaintext tabindex="-1"}
    # e2fsck -p block-device
    ```

## [Chapter 17. Mounting file systems](#mounting-file-systems) {#chapter-17.-mounting-file-systems .title}

As a system administrator, you can mount file systems on your system to access data on them.

### [17.1. The Linux mount mechanism](#the-linux-mount-mechanism) {#the-linux-mount-mechanism .title}

On Linux and similar systems, file systems can exist on partitions or removable devices like CDs, DVDs, and USB drives. They are attached to a directory tree at a mount point and can also be detached. When mounted, the original directory content is not accessible.

Linux does not prevent you from mounting a file system to a directory with a file system already attached to it.

When mounting, you can identify the device by:

-   a universally unique identifier (UUID): for example, `UUID=34795a28-ca6d-4fd8-a347-73671d0c19cb`{.literal}
-   a volume label: for example, `LABEL=home`{.literal}
-   a full path to a non-persistent block device: for example, `/dev/sda3`{.literal}

When you mount a file system by using the `mount`{.literal} command without all required information, the command relies on defaults. This includes cases where the device name, target directory, or file system type is missing. In such cases, the `mount`{.literal} utility reads the contents of the `/etc/fstab`{.literal} file. It checks whether the given file system is listed there.

The `/etc/fstab`{.literal} file contains a list of device names and directories. These directories indicate where the selected file systems are mounted. The file also specifies the file system type and mount options. Therefore, when mounting a file system that is listed in `/etc/fstab`{.literal}, the following command syntax is sufficient.

-   Mounting by the mount point:

    ``` {.language-plaintext tabindex="-1"}
    # mount directory
    ```

-   Mounting by the block device:

    ``` {.language-plaintext tabindex="-1"}
    # mount device
    ```

### [17.2. Listing currently mounted file systems](#listing-currently-mounted-file-systems) {#listing-currently-mounted-file-systems .title}

List all currently mounted file systems on the command line by using the `findmnt`{.literal} utility.

**Procedure**

-   To list all mounted file systems, use the `findmnt`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ findmnt
    ```

-   To limit the listed file systems only to a certain file system type, add the `--types`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    $ findmnt --types fs-type
    ```

    Following is an example to list only XFS file systems:

    ``` {.language-plaintext tabindex="-1"}
    $ findmnt --types xfs
    ```

    ``` {.language-plaintext tabindex="-1"}
    TARGET  SOURCE                                                FSTYPE OPTIONS
    /       /dev/mapper/luks-5564ed00-6aac-4406-bfb4-c59bf5de48b5 xfs    rw,relatime
    ├─/boot /dev/sda1                                             xfs    rw,relatime
    └─/home /dev/mapper/luks-9d185660-7537-414d-b727-d92ea036051e xfs    rw,relatime
    ```

### [17.3. Mounting a file system with mount](#mounting-a-file-system-with-mount) {#mounting-a-file-system-with-mount .title}

You can attach a file system to a directory in the file hierarchy by using the `mount`{.literal} utility. This makes the file system accessible to users and applications.

**Prerequisites**

-   Verify that no file system is already mounted on your chosen mount point:

    ``` {.language-plaintext tabindex="-1"}
    $ findmnt mount-point
    ```

**Procedure**

1.  To attach a certain file system, use the `mount`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    # mount device mount-point
    ```

    For example, to mount a local XFS file system identified by UUID:

    ``` {.language-plaintext tabindex="-1"}
    # mount UUID=ea74bbec-536d-490c-b8d9-5b40bbd7545b /mnt/data
    ```

2.  If `mount`{.literal} cannot recognize the file system type automatically, specify it by using the `--types`{.literal} option:

    ``` {.language-plaintext tabindex="-1"}
    # mount --types type device mount-point
    ```

    For example, to mount a remote NFS file system:

    ``` {.language-plaintext tabindex="-1"}
    # mount --types nfs4 host:/remote-export /mnt/nfs
    ```

### [17.4. Moving a mount point](#moving-a-mount-point) {#moving-a-mount-point .title}

Change the mount point of a mounted file system to a different directory by using the `mount`{.literal} utility.

**Procedure**

1.  To change the directory in which a file system is mounted:

    ``` {.language-plaintext tabindex="-1"}
    # mount --move old-directory new-directory
    ```

    For example, to move the file system mounted in the `/mnt/userdirs/`{.literal} directory to the `/home/`{.literal} mount point:

    ``` {.language-plaintext tabindex="-1"}
    # mount --move /mnt/userdirs /home
    ```

2.  Verify that the file system has been moved as expected:

    ``` {.language-plaintext tabindex="-1"}
    $ findmnt
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ ls old-directory
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ ls new-directory
    ```

### [17.5. Unmounting a file system with umount](#unmounting-a-file-system-with-umount) {#unmounting-a-file-system-with-umount .title}

Unmount a file system by using the `umount`{.literal} utility.

**Procedure**

1.  Try unmounting the file system by using either of the following commands:

    -   By mount point:

        ``` {.language-plaintext tabindex="-1"}
        # umount mount-point
        ```

    -   By device:

        ``` {.language-plaintext tabindex="-1"}
        # umount device
        ```

    If the command fails with an error similar to the following, it means that the file system is in use because of a process is using resources on it:

    ``` {.language-plaintext tabindex="-1"}
    umount: /run/media/user/FlashDrive: target is busy.
    ```

2.  If the file system is in use, use the `fuser`{.literal} utility to determine which processes are accessing it. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ fuser --mount /run/media/user/FlashDrive /run/media/user/FlashDrive: 18351
    ```

    Afterwards, stop the processes by using the file system and try unmounting it again.

### [17.6. Mounting and unmounting file systems in the web console](#mounting-and-unmounting-file-systems-in-the-web-console) {#mounting-and-unmounting-file-systems-in-the-web-console .title}

To be able to use partitions on RHEL systems, you need to mount a file system on the partition as a device. You also can unmount a file system and the RHEL system will stop using it. You can delete, remove, or re-format devices by unmounting the file system.

**Prerequisites**

-   The `cockpit-storaged`{.literal} package is installed on your system.

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   If you want to unmount a file system, ensure that the system does not use any file, service, or application stored in the partition.

**Procedure**

1.  Log in to the RHEL 10 web console.
2.  Click the **Storage** tab.
3.  In the **Storage** table, select a volume from which you want to delete the partition.
4.  In the **GPT partitions** section, click the menu button, ⋮ next to the partition whose file system you want to mount or unmount.
5.  Click Mount or Unmount.

### [17.7. Common mount options](#common-mount-options) {#common-mount-options .title}

The mount utility supports various options for controlling file system behavior, access permissions, and mounting preferences across different file system types.

The following table lists the most common options of the `mount`{.literal} utility. You can apply these mount options by using the following syntax:

``` {.language-plaintext tabindex="-1"}
# mount --options option1,option2,option3 device mount-point
```

+----------------------+-------------------------------------------------------------------------------------------------------------+
| Option               | Description                                                                                                 |
+:=====================+:============================================================================================================+
| `async`{.literal}    | Enables asynchronous input and output operations on the file system.                                        |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `auto`{.literal}     | Configures the file system for automatic mounting when the `mount -a`{.literal} command is used.            |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `defaults`{.literal} | Provides an alias for the `async,auto,dev,exec,nouser,rw,suid`{.literal} options.                           |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `exec`{.literal}     | Specifies that binary files can be executed on the file system.                                             |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `loop`{.literal}     | Mounts an image as a loop device.                                                                           |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `noauto`{.literal}   | Default behavior disables the automatic mount of the file system by using the `mount -a`{.literal} command. |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `noexec`{.literal}   | Disallows the execution of binary files on the particular file system.                                      |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `nouser`{.literal}   | Disallows an ordinary user (that is, other than root) to mount and unmount the file system.                 |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `remount`{.literal}  | Remounts the file system in case it is already mounted.                                                     |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `ro`{.literal}       | Mounts the file system for reading only.                                                                    |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `rw`{.literal}       | Mounts the file system for both reading and writing.                                                        |
+----------------------+-------------------------------------------------------------------------------------------------------------+
| `user`{.literal}     | Specifies that non-root users can mount and unmount the file system.                                        |
+----------------------+-------------------------------------------------------------------------------------------------------------+

: Table 17.1. Common mount options

Show more

## [Chapter 18. Sharing a mount on multiple mount points](#sharing-a-mount-on-multiple-mount-points) {#chapter-18.-sharing-a-mount-on-multiple-mount-points .title}

As a system administrator, you can duplicate mount points to make the file systems accessible from multiple directories.

### [18.1. Types of shared mounts](#types-of-shared-mounts) {#types-of-shared-mounts .title}

There are multiple types of shared mounts that you can use. The key difference between them lies in how they behave when another file system is mounted under one of the shared mount points. These shared mounts use the *shared subtrees* feature to function.

The following mount types are available:

`private`{.literal}

:   This type does not receive or forward any propagation events.

    When you mount another file system under either the duplicate or the original mount point, it is not reflected in the other.

`shared`{.literal}

:   This type creates an exact replica of a given mount point.

    When a mount point is marked as a `shared`{.literal} mount, any mount within the original mount point is reflected in it, and vice versa.

    This is the default mount type of the root file system.

`slave`{.literal}

:   This type creates a limited duplicate of a given mount point.

    When a mount point is marked as a `slave`{.literal} mount, any mount within the original mount point is reflected in it, but no mount within a `slave`{.literal} mount is reflected in its original.

`unbindable`{.literal}
:   This type prevents the given mount point from being duplicated whatsoever.

**Additional resources**

-   [The *Shared subtrees* article on Linux Weekly News](https://lwn.net/Articles/159077/)

### [18.2. Creating a private mount point duplicate](#creating-a-private-mount-point-duplicate) {#creating-a-private-mount-point-duplicate .title}

Duplicate a mount point as a private mount. File systems that you later mount under the duplicate or the original mount point are not reflected in the other.

**Procedure**

1.  Create a virtual file system (VFS) node from the original mount point:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind original-dir original-dir
    ```

2.  Mark the original mount point as private:

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-private original-dir
    ```

    Alternatively, to change the mount type for the selected mount point and all mount points under it, use the `--make-rprivate`{.literal} option instead of `--make-private`{.literal}.

3.  Create the duplicate:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind original-dir duplicate-dir
    ```

**Example 18.1. Duplicating /media into /mnt as a private mount point**

1.  Create a VFS node from the `/media`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind /media /media
    ```

2.  Mark the `/media`{.literal} directory as private:

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-private /media
    ```

3.  Create its duplicate in `/mnt`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind /media /mnt
    ```

4.  It is now possible to verify that `/media`{.literal} and `/mnt`{.literal} share content but none of the mounts within `/media`{.literal} appear in `/mnt`{.literal}. For example, if the CD-ROM drive contains non-empty media and the `/media/cdrom/`{.literal} directory exists, use:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/cdrom /media/cdrom
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /media/cdrom
    ```

    ``` {.language-plaintext tabindex="-1"}
    EFI  GPL  isolinux  LiveOS
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /mnt/cdrom
    #
    ```

5.  It is also possible to verify that file systems mounted in the `/mnt`{.literal} directory are not reflected in `/media`{.literal}. For example, if a non-empty USB flash drive that uses the `/dev/sdc1`{.literal} device is plugged in and the `/mnt/flashdisk/`{.literal} directory is present, use:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/sdc1 /mnt/flashdisk
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /media/flashdisk
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /mnt/flashdisk
    ```

    ``` {.language-plaintext tabindex="-1"}
    en-US  publican.cfg
    ```

### [18.3. Creating a shared mount point duplicate](#creating-a-shared-mount-point-duplicate) {#creating-a-shared-mount-point-duplicate .title}

Duplicate a mount point as a shared mount. File systems that you later mount under the original directory or the duplicate are always reflected in the other.

**Procedure**

1.  Create a virtual file system (VFS) node from the original mount point:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind original-dir original-dir
    ```

2.  Mark the original mount point as shared:

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-shared original-dir
    ```

    Alternatively, to change the mount type for the selected mount point and all mount points under it, use the `--make-rshared`{.literal} option instead of `--make-shared`{.literal}.

3.  Create the duplicate:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind original-dir duplicate-dir
    ```

**Example 18.2. Duplicating /media into /mnt as a shared mount point**

To make the `/media`{.literal} and `/mnt`{.literal} directories share the same content:

1.  Create a VFS node from the `/media`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind /media /media
    ```

2.  Mark the `/media`{.literal} directory as shared:

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-shared /media
    ```

3.  Create its duplicate in `/mnt`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind /media /mnt
    ```

4.  It is now possible to verify that a mount within `/media`{.literal} also appears in `/mnt`{.literal}. For example, if the CD-ROM drive contains non-empty media and the `/media/cdrom/`{.literal} directory exists, use:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/cdrom /media/cdrom
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /media/cdrom
    ```

    ``` {.language-plaintext tabindex="-1"}
    EFI  GPL  isolinux  LiveOS
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /mnt/cdrom
    ```

    ``` {.language-plaintext tabindex="-1"}
    EFI  GPL  isolinux  LiveOS
    ```

5.  Similarly, it is possible to verify that any file system mounted in the `/mnt`{.literal} directory is reflected in `/media`{.literal}. For example, if a non-empty USB flash drive that uses the `/dev/sdc1`{.literal} device is plugged in and the `/mnt/flashdisk/`{.literal} directory is present, use:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/sdc1 /mnt/flashdisk
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /media/flashdisk
    ```

    ``` {.language-plaintext tabindex="-1"}
    en-US  publican.cfg
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /mnt/flashdisk
    ```

    ``` {.language-plaintext tabindex="-1"}
    en-US  publican.cfg
    ```

### [18.4. Creating a slave mount point duplicate](#creating-a-slave-mount-point-duplicate) {#creating-a-slave-mount-point-duplicate .title}

Duplicate a mount point as a `slave`{.literal} mount type. File systems that you later mount under the original mount point are reflected in the duplicate but not the other way around.

**Procedure**

1.  Create a virtual file system (VFS) node from the original mount point:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind original-dir original-dir
    ```

2.  Mark the original mount point as shared:

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-shared original-dir
    ```

    Alternatively, to change the mount type for the selected mount point and all mount points under it, use the `--make-rshared`{.literal} option instead of `--make-shared`{.literal}.

3.  Create the duplicate and mark it as the `slave`{.literal} type:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind original-dir duplicate-dir
    ```

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-slave duplicate-dir
    ```

**Example 18.3. Duplicating /media into /mnt as a slave mount point**

This example shows how to get the content of the `/media`{.literal} directory to appear in `/mnt`{.literal} as well, but without any mounts in the `/mnt`{.literal} directory to be reflected in `/media`{.literal}.

1.  Create a VFS node from the `/media`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind /media /media
    ```

2.  Mark the `/media`{.literal} directory as shared:

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-shared /media
    ```

3.  Create its duplicate in `/mnt`{.literal} and mark it as `slave`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind /media /mnt
    ```

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-slave /mnt
    ```

4.  Verify that a mount within `/media`{.literal} also appears in `/mnt`{.literal}. For example, if the CD-ROM drive contains non-empty media and the `/media/cdrom/`{.literal} directory exists, use:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/cdrom /media/cdrom
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /media/cdrom
    ```

    ``` {.language-plaintext tabindex="-1"}
    EFI  GPL  isolinux  LiveOS
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /mnt/cdrom
    ```

    ``` {.language-plaintext tabindex="-1"}
    EFI  GPL  isolinux  LiveOS
    ```

5.  Also verify that file systems mounted in the `/mnt`{.literal} directory are not reflected in `/media`{.literal}. For example, if a non-empty USB flash drive that uses the `/dev/sdc1`{.literal} device is plugged in and the `/mnt/flashdisk/`{.literal} directory is present, use:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/sdc1 /mnt/flashdisk
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /media/flashdisk
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls /mnt/flashdisk
    ```

    ``` {.language-plaintext tabindex="-1"}
    en-US  publican.cfg
    ```

### [18.5. Preventing a mount point from being duplicated](#preventing-a-mount-point-from-being-duplicated) {#preventing-a-mount-point-from-being-duplicated .title}

Mark a mount point as unbindable so that it is not possible to duplicate it in another mount point.

**Procedure**

-   To change the type of a mount point to an unbindable mount, use:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind mount-point mount-point
    ```

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-unbindable mount-point
    ```

    Alternatively, to change the mount type for the selected mount point and all mount points under it, use the `--make-runbindable`{.literal} option instead of `--make-unbindable`{.literal}.

    Any subsequent attempt to make a duplicate of this mount fails with the following error:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind mount-point duplicate-dir
    ```

    ``` {.language-plaintext tabindex="-1"}
    mount: wrong fs type, bad option, bad superblock on mount-point,
    missing codepage or helper program, or other error
    In some cases useful info is found in syslog - try
    dmesg | tail  or so
    ```

**Example 18.4. Preventing /media from being duplicated**

-   To prevent the `/media`{.literal} directory from being shared, use:

    ``` {.language-plaintext tabindex="-1"}
    # mount --bind /media /media
    ```

    ``` {.language-plaintext tabindex="-1"}
    # mount --make-unbindable /media
    ```

## [Chapter 19. Persistently mounting file systems](#persistently-mounting-file-systems) {#chapter-19.-persistently-mounting-file-systems .title}

As a system administrator, you can persistently mount file systems to configure non-removable storage.

### [19.1. The /etc/fstab file](#the-etc-fstab-file) {#the-etcfstab-file .title}

Use the `/etc/fstab`{.literal} configuration file to control persistent mount points of file systems. Each line in the `/etc/fstab`{.literal} file defines a mount point of a file system.

It includes the following fields separated by white space:

-   The block device identified by a persistent attribute or a path in the `/dev`{.literal} directory.
-   The directory where the device will be mounted.
-   The file system on the device.
-   Mount options for the file system, which includes the `defaults`{.literal} option to mount the partition at boot time with default options. The mount option field also recognizes the `systemd`{.literal} mount unit options in the `x-systemd.`{.literal}*`option`{.literal}* format.
-   Backup option for the `dump`{.literal} utility.
-   Check order for the `fsck`{.literal} utility.

Note

The `systemd-fstab-generator`{.literal} dynamically converts the entries from the `/etc/fstab`{.literal} file to the `systemd-mount`{.literal} units. The `systemd`{.literal} auto mounts LVM volumes from `/etc/fstab`{.literal} during manual activation unless the `systemd-mount`{.literal} unit is masked.

**Example 19.1. The `/boot`{.literal} file system in `/etc/fstab`{.literal}**

+-------------------------------------------------------+-------------------+-----------------+----------------------+---------------+---------------+
| Block device                                          | Mount point       | File system     | Options              | Backup        | Check         |
+:======================================================+:==================+:================+:=====================+:==============+:==============+
| `UUID=ea74bbec-536d-490c-b8d9-5b40bbd7545b`{.literal} | `/boot`{.literal} | `xfs`{.literal} | `defaults`{.literal} | `0`{.literal} | `0`{.literal} |
+-------------------------------------------------------+-------------------+-----------------+----------------------+---------------+---------------+

Show more

The `systemd`{.literal} service automatically generates mount units from entries in `/etc/fstab`{.literal}.

For more information, see the `fstab(5)`{.literal} and `systemd.mount(5)`{.literal} man pages on your system.

### [19.2. Adding a file system to /etc/fstab](#adding-a-file-system-to--etc-fstab) {#adding-a-file-system-to-etcfstab .title}

Configure persistent mount point for a file system in the `/etc/fstab`{.literal} configuration file.

**Procedure**

1.  Find out the Universally Unique Identifier (UUID) attribute of the file system:

    ``` {.language-plaintext tabindex="-1"}
    $ lsblk --fs storage-device
    ```

    For example, view the UUID of a partition:

    ``` {.language-plaintext tabindex="-1"}
    $ lsblk --fs /dev/sda1
    ```

    ``` {.language-plaintext tabindex="-1"}
    NAME FSTYPE LABEL UUID                                 MOUNTPOINT
    sda1 xfs    Boot  ea74bbec-536d-490c-b8d9-5b40bbd7545b /boot
    ```

2.  If the mount point directory does not exist, create it:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir --parents mount-point
    ```

3.  As root, edit the `/etc/fstab`{.literal} file and add a line for the file system, identified by the UUID.

    For example, the following shows the `/boot`{.literal} mount point in `/etc/fstab`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    UUID=ea74bbec-536d-490c-b8d9-5b40bbd7545b /boot xfs defaults 0 0
    ```

4.  Regenerate mount units so that your system registers the new configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

5.  Try mounting the file system to verify that the configuration works:

    ``` {.language-plaintext tabindex="-1"}
    # mount mount-point
    ```

**Additional resources**

-   [Overview of persistent naming attributes](#device-names-managed-by-the-udev-mechanism-in-devdisk "6.3. Device names managed by the udev mechanism in /dev/disk/")

## [Chapter 20. Mounting file systems on demand](#mounting-file-systems-on-demand) {#chapter-20.-mounting-file-systems-on-demand .title}

As a system administrator, you can configure file systems, such as NFS, to mount automatically on demand.

### [20.1. The autofs service](#the-autofs-service) {#the-autofs-service .title}

The `autofs`{.literal} service can mount and unmount file systems automatically (on-demand), therefore saving system resources. It mounts file systems such as Network File System (NFS), Andrew File System (AFS), Server Message Block File System (SMBFS), and CIFS.

One drawback of permanent mounting by using `/etc/fstab`{.literal} is that the system must dedicate resources to keep the mounted file system in place. This occurs regardless of how infrequently a user accesses it. This might affect system performance when, for example, the system is maintaining NFS mounts to many systems at one time.

An alternative to `/etc/fstab`{.literal} is to use the kernel-based `autofs`{.literal} service. It consists of:

-   A kernel module that implements a file system.
-   A user-space service that performs all of the other functions.

For more information, see the `autofs(8)`{.literal} man page on your system.

### [20.2. The autofs configuration files](#the-autofs-configuration-files) {#the-autofs-configuration-files .title}

This section describes the usage and syntax of configuration files used by the `autofs`{.literal} service.

**The master map file**

The `autofs`{.literal} service uses `/etc/auto.master`{.literal} (master map) as its default primary configuration file. This can be changed to use another supported network source and name by using the `autofs`{.literal} configuration in the `/etc/autofs.conf`{.literal} configuration file in conjunction with the Name Service Switch (NSS) mechanism.

All on-demand mount points must be configured in the master map. Mount point, host name, exported directory, and options can all be specified in a set of files (or other supported network sources) rather than configuring them manually for each host.

The master map file lists mount points controlled by `autofs`{.literal}, and their corresponding configuration files or network sources known as automount maps. The format of the master map is:

``` {.language-plaintext tabindex="-1"}
mount-point  map-name  options
```

The variables used in this format are:

*mount-point*
:   The `autofs`{.literal} mount point; for example, `/mnt/data`{.literal}.

*map-file*
:   The map source file, which contains a list of mount points and the file system location from which those mount points should be mounted.

*options*
:   If supplied, these apply to all entries in the given map, if they do not themselves have options specified.

**Example 20.1. The /etc/auto.master file**

The following is a sample line from `/etc/auto.master`{.literal} file:

``` {.language-plaintext tabindex="-1"}
/mnt/data  /etc/auto.data
```

**Map files**

Map files configure the properties of individual on-demand mount points.

The automounter creates the directories if they do not exist. If the directories exist before the automounter was started, the automounter does not remove them when it exits. If a timeout is specified, the directory is automatically unmounted if the directory is not accessed for the timeout period.

The general format of maps is similar to the master map. However, the options field appears between the mount point and the location instead of at the end of the entry as in the master map:

``` {.language-plaintext tabindex="-1"}
mount-point  options  location
```

The variables used in this format are:

*mount-point*
:   This refers to the `autofs`{.literal} mount point. This can be a single directory name for an indirect mount or the full path of the mount point for direct mounts. Each direct and indirect map entry key (*mount-point*) can be followed by a space separated list of offset directories (subdirectory names each beginning with `/`{.literal}) making them what is known as a multi-mount entry.

*options*
:   When supplied, these options are appended to the master map entry options, if any, or used instead of the master map options if the configuration entry `append_options`{.literal} is set to `no`{.literal}.

*location*
:   This refers to the file system location such as a local file system path (preceded with the Sun map format escape character `:`{.literal} for map names beginning with `/`{.literal}), an NFS file system or other valid file system location.

**Example 20.2. A map file**

The following is a sample from a map file; for example, `/etc/auto.misc`{.literal}. To use this map file for mounting under `/misc`{.literal}, add the following to the master map file `/etc/auto.master`{.literal}:

``` {.language-plaintext tabindex="-1"}
/misc        /etc/auto.misc
```

The /etc/auto.misc file contains:

``` {.language-plaintext tabindex="-1"}
payroll  -fstype=nfs4  personnel:/exports/payroll
sales    -fstype=xfs   :/dev/hda4
```

The first column in the map file indicates the `autofs`{.literal} mount point: `sales`{.literal} and `payroll`{.literal} from the server called `personnel`{.literal}. The second column indicates the options for the `autofs`{.literal} mount. The third column indicates the source of the mount.

Following the given configuration, the `autofs`{.literal} mount points are `/home/payroll`{.literal} and `/home/sales`{.literal}. The `-fstype=`{.literal} option is often omitted and is not needed if the file system is NFS, including mounts for NFSv4 if the system default is NFSv4 for NFS mounts.

By using the given configuration, if a process requires access to an `autofs`{.literal} unmounted directory such as `/home/payroll/2006/July.sxc`{.literal}, the `autofs`{.literal} service automatically mounts the directory.

**The amd map format**

The `autofs`{.literal} service recognizes map configuration in the `amd`{.literal} format as well. This is useful if you want to reuse existing automounter configuration written for the `am-utils`{.literal} service, which has been removed from Red Hat Enterprise Linux.

However, use the simpler `autofs`{.literal} format described in the previous sections.

For more information, see the: \* `autofs(5)`{.literal}, `autofs.conf(5)`{.literal}, and `auto.master(5)`{.literal} man pages on your system \* `/usr/share/doc/autofs/README.amd-maps`{.literal} file

### [20.3. Configuring autofs mount points](#configuring-autofs-mount-points) {#configuring-autofs-mount-points .title}

Configure on-demand mount points by using the `autofs`{.literal} service.

**Prerequisites**

-   Install the `autofs`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install autofs
    ```

-   Start and enable the `autofs`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now autofs
    ```

**Procedure**

1.  Create a map file for the on-demand mount point, located at `/etc/auto.`{.literal}*`identifier`{.literal}*. Replace *identifier* with a name that identifies the mount point.

2.  In the map file, enter the mount point, options, and location fields as described in [The autofs configuration files](#the-autofs-configuration-files "20.2. The autofs configuration files") section.

3.  Register the map file in the master map file, as described in [The autofs configuration files](#the-autofs-configuration-files "20.2. The autofs configuration files") section.

4.  Allow the service to re-read the configuration, so it can manage the newly configured `autofs`{.literal} mount:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload autofs.service
    ```

5.  Try accessing content in the on-demand directory:

    ``` {.language-plaintext tabindex="-1"}
    # ls automounted-directory
    ```

### [20.4. Configuring autofs to use ldap for storing and retrieving automount maps](#configuring-autofs-to-use-ldap-for-storing-and-retrieving-automount-maps) {#configuring-autofs-to-use-ldap-for-storing-and-retrieving-automount-maps .title}

You can configure the `autofs`{.literal} service to retrieve automount maps stored in an LDAP directory.

**Prerequisites**

-   The `autofs`{.literal} and `openldap`{.literal} packages are installed.
-   A Kerberos-capable service is running for secure authentication.

**Procedure**

1.  To configure LDAP access, modify the `/etc/openldap/ldap.conf`{.literal} file. Ensure that the `BASE`{.literal} and `URI`{.literal} options are set to reflect the appropriate server and base for locating automount entries.

2.  In the `/etc/autofs.conf`{.literal} file configure the LDAP schema for automount maps. By default, `autofs`{.literal} will check the commonly used schemas in the order given in the configuration file:

    ``` {.language-plaintext tabindex="-1"}
    #
    # Define the LDAP schema to used for lookups
    #
    # If no schema is set autofs checks each of the schemas
    # below in the order given to try and locate an appropriate
    # basdn for lookups. If you want to minimize the number of
    # queries to the server set the values here.
    #
    #map_object_class = nisMap
    #entry_object_class = nisObject
    #map_attribute = nisMapName
    #entry_attribute = cn
    #value_attribute = nisMapEntry
    #
    # Other common LDAP naming
    #
    #map_object_class = automountMap
    #entry_object_class = automount
    #map_attribute = ou
    #entry_attribute = cn
    #value_attribute = automountInformation
    #
    #map_object_class = automountMap
    #entry_object_class = automount
    #map_attribute = automountMapName
    #entry_attribute = automountKey
    #value_attribute = automountInformation
    ```

    Note

    You can also set these values explicitly to marginally reduce LDAP queries. You can write the attributes in both lower and upper cases in the `/etc/autofs.conf`{.literal} file.

3.  The most recently established schema for storing automount maps in LDAP is described by the `rfc2307bis`{.literal} draft. To use this schema, configure it in the `/etc/autofs.conf`{.literal} file by uncommenting and setting the appropriate value for the `ldap_schema`{.literal} option. For example, if you are using a non-standard schema or need to override the default behavior, you can specify the relevant schema attributes in the `/etc/autofs.conf`{.literal} file. The following values correspond to commonly used schema settings such as those from the `rfc2307bis`{.literal} draft:

    ``` {.language-plaintext tabindex="-1"}
    default_map_object_class = automountMap
    default_entry_object_class = automount
    default_map_attribute = automountMapName
    default_entry_attribute = automountKey
    default_value_atrribute = automountInformation
    ```

    Note that the autofs automatically detects standard schemas, and specifying these settings is typically only necessary in custom or mixed-schema environments. If used, only one complete set of schema definitions should be active.

4.  If you choose to specify a custom schema in the configuration, ensure that only one complete set of schema-related entries is active. Comment out any other to avoid conflicts. In the `rfc2307bis`{.literal} schema, the `automountKey`{.literal} attribute replaces the `cn`{.literal} attribute used in the older `rfc2307`{.literal} schema. The following is an example of a corresponding LDAP Data Interchange Format (LDIF) configuration:

    ``` {.language-plaintext tabindex="-1"}
    # auto.master, example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    dn: automountMapName=auto.master,dc=example,dc=com
    objectClass: top
    objectClass: automountMap
    automountMapName: auto.master
    ```

    ``` {.language-plaintext tabindex="-1"}
    # /home, auto.master, example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    dn: automountMapName=auto.master,dc=example,dc=com
    objectClass: automount
    automountKey: /home
    automountInformation: auto.home
    ```

    ``` {.language-plaintext tabindex="-1"}
    # auto.home, example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    dn: automountMapName=auto.home,dc=example,dc=com
    objectClass: automountMap
    automountMapName: auto.home
    ```

    ``` {.language-plaintext tabindex="-1"}
    # foo, auto.home, example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    dn: automountKey=foo,automountMapName=auto.home,dc=example,dc=com
    objectClass: automount
    automountKey: foo
    automountInformation: filer.example.com:/export/foo
    ```

    ``` {.language-plaintext tabindex="-1"}
    # /, auto.home, example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    dn: automountKey=/,automountMapName=auto.home,dc=example,dc=com
    objectClass: automount
    automountKey: /
    automountInformation: filer.example.com:/export/&
    ```

5.  To allow authentication from an LDAP server, edit the `/etc/autofs_ldap_auth.conf`{.literal} file:

    a.  Change `authrequired`{.literal} to yes.

    b.  Set the principal to the Kerberos host principal for the LDAP server, `host/FQDN@REALM`{.literal}. The principal name is used to connect to the directory as part of GSS client authentication:

        ``` {.language-plaintext tabindex="-1"}
        <autofs_ldap_sasl_conf
             usetls="no"
             tlsrequired="no"
             authrequired="yes"
             authtype="GSSAPI"
        clientprinc="host/server.example.com@EXAMPLE.COM"/>
             secret="<ldap password>"/>
        ```

        For more information about host principal, see [Using canonicalized DNS host names in IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/working_with_dns_in_identity_management/using-canonicalized-dns-host-names-in-idm). You can also run `klist -k`{.literal} to get the exact host principal information.

**Additional resources**

-   [The `rfc2307bis`{.literal} draft](https://tools.ietf.org/html/draft-howard-rfc2307bis)

### [20.5. Automounting NFS server user home directories with autofs service](#automounting-nfs-server-user-home-directories-with-autofs-service) {#automounting-nfs-server-user-home-directories-with-autofs-service .title}

Configure the **autofs** service to mount user home directories automatically.

**Prerequisites**

-   The **autofs** package is installed.
-   The **autofs** service is enabled and running.

**Procedure**

1.  Define the mount point and the local automount map by editing the `/etc/auto.master`{.literal} file on the server where you want to mount user home directories, and add:

    ``` {.language-plaintext tabindex="-1"}
    /home /etc/auto.home
    ```

2.  Create the local automount map file `/etc/auto.home`{.literal} on the server where you need to mount user home directories, and add:

    ``` {.language-plaintext tabindex="-1"}
    * -fstype=nfs,rw,sync host.example.com:/home/&
    ```

    You can skip *`fstype`{.literal}* parameter, as it is *`nfs`{.literal}* by default. For more information, see `autofs(5)`{.literal} man page on your system.

3.  Reload the `autofs`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl reload autofs
    ```

### [20.6. Overriding or augmenting autofs site configuration files](#overriding-or-augmenting-autofs-site-configuration-files) {#overriding-or-augmenting-autofs-site-configuration-files .title}

It is sometimes useful to override site defaults for a specific mount point on a client system.

**Initial conditions:**

For example, consider the following conditions:

-   `nsswitch`{.literal} tells autofs which services to check for maps.

-   The map you want to augment or add to is named `auto.home`{.literal}.

-   The `auto.home`{.literal} map is stored in `ldap`{.literal} and the `/etc/nsswitch.conf`{.literal} has the following directive:

    ``` {.language-plaintext tabindex="-1"}
    automount: files ldap
    ```

-   The `/etc/auto.master`{.literal} map file contains:

    ``` {.language-plaintext tabindex="-1"}
    /home /etc/auto.home
    ```

-   The map /etc/auto.home\` file contains:

    ``` {.language-plaintext tabindex="-1"}
    *  fileserver.example.com:/export/home/&
    ```

**Using plus map inclusion:**

To read the centrally managed `auto.home`{.literal} map through `nsswitch`{.literal}, remove the wildcard map entry `* fileserver.example.com:/export/home/&`{.literal} from the local `/etc/auto.home`{.literal} file and replace it with `+auto.home`{.literal}.

Note

Plus map inclusion can only be used in local maps. When `autofs`{.literal} encounters the `files`{.literal} source through a plus map inclusion, it skips it if the included map name is identical to the map currently being read. In this case, since both are `auto.home`{.literal}, `autofs`{.literal} proceeds to the next source defined in `nsswitch.conf`{.literal}, which is `ldap`{.literal}. If a wildcard map entry is present in the map, it does not affect the directory listing, even when browse mode is enabled. This is because `autofs`{.literal} does not know what the wildcard might match when a lookup is done. As a result, it cannot create mount point directories in advance.

**Overriding or Adding Entries**

To override or add specific entries locally, place them before the `+auto.home`{.literal} line in `/etc/auto.home`{.literal}. For example the `/etc/auto.home`{.literal} file would look like:

``` {.language-plaintext tabindex="-1"}
mydir  someserver:/export/mydir

+auto.home
```

Note

To display local entries like mydir when listing /home, enable browse mode by setting browse_mode = yes in /etc/autofs.conf. Wildcard entries (like \*) do not appear in directory listings unless accessed.

### [20.7. Using systemd.automount to mount a file system on-demand with /etc/fstab](#using-systemd-automount-to-mount-a-file-system-on-demand-with--etc-fstab) {#using-systemd.automount-to-mount-a-file-system-on-demand-with-etcfstab .title}

Mount a file system on-demand by using the automount systemd units when mount point is defined in `/etc/fstab`{.literal}. You have to add an automount unit for each mount and enable it.

**Procedure**

1.  Add required `fstab`{.literal} entry as documented in [Persistently mounting file systems](#the-etc-fstab-file "19.1. The /etc/fstab file"). For example:

    ``` {.language-plaintext tabindex="-1"}
    /dev/disk/by-id/da875760-edb9-4b82-99dc-5f4b1ff2e5f4  /mount/point  xfs  defaults  0 0
    ```

2.  Add `x-systemd.automount`{.literal} to the options field of entry created in the previous step.

3.  Load newly created units so that your system registers the new configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

4.  Start the automount unit:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start mount-point.automount
    ```

**Verification**

1.  Check that *`mount-point.automount`{.literal}* is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status mount-point.automount
    ```

2.  Check that automounted directory has required content:

    ``` {.language-plaintext tabindex="-1"}
    # ls /mount/point
    ```

### [20.8. Using systemd.automount to mount a file system on-demand with a mount unit](#using-systemd-automount-to-mount-a-file-system-on-demand-with-a-mount-unit) {#using-systemd.automount-to-mount-a-file-system-on-demand-with-a-mount-unit .title}

Mount a file system on-demand by using the `automount`{.literal} systemd units when mount point is defined by a mount unit. You have to add an automount unit for each mount and enable it.

**Procedure**

1.  Create a mount unit. For example:

    ``` {.language-plaintext tabindex="-1"}
    mount-point.mount
    [Mount]
    What=/dev/disk/by-uuid/f5755511-a714-44c1-a123-cfde0e4ac688
    Where=/mount/point
    Type=xfs
    ```

2.  Create a unit file with the same name as the mount unit, but with extension `.automount`{.literal}.

3.  Open the file and create an `[Automount]`{.literal} section. Set the `Where=`{.literal} option to the mount path:

    ``` {.language-plaintext tabindex="-1"}
    [Automount]
    Where=/mount/point
    [Install]
    WantedBy=multi-user.target
    ```

4.  Load newly created units so that your system registers the new configuration:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl daemon-reload
    ```

5.  Enable and start the automount unit instead:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now mount-point.automount
    ```

**Verification**

1.  Check that *`mount-point.automount`{.literal}* is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status mount-point.automount
    ```

2.  Check that automounted directory has required content:

    ``` {.language-plaintext tabindex="-1"}
    # ls /mount/point
    ```

**Additional resources**

-   [Managing systemd](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/working-with-systemd-unit-files)

## [Chapter 21. Using SSSD component from IdM to cache the autofs maps](#using-sssd-component-from-idm-to-cache-the-autofs-maps) {#chapter-21.-using-sssd-component-from-idm-to-cache-the-autofs-maps .title}

The System Security Services Daemon (SSSD) is a system service to access remote service directories and authentication mechanisms. Data caching is useful when network connectivity is slow. You can configure the SSSD service to cache autofs maps.

### [21.1. Configuring SSSD to cache autofs maps](#configuring-sssd-to-cache-autofs-maps) {#configuring-sssd-to-cache-autofs-maps .title}

The System Security Services Daemon (SSSD) service can cache `autofs`{.literal} maps stored on an Identity Management (IdM) server. It avoids the need to configure `autofs`{.literal} to directly use the IdM server.

**Prerequisites**

-   The `sssd`{.literal} package is installed.

**Procedure**

1.  Open the SSSD configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # vim /etc/sssd/sssd.conf
    ```

2.  Add the `autofs`{.literal} service to the list of services handled by SSSD.

    ``` {.language-plaintext tabindex="-1"}
    [sssd]
    domains = ldap
    services = nss,pam,autofs
    ```

3.  Create a new `[autofs]`{.literal} section. You can leave this blank, because the default settings for an `autofs`{.literal} service work with most infrastructures.

    ``` {.language-plaintext tabindex="-1"}
    [nss]

    [pam]

    [sudo]

    [autofs]

    [ssh]

    [pac]
    ```

    For more information, see the `sssd.conf`{.literal} man page on your system.

4.  Optional: Set a search base for the `autofs`{.literal} entries. By default, this is the Lightweight Directory Access Protocol (LDAP) search base. A subtree can be specified in the `ldap_autofs_search_base`{.literal} parameter.

    ``` {.language-plaintext tabindex="-1"}
    [domain/EXAMPLE]

    ldap_search_base = "dc=example,dc=com"
    ldap_autofs_search_base = "ou=automount,dc=example,dc=com"
    ```

5.  Restart SSSD service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart sssd.service
    ```

6.  Check the `/etc/nsswitch.conf`{.literal} file, so that SSSD is listed as a source for automount configuration:

    ``` {.language-plaintext tabindex="-1"}
    automount: sss files
    ```

7.  Restart `autofs`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart autofs.service
    ```

8.  Test the configuration by listing a user's `/home`{.literal} directory, assuming there is a master map entry for `/home`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # ls /home/userName
    ```

    If this does not mount the remote file system, check the `/var/log/messages`{.literal} file for errors. If necessary, increase the debug level in the `/etc/sysconfig/autofs`{.literal} file by setting the `logging`{.literal} parameter to `debug`{.literal}.

## [Chapter 22. Setting read-only permissions for the root file system](#setting-read-only-permissions-for-the-root-file-system) {#chapter-22.-setting-read-only-permissions-for-the-root-file-system .title}

Sometimes, you need to mount the root file system (`/`{.literal}) with read-only permissions. For example, to enhance security or to ensure data integrity after an unexpected system power-off.

### [22.1. Files and directories that always retain write permissions](#files-and-directories-that-always-retain-write-permissions) {#files-and-directories-that-always-retain-write-permissions .title}

For the system to function properly, some files and directories need to retain write permissions. When the root file system is mounted in read-only mode, these files are mounted in RAM by using the `tmpfs`{.literal} temporary file system.

The default set of such files and directories is read from the `/etc/rwtab`{.literal} file. Note that the `readonly-root`{.literal} package is required to have this file present in your system.

``` {.language-plaintext tabindex="-1"}
dirs /var/cache/man
dirs    /var/gdm
<content truncated>

empty   /tmp
empty   /var/cache/foomatic
<content truncated>

files   /etc/adjtime
files   /etc/ntp.conf
<content truncated>
```

Entries in the `/etc/rwtab`{.literal} file follow this format:

``` {.language-plaintext tabindex="-1"}
copy-method    path
```

In this syntax:

-   Replace *copy-method* with one of the keywords specifying how the file or directory is copied to tmpfs.
-   Replace *path* with the path to the file or directory.

The `/etc/rwtab`{.literal} file recognizes the following ways in which a file or directory can be copied to `tmpfs`{.literal}:

`empty`{.literal}

:   An empty path is copied to `tmpfs`{.literal}. For example:

    ``` {.language-plaintext tabindex="-1"}
    empty /tmp
    ```

`dirs`{.literal}

:   A directory tree is copied to `tmpfs`{.literal}, empty. For example:

    ``` {.language-plaintext tabindex="-1"}
    dirs /var/run
    ```

`files`{.literal}

:   A file or a directory tree is copied to `tmpfs`{.literal} intact. For example:

    ``` {.language-plaintext tabindex="-1"}
    files /etc/resolv.conf
    ```

The same format applies when adding custom paths to `/etc/rwtab.d/`{.literal}.

### [22.2. Configuring the root file system to mount with read-only permissions on boot](#configuring-the-root-file-system-to-mount-with-read-only-permissions-on-boot) {#configuring-the-root-file-system-to-mount-with-read-only-permissions-on-boot .title}

Configure the root file system to mount as read-only on boot by modifying kernel options, `fstab`{.literal}, and read-only root settings.

**Procedure**

1.  In the `/etc/sysconfig/readonly-root`{.literal} file, set the `READONLY`{.literal} option to `yes`{.literal} to mount the file systems as read-only:

    ``` {.language-plaintext tabindex="-1"}
    READONLY=yes
    ```

2.  Add the `ro`{.literal} option in the root entry (`/`{.literal}) in the `/etc/fstab`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    /dev/mapper/luks-c376919e...  /  xfs  x-systemd.device-timeout=0,ro  1  1
    ```

3.  Enable the `ro`{.literal} kernel option:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=ALL --args="ro"
    ```

4.  Ensure that the `rw`{.literal} kernel option is disabled:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --update-kernel=ALL --remove-args="rw"
    ```

5.  If you need to add files and directories to be mounted with write permissions in the `tmpfs`{.literal} file system, create a text file in the `/etc/rwtab.d/`{.literal} directory and put the configuration there.

    For example, to mount the `/etc/example/file`{.literal} file with write permissions, add this line to the `/etc/rwtab.d/example`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    files /etc/example/file
    ```

    Important

    Changes made to files and directories in `tmpfs`{.literal} do not persist across boots.

6.  Reboot the system to apply the changes.

**Troubleshooting**

-   If you mount the root file system with read-only permissions by mistake, you can remount it with read-and-write permissions again by using the following command:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o remount,rw /
    ```

## [Chapter 23. Limiting storage space usage on XFS with quotas](#limiting-storage-space-usage-on-xfs-with-quotas) {#chapter-23.-limiting-storage-space-usage-on-xfs-with-quotas .title}

Implement disk quotas to restrict storage for users or groups and set warning levels. XFS quotas manage disk space (blocks) and inodes at user, group, directory, or project level. Per-project quotas control directory hierarchy disk usage.

### [23.1. Disk quotas](#disk-quotas) {#disk-quotas .title}

Disk quotas are limits that control how much disk space users and groups can consume on a file system. They help prevent any single user from using all available storage space and provide fair resource allocation across multiple users.

In most computing environments, disk space is not infinite. The quota subsystem provides a mechanism to control usage of disk space.

You can configure disk quotas for individual users as well as user groups on the local file systems. This makes it possible to manage space for user-specific files, such as email, separately from space for projects. The quota subsystem warns users when they exceed their allotted limit, but allows extra space for current work (hard limit/soft limit).

If quotas are implemented, you need to check if the quotas are exceeded and make sure the quotas are accurate. If users repeatedly exceed quotas or consistently reach soft limits, a system administrator can help them use less disk space. Alternatively, the administrator can increase the user's disk quota.

You can set quotas to control:

-   The number of consumed disk blocks.
-   The number of inodes, which are data structures that contain information about files in UNIX file systems. Because inodes store file-related information, this allows control over the number of files that can be created.

### [23.2. The xfs_quota tool](#the-xfs_quota-tool) {#the-xfs_quota-tool .title}

You can use the `xfs_quota`{.literal} tool to manage quotas on XFS file systems. In addition, you can use XFS file systems with limit enforcement turned off as an effective disk usage accounting system.

The XFS quota system differs from other file systems in a number of ways. Most importantly, XFS considers quota information as file system metadata and uses journaling to provide a higher level guarantee of consistency.

For more information, see the `xfs_quota(8)`{.literal} man page on your system.

### [23.3. File system quota management in XFS](#file-system-quota-management-in-xfs) {#file-system-quota-management-in-xfs .title}

The XFS quota subsystem manages limits on disk space (blocks) and file (inode) usage. XFS quotas control or report on usage of these items on a user, group, or directory or project level. Group and project quotas are only mutually exclusive on older non-default XFS disk formats.

When managing on a per-directory or per-project basis, XFS manages the disk usage of directory hierarchies associated with a specific project.

### [23.4. Enabling disk quotas for XFS](#enabling-disk-quotas-for-xfs) {#enabling-disk-quotas-for-xfs .title}

Enable disk quotas for users, groups, and projects on an XFS file system. Once quotas are enabled, the `xfs_quota`{.literal} tool can be used to set limits and report on disk usage.

**Procedure**

1.  Enable quotas for users:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o uquota /dev/xvdb1 /xfs
    ```

    Replace `uquota`{.literal} with `uqnoenforce`{.literal} to allow usage reporting without enforcing any limits.

2.  Enable quotas for groups:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o gquota /dev/xvdb1 /xfs
    ```

    Replace `gquota`{.literal} with `gqnoenforce`{.literal} to allow usage reporting without enforcing any limits.

3.  Enable quotas for projects:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o pquota /dev/xvdb1 /xfs
    ```

    Replace `pquota`{.literal} with `pqnoenforce`{.literal} to allow usage reporting without enforcing any limits.

4.  Alternatively, include the quota mount options in the `/etc/fstab`{.literal} file. The following example shows entries in the `/etc/fstab`{.literal} file to enable quotas for users, groups, and projects, respectively, on an XFS file system. These examples also mount the file system with read/write permissions:

    ``` {.language-plaintext tabindex="-1"}
    # vim /etc/fstab
    ```

    ``` {.language-plaintext tabindex="-1"}
    /dev/xvdb1    /xfs    xfs    rw,quota       0  0
    /dev/xvdb1    /xfs    xfs    rw,gquota      0  0
    /dev/xvdb1    /xfs    xfs    rw,prjquota    0  0
    ```

    For more information, see the `xfs(5)`{.literal} and `xfs_quota(8)`{.literal} man pages on your system.

### [23.5. Reporting XFS usage](#reporting-xfs-usage) {#reporting-xfs-usage .title}

Use the `xfs_quota`{.literal} tool to set limits and report on disk usage. By default, `xfs_quota`{.literal} is run interactively, and in basic mode. Basic mode subcommands report usage, and are available to all users.

**Prerequisites**

-   Quotas have been enabled for the XFS file system. See [Enabling disk quotas for XFS](#enabling-disk-quotas-for-xfs "23.4. Enabling disk quotas for XFS").

**Procedure**

1.  Start the `xfs_quota`{.literal} shell:

    ``` {.language-plaintext tabindex="-1"}
    # xfs_quota
    ```

2.  Show usage and limits for the given user:

    ``` {.language-plaintext tabindex="-1"}
    xfs_quota> quota username
    ```

3.  Show free and used counts for blocks and inodes:

    ``` {.language-plaintext tabindex="-1"}
    xfs_quota> df
    ```

4.  Run the help command to display the basic commands available with `xfs_quota`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    xfs_quota> help
    ```

5.  Specify `q`{.literal} to exit `xfs_quota`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    xfs_quota> q
    ```

    For more information, see the `xfs_quota(8)`{.literal} man page on your system.

### [23.6. Modifying XFS quota limits](#modifying-xfs-quota-limits) {#modifying-xfs-quota-limits .title}

Start the `xfs_quota`{.literal} tool with the `-x`{.literal} option to enable expert mode and run the administrator commands to modify the quota system. The subcommands of this mode allow actual configuration of limits, and are available only to users with elevated privileges.

**Prerequisites**

-   Quotas have been enabled for the XFS file system. See [Enabling disk quotas for XFS](#enabling-disk-quotas-for-xfs "23.4. Enabling disk quotas for XFS").

**Procedure**

1.  Start the `xfs_quota`{.literal} shell with the `-x`{.literal} option to enable expert mode:

    ``` {.language-plaintext tabindex="-1"}
    # xfs_quota -x /path
    ```

2.  Report quota information for a specific file system:

    ``` {.language-plaintext tabindex="-1"}
    xfs_quota> report /path
    ```

    For example, to display a sample quota report for `/home`{.literal} (on `/dev/blockdevice`{.literal}), use the command `report -h /home`{.literal}. This displays output similar to the following:

    ``` {.language-plaintext tabindex="-1"}
    User quota on /home (/dev/blockdevice)
    Blocks
    User ID      Used   Soft   Hard Warn/Grace
    ---------- ---------------------------------
    root            0      0      0  00 [------]
    testuser   103.4G      0      0  00 [------]
    ```

3.  Modify quota limits:

    ``` {.language-plaintext tabindex="-1"}
    xfs_quota> limit isoft=500m ihard=700m user
    ```

    For example, to set a soft and hard inode count limit of 500 and 700 respectively for user `john`{.literal}, whose home directory is `/home/john`{.literal}, use the following command:

    ``` {.language-plaintext tabindex="-1"}
    # xfs_quota -x -c 'limit isoft=500 ihard=700 john' /home/
    ```

    In this case, pass `mount_point`{.literal} which is the mounted xfs file system.

4.  Display the expert commands available with `xfs_quota -x`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    xfs_quota> help
    ```

**Verification**

-   Verify that the quota limits have been modified:

    ``` {.language-plaintext tabindex="-1"}
    xfs_quota> report -i -u
    ```

    ``` {.language-plaintext tabindex="-1"}
    User quota on /home (/dev/loop0)
                                   Inodes
    User ID          Used       Soft       Hard    Warn/ Grace
    ---------- --------------------------------------------------
    root                3          0          0     00 [------]
    testuser            2        500        700     00 [------]
    ```

    For more information, see the xfs_quota(8)\` man page on your system.

### [23.7. Setting project limits for XFS](#setting-project-limits-for-xfs) {#setting-project-limits-for-xfs .title}

Configure limits for project-controlled directories.

**Procedure**

1.  Add the project-controlled directories to `/etc/projects`{.literal}. For example, the following adds the `/var/log`{.literal} path with a unique ID of 11 to `/etc/projects`{.literal}. Your project ID can be any numerical value mapped to your project.

    ``` {.language-plaintext tabindex="-1"}
    # echo 11:/var/log >> /etc/projects
    ```

2.  Add project names to `/etc/projid`{.literal} to map project IDs to project names. For example, the following associates a project called `logfiles`{.literal} with the project ID of 11 as defined in the previous step.

    ``` {.language-plaintext tabindex="-1"}
    # echo logfiles:11 >> /etc/projid
    ```

3.  Initialize the project directory. For example, the following initializes the project directory `/var`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # xfs_quota -x -c 'project -s logfiles' /var
    ```

4.  Configure quotas for projects with initialized directories:

    ``` {.language-plaintext tabindex="-1"}
    # xfs_quota -x -c 'limit -p bhard=1g logfiles' /var
    ```

    For more information, see the `xfs_quota(8)`{.literal}, `projid(5)`{.literal}, and `projects(5)`{.literal} man pages on your system.

## [Chapter 24. Limiting storage space usage on ext4 with quotas](#limiting-storage-space-usage-on-ext4-with-quotas) {#chapter-24.-limiting-storage-space-usage-on-ext4-with-quotas .title}

You have to enable disk quotas on your system before you can assign them. You can assign disk quotas per user, per group or per project. However, if there is a soft limit set, you can exceed these quotas for a configurable period of time, known as the grace period.

### [24.1. Installing the quota tool](#installing-the-quota-tool) {#installing-the-quota-tool .title}

You must install the `quota`{.literal} RPM package to implement disk quotas.

**Procedure**

-   Install the `quota`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install quota
    ```

### [24.2. Enabling quota feature on file system creation](#enabling-quota-feature-on-file-system-creation) {#enabling-quota-feature-on-file-system-creation .title}

You can enable the disk quota feature when creating an ext4 file system. This allows you to enforce storage limits for users, groups, or projects.

**Procedure**

1.  Enable quotas on file system creation:

    ``` {.language-plaintext tabindex="-1"}
    # mkfs.ext4 -O quota /dev/sda
    ```

    Note

    Only user and group quotas are enabled and initialized by default.

2.  Change the defaults on file system creation:

    ``` {.language-plaintext tabindex="-1"}
    # mkfs.ext4 -O quota -E quotatype=usrquota:grpquota:prjquota /dev/sda
    ```

3.  Mount the file system:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/sda
    ```

### [24.3. Enabling quota feature on existing file systems](#enabling-quota-feature-on-existing-file-systems) {#enabling-quota-feature-on-existing-file-systems .title}

Enable the quota feature on existing file system by using the `tune2fs`{.literal} command.

**Procedure**

1.  Unmount the file system:

    ``` {.language-plaintext tabindex="-1"}
    # umount /dev/sda
    ```

2.  Enable quotas on existing file system:

    ``` {.language-plaintext tabindex="-1"}
    # tune2fs -O quota /dev/sda
    ```

    Note

    Only user and group quotas are initialized by default.

3.  Change the defaults:

    ``` {.language-plaintext tabindex="-1"}
    # tune2fs -Q usrquota,grpquota,prjquota /dev/sda
    ```

4.  Mount the file system:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/sda
    ```

### [24.4. Enabling quota enforcement](#enabling-quota-enforcement) {#enabling-quota-enforcement .title}

The quota accounting is enabled by default after mounting the file system without any additional options, but quota enforcement is not.

**Prerequisites**

-   Quota feature is enabled and the default quotas are initialized.

**Procedure**

-   Enable quota enforcement by `quotaon`{.literal} for the user quota:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/sda /mnt
    ```

    ``` {.language-plaintext tabindex="-1"}
    # quotaon /mnt
    ```

    Note

    The quota enforcement can be enabled at mount time by using `usrquota`{.literal}, `grpquota`{.literal}, or `prjquota`{.literal} mount options.

    ``` {.language-plaintext tabindex="-1"}
    # mount -o usrquota,grpquota,prjquota /dev/sda /mnt
    ```

-   Enable user, group, and project quotas for all file systems:

    ``` {.language-plaintext tabindex="-1"}
    # quotaon -vaugP
    ```

    -   If neither of the `-u`{.literal}, `-g`{.literal}, or `-P`{.literal} options are specified, only the user quotas are enabled.
    -   If only `-g`{.literal} option is specified, only group quotas are enabled.
    -   If only `-P`{.literal} option is specified, only project quotas are enabled.

-   Enable quotas for a specific file system, such as `/home`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # quotaon -vugP /home
    ```

### [24.5. Assigning quotas per user](#assigning-quotas-per-user) {#assigning-quotas-per-user .title}

The disk quotas are assigned to users with the `edquota`{.literal} command.

Note

The text editor defined by the `EDITOR`{.literal} environment variable is used by `edquota`{.literal}. To change the editor, set the `EDITOR`{.literal} environment variable in your `~/.bash_profile`{.literal} file to the full path of the required editor.

**Prerequisites**

-   User must exist prior to setting the user quota.

**Procedure**

1.  Assign the quota for a user:

    ``` {.language-plaintext tabindex="-1"}
    # edquota username
    ```

    Replace *username* with the user to which you want to assign the quotas.

    For example, if you enable a quota for the `/dev/sda`{.literal} partition and run the command `edquota testuser`{.literal}, the default editor displays the following:

    ``` {.language-plaintext tabindex="-1"}
    Disk quotas for user testuser (uid 501):
    Filesystem   blocks   soft   hard   inodes   soft   hard
    /dev/sda      44043      0      0    37418      0      0
    ```

2.  Change the required limits.

    If any of the values are set to 0, limit is not set. Change them in the text editor.

    For example, the following shows the soft and hard block limits for the testuser have been set to 50000 and 55000 respectively.

    ``` {.language-plaintext tabindex="-1"}
    Disk quotas for user testuser (uid 501):
    Filesystem   blocks   soft   hard   inodes   soft   hard
    /dev/sda      44043  50000  55000    37418      0      0
    ```

    -   The first column is the name of the file system that has a quota enabled for it.

    -   The second column shows how many blocks the user is currently using.

    -   The next two columns are used to set soft and hard block limits for the user on the file system.

    -   The `inodes`{.literal} column shows how many inodes the user is currently using.

    -   The last two columns are used to set the soft and hard inode limits for the user on the file system.

        -   The hard block limit is the absolute maximum amount of disk space that a user or group can use. Once this limit is reached, no further disk space can be used.
        -   The soft block limit defines the maximum amount of disk space that can be used. However, unlike the hard limit, the soft limit can be exceeded for a certain amount of time. That time is known as the *grace period*. The grace period can be expressed in seconds, minutes, hours, days, weeks, or months.

**Verification**

-   Verify that the quota for the user has been set:

    ``` {.language-plaintext tabindex="-1"}
    # quota -v testuser
    ```

    ``` {.language-plaintext tabindex="-1"}
    Disk quotas for user testuser:
    Filesystem  blocks  quota  limit  grace  files  quota  limit  grace
    /dev/sda      1000*  1000   1000             0      0      0
    ```

### [24.6. Assigning quotas per group](#assigning-quotas-per-group) {#assigning-quotas-per-group .title}

You can assign disk quotas on a per-group basis to limit the storage space and number of inodes available to a specific group.

**Prerequisites**

-   Group must exist prior to setting the group quota.

**Procedure**

1.  Set a group quota:

    ``` {.language-plaintext tabindex="-1"}
    # edquota -g groupname
    ```

    For example, to set a group quota for the `devel`{.literal} group:

    ``` {.language-plaintext tabindex="-1"}
    # edquota -g devel
    ```

    This command displays the existing quota for the group in the text editor:

    ``` {.language-plaintext tabindex="-1"}
    Disk quotas for group devel (gid 505):
    Filesystem   blocks  soft  hard  inodes  soft  hard
    /dev/sda     440400     0     0   37418     0     0
    ```

2.  Modify the limits and save the file.

**Verification**

-   Verify that the group quota is set:

    ``` {.language-plaintext tabindex="-1"}
    # quota -vg groupname
    ```

### [24.7. Assigning quotas per project](#assigning-quotas-per-project) {#assigning-quotas-per-project .title}

You can assign disk quotas per project to control how much storage space a specific project directory consumes on a file system.

**Prerequisites**

-   Project quota is enabled on your file system.

**Procedure**

1.  Add the project-controlled directories to `/etc/projects`{.literal}. For example, the following adds the `/var/log`{.literal} path with a unique ID of 11 to `/etc/projects`{.literal}. Your project ID can be any numerical value mapped to your project.

    ``` {.language-plaintext tabindex="-1"}
    # echo 11:/var/log >> /etc/projects
    ```

2.  Add project names to `/etc/projid`{.literal} to map project IDs to project names. For example, the following associates a project called `Logs`{.literal} with the project ID of 11 as defined in the previous step.

    ``` {.language-plaintext tabindex="-1"}
    # echo Logs:11 >> /etc/projid
    ```

3.  Set the required limits:

    ``` {.language-plaintext tabindex="-1"}
    # edquota -P 11
    ```

    Note

    You can choose the project either by its project ID (`11`{.literal} in this case), or by its name (`Logs`{.literal} in this case).

4.  Using `quotaon`{.literal}, enable quota enforcement:

    See [Enabling quota enforcement](#enabling-quota-enforcement "24.4. Enabling quota enforcement").

**Verification**

-   Verify that the project quota is set:

    ``` {.language-plaintext tabindex="-1"}
    # quota -vP 11
    ```

    Note

    You can verify either by the project ID, or by the project name.

    For more information, see the `edquota(8)`{.literal}, `projid(5)`{.literal}, and `projects(5)`{.literal} man pages on your system.

### [24.8. Setting the grace period for soft limits](#setting-the-grace-period-for-soft-limits) {#setting-the-grace-period-for-soft-limits .title}

If a given quota has soft limits, you can edit the grace period. The grace period is the amount of time a soft limit can be exceeded.

You can set the grace period for users, groups, or projects.

**Procedure**

-   Edit the grace period:

    ``` {.language-plaintext tabindex="-1"}
    # edquota -t
    ```

    Important

    Other `edquota`{.literal} commands operate on quotas for a particular user, group, or project. However, the `-t`{.literal} option operates on every file system with quotas enabled.

### [24.9. Turning file system quotas off](#turning-file-system-quotas-off) {#turning-file-system-quotas-off .title}

Use `quotaoff`{.literal} to turn disk quota enforcement off on the specified file systems. Quota accounting stays enabled after running this command.

**Procedure**

-   To turn all user and group quotas off:

    ``` {.language-plaintext tabindex="-1"}
    # quotaoff -vaugP
    ```

    -   If neither of the `-u`{.literal}, `-g`{.literal}, or `-P`{.literal} options are specified, only the user quotas are disabled.

    -   If only `-g`{.literal} option is specified, only group quotas are disabled.

    -   If only `-P`{.literal} option is specified, only project quotas are disabled.

    -   The `-v`{.literal} switch causes verbose status information to display as the command executes.

        For more information, see the `quotaoff(8)`{.literal} man page on your system.

### [24.10. Reporting on disk quotas](#reporting-on-disk-quotas) {#reporting-on-disk-quotas .title}

Create a disk quota report by using the `repquota`{.literal} utility.

**Procedure**

1.  Run the `repquota`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    # repquota
    ```

    For example, the command `repquota /dev/sda`{.literal} produces this output:

    ``` {.language-plaintext tabindex="-1"}
    *** Report for user quotas on device /dev/sda
    Block grace time: 7days; Inode grace time: 7days
                Block limits            File limits
    User        used    soft    hard    grace   used    soft    hard    grace
    ----------------------------------------------------------------------
    root      --      36       0       0              4     0     0
    kristin   --     540       0       0            125     0     0
    testuser  --  440400  500000  550000          37418     0     0
    ```

2.  View the disk usage report for all quota-enabled file systems:

    ``` {.language-plaintext tabindex="-1"}
    # repquota -augP
    ```

    The `--`{.literal} symbol displayed after each user determines whether the block or inode limits have been exceeded. If either soft limit is exceeded, a `+`{.literal} character appears in place of the corresponding `-`{.literal} character. The first `-`{.literal} character represents the block limit, and the second represents the inode limit.

    The `grace`{.literal} columns are normally blank. If a soft limit has been exceeded, the column contains a time specification equal to the amount of time remaining on the grace period. If the grace period has expired, `none`{.literal} appears in its place.

    For more information, see the `repquota(8)`{.literal} man page for more information.

## [Chapter 25. Discarding unused blocks](#discarding-unused-blocks) {#chapter-25.-discarding-unused-blocks .title}

Discard operations improve storage performance and lifespan by informing the storage device which blocks are no longer in use. It allows SSDs to optimize wear leveling and enabling thin-provisioned storage to reclaim space.

**Prerequisites**

-   The block device underlying the file system must support physical discard operations.

    Physical discard operations are supported if the value in the `/sys/block/`{.literal}*`<device>`{.literal}*`/queue/discard_max_bytes`{.literal} file is not zero.

### [25.1. Types of block discard operations](#types-of-block-discard-operations) {#types-of-block-discard-operations .title}

Block discard operations can be performed by using batch, online, or periodic methods, each with specific use cases and performance recommendations.

The following list describes the various discard operations:

Batch discard
:   This type of discard is part of the `fstrim`{.literal} command. It discards all unused blocks in a file system that match criteria specified by the administrator. Red Hat Enterprise Linux 10 supports batch discard on XFS and ext4 formatted devices that support physical discard operations.

Online discard

:   This type of discard operation is configured at mount time with the discard option, and runs in real time without user intervention. However, it only discards blocks that are transitioning from used to free. Red Hat Enterprise Linux 10 supports online discard on XFS and ext4 formatted devices.

    Use batch discard unless online discard is required to maintain performance or batch discard is not feasible for the system workload.

Periodic discard
:   Batch operations that are run regularly by a `systemd`{.literal} service.

All types are supported by the XFS and ext4 file systems.

**Recommendations**

Use batch or periodic discard.

Use online discard only if:

-   the system's workload is such that batch discard is not feasible, or
-   online discard operations are necessary to maintain performance.

### [25.2. Performing batch block discard](#performing-batch-block-discard) {#performing-batch-block-discard .title}

You can perform a batch block discard operation to discard unused blocks on a mounted file system.

**Prerequisites**

-   The file system is mounted.
-   The block device underlying the file system supports physical discard operations.

**Procedure**

-   Use the `fstrim`{.literal} utility:

    -   To perform discard only on a selected file system, use:

        ``` {.language-plaintext tabindex="-1"}
        # fstrim mount-point
        ```

    -   To perform discard on all mounted file systems, use:

        ``` {.language-plaintext tabindex="-1"}
        # fstrim --all
        ```

-   If you run the `fstrim`{.literal} command on:

    -   a device that does not support discard operations, or

    -   a logical device (LVM or MD) composed of multiple devices, where any one of the device does not support discard operations, the following message displays:

        ``` {.language-plaintext tabindex="-1"}
        # fstrim /mnt/non_discard
        ```

        ``` {.language-plaintext tabindex="-1"}
        fstrim: /mnt/non_discard: the discard operation is not supported
        ```

### [25.3. Enabling online block discard](#enabling-online-block-discard) {#enabling-online-block-discard .title}

You can perform online block discard operations to automatically discard unused blocks on all supported file systems. For more information, see the `mount(8)`{.literal} and `fstab(5)`{.literal} man pages on your system.

**Procedure**

-   Enable online discard at mount time:

    -   When mounting a file system manually, add the `-o discard`{.literal} mount option:

        ``` {.language-plaintext tabindex="-1"}
        # mount -o discard device mount-point
        ```

    -   When mounting a file system persistently, add the `discard`{.literal} option to the mount entry in the `/etc/fstab`{.literal} file.

### [25.4. Enabling periodic block discard](#enabling-periodic-block-discard) {#enabling-periodic-block-discard .title}

You can enable a `systemd`{.literal} timer to regularly discard unused blocks on all supported file systems.

**Procedure**

-   Enable and start the `systemd`{.literal} timer:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now fstrim.timer
    ```

    ``` {.language-plaintext tabindex="-1"}
    Created symlink /etc/systemd/system/timers.target.wants/fstrim.timer → /usr/lib/systemd/system/fstrim.timer.
    ```

**Verification**

-   Verify the status of the timer:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status fstrim.timer
    ```

    ``` {.language-plaintext tabindex="-1"}
    fstrim.timer - Discard unused blocks once a week
       Loaded: loaded (/usr/lib/systemd/system/fstrim.timer; enabled; vendor preset: disabled)
       Active: active (waiting) since Wed 2023-05-17 13:24:41 CEST; 3min 15s ago
      Trigger: Mon 2023-05-22 01:20:46 CEST; 4 days left
         Docs: man:fstrim

    May 17 13:24:41 localhost.localdomain systemd[1]: Started Discard unused blocks once a week.
    ```

## [Chapter 26. Factors affecting I/O and file system performance](#factors-affecting-i-o-and-file-system-performance) {#chapter-26.-factors-affecting-io-and-file-system-performance .title}

The appropriate settings for storage and file system performance are highly dependent on the storage purpose. I/O and file system performance can be affected by various factors.

Following is a list of factors that can affect I/O and file system performance:

-   Data write or read patterns
-   Sequential or random
-   Buffered or Direct IO
-   Data alignment with underlying geometry
-   Block size
-   File system size
-   Journal size and location
-   Recording access times
-   Ensuring data reliability
-   Pre-fetching data
-   Pre-allocating disk space
-   File fragmentation
-   Resource contention

### [26.1. Tools for monitoring and diagnosing I/O and file system issues](#tools-for-monitoring-and-diagnosing-i-o-and-file-system-issues) {#tools-for-monitoring-and-diagnosing-io-and-file-system-issues .title}

Monitor and diagnose I/O and file system issues efficiently by using tools that track performance metrics, analyze device load, latency, and trace operations. These tools help to pinpoint bottlenecks and optimize system performance in Red Hat Enterprise Linux 10 environments.

The following tools are available in Red Hat Enterprise Linux 10 for monitoring system performance and diagnosing performance problems related to I/O and file systems:

-   `vmstat`{.literal} tool reports on processes, memory, paging, block I/O, interrupts, and CPU activity across the entire system. It can help administrators determine whether the I/O subsystem is responsible for any performance issues. If `vmstat`{.literal} analysis shows that the I/O subsystem causes reduced performance, administrators can use `iostat`{.literal} to identify the responsible I/O device.

-   `iostat`{.literal} reports on I/O device load in your system. It is provided by the `sysstat`{.literal} package.

-   `blktrace`{.literal} provides detailed information about how time is spent in the I/O subsystem. The companion utility `blkparse`{.literal} reads the raw output from `blktrace`{.literal} and produces a human readable summary of recorded input and output operations.

-   `btt`{.literal} analyzes `blktrace`{.literal} output and displays the amount of time that data spends in each area of the I/O stack. This makes it easier to spot bottlenecks in the I/O subsystem. This utility is provided as part of the `blktrace`{.literal} package. Some of the important events tracked by the `blktrace`{.literal} mechanism and analyzed by `btt`{.literal} are:

    -   Queuing of the I/O event (`Q`{.literal})
    -   Dispatch of the I/O to the driver event (`D`{.literal})
    -   Completion of I/O event (`C`{.literal})

-   `iowatcher`{.literal} can use the `blktrace`{.literal} output to graph I/O over time. It focuses on the Logical Block Address (LBA) of disk I/O, throughput, seeks per second, and I/O operations per second. This can help to identify when you are hitting the operations-per-second limit of a device.

-   BPF Compiler Collection (BCC) is a library, which facilitates the creation of the extended Berkeley Packet Filter (`eBPF`{.literal}) programs. The `eBPF`{.literal} programs are triggered on events, such as disk I/O, TCP connections, and process creations.

    The BCC tools are installed in the `/usr/share/bcc/tools/`{.literal} directory. The following `bcc-tools`{.literal} helps to analyze performance:

    -   `biolatency`{.literal} summarizes the latency in block device I/O (disk I/O) in histogram. This allows the distribution to be studied, including two modes for device cache hits and for cache misses, and latency outliers.
    -   `biosnoop`{.literal} is a basic block I/O tracing tool for displaying each I/O event along with the issuing process ID and I/O latency. Using this tool, you can investigate disk I/O performance issues.
    -   `biotop`{.literal} is used for block i/o operations in the kernel.
    -   `filelife`{.literal} tool traces the `stat()`{.literal} syscalls.
    -   `fileslower`{.literal} traces slow synchronous file reads and writes.
    -   `filetop`{.literal} displays file reads and writes by process.
    -   `ext4slower`{.literal}, `nfsslower`{.literal}, and `xfsslower`{.literal} are tools that show file system operations slower than a certain threshold, which defaults to `10ms`{.literal}.

-   `bpftace`{.literal} is a tracing language for `eBPF`{.literal} used for analyzing performance issues. It also provides trace utilities like BCC for system observation, which is useful for investigating I/O performance issues.

-   The following `SystemTap`{.literal} scripts may be useful in diagnosing storage or file system performance problems:

    -   `disktop.stp`{.literal}: Checks the status of reading or writing disk every 5 seconds and outputs the top ten entries during that period.
    -   `iotime.stp`{.literal}: Prints the amount of time spent on read and write operations, and the number of bytes read and written.
    -   `traceio.stp`{.literal}: Prints the top ten executable based on cumulative I/O traffic observed, every second.
    -   `traceio2.stp`{.literal}: Prints the executable name and process identifier as reads and writes to the specified device occur.
    -   `Inodewatch.stp`{.literal}: Prints the executable name and process identifier each time a read or write occurs to the specified inode on the specified device.
    -   `inodewatch2.stp`{.literal}: Prints the executable name, process identifier, and attributes each time the attributes are changed on the specified inode on the specified inode.

For more information, see:

-   `vmstat(8)`{.literal}, `iostat(1)`{.literal}, `blktrace(8)`{.literal}, `blkparse(1)`{.literal}, `btt(1)`{.literal}, `bpftrace`{.literal}, and `iowatcher(1)`{.literal} man pages on your system.

**Additional resources**

-   [Analyzing system performance with eBPF](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/analyzing-system-performance-with-ebpf)

### [26.2. Available tuning options for formatting a file system](#available-tuning-options-for-formatting-a-file-system) {#available-tuning-options-for-formatting-a-file-system .title}

Some file system configuration decisions cannot be changed after the device is formatted. These include the size, block size, geometry, and external journals.

The following are the details of the options that are available before formatting a storage device:

`Size`{.literal}
:   Create an appropriately-sized file system for your workload. Smaller file systems require less time and memory for file system checks. However, if a file system is too small, its performance suffers from high fragmentation.

`Block size`{.literal}

:   The block is the unit of work for the file system. The block size determines how much data can be stored in a single block. It therefore sets the smallest data amount written or read at one time.

    The default block size is appropriate for most use cases. However, your file system performs better if the block size matches the typical read or write amount. Optimal performance occurs when the block size equals or slightly exceeds the data typically accessed at once.

    A small file still uses an entire block. Files can be spread across multiple blocks, but this can create additional runtime overhead.

    Additionally, some file systems are limited to a certain number of blocks, which limits the maximum size of the file system. Block size is specified as part of the file system options when formatting a device with the `mkfs`{.literal} command. The parameter that specifies the block size varies with the file system.

`Geometry`{.literal}

:   File system geometry is concerned with the distribution of data across a file system. If your system uses striped storage like RAID, align data and metadata with the underlying storage geometry when formatting. This improves performance.

    Many devices export recommended geometry, which is then set automatically when the devices are formatted with a particular file system. If your device does not export these recommendations, or you want to change them, specify geometry manually when formatting with `mkfs`{.literal}.

    The parameters that specify file system geometry vary with the file system.

`External journals`{.literal}
:   Journaling file systems document changes in a journal file before running write operations. This reduces the likelihood of device corruption during system crashes or power failures. It also speeds up recovery.

Note

It is preferable to not use the external journals option.

Metadata-intensive workloads involve very frequent updates to the journal. A larger journal uses more memory, but reduces the frequency of write operations. Additionally, you can improve the seek time of a device with a metadata-intensive workload by placing its journal on dedicated storage. Use storage as fast as, or faster than the primary storage.

Warning

Ensure that external journals are reliable. Losing an external journal device causes file system corruption. External journals must be created at format time, with journal devices being specified at mount time.

### [26.3. Available tuning options for mounting a file system](#available-tuning-options-for-mounting-a-file-system) {#available-tuning-options-for-mounting-a-file-system .title}

You can explore key tuning options for mounting file systems, including `atime`{.literal}, `noatime`{.literal}, and read-ahead settings, to select mount options that balance performance and functionality for different workloads.

The following are the options available to most file systems and can be specified as the device is mounted:

`Access Time`{.literal}

:   Every time a file is read, its metadata is updated with the time at which access occurred (`atime`{.literal}). This involves additional write I/O. The `relatime`{.literal} is the default `atime`{.literal} setting for most file systems.

    However, if updating this metadata is time consuming, and if accurate access time data is not required, you can mount the file system with the `noatime`{.literal} mount option. This disables updates to metadata when a file is read. It also enables `nodiratime`{.literal} behavior, which disables updates to metadata when a directory is read.

Note

Disabling `atime`{.literal} updates by using the `noatime mount`{.literal} option can break applications that rely on them, for example, backup programs.

`Read-ahead`{.literal}

:   `Read-ahead`{.literal} behavior speeds up file access by pre-fetching data that is likely to be needed soon and loading it into the page cache, where it can be retrieved more quickly than if it were on disk. The higher the read-ahead value, the further ahead the system pre-fetches data.

    Red Hat Enterprise Linux attempts to set an appropriate read-ahead value based on what it detects about your file system. However, accurate detection is not always possible. For example, if a storage array presents itself to the system as a single LUN, the system detects the single LUN, and does not set the appropriate read-ahead value for an array.

    Workloads that involve heavy streaming of sequential I/O often benefit from high read-ahead values. The storage-related tuned profiles provided with Red Hat Enterprise Linux raise the read-ahead value, as does using LVM striping, but these adjustments are not always sufficient for all workloads.

### [26.4. Discarding blocks that are unused](#Discarding-blocks-that-are-unused) {#discarding-blocks-that-are-unused .title}

Regularly discarding blocks that are not in use by the file system is a good practice for both solid-state disks and thinly-provisioned storage.

**Additional resources**

-   [Types of block discard operations](#types-of-block-discard-operations "25.1. Types of block discard operations")

### [26.5. Solid-state disks tuning considerations](#solid-state-disks-tuning-considerations) {#solid-state-disks-tuning-considerations .title}

Solid-state disks (SSD) use NAND flash chips rather than rotating magnetic platters to store persistent data. SSD provides a constant access time for data across their full Logical Block Address range. It does not incur measurable seek costs like their rotating counterparts.

They are more expensive per gigabyte of storage space and have a lesser storage density. However, they also have lower latency and greater throughput than Hard Disk Drives (HDD)s.

Performance generally degrades as the used blocks on an SSD approach the capacity of the disk. The degree of degradation varies by vendor, but all devices experience degradation in this circumstance. Enabling discard behavior can help to alleviate this degradation.

The default I/O scheduler and virtual memory options are suitable for use with SSDs. Consider the following factors when configuring settings that can affect SSD performance:

`I/O Scheduler`{.literal}

:   Any I/O scheduler is expected to perform well with most SSDs. However, as with any other storage type, benchmark to determine the optimal configuration for a given workload. When using SSDs, change the I/O scheduler only to benchmark particular workloads.

    For instructions on how to switch between I/O schedulers, see the `/usr/share/doc/kernel-version/Documentation/block/switching-sched.txt`{.literal} file.

    For single queue Host Bus Adapter (HBA), the default I/O scheduler is `deadline`{.literal}. For multiple queue HBA, the default I/O scheduler is `none`{.literal}.

`Virtual Memory`{.literal}
:   Like the I/O scheduler, virtual memory (VM) subsystem requires no special tuning. Given the fast nature of I/O on SSD, try turning down the `vm_dirty_background_ratio`{.literal} and `vm_dirty_ratio`{.literal} settings. Increased write-out activity does not usually have a negative impact on the latency of other operations on the disk. However, this tuning can generate more overall I/O, and is therefore not generally preferable without workload-specific testing.

`Swap`{.literal}
:   An SSD can also be used as a swap device, and is likely to produce good page-out and page-in performance.

**Additional resources**

-   [Types of block discard operations](#types-of-block-discard-operations "25.1. Types of block discard operations")

### [26.6. Generic block device tuning parameters](#generic-block-device-tuning-parameters) {#generic-block-device-tuning-parameters .title}

The generic tuning parameters listed here are available in the `/sys/block/sdX/queue/`{.literal} directory.

The following listed tuning parameters are separate from I/O scheduler tuning, and are applicable to all I/O schedulers:

`add_random`{.literal}
:   Some I/O events contribute to the entropy pool for the `/dev/random`{.literal}. This parameter can be set to `0`{.literal} if the overhead of these contributions become measurable.

`iostats`{.literal}

:   By default, `iostats`{.literal} is enabled and the default value is `1`{.literal}. Setting `iostats`{.literal} to `0`{.literal} disables gathering of I/O statistics for the device. This removes a small amount of overhead with the I/O path.

    Setting `iostats`{.literal} to `0`{.literal} might improve performance for high performance devices, such as certain Non-volatile Memory Express (NVMe) storage devices. It is preferable to leave `iostats`{.literal} enabled unless otherwise specified for the given storage model by the vendor.

    If you disable `iostats`{.literal}, the I/O statistics for the device are no longer present within the `/proc/diskstats`{.literal} file. The content of `/sys/diskstats`{.literal} file is the source of I/O information for monitoring I/O tools, such as `sar`{.literal} or `iostats`{.literal}. Therefore, if you disable the `iostats`{.literal} parameter for a device, it is no longer present in the output of I/O monitoring tools.

`max_sectors_kb`{.literal}

:   Specifies the maximum size of an I/O request in kilobytes. The default value is `512`{.literal} KB. The minimum value for this parameter is determined by the logical block size of the storage device. The maximum value for this parameter is determined by the value of the `max_hw_sectors_kb`{.literal}.

    `max_sectors_kb`{.literal} must always be a multiple of the optimal I/O size and the internal erase block size. Use a value of `logical_block_size`{.literal} for either parameter if they are zero or not specified by the storage device.

`nomerges`{.literal}
:   Most workloads benefit from request merging. However, disabling merges can be useful for debugging purposes. By default, the `nomerges`{.literal} parameter is set to `0`{.literal}, which enables merging. To disable simple one-hit merging, set `nomerges`{.literal} to `1`{.literal}. and to disable all types of merging, set `nomerges`{.literal} to `2`{.literal}.

`nr_requests`{.literal}
:   It is the maximum allowed number of the queued I/O. If the current I/O scheduler is `none`{.literal}, this number can only be reduced; otherwise the number can be increased or reduced.

`optimal_io_size`{.literal}
:   Some storage devices report an optimal I/O size through this parameter. If this value is reported, applications issue I/O aligned to and in multiples of the optimal I/O size wherever possible.

`read_ahead_kb`{.literal}

:   Defines the maximum number of kilobytes that the operating system may read ahead during a sequential read operation. As a result, the necessary information is already present within the kernel page cache for the next sequential read. This improves read I/O performance.

    Device mappers often benefit from a high `read_ahead_kb`{.literal} value. `128`{.literal} KB for each device to be mapped is a good starting point. Increasing the `read_ahead_kb`{.literal} value up to request queue's `max_sectors_kb`{.literal} of the disk might improve performance where sequential reading of large files occur.

`rotational`{.literal}
:   Some solid-state disks do not correctly advertise their solid-state status, and are mounted as traditional rotational disks. Manually set the `rotational`{.literal} value to `0`{.literal} to disable unnecessary seek-reducing logic in the scheduler.

`rq_affinity`{.literal}
:   The default value of the `rq_affinity`{.literal} is `1`{.literal}. It completes the I/O operations on one CPU core, which is in the same CPU group of the issued CPU core. To perform completions only on the processor that issued the I/O request, set the `rq_affinity`{.literal} to `2`{.literal}. To disable the mentioned two abilities, set it to `0`{.literal}.

`scheduler`{.literal}
:   To set the scheduler or scheduler preference order for a storage device, edit the `/sys/block/`{.literal}*`devname`{.literal}*`/queue/scheduler`{.literal}. Replace *devname* with the device name you want to configure.

## [Chapter 27. configuring Stratis file systems](#configuring-stratis-file-systems) {#chapter-27.-configuring-stratis-file-systems .title}

Stratis is a local storage-management solution for Red Hat Enterprise Linux. It is focused on simplicity, ease of use, and gives you access to advanced storage features.

Stratis runs as a service to manage pools of physical storage devices, simplifying local storage management with ease of use. It helps you configure and manage complex storage configurations.

Stratis can help you with:

-   Initial configuration of storage
-   Making changes later
-   Using advanced storage features

The central concept of Stratis is a storage pool. This pool is created from one or more local disks or partitions, and file systems are created from the pool. The pool enables features such as:

-   File system snapshots
-   Thin provisioning
-   Caching
-   Encryption

### [27.1. Components of a Stratis file system](#components-of-a-stratis-file-system) {#components-of-a-stratis-file-system .title}

Stratis consists of three main components that work together to provide advanced storage management. These components are block devices, storage pools, and file systems. They provide thin provisioning, snapshots, and automatic space management.

Externally, Stratis presents the following file system components on the command line and through the API:

`blockdev`{.literal}
:   Block devices, such as disks or disk partitions.

`pool`{.literal}

:   Composed of one or more block devices.

    A pool has a fixed total size, equal to the size of the block devices.

    The pool contains most Stratis layers, such as the non-volatile data cache by using the `dm-cache`{.literal} target.

    Stratis creates a `/dev/stratis/`{.literal}*`my-pool`{.literal}*`/`{.literal} directory for each pool. This directory contains links to devices that represent Stratis file systems in the pool.

`filesystem`{.literal}

:   Each pool can contain zero or more file systems. A pool containing file systems can store any number of files.

    File systems are thinly provisioned and do not have a fixed total size. The actual size of a file system grows with the data stored on it. If the data size approaches the virtual file system size, Stratis automatically grows the thin volume and the file system.

    The file systems are formatted with the XFS file system. Stratis uses the XFS file system for its storage, and provisions a Stratis volume.

Note

A Stratis volume is referred to as a "Stratis filesystem\" throughout the rest of the documentation. This is to retain alignment with the command line interface.

Important

Stratis tracks information about file systems that it created. XFS is not aware of this information. Changes made by using XFS do not automatically update Stratis.

Stratis creates links to file systems at the `/dev/stratis/`{.literal}*`my-pool`{.literal}*`/`{.literal}*`my-fs`{.literal}* path.

Stratis uses many Device Mapper devices, which appear in `dmsetup`{.literal} listings and the `/proc/partitions`{.literal} file. Similarly, the `lsblk`{.literal} command output reflects the internal workings and layers of Stratis.

### [27.2. Block devices compatible with Stratis](#block-devices-compatible-with-stratis) {#block-devices-compatible-with-stratis .title}

Stratis supports various block devices including physical drives, logical volumes, and networked storage. You can build Stratis pools from different storage types while maintaining advanced features like thin provisioning and snapshots.

Storage devices that can be used with Stratis.

**Supported devices**

Stratis pools have been tested to work on these types of block devices:

-   Linux Unified Key Setup (LUKS)
-   Logical Volume Manager (LVM) logical volumes
-   Multiple Device (MD) Redundant Array of Independent Disks (RAID)
-   Device Mapper (DM) Multipath
-   Internet Small Computer System Interface (iSCSI)
-   Hard Disk Drives (HDDs) and Solid-State Disks (SSDs)
-   Non-volatile Memory Express (NVMe) devices

### [27.3. Installing Stratis](#installing-stratis) {#installing-stratis .title}

Install the Stratis storage management system to enable advanced storage features on your RHEL system. These include thin provisioning, file system snapshots, and flexible pool-based storage management.

**Procedure**

1.  Install packages that provide the Stratis service and command-line utilities:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install stratisd stratis-cli
    ```

2.  To start the `stratisd`{.literal} service and enable it to launch at boot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now stratisd
    ```

**Verification**

-   Verify that the `stratisd`{.literal} service is enabled and is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status stratisd
    ```

    ``` {.language-plaintext tabindex="-1"}
    stratisd.service - Stratis daemon
    Loaded: loaded (/usr/lib/systemd/system/stratisd.service; enabled; preset:>
    Active: active (running) since Tue 2025-03-25 14:04:42 CET; 30min ago
    Docs: man:stratisd(8)
    Main PID: 24141 (stratisd)
    Tasks: 22 (limit: 99365)
    Memory: 10.4M
    CPU: 1.436s
    CGroup: /system.slice/stratisd.service
    └─24141 /usr/libexec/stratisd --log-level debug
    ```

### [27.4. Creating an unencrypted Stratis pool](#creating-an-unencrypted-stratis-pool) {#creating-an-unencrypted-stratis-pool .title}

You can create an unencrypted Stratis pool from one or more block devices.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").

-   The block device on which you are creating a Stratis pool is not in use, unmounted, and is at least 1 GB in space.

-   On the IBM Z architecture, the `/dev/dasd*`{.literal} block devices must be partitioned. Use the partition device for creating the Stratis pool.

    For information about partitioning DASD devices, see [Configuring a Linux instance on 64-bit IBM Z](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/configuring-a-linux-instance-on-64-bit-ibm-z).

Note

You can only encrypt a Stratis pool during creation, and not later.

**Procedure**

1.  Erase any file system, partition table, or RAID signatures that exist on each block device that you want to use in the Stratis pool:

    ``` {.language-plaintext tabindex="-1"}
    # wipefs --all block-device
    ```

    The *`block-device`{.literal}* value is the path to the block device; for example, `/dev/sdb`{.literal}.

2.  Create the new unencrypted Stratis pool on the selected block device:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool create my-pool block-device
    ```

    The *`block-device`{.literal}* value is the path to an empty or wiped block device.

    You can also specify multiple block devices on a single line by using the following command:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool create my-pool block-device-1 block-device-2
    ```

**Verification**

-   Verify that the new Stratis pool was created:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list
    ```

### [27.5. Creating an unencrypted Stratis pool by using the web console](#creating-an-unencrypted-stratis-pool-by-using-the-web-console) {#creating-an-unencrypted-stratis-pool-by-using-the-web-console .title}

You can use the web console to create an unencrypted Stratis pool from one or more block devices.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").

-   The block device on which you are creating a Stratis pool is not in use, unmounted, and is at least 1 GB in space.

Note

You cannot encrypt an unencrypted Stratis pool after it is created.

**Procedure**

1.  Log in to the RHEL 10 web console.
2.  Click Storage.
3.  In the **Storage** table, click the menu button and select **Create Stratis pool**.
4.  In the **Name** field, enter a name for the Stratis pool.
5.  Select the **Block devices** from which you want to create the Stratis pool.
6.  Optional: If you want to specify the maximum size for each file system that is created in the pool, select **Manage filesystem sizes**.
7.  Click Create.

**Verification**

-   Go to the **Storage** section and verify that you can see the new Stratis pool in the **Devices** table.

### [27.6. Creating an encrypted Stratis pool by using a key in the kernel keyring](#creating-an-encrypted-stratis-pool-using-a-key-in-the-kernel-keyring) {#creating-an-encrypted-stratis-pool-by-using-a-key-in-the-kernel-keyring .title}

To secure your data, use the kernel keyring to create an encrypted Stratis pool from one or more block devices. When you do so, the kernel keyring is used as the primary encryption mechanism. After subsequent system reboots this kernel keyring is used to unlock the encrypted Stratis pool.

When creating an encrypted Stratis pool from one or more block devices, note the following:

-   Each block device is encrypted by using the `cryptsetup`{.literal} library and implements the `LUKS2`{.literal} format.
-   Each Stratis pool can either have a unique key or share the same key with other pools. These keys are stored in the kernel keyring.
-   The block devices that comprise a Stratis pool must be either all encrypted or all unencrypted. It is not possible to have both encrypted and unencrypted block devices in the same Stratis pool.
-   Block devices added to the data cache of an encrypted Stratis pool are automatically encrypted.

**Prerequisites**

-   Stratis v2.1.0 or later is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").

-   The block device on which you are creating a Stratis pool is not in use, unmounted, and is at least 1 GB in space.

-   On the IBM Z architecture, the `/dev/dasd*`{.literal} block devices must be partitioned. Use the partition in the Stratis pool.

    For information about partitioning DASD devices, see [Configuring a Linux instance on 64-bit IBM Z](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/configuring-a-linux-instance-on-64-bit-ibm-z).

**Procedure**

1.  Erase any file system, partition table, or RAID signatures that exist on each block device that you want to use in the Stratis pool:

    ``` {.language-plaintext tabindex="-1"}
    # wipefs --all block-device
    ```

    The *`block-device`{.literal}* value is the path to the block device; for example, `/dev/sdb`{.literal}.

2.  If you have not set a key already, run the following command and follow the prompts to create a key set to use for the encryption:

    ``` {.language-plaintext tabindex="-1"}
    # stratis key set --capture-key key-description
    ```

    The *`key-description`{.literal}* is a reference to the key that gets created in the kernel keyring. You will be prompted to enter a key value at the command-line. You can also place the key value in a file and use the `--keyfile-path`{.literal} option instead of the `--capture-key`{.literal} option.

3.  Create the encrypted Stratis pool and specify the key description to use for the encryption:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool create --key-desc key-description my-pool block-device
    ```

    *`key-description`{.literal}*
    :   References the key that exists in the kernel keyring, which you created in the previous step.

    *`my-pool`{.literal}*
    :   Specifies the name of the new Stratis pool.

    *`block-device`{.literal}*

    :   Specifies the path to an empty or wiped block device.

        You can also specify multiple block devices on a single line by using the following command:

        ``` {.language-plaintext tabindex="-1"}
        # stratis pool create --key-desc key-description my-pool block-device-1 block-device-2
        ```

**Verification**

-   Verify that the new Stratis pool was created:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list
    ```

### [27.7. Creating an encrypted Stratis pool by using Clevis](#creating-an-encrypted-stratis-pool-using-clevis) {#creating-an-encrypted-stratis-pool-by-using-clevis .title}

Starting with Stratis 2.4.0, you can create an encrypted pool by using the Clevis mechanism by specifying Clevis options at the command line.

**Prerequisites**

-   Stratis v2.3.0 or later is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   An encrypted Stratis pool is created. For more information, see [Creating an encrypted Stratis pool by using a key in the kernel keyring](#creating-an-encrypted-stratis-pool-using-a-key-in-the-kernel-keyring "27.6. Creating an encrypted Stratis pool by using a key in the kernel keyring").
-   Your system supports Trusted Platform Module (TPM) 2.0.

**Procedure**

1.  Erase any file system, partition table, or RAID signatures that exist on each block device that you want to use in the Stratis pool:

    ``` {.language-plaintext tabindex="-1"}
    # wipefs --all block-device
    ```

    The *`block-device`{.literal}* value is the path to the block device; for example, `/dev/sdb`{.literal}.

2.  Create the encrypted Stratis pool and specify the Clevis mechanism to use for the encryption:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool create --clevis tpm2 my-pool block-device
    ```

    *`tpm2`{.literal}*
    :   Specifies the Clevis mechanism to use.

    *`my-pool`{.literal}*
    :   Specifies the name of the new Stratis pool.

    *`block-device`{.literal}*

    :   Specifies the path to an empty or wiped block device.

        Alternatively, use the Clevis tang server mechanism by using the following command:

        ``` {.language-plaintext tabindex="-1"}
        # stratis pool create --clevis tang --tang-url my-url --thumbprint thumbprint my-pool block-device
        ```

    *`tang`{.literal}*
    :   Specifies the Clevis mechanism to use.

    *`my-url`{.literal}*
    :   Specifies the URL of the tang server.

    *`thumbprint`{.literal}*

    :   References the thumbprint of the tang server.

        You can also specify multiple block devices on a single line by using the following command:

        ``` {.language-plaintext tabindex="-1"}
        # stratis pool create --clevis tpm2 my-pool block-device-1 block-device-2
        ```

**Verification**

-   Verify that the new Stratis pool was created:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list
    ```

    Note

    You can also create an encrypted pool by using both Clevis and keyring mechanisms by specifying both Clevis and keyring options at the same time during pool creation.

### [27.8. Creating an encrypted Stratis pool by using the storage RHEL system role](#creating-an-encrypted-stratis-pool-by-using-the-storage-rhel-system-role) {#creating-an-encrypted-stratis-pool-by-using-the-storage-rhel-system-role .title}

To secure your data, you can create an encrypted Stratis pool with the `storage`{.literal} RHEL system role. In addition to a passphrase, you can use Clevis and Tang or TPM protection as an encryption method.

Important

You can configure Stratis encryption only on the entire pool.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   You can connect to the Tang server. For more information, see [Deploying a Tang server with SELinux in enforcing mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-by-using-policy-based-decryption#deploying-a-tang-server-with-selinux-in-enforcing-mode).

**Procedure**

1.  Store your sensitive variables in an encrypted file:

    a.  Create the vault:

        ``` {.language-plaintext tabindex="-1"}
        $ ansible-vault create ~/vault.yml
        ```

        ``` {.language-plaintext tabindex="-1"}
        New Vault password: <vault_password>
        Confirm New Vault password: <vault_password>
        ```

    b.  After the `ansible-vault create`{.literal} command opens an editor, enter the sensitive data in the *`<key>`{.literal}*`: `{.literal}*`<value>`{.literal}* format:

        ``` {.language-plaintext tabindex="-1"}
        luks_password: <password>
        ```

    c.  Save the changes, and close the editor. Ansible encrypts the data in the vault.

2.  Create a playbook file, for example, `~/playbook.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Manage local storage
      hosts: managed-node-01.example.com
      vars_files:
        - ~/vault.yml
      tasks:
        - name: Create a new encrypted Stratis pool with Clevis and Tang
          ansible.builtin.include_role:
            name: redhat.rhel_system_roles.storage
          vars:
            storage_pools:
               - name: mypool
                 disks:
                   - sdd
                   - sde
                 type: stratis
                 encryption: true
                 encryption_password: "{{ luks_password }}"
                 encryption_clevis_pin: tang
                 encryption_tang_url: tang-server.example.com:7500
    ```

    The settings specified in the example playbook include the following:

    `encryption_password`{.literal}
    :   Password or passphrase used to unlock the LUKS volumes.

    `encryption_clevis_pin`{.literal}
    :   Clevis method that you can use to encrypt the created pool. You can use `tang`{.literal} and `tpm2`{.literal}.

    `encryption_tang_url`{.literal}
    :   URL of the Tang server.

    For details about all variables used in the playbook, see the `/usr/share/ansible/roles/rhel-system-roles.storage/README.md`{.literal} file on the control node.

3.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --ask-vault-pass --syntax-check ~/playbook.yml
    ```

    Note that this command only validates the syntax and does not protect against a wrong but valid configuration.

4.  Run the playbook:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --ask-vault-pass ~/playbook.yml
    ```

**Verification**

-   Verify that the pool was created with Clevis and Tang configured:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible managed-node-01.example.com -m command -a 'sudo stratis report'
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
                            "clevis_config": {
                                "thp": "j-G4ddvdbVfxpnUbgxlpbe3KutSKmcHttILAtAkMTNA",
                                "url": "tang-server.example.com:7500"
                            },
                            "clevis_pin": "tang",
                            "in_use": true,
                            "key_description": "blivet-mypool",
    ```

**Additional resources**

-   [Ansible vault](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/ansible-vault)

### [27.9. Creating an encrypted Stratis pool by using the web console](#creating-an-encrypted-stratis-pool-by-using-the-web-console) {#creating-an-encrypted-stratis-pool-by-using-the-web-console .title}

To secure your data, you can use the web console to create an encrypted Stratis pool from one or more block devices.

When creating an encrypted Stratis pool from one or more block devices, note the following:

-   Each block device is encrypted by using the `cryptsetup`{.literal} library and implements the Linux Unified Key Setup version 2 (LUKS2) format.
-   Each Stratis pool can either have a unique key or share the same key with other pools. These keys are stored in the kernel keyring.
-   The block devices that comprise a Stratis pool must be either all encrypted or all unencrypted. It is not possible to have both encrypted and unencrypted block devices in the same Stratis pool.
-   Block devices added to the data tier of an encrypted Stratis pool are automatically encrypted.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   Stratis v2.1.0 or later is installed and the `stratisd`{.literal} service is running.

-   The block device on which you are creating a Stratis pool is not in use, unmounted, and is at least 1 GB in space.

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click Storage.

3.  In the **Storage** table, click the menu button and select **Create Stratis pool**.

4.  In the **Name** field, enter a name for the Stratis pool.

5.  Select the **Block devices** from which you want to create the Stratis pool.

6.  Select the type of encryption, you can use a passphrase, a Tang keyserver, or both:

    -   Passphrase:

        i.  Enter a passphrase.
        ii. Confirm the passphrase.

    -   Tang keyserver:

        i.  Enter the keyserver address. For more information, see [Deploying a Tang server with SELinux in enforcing mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-by-using-policy-based-decryption#deploying-a-tang-server-with-selinux-in-enforcing-mode).

7.  Optional: If you want to specify the maximum size for each file system that is created in pool, select **Manage filesystem sizes**.

8.  Click Create.

**Verification**

-   Go to the **Storage** section and verify that you can see the new Stratis pool in the **Devices** table.

### [27.10. Renaming a Stratis pool by using the web console](#renaming-a-stratis-pool-by-using-the-web-console) {#renaming-a-stratis-pool-by-using-the-web-console .title}

You can use the web console to rename an existing Stratis pool.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   Stratis is installed and the `stratisd`{.literal} service is running.

    The web console detects and installs Stratis by default. However, for manually installing Stratis, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").

-   A Stratis pool is created.

**Procedure**

1.  Log in to the RHEL 10 web console.
2.  Click Storage.
3.  In the **Storage** table, click the Stratis pool you want to rename.
4.  On the **Stratis pool** page, click edit next to the **Name** field.
5.  In the **Rename Stratis pool** dialog box, enter a new name.
6.  Click Rename.

### [27.11. configuring overprovisioning mode in Stratis file system](#configuring-overprovisioning-mode-in-stratis-file-system) {#configuring-overprovisioning-mode-in-stratis-file-system .title}

By default, every Stratis pool is overprovisioned, meaning logical file system size can exceed physical allocation. Stratis monitors usage and increases allocation automatically when space is available. If the pool is full, no additional space can be assigned.

Note

If the file system runs out of space, users might lose data. For applications where the risk of data loss outweighs the benefits of overprovisioning, this feature can be disabled.

Stratis continuously monitors the pool usage and reports the values by using the D-Bus API. Storage administrators must monitor these values and add devices to the pool as needed to prevent it from reaching capacity.

**Prerequisites**

-   Stratis is installed. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").

**Procedure**

-   To configure the pool correctly, you have two possibilities:

    -   Create a pool from one or more block devices to make the pool fully provisioned at the time of creation:

        ``` {.language-plaintext tabindex="-1"}
        # stratis pool create --no-overprovision pool-name /dev/sdb
        ```

    -   By using the `--no-overprovision`{.literal} option, the pool cannot allocate more logical space than actual available physical space.

        1.  Set overprovisioning mode in the existing pool:

            ``` {.language-plaintext tabindex="-1"}
            # stratis pool overprovision pool-name <yes|no>
            ```

            If set to \"yes\", you enable overprovisioning to the pool. This means the sum of the logical sizes of the Stratis file systems supported by the pool can exceed the available data space. If the pool is overprovisioned and the sum of the logical sizes of all file systems exceeds the available space, overprovisioning cannot be turned off. The system returns an error.

**Verification**

1.  View the full list of Stratis pools:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list
    ```

    ``` {.language-plaintext tabindex="-1"}
    Name       Total Physical                    Properties    UUID                                  Alerts
    pool-name  1.42 TiB / 23.96 MiB / 1.42 TiB  ~Ca,~Cr,~Op    cb7cb4d8-9322-4ac4-a6fd-eb7ae9e1e540
    ```

2.  Check if there is an indication of the pool overprovisioning mode flag in the `stratis pool list`{.literal} output. The \" \~ \" is a math symbol for \"NOT\", so `~Op`{.literal} means no-overprovisioning.

3.  Optional: Check overprovisioning on a specific pool:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool overprovision pool-name yes
    ```

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list
    ```

    ``` {.language-plaintext tabindex="-1"}
    Name          Total Physical                    Properties     UUID                                   Alerts
    pool-name     1.42 TiB / 23.96 MiB / 1.42 TiB   ~Ca,~Cr,~Op    cb7cb4d8-9322-4ac4-a6fd-eb7ae9e1e540
    ```

### [27.12. Binding a Stratis pool to NBDE](#binding-a-stratis-pool-to-nbde) {#binding-a-stratis-pool-to-nbde .title}

Binding an encrypted Stratis pool to Network Bound Disk Encryption (NBDE) requires a Tang server. When a system containing the Stratis pool reboots, it connects with the Tang server to automatically unlock the encrypted pool. You do not need to provide the kernel keyring description.

Note

Binding a Stratis pool to a supplementary Clevis encryption mechanism does not remove the primary kernel keyring encryption.

**Prerequisites**

-   Stratis v2.3.0 or later is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   An encrypted Stratis pool is created, and you have the key description of the key that was used for the encryption. For more information, see [Creating an encrypted Stratis pool by using a key in the kernel keyring](#creating-an-encrypted-stratis-pool-using-a-key-in-the-kernel-keyring "27.6. Creating an encrypted Stratis pool by using a key in the kernel keyring").
-   You can connect to the Tang server. For more information, see [Deploying a Tang server with SELinux in enforcing mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-by-using-policy-based-decryption#deploying-a-tang-server-with-selinux-in-enforcing-mode).

**Procedure**

-   Bind an encrypted Stratis pool to NBDE:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool bind nbde --trust-url my-pool tang-server
    ```

    *`my-pool`{.literal}*
    :   Specifies the name of the encrypted Stratis pool.

    *`tang-server`{.literal}*
    :   Specifies the IP address or URL of the Tang server.

**Additional resources**

-   [Configuring automated unlocking of encrypted volumes using policy-based decryption](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-by-using-policy-based-decryption)

### [27.13. Binding a Stratis pool to TPM](#binding-a-stratis-pool-to-tpm) {#binding-a-stratis-pool-to-tpm .title}

When you bind an encrypted Stratis pool to the Trusted Platform Module (TPM) 2.0, the system containing the pool reboots, and the pool is automatically unlocked without you having to provide the kernel keyring description.

**Prerequisites**

-   Stratis v2.3.0 or later is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   An encrypted Stratis pool is created, and you have the key description of the key that was used for the encryption. For more information, see [Creating an encrypted Stratis pool by using a key in the kernel keyring](#creating-an-encrypted-stratis-pool-using-a-key-in-the-kernel-keyring "27.6. Creating an encrypted Stratis pool by using a key in the kernel keyring").
-   Your system supports TPM 2.0.

**Procedure**

-   Bind an encrypted Stratis pool to TPM:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool bind tpm my-pool
    ```

    *`my-pool`{.literal}*
    :   Specifies the name of the encrypted Stratis pool.

    *`key-description`{.literal}*
    :   References the key that exists in the kernel keyring, which was generated when you created the encrypted Stratis pool.

### [27.14. Unlocking an encrypted Stratis pool with kernel keyring](#unlocking-an-encrypted-stratis-pool-with-kernel-keyring) {#unlocking-an-encrypted-stratis-pool-with-kernel-keyring .title}

After a system reboot, your encrypted Stratis pool or the block devices that comprise it might not be visible. You can unlock the pool by using the kernel keyring that was used to encrypt the pool.

**Prerequisites**

-   Stratis v2.1.0 is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   An encrypted Stratis pool is created. For more information, see [Creating an encrypted Stratis pool by using a key in the kernel keyring](#creating-an-encrypted-stratis-pool-using-a-key-in-the-kernel-keyring "27.6. Creating an encrypted Stratis pool by using a key in the kernel keyring").

**Procedure**

1.  Re-create the key set by using the same key description that was used previously:

    ``` {.language-plaintext tabindex="-1"}
    # stratis key set --capture-key key-description
    ```

    `key-description`{.literal} references the key that exists in the kernel keyring, which was generated when you created the encrypted Stratis pool.

2.  Verify that the Stratis pool is visible:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list
    ```

### [27.15. Unbinding a Stratis pool from supplementary encryption](#unbinding-a-stratis-pool-from-supplementary-encryption) {#unbinding-a-stratis-pool-from-supplementary-encryption .title}

When you unbind an encrypted Stratis pool from a supported supplementary encryption mechanism, the primary kernel keyring encryption remains in place. This is not true for pools that are created with Clevis encryption from the start.

**Prerequisites**

-   Stratis v2.3.0 or later is installed on your system. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   An encrypted Stratis pool is created. For more information, see [Creating an encrypted Stratis pool by using a key in the kernel keyring](#creating-an-encrypted-stratis-pool-using-a-key-in-the-kernel-keyring "27.6. Creating an encrypted Stratis pool by using a key in the kernel keyring").
-   The encrypted Stratis pool is bound to a supported supplementary encryption mechanism.

**Procedure**

-   Unbind an encrypted Stratis pool from a supplementary encryption mechanism:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool unbind clevis my-pool
    ```

    *`my-pool`{.literal}* specifies the name of the Stratis pool you want to unbind.

**Additional resources**

-   [Binding an encrypted Stratis pool to NBDE](#binding-a-stratis-pool-to-nbde "27.12. Binding a Stratis pool to NBDE")
-   [Binding an encrypted Stratis pool to TPM](#binding-a-stratis-pool-to-tpm "27.13. Binding a Stratis pool to TPM")

### [27.16. Starting and stopping Stratis pool](#starting-and-stopping-stratis-pool) {#starting-and-stopping-stratis-pool .title}

You can start and stop Stratis pools. This gives you the option to disassemble or bring down all the objects that were used to construct the pool. These objects include file systems, cache devices, thin pool, and encrypted devices.

Note that if the pool actively uses any device or file system, it might issue a warning and not stop. The stopped state is recorded in the pool's metadata. These pools do not start on the following boot, until the pool receives a start command.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   An unencrypted or an encrypted Stratis pool is created. For more information, see [Creating an unencrypted Stratis pool](#creating-an-unencrypted-stratis-pool "27.4. Creating an unencrypted Stratis pool") or [Creating an encrypted Stratis pool by using a key in the kernel keyring](#creating-an-encrypted-stratis-pool-using-a-key-in-the-kernel-keyring "27.6. Creating an encrypted Stratis pool by using a key in the kernel keyring").

**Procedure**

-   Use the following command to stop the Stratis pool. This tears down the storage stack but leaves all metadata intact:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool stop --name pool-name
    ```

-   Use the following command to start the Stratis pool. The `--unlock-method`{.literal} option specifies the method of unlocking the pool if it is encrypted:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool start --unlock-method <keyring|clevis> --name pool-name
    ```

    Note

    You can start the pool by using either the pool name or the pool UUID.

**Verification**

-   Use the following command to list all active pools on the system:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list
    ```

-   Use the following command to list all the stopped pools:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list --stopped
    ```

-   Use the following command to view detailed information for a stopped pool. If the UUID is specified, the command prints detailed information about the pool corresponding to the UUID:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list --stopped --uuid UUID
    ```

### [27.17. Creating a Stratis file system](#creating-a-stratis-file-system) {#creating-a-stratis-file-system .title}

Create a Stratis file system to leverage advanced storage capabilities within a storage pool. These include thin provisioning, automatic file system growth, and integrated snapshot support.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   A Stratis pool is created. For more information, see [Creating an unencrypted Stratis pool](#creating-an-unencrypted-stratis-pool "27.4. Creating an unencrypted Stratis pool") or [using a key in the kernel keyring](#creating-an-encrypted-stratis-pool-using-a-key-in-the-kernel-keyring "27.6. Creating an encrypted Stratis pool by using a key in the kernel keyring").

**Procedure**

1.  Create a Stratis file system on a pool:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem create --size number-and-unit my-pool my-fs
    ```

    *`number-and-unit`{.literal}*
    :   Specifies the size of a file system. The specification format must follow the standard size specification format for input, that is B, KiB, MiB, GiB, TiB or PiB.

    *`my-pool`{.literal}*
    :   Specifies the name of the Stratis pool.

    *`my-fs`{.literal}*

    :   Specifies an arbitrary name for the file system.

        For example, create a Stratis file system:

        ``` {.language-plaintext tabindex="-1"}
        # stratis filesystem create --size 10GiB pool1 filesystem1
        ```

2.  Set a size limit of a file system:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem create --size number-and-unit --size-limit number-and-unit my-pool my-fs
    ```

    Note

    This option is available starting with Stratis 3.6.0.

    You can also remove the size limit later, if needed:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem unset-size-limit my-pool my-fs
    ```

**Verification**

-   List file systems within the pool to check if the Stratis file system is created:

    ``` {.language-plaintext tabindex="-1"}
    # stratis fs list my-pool
    ```

**Additional resources**

-   [Mounting a Stratis file system](#mounting-a-stratis-file-system "27.18. Mounting a Stratis file system")

### [27.18. Mounting a Stratis file system](#mounting-a-stratis-file-system) {#mounting-a-stratis-file-system .title}

Mount an existing Stratis file system to access the content.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   A Stratis file system is created. For more information, see [Creating a Stratis file system](#creating-a-stratis-file-system "27.17. Creating a Stratis file system").

**Procedure**

-   To mount the file system, use the entries that Stratis maintains in the `/dev/stratis/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/stratis/my-pool/my-fs mount-point
    ```

    The file system is now mounted on the *mount-point* directory and ready to use.

    Note

    Unmount all file systems belonging to a pool before stopping it. The pool does not stop if any file system is still mounted.

### [27.19. Configuring mounting a Stratis file system at boot](#configuring-mounting-a-Stratis-file-system-at-boot) {#configuring-mounting-a-stratis-file-system-at-boot .title}

You can configure a Stratis filesystem to mount at boot by configuring a mechanism that starts the pool correctly. Without this, the mount operation fails. Stratis provides two systemd services to support this process.

Note

Stratis does not support managing the root filesystem currently. These instructions apply only to non-root filesystems.

**Prerequisites**

-   A Stratis file system, for example *\<my-fs\>* is created on a Stratis pool, for example *\<my-pool\>*. For more information, see [Creating a Stratis file system](#creating-a-stratis-file-system "27.17. Creating a Stratis file system").
-   A mountpoint directory is created, for example *\<mount-point\>*.
-   The UUID of the filesystem's pool is determined, for example *\<pool-uuid\>*.

**Procedure**

-   As root, edit the `/etc/fstab`{.literal} file.

    -   Add `x-systemd.requires=stratis-fstab-setup@`{.literal}*`<pool-uuid>`{.literal}*`.service`{.literal} to the mount options of the `/etc/fstab`{.literal} entry:

        ``` {.language-plaintext tabindex="-1"}
        /dev/stratis/<my-pool>/<my-fs> <mount-point> xfs defaults,x-systemd.requires=stratis-fstab-setup@<pool-uuid>.service
        ```

    -   Add `x-systemd.requires=stratis-fstab-setup-with-network@`{.literal}*`<pool-uuid>`{.literal}*`.service`{.literal} and `_netdev`{.literal} if the pool is encrypted by using NBDE (Network Bound Disk Encryption) with Clevis:

        ``` {.language-plaintext tabindex="-1"}
        /dev/stratis/<my-pool>/<my-fs> <mount-point> xfs defaults,x-systemd.requires=stratis-fstab-setup-with-network@<pool-uuid>.service,_netdev
        ```

        Replace:

-   *\<my-pool\>* with the name of the Stratis pool that contains the file system.

-   *\<my-fs\>* with the name of the Stratis file system created within the pool.

-   *\<mount-point\>* with the name of the directory where you want to mount the file system.

-   *\<pool-uuid\>* with the UUID of the file system's pool.

    Important

    Mounting a Stratis filesystem from an encrypted Stratis pool on boot can cause the boot process to stop. This continues until a password is provided. If the pool is encrypted by using any unattended mechanism, for example, NBDE or TPM2, the Stratis pool is unlocked automatically. If not, the user may need to enter a password in the console to unlock the filesystem's pool.

### [27.20. Creating and configuring a Stratis file system by using the web console](#creating-and-configuring-a-Stratis-file-system-using-the-web-console) {#creating-and-configuring-a-stratis-file-system-by-using-the-web-console .title}

You can use the web console to create a file system on an existing Stratis pool.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   The `stratisd`{.literal} service is running.

-   A Stratis pool is created.

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click Storage.

3.  Click the Stratis pool on which you want to create a file system.

4.  On the **Stratis pool** page, scroll to the **Stratis filesystems** section and click Create new filesystem.

5.  Enter a name for the file system.

6.  Enter a mount point for the file system.

7.  Select the mount option.

8.  In the **At boot** drop-down menu, select when you want to mount your file system.

9.  Create the file system:

    -   If you want to create and mount the file system, click Create and mount.
    -   If you want to only create the file system, click Create only.

**Verification**

-   The new file system is visible on the **Stratis pool** page under the **Stratis filesystems** tab.

## [Chapter 28. Extending a Stratis pool with additional block devices](#extending-a-stratis-pool-with-additional-block-devices) {#chapter-28.-extending-a-stratis-pool-with-additional-block-devices .title}

You can attach additional block devices to a Stratis pool to provide more storage capacity for Stratis file systems. You can do it manually or by using the web console.

### [28.1. Adding block devices to a Stratis pool](#adding-block-devices-to-a-stratis-pool) {#adding-block-devices-to-a-stratis-pool .title}

You can add one or more block devices to a Stratis pool.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   The block device on which you are creating a Stratis pool is not in use, unmounted, and is at least 1 GB in space.

**Procedure**

-   To add one or more block devices to the pool, use:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool add-data my-pool device-1 device-2 device-n
    ```

### [28.2. Adding a block device to a Stratis pool by using the web console](#adding-a-block-device-to-a-stratis-pool-by-using-the-web-console) {#adding-a-block-device-to-a-stratis-pool-by-using-the-web-console .title}

You can use the web console to add a block device to an existing Stratis pool. You can also add caches as a block device.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   The `stratisd`{.literal} service is running.

-   A Stratis pool is created.

-   The block device on which you are creating a Stratis pool is not in use, unmounted, and is at least 1 GB in space.

**Procedure**

1.  Log in to the RHEL 10 web console.
2.  Click Storage.
3.  In the **Storage** table, click the Stratis pool to which you want to add a block device.
4.  On the **Stratis pool** page, click Add block devices and select the **Tier** where you want to add a block device as data or cache.
5.  If you are adding the block device to a Stratis pool that is encrypted with a passphrase, enter the passphrase.
6.  Under **Block devices**, select the devices you want to add to the pool.
7.  Click Add.

## [Chapter 29. Monitoring Stratis file systems](#monitoring-stratis-file-systems) {#chapter-29.-monitoring-stratis-file-systems .title}

As a Stratis user, you can view information about Stratis file systems on your system to monitor their state and free space.

### [29.1. Displaying information about Stratis file systems](#displaying-information-about-stratis-file-systems) {#displaying-information-about-stratis-file-systems .title}

You can list statistics about your Stratis file systems by using the `stratis`{.literal} utility. These include total, used, and free size, file systems, and block devices belonging to a pool.

The size of an XFS file system is the total amount of user data that it can manage. On a thinly provisioned Stratis pool, a Stratis file system can appear to have a size that is larger than the allocated space. The XFS file system is sized to match this apparent size, which means it is usually larger than the allocated space. Standard Linux utilities, such as df, report the size of the XFS file system. This value generally overestimates the space required by the XFS file system and hence the space allocated for it by Stratis.

Important

Regularly monitor the usage of your overprovisioned Stratis pools. If a file system usage approaches the allocated space, Stratis automatically increases the allocation by using available space in the pool. However, if all the available space is already allocated and the pool is full, no additional space can be assigned. This causes the file system to run out of space. This may lead to the risk of data loss in the application by using the Stratis file system.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, See [Installing Stratis](#installing-stratis "27.3. Installing Stratis").

**Procedure**

-   To display information about all **block devices** used for Stratis on your system:

    ``` {.language-plaintext tabindex="-1"}
    # stratis blockdev
    ```

    ``` {.language-plaintext tabindex="-1"}
    Pool Name   Device Node  Physical Size  Tier UUID
    my-pool     /dev/sdb     9.10 TiB       Data    ec9fb718-f83c-11ef-861e-7446a09dccfb
    ```

-   To display information about all Stratis **pools** on your system:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool
    ```

    ``` {.language-plaintext tabindex="-1"}
    Name     Total/Used/Free                 Properties  UUID                                  Alerts
    my-pool  8.00 GiB / 800.99 MiB / 7.22 GiB  -Ca,-Cr,Op   e22772c2-afe9-446c-9be5-2f78f682284e  WS001
    ```

-   To display information about all Stratis **file systems** on your system:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem
    ```

    ``` {.language-plaintext tabindex="-1"}
    Pool Filesystem  Total/Used/Free/Limit                 Device                     UUID
    Spool1  sfs1        1 TiB / 546 MiB / 1023.47 GiB / None  /dev/stratis/spool1/sfs1   223265f5-8f17-4cc2-bf12-c3e9e71ff7bf
    ```

    You can also display detailed information about a Stratis file system on your system by specifying the file system name or UUID:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem list my-pool --name my-fs
    ```

    ``` {.language-plaintext tabindex="-1"}
    UUID: 47255008-9bc7-4bd2-8294-e9d25cd9e7ba
    Name: my-fs
    Pool: my-pool
    Device: /dev/stratis/my-pool/my-fs
    Created: Nov 08 2018 08:03
    Snapshot origin: None
    Sizes:
        Logical size of thin device: 1 TiB
        Total used (including XFS metadata): 546 MiB
        Free: 1023.47 GiB
     Size Limit: None
    ```

### [29.2. Viewing a Stratis pool by using the web console](#viewing-a-stratis-pool-by-using-the-web-console) {#viewing-a-stratis-pool-by-using-the-web-console .title}

You can use the web console to view an existing Stratis pool and the file systems it contains.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   The `stratisd`{.literal} service is running.

-   You have an existing Stratis pool.

**Procedure**

1.  Log in to the RHEL 10 web console.

2.  Click Storage.

3.  In the **Storage** table, click the Stratis pool you want to view.

    The Stratis pool page displays all the information about the pool and the file systems that you created in the pool.

## [Chapter 30. Using snapshots on Stratis file systems](#using-snapshots-on-stratis-file-systems) {#chapter-30.-using-snapshots-on-stratis-file-systems .title}

You can use snapshots on Stratis file systems to capture file system state at arbitrary times and restore it in the future.

### [30.1. Characteristics of Stratis snapshots](#characteristics-of-stratis-snapshots) {#characteristics-of-stratis-snapshots .title}

Stratis snapshots are regular file systems created as point-in-time copies of other Stratis file systems. They operate independently of their source file system and can be used for backup, testing, or data recovery purposes.

The current snapshot implementation in Stratis is characterized by the following:

-   A snapshot of a file system is another file system.
-   A snapshot and its origin are not linked in lifetime. A snapshotted file system can live longer than the file system it was created from.
-   A file system does not have to be mounted to create a snapshot from it.
-   Each snapshot uses around half a gigabyte of actual backing storage, which is needed for the XFS log.

### [30.2. Creating a Stratis snapshot](#creating-a-stratis-snapshot) {#creating-a-stratis-snapshot .title}

You can create a Stratis file system as a snapshot of an existing Stratis file system.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   You have created a Stratis file system. For more information, see [Creating a Stratis file system](#creating-a-stratis-file-system "27.17. Creating a Stratis file system").

**Procedure**

-   Create a Stratis snapshot:

    ``` {.language-plaintext tabindex="-1"}
    # stratis fs snapshot my-pool my-fs my-fs-snapshot
    ```

    A snapshot is a first class Stratis file system. You can create multiple Stratis snapshots. These include snapshots of a single origin file system or another snapshot file system. If a file system is a snapshot, its **origin** field displays the UUID of its origin file system. This appears in the detailed file system listing.

### [30.3. Accessing the content of a Stratis snapshot](#accessing-the-content-of-a-stratis-snapshot) {#accessing-the-content-of-a-stratis-snapshot .title}

You can mount a snapshot of a Stratis file system to make it accessible for read and write operations.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   You have created a Stratis snapshot. For more information, see [Creating a Stratis snapshot](#creating-a-stratis-snapshot "30.2. Creating a Stratis snapshot").

**Procedure**

-   To access the snapshot, mount it as a regular file system from the `/dev/stratis/`{.literal}*`my-pool`{.literal}*`/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/stratis/my-pool/my-fs-snapshot mount-point
    ```

### [30.4. Reverting a Stratis file system to a previous snapshot](#reverting-a-stratis-file-system-to-a-previous-snapshot) {#reverting-a-stratis-file-system-to-a-previous-snapshot .title}

You can revert the content of a Stratis file system to the state captured in a Stratis snapshot.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   You have created a Stratis snapshot. For more information, see [Creating a Stratis snapshot](#creating-a-stratis-snapshot "30.2. Creating a Stratis snapshot").

**Procedure**

1.  Optional: Back up the current state of the file system to be able to access it later:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem snapshot my-pool my-fs my-fs-backup
    ```

2.  Schedule a revert of your file system to the previously taken snapshot:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem schedule-revert my-pool my-fs-snapshot
    ```

3.  Optional: Run the following to check if the revert is scheduled successfully:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem list my-pool --name my-fs-snapshot
    ```

    ``` {.language-plaintext tabindex="-1"}
    UUID: b14987eb-b735-4c68-8962-f53f6b644cbc
    Name: my-fs-snapshot
    Pool: my-pool

    Device: /dev/stratis/p1/my-fs-snapshot

    Created: Mar 18 2025 12:29

    Snapshot origin: f5a881b1-299d-4147-8ead-b4a56c623692
    Revert scheduled: Yes

    Sizes:
    Logical size of thin device: 1 TiB
    Total used (including XFS metadata): 5.42 GiB
    Free: 1018.58 GiB
    ```

    Note

    It is not possible to schedule more than one revert operation into the same origin filesystem. Also, if you try to destroy the origin file system, or the snapshot to which the revert is scheduled, the operation fails.

    You can also cancel the revert operation any time before you restart the pool:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem cancel-revert my-pool my-fs-snapshot
    ```

    You can run the following to check if the cancellation is scheduled successfully:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem list my-pool --name my-fs-snapshot
    ```

    ``` {.language-plaintext tabindex="-1"}
    UUID: b14987eb-b735-4c68-8962-f53f6b644cbc
    Name: my-fs-snapshot
    Pool: my-pool

    Device: /dev/stratis/p1/my-fs-snapshot

    Created: Mar 18 2025 12:29

    Snapshot origin: f5a881b1-299d-4147-8ead-b4a56c623692
    Revert scheduled: No

    Sizes:
    Logical size of thin device: 1 TiB
    Total used (including XFS metadata): 5.42 GiB
    Free: 1018.58 GiB

    Size Limit: None
    ```

    If not cancelled, the scheduled revert will proceed when you restart the pool:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool stop --name my-pool
    ```

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool start --name my-pool
    ```

**Verification**

1.  List the file system belonging to the pool:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem list my-pool
    ```

The `my-fs-snapshot`{.literal} now does not appear in the list of file systems in the pool. It is reverted to the previously copied `my-fs-snapshot`{.literal} state. The content of the file system named `my-fs`{.literal} is now identical to the snapshot `my-fs-snapshot`{.literal}.

### [30.5. Removing a Stratis snapshot](#removing-a-stratis-snapshot) {#removing-a-stratis-snapshot .title}

You can remove a Stratis snapshot from a pool. Data on the snapshot are lost.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information,see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   You have created a Stratis snapshot. For more information, see [Creating a Stratis snapshot](#creating-a-stratis-snapshot "30.2. Creating a Stratis snapshot").

**Procedure**

1.  Unmount the snapshot:

    ``` {.language-plaintext tabindex="-1"}
    # umount /dev/stratis/my-pool/my-fs-snapshot
    ```

2.  Destroy the snapshot:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem destroy my-pool my-fs-snapshot
    ```

## [Chapter 31. Removing Stratis file systems](#removing-stratis-file-systems) {#chapter-31.-removing-stratis-file-systems .title}

You can remove an existing Stratis file system or pool. Once a Stratis file system or pool is removed, it cannot be recovered.

### [31.1. Removing a Stratis file system](#removing-a-stratis-file-system) {#removing-a-stratis-file-system .title}

You can remove an existing Stratis file system. Data stored on it are lost.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").
-   You have created a Stratis file system. For more information, see [Creating a Stratis file system](#creating-a-stratis-file-system "27.17. Creating a Stratis file system").

**Procedure**

1.  Unmount the file system:

    ``` {.language-plaintext tabindex="-1"}
    # umount /dev/stratis/my-pool/my-fs
    ```

2.  Destroy the file system:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem destroy my-pool my-fs
    ```

**Verification**

-   Verify that the file system no longer exists:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem list my-pool
    ```

### [31.2. Deleting a file system from a Stratis pool by using the web console](#deleting-a-file-system-from-a-stratis-pool-by-using-the-web-console) {#deleting-a-file-system-from-a-stratis-pool-by-using-the-web-console .title}

You can use the web console to delete a file system from an existing Stratis pool. Deleting a Stratis pool file system erases all the data it contains.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   Stratis is installed and the `stratisd`{.literal} service is running.

    The web console detects and installs Stratis by default. However, for manually installing Stratis, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").

-   You have an existing Stratis pool and a file system is created on the Stratis pool.

**Procedure**

1.  Log in to the RHEL 10 web console.
2.  Click Storage.
3.  In the **Storage** table, click the Stratis pool from which you want to delete a file system.
4.  On the **Stratis pool** page, scroll to the **Stratis filesystems** section and click the menu button ⋮ for the file system you want to delete.
5.  From the drop-down menu, select Delete.
6.  In the **Confirm deletion** dialog box, click Delete.

### [31.3. Removing a Stratis pool](#removing-a-stratis-pool) {#removing-a-stratis-pool .title}

You can remove an existing Stratis pool. Data stored on it are lost.

**Prerequisites**

-   Stratis is installed and the `stratisd`{.literal} service is running. For more information, see [Installing Stratis](#installing-stratis "27.3. Installing Stratis").

-   You have created a Stratis pool:

    -   To create an unencrypted pool, see [Creating an unencrypted Stratis pool](#creating-an-unencrypted-stratis-pool "27.4. Creating an unencrypted Stratis pool").
    -   To create an encrypted pool, see [Creating an encrypted Stratis pool by using a key in the kernel keyring](#creating-an-encrypted-stratis-pool-using-a-key-in-the-kernel-keyring "27.6. Creating an encrypted Stratis pool by using a key in the kernel keyring").

**Procedure**

1.  List file systems on the pool:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem list my-pool
    ```

2.  Unmount all file systems on the pool:

    ``` {.language-plaintext tabindex="-1"}
    # umount /dev/stratis/my-pool/my-fs-1 \
             /dev/stratis/my-pool/my-fs-2 \
             /dev/stratis/my-pool/my-fs-n
    ```

3.  Destroy the file systems:

    ``` {.language-plaintext tabindex="-1"}
    # stratis filesystem destroy my-pool my-fs-1 my-fs-2
    ```

4.  Destroy the pool:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool destroy my-pool
    ```

**Verification**

-   Verify that the pool no longer exists:

    ``` {.language-plaintext tabindex="-1"}
    # stratis pool list
    ```

### [31.4. Deleting a Stratis pool by using the web console](#deleting-a-stratis-pool-by-using-the-web-console) {#deleting-a-stratis-pool-by-using-the-web-console .title}

You can use the web console to delete an existing Stratis pool. Deleting a Stratis pool erases all the data it contains.

**Prerequisites**

-   You have installed the RHEL 10 web console.

    For instructions, see [Installing and enabling the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_systems_in_the_rhel_web_console/getting-started-with-the-rhel-web-console#installing-and-enabling-the-web-console).

-   The `stratisd`{.literal} service is running.

-   You have an existing Stratis pool.

**Procedure**

1.  Log in to the RHEL 10 web console.
2.  Click Storage.
3.  In the **Storage** table, click the menu button ⋮ for the Stratis pool you want to delete.
4.  From the drop-down menu, select Delete pool.
5.  In the **Permanently delete pool** dialog box, click Delete.

## [Chapter 32. Getting started with an ext4 file system](#getting-started-with-an-ext4-file-system) {#chapter-32.-getting-started-with-an-ext4-file-system .title}

As a system administrator, you can create, mount, resize, back up, and restore ext4 file systems. The ext4 file system is a scalable extension of ext3. In Red Hat Enterprise Linux 10, it supports individual files up to 16 TB and file systems up to 50 TB.

### [32.1. Features of an ext4 file system](#features-of-an-ext4-file-system) {#features-of-an-ext4-file-system .title}

Explore key ext4 file system features, including extents for efficient large file handling, improved file system check times, advanced allocation techniques, metadata integrity, extended attributes, quota journaling, and subsecond timestamps.

Following are details of the features of an ext4 file system:

-   Using extents: The ext4 file system uses extents, which improves performance when using large files and reduces metadata overhead for large files.

-   Ext4 labels unallocated block groups and inode table sections so they can be skipped during a file system check. It leads to a quick file system check, which becomes more beneficial as the file system grows in size.

-   Metadata checksum: By default, this feature is enabled in Red Hat Enterprise Linux 10.

-   Allocation features of an ext4 file system:

    -   Persistent pre-allocation
    -   Delayed allocation
    -   Multi-block allocation
    -   Stripe-aware allocation

-   Extended attributes (`xattr`{.literal}): This allows the system to associate several additional name and value pairs per file.

-   Quota journaling: This avoids the need for lengthy quota consistency checks after a crash.

    Note

    The only supported journaling mode in ext4 is `data=ordered`{.literal} (default).

-   Subsecond timestamps - This gives timestamps to the subsecond.

For more information, see the `ext4`{.literal} man page on your system.

**Additional resources**

-   [Is the EXT journaling option \"data=writeback\" supported in RHEL?](https://access.redhat.com/solutions/424073)

### [32.2. Creating an ext4 file system](#creating-an-ext4-file-system) {#creating-an-ext4-file-system .title}

As a system administrator, you can create an ext4 file system on a block device by using `mkfs.ext4`{.literal} command.

**Prerequisites**

-   A partition on your disk. For information about creating Master Boot Record (MBR) or GUID Partition Table (GPT) partitions, see [Creating a partition table on a disk with parted](#creating-a-partition-table-on-a-disk-with-parted "7.2. Creating a partition table on a disk with parted").
-   Alternatively, use an Logical Volume Manager (LVM) or Multiple Device (MD) volume.

**Procedure**

1.  To create an ext4 file system:

    -   For a regular-partition device, an LVM volume, an MD volume, or a similar device, use the following command:

        ``` {.language-plaintext tabindex="-1"}
        # mkfs.ext4 /dev/block_device
        ```

        Replace /dev/*block_device* with the path to a block device.

        For example, `/dev/sdb1`{.literal}, `/dev/disk/by-uuid/05e99ec8-def1-4a5e-8a9d-5945339ceb2a`{.literal}, or `/dev/my-volgroup/my-lv`{.literal}. In general, the default options are optimal for most usage scenarios.

    -   For striped block devices (for example, RAID5 arrays), the stripe geometry can be specified at the time of file system creation. Using proper stripe geometry enhances the performance of an ext4 file system. For example, to create a file system with a 64k stride (that is, 16 x 4096) on a 4k-block file system, use the following command:

        ``` {.language-plaintext tabindex="-1"}
        # mkfs.ext4 -E stride=16,stripe-width=64 /dev/block_device
        ```

        In the given example:

        -   stride=value: Specifies the RAID chunk size
        -   stripe-width=value: Specifies the number of data disks in a RAID device, or the number of stripe units in the stripe.

    Note

    -   To specify a UUID when creating a file system:

        ``` {.language-plaintext tabindex="-1"}
        # mkfs.ext4 -U UUID /dev/block_device
        ```

        Replace *UUID* with the UUID you want to set: for example, `7cd65de3-e0be-41d9-b66d-96d749c02da7`{.literal}.

        Replace /dev/*block_device* with the path to an ext4 file system to have the UUID added to it: for example, `/dev/sda8`{.literal}.

    -   To specify a label when creating a file system:

        ``` {.language-plaintext tabindex="-1"}
        # mkfs.ext4 -L label-name /dev/block_device
        ```

2.  To view the created ext4 file system:

    ``` {.language-plaintext tabindex="-1"}
    # blkid
    ```

### [32.3. Mounting an ext4 file system](#mounting-an-ext4-file-system) {#mounting-an-ext4-file-system .title}

As a system administrator, you can mount an ext4 file system by using the `mount`{.literal} utility.

**Prerequisites**

-   An ext4 file system. For information about creating an ext4 file system, see [Creating an ext4 file system](#creating-an-ext4-file-system "32.2. Creating an ext4 file system").

**Procedure**

1.  To create a mount point to mount the file system:

    ``` {.language-plaintext tabindex="-1"}
    # mkdir /mount/point
    ```

    Replace */mount/point* with the directory name where mount point of the partition must be created.

2.  To mount an ext4 file system:

    -   To mount an ext4 file system with no extra options:

        ``` {.language-plaintext tabindex="-1"}
        # mount /dev/block_device /mount/point
        ```

    -   To mount the file system persistently, see [Persistently mounting file systems](#persistently-mounting-file-systems "Chapter 19. Persistently mounting file systems").

3.  To view the mounted file system:

    ``` {.language-plaintext tabindex="-1"}
    # df -h
    ```

### [32.4. Resizing an ext4 file system](#resizing-an-ext4-file-system) {#resizing-an-ext4-file-system .title}

As a system administrator, you can resize an ext4 file system by using the `resize2fs`{.literal} utility. The `resize2fs`{.literal} utility reads the size in units of file system block size, unless a suffix indicating a specific unit is used.

The following suffixes indicate specific units:

-   s (sectors) - `512`{.literal} byte sectors
-   K (kilobytes) - `1,024`{.literal} bytes
-   M (megabytes) - `1,048,576`{.literal} bytes
-   G (gigabytes) - `1,073,741,824`{.literal} bytes
-   T (terabytes) - `1,099,511,627,776`{.literal} bytes

**Prerequisites**

-   An ext4 file system. For information about creating an ext4 file system, see [Creating an ext4 file system](#creating-an-ext4-file-system "32.2. Creating an ext4 file system").
-   An underlying block device of an appropriate size to hold the file system after resizing.

**Procedure**

1.  To resize an ext4 file system, take the following steps:

    -   To shrink and grow the size of an unmounted ext4 file system:

        ``` {.language-plaintext tabindex="-1"}
        # umount /dev/block_device
        ```

        ``` {.language-plaintext tabindex="-1"}
        # e2fsck -f /dev/block_device
        ```

        ``` {.language-plaintext tabindex="-1"}
        # resize2fs /dev/block_device size
        ```

        Replace */dev/block_device* with the path to the block device, for example `/dev/sdb1`{.literal}.

        Replace *size* with the required resize value by using `s`{.literal}, `K`{.literal}, `M`{.literal}, `G`{.literal}, and `T`{.literal} suffixes.

    -   An ext4 file system may be grown while mounted by using the `resize2fs`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        # resize2fs /mount/device size
        ```

        Note

        The size parameter is optional (and often redundant) when expanding. The `resize2fs`{.literal} automatically expands to fill the available space of the container, usually a logical volume or partition.

2.  To view the resized file system:

    ``` {.language-plaintext tabindex="-1"}
    # df -h
    ```

### [32.5. Comparison of tools used with ext4 and XFS](#comparison-of-tools-used-with-ext4-and-xfs_getting-started-with-an-ext4-file-system) {#comparison-of-tools-used-with-ext4-and-xfs-1 .title}

Different tools and commands accomplish common file system tasks on ext4 and XFS, including creation, checking, resizing, and backup operations.

This section compares which tools to use to accomplish common tasks on the ext4 and XFS file systems.

+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Task                           | ext4                                  | XFS                                                    |
+:===============================+:======================================+:=======================================================+
| Create a file system           | `mkfs.ext4`{.literal}                 | `mkfs.xfs`{.literal}                                   |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| File system check              | `e2fsck`{.literal}                    | `xfs_repair`{.literal}                                 |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Resize a file system           | `resize2fs`{.literal}                 | `xfs_growfs`{.literal}                                 |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Save an image of a file system | `e2image`{.literal}                   | `xfs_metadump`{.literal} and `xfs_mdrestore`{.literal} |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Label or tune a file system    | `tune2fs`{.literal}                   | `xfs_admin`{.literal}                                  |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Back up a file system          | `tar`{.literal} and `rsync`{.literal} | `xfsdump`{.literal} and `xfsrestore`{.literal}         |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| Quota management               | `quota`{.literal}                     | `xfs_quota`{.literal}                                  |
+--------------------------------+---------------------------------------+--------------------------------------------------------+
| File mapping                   | `filefrag`{.literal}                  | `filefrag`{.literal}                                   |
+--------------------------------+---------------------------------------+--------------------------------------------------------+

Show more

Note

If you want a complete client-server solution for backups over network, you can use `bacula`{.literal} backup utility that is available in RHEL 9. For more information about Bacula, see [Bacula backup solution](https://www.bacula.org/documentation/documentation/).

## [Legal Notice](#idm139944793744784) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
