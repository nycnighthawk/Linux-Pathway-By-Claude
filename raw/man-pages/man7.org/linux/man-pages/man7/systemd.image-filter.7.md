---
{"title": "systemd.image-filter(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/systemd.image-filter.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd.image-filter(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [USE](#USE) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                           |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD.IMAGE-FILTER(7)    systemd.image-filter   SYSTEMD.IMAGE-FILTER(7)

## [](#NAME)NAME

           systemd.image-filter - Disk Image Dissection Filter

## [](#DESCRIPTION)DESCRIPTION

           In systemd, whenever a disk image (DDI) implementing the UAPI.2
           Discoverable Partitions Specification[1] is activated, a filter
           may be specified controlling which partitions to consider for
           mounting. Such a disk image dissection filter is a string that
           contains per-partition-type patterns, separated by colons (":").
           The individual rules consist of a partition identifier, an equal
           sign ("="), and a shell globbing pattern applied to the GPT label
           string of the partition. See glob(7) for details on shell
           globbing.

           The partition identifiers currently defined are: root, usr, home,
           srv, esp, xbootldr, swap, root-verity, root-verity-sig,
           usr-verity, usr-verity-sig, tmp, var. These identifiers match the
           relevant partition types in the Discoverable Partitions
           Specification, but are agnostic to CPU architectures.

## [](#USE)USE

           Various systemd components that support operating with disk images
           support a --image-filter= command line option to specify the image
           filter to use. If no filter is specified all partitions in
           partition table are considered and no per-label filtering is
           applied (except that partitions with the "_empty" label are always
           ignored).

           For the host root file system image itself
           systemd-gpt-auto-generator(8) is responsible for processing the
           GPT partition table and making use of the included discoverable
           partitions. It accepts an image filter via the kernel command line
           option systemd.image_filter=.

## [](#EXAMPLES)EXAMPLES

           The following image filter string dictates that for the root file
           system partition only partitions shall be considered whose label
           begins with "ParticleOS-". For the /usr/ partition the precise
           label "ParticleOS_47110815" is required.

               root=ParticleOS-*:usr=ParticleOS_47110815

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd-dissect(1), systemd-gpt-auto-generator(8),
           systemd.image-policy(7)

## [](#NOTES)NOTES

            1. UAPI.2 Discoverable Partitions Specification
               https://uapi-group.org/specifications/specs/discoverable_partitions_specification

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

    systemd 262~devel                                 SYSTEMD.IMAGE-FILTER(7)

------------------------------------------------------------------------

Pages that refer to this page: [systemd-dissect(1)](../man1/systemd-dissect.1.html),  [systemd-mstack(1)](../man1/systemd-mstack.1.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-gpt-auto-generator(8)](../man8/systemd-gpt-auto-generator.8.html)

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
