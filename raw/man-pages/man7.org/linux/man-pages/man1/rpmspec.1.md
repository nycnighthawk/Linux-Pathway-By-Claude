---
{"title": "rpmspec(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rpmspec.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpmspec(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPERATIONS](#OPERATIONS) \| [ARGUMENTS](#ARGUMENTS) \| [OPTIONS](#OPTIONS) \| [QUERY OPTIONS](#QUERY_OPTIONS) \| [LIST OPTIONS](#LIST_OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPMSPEC(1)               General Commands Manual               RPMSPEC(1)

## [](#NAME)NAME

           rpmspec - RPM Spec Tool

## [](#SYNOPSIS)SYNOPSIS

           rpmspec {-q|--query} [options] [query-options] SPEC_FILE ...

           rpmspec {-P|--parse} [options] SPEC_FILE ...

           rpmspec --shell [options] [SPEC_FILE ...]

           rpmspec --sources [options] [list-options] SPEC_FILE ...

           rpmspec --patches [options] [list-options] SPEC_FILE ...

## [](#DESCRIPTION)DESCRIPTION

           rpmspec is a tool for querying a spec file. More specifically for
           querying hypothetical packages which would be created from the
           given spec file. So querying a spec file with rpmspec is similar
           to querying a package built from that spec file. But it is not
           identical. With rpmspec you can't query all fields which you can
           query from a built package. E. g. you can't query BUILDTIME with
           rpmspec for obvious reasons. You also cannot query other fields
           automatically generated during a build of a package like auto
           generated dependencies.

## [](#OPERATIONS)OPERATIONS

           -q, --query
               Query parsed spec header, similarly to querying packages.

           -P, --parse
               Output parsed spec file to the standard output. That is,
               conditionals are handled, macros parsed and so on.

           --shell
               Invoke an interactive shell for inspecting macros, optionally
               after parsing a spec. Mainly useful for troubleshooting.

           --sources
               List all source files defined in the spec file(s), one file
               per line.

           --patches
               List all patch files defined in the spec file(s), one file per
               line.

## [](#ARGUMENTS)ARGUMENTS

           SPECFILE
               RPM spec file used for building packages with rpmbuild.

## [](#OPTIONS)OPTIONS

           See rpm-common(8) for the options common to all operations.

## [](#QUERY_OPTIONS)QUERY OPTIONS

           --qf QUERYFMT, --queryformat QUERYFMT
               Specify output format for spec queries. See rpm-queryformat(7)
               for details.

           --rpms
               Operate on the all binary package headers generated from spec.

           --builtrpms
               Operate only on the binary package headers of packages which
               would be built from spec. That means ignoring package headers
               of packages that won't be built from spec i. e. ignoring
               package headers of packages without file section.

           --srpm
               Operate on the source package header(s) generated from spec.

## [](#LIST_OPTIONS)LIST OPTIONS

           --full
               Show full URLs when listing --sources or --patches.

## [](#ENVIRONMENT)ENVIRONMENT

           See rpm-common(8).

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a nonzero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

           rpmspec -q rpm.spec
               Get list of binary packages which would be generated from the
               rpm spec file, eg:
                   rpm-4.11.3-3.fc20.x86_64
                   rpm-libs-4.11.3-3.fc20.x86_64
                   rpm-build-libs-4.11.3-3.fc20.x86_64
                   ...

           rpmspec -q --qf "%{name}: %{summary}n" rpm.spec
               Get summary infos for single binary packages generated from
               the rpm spec file, eg:
                   rpm: The RPM package management system
                   rpm-libs: Libraries for manipulating RPM packages
                   rpm-build-libs: Libraries for building and signing RPM packages
                   ...

           rpmspec -q --srpm rpm.spec
               Get the source package which would be generated from the rpm
               spec file, eg:
                   rpm-4.11.3-3.fc20.x86_64

           rpmspec -P rpm.spec
               Parse the rpm spec file to standard output, eg:
                   Summary: The RPM package management system
                   Name: rpm
                   Version: 4.14.0
                   ...

           rpmspec --shell
               Run interactive macro shell for debugging macros, eg:
                   > %define foo bar
                   > %foo
                   bar
                   > %(date)
                   Tue Apr 13 03:55:37 PM EEST 2021
                   > %getncpus
                   8

           rpmspec --shell popt.spec
               Run interactive macros shell in spec context, eg:
                   %name
                   popt
                   %version
                   1.18

           rpmspec --sources example.spec
               Get list of all sources for given spec files, eg:
                   source-example.tar.gz
                   hello-source.tar.gz

           rpmspec --sources --full example.spec
               Get list of all sources with their full URLs or absolute paths
               for given spec files, eg:
                   http://example.com/source-example.tar.gz
                   hello-source.tar.gz

           rpmspec --patches example.spec
               Get list of all patches for given spec files, eg:
                   hello-1.0-install.patch

## [](#SEE_ALSO)SEE ALSO

           popt(3), rpm(8), rpmbuild(1), rpm-queryformat(7), rpm-macros(7)

           rpmspec --help - as rpm supports customizing the options via popt
           aliases it's impossible to guarantee that what's described in the
           manual matches what's available.

           http://www.rpm.org/ 

## [](#COLOPHON)COLOPHON

           This page is part of the rpm (RPM Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/rpm⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/rpm.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-27.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    RPM 6.1.90                      2026-08-03                     RPMSPEC(1)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild(1)](../man1/rpmbuild.1.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [rpm-macros(7)](../man7/rpm-macros.7.html),  [rpm(8)](../man8/rpm.8.html),  [rpm-common(8)](../man8/rpm-common.8.html)

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
