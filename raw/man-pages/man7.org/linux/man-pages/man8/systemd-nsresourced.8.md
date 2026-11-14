---
{"title": "systemd-nsresourced.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-nsresourced.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-nsresourced.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8) systemd-nsresourced.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-nsresourced.service, systemd-nsresourced - User Namespace
           Resource Delegation Service

## [](#SYNOPSIS)SYNOPSIS

           systemd-nsresourced.service

           /usr/lib/systemd/systemd-nsresourced

## [](#DESCRIPTION)DESCRIPTION

           systemd-nsresourced is a system service that permits transient
           delegation of a UID/GID range to a user namespace (see
           user_namespaces(7)) allocated by a client, via a Varlink IPC API.

           Unprivileged clients may allocate a user namespace, and then
           request a UID/GID range to be assigned to it via this service. The
           user namespace may then be used to run containers and other
           sandboxes, and/or apply it to an id-mapped mount.

           Allocations of UIDs/GIDs this way are transient: when a user
           namespace goes away, its UID/GID range is returned to the pool of
           available ranges. In order to ensure that clients cannot gain
           persistency in their transient UID/GID range a BPF-LSM based
           policy is enforced that ensures that user namespaces set up this
           way can only write to file systems they allocate themselves or
           that are explicitly allowlisted via systemd-nsresourced.

           systemd-nsresourced automatically ensures that any registered UID
           ranges show up in the system's NSS database via the User/Group
           Record Lookup API via Varlink[1].

           Currently, only UID/GID ranges consisting of either exactly 1 or
           exactly 65536 UIDs/GIDs can be registered with this service.
           Moreover, UIDs and GIDs are always allocated together, and
           symmetrically.

           The allocation API supports delegated ranges: additional UID/GID
           ranges that are mapped 1:1 into the user namespace rather than
           being translated to a target UID/GID. These delegated ranges
           enable nested user namespace scenarios where a container needs to
           create child user namespaces with their own transient UID ranges.
           Normally, the kernel restricts which UIDs can be mapped into a
           user namespace to those that are also mapped in the parent.
           Delegated ranges solve this by pre-allocating additional ranges
           that are visible inside the user namespace and can be used by
           nested AllocateUserRange() calls. Up to 16 delegated ranges can be
           requested per user namespace, each of size 65536. The ranges are
           allocated from the container UID ranges as per Users, Groups, UIDs
           and GIDs on systemd Systems[2].

           The allocation API also supports identity mappings: instead of
           allocating a transient UID/GID range, the user namespace can be
           configured to map the caller's UID/GID to root (UID 0) inside the
           namespace, or to itself. Identity mappings can be combined with
           delegated ranges to enter a privileged user namespace from which
           the container can be set up after which the container can run in
           one of the delegated ranges. Identity mapped users are not subject
           to BPF-LSM write restrictions unlike the transient ranges.

           Additionally, the allocation API supports mapping the foreign UID
           range into the user namespace. When this option is enabled, the
           foreign UID range is mapped 1:1 into the user namespace, allowing
           processes inside to access and manipulate files owned by the
           foreign UID range.

           The service provides API calls to allowlist mounts (referenced via
           their mount file descriptors as per Linux fsmount() API), to pass
           ownership of a cgroup subtree to the user namespace and to
           delegate a virtual Ethernet device pair to the user namespace.
           When used in combination this is sufficient to implement fully
           unprivileged container environments, as implemented by
           systemd-nspawn(1), fully unprivileged RootImage= (see
           systemd.exec(5)) or fully unprivileged disk image tools such as
           systemd-dissect(1).

           This service provides one Varlink[3] service:
           io.systemd.NamespaceResource allows registering user namespaces,
           and assign mounts, cgroups and network interfaces to it.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-mountfsd.service(8), systemd-nspawn(1),
           systemd.exec(5), systemd-dissect(1), user_namespaces(7)

## [](#NOTES)NOTES

            1. User/Group Record Lookup API via Varlink
               https://systemd.io/USER_GROUP_API

            2. Users, Groups, UIDs and GIDs on systemd Systems
               https://systemd.io/UIDS-GIDS

            3. Varlink
               https://varlink.org/

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                  SYSTEMD-....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [systemd.nspawn(5)](../man5/systemd.nspawn.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-mountfsd.service(8)](../man8/systemd-mountfsd.service.8.html)

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
