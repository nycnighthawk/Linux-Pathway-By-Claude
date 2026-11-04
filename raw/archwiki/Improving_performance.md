---
{"title": "Improving performance", "url": "https://wiki.archlinux.org/title/Improving_performance", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Improving performance

Related articles

-   [/Boot process](../en/Improving_performance/Boot_process.html "Improving performance/Boot process")
-   [Pacman/Tips and tricks#Performance](../en/Pacman/Tips_and_tricks.html#Performance "Pacman/Tips and tricks")
-   [OpenSSH#Speeding up SSH](../en/OpenSSH.html#Speeding_up_SSH "OpenSSH")
-   [Openoffice#Speed up OpenOffice](../en/Apache_OpenOffice.html#Speed_up_OpenOffice "Openoffice")
-   [Laptop](../en/Laptop.html "Laptop")
-   [Preload](../en/Preload.html "Preload")

This article provides information on basic system diagnostics relating to performance as well as steps that may be taken to reduce resource consumption or to otherwise optimize the system with the end-goal being either perceived or documented improvements to a system\'s performance. See also [Gaming#Improving performance](../en/Gaming.html#Improving_performance "Gaming") for additional gaming and low latency specific advice.

## The basics {#The_basics}

### Know your system {#Know_your_system}

The best way to tune a system is to target bottlenecks, or subsystems which limit overall speed. The system specifications can help identify them.

-   If the computer becomes slow when large applications (such as LibreOffice and Firefox) run at the same time, check if the amount of RAM is sufficient. Use the following command, and check the \"available\" column:

        $ free -h

-   If boot time is slow, and applications take a long time to load at first launch (only), then the hard drive is likely to blame. The speed of a hard drive can be measured with the `hdparm` command:

        # hdparm -t /dev/sdX

    **Note** [hdparm](https://archlinux.org/packages/?name=hdparm) indicates only the pure read speed of a hard drive, and is not a valid benchmark. A value higher than 40MB/s (while idle) is however acceptable on an average system.

-   If CPU load is consistently high even with enough RAM available, then try to lower CPU usage by disabling running [daemons](../en/Systemd.html "Daemons") and/or processes. This can be monitored in several ways, for example with [htop](https://archlinux.org/packages/?name=htop), `pstree` or any other [system monitoring](../en/List_of_applications/Utilities.html#System_monitors "List of applications/Utilities") tool:

        $ htop

-   If applications using direct rendering are slow (i.e those which use the GPU, such as video players, games, or even a [window manager](../en/Window_manager.html "Window manager")), then improving GPU performance should help. The first step is to verify if direct rendering is actually enabled. This is indicated by the `glxinfo` command, part of the [mesa-utils](https://archlinux.org/packages/?name=mesa-utils) package, which should return `direct rendering: Yes` when used:

        $ glxinfo | grep "direct rendering"

-   When running a [desktop environment](../en/Desktop_environment.html "Desktop environment"), disabling (unused) visual desktop effects may reduce GPU usage. Use a more lightweight environment or create a [custom environment](../en/Desktop_environment.html#Custom_environments "Desktop environment") if the current does not meet the hardware and/or personal requirements.

-   Using an optimized [kernel](../en/Kernel.html "Kernel") improves performance. Generally, [linux-zen](https://archlinux.org/packages/?name=linux-zen) is a good option. However, the default kernel can be tweaked as shown in certain parts of this article to perform better.

### Benchmarking {#Benchmarking}

The effects of optimization are often difficult to judge. They can however be measured by [benchmarking](../en/Benchmarking.html "Benchmarking") tools.

## Storage devices {#Storage_devices}

### Sector size {#Sector_size}

Check that your NVMe drives and Advanced Format hard disk drives are using the [optimal logical sector size](../en/Advanced_Format.html "Advanced Format").

### Partitioning {#Partitioning}

Make sure that your partitions are [properly aligned](../en/Partitioning.html#Partition_alignment "Partitioning").

#### Multiple drives {#Multiple_drives}

If you have multiple disks available, you can set them up as a software [RAID](../en/RAID.html "RAID") for serious speed improvements.

Creating [swap](../en/Swap.html "Swap") on a separate disk can also help quite a bit, especially if your machine swaps frequently.

##### An SSD as a cache for an HDD {#An_SSD_as_a_cache_for_an_HDD}

When forgoing hard disk drives is not an option, a solid state drive can be added as a caching layer to improve the read and/or write speeds and reduce the noise from random access. The options to accomplish this include [LVM#Cache](../en/LVM.html#Cache "LVM"), [Bcache](../en/Bcache.html "Bcache") and [Bcachefs#SSD caching](../en/Bcachefs.html#SSD_caching "Bcachefs").

#### Layout on HDDs {#Layout_on_HDDs}

If using a traditional spinning HDD, your partition layout can influence the system\'s performance. Sectors at the beginning of the drive (closer to the outside of the disk) are faster than those at the end. Also, a smaller partition requires less movements from the drive\'s head, and so speed up disk operations. Therefore, it is advised to create a small partition (15-20GiB, more or less depending on your needs) only for your system, as near to the beginning of the drive as possible. Other data (pictures, videos) should be kept on a separate partition, and this is usually achieved by separating the home directory (`/home`) from the system (`/`).

**Note** As with all advice on this page, measure what benefits are provided: unless [short stroking](https://blog.stuffedcow.net/2019/09/hard-disk-geometry-microbenchmarking/#shortstroke) the hard drive and using only a few percent of its total capacity, separating partitions will improve access time by only a few percent since the read/write operations will still be spread over the whole drive in general use. Comparatively, upgrading to an SSD will improve performance by more than an order of magnitude.

### Choosing and tuning your filesystem {#Choosing_and_tuning_your_filesystem}

Choosing the best filesystem for a specific system is very important because each has its own strengths. The [File systems](../en/File_systems.html "File systems") article provides a short summary of the most popular ones. You can also find relevant articles in [Category:File systems](../en/Category:File_systems.html "Category:File systems").

#### Mount options {#Mount_options}

The various [\*atime](../en/Fstab.html#atime_options "Fstab") options can mitigate the performance penalty of `strictatime`.

Other mount options are filesystem specific, therefore see the relevant articles for the filesystems:

-   [Ext3](../en/Ext3.html "Ext3")
-   [Ext4#Improving performance](../en/Ext4.html#Improving_performance "Ext4")
-   [JFS#Optimizations](../en/JFS.html#Optimizations "JFS")
-   [XFS#Performance](../en/XFS.html#Performance "XFS")
-   [Btrfs#Defragmentation](../en/Btrfs.html#Defragmentation "Btrfs"), [Btrfs#Compression](../en/Btrfs.html#Compression "Btrfs"), and [btrfs(5)](https://man.archlinux.org/man/btrfs.5)
-   [ZFS#Tuning](../en/ZFS.html#Tuning "ZFS")
-   [NTFS#Improving performance](../en/NTFS.html#Improving_performance "NTFS")

### Tuning kernel parameters {#Tuning_kernel_parameters}

There are several key tunables affecting the performance of block devices, see [sysctl#Virtual memory](../en/Sysctl.html#Virtual_memory "Sysctl") for more information.

### Input/output schedulers {#Input/output_schedulers}

#### Background information {#Background_information}

The input/output *(I/O)* scheduler is the kernel component that decides in which order the block I/O operations are submitted to storage devices. It is useful to remind here some specifications of two main drive types because the goal of the I/O scheduler is to optimize the way these are able to deal with read requests:

-   An HDD has spinning disks and a head that moves physically to the required location. Therefore, random latency is quite high ranging between 3 and 12ms (whether it is a high end server drive or a laptop drive and bypassing the disk controller write buffer) while sequential access provides much higher throughput. The typical HDD throughput is about 200 I/O operations per second *(IOPS)*.

&nbsp;

-   An SSD does not have moving parts, random access is as fast as sequential one, typically under 0.1ms, and it can handle multiple concurrent requests. The typical SSD throughput is greater than 10,000 IOPS, which is more than needed in common workload situations.

If there are many processes making I/O requests to different storage parts, thousands of IOPS can be generated while a typical HDD can handle only about 200 IOPS. There is a queue of requests that have to wait for access to the storage. This is where the I/O schedulers plays an optimization role.

#### The scheduling algorithms {#The_scheduling_algorithms}

One way to improve throughput is to linearize access: by ordering waiting requests by their logical address and grouping the closest ones. Historically this was the first Linux I/O scheduler called [elevator](https://en.wikipedia.org/wiki/Elevator_algorithm "wikipedia:Elevator algorithm").

One issue with the elevator algorithm is that it is not optimal for a process doing sequential access: reading a block of data, processing it for several microseconds then reading next block and so on. The elevator scheduler does not know that the process is about to read another block nearby and, thus, moves to another request by another process at some other location. The [anticipatory](https://en.wikipedia.org/wiki/Anticipatory_scheduling "wikipedia:Anticipatory scheduling") I/O scheduler overcomes the problem: it pauses for a few milliseconds in anticipation of another close-by read operation before dealing with another request.

While these schedulers try to improve total throughput, they might leave some unlucky requests waiting for a very long time. As an example, imagine the majority of processes make requests at the beginning of the storage space while an unlucky process makes a request at the other end of storage. This potentially infinite postponement of the process is called starvation. To improve fairness, the [deadline](https://en.wikipedia.org/wiki/Deadline_scheduler "wikipedia:Deadline scheduler") algorithm was developed. It has a queue ordered by address, similar to the elevator, but if some request sits in this queue for too long then it moves to an \"expired\" queue ordered by expire time. The scheduler checks the expire queue first and processes requests from there and only then moves to the elevator queue. Note that this fairness has a negative impact on overall throughput.

The [Completely Fair Queuing (CFQ)](https://en.wikipedia.org/wiki/CFQ "wikipedia:CFQ") approaches the problem differently by allocating a timeslice and a number of allowed requests by queue depending on the priority of the process submitting them. It supports [cgroup](../en/Cgroups.html "Cgroup") that allows to reserve some amount of I/O to a specific collection of processes. It is in particular useful for shared and cloud hosting: users who paid for some IOPS want to get their share whenever needed. Also, it idles at the end of synchronous I/O waiting for other nearby operations, taking over this feature from the *anticipatory* scheduler and bringing some enhancements. Both the *anticipatory* and the *elevator* schedulers were decommissioned from the Linux kernel replaced by the more advanced alternatives presented below.

The [Budget Fair Queuing (BFQ)](https://docs.kernel.org/block/bfq-iosched.html) is based on CFQ code and brings some enhancements. It does not grant the disk to each process for a fixed time-slice but assigns a \"budget\" measured in number of sectors to the process and uses heuristics. It is a relatively complex scheduler, it may be more adapted to rotational drives and slow SSDs because its high per-operation overhead, especially if associated with a slow CPU, can slow down fast devices. The objective of BFQ on personal systems is that for interactive tasks, the storage device is virtually as responsive as if it was idle. In its default configuration it focuses on delivering the lowest latency rather than achieving the maximum throughput, which can sometimes greatly [accelerate the startup of applications](https://www.phoronix.com/review/linux-50hdd-io/2) on hard drives.

[Kyber](https://lwn.net/Articles/720675/) is a recent scheduler inspired by active queue management techniques used for network routing. The implementation is based on \"tokens\" that serve as a mechanism for limiting requests. A queuing token is required to allocate a request, this is used to prevent starvation of requests. A dispatch token is also needed and limits the operations of a certain priority on a given device. Finally, a target read latency is defined and the scheduler tunes itself to reach this latency goal. The implementation of the algorithm is relatively simple and it is deemed efficient for fast devices.

#### Kernel\'s I/O schedulers {#Kernel's_I/O_schedulers}

While some of the early algorithms have now been decommissioned, the official Linux kernel supports a number of I/O schedulers. The [Multi-Queue Block I/O Queuing Mechanism (blk-mq)](https://www.thomas-krenn.com/en/wiki/Linux_Multi-Queue_Block_IO_Queueing_Mechanism_(blk-mq)) maps I/O queries to multiple queues, the tasks are distributed across threads and therefore CPU cores. Within this framework the following schedulers are available:

-   *None*, where no queuing algorithm is applied.
-   *mq-deadline*, the adaptation of the deadline scheduler (see below) to multi-threading.
-   *Kyber*
-   *BFQ*

#### Changing I/O scheduler {#Changing_I/O_scheduler}

**Note** The best choice of scheduler depends on both the device and the exact nature of the workload. Also, the throughput in MB/s is not the only measure of performance: deadline or fairness deteriorate the overall throughput but may improve system responsiveness. [Benchmarking](../en/Benchmarking.html "Benchmarking") may be useful to indicate each I/O scheduler performance.

To list the available schedulers for a device and the active scheduler (in brackets):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ cat /sys/block/sda/queue/scheduler
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
mq-deadline kyber [bfq] none
```

To list the available schedulers for all devices:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ grep "" /sys/block/*/queue/scheduler
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
/sys/block/pktcdvd0/queue/scheduler:none
/sys/block/sda/queue/scheduler:mq-deadline kyber [bfq] none
/sys/block/sr0/queue/scheduler:[mq-deadline] kyber bfq none
```

To change the active I/O scheduler to *bfq* for device *sda*, use:

    # echo bfq > /sys/block/sda/queue/scheduler

The process to change I/O scheduler, depending on whether the disk is rotating or not can be automated and persist across reboots. For example the [udev](../en/Udev.html "Udev") rules below set the scheduler to *bfq* for rotational drives, *bfq* for [SSD](../en/Solid_state_drive.html "SSD")/eMMC drives and *none* for [NVMe](../en/Solid_state_drive/NVMe.html "NVMe") drives:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/udev/rules.d/60-ioschedulers.rules
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
# HDD
ACTION=="add|change", KERNEL=="sd[a-z]*", ATTR{queue/rotational}=="1", ATTR{queue/scheduler}="bfq"

# SSD
ACTION=="add|change", KERNEL=="sd[a-z]*|mmcblk[0-9]*", ATTR{queue/rotational}=="0", ATTR{queue/scheduler}="bfq"

# NVMe SSD
ACTION=="add|change", KERNEL=="nvme[0-9]*", ENV{DEVTYPE}=="disk", ATTR{queue/scheduler}="none"
```

Reboot or force [udev#Loading new rules](../en/Udev.html#Loading_new_rules "Udev").

#### Tuning I/O scheduler {#Tuning_I/O_scheduler}

Each of the kernel\'s I/O scheduler has its own tunables, such as the latency time, the expiry time or the FIFO parameters. They are helpful in adjusting the algorithm to a particular combination of device and workload. This is typically to achieve a higher throughput or a lower latency for a given utilization. The tunables and their description can be found within the [kernel documentation](https://docs.kernel.org/block/index.html).

To list the available tunables for a device, in the example below *sdb* which is using *deadline*, use:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
$ ls /sys/block/sdb/queue/iosched
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
fifo_batch  front_merges  read_expire  write_expire  writes_starved
```

To improve *deadline\'*s throughput at the cost of latency, one can increase `fifo_batch` with the command:

    # echo 32 > /sys/block/sdb/queue/iosched/fifo_batch

### Power management configuration and write cache {#Power_management_configuration_and_write_cache}

When dealing with traditional rotational disks (HDDs) you may want to completely disable or lower power saving features, and check if the write cache is enabled.

See [Hdparm#Power management configuration](../en/Hdparm.html#Power_management_configuration "Hdparm") and [Hdparm#Write cache](../en/Hdparm.html#Write_cache "Hdparm").

Afterwards, you can make a [udev rule](../en/Hdparm.html#Persistent_configuration_using_udev_rule "Hdparm") to apply them on boot-up.

**Tip** [GNOME](../en/GNOME.html "GNOME") allows the setting of some of these parameters through the Disks application and does not require a udev rule.

**Note** Some features might not be supported by your hard drive. If that\'s the case, Hdparm will notify you. Hence, simply ignore the configuration of this certain feature.

### Reduce disk reads/writes {#Reduce_disk_reads/writes}

Avoiding unnecessary access to slow storage drives is good for performance and also increasing lifetime of the devices, although on modern hardware the difference in life expectancy is usually negligible.

**Note** A 32GB SSD with a mediocre 10x write amplification factor, a standard 10000 write/erase cycle, and **10GB of data written per day**, would get an **8 years life expectancy**. It gets better with [bigger SSDs](https://kcall.co.uk/ssd/) and modern controllers with less write amplification. See also [this endurance experiment](https://web.archive.org/web/20161124030749/http://techreport.com/review/27909/the-ssd-endurance-experiment-theyre-all-dead) when considering whether any particular strategy to limit disk writes is actually needed.

#### Show disk writes {#Show_disk_writes}

The [iotop](https://archlinux.org/packages/?name=iotop) package can sort by disk writes, and show how much and how frequently programs are writing to the disk. See [iotop(8)](https://man.archlinux.org/man/iotop.8) for details.

#### Relocate files to tmpfs {#Relocate_files_to_tmpfs}

Relocate files, such as your browser profile, to a [tmpfs](../en/Tmpfs.html "Tmpfs") file system, for improvements in application response as all the files are now stored in RAM:

-   Refer to [Profile-sync-daemon](../en/Profile-sync-daemon.html "Profile-sync-daemon") for syncing browser profiles. Certain browsers might need special attention, see e.g. [Firefox on RAM](../en/Firefox_on_RAM.html "Firefox on RAM").
-   Refer to [Anything-sync-daemon](../en/Anything-sync-daemon.html "Anything-sync-daemon") for syncing any specified folder.
-   Refer to [Makepkg#Improving build times](../en/Makepkg.html#Improving_build_times "Makepkg") for improving compile times by building packages in tmpfs.

#### File systems {#File_systems}

Refer to corresponding [file system](../en/File_system.html "File system") page in case there were performance improvements instructions, see the list at [#Choosing and tuning your filesystem](#Choosing_and_tuning_your_filesystem).

#### Swap space {#Swap_space}

See [Swap#Performance](../en/Swap.html#Performance "Swap") for details.

#### Writeback interval and buffer size {#Writeback_interval_and_buffer_size}

See [Sysctl#Virtual memory](../en/Sysctl.html#Virtual_memory "Sysctl") for details.

#### Disable core dumps {#Disable_core_dumps}

See [Core dump#Disabling automatic core dumps](../en/Core_dump.html#Disabling_automatic_core_dumps "Core dump").

### Storage I/O scheduling with ionice {#Storage_I/O_scheduling_with_ionice}

Many tasks such as backups do not rely on a short storage I/O delay or high storage I/O bandwidth to fulfill their task, they can be classified as background tasks. On the other hand quick I/O is necessary for good UI responsiveness on the desktop. Therefore it is beneficial to reduce the amount of storage bandwidth available to background tasks, whilst other tasks are in need of storage I/O. This can be achieved by making use of the Linux I/O scheduler BFQ, which allows setting different priorities for processes.

The I/O priority of a background process can be reduced to the \"Idle\" level by starting it with

    $ ionice -c 3 command

See [a short introduction to ionice](https://www.cyberciti.biz/tips/linux-set-io-scheduling-class-priority.html) and [ionice(1)](https://man.archlinux.org/man/ionice.1) for more information.

### Trimming {#Trimming}

For optimal performance, empty blocks of solid state drives should be discarded (a.k.a. trimmed) periodically to optimize random write speeds. See [Solid state drive#TRIM](../en/Solid_state_drive.html#TRIM "Solid state drive") for more information.

## Network {#Network}

### General information {#General_information}

-   Kernel networking: see [Sysctl#Improving performance](../en/Sysctl.html#Improving_performance "Sysctl")
-   NIC: see [Network configuration#Set device MTU and queue length](../en/Network_configuration.html#Set_device_MTU_and_queue_length "Network configuration")
-   DNS: consider using a caching DNS resolver, see [Domain name resolution#DNS servers](../en/Domain_name_resolution.html#DNS_servers "Domain name resolution")
-   Samba: see [Samba#Improve throughput](../en/Samba.html#Improve_throughput "Samba")

### Regulatory domain {#Regulatory_domain}

**This article or section is a candidate for merging with [Network configuration/Wireless#Respecting the regulatory domain](../en/Network_configuration/Wireless.html#Respecting_the_regulatory_domain "Network configuration/Wireless").**

**Notes:** We already have a good section on this at the target page, might be beneficial to move most of the content there and just leave this as a stub with emphasis on the kernel parameter to override the settings when applied incorrectly. (Discuss in [Talk:Improving performance](../en/Talk:Improving_performance.html))

Different countries have different standards for wireless network services, and you will typically be able to achieve a stronger signal by setting the correct domain for your network configuration. This will typically be configured during setup, but in some cases [the settings will not be applied correctly](https://community.frame.work/t/responded-amd-rz616-wifi-card-doesnt-work-with-6ghz-on-kernel-6-7/43226). Check the contents of `/sys/module/cfg80211/parameters/ieee80211_regdom`; if the value is `00` (a global setting that is generally more restrictive) or set to the incorrect region, try adding the following [kernel parameter](../en/Kernel_parameter.html "Kernel parameter"), replacing *`XX`* with the correct country code (e.g., `US` for the United States):

    cfg80211.ieee80211_regdom=XX

Then reboot your system.

### Power management {#Power_management}

Certain devices have issues whereby their network adapters will incorrectly entering power saving mode while still in use, throttling performance or causing disconnections. If this happens to you, ensure that you [upgrade](../en/System_maintenance.html#Upgrading_the_system "Upgrade") your packages to the latest version to receive any necessary firmware updates, and see [Power management#Network interfaces](../en/Power_management.html#Network_interfaces "Power management").

## CPU {#CPU}

### Overclocking {#Overclocking}

[Overclocking](https://en.wikipedia.org/wiki/Overclocking "wikipedia:Overclocking") improves the computational performance of the CPU by increasing its peak clock frequency. The ability to overclock depends on the combination of CPU model and motherboard model. It is most frequently done through the BIOS. Overclocking also has disadvantages and risks. It is neither recommended nor discouraged here.

Many Intel chips will not correctly report their clock frequency to acpi_cpufreq and most other utilities. This will result in excessive messages in [dmesg](../en/Core_utilities.html#Essentials "Dmesg"), which can be avoided by unloading and blacklisting the kernel module `acpi_cpufreq`. To read their clock speed use *i7z* from the [i7z](https://aur.archlinux.org/packages/i7z/)^AUR^ package. To check for correct operation of an overclocked CPU, it is recommended to do [stress testing](../en/Stress_testing.html "Stress testing").

### Frequency scaling {#Frequency_scaling}

See [CPU frequency scaling](../en/CPU_frequency_scaling.html "CPU frequency scaling").

### CPU scheduler {#CPU_scheduler}

The default CPU scheduler in the mainline Linux kernel is [EEVDF](https://lwn.net/Articles/925371/).

**This article or section needs expansion.**

**Reason:** Add CFS, the previous default scheduler, to the list. (Discuss in [Talk:Improving performance](../en/Talk:Improving_performance.html))

-   **[Project C](https://cchalpha.blogspot.com/2020/05/project-c-announcement.html)** --- Cross-project for refactoring BMQ into Project C, with re-creation of PDS based on the Project C code base. So it is a merge of the two projects, with a subsequent update of the PDS as Project C. Recommended as a more recent development.

[https://cchalpha.blogspot.com/](https://cchalpha.blogspot.com/) \|\| [linux-prjc](https://aur.archlinux.org/packages/linux-prjc/)^AUR^

-   **BORE** --- The BORE scheduler focuses on sacrificing some fairness for lower latency in scheduling interactive tasks, it is built on top of CFS and is only adjusted for vruntime code updates, so the overall changes are quite small compared to other unofficial CPU schedulers.

[https://github.com/firelzrd/bore-scheduler](https://github.com/firelzrd/bore-scheduler) \|\| [linux-cachyos-bore](https://aur.archlinux.org/packages/linux-cachyos-bore/)^AUR^

-   **SCX** --- Allows dynamic injection of various CPU schedulers without requiring a system reset.

[https://github.com/sched-ext/scx](https://github.com/sched-ext/scx) \|\| [scx-scheds](https://archlinux.org/packages/?name=scx-scheds)

### Real-time kernel {#Real-time_kernel}

Some applications such as running a TV tuner card at full HD resolution (1080p) may benefit from using a [realtime kernel](../en/Realtime_kernel.html "Realtime kernel").

### Adjusting priorities of processes {#Adjusting_priorities_of_processes}

See also [nice(1)](https://man.archlinux.org/man/nice.1) and [renice(1)](https://man.archlinux.org/man/renice.1).

#### Ananicy Cpp {#Ananicy_Cpp}

[Ananicy Cpp](https://gitlab.com/ananicy-cpp/ananicy-cpp) ([ananicy-cpp](https://archlinux.org/packages/?name=ananicy-cpp)) is a daemon for automatically adjusting the nice levels of processes. The nice level represents the priority of the process when allocating CPU resources.

**Note** [GameMode](../en/GameMode.html "GameMode") and Ananicy Cpp both adjust the nice levels of processes. However, combining both tools is not recommended.[\[1\]](https://github.com/CachyOS/ananicy-rules/blob/master/README.md#gamemode--ananicy-cpp--bad-idea)

**Tip** A community-maintained list of Ananicy rules is available on GitHub at [CachyOS/ananicy-rules](https://github.com/CachyOS/ananicy-rules), which is packaged as [cachyos-ananicy-rules](https://aur.archlinux.org/packages/cachyos-ananicy-rules/)^AUR^.

#### cgroups

See [cgroups](../en/Cgroups.html "Cgroups").

#### LimitCPU {#LimitCPU}

[LimitCPU](https://limitcpu.sourceforge.net/) is a program to limit the CPU usage percentage of a specific process. After installing [limitcpu](https://aur.archlinux.org/packages/limitcpu/)^AUR^, you may limit the CPU usage of a process\'s PID using a scale of 0 to 100 times the number of CPU cores that the computer has. For example, with eight CPU cores the percentage range will be 0 to 800. Usage:

    $ limitcpu -l 50 -p 5081

### irqbalance

The purpose of [irqbalance](https://archlinux.org/packages/?name=irqbalance) is to distribute hardware interrupts across processors on a multiprocessor system in order to increase performance. It can be [controlled](../en/Systemd.html#Using_units "Systemd") by the provided `irqbalance.service`.

**Warning** In some cases, irqbalance can interfere with power saving and can lead to stuttering or bad framerates in video games [\[2\]](https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/1833322/comments/4).

### Turn off CPU exploit mitigations {#Turn_off_CPU_exploit_mitigations}

**Warning** Do not apply this setting without considering the vulnerabilities it opens up. Among other things, if this option is enabled, you **must not rely on a virtual machine to isolate untrusted programs**. See [this](https://phoronix.com/scan.php?page=news_item&px=Linux-Improve-CPU-Spec-Switches) and [this](https://linuxreviews.org/HOWTO_make_Linux_run_blazing_fast_(again)_on_Intel_CPUs) for more information.

Turning off CPU exploit mitigations may improve performance. Use below [kernel parameter](../en/Kernel_parameter.html "Kernel parameter") to disable them all:

    mitigations=off

The explanations of all the switches it toggles are given at [kernel.org](https://docs.kernel.org/admin-guide/kernel-parameters.html). You can use [spectre-meltdown-checker](https://aur.archlinux.org/packages/spectre-meltdown-checker/)^AUR^ or [lscpu(1)](https://man.archlinux.org/man/lscpu.1) (from [util-linux](https://archlinux.org/packages/?name=util-linux)) for vulnerability check.

**Note** When using an Intel CPU from generation 10 and later, or AMD Ryzen series 1000 and later, the performance uplift from disabling mitigations is only up to 5% instead of the up to 25% for the previous CPU generations. See [the general review from early 2021](https://www.phoronix.com/scan.php?page=article&item=3-years-specmelt), [the test on Rocket Lake](https://www.phoronix.com/scan.php?page=article&item=spectre-rocket-lake) and [the test on Alder Lake](https://www.phoronix.com/scan.php?page=article&item=alder-lake-mitigations)

### Tuning compilation for your CPU {#Tuning_compilation_for_your_CPU}

Depending on your CPU, you may be able to gain a small performance boost by compiling software tuned for your native CPU [microarchitecture](https://en.wikipedia.org/wiki/Microarchitecture "wikipedia:Microarchitecture") with the flag `-march=native`, but any binaries you compile with this flag will be slow or broken on other CPU microarchitectures. If you use this option and want to switch or upgrade your CPU, you need to either recompile your binaries or choose a new CPU that uses the same microarchitecture as your old one. You can [apply this option by default for makepkg](../en/Makepkg.html#Optimization "Makepkg").

If you [compile your own kernel](../en/Kernel.html#Compilation "Kernel"), you can also enable this option during kernel compilation with the `CONFIG_X86_NATIVE_CPU` option. However, kernel improvements will be smaller as the kernel [forbids](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/arch/x86/Makefile#L77) extended vector instructions in generic code, which are responsible for the most of performance improvement in regular binaries, so most of the performance improvement will come from [much smaller micro-optimizations](https://github.com/gcc-mirror/gcc/blob/ffa98429b93934be87f58bc3af481a69310aedaf/gcc/config/i386/x86-tune-costs.h).

## Graphics {#Graphics}

### Xorg configuration {#Xorg_configuration}

Graphics performance may depend on the settings in [xorg.conf(5)](https://man.archlinux.org/man/xorg.conf.5); see the [NVIDIA](../en/NVIDIA.html "NVIDIA"), [AMDGPU](../en/AMDGPU.html "AMDGPU") and [Intel](../en/Intel_graphics.html "Intel") articles. Improper settings may stop Xorg from working, so caution is advised.

### Mesa configuration {#Mesa_configuration}

The performance of the Mesa drivers can be configured via [drirc](https://dri.freedesktop.org/wiki/ConfigurationInfrastructure/). [adriconf](https://archlinux.org/packages/?name=adriconf) (Advanced DRI Configurator) is a GUI tool to configure Mesa drivers by setting options and writing them to the standard drirc file.

### Hardware video acceleration {#Hardware_video_acceleration}

[Hardware video acceleration](../en/Hardware_video_acceleration.html "Hardware video acceleration") makes it possible for the video card to decode/encode video.

### Overclocking {#Overclocking_2}

As with CPUs, overclocking can directly improve performance, but is generally recommended against. There are several packages, such as [rovclock](https://aur.archlinux.org/packages/rovclock/)^AUR^ (ATI cards), [rocm-smi-lib](https://archlinux.org/packages/?name=rocm-smi-lib) (recent AMD cards), [nvclock](https://aur.archlinux.org/packages/nvclock/)^AUR^ (old NVIDIA - up to Geforce 9), and [nvidia-utils](https://archlinux.org/packages/?name=nvidia-utils) for recent NVIDIA cards.

See [AMDGPU#Overclocking](../en/AMDGPU.html#Overclocking "AMDGPU") or [NVIDIA/Tips and tricks#Enabling overclocking in nvidia-settings](../en/NVIDIA/Tips_and_tricks.html#Enabling_overclocking_in_nvidia-settings "NVIDIA/Tips and tricks").

### Enabling PCIe resizable BAR {#Enabling_PCIe_resizable_BAR}

**Note**

-   On some systems enabling PCIe resizable BAR can result in a significant loss of performance. Benchmark your system to make sure it increases performance. Note that on the newer Intel Arc dedicated GPUs, resizable BAR is officially recommended by Intel and will almost always improve performance.
-   The [Compatibility Support Module (CSM)](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#CSM_booting "wikipedia:Unified Extensible Firmware Interface") must be disabled for this to take effect.

The PCI specification allows larger [Base Address Registers](https://en.wikipedia.org/wiki/PCI_configuration_space#Standardized_registers "wikipedia:PCI configuration space") (BARs) to be used for exposing PCI devices memory to the PCI Controller. This can result in a performance increase for video cards. Having access to the full video memory improves performance, but also enables optimizations in the graphics driver. The combination of resizable BAR, above 4G decoding and these driver optimizations are what AMD calls [AMD Smart Access Memory](https://www.amd.com/en/gaming/technologies/smart-technologies.html), available at first on AMD Series 500 chipset motherboards, later expanded to AMD Series 400 and Intel Series 300 and later through UEFI updates. This setting may not be available on all motherboards, and is known to sometimes cause boot problems on certain boards.

If the BAR has a 256M size, the feature is not enabled or not supported:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# journalctl -k --grep=BAR=
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[drm] Detected VRAM RAM=8176M, BAR=256M
```

To enable it, enable the setting named \"Above 4G Decode\" or \"\>4GB MMIO\" in your motherboard settings. Verify that the BAR is now larger:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# journalctl -k --grep=BAR=
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
[drm] Detected VRAM RAM=8176M, BAR=8192M
```

**Note** For NVIDIA Blackwell (GeForce RTX 5000 series) GPUs, the [NVIDIA](../en/NVIDIA.html "NVIDIA") driver does not enable Resizable BAR automatically, even if it is enabled in firmware. In addition to enabling Above 4G Decoding and Resizable BAR in UEFI, the driver must be explicitly instructed to use it:

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
/etc/modprobe.d/nvidia-rebar.conf
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
options nvidia NVreg_EnableResizableBar=1
```

Then [regenerate the initramfs](../en/Regenerate_the_initramfs.html "Regenerate the initramfs") so the option is applied when the NVIDIA kernel module is loaded early during boot.

A full power cycle (shutdown and power off) may be required for PCIe BAR resizing to take effect.

Resizable BAR can be verified using `lspci -vv`, where the GPU BAR size should be larger than 256 MB (example shown is a NVIDIA model 4070Ti Super with 16GB of RAM):

``` {style="margin-bottom: 0; border-bottom:none; padding-bottom:0.8em;"}
# lspci -vv -d ::03xx | grep BAR
```

``` {style="margin-top: 0; border-top-style:dashed; padding-top: 0.8em;"}
Capabilities: [bb0 v1] Physical Resizable BAR
                BAR 0: current size: 16MB, supported: 16MB
                BAR 1: current size: 16GB, supported: 64MB 128MB 256MB 512MB 1GB 2GB 4GB 8GB 16GB
                BAR 3: current size: 32MB, supported: 32MB
```

## RAM, swap and OOM handling {#RAM,_swap_and_OOM_handling}

### Clock frequency and timings {#Clock_frequency_and_timings}

RAM can run at different clock frequencies and timings, which can be configured in the BIOS. Memory performance depends on both values. Selecting the highest preset presented by the BIOS usually improves the performance over the default setting. Note that increasing the frequency to values not supported by both motherboard and RAM vendor is overclocking, and similar risks and disadvantages apply, see [#Overclocking](#Overclocking).

### Root on RAM overlay {#Root_on_RAM_overlay}

**This article or section is out of date.**

**Reason:** The liveroot script appears to be unmaintained, but this approach should still work. (Discuss in [Talk:Improving performance#Section_5.2: liveroot hasn\'t been updated since 2016](../en/Talk:Improving_performance.html#Section_5.2:_liveroot_hasn't_been_updated_since_2016 "Talk:Improving performance"))

If running off a slow writing medium (USB, spinning HDDs) and storage requirements are low, the root may be run on a RAM overlay ontop of read only root (on disk). This can vastly improve performance at the cost of a limited writable space to root. See [liveroot](https://aur.archlinux.org/packages/liveroot/)^AUR^.

### Swap on zram or zswap {#Swap_on_zram_or_zswap}

Similar benefits (at similar costs) can be achieved using [zswap](../en/Zswap.html "Zswap") or [swap on zram](../en/Zram.html#Usage_as_swap "Zram"). The two are generally similar in intent although not operation:

-   zswap operates as a compressed RAM cache and neither requires (nor permits) extensive userspace configuration. It works in conjunction with a swap device by acting as its cache. Pages that would normally enter swap can enter zswap instead.
-   zram is a kernel module which can be used to create a compressed block device in RAM. This compressed block device can be used as a swap device, with no other swap device required to back it up. It comes with many options, including the possibility of using a backing device for holding cold pages.

Because both options involve the [swap](../en/Swap.html "Swap") subsystem, configuration that affects swap also affects these systems. For example, [swappiness](../en/Swap.html#Swappiness "Swappiness") determines whether the kernel should prioritize dropping file cache or moving pages to swap when memory pressure is high. Because zswap intercepts the action of moving pages to swap and zram acts as the swap, the option would also determine how often these two mechanisms are used.

### Using the graphics card\'s RAM {#Using_the_graphics_card's_RAM}

In the unlikely case that you have very little RAM and a surplus of video RAM, you can use the latter as swap. See [Swap on video RAM](../en/Swap_on_video_RAM.html "Swap on video RAM").

### Improving system responsiveness under low-memory conditions {#Improving_system_responsiveness_under_low-memory_conditions}

**This article or section needs expansion.**

**Reason:** The [systemd.service(5)](https://man.archlinux.org/man/systemd.service.5) watchdog settings should be mentioned and crosslinked, see also [Systemd#Notifying about failed services](../en/Systemd.html#Notifying_about_failed_services "Systemd")). (Discuss in [Talk:Improving performance](../en/Talk:Improving_performance.html))

On traditional GNU/Linux system, especially for graphical workstations, when allocated memory is overcommitted, the overall system\'s responsiveness may degrade to a nearly unusable state before either triggering the in-kernel out-of-memory (OOM)-killer or a sufficient amount of memory got free (which is unlikely to happen quickly when the system is unresponsive, as you can hardly close any memory-hungry applications which may continue to allocate more memory). The behaviour also depends on specific setups and conditions, returning to a normal responsive state may take from a few seconds to more than half an hour, which could be a pain to wait in serious scenario like during a conference presentation.

While the behaviour of the kernel as well as the userspace things under low-memory conditions may improve in the future as discussed on [kernel](https://lore.kernel.org/lkml/d9802b6a-949b-b327-c4a6-3dbca485ec20@gmx.com/T/) and [Fedora](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/XUZLHJ5O32OX24LG44R7UZ2TMN6NY47N/) mailing lists, users can use more feasible and effective options than hard-resetting the system or tuning the `vm.overcommit_*` [sysctl](../en/Sysctl.html "Sysctl") parameters:

-   Manually trigger the kernel OOM-killer with [Magic SysRq key](https://docs.kernel.org/admin-guide/sysrq.html), namely `Alt+SysRq+f`.
-   Use a userspace OOM daemon to tackle these automatically (or interactively).

**Warning** Triggering OOM killer to kill running applications may lose your unsaved works. It is up to you that either you are patient enough to wait in hope that applications will finally free the memory normally, or you want to bring back unresponsive system as soon as possible.

Sometimes a user may prefer OOM daemon to SysRq because with kernel OOM-killer you cannot prioritize the process to (or not) terminate. To list some OOM daemons:

-   **systemd-oomd** --- Provided by [systemd](../en/Systemd.html "Systemd") as `systemd-oomd.service` that uses cgroups-v2 and pressure stall information (PSI) to monitor and take action on processes before an OOM occurs in kernel space.

[https://github.com/systemd/systemd](https://github.com/systemd/systemd), [systemd-oomd(8)](https://man.archlinux.org/man/systemd-oomd.8) \|\| [systemd](https://archlinux.org/packages/?name=systemd)

-   **earlyoom** --- Simple userspace OOM-killer implementation written in C.

[https://github.com/rfjakob/earlyoom](https://github.com/rfjakob/earlyoom) \|\| [earlyoom](https://archlinux.org/packages/?name=earlyoom)

-   **oomd** --- OOM-killer implementation based on [PSI](https://lwn.net/Articles/759781/), requires Linux kernel version 4.20+. Configuration is in JSON and is quite complex. Confirmed to work in Facebook\'s production environment.

[https://github.com/facebookincubator/oomd](https://github.com/facebookincubator/oomd) \|\| [oomd](https://aur.archlinux.org/packages/oomd/)^AUR^

-   **nohang** --- Sophisticated OOM handler written in Python, with optional PSI support, more configurable than earlyoom.

[https://github.com/hakavlad/nohang](https://github.com/hakavlad/nohang) \|\| [nohang-git](https://aur.archlinux.org/packages/nohang-git/)^AUR^

-   **low-memory-monitor** --- GNOME developer\'s effort that aims to provide better communication to userspace applications to indicate the low memory state, besides that it could be configured to trigger the kernel OOM-killer. Based on PSI, requires Linux 5.2+.

[https://gitlab.freedesktop.org/hadess/low-memory-monitor/](https://gitlab.freedesktop.org/hadess/low-memory-monitor/) \|\| [low-memory-monitor-git](https://aur.archlinux.org/packages/low-memory-monitor-git/)^AUR^

-   **uresourced** --- A small daemon that enables cgroup based resource protection for the active graphical user session.

[https://gitlab.freedesktop.org/benzea/uresourced](https://gitlab.freedesktop.org/benzea/uresourced) \|\| [uresourced](https://aur.archlinux.org/packages/uresourced/)^AUR^

-   **bustd** --- Very lightweight userspace OOM-killer, useful for slower machines. Based on PSI, requires Linux 4.2+.

[https://github.com/vrmiguel/bustd](https://github.com/vrmiguel/bustd) \|\| [bustd](https://aur.archlinux.org/packages/bustd/)^AUR^

## See also {#See_also}

-   [Red Hat Performance Tuning Guide](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Performance_Tuning_Guide/index.html)
-   [Linux Performance Measurements using vmstat](https://www.thomas-krenn.com/en/wiki/Linux_Performance_Measurements_using_vmstat)
