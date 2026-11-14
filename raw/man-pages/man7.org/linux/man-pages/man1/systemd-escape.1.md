---
{"title": "systemd-escape(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/systemd-escape.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-escape(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-ESCAPE(1)             systemd-escape            SYSTEMD-ESCAPE(1)

## [](#NAME)NAME

           systemd-escape - Escape strings for usage in systemd unit names

## [](#SYNOPSIS)SYNOPSIS

           systemd-escape [OPTIONS...] [STRING...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-escape may be used to escape strings for inclusion in
           systemd unit names. The command may be used to escape and to undo
           escaping of strings.

           The command takes any number of strings on the command line, and
           will process them individually, one after another. It will output
           them separated by spaces to stdout. If --stdin is specified,
           strings are instead read from standard input, one per line, and
           the result for each input line is written on a separate output
           line.

           By default, this command will escape the strings passed, unless
           --unescape is passed which results in the inverse operation being
           applied. If --mangle is given, a special mode of escaping is
           applied instead, which assumes the string is already escaped but
           will escape everything that appears obviously non-escaped.

           For details on the escaping and unescaping algorithms see the
           relevant section in systemd.unit(5).

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --suffix=
               Appends the specified unit type suffix to the escaped string.
               Takes one of the unit types supported by systemd, such as
               "service" or "mount". May not be used in conjunction with
               --template=, --unescape or --mangle.

               Added in version 216.

           --template=
               Inserts the escaped strings in a unit name template. Takes a
               unit name template such as foobar@.service. With --unescape,
               expects instantiated unit names for this template and extracts
               and unescapes just the instance part. May not be used in
               conjunction with --suffix=, --instance or --mangle.

               Added in version 216.

           --stdin
               Read strings from standard input, one per line, instead of
               from the command line. The line ending is not included in the
               string to escape or unescape, and the result for each line is
               written on a separate output line. This option may not be
               combined with command line strings.

               Added in version 262.

           --path, -p
               When escaping or unescaping a string, assume it refers to a
               file system path. This simplifies the path (leading, trailing,
               and duplicate "/" characters are removed, no-op path "."
               components are removed, and for absolute paths, leading ".."
               components are removed). After the simplification, the path
               must not contain "..".

               This is particularly useful for generating strings suitable
               for unescaping with the "%f" specifier in unit files, see
               systemd.unit(5).

               Added in version 216.

           --unescape, -u
               Instead of escaping the specified strings, undo the escaping,
               reversing the operation. May not be used in conjunction with
               --suffix= or --mangle.

               Added in version 216.

           --mangle, -m
               Like --escape, but only escape characters that are obviously
               not escaped yet, and possibly automatically append an
               appropriate unit type suffix to the string. May not be used in
               conjunction with --suffix=, --template= or --unescape.

               Added in version 216.

           --instance
               With --unescape, unescape and print only the instance part of
               an instantiated unit name template. Results in an error for an
               uninstantiated template like ssh@.service or a non-template
               name like ssh.service. Must be used in conjunction with
               --unescape and may not be used in conjunction with --template.

               Added in version 240.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXAMPLES)EXAMPLES

           To escape a single string:

               $ systemd-escape 'Hallöchen, Meister'
               Hall\xc3\xb6chen\x2c\x20Meister

           To undo escaping on a single string:

               $ systemd-escape -u 'Hall\xc3\xb6chen\x2c\x20Meister'
               Hallöchen, Meister

           To generate the mount unit for a path:

               $ systemd-escape -p --suffix=mount "/tmp//waldi/foobar/"
               tmp-waldi-foobar.mount

           To generate instance names of three strings:

               $ systemd-escape --template=systemd-nspawn@.service 'My Container 1' 'containerb' 'container/III'
               systemd-nspawn@My\x20Container\x201.service systemd-nspawn@containerb.service systemd-nspawn@container-III.service

           To generate instance names from standard input:

               $ printf '%s\n' 'My Container 1' 'container/III' | systemd-escape --stdin --template=systemd-nspawn@.service
               systemd-nspawn@My\x20Container\x201.service
               systemd-nspawn@container-III.service

           To extract the instance part of an instantiated unit:

               $ systemd-escape -u --instance 'systemd-nspawn@My\x20Container\x201.service'
               My Container 1

           To extract the instance part of an instance of a particular
           template:

               $ systemd-escape -u --template=systemd-nspawn@.service 'systemd-nspawn@My\x20Container\x201.service'
               My Container 1

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.unit(5), systemctl(1)

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

    systemd 262~devel                                       SYSTEMD-ESCAPE(1)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.unit(5)](../man5/systemd.unit.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-loop@.service(8)](../man8/systemd-loop@.service.8.html)

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
