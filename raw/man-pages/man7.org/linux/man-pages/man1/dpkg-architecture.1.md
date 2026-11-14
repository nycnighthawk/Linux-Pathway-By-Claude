---
{"title": "dpkg-architecture(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dpkg-architecture.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-architecture(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [TERMS](#TERMS) \| [VARIABLES](#VARIABLES) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-architecture(1)            dpkg suite           dpkg-architecture(1)

## [](#NAME)NAME

           dpkg-architecture - set and determine the architecture for package
           building

## [](#SYNOPSIS)SYNOPSIS

           dpkg-architecture [option...] [command]

## [](#DESCRIPTION)DESCRIPTION

           dpkg-architecture provides a facility to determine and set the
           build and host architecture for package building.

           The build architecture is always determined by either the
           DEB_BUILD_ARCH variable if set (and --force not being specified)
           or by an external call to dpkg(1), and cannot be set at the
           command line.

           You can specify the host architecture by providing one or both of
           the options --host-arch and --host-type, otherwise the
           DEB_HOST_ARCH variable is used if set (and --force not being
           specified).  The default is determined by an external call to
           gcc(1), or the same as the build architecture if CC or gcc are
           both not available.  One out of --host-arch and --host-type is
           sufficient, the value of the other will be set to a usable
           default.  Indeed, it is often better to only specify one, because
           dpkg-architecture will warn you if your choice does not match the
           default.

## [](#COMMANDS)COMMANDS

           -l, --list
               Print the environment variables, one each line, in the format
               VARIABLE=value.  This is the default action.

               Support for long command since dpkg 1.17.17.

           -e, --equal architecture
               Check for equality of architecture.  It compares the current
               or specified Debian host architecture against architecture, to
               check if they are equal.  This action will not expand the
               architecture wildcards.  Command finishes with an exit status
               of 0 if matched, 1 if not matched.

               Supported since dpkg 1.13.13.  Support for long command since
               dpkg 1.17.17.

           -i, --is architecture-wildcard
               Check for identity of architecture.  It compares the current
               or specified Debian host architecture against
               architecture-wildcard after having expanded it as an
               architecture wildcard, to check if they match.  Command
               finishes with an exit status of 0 if matched, 1 if not
               matched.

               Supported since dpkg 1.13.13.  Support for long command since
               dpkg 1.17.17.

           -q, --query variable-name
               Print the value of a single variable.

               Support for long command since dpkg 1.17.17.

           -s, --print-set
               Print an export command.  This can be used to set the
               environment variables using the POSIX shell or make eval,
               depending on the output format.

               Support for long command since dpkg 1.17.17.

           -u, --print-unset
               Print a similar command to --print-set but to unset all
               variables.

               Support for long command since dpkg 1.17.17.

           -c, --command command-string
               Execute a command-string in an environment which has all
               variables set to the determined value.

               If the command-string contains shell metacharacters, then it
               will be invoked through the system bourne shell.

               Support for long command since dpkg 1.17.17.

           -L, --list-known
               Print a list of valid architecture names.  Possibly restricted
               by one or more of the matching options --match-wildcard,
               --match-bits or --match-endian

               Supported since dpkg 1.17.14.  Support for long command since
               dpkg 1.17.17.

           -?, --help
               Show the usage message and exit.

               Support for long command since dpkg 1.17.17.

           --version
               Show the version and exit.

               Supported since dpkg 1.17.17.

## [](#OPTIONS)OPTIONS

           -a, --host-arch architecture
               Set the host Debian architecture.

               Support for long option since dpkg 1.17.17.

           -t, --host-type gnu-system-type
               Set the host GNU system type.

               Support for long option since dpkg 1.17.17.

           -A, --target-arch architecture
               Set the target Debian architecture.

               Supported since dpkg 1.17.14.  Support for long option since
               dpkg 1.17.17.

           -T, --target-type gnu-system-type
               Set the target GNU system type.

               Supported since dpkg 1.17.14.  Support for long option since
               dpkg 1.17.17.

           -W, --match-wildcard architecture-wildcard
               Restrict the architectures listed by --list-known to ones
               matching the specified architecture wildcard.

               Supported since dpkg 1.17.14.  Support for long option since
               dpkg 1.17.17.

           -B, --match-bits architecture-bits
               Restrict the architectures listed by --list-known to ones with
               the specified CPU bits.  Either 32 or 64.

               Supported since dpkg 1.17.14.  Support for long option since
               dpkg 1.17.17.

           -E, --match-endian architecture-endianness
               Restrict the architectures listed by --list-known to ones with
               the specified endianness.  Either little or big.

               Supported since dpkg 1.17.14.  Support for long option since
               dpkg 1.17.17.

           --print-format format
               Sets the output format for --print-set and --print-unset, to
               either shell (default) or make.

               Supported since dpkg 1.20.6.

           -f, --force
               Values set by existing environment variables with the same
               name as used by the scripts are honored (i.e. used by
               dpkg-architecture), except if this force flag is present.
               This allows the user to override a value even when the call to
               dpkg-architecture is buried in some other script (for example
               dpkg-buildpackage(1)).

               Support for long option since dpkg 1.17.17.

## [](#TERMS)TERMS

           build machine
               The machine the package is built on.

           host machine
               The machine the package is built for.

           target machine
               The machine the compiler is building for, or the emulator will
               run code for.  This is only needed when building a
               cross-toolchain (or emulator), one that will be built on the
               build architecture, to be run on the host architecture, and
               that itself will build (or run emulated) code for the target
               architecture.

           Debian architecture
               A Debian architecture describes a “machine” (considering it as
               an abstraction not necessarily tied to an actual physical
               device) representing a specific execution environment,
               including its CPU and attributes (such as endianness and
               bits), an operating system (usually a kernel, but other
               paradigms using userland services are possible) and its
               interfaces towards userland including the executable format
               and their ABI, and a libc library and its ABI.

               The special architecture all denotes an architecture
               independent execution environment, used for things such as
               shell and Perl scripts or documentation.

               A Debian architecture is used in binary package metadata and
               filenames (which specifies the binary tree in a package
               repository), and can appear in package relationships.

               An architecture must start with an alphanumeric character
               (“0-9a-zA-Z”), and then gets followed by alphanumeric or dash
               (“-”) characters.

               Examples: amd64, i386, sparc64, hurd-amd64,
               musl-linux-riscv64.

           Debian architecture tuple
               A Debian architecture tuple is the fully qualified
               architecture with all its components spelled out.  This
               differs with Debian architectures in that at least the cpu
               component does not embed the abi.  The current tuple has the
               form abi-libc-os-cpu.

               Examples: base-gnu-linux-amd64, eabihf-musl-linux-arm.

           Debian architecture wildcard
               A Debian architecture wildcard is a special architecture that
               acts as a pattern and will match any ”machine” architecture
               being part of it (except for all).

               The general form is a Debian architecture tuple with four or
               less elements, and with at least one of them being any.
               Missing elements of the tuple are prefixed implicitly as any,
               and thus the following pairs are equivalent:

               any-any-any-any = any
               any-any-os-any = os-any
               any-libc-any-any = libc-any-any

               Examples: linux-any, any-i386, hurd-any, eabi-any-any-arm,
               musl-any-any.

           GNU system type
               A GNU architecture specification string consisting of two
               parts separated by a hyphen: CPU and system.

               The CPU part never contains a hyphen, while the system part
               might itself contain a hyphen to separate a kernel from its
               general ABI, where the general ABI might contain both runtime
               (such as libc) and executable ABI specifiers joined without a
               hyphen.

               Examples: i586-linux-gnu, sparc64-linux-gnu, i686-gnu,
               x86_64-netbsd.

           multiarch triplet
               The clarified GNU system type, used for filesystem paths.
               This triplet does not change even when the baseline ISA gets
               bumped, so that the resulting paths are stable over time.  The
               only current difference with the GNU system type is that the
               CPU part for i386 based systems is always i386.

               Examples: i386-linux-gnu, x86_64-linux-gnu.  Example paths:
               /lib/powerpc64le-linux-gnu/, /usr/lib/i386-gnu/.

## [](#VARIABLES)VARIABLES

           The following variables are read from the environment (unless
           --force has been specified) and set by dpkg-architecture (see the
           TERMS section for a description of the naming scheme):

           DEB_BUILD_ARCH
               The Debian architecture of the build machine.

               Note: If you are not building tools that need to run during
               the build, these are probably not the variables you are
               looking for.  See the "TERMS" section for the meanings of
               these terms.

           DEB_BUILD_ARCH_ABI
               The Debian ABI name of the build machine.

               Supported since dpkg 1.18.11.

           DEB_BUILD_ARCH_LIBC
               The Debian libc name of the build machine.

               Supported since dpkg 1.18.11.

           DEB_BUILD_ARCH_OS
               The Debian system name of the build machine.

               Supported since dpkg 1.13.2.

           DEB_BUILD_ARCH_CPU
               The Debian CPU name of the build machine.

               Supported since dpkg 1.13.2.

           DEB_BUILD_ARCH_BITS
               The pointer size of the build machine (in bits).

               Supported since dpkg 1.15.4.

           DEB_BUILD_ARCH_ENDIAN
               The endianness of the build machine (little / big).

               Supported since dpkg 1.15.4.

           DEB_BUILD_GNU_CPU
               The GNU CPU part of DEB_BUILD_GNU_TYPE.

           DEB_BUILD_GNU_SYSTEM
               The GNU system part of DEB_BUILD_GNU_TYPE.

           DEB_BUILD_GNU_TYPE
               The GNU system type of the build machine.

           DEB_BUILD_MULTIARCH
               The clarified GNU system type of the build machine, used for
               filesystem paths.

               Supported since dpkg 1.16.0.

           DEB_HOST_ARCH
               The Debian architecture of the host machine.

           DEB_HOST_ARCH_ABI
               The Debian ABI name of the host machine.

               Supported since dpkg 1.18.11.

           DEB_HOST_ARCH_LIBC
               The Debian libc name of the host machine.

               Supported since dpkg 1.18.11.

           DEB_HOST_ARCH_OS
               The Debian system name of the host machine.

               Supported since dpkg 1.13.2.

           DEB_HOST_ARCH_CPU
               The Debian CPU name of the host machine.

               Supported since dpkg 1.13.2.

           DEB_HOST_ARCH_BITS
               The pointer size of the host machine (in bits).

               Supported since dpkg 1.15.4.

           DEB_HOST_ARCH_ENDIAN
               The endianness of the host machine (little / big).

               Supported since dpkg 1.15.4.

           DEB_HOST_GNU_CPU
               The GNU CPU part of DEB_HOST_GNU_TYPE.

           DEB_HOST_GNU_SYSTEM
               The GNU system part of DEB_HOST_GNU_TYPE.

           DEB_HOST_GNU_TYPE
               The GNU system type of the host machine.

           DEB_HOST_MULTIARCH
               The clarified GNU system type of the host machine, used for
               filesystem paths.

               Supported since dpkg 1.16.0.

           DEB_TARGET_ARCH
               The Debian architecture of the target machine.

               Note: If you are not building cross-toolchains (or emulators),
               these are probably not the variables you are looking for.  See
               the "TERMS" section for the meanings of these terms.

               Supported since dpkg 1.17.14.

           DEB_TARGET_ARCH_ABI
               The Debian ABI name of the target machine.

               Supported since dpkg 1.18.11.

           DEB_TARGET_ARCH_LIBC
               The Debian libc name of the target machine.

               Supported since dpkg 1.18.11.

           DEB_TARGET_ARCH_OS
               The Debian system name of the target machine.

               Supported since dpkg 1.17.14.

           DEB_TARGET_ARCH_CPU
               The Debian CPU name of the target machine.

               Supported since dpkg 1.17.14.

           DEB_TARGET_ARCH_BITS
               The pointer size of the target machine (in bits).

               Supported since dpkg 1.17.14.

           DEB_TARGET_ARCH_ENDIAN
               The endianness of the target machine (little / big).

               Supported since dpkg 1.17.14.

           DEB_TARGET_GNU_CPU
               The GNU CPU part of DEB_TARGET_GNU_TYPE.

               Supported since dpkg 1.17.14.

           DEB_TARGET_GNU_SYSTEM
               The GNU system part of DEB_TARGET_GNU_TYPE.

               Supported since dpkg 1.17.14.

           DEB_TARGET_GNU_TYPE
               The GNU system type of the target machine.

               Supported since dpkg 1.17.14.

           DEB_TARGET_MULTIARCH
               The clarified GNU system type of the target machine, used for
               filesystem paths.

               Supported since dpkg 1.17.14.

## [](#FILES)FILES

       Architecture tables
           All these files have to be present for dpkg-architecture to work.
           Their location can be overridden at runtime with the environment
           variable DPKG_DATADIR.  These tables contain a format Version
           pseudo-field on their first line to mark their format, so that
           parsers can check if they understand it, such as "# Version=1.0".

           /usr/local/share/dpkg/cputable
               Table of known CPU names and mapping to their GNU name.

               Format version 1.0, supported since dpkg 1.13.2.

           /usr/local/share/dpkg/ostable
               Table of known operating system names and mapping to their GNU
               name.

               Format version 2.0, supported since dpkg 1.18.11.

           /usr/local/share/dpkg/tupletable
               Mapping between Debian architecture tuples and Debian
               architecture names.

               Format version 1.0, supported since dpkg 1.18.11.

           /usr/local/share/dpkg/abitable
               Table of Debian architecture ABI attribute overrides.

               Format version 2.0, supported since dpkg 1.18.11.

       Packaging support
           /usr/local/share/dpkg/architecture.mk
               Makefile snippet that properly sets and exports all the
               variables that dpkg-architecture outputs.

               Supported since dpkg 1.16.1.

## [](#EXAMPLES)EXAMPLES

           dpkg-buildpackage accepts the -a option and passes it to
           dpkg-architecture.  Other examples:

            CC=i386-gnu-gcc dpkg-architecture -c debian/rules build

            eval $(dpkg-architecture -u)

           Check if the current or specified host architecture is equal to an
           architecture:

            dpkg-architecture -elinux-arm64

            dpkg-architecture -ariscv64 -elinux-riscv64

           Check if the current or specified host architecture is a Linux
           system:

            dpkg-architecture -ilinux-any

            dpkg-architecture -aamd64 -ilinux-any

       Usage in debian/rules
           The environment variables set by dpkg-architecture are passed to
           debian/rules as make variables (see make documentation).  However,
           you should not rely on them, as this breaks manual invocation of
           the script.  Instead, you should always initialize them using
           dpkg-architecture with the -q option.  Here are some examples,
           which also show how you can improve the cross compilation support
           in your package:

           Retrieving the GNU system type and forwarding it to ./configure:

            DEB_BUILD_GNU_TYPE ?= $(shell dpkg-architecture -qDEB_BUILD_GNU_TYPE)
            DEB_HOST_GNU_TYPE ?= $(shell dpkg-architecture -qDEB_HOST_GNU_TYPE)
            [...]
            ifeq ($(DEB_BUILD_GNU_TYPE), $(DEB_HOST_GNU_TYPE))
              confflags += --build=$(DEB_HOST_GNU_TYPE)
            else
              confflags += --build=$(DEB_BUILD_GNU_TYPE) \
                           --host=$(DEB_HOST_GNU_TYPE)
            endif
            [...]
            ./configure $(confflags)

           Doing something only for a specific architecture:

            DEB_HOST_ARCH ?= $(shell dpkg-architecture -qDEB_HOST_ARCH)

            ifeq ($(DEB_HOST_ARCH),arm64)
              [...]
            endif

           or if you only need to check the CPU or OS type, use the
           DEB_HOST_ARCH_CPU or DEB_HOST_ARCH_OS variables.

           Note that you can also rely on an external Makefile snippet to
           properly set all the variables that dpkg-architecture can provide:

            include /usr/local/share/dpkg/architecture.mk

            ifeq ($(DEB_HOST_ARCH),arm64)
              [...]
            endif

           In any case, you should never use dpkg --print-architecture to get
           architecture information during a package build.

## [](#ENVIRONMENT)ENVIRONMENT

           DPKG_DATADIR
               If set, it will be used as the dpkg data directory, where the
               architecture tables are located.  Defaults to
               «/usr/local/share/dpkg».

               Supported since dpkg 1.14.17.

           DPKG_COLORS
               Sets the color mode.  The currently accepted values are: auto
               (default), always and never.

               Supported since dpkg 1.18.5.

           DPKG_NLS
               If set, it will be used to decide whether to activate Native
               Language Support, also known as internationalization (or i18n)
               support.  The accepted values are: 0 and 1 (default).

               Supported since dpkg 1.19.0.

## [](#SEE_ALSO)SEE ALSO

           dpkg-buildpackage(1).

## [](#COLOPHON)COLOPHON

           This page is part of the dpkg (Debian Package Manager) project.
           Information about the project can be found at 
           ⟨https://wiki.debian.org/Teams/Dpkg/⟩.  If you have a bug report
           for this manual page, see
           ⟨http://bugs.debian.org/cgi-bin/pkgreport.cgi?src=dpkg⟩.  This
           page was obtained from the project's upstream Git repository ⟨git
           clone https://git.dpkg.org/git/dpkg/dpkg.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.23.7-216-gff7e9               2026-03-07           dpkg-architecture(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_installdeb(1)](../man1/dh_installdeb.1.html),  [dh_installdebconf(1)](../man1/dh_installdebconf.1.html),  [dpkg-buildpackage(1)](../man1/dpkg-buildpackage.1.html),  [deb-src-control(5)](../man5/deb-src-control.5.html),  [deb-src-rules(5)](../man5/deb-src-rules.5.html),  [debhelper(7)](../man7/debhelper.7.html),  [debhelper-compat-upgrade-checklist(7)](../man7/debhelper-compat-upgrade-checklist.7.html)

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
