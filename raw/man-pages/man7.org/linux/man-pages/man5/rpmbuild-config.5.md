---
{"title": "rpmbuild-config(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/rpmbuild-config.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rpmbuild-config(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION](#CONFIGURATION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                            |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPMBUILD-CONFIG(5)         File Formats Manual         RPMBUILD-CONFIG(5)

## [](#NAME)NAME

           rpmbuild-config - rpmbuild macro configuration

## [](#SYNOPSIS)SYNOPSIS

           NAME VALUE

## [](#DESCRIPTION)DESCRIPTION

           The primary configuration mechanism in rpmbuild is rpm-macros(7).
           See rpm-config(5) for the description of the general mechanism,
           this manual only describes the configurables affecting rpmbuild
           operation.

## [](#CONFIGURATION)CONFIGURATION

           The following configurables are supported for the rpm build
           operation, typically invoked through the rpmbuild command.

       Locations and filenames
           %_builddir DIRECTORY
               The directory where the per-package build directories will be
               placed when building.

           %_fileattrsdir DIRECTORY
               The directory where the file classifier configuration is
               located.

           %_rpmdir DIRECTORY
               The directory where newly built binary packages will be
               written.

           %_rpmfilename TEMPLATE
               The output binary package filename query format used when
               building binary packages, as described by rpm-queryformat(7).
               The filename is considered relative to %_rpmdir.

           %_sourcedir DIRECTORY
               The directory where the sources and patches are found when
               building.

           %_srcrpmdir DIRECTORY
               The directory where newly built source packages will be
               written.

           %_topdir DIRECTORY
               The toplevel directory under which the package build
               directories reside by default.

       Informational tags
           These are a special group of macros that if defined, behave as if
           the corresponding tag had been used in a specfile. This allows
           changing the values without modifying thousands of specfiles.

           %bugurl URL
               Configurable bug URL, same as BugURL: tag in a specfile. If
               set, should point to a website for searching for existing and
               filing new issues for this package.

           %distribution STRING
               Configurable distribution informationsame as Distribution: tag
               in a specfile.

           %disturl URL
               Configurable distribution URL, same as DistURL: tag in a
               specfile.

           %disttag STRING
               Configurable distribution tag, same as DistTag: tag in a
               specfile.

           %modularitylabel STRING
               Configurable modularity label, same as ModularityLabel: in a
               specfile. Obsolete.

           %packager STRING
               Configurable packager information, same as Packager: in a
               specfile.

           %translationurl URL
               Configurable translation URL, same as TranslationURL: in a
               specfile.

           %upstreamreleases URL
               Configurable URL for checking for newer upstream releases,
               same as UpstreamReleases: in a specfile.

           %vendor STRING
               Configurable vendor information, same as Vendor: in a
               specfile.

       Build operation
           These settings affect various aspects of the build and can cause a
           build to fail or succeed, but have no direct impact on the
           produced packages.

           %_build_pkgcheck EXECUTABLE
               A program to call for each successfully built and written
               binary package, such as rpmlint. The path to the package is
               passed to the program as a command-line argument.

           %_build_pkgcheck_set EXECUTABLE
               A program to call for the whole binary package set after a
               successfully build, such as rpmlint. The paths to the package
               set are passed to the program as command-line arguments.

           %_build_pkgcheck_srpm EXECUTABLE
               A program to call for each successfully built and written
               source package, such as rpmlint. The path to the package is
               passed to the program as a command-line argument.

           %_default_patch_flags STRING
               Set of default options on all %patch applications.

           %_default_patch_fuzz NUMBER
               Default fuzz level for patch application in spec file. See
               patch(1) for details.

           %_smp_ncpus_max NUMBER
               A hard limit for maximum number of CPU's to use in parallel
               during a package build. Zero means unlimited.

           %_smp_nthreads_max NUMBER
               A hard limit for maximum number of threads to use in parallel
               during a package build. Zero means unlimited.

           %_smp_tasksize_proc NUMBER
               Assumed task size of build processes (during compilation).
               Used for tuning the amount of parallelism based on available
               memory.

           %_smp_tasksize_thread NUMBER
               Assumed task size of threads (during package generation). Used
               for tuning the amount of parallelism based on available
               memory.

       Package generation
           These settings affect various aspects of the produced binary and
           source packages.

           %build_mtime_policy POLICY
               Define how file timestamps are handled in built packages.
               Clamping means ensuring the value does not exceed the
               threshold value.
               •   clamp_to_buildtime: Clamp file timestamps to package
                   buildtime.
               •   clamp_to_source_date_epoch: Clamp file timestamps to the
                   SOURCE_DATE_EPOCH environment variable.

           %clamp_mtime_to_source_date_epoch BOOLEAN
               Alias for %build_mtime_policy clamp_to_source_date_epoch. Do
               not use. Deprecated and scheduled for removal.

           %source_date_epoch_from_changelog BOOLEAN
               Whether to set the SOURCE_DATE_EPOCH environment variable from
               the timestamp of the topmost %changelog entry.

           %use_source_date_epoch_as_buildtime BOOLEAN
               Whether to use the SOURCE_DATE_EPOCH environment variable
               value as the buildtime of packages.

           %_binary_filedigest_algorithm HASHALGO
               The algorithm to use for generating per-file checksums (aka
               digests) of binary packages.  See rpm-config(5) for the
               supported values.

           %_binary_payload IOFLAGS
               The IO method and compression to use for generating the
               payload of binary packages. See rpm-payloadflags(7).

           %_buildhost HOSTNAME
               Use HOSTNAME as the package buildhost instead of acquiring the
               value from gethostname(2).

           %_buildtime TIMESTAMP
               Use TIMESTAMP as the package buildtime instead of acquiring
               the value from time(2).

           %_changelog_trimage TIMESTAMP
               Maximum age of preserved changelog entries in binary packages,
               relative to newest existing entry. Unix timestamp format. The
               value of zero disables trimming by age.

           %_changelog_trimtime TIMESTAMP
               An alternative strategy for changelog trimming: trim all
               changelog entries older than the specified timestamp. Unix
               timestamp format. The value of zero disables trimming by time.

           %_docdir_fmt TEMPLATE
               A template for the per-package documentation directory name,
               ie. the files packaged with %doc.

           %__docdir_path PATH
               A colon separated list of directories whose contents should be
               always considered as documentation.

           %_openpgp_autosign_id KEYID
               The OpenPGP key id or fingerprint to use for automatically
               signing packages after a successful build. See also
               rpmsign(1).

           %_rpmformat VERSION
               The RPM package format to produce. Supported values are:
               •   4: RPM v4 format
               •   6: RPM v6 format

           %_source_filedigest_algorithm HASHALGO
               The algorithm to use for generating per-file checksums (aka
               digests) of source packages. See rpm-config(5) for the
               supported values.

           %_source_payload
               The IO method and compression to use for generating the
               payload of source packages. See rpm-payloadflags(7).

           %__gpg_reserved_space NUMBER
               The number of bytes to reserve for signatures in the signature
               header. This reserve helps to speed up package signing
               significantly.

       Debuginfo generation
           Debuginfo sub-packages contain information necessary to debug
           otherwise release-specification builds with a debugger. These
           settings determine whether debuginfo packages are generated and
           various aspects of the generated debugging information.

           %_build_id_links MODE
               Defines how and if build_id links are generated for ELF files.
               The following settings are supported:
               •   none: No build_id links are generated.
               •   alldebug: Generate rpm < 4.14 style build_id links, ie
                   everything in the -debuginfo package.
               •   separate: Generate build_id links in binary packages.
               •   compat: Same as separate but with a compatibility link(s)
                   in the -debuginfo packages.

           %_debuginfo_subpackages BOOLEAN
               Whether rpm should create separate debuginfo packages for each
               subpackage.

           %_debugsource_packages BOOLEAN
               Whether rpm should put debug source files into their own
               subpackage.

           %_enable_debug_packages BOOLEAN
               Whether rpm should generate debuginfo subpackages.

           %_include_gdb_index BOOLEAN
               Include a .gdb_index section in the .debug files. Requires
               %_enable_debug_packages to be enabled and gdb-add-index(1) to
               be installed.

           %_include_minidebuginfo BOOLEAN
               Include minimal debug information in build binaries. Requires
               %_enable_debug_packages to be enabled.

           %_no_recompute_build_ids BOOLEAN
               Disable recomputation of build-ids. Cannot be used with
               %_unique_build_ids.

           %_unique_build_ids BOOLEAN
               Whether build-ids should be made unique between package
               version/releases when generating debuginfo packages.

           %_unique_debug_names BOOLEAN
               Whether .debug files should be made unique between package
               version, release and architecture. Requires %_unique_build_ids
               to be enabled.

           %_unique_debug_srcs BOOLEAN
               Whether the /usr/debug/src/<package> directories should be
               unique between package version, release and architecture.

           %__find_debuginfo EXECUTABLE
               The location of the debuginfo helper executable.

       Legacy compatibility
           These settings deal with several decades of backwards
           compatibility. Most of them determine whether a particular issue
           is considered an error or just a warning. Sometimes also useful
           for temporarily working around issues while packaging.

           %_binaries_in_noarch_packages_terminate_build BOOLEAN
               Whether ELF binaries in noarch packages should terminate a
               build.

           %_duplicate_files_terminate_build BOOLEAN
               Whether duplicate files in %files section should terminate a
               build.

           %_empty_manifest_terminate_build BOOLEAN
               Whether an empty %files manifest file should terminate a
               build.

           %_invalid_encoding_terminates_build BOOLEAN
               Whether a non-UTF8 encoding in package data should terminate a
               build.

           %__find_provides EXECUTABLE
               The executable to use for rpm 3.x style provides generation.
               Do not use. Deprecated and scheduled for removal.

           %__find_requires EXECUTABLE
               The executable to use for rpm 3.x style requires generation.
               Do not use. Deprecated and scheduled for removal.

           %_missing_build_ids_terminate_build BOOLEAN
               Whether ELF files without build-ids should terminate a build.
               For historical reasons, this is only applicable if
               %_enable_debug_packages is also enabled.

           %_missing_doc_files_terminate_build BOOLEAN
               Whether missing %doc files in the build directory should
               terminate a build.

           %_unpackaged_files_terminate_build BOOLEAN
               Whether unpackaged files in a build root should terminate a
               build.

           %_nonzero_exit_pkgcheck_terminate_build BOOLEAN
               Whether the build of packages should fail if package checker
               (if defined) returns an error? See the %_build_pkgcheck_*
               macros.

           %_use_internal_dependency_generator BOOLEAN
               If enabled, use rpm 3.x style dependency generation. Do not
               use. Deprecated and scheduled for removal.

           %_use_weak_usergroup_deps BOOLEAN
               If enabled, dilute user() and group() requires into
               recommends. Useful when transitioning to rpm-sysusers(7) based
               user/group management.

           %_wrong_version_format_terminate_build BOOLEAN
               Whether invalid version format in dependencies etc should
               terminate a build.

## [](#SEE_ALSO)SEE ALSO

           rpmbuild(1), rpm-common(8), rpm-macrofile(5), rpm-rpmrc(5),
           rpm-config(5), rpm-payloadflags(7) rpm-macros(7)

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

    RPM 6.1.90                      2026-08-03             RPMBUILD-CONFIG(5)

------------------------------------------------------------------------

Pages that refer to this page: [rpmbuild(1)](../man1/rpmbuild.1.html),  [rpm-macrofile(5)](../man5/rpm-macrofile.5.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [rpm-dependency-generators(7)](../man7/rpm-dependency-generators.7.html),  [rpm-payloadflags(7)](../man7/rpm-payloadflags.7.html),  [rpm-queryformat(7)](../man7/rpm-queryformat.7.html),  [rpm-sysusers(7)](../man7/rpm-sysusers.7.html)

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
