---
{"title": "systemd-imds-generator(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-imds-generator.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-imds-generator(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [KERNEL COMMAND LINE](#KERNEL_COMMAND_LINE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                        |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-IMDS-GENERATOR(8) systemd-imds-generatorSYSTEMD-IMDS-GENERATOR(8)

## [](#NAME)NAME

           systemd-imds-generator - Generator to automatically enable IMDS on
           supporting environments

## [](#SYNOPSIS)SYNOPSIS

           /usr/lib/systemd/system-generators/systemd-imds-generator

## [](#DESCRIPTION)DESCRIPTION

           systemd-imds-generator is a generator that enables IMDS (Instance
           Metadata Service) functionality at boot on systems that support
           it. Specifically it does three things:

           •   It pulls the systemd-imdsd.socket unit (which activates
               systemd-imdsd@.service(8)) into the initial transaction, which
               provides IMDS access to local applications via Varlink IPC.

           •   It pulls the systemd-imds-early-network.service unit into the
               initial transaction, which generates a suitable
               systemd.network(5) network configuration file that allows
               early-boot network access to the IMDS functionality.

           •   It pulls the systemd-imds-import.service unit into the initial
               transaction, which automatically imports various credentials
               from IMDS into the local system, storing them in
               /run/credstore/.

           By default, whether to pull in these services or not is decided
           based on hwdb(7) information, that detects various IMDS
           environments automatically. However, this logic may be overridden
           via systemd.imds=, see below.

           systemd-imds-generator implements systemd.generator(7).

## [](#KERNEL_COMMAND_LINE)KERNEL COMMAND LINE

           systemd-imds-generator understands the following kernel command
           line parameters:

           systemd.imds=
               Takes a boolean argument or the special value "auto", and may
               be used to enable or disable the IMDS logic. Note that this
               controls only whether the relevant services (as listed above)
               are automatically pulled into the initial transaction, it has
               no effect if some other unit or the user explicitly activates
               the relevant units. If this option is not used (or set to
               "auto") automatic detection of IMDS is used, see above.

               Added in version 261.

           systemd.imds.network=
               Takes one of "off", "locked", "unlocked". Controls whether and
               how to set up networking for IMDS endpoint access. Unless set
               to "off" early boot networking is enabled, ensuring that the
               IMDS endpoint can be reached. If set to "locked" direct access
               to the IMDS endpoint by regular unprivileged processes is
               disabled via a "prohibit" route, so that any access must be
               done through systemd-imdsd@.service or its associated tools.
               If set to "unlocked" (the default) this "prohibit" route is
               not created, and regular unprivileged processes can directly
               contact IMDS.

               Added in version 261.

           systemd.imds.import=
               Takes a boolean argument. If false the
               systemd-imds-import.service (see above) is not pulled into the
               initial transaction, i.e. no credentials are imported from
               IMDS. Defaults to true in the initrd, and false otherwise.

               Added in version 261.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-imds(1), systemd-imdsd@.service(8),
           systemd.system-credentials(7)

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

    systemd 262~devel                               SYSTEMD-IMDS-GENERATOR(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-imds(1)](../man1/systemd-imds.1.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-imdsd@.service(8)](../man8/systemd-imdsd@.service.8.html)

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
