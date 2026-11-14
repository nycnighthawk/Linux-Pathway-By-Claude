---
{"title": "systemd-tpm2-setup.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-tpm2-setup-early.service.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-tpm2-setup.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8)  systemd-tpm2-setup.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-tpm2-setup.service, systemd-tpm2-setup-early.service,
           systemd-tpm2-setup - Set up the TPM2 Storage Root Key (SRK),
           Endorsement Key (EK), and initialize NvPCRs at boot

## [](#SYNOPSIS)SYNOPSIS

           systemd-tpm2-setup.service

           /usr/lib/systemd/systemd-tpm2-setup

## [](#DESCRIPTION)DESCRIPTION

           systemd-tpm2-setup.service and systemd-tpm2-setup-early.service
           are services that generate the Storage Root Key (SRK) and
           Endorsement Key (EK) if they have not been generated yet, and
           stores them in the TPM. If NvPCRs (additional PCR registers in TPM
           NV Indexes) are defined, these are initialized with the anchoring
           secret.

           The services will store the public key of the SRK key pair in a
           PEM file in /run/systemd/tpm2-srk-public-key.pem and
           /var/lib/systemd/tpm2-srk-public-key.pem. They will also store it
           in TPM2B_PUBLIC format in
           /run/systemd/tpm2-srk-public-key.tpm2_public and
           /var/lib/systemd/tpm2-srk-public-key.tpm2b_public.

           systemd-tpm2-setup-early.service runs very early at boot (possibly
           in the initrd), and writes the SRK public key to
           /run/systemd/tpm2-srk-public-key.*  (as /var/ is generally not
           accessible this early yet), while systemd-tpm2-setup.service runs
           during a later boot phase and saves the public key to
           /var/lib/systemd/tpm2-srk-public-key.*.

## [](#FILES)FILES

           /run/systemd/tpm2-srk-public-key.pem,
           /run/systemd/tpm2-srk-public-key.tpm2b_public
               The SRK public key in PEM and TPM2B_PUBLIC format, written
               during early boot.

               Added in version 255.

           /var/lib/systemd/tpm2-srk-public-key.pem,
           /var/lib/systemd/tpm2-srk-public-key.tpm2_public
               The SRK public key in PEM and TPM2B_PUBLIC format, written
               during later boot (once /var/ is available).

               Added in version 255.

           /usr/lib/nvpcr/*.nvpcr
               Definition files for NvPCRs.

               Added in version 259.

## [](#SEE_ALSO)SEE ALSO

           systemd(1)

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

Pages that refer to this page: [systemd-cryptenroll(1)](../man1/systemd-cryptenroll.1.html),  [ukify(1)](../man1/ukify.1.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-tpm2-clear.service(8)](../man8/systemd-tpm2-clear.service.8.html)

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
