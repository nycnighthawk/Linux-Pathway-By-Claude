---
{"title": "numactl(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/numactl.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# numactl(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [NOTES](#NOTES) \| [FILES](#FILES) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NUMACTL(8)             Linux Administrator's Manual            NUMACTL(8)

## [](#NAME)NAME

           numactl - Control NUMA policy for processes or shared memory

## [](#SYNOPSIS)SYNOPSIS

           numactl [ --all ] [ --balancing ] [ --interleave nodes ] [
           --weighted-interleave nodes ] [ --preferred node ] [ --preferred-
           many nodes ] [ --membind nodes ] [ --cpunodebind nodes ] [
           --physcpubind cpus ] [ --localalloc ] [--] command {arguments ...}
           numactl --show
           numactl --hardware [--cpu-compress]
           numactl --version
           numactl [ --huge ] [ --offset offset ] [ --shmmode shmmode ] [
           --length length ] [ --strict ]
           [ --shmid id ] --shm shmkeyfile | --file tmpfsfile
           [ --touch ] [ --dump ] [ --dump-nodes ] memory policy

## [](#DESCRIPTION)DESCRIPTION

           numactl runs processes with a specific NUMA scheduling or memory
           placement policy.  The policy is set for command and inherited by
           all of its children.  In addition it can set persistent policy for
           shared memory segments or files.

           Use -- before command if using command options that could be
           confused with numactl options.

           nodes may be specified as N,N,N or  N-N or N,N-N or  N-N,N-N and
           so forth.  Relative nodes may be specified as +N,N,N or  +N-N or
           +N,N-N and so forth. The + indicates that the node numbers are
           relative to the process' set of allowed nodes in its current
           cpuset.  A !N-N notation indicates the inverse of N-N, in other
           words all nodes except N-N.  If used with + notation, specify !+N-
           N. When same is specified the previous nodemask specified on the
           command line is used.  all means all nodes in the current cpuset.

           Instead of a number a node can also be:
           netdev:DEV                 The node connected to network device DEV.
           file:PATH                  The node the block device of PATH.
           ip:HOST                    The node of the network device of HOST
           block:PATH                 The node of block device PATH
           pci:[seg:]bus:dev[:func]   The node of a PCI device.

           Note that block resolves the kernel block device names only for
           udev names in /dev use file:

           Policy settings are:

           --all, -a
                  Unset default cpuset awareness, so user can use all
                  possible CPUs/nodes for following policy settings.

           --interleave=nodes, -i nodes
                  Set a memory interleave policy. Memory will be allocated
                  using round robin on nodes.  When memory cannot be
                  allocated on the current interleave target fall back to
                  other nodes.  Multiple nodes may be specified on
                  --interleave, --membind and --cpunodebind.

           --weighted-interleave=nodes, -w nodes
                  Set a weighted memory interleave policy. Memory will be
                  allocated using the weighted ratio for each node, which can
                  be read from
                  /sys/kernel/mm/mempolicy/weighted_interleave/node*.  When
                  memory cannot be allocated on the current interleave target
                  fall back to other nodes.

           --membind=nodes, -m nodes
                  Only allocate memory from nodes.  Allocation will fail when
                  there is not enough memory available on these nodes.  nodes
                  may be specified as noted above.

           --cpunodebind=nodes, -N nodes
                  Only execute command on the CPUs of nodes.  Note that nodes
                  may consist of multiple CPUs.  nodes may be specified as
                  noted above.

           --physcpubind=cpus, -C cpus
                  Only execute process on cpus.  This accepts cpu numbers as
                  shown in the processor fields of /proc/cpuinfo, or relative
                  cpus as in relative to the current cpuset.  You may specify
                  "all", which means all cpus in the current cpuset.
                  Physical cpus may be specified as N,N,N or  N-N or N,N-N or
                  N-N,N-N and so forth.  Relative cpus may be specified as
                  +N,N,N or  +N-N or +N,N-N and so forth. The + indicates
                  that the cpu numbers are relative to the process' set of
                  allowed cpus in its current cpuset.  A !N-N notation
                  indicates the inverse of N-N, in other words all cpus
                  except N-N.  If used with + notation, specify !+N-N.

           --localalloc, -l
                  Try to allocate on the current node of the process, but if
                  memory cannot be allocated there fall back to other nodes.

           --preferred=node, -p node
                  Preferably allocate memory on node, but if memory cannot be
                  allocated there fall back to other nodes.  This option
                  takes only a single node number.  Relative notation may be
                  used.

           --balancing, -b
                  Enable Linux kernel NUMA balancing for the process if it is
                  supported by kernel.  This should only be used with
                  --membind, -m only, otherwise ignored.

           --preferred-many=nodes, -P nodes
                  Preferably allocate memory on nodes, but if memory cannot
                  be allocated there fall back to other nodes.  This option
                  takes a mask of preferred nodes where the closest node to
                  local is considered most preferred.  Relative notation may
                  be used.

           --show, -s
                  Show NUMA policy settings of the current process.

           --hardware, -H
                  Show inventory of available nodes on the system. When the
                  --cpu-compress option is set show cpu ranges. This is not
                  default not break any existing scripts.

           Numactl can set up policy for a SYSV shared memory segment or a
           file in shmfs/hugetlbfs.

           --version
           print the version of the numactl package and exit.

           The following policy settings are persistent and will be used by
           all mappings from that shared memory. The order of options matters
           here.  The specification must at least include either of --shm,
           --shmid, --file to specify the shared memory segment or file and a
           memory policy like described above ( --interleave, --localalloc,
           --preferred, --preferred-many, --membind ).

           --huge
           When creating a SYSV shared memory segment use huge pages.  Only
           valid before --shmid or --shm

           --offset
           Specify offset into the shared memory segment. Default 0.  Valid
           units are m (for MB), g (for GB), k (for KB), otherwise it
           specifies bytes.

           --strict
           Give an error when a page in the policied area in the shared
           memory segment already was faulted in with a conflicting policy.
           Default is to silently ignore this.

           --shmmode shmmode
           Only valid before --shmid or --shm When creating a shared memory
           segment set it to numeric mode shmmode.

           --length length
           Apply policy to length range in the shared memory segment or make
           the segment length long Default is to use the remaining length
           Required when a shared memory segment is created and specifies the
           length of the new segment then. Valid units are m (for MB), g (for
           GB), k (for KB), otherwise it specifies bytes.

           --shmid id
           Create or use a shared memory segment with numeric ID id

           --shm shmkeyfile
           Create or use a shared memory segment, with the ID generated using
           ftok(3) from shmkeyfile

           --file tmpfsfile
           Set policy for a file in tmpfs or hugetlbfs

           --touch
           Touch pages to enforce policy early. Default is to not touch them,
           the policy is applied when an applications maps and accesses a
           page.

           --dump
           Dump policy in the specified range.

           --dump-nodes
           Dump all nodes of the specific range (very verbose!)

           Valid node specifiers
           all                 All nodes
           number              Node number
           number1{,number2}   Node number1 and Node number2
           number1-number2     Nodes from number1 to number2
           ! nodes             Invert selection of the following specification.

## [](#EXAMPLES)EXAMPLES

           numactl --physcpubind=+0-4,8-12 myapplic arguments Run myapplic on
           cpus 0-4 and 8-12 of the current cpuset.

           numactl --interleave=all bigdatabase arguments Run big database
           with its memory interleaved on all CPUs.

           numactl --weighted-interleave=all bigdatabase arguments Run big
           database with its memory interleaved with weighted ratio on all
           CPUs.

           numactl --cpunodebind=0 --membind=0,1 process Run process on node
           0 with memory allocated on node 0 and 1.

           numactl --cpunodebind=0 --membind=0,1 -- process -l Run process as
           above, but with an option (-l) that would be confused with a
           numactl option.

           numactl --cpunodebind=0 --balancing --membind=0,1 process Run
           process on node 0 with memory allocated on node 0 and 1.  Optimize
           the page placement with Linux kernel NUMA balancing mechanism if
           possible.

           numactl --cpunodebind=netdev:eth0 --membind=netdev:eth0 network-
           server Run network-server on the node of network device eth0 with
           its memory also in the same node.

           numactl --preferred=1 numactl --show Set preferred node 1 and show
           the resulting state.

           numactl --preferred-many=0x3 numactl --show Set preferred nodes 1
           and 2, and show the resulting state.

           numactl --length 1g --shm /tmp/shmkey --interleave=all Interleave
           all of the sysv shared memory region of size 1g specified by
           /tmp/shmkey over all nodes.

           Place a tmpfs file on 2 nodes:
             numactl --membind=2 dd if=/dev/zero of=/dev/shm/A bs=1M
           count=1024
             numactl --membind=3 dd if=/dev/zero of=/dev/shm/A seek=1024
           bs=1M count=1024

           numactl --localalloc /dev/shm/file Reset the policy for the shared
           memory file file to the default localalloc policy.

## [](#NOTES)NOTES

           Requires a NUMA policy aware kernel.

           Command is not executed using a shell. If you want to use shell
           metacharacters in the child use sh -c as wrapper.

           Setting policy for a hugetlbfs file does currently not work
           because it cannot be extended by truncate.

           Shared memory segments larger than numactl's address space cannot
           be completely policied. This could be a problem on 32bit
           architectures.  Changing it piece by piece may work.

           The old --cpubind which accepts node numbers, not cpu numbers, is
           deprecated and replaced with the new --cpunodebind and
           --physcpubind options.

## [](#FILES)FILES

           /proc/cpuinfo for the listing of active CPUs. See proc(5) for
           details.

           /sys/devices/system/node/node*/numastat for NUMA memory hit
           statistics.

## [](#COPYRIGHT)COPYRIGHT

           Copyright 2002,2004 Andi Kleen, SuSE Labs.  numactl and the demo
           programs are under the GNU General Public License, v.2

## [](#SEE_ALSO)SEE ALSO

           set_mempolicy(2) , get_mempolicy(2) , mbind(2) ,
           sched_setaffinity(2) , sched_getaffinity(2) , proc(5) , ftok(3) ,
           shmat(2) , migratepages(8)

## [](#COLOPHON)COLOPHON

           This page is part of the numactl (NUMA commands) project.
           Information about the project can be found at 
           ⟨http://oss.sgi.com/projects/libnuma/⟩.  If you have a bug report
           for this manual page, send it to linux-numa@vger.kernel.org.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/numactl/numactl.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    SuSE Labs                        Mar 2004                      NUMACTL(8)

------------------------------------------------------------------------

Pages that refer to this page: [get_mempolicy(2)](../man2/get_mempolicy.2.html),  [mbind(2)](../man2/mbind.2.html),  [sched_setaffinity(2)](../man2/sched_setaffinity.2.html),  [set_mempolicy(2)](../man2/set_mempolicy.2.html),  [numa(3)](../man3/numa.3.html),  [cpuset(7)](../man7/cpuset.7.html),  [numa(7)](../man7/numa.7.html),  [migratepages(8)](../man8/migratepages.8.html),  [migspeed(8)](../man8/migspeed.8.html),  [numastat(8)](../man8/numastat.8.html)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
