---
{"title": "systemd-id128(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-id128.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-id128(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-ID128(1)              systemd-id128              SYSTEMD-ID128(1)

## [](#NAME)NAME

           systemd-id128 - Generate and print sd-128 identifiers

## [](#SYNOPSIS)SYNOPSIS

           systemd-id128 [OPTIONS...] new

           systemd-id128 [OPTIONS...] machine-id

           systemd-id128 [OPTIONS...] boot-id

           systemd-id128 [OPTIONS...] invocation-id

           systemd-id128 [OPTIONS...] var-partition-uuid

           systemd-id128 [OPTIONS...] show [NAME|UUID...]

## [](#DESCRIPTION)DESCRIPTION

           id128 may be used to conveniently print sd-id128(3) UUIDs. What
           identifier is printed depends on the specific verb.

           With new, a new random identifier will be generated.

           With machine-id, the identifier of the current machine will be
           printed. See machine-id(5).

           With boot-id, the identifier of the current boot will be printed.

           With invocation-id, the identifier of the current service
           invocation will be printed. This is available in systemd services.
           See systemd.exec(5).

           With show, well-known IDs are printed (for now, only GPT partition
           type UUIDs), along with brief identifier strings. When no
           arguments are specified, all known IDs are shown. When arguments
           are specified, they may be the identifiers or ID values of one or
           more known IDs, which are then printed with their name, or
           arbitrary IDs, which are then printed with a placeholder name.
           Combine with --uuid to list the IDs in UUID style, i.e. the way
           GPT partition type UUIDs are usually shown.

           machine-id, boot-id, and show may be combined with the
           --app-specific=app-id switch to generate application-specific IDs.
           See sd_id128_get_machine(3) for the discussion when this is
           useful. Support for show --app-specific= was added in version 255.

           var-partition-uuid prints a UUID which, following the UAPI.2
           Discoverable Partitions Specification[1], should be used as the
           GPT partition UUID for /var/, being derived from the GPT partition
           type, keyed by the local /etc/machine-id. Added in version 257.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -p, --pretty
               Generate output as programming language snippets.

               Added in version 240.

           -P, --value
               Only print the value. May be combined with -u/--uuid.

               Added in version 255.

           -a app-id, --app-specific=app-id
               With this option, identifiers will be printed that are the
               result of hashing the application identifier app-id and
               another ID. The app-id argument must be a valid sd-id128
               string identifying the application. When used with machine-id,
               the other ID will be the machine ID as described in
               machine-id(5), when used with boot-id, the other ID will be
               the boot ID, and when used with show, the other ID or IDs
               should be specified via the positional arguments.

               Added in version 240.

           -u, --uuid
               Generate output as a UUID formatted in the "canonical
               representation", with five groups of digits separated by
               hyphens. See the Wikipedia entry for Universally Unique
               Identifiers[2] for more discussion.

               Added in version 244.

           --no-pager
               Do not pipe output into a pager.

           --no-legend
               Do not print the legend, i.e. column headers and the footer
               with hints.

           --json=MODE
               Shows output formatted as JSON. Expects one of "short" (for
               the shortest possible output without any redundant whitespace
               or line breaks), "pretty" (for a pretty version of the same,
               with indentation and line breaks) or "off" (to turn off JSON
               output, the default).

           -j
               Equivalent to --json=pretty if running on a terminal, and
               --json=short otherwise.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXIT_STATUS)EXIT STATUS

           On success 0 is returned, and a non-zero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           Example 1. Show a well-known UUID

               $ systemd-id128 show --value user-home
               773f91ef66d449b5bd83d683bf40ad16

               $ systemd-id128 show --value --uuid user-home
               773f91ef-66d4-49b5-bd83-d683bf40ad16

               $ systemd-id128 show 773f91ef-66d4-49b5-bd83-d683bf40ad16
               NAME      ID
               user-home 773f91ef66d449b5bd83d683bf40ad16

           Example 2. Generate an application-specific UUID

               $ systemd-id128 machine-id -u
               3a9d668b-4db7-4939-8a4a-5e78a03bffb7

               $ systemd-id128 new -u
               1fb8f24b-02df-458d-9659-cc8ace68e28a

               $ systemd-id128 machine-id -u -a 1fb8f24b-02df-458d-9659-cc8ace68e28a
               47b82cb1-5339-43da-b2a6-1c350aef1bd1

               $ systemd-id128 -Pu show 3a9d668b-4db7-4939-8a4a-5e78a03bffb7 \
                   -a 1fb8f24b-02df-458d-9659-cc8ace68e28a
               47b82cb1-5339-43da-b2a6-1c350aef1bd1

           On a given machine with the ID
           3a9d668b-4db7-4939-8a4a-5e78a03bffb7, for the application
           1fb8f24b-02df-458d-9659-cc8ace68e28a, we generate an
           application-specific machine ID
           (47b82cb1-5339-43da-b2a6-1c350aef1bd1). If we want to later
           recreate the same calculation on a different machine, we need to
           specify both IDs explicitly as parameters to show.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), sd-id128(3), sd_id128_get_machine(3)

## [](#NOTES)NOTES

            1. UAPI.2 Discoverable Partitions Specification
               https://uapi-group.org/specifications/specs/discoverable_partitions_specification

            2. Universally Unique Identifiers
               https://en.wikipedia.org/wiki/Universally_unique_identifier#Format

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

    systemd 262~devel                                        SYSTEMD-ID128(1)

------------------------------------------------------------------------

Pages that refer to this page: [sd-id128(3)](../man3/sd-id128.3.html),  [sd_id128_get_machine(3)](../man3/sd_id128_get_machine.3.html),  [sd_id128_randomize(3)](../man3/sd_id128_randomize.3.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-gpt-auto-generator(8)](../man8/systemd-gpt-auto-generator.8.html)

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
