---
{"title": "uuidgen(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/uuidgen.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# uuidgen(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFORMING TO](#CONFORMING_TO) \| [EXAMPLES](#EXAMPLES) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    UUIDGEN(1)                    User Commands                    UUIDGEN(1)

## [](#NAME)NAME

           uuidgen - create a new UUID value

## [](#SYNOPSIS)SYNOPSIS

           uuidgen [options]

## [](#DESCRIPTION)DESCRIPTION

           The uuidgen program creates (and prints) a new universally unique
           identifier (UUID) using the libuuid(3) library. The new UUID can
           reasonably be considered unique among all UUIDs created on the
           local system, and among UUIDs created on other systems in the past
           and in the future.

           There are three types of UUIDs which uuidgen can generate:
           time-based UUIDs, random-based UUIDs, and hash-based UUIDs. By
           default uuidgen will generate a random-based UUID if a
           high-quality random number generator is present. Otherwise, it
           will choose a time-based UUID. It is possible to force the
           generation of one of these first two UUID types by using the
           --random or --time options.

           The third type of UUID is generated with the --md5 or --sha1
           options, followed by --namespace namespace and --name name. The
           namespace may either be a well-known UUID, or else an alias to one
           of the well-known UUIDs defined in RFC 4122, that is @dns, @url,
           @oid, or @x500. The name is an arbitrary string value. The
           generated UUID is the digest of the concatenation of the namespace
           UUID and the name value, hashed with the MD5 or SHA1 algorithms.
           It is, therefore, a predictable value which may be useful when
           UUIDs are being used as handles or nonces for more complex values
           or values which shouldn’t be disclosed directly. See the RFC for
           more information.

## [](#OPTIONS)OPTIONS

           -r, --random
               Generate a random-based UUID. This method creates a UUID
               consisting mostly of random bits. It requires that the
               operating system has a high quality random number generator,
               such as /dev/random.

           -t, --time
               Generate a time-based UUID. This method creates a UUID based
               on the system clock plus the system’s ethernet hardware
               address, if present.

           -m, --md5
               Use MD5 as the hash algorithm.

           -s, --sha1
               Use SHA1 as the hash algorithm.

           -6, --time-v6
               Generate a time-based UUID. This method creates a UUID based
               on the system clock and is lexicographically sortable
               according to the contained timestamp.

           -7, --time-v7
               Generate a time-based UUID. This method creates a UUID based
               on the system clock and is lexicographically sortable
               according to the contained timestamp.

           -n, --namespace namespace
               Generate the hash with the namespace prefix. The namespace is
               UUID, or '@ns' where "ns" is well-known predefined UUID
               addressed by namespace name (see above).

           -N, --name name
               Generate the hash of the name.

           -C, --count num
               Generate multiple UUIDs using the enhanced capability of the
               libuuid to cache time-based UUIDs, thus resulting in improved
               performance. However, this holds no significance for other
               UUID types.

           -x, --hex
               Interpret name name as a hexadecimal string.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#CONFORMING_TO)CONFORMING TO

           OSF DCE 1.1

## [](#EXAMPLES)EXAMPLES

           uuidgen --sha1 --namespace @dns --name "www.example.com"

## [](#AUTHORS)AUTHORS

           uuidgen was written by Andreas Dilger for libuuid(3).

## [](#SEE_ALSO)SEE ALSO

           uuidparse(1), libuuid(3), RFC 4122
           <https://tools.ietf.org/html/rfc4122> RFC XXXX
           <https://tools.ietf.org/html/rfcXXXX>

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The uuidgen command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                     UUIDGEN(1)

------------------------------------------------------------------------

Pages that refer to this page: [uuidparse(1)](../man1/uuidparse.1.html),  [uuid(3)](../man3/uuid.3.html),  [uuid_generate(3)](../man3/uuid_generate.3.html),  [swaplabel(8)](../man8/swaplabel.8.html),  [uuidd(8)](../man8/uuidd.8.html)

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
