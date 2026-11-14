---
{"title": "rpm-spec-macros(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/rpm-spec-macros.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpm-spec-macros(7) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPM-SPEC-MACROS(7)   Miscellaneous Information Manual  RPM-SPEC-MACROS(7)

## [](#NAME)NAME

           rpm-spec-macros - RPM spec macros

## [](#SYNOPSIS)SYNOPSIS

           %NAME

           %NAME [OPTIONS] [ARGUMENTS]

           %NAME [...]

## [](#DESCRIPTION)DESCRIPTION

           This manual describes RPM macros that are specific to rpm-spec(5)
           files. Distributions commonly ship with numerous additional build
           helper macros for different language ecosystems and so on,
           documented here are only the macros shipped with RPM itself.

           For general RPM macro syntax and usage, see rpm-macros(7) and
           rpm-macrofile(5).

       Build steps
           %autopatch [OPTIONS] [NUMBER ...]
               Apply (a range of) patch numbers. Use in combination with
               %autosetup -N for finer control over patch application.

               Only available in the %prep section.

               -m MIN
                   Apply patches starting from MIN range.
               -M MAX
                   Apply patches up to MAX range.
               -p N
                   Patch prefix stripping level (same as -p to patch(1))
               -q
                   Don't warn if there are no matching patches.
               -v
                   Verbose operation.

           %autosetup [OPTIONS]
               Prepare sources for building: unpack source archives and apply
               patches. See also %setup.

               Only available in the %prep section.

               -a N
                   Unpack source N after changing to the build directory. If
                   multiple instances are needed, use %setup instead.
               -b N
                   Unpack source N before changing to the build directory. If
                   multiple instances are needed, use %setup instead.
               -c
                   Create the build directory (and change to it) before
                   unpacking.
               -C
                   Create the build directory and ensure the archive contents
                   are unpacked there, stripping the top level directory in
                   the archive paths if one exists.
               -D
                   Do not delete the build directory prior to unpacking (used
                   when more than one source is to be unpacked with -a or
                   -b).
               -n
                   Set the name of build directory (default is
                   %{name}-%{version} macro-expanded).
               -N
                   Disable automatic patch application (used for manual
                   %autopatch invocation).
               -p N
                   Patch prefix stripping level (same as -p to patch(1) and
                   %patch).
               -S VCS
                   Specify the Version Control System to use. Supported VCS's
                   are:
                   •   bzr
                   •   gendiff
                   •   git
                   •   git_am
                   •   hg
                   •   patch (default)
                   •   quilt

                   Note that the exact behavior depends on the VCS: for
                   example quilt(1) only controls patches whereas git(1) and
                   hg(1) control the entire source repository.
               -T
                   Skip the default unpacking of the first source (mostly
                   used with -a or -b).
               -v
                   Verbose operation.

           %configure [...]
               Invoke a configure script of an autoconf(1) based software
               with appropriate options for RPM integration, such as
               preconfigured system paths. Any options and arguments are
               passed directly to the script.

               Typical use (but common also in %build section of older spec
               files):
                   %conf
                   %configure --enable-wibble

           %find_lang [OPTIONS] NAME [PREFIX]
               Look for translation files in the buildroot, generating a
               NAME.lang %files manifest for them. NAME is usually the
               upstream project name.

               Available options:

               --all-name
                   Match all package/domain names.
               --generate-subpackages
                   Place translations in per-language sub-packages.
               --with-gnome
                   Find GNOME help files.
               --with-html
                   Find HTML files.
               --with-kde
                   Find KDE help files.
               --with-mate
                   Find MATE help files.
               --with-qt
                   Find QT locale files.
               --with-man
                   Find translated man(1) pages.
               --without-mo
                   Do not find locale files.

               Typical use:
                   %install
                   %make_install
                   %find_lang %{name}

                   %files -f %{name}.lang

           %make_build [...]
               Invoke make(1) for build purposes, with appropriate options
               for RPM integration, such as managing the number of parallel
               jobs. Any options and arguments are passed directly to
               make(1).

               Typical use:
                   %build
                   %make_build

           %make_install [...]
               Invoke make(1) for install purposes, with appropriate options
               for RPM integration, such as DESTDIR pointed at
               $RPM_BUILD_ROOT. Any options and arguments are passed directly
               to make(1).

               Typical use:
                   %install
                   %make_install

           %patch [OPTIONS] [NUMBER ...]
               Apply patch numbers specified in arguments. See also
               %autosetup and %autopatch.

               Only available in the %prep section.

               -b SUF
                   Backup patched files with suffix SUF.
               -d DIR
                   Change to directory DIR before doing anything else.
               -E
                   Remove files emptied by patching.
               -F N
                   Maximum fuzz factor (context diffs).
               -p N
                   Patch prefix stripping level (same as -p to patch(1))
               -R
                   Assume reversed patch.
               -o FILE
                   Send output to FILE instead of patching in place.
               -z SUF
                   Same as -b.
               -Z
                   Set file mtime and atime from patch headers using UTC
                   (context diffs).
               -P N
                   Apply patch number N. Same as passing N as a positional
                   argument.

           %setup [OPTIONS]
               Unpack sources. See also %autosetup.

               Only available inside the %prep section.

               -a N
                   Unpack source N after changing to the build directory.
               -b N
                   Unpack source N before changing to the build directory.
               -c
                   Create the build directory (and change to it) before
                   unpacking.
               -C
                   Create the build directory and ensure the archive contents
                   are unpacked there, stripping the top level directory in
                   the archive paths if one exists.
               -D
                   Do not delete the build directory prior to unpacking (used
                   when more than one source is to be unpacked with -a or
                   -b).
               -n
                   Set the name of build directory (default is
                   %{name}-%{version} macro-expanded).
               -T
                   Skip the default unpacking of the first source (mostly
                   used with -a or -b).
               -q
                   Quiet operation.

       Sources and patches
           %{P:NUMBER}
               Shorthand for %{PATCH​NUMBER}.

           %PATCH​NUMBER
               Expand to the filename of the specified Patch NUMBER.

           %PATCHURL​NUMBER
               Expand to the full URL of the specified Patch NUMBER.

           %patches
               Space separated list of all the patches in the package.

           %{S:NUMBER}
               Shorthand for %{SOURCE​NUMBER}.

           %SOURCE​NUMBER
               Expand to the filename of the specified Source NUMBER.

           %SOURCEURL​NUMBER
               Expand to the full URL of the specified Source NUMBER.

           %sources
               Space separated list of all the sources in the package.

       Conditional builds
           %bcond NAME DEFAULT
               Create a build conditional for a feature called NAME,
               defaulting to either on (1) or off (0).

               Added: 4.17.1

                   # Create a "gnutls" build conditional, enabled by default:
                   %bcond gnutls 1
                   # Create a "bootstrap" build conditional, disabled by default:
                   %bcond bootstrap 0

           %bcond_with NAME
               Deprecated. Identical to %bcond NAME 0.

           %bcond_without NAME
               Deprecated. Identical to %bcond NAME 1.

           %{with NAME}
               Test if build conditional NAME is enabled.

                   %if %{with gnutls}
                   BuildRequires: gnutls-devel
                   %endif

           %{without NAME}
               Test if build conditional NAME is disabled.

           %with_​NAME
               Alternative form of testing a build conditional.

                   %configure \
                        %{?with_static:--enable-static} \
                        %{!?with_static:--disable-static}

           See http://rpm.org/docs/latest/manual/conditionalbuilds.html  for
           more information.

       Path macros
           RPM defines paths for various common locations in UNIX-like
           systems for the sake of flexibility and some portability. Most of
           these macros honor the prefix defined in %_prefix (not to be
           confused with %prefix from relocatable packages).

           The values in parenthesis reflect common values of these macros on
           modern Linux systems and are provided for mental reference only.

           %_bindir
               Most user commands. (/usr/bin)
           %_datadir
               Architecture independent data. (/usr/share)
           %_datarootdir
               Alias for %_datadir.
           %_includedir
               Standard include files. (/usr/include)
           %_infodir
               Info pages. (/usr/share/info)
           %_libdir
               Standard libraries. (/usr/lib or /usr/lib64)
           %_libexecdir
               Binaries run by other commands. (/usr/libexec)
           %_localstatedir
               Variable data files. (/var)
           %_mandir
               Manual pages. (/usr/share/man)
           %_prefix
               Prefix of most path macros. (/usr)
           %_rundir
               Run-time variable data. (/run)
           %_sharedstatedir
               Variable state information. (/var/lib)
           %_sbindir
               Non-essential standard system binaries. (/usr/sbin)
           %_sysconfdir
               Host-specific system configuration. (/etc)

           For historical reasons, the path name macros follow autoconf(1)
           practises.

       Architecture families
           Macros for testing architecture families with %ifarch
           conditionals.

           Typical use:
               %ifarch %{arm32}
               BuildRequires: arm-and-leg-devel
               %endif

           %alpha
               Alpha processors.
           %arm32
               32-bit ARM processors.
           %arm64
               64-bit ARM processors.
           %e2k
               E2K processors.
           %ix86
               32-bit x86 processors.
           %loongarch64
               64-bit LOONGARCH processors.
           %mips
               All MIPS processors.
           %mips32
               32-bit MIPS processors.
           %mips64
               64-bit MIPS processors.
           %mipseb
               Big-endian MIPS processors.
           %mipsel
               Little-endian MIPS processors.
           %power64
               64-bit PowerPC processors.
           %riscv32
               32-bit RISC-V processors.
           %riscv64
               64-bit RISC-V processors.
           %riscv128
               128-bit RISC-V processors.
           %riscv
               All RISC-V processors.
           %sparc
               All Sparc processors.
           %x86_64
               64-bit x86 processors.

       Compiler flags
           %build_cflags
               C compiler flags.  This is traditionally called CFLAGS in
               makefiles.

           %build_cxxflags
               C++ compiler flags.  This is traditionally called CXXFLAGS in
               makefiles.

           %build_fflags
               Fortran compiler flags.  Makefiles use both FFLAGS and FCFLAGS
               as the corresponding variable names.

           %optflags
               Unspecified compiler flags from rpm-rpmrc(5).

               Deprecated, use one of the language specific %build_*flags
               macros instead.

           %set_build_flags
               Shell code to set various compiler/linker environment
               variables such as CFLAGS and LDFLAGS if they have not been set
               already.

       Platform macros
           %_host
               Shorthand for %{_host_cpu}-%{_host_os}

           %_host_cpu
               The architecture of the host where RPM is running.

           %_host_os
               The operating system of the host where RPM is running.

           %_target
               Shorthand for %{_target_cpu}-%{_target_os}.

           %_target_cpu
               The architecture for which the current package is being built
               for.

           %_target_os
               The operating system for which the current package is being
               built for.

## [](#SEE_ALSO)SEE ALSO

           rpmbuild(1) rpm-spec(5) rpm-macros(7)

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

    RPM 6.1.90                      2026-08-03             RPM-SPEC-MACROS(7)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild(1)](../man1/rpmbuild.1.html),  [rpm-spec(5)](../man5/rpm-spec.5.html)

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
