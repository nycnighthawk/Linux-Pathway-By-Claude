---
{"title": "systemd.slice(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/systemd.slice.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.slice(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTOMATIC DEPENDENCIES](#AUTOMATIC_DEPENDENCIES) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD.SLICE(5)              systemd.slice              SYSTEMD.SLICE(5)

## [](#NAME)NAME

           systemd.slice - Slice unit configuration

## [](#SYNOPSIS)SYNOPSIS

           slice.slice

## [](#DESCRIPTION)DESCRIPTION

           A unit configuration file whose name ends in ".slice" encodes
           information about a slice unit. A slice unit is a concept for
           hierarchically managing resources of a group of processes. This
           management is performed by creating a node in the Linux Control
           Group (cgroup) tree. Units that manage processes (primarily scope
           and service units) may be assigned to a specific slice. For each
           slice, certain resource limits may be set that apply to all
           processes of all units contained in that slice. Slices are
           organized hierarchically in a tree. The name of the slice encodes
           the location in the tree. The name consists of a dash-separated
           series of names, which describes the path to the slice from the
           root slice. The root slice is named -.slice. Example:
           foo-bar.slice is a slice that is located within foo.slice, which
           in turn is located in the root slice -.slice.

           Note that slice units cannot be templated, nor is possible to add
           multiple names to a slice unit by creating additional symlinks to
           its unit file.

           By default, service and scope units are placed in system.slice,
           virtual machines and containers registered with
           systemd-machined(8) are found in machine.slice, and user sessions
           handled by systemd-logind(8) in user.slice. See systemd.special(7)
           for more information.

           See systemd.unit(5) for the common options of all unit
           configuration files. The common configuration items are configured
           in the generic [Unit] and [Install] sections. The slice specific
           configuration options are configured in the [Slice] section.
           Currently, only generic resource control settings as described in
           systemd.resource-control(5) are allowed.

           See the New Control Group Interfaces[1] for an introduction on how
           to make use of slice units from programs.

## [](#AUTOMATIC_DEPENDENCIES)AUTOMATIC DEPENDENCIES

       Implicit Dependencies
           The following dependencies are implicitly added:

           •   Slice units automatically gain dependencies of type After= and
               Requires= on their immediate parent slice unit.

       Default Dependencies
           The following dependencies are added unless DefaultDependencies=no
           is set:

           •   Slice units will automatically have dependencies of type
               Conflicts= and Before= on shutdown.target. These ensure that
               slice units are removed prior to system shutdown. Only slice
               units involved with late system shutdown should disable
               DefaultDependencies= option.

## [](#OPTIONS)OPTIONS

           Slice unit files may include [Unit] and [Install] sections, which
           are described in systemd.unit(5).

           Slice files may include a [Slice] section. Many options that may
           be used in this section are shared with other unit types. These
           options are documented in systemd.resource-control(5).

           The options specific to the [Slice] section of slice units are the
           following:

           ConcurrencyHardMax=, ConcurrencySoftMax=
               Configures a hard and a soft limit on the maximum number of
               units assigned to this slice (or any descendent slices) that
               may be active at the same time. If the hard limit is reached
               no further units associated with the slice may be activated,
               and their activation will fail with an error. If the soft
               limit is reached any further requested activation of units
               will be queued, but no immediate error is generated. The
               queued activation job will remain queued until the number of
               concurrent active units within the slice is below the limit
               again.

               If the special value "infinity" is specified, no concurrency
               limit is enforced. This is the default.

               Note that if multiple start jobs are queued for units, and all
               their dependencies are fulfilled they'll be processed in an
               order that is dependent on the unit type, the CPU weight (for
               unit types that know the concept, such as services), the nice
               level (similar), and finally in alphabetical order by the unit
               name. This may be used to influence dispatching order when
               using ConcurrencySoftMax= to pace concurrency within a slice
               unit.

               Note that these options have a hierarchial effect: a limit set
               for a slice unit will apply to both the units immediately
               within the slice, but also all units further down the slice
               tree. Also note that each sub-slice unit counts as one unit
               each too, and thus when choosing a limit for a slice hierarchy
               the limit must provide room for both the payload units (i.e.
               services, mounts, ...) and structural units (i.e. slice
               units), if any are defined.

               Added in version 258.

           ActivatingConcurrencyMax=
               Configures a limit on the maximum number of units assigned to
               this slice (or any descendent slices) that may be in the
               activating state at the same time. Unlike ConcurrencySoftMax=
               which limits units in the active state, this option limits
               units while they are starting up. Once a unit leaves the
               activating state (whether to active, failed, or any other
               state), it no longer counts toward this limit, allowing the
               next queued unit to begin starting.

               This is particularly useful for managing the "thundering herd"
               problem during system boot, where many long-running services
               (such as container workloads) attempt to start simultaneously.
               By setting ActivatingConcurrencyMax=, you can pace the startup
               process to limit CPU and I/O pressure, while still allowing
               all services to eventually reach the active state.

               When the limit is reached, further activation requests are
               queued and will be dispatched automatically once running
               activations complete. No error is returned to the caller. Note
               that if a unit becomes stuck in the activating state (for
               example, due to a hung process or missing dependency), it will
               continue to occupy a slot until it leaves that state.
               Configure appropriate timeouts (e.g., TimeoutStartSec=) on
               individual units to prevent indefinite blocking.

               Setting ActivatingConcurrencyMax=0 blocks all activation
               requests in the slice hierarchy indefinitely. Queued units
               will never start until the limit is raised. This can be used
               to intentionally freeze slice startup, matching the behavior
               of ConcurrencySoftMax=0.

               If the special value "infinity" is specified, no concurrency
               limit is enforced. This is the default.

               Note that this option has a hierarchical effect: a limit set
               for a slice unit will apply to both the units immediately
               within the slice and all units further down the slice tree.
               Note that slice units themselves never enter the activating
               state, so nested slices do not count toward the limit.

               Added in version 262.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.unit(5), systemd.resource-control(5),
           systemd.service(5), systemd.scope(5), systemd.special(7),
           systemd.directives(7)

## [](#NOTES)NOTES

            1. New Control Group Interfaces
               https://systemd.io/CONTROL_GROUP_INTERFACE

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

    systemd 262~devel                                        SYSTEMD.SLICE(5)

------------------------------------------------------------------------

Pages that refer to this page: [journalctl(1)](../man1/journalctl.1.html),  [systemd(1)](../man1/systemd.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [systemd-run(1)](../man1/systemd-run.1.html),  [sd_bus_creds_get_pid(3)](../man3/sd_bus_creds_get_pid.3.html),  [sd_pid_get_owner_uid(3)](../man3/sd_pid_get_owner_uid.3.html),  [capsule@.service(5)](../man5/capsule@.service.5.html),  [systemd.resource-control(5)](../man5/systemd.resource-control.5.html),  [systemd.service(5)](../man5/systemd.service.5.html),  [systemd.unit(5)](../man5/systemd.unit.5.html),  [user@.service(5)](../man5/user@.service.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html),  [systemd.syntax(7)](../man7/systemd.syntax.7.html),  [pam_systemd(8)](../man8/pam_systemd.8.html)

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
