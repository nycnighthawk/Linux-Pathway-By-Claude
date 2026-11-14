---
{"title": "debhelper-compat-upgrade-checklist(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/debhelper-compat-upgrade-checklist.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# debhelper-compat-upgrade-checklist(7) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    debhelper(7)                    Debhelper                    debhelper(7)

## [](#NAME)NAME

           debhelper-compat-upgrade-checklist - Upgrade checklist for
           supported debhelper compat levels

## [](#SYNOPSIS)SYNOPSIS

           This document is an upgrade checklist of all the supported
           debhelper compat levels. It also lists all the supported debhelper
           compat levels.

           The dh_assistant compat-upgrade-checklist command can provide a
           package specific upgrade checklist from compat 7 and up (requires
           debhelper/13.25 or later). Its main limitation is accuracy of its
           heuristics. Please review the documentation of dh_assistant(1) for
           details.

           Information about how to declare the compat level is in
           "COMPATIBILITY LEVELS" in debhelper(7).

           If you are upgrading from a (now) obsolete compat level, then
           please refer to debhelper-obsolete-compat(7).

## [](#DESCRIPTION)DESCRIPTION

       Upgrade checklist for supported compatibility levels
           These are the available compatibility levels:

           v15 This compatibility level is still open for development; use
               with caution.

               Changes from v14 are:

               -       The single-binary add-on for dh is no longer
                       implicitly activated by source packages that have a
                       single Package stanza in debian/control. If the
                       package needs the short-cuts for single-binary
                       packages, it must explicitly activate the
                       single-binary add-in.

                       This can be done via a Build-Depends on
                       dh-sequence-single-binary.

                       Any --without single-binary passed to dh to avoid the
                       warning in compat 14 can now be removed to simplify
                       debian/rules without triggering the warning.

               -       It is now an error to use package-less versions of
                       debhelper configuration files when there are 2 or more
                       binary packages listed in debian/control in most
                       cases.  Legacy files should be renamed to
                       debian/package.foo (from debian/foo) where package is
                       the first binary package listed in debian/control.

                       The primary exception to this change are files such as
                       debian/changelog, debian/NEWS, and debian/copyright,
                       where the same file is used for all packages by
                       default.  These cases will remain unchanged.

               -       It is now an error to use a packaging file without the
                       package prefix for --name even if the source package
                       only produces one binary package. As example, if you
                       had a debian/bar.service with the following snippet in
                       debian/rules:

                        override_dh_installsystemd:
                           dh_installsystemd -p foo --name bar

                       Then you need to rename debian/bar.service to
                       debian/foo.bar.service.

           v14 This is the recommended mode of operation.

               Changes from v13 are:

               -       The dh_installmodules tool will now install its
                       configuration files under /usr/lib/modprobe.d/package
                       instead of /etc/modprobe.d.

                       Please consider using the "rm_conffile" feature from
                       dh_installdeb(1) to ensure the proper removal of
                       previous modprobe files.

                       Note: Retroactively change in debhelper/14.1 - The
                       dh_installpam command had a similar change, which was
                       reverted at the request of the pam maintainer.

               -       Packages using the dh sequencer should be aware the
                       following changes:

                       -   The order and placement has changed for
                           dh_strip_nondeterminism, dh_compress, and
                           dh_fixperm. Previously, these three commands were
                           run in the listed order between dh_installxfonts
                           and dh_missing.

                           Their new placement is after dh_missing (arch:all)
                           or dh_shlibdeps (arch:any) and before
                           dh_installdeb. Additionally, their new order is
                           dh_fixperms, dh_strip_nondeterminism, and then
                           dh_compress.

                           This change may require updates to third-party
                           add-ons that use either of these three commands as
                           anchor or to hook targets for any of these
                           commands that made assumptions about the command
                           order.

                           Additionally, dh_strip_nondeterminism and
                           dh_compress plus any commands added by third-party
                           add-ons using these as anchors will no longer be
                           able to rely on the mode/ownership normalization
                           by dh_fixperms, which may expose bugs in the form
                           of incorrect mode or ownership in the resulting
                           binary package.

                           Please file any such bugs against the relevant
                           tool. Feel free to include the debhelper
                           maintainers in CC.

                       -   The tool dh_installsysusers is now included in the
                           default sequence. This helper tool will process
                           systemd sysusers files.

                       -   The dh_installalternatives tool will now be run
                           after dh_link rather than after
                           dh_installinitramfs in the default dh sequence.

                       -   The dh_dwz command has been removed from the
                           default sequence. If it is still desired, add
                           dh-sequence-dwz to Build-Depends-Arch or run it in
                           execute_before_dh_strip-arch with -a to get the
                           closest emulation of the previous behavior.

                           Note: The dh_dwz command will cause a lot of
                           differences in the generated debug symbols.  If
                           you use diffoscope as part of your compat upgrade
                           checks, you may want to temporarily use dh_dwz to
                           keep the delta reviewable while upgrading and then
                           remove dh_dwz afterwards.

                       -   Use of the dh_gconf command in override and hook
                           targets now causes an error.  The dh_gconf command
                           has been a no-op for years and was removed in
                           debhelper 13.4.

                       -   A new tool called dh_computeautosubstvars has been
                           added and is now run immediately before
                           dh_gencontrol. If you inject commands before
                           dh_gencontrol (either via hook targets or
                           third-party sequence add-on), consider moving them
                           to after dh_installdeb instead as the new tool
                           generally assumes no more changes will occur
                           between it is called and dh_gencontrol is called.

                           Notable exception to this assumption if you have
                           to tweak substvars per
                           <https://lists.debian.org/debian-devel/2024/03/msg00030.html>.

                       -   This item only applies to source packages that
                           have exactly one Package stanza in debian/control.

                           The dh_auto_install command now unconditionally
                           uses --destdir=debian/tmp by default. The
                           special-case for source packages building a single
                           binary package is now moved to single-binary dh
                           addon. Note, this add-on is activated by default
                           in compat 14 but not in compat 15 (see next bullet
                           item).

                       -   This item only applies to source packages that
                           have exactly one Package stanza in debian/control.

                           The dh sequencer will warn if the single-binary
                           addon is implicitly activated to warn maintainers
                           of the pending compat 15 change in
                           dh_auto_install. The implicit activation is a
                           transitional feature to reduce the changes of
                           risks with this change.  In compat 15, the
                           implicit activation will no longer trigger.

                           Maintainers are urged to either explicitly
                           activate the single-binary addon to preserve the
                           existing behaviour (e.g., by adding
                           dh-sequence-single-binary to Build-Depends), or
                           explicitly passing --destdir to dh_auto_install if
                           used and then passing --without single-binary to
                           dh (the latter to silence the warning).

                           The rationale for this change is to avoid
                           "surprises" when adding a second binary package
                           later.  Previously, debhelper would silently
                           change behaviour often resulting in empty binary
                           packages being uploaded to the archive by mistake.
                           With the new behaviour, the single-binary addon
                           will detect the mismatch and warn the maintainer
                           of what is about to happen.

               -       The dh_installsystemduser tool will default to
                       enabling systemd user units, start them on
                       installation, restart them on upgrades and stop them
                       on uninstalling the package.

               -       The dh_gencontrol tool now automatically applies
                       relationship substvars to relevant fields. That means
                       that many substvars such as ${misc:Depends} and
                       ${shlibs:Depends} no longer need to be explicitly
                       mentioned in debian/control. This applies to any
                       substvar named after a field that the installed
                       version of dpkg considers a relation or
                       dependency-like field. At the time of writing, the
                       list consists of:

                       -   Pre-Depends

                       -   Depends

                       -   Recommends

                       -   Suggests

                       -   Enhances

                       -   Conflicts

                       -   Breaks

                       -   Replaces

                       -   Provides

                       -   Built-Using

                       -   Static-Built-Using

                       This means that Depends: foo, ${misc:Depends} in
                       debian/control can now be reduced to Depends: foo and
                       Depends: ${misc:Depends}, ${shlibs:Depends} can be
                       removed entirely as examples of how the feature works.

                       Note that other substvars such as ${binary:Version}
                       are unaffected by this change and should still be used
                       explicitly as necessary. Additionally, for Essential:
                       yes packages that manually promoted ${shlibs:Depends}
                       into Pre-Depends field, dh_shlibdeps will handle this
                       automatically as well (see the next compat item).

                       See
                       <https://lists.debian.org/debian-devel/2024/02/msg00230.html>
                       for the details of this proposal. The summary in
                       <https://lists.debian.org/debian-devel/2024/03/msg00030.html>
                       also covers when the substvars need tweaking.  The
                       most common case involves using the -d option from
                       dpkg-shlibdeps possibly via dh_shlibdeps.

                       Note: This change will cause false-positives from an
                       unfixed lintian(1). Please check
                       <https://bugs.debian.org/1067653> for lintian(1)
                       support for this change.

                       Finally, debhelper also applies this feature the
                       substvars for the following fields due to
                       implementation details:

                       -   Commands

                           See #638517 <https://bugs.debian.org/638517> for
                           what the field is used for.

               -       The dh_shlibdeps tool now defaults to using
                       ${shlibs:Pre-Depends} for packages that are Essential:
                       yes.

                       Note due to the dh_gencontrol change above, any
                       package using dh_gencontrol will not have to do
                       anything for this migration.

                       Fixed in debhelper/14.3: There was a bug in the
                       implementation that meant it did not trigger for
                       compat 14 before debhelper/14.3.

               -       When running dh_auto_install, debhelper provided build
                       systems will now ensure all paths in the destdir have
                       minimal user permissions (chmod -R u+rwX) to avoid
                       weird permission denied errors during builds.

                       Third-party provided debhelper build systems are
                       recommended to support this as well.  This can be done
                       by running

                            $this->ensure_minimal_permissions($destdir) if not compat(13);

                       in the debhelper Buildsystem code from their sub
                       install implementation after the upstream code has
                       been run.

                       If you are not using dh_auto_install and you run into
                       weird permission denied errors, you can often solve
                       this by running chmod -R u+rwX DIRECTORY after running
                       the install target from the upstream build system.

                       Please take care to check if your package has any
                       special cases for permissions where files or
                       directories for some reason must not have the "user
                       write bit" set. Known cases are *.ali files and
                       /etc/sudoers.d, which dh_fixperms will fix up by
                       default.

                       The problem with uncommon permissions have always been
                       present in theory. However, it has become considerable
                       more visible with dh_fixperms being run later in the
                       sequence as of compat 14 and with the move to remove
                       fakeroot by default (which papered over some of these
                       issues). This change is aimed at mitigating the
                       problem.

               -       The debhelper configuration files are subject to the
                       following changes:

                       -   It now triggers a warning to use package-less
                           versions of debhelper configuration files when
                           there are 2 or more binary packages listed in
                           debian/control in most cases.  Legacy files should
                           be renamed to debian/package.foo (from debian/foo)
                           where package is the first binary package listed
                           in debian/control.

                           The primary exception to this change are files
                           such as debian/changelog, debian/NEWS, and
                           debian/copyright, where the same file is used for
                           all packages by default.  These cases will remain
                           unchanged.  The debhelper tool using the files
                           will trigger warnings on usage.

                           In compat 15 (or later), this is changed to an
                           error.

                           For most packages, this item can be fixed by
                           running:

                                apt-get satisfy 'debputy (>= 0.1.73~), debhelper (>= 13.26~)'
                                debputy migrate-from-dh --migration-target=dh-package-prefixed-config-files

                           The only known caveat are architecture specific
                           configuration files (such as debian/symbols.amd64
                           or debian/install.amd64).

                       -   It now triggers a warning to use a packaging file
                           without the package prefix for --name even if the
                           source package only produces one binary package.
                           As example, if you had a debian/bar.service with
                           the following snippet in debian/rules:

                            override_dh_installsystemd:
                               dh_installsystemd -p foo --name bar

                           Then you need to rename debian/bar.service to
                           debian/foo.bar.service.

                           In compat 15 (or later), this is changed to an
                           error.

                           For most packages, this item can be fixed by
                           running:

                                apt-get satisfy 'debputy (>= 0.1.73~), debhelper (>= 13.26~)'
                                debputy migrate-from-dh --migration-target=dh-package-prefixed-config-files

                           The only known caveat are architecture specific
                           configuration files. The debhelper stack does not
                           accept any config files that have architecture
                           restrictions and --name. However, third-party
                           add-ons might.

                       -   The default look up rules for Dh_Lib based tools
                           now assume that configuration files are no longer
                           named (--name) nor support architecture
                           restrictions by default.  If you work with a
                           third-party debhelper-like tool and need support
                           for either of these features, please file a bug
                           against the tool asking it to declare its
                           configuration file with the relevant options in
                           its pkgfile call.

                           Note that debhelper itself tweaked its rules for
                           most of its tools as well based on analysis of
                           usage via codesearch.debian.org. Should you be
                           relying on a feature like architecture
                           restrictions for a given config file that is no
                           longer supported, please file a feature request
                           for the use-case and it might be restored.

               -       Packages using the cmake build system should be aware
                       of the following changes:

                       -   The cmake buildsystem now passes
                           -DCMAKE_BUILD_RPATH_USE_ORIGIN=ON to cmake(1) to
                           avoid some reproducibility issues.

                       -   The cmake build system now sets the ASMFLAGS
                           environment variable when it is unset and ASFLAGS
                           is present. The former name (ASMFLAGS) is the name
                           cmake expects, while the latter (ASFLAGS) is the
                           name that dpkg-buildpackage(1) uses.

                       -   The cmake build systems now use cmake --install
                           instead of make install in the dh_auto_install(1)
                           call.  Any override of dh_auto_install that passes
                           extra parameters to the upstream build system
                           should be reviewed.

               -       Packages using the meson build system should be aware
                       of the following changes:

                       -   The meson build system now passes
                           --auto-features=enabled to meson.

                       -   The meson+ninja build system now use meson install
                           instead of ninja install in the dh_auto_install(1)
                           call.  Any override of dh_auto_install that passes
                           extra parameters to the upstream build system
                           should be reviewed.

               -       The debian/compat file is no longer accepted as a
                       source for specifying the debhelper compat level.
                       Please review "COMPATIBILITY LEVELS" in debhelper(7)
                       for alternatives.

               -       The tool dh_installtmpfiles now runs with --remove on
                       package removal, and --purge on package purge. systemd
                       v256 is required for the latter.

               -       The dh_lintian tool no longer accepts architecture
                       specific overrides files for packages with Multi-Arch:
                       same in debian/control, since these would not be
                       co-installable. Instances affected by this error
                       should migrate to lintian(1) architecture specific
                       overrides.

               -       The third-party dh_qmldeps tool (from pkg-kde-tools
                       package) no longer demote detected dependencies. In
                       v13 you get warnings about demotions. You can use the
                       -d dependency field in the debian/PKG.qmlfiles to get
                       the dependencies end up in the correct dependency
                       field.

           v13 Changes from v12 are:

               -       The meson+ninja build system now uses meson test
                       instead of ninja test when running the test suite.
                       Any override of dh_auto_test that passes extra
                       parameters to upstream test runner should be reviewed
                       as meson test is not command line compatible with
                       ninja test.

               -       All debhelper like tools based on the official
                       debhelper library (including dh and the official dh_*
                       tools) no longer accepts abbreviated command
                       parameters.  At the same time, dh now optimizes out
                       calls to redundant dh_* helpers even when passed long
                       command line options.

               -       The ELF related debhelper tools (dh_dwz, dh_strip,
                       dh_makeshlibs, dh_shlibdeps) are now only run for arch
                       dependent packages by default (i.e. they are excluded
                       from *-indep targets and are passed -a by default). If
                       you need them for *-indep targets, you can add an
                       explicit Build-Depends on dh-sequence-elf-tools.

               -       The third-party gradle build system (from
                       gradle-debian-helper package) now runs the
                       upstream-provided test suite automatically.  To
                       suppress such behavior, override dh_auto_test.

               -       The dh_installman tool now aborts if it sees
                       conflicting definitions of a manpage.  This typically
                       happens if the upstream build system is installing a
                       compressed version and the package lists an
                       uncompressed version of the manpage in
                       debian/package.manpages.  Often the easiest fix is to
                       remove the manpage from debian/package.manpages
                       (assuming both versions are identical).

               -       The dh_auto_* helpers now reset the environment
                       variable HOME and the common XDG_* variables.  Please
                       see description of the environment variables in
                       "ENVIRONMENT" in debhelper(1) for how this is handled.

                       This feature changed between debhelper 13 and
                       debhelper 13.2.

               -       The dh command will now error if an override or hook
                       target for an obsolete command are present in
                       debian/rules (e.g. override_dh_systemd_enable:).

               -       The dh_missing command will now default to
                       --fail-missing.  This can be reverted to a non-fatal
                       warning by explicitly passing --list-missing like it
                       was in compat 12.

                       If you do not want the warning either, please omit the
                       call to dh_missing.  If you use the dh command
                       sequencer, then you can do this by inserting an empty
                       override target in the debian/rules file of the
                       relevant package.  As an example:

                           # Disable dh_missing
                           override_dh_missing:

               -       The dh command sequencer now runs dh_installtmpfiles
                       in the default sequence.  The dh_installtmpfiles takes
                       over handling of tmpfiles.d configuration files.
                       Related functionality in dh_installsystemd is now
                       disabled.

                       Note that dh_installtmpfiles responds to
                       debian/package.tmpfiles where dh_installsystemd used a
                       name without the trailing "s".

               -       Many dh_* tools now support limited variable expansion
                       via the ${foo} syntax.  In many cases, this can be
                       used to reference paths that contain either spaces or
                       dpkg-architecture(1) values.  While this can reduce
                       the need for dh-exec(1) in some cases, it is not a
                       replacement dh-exec(1) in general.  If you need
                       filtering, renaming, etc., the package will still need
                       dh-exec(1).

                       Please see "Substitutions in debhelper config files"
                       for syntax and available substitution variables.  To
                       dh_* tool writers, substitution expansion occurs as a
                       part of the filearray and filedoublearray functions.

               -       The dh command sequencer will now skip all hook and
                       override targets for dh_auto_test, dh_dwz and dh_strip
                       when DEB_BUILD_OPTIONS lists the relevant nocheck /
                       nostrip options.

                       Any package relying on these targets to always be run
                       should instead move relevant logic out of those
                       targets.  E.g. non-test related packaging code from
                       override_dh_auto_test would have to be moved to
                       execute_after_dh_auto_build or
                       execute_before_dh_auto_install.

               -       The cmake buildsystem now passes
                       -DCMAKE_SKIP_INSTALL_ALL_DEPENDENCY=ON to cmake(1) to
                       speed up automatic installation process. If for some
                       reason you need previous behavior, override the flag:

                           dh_auto_configure -- -DCMAKE_SKIP_INSTALL_ALL_DEPENDENCY=OFF ...

           v12 Changes from v11 are:

               -       The dh_makeshlibs tool now generates shlibs files with
                       versioned dependency by default.  This means that
                       -VUpstream-Version (a.k.a. -V) is now the default.

                       If an unversioned dependency in the shlibs file is
                       wanted, this can be obtained by passing -VNone
                       instead.  However, please see dh_makeshlibs(1) for the
                       caveat of unversioned dependencies.

               -       The -s (--same-arch) option is removed.  Please use -a
                       (--arch) instead.

               -       Invoking dh_clean -k now causes an error instead of a
                       deprecation warning.

               -       The --no-restart-on-upgrade option in dh_installinit
                       has been removed.  Please use the new name
                       --no-stop-on-upgrade

               -       There was a bug in the doit (and similar) functions
                       from Debian::Debhelper::Dh_Lib that made them spawn a
                       shell in one particular circumstance.  This bug is now
                       removed and will cause helpers that rely on the bug to
                       fail with a "command not found"-error.

               -       The --list-missing and --fail-missing in dh_install
                       has been removed.  Please use dh_missing and its
                       corresponding options, which can also see the files
                       installed by other helpers.

               -       The dh_installinit helper no longer installs
                       configuration for the upstart init system.  Instead,
                       it will abort the build if it finds an old upstart
                       configuration file.  The error is there to remind the
                       package maintainer to ensure the proper removal of the
                       conffiles shipped in previous versions of the package
                       (if any).

               -       The dh_installdeb tool will do basic validation of
                       some dpkg-maintscript-helper(1) commands and will
                       error out if the commands appear to be invalid.

               -       The dh_missing tool will now default to
                       --list-missing.

               -       The dh_makeshlibs tool will now only pass libraries to
                       dpkg-gensymbols(1) if the ELF binary has a SONAME
                       (containing ".so").

               -       The dh_compress tool no longer compresses examples
                       (i.e. anything installed in
                       </usr/share/doc/package/examples>.)

               -       The standard sequence in dh now includes dh_dwz and
                       dh_installinitramfs by default.  This makes the dwz
                       and installinitramfs sequences obsolete and they will
                       now fail with an error.  If you want to skip these
                       commands, then please insert an empty override target
                       for them in debian/rules (e.g. override_dh_dwz:)

               -       The build systems meson and autoconf no longer
                       explicitly set the --libexecdir variable and thus
                       relies on the build system default - which should be
                       /usr/libexec (per FHS 3.0, adopted in Debian Policy
                       4.1.5).

                       If a particular upstream package does not use the
                       correct default, the parameter can often be passed
                       manually via dh_auto_configure(1).  E.g.  via the
                       following example:

                           override_dh_auto_configure:
                               dh_auto_configure -- --libexecdir=/usr/libexec

                       Note the -- before the --libexecdir parameter.

               -       Retroactively removed in debhelper/13.5:

                       The dh_installdeb tool would no longer install the
                       maintainer provided conffiles file as it was deemed
                       unnecessary.  However, the remove-on-upgrade from
                       dpkg/1.20 made the file relevant again and
                       dh_installdeb now installs it again in compat levels
                       12+.

               -       The dh_installsystemd tool no longer relies on
                       dh_installinit for handling systemd services that have
                       a sysvinit alternative.  Both tools must now be used
                       in such a case to ensure the service is properly
                       started under both sysvinit and systemd.

                       If you have an override for dh_installinit (e.g. to
                       call it with --no-start) then you will probably need
                       one for dh_installsystemd as well now.

                       This change makes dh_installinit inject a
                       misc:Pre-Depends for init-system-helpers (>= 1.54~).
                       Please ensure that the package lists
                       ${misc:Pre-Depends} in its Pre-Depends field before
                       upgrading to compat 12.

               -       The third-party dh_golang tool (from dh-golang
                       package) now defaults on honoring DH_GOLANG_EXCLUDES
                       variable for source installation in -dev packages and
                       not only during the building process. Please set
                       DH_GOLANG_EXCLUDES_ALL to false to revert to the
                       previous behaviour. See
                       Debian::Debhelper::Buildsystem::golang(3pm) for
                       details and examples.

               -       dh_installsystemduser is now included in the dh
                       standard sequence by default.

               -       The python-distutils buildsystem is now removed.
                       Please use the third-party build system pybuild
                       instead.

           v11 This mode is discouraged.

               The compat 11 is discouraged for new packages as it suffers
               from feature interaction between dh_installinit and
               dh_installsystemd causing services to not run correctly in
               some cases.  Please consider using compatibility mode 10 or 12
               instead.  More details about the issue are available in
               Debian#887904 and
               <https://lists.debian.org/debian-release/2019/04/msg01442.html>.

               Changes from v10 are:

               -       dh_installinit no longer installs service or tmpfile
                       files, nor generates maintainer scripts for those
                       files.  Please use the new dh_installsystemd helper.

               -       The dh_systemd_enable and dh_systemd_start helpers
                       have been replaced by the new dh_installsystemd
                       helper.  For the same reason, the systemd sequence for
                       dh has also been removed.  If you need to disable the
                       dh_installsystemd helper tool, please use an empty
                       override target.

                       Please note that the dh_installsystemd tool has a
                       slightly different behaviour in some cases (e.g. when
                       using the --name parameter).

               -       dh_installdirs no longer creates debian/package
                       directories unless explicitly requested (or it has to
                       create a subdirectory in it).

                       The vast majority of all packages will be unaffected
                       by this change.

               -       The makefile buildsystem now passes INSTALL="install
                       --strip-program=true" to make(1).  Derivative
                       buildsystems (e.g. configure or cmake) are unaffected
                       by this change.

               -       The autoconf buildsystem now passes --runstatedir=/run
                       to ./configure.

               -       The cmake buildsystem now passes
                       -DCMAKE_INSTALL_RUNSTATEDIR=/run to cmake(1).

               -       dh_installman will now prefer detecting the language
                       from the path name rather than the extension.

               -       dh_auto_install will now only create the destination
                       directory it needs.  Previously, it would create the
                       package build directory for all packages.  This will
                       not affect packages that only build with debhelper
                       commands, but it may expose bugs in commands not
                       included in debhelper.

               -       The helpers dh_installdocs, dh_installexamples,
                       dh_installinfo, and dh_installman now error out if
                       their config has a pattern that does not match
                       anything or reference a path that does not exist.

                       Known exceptions include building with the nodoc
                       profile, where the above tools will silently permit
                       failed matches where the patterns are used to specify
                       documentation.

               -       The helpers dh_installdocs, dh_installexamples,
                       dh_installinfo, and dh_installman now accept the
                       parameter --sourcedir with same meaning as dh_install.
                       Furthermore, they now also fall back to debian/tmp
                       like dh_install.

                       Migration note: A bug in debhelper 11 up to 11.1.5
                       made dh_installinfo incorrectly ignore --sourcedir.

               -       The perl-makemaker and perl-build build systems no
                       longer pass -I. to perl.  Packages that rely on this
                       behavior can often use the PERL5LIB environment
                       variable as a substitute.  E.g. by adding export
                       PERL5LIB=. in their debian/rules file (or similar).

               -       The PERL_USE_UNSAFE_INC environment variable is no
                       longer set by dh or any of the dh_auto_* tools.  It
                       was added as a temporary work around to avoid a lot of
                       packages failing to build at the same time.

                       Note this item will eventually become obsolete as
                       upstream intends to drop support for the
                       PERL_USE_UNSAFE_INC environment variable.  When perl
                       drops support for it, then this variable will be
                       removed retroactively from existing compat levels as
                       well.

               -       The dh_makeshlibs helper will now exit with an error
                       if objdump returns a non-zero exit from analysing a
                       given file.

               -       The dh_installdocs and dh_installexamples tools may
                       now install most of the documentation in a different
                       path to comply with the recommendation from Debian
                       policy §12.3 (since version 3.9.7).

                       Note that if a given source package only contains a
                       single binary package in debian/control or none of the
                       packages are -doc packages, then this change is not
                       relevant for that source package and you can skip to
                       the next change.

                       By default, these tools will now attempt to determine
                       a "main package for the documentation" (called a
                       doc-main-package from here on) for every -doc package.
                       If they find such a doc-main-package, they will now
                       install the documentation into the path
                       /usr/share/doc/doc-main-package in the given doc
                       package.  I.e. the path can change but the
                       documentation is still shipped in the -doc package.

                       The --doc-main-package option (or, since
                       debhelper/13.28, the X-Doc-Main-Package field) can be
                       used when the auto-detection is insufficient or to
                       reset the path to its previous value if there is a
                       reason to diverge from Debian policy recommendation.

                       Some documentation will not be affected by this
                       change.  These exceptions include the copyright file,
                       changelog files, README.Debian, etc.  These files will
                       still be installed in the path /usr/share/doc/package.

               -       The dh_strip and dh_shlibdeps tools no longer uses
                       filename patterns to determine which files to process.
                       Instead, they open the file and look for an ELF header
                       to determine if a given file is an shared object or an
                       ELF executable.

                       This change may cause the tools to process more files
                       than previously.

           v10 Changes from v9 are:

               -       dh_installinit will no longer installs a file named
                       debian/package as an init script.

               -       dh_installdocs will error out if it detects links
                       created with --link-doc between packages of
                       architecture "all" and non-"all" as it breaks binNMUs.

               -       dh_installdeb no longer installs a maintainer-provided
                       debian/package.shlibs file.  This is now done by
                       dh_makeshlibs instead.

               -       dh_installwm refuses to create a broken package if no
                       man page can be found (required to register for the
                       x-window-manager alternative).

               -       Debhelper will default to --parallel for all
                       buildsystems that support parallel building.  This can
                       be disabled by using either --no-parallel or passing
                       --max-parallel with a value of 1.

               -       The dh command will not accept any of the deprecated
                       "manual sequence control" parameters (--before,
                       --after, etc.).  Please use override targets instead.

                       Retroactively applied to earlier compat levels: dh no
                       longer accepts any of these since debhelper/12.4.

               -       The dh command will no longer use log files to track
                       which commands have been run.  The dh command still
                       keeps track of whether it already ran the "build"
                       sequence and skip it if it did.

                       The main effects of this are:

                       -   With this, it is now easier to debug the install
                           or/and binary sequences because they can now
                           trivially be re-run (without having to do a full
                           "clean and rebuild" cycle)

                       -   The main caveat is that dh_* now only keeps track
                           of what happened in a single override target.
                           When all the calls to a given dh_cmd command
                           happens in the same override target everything
                           will work as before.

                           Example of where it can go wrong:

                             override_dh_foo:
                               dh_foo -pmy-pkg

                             override_dh_bar:
                               dh_bar
                               dh_foo --remaining

                           In this case, the call to dh_foo --remaining will
                           also include my-pkg, since dh_foo -pmy-pkg was run
                           in a separate override target.  This issue is not
                           limited to --remaining, but also includes -a, -i,
                           etc.

               -       The dh_installdeb command now shell-escapes the lines
                       in the maintscript config file.  This was the original
                       intent but it did not work properly and packages have
                       begun to rely on the incomplete shell escaping (e.g.
                       quoting file names).

               -       The dh_installinit command now defaults to
                       --restart-after-upgrade.  For packages needing the
                       previous behaviour, please use
                       --no-restart-after-upgrade.

               -       The autoreconf sequence is now enabled by default.
                       Please pass --without autoreconf to dh if this is not
                       desirable for a given package

               -       The systemd sequence is now enabled by default.
                       Please pass --without systemd to dh if this is not
                       desirable for a given package.

               -       Retroactively removed: dh no longer creates the
                       package build directory when skipping running
                       debhelper commands. This will not affect packages that
                       only build with debhelper commands, but it may expose
                       bugs in commands not included in debhelper.

                       This compatibility feature had a bug since its
                       inception in debhelper/9.20130516 that made it fail to
                       apply in compat 9 and earlier.  As there has been no
                       reports of issues caused by this bug in those ~5
                       years, this item have been removed rather than fixed.

           v9  Changes from v8 are:

               -       Multiarch support. In particular, dh_auto_configure
                       passes multiarch directories to autoconf in --libdir
                       and --libexecdir.

               -       dh is aware of the usual dependencies between targets
                       in debian/rules.  So, "dh binary" will run any build,
                       build-arch, build-indep, install, etc targets that
                       exist in the rules file. There's no need to define an
                       explicit binary target with explicit dependencies on
                       the other targets.

               -       dh_strip compresses debugging symbol files to reduce
                       the installed size of -dbg packages.

               -       dh_auto_configure does not include the source package
                       name in --libexecdir when using autoconf.

               -       dh does not default to enabling --with=python-support

                       (Obsolete: As the dh_pysupport tool was removed from
                       Debian stretch.  Since debhelper/10.3, dh no longer
                       enables this sequence add-on regardless of compat
                       level)

               -       All of the dh_auto_* debhelper programs and dh set
                       environment variables listed by dpkg-buildflags,
                       unless they are already set.

               -       dh_auto_configure passes dpkg-buildflags CFLAGS,
                       CPPFLAGS, and LDFLAGS to perl Makefile.PL and Build.PL

               -       dh_strip puts separated debug symbols in a location
                       based on their build-id.

               -       Executable debhelper config files are run and their
                       output used as the configuration.

               This mode is deprecated.

           v8  Changes from v7 are:

               -       Commands will fail rather than warning when they are
                       passed unknown options.

               -       dh_makeshlibs will run dpkg-gensymbols on all shared
                       libraries that it generates shlibs files for. So -X
                       can be used to exclude libraries.  Also, libraries in
                       unusual locations that dpkg-gensymbols would not have
                       processed before will be passed to it, a behavior
                       change that can cause some packages to fail to build.

               -       dh requires the sequence to run be specified as the
                       first parameter, and any switches come after it. Ie,
                       use "dh $@ --foo", not "dh --foo $@".

               -       dh_auto_* prefer to use Perl's Module::Build in
                       preference to Makefile.PL.

               This mode is deprecated.

           v7  This mode is deprecated.

               This is the lowest supported compatibility level.

               If you are upgrading from an earlier compatibility level,
               please review debhelper-obsolete-compat(7).

## [](#SEE_ALSO)SEE ALSO

           debhelper-obsolete-compat(7)
               Upgrading from a (now) obsolete compatibility level? This
               document covers the upgrade checklist up to the earliest
               supported level.

           debhelper(7)
               General information about the debhelper framework. This
               document also covers how to declare your chosen debhelper
               compat level.

## [](#AUTHORS)AUTHORS

           Niels Thykier <niels@thykier.net>

           Joey Hess

## [](#COLOPHON)COLOPHON

           This page is part of the debhelper (helper programs for
           debian/rules) project.  Information about the project can be found
           at [unknown -- if you know, please contact man-pages@man7.org] If
           you have a bug report for this manual page, send it to
           submit@bugs.debian.org.  This page was obtained from the project's
           upstream Git repository
           ⟨https://salsa.debian.org/debian/debhelper.git⟩ on 2026-08-03.
           (At that time, the date of the most recent commit that was found
           in the repository was 2026-07-22.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    14.3                            2026-08-03                   debhelper(7)

------------------------------------------------------------------------

Pages that refer to this page: [debhelper(7)](../man7/debhelper.7.html)

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
