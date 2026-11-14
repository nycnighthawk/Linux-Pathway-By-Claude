---
{"title": "netcap(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/netcap.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# netcap(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ADVANCED MODE](#ADVANCED_MODE) \| [JSON OUTPUT](#JSON_OUTPUT) \| [INTERPRETATION](#INTERPRETATION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NETCAP:(8)           System Administration Utilities           NETCAP:(8)

## [](#NAME)NAME

           netcap - a program to review network capability posture

## [](#SYNOPSIS)SYNOPSIS

           netcap [--advanced [--interface IFACE ] [--list-interfaces]
           [--json] [--no-color]]

## [](#DESCRIPTION)DESCRIPTION

           netcap is a program that prints out a report of process
           capabilities.  By default, it runs in its historical filtered
           mode: if an application is using tcp, udp, raw, or packet family
           sockets AND has any capabilities, it will be in the report. If the
           process has partial capabilities, it is further examined to see if
           it has an open-ended bounding set. If this is found to be true, a
           '+' symbol is added. If the process has ambient capabilities, a
           '@' symbol is added.  Bluetooth sockets are not discovered in this
           historical filtered mode; use --advanced when Bluetooth listener
           discovery is needed.

           With --advanced, netcap switches to bind/listener inventory mode
           for the current network namespace. In this mode, reachable
           binds/listeners are reported regardless of whether the owning
           process has capabilities, including Bluetooth listeners that are
           not visible in classic mode.

           Some directories in the /proc file system are readonly by root.
           The program will try to access and report what it can.  Full
           output normally requires root, or a combination of
           CAP_DAC_READ_SEARCH (to read other processes' /proc/<pid>/fd) and
           CAP_NET_ADMIN (for NETLINK_SOCK_DIAG queries that cover SCTP,
           DCCP, and, when built with VSOCK support, VSOCK). Without these
           permissions, the report is partial; missing sock_diag-derived
           protocols are omitted without an explicit warning.

## [](#OPTIONS)OPTIONS

           --advanced
                  Enable the posture/tree view. This mode inventories
                  reachable binds in the current network namespace and shows
                  per-process capabilities, defenses, and flags.

           --interface IFACE
                  With --advanced, limit the report to the named interface.
                  Output format and wrapping are unchanged; only interface-
                  scoped rows for that interface are kept. This also filters
                  --list-interfaces output to the named interface.

           --list-interfaces
                  With --advanced, list the current network namespace
                  interface names instead of the exposure tree.

           --json With --advanced, emit machine-readable JSON instead of the
                  tree view. When combined with --list-interfaces, emit
                  machine-readable interface inventory JSON instead of text.

           --no-color
                  Suppress colored output. By default, when stdout is a
                  terminal, keywords are colorized by severity to highlight
                  problems, cautions, and positive hardening state.

## [](#ADVANCED_MODE)ADVANCED MODE

           Advanced mode is an attack-surface and posture inventory for the
           current network namespace. It is intended for administrators who
           need a structured view of bind ownership and process hardening
           state.

           With --advanced --list-interfaces, the advanced-mode interface
           snapshot is rendered directly without enumerating listeners. This
           is intended as a simple interface enumeration step before later
           per-interface analysis.  With --advanced --interface IFACE, the
           same inventory and tree/JSON renderers are used, but only
           endpoints projected onto that interface are retained.

           The tree layout is:

                  Planes -> interface -> protocol -> bind -> port -> process
                  -> caps/defenses/flags

           For VSOCK, the interface/address hierarchy is skipped and rendered
           as:

                  Planes -> endpoint -> process -> caps/defenses/flags

           For BLUETOOTH, the interface is the HCI adapter (for example
           hci0).  Bluetooth bind nodes are the local controller address or *
           for wildcard binds.

           Planes are grouped as INET (external), INET (loopback), BLUETOOTH,
           VSOCK, and LINK-LAYER. These names match the tree output exactly.

           The console tree is a causal exposure chain: protocol, then bind
           address, then port, then owning process. Wildcard binds are
           printed as *. In tree view, a single 0.0.0.0 or :: listener is
           expanded onto every non-loopback interface in the current
           namespace. The same daemon may therefore appear under multiple
           interfaces, reflecting wildcard-bind reachability.  Some endpoints
           may appear under interface multicast/group when bound to multicast
           addresses that do not map to a single interface; these represent
           group-joined sockets rather than point-to-point listeners.

           Under each protocol, bind nodes are socket bind addresses
           (exposure), and port nodes are children of binds.  Each process
           entry may include a unit field showing the systemd service or
           scope name, extracted from the process cgroup hierarchy; it is
           omitted when the process is not managed by systemd.  Each process
           line also includes an optional exe field showing the full
           executable path read from /proc/<pid>/exe; it is omitted for
           kernel threads or when the path is unreadable. The kernel Name:
           field shown as comm is truncated to 15 characters, so exe provides
           the complete binary path.

           Socket selection is protocol-specific:

           • TCP: LISTEN sockets only.

           • UDP/UDPLITE: bound sockets.

           • RFCOMM: all owned RFCOMM sockets (state and channel are not
             exposed by the kernel's proc interface).

           • HCI: all bound raw management sockets; semantics differ from
             port listeners and are analogous to packet sockets.

           • SCTP/DCCP: listener sockets only; established flows are not
             shown.  These protocols are discovered via NETLINK_SOCK_DIAG,
             which requires CAP_NET_ADMIN; without that capability, SCTP and
             DCCP listeners are silently absent from the report.

           • VSOCK: when built with linux/vm_sockets.h, stream LISTEN
             sockets, plus bound datagram/seqpacket sockets.

           • RAW/PACKET: shown as binds; semantics differ from port
             listeners.

             The defenses section is best-effort: no_new_privs and seccomp
             mode are read from /proc/<pid>/status when available, and the
             LSM label is read from /proc/<pid>/attr/current when available.
             runs_as_nonroot is always reported.

             Flags annotate notable conditions:

           • wildcard-bind: bind is bound to a wildcard address (for example
             0.0.0.0 or ::).

           • hypervisor-plane: bind is in the VSOCK communication plane.

           • proximity-plane: bind is reachable by any Bluetooth device
             within radio range.

           • ssh-on-vsock-port-22: VSOCK bind uses port 22.

           • privileged-caps: process has capabilities considered privileged
             for attack-surface review (CAP_SYS_ADMIN, CAP_SYS_PTRACE,
             CAP_DAC_READ_SEARCH, CAP_NET_ADMIN, and CAP_NET_RAW).

             The caps field may include bracketed annotations: [ambient-
             present] indicates ambient capabilities are set, and [open-
             ended-bounding] indicates the bounding set is non-empty (the
             process or its children can potentially gain additional
             capabilities).

## [](#JSON_OUTPUT)JSON OUTPUT

           When --advanced --json is used, the top-level object contains:

           • schema_version (integer).

           • planes (array).

             Each plane object contains name, optional scope (external or
             loopback), and either:

           • ifaces (INET/LINK-LAYER/BLUETOOTH planes), or

           • endpoints (VSOCK plane).

             Under ifaces: each interface has name and addrs (array). Each
             addr object has addr and endpoints (array).

             For INET, LINK-LAYER, and BLUETOOTH planes, each endpoint object
             has label, proto, bind, port, and processes (array). For
             BLUETOOTH planes, interface names are HCI adapter names (for
             example hci0); port is 0 for HCI sockets and for RFCOMM sockets
             whose channel is not exposed by procfs.  For VSOCK planes,
             endpoint objects use label, vsock_type (socket type string:
             stream/dgram/seqpacket), cid (source CID or the string ANY),
             port, and processes; they do not include proto or bind.  When
             built without linux/vm_sockets.h, the VSOCK plane and VSOCK
             flags are omitted.

             Each process object has comm, optional exe, pid, uid, optional
             unit, caps, ambient_present (boolean), open_ended_bounding
             (boolean), defenses object, and flags array.

             ambient_present and open_ended_bounding are the structured
             equivalents of the [ambient-present] and [open-ended-bounding]
             annotations that may appear in the caps text string; both fields
             are always present in JSON output.

             Fields under endpoints/processes/defenses may be omitted when
             unavailable.  When process defenses are present, they include
             runs_as_nonroot, derived from the real UID (first field of Uid:
             in /proc/<pid>/status): yes when real uid != 0, no when real uid
             == 0. A process that started as root and later changed only
             effective UID via setuid still reports no.

             If a plane has no discovered binds, it appears with an empty
             list. If a consumer does not receive a given plane, treat it as
             none found or omitted by the producer.

             When --advanced --list-interfaces --json is used, the top-level
             object contains schema_version (integer) and interfaces (array
             of interface-name strings).

## [](#INTERPRETATION)INTERPRETATION

           netcap reports processes that are both network-facing and running
           with capabilities. The capability set shown is the permitted set.
           A '+' annotation means the process has an open-ended bounding set,
           and an '@' annotation means the process has ambient capabilities.

           Colorized tree output is intended to prioritize remediation
           quickly: orange highlights problems to fix, yellow highlights
           cautionary conditions to review, green highlights good hardening
           state, and uncolored output is neutral context.

           The caps line shows permitted capabilities. Orange-tier
           capabilities represent severe privilege that is rarely necessary
           for network-facing daemons: sys_ptrace, sys_module, sys_rawio,
           setuid, setgid, setpcap, and audit_control. Yellow-tier
           capabilities are common but still materially increase attack
           impact: sys_admin, dac_override, dac_read_search, net_admin,
           net_raw, chown, fowner, mknod, and sys_chroot. caps: (full) means
           all capabilities are present (effectively full root privilege).
           caps: (none) is ideal.

           Ambient capabilities are inherited across execve by child
           processes (unless constrained by no_new_privs), so their presence
           on a network daemon is typically a problem. The ambient: line
           lists active ambient capabilities.

           [open-ended-bounding] means the process has not trimmed its
           bounding set ceiling. This is not active privilege by itself, but
           it leaves future privilege-acquisition paths open (for example via
           file capabilities or ambient inheritance). For libcap-ng users,
           trimming is typically a one-flag change (CAPNG_SELECT_BOUNDS) in
           existing capability-set calls; with libcap, bounding capabilities
           are dropped individually.

           Defense fields summarize exploit-resistance posture: no_new_privs:
           yes blocks privilege gain through setuid/file-capability exec
           paths and is often the highest-value single toggle. seccomp:
           filter restricts available syscalls (disabled means no syscall
           filtering). runs_as_nonroot: yes indicates non-UID-0 execution.

           Flags provide reachability and interception context: wildcard-bind
           means the daemon listens on every interface, hypervisor-plane
           indicates host/ guest boundary exposure (VSOCK), proximity-plane
           indicates that the bind is reachable by Bluetooth devices within
           radio range, and reuseport means another process with the same UID
           could bind and potentially intercept traffic.

           raw/raw6 and packet protocol nodes denote sockets with IP- or
           link-layer packet craft/sniff capabilities, significantly
           expanding what an attacker can do post-compromise.  Bluetooth
           protocol nodes denote proximity-based attack surface. hci nodes
           provide raw controller management access and are shown in yellow.
           rfcomm sockets are reachable by nearby devices without prior host
           access and, unless the adapter is configured to require pairing,
           may be reachable without authentication. Adapter BD_ADDR
           resolution requires HCI ioctl access; without it, adapter identity
           is shown as hci?/*.

## [](#SEE_ALSO)SEE ALSO

           pscap(8), filecap(8), capabilities(7), netstat(8).

## [](#AUTHOR)AUTHOR

           Steve Grubb

## [](#COLOPHON)COLOPHON

           This page is part of the libcap-ng (capabilities commands and
           library (NG)) project.  Information about the project can be found
           at ⟨https://people.redhat.com/sgrubb/libcap-ng/⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           tarball fetched from
           ⟨https://people.redhat.com/sgrubb/libcap-ng/index.html⟩ on
           2026-08-04.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Red Hat                         March 2026                     NETCAP:(8)

------------------------------------------------------------------------

Pages that refer to this page: [capabilities(7)](../man7/capabilities.7.html),  [filecap(8)](../man8/filecap.8.html),  [pscap(8)](../man8/pscap.8.html)

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
