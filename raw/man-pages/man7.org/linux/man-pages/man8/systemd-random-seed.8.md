---
{"title": "systemd-random-seed.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-random-seed.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-random-seed.service(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-....SERVICE(8) systemd-random-seed.service SYSTEMD-....SERVICE(8)

## [](#NAME)NAME

           systemd-random-seed.service, systemd-random-seed - Load and save
           the OS system random seed at boot and shutdown

## [](#SYNOPSIS)SYNOPSIS

           systemd-random-seed.service

           /usr/lib/systemd/systemd-random-seed

## [](#DESCRIPTION)DESCRIPTION

           systemd-random-seed.service is a service that loads an on-disk
           random seed into the kernel entropy pool during boot and saves it
           at shutdown. See random(4) for details. By default, no entropy is
           credited when the random seed is written into the kernel entropy
           pool, but this may be changed with $SYSTEMD_RANDOM_SEED_CREDIT,
           see below. On disk the random seed is stored in
           /var/lib/systemd/random-seed.

           Note that this service runs relatively late during the early boot
           phase, i.e. generally after the initrd phase has finished and the
           /var/ file system has been mounted. Many system services require
           entropy much earlier than this — this service is hence of limited
           use for complex system. It is recommended to use a boot loader
           that can pass an initial random seed to the kernel to ensure that
           entropy is available from earliest boot on, for example
           systemd-boot(7), with its bootctl random-seed functionality.

           When loading the random seed from disk, the file is immediately
           updated with a new seed retrieved from the kernel, in order to
           ensure no two boots operate with the same random seed. This new
           seed is retrieved synchronously from the kernel, which means the
           service will not complete start-up until the random pool is fully
           initialized. On entropy-starved systems this may take a while.
           This functionality is intended to be used as synchronization point
           for ordering services that require an initialized entropy pool to
           function securely (i.e. services that access /dev/urandom without
           any further precautions).

           Care should be taken when creating OS images that are replicated
           to multiple systems: if the random seed file is included
           unmodified each system will initialize its entropy pool with the
           same data, and thus — if otherwise entropy-starved — generate the
           same or at least guessable random seed streams. As a safety
           precaution crediting entropy is thus disabled by default. It is
           recommended to remove the random seed from OS images intended for
           replication on multiple systems, in which case it is safe to
           enable entropy crediting, see below. Also see Safely Building
           Images[1].

           See Random Seeds[2] for further information.

## [](#ENVIRONMENT)ENVIRONMENT

           $SYSTEMD_RANDOM_SEED_CREDIT
               By default, systemd-random-seed.service does not credit any
               entropy when loading the random seed. With this option this
               behaviour may be changed: it either takes a boolean parameter
               or the special string "force". Defaults to false, in which
               case no entropy is credited. If true, entropy is credited if
               the random seed file and system state pass various superficial
               concisistency checks. If set to "force" entropy is credited,
               regardless of these checks, as long as the random seed file
               exists.

               Added in version 243.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), random(4), systemd-boot(7), systemd-stub(7),
           bootctl(1), systemd-boot-random-seed.service(8)

## [](#NOTES)NOTES

            1. Safely Building Images
               https://systemd.io/BUILDING_IMAGES

            2. Random Seeds
               https://systemd.io/RANDOM_SEEDS

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

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-boot-random-seed.service(8)](../man8/systemd-boot-random-seed.service.8.html)

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
